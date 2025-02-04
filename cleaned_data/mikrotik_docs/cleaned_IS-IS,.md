# Document Information
Title: IS-IS
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/201523543/IS-IS,

# Content
# Overview
The IS-IS (Intermediate System - Intermediate System) protocol is an Interior Gateway Protocol (IGP) used to distribute IP routing information throughout a single Autonomous System.
It was originally developed as a routing protocol for CLNP but later extended to include IP routing when IP became popular.  An extended version is sometimes referred to as Integrated IS-IS.
IS-IS belongs to the link-state protocol family, which exchanges topology information between nearest neighbors and floods it throughout the AS. The main advantage is that complete knowledge of the network topology allows one to choose the best path to the destination. It can also be useful for traffic engineering purposes.
Neighbours periodically exchangeHellopackets, forms adjacency and selects designated IS based on the negotiation. Hello packets are sent individually forLevel-1andLevel-2.
Standards and Technologies:
# IS-IS Terminology
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
# ISIS does not work and prints warning message "invalid 3way tlv"
This warning indicates that most likely remote neighbor does not comply  to 3-way handshake for point-to-point networks from RFC 5302. For example, on Cisco you have to enable "isis three-way-handshake ietf" on interface to have 15byte TLV.