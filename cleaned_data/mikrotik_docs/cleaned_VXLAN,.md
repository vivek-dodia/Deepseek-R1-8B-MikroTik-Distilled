# Document Information
Title: VXLAN
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/100007937/VXLAN,

# Content
# Introduction
Virtual eXtensible Local Area Network (VXLAN) is a tunneling protocol designed to solve the problem of limited VLAN IDs (4096) in IEEE 802.1Q, and it is described by IETF RFC 7348. With VXLAN the size of the identifier is expanded to 24 bits (16777216). It creates a Layer 2 overlay scheme on a Layer 3 network and the protocol runs over UDP. RouterOS VXLAN interface supports IPv4 or IPv6 (since version 7.6), but dual-stack is not supported.
Only devices within the same VXLAN segment can communicate with each other. Each VXLAN segment is identified through a 24-bit segment ID, termed the VXLAN Network Identifier (VNI). Unlike most tunnels, a VXLAN is a 1-to-N network, not just point-to-point. VXLAN endpoints, which terminate VXLAN tunnels are known as VXLAN tunnel endpoints (VTEPs). RouterOS only supports statically configured remote VTEPs. When unicast traffic needs to be sent over VXLAN, a device can learn the IP address of the other endpoint dynamically in a manner similar to a learning bridge, and forward traffic only to the necessary VTEP. For traffic that needs to be flooded (broadcast, unknown-unicast, and multicast) to all VTEPs on the same segment, VXLAN can use multicast or unicast with head-end replication to send one replica for every remote VTEP.
# Configuration options
This section describes the VXLAN interface and VTEP configuration options.
Sub-menu:/interface vxlan
```
/interface vxlan
```
Property | Description
----------------------
allow-fast-path(yes | no; Default:yes) | Whether to allowFast Pathprocessing. Fragmented and flooded packets over VXLANare redirected via a slow path. Fast Path is disabled for VXLAN interface that uses VRF. The setting is available since RouterOS version 7.8.
arp(disabled | enabled | local-proxy-arp | proxy-arp | reply-only; Default:enabled) | Address Resolution Protocol settingdisabled- the interface will not use ARPenabled- the interface will use ARPlocal-proxy-arp-the router performs proxy ARP on the interface and sends replies to the same interfaceproxy-arp-the router performs proxy ARP on the interface and sends replies to other interfacesreply-only- the interface will only reply to requests originating from matching IP address/MAC address combinations which are entered as static entries in theIP/ARPtable. No dynamic entries will be automatically stored in theIP/ARPtable. Therefore for communications to be successful, a valid static entry must already exist.
arp-timeout(auto | integer; Default:auto) | How long the ARP record is kept in the ARP table after no packets are received from IP. Valueautoequals to the value ofarp-timeoutinIP/Settings, default is the 30s.
bridge(name; Default: ) | Name of thebridgeinterface to which VXLAN interface will be added as a slave port.
bridge-pvid(integer 1..4094;Default:1) | Used to assign PVID parameter for dynamically bridge port. This property only has an effect when bridge vlan-filtering is set to yes.
comment(string; Default: ) | Short description of the interface.
disabled(yes | no; Default:no) | Changes whether the interface is disabled.
dont-fragment(auto | disabled | enabled | inherit; Default:auto) | The Don't Fragment (DF) flag controls whether a packet can be broken into smaller packets, called fragments, before being sent over a network. When configuring VXLAN, this setting determines the presence of the DF flag on the outer IPv4 header and can control packet fragmentation if the encapsulated packet exceeds the outgoing interface MTU. This setting has three options:auto- if the device supports VXLAN offloading, the dont-fragment mode will operate asenabled. if VXLAN offloading is not supported, it will use theinheritmode.disabled- the DF flag is not set on the outer IPv4 header, which means that packets can be fragmented if they are too large to be sent over the outgoing interface. This also allows packet fragmentation when VXLAN uses IPv6 underlay.enabled- the DF flag is always set on the outer IPv4 header, which means that packets will not be fragmented and will be dropped if they exceed the outgoing interface's MTU. This also avoids packet fragmentation when VXLAN uses IPv6 underlay.inherit- The DF flag on the outer IPv4 header is based on the inner IPv4 DF flag. If the inner IPv4 header has the DF flag set, the outer IPv4 header will also have it set. If the packet exceeds the outgoing interface's MTU and DF is set, it will be dropped. If the inner packet is non-IP, the outer IPv4 header will not have the DF flag set and packets can be fragmented. If the inner packet is IPv6, the outer IPv4 header will always set the DF flag and packets cannot be fragmented. Note that when VXLAN uses IPv6 underlay, this setting does not have any effect and is treated the same asdisabled.The setting is available since RouterOS version 7.8.
group(IPv4 | IPv6; Default: ) | When specified, a multicast group address can be used to forward broadcast, unknown-unicast, and multicast traffic between VTEPs. This property requires specifying theinterfacesetting. The interface will use IGMP or MLD to join the specified multicast group, make sure to add the necessary PIM and IGMP/MDL configuration. When this property is set, thevteps-ip-versionautomatically gets updated to the used multicast IP version.
hw(yes | no; Default:yes) | Allows to disable hardware offloading, only applies to devices that support VXLAN offloading.
interface(name; Default:) | Interface name used for multicast forwarding. This property requires specifying thegroupsetting.
local-address(IPv4 | IPv6; Default: ) | Specifies the local source address for the VXLAN interface. If not set, one IP address of the egress interface will be selected as a source address for VXLAN packets. When the property is set, thevteps-ip-versionautomatically gets updated to the used local IP version. The setting is available since RouterOS version 7.7.
mac-address(MAC; Default: ) | Static MAC address of the interface. Arandomly generated MAC address will be assigned when not specified.
max-fdb-size(integer: 1..65535; Default:4096) | Limits the maximum number of MAC addresses that VXLAN can store in the forwarding database (FDB).
mtu(integer; Default:1500) | For the maximum transmission unit, the VXLAN interface will set MTU to 1500 by default. Thel2mtuwill be set automatically according to the associatedinterface(subtracting 50 bytes corresponding to the VXLAN header). If no interface is specified, thel2mtuvalue of 65535 is used. Thel2mtucannot be changed.
name(text; Default:vxlan1) | Name of the interface.
port(integer: 1..65535; Default:4789) | Used UDP port number for listening and sending packets to remote VTEPs.
ttl(auto | integer: 0..255; Default:auto) | Specifies the TTL value to use in outgoing packets. By default, the TTL is set to 64 when using theautooption. However, if VXLAN is using a multicast underlay network, the default TTL is set to 1. If the multicast network involves routing, you will need to increase the TTL to a higher value.
vni(integer: 1..16777216; Default:) | VXLAN Network Identifier (VNI).
vrf(name; Default:main) | Set VRF for the VXLAN interface on which the VTEPs listen and make connections. VRF is not supported when usinginterfaceand multicastgroupsettings. The same UDPportcannot be used in multiple routing tables at the same time. The setting is available since RouterOS version 7.7.
vteps-ip-version(ipv4 | ipv6; Default:ipv4) | Used IP protocol version for statically configured VTEPs. The RouterOS VXLAN interface does not support dual-stack, any configured remote VTEPs with the opposite IP version will be ignored. When multicastgrouporlocal-addressproperties are set, thevteps-ip-versionautomatically gets updated to the used IP version. The setting is available since RouterOS version 7.6.
Property
Description
```
disabled
```
```
enabled
```
```
local-proxy-arp
```
```
proxy-arp
```
```
reply-only
```
```
auto
```
```
arp-timeout
```
The Don't Fragment (DF) flag controls whether a packet can be broken into smaller packets, called fragments, before being sent over a network. When configuring VXLAN, this setting determines the presence of the DF flag on the outer IPv4 header and can control packet fragmentation if the encapsulated packet exceeds the outgoing interface MTU. This setting has three options:
```
auto
```
```
enabled
```
```
inherit
```
```
disabled
```
```
enabled
```
```
inherit
```
```
disabled
```
The setting is available since RouterOS version 7.8.
```
interface
```
```
vteps-ip-version
```
```
group
```
```
vteps-ip-version
```
Static MAC address of the interface. Arandomly generated MAC address will be assigned when not specified.
Limits the maximum number of MAC addresses that VXLAN can store in the forwarding database (FDB).
For the maximum transmission unit, the VXLAN interface will set MTU to 1500 by default. Thel2mtuwill be set automatically according to the associatedinterface(subtracting 50 bytes corresponding to the VXLAN header). If no interface is specified, thel2mtuvalue of 65535 is used. Thel2mtucannot be changed.
```
l2mtu
```
```
interface
```
```
l2mtu
```
```
l2mtu
```
Used UDP port number for listening and sending packets to remote VTEPs.
Specifies the TTL value to use in outgoing packets. By default, the TTL is set to 64 when using theautooption. However, if VXLAN is using a multicast underlay network, the default TTL is set to 1. If the multicast network involves routing, you will need to increase the TTL to a higher value.
```
auto
```
VXLAN Network Identifier (VNI).
vrf(name; Default:main)
```
interface
```
```
group
```
```
port
```
Used IP protocol version for statically configured VTEPs. The RouterOS VXLAN interface does not support dual-stack, any configured remote VTEPs with the opposite IP version will be ignored. When multicastgrouporlocal-addressproperties are set, thevteps-ip-versionautomatically gets updated to the used IP version. The setting is available since RouterOS version 7.6.
```
group
```
```
local-address
```
```
vteps-ip-version
```
Sub-menu:/interface vxlan vteps
```
/interface vxlan vteps
```
Property | Description
----------------------
comment(string; Default: ) | Short description of the configured VTEP.
interface(name; Default:) | Name of the VXLAN interface.
remote-ip(IPv4 | IPv6; Default:) | The IPv4 or IPv6 destination address of remote VTEP.
Property
Description
The IPv4 or IPv6 destination address of remote VTEP.
# Forwarding table
Since RouterOS version 7.9, it is possible to monitor the learned MAC addresses from remote VTEPs.
Sub-menu:/interface vxlan fdb
```
/interface vxlan fdb
```
Property | Description
----------------------
interface(read-only:name) | Name of the VXLAN interface.
mac-address(read-only: MAC address) | MAC address.
remote-ip(read-only: IPv4 | IPv6 address) | The IPv4 or IPv6 destination address of remote VTEP.
Property
Description
MAC address.
The IPv4 or IPv6 destination address of remote VTEP.
```
[admin@MikroTik] > /interface vxlan fdb print
0 remote-ip=2001::2 mac-address=56:FF:AA:1A:72:33 interface=vxlan1
1 remote-ip=2002::2 mac-address=AE:EC:C4:12:8B:B9 interface=vxlan1
2 remote-ip=192.168.10.20 mac-address=FE:AF:58:31:A7:B6 interface=vxlan2
```
# Configuration example
This configuration example creates a single VXLAN tunnel between two statically configured VTEP endpoints.
First, create VXLAN interfaces on both routers.
```
/interface vxlan
add name=vxlan1 port=4789 vni=10
```
Then configure VTEPs on both routers with respective IPv4 destination addresses. Both devices should have an active route toward the destination address.
```
# Router1
/interface vxlan vteps
add interface=vxlan1 remote-ip=192.168.10.10
# Router2
/interface vxlan vteps
add interface=vxlan1 remote-ip=192.168.20.20
```
The configuration is complete. It is possible to include the VXLAN interface into a bridge with other Ethernet interfaces.