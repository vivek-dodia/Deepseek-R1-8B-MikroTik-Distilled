# Thread Information
Title: Thread-1122079
Section: RouterOS
Thread ID: 1122079

# Discussion

## Initial Question
I have a strange problem with Mikrotik Hex model RB750Gr3I have gigabit internet on fiber and 5g network connected to my Mikrotik but I can't really use more than 250 Mbps. Only if I reach full bandwidth can I activate fast track, and since I can't use it as pcc and load balance with fast track activated, What should I do to fix this problem? According to the tests, the processor is not used more than 50% of the time, what is the reason? What is the limit? ---

## Response 1
CPU in hEX Gr3 is not exactly speed monster. It's got 2 CPU cores (with 4 threads altogether but I don't know how ROS utilizes that). And the gotcha: all packets of same connection are handled by same CPU core/thread (processing may move between cores, but there's no parallel processing). And windows file transfers are single connection (AFAIK MS went ahead implementing multi-connection SMB transfers but it's a new feature and not sll servers and clients support that), so all traffic hits same CPU core. Similarly single HTTP/HTTPS file download or (plain old) FTP and many more. Torrents are not affected (that much) as torrent clients communicate with many peers and processing of those connections is nicely spread over all CPU cores, but each individual connection is still affected.And that's what you're seeing.And a side remark: using PCC/mangle does not entirely disqualify fasttrack ... just the fasttrack rule (which marks connections for fasttracking) has to be adjusted so that it only affects connections which don't need mangling. Or create accept rule(s) which deal with connections requiring mangling and place it/them above fasttrack rule. I'm not saying that in your particular case this would help though. ---

## Response 2
@soheilsh have you seen the test results on mikrotik website?Routing 25 ip filter rules 512 byte265.2 MbpsYour test results confirm that. This device is not suitable for your needs. ---

## Response 3
And the Hex refresh is roughly double of that, 498.1:https://mikrotik.com/product/hex_2024#fndtn-testresultsstill half the speed you want/need.You need either (looking ahead) a RB5009 at around 3 Gb, $219:https://mikrotik.com/product/rb5009ug_s ... estresultsor a hap Ax3 (as router), 1145.2, $139:https://mikrotik.com/product/hap_ax3#fndtn-testresultsAn Ax2, if you want to save a few bucks, is almost there, 912.9, $ 99:https://mikrotik.com/product/hap_ax2#fndtn-testresults ---

## Response 4
And the Hex refresh is roughly double of that, 498.1:https://mikrotik.com/product/hex_2024#fndtn-testresultsstill half the speed you want/need.You need either (looking ahead) a RB5009 at around 3 Gb, $219:https://mikrotik.com/product/rb5009ug_s ... estresultsor a hap Ax3 (as router), 1145.2, $139:https://mikrotik.com/product/hap_ax3#fndtn-testresultsAn Ax2, if you want to save a few bucks, is almost there, 912.9, $ 99:https://mikrotik.com/product/hap_ax2#fndtn-testresultsI was just looking at the hap lite tc test specifications. Its speed is very close to hex. It's really stupid. Hex has a 2-core, 2-thread processor, but hap lite has a single core with a low frequency! ---

## Response 5
CPU in hEX Gr3 is not exactly speed monster. It's got 2 CPU cores (with 4 threads altogether but I don't know how ROS utilizes that). And the gotcha: all packets of same connection are handled by same CPU core/thread (processing may move between cores, but there's no parallel processing). And windows file transfers are single connection (AFAIK MS went ahead implementing multi-connection SMB transfers but it's a new feature and not sll servers and clients support that), so all traffic hits same CPU core. Similarly single HTTP/HTTPS file download or (plain old) FTP and many more. Torrents are not affected (that much) as torrent clients communicate with many peers and processing of those connections is nicely spread over all CPU cores, but each individual connection is still affected.And that's what you're seeing.And a side remark: using PCC/mangle does not entirely disqualify fasttrack ... just the fasttrack rule (which marks connections for fasttracking) has to be adjusted so that it only affects connections which don't need mangling. Or create accept rule(s) which deal with connections requiring mangling and place it/them above fasttrack rule. I'm not saying that in your particular case this would help though.I don't know how this is a problem, but I was shocking by MikroTik. If I install the same hex on OpenWRT, the load balance speed is similar to PCC, giving me gigabit speeds. ---

## Response 6
Is there a way other than pcc that I can do two 500 Mbps internet links with hex link aggregation? ---

## Response 7
No, not when device is running ROS. You'll simply have to accept that ROS is not the most performing OS on many of supported devices. ---

## Response 8
I was just looking at the hap lite tc test specifications. Its speed is very close to hex. It's really stupid. Hex has a 2-core, 2-thread processor, but hap lite has a single core with a low frequency!They are different architectures and hAP lite just might be using CPU which does more per core snd CPU cyle. ---

## Response 9
with Fasttrack you can get Full Speed with the 750GR3and with 7.18beta this is also working with IPv6 ---

## Response 10
with Fasttrack you can get Full Speed with the 750GR3and with 7.18beta this is also working with IPv6In some use cases fasttrack can't be used. E.g. in case by @OP. ---

## Response 11
Hard to assess if PCC vice ECMP is more useful without knowing the ISP particulars. ( speaking about need for mangling etc.) ---

## Response 12
with Fasttrack you can get Full Speed with the 750GR3and with 7.18beta this is also working with IPv6really? 7.18beta pcc work with fasttrack? ---

## Response 13
if you really want significantly better performance you must go to next tier of MikroTIk devices like RB5009UG+S+INi know is more expensive but It is what it isa halfway option is hAP ax²both options offer very good price to performance ratio ---

## Response 14
if you really want significantly better performance you must go to next tier of MikroTIk devices like RB5009UG+S+INi know is more expensive but It is what it isa halfway option is hAP ax²both options offer very good price to performance ratioNot suitable for a country whose currency has fallen against the dollar. ---

## Response 15
with Fasttrack you can get Full Speed with the 750GR3and with 7.18beta this is also working with IPv6really? 7.18beta pcc work with fasttrack?No I am saying since Vers7, ECMP is now automatically applied and is actually a more favourable load balancing approach IMHO.It automatically provides load balancing when one has multiple WANs and one does not designate any distance difference between the WANs.The real power is if one of the WANS lets say in a four ISP setup, is not available, ECMP will automatically distribute the load between the three other WANS.To approximate the same thing in PCC is way more complex in comparison.Where PCC comes into play is if there is much disparity between the ISPs in terms of throughput as the ECMP will not favour the larger throughput WAN and thus the available bandwidth will not be used in a reasonable proportion. With PCC you can modify the number of times in a cycle, the router goes to a specific WAN ( to ensure a larger bandwith ISP) sees more sessions compared to the lesser bandwidth ISPs. There is also some issues with banks needed to see sessions from the same ISP from a user etc........ Although it may be less of an issue now than before.One can achieve better load balancing granularity by bandwidth based load balancing but that is a step more complex than PCC........As per Tomas -A sticky connection• A sticky connection is a connection, that onceestablished through one interface, will always go outthat exact interface.• This is required, because when we switch to a secondlink, we only need to switch new connections.• In PCC, this is done automatically. Using bandwidth based load balancinghowever, this has to be done manually which implies a second layer of manglesOne then uses traffic monitoring to trigger an action above a certain traffic threshold --> move sessions to next WAN ( via changing the routing table by changing routing mark )Similarly one uses traffic monitoring to trigger an action below a certain traffic threshold ---> move sessions back to this WAN ( via changing the routing table by changing routing mark) ---

## Response 16
really? 7.18beta pcc work with fasttrack?No I am saying since Vers7, ECMP is now automatically applied and is actually a more favourable load balancing approach IMHO.It automatically provides load balancing when one has multiple WANs and one does not designate any distance difference between the WANs.The real power is if one of the WANS lets say in a four ISP setup, is not available, ECMP will automatically distribute the load between the three other WANS.To approximate the same thing in PCC is way more complex in comparison.Where PCC comes into play is if there is much disparity between the ISPs in terms of throughput as the ECMP will not favour the larger throughput WAN and thus the available bandwidth will not be used in a reasonable proportion. With PCC you can modify the number of times in a cycle, the router goes to a specific WAN ( to ensure a larger bandwith ISP) sees more sessions compared to the lesser bandwidth ISPs. There is also some issues with banks needed to see sessions from the same ISP from a user etc........ Although it may be less of an issue now than before.One can achieve better load balancing granularity by bandwidth based load balancing but that is a step more complex than PCC........As per Tomas -A sticky connection• A sticky connection is a connection, that onceestablished through one interface, will always go outthat exact interface.• This is required, because when we switch to a secondlink, we only need to switch new connections.• In PCC, this is done automatically. Using bandwidth based load balancinghowever, this has to be done manually which implies a second layer of manglesOne then uses traffic monitoring to trigger an action above a certain traffic threshold --> move sessions to next WAN ( via changing the routing table by changing routing mark )Similarly one uses traffic monitoring to trigger an action below a certain traffic threshold ---> move sessions back to this WAN ( via changing the routing table by changing routing mark)What do you suggest now? What should I do? I don't want to replace the hex, I want to fix the problem.I consider this problem a cat and mouse game on the part of Mikrotik to buy a new device. ---

## Response 17
@MKX for the version 7 ECMP it uses L3 hash policy as depicted below.Can you explain these further??Is there a practical reason to consider L4 or L3 inner( what the heck is L3 inner) ( maybe one works better for consistent interactions with banks etc. ).....Screenshot 2025-01-25 131307.jpg ---

## Response 18
@MKX for the version 7 ECMP it uses L3 hash policy as depicted below.Can you explain these further??I don't have any experience or knowledge of ECMP. The terms you're asking about sound similar to some terms from (L2) bonding (which I believe I understand well enough), but I've no idea whether they are actually similar or not. So I'll pass this one. ---

## Response 19
What do you suggest now? What should I do? I don't want to replace the hex, I want to fix the problem.I consider this problem a cat and mouse game on the part of Mikrotik to buy a new device.Well the problem is not understanding the specifications available on the product pages or coming here to ask for assistance prior to purchasing.In either case there is no way around the limits of using the routers with firewall rules in place to 1gig or close to your ISP without acquiring the correct product.In your case the best approach is the hapax3, if budget is the issue.The hex you have makes an excellent managed switch you can use on your network and/or as a backup router and/or travel router................ ---

## Response 20
What do you suggest now? What should I do? I don't want to replace the hex, I want to fix the problem.I consider this problem a cat and mouse game on the part of Mikrotik to buy a new device.Well the problem is not understanding the specifications available on the product pages or coming here to ask for assistance prior to purchasing.In either case there is no way around the limits of using the routers with firewall rules in place to 1gig or close to your ISP without acquiring the correct product.In your case the best approach is the hapax3, if budget is the issue.The hex you have makes an excellent managed switch you can use on your network and/or as a backup router and/or travel router................As I said, in the country where I live, access to Mikrotik equipment is difficult. I had a question: does ecmp no longer work in version 7? ---

## Response 21
ECMP works very well in ROS7, works with fasttrack enabled and applicable to the connections using ECMP, and since 7.16 you can use the L4 mode (for both IPv4 and IPv6), and in my tests with L4, you achieve the same results as with PCC both-address-and-ports (when the PCC remainder distribution is equal, which means you don't give more weight to a particular outgoing route). Before 7.16 the only choice was L3 and it worked like PCC both-addresses. When using IPv6 you'll need srcnat netmap (NAT66) rules to change the prefixes to the correct one for each outgoing interfaces. Other than that, it also works very well with IPv6.For issue such as Incoming Wireguard connections, or generic port forwarding (dstnat), I've found that the following config simplified a lot, and most of the time mangle rules are no longer needed, only routing rules:* In the main routing table, keep the routes with increasing distance (failover mode, NOT ECMP). We'll let Wireguard and the port forwarded (dstnat) connections use this main table and not being load balanced (only use the main route).* Create an additional routing table named ECMP. In this table we add all the ECMP routes (with the same distance).* For the Routing Rules table:- First rule at the top (with this, connections between the router's subnets will use the main table):
```
/routing ruleaddaction=lookup min-prefix=0table=main- Followed by rules excluding dstnat hosts from ECMP by making them use the main routing table, as well as any other hosts/subnets that should skip ECMP:
```

```
/routing ruleaddaction=lookup dst-address=0.0.0.0/0src-address=a.b.c.d/32table=mainaddaction=lookup dst-address=0.0.0.0/0src-address=e.f.g.h/24table=main...- And the rules that tell the rest to use the ECMP table:
```

```
/routing ruleaddaction=lookup dst-address=0.0.0.0/0src-address=192.168.0.0/16table=ECMPaddaction=lookup dst-address=0.0.0.0/0src-address=172.16.0.0/12table=ECMPaddaction=lookup dst-address=0.0.0.0/0src-address=10.0.0.0/8table=ECMPaddaction=lookup dst-address=2000::/3 src-address=2000::/3table=ECMPIf you need more complexexclusion(from ECMP) conditions than a few exclusion addresses, you can ressort to mangle (because mangle has priority over routing rules). Create a separate routing table, WAN1_ONLY for example, with only one default route. Add rules to the Mangle table to mark-connection & mark-routing for specific conditions for WAN1_ONLY to be used. Then add connection-mark=no-mark to the fasttrack rules. That way most of the outgoing traffic will still use ECMP and fasttrack.The hEX RB750Gr3 with fasttrack can now with 7.18beta2 achieve over 900Mbps (919Mbps in my tests) download on speedtest.net usingIPv6test servers too. Attached is the result before and after enabling fasttrack for IPv6 in 7.18beta2 on the old hEX.

---
```

## Response 22
ECMP works very well in ROS7, works with fasttrack enabled and applicable to the connections using ECMP, and since 7.16 you can use the L4 mode (for both IPv4 and IPv6), and in my tests with L4, you achieve the same results as with PCC both-address-and-ports (when the PCC remainder distribution is equal, which means you don't give more weight to a particular outgoing route). Before 7.16 the only choice was L3 and it worked like PCC both-addresses. When using IPv6 you'll need srcnat netmap (NAT66) rules to change the prefixes to the correct one for each outgoing interfaces. Other than that, it also works very well with IPv6.For issue such as Incoming Wireguard connections, or generic port forwarding (dstnat), I've found that the following config simplified a lot, and most of the time mangle rules are no longer needed, only routing rules:* In the main routing table, keep the routes with increasing distance (failover mode, NOT ECMP). We'll let Wireguard and the port forwarded (dstnat) connections use this main table and not being load balanced (only use the main route).* Create an additional routing table named ECMP. In this table we add all the ECMP routes (with the same distance).* For the Routing Rules table:- First rule at the top (with this, connections between the router's subnets will use the main table):
```
/routing ruleaddaction=lookup min-prefix=0table=main- Followed by rules excluding dstnat hosts from ECMP by making them use the main routing table, as well as any other hosts/subnets that should skip ECMP:
```

```
/routing ruleaddaction=lookup dst-address=0.0.0.0/0src-address=a.b.c.d/32table=mainaddaction=lookup dst-address=0.0.0.0/0src-address=e.f.g.h/24table=main...- And the rules that tell the rest to use the ECMP table:
```

```
/routing ruleaddaction=lookup dst-address=0.0.0.0/0src-address=192.168.0.0/16table=ECMPaddaction=lookup dst-address=0.0.0.0/0src-address=172.16.0.0/12table=ECMPaddaction=lookup dst-address=0.0.0.0/0src-address=10.0.0.0/8table=ECMPaddaction=lookup dst-address=2000::/3 src-address=2000::/3table=ECMPIf you need more complexexclusion(from ECMP) conditions than a few exclusion addresses, you can ressort to mangle (because mangle has priority over routing rules). Create a separate routing table, WAN1_ONLY for example, with only one default route. Add rules to the Mangle table to mark-connection & mark-routing for specific conditions for WAN1_ONLY to be used. Then add connection-mark=no-mark to the fasttrack rules. That way most of the outgoing traffic will still use ECMP and fasttrack.The hEX RB750Gr3 with fasttrack can now with 7.18beta2 achieve over 900Mbps (919Mbps in my tests) download on speedtest.net usingIPv6test servers too. Attached is the result before and after enabling fasttrack for IPv6 in 7.18beta2 on the old hEX.No matter how hard I try, ecmp doesn't work for me. I don't know what the problem is.you have a telegram id ?

---
```

## Response 23
As shown in the picture, the ecmp flag has been added for gateways, but only the internet link is working. ---

## Response 24
ecmp It doesn't work properly, the speed is still limited with Fasttrack. ---

## Response 25
When downloading something from a single server/host, even with a download manager softwares the IP addresses on both ends of the connections are the same. To have the connections distributed over the multiple outgoing WAN links, you must ensure that IPv4 Multipath Hash Policy (under IP -> IP Settings) is set to L4 (there is a similar setting for IPv4 under IPv6 -> Settings too). With the default setting (L3) only the IP addresses are used to calculate the hashes, which means those connections all have the same hash and will only use one line. With L4, the port numbers will also be used in the calculation and the different connections to the same host will have different hash values. This is similar to the PCC modes both-addresses and both-addresses-and-ports.As for fasttrack: at the top of the IP -> Firewall -> Filter table there is a dummy rule created by fasttrack (with the comment "special dummy rule to show the fasttrack counters"). Select that rule and click "Reset Counters", then run you speed tests. Do you see that counter rapidly increasing during the tests and counting most of the speed test traffic? If not, there might be something with your firewall configuration and/or bridge configuration. If possible, make an export of your configuration with:
```
/exporthide-sensitive file=configDownload config.rsc to your computer, use a plaintext editor to censor things like MAC addresses, keys, usernames, public IP addresses, etc... (as well the sensitive data in the scripts, if any). Then post the censored content here maybe?

---
```

## Response 26
When downloading something from a single server/host, even with a download manager softwares the IP addresses on both ends of the connections are the same. To have the connections distributed over the multiple outgoing WAN links, you must ensure that IPv4 Multipath Hash Policy (under IP -> IP Settings) is set to L4 (there is a similar setting for IPv4 under IPv6 -> Settings too). With the default setting (L3) only the IP addresses are used to calculate the hashes, which means those connections all have the same hash and will only use one line. With L4, the port numbers will also be used in the calculation and the different connections to the same host will have different hash values. This is similar to the PCC modes both-addresses and both-addresses-and-ports.As for fasttrack: at the top of the IP -> Firewall -> Filter table there is a dummy rule created by fasttrack (with the comment "special dummy rule to show the fasttrack counters"). Select that rule and click "Reset Counters", then run you speed tests. Do you see that counter rapidly increasing during the tests and counting most of the speed test traffic? If not, there might be something with your firewall configuration and/or bridge configuration. If possible, make an export of your configuration with:
```
/exporthide-sensitive file=configDownload config.rsc to your computer, use a plaintext editor to censor things like MAC addresses, keys, usernames, public IP addresses, etc... (as well the sensitive data in the scripts, if any). Then post the censored content here maybe?# 2025-01-27 18:58:14 by RouterOS 7.17# model = RB750Gr3/ip pooladd name=dhcp_pool0 ranges=192.168.1.10-192.168.1.253/ip dhcp-serveradd address-pool=dhcp_pool0 interface=bridge1 lease-time=1d name=dhcp1/interface bridge portadd bridge=bridge1 interface=ether2 internal-path-cost=10 path-cost=10add bridge=bridge1 interface=ether4 internal-path-cost=10 path-cost=10add bridge=bridge1 interface=ether5add bridge=bridge1 interface=ether3add bridge=bridge1 interface=ether1/ip settingsset accept-redirects=yes accept-source-route=yes ipv4-multipath-hash-policy=\l4/ip addressadd address=192.168.1.2/24 interface=bridge1 network=192.168.1.0/ip firewall filteradd action=fasttrack-connection chain=forward hw-offload=yes src-address=\192.168.1.70add action=fasttrack-connection chain=forward hw-offload=yes src-address=\192.168.1.71add action=fasttrack-connection chain=forward hw-offload=yes src-address=\192.168.1.72add action=fasttrack-connection chain=forward hw-offload=yes src-address=\192.168.1.80add action=fasttrack-connection chain=forward hw-offload=yes src-address=\192.168.1.81add action=fasttrack-connection chain=forward hw-offload=yes src-address=\192.168.1.82/ip firewall natadd action=masquerade chain=srcnat/ip routeadd disabled=no distance=1 dst-address=0.0.0.0/0 gateway=192.168.1.1 \pref-src="" routing-table=main scope=30 suppress-hw-offload=no \target-scope=10add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=192.168.8.1 \pref-src="" routing-table=main scope=30 suppress-hw-offload=no \target-scope=10

---
```