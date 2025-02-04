# Document Information
Title: Log
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328094/Log,

# Content
# 2Summary3Log messages4Logging configuration4.1Actions4.2Topics4.2.1List of Facility independent topics4.2.2Topics used by various RouterOS facilities5Examples5.1Logging to file
# Summary
RouterOS is capable of logging various system events and status information. Logs can be saved in routers memory (RAM), disk, file, sent by email or even sent to remote syslog server (RFC 3164).
From MikroTik RouterOS 7.18 support for CEF (Commont Event Format) logging format is added, as well as timestamp support for milliseconds.
Video: Logging Basics
# Log messages
Sub-menu level:/log
-------------------
Sub-menu level:/log
```
/log
```
All messages stored in routers local memory can be printed from/logmenu. Each entry contains time and date when event occurred, topics that this message belongs to and message itself.
```
/log
```
```
[admin@MikroTik] /log> print
jan/02/1970 02:00:09 system,info router rebooted
sep/15 09:54:33 system,info,account user admin logged in from 10.1.101.212 via winbox
sep/15 12:33:18 system,info item added by admin
sep/15 12:34:26 system,info mangle rule added by admin
sep/15 12:34:29 system,info mangle rule moved by admin
sep/15 12:35:34 system,info mangle rule changed by admin
sep/15 12:42:14 system,info,account user admin logged in from 10.1.101.212 via telnet
sep/15 12:42:55 system,info,account user admin logged out from 10.1.101.212 via telnet
01:01:58 firewall,info input: in:ether1 out:(none), src-mac 00:21:29:6d:82:07, proto UDP,
10.1.101.1:520->10.1.101.255:520, len 452
```
If logs are printed at the same date when log entry was added, then only time will be shown. In example above you can see that second message was added on sep/15 current year (year is not added) and the last message was added today so only the time is displayed.
Printcommand accepts several parameters that allows to detect new log entries, print only necessary messages and so on.
For example following command will print all log messages where one of the topics is info and will detect new log entries until Ctrl+C is pressed.
```
[admin@MikroTik] /log > print follow where topics~".info"
12:52:24 script,info hello from script
-- Ctrl-C to quit.
```
In this example it will print only the dhcp info messages:
```
[admin@MikroTik] log/print where topics~"dhcp.info"
11:42:32 dhcp,info defconf deassigned 192.168.88.37 for B0:E4:5C:27:EF:F2 Samsung
11:42:32 dhcp,info defconf assigned 192.168.88.37 for B0:E4:5C:27:EF:F2 Samsung
```
If print is in follow mode you can hit 'space' on keyboard to insert separator:
```
[admin@MikroTik] /log > print follow where topics~".info"
12:52:24 script,info hello from script
= = = = = = = = = = = = = = = = = = = = = = = = = = =
-- Ctrl-C to quit.
```
# Logging configuration
Sub-menu level:/system logging
------------------------------
Sub-menu level:/system logging
```
/system logging
```
Property | Description
----------------------
action(name; Default:memory) | specifies one of the system default actions or user specified action listed in actions menu
prefix(string; Default: ) | prefix added at the beginning of log messages
regex(string; Default: ) | regex which will be used in order to match or not match message. If the regex is not matched, then even if topic is configured to be logged, but log message does not match regex, action will not be performed.
topics(account, async, backup, bfd, bgp, bridge, calc, caps, certificate, container, clock, critical, ddns, debug, dhcp, dns, dot1x, dude, e-mail, error, event, fetch, firewall, gps, gsm, health, hotspot, igmp-proxy, info, interface, ipsec, iscsi, isdn, isis, kvm, l2tp, ldp, lora, lte, manager, mme, mpls, mqtt, mvrp, natpmp, netinstall, netwatch, ntp, ospf, ovpn, packet, pim, poe-out, ppp, pppoe, pptp, queue, radius, radvd, raw, read, rip, route, rpki, rsvp, script, sertcp, simulator, smb, snmp, ssh, sstp, state, store, stp, system, telephony, tftp, timer, tr069, update, upnp, ups, vpls, vrrp, warning, watchdog, web-proxy, wireguard, wireless, write; Default:info) | log all messages that falls into specified topic or list of topics.'!'character can be used before topic to exclude messages falling under this topic. For example, we want to log NTP debug info without too much details:/system logging add topics=ntp,debug,!packet
'!'character can be used before topic to exclude messages falling under this topic. For example, we want to log NTP debug info without too much details:
```
/system logging add topics=ntp,debug,!packet
```
# Actions
Sub-menu level:/system logging action
-------------------------------------
Sub-menu level:/system logging action
```
/system logging action
```
Property | Description
----------------------
cef-event-delimiter(string; Default:\r\n) | option helps remote syslog to distinguish between individual events within sent batch
disk-file-count(integer [1..65535]; Default:2) | specifies number of files used to store log messages, applicable only if action=disk
disk-file-name(string; Default:log) | name of the file used to store log messages, applicable only if action=disk
disk-lines-per-file(integer [1..65535]; Default:100) | specifies maximum size of file in lines, applicable only if action=disk
disk-stop-on-full(yes|no; Default:no) | whether to stop to save log messages to disk after the specified disk-lines-per-file and disk-file-count number is reached, applicable only if action=disk
email-start-tls(yes | no; Default:no) | Whether to use tls when sending email, applicable only if action=email
email-to(string; Default: ) | email address where logs are sent, applicable only if action=email
memory-lines(integer [1..65535]; Default:1000) | number of records in local memory buffer, applicable only if action=memory
memory-stop-on-full(yes|no; Default:no) | whether to stop to save log messages in local buffer after the specified memory-lines number is reached
name(string; Default: ) | name of an action
remember(yes|no; Default: ) | whether to keep log messages, which have not yet been displayed in console, applicable if action=echo
remote-log-format(cef, default, syslog; Default:default) | Format for logs to be sent to remote instance:cef - logs are sent in CEF format;default - logs are sent as it is;syslog - logs are sent in BSD-syslog format
remote-port(IP/IPv6 Address[:Port]; Default:0.0.0.0:514) | remote logging server's IP/IPv6 address and UDP port, applicable if action=remote
remote-protocol(tcp / udp; Default:udp) | protocol for remote logging messages
src-address(IP address; Default:0.0.0.0) | source address used when sending packets to remote server
syslog-facility(auth, authpriv, cron, daemon, ftp, kern, local0, local1, local2, local3, local4, local5, local6, local7, lpr, mail, news, ntp, syslog, user, uucp; Default:daemon) |
syslog-severity(alert, auto, critical, debug, emergency, error, info, notice, warning; Default:auto) | Severity level indicator defined in RFC 3164:Emergency: system is unusableAlert: action must be taken immediatelyCritical: critical conditionsError: error conditionsWarning: warning conditionsNotice: normal but significant conditionInformational: informational messagesDebug: debug-level messages
syslog-time-format(bsd-syslog, iso8601; Default:bsd-syslog) | Timelog format for messages
target(disk, echo, email, memory, remote; Default:memory) | storage facility or target of log messagesdisk - logs are saved to the hard driveecho - logs are displayed on the console screenemail - logs are sent by emailmemory - logs are stored in local memory bufferremote - logs are sent to remote host
Format for logs to be sent to remote instance:
# Topics
Each log entry have topic which describes the origin of log message. There can be more than one topic assigned to log message. For example, OSPF debug logs have four different topics: route, ospf, debug and raw.
```
11:11:43 route,ospf,debug SEND: Hello Packet 10.255.255.1 -> 224.0.0.5 on lo0
11:11:43 route,ospf,debug,raw PACKET:
11:11:43 route,ospf,debug,raw 02 01 00 2C 0A FF FF 03 00 00 00 00 E7 9B 00 00
11:11:43 route,ospf,debug,raw 00 00 00 00 00 00 00 00 FF FF FF FF 00 0A 02 01
11:11:43 route,ospf,debug,raw 00 00 00 28 0A FF FF 01 00 00 00 00
```
# List of Facility independent topics
Topic | Description
-------------------
critical | Log entries marked as critical, these log entries are printed to console each time you log in.
debug | Debug log entries
error | Error messages
info | Informative log entry
packet | Log entry that shows contents from received/sent packet
raw | Log entry that shows raw contents of received/sent packet
warning | Warning message.
# Topics used by various RouterOS facilities
Topic | Description
-------------------
account | Log messages generated by accounting facility.
async | Log messages generated by asynchronous devices
backup | Log messages generated by backup creation facility.
bfd | Log messages generated by BFD protocol
bgp | Log messages generated by BGP protocol
calc | Routing calculation log messages.
caps | CAPsMAN wireless device management
certificate | Security certificate
clock | Log messages generated by Clock, IP Cloud time changes.
dns | Name server lookup related information
ddns | Log messages generated by Dynamic DNS tool
dude | Messages related to the Dude server package The Dude tool
dhcp | DHCP client, server and relay log messages
e-mail | Messages generated by e-mail tool.
event | Log message generated at routing event. For example, new route have been installed in routing table.
firewall | Firewall log messages generated whenaction=logis set in firewall rule
gsm | Log messages generated by GSM devices
hotspot | Hotspot related log entries
igmp-proxy | IGMP Proxy related log entries
ipsec | IPSec log entries
iscsi |
isdn |
interface |
kvm | Messages related to the KVM virtual machine functionality
l2tp | Log entries generated by L2TP client and server
lte | Messages related to the LTE/4G modem configuration
ldp | LDP protocol related messages
manager | User Manager log messages.
mme | MME routing protocol messages
mpls | MPLS messages
ntp | sNTP client generated log entries
ospf | OSPF routing protocol messages
ovpn | OpenVPN tunnel messages
pim | Multicast PIM-SM related messages
ppp | ppp facility messages
pppoe | PPPoE server/client related messages
pptp | PPTP server/client related messages
radius | Log entries generated by RADIUS Client
radvd | IPv6 radv daemon log messages.
read | SMS tool messages
rip | RIP routing protocol messages
route | Routing facility log entries
rsvp | Resource Reservation Protocol generated messages.
script | Log entries generated from scripts
sertcp | Log messages related to facility responsible for "/port remote-access"
simulator |
state | DHCP Client and routing state messages.
store | Log entries generated by Store facility
smb | Messages related to the SMB file sharing system
snmp | Messages related to Simple network management protocol (SNMP) configuration
system | Generic system messages
telephony | Obsolete! Previously used by the IP telephony package
tftp | TFTP server generated messages
timer | Log messages that are related to timers used in RouterOS. For example bgp keepalive logs12:41:40 route,bgp,debug,timer KeepaliveTimer expired
12:41:40 route,bgp,debug,timer     RemoteAddress=2001:470:1f09:131::1
ups | Messages generated by UPS monitoring tool
vrrp | Messages generated VRRP
watchdog | Watchdog generated log entries
web-proxy | Log messages generated by web proxy
wireless | Wireless log entries.
write | SMS tool messages.
```
12:41:40 route,bgp,debug,timer KeepaliveTimer expired
12:41:40 route,bgp,debug,timer     RemoteAddress=2001:470:1f09:131::1
```
# Examples
# Logging to file
To log everything to file, add new log action:
```
/system logging action add name=file target=disk disk-file-name=log
```
and then make everything log using this new action:
```
/system logging add action=file
```
You can log only errors there by issuing command:
```
/system logging add topics=error action=file
```
You can specify maximum size of file in lines by specifyingdisk-lines-per-file.<file>.0.txtis active file were new logs are going to be appended and once it size will reach maximum it will become<file>.1.txt, and new empty<file>.0.txtwill be created.
```
/system logging action add name=usb target=disk disk-file-name=usb1/log
```