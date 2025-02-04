---
title: Thread-9322
url: https://forum.mikrotik.com/viewtopic.php?t=9322&sid=49f92a630bc7970d8ca50523be880e8f
thread_id: 9322
section: RouterOS
post_count: 7
date_crawled: 2025-02-03T21:22:05.420125
---

### Post 1
Author: Unknown
Date: Unknown

Hello!I can log the nat from my client how to connect the internet?My master router ist mikrotik!Thank you for your advance?I have Nice day!I can search the forum and have no post!

---
### Post 2
Author: Unknown
Date: Unknown

To log data from NAT table, or to log specific data from NAT table.Use action=log before NAT rule (log-prefix to assign prefix for the log info).E.g.'ip firewall nat add chain=srcnat action=log src-address=x.x.x.x/xxip firewall nat add chain=srcnat action=masquerade src-address=x.x.x.x/xx'

---
### Post 3
Author: Unknown
Date: Unknown

Sergejs!The example workt!I can download the logfile the log downloader?

---
### Post 4
Author: Unknown
Date: Unknown

I don't understand you correctly.But here isSyslogdaemon for Windows, that will help you to handle your logs.

---
### Post 5
Author: Unknown
Date: Unknown

I don't understand you correctly.But here isSyslogdaemon for Windows, that will help you to handle your logs.I put down!I tested in the nigth!Thank you!

---
### Post 6
Author: Unknown
Date: Unknown

I don't understand you correctly.But here isSyslogdaemon for Windows, that will help you to handle your logs.I put down!I tested in the nigth!Thank you!

---
### Post 7
Author: Unknown
Date: Unknown

Revitalizing this old question: is this still the way to do it? Using a RB5009 with 7.16.2, I'm not getting consistent results. It does log /some/ new outgoing connections, but only some, and some not... What is the current and preferred method of logging new outgoing NATted connections?

---
