# Repository Information
Name: mikrotik_stats

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/tuxpowered/mikrotik_stats.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: dump_stats.rsc
================================================
:local date [/system/clock/get date]
:local time [/system/clock/get time]
:local ifaceStats [/interface/print stats as-value]
/file/add name="stats/iface_$date_$time" contents=$ifaceStats
:local lteStats [/interface/lte/monitor lte1 once as-value]
/file/add name="stats/lte_$date_$time" contents=$lteStats
================================================

File: fetch_stats.py
================================================
#!/usr/bin/python3
from collections import defaultdict
import os
import paramiko
import re
import requests
import tempfile
from datetime import datetime, timedelta
MT_IPADDRESS = 'xxx'
MT_HOSTNAME = 'xxx'
MT_USERNAME = 'grafana'
SSH_KEYFILE = '/var/lib/grafana-agent/.ssh/grafana-mikrotik'
GRAPHITE_URL = 'xxx'
GRAPHITE_USER = 'xxx'
GRAPHITE_PASS = 'xxx'
LTE_METRICS = [
    'band',
    'bandwidth',
    'current-cellid',
    'earfcn',
    'enb-id',
    'lac',
    'phy-cellid',
    'sector-id',
    'session-uptime',
    'sinr',
    'rsrp',
    'rsrq',
]
def connect_sftp():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=MT_IPADDRESS,
        username=MT_USERNAME,
        key_filename=SSH_KEYFILE,
    )
    return ssh.open_sftp()
def get_stats(sftp, td):
    files = sftp.listdir('stats')
    for file in files:
        local_path = f'{td}/{file}'
        sftp.get(f'stats/{file}', local_path)
        if os.stat(local_path).st_size > 0:
            if parse_stats_file(local_path):
                sftp.remove(f'stats/{file}')
def parse_stats_file(path):
    r = re.match(r'([a-z]+)_([0-9-]+_[0-9:]+)', os.path.basename(path))
    stat_name = r.group(1)
    time_stamp = int(datetime.strptime(r.group(2), '%Y-%m-%d_%H:%M:%S').timestamp())
    all_sent = True
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            while True:
                r_start = re.match(r'\.id=\*?([0-9]+);', line)
                if r_start is None:
                    break
                object_id = r_start.group(1)
                line = line[r_start.end():]
                r_end = re.search(r'\.id=\*?[0-9]+;', line)
                if r_end is None:
                    # Fake object id for cases when there's no object id.
                    object_string = line + f';id={object_id}'
                else:
                    # Fake object id for cases when there's no object id.
                    object_string = line[:r_end.start()-1] + f';id={object_id}'
                    line = line[r_end.start():]
                # Some metrics, like LTE SCCs, have multiple values per one key.
                # We store all metrics as arrays, even if they have just one value.
                metrics_dict = defaultdict(lambda: [])
                var = None
                for metric in object_string.split(';'):
                    if '=' in metric:
                        var, val = metric.split('=')
                    else:
                        val = metric  # repeated key
                    metrics_dict[var].append(val)
                all_sent &= parse_metrics(time_stamp, stat_name, metrics_dict)
    return all_sent
def parse_metrics(time_stamp, stat_name, metrics_raw):
    metrics_parsed = {}  # some metrics are split, we need a new dict
    for var, vals in metrics_raw.items():
        if var == 'session-uptime':
            # The date elements are optional apparently
            # session-uptime=3d00:50:25
            r = re.match(r'([0-9]+)d([0-9]+):([0-9]+):([0-9]+)', vals[0])
            if r is None:
                continue
            td = timedelta(
                days=int(r.group(1)) if r.group(1) else 0,
                hours=int(r.group(2)) if r.group(2) else 0,
                minutes=int(r.group(3)) if r.group(3) else 0,
                seconds=int(r.group(4)) if r.group(4) else 0,
            )
            metrics_parsed['session-uptime'] = td.total_seconds()
        elif var == 'earfcn':
            r = re.match(r'([0-9]+) \(band ([0-9]+), bandwidth ([0-9]+)([a-zA-Z]+)', vals[0])
            metrics_parsed['earfcn'] = int(r.group(1))
            metrics_parsed['band'] = int(r.group(2))
            if r.group(4).lower() == 'mhz':
                freq_unit = 1000000
            elif r.group(4).lower() == 'khz':
                freq_unit = 1000
            else:
                raise Exception('Can\t determine frequency unit!')
            metrics_parsed['bandwidth'] = int(r.group(3)) * freq_unit
        elif var in ['primary-band', 'ca-band']:
            if var == 'primary-band':
                i = 0
            else:
                i = 1
            for val in vals:
                #  B1@20Mhz earfcn: 500 phy-cellid: 67
                r = re.match(r'B([0-9]+)@([0-9]+)([a-zA-Z]+) earfcn: ([0-9]+) phy-cellid: ([0-9]+)', val)
                metrics_parsed[f'{i}.cell'] = int(r.group(5))
                metrics_parsed[f'{i}.earfcn'] = int(r.group(4))
                metrics_parsed[f'{i}.band'] = int(r.group(1))
                if r.group(3).lower() == 'mhz':
                    freq_unit = 1000000
                elif r.group(3).lower() == 'mhz':
                    freq_unit = 1000
                metrics_parsed[f'{i}.bandwidth'] = int(r.group(2)) * freq_unit
                i += 1
        else:
            try:
                metrics_parsed[var] = float(vals[0])
            except ValueError:
                pass
    obj_name = metrics_raw.get('name')
    if obj_name is None:
        obj_name = metrics_raw['id'][0]
    else:
        obj_name = obj_name[0]
    all_sent = True
    all_sent &= send_to_carbon(stat_name, obj_name, metrics_parsed, time_stamp)
    return all_sent
def send_to_carbon(stat_name, obj_name, metrics_parsed, time_stamp):
    metrics_carbon = []
    for var, val in metrics_parsed.items():
        metrics_carbon.append({
            'name': f'{MT_HOSTNAME}.{stat_name}.{obj_name}.{var}',
            'value': val,
            'interval': 60,
            'time': time_stamp,
        })
    print(metrics_parsed)
    print(metrics_carbon)
    req = requests.post(
        GRAPHITE_URL,
        headers={
            'Authorization': f'Bearer {GRAPHITE_USER}:{GRAPHITE_PASS}',
        },
        json=metrics_carbon,
    )
    print(time_stamp, metrics_carbon, req.status_code)
    if req.status_code == 200:
        return True
    return False
def main():
    sftp = connect_sftp()
    with tempfile.TemporaryDirectory() as td:
        get_stats(sftp, td)
if __name__ == '__main__':
    main()
================================================

File: README.md
================================================
# Goal
This tool provides reliable way of getting interface counters and LTE information
from a Mikrotik device which might be ocassionally disconnected from the network.
The script running on a Mikrotik device will collect needed metrics and store them
in files for later retrival.
# Limitations
Metrics are stored in a ram disk, so the tool is not reliable enough to collect
information properly in case of power failures.
There's no locking to prevent files being read as they are written.
Maybe adding a little delay to collector's cron job would be enough.
# Installation on Mikrotik
Create storage space for the stats dumps:
```
/disk
add slot=stats tmpfs-max-size=32000000 type=tmpfs
```
Schedule the script to run every minute.
It needs quite broad permissions
```
/system scheduler
add interval=1m name=dump_stats on-event=dump_stats policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
```
# Installation on collector
Provide Mikrotik's IP address, ssh and graphite credentuials.
Edit the script to update the constants at the top of the file. 
Use a systemd timer or a cron job to run the script every minute.