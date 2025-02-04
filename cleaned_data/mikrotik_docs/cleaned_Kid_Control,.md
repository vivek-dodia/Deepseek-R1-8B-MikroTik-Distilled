# Document Information
Title: Kid Control
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/129531911/Kid+Control,

# Content
# Summary
Sub-menu:/ip kid-control
```
/ip kid-control
```
"Kid control" is a parental control feature to limit internet connectivity for LAN devices.
# Property Description
In this menu, it is possible to create a profile for each Kid and restrict internet accessibility.
Property | Description
----------------------
name(string) | Name of the Kid's profile
mon,tue,wed,thu,fri,sat,sun(time) | Each day of the week. Time of day, when internet access should be allowed
disabled(yes | no) | Whether restrictions are enabled
rate-limit(string) | The maximum available data rate for flow
tur-mon,tur-tue,tur-wed,tur-thu,tur-fri,tur-sat,tur-sun(time) | Time unlimited rate. Time of day, when internet access should be unlimited
Time unlimited rate parameters have higher priority than rate-limit parameter.
# Devices
Sub-menu:/ip kid-control device
```
/ip kid-control device
```
This sub-menu contains information if there are multiple connected devices to the internet (phone, tablet, gaming console, tv etc.). The device is identified by the MAC address that is retrieved from the ARP table. The appropriate IP address is taken from there.
Property | Description
----------------------
name(string) | Name of the device
mac-address(string) | Devices mac-address
user(string) | To which profile append the device
reset-counters([id, name]) | Reset bytes-up and bytes-down counters.
# Application example
With the following example we will restrict access for Peter's mobile phone:
```
[admin@MikroTik] > /ip kid-control add name=Peter mon="" tur-tue="00:00-24h" wed="" tur-thu="11:00-22:00" fri="" sat="18:30-22:00" tur-sun="15h-21h" rate-limit=3M
[admin@MikroTik] > /ip kid-control device add name=Mobile-phone user=Peter mac-address=FF:FF:FF:ED:83:63
```
Internet access limitation is implemented by adding dynamic firewall filter rules or simple queue rules. Here are example firewall filter rules:
```
[admin@MikroTik] > /ip firewall filter print
1  D ;;; Mobile-phone, kid-control
chain=forward action=reject src-address=192.168.88.254
2  D ;;; Mobile-phone, kid-control
chain=forward action=reject dst-address=192.168.88.254
```
Dynamically created simple queue:
```
[admin@MikroTik] > /queue simple print
Flags: X - disabled, I - invalid, D - dynamic
1  D ;;; Mobile-phone, kid-control
name="queue1" target=192.168.88.254/32 parent=none packet-marks="" priority=8/8 queue=default-small/default-small limit-at=3M/3M max-limit=3M/3M burst-limit=0/0
burst-threshold=0/0 burst-time=0s/0s bucket-size=0.1/0.1
```
It is possible to monitor how much data is used by the specific device:
```
[admin@MikroTik] > /ip kid-control device print stats
Flags: X - disabled, D - dynamic, B - blocked, L - limited, I - inactive
# NAME                                                                                                                 IDLE-TIME    RATE-DOWN   RATE-UP   BYTES-DOWN     BYTES-UP
1 BI Mobile-phone                                                                                                               30s         0bps      0bps    3438.1KiB       8.9KiB
```
It is also possible topauseInternet access for the created kids, it will restrict all access untilresumeis used, which will continue with configured settings:
```
[admin@MikroTik] > /ip kid-control pause Peter
[admin@MikroTik] > /ip kid-control print
Flags: X - disabled, P - paused, B - blocked, L - rate-limited
# NAME                                                                                                                    SUN      MON      TUE      WED      THU      FRI      SAT
0 PB Peter                                                                                                                 15h-21h                             11h-22h          18:30h-22h
```