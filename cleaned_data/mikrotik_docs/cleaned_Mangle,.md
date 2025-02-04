# Document Information
Title: Mangle
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/48660587/Mangle,

# Content
# Introduction
Mangle is a kind of 'marker' that marks packets for future processing with special marks. Many other facilities in RouterOS make use of these marks, e.g. queue trees, NAT, routing. They identify a packet based on its mark and process it accordingly. The mangle marks exist only within the router, they are not transmitted across the network.
Additionally, the mangle facility is used to modify some fields in the IP header, like TOS (DSCP) and TTL fields.
Firewall mangle rules consist of five predefined chains that cannot be deleted:
# Configuration example
# Change MSS
It is a known fact that VPN links have a smaller packet size due to encapsulation overhead. A large packet with MSS that exceeds the MSS of the VPN link should be fragmented before sending it via that kind of connection. However, if the packet has aDon't Fragmentflag set, it cannot be fragmented and should be discarded. On links that have broken path MTU discovery (PMTUD), it may lead to a number of problems, including problems with FTP and HTTP data transfer and e-mail services.
In the case of a link with broken PMTUD, a decrease of the MSS of the packets coming through the VPN link resolves the problem. The following example demonstrates how to decrease the MSS value via mangle:
```
/ip firewall mangle add out-interface=pppoe-out protocol=tcp tcp-flags=syn action=change-mss new-mss=1300 chain=forward tcp-mss=1301-65535
```
# Marking Connections
Sometimes it is necessary to perform some actions on the packets belonging to specific connection (for example, to mark packets from/to specific host for queues), but inspecting each packets IP header is quite expensive task. We can use connection marks to optimize the setup a bit.
```
/ip firewall mangle
add chain=forward in-interface=local src-address=192.168.88.123 connection-state=new action=mark-connection new-connection-mark=client_conn
add chain=forward connection-mark=client_conn action=mark-packet new-packet-mark=client_p
```
# Mangle Actions
Table list mangle actions and associated properties.Other actions are listedhere.
Property | Description
----------------------
action(action name; Default:accept) | change-dscp- change the Differentiated Services Code Point (DSCP) field value specified by thenew-dscpparameterchange-mss- change the Maximum Segment Size field value of the packet to a value specified bythe new-mssparameterchange-ttl- change the Time to Live field value of the packet to a value specified by thenew-ttlparameterclear-df- clear 'Do Not Fragment' Flagfasttrack-connection- shows fasttrack counters, useful for statisticsmark-connection- place a mark specified by the new-connection-mark parameter on the entire connection that matches the rulemark-packet- place a mark specified by the new-packet-mark parameter on a packet that matches the rulemark-routing- place a mark specified by the new-routing-mark parameter on a packet. This kind of mark is used for policy routing purposes only. Do not apply any other routing marks besides "main" for the packets processed by FastTrack, since FastTrack can only work in the main routing table.route- forces packets to a specific gateway IP by ignoring normal routing decisions (prerouting chain only)set-priority- set priority specified by the new-priority parameter on the packets sent out through a link that is capable of transporting priority (VLAN or WMM-enabled wireless interface).Read moresniff-pc- send a packet to a remoteRouterOS CALEAserver.sniff-tzsp- send a packet to a remote TZSP compatible system (such as Wireshark). Set remote target withsniff-targetandsniff-target-portparameters (Wireshark recommends port 37008)strip-ipv4-options- strip IPv4 option fields from IP header, the action does not actually remove IPv4 options but rather replaces all option octets with NOP, further matcher withipv4-options=anywill still match the packet.
new-dscp(integer: 0..63; Default: ) | Sets a new DSCP value for a packet
new-mss(integer; Default: ) | Sets a new MSS for a packet.
new-packet-mark(string; Default: ) | Sets a newpacket-markvalue
new-priority(integer | from-dscp | from-dscp-high-3-bits | from-ingress; Default: ) | Sets a new priority for a packet. This can be the VLAN, WMM, DSCP or MPLS EXP priorityRead more. This property can also be used to set an internal priority.
new-routing-mark(string; Default: ) | Sets a newrouting-markvalue (in RouterOS v7 routing mark must be created before as a newRouting table)
new-ttl(decrement | increment | set:integer; Default: ) | Sets a new Time to live value
route-dst(IP, Default:) | Matches packets with a specific gateway
```
change-dscp
```
```
new-dscp
```
```
change-mss
```
```
the new-mss
```
```
change-ttl
```
```
new-ttl
```
```
clear-df
```
```
fasttrack-connection
```
```
mark-connection
```
```
mark-packet
```
```
mark-routing
```
```
route
```
```
set-priority
```
```
sniff-pc
```
```
sniff-tzsp
```
```
sniff-target
```
```
sniff-target-port
```
```
strip-ipv4-options
```
```
ipv4-options=any
```
Sets a new MSS for a packet.
```
packet-mark
```
```
routing-mark
```