---
title: IP Addressing
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/328247/IP+Addressing,
crawled_date: 2025-02-02T21:09:05.141082
section: mikrotik_docs
type: documentation
---

* 1Overview
* 2IPv4 Addressing2.1Private Address Range2.2Other Reserved Address Ranges2.3Adding IP Address
* 3IPv6 Addressing3.1Address Types3.1.1Unicast Addresses3.1.1.1Link-local Address3.1.1.2Unique Local Address3.1.1.3Special Purpose Address3.1.1.4Compatibility Address3.1.2Multicast Address3.1.3Anycast Address3.2Interface Identifier3.2.1EUI-643.3Configuring IPv6 Address3.4SLAAC IPv6 Address3.5Properties3.6Read-only properties3.7Frequently asked questions
* 2.1Private Address Range
* 2.2Other Reserved Address Ranges
* 2.3Adding IP Address
* 3.1Address Types3.1.1Unicast Addresses3.1.1.1Link-local Address3.1.1.2Unique Local Address3.1.1.3Special Purpose Address3.1.1.4Compatibility Address3.1.2Multicast Address3.1.3Anycast Address
* 3.2Interface Identifier3.2.1EUI-64
* 3.3Configuring IPv6 Address
* 3.4SLAAC IPv6 Address
* 3.5Properties
* 3.6Read-only properties
* 3.7Frequently asked questions
* 3.1.1Unicast Addresses3.1.1.1Link-local Address3.1.1.2Unique Local Address3.1.1.3Special Purpose Address3.1.1.4Compatibility Address
* 3.1.2Multicast Address
* 3.1.3Anycast Address
* 3.1.1.1Link-local Address
* 3.1.1.2Unique Local Address
* 3.1.1.3Special Purpose Address
* 3.1.1.4Compatibility Address
* 3.2.1EUI-64
# Overview
IP addresses serve for general host identification purposes in IP networks (RFC 791). A typical (IPv4) address consists of four octets. For proper addressing the router also needs the network mask value, id est which bits of the complete IP address refer to the address of the host, and which - to the address of the network. The network address value is calculated by binary AND operation from a network mask and IP address values. It's also possible to specify an IP address followed by a slash "/" and the number of bits that form the network address.
In most cases, it is enough to specify the address, the netmask, and the interface arguments. The network prefix and the broadcast address are calculated automatically.
It is possible to add multiple IP addresses to an interface or to leave the interface without any addresses assigned to it. In the case of bridging or PPPoE connection, the physical interface may not have any address assigned, yet be perfectly usable. Configuring an IP address to a physical interface included in a bridge would mean actually setting it on the bridge interface itself.
You can use/ip address print detailto see which interface the address belongs to.
# IPv4 Addressing
IPv4 uses 4-byte addresses which are segmented in four 8-bit fields called octets. Each octet is converted to a decimal format and separated by a dot. For example:
```
11000000 10101000 00000011 00011000 => 192.168.3.24
```
The IPv4 network consists of three addresses:
* network address- a standard way to refer to an IPv4 address assigned to a network. For example, we could refer to the network 192.168.1.0 or 172.16.0.0 as a “Network Address.”
* broadcast address- a special address for each network that allows communication to all the hosts in that network. The broadcast address uses the highest address in the network range. for example, broadcast address if 192.168.1.0/24 network will be 192.168.1.255
* host address- any other address that is not a network address and broadcast address can be used as a host address. For example, 192.168.1.2 - 254 host addresses can be used from 192.168.1.0/24 address range
There are several types of IP addressing
* unicast- normally refers to a single sender or a single receiver, and can be used for both sending and receiving. Usually, a unicast address is associated with a single device or host, but it is not a one-to-one correspondence.
* broadcast- address to send data to all possible destinations ("all-hosts broadcast"), which permits the sender to send the data only once, and all receivers receive a copy of it. In the IPv4 protocol, the address255.255.255.255is used for local broadcast. In addition, a directed (limited) broadcast can be made by combining the network prefix with a host suffix composed entirely of binary 1s. For example, the destination address used for directed broadcast to devices on the 192.0.2.0/24 network is 192.0.2.255
* multicast- address associated with a group of interested receivers. In IPv4, addresses 224.0.0.0 through 239.255.255.255 are designated as multicast addresses. The sender sends a single datagram from its unicast address to the multicast group address and the intermediary routers take care of making copies and sending them to all receivers that have joined the corresponding multicast group.
## Private Address Range
The following IP address ranges are reserved (RFC 6890) for private addressing. These addresses are not routed in the global routing table and should be translated to global addresses with network address translation (NAT):
* 10.0.0.0/8 - start: 10.0.0.0; end: 10.255.255.255
* 172.16.0.0/12 - start: 172.16.0.0; end:172.31.255.255
* 192.168.0.0/16 - start: 192.168.0.0; end: 192.168.255.255
## Other Reserved Address Ranges
* 198.18.0.0/15 - benchmarking
* 192.88.99.0/24 - 6to4 relay anycast address range
* 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24 - documentation
* 169.254.0.0/16 - auto-configuration address range
## Adding IP Address
Consider a setup where two routers are directly connected with the cable and we do not want to waste address space:
R1 configuration:
```
/ip address
add address=10.1.1.1/32 interface=ether1 network=172.16.1.1
```
R2 configuration:
```
/ip address
add address=172.16.1.1/32 interface=ether1 network=10.1.1.1
```
# IPv6 Addressing
Internet Protocol version 6 (IPv6) is the newer version of the Internet Protocol (IP). It was initially expected to replace IPv4 in a short enough time, but for now, it seems that these two versions will coexist on the Internet in foreseeable future. Nevertheless, IPv6 becomes more important, as the date of the unallocated IPv4 address pool's exhaustion approaches.
The two main benefits of IPv6 over IPv4 are:
* much larger address space;
* support of stateless and stateful address auto-configuration;
* built-in security;
* new header format (faster forwarding).
IPv6 uses 16 bytes addresses compared to 4-byte addresses in IPv4. IPv6 address syntax and types are described inRFC 4291.
There are multiple IPv6 address types, that can be recognized by their prefix. RouterOS distinguishes the following:
* multicast (with prefix ff00::/8)
* link-local (with prefix fe80::/10)
* unique local addresses (with prefix fc00::/7)
* loopback (the address::1/128)
* unspecified (the address::/128)
* other (all other addresses, including the obsoleted site-local addresses, andRFC 4193unique local addresses; they all are treated as global unicast).
One difference between IPv6 and IPv4 addresses is that IPv6 automatically generates alink-localIPv6 address for each active interface that has IPv6 support.
IPv6 addresses are represented a little bit differently than IPv4 addresses. For IPv6, the 128-bit address is divided into eight 16-bit blocks, and each 16-bit block is converted to a 4-digit hexadecimal number and separated by colons. The resulting representation is called colon-hexadecimal.
In the example below IPv6 address in binary format is converted to a colon-hexadecimal representation
```
0010000000000001 0000010001110000 0001111100001001 0000000100110001
0000000000000000 0000000000000000 0000000000000000 0000000000001001
```
```
2001:0470:1f09:0131:0000:0000:0000:0009
```
The IPv6 address can be further simplified by removing leading zeros in each block:
```
2001:470:1f09:131:0:0:0:9
```
As you can see IPv6 addresses can have long sequences of zeros. This contiguous sequence can be compressed to::
```
2001:470:1f09:131::9
```
IPv6 prefix is written inaddress/prefix-lengthformat. Compared to IPv4 decimal representation of a network mask cannot be used. Prefix examples:
```
2001:470:1f09:131::/64
2001:db8:1234::/48
2607:f580::/32
2000::/3
```
## Address Types
Several IPv6 address types exist:
* Unicast
* Anycast
* Multicast
As you can see there are no Broadcast addresses in the IPv6 network, compared to the IPv4 broadcast functionality was completely replaced with multicast.
### Unicast Addresses
Packets addressed to a unicast address are delivered only to a single interface. To this group belong:
* globally unique addresses and can be used to connect to addresses with global scope anywhere;
* link-local addresses;
* unique local addresses (ULA RFC4193)
* site-local addresses (FEC0::/48) - deprecated;
* special-purpose addresses;
* compatibility addresses;
A global unicast address can be automatically assigned to the node byStateless Address auto-configuration.
#### Link-local Address
A link-local address is required on every IPv6-enabled interface, applications may rely on the existence of a link-local address even when there is no IPv6 routing, that is why the link-local address is generated automatically for every active interface using its interface identifier (calculated EUI-64 from MAC address if present). The address prefix is alwaysFE80::/64and IPv6 router never forwards link-local traffic beyond the link.
These addresses are comparable to the auto-configuration addresses 169.254.0.0/16 of IPv4.
A link-local address is also required for IPv6 Neighbor Discovery processes.
#### Unique Local Address
Unique Local Address (ULA) is reserved for local use in the home and enterprise environments not routed in public address space and is equivalent to IPv4 private address ranges.
The reserved address range isfc00::/7
#### Special Purpose Address
Address | Description
---------------------
Unspecified address (::/128) | Never assigned to an interface or used as a destination address, used only to indicate the absence of an address. Equivalent to IPv4 0.0.0.0 address.
loopback address (::1/128) | Used to identify a loopback interface, enabling a node to send packets to itself. It is equivalent to the IPv4 loopback address of 127.0.0.1.
2002::/16 | This prefix is used for 6to4 addressing. Here, an address from the IPv4 network 192.88.99.0/24 is also used.
2001:db8::/32 | Address range reserved for documentation. These should never be seen as the source or destination.
2001:0010::/28 | Orchid fixed term experiment. Should not be seen as a source or destination
2001:0002::/48 | Used for benchmarking, should not be seen as source or destination
2001:0000::/32 | Teredo
#### Compatibility Address
Address | Description
---------------------
IPv4 compatible address | used by dual-stack nodes that are communicating with IPv6 over an IPv4 infrastructure. When the IPv4-compatible address is used as an IPv6 destination, IPv6 traffic is automatically encapsulated with an IPv4 header and sent to the destination by using the IPv4 infrastructure. The address is written in the following format::w.x.y.z, where w.x.y.z is the dotted decimal representation of a public IPv4 address.
IPv4 mapped address | used to represent an IPv4-only node to an IPv6 node. It is used only for internal representation. The IPv4-mapped address is never used as a source or destination address for an IPv6 packet. The IPv6 protocol does not support the use of IPv4-mapped addresses. The address is written in the following format:::ffff:w.x.y.z, wherew.x.y.zis the dotted-decimal representation of a public IPv4 address.
```
::w.x.y.z
```
```
::ffff:w.x.y.z
```
```
w.x.y.z
```
### Multicast Address
The most important multicast aspects are:
* traffic is sent to a single address but is processed by multiple hosts;
* group membership is dynamic, allowing hosts to join and leave the group at any time;
* in IPv6, Multicast Listener Discovery (MLD) messages are used to determine group membership on a network segment, also known as a link or subnet;
* a host can send traffic to the group's address without belonging to the corresponding group.
A single IPv6 multicast address identifies each multicast group. Each group's reserved IPv6 address is shared by all host members of the group who listen and receive any IPv6 messages sent to the group's address.
The multicast address consists of the following parts:
* The first 8 bits in the multicast address are always 1111 1111 (which is FF in hexadecimal format).
* The flag uses the 9th to 12th bit and shows if this multicast address is predefined (well-known) or not. If it is well-known, all bits are 0s.
* Scope ID indicates to which scope multicast address belongs, for example, Scope ID=2 is link-local scope.
* The group ID is used to specify a multicast group. There are predefined group IDs, such as Group ID=1 - all nodes. Therefore, if the multicast address is ff02::1, that means Scope ID=2 and Group ID=1, indicating all nodes in link-local scope. This is analogous to broadcast on IPv4.
Here is the table of reserved IPV6 addresses for multicast:
Address | Description
---------------------
FF02::1 | The all-nodes address is used to reach all nodes on the same link.
FF02::2 | The all-routers address is used to reach all routers on the same link.
FF02::5 | The all-Open Shortest Path First (OSPF) router address is used to reach all OSPF routers on the same link.
FF02::6 | The all-OSPF-designated router's address is used to reach all OSPF-designated routers on the same link.
FF02::1:FFXX:XXXX | The solicited-node address is used in the address resolution process to resolve the IPv6 address of a link-local node to its link-layer address. The last 24 bits (XX:XXXX) of the solicited-node address are the last 24 bits of an IPv6 unicast address.
The following table is a partial list of IPv6 multicast addresses that are reserved for IPv6 multicasting and registered with the Internet Assigned Numbers Authority (IANA). For a complete list of assigned addresses readIANA document.
Multicast addresses can be used to discover nodes in a network. For example, discover all nodes
```
mrz@bumba:/media/aaa/ver$ ping6 ff02::1%eth0
PING ff02::1%eth0(ff02::1) 56 data bytes
64 bytes from fe80::21a:4dff:fe5d:8e56: icmp_seq=1 ttl=64 time=0.037 ms
64 bytes from fe80::20c:42ff:fe0d:2c38: icmp_seq=1 ttl=64 time=4.03 ms (DUP!)
64 bytes from fe80::20c:42ff:fe28:7945: icmp_seq=1 ttl=64 time=5.59 ms (DUP!)
64 bytes from fe80::20c:42ff:fe49:fce5: icmp_seq=1 ttl=64 time=5.60 ms (DUP!)
64 bytes from fe80::20c:42ff:fe21:f1ec: icmp_seq=1 ttl=64 time=5.88 ms (DUP!)
64 bytes from fe80::20c:42ff:fe72:a1b0: icmp_seq=1 ttl=64 time=6.70 ms (DUP!)
```
discover all routers
```
mrz@bumba:/media/aaa/ver$ ping6 ff02::2%eth0
PING ff02::2%eth0(ff02::2) 56 data bytes
64 bytes from fe80::20c:42ff:fe28:7945: icmp_seq=1 ttl=64 time=0.672 ms
64 bytes from fe80::20c:42ff:fe0d:2c38: icmp_seq=1 ttl=64 time=1.44 ms (DUP!)
```
### Anycast Address
An anycast address is a new type of address incorporated in IPv6.
Anycasting is a new networking paradigm supporting service-oriented Addresses where an identical address can be assigned to multiple nodes providing a specific service. An anycast packet (i.e., one with an anycast destination address) is delivered to one of these nodes with the same anycast address.
An anycast address is not assigned a specific address range. It is assigned from the unicast address range.
## Interface Identifier
The last 64 bits of an IPv6 address are the interface identifier that is unique to the 64-bit prefix of the IPv6 address. There are several ways how to determine interface identifier:
* EUI-64;
* randomly generated to provide a level of anonymity;
* manually configured.
### EUI-64
Traditional interface identifiers for network adapters are 48-bit MAC addresses. This address consists of a 24-bit manufacturer ID and a 24-bit board ID.
IEEE EUI-64 is a new standard for network interface addresses. The company ID is still 24 bits in length, but the extension ID is 40 bits, creating a much larger address space for network adapters.
To create a EUI-64 address from the interface MAC address:
* 0xFFFE is inserted into the MAC address between the manufacturer ID and the board ID.
* The seventh bit of the first byte is reversed.
Let's make an example with the following MAC address 00:0C:42:28:79:45.
The image above illustrates the conversion process. When the result is converted to colon-hexadecimal notation, we get the interface identifier20C:42FF:FE28:7945. As a result, the corresponding link-local address is
```
20C:42FF:FE28:7945
```
```
FE80::20C:42FF:FE28:7945/64
```
In RouterOS, if the EUI-64 parameter of an address is configured, the last 64 bits of that address will be automatically generated and updated using interface identifier. The last bits must be configured to be zero for this case. Example:
```
[admin@MikroTik] > ipv6 address add address=fc00:3::/64 interface=ether3 eui-64=yes
[admin@MikroTik] > ipv6 address print
Flags: X - disabled, I - invalid, D - dynamic, G - global, L - link-local
#    ADDRESS                                     INTERFACE                  ADVERTISE
...
5  G fc00:3::20c:42ff:fe1d:3d4/64                ether3                     yes
[admin@MikroTik] > interface ethernet set ether3 mac-address=10:00:00:00:00:01
[admin@MikroTik] > ipv6 address print
Flags: X - disabled, I - invalid, D - dynamic, G - global, L - link-local
#    ADDRESS                                     INTERFACE                  ADVERTISE
...
5  G fc00:3::1200:ff:fe00:1/64                   ether3                     yes
```
## Configuring IPv6 Address
This example shows how to set up simple addressing with global IPv6 addresses between two routers.
R1 configuration:
```
/ipv6 address
add address=2001:DB8::1/64 interface=ether1 advertise=no
```
R2 configuration:
```
/ipv6 address
add address=2001:DB8::2/64 interface=ether1 advertise=no
```
Check the address list:
```
[admin@R1] /ipv6 address> print
Flags: X - disabled, I - invalid, D - dynamic, G - global, L - link-local
#    ADDRESS                                     FROM-POOL INTERFACE     ADVERTISE
0  G 2001:db8::1/64                                        ether1        no
3 DL fe80::219:d1ff:fe39:3535/64                           ether1        no
```
Notice that our added address has a G flag indicating that this address can be globally routed. We also have a link-local address on the interface which is created automatically for every IPv6-capable interface.
Test connectivity:
```
[admin@R1] /ipv6 address> /ping 2001:DB8::2
HOST                                     SIZE TTL TIME  STATUS
2001:db8::2                 56  64 12ms  echo reply
2001:db8::2                 56  64 0ms   echo reply
    sent=2 received=2 packet-loss=0% min-rtt=0ms avg-rtt=6ms max-rtt=12ms
```
## SLAAC IPv6 Address
If under IPv6/Settings menu "accept-router-advertisements" option is enabled and the router receives a Router Advertisement packet, then the SLAAC IPv6 address will be automatically assigned to the interface on which the advertisements were received. This address will have DG flags meaning that the address is dynamic and global. Such addresses will show valid and lifetime parameters.
```
[admin@R1] /ipv6/address/print detail where dynamic && global 
Flags: X - disabled, I - invalid, D - dynamic; G - global, L - link-local 
 0 DG address=2001:db8::::ba69:f4ff:fe84:545/64 from-pool="" interface=ether1 
      actual-interface=test_fp eui-64=no advertise=no no-dad=no valid=4w2d 
      preferred=1w
```
If SLAAC addresses are accepted, then also dynamic route toward the Internet will be generated. It will also contain a few limitations if specified on the advertisement packet. For example, hop-limit and MTU. If multiple addresses are received on the same interface, then the lowest of the MTU values per interface will be used.
```
[admin@R1] /routing/route/print detail where slaac 
Flags: X - disabled, F - filtered, U - unreachable, A - active; 
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, a - ldp-address, l - ldp-mapping, g - slaac, y - bgp-mpls-vpn; 
H - hw-offloaded; + - ecmp, B - blackhole 
 Ag + afi=ip6 contribution=active dst-address=::/0 routing-table=main 
       pref-src="" gateway=fe80::ba69:f4ff:fe84:7b2%ether1
       immediate-gw=fe80::ba69:f4ff:fe84:7b2%ether1 distance=1 scope=30 
       target-scope=10 belongs-to="slaac" mtu=1400 hoplimit=10 
       debug.fwp-ptr=0x201C2C00
```
## Properties
Property | Description
----------------------
address(Address/Netmask; Default: ) | Ipv6 address. Allowed netmask range is 0..128. Address can also be constructed from the pool iffrom-poolproperty is specified.For example if address is set to ::1/64 then address will be constructed as follows <prefix_from_pool>::1/64
advertise(yes | no; Default:no) | Whether to enable stateless address configuration. The prefix of that address is automatically advertised three times to hosts using ICMPv6 protocol. The option is set by default for addresses with prefix length 64. If address is removed or changed, then old prefix will be deprecated by automatically advertising the old prefix with lifetime set to "0s" three times to hosts using ICMPv6 protocol
commentcomment(string; Default: ) | Descriptive name of an item
disabled(yes | no; Default:no) | Whether address is disabled or not. By default it is not disabled
eui-64(yes | no; Default:no) | Whether to calculate EUI-64 address and use it as last 64 bits of the IPv6 address.
from-pool(string; Default: ) | Name of the pool from which prefix will be taken to construct IPv6 address taking last part of the address fromaddressproperty.
no-dad(yes | no; Default:no) | If enabled (yes) - disables Duplicate Address Detection (DAD) for IPv6 addresses on an interface. This can be useful in scenarios where you want to assign static IPv6 addresses to devices and avoid the delay caused by DAD.
interface(string; Default: ) | Name of an interface on which Ipv6 address is set.
auto-link-local (yes | no; Default: yes) | If newly created address is manual link-local address this setting allows to override dynamically created IPv6 link-local address.
## Read-only properties
Property | Description
----------------------
actual-interface(string) | Actual interface on which address is set up. For example, if address was configured on ethernet interface and ethernet interface was added to bridge, then actual interface is bridge not ethernet.
dynamic(yes | no) | Whether address is dynamically created
global(yes | no) | Whether address is global
invalid(yes | no) | Whether address is invalid
link-local(yes | no) | Whether address is link local
deprecated(yes | no) | Whether address is deprecated
slave(yes | no) | Whether address belongs to an interface which is a slave port to some other master interface
## Frequently asked questions
Q: Does RouterOS support NAT64?A: No, currently NAT64 is not implemented in RouterOS