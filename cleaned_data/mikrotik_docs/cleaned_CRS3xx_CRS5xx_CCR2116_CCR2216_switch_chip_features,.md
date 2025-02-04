# Document Information
Title: CRS3xx, CRS5xx, CCR2116, CCR2216 switch chip features
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/30474317/CRS3xx+CRS5xx+CCR2116+CCR2216+switch+chip+features,

# Content
# Summary
The CCR3xx, CRS5xx series switches and CCR2116, CCR2216 routers have highly integrated switches with high-performance CPU and feature-rich packet processors. These devices can be designed into various Ethernet applications including unmanaged switch, Layer 2 managed switch, carrier switch, inter-VLAN router, and wired unified packet processor.
# Features
Features | Description
----------------------
Forwarding | Configurable ports for switching or routingFull non-blocking wire-speed switchingLarge Unicast FDB for Layer 2 unicast forwardingForwarding Databases works based on IVLJumbo frame supportIGMP Snooping supportDHCP Snooping with Option 82
Routing | Layer 3 Hardware Offloading:IPv4, IPv6 Unicast RoutingSupported on Ethernet, Bridge, Bonding, and VLAN interfacesECMPBlackholesOffloaded Fasttrack connections1Offloaded NAT for Fasttrack connections1Multiple MTU profiles
Spanning Tree Protocol | STPRSTPMSTPEdge port, BPDU Guard, Root Guard
Mirroring | Various types of mirroring:Port based mirroringVLAN based mirroringMAC based mirroringRemote Switch Port Analyzer (RSPAN)
VLAN | Fully compatible with IEEE802.1Q and IEEE802.1ad VLAN4k active VLANsFlexible VLAN assignment:Port based VLANProtocol based VLANMAC based VLANVLAN filteringIngress VLAN translationMultiple VLAN Registration protocol (MVRP)
Bonding | Supports 802.3ad (LACP), balance-xor and active-backup modesUp to 8 member ports per bonding interfaceHardware automatic failover and load balancingMLAG
Quality of Service (QoS) | Eight output queues per portDSCP and 802.1p PCP mappingPort based Layer2 and Layer3 trust settingsPort and Queue based egress rate limiterPolicy based QoS via ACL rulesStrict Priority (SP) and Shaped Deficit Weighted Round Robin (SDWRR) queuingEnhanced Transmission Selection (ETS) schedulingWeighted Random Early Detection (WRED)1Explicit Congestion Notification (ECN)1Priority-based Flow Control (PFC)1Resource allocation control (queue, shared-pool and multicast based) with extensive monitoring capabilitiesCompatible with Dante enviromentsCompatible with RDMA over Converged Ethernet (RoCE) enviroment1Ingress traffic limiting (port based or via ACL rules)Traffic storm control
Port isolation | Applicable for Private VLAN implementation
Access Control List | Ingress ACL tablesClassification based on ports, L2, L3, L4 protocol header fieldsACL actions include filtering, forwarding and modifying of the protocol header fields
PTP | Two-step Ordinary Clock and Boundary Clock.Hardware timestamping, ensuring clock syncronization in nanosecond(ns) range.IPv4 and Layer 2 (L2) multicast transport modes.End-to-End (E2E) and Peer-to-Peer (P2P) delay mechanisms.IEEE 1588-2008 (PTPv2)Profile Support for:802.1AS: Audio Video Bridging (AVB) and Time-Sensitive Networking (TSN).AES67: High-performance audio-over-IP interoperability.G.8275.1: Frequency and phase synchronization in PTP-aware networks.SMPTE: Audio/video synchronization in professional broadcast environments
Eight output queues per port
DSCP and 802.1p PCP mapping
Port based Layer2 and Layer3 trust settings
Port and Queue based egress rate limiter
Policy based QoS via ACL rules
Strict Priority (SP) and Shaped Deficit Weighted Round Robin (SDWRR) queuing
Enhanced Transmission Selection (ETS) scheduling
Weighted Random Early Detection (WRED)1
Explicit Congestion Notification (ECN)1
Priority-based Flow Control (PFC)1
Resource allocation control (queue, shared-pool and multicast based) with extensive monitoring capabilities
Compatible with Dante enviroments
Compatible with RDMA over Converged Ethernet (RoCE) enviroment1
Ingress traffic limiting (port based or via ACL rules)
Traffic storm control
# Models
This table clarifies the main differences between Cloud Router Switch models and CCR routers.
Model | Switch Chip | CPU | Cores | 10G SFP+ | 10G Ethernet | 25G SFP28 | 40G QSFP+ | 100G QSFP28 | ACL rules | Unicast FDB entries | Jumbo Frame (Bytes)
netPower 15FR (CRS318-1Fi-15Fr-2S) | Marvell-98DX224S | 800MHz | 1 | - | - | - | - | - | 128 | 16,000 | 10218
netPower 16P (CRS318-16P-2S+) | Marvell-98DX226S | 800MHz | 1 | 2 | - | - | - | - | 128 | 16,000 | 10218
CRS310-1G-5S-4S+ (netFiber 9/IN) | Marvell-98DX226S | 800MHz | 1 | 4 | - | - | - | - | 128 | 16,000 | 10218
CRS320-8P-8B-4S+RM | Marvell-98DX226S | 800MHz | 2 | 4 | - | - | - | - | 128 | 16,000 | 10218
CRS326-24G-2S+ (RM/IN) | Marvell-98DX3236 | 800MHz | 1 | 2 | - | - | - | - | 128 | 16,000 | 10218
CRS328-24P-4S+ | Marvell-98DX3236 | 800MHz | 1 | 4 | - | - | - | - | 128 | 16,000 | 10218
CRS328-4C-20S-4S+ | Marvell-98DX3236 | 800MHz | 1 | 4 | - | - | - | - | 128 | 16,000 | 10218
CRS305-1G-4S+ | Marvell-98DX3236 | 800MHz | 1 | 4 | - | - | - | - | 128 | 16,000 | 10218
CRS309-1G-8S+ | Marvell-98DX8208 | 800MHz | 2 | 8 | - | - | - | - | 1024 | 32,000 | 10218
CRS317-1G-16S+ | Marvell-98DX8216 | 800MHz | 2 | 16 | - | - | - | - | 1024 | 128,000 | 10218
CRS312-4C+8XG | Marvell-98DX8212 | 650MHz | 1 | 4 (combo ports) | 8 + 4 (combo ports) | - | - | - | 512 | 32,000 | 10218
CRS326-24S+2Q+ | Marvell-98DX8332 | 650MHz | 1 | 24 | - | - | 2 | - | 256 | 32,000 | 10218
CRS326-4C+20G+2Q+RM | Marvell-98DX8332 | 650MHz | 1 | 4 (combo ports) | - | - | 2 | - | 256 | 32,000 | 10218
CRS354-48G-4S+2Q+ | Marvell-98DX3257 | 650MHz | 1 | 4 | - | - | 2 | - | 170 | 32,000 | 10218
CRS354-48P-4S+2Q+ | Marvell-98DX3257 | 650MHz | 1 | 4 | - | - | 2 | - | 170 | 32,000 | 10218
CRS504-4XQ (IN/OUT) | Marvell-98DX4310 | 650MHz | 1 | - | - | - | - | 4 | 1024 | 128,000 | 10218
CRS510-8XS-2XQ-IN | Marvell-98DX4310 | 650MHz | 1 | - | - | 8 | - | 2 | 1024 | 128,000 | 10218
CRS518-16XS-2XQ | Marvell-98DX8525 | 650MHz | 1 | - | - | 16 | - | 2 | 1024 | 128,000 | 10218
CRS520-4XS-16XQ-RM | Marvell-98CX8410 | 2000MHz | 4 | - | 2 | 4 | - | 16 | 682 | 256,000 | 9570
CCR2116-12G-4S+ | Marvell-98DX3255 | 2000MHz | 16 | 4 | - | - | - | - | 512 | 32,000 | 9570
CCR2216-1G-12XS-2XQ | Marvell-98DX8525 | 2000MHz | 16 | - | - | 12 | - | 2 | 1024 | 128,000 | 9570
# Abbreviations
# Port switching
In order to set up a port switching, check theBridge Hardware Offloadingpage.
# VLAN
Since RouterOS version 6.41, a bridge provides VLAN aware Layer2 forwarding and VLAN tag modifications within the bridge. This set of features makes bridge operation more like a traditional Ethernet switch and allows to overcome Spanning Tree compatibility issues compared to the configuration when tunnel-like VLAN interfaces are bridged. Bridge VLAN Filtering configuration is highly recommended to comply with STP (802.1D), RSTP (802.1w) standards and it is mandatory to enable MSTP (802.1s) support in RouterOS.
# VLAN Filtering
VLAN filtering is described on theBridge VLAN Filteringsection.
VLAN setup examples
Below are describes some of the most common ways how to utilize VLAN forwarding.
# Port-Based VLAN
The configuration is described on theBridge VLAN FIlteringsection.
# MAC Based VLAN
Enable switching on ports by creating a bridge with enabled hw-offloading:
```
/interface bridge
add name=bridge1 vlan-filtering=yes
/interface bridge port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
```
Add VLANs in the Bridge VLAN table and specify ports:
```
/interface bridge vlan
add bridge=bridge1 tagged=ether2 untagged=ether7 vlan-ids=200,300,400
```
Add Switch rules which assign VLAN id based on MAC address:
```
/interface ethernet switch rule
add switch=switch1 ports=ether7 src-mac-address=A4:12:6D:77:94:43/FF:FF:FF:FF:FF:FF new-vlan-id=200
add switch=switch1 ports=ether7 src-mac-address=84:37:62:DF:04:20/FF:FF:FF:FF:FF:FF new-vlan-id=300
add switch=switch1 ports=ether7 src-mac-address=E7:16:34:A1:CD:18/FF:FF:FF:FF:FF:FF new-vlan-id=400
```
# Protocol Based VLAN
Enable switching on ports by creating a bridge with enabled hw-offloading:
```
/interface bridge
add name=bridge1 vlan-filtering=yes
/interface bridge port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```
Add VLANs in the Bridge VLAN table and specify ports:
```
/interface bridge vlan
add bridge=bridge1 tagged=ether2 untagged=ether6 vlan-ids=200
add bridge=bridge1 tagged=ether2 untagged=ether7 vlan-ids=300
add bridge=bridge1 tagged=ether2 untagged=ether8 vlan-ids=400
```
Add Switch rules which assign VLAN id based on MAC protocol:
```
/interface ethernet switch rule
add mac-protocol=ip new-vlan-id=200 ports=ether6 switch=switch1
add mac-protocol=ipx new-vlan-id=300 ports=ether7 switch=switch1
add mac-protocol=0x80F3 new-vlan-id=400 ports=ether8 switch=switch1
```
# VLAN Tunneling (Q-in-Q)
Since RouterOS v6.43 it is possible to use a provider bridge (IEEE 802.1ad) and Tag Stacking VLAN filtering, and hardware offloading at the same time. The configuration is described in theBridge VLAN Tunneling (Q-in-Q)section.
# Ingress VLAN translation
It is possible to translate a certain VLAN ID to a different VLAN ID using ACL rules on an ingress port. In this example we create two ACL rules, allowing bidirectional communication. This can be done by doing the following.
Create a new bridge and add ports to it with hardware offloading:
```
/interface bridge
add name=bridge1 vlan-filtering=no
/interface bridge port
add interface=ether1 bridge=bridge1 hw=yes
add interface=ether2 bridge=bridge1 hw=yes
```
Add ACL rules to translate a VLAN ID in each direction:
```
/interface ethernet switch rule
add new-dst-ports=ether2 new-vlan-id=20 ports=ether1 switch=switch1 vlan-id=10
add new-dst-ports=ether1 new-vlan-id=10 ports=ether2 switch=switch1 vlan-id=20
```
Add both VLAN IDs to the bridge VLAN table:
```
/interface bridge vlan
add bridge=bridge1 tagged=ether1 vlan-ids=10
add bridge=bridge1 tagged=ether2 vlan-ids=20
```
Enable bridge VLAN filtering:
```
/interface bridge set bridge1 vlan-filtering=yes
```
# (R/M)STP
CRS3xx, CRS5xx series switches, and CCR2116, CCR2216 routers are capable of running STP, RSTP, and MSTP on a hardware level. For more detailed information you should check out theSpanning Tree Protocolmanual page.
# Bonding
CRS3xx, CRS5xx series switches and CCR2116, CCR2216 routers support hardware offloading with bonding interfaces. Only802.3adandbalance-xorbonding modes are hardware offloaded, other bonding modes will use the CPU's resources. You can find more information about the bonding interfaces in theBonding Interfacesection. If802.3admode is used, then LACP (Link Aggregation Control Protocol) is supported.
```
802.3ad
```
```
balance-xor
```
```
802.3ad
```
To create a hardware offloaded bonding interface, you must create a bonding interface with a supported bonding mode:
```
/interface bonding
add mode=802.3ad name=bond1 slaves=ether1,ether2
```
This interface can be added to a bridge alongside other interfaces:
```
/interface bridge
add name=bridge
/interface bridge port
add bridge=bridge interface=bond1 hw=yes
add bridge=bridge interface=ether3 hw=yes
add bridge=bridge interface=ether4 hw=yes
```
Make sure that the bonding interface is hardware offloaded by checking the "H" flag:
```
/interface bridge port print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload
# INTERFACE                                 BRIDGE                                 HW
0   H bond1                                     bridge                                 yes
1   H ether3                                    bridge                                 yes
2   H ether4                                    bridge                                 yes
```
# Multi-chassis Link Aggregation Group
MLAG (Multi-chassis Link Aggregation Group) implementation in RouterOS allows configuring LACP bonds on two separate devices, while the client device believes to be connected on the same machine. This provides a physical redundancy in case of switch failure. All CRS3xx, CRS5xx series and CCR2116, CCR2216 devices can be configured with MLAG. Readherefor more information.
# L3 Hardware Offloading
Layer3 hardware offloading (otherwise known as IP switching or HW routing) will allow to offload some of the router features onto the switch chip. This allows reaching wire speeds when routing packets, which simply would not be possible with the CPU.
Offloaded feature set depends on the used chipset. Readherefor more info.
# Port isolation
Since RouterOS v6.43 is it possible to create a Private VLAN setup, an example can be found in theSwitch chip port isolationmanual page. Hardware offloaded bonding interfaces are not included in the switch port-isolation menu, but it is still possible to configure port-isolation individually oneach secondary interface of the bonding.
# IGMP/MLD Snooping
CRS3xx, CRS5xx series switches and CCR2116, CCR2216 routers are capable of using IGMP/MLD Snooping on a hardware level. To see more detailed information, you should check out theIGMP/MLD snoopingmanual page.
# DHCP Snooping and DHCP Option 82
CRS3xx, CRS5xx series switches and CCR2116, CCR2216 routers are capable of using DHCP Snooping with Option 82 on a hardware level. The switch will create a dynamic ACL rule to capture the DHCP packets and redirect them to the main CPU for further processing. To see more detailed information, please visit theDHCP Snooping and DHCP Option 82manual page.
# Controller Bridge and Port Extender
Controller Bridge (CB) and Port Extender (PE) is an IEEE 802.1BR standard implementation in RouterOS. It allows virtually extending the CB ports with a PE device and managing these extended interfaces from a single controlling device. Such configuration provides a simplified network topology, flexibility, increased port density, and ease of manageability. See more details onController Bridge and Port Extender manual.
# Mirroring
Mirroring is a function that allows a network switch to duplicate all the data passing through it and send a copy to another specified port, known as themirror-target. This feature is useful for setting up a tap device, which allows for analyzing network traffic using a separate device. You can set up mirroring in a simple way by designating source ports (seemirror-egressandmirror-ingressin/interface/ethernet/switch/port), or you can configure more advanced mirroring based on different criteria (seemirrorin/interface/ethernet/switch/rule).
```
mirror-target
```
```
mirror-egress
```
```
mirror-ingress
```
```
/interface/ethernet/switch/port
```
```
mirror
```
```
/interface/ethernet/switch/rule
```
It is important to note that themirror-targetport must be on the same switch. You can check the device block diagram or navigate to the/interface/ethernetmenu to identify which interfaces are connected where. When setting up the configration, it is not mandatory to add themirror-targetinterface to the same hardware offloaded bridge where the source ports are set up. Themirror-targetport can be a standalone interface (not configured as a bridge port), or it can be within a bridge setup. When using themirror-targetwith a bridge, note that data and mirrored traffic may both travel on the same LAN. In such cases, consider employing RSPAN (Remote Switch Port Analyzer), where mirrored traffic is encapsulated into a separate VLAN before being transmitted over the network.
```
mirror-target
```
```
/interface/ethernet
```
```
mirror-target
```
```
mirror-target
```
```
mirror-target
```
Additionally, you can set themirror-targetport to a special value "cpu", which means that the copied packets will be sent to the switch chip's CPU port.
```
mirror-target
```
# Configuration examples
# Port Based Mirroring
Starting from RouterOS version 7.15, it is possible to configure multiple source ports and selectively choose whether to mirror incoming traffic, outgoing traffic, or both. In this example, both incoming and outgoing traffic from theether2interface will be copied and sent to theether3interface for monitoring or analysis.
```
# Since RouterOS v7.15
/interface ethernet switch port
set ether2 mirror-egress=yes mirror-ingress=yes
/interface ethernet switch
set switch1 mirror-target=ether3
# Older RouterOS:
/interface ethernet switch
set switch1 mirror-source=ether2 mirror-target=ether3
```
# VLAN Based Mirroring
Using ACL rules, it is possible to mirror packets from multiple interfaces using theportssetting. Additionally, you can specify more detailed criteria such as VLAN ID, MAC/IP address or TCP/UDP port. Onlyingresspackets are mirrored tomirror-targetinterface. This example will mirror incoming VLAN 11 traffic from theether2interface, and send copies to theether3interface. To use an ACL rule with avlan-idmatcher, you need to havebridge vlan-filteringenabled.
```
ports
```
```
mirror-target
```
```
vlan-id
```
```
/interface bridge
set bridge1 vlan-filtering=yes
/interface ethernet switch
set switch1 mirror-target=ether3
/interface ethernet switch rule
add mirror=yes ports=ether1 switch=switch1 vlan-id=11
```
# MAC Based Mirroring
This example will mirror incoming traffic with 64:D1:54:D9:27:E6 MAC destination or source address from theether1interface, and send copies to theether3interface.
```
/interface ethernet switch
set switch1 mirror-target=ether3
/interface ethernet switch rule
add mirror=yes ports=ether1 switch=switch1 dst-mac-address=64:D1:54:D9:27:E6/FF:FF:FF:FF:FF:FF
add mirror=yes ports=ether1 switch=switch1 src-mac-address=64:D1:54:D9:27:E6/FF:FF:FF:FF:FF:FF
```
# IP Based Mirroring
This example will mirror incoming traffic with 192.168.88.0/24 IP destination or source address from theether1interface, and send copies to theether3interface.
```
/interface ethernet switch
set switch1 mirror-target=ether3 mirror-source=none
/interface ethernet switch rule
add mirror=yes ports=ether1 switch=switch1 src-address=192.168.88.0/24
add mirror=yes ports=ether1 switch=switch1 dst-address=192.168.88.0/24
```
There are other options as well, check theACL sectionto find out all possible parameters that can be used to match packets.
# Remote Switch Port Analyzer
This example will mirror incomming and outgoing traffic from theether2interface, copies will be encapsulated in 802.1Q VLAN using the 999 as VLAN ID, and packets will be sent to theether3interface. If the original traffic is already VLAN tagged, RSPAN will add another layer of VLAN tagging as an outer tag. This results in the mirrored traffic being tagged twice. If themirror-targetport is included in vlan-filtering bridge, it is not required to make the interface as tagged VLAN member under the/interface/bridge/vlanmenu for the RSPAN.
```
mirror-target
```
```
/interface/bridge/vlan
```
```
/interface ethernet switch port
set ether2 mirror-egress=yes mirror-ingress=yes
/interface ethernet switch
set switch1 mirror-target=ether3 rspan=yes rspan-egress-vlan-id=999 rspan-ingress-vlan-id=999
```
# Property Reference
Sub-menu:/interface/ethernet/switch
```
/interface/ethernet/switch
```
Property | Description
----------------------
mirror-target(cpu | name | none; Default:none) | Selects a single mirroring target port. Packets frommirror-egressandmirror-ingress(/interface/ethernet/switch/port) andmirror(/interface/ethernet/switch/rule) will be sent to the selected port.
rspan(no | yes; Default:no) | Enables Remote Switch Port Analyzer (RSPAN) feature onmirror-target. Traffic marked for ingress or egress mirroring is carried over a specified remote analyzer VLAN -rspan-egress-vlan-idandrspan-ingress-vlan-id.
rspan-egress-vlan-id(integer: 1..4095; Default:1) | Selects the VLAN ID for marked egress traffic. Only applies whenrspanis enabled.
rspan-ingress-vlan-id(integer: 1..4095; Default:1) | Selects the VLAN ID for marked ingress traffic. Only applies whenrspanis enabled.
Selects a single mirroring target port. Packets frommirror-egressandmirror-ingress(/interface/ethernet/switch/port) andmirror(/interface/ethernet/switch/rule) will be sent to the selected port.
```
mirror-egress
```
```
mirror-ingress
```
```
/interface/ethernet/switch/port
```
```
/interface/ethernet/switch/rule
```
```
mirror-target
```
```
rspan-egress-vlan-id
```
```
rspan-ingress-vlan-id
```
```
rspan
```
```
rspan
```
Sub-menu:/interface/ethernet/switch/port
```
/interface/ethernet/switch/port
```
Property | Description
----------------------
mirror-egress(no | yes; Default:no) | Whether to send egress packet copy to themirror-targetport.
mirror-ingress(no | yes; Default:no) | Whether to send ingress packet copy to themirror-targetport.
Whether to send egress packet copy to themirror-targetport.
```
mirror-target
```
Whether to send ingress packet copy to themirror-targetport.
```
mirror-target
```
Sub-menu:/interface/ethernet/switch/rule
```
/interface/ethernet/switch/rule
```
Property | Description
----------------------
mirror(no | yes; Default:no) | Whether to send a packet copy tomirror-targetport.
```
mirror-target
```
# Traffic Shaping
It is possible to limit ingress traffic that matches certain parameters with ACL rules and it is possible to limit ingress/egress traffic per port basis. The policer is used for ingress traffic, the shaper is used for egress traffic. The ingress policer controls the received traffic with packet drops. Everything that exceeds the defined limit will get dropped. This can affect the TCP congestion control mechanism on end hosts and achieved bandwidth can be actually less than defined. The egress shaper tries to queue packets that exceed the limit instead of dropping them. Eventually, it will also drop packets when the output queue gets full, however, it should allow utilizing the defined throughput better.
Port-based traffic police and shaper:
```
/interface ethernet switch port
set ether1 ingress-rate=10M egress-rate=5M
```
MAC-based traffic policer:
```
/interface ethernet switch rule
add ports=ether1 switch=switch1 src-mac-address=64:D1:54:D9:27:E6/FF:FF:FF:FF:FF:FF rate=10M
```
VLAN-based traffic policer:
```
/interface bridge
set bridge1 vlan-filtering=yes
/interface ethernet switch rule
add ports=ether1 switch=switch1 vlan-id=11 rate=10M
```
Protocol-based traffic policer:
```
/interface ethernet switch rule
add ports=ether1 switch=switch1 mac-protocol=ipx rate=10M
```
There are other options as well, check theACL sectionto find out all possible parameters that can be used to match packets.
# Traffic Storm Control
Since RouterOS v6.42 it is possible to enable traffic storm control. A traffic storm can emerge when certain frames are continuously flooded on the network.Storm control settings is generally configured on non-uplink ports to restrict incoming storm traffic on those specific ports. This helps safeguard the entire switch and its connected ports by minimizing the impact of traffic storms across the network.
For example, if a network loop has been created and no loop avoidance mechanisms are used (e.g.Spanning Tree Protocol), broadcast or multicast frames can quickly overwhelm the network, causing degraded network performance or even complete network breakdown. With CRS3xx, CRS5xx series switches and CCR2116, CCR2216 routers it is possible to limit broadcast, unknown multicast and unknown unicast traffic. Unknown unicast traffic is considered when a switch does not contain a host entry for the destined MAC address. Unknown multicast traffic is considered when a switch does not contain a multicast group entry in the/interface bridge mdbmenu. Storm control settings should be applied to ingress ports, the egress traffic will be limited.
```
/interface bridge mdb
```
Sub-menu:/interface ethernet switch port
```
/interface ethernet switch port
```
Property | Description
----------------------
limit-broadcasts(yes | no; Default:yes) | Limit broadcast traffic on a switch port.
limit-unknown-multicasts(yes | no; Default:no) | Limit unknown multicast traffic on a switch port.
limit-unknown-unicasts(yes | no; Default:no) | Limit unknown unicast traffic on a switch port.
storm-rate(integer 0..100; Default:100) | Amount of broadcast, unknown multicast and/or unknown unicast traffic is limited to in percentage of the link speed.
For example, to limit 1% (10Mbps) of broadcast and unknown unicast traffic on ether1 (1Gbps), use the following commands:
```
/interface ethernet switch port
set ether1 storm-rate=1 limit-broadcasts=yes limit-unknown-unicasts=yes
```
# MPLS hardware offloading
Since RouterOS v6.41 it is possible to offload certain MPLS functions to the switch chip, the switch must be a (P)rovider router in a PE-P-PE setup in order to achieve hardware offloading. A setup example can be found in theBasic MPLS setup examplemanual page. The hardware offloading will only take place when LDP interfaces are configured as physical switch interfaces (e.g. Ethernet, SFP, SFP+).
# Switch Rules (ACL)
Access Control List contains ingress policy and egress policy engines. Seethis tableon how many rules each device supports. It is an advanced tool for wire-speed packet filtering, forwarding and modifying based on Layer2, Layer3 and Layer4 protocol header field conditions.
Sub-menu:/interface ethernet switch rule
```
/interface ethernet switch rule
```
Property | Description
----------------------
copy-to-cpu(no | yes; Default:no) | Clones the matching packet and sends it to the CPU.
disabled(yes | no; Default:no) | Enables or disables ACL entry.
dscp(0..63) | Matching the DSCP field of the packet (only applies to IPv4 packets).
dst-address(IP address/Mask) | Matching destination IPv4 address and mask, also matches the destination IP in ARP packets.
dst-address6(IPv6 address/Mask) | Matching destination IPv6 address and mask.
dst-mac-address(MAC address/Mask) | Matching destination MAC address and mask.
dst-port(0..65535) | Matching destination protocol port number (applies to IPv4 and IPv6 packets ifmac-protocolis not specified).
flow-label(0..1048575) | Matching IPv6 flow label.
mac-protocol(802.2 | arp | capsman | dot1x | homeplug-av | ip | ipv6 | ipx | lacp | lldp | loop-protect | macsec | mpls-multicast | mpls-unicast | packing-compr | packing-simple | pppoe | pppoe-discovery | rarp | romon | service-vlan | vlan | or 0..65535 | or 0x0000-0xffff) | Matching particular MAC protocol specified by protocol name or number
mirror(no | yes) | Clones the matching packet and sends it to the mirror-target port.
new-dst-ports(ports | bond | all) | Changes the destination port to the specified value:If the setting is left empty (e.g.new-dst-ports=""), the packet will be dropped;If a port orhardware-offloaded bondinginterface is specified, the packet will be redirected to that port. Only single port or bond interface is supported;if you use theallargument, packet will be allowed to pass through to the egress processing without being dropped;If this parameter is not used, the packet will be accepted as is.
new-vlan-id(0..4095) | Changes the VLAN ID to the specified value. Requiresvlan-filtering=yes.
new-vlan-priority(0..7) | Changes the VLAN priority (priority code point). Requiresvlan-filtering=yes.
ports(ports | bond) | Matching switch interfaces where the rule will apply to incoming traffic. Multiple ports andhardware-offloaded bondinginterfaces can be selected. Note that theswitch1-cpuport cannot be selected. Ifportsproperty is left empty, the rule will apply to all switch interfaces.
protocol(dccp | ddp | egp | encap | etherip | ggp | gre | hmp | icmp | icmpv6 | idpr-cmtp | igmp | ipencap | ipip | ipsec-ah | ipsec-esp | ipv6 | ipv6-frag | ipv6-nonxt | ipv6-opts | ipv6-route | iso-tp4 | l2tp | ospf | pim | pup | rdp | rspf | rsvp | sctp | st | tcp | udp | udp-lite | vmtp | vrrp | xns-idp | xtp | or 0..255) | Matching particular IP protocol specified by protocol name or number. Only applies to IPv4 packets ifmac-protocolis not specified. To match certain IPv6 protocols, use themac-protocol=ipv6setting.
rate(0..4294967295) | Sets ingress traffic limitation (bits per second) for matched traffic.
redirect-to-cpu(no | yes) | Changes the destination port of a matching packet to the CPU.
src-address(IP address/Mask) | Matching source IPv4 address and mask, also matches the source IP in ARP packets.
src-address6(IPv6 address/Mask) | Matching source IPv6 address and mask.
src-mac-address(MAC address/Mask) | Matching source MAC address and mask.
src-port(0..65535) | Matching source protocol port number (applies to IPv4 and IPv6 packets ifmac-protocolis not specified).
switch(switch group) | Matching switch group on which will the rule apply.
traffic-class(0..255) | Matching IPv6 traffic class.
vlan-id(0..4095) | Matching VLAN ID. Requiresvlan-filtering=yes.
vlan-header(not-present | present) | Matching VLAN header, whether the VLAN header is present or not. Requiresvlan-filtering=yes.
vlan-priority(0..7) | Matching VLAN priority (priority code point).
```
mac-protocol
```
Changes the destination port to the specified value:
```
new-dst-ports=""
```
```
all
```
```
vlan-filtering=yes
```
```
vlan-filtering=yes
```
```
switch1-cpu
```
```
ports
```
```
mac-protocol
```
```
mac-protocol=ipv6
```
```
mac-protocol
```
```
vlan-filtering=yes
```
```
vlan-filtering=yes
```
Action parameters:
Layer2 condition parameters:
Layer3 condition parameters:
Layer4 condition parameters:
# Port Security
It is possible to limit allowed MAC addresses on a single switch port. For example, to allow64:D1:54:81:EF:8E MAC address on a switch port,start by switching multiple ports together, in this example64:D1:54:81:EF:8E is going to be located behindether1.
Create an ACL rule to allow the given MAC address and drop all other traffic onether1(for ingress traffic):
```
/interface ethernet switch rule
add ports=ether1 src-mac-address=64:D1:54:81:EF:8E/FF:FF:FF:FF:FF:FF switch=switch1
add new-dst-ports="" ports=ether1 switch=switch1
```
Switch all required ports together, disable MAC learning and disable unknown unicast flooding onether1:
```
/interface bridge
add name=bridge1
/interface bridge port
add bridge=bridge1 interface=ether1 hw=yes learn=no unknown-unicast-flood=no
add bridge=bridge1 interface=ether2 hw=yes
```
Add a static hosts entry for64:D1:54:81:EF:8E(for egress traffic):
```
/interface bridge host
add bridge=bridge1 interface=ether1 mac-address=64:D1:54:81:EF:8E
```
# Dual Boot
The “dual boot” feature allows you to choose which operating system you prefer to use on CRS3xx series switches, RouterOS or SwOS. Device operating system could be changed using:
```
/system routerboard settings set boot-os=swos
```
More details about SwOS are described here:SwOS manual
# Configuring SwOS using RouterOS
Since RouterOS 6.43 it is possible to load, save and reset SwOS configuration, as well as upgrade SwOS and set an IP address for the CRS3xx series switches by using RouterOS.
```
/system swos save-config
```
```
/system swos load-config
```
```
/system swos password
```
```
/system swos reset-config
```
```
/system swos upgrade
```
Property | Description
----------------------
address-acquisition-mode(dhcp-only | dhcp-with-fallback | static; Default:dhcp-with-fallback) | Changes address acquisition method:dhcp-only- uses only a DHCP client to acquire addressdhcp-with-fallback- for the first 10 seconds will try to acquire address using a DHCP client. If the request is unsuccessful, then address falls back to static as defined bystatic-ip-addresspropertystatic- address is set as defined bystatic-ip-addressproperty
allow-from(IP/Mask; Default:0.0.0.0/0) | IP address or a network from which the switch is accessible. By default, the switch is accessible by any IP address.
allow-from-ports(name; Default: ) | List of switch ports from which the device is accessible. By default, all ports are allowed to access the switch
allow-from-vlan(integer: 0..4094; Default:0) | VLAN ID from which the device is accessible. By default, all VLANs are allowed
identity(name; Default:Mikrotik) | Name of the switch (used for Mikrotik Neighbor Discovery protocol)
static-ip-address(IP; Default:192.168.88.1) | IP address of the switch in caseaddress-acquisition-modeis either set todhcp-with-fallbackorstatic. By setting a static IP address, the address acquisition process does not change, which is DHCP with fallback by default. This means that the configured static IP address will become active only when there is going to be no DHCP servers in the same broadcast domain
dhcp-only- uses only a DHCP client to acquire address
dhcp-with-fallback- for the first 10 seconds will try to acquire address using a DHCP client. If the request is unsuccessful, then address falls back to static as defined bystatic-ip-addressproperty
static- address is set as defined bystatic-ip-addressproperty
# See also
CRS Router
CRS3xx VLANs with Bonds
Basic VLAN switching
Bridge Hardware Offloading
Route Hardware Offloading
Spanning Tree Protocol
MTU on RouterBOARD
Layer2 misconfiguration
Bridge VLAN Table
Bridge IGMP/MLD snooping
Multi-chassis Link Aggregation Group