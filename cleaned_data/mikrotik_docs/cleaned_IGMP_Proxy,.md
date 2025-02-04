# Document Information
Title: IGMP Proxy
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/128221386/IGMP+Proxy,

# Content
# Summary
Internet Group Management Protocol (IGMP) proxy can implement multicast routing. It is forwarding IGMP frames and is commonly used when there is no need for a more advanced protocol like PIM.
IGMP proxy features:
On the other hand, IGMP proxy is not well suited for complicated multicast routing setups. Compared to PIM-based solutions, IGMP proxy does not support more than one upstream interface and routing loops are not detected or avoided.
By default, IGMP proxy upstream interface will send IGMPv3 membership reports and it will detect what IGMP version the upstream device (e.g. multicast router) is using based on received queries. In case IGMPv1/v2 queries are received, the upstream port will fall back to the lower IGMP version. It will convert back to IGMPv3 when IGMPv1/v2 querier present timer (400s) expires. Downstream interfaces of IGMP proxy will only send IGMPv2 queries.
# Configuration options
General IGMP proxy configuration.
Sub-menu:/routing igmp-proxy
```
/routing igmp-proxy
```
Property | Description
----------------------
query-interval(time:1s..1h; Default:2m5s) | How often to send out IGMP Query messages over downstream interfaces.
query-response-interval(time: 1s..1h; Default:10s) | How long to wait for responses to an IGMP Query message.
quick-leave | Specifies action on IGMP Leave message. If quick-leave is on, then an IGMP Leave message is sent upstream as soon as a leave message is received from the first client on the downstream interface. Useyesonly in case there is only one subscriber behind the proxy.
Property
Description
Configure what interfaces will participate as IGMP proxy interfaces on the router. If an interface is not configured as an IGMP proxy interface, then all IGMP traffic received on it will be ignored.
Sub-menu:/routing igmp-proxy interface
```
/routing igmp-proxy interface
```
Property | Description
----------------------
alternative-subnets(IP/Mask; Default:) | By default, only packets from directly attached subnets are accepted. This parameter can be used to specify a list of alternative valid packet source subnets, both for data or IGMP packets. Has an effect only on the upstream interface. Should be used when the source of multicast data often is in a different IP network.
interface(name; Default:all) | Name of the interface.
threshold(integer: 0..4294967295; Default:1) | Minimal TTL. Packets received with a lower TTL value are ignored
upstream(yes | no; Default:no) | The interface is called "upstream" if it's in the direction of the root of the multicast tree. An IGMP forwarding router must have exactly one upstream interface configured. The upstream interface is used to send out IGMP membership requests.
Property
Description
It is possible to get detailed status information for each interface using theprintstatuscommand.
```
print
```
```
status
```
```
[admin@MikroTik] /routing igmp-proxy interface print status
Flags: X - disabled, I - inactive, D - dynamic; U - upstream
0  U interface=ether2 threshold=1 alternative-subnets="" upstream=yes source-ip-address=192.168.10.10 rx-bytes=3018487500 rx-packets=2012325 tx-bytes=0 tx-packets=0
1    interface=ether3 threshold=1 alternative-subnets="" upstream=no querier=yes source-ip-address=192.168.20.10 rx-bytes=0 rx-packets=0 tx-bytes=2973486000 tx-packets=1982324
2    interface=ether4 threshold=1 alternative-subnets="" upstream=no querier=yes source-ip-address=192.168.30.10 rx-bytes=0 rx-packets=0 tx-bytes=152019000 tx-packets=101346
```
Property | Description
----------------------
querier(read-only; yes|no) | Whether the interface is acting as an IGMP querier.
source-ip-address(read-only; IP address) | The detected source IP for the interface.
rx-bytes(read-only; integer) | The total amount of received multicast traffic on the interface.
rx-packet(read-only; integer) | The total amount of received multicast packets on the interface.
tx-bytes(read-only; integer) | The total amount of transmitted multicast traffic on the interface.
tx-packet(read-only; integer) | The total amount of transmitted multicast packets on the interface.
Property
Description
Multicast forwarding cache (MFC) status.
Sub-menu:/routing igmp-proxy mfc
```
/routing igmp-proxy mfc
```
Property | Description
----------------------
active-downstream-interfaces(read-only:name) | The packet stream is going out of the router through this interface.
bytes(read-only:integer) | The total amount of received multicast traffic.
group(read-only: IP address) | IGMP group address.
packets(read-only: integer) | The total amount of received multicast packets.
source(read-only: IP address) | The multicast data originator address.
upstream-interface(read-only: name) | The packet stream is coming into the router through this interface.
wrong-packets(read-only: integer) | The total amount of received multicast packets that arrived on a wrong interface, for example, a multicast stream that is received on a downstream interface instead of an upstream interface.
Property
Description
The total amount of received multicast packets that arrived on a wrong interface, for example, a multicast stream that is received on a downstream interface instead of an upstream interface.
RouterOS support static multicast forwarding rules for IGMP proxy. If a static rule is added, all dynamic rules for that group will be ignored. These rules will take effect only if IGMP-proxy interfaces are configured (upstream and downstream interfaces should be set) or these rules won't be active.
Property | Description
----------------------
downstream-interfaces(name; Default: ) | The received stream will be sent out to the listed interfaces only.
group(read-only: IP address) | Themulticast group address this rule applies.
source(read-only: IP address) | The multicast data originator address.
upstream-interface(read-only: name) | Theinterface that is receiving stream data.
Property
Description
# Examples
To forward all multicast data coming fromtheether2interface to the downstream bridge interface, where subscribers are connected, use the configuration below. Both interfaces should have an IP address.
```
/routing igmp-proxy interface
add interface=ether2 upstream=yes
add interface=bridge1
[admin@MikroTik] /routing igmp-proxy interface print
Flags: U - UPSTREAM
Columns: INTERFACE, THRESHOLD
# INTERFACE  THRESHOLD
0 U ether2             1
1   bridge1            1
```
You may also need to configurealternative-subnetson the upstream interface in case the multicast sender address is in an IP subnet that is not directly reachable from the local router:
```
alternative-subnets
```
```
/routing igmp-proxy interface
set [find upstream=yes] alternative-subnets=192.168.50.0/24,192.168.60.0/24
```
To enablequick-leave, use the setting below:
```
quick-leave
```
```
/routing igmp-proxy
set quick-leave=yes
```