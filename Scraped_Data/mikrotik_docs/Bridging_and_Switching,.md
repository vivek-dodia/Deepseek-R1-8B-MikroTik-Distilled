---
title: Bridging and Switching
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/328068/Bridging+and+Switching,
crawled_date: 2025-02-02T21:09:50.949688
section: mikrotik_docs
type: documentation
---

* 1Summary
* 2Bridge Interface Setup2.1Example2.2Bridge Monitoring
* 3Spanning Tree Protocol3.1Per-port STP3.1.1Create edge ports3.1.2Drop received BPDUs3.1.3Enable BPDU guard3.1.4Enable Root guard
* 4Bridge Settings
* 5Port Settings5.1Example5.2Interface lists5.3Bridge Port Monitoring
* 6Hosts Table6.1Monitoring6.2Static entries
* 7Multicast Table7.1Static entries
* 8Bridge Hardware Offloading8.1Example
* 9Bridge VLAN Filtering9.1Bridge VLAN table9.2Bridge port settings9.3Bridge host table9.4VLAN Example - Trunk and Access Ports9.5VLAN Example - Trunk and Hybrid Ports9.6VLAN Example - InterVLAN Routing by Bridge9.7Management access configuration9.7.1Untagged access without VLAN filtering9.7.2Tagged access without VLAN filtering9.7.3Tagged access with VLAN filtering9.7.4Untagged access with VLAN filtering9.7.5Changing untagged VLAN for the bridge interface9.8VLAN Tunneling (QinQ)9.9Tag stacking9.10MVRP9.10.1Property Reference
* 10Fast Forward
* 11IGMP/MLD Snooping
* 12DHCP Snooping and DHCP Option 82
* 13Controller Bridge and Port Extender
* 14Bridge Firewall14.1Bridge Packet Filter14.2Bridge NAT
* 15See also
* 2.1Example
* 2.2Bridge Monitoring
* 3.1Per-port STP3.1.1Create edge ports3.1.2Drop received BPDUs3.1.3Enable BPDU guard3.1.4Enable Root guard
* 3.1.1Create edge ports
* 3.1.2Drop received BPDUs
* 3.1.3Enable BPDU guard
* 3.1.4Enable Root guard
* 5.1Example
* 5.2Interface lists
* 5.3Bridge Port Monitoring
* 6.1Monitoring
* 6.2Static entries
* 7.1Static entries
* 8.1Example
* 9.1Bridge VLAN table
* 9.2Bridge port settings
* 9.3Bridge host table
* 9.4VLAN Example - Trunk and Access Ports
* 9.5VLAN Example - Trunk and Hybrid Ports
* 9.6VLAN Example - InterVLAN Routing by Bridge
* 9.7Management access configuration9.7.1Untagged access without VLAN filtering9.7.2Tagged access without VLAN filtering9.7.3Tagged access with VLAN filtering9.7.4Untagged access with VLAN filtering9.7.5Changing untagged VLAN for the bridge interface
* 9.8VLAN Tunneling (QinQ)
* 9.9Tag stacking
* 9.10MVRP9.10.1Property Reference
* 9.7.1Untagged access without VLAN filtering
* 9.7.2Tagged access without VLAN filtering
* 9.7.3Tagged access with VLAN filtering
* 9.7.4Untagged access with VLAN filtering
* 9.7.5Changing untagged VLAN for the bridge interface
* 9.10.1Property Reference
* 14.1Bridge Packet Filter
* 14.2Bridge NAT
# Summary
Ethernet-like networks (Ethernet, Ethernet over IP, IEEE 802.11 in ap-bridge or bridge mode, WDS, VLAN) can be connected together using MAC bridges. The bridge feature allows the interconnection of hosts connected to separate LANs (using EoIP, geographically distributed networks can be bridged as well if any kind of IP network interconnection exists between them) as if they were attached to a single LAN. As bridges are transparent, they do not appear in the traceroute list, and no utility can make a distinction between a host working in one LAN and a host working in another LAN if these LANs are bridged. However, depending on the way the LANs are interconnected, latency and data rate between hosts may vary.
Network loops may emerge (intentionally or not) in complex topologies. Without any special treatment, loops would prevent the network from functioning normally, as they would lead to avalanche-like packet multiplication. Each bridge runs an algorithm that calculates how the loop can be prevented. (R/M)STP allows bridges to communicate with each other, so they can negotiate a loop-free topology. All other alternative connections that would otherwise form loops are put on standby, so that should the main connection fail, another connection could take its place. This algorithm exchanges configuration messages (BPDU - Bridge Protocol Data Unit) periodically, so that all bridges are updated with the newest information about changes in a network topology. (R/M)STP selects a root bridge which is responsible for network reconfiguration, such as blocking and opening ports on other bridges. The root bridge is the bridge with the lowest bridge ID.
# Bridge Interface Setup
To combine a number of networks into one bridge, a bridge interface should be created. Later, all the desired interfaces should be set up as its ports. By default, bridge MAC address will be chosen automatically, depending on the bridge port configuration. To avoid unwanted MAC address changes, it is recommended to disable "auto-mac" and manually specifying the MAC address by using "admin-mac".
```
auto-mac
```
```
admin-mac
```
Sub-menu:/interface bridge
```
/interface bridge
```
Property | Description | Data rate | Long | Short
-------------------------------------------------
add-dhcp-option82(yes|no; Default:no) | Whether to add DHCP Option-82 information (Agent Remote ID and Agent Circuit ID) to DHCP packets. Can be used together with Option-82 capable DHCP server to assign IP addresses and implement policies. This property only has an effect whendhcp-snoopingis set toyes.
admin-mac(MAC address; Default:none) | Static MAC address of the bridge. This property only has an effect whenauto-macis set tono.
ageing-time(time; Default:00:05:00) | How long a host's information will be kept in the bridge database.
arp(disabled|enabled|local-proxy-arp | proxy-arp | reply-only; Default:enabled) | Address Resolution Protocol settingdisabled- the interface will not use ARPenabled- the interface will use ARPlocal-proxy-arp-the router performs proxy ARP on the interface and sends replies to the same interfaceproxy-arp-the router performs proxy ARP on the interface and sends replies to other interfacesreply-only- the interface will only respond to requests originating from matching IP address/MAC address combinations that are entered as static entries in the IP/ARP table. No dynamic entries will be automatically stored in the IP/ARP table. Therefore, for communications to be successful, a valid static entry must already exist.
arp-timeout(auto | integer; Default:auto) | How long the ARP record is kept in the ARP table after no packets are received from IP address. Valueautoequals to the value ofarp-timeoutinip/settings, default is30s.
auto-mac(yes | no; Default:yes) | Whenauto-mac=yesis configured, the bridge will automatically select a MAC address for the bridge interface based on the following order of priority:From an Ethernet interface that is part of the bridge;From a non-Ethernet interface in the bridge (e.g., WiFi or tunnel);A randomly generated address if neither of the above is available.If the configuration is changed, for example, you add a new port to the bridge, the bridge’s MAC address will be updated only if a higher-priority address source becomes available. For example, if the bridge initially used a randomly generated MAC, then an Ethernet interface was added, the MAC would update according to the highest available priority (in this case, the Ethernet interface).The bridge will also update the MAC address if the current MAC is associated with a port that is moved to a different bridge.The current MAC address and its priority level are saved and will be reused after a reboot.Whenauto-mac=nois configured, you can set a static MAC address manually using theadmin-macproperty.
comment(string; Default: ) | Short description of the interface.
dhcp-snooping(yes | no; Default:no) | Enables or disables DHCP Snooping on the bridge.
disabled(yes | no; Default:no) | Changes whether the bridge is disabled.
ether-type(0x9100 | 0x8100 | 0x88a8; Default:0x8100) | Changes the EtherType, which will be used to determine if a packet has a VLAN tag. Packets that have a matching EtherType are considered as tagged packets. This property only has an effect whenvlan-filteringis set toyes.
fast-forward(yes | no; Default:yes) | Special and faster case ofFast Pathwhich works only on bridges with 2 interfaces (enabled by default only for new bridges). More details can be found in theFast Forwardsection.
forward-delay(time; Default:00:00:15) | The time which is spent during the initialization phase of the bridge interface (i.e., after router startup or enabling the interface) in the listening/learning state before the bridge will start functioning normally.
forward-reserved-addresses(yes | no:Default:no) | Whether to forward IEEE reserved multicast MAC address that are inthe01:80:C2:00:00:0xrange. Bridges compliant with R/M/STP standards should refrain from forwarding these packets, this property can only be applied whenprotocol-modeis set tonone.Enabling forwarding of reserved MAC addresses may affect certain protocols relying on these addresses. It is advisable to enable forwarding only when absolutely necessary, such as in transparent bridging setups (e.g., extending long links, using bridge as media converters, or conducting network analysis).Here are some notable MAC addresses and protocols used by RouterOS:01:80:C2:00:00:00 -Spanning Tree Protocol (STP);01:80:C2:00:00:01 -EthernetFlow Control;01:80:C2:00:00:02 -Link Aggregation Control Protocol (LACP);01:80:C2:00:00:03 -Dot1xclient and server;01:80:C2:00:00:08 -Spanning Tree Protocol (for 802.1ad bridges, usingether-type=0x88a8);01:80:C2:00:00:0D -Multiple VLAN Registration protocol(for 802.1ad bridges, usingether-type=0x88a8);01:80:C2:00:00:0E -Link Layer Discovery ProtocolandMulti-chassis Link Aggregation Group;
frame-types(admit-all | admit-only-untagged-and-priority-tagged | admit-only-vlan-tagged; Default:admit-all) | Specifies allowed frame types on a bridge port. This property only has an effect whenvlan-filteringis set toyes.
igmp-snooping(yes | no; Default:no) | Enables multicast group and port learning to prevent multicast traffic from flooding all interfaces in a bridge.
igmp-version(2 | 3; Default:2) | Selects the IGMP version in which IGMP membership queries will be generated when the bridge interface is acting as an IGMP querier. This property only has an effect whenigmp-snoopingandmulticast-querieris set toyes.
ingress-filtering(yes | no; Default:yes) | Enables or disables VLAN ingress filtering, which checks if the ingress port is a member of the received VLAN ID in the bridge VLAN table. By default, VLANs that don't exist in the bridge VLAN table are dropped before they are sent out (egress), but this property allows you to drop the packets when they are received (ingress). Should be used withframe-typesto specify if the ingress traffic should be tagged or untagged. This property only has an effect whenvlan-filteringis set toyes. The setting is enabled by default since RouterOS v7.
l2mtu(read-only; Default: ) | L2MTU indicates the maximum size of the frame without a MAC header that can be sent by this interface. The L2MTU value will be automatically set by the bridge and it will use the lowest L2MTU value of any associated bridge port. This value cannot be manually changed.
last-member-interval(time; Default:1s) | When the last client on the bridge port unsubscribes to a multicast group and the bridge is acting as an active querier, the bridge will send group-specific IGMP/MLD query, to make sure that no other client is still subscribed. The setting changes the response time for these queries. In case no membership reports are received in a certain time period (last-member-interval*last-member-query-count), the multicast group is removed from the multicast database (MDB).If the bridge port is configured withfast-leave, the multicast group is removed right away without sending any queries.This property only has an effect whenigmp-snoopingandmulticast-querieris set toyes.
last-member-query-count(integer: 0..4294967295; Default:2) | How many times shouldlast-member-intervalpass until the IGMP/MLD snooping bridge stops forwarding a certain multicast stream. This property only has an effect whenigmp-snoopingandmulticast-querieris set toyes.
max-hops(integer: 6..40; Default:20) | Bridge count which BPDU can pass in an MSTP enabled network in the same region before BPDU is being ignored. This property only has an effect whenprotocol-modeis set tomstp.
max-learned-entries(integer: 0..4294967295 | auto | unlimited; Default:auto) | Sets the maximum number of learned hosts for the bridge interface. The default value isauto, and it depends on the installed amount of RAM. It is possible to set a higher value than the default or chooseunlimitedoption, but it increases the risk of out-of-memory condition.The default values for certain RAM sizes:8192 for 64 MB;16384 for 128 MB;32768 for 256 MB;65536 for 512 MB;131072 for 1024 MB or higher.This limit specifically applies to the bridge interface, not the hardware limits on the switch FDB table. Even if the bridge limit is reached, the switch can continue learn hosts up to its hardware limits and make correct forwarding decisions. However, these additional hosts will not show up in the "/interface bridge host" table nor can be monitored. Additionally, hitting this limit could impact MLAG host synchronization.This setting has been available since RouterOS version 7.16.
max-message-age(time: 6s..40s; Default:00:00:20) | Changes the Max Age value in BPDU packets, which is transmitted by the root bridge. A root bridge sends a BPDUs with Max Age set tomax-message-agevalue and a Message Age of 0. Every sequential bridge will increment the Message Age before sending their BPDUs. Once a bridge receives a BPDU where Message Age is equal or greater than Max Age, the BPDU is ignored.This property only has an effect whenprotocol-modeis set tostporrstp.
membership-interval(time; Default:4m20s) | The amount of time after an entry in the Multicast Database (MDB) is removed if no IGMP/MLD membership reports are received on a bridge port. This property only has an effect whenigmp-snoopingis set toyes.
mld-version(1 | 2; Default:1) | Selects the MLD version in which MLD membership queries will be generated, when the bridge interface is acting as an MLD querier. This property only has an effect when the bridge has an active IPv6 address,igmp-snoopingandmulticast-querieris set toyes.
mtu(integer; Default:auto) | Maximum transmission unit, by default, the bridge will set MTU automatically and it will use the lowest MTU value of any associated bridge port. The default bridge MTU value without any bridge ports added is 1500. The MTU value can be set manually, but it cannot exceed the bridge L2MTU or the lowest bridge port L2MTU. If a new bridge port is added with L2MTU which is smaller than theactual-mtuof the bridge (set by themtuproperty), then manually set value will be ignored and the bridge will act as ifmtu=autois set.When adding VLAN interfaces on the bridge, and when VLAN is using higher MTU than default 1500, it is recommended to set manually the MTU of the bridge.
multicast-querier(yes | no; Default:no) | Multicast querier generates periodic IGMP/MLD general membership queries to which all IGMP/MLD capable devices respond with an IGMP/MLD membership report, usually a PIM (multicast) router or IGMP proxy generates these queries.By using this property you can make an IGMP/MLD snooping enabled bridge to generate IGMP/MLD general membership queries. This property should be used whenever there is no active querier (PIM router or IGMP proxy) in a Layer2 network. Without a multicast querier in a Layer2 network, the Multicast Database (MDB) is not being updated, the learned entries will timeout and IGMP/MLD snooping will not function properly.Only untagged IGMP/MLD general membership queries are generated, IGMP queries are sent with IPv4 0.0.0.0 source address, MLD queries are sent with IPv6 link-local address of the bridge interface. The bridge will not send queries if an external IGMP/MLD querier is detected (see the monitoring valuesigmp-querierandmld-querier).This property only has an effect whenigmp-snoopingis set toyes.
multicast-router(disabled | permanent | temporary-query; Default:temporary-query) | A multicast router port is a port where a multicast router or querier is connected. On this port, unregistered multicast streams and IGMP/MLD membership reports will be sent. This setting changes the state of the multicast router for a bridge interface itself. This property can be used to send IGMP/MLD membership reports to the bridge interface for further multicast routing or proxying. This property only has an effect whenigmp-snoopingis set toyes.disabled- disabled multicast router state on the bridge interface. Unregistered multicast and IGMP/MLD membership reports are not sent to the bridge interface regardless of what is configured on the bridge interface.permanent- enabled multicast router state on the bridge interface. Unregistered multicast and IGMP/MLD membership reports are sent to the bridge interface itself regardless of what is configured on the bridge interface.temporary-query- automatically detect multicast router state on the bridge interface using IGMP/MLD queries.
name(text; Default:bridgeN) | Name of the bridge interface.
port-cost-mode(long | short; Default:long) | Changes the port path-cost and internal-path-cost mode for bridged ports, utilizing automatic values based on interface speed. This setting does not impact bridged ports with manually configuredpath-costorinternal-path-costproperties. Below are examples illustrating the path-costs corresponding to specific data rates (with proportionate calculations for intermediate rates):Data rateLongShort10 Mbps2,000,000100100 Mbps200,000191 Gbps20,000410 Gbps2,000225 Gbps800140 Gbps500150 Gbps4001100 Gbps2001For bonded interfaces, the highest path-cost among all bonded member ports is applied, this value remains unaffected by the total link speed of the bonding.For virtual interfaces (such asVLAN, EoIP, VXLAN), as well as wifi, wireless, and 60GHz interfaces, a path-cost of 20,000 is assigned for long mode, and 10 for short mode.For dynamically bridged interfaces (e.g. wifi, wireless, PPP, VPLS), the path-cost defaults to 20,000 for long mode and 10 for short mode. However, this can be manually overridden by the service that dynamically adds interfaces to bridge, for instance, by using the CAPsMANdatapath.bridge-costsetting.Useport monitorto observe the applied path-cost.This property has an effect whenprotocol-modeis set tostp,rstp, ormstp. | 10 Mbps | 2,000,000 | 100 | 100 Mbps | 200,000 | 19 | 1 Gbps | 20,000 | 4 | 10 Gbps | 2,000 | 2 | 25 Gbps | 800 | 1 | 40 Gbps | 500 | 1 | 50 Gbps | 400 | 1 | 100 Gbps | 200 | 1
10 Mbps | 2,000,000 | 100
100 Mbps | 200,000 | 19
1 Gbps | 20,000 | 4
10 Gbps | 2,000 | 2
25 Gbps | 800 | 1
40 Gbps | 500 | 1
50 Gbps | 400 | 1
100 Gbps | 200 | 1
priority(integer: 0..65535 decimal format or 0x0000-0xffff hex format; Default:32768 / 0x8000) | Bridge priority, used by R/STP to determine root bridge, used by MSTP to determine CIST and IST regional root bridge. This property has no effect whenprotocol-modeis set tonone.
protocol-mode(none | rstp | stp | mstp; Default:rstp) | Select Spanning tree protocol (STP) or Rapid spanning tree protocol (RSTP) to ensure a loop-free topology for any bridged LAN. RSTP provides a faster spanning tree convergence after a topology change. Select MSTP to ensure loop-free topology across multiple VLANs.The forwarding of reserved MAC addresses that are inthe01:80:C2:00:00:0xrange is separatedfromprotocol-mode=none, and is now available as a controllable propertyforward-reserved-addressessinceRouterOS v7.16.
pvid(integer: 1..4094; Default:1) | Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. It applies e.g. to frames sent from bridge IP and destined to a bridge port. This property only has an effect whenvlan-filteringis set toyes.
querier-interval(time; Default:4m15s) | Changes the timeout period for detected querier and multicast-router ports. This property only has an effect whenigmp-snoopingis set toyes.
query-interval(time; Default:2m5s) | Changes the interval on how often IGMP/MLD general membership queries are sent out when the bridge interface is acting as an IGMP/MLD querier. The interval takes place when the last startup query is sent. This property only has an effect whenigmp-snoopingandmulticast-querieris set toyes.
query-response-interval(time; Default:10s) | The setting changes the response time for general IGMP/MLD queries when the bridge is active as an IGMP/MLD querier.This property only has an effect whenigmp-snoopingandmulticast-querieris set toyes.
region-name(text; Default: ) | MSTP region name. This property only has an effect whenprotocol-modeis set tomstp.
region-revision(integer: 0..65535; Default:0) | MSTP configuration revision number. This property only has an effect whenprotocol-modeis set tomstp.
startup-query-count(integer: 0..4294967295; Default:2) | Specifies how many times general IGMP/MLD queries must be sent when bridge interface is enabled or active querier timeouts. This property only has an effect whenigmp-snoopingandmulticast-querieris set toyes.
startup-query-interval(time; Default:31s250ms) | Specifies the interval between startup general IGMP/MLD queries. This property only has an effect whenigmp-snoopingandmulticast-querieris set toyes.
transmit-hold-count(integer: 1..10; Default:6) | The Transmit Hold Count used by the Port Transmit state machine to limit the transmission rate.
vlan-filtering(yes | no; Default:no) | Globally enables or disables VLAN functionality for the bridge.
```
dhcp-snooping
```
```
yes
```
```
auto-mac
```
```
no
```
* disabled- the interface will not use ARP
* enabled- the interface will use ARP
* local-proxy-arp-the router performs proxy ARP on the interface and sends replies to the same interface
* proxy-arp-the router performs proxy ARP on the interface and sends replies to other interfaces
* reply-only- the interface will only respond to requests originating from matching IP address/MAC address combinations that are entered as static entries in the IP/ARP table. No dynamic entries will be automatically stored in the IP/ARP table. Therefore, for communications to be successful, a valid static entry must already exist.
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
```
ip/settings
```
Whenauto-mac=yesis configured, the bridge will automatically select a MAC address for the bridge interface based on the following order of priority:
```
auto-mac=yes
```
* From an Ethernet interface that is part of the bridge;
* From a non-Ethernet interface in the bridge (e.g., WiFi or tunnel);
* A randomly generated address if neither of the above is available.
If the configuration is changed, for example, you add a new port to the bridge, the bridge’s MAC address will be updated only if a higher-priority address source becomes available. For example, if the bridge initially used a randomly generated MAC, then an Ethernet interface was added, the MAC would update according to the highest available priority (in this case, the Ethernet interface).The bridge will also update the MAC address if the current MAC is associated with a port that is moved to a different bridge.
The current MAC address and its priority level are saved and will be reused after a reboot.
Whenauto-mac=nois configured, you can set a static MAC address manually using theadmin-macproperty.
```
auto-mac=no
```
```
admin-mac
```
```
vlan-filtering
```
```
yes
```
Whether to forward IEEE reserved multicast MAC address that are inthe01:80:C2:00:00:0xrange. Bridges compliant with R/M/STP standards should refrain from forwarding these packets, this property can only be applied whenprotocol-modeis set tonone.
```
protocol-mode
```
```
none
```
Enabling forwarding of reserved MAC addresses may affect certain protocols relying on these addresses. It is advisable to enable forwarding only when absolutely necessary, such as in transparent bridging setups (e.g., extending long links, using bridge as media converters, or conducting network analysis).
Here are some notable MAC addresses and protocols used by RouterOS:
* 01:80:C2:00:00:00 -Spanning Tree Protocol (STP);
* 01:80:C2:00:00:01 -EthernetFlow Control;
* 01:80:C2:00:00:02 -Link Aggregation Control Protocol (LACP);
* 01:80:C2:00:00:03 -Dot1xclient and server;
* 01:80:C2:00:00:08 -Spanning Tree Protocol (for 802.1ad bridges, usingether-type=0x88a8);
* 01:80:C2:00:00:0D -Multiple VLAN Registration protocol(for 802.1ad bridges, usingether-type=0x88a8);
* 01:80:C2:00:00:0E -Link Layer Discovery ProtocolandMulti-chassis Link Aggregation Group;
```
ether-type=0x88a8
```
```
ether-type=0x88a8
```
```
vlan-filtering
```
```
yes
```
```
igmp-snooping
```
```
multicast-querier
```
```
yes
```
```
frame-types
```
```
vlan-filtering
```
```
yes
```
When the last client on the bridge port unsubscribes to a multicast group and the bridge is acting as an active querier, the bridge will send group-specific IGMP/MLD query, to make sure that no other client is still subscribed. The setting changes the response time for these queries. In case no membership reports are received in a certain time period (last-member-interval*last-member-query-count), the multicast group is removed from the multicast database (MDB).
```
last-member-interval
```
```
last-member-query-count
```
If the bridge port is configured withfast-leave, the multicast group is removed right away without sending any queries.
This property only has an effect whenigmp-snoopingandmulticast-querieris set toyes.
```
igmp-snooping
```
```
multicast-querier
```
```
yes
```
```
last-member-interval
```
```
igmp-snooping
```
```
multicast-querier
```
```
yes
```
```
protocol-mode
```
```
mstp
```
Sets the maximum number of learned hosts for the bridge interface. The default value isauto, and it depends on the installed amount of RAM. It is possible to set a higher value than the default or chooseunlimitedoption, but it increases the risk of out-of-memory condition.
```
auto
```
```
unlimited
```
The default values for certain RAM sizes:
* 8192 for 64 MB;
* 16384 for 128 MB;
* 32768 for 256 MB;
* 65536 for 512 MB;
* 131072 for 1024 MB or higher.
This limit specifically applies to the bridge interface, not the hardware limits on the switch FDB table. Even if the bridge limit is reached, the switch can continue learn hosts up to its hardware limits and make correct forwarding decisions. However, these additional hosts will not show up in the "/interface bridge host" table nor can be monitored. Additionally, hitting this limit could impact MLAG host synchronization.
```
/interface bridge host
```
This setting has been available since RouterOS version 7.16.
```
max-message-age
```
```
protocol-mode
```
```
stp
```
```
rstp
```
```
igmp-snooping
```
```
yes
```
```
igmp-snooping
```
```
multicast-querier
```
```
yes
```
Maximum transmission unit, by default, the bridge will set MTU automatically and it will use the lowest MTU value of any associated bridge port. The default bridge MTU value without any bridge ports added is 1500. The MTU value can be set manually, but it cannot exceed the bridge L2MTU or the lowest bridge port L2MTU. If a new bridge port is added with L2MTU which is smaller than theactual-mtuof the bridge (set by themtuproperty), then manually set value will be ignored and the bridge will act as ifmtu=autois set.
```
actual-mtu
```
```
mtu
```
```
mtu=auto
```
When adding VLAN interfaces on the bridge, and when VLAN is using higher MTU than default 1500, it is recommended to set manually the MTU of the bridge.
Multicast querier generates periodic IGMP/MLD general membership queries to which all IGMP/MLD capable devices respond with an IGMP/MLD membership report, usually a PIM (multicast) router or IGMP proxy generates these queries.
By using this property you can make an IGMP/MLD snooping enabled bridge to generate IGMP/MLD general membership queries. This property should be used whenever there is no active querier (PIM router or IGMP proxy) in a Layer2 network. Without a multicast querier in a Layer2 network, the Multicast Database (MDB) is not being updated, the learned entries will timeout and IGMP/MLD snooping will not function properly.
Only untagged IGMP/MLD general membership queries are generated, IGMP queries are sent with IPv4 0.0.0.0 source address, MLD queries are sent with IPv6 link-local address of the bridge interface. The bridge will not send queries if an external IGMP/MLD querier is detected (see the monitoring valuesigmp-querierandmld-querier).
```
igmp-querier
```
```
mld-querier
```
This property only has an effect whenigmp-snoopingis set toyes.
```
igmp-snooping
```
```
yes
```
```
igmp-snooping
```
```
yes
```
* disabled- disabled multicast router state on the bridge interface. Unregistered multicast and IGMP/MLD membership reports are not sent to the bridge interface regardless of what is configured on the bridge interface.
* permanent- enabled multicast router state on the bridge interface. Unregistered multicast and IGMP/MLD membership reports are sent to the bridge interface itself regardless of what is configured on the bridge interface.
* temporary-query- automatically detect multicast router state on the bridge interface using IGMP/MLD queries.
```
disabled
```
```
permanent
```
```
temporary-query
```
Changes the port path-cost and internal-path-cost mode for bridged ports, utilizing automatic values based on interface speed. This setting does not impact bridged ports with manually configuredpath-costorinternal-path-costproperties. Below are examples illustrating the path-costs corresponding to specific data rates (with proportionate calculations for intermediate rates):
```
path-cost
```
```
internal-path-cost
```
Data rate | Long | Short
------------------------
10 Mbps | 2,000,000 | 100
100 Mbps | 200,000 | 19
1 Gbps | 20,000 | 4
10 Gbps | 2,000 | 2
25 Gbps | 800 | 1
40 Gbps | 500 | 1
50 Gbps | 400 | 1
100 Gbps | 200 | 1
For bonded interfaces, the highest path-cost among all bonded member ports is applied, this value remains unaffected by the total link speed of the bonding.
For virtual interfaces (such asVLAN, EoIP, VXLAN), as well as wifi, wireless, and 60GHz interfaces, a path-cost of 20,000 is assigned for long mode, and 10 for short mode.
For dynamically bridged interfaces (e.g. wifi, wireless, PPP, VPLS), the path-cost defaults to 20,000 for long mode and 10 for short mode. However, this can be manually overridden by the service that dynamically adds interfaces to bridge, for instance, by using the CAPsMANdatapath.bridge-costsetting.
```
datapath.bridge-cost
```
Useport monitorto observe the applied path-cost.
This property has an effect whenprotocol-modeis set tostp,rstp, ormstp.
```
protocol-mode
```
```
stp
```
```
rstp
```
```
mstp
```
```
protocol-mode
```
```
none
```
Select Spanning tree protocol (STP) or Rapid spanning tree protocol (RSTP) to ensure a loop-free topology for any bridged LAN. RSTP provides a faster spanning tree convergence after a topology change. Select MSTP to ensure loop-free topology across multiple VLANs.
The forwarding of reserved MAC addresses that are inthe01:80:C2:00:00:0xrange is separatedfromprotocol-mode=none, and is now available as a controllable propertyforward-reserved-addressessinceRouterOS v7.16.
```
protocol-mode=none
```
```
forward-reserved-addresses
```
```
vlan-filtering
```
```
yes
```
```
igmp-snooping
```
```
yes
```
```
igmp-snooping
```
```
multicast-querier
```
```
yes
```
```
igmp-snooping
```
```
multicast-querier
```
```
yes
```
```
protocol-mode
```
```
mstp
```
```
protocol-mode
```
```
mstp
```
```
igmp-snooping
```
```
multicast-querier
```
```
yes
```
```
igmp-snooping
```
```
multicast-querier
```
```
yes
```
## Example
To add and enable a bridge interface that will forward L2 packets:
```
[admin@MikroTik] > interface bridge add
[admin@MikroTik] > interface bridge print 
Flags: X - disabled, R - running 
0 R name="bridge1" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=5E:D2:42:95:56:7F protocol-mode=rstp fast-forward=yes 
igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6 vlan-filtering=no 
dhcp-snooping=no
```
## Bridge Monitoring
To monitor the current status of a bridge interface, use themonitorcommand.
```
monitor
```
Sub-menu:/interface bridge monitor
```
/interface bridge monitor
```
Property | Description
----------------------
current-mac-address(MAC address) | Current MAC address of the bridge
designated-port-count(integer) | Number of designated bridge ports
igmp-querier(none|interface & IPv4 address) | Shows a bridge port and source IP address from the detected IGMP querier. Only shows detected external IGMP querier, local bridge IGMP querier (including IGMP proxy and PIM) will not be displayed. Monitoring value appears only whenigmp-snoopingis enabled.
mld-querier(none|interface & IPv6 address) | Shows a bridge port and source IPv6 address from the detected MLD querier. Only shows detected external MLD querier, local bridge MLD querier will not be displayed. Monitoring value appears only whenigmp-snoopingis enabled and the bridge has an active IPv6 address.
multicast-router(yes | no) | Shows if a multicast router is detected on the port. Monitoring value appears only whenigmp-snoopingis enabled.
port-count(integer) | Number of the bridge ports
root-bridge(yes | no) | Shows whether the bridge is the root bridge of the spanning tree
root-bridge-id(text) | The root bridge ID, which is in form of bridge-priority.bridge-MAC-address
root-path-cost(integer) | The total cost of the path to the root-bridge
root-port(name) | Port to which the root bridge is connected to
state(enabled | disabled) | State of the bridge
```
igmp-snooping
```
```
igmp-snooping
```
```
igmp-snooping
```
```
[admin@MikroTik] /interface bridge monitor bridge1 
                  state: enabled
    current-mac-address: CC:2D:E0:E4:B3:38
            root-bridge: yes
         root-bridge-id: 0x8000.CC:2D:E0:E4:B3:38
         root-path-cost: 0
              root-port: none
             port-count: 2
  designated-port-count: 2
           fast-forward: no
```
# Spanning Tree Protocol
RouterOS bridge interfaces are capable of running Spanning Tree Protocol to ensure a loop-free and redundant topology. For small networks with just 2 bridges STP does not bring many benefits, but for larger networks properly configured STP is very crucial, leaving STP-related values to default may result in a completely unreachable network in case of an even single bridge failure. To achieve a proper loop-free and redundant topology, it is necessary to properly set bridge priorities, port path costs, and port priorities.
STP has multiple variants, currently, RouterOS supports STP, RSTP, and MSTP. Depending on needs, either one of them can be used, some devices are able to run some of these protocols using hardware offloading, detailed information about which device support it can be found in theHardware Offloadingsection. STP is considered to be outdated and slow, it has been almost entirely replaced in all network topologies by RSTP, which is backward compatible with STP. For network topologies that depend on VLANs, it is recommended to use MSTP since it is a VLAN aware protocol and gives the ability to do load balancing per VLAN groups. There are a lot of considerations that should be made when designing an STP enabled network, more detailed case studies can be found in theSpanning Tree Protocolarticle. In RouterOS, theprotocol-modeproperty controls the used STP variant.
```
protocol-mode
```
## Per-port STP
There might be certain situations where you want to limit STP functionality on single or multiple ports. Below you can find some examples for different use cases.
### Create edge ports
Setting a bridge port as an edge port will restrict it from sending BPDUs and will ignore any received BPDUs:
```
/interface bridge
add name=bridge1
/interface bridge port
add bridge=bridge1 interface=ether1 edge=yes
add bridge=bridge1 interface=ether2
```
### Drop received BPDUs
The bridge filter or NAT rules cannot drop BPDUs when the bridge has STP/RSTP/MSTP enabled due to the special processing of BPDUs. However, dropping received BPDUs on a certain port can be done on some switch chips using ACL rules:
On CRS3xx:
```
/interface ethernet switch rule
add dst-mac-address=01:80:C2:00:00:00/FF:FF:FF:FF:FF:FF new-dst-ports="" ports=ether1 switch=switch1
```
On CRS1xx/CRS2xx withAccess Control List (ACL) support:
```
/interface ethernet switch acl
add action=drop mac-dst-address=01:80:C2:00:00:00 src-ports=ether1
```
In this example all received BPDUs onether1are dropped.
### Enable BPDU guard
In this example, ifether1receives a BPDU, it will block the port and will require you to manually re-enable it.
```
/interface bridge
add name=bridge1
/interface bridge port
add bridge=bridge1 interface=ether1 bpdu-guard=yes
add bridge=bridge1 interface=ether2
```
### Enable Root guard
In this example,ether1is configured withrestricted-role=yes.It prevented the port from becoming the root port for the CIST or any MSTI, regardless of its best spanning tree priority vector. Such a port will be selected as an Alternate Port (discarding state) and remains so as long as it continues to receive superior BPDUs. It will automatically transition to the forwarding state when it no longer detects a superior root path. Network administrators may enable this setting to safeguard against external bridges influencing the active spanning tree.
```
restricted-role=yes.
```
```
/interface bridge
add name=bridge1
/interface bridge port
add bridge=bridge1 interface=ether1 restricted-role=yes
add bridge=bridge1 interface=ether2
[admin@MikroTik] /interface/bridge/port monitor [find]
                 interface: ether1                   ether2
                    status: in-bridge                in-bridge
               port-number: 1                        2
                      role: alternate-port           designated-port
                 edge-port: no                       yes
       edge-port-discovery: yes                      yes
       point-to-point-port: yes                      yes
              external-fdb: no                       no
              sending-rstp: yes                      yes
                  learning: no                       yes
                forwarding: no                       yes
          actual-path-cost: 20000                    20000
            root-path-cost: 20000                    
         designated-bridge: 0x7000.64:D1:54:C7:3A:6E 
           designated-cost: 0                        
    designated-port-number: 1                        
          hw-offload-group: switch1                  switch1
```
# Bridge Settings
Under the bridge settings menu, it is possible to control certain features for all bridge interfaces and monitor global bridge counters.
Sub-menu:/interface bridge settings
```
/interface bridge settings
```
Property | Description
----------------------
use-ip-firewall(yes | no; Default:no) | Force bridged traffic to also be processed by prerouting, forward, and postrouting sections of IP routing (see more details onPacket Flowarticle). This does not apply to routed traffic. This property is required in case you want to assignSimple Queuesor globalQueue Treeto traffic in a bridge. Propertyuse-ip-firewall-for-vlanis required in case bridgevlan-filteringis used.
use-ip-firewall-for-pppoe(yes | no; Default:no) | Send bridged un-encrypted PPPoE traffic to also be processed byIP/Firewall. This property only has an effect whenuse-ip-firewallis set toyes. This property is required in case you want to assignSimple Queuesor globalQueue Treeto PPPoE traffic in a bridge.
use-ip-firewall-for-vlan(yes | no; Default:no) | Send bridged VLAN traffic to also be processed byIP/Firewall. This property only has an effect whenuse-ip-firewallis set toyes. This property is required in case you want to assignSimple Queuesor globalQueue Treeto VLAN traffic in a bridge.
allow-fast-path(yes | no; Default:yes) | Whether to enable a bridgeFast Pathglobally.
bridge-fast-path-active(yes | no; Default:) | Shows whether a bridge FastPath is active globally, Fast Path status per bridge interface is not displayed.
bridge-fast-path-packets(integer; Default:) | Shows packet count forwarded by bridge Fast Path.
bridge-fast-path-bytes(integer; Default:) | Shows byte count forwarded by bridge Fast Path.
bridge-fast-forward-packets(integer; Default:) | Shows packet count forwarded by bridge Fast Forward.
bridge-fast-forward-bytes(integer; Default:) | Shows byte count forwarded by bridge Fast Forward.
```
use-ip-firewall-for-vlan
```
```
vlan-filtering
```
```
use-ip-firewall
```
```
yes
```
```
use-ip-firewall
```
```
yes
```
# Port Settings
Port submenu is used to add interfaces in a particular bridge.
Sub-menu:/interface bridge port
```
/interface bridge port
```
Property | Description
----------------------
auto-isolate(yes | no; Default:no) | When enabled, prevents a port moving from discarding into forwarding state if no BPDUs are received from the neighboring bridge. The port will change into a forwarding state only when a BPDU is received. This property only has an effect whenprotocol-modeis set torstpormstpandedgeis set tono.
bpdu-guard(yes | no; Default:no) | Enables or disables BPDU Guard feature on a port. This feature puts the port in a disabled role if it receives a BPDU and requires the port to be manually disabled and enabled if a BPDU was received. Should be used to prevent a bridge from BPDU related attacks. This property has no effect whenprotocol-modeis set tonone.
bridge(name; Default:none) | The bridge interface where the respective interface is grouped in.
broadcast-flood(yes | no; Default:yes) | When enabled, bridge floods broadcast traffic to all bridge egress ports. When disabled, drops broadcast traffic on egress ports. Can be used to filter all broadcast traffic on an egress port. Broadcast traffic is considered as traffic that usesFF:FF:FF:FF:FF:FFas destination MAC address, such traffic is crucial for many protocols such as DHCP, ARP, NDP, BOOTP (Netinstall), and others. This option does not limit traffic flood to the CPU.
edge(auto | no | no-discover | yes | yes-discover; Default:auto) | Set port as edge port or non-edge port, or enable edge discovery. Edge ports are connected to a LAN that has no other bridges attached. An edge port will skip the learning and the listening states in STP and will transition directly to the forwarding state, this reduces the STP initialization time. If the port is configured to discover edge port then as soon as the bridge detects a BPDU coming to an edge port, the port becomes a non-edge port. This property has no effect whenprotocol-modeis set tonone.no- non-edge port, will participate in learning and listening states in STP.no-discover- non-edge port with enabled discovery, will participate in learning and listening states in STP, a port can become an edge port if no BPDU is received.yes- edge port without discovery, will transit directly to forwarding state.yes-discover- edge port with enabled discovery, will transit directly to forwarding state.auto- same asno-discover, but will additionally detect if a bridge port is a Wireless interface with disabled bridge-mode, such interface will be automatically set as an edge port without discovery.
fast-leave(yes | no; Default:no) | Enables IGMP/MLD fast leave feature on the bridge port. The bridge will stop forwarding multicast traffic to a bridge port when an IGMP/MLD leave message is received. This property only has an effect whenigmp-snoopingis set toyes.
frame-types(admit-all | admit-only-untagged-and-priority-tagged | admit-only-vlan-tagged; Default:admit-all) | Specifies allowed ingress frame types on a bridge port. This property only has an effect whenvlan-filteringis set toyes.
ingress-filtering(yes | no; Default:yes) | Enables or disables VLAN ingress filtering, which checks if the ingress port is a member of the received VLAN ID in the bridge VLAN table. Should be used withframe-typesto specify if the ingress traffic should be tagged or untagged. This property only has effect whenvlan-filteringis set toyes. The setting is enabled by default since RouterOS v7.
learn(auto | no | yes; Default:auto) | Changes MAC learning behavior on a bridge portyes- enables MAC learningno- disables MAC learningauto- detects if bridge port is a Wireless interface and uses a Wireless registration table instead of MAC learning, will use Wireless registration table if theWireless interfaceis set to one ofap-bridge,bridge,wds-slavemode and bridge mode for theWireless interfaceis disabled.
multicast-router(disabled | permanent | temporary-query; Default:temporary-query) | A multicast router port is a port where a multicast router or querier is connected. On this port, unregistered multicast streams and IGMP/MLD membership reports will be sent. This setting changes the state of the multicast router for bridge ports. This property can be used to send IGMP/MLD membership reports to certain bridge ports for further multicast routing or proxying. This property only has an effect whenigmp-snoopingis set toyes.disabled- disabled multicast router state on the bridge port. Unregistered multicast and IGMP/MLD membership reports are not sent to the bridge port regardless of what is connected to it.permanent- enabled multicast router state on the bridge port. Unregistered multicast and IGMP/MLD membership reports are sent to the bridge port regardless of what is connected to it.temporary-query- automatically detect multicast router state on the bridge port using IGMP/MLD queries.
horizon(integer 0..429496729; Default:none) | Use split horizon bridging to prevent bridging loops. Set the same value for a group of ports, to prevent them from sending data to ports with the same horizon value. Split horizon is a software feature that disables hardware offloading. Read more aboutBridge split horizon.
hw(yes | no; Default:yes) | Allows to enable or disablehardware offloadingon interfaces capable of HW offloading. For software interfaces likeEoIPorVLANthis setting is ignored and has no effect. Certain bridge or port functions can automatically disable HW offloading, use theprintcommand to see whether the "H" flag is active.
internal-path-cost(integer: 1..200000000; Default:) | Path cost to the interface for MSTI0 inside a region. If not manually configured, the bridge automatically determines the internal-path-cost based on the interface speed and theport-cost-modesetting. To revert to the automatic determination and remove any manually applied value, simply use an exclamation mark before theinternal-path-costproperty. This property only has effect whenprotocol-modeis set tomstp./interface bridge port set [find interface=sfp28-1] !internal-path-costUseport monitorto observe the applied internal-path-cost.
interface(name; Default:none) | Name of the interface or interface list.
path-cost(integer: 1..200000000; Default:) | Path cost to the interface, used by STP and RSTP to determine the best path, and used by MSTP to determine the best path between regions. If not manually configured, the bridge automatically determines the path-cost based on the interface speed and theport-cost-modesetting. To revert to the automatic determination and remove any manually applied value, simply use an exclamation mark before thepath-costproperty. This property has no effect whenprotocol-modeis set tonone./interface bridge port set [find interface=sfp28-1] !path-costUseport monitorto observe the applied path-cost.
point-to-point(auto | yes | no; Default:auto) | Specifies if a bridge port is connected to a bridge using a point-to-point link for faster convergence in case of failure. By setting this property toyes, you are forcing the link to be a point-to-point link, which will skip the checking mechanism, which detects and waits for BPDUs from other devices from this single link. By setting this property tono, you are expecting that a link can receive BPDUs from multiple devices. By setting the property toyes, you are significantly improving (R/M)STP convergence time. In general, you should only set this property tonoif it is possible that another device can be connected between a link, this is mostly relevant to Wireless mediums and Ethernet hubs. If the Ethernet link is full-duplex,autoenables point-to-point functionality. This property has no effect whenprotocol-modeis set tonone.
priority(integer: 0..240; Default:128) | The priority of the interface, used by STP to determine the root port, used by MSTP to determine root port between regions.
pvid(integer 1..4094; Default:1) | Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. This property only has an effect whenvlan-filteringis set toyes.
restricted-role(yes | no; Default:no) | Enables or disables the restricted role on a port. When enabled, it prevents the port from becoming the root port for the CIST or any MSTI, regardless of its best spanning tree priority vector. Such a port will be selected as an Alternate Port (discarding state) and remains so as long as it continues to receive superior BPDUs. It will automatically transition to the forwarding state when it no longer detects a superior root path. Network administrators may enable this setting to safeguard against external bridges influencing the active spanning tree, a feature also known as root-guard or root-protection. This property has an effect whenprotocol-modeis set tostp,rstp, ormstp(support for STP and RSTP is available since RouterOS v7.14).
restricted-tcn(yes | no; Default:no) | Enables or disables topology change notification (TCN) handling on a port. When enabled, it causes the port not to propagate received topology change notifications to other ports, and any changes caused by the port itself does not result in topology change notification to other ports. This parameter is disabled by default. It can be set by a network administrator to prevent external bridges causing MAC address flushing in local network. This property has an effect whenprotocol-modeis set tostp,rstp, ormstp(support for STP and RSTP is available since RouterOS v7.14).
tag-stacking(yes | no; Default:no) | Forces all packets to be treated as untagged packets. Packets on ingress port will be tagged with another VLAN tag regardless if a VLAN tag already exists, packets will be tagged with a VLAN ID that matches thepvidvalue and will use EtherType that is specified inether-type. This property only has effect whenvlan-filteringis set toyes.
trusted(yes | no; Default:no) | When enabled, it allows forwarding DHCP packets towards the DHCP server through this port. Mainly used to limit unauthorized servers to provide malicious information for users. This property only has an effect whendhcp-snoopingis set toyes.
unknown-multicast-flood(yes | no; Default:yes) | Changes the multicast flood option on bridge port, only controls the egress traffic. When enabled, the bridge allows flooding multicast packets to the specified bridge port, but when disabled, the bridge restricts multicast traffic from being flooded to the specified bridge port. The setting affects all multicast traffic, this includes non-IP, IPv4, IPv6 and the link-local multicast ranges (e.g. 224.0.0.0/24 andff02::1).Note that whenigmp-snoopingis enabled and IGMP/MLD querier is detected, the bridge will automatically restrict unknown IP multicast from being flooded, so the setting is not mandatory for IGMP/MLD snooping setups.When using this setting together withigmp-snooping, the only multicast traffic that is allowed on the bridge port is the known multicast from the MDB table.
unknown-unicast-flood(yes | no; Default:yes) | Changes the unknown unicast flood option on bridge port, only controls the egress traffic. When enabled, the bridge allows flooding unknown unicast packets to the specified bridge port, but when disabled, the bridge restricts unknown unicast traffic from being flooded to the specified bridge port.If a MAC address is not learned inthe host table, then the traffic is considered as unknown unicast traffic and will be flooded to all ports. MAC address is learned as soon as a packet on a bridge port is received and the source MAC address is added to the bridge host table. Since it is required for the bridge to receive at least one packet on the bridge port to learn the MAC address, it is recommended to use static bridge host entries to avoid packets being dropped until the MAC address has been learned.
```
protocol-mode
```
```
rstp
```
```
mstp
```
```
edge
```
```
no
```
```
protocol-mode
```
```
none
```
```
protocol-mode
```
```
none
```
* no- non-edge port, will participate in learning and listening states in STP.
* no-discover- non-edge port with enabled discovery, will participate in learning and listening states in STP, a port can become an edge port if no BPDU is received.
* yes- edge port without discovery, will transit directly to forwarding state.
* yes-discover- edge port with enabled discovery, will transit directly to forwarding state.
* auto- same asno-discover, but will additionally detect if a bridge port is a Wireless interface with disabled bridge-mode, such interface will be automatically set as an edge port without discovery.
```
no
```
```
no-discover
```
```
yes
```
```
yes-discover
```
```
auto
```
```
no-discover
```
```
igmp-snooping
```
```
yes
```
```
vlan-filtering
```
```
yes
```
```
frame-types
```
```
vlan-filtering
```
```
yes
```
* yes- enables MAC learning
* no- disables MAC learning
* auto- detects if bridge port is a Wireless interface and uses a Wireless registration table instead of MAC learning, will use Wireless registration table if theWireless interfaceis set to one ofap-bridge,bridge,wds-slavemode and bridge mode for theWireless interfaceis disabled.
```
yes
```
```
no
```
```
auto
```
```
ap-bridge
```
```
bridge
```
```
wds-slave
```
```
igmp-snooping
```
```
yes
```
* disabled- disabled multicast router state on the bridge port. Unregistered multicast and IGMP/MLD membership reports are not sent to the bridge port regardless of what is connected to it.
* permanent- enabled multicast router state on the bridge port. Unregistered multicast and IGMP/MLD membership reports are sent to the bridge port regardless of what is connected to it.
* temporary-query- automatically detect multicast router state on the bridge port using IGMP/MLD queries.
```
disabled
```
```
permanent
```
```
temporary-query
```
```
print
```
Path cost to the interface for MSTI0 inside a region. If not manually configured, the bridge automatically determines the internal-path-cost based on the interface speed and theport-cost-modesetting. To revert to the automatic determination and remove any manually applied value, simply use an exclamation mark before theinternal-path-costproperty. This property only has effect whenprotocol-modeis set tomstp.
```
port-cost-mode
```
```
internal-path-cost
```
```
protocol-mode
```
```
mstp
```
```
/interface bridge port set [find interface=sfp28-1] !internal-path-cost
```
Useport monitorto observe the applied internal-path-cost.
Path cost to the interface, used by STP and RSTP to determine the best path, and used by MSTP to determine the best path between regions. If not manually configured, the bridge automatically determines the path-cost based on the interface speed and theport-cost-modesetting. To revert to the automatic determination and remove any manually applied value, simply use an exclamation mark before thepath-costproperty. This property has no effect whenprotocol-modeis set tonone.
```
port-cost-mode
```
```
path-cost
```
```
protocol-mode
```
```
none
```
```
/interface bridge port set [find interface=sfp28-1] !path-cost
```
Useport monitorto observe the applied path-cost.
```
yes
```
```
no
```
```
yes
```
```
no
```
```
auto
```
```
protocol-mode
```
```
none
```
```
vlan-filtering
```
```
yes
```
```
protocol-mode
```
```
stp
```
```
rstp
```
```
mstp
```
```
protocol-mode
```
```
stp
```
```
rstp
```
```
mstp
```
```
pvid
```
```
ether-type
```
```
vlan-filtering
```
```
yes
```
```
dhcp-snooping
```
```
yes
```
Changes the multicast flood option on bridge port, only controls the egress traffic. When enabled, the bridge allows flooding multicast packets to the specified bridge port, but when disabled, the bridge restricts multicast traffic from being flooded to the specified bridge port. The setting affects all multicast traffic, this includes non-IP, IPv4, IPv6 and the link-local multicast ranges (e.g. 224.0.0.0/24 andff02::1).
Note that whenigmp-snoopingis enabled and IGMP/MLD querier is detected, the bridge will automatically restrict unknown IP multicast from being flooded, so the setting is not mandatory for IGMP/MLD snooping setups.
```
igmp-snooping
```
When using this setting together withigmp-snooping, the only multicast traffic that is allowed on the bridge port is the known multicast from the MDB table.
```
igmp-snooping
```
Changes the unknown unicast flood option on bridge port, only controls the egress traffic. When enabled, the bridge allows flooding unknown unicast packets to the specified bridge port, but when disabled, the bridge restricts unknown unicast traffic from being flooded to the specified bridge port.
If a MAC address is not learned inthe host table, then the traffic is considered as unknown unicast traffic and will be flooded to all ports. MAC address is learned as soon as a packet on a bridge port is received and the source MAC address is added to the bridge host table. Since it is required for the bridge to receive at least one packet on the bridge port to learn the MAC address, it is recommended to use static bridge host entries to avoid packets being dropped until the MAC address has been learned.
## Example
To group ether1 and ether2 in the already created bridge1 interface.
```
[admin@MikroTik] /interface bridge port add bridge=bridge1 interface=ether1
[admin@MikroTik] /interface bridge port add bridge=bridge1 interface=ether2
[admin@MikroTik] /interface bridge port print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE       BRIDGE       HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0     ether1          bridge1      yes  100     0x80         10                 10       none
 1     ether2          bridge1      yes  200     0x80         10                 10       none
```
## Interface lists
Starting with RouterOS v6.41 it possible to add interface lists as a bridge port and sort them. Interface lists are useful for creating simpler firewall rules. Below is an example how to add an interface list to a bridge:
```
/interface list
add name=LAN1
add name=LAN2
/interface list member
add interface=ether1 list=LAN1
add interface=ether2 list=LAN1
add interface=ether3 list=LAN2
add interface=ether4 list=LAN2
/interface bridge port
add bridge=bridge1 interface=LAN1
add bridge=bridge1 interface=LAN2
```
Ports from an interface list added to a bridge will show up as dynamic ports:
```
[admin@MikroTik] /interface bridge port> pr
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE       BRIDGE       HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0     LAN1            bridge1      yes    1     0x80         10                 10       none
 1  D  ether1          bridge1      yes    1     0x80         10                 10       none
 2  D  ether2          bridge1      yes    1     0x80         10                 10       none
 3     LAN2            bridge1      yes    1     0x80         10                 10       none
 4  D  ether3          bridge1      yes    1     0x80         10                 10       none
 5  D  ether4          bridge1      yes    1     0x80         10                 10       none
```
It is also possible to sort the order of lists in which they appear. This can be done using themovecommand. Below is an example of how to sort interface lists:
```
move
```
```
[admin@MikroTik] > /interface bridge port move 3 0
[admin@MikroTik] > /interface bridge port print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE       BRIDGE       HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0     LAN2            bridge1      yes    1     0x80         10                 10       none
 1  D  ether3          bridge1      yes    1     0x80         10                 10       none
 2  D  ether4          bridge1      yes    1     0x80         10                 10       none
 3     LAN1            bridge1      yes    1     0x80         10                 10       none
 4  D  ether1          bridge1      yes    1     0x80         10                 10       none
 5  D  ether2          bridge1      yes    1     0x80         10                 10       none
```
Starting from RouterOS version 7.17, you can useinterface listsfor thetaggedanduntaggedproperties in thebridge VLAN table. This change allows for more flexible VLAN assignment to ports by simply modifying the interface list members, rather than updating each bridge VLAN entry individually.
```
tagged
```
```
untagged
```
If different interface lists are specified for thetaggedanduntaggedsettings, and there is overlap between the interface members, theuntaggedlist will take priority. You can check the current interface configuration withcurrent-taggedandcurrent-untaggedproperties using theprintcommand.
```
tagged
```
```
untagged
```
```
untagged
```
```
current-tagged
```
```
current-untagged
```
```
print
```
Below is an example where new interfaces are added to already existing interface lists. This shows how the bridge port and VLAN tables are automatically updated without directly changing settings in those menus.
```
/interface list
add name=vlan10_untagged
add name=vlan20_untagged
add name=vlan_tagged
/interface list member
add interface=ether2 list=vlan10_untagged
add interface=ether3 list=vlan10_untagged
add interface=ether4 list=vlan20_untagged
add interface=sfp-sfpplus1 list=vlan_tagged
/interface bridge
add frame-types=admit-only-vlan-tagged name=bridge1 vlan-filtering=yes
/interface bridge port
add bridge=bridge1 frame-types=admit-only-untagged-and-priority-tagged interface=vlan10_untagged pvid=10
add bridge=bridge1 frame-types=admit-only-untagged-and-priority-tagged interface=vlan20_untagged pvid=20
add bridge=bridge1 frame-types=admit-only-vlan-tagged interface=vlan_tagged
/interface bridge vlan
add bridge=bridge1 tagged=vlan_tagged vlan-ids=10
add bridge=bridge1 tagged=vlan_tagged vlan-ids=20
[admin@MikroTik] /interface bridge port print 
Flags: D - DYNAMIC; H - HW-OFFLOAD
Columns: INTERFACE, BRIDGE, HW, PVID, PRIORITY, HORIZON
#    INTERFACE        BRIDGE   HW   PVID  PRIORITY  HORIZON
0    vlan10_untagged  bridge1  yes    10  0x80      none   
1 DH ether2           bridge1  yes    10  0x80      none   
2 DH ether3           bridge1  yes    10  0x80      none   
3    vlan20_untagged  bridge1  yes    20  0x80      none   
4 DH ether4           bridge1  yes    20  0x80      none   
5    vlan_tagged      bridge1  yes     1  0x80      none   
6 DH sfp-sfpplus1     bridge1  yes     1  0x80      none   
[admin@MikroTik] /interface bridge vlan print
Flags: D - DYNAMIC
Columns: BRIDGE, VLAN-IDS, CURRENT-TAGGED, CURRENT-UNTAGGED
#   BRIDGE   VLAN-IDS  CURRENT-TAGGED  CURRENT-UNTAGGED
;;; added by pvid
0 D bridge1        10                  ether2          
                                       ether3          
;;; added by pvid
1 D bridge1        20                  ether4          
2   bridge1        10  sfp-sfpplus1                    
3   bridge1        20  sfp-sfpplus1                 
# make necessary changes to interface list members:
/interface list member add list=vlan20_untagged interface=ether5
/interface list member add list=vlan_tagged interface=sfp-sfpplus2 
# verify changes in bridge port and vlan menus:
[admin@MikroTik] > /interface bridge port print 
Flags: D - DYNAMIC; H - HW-OFFLOAD
Columns: INTERFACE, BRIDGE, HW, PVID, PRIORITY, HORIZON
#    INTERFACE        BRIDGE   HW   PVID  PRIORITY  HORIZON
0    vlan10_untagged  bridge1  yes    10  0x80      none   
1 DH ether2           bridge1  yes    10  0x80      none   
2 DH ether3           bridge1  yes    10  0x80      none   
3    vlan20_untagged  bridge1  yes    20  0x80      none   
4 DH ether4           bridge1  yes    20  0x80      none   
5 DH ether5           bridge1  yes    20  0x80      none   
6    vlan_tagged      bridge1  yes     1  0x80      none   
7 DH sfp-sfpplus1     bridge1  yes     1  0x80      none   
8 DH sfp-sfpplus2     bridge1  yes     1  0x80      none   
[admin@MikroTik] > /interface bridge vlan print 
Flags: D - DYNAMIC
Columns: BRIDGE, VLAN-IDS, CURRENT-TAGGED, CURRENT-UNTAGGED
#   BRIDGE   VLAN-IDS  CURRENT-TAGGED  CURRENT-UNTAGGED
;;; added by pvid
0 D bridge1        10                  ether2          
                                       ether3          
;;; added by pvid
1 D bridge1        20                  ether4          
                                       ether5          
2   bridge1        10  sfp-sfpplus1                    
                       sfp-sfpplus2                    
3   bridge1        20  sfp-sfpplus1                    
                       sfp-sfpplus2
```
## Bridge Port Monitoring
To monitor the current status of bridge ports, use themonitorcommand.
```
monitor
```
Sub-menu:/interface bridge port monitor
```
/interface bridge port monitor
```
Property | Description
----------------------
actual-path-cost(integer: 1..200000000) | Shows the actual port path-cost. Either manually applied or automatically determined based on the interface speed and theport-cost-modesetting.
designated-bridge(bridge identifier) | Shows the received bridge identifier.
designated-cost(integer) | Shows the received root-path-cost.
designated-port-number(integer) | Shows the received port number.
edge-port(yes | no) | Whether the port is an edge port or not.
edge-port-discovery(yes | no) | Whether the port is set to automatically detect edge ports.
external-fdb(yes | no) | Whether the registration table is used instead of a forwarding database.
forwarding(yes | no) | Shows if the port is not blocked by (R/M)STP.
hw-offload-group(switchX) | Switch chip used by the port.
interface(name) | Interface name.
learning(yes | no) | Shows whether the port is capable of learning MAC addresses.
multicast-router(yes | no) | Shows if a multicast router is detected on the port. Monitoring value appears only whenigmp-snoopingis enabled.
port-number(integer 1..4095) | A port-number will be assigned in the order that ports got added to the bridge, but this is only true until reboot. After reboot, the internal port numbering will be used.
point-to-point-port(yes | no) | Whether the port is connected to a bridge port using full-duplex (yes) or half-duplex (no).
role(designated | root-port | alternate | backup | disabled) | (R/M)STP algorithm assigned port role:disabled-port- disabled or inactive port.root-port- port that is facing towards the root bridge and has the best (lowest cost) path to the root bridge. Only one root port is elected per bridge (except the root bridge itself).alternative-port- port that is facing towards the root bridge, but is not going to forward traffic. Port provides a backup path to the root bridge if the current root port fails.designated-port- port that is facing away from the root bridge and forwards traffic away from the root bridge to downstream devices.backup-port- port that is facing away from the root bridge, but is going to forward traffic. Port that serves as a backup for a designated port on the same segment.In RouterOS, therolemonitoring property displays RSTP roles, such asalternate-portandbackup-port, even when STP mode is enabled. While this is technically incorrect, it does not affect the operation of STP. This is because STP treats all blocked ports the same, without differentiating their purpose (e.g., as potential backup paths). The displayed roles are simply a reflection of RSTP functionality and have no practical impact when STP is in use. See more details onSTP and RSTP page.
root-path-cost(integer) | The total cost of the path to the root-bridge
sending-rstp(yes | no) | Whether the port is using RSTP or MSTP BPDU types. A port will transit to STP type when RSTP/MSTP enabled port receives an STP BPDU. This settingsdoes notindicate whether the BDPUs are actually sent.
status(in-bridge | inactive) | Port status:in-bridge- port is enabledinactive- port is disabled.
```
port-cost-mode
```
```
igmp-snooping
```
(R/M)STP algorithm assigned port role:
* disabled-port- disabled or inactive port.
* root-port- port that is facing towards the root bridge and has the best (lowest cost) path to the root bridge. Only one root port is elected per bridge (except the root bridge itself).
* alternative-port- port that is facing towards the root bridge, but is not going to forward traffic. Port provides a backup path to the root bridge if the current root port fails.
* designated-port- port that is facing away from the root bridge and forwards traffic away from the root bridge to downstream devices.
* backup-port- port that is facing away from the root bridge, but is going to forward traffic. Port that serves as a backup for a designated port on the same segment.
```
disabled-port
```
```
root-port
```
```
alternative-port
```
```
designated-port
```
```
backup-port
```
In RouterOS, therolemonitoring property displays RSTP roles, such asalternate-portandbackup-port, even when STP mode is enabled. While this is technically incorrect, it does not affect the operation of STP. This is because STP treats all blocked ports the same, without differentiating their purpose (e.g., as potential backup paths). The displayed roles are simply a reflection of RSTP functionality and have no practical impact when STP is in use. See more details onSTP and RSTP page.
```
alternate-port
```
```
backup-port
```
* in-bridge- port is enabled
* inactive- port is disabled.
```
in-bridge
```
```
inactive
```
```
[admin@MikroTik] /interface bridge port monitor [find interface=sfp-sfpplus2]
               interface: sfp-sfpplus2
                  status: in-bridge
             port-number: 1
                    role: root-port
               edge-port: no
     edge-port-discovery: yes
     point-to-point-port: yes
            external-fdb: no
            sending-rstp: yes
                learning: yes
              forwarding: yes
               path-cost: 2000
          root-path-cost: 4000
       designated-bridge: 0x8000.DC:2C:6E:9E:11:1C
         designated-cost: 2000
  designated-port-number: 2
```
# Hosts Table
MAC addresses that have been learned on a bridge interface can be viewed in thehostmenu. Below is a table of parameters and flags that can be viewed.
Sub-menu:/interface bridge host
```
/interface bridge host
```
Property | Description
----------------------
bridge(read-only: name) | The bridge the entry belongs to
disabled(read-only: flag) | Whether the static host entry is disabled
dynamic(read-only: flag) | Whether the host has been dynamically created
external(read-only: flag) | Whether the host has been learned using an external table, for example, from a switch chip or Wireless registration table. Adding a static host entry on a hardware-offloaded bridge port will also display an active external flag
invalid(read-only: flag) | Whether the host entry is invalid, can appear for statically configured hosts on already removed interface
local(read-only: flag) | Whether the host entry is created from the bridge itself (that way all local interfaces are shown)
mac-address(read-only: MAC address) | Host's MAC address
on-interface(read-only: name) | Which of the bridged interfaces the host is connected to
## Monitoring
To get the active hosts table:
```
[admin@MikroTik] /interface bridge host print
Flags: X - disabled, I - invalid, D - dynamic, L - local, E - external 
 #       MAC-ADDRESS        VID ON-INTERFACE            BRIDGE
 0   D   B8:69:F4:C9:EE:D7      ether1                  bridge1
 1   D   B8:69:F4:C9:EE:D8      ether2                  bridge1
 2   DL  CC:2D:E0:E4:B3:38      bridge1                 bridge1
 3   DL  CC:2D:E0:E4:B3:39      ether2                  bridge1
```
## Static entries
It is possible to add a static MAC address entry into the host table. This can be used to forward a certain type of traffic through a specific port. Another use case for static host entries is to protect the device resources by disabling dynamic learning and relying only on configured static host entries. Below is a table of possible parameters that can be set when adding a static MAC address entry into the host table.
Sub-menu:/interface bridge host
```
/interface bridge host
```
Property | Description
----------------------
bridge(name; Default:none) | The bridge interface to which the MAC address is going to be assigned.
disabled(yes | no; Default:no) | Disables/enables static MAC address entry.
interface(name; Default:none) | Name of the interface.
mac-address(MAC address; Default: ) | MAC address that will be added to the host table statically.
vid(integer: 1..4094; Default: ) | VLAN ID for the statically added MAC address entry.
For example, if it was required that all traffic destined to4C:5E:0C:4D:12:43is forwarded only throughether2, then the following commands can be used:
```
/interface bridge host
add bridge=bridge interface=ether2 mac-address=4C:5E:0C:4D:12:43
```
# Multicast Table
WhenIGMP/MLD snoopingis enabled, the bridge will start to listen to IGMP/MLD communication, create multicast database (MDB) entries, and make forwarding decisions based on the received information. Packets with link-local multicast destination addresses 224.0.0.0/24 andff02::1 are not restricted and are always flooded on all ports and VLANs.To see learned multicast database entries, use theprintcommand.
```
print
```
Sub-menu:/interface bridge mdb
```
/interface bridge mdb
```
Property | Description
----------------------
bridge(read-only:name) | Shows the bridge interface the entry belongs to.
group(read-only:ipv4 | ipv6 | MAC address) | Shows a multicast group address.
on-ports(read-only: name) | Shows the bridge ports which are subscribed to the certain multicast group.
vid(read-only: integer) | Shows the VLAN ID for the multicast group, only applies whenvlan-filteringis enabled.
Property
Description
```
vlan-filtering
```
```
[admin@MikroTik] /interface bridge mdb print 
Flags: D - DYNAMIC
Columns: GROUP, VID, ON-PORTS, BRIDGE
 #   GROUP              VID  ON-PORTS  BRIDGE 
 0 D ff02::2              1  bridge1   bridge1
 1 D ff02::6a             1  bridge1   bridge1
 2 D ff02::1:ff00:0       1  bridge1   bridge1
 3 D ff02::1:ff01:6a43    1  bridge1   bridge1
 4 D 229.1.1.1           10  ether2    bridge1
 5 D 229.2.2.2           10  ether3    bridge1
                             ether2           
 6 D ff02::2             10  ether5    bridge1
                             ether3           
                             ether2           
                             ether4
```
## Static entries
Since RouterOS version 7.7, it is possible to create static MDB entries for IPv4 and IPv6 multicast groups.
Sub-menu:/interface bridge mdb
```
/interface bridge mdb
```
Property | Description
----------------------
bridge(name; Default: ) | The bridge interface to which the MDB entry is going to be assigned.
disabled(yes | no; Default:no) | Disables or enables static MDB entry.
group(ipv4 | ipv6 | MAC address; Default: ) | The IPv4, IPv6 or MAC multicast address. Static entries forlink-local multicast groups 224.0.0.0/24 andff02::1 cannot be created, as these packets are always flooded on all ports and VLANs.
ports(name; Default: ) | The list of bridge ports to which the multicast group will be forwarded.
vid(integer: 1..4094; Default: ) | The VLAN ID on which the MDB entry will be created, only applies whenvlan-filteringis enabled. When VLAN ID is not specified, the entry will work in shared-VLAN mode and dynamically apply on all defined VLAN IDs for particular ports.
Property
Description
```
vlan-filtering
```
For example, to create a static MDB entry for multicast group 229.10.10.10 on ports ether2 and ether3 on VLAN 10, use the command below:
```
/interface bridge mdb
add bridge=bridge1 group=229.10.10.10 ports=ether2,ether3 vid=10
```
Verify the results with theprintcommand:
```
print
```
```
[admin@MikroTik] > /interface bridge mdb print where group=229.10.10.10
Columns: GROUP, VID, ON-PORTS, BRIDGE
 # GROUP         VID  ON-PORTS  BRIDGE 
12 229.10.10.10   10  ether2    bridge1
                      ether3
```
In case a certain IPv6 multicast group does not need to be snooped and it is desired to be flooded on all ports and VLANs, it is possible to create a static MDB entry on all VLANs and ports, including the bridge interface itself. Use the command below to create a static MDB entry for multicast group ff02::2 on all VLANs and ports (modify theportssetting for your particular setup):
```
ports
```
```
/interface bridge mdb
add bridge=bridge1 group=ff02::2 ports=bridge1,ether2,ether3,ether4,ether5
[admin@MikroTik] > /interface bridge mdb print where group=ff02::2
Flags: D - DYNAMIC
Columns: GROUP, VID, ON-PORTS, BRIDGE
 #   GROUP    VID  ON-PORTS  BRIDGE 
 0   ff02::2                 bridge1
15 D ff02::2    1  bridge1   bridge1
16 D ff02::2   10  bridge1   bridge1
                   ether2           
                   ether3           
                   ether4           
                   ether5           
17 D ff02::2   20  bridge1   bridge1
                   ether2           
                   ether3           
18 D ff02::2   30  bridge1   bridge1
                   ether2           
                   ether3
```
# Bridge Hardware Offloading
It is possible to switch multiple ports together if a device has a built-in switch chip. While a bridge is a software feature that will consume CPU's resources, the bridge hardware offloading feature will allow you to use the built-in switch chip to forward packets. This allows you to achieve higher throughput if configured correctly.
In previous versions (prior to RouterOS v6.41) you had to use themaster-portproperty to switch multiple ports together, but in RouterOS v6.41 this property is replaced with the bridge hardware offloading feature, which allows your to switch ports and use some of the bridge features, for example,Spanning Tree Protocol.
Below is a list of devices and feature that supports hardware offloading (+) or disables hardware offloading (-):
RouterBoard/[Switch Chip] Model | Features in Switch menu | Bridge STP/RSTP | Bridge MSTP | Bridge IGMP Snooping | Bridge DHCP Snooping | Bridge VLAN Filtering | Bonding4, 5 | Horizon4
CRS3xx, CRS5xx series | + | + | + | + | + | + | + | -
CCR2116, CCR2216 | + | + | + | + | + | + | + | -
CRS1xx/CRS2xx series | + | + | - | +2 | +1 | - | - | -
[QCA8337] | + | + | - | - | +2 | - | - | -
[Atheros8327] | + | + | - | - | +2 | - | - | -
[Atheros8316] | + | + | - | - | +2 | - | - | -
[Atheros8227] | + | + | - | - | - | - | - | -
[Atheros7240] | + | + | - | - | - | - | - | -
[IPQ-PPE] | +6 | - | - | - | - | - | - | -
[ICPlus175D] | + | - | - | - | - | - | - | -
[MT7621, MT7531, EN7562CT] | + | +3 | +3 | - | - | +3 | - | -
[RTL8367] | + | +3 | +3 | - | - | +3 | - | -
[88E6393X,88E6191X, 88E6190] | + | + | + | + | + | +3 | +7 | -
[88E6393X,88E6191X, 88E6190]
Footnotes:
* The feature will not work properly in VLAN switching setups. It is possible to correctly snoop DHCP packets only for a single VLAN, but this requires that these DHCP messages get tagged with the correct VLAN tag using an ACL rule, for example,/interface ethernet switch acl add dst-l3-port=67-68 ip-protocol=udp mac-protocol=ip new-customer-vid=10 src-ports=switch1-cpu. DHCP Option 82 will not contain any information regarding VLAN-ID.
* The feature will not work properly in VLAN switching setups.
* The HW vlan-filtering and R/M/STP was added in the RouterOS 7.1rc1 (for RTL8367) and 7.1rc5 (for MT7621) versions. The switch does not support other ether-type 0x88a8 or 0x9100 (only 0x8100 is supported) and no tag-stacking. Using these features will disable HW offload.
* The HW offloading will be disabled only for the specific bridge port, not the entire bridge.
* Only802.3adandbalance-xormodes can be HW offloaded. Other bonding modes do not support HW offloading.
* Currently, HW offloaded bridge support for the IPQ-PPE switch chip is still a work in progress. We recommend using, the default, non-HW offloaded bridge (enabled RSTP).
* The802.3admode is compatible only with R/M/STP enabled bridge.
```
/interface ethernet switch acl add dst-l3-port=67-68 ip-protocol=udp mac-protocol=ip new-customer-vid=10 src-ports=switch1-cpu
```
```
802.3ad
```
```
balance-xor
```
```
802.3ad
```
Bridge Hardware Offloading should be considered as port switching, but with more possible features. By enabling hardware offloading you are allowing a built-in switch chip to process packets using its switching logic. The diagram below illustrates that switching occurs before any software related action.
A packet that is received by one of the ports always passes through the switch logic first. Switch logic decides which ports the packet should be going to (most commonly this decision is made based on the destination MAC address of a packet, but there might be other criteria that might be involved based on the packet and the configuration). In most cases the packet will not be visible to RouterOS (only statistics will show that a packet has passed through), this is because the packet was already processed by the switch chip and never reached the CPU.
Though it is possible in certain situations to allow a packet to be processed by the CPU, this is usually called a packet forwarding to the switch CPU port (or the bridge interface in bridge VLAN filtering scenario). This allows the CPU to process the packet and lets the CPU to forward the packet. Passing the packet to the CPU port will give you the opportunity to route packets to different networks, perform traffic control and other software related packet processing actions. To allow a packet to be processed by the CPU, you need to make certain configuration changes depending on your needs and on the device you are using (most commonly passing packets to the CPU are required for VLAN filtering setups). Check the manual page for your specific device:
* CRS1xx/2xx series switches
* CRS3xx, CRS5xx series switches and CCR2116, CCR2216 routers
* non-CRS series switches
## Example
Port switching with bridge configuration and enabled hardware offloading:
```
/interface bridge
add name=bridge1
/interface bridge port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether3 hw=yes
add bridge=bridge1 interface=ether4 hw=yes
add bridge=bridge1 interface=ether5 hw=yes
```
Make sure that hardware offloading is enabled and active by checking the "H" flag:
```
[admin@MikroTik] /interface bridge port print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE       BRIDGE       HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0   H ether2          bridge1      yes    1     0x80         10                 10       none
 1   H ether3          bridge1      yes    1     0x80         10                 10       none
 2   H ether4          bridge1      yes    1     0x80         10                 10       none
 3   H ether5          bridge1      yes    1     0x80         10                 10       none
```
# Bridge VLAN Filtering
Bridge VLAN Filtering provides VLAN-aware Layer 2 forwarding and VLAN tag modifications within the bridge. This set of features makes bridge operation more similar to a traditional Ethernet switch and allows overcoming Spanning Tree compatibility issues compared to the configuration when VLAN interfaces are bridged. Bridge VLAN Filtering configuration is highly recommended to comply with STP (IEEE 802.1D), RSTP (IEEE 802.1W) standards and is mandatory to enable MSTP (IEEE 802.1s) support in RouterOS.
The main VLAN setting isvlan-filteringwhich globally controls VLAN-awareness and VLAN tag processing in the bridge. Ifvlan-filtering=nois configured, the bridge ignores VLAN tags, works in a shared-VLAN-learning (SVL) mode, and cannot modify VLAN tags of packets. Turning onvlan-filteringenables all bridge VLAN related functionality and independent-VLAN-learning (IVL) mode. Besides joining the ports for Layer2 forwarding, the bridge itself is also an interface therefore it has Port VLAN ID (pvid).
```
vlan-filtering
```
```
vlan-filtering=no
```
```
vlan-filtering
```
## Bridge VLAN table
Bridge VLAN table represents per-VLAN port mapping with an egress VLAN tag action.Thetaggedports send out frames with a corresponding VLAN ID tag.Theuntaggedports remove a VLAN tag before sending out frames. Bridge ports withframe-typesset toadmit-alloradmit-only-untagged-and-priority-taggedwill be automatically added as untagged ports for thepvidVLAN.
```
tagged
```
```
untagged
```
```
frame-types
```
```
admit-all
```
```
admit-only-untagged-and-priority-tagged
```
```
pvid
```
Sub-menu:/interface bridge vlan
```
/interface bridge vlan
```
Property | Description
----------------------
bridge(name; Default:none) | The bridge interface which the respective VLAN entry is intended for.
disabled(yes | no; Default:no) | Enables or disables Bridge VLAN entry.
tagged(interfaces; Default:none) | Interfaces orinterface listwith a VLAN tag adding action in egress. This setting accepts comma-separated values. e.g.tagged=ether1,ether2.
untagged(interfaces; Default:none) | Interfaces orinterface listwith a VLAN tag removing action in egress. This setting accepts comma-separated values. e.g.untagged=ether3,ether4.
vlan-ids(integer 1..4094; Default:1) | The list of VLAN IDs for certain port configuration. This setting accepts the VLAN ID range as well as comma-separated values. e.g.vlan-ids=100-115,120,122,128-130.
```
tagged=ether1,ether2
```
```
untagged=ether3,ether4.
```
```
vlan-ids=100-115,120,122,128-130
```
## Bridge port settings
Each bridge port have multiple VLAN related settings, that can change untagged VLAN membership, VLAN tagging/untagging behavior and packet filtering based on VLAN tag presence.
Sub-menu:/interface bridge port
```
/interface bridge port
```
Property | Description
----------------------
frame-types(admit-all | admit-only-untagged-and-priority-tagged | admit-only-vlan-tagged; Default:admit-all) | Specifies allowed ingress frame types on a bridge port. This property only has an effect whenvlan-filteringis set toyes.
ingress-filtering(yes | no; Default:yes) | Enables or disables VLAN ingress filtering, which checks if the ingress port is a member of the received VLAN ID in the bridge VLAN table. Should be used withframe-typesto specify if the ingress traffic should be tagged or untagged. This property only has effect whenvlan-filteringis set toyes. The setting is enabled by default since RouterOS v7.
pvid(integer 1..4094; Default:1) | Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. This property only has an effect whenvlan-filteringis set toyes.
tag-stacking(yes | no; Default:no) | Forces all packets to be treated as untagged packets. Packets on ingress port will be tagged with another VLAN tag regardless if a VLAN tag already exists, packets will be tagged with a VLAN ID that matches thepvidvalue and will use EtherType that is specified inether-type. This property only has effect whenvlan-filteringis set toyes.
```
vlan-filtering
```
```
yes
```
```
frame-types
```
```
vlan-filtering
```
```
yes
```
```
vlan-filtering
```
```
yes
```
```
pvid
```
```
ether-type
```
```
vlan-filtering
```
```
yes
```
## Bridge host table
Bridge host table allows monitoring learned MAC addresses. Whenvlan-filteringis enabled, it shows learned VLAN ID as well (enabled independent-VLAN-learning or IVL).
```
vlan-filtering
```
```
[admin@MikroTik] > /interface bridge host print where !local 
Flags: X - disabled, I - invalid, D - dynamic, L - local, E - external 
 #       MAC-ADDRESS        VID ON-INTERFACE       BRIDGE
 0   D   CC:2D:E0:E4:B3:AA  300 ether3             bridge1
 1   D   CC:2D:E0:E4:B3:AB  400 ether4             bridge1
```
## VLAN Example - Trunk and Access Ports
Create a bridge with disabledvlan-filteringto avoid losing access to the device before VLANs are completely configured. If you need a management access to the bridge, see theManagement access configurationsection.
```
vlan-filtering
```
```
/interface bridge
add name=bridge1 vlan-filtering=no
```
Add bridge ports and specifypvidfor access ports to assign their untagged traffic to the intended VLAN. Useframe-typessetting to accept only tagged or untagged packets.
```
pvid
```
```
frame-types
```
```
/interface bridge port
add bridge=bridge1 interface=ether2 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether6 pvid=200 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether7 pvid=300 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether8 pvid=400 frame-types=admit-only-untagged-and-priority-tagged
```
Add Bridge VLAN entries and specify tagged ports in them.Bridge ports withframe-typesset toadmit-only-untagged-and-priority-taggedwill be automatically added as untagged ports for thepvidVLAN.
```
frame-types
```
```
admit-only-untagged-and-priority-tagged
```
```
pvid
```
```
/interface bridge vlan
add bridge=bridge1 tagged=ether2 vlan-ids=200 
add bridge=bridge1 tagged=ether2 vlan-ids=300
add bridge=bridge1 tagged=ether2 vlan-ids=400
```
In the end, when VLAN configuration is complete, enable Bridge VLAN Filtering.
```
/interface bridge set bridge1 vlan-filtering=yes
```
Optional step is to setframe-types=admit-only-vlan-taggedon the bridge interface in order to disable the default untagged VLAN 1 (pvid=1).
```
frame-types=admit-only-vlan-tagged
```
```
pvid=1
```
```
/interface bridge set bridge1 frame-types=admit-only-vlan-tagged
```
## VLAN Example - Trunk and Hybrid Ports
Create a bridge with disabledvlan-filteringto avoid losing access to the router before VLANs are completely configured. If you need a management access to the bridge, see theManagement access configurationsection.
```
vlan-filtering
```
```
/interface bridge
add name=bridge1 vlan-filtering=no
```
Add bridge ports and specifypvidon hybrid VLAN ports to assign untagged traffic to the intended VLAN.  Useframe-typessetting to accept only tagged packets on ether2.
```
pvid
```
```
frame-types
```
```
/interface bridge port
add bridge=bridge1 interface=ether2 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether6 pvid=200
add bridge=bridge1 interface=ether7 pvid=300
add bridge=bridge1 interface=ether8 pvid=400
```
Add Bridge VLAN entries and specify tagged ports in them. In this example egress VLAN tagging is done on ether6,ether7,ether8 ports too, making them into hybrid ports.Bridge ports withframe-typesset toadmit-allwill be automatically added as untagged ports for thepvidVLAN.
```
frame-types
```
```
admit-all
```
```
pvid
```
```
/interface bridge vlan 
add bridge=bridge1 tagged=ether2,ether7,ether8 vlan-ids=200
add bridge=bridge1 tagged=ether2,ether6,ether8 vlan-ids=300
add bridge=bridge1 tagged=ether2,ether6,ether7 vlan-ids=400
```
In the end, when VLAN configuration is complete, enable Bridge VLAN Filtering.
```
/interface bridge set bridge1 vlan-filtering=yes
```
Optional step is to setframe-types=admit-only-vlan-taggedon the bridge interface in order to disable the default untagged VLAN 1 (pvid=1).
```
frame-types=admit-only-vlan-tagged
```
```
pvid=1
```
```
/interface bridge set bridge1 frame-types=admit-only-vlan-tagged
```
## VLAN Example - InterVLAN Routing by Bridge
Create a bridge with disabledvlan-filteringto avoid losing access to the router before VLANs are completely configured.If you need a management access to the bridge, see theManagement access configurationsection.
```
vlan-filtering
```
```
/interface bridge
add name=bridge1 vlan-filtering=no
```
Add bridge ports and specifypvidfor VLAN access ports to assign their untagged traffic to the intended VLAN. Useframe-typessetting to accept only untagged packets.
```
pvid
```
```
frame-types
```
```
/interface bridge port
add bridge=bridge1 interface=ether6 pvid=200 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether7 pvid=300 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether8 pvid=400 frame-types=admit-only-untagged-and-priority-tagged
```
Add Bridge VLAN entries and specify tagged ports in them. In this examplebridge1interface is the VLAN trunk that will send traffic further to do InterVLAN routing.Bridge ports withframe-typesset toadmit-only-untagged-and-priority-taggedwill be automatically added as untagged ports for thepvidVLAN.
```
frame-types
```
```
admit-only-untagged-and-priority-tagged
```
```
pvid
```
```
/interface bridge vlan
add bridge=bridge1 tagged=bridge1 vlan-ids=200
add bridge=bridge1 tagged=bridge1 vlan-ids=300
add bridge=bridge1 tagged=bridge1 vlan-ids=400
```
Configure VLAN interfaces on thebridge1to allow handling of tagged VLAN traffic at routing level and set IP addresses to ensure routing between VLANs as planned.
```
/interface vlan
add interface=bridge1 name=VLAN200 vlan-id=200
add interface=bridge1 name=VLAN300 vlan-id=300
add interface=bridge1 name=VLAN400 vlan-id=400
/ip address
add address=20.0.0.1/24 interface=VLAN200
add address=30.0.0.1/24 interface=VLAN300
add address=40.0.0.1/24 interface=VLAN400
```
In the end, when VLAN configuration is complete, enable Bridge VLAN Filtering:
```
/interface bridge set bridge1 vlan-filtering=yes
```
Optional step is to setframe-types=admit-only-vlan-taggedon the bridge interface in order to disable the default untagged VLAN 1 (pvid=1).
```
frame-types=admit-only-vlan-tagged
```
```
pvid=1
```
```
/interface bridge set bridge1 frame-types=admit-only-vlan-tagged
```
Since RouterOS v7, it is possible to route traffic using the L3 HW offloading on certain devices. See more details onL3 Hardware Offloading.
## Management access configuration
There are multiple ways to set up management access on a device that uses bridge VLAN filtering. Below are some of the most popular approaches to properly enable access to a router/switch. Start by creating a bridge without VLAN filtering enabled:
```
/interface bridge
add name=bridge1 vlan-filtering=no
```
### Untagged access without VLAN filtering
In case VLAN filtering will not be used and access with untagged traffic is desired, the only requirement is to create an IP address on the bridge interface.
```
/ip address
add address=192.168.99.1/24 interface=bridge1
```
### Tagged access without VLAN filtering
In case VLAN filtering will not be used and access with tagged traffic is desired, create a routable VLAN interface on the bridge and add an IP address on the VLAN interface.
```
/interface vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip address
add address=192.168.99.1/24 interface=MGMT
```
### Tagged access with VLAN filtering
In case VLAN filtering is used and access with tagged traffic is desired, additional steps are required. In this example, VLAN 99 will be used to access the device. A VLAN interface on the bridge must be created and an IP address must be assigned to it.
```
/interface vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip address
add address=192.168.99.1/24 interface=MGMT
```
For example, if you want to allow access to the device from portsether3,ether4,sfp-sfpplus1using tagged VLAN 99 traffic, then you must add this entry to the VLAN table. Note that thebridge1interface is also included in the tagged port list:
```
/interface bridge vlan
add bridge=bridge1 tagged=bridge1,ether3,ether4,sfp-sfpplus1 vlan-ids=99
```
After that you can enable VLAN filtering:
```
/interface bridge set bridge1 vlan-filtering=yes
```
### Untagged access with VLAN filtering
In case VLAN filtering is used and access with untagged traffic is desired, the VLAN interface must use the same VLAN ID as the untagged port VLAN ID (pvid). Just like in the previous example, start by creating a VLAN interface on the bridge and add an IP address for the VLAN.
```
pvid
```
```
/interface vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip address
add address=192.168.99.1/24 interface=MGMT
```
For example, untagged portsether2andether3should be able to communicate with the VLAN 99 interface using untagged traffic. In order to achieve this, these ports should be configured with thepvidthat matches the VLAN ID on management VLAN. Note that thebridge1interface is a tagged port member, you can configure additional tagged ports if necessary (see the previous example).
```
pvid
```
```
/interface bridge port
set [find interface=ether2] pvid=99
set [find interface=ether3] pvid=99
/interface bridge vlan 
add bridge=bridge1 tagged=bridge1 untagged=ether2,ether3 vlan-ids=99
```
After that you can enable VLAN filtering:
```
/interface bridge set bridge1 vlan-filtering=yes
```
### Changing untagged VLAN for the bridge interface
In case VLAN filtering is used, it is possible to change the untagged VLAN ID for the bridge interface using thepvidsetting. Note that creating routable VLAN interfaces and allowing tagged traffic on the bridge is a more flexible and generally recommended option.
```
pvid
```
First, create an IP address on the bridge interface.
```
/ip address
add address=192.168.99.1/24 interface=bridge1
```
For example, untaggedbridge1traffic should be able to communicate with untaggedether2andether3ports and taggedsfp-sfpplus1port in VLAN 99. In order to achieve this,bridge1,ether2,ether3should be configured with the samepvidand sfp-sfpplus1 added as a tagged member.
```
pvid
```
```
/interface bridge
set [find name=bridge1] pvid=99
/interface bridge port
set [find interface=ether2] pvid=99
set [find interface=ether3] pvid=99
/interface bridge vlan
add bridge=bridge1 tagged=sfp-sfpplus1 untagged=bridge1,ether2,ether3 vlan-ids=99
```
After that you can enable VLAN filtering:
```
/interface bridge set bridge1 vlan-filtering=yes
```
## VLAN Tunneling (QinQ)
Since RouterOS v6.43 the RouterOS bridge is IEEE 802.1ad compliant and it is possible to filter VLAN IDs based on Service VLAN ID (0x88a8) rather than Customer VLAN ID (0x8100). The same principles can be applied as with IEEE 802.1Q VLAN filtering (the same setup examples can be used). Below is a topology for a commonProvider bridge:
In this example,R1,R2,R3,andR4might be sending any VLAN tagged traffic by 802.1Q (CVID), butSW1andSW2needs isolate traffic between routers in a way thatR1is able to communicate only withR3,andR2is only able to communicate withR4. To do so, you can tag all ingress traffic with an SVID and only allow these VLANs on certain ports. Start by enabling the service tag 0x88a8, introduced by802.1ad, on the bridge. Use these commands onSW1andSW2:
```
802.1ad
```
```
/interface bridge
add name=bridge1 vlan-filtering=no ether-type=0x88a8
```
In this setup,ether1andether2are going to be access ports (untagged), use thepvidparameter to tag all ingress traffic on each port, use these commands onSW1andSW2:
```
pvid
```
```
/interface bridge port
add interface=ether1 bridge=bridge1 pvid=200
add interface=ether2 bridge=bridge1 pvid=300
add interface=ether3 bridge=bridge1
```
Specify tagged and untagged ports in the bridge VLAN table, use these commands onSW1andSW2:
```
/interface bridge vlan
add bridge=bridge1 tagged=ether3 untagged=ether1 vlan-ids=200
add bridge=bridge1 tagged=ether3 untagged=ether2 vlan-ids=300
```
When the bridge VLAN table is configured, you can enable bridge VLAN filtering, use these commands onSW1andSW2:
```
/interface bridge set bridge1 vlan-filtering=yes
```
## Tag stacking
Since RouterOS v6.43 it is possible to forcefully add a new VLAN tag over any existing VLAN tags, this feature can be used to achieve a CVID stacking setup, where a CVID (0x8100) tag is added before an existing CVID tag. This type of setup is very similar totheProvider bridgesetup, to achieve the same setup but with multiple CVID tags (CVID stacking) we can use the same topology:
In this exampleR1,R2,R3,andR4might be sending any VLAN tagged traffic, it can be 802.1ad, 802.1Q or any other type of traffic, butSW1andSW2needs isolate traffic between routers in a way thatR1is able to communicate only withR3,andR2is only able to communicate withR4. To do so, you can tag all ingress traffic with a new CVID tag and only allow these VLANs on certain ports. Start by selecting the proper EtherType, use these commands onSW1andSW2:
```
/interface bridge
add name=bridge1 vlan-filtering=no ether-type=0x8100
```
In this setup,ether1andether2will ignore any VLAN tags that are present and add a new VLAN tag, use thepvidparameter to tag all ingress traffic on each port and allowtag-stackingon these ports, use these commands onSW1andSW2:
```
pvid
```
```
tag-stacking
```
```
/interface bridge port
add interface=ether1 bridge=bridge1 pvid=200 tag-stacking=yes
add interface=ether2 bridge=bridge1 pvid=300 tag-stacking=yes
add interface=ether3 bridge=bridge1
```
Specify tagged and untagged ports in the bridge VLAN table, you only need to specify the VLAN ID of the outer tag, use these commands onSW1andSW2:
```
/interface bridge vlan
add bridge=bridge1 tagged=ether3 untagged=ether1 vlan-ids=200
add bridge=bridge1 tagged=ether3 untagged=ether2 vlan-ids=300
```
When the bridge VLAN table is configured, you can enable bridge VLAN filtering, which is required in order for thepvidparameter to have any effect, use these commands onSW1andSW2:
```
/interface bridge set bridge1 vlan-filtering=yes
```
## MVRP
Multiple VLAN Registration protocol (MVRP) is a protocol based on Multiple Registration Protocol (MRP) which allows to register attributes (VLAN IDs in case of MVRP) with other members of Bridged LAN.
An MRP application can make or withdraw declarations of attributes which result in registration or leaving of those attributes with other MRP participants.
Here's how it works.
MRP consists of two parts:
* Applicant- responsible for sending declarations (or leaves). Its behavior can be configured on a per-port basis using the setting calledmvrp-applicant-state, and per-VLAN using themvrp-forbiddensetting.
* Registrar- responsible for registering incoming declarations. Its configuration can be set per-port using themvrp-registrar-statesetting, and per-VLAN using themvrp-forbiddensetting.
Applicant- responsible for sending declarations (or leaves). Its behavior can be configured on a per-port basis using the setting calledmvrp-applicant-state, and per-VLAN using themvrp-forbiddensetting.
```
mvrp-applicant-state
```
```
mvrp-forbidden
```
Registrar- responsible for registering incoming declarations. Its configuration can be set per-port using themvrp-registrar-statesetting, and per-VLAN using themvrp-forbiddensetting.
```
mvrp-registrar-state
```
```
mvrp-forbidden
```
Registration Propagation:Incoming registration on a bridge port dynamically makes that specific port a tagged VLAN member. Additionally, the attributes associated with this registration are spread to all active (forwarding) bridge ports as a declaration.
Declaration Operation:In case of MVRP, the configured VLAN's get declared on each port, but they will only get configured as members of those VLAN's when a declaration is received from the LAN (Registrar will register the VLAN). From the perspective of an end-station, a single declaration will be registered on each upstream port across the entire LAN. When another end-station declares the same attribute, a path of registrations will be made between the two (or more) end stations, see the picture below.
MVRP helps to dynamically propagate VLAN information throughout the bridged network and configure VLANs only on the needed ports. This makes the network efficient by avoiding unnecessary traffic flooding.
As noted before, MVRP is only active on ports that are forwarding. In case of MSTP declarations and registrations are made only if the port is forwarding in the MSTI in which VLAN is mapped.
The point-to-point ports speed up theprocess of registration (or leaving). Manually configuringpoint-to-point=yescan be advantageous for non-Ethernet interfaces.
```
point-to-point=yes
```
### Property Reference
Sub-menu:/interface bridge
```
/interface bridge
```
Property | Description
----------------------
mvrp(yes|no; Default:no) | Enables MVRP for bridge. It ensures that the MAC address 01:80:C2:00:00:21 is trapped and not forwarded, thevlan-filteringmust be enabled.
Property
Description
mvrp(yes|no; Default:no)
Enables MVRP for bridge. It ensures that the MAC address 01:80:C2:00:00:21 is trapped and not forwarded, thevlan-filteringmust be enabled.
```
vlan-filtering
```
Sub-menu:/interface bridge port
```
/interface bridge port
```
The port menu enables control over the applicant and registrar settings on a per-port basis.
Property | Description
----------------------
mvrp-applicant-state(non-participant | normal-participant;Default:normal-participant) | MVRP applicant options:non-participant- port does not send any MRP messages;normal-participant- port participates normally in MRP exchanges.
mvrp-registrar-state(fixed | normal; Default:normal) | MVRP registrar options:fixed- port ignores all MRP messages, and remains Registered (IN) in all configured vlans.normal- port receives MRP messages and handles them according to the standard.
Property
Description
mvrp-applicant-state(non-participant | normal-participant;Default:normal-participant)
MVRP applicant options:
* non-participant- port does not send any MRP messages;
* normal-participant- port participates normally in MRP exchanges.
non-participant- port does not send any MRP messages;
normal-participant- port participates normally in MRP exchanges.
mvrp-registrar-state(fixed | normal; Default:normal)
MVRP registrar options:
* fixed- port ignores all MRP messages, and remains Registered (IN) in all configured vlans.
* normal- port receives MRP messages and handles them according to the standard.
fixed- port ignores all MRP messages, and remains Registered (IN) in all configured vlans.
normal- port receives MRP messages and handles them according to the standard.
To monitor the currently declared and registered VLAN IDs, use themonitorcommand.
```
monitor
```
```
[admin@MikroTik] > interface/bridge/port monitor [find interface=sfp-sfpplus1]
            interface: sfp-sfpplus1
               status: in-bridge
          port-number: 1
                 role: designated-port
            edge-port: no
  edge-port-discovery: yes
  point-to-point-port: yes
         external-fdb: no
         sending-rstp: yes
             learning: yes
           forwarding: yes
     actual-path-cost: 2000
     hw-offload-group: switch1
    declared-vlan-ids: 1,10,20-21
  registered-vlan-ids: 1,10,20,30-33
```
Sub-menu:/interface bridge vlan
```
/interface bridge vlan
```
All ports that are members of static VLANs or dynamic untagged VLANs created by the portpvidsetting are treated as "fixed." Meaning the registrar disregards all MRP messages and remains registered (IN) for those VLANs.
```
pvid
```
When VLAN is neither manually configured nor created by the portpvidsetting, incoming registrations on a bridge port can dynamically designate that specific port as a tagged VLAN member. Themvrp-forbiddenfeature allows creating a list of ports that are restricted from registering into a specific VLAN ID.
```
pvid
```
```
mvrp-forbidden
```
VLANs that are static or dynamic will be declared by the applicants unless this functionality is disabled by the port'smvrp-applicant-state, or by VLAN'smvrp-forbiddensetting.
```
mvrp-applicant-state
```
```
mvrp-forbidden
```
Property | Description
----------------------
mvrp-forbidden(interfaces; Default:) | Ports that ignore all MRP messages and remains Not Registered (MT), as well as disables applicant from declaring specific VLAN ID.
Property
Description
mvrp-forbidden(interfaces; Default:)
Ports that ignore all MRP messages and remains Not Registered (MT), as well as disables applicant from declaring specific VLAN ID.
Sub-menu:/interface bridge vlan mvrp
```
/interface bridge vlan mvrp
```
The MVRP attributes menu can be used to see internal MVRP attribute states, as specified in the IEEE 802.1Q-2011.
Property | Description
----------------------
applicant-state | The Applicant state machine that declares attributes. Its state can be VO, VP, VN, AN, AA, QA, LA, AO, QO, AP, QP, or LO. Each state consists of two letters.The first letter indicates the state:V—Very anxious;A—Anxious;Q—Quiet;L—Leaving.The second letter indicates the membership state:A - Active member;P - Passive member;O - Observer;N - New.For example, VP indicates "Very anxious, Passive member."
registrar-state | The Registrar state machine that records the registration state of attributes declared by other participants. Its state can be IN, LV, or MT:IN—Registered;LV—Previously registered, but now being timed out;MT—Not registered.
Property
Description
applicant-state
The Applicant state machine that declares attributes. Its state can be VO, VP, VN, AN, AA, QA, LA, AO, QO, AP, QP, or LO. Each state consists of two letters.
The first letter indicates the state:
* V—Very anxious;
* A—Anxious;
* Q—Quiet;
* L—Leaving.
The second letter indicates the membership state:
* A - Active member;
* P - Passive member;
* O - Observer;
* N - New.
For example, VP indicates "Very anxious, Passive member."
registrar-state
The Registrar state machine that records the registration state of attributes declared by other participants. Its state can be IN, LV, or MT:
* IN—Registered;
* LV—Previously registered, but now being timed out;
* MT—Not registered.
```
[admin@Mikrotik] /interface/bridge/vlan/mvrp print where vlan-id=10
Columns: BRIDGE, PORT, VLAN-ID, REGISTRAR-STATE, APPLICANT-STATE, LAST-EVENT
 #  BRIDGE    PORT           VLAN-ID  REGISTRAR-STATE  APPLICANT-STATE  LAST-EVENT
 1  bridge67  sfp-sfpplus1        10  IN               Quiet Active     JoinIn    
 9  bridge67  sfp-sfpplus5        10  MT               Quiet Active     JoinEmpty 
17  bridge67  sfp-sfpplus9        10  MT               Quiet Active     JoinEmpty 
25  bridge67  sfp-sfpplus13       10  IN               Quiet Active     JoinIn
```
# Fast Forward
Fast Forward allows forwarding packets faster under special conditions. When Fast Forward is enabled, then the bridge can process packets even faster since it can skip multiple bridge-related checks, including MAC learning. Below you can find a list of conditions thatMUSTbe met in order for Fast Forward to be active:
* Bridge hasfast-forwardset toyes
* Bridge has only 2 running ports
* Both bridge ports supportFast Path, Fast Path is active on ports and globally on the bridge
* Bridge Hardware Offloadingis disabled
* Bridge VLAN Filteringis disabled
* Bridge DHCP snoopingis disabled
* unknown-multicast-floodis set toyes
* unknown-unicast-floodis set toyes
* broadcast-floodis set toyes
* MAC address for the bridge matches with a MAC address from one of the bridge slave ports
* horizonfor both ports is set tonone
```
fast-forward
```
```
yes
```
```
unknown-multicast-flood
```
```
yes
```
```
unknown-unicast-flood
```
```
yes
```
```
broadcast-flood
```
```
yes
```
```
horizon
```
```
none
```
It is possible to check how many packets where processed by Fast Forward:
```
[admin@MikroTik] /interface bridge settings> pr
              use-ip-firewall: no
     use-ip-firewall-for-vlan: no
    use-ip-firewall-for-pppoe: no
              allow-fast-path: yes
      bridge-fast-path-active: yes
     bridge-fast-path-packets: 0
       bridge-fast-path-bytes: 0
  bridge-fast-forward-packets: 16423
    bridge-fast-forward-bytes: 24864422
```
Since RouterOS 6.44 it is possible to monitor Fast Forward status, for example:
```
[admin@MikroTik] /interface bridge monitor bridge1 
                  state: enabled
    current-mac-address: B8:69:F4:C9:EE:D7
            root-bridge: yes
         root-bridge-id: 0x8000.B8:69:F4:C9:EE:D7
         root-path-cost: 0
              root-port: none
             port-count: 2
  designated-port-count: 2
           fast-forward: yes
```
# IGMP/MLD Snooping
The bridge supports IGMP/MLD snooping. It controls multicast streams and prevents multicast flooding on unnecessary ports. Its settings are placed in the bridge menu and it works independently in every bridge interface. Software-driven implementation works on all devices with RouterOS, but CRS3xx, CRS5xx series switches, CCR2116, CR2216 routers, and88E6393X, 88E6191X, 88E6190 switch chipsalso support IGMP/MLD snooping with hardware offloading. See more details onIGMP/MLD snooping manual.
# DHCP Snooping and DHCP Option 82
DHCP Snooping and DHCP Option 82 is supported by bridge. The DHCP Snooping is a Layer2 security feature, that limits unauthorized DHCP servers from providing malicious information to users. In RouterOS, you can specify which bridge ports are trusted (where known DHCP server resides and DHCP messages should be forwarded) and which are untrusted (usually used for access ports, received DHCP server messages will be dropped). The DHCP Option 82 is additional information (Agent Circuit ID and Agent Remote ID) provided by DHCP Snooping enabled devices that allow identifying the device itself and DHCP clients.
In this example, SW1 and SW2 are DHCP Snooping, and Option 82 enabled devices. First, we need to create a bridge, assign interfaces and mark trusted ports. Use these commands onSW1:
```
/interface bridge
add name=bridge
/interface bridge port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2 trusted=yes
```
For SW2, the configuration will be similar, but we also need to mark ether1 as trusted, because this interface is going to receive DHCP messages with Option 82 already added. You need to mark all ports as trusted if they are going to receive DHCP messages with added Option 82, otherwise these messages will be dropped. Also, we add ether3 to the same bridge and leave this port untrusted, imagine there is an unauthorized (rogue) DHCP server. Use these commands onSW2:
```
/interface bridge
add name=bridge
/interface bridge port
add bridge=bridge interface=ether1 trusted=yes
add bridge=bridge interface=ether2 trusted=yes
add bridge=bridge interface=ether3
```
Then we need to enable DHCP Snooping and Option 82. In case your DHCP server does not support DHCP Option 82 or you do not implement any Option 82 related policies, this option can be disabled. Use these commands onSW1andSW2:
```
/interface bridge
set [find where name="bridge"] dhcp-snooping=yes add-dhcp-option82=yes
```
Now both devices will analyze what DHCP messages are received on bridge ports. TheSW1is responsible for adding and removing the DHCP Option 82. TheSW2will limit rogue DHCP server from receiving any discovery messages and drop malicious DHCP server messages from ether3.
# Controller Bridge and Port Extender
Controller Bridge (CB) and Port Extender (PE) is an IEEE 802.1BR standard implementation in RouterOS for CRS3xx, CRS5xx series switches and CCR2116, CCR2216 routers. It allows virtually extending the CB ports with a PE device and managing these extended interfaces from a single controlling device. Such configuration provides a simplified network topology, flexibility, increased port density, and ease of manageability. See more details onController Bridge and Port Extender manual.
# Bridge Firewall
The bridge firewall implements packet filtering and thereby provides security functions that are used to manage data flow to, from, and through the bridge.
Packet flow diagramshows how packets are processed through the router. It is possible to force bridge traffic to go through/ip firewall filterrules (see the bridge settings).
```
/ip firewall filter
```
There are two bridge firewall tables:
* filter- bridge firewall with three predefined chains:input- filters packets, where the destination is the bridge (including those packets that will be routed, as they are destined to the bridge MAC address anyway)output- filters packets, which come from the bridge (including those packets that has been routed normally)forward- filters packets, which are to be bridged (note: this chain is not applied to the packets that should be routed through the router, just to those that are traversing between the ports of the same bridge)
* nat- bridge network address translation provides ways for changing source/destination MAC addresses of the packets traversing a bridge. Has two built-in chains:srcnat- used for "hiding" a host or a network behind a different MAC address. This chain is applied to the packets leaving the router through a bridged interfacedstnat- used for redirecting some packets to other destinations
* input- filters packets, where the destination is the bridge (including those packets that will be routed, as they are destined to the bridge MAC address anyway)
* output- filters packets, which come from the bridge (including those packets that has been routed normally)
* forward- filters packets, which are to be bridged (note: this chain is not applied to the packets that should be routed through the router, just to those that are traversing between the ports of the same bridge)
* srcnat- used for "hiding" a host or a network behind a different MAC address. This chain is applied to the packets leaving the router through a bridged interface
* dstnat- used for redirecting some packets to other destinations
You can put packet marks in bridge firewall (filter and NAT), which are the same as the packet marks in IP firewall configured by'/ip firewall mangle'. In this way, packet marks put by bridge firewall can be used in 'IP firewall', and vice versa.
```
'/ip firewall mangle'
```
General bridge firewall properties are described in this section. Some parameters that differ between nat and filter rules are described in further sections.
Sub-menu:/interface bridge filter, /interface bridge nat
```
/interface bridge filter, /interface bridge nat
```
Property | Description
----------------------
802.3-sap(integer; Default: ) | DSAP (Destination Service Access Point) and SSAP (Source Service Access Point) are 2 one-byte fields, which identify the network protocol entities which use the link-layer service. These bytes are always equal. Two hexadecimal digits may be specified here to match an SAP byte.
802.3-type(integer; Default: ) | Ethernet protocol type, placed after the IEEE 802.2 frame header. Works only if 802.3-sap is 0xAA (SNAP - Sub-Network Attachment Point header). For example, AppleTalk can be indicated by the SAP code of 0xAA followed by a SNAP type code of 0x809B.
action(accept | drop | jump | log | mark-packet | passthrough | return | set-priority; Default: ) | Action to take if the packet is matched by the rule:accept- accept the packet. The packet is not passed to the next firewall ruledrop- silently drop the packetjump- jump to the user-defined chain specified by the value ofjump-targetparameterlog- add a message to the system log containing the following data: in-interface, out-interface, src-mac, protocol, src-ip:port->dst-ip:port and length of the packet. After the packet is matched it is passed to the next rule in the list, similar aspassthroughmark-packet- place a mark specified by the new-packet-mark parameter on a packet that matches the rulepassthrough- if the packet is matched by the rule, increase counter and go to next rule (useful for statistics)return- passes control back to the chain from where the jump took placeset-priority- set priority specified by the new-priority parameter on the packets sent out through a link that is capable of transporting priority (VLAN or WMM-enabled wireless interface).Read more
arp-dst-address(IP address; Default: ) | ARP destination IP address.
arp-dst-mac-address(MAC address; Default: ) | ARP destination MAC address.
arp-gratuitous(yes | no; Default: ) | Matches ARP gratuitous packets.
arp-hardware-type(integer; Default:1) | ARP hardware type. This is normally Ethernet (Type 1).
arp-opcode(arp-nak | drarp-error | drarp-reply | drarp-request | inarp-reply | inarp-request | reply | reply-reverse | request | request-reverse; Default: ) | ARP opcode (packet type)arp-nak- negative ARP reply (rarely used, mostly in ATM networks)drarp-error- Dynamic RARP error code, saying that an IP address for the given MAC address can not be allocateddrarp-reply- Dynamic RARP reply, with a temporary IP address assignment for a hostdrarp-request- Dynamic RARP request to assign a temporary IP address for the given MAC addressinarp-reply- InverseARP Replyinarp-request- InverseARP Requestreply- standard ARP reply with a MAC addressreply-reverse- reverse ARP (RARP) reply with an IP address assignedrequest- standard ARP request to a known IP address to find out unknown MAC addressrequest-reverse- reverse ARP (RARP) request to a known MAC address to find out the unknown IP address (intended to be used by hosts to find out their own IP address, similarly to DHCP service)
arp-packet-type(integer 0..65535 | hex 0x0000-0xffff; Default: ) | ARP Packet Type.
arp-src-address(IP address; Default: ) | ARP source IP address.
arp-src-mac-address(MAC addres; Default: ) | ARP source MAC address.
chain(text; Default: ) | Bridge firewall chain, which the filter is functioning in (either a built-in one, or a user-defined one).
dst-address(IP address; Default: ) | Destination IP address (only if MAC protocol is set to IP).
dst-address6(IPv6 address; Default: ) | Destination IPv6 address (only if MAC protocol is set to IPv6).
dst-mac-address(MAC address; Default: ) | Destination MAC address.
dst-port(integer 0..65535; Default: ) | Destination port number or range (only for TCP or UDP protocols).
in-bridge(name; Default: ) | Bridge interface through which the packet is coming in.
in-bridge-list(name; Default: ) | Set of bridge interfaces defined ininterface list. Works the same asin-bridge.
in-interface(name; Default: ) | Physical interface (i.e., bridge port) through which the packet is coming in.
in-interface-list(name; Default: ) | Set of interfaces defined ininterface list. Works the same asin-interface.
ingress-priority(integer 0..63; Default: ) | Matches the priority of an ingress packet. Priority may be derived from VLAN, WMM, DSCP or MPLS EXP bit.read more
ip-protocol(dccp | ddp | egp | encap | etherip | ggp | gre | hmp | icmp | icmpv6 | idpr-cmtp | igmp | ipencap | ipip | ipsec-ah | ipsec-esp | ipv6 | ipv6-frag | ipv6-nonxt | ipv6-opts | ipv6-route | iso-tp4 | l2tp | ospf | pim | pup | rdp | rspf | rsvp | sctp | st | tcp | udp | udp-lite | vmtp | vrrp | xns-idp | xtp; Default: ) | IP protocol (only if MAC protocol is set to IPv4)dccp- Datagram Congestion Control Protocolddp- Datagram Delivery Protocolegp- Exterior Gateway Protocolencap- Encapsulation Headeretherip- Ethernet-within-IP Encapsulationggp- Gateway-to-Gateway Protocolgre- Generic Routing Encapsulationhmp- Host Monitoring Protocolicmp- IPv4 Internet Control Message Protocolicmpv6- IPv6 Internet Control Message Protocolidpr-cmtp- Inter-Domain Policy Routing Control Message Transport Protocoligmp- Internet Group Management Protocolipencap- IP in IP (encapsulation)ipip- IP-within-IP Encapsulation Protocolipsec-ah- IPsec Authentication Headeripsec-esp- IPsec Encapsulating Security Payloadipv6- Internet Protocol version 6ipv6-frag- Fragment Header for IPv6ipv6-nonxt- No Next Header for IPv6ipv6-opts- Destination Options for IPv6ipv6-route- Routing Header for IPv6iso-tp4- ISO Transport Protocol Class 4l2tp- Layer Two Tunneling Protocolospf- Open Shortest Path Firstpim- Protocol Independent Multicastpup- PARC Universal Packetrdp- Reliable Data Protocolrspf- Radio Shortest Path Firstrsvp- Reservation Protocolsctp- Stream Control Transmission Protocolst- Internet Stream Protocoltcp- Transmission Control Protocoludp- User Datagram Protocoludp-lite- Lightweight User Datagram Protocolvmtp- Versatile Message Transaction Protocolvrrp- Virtual Router Redundancy Protocolxns-idp- Xerox Network Systems Internet Datagram Protocolxtp- Xpress Transport Protocol
jump-target(name; Default: ) | Ifaction=jumpspecified, then specifies the user-defined firewall chain to process the packet.
limit(integer/time,integer; Default: ) | Matches packets up to a limited rate. A rule using this matcher will match until this limit is reached.count- maximum average packet rate, measured in packets per second (pps), unless followed by Time optiontime- specifies the time interval over which the packet rate is measuredburst- number of packets to match in a burst
log(yes | no; Default:no) | Add a message to the system log containing the following data: in-interface, out-interface, src-mac, dst-mac, eth-protocol, ip-protocol, src-ip:port->dst-ip:port, and length of the packet.
log-prefix(text; Default: ) | Defines the prefix to be printed before the logging information.
mac-protocol(802.2 | arp | capsman | dot1x | homeplug-av | ip | ipv6 | ipx | lacp | length | lldp | loop-protect | macsec | mpls-multicast | mpls-unicast | packing-compr | packing-simple | pppoe | pppoe-discovery | rarp | romon | service-vlan | vlan | integer 0..65535 | hex 0x0000-0xffff; Default: ) | Ethernet payload type (MAC-level protocol). To match protocol type for VLAN encapsulated frames (0x8100 or 0x88a8), avlan-encapproperty should be used.802.2- 802.2 Frames (0x0004)arp- Address Resolution Protocol (0x0806)homeplug-av- HomePlug AV MME (0x88E1)ip- Internet Protocol version 4 (0x0800)ipv6- Internet Protocol Version 6 (0x86DD)ipx- Internetwork Packet Exchange (0x8137)length- Packets with length field (0x0000-0x05DC)lldp- Link Layer Discovery Protocol (0x88CC)loop-protect- Loop Protect Protocol (0x9003)mpls-multicast- MPLS multicast (0x8848)mpls-unicast- MPLS unicast (0x8847)packing-compr- Encapsulated packets with compressedIP packing(0x9001)packing-simple- Encapsulated packets with simpleIP packing(0x9000)pppoe- PPPoE Session Stage (0x8864)pppoe-discovery- PPPoE Discovery Stage (0x8863)rarp- Reverse Address Resolution Protocol (0x8035)service-vlan- Provider Bridging (IEEE 802.1ad) & Shortest Path Bridging IEEE 802.1aq (0x88A8)vlan- VLAN-tagged frame (IEEE 802.1Q) and Shortest Path Bridging IEEE 802.1aq with NNI compatibility (0x8100)
new-packet-mark(string; Default: ) | Sets a new packet-mark value.
new-priority(integer | from-ingress; Default: ) | Sets a new priority for a packet. This can be the VLAN, WMM or MPLS EXP priorityRead more. This property can also be used to set an internal priori
out-bridge(name; Default: ) | Outgoing bridge interface.
out-bridge-list(name; Default: ) | Set of bridge interfaces defined ininterface list. Works the same asout-bridge.
out-interface(name; Default: ) | Interface that the packet is leaving the bridge through.
out-interface-list(name; Default: ) | Set of interfaces defined ininterface list. Works the same asout-interface.
packet-mark(name; Default: ) | Match packets with a certain packet mark.
packet-type(broadcast | host | multicast | other-host; Default: ) | MAC frame type:broadcast- broadcast MAC packethost- packet is destined to the bridge itselfmulticast- multicast MAC packetother-host- packet is destined to some other unicast address, not to the bridge itself
src-address(IP address; Default: ) | Source IP address (only if MAC protocol is set to IPv4).
src-address6(IPv6 address; Default: ) | Source IPv6 address (only if MAC protocol is set to IPv6).
src-mac-address(MAC address; Default: ) | Source MAC address.
src-port(integer 0..65535; Default: ) | Source port number or range (only for TCP or UDP protocols).
stp-flags(topology-change | topology-change-ack; Default: ) | The BPDU (Bridge Protocol Data Unit) flags. Bridge exchange configuration messages named BPDU periodically for preventing loopstopology-change- topology change flag is set when a bridge detects port state change, to force all other bridges to drop their host tables and recalculate network topologytopology-change-ack- topology change acknowledgment flag is sent in replies to the notification packets
stp-forward-delay(integer 0..65535; Default: ) | Forward delay timer.
stp-hello-time(integer 0..65535; Default: ) | STP hello packets time.
stp-max-age(integer 0..65535; Default: ) | Maximal STP message age.
stp-msg-age(integer 0..65535; Default: ) | STP message age.
stp-port(integer 0..65535; Default: ) | STP port identifier.
stp-root-address(MAC address; Default: ) | Root bridge MAC address.
stp-root-cost(integer 0..65535; Default: ) | Root bridge cost.
stp-root-priority(integer 0..65535; Default: ) | Root bridge priority.
stp-sender-address(MAC address; Default: ) | STP message sender MAC address.
stp-sender-priority(integer 0..65535; Default: ) | STP sender priority.
stp-type(config | tcn; Default: ) | The BPDU type:config- configuration BPDUtcn- topology change notification
tls-host(string; Default: ) | Allows matching https traffic based on TLS SNI hostname. AcceptsGLOB syntaxfor wildcard matching. Note that matcher will not be able to match hostname if the TLS handshake frame is fragmented into multiple TCP segments (packets).
vlan-encap(802.2 | arp | ip | ipv6 | ipx | length | mpls-multicast | mpls-unicast | pppoe | pppoe-discovery | rarp | vlan | integer 0..65535 | hex 0x0000-0xffff; Default: ) | Matches the MAC protocol type encapsulated in the VLAN frame.
vlan-id(integer 0..4095; Default: ) | Matches the VLAN identifier field.
vlan-priority(integer 0..7; Default: ) | Matches the VLAN priority (priority code point)
* accept- accept the packet. The packet is not passed to the next firewall rule
* drop- silently drop the packet
* jump- jump to the user-defined chain specified by the value ofjump-targetparameter
* log- add a message to the system log containing the following data: in-interface, out-interface, src-mac, protocol, src-ip:port->dst-ip:port and length of the packet. After the packet is matched it is passed to the next rule in the list, similar aspassthrough
* mark-packet- place a mark specified by the new-packet-mark parameter on a packet that matches the rule
* passthrough- if the packet is matched by the rule, increase counter and go to next rule (useful for statistics)
* return- passes control back to the chain from where the jump took place
* set-priority- set priority specified by the new-priority parameter on the packets sent out through a link that is capable of transporting priority (VLAN or WMM-enabled wireless interface).Read more
```
jump-target
```
```
passthrough
```
* arp-nak- negative ARP reply (rarely used, mostly in ATM networks)
* drarp-error- Dynamic RARP error code, saying that an IP address for the given MAC address can not be allocated
* drarp-reply- Dynamic RARP reply, with a temporary IP address assignment for a host
* drarp-request- Dynamic RARP request to assign a temporary IP address for the given MAC address
* inarp-reply- InverseARP Reply
* inarp-request- InverseARP Request
* reply- standard ARP reply with a MAC address
* reply-reverse- reverse ARP (RARP) reply with an IP address assigned
* request- standard ARP request to a known IP address to find out unknown MAC address
* request-reverse- reverse ARP (RARP) request to a known MAC address to find out the unknown IP address (intended to be used by hosts to find out their own IP address, similarly to DHCP service)
```
in-bridge
```
```
in-interface
```
* dccp- Datagram Congestion Control Protocol
* ddp- Datagram Delivery Protocol
* egp- Exterior Gateway Protocol
* encap- Encapsulation Header
* etherip- Ethernet-within-IP Encapsulation
* ggp- Gateway-to-Gateway Protocol
* gre- Generic Routing Encapsulation
* hmp- Host Monitoring Protocol
* icmp- IPv4 Internet Control Message Protocol
* icmpv6- IPv6 Internet Control Message Protocol
* idpr-cmtp- Inter-Domain Policy Routing Control Message Transport Protocol
* igmp- Internet Group Management Protocol
* ipencap- IP in IP (encapsulation)
* ipip- IP-within-IP Encapsulation Protocol
* ipsec-ah- IPsec Authentication Header
* ipsec-esp- IPsec Encapsulating Security Payload
* ipv6- Internet Protocol version 6
* ipv6-frag- Fragment Header for IPv6
* ipv6-nonxt- No Next Header for IPv6
* ipv6-opts- Destination Options for IPv6
* ipv6-route- Routing Header for IPv6
* iso-tp4- ISO Transport Protocol Class 4
* l2tp- Layer Two Tunneling Protocol
* ospf- Open Shortest Path First
* pim- Protocol Independent Multicast
* pup- PARC Universal Packet
* rdp- Reliable Data Protocol
* rspf- Radio Shortest Path First
* rsvp- Reservation Protocol
* sctp- Stream Control Transmission Protocol
* st- Internet Stream Protocol
* tcp- Transmission Control Protocol
* udp- User Datagram Protocol
* udp-lite- Lightweight User Datagram Protocol
* vmtp- Versatile Message Transaction Protocol
* vrrp- Virtual Router Redundancy Protocol
* xns-idp- Xerox Network Systems Internet Datagram Protocol
* xtp- Xpress Transport Protocol
```
action=jump
```
* count- maximum average packet rate, measured in packets per second (pps), unless followed by Time option
* time- specifies the time interval over which the packet rate is measured
* burst- number of packets to match in a burst
* 802.2- 802.2 Frames (0x0004)
* arp- Address Resolution Protocol (0x0806)
* homeplug-av- HomePlug AV MME (0x88E1)
* ip- Internet Protocol version 4 (0x0800)
* ipv6- Internet Protocol Version 6 (0x86DD)
* ipx- Internetwork Packet Exchange (0x8137)
* length- Packets with length field (0x0000-0x05DC)
* lldp- Link Layer Discovery Protocol (0x88CC)
* loop-protect- Loop Protect Protocol (0x9003)
* mpls-multicast- MPLS multicast (0x8848)
* mpls-unicast- MPLS unicast (0x8847)
* packing-compr- Encapsulated packets with compressedIP packing(0x9001)
* packing-simple- Encapsulated packets with simpleIP packing(0x9000)
* pppoe- PPPoE Session Stage (0x8864)
* pppoe-discovery- PPPoE Discovery Stage (0x8863)
* rarp- Reverse Address Resolution Protocol (0x8035)
* service-vlan- Provider Bridging (IEEE 802.1ad) & Shortest Path Bridging IEEE 802.1aq (0x88A8)
* vlan- VLAN-tagged frame (IEEE 802.1Q) and Shortest Path Bridging IEEE 802.1aq with NNI compatibility (0x8100)
```
out-bridge
```
```
out-interface
```
* broadcast- broadcast MAC packet
* host- packet is destined to the bridge itself
* multicast- multicast MAC packet
* other-host- packet is destined to some other unicast address, not to the bridge itself
* topology-change- topology change flag is set when a bridge detects port state change, to force all other bridges to drop their host tables and recalculate network topology
* topology-change-ack- topology change acknowledgment flag is sent in replies to the notification packets
* config- configuration BPDU
* tcn- topology change notification
Footnotes:
* STP matchers are only valid if the destination MAC address is01:80:C2:00:00:00/FF:FF:FF:FF:FF:FF(Bridge Group address), also STP should be enabled.
```
01:80:C2:00:00:00/FF:FF:FF:FF:FF:FF
```
* ARP matchers are only valid ifmac-protocolisarporrarp
```
arp
```
```
rarp
```
* VLAN matchers are only valid for0x8100or0x88a8ethernet protocols
```
0x8100
```
```
0x88a8
```
* IP or IPv6 related matchers are only valid ifmac-protocolis either set toiporipv6
```
ip
```
```
ipv6
```
* 802.3 matchers are only consulted if the actual frame is compliant with IEEE 802.2 and IEEE 802.3 standards. These matchers are ignored for other packets.
## Bridge Packet Filter
This section describes specific bridge filter options.
Sub-menu:/interface bridge filter
```
/interface bridge filter
```
Property | Description
----------------------
action(accept | drop | jump | log | mark-packet | passthrough | return | set-priority; Default:accept) | Action to take if the packet is matched by the rule:accept- accept the packet. No action, i.e., the packet is passed through without undertaking any action, and no more rules are processed in the relevant list/chaindrop- silently drop the packet (without sending the ICMP reject message)jump- jump to the chain specified by the value of the jump-target argumentlog- add a message to the system log containing the following data: in-interface, out-interface, src-mac, dst-mac, eth-proto, protocol, src-ip:port->dst-ip:port and length of the packet. After packet is matched it is passed to the next rule in the list, similar as passthroughmark- mark the packet to use the mark laterpassthrough- ignore this rule and go on to the next one. Acts the same way as a disabled rule, except for the ability to count packetsreturn- return to the previous chain, from where the jump took placeset-priority- set priority specified by the new-priority parameter on the packets sent out through a link that is capable of transporting priority (VLAN or WMM-enabled wireless interface).Read more
* accept- accept the packet. No action, i.e., the packet is passed through without undertaking any action, and no more rules are processed in the relevant list/chain
* drop- silently drop the packet (without sending the ICMP reject message)
* jump- jump to the chain specified by the value of the jump-target argument
* log- add a message to the system log containing the following data: in-interface, out-interface, src-mac, dst-mac, eth-proto, protocol, src-ip:port->dst-ip:port and length of the packet. After packet is matched it is passed to the next rule in the list, similar as passthrough
* mark- mark the packet to use the mark later
* passthrough- ignore this rule and go on to the next one. Acts the same way as a disabled rule, except for the ability to count packets
* return- return to the previous chain, from where the jump took place
* set-priority- set priority specified by the new-priority parameter on the packets sent out through a link that is capable of transporting priority (VLAN or WMM-enabled wireless interface).Read more
## Bridge NAT
This section describes specific bridge NAT options.
Sub-menu:/interface bridge nat
```
/interface bridge nat
```
Property | Description
----------------------
action(accept | drop | jump | mark-packet | redirect | set-priority | arp-reply | dst-nat | log | passthrough | return | src-nat; Default:accept) | Action to take if the packet is matched by the rule:accept- accept the packet. No action, i.e., the packet is passed through without undertaking any action, and no more rules are processed in the relevant list/chainarp-reply- send a reply to an ARP request (any other packets will be ignored by this rule) with the specified MAC address (only valid in dstnat chain)drop- silently drop the packet (without sending the ICMP reject message)dst-nat- change destination MAC address of a packet (only valid in dstnat chain)jump- jump to the chain specified by the value of the jump-target argumentlog- log the packetmark- mark the packet to use the mark laterpassthrough- ignore this rule and go on to the next one. Acts the same way as a disabled rule, except for the ability to count packetsredirect- redirect the packet to the bridge itself (only valid in dstnat chain)return- return to the previous chain, from where the jump took placeset-priority- set priority specified by the new-priority parameter on the packets sent out through a link that is capable of transporting priority (VLAN or WMM-enabled wireless interface).Read moresrc-nat- change source MAC address of a packet (only valid in srcnat chain)
to-arp-reply-mac-address(MAC address; Default: ) | Source MAC address to put in Ethernet frame and ARP payload, whenaction=arp-replyis selected
to-dst-mac-address(MAC address; Default: ) | Destination MAC address to put in Ethernet frames, whenaction=dst-natis selected
to-src-mac-address(MAC address; Default: ) | Source MAC address to put in Ethernet frames, whenaction=src-natis selected
* accept- accept the packet. No action, i.e., the packet is passed through without undertaking any action, and no more rules are processed in the relevant list/chain
* arp-reply- send a reply to an ARP request (any other packets will be ignored by this rule) with the specified MAC address (only valid in dstnat chain)
* drop- silently drop the packet (without sending the ICMP reject message)
* dst-nat- change destination MAC address of a packet (only valid in dstnat chain)
* jump- jump to the chain specified by the value of the jump-target argument
* log- log the packet
* mark- mark the packet to use the mark later
* passthrough- ignore this rule and go on to the next one. Acts the same way as a disabled rule, except for the ability to count packets
* redirect- redirect the packet to the bridge itself (only valid in dstnat chain)
* return- return to the previous chain, from where the jump took place
* set-priority- set priority specified by the new-priority parameter on the packets sent out through a link that is capable of transporting priority (VLAN or WMM-enabled wireless interface).Read more
* src-nat- change source MAC address of a packet (only valid in srcnat chain)
```
action=arp-reply
```
```
action=dst-nat
```
```
action=src-nat
```
# See also
* CRS1xx/2xx series switches
* CRS3xx, CRS5xx series switches, and CCR2116, CCR2216 routers
* Switch chip features
* MTU on RouterBOARD
* Layer2 misconfiguration
* Bridge VLAN Table
* Wireless VLAN Trunk
* VLANs on Wireless