---
title: VPLS
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/40992798/VPLS,
crawled_date: 2025-02-02T21:11:39.402130
section: mikrotik_docs
type: documentation
---

# Summary
The virtual Private Lan Service (VPLS) interface can be considered a tunnel interface just liketheEoIPinterface. To achieve transparent ethernet segment forwarding between customer sites.
Negotiation of VPLS tunnels can be done by LDP protocol or MP-BGP - both endpoints of tunnel exchange labels they are going to use for the tunnel.
Data forwarding in the tunnel happens by imposing 2 labels on packets: tunnel label and transport label - a label that ensures traffic delivery to the other endpoint of the tunnel.
MikroTik RouterOS implements the following VPLS features:
* VPLS LDP signaling (RFC 4762)
* Cisco style static VPLS pseudowires (RFC 4447 FEC type 0x80)
* VPLS pseudowire fragmentation and reassembly (RFC 4623)
* VPLS MP-BGP based autodiscovery and signaling (RFC 4761)
* Cisco VPLS BGP-based auto-discovery (draft-ietf-l2vpn-signaling-08)
* support for multiple import/export route-target extended communities for BGP based VPLS (both, RFC 4761 and draft-ietf-l2vpn-signaling-08)
# VPLS Prerequisities
For VPLS to be able to transport MPLS packets, one of the label distribution protocols should be already running on the backbone, it can be LDP, RSVP-TE, or static bindings.
Before moving forward, familiarize yourself with theprerequisites required for LDPand prerequisites for RSVP-TE.
In case, if BGP should be used as a VPLS discovery and signaling protocol, the backbone should be running iBGP preferably with route reflector/s.
# Example Setup
Let's consider that we already have a working LDP setup from theLDP configuration example.
Routers R1, R3, and R4 have connected Customer A sites, and routers R1 and R3 have connected Customer B sites. Customers require transparent L2 connectivity between the sites.
# Reference
## General
Sub-menu:/interface vpls
```
/interface vpls
```
List of all VPLS interfaces. This menu shows also dynamically created BGP-based VPLS interfaces.
### Properties
Property | Description
----------------------
arp(disabled | enabled | proxy-arp | reply-only; Default:enabled) | Address Resolution Protocol
arp-timeout(time interval | auto; Default: auto) | 
bridge(name; Default:) | 
bridge-cost(integer [1..200000000]; Default:) | Cost of the bridge port.
bridge-horizon(none | integer; Default:none) | If set tononebridge horizon will not be used.
bridge-pvid(integer 1..4094; Default:1) | Used to assign port VLAN ID (pvid) for dynamically bridged interface. This property only has an effect when bridge vlan-filtering is set to yes.
cisco-static-id(integer [0..4294967295]; Default:0) | Cisco-style VPLS tunnel ID.
comment(string; Default: ) | Short description of the item
disable-running-check(yes | no; Default:no) | Specifies whether to detect if an interface is running or not. If set tonointerface will always havetherunningflag.
disabled(yes | no; Default:yes) | Defines whether an item is ignored or used. By default VPLS interface is disabled.
mac-address(MAC; Default: ) | 
mtu(integer [32..65536]; Default:1500) | 
name(string; Default: ) | Name of the interface
pw-l2mtu(integer [0..65536]; Default:1500) | L2MTU value advertised to a remote peer.
pw-type(raw-ethernet | tagged-ethernet | vpls; Default:raw-ethernet) | Pseudowire type.
peer(IP; Default: ) | The IP address of the remote peer.
pw-control-word(disabled | enabled | default; Default:default) | Enables/disables Control Word usage. Default values for regular and cisco style VPLS tunnels differ. Cisco style by default has control word usage disabled. Read more in theVPLS Control Wordarticle.
vpls-id(AsNum | AsIp; Default: ) | A unique number that identifies the VPLS tunnel. Encoding is 2byte+4byte or 4byte+2byte number.
```
running
```
Read-only properties
Property | Description
----------------------
cisco-bgp-signaled(yes | no) | 
vpls(string) | name of thebgp-vpls instanceused to create dynamic vpls interface
bgp-signaled | 
bgp-vpls | 
bgp-vpls-prfx | 
dynamic(yes | no) | 
l2mtu(integer) | 
running(yes | no) |
### Monitoring
Command/interface vpls monitor [id]will display the current VPLS interface status
```
/interface vpls monitor [id]
```
For example:
```
[admin@10.0.11.23] /interface vpls> monitor vpls2
remote-label: 800000
local-label: 43
remote-status: 
transport: 10.255.11.201/32
transport-nexthop: 10.0.11.201
imposed-labels: 800000
```
Available read-only properties:
Property | Description
----------------------
imposed-label(integer) | VPLS imposed label
local-label(integer) | Local VPLS label
remote-group() | 
remote-label(integer) | Remote VPLS label
remote-status(integer) | 
transport-nexthop(IP prefix) | Shows used transport address (typically Loopback address).
transport(string) | Name of the transport interface. Set if VPLS is running over the Traffic Engineering tunnel.