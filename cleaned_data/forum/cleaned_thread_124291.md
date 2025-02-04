# Thread Information
Title: Thread-124291
Section: RouterOS
Thread ID: 124291

# Discussion

## Initial Question
I do log packet from my mikrotik's to Splunk.This works nice, except I have problem to categorize package.Here is a list of prefix I have found:
```
certificate,debug
certificate,info
dhcp,critical,error
dhcp,debug
dhcp,debug,packet
dhcp,debug,state
dhcp,info
dhcp,warning
dns
dns,packet
e-mail,debug
firewall,info
interface,info
ipsec
ipsec,debug
ipsec,debug,packet
ipsec,error
ipsec,info
l2tp,debug
l2tp,debug,packet
l2tp,info
l2tp,ppp,debug
l2tp,ppp,debug,packet
l2tp,ppp,error
l2tp,ppp,info
l2tp,ppp,info,account
ntp,debug
ntp,debug,packet
pptp,debug
pptp,debug,packet
pptp,info
pptp,ppp,debug
pptp,ppp,debug,packet
pptp,ppp,error
pptp,ppp,info
pptp,ppp,info,account
radvd,debug
route,debug
route,debug,calc
route,debug,event
script,error
snmp
snmp,debug
ssh,debug
ssh,debug,packet
ssh,info
sstp,packet
system,e-mail,error
system,error,critical
system,info
system,info,account
upnpIt looks like its on format:module,severity,info, eksssh,debug,packetBut that is only half true.What about:system,error,criticalis that module,severity,severity?system,e-mail,errormodule,module,severity?ipsechere is severity missingpptp,ppp,info,accountmodule,module,severity,info?Why no just clean this up to only use module, severity, info.Eks:e-mail,error, blabla other infoOn all message use severity.E-mail should be its own module, not listed under system.Hope some one can clean this up.  It would make Splunk application much more easy.Jo

---
```

## Response 1
Still nothing has happen to this. ---

## Response 2
I am still waiting for this to be fixed (cleaned up)Should not be to hard??If it can not be done whit 6.x, add it to the 7.x version of ros ---

## Response 3
I can see that v7 beta has not fixed anything regarding log format. ---

## Response 4
I don't think anyone cares. ---

## Response 5
Seems so. But the idea is not bad, I like it. ---

## Response 6
When using external logging tools like Splunk to analyse logs, this old and messy format gives a lot of extra work.I have sent this request two times to MikroTik so they know about it. ---

## Response 7
I have filed a feature request some time ago to allow more control over the logging.Of course the best would be when there is much more detail about the log message in the prefix, probably even up to a unique identifier of each message.(so you don't have to rely on pattern matching of the message text to separate the individual error messages for the same category)When each message has a unique category it would also be possible to suppress certain messages while showing detailed output of some category for some reason (when not using Splunk but only the internal logging handler).Lacking that, I have proposed to add regexp matching capability to the logging topics matcher, but of course more detailed topics would be best. ---

## Response 8
Still not fixed in v7.1 ---

## Response 9
ROS-internally they just throw all into the same bin and call it "topics". So no distinction between module and severity.But they seem to already separate module/severity when logging to syslog-server (seehttps://help.mikrotik.com/docs/display/ROS/Log). ---

## Response 10
There are some small changes in 7.x but as you see in the list below, its not possible to see what severity level each type of log lines have.Example some DNS just shows DNS. IT should be in an equal comma separated format. Examplel2tp, ppp, info, accountcompare tol2tp, info. Severity at 3rd or 2end field??Look at these two:system, critical, infosystem, error, criticalWhat critically are those messages?Taken from 7.5 logs:
```
bridge,info
bridge,stp
dhcp,debug
dhcp,debug,packet
dhcp,debug,state
dhcp,info
dhcp,warning
dns
dns,error
dns,packet
dns,warning
e-mail,info
firewall,info
info
interface,info
ipsec
ipsec,error
ipsec,info
l2tp,info
l2tp,ppp,error
l2tp,ppp,info
l2tp,ppp,info,account
netwatch,info
ntp,warning
poe-out,info
route,bgp,error
route,bgp,info
route,ospf,info
route,ospf,warning
script,error
script,info
snmp
ssh,info
system,critical,info
system,error,critical
system,info
system,info,account
system,info,critical
upnp
wireguard,debug
wireless,infoMake it some like this:Module,Severity,Type,Other

---
```

## Response 11
As written above, I would propose adding another identifier which is unique for the message. E.g. an 8-digit hex number. That would be last in the sequence.This allows to suppress one particular message or to match it in a script. The number would be assigned once to each specific message and never change. Maybe the first digit of the number would indicate the severity, then some digits for the module, and the remainder the message number. ---

## Response 12
I like that idea, an ID in form of a number of text.If you look at logg message for a Cisco Router/Firewall, all message have their own ID:
```
%CDP_PD-4-POWER_OK
%DOT11-4-BA_FLUSH
%DOT11-6-ROAMED
%EVT-4-WRN
%HA_EM-6-LOG
%ILPOWER-7-DETECT
%LINEPROTO-5-UPDOWN
%LINK-3-UPDOWN
%LINK-5-CHANGED
%LINK-6-UPDOWN
%SW_MATM-4-MACFLAP_NOTIF
%SYS-3-HARIKARI
%SYS-5-CONFIG_I
%SYS-5-RELOADetcThey are in the formModule-Severity-Type_of_message.Some like I requested above

---
```

## Response 13
Yes, most professional systems have such a structure. E.g. VMS, IBM operating systems, even Microsoft Windows has error numbers.Essential in my opinion is that the number is only an addition for programming purposes (scripting, logging in external systems, etc) and not a replacement as it is in Microsoft Windows.(something went wrong, error code 89abcdef. which you then have to google to see what it even means. there should always be a message text) ---

## Response 14
I am not very happy with the Microsoft logging part.Yes, each message has its own ID, so that is ok, but:XML will give large/long messages.Standard logs: hard to see what belongs to what and they do add an message telling: "This message was genereted due to ++++".Same text added to same EventCode id. Just makes the message longer without giving any thing extra.And if you install Swedish or other language on a server running Citrix or other Multi user system) the log message are mixed in English and Swedish.... ---

## Response 15
The best solution to make logging great again for syslog:Just use:rfc 5424(released March 2009)There all modules are separated by correct name at correct location in the message.Messages that belongs together have same IDetc...Please MT do follow standards.https://www.rfc-editor.org/rfc/rfc5424 ---

## Response 16
mikrotik already has a checkbox to enable rfc3164 compatibility. ---

## Response 17
How do you know? ---

## Response 18
syslog001.JPGbsd-syslog (yes|no; Default: ) whether to use bsd-syslog as defined in RFC 3164https://wiki.mikrotik.com/wiki/Manual:System/Log ---

## Response 19
Does no help at all. BSD logs are even worse . Look at these DHCP debug logs.BSD logs
```
2022-11-08T17:06:35.639612+01:00 <31>Nov  8 17:06:34 OVA MikroTik:     Client-Id = 01-00-0C-AA-9B-EA-66
2022-11-08T17:06:35.639683+01:00 <31>Nov  8 17:06:34 OVA MikroTik: dhcp-client on bridge received ack with id 3916435468 from 10.11.10.1
2022-11-08T17:06:35.639744+01:00 <31>Nov  8 17:06:34 OVA MikroTik:     ciaddr = 0.0.0.0
2022-11-08T17:06:35.639831+01:00 <31>Nov  8 17:06:34 OVA MikroTik:     yiaddr = 10.11.10.141
2022-11-08T17:06:35.639884+01:00 <31>Nov  8 17:06:34 OVA MikroTik:     siaddr = 10.11.10.1
2022-11-08T17:06:35.639956+01:00 <31>Nov  8 17:06:34 OVA MikroTik:     chaddr = 00:0C:AA:9B:EA:66
2022-11-08T17:06:35.640060+01:00 <31>Nov  8 17:06:34 OVA MikroTik:     Subnet-Mask = 255.255.254.0
2022-11-08T17:06:35.640144+01:00 <31>Nov  8 17:06:34 OVA MikroTik:     Router = 10.11.10.1
2022-11-08T17:06:35.640210+01:00 <31>Nov  8 17:06:34 OVA MikroTik:     Domain-Server = 10.11.10.1
2022-11-08T17:06:35.640285+01:00 <31>Nov  8 17:06:34 OVA MikroTik:     NTP-Server = 10.11.10.1
2022-11-08T17:06:35.640349+01:00 <31>Nov  8 17:06:34 OVA MikroTik:     Address-Time = 86400
2022-11-08T17:06:35.640431+01:00 <31>Nov  8 17:06:34 OVA MikroTik:     Msg-Type = ack
2022-11-08T17:06:35.640493+01:00 <31>Nov  8 17:06:34 OVA MikroTik:     Server-Id = 10.11.10.1
2022-11-08T17:06:35.640567+01:00 <30>Nov  8 17:06:34 OVA MikroTik: dhcp-client on bridge got IP address 10.11.10.141
2022-11-08T17:06:35.640631+01:00 <31>Nov  8 17:06:34 OVA MikroTik: dhcp-client on bridge entering <bound> state
2022-11-08T17:06:37.048188+01:00 <30>Nov  8 17:06:36 OVA MikroTik: user jotne logged in from 10.11.10.32 via winbox
2022-11-08T17:06:37.231730+01:00 <30>Nov  8 17:06:36 OVA MikroTik: local query: #1 upgrade.mikrotik.com. A
2022-11-08T17:06:37.260367+01:00 <30>Nov  8 17:06:36 OVA MikroTik: done query: #1 upgrade.mikrotik.com 159.148.172.226Without BSD
```

```
2022-11-08T17:08:43.989247+01:00 <13>dhcp,debug,packet MikroTik:     Client-Id = 01-00-0C-AA-9B-EA-66
2022-11-08T17:08:43.989411+01:00 <13>dhcp,debug,packet MikroTik: dhcp-client on bridge received ack with id 1310283069 from 10.11.10.1
2022-11-08T17:08:43.989411+01:00 <13>dhcp,debug,packet MikroTik:     flags = broadcast
2022-11-08T17:08:43.989506+01:00 <13>dhcp,debug,packet MikroTik:     ciaddr = 0.0.0.0
2022-11-08T17:08:43.989571+01:00 <13>dhcp,debug,packet MikroTik:     yiaddr = 10.11.10.141
2022-11-08T17:08:43.989619+01:00 <13>dhcp,debug,packet MikroTik:     siaddr = 10.11.10.1
2022-11-08T17:08:43.989698+01:00 <13>dhcp,debug,packet MikroTik:     chaddr = 00:0C:AA:9B:EA:66
2022-11-08T17:08:43.989748+01:00 <13>dhcp,debug,packet MikroTik:     Subnet-Mask = 255.255.254.0
2022-11-08T17:08:43.989859+01:00 <13>dhcp,debug,packet MikroTik:     Router = 10.11.10.1
2022-11-08T17:08:43.990017+01:00 <13>dhcp,debug,packet MikroTik:     Domain-Server = 10.11.10.1
2022-11-08T17:08:43.990017+01:00 <13>dhcp,debug,packet MikroTik:     NTP-Server = 10.11.10.1
2022-11-08T17:08:43.990017+01:00 <13>dhcp,debug,packet MikroTik:     Address-Time = 86400
2022-11-08T17:08:43.990114+01:00 <13>dhcp,debug,packet MikroTik:     Msg-Type = ack
2022-11-08T17:08:43.990203+01:00 <13>dhcp,debug,packet MikroTik:     Server-Id = 10.11.10.1
2022-11-08T17:08:43.990315+01:00 <13>dhcp,info MikroTik: dhcp-client on bridge got IP address 10.11.10.141
2022-11-08T17:08:43.990362+01:00 <13>dhcp,debug,state MikroTik: dhcp-client on bridge entering <bound> stateAs you see with BSD, you do not see what module data belongs to, but it sends the router name as extra info.Without BSD it sends DHCP, DEBUG, PACKETIt would help allot if an ID was sent as part of the DHCP request (or other logs that are multiple lines) to make sure what belongs togeather.

---
```

## Response 20
Using telegraf I tried BSD or non-BSD logging - it's not working. Telegraf complains.2023-01-18T21:52:38Z E! [inputs.syslog] Error in plugin: expecting an alphanumeric tag (max 32 characters) [col 34]Only mikrotik gives me such trouble. Anything changed in syslog since the 90s? :DUnless someone has an idea, guess I'll open a ticket w/ mikrotik. Thank! ---

## Response 21
Holy crap - I just noticed this thread started years agoWish I knew this before buying any mikrotik product.Do I get this right, Mikrotik thinks logging isn't important? Is there a second option that I'm not aware? Cloud logging perhaps? ---

## Response 22
I did make a support request for it some times ago, and MT responded that they sad that they will look at it.In may year of making Splunk for Mikrotik, I have worked around it.But it would love that MT fixes this. ---

## Response 23
It probably is a "work in progress". That is MikroTik language for: we know that it is important but we do not have the resources to work on it. ---

## Response 24
As of comment in 7.8beta post. No need to change it, just add a new logging option that do follow a more standard format.DHCP logs are another system that fails that are in the same range. SUP-105355For the logging I always like to get, host_name and class_id (MSFT 5.0 etc). That can you can get when enable DHCP debug message.A complete set of one DHCP request looks like this (with timestamp not shown)
```
dhcp,debug MikroTik: DHCP-vlan20-Guest received request id 2761716067 from 0.0.0.0 '1:c4:5d:83:59:7c:41'
dhcp,debug,packet MikroTik:     flags = broadcast
dhcp,debug,packet MikroTik:     ciaddr = 0.0.0.0
dhcp,debug,packet MikroTik:     chaddr = C4:5D:83:59:7C:41
dhcp,debug,packet MikroTik:     Host-Name = "GalaxyWatch3-CC40"
dhcp,debug,packet MikroTik:     Address-Request = 10.10.20.142
dhcp,debug,packet MikroTik:     Msg-Type = request
dhcp,debug,packet MikroTik:     Server-Id = 10.10.20.1
dhcp,debug,packet MikroTik:     Parameter-List = Subnet-Mask,Router,Interface-MTU,Auto-Proxy-Config,NTP-Server,Domain-Name,Domain-Server,Host-Name
dhcp,debug,packet MikroTik:     Max-DHCP-Message-Size = 576
dhcp,debug,packet MikroTik:     Client-Id = 01-C4-5D-83-59-7C-41
dhcp,debug MikroTik: lease offered, addressed to me
dhcp,info MikroTik: DHCP-vlan20-Guest assigned 10.10.20.142 for C4:5D:83:59:7C:41 GalaxyWatch3-CC40
dhcp,debug MikroTik: DHCP-vlan20-Guest sending ack with id 2761716067 to 255.255.255.255
dhcp,debug,packet MikroTik:     flags = broadcast
dhcp,debug,packet MikroTik:     ciaddr = 0.0.0.0
dhcp,debug,packet MikroTik:     yiaddr = 10.10.20.142
dhcp,debug,packet MikroTik:     siaddr = 10.10.20.1
dhcp,debug,packet MikroTik:     chaddr = C4:5D:83:59:7C:41
dhcp,debug,packet MikroTik:     Subnet-Mask = 255.255.255.0
dhcp,debug,packet MikroTik:     Router = 10.10.20.1
dhcp,debug,packet MikroTik:     Domain-Server = 10.10.10.1Using commands in Splunk or other tools I can join those message looking for first to last message in one request.This works fine in a system with low DHCP request.  But when there are many requests at more or less the same time, they will be merged together.A solution for this would be that all message belongs to same request.  Then we could just join those message to one request.

---
```

## Response 25
I'd add "don't use multi-line log entries" (DHCP being the worst oftener): one event, one entry.That I do agree to. It will solve the DHCP multiline logg. ---

## Response 26
I'd add "don't use multi-line log entries" (DHCP being the worst oftener): one event, one entry.That I do agree to. It will solve the DHCP multiline logg.LOL. Yes, your example above is what I was talking about. It clutters the log when reading for a single client's thing & no doubt must be a nightmare to parse.They have multi cores CPUs, so violating "one event, one entry", make matching lines impossible in some cases no doubt. ---

## Response 27
I've been going back and forth trying different log systems, and always get reminded by the useless log format of RouterOS. At least map the severity levels automatically instead of requiring a fixed value. I could work around that by creating separate log actions, but that's stupid. ---

## Response 28
I've been going back and forth trying different log systems, and always get reminded by the useless log format of RouterOS. At least map the severity levels automatically instead of requiring a fixed value. I could work around that by creating separate log actions, but that's stupid.on my syslog server all logs are undernoticeseverity/level ---

## Response 29
That is not realted to the topic, it is the broken syslog agent that only allows the raw message to be sent including its topics, or the "bsd format" with a fixed facility and severity can be selected but the topics are not sent. We need a setting inbetween that. ---

## Response 30
To actually contribute constructively I would like to see support for RFC 5424, with severity levels mapped probably to their corresponding syslog level. Use preferrablyonetopic for the application name.https://www.rfc-editor.org/rfc/rfc5424Edit: Ok, my bad, the severity level does get set automatically when using the BSD Syslog option. Though, as mentioned, some other data is omitted instead. ---

## Response 31
Edit: Ok, my bad, the severity level does get set automatically when using the BSD Syslog option. Though, as mentioned, some other data is omitted instead.Example for logs not usingBSDsyslog (log part in red are tags I do add to the logs)dnsserial=yyyyyyy MikroTik:done query: #56718 brb.duolingo.com. 54.230.111.35Example for logs using BSD syslogFeb 19 13:24:32 RB951serial=xxxxxxxx MikroTik:done query: #16955 brb.duolingo.com. 54.230.111.35As you see, non-BSD add what module that do sends the logs. This is a must since there are many types of modules sending logs.The BSD on the other hand removes the module information but adds the Time of log and identity of the router.@ Mikrotik. Please fix this and useRFC 5424. What can we to to help? ---

## Response 32
Not even the BSD-on rfc3164 is correct.https://www.rfc-editor.org/rfc/rfc3164.html
```
BSD-on: "<30>Apr 11 14:17:05 HOST user admin logged in from 192.168.2.3 via winbox"
BSD-off: "system,info,account user admin logged in from 192.168.2.3 via winbox"Mickrotik Syslog 3164 is missing the TAG field from rfc3164, can't parse it correctly, have to create a parser from scrach for this type of log.And the BSD-off option has no severity level or hostname format for parsing but can be Regexed by keyword somehow to extract severity..,Not even using a custom parser can fix this. (the only way is to somehow group logs in a buffer by pairs with the same message, but becomes too complex is a log is dropped)This should be critical in priority.

---
```

## Response 33
Well, found a way to get everything i wanted with some wiring.Add prefixes for every log severity defined inhttps://help.mikrotik.com/docs/display/ROS/LogIn reality there are only 5 that are useful: info, warning, error, critical, debugFor every one define a prefix in this format:
```
<pri> hostpri: is a number, use a table like this one:https://techdocs.broadcom.com/us/en/sym ... -grid.htmlfor example for info logs use: 30 and so on.host: manually enter your host.Use the non-BSD remote log.At the receiving forwarder use this regex:
```

```
^(?<topics>[^ ]*) \<(?<pri>[^ ]+)\> (?<host>[^ ]+): (?<message>.+)$Thats it, fixed partially, original timestamp is the only thing missing so there will be some skew.

---
```

## Response 34
It may help some, but where do you put a message like this:
```
system,error,critical MikroTik: router was rebooted without proper shutdownIs this an error message with severity 3, or a critical message with severity 2Only good way to fix this is for MT to use RFC 5424 and make all logs uniform with same format everywhere.BSD format is based on the obsolete RFC 3164 released in 2001.  Even there MT have messed up the format.https://www.rfc-editor.org/rfc/rfc3164RFC 5424 was released in 2009 so MT can not say it was just released...https://www.rfc-editor.org/rfc/rfc5424Example for a RFC 5424 message<165>1 2003-10-11T22:14:15.003Z mymachine.example.com  evntslog - ID47 [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"] BOMAn application event log entry..165 would be a local4 message with severity normal.  Time format is easy to read and should always be in UTC zone (Zulu)PS MT are not the only company that have a messed up logs.  Cisco may be some better in some product and worse in other.But since Cisco now bought Splunk (for $28 billion), it may force them to start to follow standard logging format.

---
```

## Response 35
Cisco is not good at following syslog standards either. It has it's own log formats, without proper headers, that change between device types, and even between IOS version.That's a logging nightmare. ---

## Response 36
I do agree with you. I guess some of the problems comes while Cisco buys other companies and do not update it to follow standard.Logs from Palo Alto are 10 times better than the one from Cisco ASA. More info, better standard used. ---

## Response 37
After 8 years...From MikroTik RouterOS 7.18 support for CEF (Commont Event Format) logging format is added, as well as timestamp support for milliseconds. ---

## Response 38
After 8 years...From MikroTik RouterOS 7.18 support for CEF (Commont Event Format) logging format is added, as well as timestamp support for milliseconds.Where did you find this info ??? ---

## Response 39
Only on the official (help) documentation, not on idiotic rumors (I'm referring to another topic).https://help.mikrotik.com/docs/Just search "CEF"Often page # change so direct link is broken, but until still valid:https://help.mikrotik.com/docs/spaces/R ... og-Summary ---

## Response 40
tnx, that is really good news ! ---

## Response 41
Yes, some other news (search on help "31 address" or "1000 characters")viewtopic.php?t=189798#p1119638@Jotne is happy now for Splunkhttps://www.splunk.com/en_us/blog/learn ... t-cef.htmlexpected format codeCEF:0|MikroTik|CHR|1.0|100|LoginSuccess|5|src=192.168.1.10 dst=192.168.1.20 suser=admin msg=User login successful CEF:0|MikroTik|CHR|1.0|100|LogoutSuccess|5|src=192.168.1.10 dst=192.168.1.20 suser=admin msg=User logout successful CEF:0|MikroTik|CHR|1.0|100|LoginSuccess|5|src=192.168.1.10 dst=192.168.1.20 suser=admin msg=User login successful CEF:0|MirkoTik|CHR|1.0|100|LogoutSuccess|5|src=192.168.1.10 dst=192.168.1.20 suser=admin msg=User logout successful ---

## Response 42
Well, I still hope there will also be some unique message code ("topic") for each and every different message that can be logged by RouterOS.As it is now, there are too many different messages grouped under the same topic, and filtering is difficult.(also because the system logging rules can only filter on topic and not on message regexp) ---

## Response 43
This will be a mayor change in how logging is done in Mikrotik. Would greatly help not for Splunk but for all that do use logging from MikrotikWhy do not Miktotik update my SUP with this information is an other question.Looking forward to beta test this. ---

## Response 44
Why do not Miktotik update my SUP with this information is an outer question.Probably the SUPs from more than a day ago have already been forgotten... ---