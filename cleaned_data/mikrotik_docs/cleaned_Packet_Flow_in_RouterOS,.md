# Document Information
Title: Packet Flow in RouterOS
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328227/Packet+Flow+in+RouterOS,

# Content
# 1Understanding Packet Flow1.1Overall Packetflow Diagram1.1.1Chains1.2Flow of Routed Packet1.2.1Forward1.2.2Input1.2.3Output1.3Flow of Bridged Packet1.3.2Bridge Forward1.3.3Bridge Input1.3.4Bridge Output1.3.5Forward With Firewall Enabled1.4Flow of Hardware Offloaded Packet1.4.1Switch Forward1.4.2Switch to CPU Input1.4.3CPU Output to Switch1.5Flow of MPLS Packet1.5.1Pop Label1.5.2Switch Label1.5.3Push Label1.6MPLS IP VPN1.7Logical Interfaces1.8IPSec Policies2Fast Path2.1How Fast Path Works3FastTrack3.1Configuration example: excluding specific host, from being Fast-Tracked3.2Requirements4Packet flow for the visually impairedUnderstanding Packet Flow
More advanced firewall setups, or complicated tasks, such as traffic prioritization, routing policies, where it is necessary to utilize more than one RouterOS facility, require knowledge: How do these facilities work together? What happens when and why?
RouterOS packet flow diagram and flow examples will try to answer these questions.
It would be very complicated to represent what is going on with the packet in one diagram, therefore a packet flow diagram is divided into three parts:
# Overall Packetflow Diagram
Let's look at the overall diagram. It looks complicated at first, but after we go through the diagram with examples it will become much clearer.
There are 4 boxes in the center of the diagram: Bridging, Routing, Mpls decisions, and local router processes. So for example, if the packet needs to be routed over the router, a packet will flow as illustrated in the image below. Without looking deeper into each facility, the packet enters the in-interface, the router determines that it is IP traffic and needs to be routed, the packet goes through all routing processes and exits the out-interface.
Let's take a look at another example that will illustrate what happens if the packet's destination is a router. For example, the in-interface receives ICMP (ping) packet, its destination is the router itself, so the packet will go forlocal-inprocessing. After the packet is processed ICMP (ping) reply is generated inside the router(local-outprocessing) and will be sent out over the out-interface.
A simple explanation of each box before we go further with examples:
Now it is time to take a deeper look at what is happening inside bridging, MPLS, and routing flows.
A simple explanation of each box before we go further with examples:
```
vlan-filtering=yes
```
# Chains
RouterOS consist of a few default chains. These chains allow you to filter packets at various points:
Each of the prerouting, input, forward, output, and postrouting blocks contains even more facilities, which are illustrated in the third part of the packet flow diagram:
A simple explanation of each box before we go further with examples:
# Flow of Routed Packet
# Forward
Now, let's take our first example where the packet gets routed over the router and look deeper through what facilities packet goes:
We already learned that packet goes into the in-interface, the router determines that it is an IP packet and needs to be routed, and here starts the complicated process:
# Input
We already learned that packet goes into the in-interface, the router determines that it is an IP packet and needs to be routed, and here starts the complicated process:
# Output
Or when a packet is originated from the router (routing output):
# Flow of Bridged Packet
Below is discussed a general bridging process in RouterOS. Most of the packets will always follow the same processing path, but in certain configurations (e.g. with enabled VLAN filtering, horizon, STP, DHCP, or IGMP snooping) some packets can be treated differently. Please visit the bridging manual for more specific information.
# Bridge Forward
Bridge forward is a process that takes place when a packet is forwarded from one bridge port to another, essentially connecting multiple devices on the same network. After receiving a packet on the in-interface, the device determines that the in-interface is a bridge port, so it gets passed through the bridging process:
```
vlan-filtering=yes
```
# Bridge Input
Bridge input is a process that takes place when a packet is destined for the bridge interface. Most commonly this happens when you need to reach some services that are running on the bridge interface (e.g. a DHCP server) or you need to route traffic to other networks. The very first steps are similar to the bridge forward process - after receiving a packet on the in-interface, the device determines that the in-interface is a bridge port, so it gets passed through the bridging process:
# Bridge Output
Bridge output is a process that takes place when a packet should exit the device through one or multiple bridge ports. Most commonly this happens when a bridge interface itself tries to reach a device connected to a certain bridge port (e.g. when a DHCP server running on a bridge interface is responding to a DHCP client). After a packet is processed on other higher-level RouterOS processes and the device finally determines that the output interface is a bridge, the packet gets passed through the bridging process:
# Forward With Firewall Enabled
In certain network configurations, you might need to enable additional processing on routing chains for bridged traffic, for example, to use simple queues or an IP firewall. This can be done when the use-ip-firewall is enabled under the bridge settings. Note that additional processing will consume more CPU resources to handle these packets. All the steps were already discussed in previous points, below is a recap:
# Flow of Hardware Offloaded Packet
On the previous topic, we solely discussed a software bridging that requires the main CPU processing to forward packets through the correct bridge port. Most of the MikroTik devices are equipped with dedicated switching hardware, the so-called switch chip or switch ASIC. This allows us to offload some of the bridging functions, like packet forwarding between bridge ports or packet filtering, to this specialized hardware chip without consuming any CPU resources. In RouterOS, we have named this function Bridge Hardware (HW) Offloading. Different MikroTik devices might have different switch chips and each chip has a different set of features available, so make sure to visit this article to get more details -Bridge Hardware Offloading.
The hardware offloading, however, does not restrict a device to only hardware limited features, rather it is possible to take advantage of the hardware and software processing at the same time. This does require a profound understanding of how packets travel through the switch chip and when exactly they are passed to the main CPU.
# Switch Forward
We will further discuss a packet flow when bridge hardware offloading is enabled and a packet is forwarded between two switched ports on a single switch chip. This is the most common and also the simplest example:
# Switch to CPU Input
This process takes place when a packet is received on a physical interface and it is destined to switch-cpu port for further software processing. There are two paths to the switch-cpu. One where hardware offloading and switching is not even used (e.g. a standalone interface for routing or a bridged interface but with deliberately disabled HW offloading), so the packet is simply passed further for software processing. Another path is taken when hardware offloading is active on the in-interface. This will cause the packet to pass through the switching decision and there are various reasons why the switch might forward the packet to the switch-cpu port:
See the packet walkthrough when an in-interface is hardware offloaded:
# CPU Output to Switch
This process takes place when a packet exits the RouterOS software processing and is received on the switch-cpu port. Again, there are two paths the packet can take. One where hardware offloading and switching are not even used (e.g. a standalone interface for routing or a bridged interface but with deliberately disabled HW offloading), so the packet is simply sent out through the physical out-interface. Another path is taken when hardware offloading is active on the out-interface. This will cause the packet to pass through the switching decision. Just like any other switch port, the switch will learn the source MAC addresses from packets that are received on the switch-cpu port. This does come in handy when a bridge contains HW and non-HW offloaded interfaces, so the switch can learn which frames should be forwarded to the CPU. See the packet walkthrough when an out-interface is hardware offloaded:
# Flow of MPLS Packet
# Pop Label
# Switch Label
# Push Label
# MPLS IP VPN
In VPNv4 setups packet arriving at PE router that needs to be forwarded to the CE router is not a typical "forward".
If incoming label and destination is bound to the VRF Then after MPLS label is popped and:
For example traffic from src:111.15.0.1 to dst:111.13.0.1
```
[admin@CCR2004_2XS] /mpls/forwarding-table> print
Flags: L - LDP, P - VPN
Columns: LABEL, VRF, PREFIX, NEXTHOPS
# LABEL  VRF      PREFIX         NEXTHOPS
0 P    17  myVrf    111.13.0.0/24
4 L    20  main     203.0.113.2    { label=impl-null; nh=111.11.0.1; interface=sfp-sfpplus1 }
[admin@CCR2004_2XS] /mpls/forwarding-table>
...
[admin@CCR2004_2XS] /ip/route> print detail
Flags: D - dynamic; X - disabled, I - inactive, A - active; c - connect, s - static, r - rip, b - bgp, o - ospf, i - is-is, d - dhcp, v - vpn, m - modem, y - bgp-mpls-vpn;
H - hw-offloaded; + - ecmp
DAc   dst-address=111.11.0.0/24 routing-table=main gateway=sfp-sfpplus1 immediate-gw=sfp-sfpplus1 distance=0 scope=10 suppress-hw-offload=no
local-address=111.11.0.2%sfp-sfpplus1
DAc   dst-address=203.0.113.1/32 routing-table=main gateway=lo immediate-gw=lo distance=0 scope=10 suppress-hw-offload=no local-address=203.0.113.1%lo
DAo   dst-address=203.0.113.2/32 routing-table=main gateway=111.11.0.1%sfp-sfpplus1 immediate-gw=111.11.0.1%sfp-sfpplus1 distance=110 scope=20 target-scope=10
suppress-hw-offload=no
DAc   dst-address=111.13.0.0/24 routing-table=myVrf gateway=sfp-sfpplus2@myVrf immediate-gw=sfp-sfpplus2 distance=0 scope=10 suppress-hw-offload=no
local-address=111.13.0.2%sfp-sfpplus2@myVrf
DAy   dst-address=111.15.0.0/24 routing-table=myVrf gateway=203.0.113.2 immediate-gw=111.11.0.1%sfp-sfpplus1 distance=200 scope=40 target-scope=30 suppress-hw-offload=no [admin@CCR2004_2XS] /ip/route>
```
Packet will be seen in the output and postrouting chains, because now it is locally originated packet with source MAC address equal to vrfInterface:
```
08:10:55 firewall,info output: in:(unknown 0) out:sfp-sfpplus2, connection-state:established src-mac f2:b5:e9:17:18:3b, proto ICMP (type 8, code 0), 111.15.0.1->111.13.0.1, len 56
08:10:55 firewall,info postrouting: in:myVrf out:sfp-sfpplus2, connection-state:established src-mac f2:b5:e9:17:18:3b, proto ICMP (type 8, code 0), 111.15.0.1->111.13.0.1, len 56
```
On the other hand, for packets routed in the direction CE→PE will be seen in the "forward" as any other routed IP traffic before being sent to the MPLS:
```
08:10:55 firewall,info prerouting: in:sfp-sfpplus2 out:(unknown 0), connection-state:established src-mac dc:2c:6e:46:f8:93, proto ICMP (type 0, code 0), 111.13.0.1->111.15.0.1, len 56
08:10:55 firewall,info forward: in:sfp-sfpplus2 out:sfp-sfpplus1, connection-state:established src-mac dc:2c:6e:46:f8:93, proto ICMP (type 0, code 0), 111.13.0.1->111.15.0.1, len 56
08:10:55 firewall,info postrouting: in:sfp-sfpplus2 out:sfp-sfpplus1, connection-state:established src-mac dc:2c:6e:46:f8:93, proto ICMP (type 0, code 0), 111.13.0.1->111.15.0.1, len 56
```
But there can be an exception. If destination IP of reply packet is local to the router and connection tracking is performing NAT translation then connection tracking will "force" packet to move through the firewall prerouting/forward/postrouting chains.
# Logical Interfaces
So far we looked at examples when in or out interfaces are actual physical interfaces (Ethernet, wireless), but how packets will flow if the router receives tunnel encapsulated packets?
Let's assume that there is an IPIP packet coming into the router. Since it is a regular ipv4 packet it will be processed through all routing-related facilities ( until "J" in the diagram). Then the router will look if the packet needs to be decapsulated., in this case, it is an IPIP packet so "yes" send the packet to decapsulation. After that packet will go another loop through all the facilities but this time as a decapsulated IPv4 packet.
It is very important because the packet actually travels through the firewall twice, so if there is a strict firewall, then there should be "accept" rules for IPIP encapsulated packets as well as decapsulated IP packets.
# IPSec Policies
Let's take a look at another tunnel type - IPSec. This type of VPN does not have logical interfaces but is processed in a similar manner.
# Fast Path
From what we learned so far, it is quite obvious that such packet processing takes a lot of CPU resources. To fast things up FastPath was introduced in the first RouterOS v6. What it does is it skips processing in the Linux kernel, basically trading some RouterOS functionality for performance. For FastPath to work, interface driver support and specific configuration conditions are required.
# How Fast Path Works
FastPath is an interface driver extension, that allows a driver to talk directly to specific RouterOS facilities and skip all others.
The packet can be forwarded by a fast path handler only if at least the source interface supports a fast path. For complete fast-forwarding, destination interface support is also required.
Currently, RouterOS has the following FastPath handlers:
IPv4 FastPath handler is used if the following conditions are met:
```
/ip route vrf
```
```
/ip hotspot
```
```
/tool mac-scan
```
```
/tool ip-scan
```
Traffic Generator automatically use FastPath if the interface supports this feature.
Currently, MPLS fast-path applies to MPLS switched traffic (frames that enter router as MPLS and must leave router as MPLS) and VPLS endpoint that do VPLS encap/decap. Other MPLS ingress and egress will operate as before.
A Bridge handler is used if the following conditions are met:
Interfaces that support FastPath:
RouterBoard | Interfaces
------------------------
RB6xx series | ether1,2
RB800 | ether1,2
RB1100 series | ether1-11
All devices | Ethernet interfaces
wireless interfaces
bridge interfaces
VLAN, VRRP interfaces
bonding interfaces (RX only)
PPPoE, L2TP interfaces
EoIP, GRE, IPIP, VXLAN interfaces.
VPLS (starting from v7.17)
EoIP, Gre, IPIP, VXLAN and L2TP interfaces have per-interface settingallow-fast-path.Allowing a fast path on these interfaces has a side effect of bypassing firewall, connection tracking, simple queues, queue tree with parent=global, IP accounting, IPsec, hotspot universal client, vrf assignment for encapsulated packets that go through a fast-path. Also, packet fragments cannot be received in FastPath.
Only interface queue that guarantees FastPath is only-hardware-queue. If you need an interface queue other than hardware then the packet will not go fully FastPath, but there is not a big impact on performance, as "interface queue" is the last step in the packet flow.
The packet may go Half-FastPath by switching from FastPath to SlowPath, but not the other way around. So, for example, if the receiving interface has FastPath support, but the out interface does not, then the router will process the packet by FastPath handlers as far as it can and then proceed with SlowPath. If the receiving interface does not support FastPath but the out interface does, the packet will be processed by SlowPath all the way through the router.
# FastTrack
Fasttrack can be decoded as Fast Path + Connection Tracking. It allows marking connections as "fast-tracked", marking packets that belong to fast-tracked connection will be sent fast-path way. The connection table entry for such a connection now will have a fast-tracked flag.
To mark a connection as fast-tracked new action was implemented "fasttrack-connection"for firewall filter and mangle. Currently, only IPv4 TCP and UDP connections can be fast-tracked and to maintain connection tracking entries some random packets will still be sent to a slow path. This must be taken into consideration when designing firewalls with enabled "fasttrack".
FastTrack handler also supports source and destination NAT, so special exceptions for NATed connections are not required.
The easiest way to start using this feature on home routers is to enable "fasttrack" for allestablished, relatedconnections:
```
/ip firewall filter
add chain=forward action=fasttrack-connection connection-state=established,related \
comment="fasttrack established/related"
add chain=forward action=accept connection-state=established,related \
comment="accept established/related"
```
Notice that the first rule marks established/related connections as fast-tracked, the second rule is still required to accept packets belonging to those connections. The reason for this is that, as was mentioned earlier, some random packets from fast-tracked connections are still sent the slow pathway and only UDP and TCP are fast-tracked, but we still want to accept packets for other protocols.
After adding the "FastTrack" rule special dummy rule appeared at the top of the list. This is not an actual rule, it is for visual information showing that some of the traffic is traveling FastPath and will not reach other firewall rules.
These rules appear as soon as there is at least one fast-tracked connection tracking entry and will disappear after the last fast-tracked connection times out in the connection table.
# Configuration example: excluding specific host, from being Fast-Tracked
```
/ip firewall filter
add action=accept chain=forward connection-state=established,related src-address=192.168.88.111
add action=accept chain=forward connection-state=established,related dst-address=192.168.88.111
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=no
add action=accept chain=forward connection-state=established,related
```
In this example, we exclude host 192.168.88.111, from being Fast-tracked, by first accepting it with the firewall rule, both for source and destination. The idea is - not allowing the traffic to reach the FastTrack action.
Note: the "exclusion" rules, must be placed before fasttrack filters, order is important.
# Requirements
IPv4 FastTrack is active if the following conditions are met:
# Packet flow for the visually impaired
The following document in DOCX format describes the diagram in a way optimized for visually impaired people. The descriptions are by Apex CoVantage care of Benetech. They are not being updated.
* Packet flow, optimized document.