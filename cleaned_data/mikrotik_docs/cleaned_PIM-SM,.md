# Document Information
Title: PIM-SM
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/61767728/PIM-SM,

# Content
# Summary
IP Multicast is a technology that allows data to be efficiently shared with many recipients over the Internet. Senders transmit their data to a specific multicast IP address, and receivers indicate their interest in receiving data sent to that address. The network then takes care of delivering the data from senders to receivers.
If both the sender and receiver for a multicast group are on the same local network segment, routers are not required for the process. Communication can happen directly, and this can be enhanced with the use ofIGMP snoopingswitches. However, if the sender and receiver are on different network segments, a multicast routing protocol must be used to establish the path for data transmission between them.
Protocol Independent Multicast - Sparse Mode (PIM-SM or PIM) enables RouterOS to support multicast streaming over the network area. PIM stands for Platform Independent Multicast, meaning it's not tied to any particular unicast routing. SM stands for Sparse-Mode, which means that specific control messages ensure that data is delivered only to network segments where there are receivers that want it. In addition to the routing protocols that manage data transmission between network segments, routers need a way to discover local receivers on their directly connected network segment. For IPv4, this is achieved through the Internet Group Management Protocol (IGMP), and Multicast Listener Discovery (MLD) for IPv6.
# Basic multicast routing on single device
Picture this scenario, you have got a router with two interfaces, namely ether1 and ether2, and each of them is set up in separate networks. Normally, the router will create connected routes and hosts on both networks will be able to communicate using unicast traffic. However, if you want to enable multicast communication between these networks, you'll need to configure multicast routing separately because it won't work otherwise. In this scenario, we are going to create a simple configuration. This involves creating a PIM instance and configuring the required interfaces.
Begin by ensuring that IP addresses are set up on the router's interfaces.
```
/ip address
add address=192.168.10.1/24 interface=ether1 network=192.168.10.0
add address=192.168.20.1/24 interface=ether2 network=192.168.20.0
```
Configure PIM instance. For this example, the default settings should work fine.
```
/routing pimsm instance
add name=pimsm-instance-1
```
Last, add interfaces and specify the PIM instance you created earlier.
```
/routing pimsm interface-template
add interfaces=ether1,ether2 instance=pimsm-instance-1
```
Now router starts listening to IGMP membership reports (client join messages) and will route multicast traffic to clients interested in receiving it.
To test the configuration, you can configure a multicast sender using RouterOStraffic-generatorand IGMP client usingGMP.
```
# Multicast Sender
/ip address
add address=192.168.10.10/24 interface=ether1 network=192.168.10.0
/tool traffic-generator packet-template
add interface=ether1 ip-dst=229.1.1.2 mac-dst=01:00:5E:01:01:02/FF:FF:FF:FF:FF:FF name=multicast
/tool traffic-generator quick tx-template=multicast mbps=10
# Multicast Client
/ip address
add address=192.168.20.10/24 interface=ether1 network=192.168.20.0
/routing gmp
add disabled=no groups=229.1.1.2 interfaces=ether1
```
To verify whether multicast traffic is being properly routed, monitor the received packet counters on the client interface or use tools likeTorchor aPacket Sniffer.
It is also possible to monitor active multicast group on router:
```
/routing pimsm uib-g print
Columns: INSTANCE, GROUP
# INSTANCE          GROUP
0 pimsm-instance-1  229.1.1.2
/routing pimsm uib-sg print
Flags: K - KEEPALIVE; S - SPT-BIT
Columns: INSTANCE, GROUP, SOURCE
# INSTANCE          GROUP      SOURCE
0 KS pimsm-instance-1  229.1.1.2  192.168.10.10
```
# Multicast routing with static RP
In the upcoming example, we'll be working with multiple PIM routers, as shown in the diagram below. PIM-SM uses shared trees and to make this work, we need to designate a specific node as the multicast root distribution point. In PIM, this router is called the Rendezvous Point, or RP. There are various methods for selecting an RP in PIM, such as the Bootstrap Router (BSR) method. However, for this example, we'll be using a straightforward approach known as static RP configuration. This means that the administrator can manually specify one or more RPs for specific multicast groups.
To get started, we'll need to configure IP addresses and set up unicast routing. In this example, we'll use OSPF to exchange routing information between the routers. See more details aboutOSFP.
```
# R1 Rendezvous Point:
/interface bridge
add name=loopback
/ip address
add address=10.0.0.1 interface=loopback network=10.0.0.1
add address=10.0.1.1/24 interface=ether2 network=10.0.1.0
add address=10.0.2.1/24 interface=ether3 network=10.0.2.0
/routing ospf instance
add disabled=no name=ospf-instance-1 router-id=10.0.0.1
/routing ospf area
add disabled=no instance=ospf-instance-1 name=ospf-area-1
/routing ospf interface-template
add area=ospf-area-1 disabled=no interfaces=loopback,ether2,ether3
# R2:
/interface bridge
add name=loopback
/ip address
add address=10.0.0.2 interface=loopback network=10.0.0.2
add address=10.0.1.2/24 interface=ether1 network=10.0.1.0
add address=192.168.20.1/24 interface=ether12 network=192.168.20.0
/routing ospf instance
add disabled=no name=ospf-instance-1 router-id=10.0.0.2
/routing ospf area
add disabled=no instance=ospf-instance-1 name=ospf-area-1
/routing ospf interface-template
add area=ospf-area-1 disabled=no interfaces=loopback,ether1,ether12
# R3:
/interface bridge
add name=loopback
/ip address
add address=10.0.0.3 interface=loopback network=10.0.0.3
add address=10.0.2.3/24 interface=ether1 network=10.0.2.0
add address=192.168.30.1/24 interface=ether12 network=192.168.30.0
/routing ospf instance
add disabled=no name=ospf-instance-1 router-id=10.0.0.3
/routing ospf area
add disabled=no instance=ospf-instance-1 name=ospf-area-1
/routing ospf interface-template
add area=ospf-area-1 disabled=no interfaces=loopback,ether1,ether12
```
As in the previous example with a single router, we need to configure the PIM instance and add the necessary interfaces on all routers.
```
# R1 Rendezvous Point:
/routing pimsm instance
add disabled=no name=pimsm-instance-1
/routing pimsm interface-template
add instance=pimsm-instance-1 interfaces=loopback,ether2,ether3
# R2:
/routing pimsm instance
add disabled=no name=pimsm-instance-1
/routing pimsm interface-template
add instance=pimsm-instance-1 interfaces=loopback,ether1,ether12
# R3:
/routing pimsm instance
add name=pimsm-instance-1
/routing pimsm interface-template
add instance=pimsm-instance-1 interfaces=loopback,ether1,ether12
```
Now, let's take a look at our PIM neighbors and their current statuses. On R1, there are two neighbors, while on R2 and R3, there's only one neighbor each.
```
# R1 Rendezvous Point:
/routing pimsm neighbor print
Flags: R - DESIGNATED-ROUTER; J - JOIN-TRACKING
Columns: INSTANCE, ADDRESS, PRIORITY
# INSTANCE          ADDRESS          PRIORITY
0 RJ pimsm-instance-1  10.0.1.2%ether2  1
1 RJ pimsm-instance-1  10.0.2.3%ether3  1
# R2:
/routing pimsm neighbor print
Flags: R - DESIGNATED-ROUTER; J - JOIN-TRACKING
Columns: INSTANCE, ADDRESS, PRIORITY
# INSTANCE          ADDRESS          PRIORITY
0  J pimsm-instance-1  10.0.1.1%ether1  1
# R3:
/routing pimsm neighbor print
Flags: J - JOIN-TRACKING
Columns: INSTANCE, ADDRESS, PRIORITY
# INSTANCE          ADDRESS          PRIORITY
0 J pimsm-instance-1  10.0.2.1%ether1  1
```
Finally, we will select one router to act as our Rendezvous Point (RP). We will configure the R1 loopback IP address on all PIM routers. It's important to ensure that each router has the correct routing information to reach the R1 loopback address.
```
# R1 Rendezvous Point:
/routing pimsm static-rp
add address=10.0.0.1 instance=pimsm-instance-1
# R2:
/routing pimsm static-rp
add address=10.0.0.1 instance=pimsm-instance-1
# R3:
/routing pimsm static-rp
add address=10.0.0.1 instance=pimsm-instance-1
```
# Property Reference
# Instance
The instance menu defines the main PIM-SM settings. The instance is then used for all other PIM-related configurations like interface-template, static RP, and Bootstrap Router.
Sub-menu:/routing pimsm instance
```
/routing pimsm instance
```
Property | Description
----------------------
afi(ipv4 | ipv6; Default:ipv4) | Specifies address family for PIM.
bsm-forward-back(yes | no; Default:) | Currently not implemented.
crp-advertise-contained(yes | no; Default:) | Currently not implemented.
name(text; Default:) | Name of the instance.
rp-hash-mask-length(integer: 0..4294967295; Default:30(IPv4), or126(IPv6)) | The hash mask allows changing how many groups to map to one of the matching RPs.
rp-static-override(yes | no; Default:no) | Changes the selection priority for static RP. When disabled, the bootstrap RP set has a higher priority. When enabled, static RP has a higher priority.
ssm-range(IPv4 | IPv6; Default: ) | Currently not implemented.
switch-to-spt(yes | no; Default:yes) | Whether to switch to Shortest Path Tree (SPT) if multicast data bandwidth threshold is reached. The router will not proceed from protocol phase one (register encapsulation) to native multicast traffic flow if this option is disabled. It is recommended to enable this option.
switch-to-spt-bytes(integer: 0..4294967295; Default:0) | Multicast data bandwidth threshold. Switching to Shortest Path Tree (SPT) happens if this threshold is reached in the specified time interval. If a value of 0 is configured, switching will happen immediately.
switch-to-spt-interval(time; Default:) | Time interval in which to account for multicast data bandwidth, used in conjunction withswitch-to-spt-bytesto determine if the switching threshold is reached.
vrf(name; Default: main) | Name of the VRF.
Property
Description
Currently not implemented.
```
switch-to-spt-bytes
```
# Interface template
The interface template menu defines which interfaces will participate in PIM and what per-interface configuration will be used.
Sub-menu:/routing pimsm interface-template
```
/routing pimsm interface-template
```
Property | Description
----------------------
hello-delay(time; Default:5s) | Randomized interval for the initial Hello message on interface startup or detecting new neighbor.
hello-period(time; Default:30s) | Periodic interval for Hello messages.
instance(name; Default:) | Name of the PIM instance this interface template belongs to.
interfaces(name; Default:all) | List of interfaces that will participate in PIM.
join-prune-period(time; Default:1m) |
join-tracking-support(yes | no; Default:yes) | Sets the value of a Tracking (T) bit in the LAN Prune Delay option in the Hello message. When enabled, a router advertises its willingness to disable Join suppression. it is possible for upstream routers to explicitly track the join membership of individual downstream routers if Join suppression is disabled. Unless all PIM routers on a link negotiate this capability, explicit tracking and the disabling of the Join suppression mechanism are not possible.
override-interval(time; Default:2s500ms) | Sets the maximum time period over which to randomize when scheduling a delayed override Join message on a network that has join suppression enabled.
priority(integer: 0..4294967295; Default:1) | The Designated Router (DR) priority. A single Designated Router is elected on each network. The priority is used only if all neighbors have advertised a priority option. Numerically largest priority is preferred. In case of a tie or if priority is not used - the numerically largest IP address is preferred.
propagation-delay(time; Default:500ms) | Sets the value for a prune pending timer. It is used by upstream routers to figure out how long they should wait for a Join override message before pruning an interface that has join suppression enabled.
source-addresses(IPv4 | IPv6; Default: ) |
Property
Description
Sets the value of a Tracking (T) bit in the LAN Prune Delay option in the Hello message. When enabled, a router advertises its willingness to disable Join suppression. it is possible for upstream routers to explicitly track the join membership of individual downstream routers if Join suppression is disabled. Unless all PIM routers on a link negotiate this capability, explicit tracking and the disabling of the Join suppression mechanism are not possible.
Sets the value for a prune pending timer. It is used by upstream routers to figure out how long they should wait for a Join override message before pruning an interface that has join suppression enabled.
# Interface
The interface menu shows all interfaces that are currently participating in PIM and their statuses. This menu contains dynamic and read-only entries that get created by defined interface templates.
Sub-menu:/routing pimsm interface
```
/routing pimsm interface
```
Property | Description
----------------------
address(IP%interface@vrf) | Shows IP address, interface, and VRF.
designated-router(yes | no) |
dr(yes | no) |
dynamic(yes | no) |
instance(name) | Name of the PIM instance this interface template belongs to.
join-tracking(yes | no) |
override-interval(time) |
priority(integer: 0..4294967295) |
propagation-delay(time) |
Property
Description
# Neighbor
The neighbor menu shows all detected neighbors that are running PIM and their statuses. This menu contains dynamic and read-only entries.
Sub-menu:/routing pimsm neighbor
```
/routing pimsm neighbor
```
Property | Description
----------------------
address(IP%interface) | Shows the neighbor's IP address and local interface the neighbor is detected on.
designated-router(yes | no) | Shows whether the neighbor is elected as Designated Router (DR).
instance(name) | Name of the PIM instance this neighbor is detected on.
join-tracking(yes | no) | Indicates the neighbor's value of a Tracking (T) bit in the LAN Prune Delay option in the Hello message.
override-interval(time) | Indicates the neighbor's value of the override interval in the LAN Prune Delay option in the Hello message.
priority(integer: 0..4294967295) | Indicates the neighbor's priority value.
propagation-delay(time) | Indicates the neighbor's value of the propagation delay in the LAN Prune Delay option in the Hello message.
timeout(time) | Shows the reminding time after the neighbor is removed from the list if no new Hello message is received. The hold time equals to neighbor'shello-period* 3.5.
Property
Description
Shows whether the neighbor is elected as Designated Router (DR).
Indicates the neighbor's value of a Tracking (T) bit in the LAN Prune Delay option in the Hello message.
```
hello-period
```
# Static RP
The static-rp menu allows manually defining the multicast group to RP mappings. Such a mechanism is not robust to failures but does at least provide a basic interoperability mechanism.
Sub-menu:/routing pimsm static-rp
```
/routing pimsm static-rp
```
Property | Description
----------------------
address(IPv4 | IPv6; Default:) | The IP address of the static RP.
group(IPv4 | IPv6; Default:224.0.0.0/4) | The multicast group that belongs to a specific RP.
instance(name; Default:) | Name of the PIM instance this static RP belongs to.
Property
Description
# Upstream Information Base
The upstream information base menus show the any-source multicast (*,G) and source-specific multicast (S,G) groups and their statuses. These menus contain only read-only entries.
Sub-menu:/routing pimsm uib-g
```
/routing pimsm uib-g
```
Property | Description
----------------------
group(IPv4 | IPv6) | The multicast group address.
instance(name) | Name of the PIM instance the multicast group is created on.
rp(IPv4 | IPv6) | The address of the Rendezvous Point for this group.
rp-local(yes | no) | Indicates whether the multicast router itself is RP.
rpf(IP%interface) | The Reverse Path Forwarding (RPF) indicates the router address and outgoing interface that a Join message for that group is directed to.
Property
Description
The address of the Rendezvous Point for this group.
Sub-menu:/routing pimsm uib-sg
```
/routing pimsm uib-sg
```
Property | Description
----------------------
group(IPv4 | IPv6) | The multicast group address.
instance(name) | Name of the PIM instance the multicast group is created on.
keepalive(yes | no) |
register(join | join-pending | prune) |
rpf(IP%interface) | The Reverse Path Forwarding (RPF) indicates the router address and outgoing interface that a Join message for that group is directed to.
source(IPv4 | IPv6) | The source IP address of the multicast group.
spt-bit(yes | no) | The Shortest Path Tree (SPT) bit indicates whether forwarding is taking place on the (S,G) Shortest Path Tree or on the (*,G) tree. A router can have an (S,G) state and still be forwarding on a (*,G) state during the interval when the source-specific tree is being constructed. When SPT bit is false, only the (*,G) forwarding state is used to forward packets from S to G. When SPT bit is true, both (*,G) and (S,G) forwarding states are used.
Property
Description
The Shortest Path Tree (SPT) bit indicates whether forwarding is taking place on the (S,G) Shortest Path Tree or on the (*,G) tree. A router can have an (S,G) state and still be forwarding on a (*,G) state during the interval when the source-specific tree is being constructed. When SPT bit is false, only the (*,G) forwarding state is used to forward packets from S to G. When SPT bit is true, both (*,G) and (S,G) forwarding states are used.