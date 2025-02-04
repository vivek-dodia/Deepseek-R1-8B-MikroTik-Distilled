# Document Information
Title: OSPF
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/9863229/OSPF,

# Content
# Overview
OSPF is Interior Gateway Protocol (IGP) designed to distribute routing information between routers belonging to the same Autonomous System (AS).
The protocol is based on link-state technology that has several advantages over distance-vector protocols such as RIP:
However, there are a few disadvantages:
RouterOS implements the following standards:
# OSPF Terminology
Before we move on let's familiarise ourselves with terms important for understanding the operation of the OSPF. These terms will be used throughout the article.
# Basic Configuration Example
To start OSPF v2 and v3 instances, the first thing to do is to add the instance and the backbone area:
```
/routing ospf instance
add name=v2inst version=2 router-id=1.2.3.4
add name=v3inst version=3 router-id=1.2.3.4
/routing ospf area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=backbone_v3 area-id=0.0.0.0 instance=v3inst
```
At this point, we can add a template. The template is used to match interfaces on which OSPF should be running, it can be done either by specifying the network or interface directly.
```
/routing ospf interface-template
add networks=192.168.0.0/24 area=backbone_v2
add networks=2001:db8::/64 area=backbone_v3
add interfaces=ether1 area=backbone_v3
```
# Routing Table Calculation
Link state database describes the routers and links that interconnect them and are appropriate for forwarding. It also contains the cost (metric) of each link. This metric is used to calculate the shortest path to the destination network.Each router can advertise a different cost for the router's own link direction, making it possible to have asymmetric links (packets to the destination travel over one path, but the response travels a different path). Asymmetric paths are not very popular, because it makes it harder to find routing problems.The value of the cost can be changed in theOSPF interface template configuration menu, for example, to add an ether2 interface with a cost of 100:
```
/routing ospf interface-template
add interfaces=ether2 cost=100 area=backbone_v2
```
The cost of an interface on Cisco routers is inversely proportional to the bandwidth of that interface. A higher bandwidth indicates a lower cost. If similar costs are necessary on RouterOS, then use the following formula:
Cost = 100000000/bw in bps.
OSPF router is using Dijkstra's Shortest Path First (SPF) algorithm to calculate the shortest path. The algorithm places the router at the root of a tree and calculates the shortest path to each destination based on the cumulative cost required to reach the destination. Each router calculates its own tree even though all routers are using the same link-state database.
# SPT Calculation
Assume we have the following network. The network consists of 4(four) routers. OSPF costs for outgoing interfaces are shown near the line that represents the link. In order to build the shortest-path tree for router R1, we need to make R1 the root and calculate the smallest cost for each destination.
As you can see from the image above multiple shortest paths have been found to the 172.16.1.0 network, allowing load balancing of the traffic to that destination calledequal-cost multipath (ECMP). After the shortest-path tree is built, a router starts to build the routing table accordingly. Networks are reached consequently to the cost calculated in the tree.
Routing table calculation looks quite simple, however, when some of the OSPF extensions are used or OSPF areas are calculated, routing calculation gets more complicated.
# Forwarding Address
OSPF router can set theforwarding-addressto something other than itself which indicates that an alternate next-hop is possible. Mostly forwarding address is set to0.0.0.0suggesting that the route is reachable only via the advertising router.
The forwarding address is set in LSA if the following conditions are met:
A router that receives such LSA can use a forwarding address if OSPF is able to resolve the forwarding address. If forwarding address is not resolved directly - router sets nexthop for forwading address from LSA as a gateway, if forwarding address is not resolved at all - the gateway will be originator-id. Resolve happens only using OSPF instance routes, not the whole routing table.
Let's look at the example setup below:
RouterR1has a static route to the external network192.168.0.0/24. OSPF is running between R1, R2, and R3, and the static route is distributed across the OSPF network.
The problem in such a setup is obvious, R2 can not reach the external network directly. Traffic going to the LAN network fromR2will be forwarded over the routerR1, but if we look at the network diagram we can see that more R2 can directly reach the router where the LAN network i located.
So knowing the forwarding address conditions, we can make routerR1to set the forwarding address. We simply need to add 10.1.101.0/24 network to OSPF networks in the router'sR1configuration:
```
/routing/ospf/interface-template add area=backbone_v2 networks=10.1.101.0/24
```
Now lets verify that forwarding address is actually working:
```
[admin@r2] /ip/route> print where dst-address=192.168.0.0/24
Flags: D - DYNAMIC; A - ACTIVE; o, y - COPY
Columns: DST-ADDRESS, GATEWAY, DISTANCE
DST-ADDRESS       GATEWAY            DISTANCE
DAo 192.168.0.0/24    10.1.101.1%ether1       110
```
On all OSPF routers you will see LSA set with forwarding address other than 0.0.0.0
```
[admin@r2] /routing/ospf/lsa> print where id=192.168.0.0
Flags: S - self-originated, F - flushing, W - wraparound; D - dynamic
1  D instance=default_ip4 type="external" originator=10.1.101.10 id=192.168.0.0
sequence=0x80000001 age=19 checksum=0xF336 body=
options=E
netmask=255.255.255.0
forwarding-address=10.1.101.1
metric=10 type-1
route-tag=0
```
# Neighbour Relationship and Adjacency
OSPF is a link-state protocol that assumes that the interface of the router is considered an OSPF link. Whenever OSPF is started, it adds the state of all the links in the locallink-state database.
There are several steps before the OSPF network becomes fully functional:
Link-state routing protocols are distributing and replicating database that describes the routing topology. The link-state protocol's flooding algorithm ensures that each router has an identical link-state database and the routing table is calculated based on this database.
After all the steps above are completed link-state database on each neighbor contains full routing domain topology (how many other routers are in the network, how many interfaces routers have, what networks link between router connects, cost of each link, and so on).
# Communication Between OSPF Routers
OSPF operates over the IP network layer using protocol number 89.A destination IP address is set to the neighbor's IP address or to one of the OSPF multicast addresses AllSPFRouters (224.0.0.5) or AllDRRouters (224.0.0.6). The use of these addresses is described later in this article.Every OSPF packet begins with a standard 24-byte header.
Field | Description
-------------------
Packet type | There are several types of OSPF packets: Hello packet, Database Description (DD) packet, Link state request packet, Link State Update packet, and Link State Acknowledgement packet. All of these packets except the Hello packet are used in link-state database synchronization.
Router ID | one of the router's IP addresses unless configured manually
Area ID | Allows OSPF router to associate the packet to the proper OSPF area.
Checksum | Allows receiving router to determine if a packet was damaged in transit.
Authentication fields | These fields allow the receiving router to verify that the packet's contents were not modified and that packet really came from the OSPF router whose Router ID appears in the packet.
There are five different OSPF packet types used to ensure proper LSA flooding over the OSPF network.
# Neighbors Discovery
OSPF discovers potential neighbors by periodically sending Hello packets out of configured interfaces. By defaultHello packetsare sent out at 10-second intervals which can be changed by settinghello-intervalin OSPF interface settings. The router learns the existence of a neighboring router when it receives the neighbor's Hello in return with matching parameters.
The transmission and reception of Hello packets also allow a router to detect the failure of the neighbor. If Hello packets are not received withindead-interval(which by default is 40 seconds) router starts to route packets around the failure. "Hello" protocol ensures that the neighboring routers agree on the Hello interval and Dead interval parameters, preventing situations when not in time received Hello packets mistakenly bring the link down.
Field | Description
-------------------
network mask | The IP mask of the originating router's interface IP address.
hello interval | the period between Hello packets (default 10s)
options | OSPF options for neighbor information
router priority | an 8-bit value used to aid in the election of the DR and BDR. (Not set in p2p links)
router dead interval | time interval has to be received before considering the neighbor is down. ( By default four times bigger than the Hello interval)
DR | the router-id of the current DR
BDR | the router-id of the current BDR
Neighbor router IDs | a list of router ids for all the originating router's neighbors
On each type of network segment Hello protocol works a little differently. It is clear that on point-to-point segments only one neighbor is possible and no additional actions are required. However, if more than one neighbor can be on the segment additional actions are taken to make OSPF functionality even more efficient.
Two routers do not become neighbors unless the following conditions are met.
# Discovery on Broadcast Subnets
The attached node to the broadcast subnet can send a single packet and that packet is received by all other attached nodes. This is very useful for auto-configuration and information replication. Another useful capability in broadcast subnets is multicast. This capability allows sending a single packet which will be received by nodes configured to receive multicast packets. OSPF is using this capability to find OSPF neighbors and detect bidirectional connectivity.
Each OSPF router joins the IP multicast groupAllSPFRouters(224.0.0.5), then the router periodically multicasts its Hello packets to the IP address 224.0.0.5. All other routers that joined the same group will receive a multicasted Hello packet. In that way, OSPF routers maintain relationships with all other OSPF routers by sending a single packet instead of sending a separate packet to each neighbor on the segment.
This approach has several advantages:
Automatic neighbor discovery by multicasting or broadcasting Hello packets. Less bandwidth usage compared to other subnet types. On the broadcast segment, there are n*(n-1)/2 neighbor relations, but those relations are maintained by sending only n Hellos. If the broadcast has the multicast capability, then OSPF operates without disturbing non-OSPF nodes on the broadcast segment. If the multicast capability is not supported all routers will receive broadcasted Hello packets even if the node is not an OSPF router.
# Discovery on NBMA Subnets
Non-broadcast multiaccess (NBMA) segments are similar to broadcast. Support more than two routers, the only difference is that NBMA does not support a data-link broadcast capability. Due to this limitation, OSPF neighbors must be discovered initially through configuration. On RouterOS static neighbor configuration is set in the/routing ospf static-neighbormenu. To reduce the amount of Hello traffic, most routers attached to the NBMA subnet should be assigned a Router Priority of 0 (set by default in RouterOS). Routers that are eligible to become Designated Routers should have priority values other than 0. It ensures that during the election of DR and BDR Hellos are sent only to eligible routers.
```
/routing ospf static-neighbor
```
# Discovery on PTMP Subnets
Point-to-MultiPoint treats the network as a collection of point-to-point links.
By design, PTMP networks should not have broadcast capabilities, which means that OSPF neighbors (the same way as for NBMA networks) must be discovered initially through configuration and all communication happens by sending unicast packets directly between neighbors. On RouterOS static neighbor configuration is set in the/routing ospf static-neighbormenu. Designated Routers and Backup Designated Routers are not elected on Point-to-multipoint subnets.
```
/routing ospf static-neighbor
```
For PTMP networks that do support broadcast, a hybrid type named "ptmp-broadcast" can be used. This network type uses multicast Hellos to discover neighbors automatically and detect bidirectional communication between neighbors. After neighbor detection "ptmp-broacast" sends unicast packets directly to the discovered neighbors. This mode is compatible with the RouterOS v6 "ptmp" type.
# Master-Slave Relation
Before database synchronization can begin, a hierarchy order of exchanging information must be established, which determines which router sendsDatabase Descriptor(DD) packets first (Master). The master router is elected based on thehighest priorityand if priority is not set then therouter IDwill be used. Note that it is a router priority-based relation to arranging the exchanging data between neighbors which does not affect DR/BDR election (meaning thatDRdoes not always have to beMaster).
# Database Synchronization
Link-state Database synchronization between OSPF routers is very important. Unsynchronized databases may lead to incorrectly calculated routing tables which could cause routing loops or black holes.
There are two types of database synchronizations:
When the connection between two neighbors first comes up,initial database synchronizationwill happen. OSPF is using explicit database download when neighbor connections first come up. This procedure is calledDatabase exchange. Instead of sending the entire database, the OSPF router sends only its LSA headers in a sequence of OSPFDatabase Description (DD)packets. The router will send the next DD packet only when the previous packet is acknowledged. When an entire sequence of DD packets has been received, the router knows which LSAs it does not have and which LSAs are more recent. The router then sendsLink-State Request (LSR)packets requesting desired LSAs, and the neighbor responds by flooding LSAs inLink-State Update (LSU)packets. After all the updates are received neighbors are said to befully adjacent.
Reliable flooding is another database synchronization method. It is used when adjacencies are already established and the OSPF router wants to inform other routers about LSA changes. When the OSPF router receives such Link State Update, it installs a new LSA in the link-state database, sends an acknowledgment packet back to the sender, repackages LSA in new LSU, and sends it out to all interfaces except the one that received the LSA in the first place.
OSPF determines if LSAs are up to date by comparing sequence numbers. Sequence numbers start with 0×80000001, the larger the number, the more recent the LSA is. A sequence number is incremented each time the record is flooded and the neighbor receiving the update resets the Maximum age timer. LSAs are refreshed every 30 minutes, but without a refresh, LSA remains in the database for the maximum age of 60 minutes.
Databases are not always synchronized between all OSPF neighbors, OSPF decides whether databases need to be synchronized depending on the network segment, for example, on point-to-point links databases are always synchronized between routers, but on Ethernet networks databases are synchronized between certain neighbor pairs.
# Synchronization on Broadcast Subnets
On the broadcast segment, there are n*(n-1)/2 neighbor relations, it will be a huge amount of Link State Updates and Acknowledgements sent over the subnet if the OSPF router will try to synchronize with each OSPF router on the subnet.
This problem is solved by electing oneDesignated Routerand oneBackup Designated Routerfor each broadcast subnet. All other routers are synchronizing and forming adjacencies only with those two elected routers. This approach reduces the number of adjacencies from n*(n-1)/2 to only 2n-3.
The image on the right illustrates adjacency formations on broadcast subnets. Routers R1 and R2 are Designated Routers and Backup Designated routers respectively. For example, if R3 wants to flood Link State Update (LSU) to both R1 and R2, a router sends LSU to the IP multicast addressAllDRouters(224.0.0.6) and only DR and BDR listen to this multicast address. Then Designated Router sends LSU addressed to AllSPFRouters, updating the rest of the routers.
# DR Election
DR and BDR routers are elected from data received in the Hello packet. The first OSPF router on a subnet is always elected as Designated Router, when a second router is added it becomes Backup Designated Router. When an existing DR or BDR fails new DR or BDR is elected to take into account configuredrouter priority. The router with the highest priority becomes the new DR or BDR.
Being Designated Router or Backup Designated Router consumes additional resources. If Router Priority is set to 0, then the router is not participating in the election process. This is very useful if certain slower routers are not capable of being DR or BDR.
# Synchronization on NBMA Subnets
Database synchronization on NBMA networks is similar to that on broadcast networks. DR and BDR are elected, databases initially are exchanged only with DR and BDR routers and flooding always goes through the DR. The only difference is that Link State Updates must be replicated and sent to each adjacent router separately.
# Synchronization on PTMP Subnets
On PTMP subnets OSPF router becomes adjacent to all other routes with which it can communicate directly.
# Understanding OSPF Areas
A distinctive feature of OSPF is the possibility to divide AS into multiple routing Areas which contain their own set of neighbors.Imagine a large network with 300+ routers and multiple links between them. Whenever link flaps or some other topology change happens in the network, this change will be flooded to all OSPF devices in the network resulting in a quite heavy load on the network and even downtime since network convergence may take some time for such a large network.
A large single-area network can produce serious issues:
The introduction of areas allows for better resource management since topology change inside one area is not flooded to other areas in the network. The concept of areas enables simplicity in network administration as well as routing summarization between areas significantly reducing the database size that needs to be stored on each OSPF neighbor. This means that each area has its own link-state database and corresponding shortest-path tree.
The structure of an area is invisible to other areas. This isolation of knowledge makes the protocol more scalable if multiple areas are used; routing table calculation takes fewer CPU resources and routing traffic is reduced.
However, multi-area setups create additional complexity. It is not recommended to separate areas with fewer than 50 routers. The maximum number of routers in one area is mostly dependent on the CPU power you have for routing table calculation.
OSPF area has unique 32-bit identification (Area ID) and the area with an Area ID of 0.0.0.0 (called the Backbone area) is the main one where any other area should connect. Routers that connect to more than one area are calledABR(Area Border Routers), and their main responsibility is summarization and update suppression between connected areas. The router connecting to another routing domain is calledASBR(Autonomous System Boundary Router).
Each area has its own link-state database, consisting of router-LSAs and network-LSAs describing how all routers within that area are interconnected. Detailed knowledge of the area's topology is hidden from all other areas; router-LSAs and network-LSAs are not flooded beyond the area's borders. Area Border Routers (ABRs) leak addressing information from one area into another in OSPF summary-LSAs. This allows one to pick the best area border router when forwarding data to destinations from another area and is calledintra-area routing.
Routing information exchange between areas is essentially a Distance Vector algorithm and to prevent algorithm convergence problems, such as counting to infinity, all areas are required to attach directly to thebackbone areamaking a simple hub-and-spoke topology. The area-ID of the backbone area is always 0.0.0.0 and can not be changed.
RouterOS area configuration is done in the/routing/ospf/areamenu.  For example, a configuration of an ABR router with multiple attached areas, one Stub area, and one default area:
```
/routing/ospf/area
```
```
/routing ospf area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=stub_area area-id=1.1.1.1 instance=v2inst type=stub
add name=another_area area-id=2.2.2.2 instance=v2inst type=default
```
OSPF can have 5 types of areas. Each area type defines what type of LSAs the area supports:
# LSA Types
Before we continue a detailed look at each area type, let's get familiar with LSA types:
# Standard Area
This area supports 1, 2, 3, 4, and 5 LSAs.
Simple multi-area network using default area. In this example, all networks from area1 are flooded to the backbone and all networks from the backbone are flooded to area1.R1:
```
/ip address add address=10.0.3.1/24 interface=ether1
/ip address add address=10.0.2.1/24 interface=ether2
/routing ospf instance
add name=v2inst version=2 router-id=1.0.0.1
/routing ospf area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=area1 area-id=1.1.1.1 type=default instance=v2inst
/routing ospf interface-template
add networks=10.0.2.0/24 area=backbone_v2
add networks=10.0.3.0/24 area=area1
```
R2:
```
/ip address add address=10.0.1.1/24 interface=ether2
/ip address add address=10.0.2.2/24 interface=ether1
/routing ospf instance
add name=v2inst version=2 router-id=1.0.0.2
/routing ospf area
add name=backbone_v2 area-id=0.0.0.0
/routing ospf interface-template
add networks=10.0.2.0/24 area=backbone_v2
add networks=10.0.1.0/24 area=backbone_v2
```
R3:
```
/ip address add address=10.0.3.2/24 interface=ether2
/ip address add address=10.0.4.1/24 interface=ether1
/routing ospf instance
add name=v2inst version=2 router-id=1.0.0.3
/routing ospf area
add name=area1 area-id=1.1.1.1 type=stub instance=v2inst
/routing ospf interface-template
add networks=10.0.3.0/24 area=area1
add networks=10.0.4.0/24 area=area1
```
# Stub Area
The main purpose of stub areas is to keep such areas from carrying external routes. Routing from these areas to the outside world is based on a default route. A stub area reduces the database size inside an area and reduces the memory requirements of routers in the area.
The stub area has a few restrictions, ASBR routers cannot be internal to the area, stub area cannot be used as a transit area for virtual links. The restrictions are made because the stub area is mainly configured not to carry external routes.
This area supports 1, 2, and 3 LSAs.
Let's consider the example above. Area1 is configured as a stub area meaning that routers R2 and R3 will not receive any routing information from the backbone area except the default route.
R1:
```
/routing ospf instance
add name=v2inst version=2 router-id=1.0.0.1
/routing ospf area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=area1 area-id=1.1.1.1 type=stub instance=v2inst
/routing ospf interface-template
add networks=10.0.0.0/24 area=backbone_v2
add networks=10.0.1.0/24 area=area1
add networks=10.0.3.0/24 area=area1
```
R2:
```
/routing ospf instance
add name=v2inst version=2 router-id=1.0.0.2
/routing ospf area
add name=area1 area-id=1.1.1.1 type=stub instance=v2inst
/routing ospf interface-template
add networks=10.0.1.0/24 area=area1
```
R3:
```
/routing ospf instance
add name=v2inst version=2 router-id=1.0.0.3
/routing ospf area
add name=area1 area-id=1.1.1.1 type=stub instance=v2inst
/routing ospf interface-template
add networks=10.0.3.0/24 area=area1
```
# Totally Stubby Area
Totally stubby area is an extension of the stub area. A totally stubby area blocks external routes and summarized (inter-area) routes from going into the area. Only intra-area routes are injected into the area. Totally stubby area is configured as a stub area with an additionalno-summariesflag. This area supports Type 1, Type 2 LSAs, and Type 3 LSAs with default routes.
```
no-summaries
```
```
/routing ospf area
add name=totally_stubby_area area-id=1.1.1.1 instance=v2inst type=stub no-summaries
```
# NSSA
Not-so-stubby area (NSSA) is useful when it is required to inject external routes, but injection of type 5 LSA routes is not required.
The illustration shows two areas (backbone and area1) and RIP connection to the router located in "area1". We need "area1" to be configured as a stub area, but it is also required to inject external RIP routes in the backbone. Area1 should be configured as NSSA in this case.
The configuration example does not coverRIPconfiguration.
R1:
```
/routing ospf instance
add name=v2inst version=2 router-id=1.0.0.1
/routing ospf area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=area1 area-id=1.1.1.1 type=nssa instance=v2inst
/routing ospf interface-template
add networks=10.0.0.0/24 area=backbone_v2
add networks=10.0.1.0/24 area=area1
```
R2:
```
/routing ospf instance
add name=v2inst version=2 router-id=1.0.0.2
/routing ospf area
add name=area1 area-id=1.1.1.1 type=nssa instance=v2inst
/routing ospf interface-template
add networks=10.0.1.0/24 area=area1
```
# External Routing Information and Default Route
On the edge of an OSPF routing domain, you can find routers calledAS boundary routers (ASBRs)that run one of the other routing protocols. The job of those routers is to import routing information learned from other routing protocols into the OSPF routing domain. External routes can be imported at two separate levels depending on the metric type.
External routes can be imported via the instanceredistributeparameter. The example below will pick and redistribute all static and RIP routes:
```
redistribute
```
```
/routing ospf instance
add name=v2inst version=2 router-id=1.2.3.4 redistribute=static,rip
```
Redistribution of default route is a special case where theoriginate-defaultthe parameter should be used:
```
originate-default
```
```
/routing ospf instance
set v2inst originate-default=if-installed
```
Since redistribution is controlled by "originate-default" and "redistribute" parameter, it introduces some corner-cases for default route filtering.
```
originate-default
```
```
redistribute
```
```
redistribute
```
```
originate-default=never
```
```
out-select-chain
```
```
out-filter-chain
```
```
originate-default
```
```
always
```
```
if-installed
```
```
out-filter-chain
```
For a complete list of redistribution values, see the reference manual.
# Route Summarisation
Route summarization is a consolidation of multiple routes into one single advertisement. It is normally done at the area boundaries (Area Border Routers).
It is better to summarise in the direction of the backbone. That way the backbone receives all the aggregated routes and injects them into other areas already summarized. There are two types of summarization: inter-area and external route summarization.
Inter-area route summarization works on area boundaries (ABRs), it does not apply to external routes injected into OSPF via redistribution. By default, ABR creates a summary LSA for each route in a specific area and advertises it in adjacent areas.
Using ranges allows for creating only one summary LSA for multiple routes and sending only a single advertisement into adjacent areas, or suppressing advertisements altogether.
If a range is configured with the 'advertise' parameter, a single summary LSA is advertised for each range if there are any routes under the range in the specific area. Otherwise (when 'advertise' parameter disabled) no summary LSAs are created and advertised outside area boundaries at all.
```
advertise
```
```
advertise
```
Inter-area route summarization can be configured from theOSPF area rangemenu.
Let's consider that we have two areas backbone and area1, area1 has several /24 routes from the 10.0.0.0/16 range and there is no need to flood the backbone area with each /24 subnet if it can be summarized. On the router connecting area1 with the backbone we can set up the area range:
```
/routing ospf area range
add prefix=10.0.0.0/16 area=area1 advertise=yes cost=10
```
External route summarization can be achieved using routing filters.  Let's consider the same example as above except that area1 has redistributed /24 routes from other protocols. To send a single summarised LSA, a blackhole route must be added and an appropriate routing filter to accept only summarised route:
```
/ip route add dst-address=10.0.0.0/16 blackhole
/routing ospf instance
set v2inst out-filter-chain=ospf_out
/routing filter rule
add chain=ospf_out rule="if (dst == 10.0.0.0/16) {accept} else {reject}"
```
# Virtual Link
As it was mentioned previously all OSPF areas have to be attached to the backbone area, but sometimes the physical connection is not possible. To overcome this, areas can be attached logically by usingvirtual links.
There are two common scenarios when virtual links can be used:
# Partitioned Backbone
OSPF allows to linking of discontinuous parts of the backbone area using virtual links. This might be required when two separate OSPF networks are merged into one large network. Virtual links can be configured between separate ABRs that touch the backbone area from each side and have a common area.
The additional area could be created to become a transit area when a common area does not exist, it is illustrated in the image above.
Virtual Links are not required for non-backbone areas when they get partitioned. OSPF does not actively attempt to repair area partitions, each component simply becomes a separate area, when an area becomes partitioned. The backbone performs routing between the new areas. Some destinations are reachable viaintra-arearouting, the area partition requiresinter-arearouting.
However, to maintain full routing after the partition, an address range has not to be split across multiple components of the area partition.
# No physical connection to a backbone
The area may not have a physical connection to the backbone, a virtual link is used to provide a logical path to the backbone of the disconnected area. A link has to be established between two ABRs that have a common area with one ABR connected to the backbone.
We can see that both R1 and R2 routers are ABRs and R1 is connected to the backbone area. Area2 will be used as atransit areaand R1 is theentry pointinto the backbone area. A virtual link has to be configured on both routers.
Virtual link configuration is added in OSPF interface templates. If we take the example setup from the "no physical connection" illustration, then the virtual link configuration would look like this:
R1:
```
/routing ospf interface-template
add vlink-transit-area=area2 area=backbone_v2 type=virtual-link vlink-neighbor-id=2.2.2.2
```
R2:
```
/routing ospf interface-template
add vlink-transit-area=area2 area=backbone_v2 type=virtual-link vlink-neighbor-id=1.1.1.1
```
# Property Reference
# Instance
Sub-menu:/routing/ospf/instance
```
/routing/ospf/instance
```
Property | Description
----------------------
domain-id(Hex | Address) | MPLS-related parameter. Identifies the OSPF domain of the instance. This value is attached to OSPF routes redistributed in BGP as VPNv4 routes as BGP extended community attribute and used when BGP VPNv4 routes are redistributed back to OSPF to determine whether to generate inter-area or AS-external LSA for that route. By default Null domain-id is used, as described in RFC 4577.
domain-tag(integer [0..4294967295]) | if set, then used in route redistribution (as route-tag in all external LSAs generated by this router), and in route calculation (all external LSAs having this route tag are ignored). Needed for interoperability with older Cisco systems. By default not set.
in-filter(string) | name of therouting filterchain used for incoming prefixes
mpls-te-address(string) | the area used for MPLS traffic engineering. TE Opaque LSAs are generated in this area. No more than one OSPF instance can have mpls-te-area configured.
mpls-te-area(string) | the area used for MPLS traffic engineering. TE Opaque LSAs are generated in this area. No more than one OSPF instance can have mpls-te-area configured.
originate-default(always | if-installed | never;) | Specifies default route (0.0.0.0/0) distribution method.
out-filter-chain(name) | name of therouting filterchain used for outgoing prefixes filtering. Output operates only with "external" routes.
out-filter-select(name) | name of the routing filter select chain, used for output selection. Output operates only with "external" routes.
redistribute(bgp,connected,copy,dhcp,fantasy,modem,ospf,rip,static,vpn;) | Enable redistribution of specific route types.
router-id(IP | name; Default:main) | OSPF Router ID. Can be set explicitly as an IP address, or as the name of the router-id instance.
version(2 | 3;Default:2) | OSPF version this instance will be running (v2 for IPv4, v3 for IPv6).
vrf(name of a routing table; Default:main) | the VRF table this OSPF instance operates on
use-dn(yes | no) | Forces to use or ignore DN bit. Useful in some CE PE scenarios to inject intra-area routes into VRF. If a parameter is unset then the DN bit is used according to RFC. Available since v6rc12.
# Notes
OSPF protocol supports two types of metrics:
# Area
Sub-menu:/routing/ospf/area
```
/routing/ospf/area
```
Property | Description
----------------------
area-id(IP address; Default:0.0.0.0) | OSPF area identifier. If the router has networks in more than one area, then an area with area-id=0.0.0.0 (the backbone) must always be present. The backbone always contains all area border routers. The backbone is responsible for distributing routing information between non-backbone areas. The backbone must be contiguous, i.e. there must be no disconnected segments. However, area border routers do not need to be physically connected to the backbone - connection to it may be simulated using avirtual link.
default-cost(integer;unset) | Default cost of injected LSAs into the area. If the value is not set, then stub area type-3 default LSA will not be originated.
instance(name;mandatory) | Name of the OSPF instance this area belongs to.
no-summaries() | Flag parameter, if set then the area will not flood summary LSAs in the stub area.
name(string) | the name of the area
nssa-translate(yes | no | candidate) | The parameter indicates which ABR will be used as a translator from type7 to type5 LSA. Applicable only if area type is NSSAyes - the router will be always used as a translatorno - the router will never be used as a translatorcandidate - OSPF elects one of the candidate routers to be a translator
type(default | nssa | stub; Default:default) | The area type. Read more on the area types in the OSPF case studies.
# Area Range
Sub-menu:/routing/ospf/area/range
```
/routing/ospf/area/range
```
Property | Description
----------------------
advertise(yes | no; Default: yes) | Whether to create a summary LSA and advertise it to the adjacent areas.
area(name;mandatory) | the OSPF area associated with this range
cost(integer [0..4294967295]) | the cost of the summary LSA this range will createdefault - use the largest cost of all routes used (i.e. routes that fall within this range)
prefix(IP prefix;mandatory) | the network prefix of this range
default - use the largest cost of all routes used (i.e. routes that fall within this range)
# Interface
Sub-menu:/routing/ospf/interface
```
/routing/ospf/interface
```
Read-only matched interface menu
# Interface Templates
Sub-menu:/routing/ospf/interface-template
```
/routing/ospf/interface-template
```
The interface template defines common network and interface matches and what parameters to assign to a matched interface.
# Matchers
Property | Description
----------------------
interfaces(name) | Interfaces to match. Accepts specific interface names or the name of the interface list.
network(IP prefix) | the network prefix associated with the area. OSPF will be enabled on all interfaces that have at least one address falling within this range. Note that the network prefix of the address is used for this check (i.e. not the local address). For point-to-point interfaces, this means the address of the remote endpoint.
interfaces(name)
Interfaces to match. Accepts specific interface names or the name of the interface list.
# Assigned Parameters
Property | Description
----------------------
area(name;mandatory) | The OSPF area to which the matching interface will be associated.
auth(simple | md5 | sha1 | sha256 | sha384 | sha512) | Specifies authentication method for OSPF protocol messages.simple- plain text authenticationmd5- keyed Message Digest 5 authenticationsha - HMAC-SHA authentication RFC5709If the parameter is unset, then authentication is not used.
auth-id(integer) | The key id is used to calculate message digest (used when MD5 or SHA authentication is enabled). The value should match all OSPF routers from the same region.
authentication-key(string) | The authentication key to be used, should match on all the neighbors of the network segment.
comment(string) |
cost(integer [0..65535]) | Interface cost expressed as link state metric.
dead-interval(time; Default:40s) | Specifies the interval after which a neighbor is declared dead. This interval is advertised in hello packets. This value must be the same for all routers on a specific network, otherwise, adjacency between them will not form
disabled(yes | no) |
hello-interval(time; Default:10s) | The interval betweenHELLOpackets that the router sends out this interface. The smaller this interval is, the faster topological changes will be detected, the tradeoff is more OSPF protocol traffic. This value must be the same for all the routers on a specific network, otherwise, adjacency between them will not form.
instance-id(integer [0..255]; Default:0) |
passive() | If enabled, then do not send or receive OSPF traffic on the matching interfaces
prefix-list(name) | Name of the address list containing networks that should be advertised to the v3 interface.
priority(integer: 0..255; Default:128) | Router's priority. Used to determine the designated router in a broadcast network. The router with the highest priority value takes precedence. Priority value 0 means the router is not eligible to become a designated or backup designated router at all.
retransmit-interval(time; Default:5s) | Time interval the lost link state advertisement will be resent. When a router sends a link state advertisement (LSA) to its neighbor, the LSA is kept until the acknowledgment is received. If the acknowledgment was not received in time (seetransmit-delay), the router will try to retransmit the LSA.
transmit-delay(time; Default:1s) | Link-state transmit delay is the estimated time it takes to transmit a link-state update packet on the interface.
type(broadcast | nbma | ptp | ptmp | ptp-unnumbered | virtual-link; Default:broadcast) | the OSPF network type on this interface. Note that if interface configuration does not exist, the default network type is 'point-to-point' on PtP interfaces and 'broadcast' on all other interfaces.broadcast- network type suitable for Ethernet and other multicast capable link layers. Elects designated routernbma- Non-Broadcast Multiple Access. Protocol packets are sent to each neighbor's unicast address. Requires manual configuration of neighbors. Elects designated routerptp- suitable for networks that consist only of two nodes. Do not elect designated routerptmp- Point-to-Multipoint. Easier to configure than NBMA because it requires no manual configuration of a neighbor. Do not elect a designated router. This is the most robust network type and as such suitable for wireless networks, if 'broadcast' mode does not work well enough for themptp-unnumbered - works the same as ptp, except that the remote neighbor does not have an associated IP address to a specific PTP interface. For example, in case an IP unnumbered is used on Cisco devices.virtual-link - for virtual link setups.
vlink-neighbor-id(IP) | Specifies therouter-idof the neighbor which should be connected over the virtual link.
vlink-transit-area(name) | A non-backbone area the two routers have in common over which the virtual link will be established. Virtual links can not be established through stub areas.
If the parameter is unset, then authentication is not used.
Router's priority. Used to determine the designated router in a broadcast network. The router with the highest priority value takes precedence. Priority value 0 means the router is not eligible to become a designated or backup designated router at all.
# Lsa
Sub-menu:/routing/ospf/lsa
```
/routing/ospf/lsa
```
Read-only list of all the LSAs currently in the LSA database.
Property | Description
----------------------
age(integer) | How long ago (in seconds) the last update occurred
area(string) | The area this LSA belongs to.
body(string) |
checksum(string) | LSA checksum
dynamic(yes | no) |
flushing(yes | no) |
id(IP) | LSA record ID
instance(string) | The instance name this LSA belongs to.
link(string) |
link-instance-id(IP) |
originator(IP) | An originator of the LSA record.
self-originated(yes | no) | Whether LSA originated from the router itself.
sequence(string) | A number of times the LSA for a link has been updated.
type(string) |
wraparound(string) |
# Neighbors
Sub-menu:/routing/ospf/neighbor
```
/routing/ospf/neighbor
```
Read-only list of currently active OSPF neighbors.
Property | Description
----------------------
address(IP) | An IP address of the OSPF neighbor router
adjacency(time) | Elapsed time since adjacency was formed
area(string) |
bdr(string) | An IP address of the Backup Designated Router
comment(string) |
db-summaries(integer) |
dr(IP) | An IP address of the Designated Router
dynamic(yes | no) |
inactive(yes | no) |
instance(string) |
ls-requests(integer) |
ls-retransmits(integer) |
priority(integer) | Priority configured on the neighbor
router-id(IP) | neighbor router'sRouterID
state(down | attempt | init | 2-way | ExStart | Exchange | Loading | full) | Down- No Hello packets have been received from a neighbor.Attempt- Applies only to NBMA clouds. The state indicates that no recent information was received from a neighbor.Init- Hello packet received from the neighbor, but bidirectional communication is not established (Its own RouterID is not listed in the Hello packet).2-way- This state indicates that bi-directional communication is established. DR and BDR elections occur during this state, routers build adjacencies based on whether the router is DR or BDR, and the link is point-to-point or a virtual link.ExStart- Routers try to establish the initial sequence number that is used for the packet information exchange. The router with a higher ID becomes the master and starts the exchange.Exchange- Routers exchange database description (DD) packets.Loading- In this state actual link state information is exchanged. Link State Request packets are sent to neighbors to request any new LSAs that were found during the Exchange state.Full- Adjacency is complete, and neighbor routers are fully adjacent. LSA information is synchronized between adjacent routers. Routers achieve the full state with their DR and BDR only, an exception is P2P links.
state-changes(integer) | Total count of OSPF state changes since neighbor identification
# Static Neighbour configuration
Sub-menu:/routing/ospf/static-neighbor
```
/routing/ospf/static-neighbor
```
Static configuration of the OSPF neighbors. Required for non-broadcast multi-access networks.
Property | Description
----------------------
address(IP%iface;mandatory) | The unicast IP address and an interface, that can be used to reach the IP of the neighbor. For example,address=1.2.3.4%ether1indicates that a neighbor with IP1.2.3.4is reachable on theether1interface.
area(name;mandatory) | Name of the area the neighbor belongs to.
comment(string) |
disabled(yes | no) |
instance-id(integer [0..255]; Default:0) |
poll-interval(time; Default:2m) | How often to send hello messages to the neighbors which are in a "down" state (i.e. there is no traffic from them)
```
address=1.2.3.4%ether1
```