# Thread Information
Title: Thread-203530
Section: RouterOS
Thread ID: 203530

# Discussion

## Initial Question
It appears that ROSv7 on ARM/ARM64 locks MPLS decapsulation to cpu0, resulting in a major bottleneck for MPLS/VPLS networks using ARM64 routers such as the CCR2004 and CCR2116.For example, on our network, we have CCR2004s as our core and site routers. When a device connected to a site router uploads traffic, throughput caps around 500-700 Mbps, cpu0 of the core router hits 95%+, and significant packet loss occurs. Download traffic is mostly unaffected by this issue.We have spoken to 3 other network operators who use VPLS and who are experiencing this. It is reproducible with both the CCR2116 and CCR2004.We recently interacted with an ISP that expressed frustration with the asymmetrical VPLS performance issues with the CCR2116/CCR2004 routers. They ended up switching to Arista for their core router, leaving their tower sites as CCR2116s. Interestingly, they are now able to pull nearly line rate (9800/9800 Mbps) over VPLS from the tower site CCRR2116s, whereas before they were limited to ~500 Mbps upload.Another ISP acquaintance tested and found that the single-core bottleneck occurs primarily during decapsulation, not during encapsulation.As a temporary workaround, we have overlaid VXLAN, which is correctly multi-threaded on ROSv7 for ARM/ARM64. However, fixing the MPLS/VPLS issue on ROSv7 for ARM64 would be ideal given all of MikroTik's flagship routers are ARM64.If you have experienced this issue, please chime in.Issue reported to MikroTik support on 12/06/2023 as SUP-136817. ---

## Response 1
That was me.Well, I was one ISP who spent some time tonight testing from a 2116 to a 1036 through two 2004's (as well as with another ISP's two 2004's from a 1036 the other night) and determined it was single-core on egress. (All boxes under test are on 7.13.2.)According to the WISP Talk Facebook discussion about this, someone else submitted a ticket about it a while back, but it appears yet to have been dealt with.Meanwhile, I also tested with CRS309's as VXLAN and VPLS encap/decap endpoints, and maxed out the CPU's with only 1200Mbps. But on those ARM boxes, it at least spread the load.I am certainly looking forward to hardware-offloaded MPLS and/or VXLAN. While I don't use either in my network (in any meaningful amount), I hope to be able to someday. ---

## Response 2
I have observed this behavior for all types of MPLS traffic (both VPLS and VPNv4) on both ARM (RB1100AHx4) and ARM64 (CCR2004) devices. It is interesting to note that if the interface to the MPLS core is a VLAN interface, the incoming VPNv4 traffic is distributed between two CPU cores in the CCR2004 (not so in the RB1100Hx4).I generated a case to Support for this behavior in the RB1100AHx4 [SUP-108967]. According to the 7.13 changelog, this behavior was improved (I have not been able to test it yet in production):*) ethernet - improved packet CPU core classifier for Alpine CPUs for non IPv4/IPv6 traffic;I suspect that this behavior is based on the fact that the hash that is responsible for distributing incoming traffic to the CPU between the different cores only analyzes the Ethernet header (source and destination MAC address) and the IP header (source and destination IP address). However, for VPLS traffic, the hash can only parse the Ethernet header (the IP header, if exists, is part of the MPLS payload). ---

## Response 3
This is quite interesting as this problem did not occur in RouterOS v6 ---

## Response 4
This is quite interesting as this problem did not occur in RouterOS v6This problem was also pesent in ROSv6. ---

## Response 5
I will add that even though it's single-core bound, the throughput on 2004 was still 8Gbps full duplex, or 9Gbps one-way (due to testing on 10Gbps ports, of course) with the router bridging an entire interface with the VPLS, routing it over the second to the second router, which passed the traffic back out on the first SFP+ port. No VLANs involved in my tests.One of the guys on WiSP Talk was running into 500Mbps limits in one direction with 2116's or 2216's in the core. Mine had no queues or filtering rules, so I'm wondering if there was some other stuff going on making it worse.My tests were also on the 16GBE version of the 2004, whereas other testing I did with another ISP was on the 12SFP+ version, which has its own set of quirks. We were running into limits around 3Gbps, which more closely matches limits I ran into when using that particular 2004 as a border BGP router with a handful of rules, no MPLS/VPLS. I couldn't push more than 3Gbps during speed tests, and finally swapped it out for a 2116, which handily passes whatever I throw at it before enabling L3HW offload. ---

## Response 6
The behavior I described above is on the CCR2004 with 12 SFP+ ports. ---

## Response 7
Very strange issue.I have a CCR2004 in production running VPLS as a PE router, and I'm unable to see single CPU core choking, CPU cores all are engaged pretty much evenly. Maybe it's config related?ROS version 7.12.1, firmware version 7.12.1 as well (if I use 7.13.x, it reboots every 15 minutes), I did 7.12.1 netinstall before racking this device and putting it to work, possibly that played a role in the issue/solution.Edit:After benchmarking thoroughly, same problem as everybody ---

## Response 8
90% to 100% on one core while the rest is 30% on CCR2116 ---

## Response 9
It seems that Mikrotik need to write a new software based MPLS data plane (FastPath module in Mikrotik terminology) that can distribute load across multiple cores.And while the code and protocols are fresh in the developers minds, having a VPLS FastPath module would be great too.I know that elsewhere on the forum there are discussions about MPLS Hardware Forwarding. This is very important for platforms like the CCR2216, CCR2116 and the CRS's but will be quite restricted in the label depth and number of VLAN TAG's that can be decapsulated. It will also not benefit any of the other Mikrotik platforms that are in widespread use within ISP's.In my opinion Mikrotik need both hardware accelerated forwarding and a software "FastPath" that can spread the load across multiple cores. ---

## Response 10
FastPath isn't going to cut it in 2024.They need to use DPDK/VPP for line-rate software dataplane. Maybe XDP for ingress filtering. ---

## Response 11
FastPath isn't going to cut it in 2024.They need to use DPDK/VPP for line-rate software dataplane. Maybe XDP for ingress filtering.They can use whatever they want, as long as it gets the job done. ---

## Response 12
MikroTik support asked me to try v7.14.1 to see if it resolved the VPLS issues. Unfortunately, it did not. 1200 Mbps is the most I can push between two CCR2116s. On the plus side, VXLAN is doing great, moving over 9Gbps between two CCR2116s. VXLAN seems to be the best bandaid solution for now until Mikrotik can implement multi-threaded MPLS/VPLS encap/decap. :/ ---

## Response 13
MikroTik support asked me to try v7.14.1 to see if it resolved the VPLS issues. Unfortunately, it did not. 1200 Mbps is the most I can push between two CCR2116s. On the plus side, VXLAN is doing great, moving over 9Gbps between two CCR2116s. VXLAN seems to be the best bandaid solution for now until Mikrotik can implement multi-threaded MPLS/VPLS encap/decap. :/Hey, was there any followup from Mikrotik on this ?I am about to need to roll out v7 for MPLS and this is concerning me. ---

## Response 14
I just tested it myself:rt1.test (CCR2216)--10G--rt1.mpls(CCR2004)---10G--rt2.mpls(CCR2004)---10G--rt2.test(CCR2216)vpls tunnel between rt1.mpls and rt2.mpls in a bridge towards the test system. That looks good to me.I just hope that in version 7.16 MPLS will work again in HW at least on the level of ROS6thanks, glueck ---

## Response 15
So , what I'm seeing here is CCR2004 as PE devices on each end, one CPU thread maxing out on encapsulation, and seems to be balanced CPU on decapsulation.Is that right??Even with the single thread you are still getting >9Gbps of throughput. ROS7.15This setup doesn't suffer from the bottlenecks that others are reporting earlier in the thread.Thanks ---

## Response 16
Any info about mpls/vpls single core issue?I have BGP router ccr2004 hw and 7.12 -> 7.15.2 made big improvement ->Sieppaa.JPG ---

## Response 17
The problem with MPLS/VPLS persists in 7.15.3. I have generated ticket [SUP-160859], but have not received a response yet. ---

## Response 18
Hi!Is there a problem with CPU load in LSR or only LER(PE) role? ---

## Response 19
Hi!Is there a problem with CPU load in LSR or only LER(PE) role?LER ---

## Response 20
I don't see why this behavior would not affect devices running as LSRs. I think that the ability to use MPLS Fastpath for label switching should significantly reduce CPU usage. ---

## Response 21
MPLS FastPath is used for label switching...Its only PE (LER) functions that are notcurrentlyhandled in FastPath.Low hanging fruit would be a VPLS FastPath module.Followed by L3 push/pop (L3VPN) FastPath module. This would be more work, but provide huge benefit for acceleration of L3 traffic end-to-end on ISP networks. ---

## Response 22
Hi!Is there a problem with CPU load in LSR or only LER(PE) role?LERThank you. ---

## Response 23
```
What's new in 7.17beta2 (2024-Sep-27 10:07):
*) mpls - added fast-path support for VPLS;And just like that we have VPLS FastPath.   It should bring about a massive performance increase.I am interested to hear how it performs in your labs and in the field.

---
```

## Response 24
Just tested vpls on CCR2004-1G-12S+2XS.Before mpls, just vlans bredged between 2 sfp ports: 3 gbps, cpu load 20-25%(common cpu load)with vpls:vpls, 7.16input(incapsulation), 3gbps 100%, 1core (cpu2)output(decapsulation), 3gbps 45-50%, 1core (cpu2)vpls, 7.17beta4: sameam i doing this wrong? Fast path counters did not grows.inputoutput ---

## Response 25
Guys, do you have any news on this topic? ---

## Response 26
Guys, do you have any news on this topic?Have you tried with RouterOS 7.17 ? (The GA release, not the RC) ---

## Response 27
Guys, do you have any news on this topic?Have you tried with RouterOS 7.17 ? (The GA release, not the RC)Tried just a minute ago and got same results, and vpls fast-patch counter on zeroes. I don`t understand how it should work. ---

## Response 28
Have you tried with RouterOS 7.17 ? (The GA release, not the RC)Tried just a minute ago and got same results, and vpls fast-patch counter on zeroes. I don`t understand how it should work.ok. i fooled myself. fast-path applies only on transit mpls packets, its for LSR or just switching(?)nothing to do here ---

## Response 29
That is only partly correct...MPLS FastPath applies to transit packets (P router) and decapsulation (PE router)VPLS FastPath which is available from 7.17 should apply to both encap/decap of packets on the PE router e.g. where the VPLS tunnel interface exists.Are you sure you do not have a configuration that is taking the traffic out of the FastPath ? ---

## Response 30
That is only partly correct...MPLS FastPath applies to transit packets (P router) and decapsulation (PE router)VPLS FastPath which is available from 7.17 should apply to both encap/decap of packets on the PE router e.g. where the VPLS tunnel interface exists.Are you sure you do not have a configuration that is taking the traffic out of the FastPath ?Yes. i get it. But i didnt find vpls fast-patch settings, Where is no documentation about it.config ---

## Response 31
If the VPLS interface is eligible for FastPath it will be enabled automatically. There is no switch for it.Post your config and I can tell you if you have anything that will make it ineligible for FastPath. ---

## Response 32
If the VPLS interface is eligible for FastPath it will be enabled automatically. There is no switch for it.Post your config and I can tell you if you have anything that will make it ineligible for FastPath.my config in previous answer: link to pastebin ---

## Response 33
In /mpls/settings you can disable/enable mpls fast path. You cannot disable/enable it only for VPLS tunnels. ---

## Response 34
In /mpls/settings you can disable/enable mpls fast path. You cannot disable/enable it only for VPLS tunnels.How can I check the effect of fast-path on the interface? Any counter or flag on interface maybe? ---