# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 204878

# Discussion

## Initial Question
Author: Wed Feb 21, 2024 9:56 pm
``` # Clean up existing queues; this part is working fine/queue simple:foreachxin=[find comment~"IPv6 Client Queue"]do={:localqueuename[get$x name];/queue simpleremove$queuename;}# Generate new queues, issues listed below/ipv6 neighbor:foreachyin=[findinterface=bridge address!~"fe80:"status!="failed"]do={:localaddr[get$y address];:localmac[get$y mac-address];:localhost[/ip arpget[findwheremac-address=$mac]host-name]:localqueueName"Client - $mac";/queue simple add name=$queueName target=($addr."/128") queue=client/client limit-at=1M/1M max-limit=10M/10M priority=8/8 parent="GatewayIPv6" comment="IPv6ClientQueue-$host";} ``` To control bandwith used by each client, I use simple queues.For IPv4 clients, each queue is automatically created (upon lease bound), updated (upon IP address change), and removed (upon lease expiry) by /ip/dhcp-server lease-script.For IPv6 clients, we don't use DHCP, so I plan to periodically scan /ipv6/neighbor and create & remove queues based on its entries.My proposed script is as follows, it should be run on a schedule:
```
Issue list:Apparently MikroTik doesn't implementaddress!~"fe80:"(address that doesn't start with fe80:).Is there another way to implement this? I confirmed thataddress~"fe80:"works (address that starts with fe80:).Issue solved onthe next post.Apparently MikroTik doesn't implementstatus!="failed".Is there another way to implement this? I confirmed thatstatus="failed"works.Issue solved onthe next post.Even though WinBox displays host name in IP -> ARP window, it is not provided on /ip/arp print. Therefore,/ip/arp get [find where mac-address=$mac] host-namefails.I confirmed that/ip/arp get [find where mac-address=$mac] interfaceworks. Are there other ways to lookup host name from a MAC address?We can get host name from IPv4 DHCP leases using/ip/dhcp-server/lease get [find where active-mac-address=$mac] host-name. Therefore, this issue is also solved.Thanks in advance.


---
```

## Response 1
Author: [SOLVED]Fri Feb 23, 2024 2:24 pm
``` /ipv6 neighborprintwhereinterface="bridge"and!(address~"^fe80:")andstatus!="failed" ``` ``` # Clean up existing queues; this part is working fine/queue simple:foreachxin=[find comment~"IPv6 Client Queue"]do={:localqueuename[get$x name];/queue simpleremove$queuename;} ``` ``` /queue simpleremove[findwherecomment~"IPv6 Client Queue"] ``` Writing that "Apparently MikroTik doesn't understand <insert wrong syntax here>" is quite arrogant.It's not up to RouterOS (MikroTik is the company) to figure out what you wanted to do and try to guess the commands you wanted executed.Apparently you doesn't understand script syntax.This work correctly on both v6.48.7 and v7.13.5
```
This is totally bad style and wrong concept:
```

```
Must be SIMPLY
```

```
---
```

## Response 2
Author: Sat Feb 24, 2024 2:39 am
``` /ipv6 neighborprintwhereinterface="bridge"and!(address~"^fe80:")andstatus!="failed" ``` ``` # Clean up existing queues; this part is working fine/queue simple:foreachxin=[find comment~"IPv6 Client Queue"]do={:localqueuename[get$x name];/queue simpleremove$queuename;} ``` ``` /queue simpleremove[findwherecomment~"IPv6 Client Queue"] ``` Writing that "Apparently MikroTik doesn't understand <insert wrong syntax here>" is quite arrogant.It's not up to RouterOS (MikroTik is the company) to figure out what you wanted to do and try to guess the commands you wanted executed.Apparently you doesn't understand script syntax.You're correct. My understanding of ROS script syntax and English language is low, therefore the apparent arrogance. I have edited the first post to reduce my apparent arrogance.This work correctly on both v6.48.7 and v7.13.5
```
Thank you. This successfully addresses issue #1 and #2.This is totally bad style and wrong concept:
```

```
Must be SIMPLY
```

```
Thank you. Apparently both code did the same thing. However, I assume your code is more CPU-efficient.Perhaps what AI bots are outputting these days for answers??No, I write the script myself, no AI involved.


---
```

## Response 3
Author: Tue Jun 25, 2024 10:51 pm
``` # Automatic Simple Queue based on IPv6 Neighbors# Copyright (C)2024 MSaid# Disable logging temporarily/system logging disable[find topics~"info"];# Clean up existing queues/queue simpleremove[findwherename~"6Client - "];# Generate new queues:localcounter0;/ipv6 neighbor:foreachyin=[findinterface="bridge"andaddress~"2001:2002:2003:2004:"andstatus!="failed"andstatus!="noarp"]do={:localaddr[get$y address];:localmac[get$y mac-address];:setcounter($counter+1);:do{/queue simple add name=("6Client - ".$mac." - ".$counter) target=($addr."/128") queue=client/client limit-at=10M/10M max-limit=215M/215M burst-limit=216M/216M burst-threshold=45M/45M burst-time=120/120 priority=8/8 parent="Gateway6" comment=("v6Client-".[/ip dhcp-server lease get [find where active-mac-address=$mac] host-name]); } on-error={/queue simple add name=("6Client-".$mac."-".$counter) target=($addr."/128") queue=client/client limit-at=10M/10M max-limit=215M/215M burst-limit=216M/216M burst-threshold=45M/45M burst-time=120/120 priority=8/8 parent="Gateway6"} } # Re-enable logging /system logging enable [find topics~"info"]; ```