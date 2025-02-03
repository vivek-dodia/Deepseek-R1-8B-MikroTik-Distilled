---
title: Scheduler
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/40992881/Scheduler,
crawled_date: 2025-02-02T21:12:52.771072
section: mikrotik_docs
type: documentation
---

## Summary
The scheduler can trigger script execution at a particular time moment, after a specified time interval, or both.
## Properties
* interval(time; default: 0s)- interval between two script executions, if time interval is set to zero, the script is only executed at its start time, otherwise it is executed repeatedly at the time interval is specified
* namename)- name of the task
* on-event(name)- name of the script to execute. It must be presented at /system script
* run-count(read-only: integer)- to monitor script usage, this counter is incremented each time the script is executed
* start-date(date)- date of the first script execution
* start-time(time)- time of the first script execution
* startup- execute the script 3 seconds after the system startup.
## Notes
Rebooting the router will reset the run-count counter.
If more than one script has to be executed simultaneously, they are executed in the order they appear in the scheduler configuration. This can be important if one scheduled script is used to disable another one.
If a more complex execution pattern is needed, it can usually be done by scheduling several scripts, and making them enable and disable each other.
Note:if scheduler item has start-time set to startup, it behaves as if start-time and start-date were set to time 3 seconds after console starts up. It means that all scripts havingstart-time is startupandinterval is 0will be executed once each time router boots. If the interval is set to value other than 0 scheduler willnotrun at startup
```
start-time is startup
```
```
interval is 0
```
## Examples
We will add a task that executes the script log-test every hour:
```
[admin@MikroTik] system script> add name=log-test source=":log info message=test" 
[admin@MikroTik] system script> print 
Flags: I - invalid 
0 name="log-test" owner="admin" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon dont-require-permissions=no run-count=0 
source=:log info message=test 
[admin@MikroTik] system script> .. scheduler 
[admin@MikroTik] system scheduler> add name=run-1h interval=1h 
on-event=log-test 
[admin@MikroTik] system scheduler> print 
Flags: X - disabled 
# NAME ON-EVENT START-DATE START-TIME INTERVAL RUN-COUNT 
0 run-1h log-test mar/30/2004 06:11:35 1h 0 
[admin@MikroTik] system scheduler>
```
In another example, there will be two scripts added that will change the bandwidth setting of a queue rule "Cust0". Every day at 9AM the queue will be set to 64Kb/s and at 5PM the queue will be set to 128Kb/s. The queue rule, the scripts, and the scheduler tasks are below:
```
[admin@MikroTik] queue simple> add name=Cust0 interface=ether1 \ 
\... dst-address=192.168.0.0/24 limit-at=64000
 [admin@MikroTik] queue simple> print
 Flags: X - disabled, I - invalid 0 name="Cust0" target-address=0.0.0.0/0 dst-address=192.168.0.0/24
 interface=ether1 limit-at=64000 queue=default priority=8 bounded=yes 
[admin@MikroTik] queue simple> /system script 
[admin@MikroTik] system script> add name=start_limit source={/queue simple set \
 \... Cust0 limit-at=64000} 
[admin@MikroTik] system script> add name=stop_limit source={/queue simple set \ 
\... Cust0 limit-at=128000} 
[admin@MikroTik] system script> print 
0 name="start_limit" source="/queue simple set Cust0 limit-at=64000" 
owner=admin run-count=0 
1 name="stop_limit" source="/queue simple set Cust0 limit-at=128000" 
owner=admin run-count=0 
[admin@MikroTik] system script> .. scheduler 
[admin@MikroTik] system scheduler> add interval=24h name="set-64k" \ 
\... start-time=9:00:00 on-event=start_limit 
[admin@MikroTik] system scheduler> add interval=24h name="set-128k" \
 \... start-time=17:00:00 on-event=stop_limit 
[admin@MikroTik] system scheduler> print
 Flags: X - disabled 
# NAME ON-EVENT START-DATE START-TIME INTERVAL RUN-COUNT
 0 set-64k start... oct/30/2008 09:00:00 1d 0 
1 set-128k stop_... oct/30/2008 17:00:00 1d 0 
[admin@MikroTik] system scheduler>
```
The following example schedules a script that sends each week a backup of router configuration by e-mail.
```
[admin@MikroTik] system script> add name=e-backup source={/system backup 
{... save name=email; /tool e-mail send to="root@host.com" subject=([/system 
{... identity get name] . " Backup") file=email.backup} 
[admin@MikroTik] system script> print 
0 name="e-backup" source="/system backup save name=ema... owner=admin run-count=0 
[admin@MikroTik] system script> .. scheduler 
[admin@MikroTik] system scheduler> add interval=7d name="email-backup" \
 \... on-event=e-backup 
[admin@MikroTik] system scheduler> print
 Flags: X - disabled
 # NAME ON-EVENT START-DATE START-TIME INTERVAL RUN-COUNT 
0 email-... e-backup oct/30/2008 15:19:28 7d 1 
[admin@MikroTik] system scheduler>
```
Do not forget to set the e-mail settings, i.e., the SMTP server and From: address under /tool e-mail. For example:
```
[admin@MikroTik] tool e-mail> set server=159.148.147.198 from=SysAdmin@host.com 
[admin@MikroTik] tool e-mail> print
 server: 159.148.147.198 
from: SysAdmin@host.com 
[admin@MikroTik] tool e-mail>
```
Example below will put 'x' in logs each hour from midnight till noon:
```
[admin@MikroTik] system script> add name=enable-x source={/system scheduler 
{... enable x} 
[admin@MikroTik] system script> add name=disable-x source={/system scheduler 
{... disable x} 
[admin@MikroTik] system script> add name=log-x source={:log info message=x} 
[admin@MikroTik] system script> .. scheduler 
[admin@MikroTik] system scheduler> add name=x-up start-time=00:00:00 \ 
\... interval=24h on-event=enable-x 
[admin@MikroTik] system scheduler> add name=x-down start-time=12:00:00
 \... interval=24h on-event=disable-x 
[admin@MikroTik] system scheduler> add name=x start-time=00:00:00 interval=1h \ 
\... on-event=log-x 
[admin@MikroTik] system scheduler> print 
Flags: X - disabled
 # NAME ON-EVENT START-DATE START-TIME INTERVAL RUN-COUNT 
0 x-up enable-x oct/30/2008 00:00:00 1d 0 
1 x-down disab... oct/30/2008 12:00:00 1d 0 
2 x log-x oct/30/2008 00:00:00 1h 0 
[admin@MikroTik] system scheduler>
```