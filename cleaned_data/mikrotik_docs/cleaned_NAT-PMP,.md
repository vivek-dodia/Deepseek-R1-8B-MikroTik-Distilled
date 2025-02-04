# Document Information
Title: NAT-PMP
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/220233819/NAT-PMP,

# Content
# Introduction
NAT Port Mapping Protocol (NAT-PMP) is a protocol used for transparent peer-to-peer network connectivity of personal computers and network-enabled intelligent devices or appliances.
Protocol operates by retrieving the external IPv4 address of a NAT gateway, thus allowing a client to make its external IPv4 address and port known to peers who may wish to communicate with it by creating dynamic NAT rules.
NAT-PMP uses UDP port number 5350 - on the client, and 5351 on the server side.
There are two interface types for PMP:internal(the one local clients are connected to) andexternal(the one the Internet is connected to).A router may only have one active external interface with a 'public' IP address on it
For more details on NAT PMP seeRFC 6886
NAT-PMP configuration is accessible from/ip nat-pmpmenu.
```
/ip nat-pmp
```
# Configuration Example
Let's consider that we already have this basic home setup illustrated above.
Before enabling PMP-NAT we need to masquerade outgoing LAN packets.
```
/ip firewall nat
add action=masquerade chain=srcnat out-interface=ether1
```
Now we can enable PMP and add internal, external interfaces:
```
/ip nat-pmp set enable=yes
/ip nat-pmp interfaces> add interface=ether1 type=external disabled=no
/ip nat-pmp interfaces> add interface=ether2 type=internal disabled=no
```
When the client from the internal interface side sends PMP request, dynamic NAT rules are created on the router:
```
[admin@MikroTik] > ip firewall nat print
Flags: X - disabled, I - invalid, D - dynamic
0 chain=srcnat action=masquerade out-interface=ether1
1 D ;;; nat-pmp 192.168.88.10: ApplicationX
chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=55000 protocol=tcp
dst-address=10.0.0.1 in-interface=ether1 dst-port=55000
2 D ;;; nat-pmp 192.168.88.10: ApplicationX
chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=55000 protocol=udp
dst-address=10.0.0.1 in-interface=ether1 dst-port=55000
```
# Properties
# General properties
Available from/ip nat-pmpmenu.
```
/ip nat-pmp
```
Property | Description
----------------------
enabled(yes | no; Default:no) | Enable NAT-PMP service
# NAT PMP Interfaces
Available from/ip nat-pmp interfacesmenu.
```
/ip nat-pmp interfaces
```
Property | Description
----------------------
interface(string; Default: ) | Interface name on which PMP will be running on
type(external | internal; Default:no) | PMP interface type:external- the interface a global IP address is assigned tointernal- router's local interface the clients are connected to
forced-ip(Ip; Default: ) | Allow specifying what public IP to use if the external interface has more than one IP available.
```
external
```
```
internal
```