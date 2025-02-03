---
title: Thread-47189
url: https://forum.mikrotik.com/viewtopic.php?t=47189&sid=49f92a630bc7970d8ca50523be880e8f
thread_id: 47189
section: RouterOS
post_count: 63
date_crawled: 2025-02-03T13:45:20.675846
---

### Post 1
Author: Unknown
Date: Unknown

I tried to Ping ipv6.google.com from the Ping tool without success.I got the error "Error in Ping To - ip address expected" from winbox, or from the command line :ping address=ipv6.google.comwhile resolving ip-address: could not get answer from dns serverSame try from a Linux machine on the same network as this router is working without problem. So i'm sure there is no problem with our DNS servers :ping6 ipv6.google.comPING ipv6.google.com(2a00:1450:8002::63) 56 data bytes64 bytes from 2a00:1450:8002::63: icmp_seq=0 ttl=53 time=48.8 ms64 bytes from 2a00:1450:8002::63: icmp_seq=1 ttl=53 time=45.8 ms64 bytes from 2a00:1450:8002::63: icmp_seq=2 ttl=53 time=46.0 ms64 bytes from 2a00:1450:8002::63: icmp_seq=3 ttl=53 time=44.4 msIf i ping directly the IP address 2a00:1450:8002::63 it's working :ping address=2a00:1450:8002::63HOST                                    SIZE  TTL TIME  STATUS2a00:1450:8002::63                      56    55  58ms  echo reply2a00:1450:8002::63                      56    55  57ms  echo reply2a00:1450:8002::63                      56    55  57ms  echo reply2a00:1450:8002::63                      56    55  57ms  echo reply2a00:1450:8002::63                      56    55  56ms  echo replySeems like there is a problem with IPv6 AAAA pointers resolution.There is no problem with IPv4 pointers : pinging google.com does work from the ping tool.ping google.comHOST                                    SIZE  TTL TIME  STATUS74.125.230.81                           56    58  46ms74.125.230.81                           56    58  46ms74.125.230.81                           56    58  45ms74.125.230.81                           56    58  44msI tried to enter our IPv6 DNS server addresses in the DNS setup, to see if direct resolution on a IPv6 enabled DNS server was working, but this does not help.Mikrotik can you correct this for 5.0 rc6 because it is a fondamental tool for IPv6 tests. Don't forget that the end of IPv4 pool is 03 march 2011. Only four monthes. We have now less than one year to fully test and deploy IPv6.Direct resolution on IPv6 enabled DNS servers is important too because futur clients near 2012 and later will not have access to IPv4 DNS servers. (they will get IPv6 only addresses so they will not be able to contact IPv4 DNS server to get AAAA records).

---
### Post 2
Author: Unknown
Date: Unknown

it used to work, will look into the problem.

---
### Post 3
Author: Unknown
Date: Unknown

Hello, It seems the problem is still there.I upgraded to ROS 5.1 and set DNS (ip->DNS) and added HE.net anycast ipv6 dns server but from mikrotik itself it doesn't resolve any domain into ipv6 address. (ipv6.google.com).But any machine in the networks resolves very good.What's the problem?Cheers.-

---
### Post 4
Author: Unknown
Date: Unknown

Same problem here with 5.1.I can't understand how Mikrotik can get positiv results here.Mikrotik, did you try through a PPPoE IPv6 connection, or Ethernet IPv6 ?I'm trying through PPPoE.Perhaps that binding to PPPoE interfaces does not work from the router ? Missing glue code ??Resolving ipv6.google.com from other machines on the Network works without problems.

---
### Post 5
Author: Unknown
Date: Unknown

I recall it never working on any version of RouterOS.At the moment:Broken on v4.17:Code:Select all[admin@Ranume] > ping ipv6.google.com
invalid value for argument address
[admin@Ranume] >Broken on v4.16:Code:Select all[admin@Skhal] > ping ipv6.google.com
invalid value for argument address
[admin@Skhal] >Broken on v5.0:Code:Select all[admin@Jeekim] > ping ipv6.google.com
dns name exists, but no appropriate record
invalid value for argument ipv6-address
[admin@Jeekim] >Working on Fedora 14 behind these MT boxes and using the same DNS servers:Code:Select all[ivo@haskaa ~]$ ping6 ipv6.google.com
PING ipv6.google.com(2a00:1450:8003::68) 56 data bytes
64 bytes from 2a00:1450:8003::68: icmp_seq=1 ttl=52 time=55.3 ms
64 bytes from 2a00:1450:8003::68: icmp_seq=2 ttl=52 time=53.4 ms
^C
--- ipv6.google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 53.486/54.393/55.301/0.936 ms
[ivo@haskaa ~]$

---
### Post 6
Author: Unknown
Date: Unknown

Testing on 5.4 but not functional yet regular.[admin@mikrotik] > :put [:resolve ipv6.google.com]failure: dns name exists, but no appropriate recordon linux behind this MT resolv works good.

---
### Post 7
Author: Unknown
Date: Unknown

Testing on 5.4 but not functional yet regular.[admin@mikrotik] > :put [:resolve ipv6.google.com]failure: dns name exists, but no appropriate recordon linux behind this MT resolv works good.v5.11 and still the same situation. Why is is so difficult to get fixed/supported?

---
### Post 8
Author: Unknown
Date: Unknown

not sure how to react:Code:Select allRouterOS 5.11 (c) 1999-2011


[admin@hs] > /ping [:resolve ipv6.google.com]
HOST                                     SIZE TTL TIME  STATUS                                                                      
2a00:1450:8005::6a                         56  49 73ms  echo reply                                                                  
2a00:1450:8005::6a                         56  49 59ms  echo reply                                                                  
    sent=2 received=2 packet-loss=0% min-rtt=59ms avg-rtt=66ms max-rtt=73ms 

[admin@hs] > :put [:resolve ipv6.google.com] 
2a00:1450:8005::6aand i have actually IPv6 working with global ipv6 addressing working.

---
### Post 9
Author: Unknown
Date: Unknown

Working for me.But i did not see this syntax in the Wiki :http://wiki.mikrotik.com/wiki/Manual:Tr ... ting_toolsWoud be simpler to have a ping6 tool or a parameter for ping.

---
### Post 10
Author: Unknown
Date: Unknown

I concur.   The behavior isn't consistent with the ipv4 ping syntax where the name resolution automatically happens, but thanks for the post!   Google lead me right to the answer here.   [:resolve ...] doesn't seem real intuitive and it's not in the mikrotik command help.   Verified it works on 5.9 with the [:resolve ...] syntax.

---
### Post 11
Author: Unknown
Date: Unknown

Devs want to address this in general manner not hacking each place with domain separately. So the change is coming.

---
### Post 12
Author: Unknown
Date: Unknown

So the change is coming.It's been almost ten months now, is this change any closer?

---
### Post 13
Author: Unknown
Date: Unknown

So the change is coming.It's been over eleven months now, is this change any closer?

---
### Post 14
Author: Unknown
Date: Unknown

yes, it is on the feature list and will be removed only when implemented.

---
### Post 15
Author: Unknown
Date: Unknown

ROS 6.0rc5:[admin@MikroTik] > ping ipv6.google.comdns name exists, but no appropriate recordinvalid value for argument ipv6-address[admin@MikroTik] > ping 2a00:1450:4017:800::1012HOST                                     SIZE TTL TIME  STATUS2a00:1450:4017:800::1012                   56  57 64ms  echo reply2a00:1450:4017:800::1012                   56  57 64ms  echo reply2a00:1450:4017:800::1012                   56  57 64ms  echo reply2a00:1450:4017:800::1012                   56  57 66ms  echo replysent=4 received=4 packet-loss=0% min-rtt=64ms avg-rtt=64ms max-rtt=66ms

---
### Post 16
Author: Unknown
Date: Unknown

that is problem with ping and requires a lot of changes to make it work. So in the mean time do this insteadros code/ping [:resolve ipv6.google.com]since workaround is pretty trivial

---
### Post 17
Author: Unknown
Date: Unknown

...So in the mean time do this instead ... since workaround is pretty trivialThen where definitely should be at least something likeresolve6!Damn, two years is almost done since the promised feature.

---
### Post 18
Author: Unknown
Date: Unknown

...So in the mean time do this instead ... since workaround is pretty trivialThen where definitely should be at least something likeresolve6!Damn, two years is almost done since the promised feature.Not a resolve6, but the ping6.

---
### Post 19
Author: Unknown
Date: Unknown

Traceroute with IPv6 and use-dns=yes does not resolve PTR of the hops, too.

---
### Post 20
Author: Unknown
Date: Unknown

Not confirmed. ROS 6.25. Traceroute with IPv6 and use-dns = yes resolve PTR.

---
### Post 21
Author: Unknown
Date: Unknown

hm-m-m... I think, 8.8.8.8 is not very IPv6...

---
### Post 22
Author: Unknown
Date: Unknown

hm-m-m... I think, 8.8.8.8 is not very IPv6...I was tired at work and was not attentive. Yes. The problem is confirmed.

---
### Post 23
Author: Unknown
Date: Unknown

Still broken in 6.35.2

---
### Post 24
Author: Unknown
Date: Unknown

[admin@MikroTik Router] > ping nextbigfuture.cominvalid value for argument address:invalid value of mac-address, mac address requiredinvalid value for argument ipv6-addressfailure: dns name exists, but no appropriate recordis this the same problem? anyone know if nextbigfuture.com is using an ipv6 address now?

---
### Post 25
Author: Unknown
Date: Unknown

[admin@MikroTik Router] > ping nextbigfuture.cominvalid value for argument address:invalid value of mac-address, mac address requiredinvalid value for argument ipv6-addressfailure: dns name exists, but no appropriate recordis this the same problem? anyone know if nextbigfuture.com is using an ipv6 address now?Not according to a dig I just did....Code:Select all;; QUESTION SECTION:
;nextbigfuture.com.             IN      A

;; ANSWER SECTION:
nextbigfuture.com.      1800    IN      A       98.124.199.3   <----- only this A record, and no AAAA record

;; AUTHORITY SECTION:
nextbigfuture.com.      172800  IN      NS      dns5.name-services.com.
nextbigfuture.com.      172800  IN      NS      dns2.name-services.com.
nextbigfuture.com.      172800  IN      NS      dns4.name-services.com.
nextbigfuture.com.      172800  IN      NS      dns3.name-services.com.
nextbigfuture.com.      172800  IN      NS      dns1.name-services.com.

;; ADDITIONAL SECTION:
dns1.name-services.com. 152547  IN      A       98.124.192.1
dns2.name-services.com. 152547  IN      A       98.124.197.1
dns3.name-services.com. 152547  IN      A       98.124.193.1
dns4.name-services.com. 152547  IN      A       98.124.194.1
dns5.name-services.com. 152547  IN      A       98.124.196.1

---
### Post 26
Author: Unknown
Date: Unknown

Still not really fixed in 6.39.2 ...Code:Select all[rtradmin@core] > /ping ipv6.google.com
invalid value for argument address:
    invalid value of mac-address, mac address required
    invalid value for argument ipv6-address
    failure: dns name exists, but no appropriate recordAlthough/ping [:resolve ipv6.google.com]works.  From my point of view, for the ping cmd it should not matter, if a host is ipv4 or ipv6.Additionally a parameter for choosing to ping a host by it's v4 or v6 would be nice.Thanks

---
### Post 27
Author: Unknown
Date: Unknown

Devs want to address this in general manner not hacking each place with domain separately. So the change is coming.Is winter coming also? Seriously, getaddrinfo migration takes this long?

---
### Post 28
Author: Unknown
Date: Unknown

This is not getaddrinfo in this case. This is set in RouterOS and, currently, it is not going to be changed to return IPv6 address first and IPv4 after that, but will return IPv4 address if available.There is no information when this will be changed to conform with the RFC to return IPv6 address if usable and then IPv4.

---
### Post 29
Author: Unknown
Date: Unknown

This is not getaddrinfo in this case. This is set in RouterOS and, currently, it is not going to be changed to return IPv6 address first and IPv4 after that, but will return IPv4 address if available.There is no information when this will be changed to conform with the RFC to return IPv6 address if usable and then IPv4.Thanks for the clarification, sadly it's not an IPv4 vs IPv6 preference issue. You simply cannot ping an IPv6 only host. Try the recordipv6.google.comon a PC and then try it from a MikroTik router.Code:Select allPS C:\> Resolve-DnsName -Server 8.8.8.8 -Name ipv6.google.com -Type A

Name                           Type   TTL   Section    NameHost
----                           ----   ---   -------    --------
ipv6.google.com                CNAME  86399 Answer     ipv6.l.google.com

Name                   : l.google.com
QueryType              : SOA
TTL                    : 59
Section                : Authority
NameAdministrator      : dns-admin.google.com
SerialNumber           : 160439217
TimeToZoneRefresh      : 900
TimeToZoneFailureRetry : 900
TimeToExpiration       : 1800
DefaultTTL             : 60



PS C:\> Resolve-DnsName -Server 8.8.8.8 -Name ipv6.google.com -Type AAAA

Name                           Type   TTL   Section    NameHost
----                           ----   ---   -------    --------
ipv6.google.com                CNAME  86394 Answer     ipv6.l.google.com

Name       : ipv6.l.google.com
QueryType  : AAAA
TTL        : 299
Section    : Answer
IP6Address : 2607:f8b0:4009:811::200eLooking at one of my routers:Code:Select all[admin@rtr1] > ping count=2 ipv6.google.com
invalid value for argument address:
    invalid value of mac-address, mac address required
    invalid value for argument ipv6-address
    failure: dns name exists, but no appropriate recordI guess, let's start by making sure we've got the right issue. I understand you don't have a plan to fix a preference for IPv6 over IPv4. Is that the same answer for this level of basic functionality?This probably extends into the tools as well. I just checked /tool traceroute. It works withwww.google.comwhich works (has an A record) and doesn't work with ipv6.google.com (no A record but has a AAAA record).

---
### Post 30
Author: Unknown
Date: Unknown

the problem will go away when IPv6 is set as a preferred option for the :resolve command and elsewhere where RouterOS attempts to resolve a hostname to IP address. When forced the :resolve command is returning the IPv6 address, hence the workaround of /ping [:resolve ipv6.only.domain] is working.

---
### Post 31
Author: Unknown
Date: Unknown

I assume that'll have the inverse effect of not working with IPv4 names then?

---
### Post 32
Author: Unknown
Date: Unknown

Wouldn't happy eyeballs dictate that it try both and utilize whichever opens faster?(Or maybe that RFC only applies to browsers and media player applications, but not appliances such as routers, etc)

---
### Post 33
Author: Unknown
Date: Unknown

This workaround is a definitive solution?the problem will go away when IPv6 is set as a preferred option for the :resolve command and elsewhere where RouterOS attempts to resolve a hostname to IP address. When forced the :resolve command is returning the IPv6 address, hence the workaround of /ping [:resolve ipv6.only.domain] is working.

---
### Post 34
Author: Unknown
Date: Unknown

This workaround is a definitive solution?the problem will go away when IPv6 is set as a preferred option for the :resolve command and elsewhere where RouterOS attempts to resolve a hostname to IP address. When forced the :resolve command is returning the IPv6 address, hence the workaround of /ping [:resolve ipv6.only.domain] is working.Yup, still no movement. I suspect we'll see little improvement until the market truly forces their hands. It's good thing that Ubnt is iterating and releasing IPv6 features for their controller on top of the support they already have in other products.

---
### Post 35
Author: Unknown
Date: Unknown

It's been over 5 years, now. Does it really take that long to figure out how to make a commonly-used utility at least fall-back to AAAA records when there are no A records? Or any of the other numerous solutions?

---
### Post 36
Author: Unknown
Date: Unknown

RouterOS 6.43.7 on all devices.I have exactly the same problem with Mikrotik unable to resolve AAAA records from a hostname.My test Mikrotik LtAP device gets CGNAT protected private IPv4 address of 100.64.0.0/18 from the mobile operator. There is no inbound access to that.The same Mikrotik LtAP device gets dynamic and changing IPv6 address address and IPv6 prefix, which is nice. That IPv6 address is accessible from the Internet.The "/ip cloud" DDNS hostname now has both A and AAAA records, which is nice. The X.sn.mynetname.net gets updated with the CGNAT external A-record and the native IPv6 address. Nice.When I am on Mikrotik CLI elsewhere in the world, there is no way to use IPv6 when saying "/system ssh 123456789.sn.mynetname.net".One of the listed "solutions" 6 years ago was " /ping [resolve ipv6.google.com]" . That only works when the hostname has only the AAAA record, but no A record.The X.sn.mynetname,net addresses have both A and AAAA records. And again, Mikrotik will only resolve to a lonely A record, if that is available. Another example of the same thing is when user says "/ping [:resolve google.com]", resolving allways to IPv4-only. "google.com" hostname has the AAAA record, Mikrotik is never bothered to ask that, ever.Even when the Mikrotik DNS cache has the target hostname and its AAAA record already known and cached (and no A record cached), Mikrotik resolver will still A-record query the outside DNS resolvers, and force using the A record for everything. Not good.This seems to be really unwanted issue to fix in Mikrotik.For the easiest solution, could Mikrotik implement a new ":resolve" function with name of ":resolve6"? That ":resolve6" will only query AAAA recods (and follow CNAMES of course). A  matching ":resolve4" would be important to have too, forcing query of the plain A records (and following the CNAMEs). And still now, the funny plain stupid-vanilla ":resolve" thingie can stay as it is and as it wants to [not]work.This suggestion does not break anything, all systems and scripts will work exactly as before. Now the users who have to use hostnames and forcing IPv6 addresses, can say "/ping [:resolve6 google.com]"  and get the functionality and results they need.

---
### Post 37
Author: Unknown
Date: Unknown

RouterOS 6.43.7 on all devices.I have exactly the same problem with Mikrotik unable to resolve AAAA records from a hostname.My test Mikrotik LtAP device gets CGNAT protected private IPv4 address of 100.64.0.0/18 from the mobile operator. There is no inbound access to that.The same Mikrotik LtAP device gets dynamic and changing IPv6 address address and IPv6 prefix, which is nice. That IPv6 address is accessible from the Internet.The "/ip cloud" DDNS hostname now has both A and AAAA records, which is nice. The X.sn.mynetname.net gets updated with the CGNAT external A-record and the native IPv6 address. Nice.When I am on Mikrotik CLI elsewhere in the world, there is no way to use IPv6 when saying "/system ssh 123456789.sn.mynetname.net".One of the listed "solutions" 6 years ago was " /ping [resolve ipv6.google.com]" . That only works when the hostname has only the AAAA record, but no A record.The X.sn.mynetname,net addresses have both A and AAAA records. And again, Mikrotik will only resolve to a lonely A record, if that is available. Another example of the same thing is when user says "/ping [:resolve google.com]", resolving allways to IPv4-only. "google.com" hostname has the AAAA record, Mikrotik is never bothered to ask that, ever.Even when the Mikrotik DNS cache has the target hostname and its AAAA record already known and cached (and no A record cached), Mikrotik resolver will still A-record query the outside DNS resolvers, and force using the A record for everything. Not good.This seems to be really unwanted issue to fix in Mikrotik.For the easiest solution, could Mikrotik implement a new ":resolve" function with name of ":resolve6"? That ":resolve6" will only query AAAA recods (and follow CNAMES of course). A  matching ":resolve4" would be important to have too, forcing query of the plain A records (and following the CNAMEs). And still now, the funny plain stupid-vanilla ":resolve" thingie can stay as it is and as it wants to [not]work.This suggestion does not break anything, all systems and scripts will work exactly as before. Now the users who have to use hostnames and forcing IPv6 addresses, can say "/ping [:resolve6 google.com]"  and get the functionality and results they need.Regardless of workarounds MikroTik's apathetic approach to IPv6 lost MikroTik 2 full network refreshes on my side in December alone to Ubiquiti. At least they (Ubiquiti) demonstrated that they are capable of developing IPv6 related features.

---
### Post 38
Author: Unknown
Date: Unknown

RouterOS 6.43.7 on all devices.I have exactly the same problem with Mikrotik unable to resolve AAAA records from a hostname.My test Mikrotik LtAP device gets CGNAT protected private IPv4 address of 100.64.0.0/18 from the mobile operator. There is no inbound access to that.The same Mikrotik LtAP device gets dynamic and changing IPv6 address address and IPv6 prefix, which is nice. That IPv6 address is accessible from the Internet.The "/ip cloud" DDNS hostname now has both A and AAAA records, which is nice. The X.sn.mynetname.net gets updated with the CGNAT external A-record and the native IPv6 address. Nice.When I am on Mikrotik CLI elsewhere in the world, there is no way to use IPv6 when saying "/system ssh 123456789.sn.mynetname.net".One of the listed "solutions" 6 years ago was " /ping [resolve ipv6.google.com]" . That only works when the hostname has only the AAAA record, but no A record.The X.sn.mynetname,net addresses have both A and AAAA records. And again, Mikrotik will only resolve to a lonely A record, if that is available. Another example of the same thing is when user says "/ping [:resolve google.com]", resolving allways to IPv4-only. "google.com" hostname has the AAAA record, Mikrotik is never bothered to ask that, ever.Even when the Mikrotik DNS cache has the target hostname and its AAAA record already known and cached (and no A record cached), Mikrotik resolver will still A-record query the outside DNS resolvers, and force using the A record for everything. Not good.This seems to be really unwanted issue to fix in Mikrotik.For the easiest solution, could Mikrotik implement a new ":resolve" function with name of ":resolve6"? That ":resolve6" will only query AAAA recods (and follow CNAMES of course). A  matching ":resolve4" would be important to have too, forcing query of the plain A records (and following the CNAMEs). And still now, the funny plain stupid-vanilla ":resolve" thingie can stay as it is and as it wants to [not]work.This suggestion does not break anything, all systems and scripts will work exactly as before. Now the users who have to use hostnames and forcing IPv6 addresses, can say "/ping [:resolve6 google.com]"  and get the functionality and results they need.Regardless of workarounds MikroTik's apathetic approach to IPv6 lost MikroTik 2 full network refreshes on my side in December alone to Ubiquiti. At least they demonstrated that they are capable of developing IPv6 related features.They are looking for another thinks like KidControland surprise KidControl doesn’t work with IPv6

---
### Post 39
Author: Unknown
Date: Unknown

KidControl doesn’t work with IPv6Well, RouterOS Version 6.44beta50 added IPv6 for KidControl and I am quite happy about this.Let's hope that means, that IPv6 will be better supported in the rest of RouterOS in the near future ....

---
### Post 40
Author: Unknown
Date: Unknown

Solution 1: A quick and easy way is to implement the following commands. These do not break existing scritps:- :resolve6  = resolves to AAAA records, following CNAME's of course- :resolve4 = resolves A records, following CNAME's of course---------- 8< -------- 8< -----Solution 2: Optionally, the current ':resolve' could be pimped to accept an optional second argument of QUERY RR. Again, as current implementations only use single argument <arg>, it could easily be extended to support the RR info too. Again,  this as well is 100% backwards compatible.  Examples:- put [:resolve xkcd.com]  = resolves as it currently does- put [:resolve xkcd.com A]  = asks for a 'A' record, as it does without second argument- put [:resolve xkcd.com AAAA] = asks for a 'AAAA' IPv6 address- etc---------- 8< -------- 8< -----Both these solutions are 100% backwards compatible to all the existing scripts, and also very very easy to implement.Depending which is considered more difficult inside Mikrotik product politics, extending current commands with backwards compatibility OR creating new commands. Personally I would prefer the second solution, since all of those 'new commands' are same in real life.Again, I hope Mikrotik notices the "current solution" of using "put  [:resolve ipv6.google.com]", does not work at all when the hostname also has an A record too.  In Google context, better example is  [:resolve google.com] , offering both A and AAAA records.

---
### Post 41
Author: Unknown
Date: Unknown

Yes, when i see how Mikrotik ignores for YEARS the ipv6 standards, i would agree that they will certainly loose corporate sector and become ipv6-"ready" home routers.There is no more unused ipv4 addresses, nor ipv4-only new businesses. The decline will be automatic, if they refuse to implement RFC and ipv6 commands, like ping6 or ping -6.For me the next router will be ipv6 - compliant.

---
### Post 42
Author: Unknown
Date: Unknown

I didn't realize there was a thread that was this old about frustration with the RFC-noncompliant nature of DNS resolution in RouterOS. I think @alaine was on the right track in 2015 when they suggested that the best angle to take is a backward-compatible improvement to:resolve. Anyone still following this thread (maybe even from Mikrotik) might want to take a look at my proposal for:resolveimprovements overhere. The exact same behaviors I suggest could be used implicitly behind the scenes to make:pingwork like you expect.Here is a relevant snippet:1. Continue the default behavior to only return one record, but provide an option full-answer=true|false to return the full answer.The :resolve command is used for both debugging and scripting purposes and this change benefits both purposes. Since RouterOS has DNS server functionality, it's always frustrating to debug DNS-related issues when the router itself doesn't have a good DNS client. Currently, the only recourse is to use dig or nslookup from a client device and then inspect :ip dns cache on the router to see what happened. From a scripting perspective, it would be nice to be given all of the answers for a query for round-robin connections, health checks, etc.2. Provide an option in :ip dns called client-behavior: prefer-v4|dual-stackprefer-v4 preserves the legacy behavior and will return A record(s) if both A and AAAA are available. Since some users are undoubtedly relying on this quirk, this can remain the RouterOS default for several versions to give them time to migrate.dual-stack follows RFC 8305 and attempts dual-stack resolution like a standard DNS client. If both address families are present and RouterOS has a configured IPv6 address it can use as a source, the AAAA record(s) are returned. After a sufficient amount of time, this should become the RouterOS default.The fact that RouterOS unconditionally prefers IPv4 makes it ill-suited as a modern dual-stack client. I don't fully understand why the choice was made in the first place. Although not in my ask here (because of the amount of work that would be involved), I do hope that RouterOS 7 has a proper RFC-8305-compliant control plane for any connections the router makes.

---
### Post 43
Author: Unknown
Date: Unknown

This is real ? Still an issue!Why not just implement a second ping command calledping6?

---
### Post 44
Author: Unknown
Date: Unknown

I understand that it is difficult to implement new features, but not keep up to date the functionality that is needed today - this is a serious miscalculation for the entire Mikrotik company as a manufacturer of telecommunication equipment,I suggest that anyone who needs IPv6 to raise this thread... until they turn it on due attention...

---
### Post 45
Author: Unknown
Date: Unknown

Is this really still an issue?Is MikroTik still not IPv6 ready?

---
### Post 46
Author: Unknown
Date: Unknown

Yup, major reason why my network is now on UniFi. Ubiquiti actually heard feedback and released updates to their platform to be much friendlier towards IPv6.Vote with your wallet.

---
### Post 47
Author: Unknown
Date: Unknown

Is this really still an issue?Is MikroTik still not IPv6 ready?Yes!((

---
### Post 48
Author: Unknown
Date: Unknown

Uff.Do you guys know a way to display / show the current SLAAC IPv6 address?

---
### Post 49
Author: Unknown
Date: Unknown

Uff.Do you guys know a way to display / show the current SLAAC IPv6 address?routeros can't get nor prefix nor address via slaac... and therefore cant show it

---
### Post 50
Author: Unknown
Date: Unknown

Wrong, RouterOS can get address using SLAAC (/ipv6 settings set accept-router-advertisements=no/yes/yes-if-forwarding-disabled) and it currently doesn't show it anywhere. You can e.g. ping something and see it using Tools->Torch or logging rules. I didn't try it, but maybe even DDNS would update hostname with it.

---
### Post 51
Author: Unknown
Date: Unknown

So now way to display except torch?Is their any ETA?Can’t recommend rOS for IPv6 deployments right now.Many things like vpn, modeconfig, etc. is missing completely

---
### Post 52
Author: Unknown
Date: Unknown

My guess is that SLAAC addresses (for the router itself) are not very high on list of priorities, since it's not what you usually need on router. But sometimes they can be useful, so I'm sure that better support (showing them, per-interface config, etc) will be added eventually. But when that might be, we can only guess.

---
### Post 53
Author: Unknown
Date: Unknown

Wrong, RouterOS can get address using SLAAC (/ipv6 settings set accept-router-advertisements=no/yes/yes-if-forwarding-disabled) and it currently doesn't show it anywhere. You can e.g. ping something and see it using Tools->Torch or logging rules.I say'd about absent address because i can't found it anywhere...but agree - SLAAC (address) work, and address i found only in /tool quick sniff...on one console ping 2001:4860:4860::8888, on other console sniff:2.553     39 ->  6C:3B:12:34:56:78 D4:CA:12:34:56:782a03:e2c0:...2001:4860:4860::8888                ipv6:ic...   70   0 no2.596     40 <-  D4:CA:12:34:56:78 6C:3B:12:34:56:78        2001:4860:4860::88882a03:e2c0:...ipv6:ic...   70   0 no...I didn't try it, but maybe even DDNS would update hostname with it.I try'ed - it really work! - ddns work viaipv6 onlyconnected router.

---
### Post 54
Author: Unknown
Date: Unknown

Hi!I want to up this thread - i hope Mikrotik will be more attractive in IPv6!!!

---
### Post 55
Author: Unknown
Date: Unknown

Still not fixed 11 years later.

---
### Post 56
Author: Unknown
Date: Unknown

I had checked in packet level (DNS UDP/53), how the commands work on ROS 7.1.1/ping ipv6.google.comCode:Select all1	0.000000	2001:my_ip_address	2001:4860:4860::8888	DNS	142	Standard query 0x5da3 A ipv6.google.com
2	0.062202	2001:4860:4860::8888	2001:my_ip_address	DNS	213	Standard query response 0x5da3 A ipv6.google.com CNAME ipv6.l.google.com SOA ns1.google.comand that's all. It' does not try to resolve ipv6.l.google.com.The error message is:invalid value for argument address:invalid value of mac-address, mac address requiredinvalid value for argument ipv6-addressfailure: dns name exists, but no appropriate record/ping [:resolve ipv6.google.com]Code:Select all3	3.582657	2001:my_ip_address	2001:4860:4860::8888	DNS	142	Standard query 0x0f09 A ipv6.google.com
4	3.685863	2001:4860:4860::8888	2001:my_ip_address	DNS	213	Standard query response 0x0f09 A ipv6.google.com CNAME ipv6.l.google.com SOA ns1.google.com
5	3.686434	2001:my_ip_address	2001:4860:4860::8888	DNS	144	Standard query 0x3dd9 AAAA ipv6.l.google.com
6	3.770671	2001:4860:4860::8888	2001:my_ip_address	DNS	172	Standard query response 0x3dd9 AAAA ipv6.l.google.com AAAA 2a00:1450:4014:80e::200eIt's clear that, the ip address resolved normally unsing :resolveThepingcommand somehow uses a different DNS resolver and doesn't follow the DNS request recursively and resolve the CNAME record.

---
### Post 57
Author: Unknown
Date: Unknown

Still not fixed as it seems (RB 4011 on RouterOS 7.6). I found this thread when researching for this exact problem.Code:Select all[user@MikroTik-RO] > ping ipv6.google.com
invalid value for argument address:
    invalid value of mac-address, mac address required
    invalid value for argument ipv6-address
    failure: dns name exists, but no appropriate record
    
[user@MikroTik-RO] > ping [:resolve ipv6.google.com]
  SEQ HOST                                     SIZE TTL TIME       STATUS                                                                                                   
    0 2a00:1450:4001:82a::200e                   56 114 18ms794us  echo reply                                                                                               
    1 2a00:1450:4001:82a::200e                   56 114 17ms54us   echo reply                                                                                               
    2 2a00:1450:4001:82a::200e                   56 114 14ms693us  echo reply                                                                                               
    sent=3 received=3 packet-loss=0% min-rtt=14ms693us avg-rtt=16ms847us max-rtt=18ms794us

---
### Post 58
Author: Unknown
Date: Unknown

Soon 12 years ago (Mon Dec 06, 2010 10:57 am), Mikrotik/janisk said wisely above "it used to work, will look into the problem".Now, how has that been going? Any improvements yet?Even Microsoft Windows, about all active versions with IPv6 address, willprefer to resolve and use AAAA addresses. And those are: Microsoft products, the real power house of networking since 1994 erahttps://en.wikipedia.org/wiki/Trumpet_Winsock. They have surpassed a heavy path to their current CLI, which is now preferring to support and prefer AAAA addresses.Now, we all wait for Mikrotik to get their own field together. Possibly one day, IPv6 enabled devices can be allowed to prefer IPv6 destinations too.

---
### Post 59
Author: Unknown
Date: Unknown

Don't forget that Microsoft started with IPv6 much sooner than MikroTik. I'm not kidding, I had working IPv6 in Windows 2000 and they made it even for NT 4.0 (according tothis pdfthey started in 1996 and first public release was in 1998). RouterOS first included IPv6 in version 3.0 (2007). It's also true that Microsoft initially cheated and had separate ping6.

---
### Post 60
Author: Unknown
Date: Unknown

Consistency, still same issue.

---
### Post 61
Author: Unknown
Date: Unknown

Resurrecting this threadBecause I struggle with IPv4/6 tests, DNS and the ping command. The workaround will not work, if there is only one domain name and the DNS server respond with multiple A and AAAA entries. Any idea how to work around this? or finally solve this issue @Mikrotik.It is very important to be able to specifcally test the IPv4 or IPv6 reachability of hosts via DNS Names. IPv6 addresses are not very compatible with my brain

---
### Post 62
Author: Unknown
Date: Unknown

Resurrecting this threadBecause I struggle with IPv4/6 tests, DNS and the ping command. The workaround will not work, if there is only one domain name and the DNS server respond with multiple A and AAAA entries. Any idea how to work around this? or finally solve this issue @Mikrotik.It is very important to be able to specifcally test the IPv4 or IPv6 reachability of hosts via DNS Names. IPv6 addresses are not very compatible with my brain:resolve now has a "type" parameter so you can do this:Code:Select all/ping [:resolve type=ipv6 domain-name=google.com] count=4

---
### Post 63
Author: Unknown
Date: Unknown

Almost forget to say: Thank youI feel a bit stupid, not to figure out the type parameter.

---
