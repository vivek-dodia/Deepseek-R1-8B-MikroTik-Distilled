# Document Information
Title: Routing Protocol Overview
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/28606515/Routing+Protocol+Overview,

# Content
# 1Feature Status2Performance Status2.1One Peer Receive Only2.2Two Peers Receive Only2.3Multi-homing Sim2.4Memory Usage:Feature Status
N/A- Feature not yet available
OK- Initial tests successful
NOK- initial tests not successful
Highlight Colors:
Feature | v7.1 | v7.2 | v7.3 | v7.6 | v7.10 | v7.12 | v7.14 | v7.15 | v7.17 | v7.18
-----------------------------------------------------------------------------------
Winbox |  |  |  |  |  |  |  |  |  |
BGP support |  |  |  |  |  |  |  |  |  |
OSPF support |  |  |  |  |  |  |  |  |  |
RIP support |  |  |  |  |  |  |  |  |  |
Router ID support |  |  |  |  |  |  |  |  |  |
Routing filter support |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
Generic |  |  |  |  |  |  |  |  |  |
/31 address support | N/A |  |  |  |  |  |  |  |  |
Convert route rules after upgrade from v6.x |  |  |  |  |  |  |  |  |  |
Static IPv6 upgrade from ROS v6 |  |  |  |  |  |  |  |  |  |
IPv4 Route Rules |  |  |  |  |  |  |  |  |  |
IPv6 Route Rules |  |  |  |  |  |  |  |  |  |
ECMP flags |  |  |  |  |  |  |  |  |  |
dst@table |  |  |  |  |  |  |  |  |  |
gateway@table |  |  |  |  |  |  |  |  |  |
gateway%interface |  |  |  |  |  |  |  |  |  |
recursive route over ipv6 LL address |  |  |  |  |  |  |  |  |  |
3 level recursive gateway with ECMP |  |  |  |  |  |  |  |  |  |
IPV6 ECMP |  |  |  |  |  |  |  |  |  |
IPv6 connected ECMP |  |  |  |  |  |  |  |  |  |
Addresses from same subnet to multiple interfaces | N/A |  |  |  |  |  |  |  |  |
Show time when route was last updated | N/A |  |  |  |  |  |  |  |  |
Check Gateway | BFD not ready |  |  |  |  |  |  |  |  |
Scope and target scope |  |  |  |  |  |  |  |  |  |
IPv4 Mangle routing-mark |  |  |  |  |  |  |  |  |  |
IPv6 Mangle routing-mark |  |  |  |  |  |  |  |  |  |
Packet SRC address | Does not work correctly with /32 addresses |  |  |  |  |  |  |  |  |
Routing-table parameter for ping and telnet |  |  |  |  |  |  |  |  |  |
Show if route is hardware accelerated | Shows if route is candidate for HW acceleration |  |  |  |  |  |  |  |  |
Custom route selection policy |  |  |  |  |  |  |  |  |  |
IPv4 with IPv6 nexthops for RFC5549 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
Routing id |  |  |  |  |  |  |  |  |  |
VRF |  |  |  |  |  |  |  |  |  |
Management services support for VRFs | telnet, ssh, api, www services can be set to listen on specific VRF |  |  |  |  |  |  |  |  |
Dynamically import/export routes from one vrf to another within the same router | N/A |  |  |  |  |  |  |  |  |
BFD | N/A |  |  |  | Initial support |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
OSPF |  |  |  |  |  |  |  |  |  |
Convert OSPF config from v6 to v7 after upgrade | Known conversion problems:NBMA neighbors place in backboneospf-v2 networks + interface may have issuesdynamic interfaces may have issuesMPLS PE CE features are not converted |  |  |  |  |  |  |  |  |
OSPF neighbors in NSSA Area |  |  |  |  |  |  |  |  |  |
OSPF in broadcast network |  |  |  |  |  |  |  |  |  |
OSPF with routing filters |  |  |  |  |  |  |  |  |  |
OSPF Virtual Link |  |  |  |  |  |  |  |  |  |
OPSF input filtering |  |  |  |  |  |  |  |  |  |
HMAC-SHA auth RFC5709 | N/A |  |  | Initial support |  |  |  |  |  |
OSPF SNMP monitoring | N/A |  |  |  |  |  |  |  |  |
BGP SNMP monitoring |  |  |  |  | For ipv4 sessions |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
IS-IS |  |  |  |  |  |  |  |  |  |
IPv4 |  |  |  |  |  | Initial support |  |  |  |
IPv6 |  |  |  |  |  |  |  |  |  |
Traffic Engineering |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
BGP |  |  |  |  |  |  |  |  |  |
Convert BGP config from v6 to v7 after upgrade |  |  |  |  |  |  |  |  |  |
BGP Templates and dynamic peers |  |  |  |  |  |  |  |  |  |
BGP connect listen on a network |  |  |  |  |  |  |  |  |  |
BGP guess remote.as |  |  |  |  |  |  |  |  |  |
Show from which peer route received | OK (/routing/route/print detail --> belongs-to) |  |  |  |  |  |  |  |  |
BGP Address Families |  |  |  |  |  |  |  |  |  |
BGP input.accept-* |  |  |  |  |  |  |  |  |  |
eBGP nexthop self |  |  |  |  |  |  |  |  |  |
Input Filter |  |  |  |  |  |  |  |  |  |
Output Filter |  |  |  |  |  |  |  |  |  |
BGP Local address auto selection |  |  |  |  |  |  |  |  |  |
BGP route reflect |  |  |  |  |  |  |  |  |  |
BGP route server |  |  |  |  |  |  |  |  |  |
BGP Roleshttps://datatracker.ietf.org/doc/draft-ietf-idr-bgp-open-policy/?include_text=1 | rfc roles not fully implemented |  |  |  |  |  |  |  |  |
BGP session uptime in "established" state |  |  |  |  |  |  |  |  |  |
BGP session last established time |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
BGP Flow Spec | Flow spec attributes are forwarded |  |  |  |  |  |  |  |  |
BGP Selection |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
BGP Selection (Multipath) | N/A |  |  |  |  |  |  |  |  |
BGP Confederation |  |  |  |  |  |  |  |  |  |
BGP Aggregation | N/A |  |  |  |  |  |  |  |  |
BGP ORF | N/A |  |  |  |  |  |  |  |  |
Discard prefixRTBHRFC 6666 | N/A |  |  |  |  |  |  |  |  |
AS-wide Unique BGP Identifier RFC 6286 | N/A |  |  |  |  |  |  |  |  |
Exported PDU PCAP saver |  |  |  |  |  |  |  |  |  |
Exported PDU PCAP loader |  |  |  |  |  |  |  |  |  |
BGP Advertisement monitoring |  | Initial implementation by dumping to pcap |  | Advertisements rework |  |  |  |  |  |
BGP Prefix limit |  |  | Initial support |  |  |  |  |  |  |
BGP advertise IPv4 prefix with IPv6 nexthop (RFC5549) |  |  |  |  |  |  |  |  |  |
BGP VPNv6 support |  |  |  |  | Prerequisites are made, need to add actual BGP Afi |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
MPLS |  |  |  |  |  |  |  |  |  |
Static label mapping |  |  |  |  |  |  |  |  |  |
Static mapping upgrade from v6 |  |  |  |  |  |  |  |  |  |
LDP IPv4 mapping |  |  |  |  |  |  |  |  |  |
LDP IPv6 mapping |  |  |  |  |  |  |  |  |  |
LDP signaled VPLS |  |  |  |  |  |  |  |  |  |
LDP config upgrade from v6 |  |  |  |  |  |  |  |  |  |
LDP Dual Stack |  |  |  |  |  |  |  |  |  |
TE |  |  |  |  |  |  |  |  |  |
TE Config upgrade from v6 |  |  |  |  |  |  |  |  |  |
VPLS Encap to TE |  |  |  |  |  |  |  |  |  |
BGP signaled VPLS |  |  |  |  |  |  |  |  |  |
VPLS config upgrade from v6 |  |  |  |  |  |  |  |  |  |
RSVP Fast reroute | N/A |  |  |  |  |  |  |  |  |
FRR/RI-RSVP (RFC 8370) | N/A |  |  |  |  |  |  |  |  |
MPLS ECMP |  |  |  |  |  |  |  |  |  |
One label per VRF |  |  |  |  |  |  |  |  |  |
Ability to use MPLS EXP-bit in Queues | N/A |  |  |  |  |  |  |  |  |
MPLS Fast-Path | N/A |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
RPKI session |  |  |  |  |  |  |  |  |  |
RPKI possibility to view received info of specific prefix |  |  |  |  |  |  |  |  |  |
RPKI show connection status |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
Filters |  |  |  |  |  |  |  |  |  |
Convert routing filters after upgrade from v6.x |  |  |  |  |  |  |  |  |  |
Syntax completion |  |  |  |  |  |  |  |  |  |
Routing filter chain drop by default without rules |  |  |  |  |  |  |  |  |  |
Routing filter prefix match |  |  |  |  |  |  |  |  |  |
Routing filter protocol match |  |  |  |  |  |  |  |  |  |
Routing filter append communities |  |  |  |  |  |  |  |  |  |
Routing filter append large community |  |  |  |  |  |  |  |  |  |
Routing filter set weight |  |  |  |  |  |  |  |  |  |
Routing filter set local pref |  |  |  |  |  |  |  |  |  |
Routing filter set MED |  |  |  |  |  |  |  |  |  |
Routing filter set origin |  |  |  |  |  |  |  |  |  |
Routing filter set igp metric from OSPF cost |  |  |  |  |  |  |  |  |  |
Routing filter match prefix with address list |  |  |  |  |  |  |  |  |  |
Routing filter match community/large community lists |  |  |  |  |  |  |  |  |  |
Routing filter add a prefix to address list | N/A |  |  |  |  |  |  |  |  |
Routing filter validate prefix with RPKI |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
Multicast |  |  |  |  |  |  |  |  |  |
IGMP-Proxy |  |  |  |  |  |  |  |  |  |
PIM-SM | Initial support |  |  |  |  |  |  |  |  |
Feature
v7.15
v7.17
v7.18
Known conversion problems:
ospf-v2 networks + interface may have issues
dynamic interfaces may have issues
MPLS PE CE features are not converted
```
FRR/RI-RSVP (RFC 8370)
```
# Performance Status
Used hardware:
The simulated upstream peer is a CHR router running ROSv6 with a copy of the global IPv4 routing table (585K routes loaded from MRT dump).
# One Peer Receive Only
DUT establishes a connection to simulated upstream peers, receives routes, and installs them in FIB.
| v6.44 | v7.1beta3 | v7.1rc7 | v7.15.3 (1008427 routes) | v7.16 (1008427 routes)
----------------------------------------------------------------------------------
CCR | 0:40 - 2:12 | 0:46 |  |  |
RB1100x4 1.4GHz | 0:32-0:38 | 0:23 |  |  |
CCR2004 | 0:32 | 0:18 |  |  |
x86 (CHR) | 0:20 |  |  |  |
RB450G (in/out affinity=alone) | after trying for 9min - ran out of memory at 558K routes | 2:02 (121MB free) |  |  |
RB450G (in/out affinity=main) | - | 1:54 |  |  |
RB450G (affinity in=alone out=input) | - | 2:12 |  |  |
CCR2116 |  |  |  | 0:36 | 0:34
CCR2216 |  |  |  | 0:39 | 0:34
CCR2216 (150 regexp as-path rules) |  |  |  |  | 2:09
# Two Peers Receive Only
DUT establishes a connection to two simulated upstream peers, receives routes, picks the best route, and installs in FIB. On ROSv7 affinity settings are set to "alone".
| v6.44 | FRR | v7.1beta3 | v7.1rc7 (846k routes per peer)
-----------------------------------------------------------
CCR | 1:01 - 2:45 |  | 1:11 |
RB1100x4 1.4GHz | 0:51 |  | 0:30 |
CCR2004 | 0:51 |  | 0:29 | 0:33
router x |  |  |  | 0:40
x86 (CHR) | 0:25 |  |  |
x86 (virtual) |  | 0:26(4cores) |  |
|  | 0:46(2cores) |  |
|  | 0:30(2cores no LDP) |  |
# Multi-homing Sim
Two DUT devices establish eBGP sessions to simulated x86 upstream routers. Both DUTs are interconnected with the iBGP session. Each DUT receives routes from upstream and readvertises routes over iBGP. On ROSv7 affinity, settings are set to "alone" and early-cut disabled.
v7.1beta3 | 1:11
v7.1beta2 | 1:29
v6.xx | 1:02 - 8:30
v7.1beta3 | 0:36
v6.xx | 0:59
| Time | Mem
v7.15.3 | 0:59 | 285MB
v7.16 | 0:48 | 297MB
Route Server
| Time | Mem
v7.15.3 | - | -MB
v7.16 | - | -MB
-MB
# Memory Usage:
```
Columns: TASKS, PRIVATE-MEM-BLOCKS, SHARED-MEM-BLOCKS, PSS, RSS, VMS, RETIRED, ID, PID, RPID, PROCESS-TIME, KERNEL-TIME, CUR-BUSY, MAX-BU>
# TASKS                         PRIVATE-M  SHARED-M  P  R  V  RE  ID       PID  R  PROCESS-  KERNEL-  CUR  MAX-BUS  CUR  MAX-CALC
0  routing tables                12.0MiB    30.2MiB   0  0  0  12  main     111  0  8s980ms   2s60ms   0ms  1s320ms  0ms  10s700ms
rib
connected networks
1  fib                           2816.0KiB  0         0  0  0      fib      130  1  3s        4s660ms       7s220ms       7s220ms
2  ospf                          512.0KiB   256.0KiB  0  0  0      ospf     137  1  1s220ms   130ms         980ms         1s40ms
connected networks
3  fantasy                       256.0KiB   0         0  0  0      fantasy  138  1  60ms      80ms          40ms          40ms
4  configuration and reporting   3840.0KiB  512.0KiB  0  0  0      static   139  1  1s270ms   110ms         260ms         260ms
5  rip                           512.0KiB   0         0  0  0      rip      136  1  120ms     70ms          60ms          120ms
connected networks
6  routing policy configuration  768.0KiB   768.0KiB  0  0  0      policy   133  1  2s290ms   3s170ms       80ms          80ms
7  BGP service                   768.0KiB   0         0  0  0      bgp      134  1  2s760ms   5s480ms       20ms          60ms
connected networks
8  BFD service                   512.0KiB   0         0  0  0      12       135  1  100ms     90ms          40ms          120ms
connected networks
9  BGP Input 10.155.101.186      3072.0KiB  6.2MiB    0  0  0      20       183  1  1s350ms   1s190ms       20ms          20ms
10  BGP Output 10.155.101.186     5.5MiB     0         0  0  0      21       184  1  5s400ms   500ms         3s880ms       3s880ms
11  BGP Input 10.155.101.232      3072.0KiB  6.2MiB    0  0  0      22       187  1  970ms     740ms         20ms          20ms
12  BGP Output 10.155.101.232     8.2MiB     0         0  0  0      23       188  1  10s830ms  960ms         7s            7s
13  Global memory                            256.0KiB               global     0  0
```