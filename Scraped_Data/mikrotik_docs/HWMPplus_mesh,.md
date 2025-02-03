---
title: HWMPplus mesh
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/8978441/HWMPplus+mesh,
crawled_date: 2025-02-02T21:13:50.758190
section: mikrotik_docs
type: documentation
---

# Summary
```
/interface mesh
```
HWMP+ is a MikroTik specific layer-2 routing protocol for wireless mesh networks. It is based on Hybrid Wireless Mesh Protocol (HWMP) from IEEE 802.11s draft standard. It can be used instead of (Rapid) Spanning Tree protocols in mesh setups to ensure loop-free optimal routing.
The HWMP+ protocol however is not compatible with HWMP from IEEE 802.11s draft standard.
Note that the distribution system you use for your network need not be a Wireless Distribution System (WDS). HWMP+ mesh routing supports not only WDS interfaces but also Ethernet interfaces inside the mesh. So you can use a simple Ethernet-based distribution system, or you can combine both WDS and Ethernet links!
# Properties
## Mesh
Property | Description
----------------------
admin-mac(MAC address;Default: 00:00:00:00:00:00) | Administratively assigned MAC address, used when theauto-macsetting is disabled
arp(disabled | enabled | proxy-arp | reply-only; Default:enabled) | Address Resolution Protocol setting
auto-mac(boolean; Default:no) | If disabled, then the value fromadmin-macwill be used as the MAC address of the mesh interface; else address of some port will be used if ports are present
hwmp-default-hoplimit(integer: 1..255; Default: ) | Maximum hop count for generated routing protocol packets; after an HWMP+ packet is forwarded "hoplimit" times, it is dropped
hwmp-prep-lifetime(time; Default:5m) | Lifetime for routes created from received PREP or PREQ messages
hwmp-preq-destination-only(boolean; Default:yes) | Whether the only destination can respond to HWMP+ PREQ message
hwmp-preq-reply-and-forward(boolean; Default:yes) | Whether intermediate nodes should forward HWMP+ PREQ message after responding to it. Useful only whenhwmp-preq-destination-onlyis disabled
hwmp-preq-retries(integer; Default:2) | How many times to retry a route discovery to a specific MAC address before the address is considered unreachable
hwmp-preq-waiting-time(time; Default:4s) | How long to wait for a response to the first PREQ message. Note that for subsequent PREQs the waiting time is increased exponentially
hwmp-rann-interval(time; Default:10s) | How often to send out HWMP+ RANN messages
hwmp-rann-lifetime(time; Default:1s) | Lifetime for routes created from received RANN messages
hwmp-rann-propagation-delay(number; Default:0.5) | How long to wait before propagating a RANN message. Value in seconds
mesh-portal(boolean; Default:no) | Whether this interface is a portal in the mesh network
mtu(number; Default:1500) | Maximum transmission unit size
name(string; Default: ) | Interface name
reoptimize-paths(boolean; Default:no) | Whether to send out periodic PREQ messages asking for known MAC addresses. Turning on this setting is useful if the network topology is changing often. Note that if no reply is received to a re-optimization PREQ, the existing path is kept anyway (until it timeouts itself)
## Port
Property | Description
----------------------
active-port-type(read-only: wireless | WDS | ethernet-mesh | ethernet-bridge | ethernet-mixed; Default: ) | port type and state actually used
hello-interval(time; Default:10s) | the maximum interval between sending out HWMP+ Hello messages. Used only for Ethernet type ports
interface(interface name; Default: ) | interface name, which is to be included in a mesh
mesh(interface name; Default: ) | mesh interface this port belongs to
path-cost(integer: 0..65535; Default:10) | path cost to the interface, used by routing protocol to determine the 'best' path
port-type(WDS | auto | ethernet | wireless; Default: ) | port type to useauto - port type is determined automatically based on the underlying interface's typeWDS - a Wireless Distribution System interface. Remote MAC address is learned from wireless connection dataethernet - Remote MAC addresses are learned either from HWMP+ Hello messages or from source MAC addresses in received or forwarded trafficwireless - Remote MAC addresses are learned from wireless connection data
* auto - port type is determined automatically based on the underlying interface's type
* WDS - a Wireless Distribution System interface. Remote MAC address is learned from wireless connection data
* ethernet - Remote MAC addresses are learned either from HWMP+ Hello messages or from source MAC addresses in received or forwarded traffic
* wireless - Remote MAC addresses are learned from wireless connection data
## FDB Status
Property | Description
----------------------
mac-address(MAC address) | MAC address corresponding for this FDB entry
seq-number(integer) | sequence number used in routing protocol to avoid loops
type(integer) | sequence number used in routing protocol to avoid loops
interface(local | outsider | direct | mesh | neighbor | larval | unknown) | type of this FDB entrylocal -- MAC address belongs to the local router itselfoutsider -- MAC address belongs to a device external to the mesh networkdirect -- MAC address belongs to a wireless client on an interface that is in the mesh networkmesh -- MAC address belongs to a device reachable over the mesh network; it can be either internal or external to the mesh networkneighbor -- MAC address belongs to a mesh router that is a direct neighbor to this routerlarval -- MAC address belongs to an unknown device that is reachable over the mesh networkunknown -- MAC address belongs to an unknown device
mesh(interface name) | the mesh interface this FDB entry belongs to
on-interface(interface name) | mesh port used for traffic forwarding, kind of a next-hop value
lifetime(time) | time remaining to live if this entry is not used for traffic forwarding
age(time) | age of this FDB entry
metric(integer) | a metric value used by routing protocol to determine the 'best' path
* local -- MAC address belongs to the local router itself
* outsider -- MAC address belongs to a device external to the mesh network
* direct -- MAC address belongs to a wireless client on an interface that is in the mesh network
* mesh -- MAC address belongs to a device reachable over the mesh network; it can be either internal or external to the mesh network
* neighbor -- MAC address belongs to a mesh router that is a direct neighbor to this router
* larval -- MAC address belongs to an unknown device that is reachable over the mesh network
* unknown -- MAC address belongs to an unknown device
# Example
This example uses static WDS links that are dynamically added as mesh ports when they become active. Two different frequencies are used: one for AP interconnections, and one for client connections to APs, so the AP must have at least two wireless interfaces. Of course, the same frequency for all connections also could be used, but that might not work as well because of potential interference issues.
Repeat this configuration on all APs:
```
/interface mesh add disabled=no
/interface mesh port add interface=wlan1 mesh=mesh1
/interface mesh port add interface=wlan2 mesh=mesh1
 # interface used for AP interconnections 
/interface wireless set wlan1 disabled=no ssid=mesh frequency=2437 band=2ghz-b/g/n mode=ap-bridge \
 wds-mode=static-mesh wds-default-bridge=mesh1 
# interface used for client connections
 /interface wireless set wlan2 disabled=no ssid=mesh-clients frequency=5180 band=5ghz-a/n/ac mode=ap-bridge 
# a static WDS interface for each AP you want to connect to
/interface wireless wds add disabled=no master-interface=wlan1 name=<descriptive name of remote end> \
 wds-address=<MAC address of remote end>
```
Here WDS interface is added manually because static WDS mode is used. If you are usingwds-mode=dynamic-mesh, all WDS interfaces will be created automatically. Thefrequencyandbandparameters are specified here only to produce valid example configuration; mesh protocol operations are by no means limited to or optimized for, these particular values.
In real-world setups you also should take care of securing the wireless connections, using/interface wireless security-profile. For simplicity, that configuration is not shown here.
Results on router A (there is one client connected to wlan2):
```
[admin@A] > /interface mesh print
Flags: X - disabled, R - running
0 R name="mesh1" mtu=1500 arp=enabled mac-address=00:0C:42:0C:B5:A4 auto-mac=yes
admin-mac=00:00:00:00:00:00 mesh-portal=no hwmp-default-hoplimit=32
hwmp-preq-waiting-time=4s hwmp-preq-retries=2 hwmp-preq-destination-only=yes
hwmp-preq-reply-and-forward=yes hwmp-prep-lifetime=5m hwmp-rann-interval=10s
hwmp-rann-propagation-delay=1s hwmp-rann-lifetime=22s
[admin@A] > /interface mesh port print detail
Flags: X - disabled, I - inactive, D - dynamic
0 interface=wlan1 mesh=mesh1 path-cost=10 hello-interval=10s port-type=auto port-type-used=wireless
1 interface=wlan2 mesh=mesh1 path-cost=10 hello-interval=10s port-type=auto port-type-used=wireless
2 D interface=router_B mesh=mesh1 path-cost=105 hello-interval=10s port-type=auto port-type-used=WDS
3 D interface=router_D mesh=mesh1 path-cost=76 hello-interval=10s port-type=auto port-type-used=WDS
```
The FDB (Forwarding Database) at the moment contains information only about local MAC addresses, non-mesh nodes reachable through a local interface, and direct mesh neighbors:
```
[admin@A] /interface mesh fdb print
Flags: A - active, R - root
MESH TYPE MAC-ADDRESS ON-INTERFACE LIFETIME AGE
A mesh1 local 00:0C:42:00:00:AA 3m17s
A mesh1 neighbor 00:0C:42:00:00:BB router_B 1m2s
A mesh1 neighbor 00:0C:42:00:00:DD router_D 3m16s
A mesh1 direct 00:0C:42:0C:7A:2B wlan2 2m56s
A mesh1 local 00:0C:42:0C:B5:A4 2m56s
[admin@A] /interface mesh fdb print detail
Flags: A - active, R - root
A mac-address=00:0C:42:00:00:AA type=local age=3m21s mesh=mesh1 metric=0 seqnum=4294967196
A mac-address=00:0C:42:00:00:BB type=neighbor on-interface=router_B age=1m6s mesh=mesh1 metric=132 seqnum=4294967196
A mac-address=00:0C:42:00:00:DD type=neighbor on-interface=router_D age=3m20s mesh=mesh1 metric=79 seqnum=4294967196
A mac-address=00:0C:42:0C:7A:2B type=direct on-interface=wlan2 age=3m mesh=mesh1 metric=10 seqnum=0
A mac-address=00:0C:42:0C:B5:A4 type=local age=3m mesh=mesh1 metric=0 seqnum=0
```
Test if ping works:
```
[admin@A] > /ping 00:0C:42:00:00:CC
00:0C:42:00:00:CC 64 byte ping time=108 ms
00:0C:42:00:00:CC 64 byte ping time=51 ms
00:0C:42:00:00:CC 64 byte ping time=39 ms
00:0C:42:00:00:CC 64 byte ping time=43 ms
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 39/60.2/108 ms
```
Router A had to discover a path to Router C first, hence the slightly larger time for the first ping. Now the FDB also contains an entry for 00:0C:42:00:00:CC, with type "mesh".
Also, test that ARP resolving works and so does IP level ping:
```
[admin@A] > /ping 10.4.0.3
10.4.0.3 64 byte ping: ttl=64 time=163 ms
10.4.0.3 64 byte ping: ttl=64 time=46 ms
10.4.0.3 64 byte ping: ttl=64 time=48 ms
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 46/85.6/163 ms
```
### Mesh traceroute
There is also a mesh traceroute command, that can help you to determine which paths are used for routing.
For example, for this network:
```
[admin@1] /interface mesh fdb print
Flags: A - active, R - root
MESH TYPE MAC-ADDRESS ON-INTERFACE LIFETIME AGE
A mesh1 local 00:0C:42:00:00:01 7m1s
A mesh1 mesh 00:0C:42:00:00:02 wds4 17s 4s
A mesh1 mesh 00:0C:42:00:00:12 wds4 4m58s 1s
A mesh1 mesh 00:0C:42:00:00:13 wds4 19s 2s
A mesh1 neighbor 00:0C:42:00:00:16 wds4 7m1s
A mesh1 mesh 00:0C:42:00:00:24 wds4 18s 3s
```
Traceroute to 00:0C:42:00:00:12 shows:
```
[admin@1] /interface mesh traceroute mesh1 00:0C:42:00:00:12
ADDRESS TIME STATUS
00:0C:42:00:00:16 1ms ttl-exceeded
00:0C:42:00:00:02 2ms ttl-exceeded
00:0C:42:00:00:24 4ms ttl-exceeded
00:0C:42:00:00:13 6ms ttl-exceeded
00:0C:42:00:00:12 6ms success
```
# Protocol description
## Reactive mode
Router A wants to discover a path to C
Router C sends a unicast response to A
In reactive mode, HWMP+ is very much like AODV (Ad-hoc On-demand Distance Vector). All paths are discovered on-demand, by flooding Path Request (PREQ) message in the network. The destination node or some router that has a path to the destination will reply with a Path Response (PREP). Note that if the destination address belongs to a client, the AP this client is connected to will serve as a proxy for him (i.e. reply to PREQs on his behalf).
This mode is best suited for mobile networks, and/or when most of the communication happens between intra-mesh nodes.
## Proactive mode
The root announces itself by flooding RANN
Internal nodes respond with PREGs
In proactive mode, there are some routers configured as portals. In general, being a portal means that the router has interfaces to some other network, i.e. it is an entry/exit point to the mesh network.
The portals will announce their presence by flooding the Root Announcement (RANN) message in the network. Internal nodes will reply with a Path Registration (PREG) message. The result of this process will be routing trees with roots in the portal.
Routes to portals will serve as a kind of default route. If an internal router does not know the path to a particular destination, it will forward all data to its closest portal. The portal will then discover the path on behalf of the router if needed. The data afterward will flow through the portal. This may lead to sub-optimal routing unless the data is addressed to the portal itself or some external network the portals have interfaces to.
A proactive mode is best suited when most of the traffic goes between internal mesh nodes and a few portal nodes.
## Topology change detection
Data flow path
After the link disappears, an error is propagated upstream
HWMP+ uses Path Error (PERR) message to notify that a link has disappeared. The message is propagated to all upstream nodes up to the data source. The source on PERR reception restarts the path discovery process.
# FAQ
Q. How is this better than RSTP?
A. It gives you optimal routing. RSTP is only for loop prevention.
Q. How the route selection is done?
A. The route with the best metric is always selected after the discovery process. There is also a configuration option to periodically reoptimize already known routes.
Route metric is calculated as the sum of individual link metrics.
Link metric is calculated in the same way as for (R)STP protocols:
* For Ethernet links the metric is configured statically (same as for OSPF, for example).
* For WDS links the metric is updated dynamically depending on actual link bandwidth, which in turn is influenced by wireless signal strength, and the selected data transfer rate.
Currently, the protocol does not take into account the amount of bandwidth being used on a link, but that might be also used in the future.
Q. How is this better than OSPF/RIP/layer-3 routing in general?
A. WDS networks usually are bridged, not routed. The ability to self-configure is important for mesh networks, and routing generally requires much more configuration than bridging. Of course, you can always run any L3 routing protocol over a bridged network, but for mesh networks that usually makes little sense.
Q. What about performance/CPU requirements?
A. The protocol itself, when properly configured, will take much fewer resources than OSPF (for example) would. Data forwarding performance on an individual router should be close to that of bridging.
Q. How does it work together with existing mesh setups that are using RSTP?
A. The internal structure of an RSTP network is transparent to the mesh protocol (because mesh hello packets are forwarded inside the RSTP network). The mesh will see the path between two entry points in the RSTP network as a single segment. On the other hand, a mesh network is not transparent to the RSTP, since RSTP hello packets are not be forwarded inside the mesh network.(This is the behavior since v3.26)
Note that if you have a WDS link between two access points, then both ends must have the same configuration (either as ports in a mesh on both ends or as ports in a bridge interface on both ends).
You can also put a bridge interface as a mesh port (to be able to use a bridge firewall, for example).
Q. Can I have multiple entry/exit points to the network?
A. If the entry/exit points are configured as portals (i.e. proactive mode is used), each router inside the mesh network will select its closest portal and forward all data to it. The portal will then discover a path on behalf of the router if needed.
Q. How to control or filter mesh traffic?
A. At the moment the only way is to use a bridge firewall. Create a bridge interface, put the WDS interfaces and/or Ethernets in that bridge, and put that bridge in a mesh interface. Then configure bridge firewall rules.
To match MAC protocol used for mesh traffic encapsulation, use MAC protocol number 0x9AAA, and to match mesh routing traffic, use MAC protocol number 0x9AAB. Example:
```
interface bridge settings set use-ip-firewall=yes 
interface bridge filter add chain=input action=log mac-protocol=0x9aaa 
interface bridge filter add chain=input action=log mac-protocol=0x9aab
```
# Advanced topics
We all know that it's easy to make problematic layer-2 bridging or routing setups and it can be hard to debug them. (Compared to layer-3 routing setups.) So here are a few bad configuration examples that could create problems for you. Avoid them!
## Problematic example 1: Ethernet switch inside a mesh
Router A is outside the mesh, all the rest of the routers are inside. For routers B, C, D all interfaces are added as mesh ports.
Router A will not be able to communicate reliably with router C. The problem manifests itself when D is the designated router for Ethernet; if B takes this role, everything is OK. The main cause of the problem is MAC address learning on Ethernet switch.
Consider what happens when router A wants to send something to C. We suppose router A either knows or floods data to all interfaces. Either way, data arrives at the switch. The switch, not knowing anything about the destination's MAC address, forwards the data to both B and D.
What happens now:
* B receives the packet on a mesh interface. Since the MAC address is not local for B and B knows that he is not the designated router for the Ethernet network, he simply ignores the packet.
* D receives the packet on a mesh interface. Since the MAC address is not local for B and D is the designated router for the Ethernet network, he initiates the path discovery process to C.
After path discovery is completed, D has information that C is reachable over B. Now D encapsulates the packet and forwards it back to the Ethernet network. The encapsulated packet is forwarded by the switch, received and forwarded by B, and received by C. So far everything is good.
Now C is likely to respond to the packet. Since B already knows where A is, he will decapsulate and forward the reply packet. But now the switch will learn that the MAC address of C is reachable through B! That means, next time when something arrives from A addressed to C, the switch will forward dataonlyto B (and B, of course, will silently ignore the packet)!
In contrast, if B took up the role of a designated router, everything would be OK, because traffic would not have to go through the Ethernet switch twice.
Troubleshooting: either avoid such setup or disable MAC address learning on the switch. Note that on many switches that is not possible.
Also note that there will be no problem, if either:
* router A supports and is configured to use HWMP+;
* or Ethernet switch is replaced with a router that supports HWMP+ and has Ethernet interfaces added as mesh ports.
## Problematic example 2: wireless modes
Consider this (invalid) setup example:
Routers A and B are inside the mesh, router C: outside. For routers A and B all interfaces are added as mesh ports.
It is not possible to bridge wlan1 and wlan2 on router B now. The reason for this is pretty obvious if you understand how WDS works. For WDS communications four address frames are used. This is because for wireless multihop forwarding you need to know both the addresses of the intermediate hops, as well as the original sender and final receiver. In contrast, non-WDS 802.11 communication includes only three MAC addresses in a frame. That's why it's not possible to do multi-hop forwarding in station mode.
Troubleshooting: depends on what you want to achieve:
* If you want router C to act as a repeater either for wireless or Ethernet traffic, configure the WDS link between router B and router C, and run mesh routing protocol on all nodes.
* In other cases configure wlan2 on router B in AP mode and WLAN on router C in station mode.