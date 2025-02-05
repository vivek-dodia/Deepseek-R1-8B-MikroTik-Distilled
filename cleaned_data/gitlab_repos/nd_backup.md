# Repository Information
Name: nd_backup

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
	url = https://gitlab.com/g_prjcts/nd_backup.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: device_backup.py
================================================
#!/bin/python3
from main.ssh import ssh
from main.telnet import telnet
from main.log import log
from main.config import radctl, mik_acc, bc
from main.templates import bkp
from multiprocessing import Pool
import time, re, tqdm, pandas
def xls_parse(file):
    try:
        data = pandas.read_excel(file).to_numpy().tolist()
    except FileNotFoundError:
        print(f'{bc.RED}[!]{bc.ENDC} Inventory file({file}) not found')
        return False
    except PermissionError:
        print(f'{bc.RED}[!]{bc.ENDC} Inventory file({file}) permission error')
    else:
        return data
def backup(device):
    date = time.strftime('%d-%b-%Y')
    name, city, vend, ip  = device
    if vend == 'huawei':
        cmd = bkp(vend, date, name, city)
        result = telnet.opt1(cmd.huawei, ip, radctl.username, radctl.password)
        if result != False:
            if not re.findall('TFTP: Uploading the file successfully.', result):
                return (f'{ip}|{name}({city}) - Backup error!')
        else:
            return (f'{ip}|{name}({city}) - Telnet Error!')
    elif vend == 'mikrotik':
        cmd = bkp(vend, date, name, city)
        s = ssh.init(ip, mik_acc.username_m, mik_acc.password_m, 2)
        if s != False:
            result = ssh.exec(cmd.mikrotik, s)
            if not re.findall('status: finished', result):
                return (f'{ip}|{name}({city}) - Backup error!')
            ssh.close(s)
        else:
            return (f'{ip}|{name}({city}) - SSH Error!')
    elif vend == 'tp_link':
        cmd = bkp(vend, date, name, city)
        result = telnet.opt1(cmd.tp_link, ip, radctl.username, radctl.password)
        if result != False:
            if not re.findall('Backup user config file OK.', result):
                return (f'{ip}|{name}({city}) - Backup error!')
        else:
            return (f'{ip}|{name}({city}) - Telnet Error!')
    else:
        return (f'{ip}|{name}({city}) Incorrect device vendor type({vend})')
def main():
    devices = xls_parse('inventory.xlsx')
    pool = Pool(processes=32)
    print(f'\n{"="*5}{bc.GREEN} Total devices to backup: {len(devices)} {bc.ENDC}{"="*5}\n')
    results = []
    for result in tqdm.tqdm(pool.imap_unordered(backup, devices), total=len(devices)):
        results.append(result)
    err_list = list(filter(bool,(results)))
    if len(err_list) != 0:
        msg = "\n".join(err_list)
        log.write(msg)
        print(f'\n{"="*5}{bc.RED} There are some errors, see log file for details {bc.ENDC}{"="*5}\n')
    else:
        print(f'\n{"="*5}{bc.CYAN} All done with no errors! {bc.ENDC}{"="*5}\n')
if __name__ == "__main__":
    main()
================================================

File: config.py
================================================
#!/bin/python3
class bc:
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLINK = '\33[5m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class log_var:
    path = 'log/' #Path to local log file
class radctl: #all values must be encoded in base64
    username = 'dGVzdA=='
    password = 'dGVzdA=='
class mik_acc: #all values must be encoded in base64
    username_m = 'dGVzdA=='
    password_m = 'dGVzdA=='
class ftp:
    usr = 'test' # User for FTP
    psw = 'test' # Password for FTP
    ip = '192.168.1.1' #TFTP & FTP Server address
    path_1 = 'Backup/TEST_BKP/' #Path to backup Huawei config files
    path_2 = 'Backup/TEST_BKP/' #Path to backup MikroTik config files
    path_3 = 'Backup/TEST_BKP/' #Path to backup TP-Link config files
================================================

File: log.py
================================================
#!/bin/python3
from main.config import log_var, bc
import os, getpass, time, re
class log:
    usr = os.getlogin()
    usr_eff = getpass.getuser()
    def write(result):
        try:
            wr_date = time.strftime('%Y-%b')
            log_date = time.strftime('%d-%b-%Y %H:%M:%S')
            file = open(f'{log_var.path}{wr_date}.log', 'a')
            file.write(f'{log.usr_eff}({log.usr})|{log_date}|{"="*50}\n')
            if result:
                for each in result.split('\n'):
                    file.write(f'{log.usr_eff}({log.usr})|{log_date}| {each}\n')
            else:
                file.write(f'{log.usr_eff}({log.usr})|{log_date}| {result}\n')
            file.close()
        except PermissionError:
            print(f'{bc.RED}[!]{bc.ENDC} Log file permission error on open')
================================================

File: ssh.py
================================================
#!/bin/python3
from main.config import bc
import time, base64, paramiko, socket
class ssh:
    timeout = 30
    def init(host, username, password, mode):
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            session.connect(hostname=host, username=base64.b64decode(username).decode("ascii"), password=base64.b64decode(password).decode("ascii"), timeout=ssh.timeout, banner_timeout=ssh.timeout, auth_timeout=ssh.timeout)
        except socket.timeout:
            #print(f'{bc.RED}[!]{bc.ENDC} Host: {host} is unreachable, timed out')
            return False
        except paramiko.AuthenticationException:
            #print(f'{bc.RED}[!]{bc.ENDC} Invalid credentials for {username} | {password}')
            return False
        except paramiko.ssh_exception.NoValidConnectionsError:
            #print(f'{bc.RED}[!]{bc.ENDC} Connection refused by {host}')
            return False
        except paramiko.ssh_exception.SSHException:
            # socket is open, but not SSH service responded
            #print(f'{bc.RED}[!]{bc.ENDC} Error reading SSH protocol banner on {host}')
            return False
        else:
            #print(f'{bc.GREEN}[+]{bc.ENDC} Connection was established successfully to {host}')
            if mode == 1:
                session = session.invoke_shell(width=250, height=25000)
                return session
            elif mode == 2:
                return session
            else:
                #print(f'{bc.RED}[!]{bc.ENDC} Incorrect SSH mode')
                return False
    def exec(cmd, session):
        stdin, stdout, stderr = session.exec_command(cmd, timeout=ssh.timeout)
        time.sleep(2)
        out = stdout.read().decode("ascii")
        return out
    def invoke(cmd, session):
        session.send(cmd+'\n')
        time.sleep(2)
        out = session.recv(999999).decode("ascii")
        return out
    def close(session):
        #print(f'{bc.RED}[!]{bc.ENDC} Disconnected')
        session.close()
        return True
================================================

File: telnet.py
================================================
#!/bin/python3
from main.config import bc
import base64, time, telnetlib
class telnet:
    def opt1(cmd, host, username, password): # For Huawei & TP-Link devices
        try:
            username = base64.b64decode(username).decode("ascii") + "\r"
            password = base64.b64decode(password).decode("ascii") + "\r"
            tn = telnetlib.Telnet(host, port = 23, timeout = 5)
            #print(f'{bc.GREEN}[+]{bc.ENDC} Connecting to {host}...')
            tn.read_until(b'User')
            tn.write(username.encode("ascii"))
            time.sleep(1)
            tn.read_until(b'Password')
            tn.write(password.encode("ascii"))
            time.sleep(1)
            tn.read_until(b'>')
            #print(f'{bc.GREEN}[+]{bc.ENDC} Connection was established successfully to {host}')
            tn.write(cmd.encode("ascii"))
            time.sleep(11)
            out = tn.read_very_eager().decode("ascii")
            tn.close()
            #print(f'{bc.RED}[!]{bc.ENDC} Disconnected from {host}')
            return out
        except:
            #print(f'{bc.RED}[!]{bc.ENDC} Unknown Telnet Error on {host}')
            return False
================================================

File: templates.py
================================================
#!/bin/python3
from main.config import ftp
class bkp():
    def __init__(self, vend, *args):
        if vend == 'huawei':
            date, name, city = args
            self.huawei = f'save\ry\rsave config.cfg\ry\rtftp {ftp.ip} vpn-instance MGMT put flash:/config.cfg {ftp.path_1}{date}_{name}({city}).cfg\r'
        if vend == 'mikrotik':
            date, name, city = args
            self.mikrotik = f'/export file=exportfile_{date}_{name}.rsc;\n:delay 5;\n/tool fetch address={ftp.ip} src-path=exportfile_{date}_{name}.rsc mode=ftp upload=yes user={ftp.usr} pass={ftp.psw} dst-path="{ftp.path_2}{date}_{name}({city}).rsc";\n:delay 2;\n'
        if vend == 'tp_link':
            date, name, city = args
            self.tp_link = f'enable\rcopy running-config startup-config\rcopy startup-config tftp ip-address {ftp.ip} filename {ftp.path_3}{date}_{name}({city}).cfg\r'
================================================

File: README.md
================================================
# Network Device Backup Tool
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Usage](#setup)
## General info
This project was created to automate the daily routine tasks for NOC engineer.
## Technologies
Project is created with:
* pandas 1.3.4
* openpyxl 3.0.9
* paramiko 2.10.3
* multiprocess 0.70.12.2
* tqdm 4.62.3
## Usage
To run this project, git clone it locally.
Change variables in main/config.py.
Install required packages via PIP ```pip3 install -r requirements.txt```
Customize your ```inventory.xlsx``` and run ```python3 device_backup.py```
================================================

File: requirements.txt
================================================
pandas==1.3.4
openpyxl==3.0.9
paramiko==2.10.3
multiprocess==0.70.12.2
tqdm==4.62.3