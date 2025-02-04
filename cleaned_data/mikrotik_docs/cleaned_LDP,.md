# Document Information
Title: LDP
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/121995275/LDP,

# Content
# Overview
MikroTik RouterOS implements Label Distribution Protocol (RFC 3036, RFC 5036, and RFC 7552) for IPv4 and IPv6 address families. LDP is a protocol that performs the set of procedures and exchange messages by which Label Switched Routers (LSRs) establish Label Switched Paths (LSPs) through a network by mapping network-layer routing information directly to data-link layer switched paths.
# Prerequisites for MPLS
# "Loopback" IP address
Although not a strict requirement, it is advisable to configure routers participating in the MPLS network with "loopback" IP addresses (not attached to any real network interface) to be used by LDP to establish sessions.
This serves 2 purposes:
In RouterOS "loopback" IP address can be configured by creating a dummy bridge interface without any ports and adding the address to it. For example:
```
/interface bridge add name=lo
/ip address add address=255.255.255.1/32 interface=lo
```
# IP connectivity
As LDP distributes labels for active routes, the essential requirement is properly configured IP routing. LDP by default distributes labels for active IGP routes (that is - connected, static, and routing protocol learned routes, except BGP).
For instructions on how to set up properly IGP refer to appropriate documentation sections:
LDP supports ECMP routes.
You should be able to reach any loopback address from any location of your network before continuing with the LDP configuration. Connectivity can be verified with the ping tool running from loopback address to loopback address.
# Example Setup
Let's consider that we have already existing four routers setup, with working IP connectivity.
```
(lo:111.111.111.1)       (lo:111.111.111.2)          (lo:111.111.111.3)         (lo:111.111.111.4)
|---------R1-----(111.11.0.0/24)-----R2-----(111.12.0.0/24)-----R3-----(111.13.0.0/24)-----R4---------|
```
# Ip Reachability
Not going deep into routing setup here is the quit export of the IP and OSPF configurations:
```
# R1
/interface bridge
add name=loopback
/ip address
add address=111.11.0.1/24 interface=ether2
add address=111.111.111.1 interface=loopback
/routing ospf instance
add name=default_ip4 router-id=111.111.111.1
/routing ospf area
add instance=default_ip4 name=backbone_ip4
/routing ospf interface-template
add area=backbone_ip4 dead-interval=10s hello-interval=1s networks=111.111.111.1
add area=backbone_ip4 dead-interval=10s hello-interval=1s networks=111.11.0.0/24
# R2
/interface bridge
add name=loopback
/ip address
add address=111.11.0.2/24 interface=ether2
add address=111.12.0.1/24 interface=ether3
add address=111.111.111.2 interface=loopback
/routing ospf instance
add name=default_ip4 router-id=111.111.111.2
/routing ospf area
add instance=default_ip4 name=backbone_ip4
/routing ospf interface-template
add area=backbone_ip4 dead-interval=10s hello-interval=1s networks=111.111.111.2
add area=backbone_ip4 dead-interval=10s hello-interval=1s networks=111.11.0.0/24
add area=backbone_ip4 dead-interval=10s hello-interval=1s networks=111.12.0.0/24
# R3
/interface bridge
add name=loopback
/ip address
add address=111.12.0.2/24 interface=ether2
add address=111.13.0.1/24 interface=ether3
add address=111.111.111.3 interface=loopback
/routing ospf instance
add name=default_ip4 router-id=111.111.111.3
/routing ospf area
add instance=default_ip4 name=backbone_ip4
/routing ospf interface-template
add area=backbone_ip4 dead-interval=10s hello-interval=1s networks=111.111.111.3
add area=backbone_ip4 dead-interval=10s hello-interval=1s networks=111.12.0.0/24
add area=backbone_ip4 dead-interval=10s hello-interval=1s networks=111.13.0.0/24
# R4
/interface bridge
add name=loopback
/ip address
add address=111.13.0.2/24 interface=ether2
add address=111.111.111.4 interface=loopback
/routing ospf instance
add name=default_ip4 router-id=111.111.111.4
/routing ospf area
add instance=default_ip4 name=backbone_ip4
/routing ospf interface-template
add area=backbone_ip4 dead-interval=10s hello-interval=1s networks=111.111.111.4
add area=backbone_ip4 dead-interval=10s hello-interval=1s networks=111.13.0.0/24
```
Verify that IP connectivity and routing are working properly
```
[admin@R4] /ip/address> /tool traceroute 111.111.111.1 src-address=111.111.111.4
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV
# ADDRESS        LOSS  SENT  LAST   AVG  BEST  WORST  STD-DEV
1  111.13.0.1     0%       4  0.6ms  0.6  0.6   0.6    0
2  111.12.0.1     0%       4  0.5ms  0.6  0.5   0.6    0.1
3  111.111.111.1  0%       4  0.6ms  0.6  0.6   0.6    0
```
# LDP Setup
In order to start distributing labels, LDP is enabled on interfaces that connect other LDP routers and not enabled on interfaces that connect customer networks.
On R1 it will look like this:
```
/mpls ldp
add afi=ip lsr-id=111.111.111.1 transport-addresses=111.111.111.1
/mpls ldp interface
add interface=ether2
```
Other routers are set up similarly.
R2:
```
/mpls ldp
add afi=ip lsr-id=111.111.111.2 transport-addresses=111.111.111.2
/mpls ldp interface
add interface=ether2
add interface=ether3
```
On R3:
```
/mpls ldp
add afi=ip lsr-id=111.111.111.3 transport-addresses=111.111.111.3
/mpls ldp interface
add interface=ether2
add interface=ether3
```
On R4:
```
/mpls ldp
add afi=ip lsr-id=111.111.111.4 transport-addresses=111.111.111.4
/mpls ldp interface
add interface=ether2
```
After LDP sessions are established, R2 should have two LDP neighbors:
```
[admin@R2] /mpls/ldp/neighbor> print
Flags: D, I - INACTIVE; O, T - THROTTLED; p - PASSIVE
Columns: TRANSPORT, LOCAL-TRANSPORT, PEER, ADDRESSES
# TRANSPORT      LOCAL-TRANSPORT  PEER             ADDRESSES
0 DO  111.111.111.1  111.111.111.2    111.111.111.1:0  111.11.0.1
111.111.111.1
1 DOp 111.111.111.3  111.111.111.2    111.111.111.3:0  111.12.0.2
111.13.0.1
111.111.111.3
```
The local mappings table shows what label is assigned to what route and peers the router have distributed labels to.
```
[admin@R2] /mpls/ldp/local-mapping> print
Flags: I - INACTIVE; D - DYNAMIC; E - EGRESS; G - GATEWAY; L - LOCAL
Columns: VRF, DST-ADDRESS, LABEL, PEERS
# VRF   DST-ADDRESS      LABEL      PEERS
0  D G  main  10.0.0.0/8       16         111.111.111.1:0
111.111.111.3:0
1 IDE L main  10.155.130.0/25  impl-null  111.111.111.1:0
111.111.111.3:0
2 IDE L main  111.11.0.0/24    impl-null  111.111.111.1:0
111.111.111.3:0
3 IDE L main  111.12.0.0/24    impl-null  111.111.111.1:0
111.111.111.3:0
4 IDE L main  111.111.111.2    impl-null  111.111.111.1:0
111.111.111.3:0
5  D G  main  111.111.111.1    17         111.111.111.1:0
111.111.111.3:0
6  D G  main  111.111.111.3    18         111.111.111.1:0
111.111.111.3:0
7  D G  main  111.111.111.4    19         111.111.111.1:0
111.111.111.3:0
8  D G  main  111.13.0.0/24    20         111.111.111.1:0
111.111.111.3:0
```
Remote mappings table on the other hand shows labels that are allocated for routes by neighboring LDP routers and advertised to this router:
```
[admin@R2] /mpls/ldp/remote-mapping> print
Flags: I - INACTIVE; D - DYNAMIC
Columns: VRF, DST-ADDRESS, NEXTHOP, LABEL, PEER
# VRF   DST-ADDRESS      NEXTHOP     LABEL      PEER
0 ID main  10.0.0.0/8                   16         111.111.111.1:0
1 ID main  10.155.130.0/25              impl-null  111.111.111.1:0
2 ID main  111.11.0.0/24                impl-null  111.111.111.1:0
3 ID main  111.12.0.0/24                17         111.111.111.1:0
4  D main  111.111.111.1    111.11.0.1  impl-null  111.111.111.1:0
5 ID main  111.111.111.2                19         111.111.111.1:0
6 ID main  111.111.111.3                20         111.111.111.1:0
7 ID main  111.111.111.4                21         111.111.111.1:0
8 ID main  111.13.0.0/24                18         111.111.111.1:0
9 ID main  0.0.0.0/0                    impl-null  111.111.111.3:0
10 ID main  111.111.111.2                16         111.111.111.3:0
11 ID main  111.111.111.1                18         111.111.111.3:0
12  D main  111.111.111.3    111.12.0.2  impl-null  111.111.111.3:0
13  D main  111.111.111.4    111.12.0.2  19         111.111.111.3:0
14 ID main  10.155.130.0/25              impl-null  111.111.111.3:0
15 ID main  111.11.0.0/24                17         111.111.111.3:0
16 ID main  111.12.0.0/24                impl-null  111.111.111.3:0
17  D main  111.13.0.0/24    111.12.0.2  impl-null  111.111.111.3:0
```
We can observe that router has received label bindings for all routes from both its neighbors - R1 and R3.
The remote mapping table will have active mappings only for the destinations that have direct next-hop, for example, let's take a closer look at 111.111.111.4 mappings. The routing table indicates that the network 111.111.111.4 is reachable via 111.12.0.2 (R3):
```
[admin@R2] /ip/route> print where dst-address=111.111.111.4
Flags: D - DYNAMIC; A - ACTIVE; o, y - COPY
Columns: DST-ADDRESS, GATEWAY, DISTANCE
DST-ADDRESS       GATEWAY            DISTANCE
DAo 111.111.111.4/32  111.12.0.2%ether3       110
```
And if we look again at the remote mapping table, the only active mapping is the one received from R3 with assigned label 19. This implies that when R2 when routing traffic to this network, will impose label 19.
```
17  D main  111.111.111.4    111.12.0.2  19         111.111.111.3:0
```
Label switching rules can be seen in the forwarding table:
```
[admin@R2] /mpls/forwarding-table> print
Flags: L, V - VPLS
Columns: LABEL, VRF, PREFIX, NEXTHOPS
# LABEL  VRF   PREFIX         NEXTHOPS
0 L    16  main  10.0.0.0/8     { nh=10.155.130.1; interface=ether1 }
1 L    18  main  111.111.111.3  { label=impl-null; nh=111.12.0.2; interface=ether3 }
2 L    19  main  111.111.111.4  { label=19; nh=111.12.0.2; interface=ether3 }
3 L    20  main  111.13.0.0/24  { label=impl-null; nh=111.12.0.2; interface=ether3 }
4 L    17  main  111.111.111.1  { label=impl-null; nh=111.11.0.1; interface=ether2 }
```
If we take a look at rule number 2, the rule says that when R2 received the packet with label 19, it will change the label to new label 19 (assigned by the R3).
As you can see from this example it is not mandatory that labels along the path should be unique.
Now if we look at the forwarding table of R3:
```
[admin@R3] /mpls/forwarding-table> print
Flags: L, V - VPLS
Columns: LABEL, VRF, PREFIX, NEXTHOPS
# LA  VRF   PREFIX         NEXTHOPS
0 L 19  main  111.111.111.4  { label=impl-null; nh=111.13.0.2; interface=ether3 }
1 L 17  main  111.11.0.0/24  { label=impl-null; nh=111.12.0.1; interface=ether2 }
2 L 16  main  111.111.111.2  { label=impl-null; nh=111.12.0.1; interface=ether2 }
3 L 18  main  111.111.111.1  { label=17; nh=111.12.0.1; interface=ether2 }
```
Rule number 0, shows that the out label is "impl-null". The reason for this is that R3 is the last hop before 111.111.111.4 will be reachable and there is no need to swap to any real label. It is known that R4 is the egress point for the 111.111.111.4 network (router is the egress point for directly connected networks because the next hop for traffic is not MPLS router), therefore it advertises the "implicit null" label for this route. This tells R3 to forward traffic for the destination 111.111.111.4/32 to R4 unlabelled, which is exactly what R3 forwarding table entry tells.
# Using traceroute in MPLS networks
RFC4950 introduces extensions to the ICMP protocol for MPLS. The basic idea is that some ICMP messages may carry an MPLS "label stack object" (a list of labels that were on the packet when it caused a particular ICMP message). ICMP messages of interest for MPLS are Time Exceeded and Need Fragment.
MPLS label carries not only label value, but also TTL field. When imposing a label on an IP packet, MPLS TTL is set to value in the IP header, when the last label is removed from the IP packet, IP TTL is set to value in MPLS TTL. Therefore MPLS switching network can be diagnosed by means of a traceroute tool that supports MPLS extension.
For example, the traceroute from R4 to R1 looks like this:
```
[admin@R1] /mpls/ldp/neighbor> /tool traceroute 111.111.111.4 src-address=111.111.111.1
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV, STATUS
# ADDRESS        LOSS  SENT  LAST   AVG  BEST  WORST  STD-DEV  STATUS
1  111.11.0.2     0%       2  0.7ms  0.7  0.7   0.7          0  <MPLS:L=19,E=0>
2  111.12.0.2     0%       2  0.4ms  0.4  0.4   0.4          0  <MPLS:L=19,E=0>
3  111.111.111.4  0%       2  0.5ms  0.5  0.5   0.5          0
```
Traceroute results show MPLS labels on the packet when it produced ICMP Time Exceeded. The above means: that when R3 received a packet with MPLS TTL 1, it had label 18 on it. This match advertised label by R3 for 111.111.111.4. In the same way, R2 observed label 17 on the packet on the next traceroute iteration - R3 switched label 17 to label 17, as explained above. R1 received packet without labels - R2 did penultimate hop popping as explained above.
# Drawbacks of using traceroute in MPLS network
# Label switching ICMP errors
One of the drawbacks of using traceroute in MPLS networks is the way MPLS handles produced ICMP errors. In IP networks ICMP errors are simply routed back to the source of the packet that caused the error. In an MPLS network, it is possible that a router that produces an error message does not even have a route to the source of the IP packet (for example in the case of asymmetric label switching paths or some kind of MPLS tunneling, e.g. to transport MPLS VPN traffic).
Due to this produced ICMP errors are not routed to the source of the packet that caused the error but switched further along the label switching path, assuming that when the label switching path endpoint will receive an ICMP error, it will know how to properly route it back to the source.
This causes the situation, that traceroute in MPLS network can not be used the same way as in IP network - to determine failure point in the network. If the label switched path is broken anywhere in the middle, no ICMP replies will come back, because they will not make it to the far endpoint of the label switching path.
# Penultimate hop popping and traceroute source address
A thorough understanding of penultimate hop behavior and routing is necessary to understand and avoid problems that penultimate hop popping causes to traceroute.
In the example setup, a regular traceroute from R5 to R1 would yield the following results:
```
[admin@R5] > /tool traceroute 9.9.9.1
ADDRESS                                    STATUS
1         0.0.0.0 timeout timeout timeout
2         2.2.2.2 37ms 4ms 4ms
mpls-label=17
3         9.9.9.1 4ms 2ms 11ms
```
compared to:
```
[admin@R5] > /tool traceroute 9.9.9.1 src-address=9.9.9.5
ADDRESS                                    STATUS
1         4.4.4.3 15ms 5ms 5ms
mpls-label=17
2         2.2.2.2 5ms 3ms 6ms
mpls-label=17
3         9.9.9.1 6ms 3ms 3ms
```
The reason why the first traceroute does not get a response from R3 is that by default traceroute on R5 uses source address 4.4.4.5 for its probes because it is the preferred source for a route over which next-hop to 9.9.9.1/32 is reachable:
```
[admin@R5] > /ip route print
Flags: X - disabled, A - active, D - dynamic,
C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme,
B - blackhole, U - unreachable, P - prohibit
# DST-ADDRESS        PREF-SRC        G GATEWAY         DISTANCE             INTERFACE
...
3 ADC  4.4.4.0/24         4.4.4.5                           0                    ether1
...
5 ADo  9.9.9.1/32                         r 4.4.4.3         110                  ether1
...
```
When the first traceroute probe is transmitted (source: 4.4.4.5, destination 9.9.9.1), R3 drops it and produces an ICMP error message (source 4.4.4.3 destination 4.4.4.5) that is switched all the way to R1. R1 then sends ICMP error back - it gets switched along the label switching path to 4.4.4.5.
R2 is the penultimate hop popping router for network 4.4.4.0/24 because 4.4.4.0/24 is directly connected to R3. Therefore R2 removes the last label and sends ICMP error to R3 unlabelled:
```
[admin@R2] > /mpls forwarding-table print
# IN-LABEL             OUT-LABELS           DESTINATION        INTERFACE            NEXTHOP
...
3 19                                        4.4.4.0/24         ether2               2.2.2.3
...
```
R3 drops the received IP packet because it receives a packet with its own address as a source address. ICMP errors produced by following probes come back correctly because R3 receives unlabelled packets with source addresses 2.2.2.2 and 9.9.9.1, which are acceptable to a route.
Command:
```
[admin@R5] > /tool traceroute 9.9.9.1 src-address=9.9.9.5
...
```
produces expected results, because the source address of traceroute probes is 9.9.9.5. When ICMP errors are traveling back from R1 to R5, the penultimate hop popping for the 9.9.9.5/32 network happens at R3, therefore it never gets to route packet with its own address as a source address.
# Optimizing label distribution
# Label binding filtering
During the implementation of the given example setup, it has become clear that not all label bindings are necessary. For example, there is no need to exchange IP route label bindings between R1 and R3 or R2 and R4, as there is no chance they will ever be used. Also, if the given network core is providing connectivity only for mentioned customer ethernet segments, there is no real use to distribute labels for networks that connect routers between themselves, the only routes that matter are /32 routes to endpoints or attached customer networks.
Label binding filtering can be used to distribute only specified sets of labels to reduce resource usage and network load.
There are 2 types of label binding filters:
```
/mpls ldp advertise-filter
```
```
/mpls ldp accept-filter
```
Filters are organized in the ordered list, specifying prefixes that must include the prefix that is tested against the filter and neighbor (or wildcard).
In the given example setup all routers can be configured so that they advertise labels only for routes that allow reaching the endpoints of tunnels. For this 2 advertise filters need to be configured on all routers:
```
/mpls ldp advertise-filter add prefix=111.111.111.0/24 advertise=yes
/mpls ldp advertise-filter add prefix=0.0.0.0/0 advertise=no
```
This filter causes routers to advertise only bindings for routes that are included by the 111.111.111.0/24 prefix which covers loopbacks (111.111.111.1/32, 111.111.111.2/32, etc). The second rule is necessary because the default filter results when no rule matches are to allow the action in question.
In the given setup there is no need to set up accept filter because by convention introduced by 2 abovementioned rules no LDP router will distribute unnecessary bindings.
Note that filter changes do not affect existing mappings, so to take the filter into effect, connections between neighbors need to be reset. either by removing neighbors from the LDP neighbor table or by restarting the LDP instance.
So on R2, for example, we get:
```
[admin@R2] /mpls/ldp/remote-mapping> print
Flags: I - INACTIVE; D - DYNAMIC
Columns: VRF, DST-ADDRESS, NEXTHOP, LABEL, PEER
# VRF   DST-ADDRESS    NEXTHOP     LABEL      PEER
0 ID main  111.111.111.2              17         111.111.111.3:0
1 ID main  111.111.111.1              16         111.111.111.3:0
2  D main  111.111.111.3  111.12.0.2  impl-null  111.111.111.3:0
3  D main  111.111.111.4  111.12.0.2  18         111.111.111.3:0
4 ID main  111.111.111.2              16         111.111.111.1:0
5  D main  111.111.111.1  111.11.0.1  impl-null  111.111.111.1:0
6 ID main  111.111.111.3              17         111.111.111.1:0
7 ID main  111.111.111.4              18         111.111.111.1:0
```
# LDP on Ipv6 and Dual-Stack links
RouterOS implements RFC 7552 to support LDP on dual-stack links.
Supported AFIs can be selected by LDP instance, as well as explicitly configured per LDP interface.
```
/mpls ldp
add afi=ip,ipv6 lsr-id=111.111.111.1 preferred-afi=ipv6
/mpls ldp interface
add interface=ether2 afi=ip
add interface=ether3 afi=ipv6
```
The example above enables LDP instance to use IPv4 and IPv6 address families and sets the preference to IPv6 withpreferred-afiparameter. LDP interface configuration on the other hand explicitly sets thatether2supports only IPv4 andether3supports only IPv6.
```
preferred-afi
```
The main question occurs how AFI is selected when there are a mix of different AFIs and what if one of the supported AFIs flaps.
The logic behind sending hellos is as follows:
From all received hellos peer determines which AFI to use for connection and for which AFIs to bind and send labels. For LDP to be able to use a specific AFI, receiving hello for that specific AFI is mandatory. Hello packet contains the transport address necessary for proper LDP operation. By comparing received AFI addresses, is determined active/passive role.
The logic behind receiving and processing hellos is as follows:
```
preferred-afi
```
If there are changes in hello packets, the existing session is terminated only in case if address family used by labels is changed, otherwise, the session is preserved.
Dual-stack element in hello packets is set only if an interface is determined to be dual-stack compatible:
In summary, the following combinations of AFIs and dual-stack element (ds6) are possible assuming that preferred-afi=ipv6:
# Property Reference
# LDP Instance
Sub-menu:/mpls
```
/mpls
```
Properties
Property | Description
----------------------
afi(ip | ipv6;Default:) | Determines supported address families by the instance.
comments(string; Default: ) | Short description of the entry
disabled(yes | no; Default:no) |
distribute-for-default(yes | no; Default:no) | Defines whether to map label for the default route.
hop-limit(integer[0..255]; Default: ) | Max hop limit used for loop detection. Works in combination with theloop-detectproperty.
loop-detect(yes | no; Default: ) | Defines whether to run LSP loop detection. Will not work correctly if not enabled on all LSRs. Should be used only on non-TTL networks such as ATMs.
lsr-id(IP; Default: ) | Unique label switching router's ID.
path-vector-limit(IP; Default: ) | Max path vector limit used for loop detection. Works in combination with theloop-detectproperty.
preferred-afi(ip | ipv6; Default:ipv6) | Determining which address family connection is preferred. Value is also set in dual-stack element (if used).
transport-addresses(IP; Default: ) | Specifies LDP session connections origin addresses and also advertises these addresses as transport addresses to LDP neighbors.
use-explicit-null(yes | no; Default:no) | Whether to distribute explicit-null label bindings.
vrf(name; Default: main) | Name of the VRF table this instance will operate on.
# Interface
Sub-menu:/mpls ldp interface
```
/mpls ldp interface
```
Property | Description
----------------------
afi(ip | ipv6;Default:) | Determines interface address family. Only AFIs that are configured as supported by the instance is taken into account. If the value is not explicitly specified then it is considered to be equal to the instance-supported AFIs.
accept-dynamic-neighbors(yes | no; Default:) | Defines whether to discover neighbors dynamically or use only statically configured inLDP neighbors menu
comments(string; Default: ) | Short description of the entry
disabled(yes | no; Default:no) |
hello-interval(string; Default: ) | The interval between hello packets that the router sends out on specified interface/s. The default value is 5s.
hold-time(string; Default: ) | Specifies the interval after which a neighbor discovered on the interface is declared as not reachable. The default value is 15s.
interface(string; Default: ) | Name of the interface or interface list where LDP will be listening.
transport-addresses(List ofIPs; Default: ) | Used transport addresses if differs from LDP Instance settings.
# Neighbors
Sub-menu:/mpls ldp neighbor
```
/mpls ldp neighbor
```
List of discovered and statically configured LDP neighbors.
Properties
Property | Description
----------------------
comments(string; Default: ) | Short description of the entry
disabled(yes | no; Default:no) |
send-targeted(yes | no; Default: ) | Specifies whether to try to send targeted hellos, used for targeted (not directly connected) LDP sessions.
transport(IP; Default: ) | Remote transport address.
Read-only Properties
Property | Description
----------------------
active-connect(yes | no) | Indicates that active role have been selected and the router is trying to establish the session.
addresses(list of IPs) | List of discovered addresses on the neighbor
inactive(yes | no) | Whether binding is active and can be selected as a candidate for forwarding.
dynamic(yes | no) | Whether entry was dynamically added
local-transport(IP) | Selected local transport address.
on-demand(yes | no) | Downstream On Demand label distribution
operational(yes | no) | Indicates whether the peer is operational.
passive(yes | no) | Indicates whether the peer is in a passive role.
passive-wait(yes | no) | Indicates whether the peer is in a passive role and currently is waiting for the session to be initialized.
path-vector-limit(integer) |
peer(IP:integer) | LSR-ID and label space of the neighbor
sending-targeted-hello(yes | no) | Whether targeted hellos are being sent to the neighbor.
throttled(yes | no) | Indicates whether session is in throttled state. Session is throttled after initialization failure, max throttle time 120s.
used-afi(yes | no) | Used transport AFI
vpls(yes | no) | Whether neighbor is used by VPLS tunnel
Downstream On Demand label distribution
# Accept Filter
Sub-menu:/mpls ldp accept-filter
```
/mpls ldp accept-filter
```
List of label bindings that should be accepted from LDP neighbors.
Property | Description
----------------------
accept(yes | no; Default:no) | Whether to accept label bindings from the neighbors for the specified prefix.
comments(string; Default: ) | Short description of the entry
disabled(yes | no; Default:no) |
neighbor(string; Default: ) | Neighbor to which this filter applies.
prefix(IP/mask; Default: ) | Prefix to match.
vrf(name; Default: ) |
# Advertise Filter
Sub-menu:/mpls ldp advertise-filter
```
/mpls ldp advertise-filter
```
List of label bindings that should be advertised to LDP neighbors.
Property | Description
----------------------
advertise(yes | no; Default:no) | Whether to advertise label bindings to the neighbors for the specified prefix.
comments(string; Default: ) | Short description of the entry
disabled(yes | no; Default:no) |
neighbor(string; Default: ) | Neighbor to which this filter applies.
prefix(IP/mask; Default: ) | Prefix to match.
vrf(name; Default: ) |
# Local Mapping
Sub-menu:/mpls local-mapping
```
/mpls local-mapping
```
This sub-menu shows labels bound to the routes locally in the router. In this menu also static mappings can be configured if there is no intention to use LDP dynamically.
Properties
Property | Description
----------------------
comments(string; Default: ) | Short description of the entry
disabled(yes | no; Default:no) |
dst-address(IP/Mask; Default: ) | Destination prefix the label is assigned to.
label(integer[0..1048576] | alert | expl-null | expl-null6 | impl-null | none; Default: ) | Label number assigned to destination.
vrf(name; Default: main) | Name of the VRF table this mapping belongs to.
Read-only Properties
Property | Description
----------------------
adv-path() |
inactive(yes | no) | Whether binding is active and can be selected as a candidate for forwarding.
dynamic(yes | no) | Whether entry was dynamically added
egress(yes | no) |
gateway(yes | no) | Whether the destination is reachable through the gateway.
local(yes | no) | Whether the destination is locally reachable on the router
peers(IP:label_space) | IP address and label space of the peer to which this entry was advertised.
# Remote Mapping
Sub-menu:/mpls remote-mapping
```
/mpls remote-mapping
```
Sub-menu shows label bindings for routes received from other routers. Static mapping can be configured if there is no intention to use LDP dynamically. This table is used to buildForwarding Table
Properties
Property | Description
----------------------
comments(string; Default: ) | Short description of the entry
disabled(yes | no; Default:no) |
dst-address(IP/Mask; Default: ) | Destination prefix the label is assigned to.
label(integer[0..1048576] | alert | expl-null | expl-null6 | impl-null | none; Default: ) | Label number assigned to destination.
nexthop(IP; Default:) |
vrf(name; Default: main) | Name of the VRF table this mapping belongs to.
Read-only Properties
Property | Description
----------------------
inactive(yes | no) | Whether binding is active and can be selected as a candidate for forwarding.
dynamic(yes | no) | Whether entry was dynamically added
path(string) |