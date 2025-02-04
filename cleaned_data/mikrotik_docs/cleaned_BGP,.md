# Document Information
Title: BGP
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328220/BGP,

# Content
# Summary
The Border Gateway Protocol (BGP) allows setting up an inter-domain dynamic routing system that automatically updates routing tables of devices running BGP in case of network topology changes.
BGP is an inter-autonomous system routing protocol based on the distance-vector algorithm. It is used to exchange routing information across the Internet and is the only protocol that is designed to deal with a network of the Internet's size and the only protocol that can deal well with having multiple connections to unrelated routing domains.
BGP is designed to allow for sophisticated administrative routing policies to be implemented. It does not exchange information about network topology but rather reachability information. As such, BGP is better suited to inter-AS environments and special cases like informational feeds. If you just need to enable dynamic routing in your network, consider OSPF instead.
Standards and Technologies:
RFC 4364BGP/MPLS IP Virtual Private Networks (VPNs)
# BGP Terminology
# BGP Basics
BGP routers exchange reachability information by means of a transport protocol, which in the case of BGP is TCP (port 179). Upon forming a TCP connection these routers exchangeOPENmessages to negotiate and confirm supported capabilities.
After agreeing on capabilities to use, the session is considered to be established and peers can start to exchange NLRIs viaUPDATEmessages. This information contains an indication of what sequence of full paths (BGP AS numbers) the route should take in order to reach the destination network (NLRI prefix).
The peers initially exchange their full routing tables and after the initial exchange, incremental updates are sent as the routing tables change. Thus, BGP does not require a periodic refresh of the entire BGP routing table.
BGP maintains the routing table version number which must be the same between any two given peers for the duration of the connection.
KEEPALIVEmessages are sent periodically to ensure that the connection is up and running, ifKEEPALIVEmessages are not received within theHold Timeinterval, the connection will be closed.
To respond to errors or special conditions,NOTIFICATIONmessages can be generated and sent to the remote peer, notification message type also indicates whether the connection should be immediately closed.
There can be two types of BGP connections:
A particular AS might have multiple BGP speakers and provide transit service to other AS-es. This implies that BGP speakers must maintain a consistent view of routing within the AS.  A consistent view of the routes exterior to the AS is provided by having all BGP routers within the AS establish direct iBGP connections with each other (full mesh) or by utilizing a Router Reflector setup.
Using a set of administrative policies BGP speakers within the AS come to an agreement as to which entry/exit point to use for a particular destination. This information is communicated to the interior routers of the AS using the interior routing protocol (IGP), for example, OSPF, RIP, or static routing. In certain setups, iBGP can take the IGP protocol role as well.
For certain BGP attributes handling behavior may change depending on what type of connection is set up, for example, the LOCAL-PREF attribute is not advertised to eBGP peers.
RouterOS divides configuration and session monitoring into three menus:
```
/routing/bgp/connection
```
```
/routing/bgp/session
```
```
/routing/bgp/template
```
# Connection Menu
Let's look at a very basic eBGP configuration example assuming, that Router1 IP is 192.168.1.1, AS 65531 and Router2 IP 192.168.1.2, AS 65532:
```
# Router1
/routing/bgp/connection
add name=toR2 remote.address=192.168.1.2 as=65531 local.role=ebgp
```
```
# Router2
/routing/bgp/connection
add name=toR1 remote.address=192.168.1.1 as=65532 local.role=ebgp
```
The BGP connection menu defines BGP outgoing connections as well as acts as a template matcher for incoming BGP connections.
local.roleparameter is used to indicate that this connection will be the eBGP. Also, notice that the connection does not require a remote AS number to be specified, RouterOS can determine a remote AS number dynamically from the first receivedOPENmessage.
```
local.role
```
The parameter equivalent to other vendors and older RouterOS "update-source" is "local.address". In most cases, it can be left unconfigured, and let the router determine the address.
```
local.address
```
When a local address is not specified, BGP will try to guess the local address depending on the current setup:
In addition to connection-specific parameters, template-specific parameters are also directly exposed in this menu, for easier configuration in simple scenarios (when templates are not necessary).
A list of all connection-specific parameters can be seen in the table below:
Property | Description
----------------------
name(string; Default: ) | Name of the BGP connection
connect(yes | no; Default:yes) | Whether to allow the router to initiate the connection.
listen(yes | no; Default: yes) | Whether to listen for incoming connections.
local- a group of parameters associated with the local side of the connection
| .address(IPv4/6; Default: ::) | Local connection address.
| .port(integer [0..65535]; Default:179 ) | Local connection port.
| .role(ebgp | ebgp-customer | ebgp-peer | ebgp-provider | ebgp-rs | ebgp-rs-client | ibgp | ibgp-rr; Default: ) | BGP role, in most common scenarios it should be set to iBGP or eBGP. More information on BGP roles can be foundin the corresponding RFC drafthttps://datatracker.ietf.org/doc/draft-ietf-idr-bgp-open-policy/?include_text=1)
| .ttl(integer [1..255]; Default:) | Time To Live (hop limit) that will be recorded in sent TCP packets.
remote- a group of parameters associated with the remote side of the connection
| .address(IPv4/6; Default: ::) | Remote address used to connect and/or listen to.
.port(integer [0..65535]; Default:179 ) | Local connection port.
.as(integer []; Default: ) | Remote AS number. If not specified BGP will determine remote AS automatically from the OPEN message.
.allowed-as() | List of remote AS numbers that are allowed to connect. Useful for dynamic peer configuration.
.ttl(integer [1..255]; Default:) | Acceptable minimum Time To Live, the hop limit for this TCP connection. For example, if 'ttl=255' then only single-hopneighborswill be able to establish the connection. This property only affects EBGP peers.
tcp-md5-key(string; Default: ) | The key used to authenticate the connection with TCP MD5 signature as described in RFC 2385. If not specified, authentication is not used.
templates(name[,name]; Default: default) | List of the template names, to inherit parameters from. Useful for dynamic BGP peers.
# Session Menu
To see the actual active sessions with selected template parameters and negotiated capabilities refer to the BGP sessions menu:
```
[admin@MikroTik] /routing/bgp/session> print
Flags: E - established
0 E name="toR2"
remote.address=192.168.1.2 .as=65532 .id=192.168.1.1 .refused-cap-opt=no
.capabilities=mp,rr,as4 .afi=ip,ipv6 .messages=43346 .bytes=3635916 .eor=""
local.address=192.168.1.1 .as=65531 .id=192.168.44.2 .capabilities=mp,rr,gr,as4 .messages=2
.bytes=71 .eor=""
output.procid=97 .keep-sent-attributes=no
.last-notification=ffffffffffffffffffffffffffffffff0015030601
input.procid=97 .limit-process-routes=500000 ebgp limit-exceeded
hold-time=3m keepalive-time=1m uptime=4s70ms
```
This menu shows read-only cached BGP session information. It will show the current status of the session, flags, last received notification, and negotiated session parameters.
Even if the BGP session is not active anymore, the cache can still be stored for some time. Routes received from a particular session are removed only if the cache expires, this allows mitigating extensive routing table recalculations if the BGP session is flapping.
Also, in this menu is located a session-specific set of commands.
Command | Description
---------------------
clear | Clear the session flags. For example, to be able to re-establish a session after the prefix limit is reached "limit-exceeded" flag must be cleared. It can be done by specifying "flag" parameter, which is able to take the following values:input-last-notificationlimit-exceededoutput-last-notificationrefused-cap-optstopped
dump-saved-advertisements | Dump saved advertisements from specified BGP session in the *.pcap file. The filename to store data is set by "save-to" parameter.
refresh | Send route refresh to a specified BGP session. Is used to trigger re-sending all the routes from the remote peer. "address-family" parameters allow specifying for which address family to send route refresh.
resend | Resend prefixes to a specified BGP session. The command takes two parameters:"address-family" - parameters allow specifying for which address family to resend prefixes."save-to" - the name of the pcap file where to dump resent messages, can be used for debugging purposes.
reset | Reset specified BGP session.
stop | Stop specified BGP session.
Clear the session flags. For example, to be able to re-establish a session after the prefix limit is reached "limit-exceeded" flag must be cleared. It can be done by specifying "flag" parameter, which is able to take the following values:
```
flag
```
```
save-to
```
```
address-family
```
Resend prefixes to a specified BGP session. The command takes two parameters:
```
address-family
```
```
save-to
```
# Template Menu
The template contains all BGP protocol-related configuration options. It can be used as a template for dynamic peers and to apply a similar configuration to a group of peers. Note that this is not the same as peer groups on Cisco devices, where the group is more than just a common configuration.
List of available template parameters:
Property | Description
----------------------
add-path-out(all|none; Default: ) |
address-families(ip | ipv6 | l2vpn | l2vpn-cisco | vpnv4; Default:ip) | List of address families about which this peer will exchange routing information. The remote peer must support (they usually do) BGP capabilities optional parameter to negotiate any other families than IP.
as(integer [0..4294967295]; Default: ) | 32-bit BGP autonomous system number. Value can be entered in AS-Plain and AS-Dot formats. The parameter is also used to set up the BGP confederation, in the following format:confederation_as/as. For example, if your AS is 34 and your confederation AS is 43, then as configuration should beas=43/34.
as-override(yes | no; Default:no) | If set, then all instances of the remote peer's AS number in the BGP AS-PATH attribute are replaced with the local AS number before sending a route update to that peer. Happens before routing filters and prepending.
cisco-vpls-nlri-len-fmt(auto-bits | auto-bytes | bits | bytes; Default: ) | VPLS NLRI length format type. Used for compatibility with Cisco VPLS. [[Read more>>]].
cluster-id(IP address; Default: ) | In case this instance is a route reflector: the cluster ID of the router reflector cluster to this instance belongs. This attribute helps to recognize routing updates that come from another route reflector in this cluster and avoid routing information looping. Note that normally there is only one route reflector in a cluster; in this case, 'cluster-id' does not need to be configured and BGP router ID is used instead
disabled(yes | no; Default:no) | Whether the template is disabled.
hold-time(time[3s..1h] | infinity; Default:3m) | Specifies the BGP Hold Time value to use when negotiating with peers.According to the BGP specification, if the router does not receive successiveKEEPALIVEand/orUPDATEand/orNOTIFICATIONmessages within the period specified in the Hold Time field of theOPENmessage, then the BGP connection to the peer will be closed.The minimal hold-time value of both peers will be used (note that the special value 0 or 'infinity' is lower than any other value)infinity- never expire the connection and never send keepalive messages.
input- a group of parameters associated with BGP input
| .accept-comunities(string; Default: ) | A quick way to filter incoming updates with specific communities. Itallows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in/routing routetable as "not active, filtered". Changes to be applied required session refresh.
.accept-ext-communities(string; Default: ) | A quick way to filter incoming updates with specific extended communities. Itallows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in/routing routetable as "not active, filtered". Changes to be applied required session refresh.
.accept-large-comunities(string; Default: ) | A quick way to filter incoming updates with specific large communities. Itallows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in/routing routetable as "not active, filtered". Changes to be applied required session refresh.
.accept-nlri(string; Default: ) | Name of the ipv4/6 address-list. A quick way to filter incoming updates with specific NLRIs. Itallows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in/routing routetable as "not active, filtered". Changes to be applied required session restart.
.accept-unknown(string; Default: ) | A quick way to filter incoming updates with specific "unknown" attributes. Itallows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in/routing routetable as "not active, filtered". Changes to be applied required session refresh.
.affinity(afi  | alone | instance | main | remote-as | vrf; Default: alone ) | Configure input multi-core processing. Read more inRouting Protocol Multi-core Supportarticle.alone- input and output of each session are processed in its own process, most likely the best option when there are a lot of cores and a lot of peersafi, instance, vrf, remote-as- try to run input/output of new session in process with similar parametersmain- run input/output in the main process (could potentially increase performance on single-core even possibly on multi-core devices with a small amount of cores)input- run output in the same process as input (can be set only for output affinity)
.allow-as(integer [0..10]; Default: ) | Indicates how many times to allow your own AS number in AS-PATH, before discarding a prefix.
.filter(name; Default: ) | Name of the routing filter chain to be used on input prefixes. This happens after NLRIs are processed. If the chain is not specified, then BGP by default accepts everything.
.ignore-as-path-len(yes | no; Default:no) | Whether to ignoretheAS_PATHattribute in the BGP route selection algorithm
| .limit-nlri-diversity(integer; Default: ) |
| .limit-process-routes-ipv4(integer; Default: ) | Try to limit the amount of received IPv4 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer.BGP session "clear"command must be used to reset the flag if the limit is reached.
| .limit-process-routes-ipv6(integer; Default: ) | Try to limit the amount of received IPv6 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. BGP session "clear" command must be used to reset the flag if the limit is reached.
keepalive-time(time [1s..30m]; Default: ) | The interval between keepalive messages, if not set by default keepalive is 1/3 of thehold-time.
multihop(yes | no; Default:no) | Specifies whether the remote peer is more than one hop away.This option affects outgoing next-hop selection as described in RFC 4271 (for EBGP only, excluding EBGP peers local to the confederation).It also affects:whether to accept connections from peers that are not in the same network (the remote address of the connection is used for this check);whether to accept incoming routes with NEXT_HOP attribute that is not in the same network as the address used to establish the connection;the target-scope of the routes installed from this peer; routes from multi-hop or IBGP peers resolve their next-hops through IGP routes by default.
name(string; Default: ) | Name of the BGP template
nexthop-choice(default | force-self | propagate; Default:default) | Affects the outgoingNEXT_HOPattribute selection. Note that next-hops set in filters always take precedence. Also note that the next-hop is not changed on route reflection, except when it's set in the filter.default- select the next-hop as described in RFC 4271force-self- always use a local address of the interface that is used to connect to the peer as the next-hop;propagate- try to propagate further the next-hop received; i.e. if the route has BGPNEXT_HOPattribute, then use it as the next-hop, otherwise, fall back to the default case
output- a group of parameters associated with BGP output
| .affinity(afi  | alone | instance | main | remote-as | vrf; Default: ) | Configure output multicore processing. Read more inRouting Protocol Multi-core Supportarticle.alone- input and output of each session is processed in its own process, the most likely best option when there are a lot of cores and a lot of peersafi, instance, vrf, remote-as- try to run input/output of new session in process with similar parametersmain- run input/output in the main process (could potentially increase performance on single-core even possibly on multicore devices with small amount of cores)input- run output in the same process as input (can be set only for output affinity)
.default-originate(always | if-installed | never; Default:never) | Specifies default route (0.0.0.0/0) distribution method.
default-prepend(integer [0..255]; Default: ) |
.filter-chain(name; Default: ) | Name of the routing filter chain to be used on the output prefixes. If the chain is not specified, then BGP by default accepts everything.
.filter-select(name; Default: ) | Name of the routing select chain to be used for prefix selection. If not specified, then default selection is used.
.keep-sent-attributes(yes | no; Default: no) | Store in memory sent prefix attributes, required for "dump-saved-advertisements" command to work. By default, sent-out prefixes are not stored to preserve the router's memory. An option should be enabled only for debugging purposes when necessary to see currently advertised prefixes.
.network(name; Default: ) | Name of the address list used to send local networks. The network is sent only if a matching IGP route exists in the routing table.
.no-client-to-client-reflection(yes | no; Default: ) | Disable client-to-client route reflection in Route Reflector setups.
.no-early-cut(yes | no; Default: ) | The early cut is the mechanism, to guess (based on default RFC behavior) what would happen with the sent NPLRI when received by the remote peer. If the algorithm determines that the NLRI is going to be dropped, a peer will not even try to send it. However such behavior may not be desired in specific scenarios, then then this option should be used to disable the early cut feature.
redistribute(bgp, connected, bgp-mpls-vpn , dhcp, fantasy, modem, ospf, rip, static, vpn; Default:) | Enable redistribution of specified route types.
remove-private-as(yes | no; Default:no | If set, then the BGPAS-PATHattribute is removed before sending out route updates if the attribute contains only private AS numbers.The removal process happens before routing filters are applied and before the local, ASnumber is prepended to the AS path.
router-id(IP | name; Default: main ) | BGP Router ID to be used. Use the ID from the/routing/router-idconfiguration by specifying the reference name, or set the ID directly by specifying IP.Equal router-ids are also used to group peers into one instance.
routing-table(string; Default: ) | Name of the routing table, to install routes in.
save-to(string; Default: ) | Filename to be used to save BGP protocol-specific packet content (Exported PDU) into pcap file. This method allows much simpler peer-specific packet capturing for debugging purposes. Pcap files in this format can also be loaded to create virtual BGP peers to recreate conditions that happened at the time when packet capture was running.
templates(name[,name]; Default: ) | List of template names from which to inherit parameters. Useful feature, to easily configure groups with overlapping configuration options.
use-bfd(yes | no; Default:no) | Whether to use theBFDprotocol for faster connection state detection.
vrf(name; Default: main ) | Name of the VRF BGP connections operates on. By default always use the "main" routing table.
```
confederation_as/as
```
```
as=43/34
```
According to the BGP specification, if the router does not receive successiveKEEPALIVEand/orUPDATEand/orNOTIFICATIONmessages within the period specified in the Hold Time field of theOPENmessage, then the BGP connection to the peer will be closed.
The minimal hold-time value of both peers will be used (note that the special value 0 or 'infinity' is lower than any other value)
Configure input multi-core processing. Read more inRouting Protocol Multi-core Supportarticle.
```
hold-time
```
This option affects outgoing next-hop selection as described in RFC 4271 (for EBGP only, excluding EBGP peers local to the confederation).
It also affects:
Configure output multicore processing. Read more inRouting Protocol Multi-core Supportarticle.
```
dump-saved-advertisements
```
The removal process happens before routing filters are applied and before the local, ASnumber is prepended to the AS path.
BGP Router ID to be used. Use the ID from the/routing/router-idconfiguration by specifying the reference name, or set the ID directly by specifying IP.
Equal router-ids are also used to group peers into one instance.
# Best-Path Selection
BGP routers can receive multiple copies of the global routing table from multiple providers.
There should be some way to compare those multiple BGP routing tables and select the best route to the destination, the solution is the BGP Best Path Selection Algorithm.
The route is evaluated by the algorithm only if it is valid. In general, the route is considered valid if:
For more information readnexthop selection and validation.
The best path algorithm also compares routes received only by asingle BGP instance. Routes installed by different BGP instances are compared by the general algorithm, i.e. route distances are compared and the route with a lower distance is preferred.
If all the criteria are met, then the following actions take place:
```
input.ignore-as-path-len
```
Interior Gateway Protocol (IGP) is lower than Exterior Gateway Protocol (EGP), and EGP is lower than INCOMPLETE
The router compares the MED attribute only for paths that have the same neighboring (leftmost) AS unlessinput.always-compare-medis enabled.Paths without explicit MED value are treated with MED of 0.
```
input.always-compare-med
```
# Routing Filter Notes
On BGP output routing filters are executed before BGP itself is modifying attributes, for example, ifnexthop-choiceis set toforce-self, then the gateway set in the routing filters will be overridden.
```
nexthop-choice
```
```
force-self
```
On BGP input routing filters are applied to the received attributes, which means that, for example, setting the gateway will work no matter whatnexhop-choicevalue is set.
```
nexhop-choice
```
# Running More than One Instance
As we already know for best path selection to work properly, BGP routes must be received from the same instance. But in certain scenarios it is necessary to run multiple BGP instances with their own separate tables.BGP determines whether sessions belongs to the same instance by comparing configured local router IDs.For example config below will run each peer in its own BGP instance
```
/routing/bgp/connection
add name=inst1_peer remote.address=192.168.1.1 as=1234 local.role=ebgp router-id=1.1.1.1
add name=inst2_peer remote.address=192.168.1.2 as=5678 local.role=ebgp router-id=2.2.2.2
```
Whenrouter-idis not specified BGP will pick the "default" ID from/routing id.
```
router-id
```
```
/routing id
```
# VPLS
```
VPLS
```
Sub Menu:/routing/bgp/vpls
```
Sub Menu:
```
```
/routing/bgp/vpls
```
This menu lists all the configured BGP-based VPLS instances. These instances allow the router to advertise VPLS BGP NLRI and indicate that the router belongs to a specific customer VPLS network.
MP-BGP-based autodiscovery and signaling (RFC 4761).
Cisco VPLS BGP-based auto-discovery (draft-ietf-l2vpn-signaling-08).
Support for multiple import/export route target extended communities for BGP-based VPLS (both, RFC 4761 and draft-ietf-l2vpn-signaling-08).
Property | Description
----------------------
bridge(name) | The name of the bridge where dynamically created VPLS interfaces should be added as ports.
bridge-cost(integer [0..4294967295]) |
bridge-horizon(none | integer [0..4294967295]) | If set tononebridge horizon will not be used.
bridge-pvid(integer 1..4094) | Used to assign port VLAN ID (pvid) for dynamically bridged interface.
cisco-id() | Unique identifier. A parameter must be set for cisco-style VPLS signaling. In most cases this should not be used, any modern software supports RFC 4761 style signaling (see site-id parameter). Parameter is a merge of l2-router-id and RD, for example: 10.155.155.1&6550:123
comment(string) | Short description of the item.
disabled(yes | no) | Defines whether an item is ignored or used.
export-route-target(list of RTs) | The setting is used to tag BGP NLRI with one or more route targets which on the remote side is used byimport-route-targets.
import-route-targets(list of RTs) | The setting is used to determine if BGP NLRI is related to a particular VPLS, by comparing route targets received from BGP NLRI.
local-pref(integer[0..4294967295]) |
name(string; Default: ) |
pw-control-word(default | disabled | enabled) | Enables/disables Control Word usage.Read more in theVPLS Control Wordarticle.
pw-l2mtu(integer[32..65535]) | Advertised pseudowire MTU value.
pw-type(raw-ethernet | tagged-ethernet | vpls) | The parameter is available starting from v5.16. It allows choosing advertised encapsulation in NLRI used only for comparison. It does not affect the functionality of the tunnel.See pw-type usage example >>
rd(string) | Specifies the value that gets attached to VPLS NLRI so that receiving routers can distinguish advertisements that may otherwise look the same. This implies that a unique route-distinguisher for every VPLS must be used. It is not necessary to use the same route distinguisher for some VPLS on all routers forming that VPLS as distinguisher is not used for determining if some BGP NLRI is related to a particular VPLS (Route Target attribute is used for this), but it is mandatory to have different distinguishers for different VPLSes. Accepts 3 types of formats.Read more>>
site-id(integer [0..65535]) | Unique site identifier. Each site must have a unique site-id. A parameter must be set for RFC 4761 style VPLS signaling.
vrf(name) | Name of the VRF table.
```
import-route-targets
```
```
See pw-type usage example >>
```
# VPN
```
VPN
```
Sub Menu:/routing/bgp/vpn
```
Sub Menu:
```
```
/routing/bgp/vpn
```
# Route Distinguisher
Route Distinguisher is a 64-bit integer, which is divided into three parts:
Currently, there are three format types defined.
2bytes | 2bytes | 2bytes | 2bytes | Type1 | Type2 | Type3
---------------------------------------------------------
ASN | 4byte value
4-byte IP | value
4-byte ASN | value
# Properties
disabled(yes | no) |
export- a group of parameters associated with the vpnv4 export
| .filter-chain(name) | The name of the routing filter chain that is used to filter prefixes before exporting.
.filter-select(name) | The name of the select filter chain that is used to select prefixes to be exported exporting.
.redistribute(bgp | connected | dhcp | fantasy | modem | ospf | rip | static | vpn) | Enable redistribution of specified route types from VRF to VPNv4.
.route-targets(rt[,rt]) | List of route targets added when exporting VPNv4 routes. The accepted RT format is similar to the one for Route Distinguishers.
import- a group of parameters associated with the vpnv4 import
| .filter-chain(name) | The name of the routing filter chain that is used to filter prefixes during import.
.route-targets(rt[,rt]) | List of route targets that will be used to import VPNv4 routes. The accepted RT format is similar to the one for Route Distinguishers.
.router-id(name | ip) | The router ID of the BGP instance that will be used for the BGP best path selection algorithm.
label-allocation-policy(per-prefix | per-vrf) |
name |
route-distinguisher(rd) | Helps to distinguish between overlapping routes from multiple VRFs. Should be unique per VRF. Accepts 3 types of formats.Read more>>
vrf(name) | Name of the VRF table that this VPN instance will use.