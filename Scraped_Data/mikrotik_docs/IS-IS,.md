---
title: IS-IS
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/201523543/IS-IS,
crawled_date: 2025-02-02T21:12:27.200563
section: mikrotik_docs
type: documentation
---

* 1Overview
* 2IS-IS Terminology
* 3Basic Configuration Example
* 4Troubleshooting4.1ISIS does not work and prints warning message "invalid 3way tlv"
* 4.1ISIS does not work and prints warning message "invalid 3way tlv"
# Overview
The IS-IS (Intermediate System - Intermediate System) protocol is an Interior Gateway Protocol (IGP) used to distribute IP routing information throughout a single Autonomous System.
It was originally developed as a routing protocol for CLNP but later extended to include IP routing when IP became popular.  An extended version is sometimes referred to as Integrated IS-IS.
IS-IS belongs to the link-state protocol family, which exchanges topology information between nearest neighbors and floods it throughout the AS. The main advantage is that complete knowledge of the network topology allows one to choose the best path to the destination. It can also be useful for traffic engineering purposes.
Neighbours periodically exchangeHellopackets, forms adjacency and selects designated IS based on the negotiation. Hello packets are sent individually forLevel-1andLevel-2.
Standards and Technologies:
* RFC 1195Use of OSI IS-IS for Routing in TCP/IP and Dual Environments
* RFC 5302Domain-Wide Prefix Distribution with Two-Level IS-IS
* RFC 5303Three-Way Handshake for IS-IS Point-to-Point Adjacencies
* RFC 5305IS-IS Extensions for Traffic Engineering (only wide metric support)
* RFC 5308Routing IPv6 with IS-IS
# IS-IS Terminology
* IS- Intermediate System is a router capable of forwarding traffic between distantly located hosts.
* LSP-Link State PDU contains information on the router's local state (usable interfaces, reachable neighbours, and the cost of the interfaces)
* SPF- Shortest-path-first algorithm
* DIS- designated intermediate system. DIS ensures that all routes in the network maintain synchronised database.Separate DISs are elected for L1 and L2 routing. Election of the DIS is based on the highest interface priority.
* Level-1 (L1) routing- Controls distribution of routing information within an IS-IS area. L1 routing is based on system ID.
* Level-2 (L2) routing- Controls distribution of routing information between IS-IS areas. L2 routing is based on area ID.
* IS-IS Adjacency- link between IS-IS neighbours. The type of adjacency formed depends on the parameters exchanged in the IS-IS Hello packets. Each of the the adjacent routers runs the DIS election process to determine whether it is eligible to be an L1 or L2 DIS on the broadcast network.
# Basic Configuration Example
Basic IS-IS setup between three routers.
R1:
```
/routing isis instance
add afi=ip areas=49.2222 disabled=no name=isis-instance-1 system-id=90ab.cdef.0001
/routing isis interface-template
add instance=isis-instance-1 interfaces=ether1 levels=l1,l2
[] /routing/isis/neighbor> print 
 0 instance=isis-instance-1 interface=ether1 level-type=l2 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 
 1 instance=isis-instance-1 interface=ether1 level-type=l2 snpa=D4:CA:6D:78:2F:2E srcid="1111.2222.cded" state=up 
 2 instance=isis-instance-1 interface=ether1 level-type=l1 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 
 3 instance=isis-instance-1 interface=ether1 level-type=l1 snpa=D4:CA:6D:78:2F:2E srcid="1111.2222.cded" state=up 
[] /routing/route> print where is-is
Flags: A - ACTIVE; i - IS-IS
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS        GATEWAY                AFI  DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW         
 i 0.0.0.0/0          10.155.101.214%ether1  ip4       115     20            10  10.155.101.214%ether1
 i 10.155.101.0/24    10.155.101.216%ether1  ip4       115     20            10  10.155.101.216%ether1
Ai 10.255.255.162/32  10.155.101.216%ether1  ip4       115     20            10  10.155.101.216%ether1
```
R2:
```
/routing isis instance
add afi=ip areas=49.2222 disabled=no l1.originate-default=always l2.originate-default=always name=isis-instance-1 \
    system-id=1111.2222.cded
/routing isis interface-template
add instance=isis-instance-1 interfaces=sfp12 levels=l1,l2
add instance=isis-instance-1 interfaces=lo levels=l2
[] /routing/isis/neighbor> print 
 0 instance=isis-instance-1 interface=sfp12 level-type=l1 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 
 1 instance=isis-instance-1 interface=sfp12 level-type=l1 snpa=C4:AD:34:43:EA:5C srcid="90ab.cdef.0001" state=up 
 2 instance=isis-instance-1 interface=sfp12 level-type=l2 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 
 3 instance=isis-instance-1 interface=sfp12 level-type=l2 snpa=C4:AD:34:43:EA:5C srcid="90ab.cdef.0001" state=up
```
R3 Cisco:
```
interface Loopback0
 ip address 10.255.255.162 255.255.255.255
 ip router isis 
!
interface GigabitEthernet1
 ip address dhcp
 ip router isis 
 negotiation auto
!
router isis
 net 49.2222.1111.2222.aded.00
!
# show isis neighbors 
Tag null:
System Id      Type Interface   IP Address      State Holdtime Circuit Id
90AB.CDEF.0001 L1   Gi1         10.155.101.183  UP    27       1111.2222.CDED.01  
90AB.CDEF.0001 L2   Gi1         10.155.101.183  UP    27       1111.2222.CDED.01  
1111.2222.CDED L1   Gi1         10.155.101.214  UP    9        1111.2222.CDED.01  
1111.2222.CDED L2   Gi1         10.155.101.214  UP    9        1111.2222.CDED.01 
# show ip route
i*L1  0.0.0.0/0 [115/11] via 10.155.101.214, 4w5d, GigabitEthernet1
      10.0.0.0/8 is variably subnetted, 5 subnets, 2 masks
C        10.155.101.0/24 is directly connected, GigabitEthernet1
L        10.155.101.216/32 is directly connected, GigabitEthernet1
i L2     10.155.255.214/32 [115/10] via 10.155.101.183, 2w3d, GigabitEthernet1
```
# Troubleshooting
## ISIS does not work and prints warning message "invalid 3way tlv"
This warning indicates that most likely remote neighbor does not comply  to 3-way handshake for point-to-point networks from RFC 5302. For example, on Cisco you have to enable "isis three-way-handshake ietf" on interface to have 15byte TLV.