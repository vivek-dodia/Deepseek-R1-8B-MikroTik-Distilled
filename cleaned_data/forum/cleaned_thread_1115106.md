# Thread Information
Title: Thread-1115106
Section: RouterOS
Thread ID: 1115106

# Discussion

## Initial Question
I was on 7.13.X previously, never had this message in the log.I don't use cache on DNS queries (it is cached upstream) so my config is this:
```
/ip dnssetallow-remote-requests=yes cache-max-ttl=0sservers=X.X.X.XSince 7.14, I get a lot of spam in the logs on every DNS request:cache full, not storingbuffer: memorytopics: dns, errorPlease allow us to disable the cache in some other way or revert the log message!

---
```

## Response 1
What device are you using ?If it is a device with 16Mb storage, 7.14 can be a 'challenge' depending on your config.Side note:If you do not want to use dns cache at all, you may also want to change this
```
/ip dnssetallow-remote-requests=yesSet to no.From Help pagesallow-remote-requests (yes | no; Default: no)Specifies whether to allow router usage as a DNS cache for remote clients. Otherwise, only the router itself will use DNS configuration.

---
```

## Response 2
1) It has nothing do to with device memory2) It has nothing to do with allowing remote requests ---

## Response 3
3) So you already know the answer. ---

## Response 4
Yes they introduced a bug where when making a DNS request that can't be added to the DNS cache, it thinks the cache is full when the TTL is just actually 0 (the only way to disable the cache).It has nothing to do with my 423.0 MiB available on device especially when the log outputs to memory as reported.It has nothing to do with allowing external requests to the DNS server. ---

## Response 5
... the sad thing is, that this bug hasn't been fixed either in 7.14.1 or in 7.15 beta6 ---

## Response 6
@lekozsEDIT: Nope, message re-appeared after one day, still have the bugORIGINAL MESSAGE:I don't know about you but I don't have the messages anymore in7.14.1 ---

## Response 7
I wonder if their support is aware of this issue or should a request be open...? ---

## Response 8
In case of doubt, always create support request incl. supout.rif. ---

## Response 9
I am seeing this as well since upgrading from 7.13 this week. I have created a ticket in reference to the issue.I found disabling "allow remote request" and re-enabling it seems to fix it. I am not certain if that's temporary or not.edit: scratch that, it started again.. ---

## Response 10
I've also opened a support ticket and linked them to this thread. Will see how it goes. ---

## Response 11
Ya i have yet to get a response. ---

## Response 12
I was on 7.13.X previously, never had this message in the log.I don't use cache on DNS queries (it is cached upstream) so my config is this:
```
/ip dnssetallow-remote-requests=yes cache-max-ttl=0sservers=X.X.X.XSince 7.14, I get a lot of spam in the logs on every DNS request:cache full, not storingbuffer: memorytopics: dns, errorPlease allow us to disable the cache in some other way or revert the log message!Hello,I had the same issue and solved it by setting a firewall rule to block outside requests on port 53 UDP, The MK DNS server was acting as a public DNS server.

---
```

## Response 13
Hello, I had the same issue and solved it by setting a firewall rule to block outside requests on port 53 UDP, The MK DNS server was acting as a public DNS server.Your failure: As usual, in this cases, either you configured the firewall badly, or thinking you were the smartest you deleted the default rules that prevent this (and other things) from happening. ---

## Response 14
Hello, I had the same issue and solved it by setting a firewall rule to block outside requests on port 53 UDP, The MK DNS server was acting as a public DNS server.Your failure: As usual, in this cases, either you configured the firewall badly, or thinking you were the smartest you deleted the default rules that prevent this (and other things) from happening.If my memory serves me right, the default settings for the MK firewall do not include a rule to block UDP traffic on port 53.My sole oversight was not executing the correct takeover of the router. This was amid a sequence of transitions, starting with a change in the main provider. The former provider assigned IPs via DHCP, but then we switched to a provider that used PPPoE, and the existing rule was set for WAN1. Initially, this was fine, but after the transition to the new PPPoE provider, the rule ceased to apply, which went unnoticed until internet connection issues began to surface. ---

## Response 15
If my memory serves me well default firewall blocks ALL incoming traffic which did not earlier originate from the inside of your network.Without exception (apart from ICMP).But I could be wrong ... ---

## Response 16
The default firewall rules dropping all on input at the end, so if not allowed before, nothing is allowed after.If you write "If my memory serves me well" it is because you have deleted the default rules, so you cannot recheck them, sinning of pride.v6, but are like the same for v7viewtopic.php?f=13&t=175129&p=856824#p856824extract code/ip firewall filter add chain=input action=accept connection-state=established, related, untracked comment="defconf: accept established, related, untracked" add chain=input action=drop connection-state=invalid comment="defconf: drop invalid" add chain=input action=accept protocol=icmp comment="defconf: accept ICMP" add chain=input action=accept dst-address=127.0.0.1 comment="defconf: accept to local loopback (for CAPsMAN)" add chain=input action=drop in-interface-list=!LAN comment="defconf:drop all not coming from LAN" ---

## Response 17
If my memory serves me well default firewall blocks ALL incoming traffic which did not earlier originate from the inside of your network.Without exception (apart from ICMP).But I could be wrong ...Since I am not a full-time MK/RouteOS admin (only from time to time), thank you for your clarification. ---

## Response 18
The default firewall rules dropping all on input at the end, so if not allowed before, nothing is allowed after.If you write "If my memory serves me well" it is because you have deleted the default rules, so you cannot recheck them, sinning of pride.As I said before this was not my building, my only error was I didn't do the proper take-over, as a "sign of pride" (I think this you meant, please correct me if I am mistaking) not at all, more sign of shame . . . . as I hope you can understand as a fellow tech DB. . . . .v6, but are like the same for v7viewtopic.php?f=13&t=175129&p=856824#p856824extract code/ip firewall filter add chain=input action=accept connection-state=established, related, untracked comment="defconf: accept established, related, untracked" add chain=input action=drop connection-state=invalid comment="defconf: drop invalid" add chain=input action=accept protocol=icmp comment="defconf: accept ICMP" add chain=input action=accept dst-address=127.0.0.1 comment="defconf: accept to local loopback (for CAPsMAN)" add chain=input action=drop in-interface-list=!LAN comment="defconf:drop all not coming from LAN"In the end in possible conclusion: this issue might not be a bug just a misconfiguration of the firewall where some "default" rules were deleted or any other rule in "sign of pride" ---

## Response 19
Anyone see any updates on this? We're seeing a log full of these errors even though, as mentioned, there's plenty of free memory. ---

## Response 20
Cache size is configurable, you might want to increase the memory (if you haven't tried already?):
```
/ip dnssetcache-size=20480KiB

---
```

## Response 21
I've seen the same in log today. 7.16beta4. Using DOH with NextDNS. ---

## Response 22
Same for me, full dns - flush do not help. ---

## Response 23
Same here on 7.16beta4.16384KiB of cache memory allocated, only 2839 KiB used, and yet my logs are full of repeating "cache full, not storing" which continue to fire.I have not performed packet captures on the outbound interface to see if it really is looking them up every time or if this is an erroneous error they introduced when adding Adblock with DoH.Has anyone fired a report to Mikrotik officially to make sure they know about this, or do they stop in here too? ---

## Response 24
I've also opened a support ticket and linked them to this thread. Will see how it goes.thank you for doing that! ---

## Response 25
I've seen the same in log today. 7.16beta4. Using DOH with NextDNS.different issue, wrong topic ---

## Response 26
This topic has many people each with a different issue, please all calm down and stop with the "me too". DoH and v7.16beta is unrelated with cache full message, that is not cleared, after cache is timed out. DoH issues in beta - please go post in the beta topic.Up to this version the IP/DNS setting cache-size was not properly working. If you see this error in the log, then it means that cache size has reached its maximum size. You can:1) Increase max cache size;2) Reduce amount of DNS requests towards cache.Cache will not store responses from the DNS server, but it will send replies from the server to clients.We are aware that log message continues to be written even if you "flush" cache. DNS at that point will again store replies in the cache, however, log will print false warnings. This is a known issue which will be resolved ---

## Response 27
duplicate:viewtopic.php?p=1088073 ---

## Response 28
This topic has many people each with a different issue, please all calm down and stop with the "me too". DoH and v7.16beta is unrelated with cache full message, that is not cleared, after cache is timed out. DoH issues in beta - please go post in the beta topic.Up to this version the IP/DNS setting cache-size was not properly working. If you see this error in the log, then it means that cache size has reached its maximum size. You can:1) Increase max cache size;2) Reduce amount of DNS requests towards cache.Cache will not store responses from the DNS server, but it will send replies from the server to clients.We are aware that log message continues to be written even if you "flush" cache. DNS at that point will again store replies in the cache, however, log will print false warnings. This is a known issue which will be resolvedThanks for acknowledging the issue.As said earlier in this post, I don't want to cache any entries myself so it's not about a cache size or memory issue.As of today and package `7.15.3` version, it is still occuring.Thank you ---

## Response 29
Hello everyone...I don't know if I'm in time with this answer, but I've had the same problem and I've solved it at least in my case, deleting the parameters added in the "Adlist" option. I noticed that since I added that parameter I started to receive the cache full notice. Good luck to all and I hope the tip serves you ---

## Response 30
Still occuring, still not fixed.. here is my configuration and some runtime infos:
```
[admin@rb4011]>/ip/dnsprintservers:<redacted>dynamic-servers:use-doh-server:verify-doh-cert:nodoh-max-server-connections:5doh-max-concurrent-queries:50doh-timeout:5sallow-remote-requests:yes
          max-udp-packet-size:4096query-server-timeout:2squery-total-timeout:10smax-concurrent-queries:100max-concurrent-tcp-sessions:20cache-size:2048KiBcache-max-ttl:0saddress-list-extra-time:0svrf:main
           mdns-repeat-ifaces:cache-used:2048KiB[admin@rb4011]>/ip/dns/cacheprintFlags:S-STATICColumns:NAME,TYPE,DATA,TTL#   NAME        TYPE   DATA         TTL0S<redacted>A<redacted>0s1S<redacted>A<redacted>0s2S<redacted>A<redacted>0s3S<redacted>CNAME<redacted>.0s4S<redacted>CNAME<redacted>.0s5S<redacted>CNAME<redacted>.0s6S<redacted>CNAME<redacted>.0s7S<redacted>CNAME<redacted>.0s8S<redacted>CNAME<redacted>.0s9S<redacted>CNAME<redacted>.0s10S<redacted>CNAME<redacted>.0s11S<redacted>CNAME<redacted>.0s12S<redacted>CNAME<redacted>.0s13S<redacted>CNAME<redacted>.0s14S<redacted>CNAME<redacted>.0s15S<redacted>CNAME<redacted>.0s16S<redacted>CNAME<redacted>.0s17S<redacted>CNAME<redacted>.0s18S<redacted>CNAME<redacted>.0s19S<redacted>CNAME<redacted>.0s20S<redacted>CNAME<redacted>.0s21S<redacted>CNAME<redacted>.0s22S<redacted>CNAME<redacted>.0s23S<redacted>A<redacted>0s24S<redacted>A<redacted>0s25S<redacted>CNAME<redacted>.0s26S<redacted>A<redacted>0s27S<redacted>CNAME<redacted>.0s28S<redacted>A<redacted>0s29S<redacted>A<redacted>0s30S<redacted>A<redacted>0s31S<redacted>A<redacted>0s32S<redacted>CNAME<redacted>.0s33S<redacted>CNAME<redacted>.0s34S<redacted>CNAME<redacted>.0s35S<redacted>CNAME<redacted>.0s36S<redacted>A<redacted>0s37S<redacted>A<redacted>0s38S<redacted>A<redacted>0s39S<redacted>A<redacted>0s40S<redacted>CNAME<redacted>.0s41S<redacted>CNAME<redacted>.0s42S<redacted>CNAME<redacted>.0s43S<redacted>CNAME<redacted>.0s[admin@rb4011]>/ip/dns/export# 2024-10-22 12:09:18 by RouterOS 7.16.1# software id = <redacted>## model = RB4011iGS+# serial number = <redacted>/ip dnssetallow-remote-requests=yes cache-max-ttl=0sservers=<redacted>/ip dnsstaticaddaddress=<redacted>name=<redacted>type=Aaddaddress=<redacted>name=<redacted>type=Aaddaddress=<redacted>name=<redacted>type=Aaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddaddress=<redacted>name=<redacted>type=Aaddaddress=<redacted>name=<redacted>type=Aaddcname=<redacted>name=<redacted>type=CNAMEaddaddress=<redacted>name=<redacted>type=Aaddcname=<redacted>name=<redacted>type=CNAMEaddaddress=<redacted>name=<redacted>type=Aaddaddress=<redacted>name=<redacted>type=Aaddaddress=<redacted>name=<redacted>type=Aaddaddress=<redacted>name=<redacted>type=Aaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddaddress=<redacted>name=<redacted>type=Aaddaddress=<redacted>name=<redacted>type=Aaddaddress=<redacted>name=<redacted>type=Aaddaddress=<redacted>name=<redacted>type=Aaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAMEaddcname=<redacted>name=<redacted>type=CNAME[admin@rb4011]>/system/scriptexport# 2024-10-22 12:13:12 by RouterOS 7.16.1# software id = <redacted>## model = RB4011iGS+# serial number = <redacted>/system scriptadddont-require-permissions=noname=<redacted>owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":do {\r\
        \n    :resolve www.example.com server (redacted)\r\
        \n    :if ([/ip dns get servers] != \"(redacted)\") do={\r\
        \n        /ip dns set servers=\"(redacted)\"\r\
        \n        :log info \"Restored DNS server to (redacted)\"\r\
        \n    }\r\
        \n} on-error={\r\
        \n    :if ([/ip dns get servers] != \"(redacted)\") do={\r\
        \n        /ip dns set servers=\"(redacted)\"\r\
        \n        :log error \"DNS server (redacted) down, using (redacted)\"\r\
        \n    }\r\
        \n}"[admin@rb4011]>/system schedulerexport# 2024-10-22 12:14:02 by RouterOS 7.16.1# software id = <redacted>## model = RB4011iGS+# serial number = <redacted>/system scheduleraddinterval=30sname=<redacted>on-event=check-dns policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=2002-01-01start-time=00:00:00I set
```

```
cache-max-ttl=0sto avoid caching DNS entries because I do the caching on the upstream server.

---
```

## Response 31
Does it help to set cache-size=0? ---

## Response 32
In my case the error was resolved after the update to version 7.16.1 , it was not a real error for space because i didn't increase the cache sizeI just apply the update.Regards ---

## Response 33
same problem with 7.16.1 but with 7.16.2 it seems to be gone... ---

## Response 34
I was on 7.13.X previously, never had this message in the log.I don't use cache on DNS queries (it is cached upstream) so my config is this:
```
/ip dnssetallow-remote-requests=yes cache-max-ttl=0sservers=X.X.X.XSince 7.14, I get a lot of spam in the logs on every DNS request:cache full, not storingbuffer: memorytopics: dns, errorPlease allow us to disable the cache in some other way or revert the log message!Hello,I had the same issue and solved it by setting a firewall rule to block outside requests on port 53 UDP, The MK DNS server was acting as a public DNS server.SOLVED TOOExactly, I have switched from ip behind na to public ip on my main mikrotik router and I forget that Allow remote request is enabling requests not only for LAN but also for WAN!I have interface lists where are my wan interfaces grouped so I just simply drop all remote requests targeting the WAN  interface:
```

```
/ip firewall filteraddchain=input protocol=udp dst-port=53in-interface-list=WAN action=drop comment="Block DNS requests from WAN"/ip firewall filteraddchain=input protocol=tcp dst-port=53in-interface-list=WAN action=drop comment="Block DNS requests from WAN"

---
```

## Response 35
Exactly, I have switched from ip behind na to public ip on my main mikrotik router and I forget that Allow remote request is enabling requests not only for LAN but also for WAN!It shouldn't as the default firewall rules only allows calls from LAN (interace list). Perhaps have a good look at your current firewall rules? ---

## Response 36
If you add such rules it is better to drop the packets in the prerouting stage.
```
/ip firewall filteraddchain=prerouting action=dropin-interface-list=WAN dst-port=53protocol=udp/ip firewall filteraddchain=prerouting action=dropin-interface-list=WAN dst-port=53protocol=tcp

---
```

## Response 37
Even better to not allow anything from WAN except VPN and established, related, etc.Oh wait ... that's done by default firewall rules ... ---