# Document Information
Title: Filter
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/48660574/Filter,

# Content
# Introduction
Firewall filters are used to allow or block specific packets forwarded to your local network, originating from your router, or destined to the router.
There are two methods on how to set up filtering:
Both methods have pros and cons, for example, from a security point of view first method is much more secure, but requires administrator input whenever traffic for a new service needs to be accepted. This strategy provides good control over the traffic and reduces the possibility of a breach because of service misconfiguration.
On the other hand, when securing a customer network it would be an administrative nightmare to accept all possible services that users may use. Therefore careful planning of the firewall is essential in advanced setups.
A firewall filter consists of three predefined chains that cannot be deleted:
Firewall filter configuration is accessible fromip/firewall/filtermenu for IPv4 andipv6/firewall/filtermenu for IPv6.
```
ip/firewall/filter
```
```
ipv6/firewall/filter
```
# Firewall Example
Lets look at basic firewall example to protect router itself and clients behind the router, for both IPv4 and IPv6 protocols.
# IPv4 firewall
# Protect the router itself
Rules of thumb followed to set up the firewall:
```
new
```
```
drop
```
```
log=yes
```
We always start by accepting already known and accepted connections, so the first rule should be to accept "established" and "related" connections.
```
/ip firewall filter
add action=accept chain=input comment="default configuration" connection-state=established,related
```
Now we can proceed by accepting some new connections, in our example we want to allow access ICMP protocol from any address and everything else only from 192.168.88.2-192.168.88.254 address range. For that we create an address list and two firewall rules.
```
/ip firewall address-list
add address=192.168.88.2-192.168.88.254 list=allowed_to_router
/ip firewall filter
add action=accept chain=input src-address-list=allowed_to_router
add action=accept chain=input protocol=icmp
```
And lastly we drop everything else:
```
add action=drop chain=input
```
Complete set of just created rules:
```
/ip firewall filter
add action=accept chain=input comment="default configuration" connection-state=established,related
add action=accept chain=input src-address-list=allowed_to_router
add action=accept chain=input protocol=icmp
add action=drop chain=input
/ip firewall address-list
add address=192.168.88.2-192.168.88.254 list=allowed_to_router
```
# Protect the LAN devices
Concept in protecting the users is very similar, except that in this case we are blocking unwanted traffic and accepting everythign else.
At first we will createaddress-listwith the name "not_in_internet" which we will use for the firewall filter rules:
```
address-list
```
```
/ip firewall address-list
add address=0.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=172.16.0.0/12 comment=RFC6890 list=not_in_internet
add address=192.168.0.0/16 comment=RFC6890 list=not_in_internet
add address=10.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=169.254.0.0/16 comment=RFC6890 list=not_in_internet
add address=127.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=224.0.0.0/4 comment=Multicast list=not_in_internet
add address=198.18.0.0/15 comment=RFC6890 list=not_in_internet
add address=192.0.0.0/24 comment=RFC6890 list=not_in_internet
add address=192.0.2.0/24 comment=RFC6890 list=not_in_internet
add address=198.51.100.0/24 comment=RFC6890 list=not_in_internet
add address=203.0.113.0/24 comment=RFC6890 list=not_in_internet
add address=100.64.0.0/10 comment=RFC6890 list=not_in_internet
add address=240.0.0.0/4 comment=RFC6890 list=not_in_internet
add address=192.88.99.0/24 comment="6to4 relay Anycast [RFC 3068]" list=not_in_internet
```
Brief firewall filter rule explanation:
```
/ip firewall filter
add action=fasttrack-connection chain=forward comment=FastTrack connection-state=established,related
add action=accept chain=forward comment="Established, Related" connection-state=established,related
add action=drop chain=forward comment="Drop invalid" connection-state=invalid log=yes log-prefix=invalid
add action=drop chain=forward comment="Drop tries to reach not public addresses from LAN" dst-address-list=not_in_internet in-interface=bridge log=yes log-prefix=!public_from_LAN out-interface=!bridge
add action=drop chain=forward comment="Drop incoming packets that are not NAT`ted" connection-nat-state=!dstnat connection-state=new in-interface=ether1 log=yes log-prefix=!NAT
add action=jump chain=forward protocol=icmp jump-target=icmp comment="jump to ICMP filters"
add action=drop chain=forward comment="Drop incoming from internet which is not public IP" in-interface=ether1 log=yes log-prefix=!public src-address-list=not_in_internet
add action=drop chain=forward comment="Drop packets from LAN that do not have LAN IP" in-interface=bridge log=yes log-prefix=LAN_!LAN src-address=!192.168.88.0/24
```
Allow only needed ICMP codes in "icmp" chain:
```
/ip firewall filter
add chain=icmp protocol=icmp icmp-options=0:0 action=accept \
comment="echo reply"
add chain=icmp protocol=icmp icmp-options=3:0 action=accept \
comment="net unreachable"
add chain=icmp protocol=icmp icmp-options=3:1 action=accept \
comment="host unreachable"
add chain=icmp protocol=icmp icmp-options=3:4 action=accept \
comment="host unreachable fragmentation required"
add chain=icmp protocol=icmp icmp-options=8:0 action=accept \
comment="allow echo request"
add chain=icmp protocol=icmp icmp-options=11:0 action=accept \
comment="allow time exceed"
add chain=icmp protocol=icmp icmp-options=12:0 action=accept \
comment="allow parameter bad"
add chain=icmp action=drop comment="deny all other types"
```
# IPv6 firewall
# Protect the router itself
Very similar to IPv4 setup, except that we have to deal with more protocols required for IPv6 to function properly.
At first we create anaddress-listfrom which you allow access to the device:
```
address-list
```
```
/ipv6 firewall address-list add address=fd12:672e:6f65:8899::/64 list=allowed
```
Brief IPv6 firewall filter rule explanation:
```
/ipv6 firewall filter
add action=accept chain=input comment="allow established and related" connection-state=established,related
add chain=input action=accept protocol=icmpv6 comment="accept ICMPv6"
add chain=input action=accept protocol=udp port=33434-33534 comment="defconf: accept UDP traceroute"
add chain=input action=accept protocol=udp dst-port=546 src-address=fe80::/10 comment="accept DHCPv6-Client prefix delegation."
add action=drop chain=input in-interface=in_interface_name log=yes log-prefix=dropLL_from_public src-address=fe80::/10
add action=accept chain=input comment="allow allowed addresses" src-address-list=allowed
add action=drop chain=input
/ipv6 firewall address-list
add address=fe80::/16 list=allowed
add address=xxxx::/48 list=allowed
add address=ff02::/16 comment=multicast list=allowed
```
# Protect the LAN devices
This step is more important than it is for IPv4. In IPv4 setups clients mostly have addresses from local address range and are NATed to public IP, that way they are not directly reachable from the public networks.
IPv6 is a different story. In most common setups, enabled IPv6 makes your clients available from the public networks, so proper firewall filter rules to protect your customers are mandatory.
In brief we will very basic LAN protection should:
```
/ipv6 firewall filter
add action=accept chain=forward comment=established,related connection-state=established,related
add action=drop chain=forward comment=invalid connection-state=invalid log=yes log-prefix=ipv6,invalid
add action=accept chain=forward comment=icmpv6 in-interface=!in_interface_name protocol=icmpv6
add action=accept chain=forward comment="local network" in-interface=!in_interface_name src-address-list=allowed
add action=drop chain=forward log-prefix=IPV6
```
# Matchers
All matcher properties are common and listedhere.
# Actions
Tables below shows list of filter specific actions and associated properties.  Other actions arelistedhere.
Property | Description
----------------------
action(action name; Default:accept) | drop- silently drop the packetfasttrack-connection- process packets from a connection using FastPath by enablingFastTrackfor the connection.IPv4only.reject- drop the packet and send an ICMP reject message; this action allows ICMP reply specification, such as: prohibit or unreachable admin/host/network/porttarpit- captures and holds TCP connections (replies with SYN/ACK to the inbound TCP SYN packet).IPv4only.
reject-with(icmp-no-route | icmp-admin-prohibited | icmp-not-neighbour| icmp-address-unreachable | icmp-port-unreachable | tcp-reset | icmp-err-src-routing-header | icmp-headers-too-long; Default:icmp-no-route) | SpecifiesICMP errorto be sent back if the packet is rejected. Applicable ifaction=rejecticmp-no-route: sends ICMP address no-route message. ICMP type 2, code 0icmp-admin-prohibited: sends ICMP address prohibited message. ICMP type 2, code 1icmp-not-neighbour: sends ICMP address not-member message. ICMP type 2, code 2icmp-address-unreachable: sends ICMP address unreachable message. ICMP type 2, code 3icmp-port-unreachable: sends ICMP port unreachable message. ICMP type 2, code 4tcp-reset: sends ICMP resetting a TCP connection. ICMP type 2, code 6icmp-err-src-routing-header: sends ICMP Error in Source Routing Header message. ICMP type 2, code 7icmp-headers-too-long: sends ICMP Headers too long message. ICMP type 2, code 8
SpecifiesICMP errorto be sent back if the packet is rejected. Applicable ifaction=reject
```
action=reject
```
# RAW Filtering
The firewall RAW table allows to selectively bypass or drop packets before connection tracking, that way significantly reducing the load on the CPU. The tool is very useful for DoS/DDoS attack mitigation.
RAW filter configuration is accessible fromip/firewall/rawmenu for IPv4 andipv6/firewall/rawmenu for IPv6.
```
ip/firewall/raw
```
```
ipv6/firewall/raw
```
The RAW table does not have matchers that depend on connection tracking ( like connection-state, layer7, etc.).If a packet is marked to bypass the connection tracking packet de-fragmentation will not occur.
Also RAW firewall can have rules only in two chains:
And has one specific action:
Property | Description
----------------------
action(action name; Default:accept) | notrack- do not send a packet to connection tracking. Useful when you still need to use regular firewall, but do not require connection tracking.
```
notrack
```
# Basic RAW Example
Let's assume that we have OSPF configuration, but due to connection tracking OSPF have adjacency problems. We can use RAW rules to fix this, by not sending OSPF packets to connection tracking.
```
/ip firewall raw
add chain=prerouting protocol=ospf action=notrack
add chain=output protocol=ospf action=notrack
```
# Read More
* Syn/DoS protection