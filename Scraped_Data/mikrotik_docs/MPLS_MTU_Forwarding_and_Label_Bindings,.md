---
title: MPLS MTU, Forwarding and Label Bindings
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/128974876/MPLS+MTU+Forwarding+and+Label+Bindings,
crawled_date: 2025-02-02T21:11:33.680945
section: mikrotik_docs
type: documentation
---

# Label Range and TTL
From the/mpls settingsmenu it is possible to assign specific dynamic label range and TTL propagation. If for some reason static label mapping is used then the dynamic range can be adjusted to exclude statically assigned label numbers from being dynamically assigned by any of the label distribution protocols.
```
/mpls settings
```
Property | Description
----------------------
dynamic-label-range(range of integer[16..1048575]; Default:16-1048575) | Range of Label numbers used for dynamic allocation. The first 16 labels are reserved for special purposes (as defined in RFC). If you intend to configure labels statically then adjust the dynamic default range not to include numbers that will be used in a static configuration.
propagate-ttl(yes | no; Default:yes) | Whether to copy TTL values from IP header to MPLS header. If this option is set tonothen hops inside the MPLS cloud will be invisible from traceroutes.
allow-fast-path(yes | no; Default:yes) | Enable/disable MPLS fast-path support.
# MPLS MTU
Configuration of MPLS MTU (path MTU + MPLS tag size) is useful in cases when there is a large variety of possible MTUs along the path. Configuring MPLS MTU to a minimum value that can pass all the hops will ensure that the MPLS packet will not be silently dropped on the devices that do not support big enough MTU.
MPLS MTUs are configured from the/mpls interfacemenu.
```
/mpls interface
```
```
[admin@rack1_b35_CCR1036] /mpls/interface> print 
Flags: X - disabled; * - builtin 
 0    ;;; router-test
      interface=ether1 mpls-mtu=1580 input=yes 
 1    ;;; router-test
      interface=ether2 mpls-mtu=1580 input=yes 
 2    interface=all mpls-mtu=1500
```
Properties
Property | Description
----------------------
comment(string; Default: ) | Short description of the interface
disabled(yes | no; Default:no) | If set toyesthen this configuration is ignored.
interface(name; Default:) | Name of the interface or interface-list to match.
input(yes | no; Default:yes) | Whether to allow MPLS input on the interface
mpls-mtu(integer [512..65535]; Default:1508) | The option represents how big packets can be carried over the interface with added MPLS labels.
The order of the entries is important due to the possibility that different interface lists can contain the same interface and in addition, that interface can be referenced directly.
Selection of the MPLS MTU happens in the following manner:
* If the interface matched the entry from this table, then try to use configured MPLS MTU value
* If the interface does not match any entry then consider MPLS MTU equal to L2MTU
* If the interface does not support L2MTU, then consider MPLS MTU equal to L3 MTU
On the MPLS ingress path, MTU is chosen by min(MPLS MTU - tagsize, l3mtu). This means that on interfaces that do not support L2MTU and default L3 MTU is set to 1500, max path MTU will be 1500 - tag size (the interface will not be able to pass full IP frame without fragmentation). In such scenarios, L3MTU must be increased by max observed tag size.
Read more on MTUs in theMTU in RouterOSarticle.
## Forwarding Table
Entries in the/mpls forwarding-tablemenu show label bindings for specific routes that will be used in MPLS label switching. Properties in this menu are read-only.
```
/mpls forwarding-table
```
```
[admin@rack1_b35_CCR1036] /mpls/forwarding-table> print 
Flags: L, V - VPLS
Columns: LABEL, VRF, PREFIX, NEXTHOPS
#   LABEL  VRF   PREFIX         NEXTHOPS                                            
0 L    16  main  10.0.0.0/8     { nh=10.155.130.1; interface=ether12 }              
1 L    18  main  111.111.111.3  { label=impl-null; nh=111.12.0.1; interface=ether2 }
2 L    17  main  111.111.111.2  { label=impl-null; nh=111.11.0.1; interface=ether1 }
```
Property | Description
----------------------
prefix(IP/Mask) | Destination prefix for which labels are assigned
label(integer) | Ingress MPLS label
ldp(yes | no) | Whether labels areLDPsignaled
nexthops() | An array of the next-hops, each entry in the array represents one ECMP next-hop. Array entry can contain several parameters:label- egress MPLS labelnh- out next-hop IP addressinterface- out the interface
out-label(integer) | Label number which is added or switched to for outgoing packet.
packets(integer) | Number of packets matched by this entry
te-sender | 
te-session | 
traffic-eng | Shows whether the entry is signaled by RSVP-TE (Traffic Engineering)
type(string) | Type of the entry, for example, "vpls", etc.
vpls(yes | no) | Shows whether the entry is used forVPLStunnels.
vpn | 
vrf | Name of the VRF table this entry belongs to
An array of the next-hops, each entry in the array represents one ECMP next-hop. Array entry can contain several parameters:
* label- egress MPLS label
* nh- out next-hop IP address
* interface- out the interface