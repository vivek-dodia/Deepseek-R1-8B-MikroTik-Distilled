---
title: Watchdog
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/8978694/Watchdog,
crawled_date: 2025-02-02T21:15:19.326855
section: mikrotik_docs
type: documentation
---

* 1Summary
* 2Properties
* 3Quick Example
# Summary
Sub-menu:/system watchdog
```
/system watchdog
```
This menu allows the configuring system to reboot, when a specific IP address does not respond, or when it detects, that the software has locked up. The detection is done in two ways:
* Software watchdog timer (mostly caused by hardware malfunction) device can recover itself with a reboot;
* Ping watchdog can monitor connectivity to a specific IP address and trigger the reboot function.
# Properties
Property | Description
----------------------
auto-send-supout(yes | no; Default:no) | After the support output file is automatically generated, it can be sent by email.
automatic-supout(yes | no; Default:yes) | When software failure happens, a file named "autosupout.rif" is generated automatically. The previous "autosupout.rif" file is renamed to "autosupout.old.rif".
no-ping-delay(time; Default: 5m) | Specifies how long will it wait before trying to reach the watch-address.
ping-timeout(time; Default: 60s) | Specifies the time interval in which the device will be pinged 6 times (after "no-ping-delay").
send-email-from(string; Default: ) | The e-mail address to send the support output file from. If not set, the value set in /tool e-mail is used.
send-email-to(string; Default: ) | The e-mail address to send the support output file to.
send-smtp-server(string; Default: ) | SMTP server address to send the support output file through. If not set, the value set in /tool e-mail is used.
watch-address(IP; Default: ) | The system will reboot, in case 6 sequential pings to the given IP address will fail. If set to none this feature is disabled. By default, the router will reboot every 6 minutes if the watch-address is set and not reachable.
watchdog-timer(yes | no; Default:yes) | Whether to reboot if a system is unresponsive for a minute.
After the support output file is automatically generated, it can be sent by email.
When software failure happens, a file named "autosupout.rif" is generated automatically. The previous "autosupout.rif" file is renamed to "autosupout.old.rif".
Specifies how long will it wait before trying to reach the watch-address.
Specifies the time interval in which the device will be pinged 6 times (after "no-ping-delay").
The e-mail address to send the support output file from. If not set, the value set in /tool e-mail is used.
The e-mail address to send the support output file to.
SMTP server address to send the support output file through. If not set, the value set in /tool e-mail is used.
The system will reboot, in case 6 sequential pings to the given IP address will fail. If set to none this feature is disabled. By default, the router will reboot every 6 minutes if the watch-address is set and not reachable.
Whether to reboot if a system is unresponsive for a minute.
# Quick Example
To make system generate a support output file and sent it automatically to support@example.com through the 192.0.2.1in case of a software crash:
```
[admin@MikroTik] system/watchdog/ set auto-send-supout=yes \
\... send-to-email=support@example.com send-smtp-server=192.0.2.1
[admin@MikroTik] system watchdog> print
      watch-address: none
     watchdog-timer: yes
      no-ping-delay: 5m
   automatic-supout: yes
   auto-send-supout: yes
   send-smtp-server: 192.0.2.1
      send-email-to: support@example.com
```