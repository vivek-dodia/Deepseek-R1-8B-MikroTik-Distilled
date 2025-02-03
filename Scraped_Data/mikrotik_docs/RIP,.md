---
title: RIP
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/328211/RIP,
crawled_date: 2025-02-02T21:12:09.862982
section: mikrotik_docs
type: documentation
---

* 1Summary
* 2General
* 3Interface
* 4Neighbor
* 5Keys
## Summary
MikroTik RouterOS implements RIP version 2 (RFC 2453). Version 1 (RFC 1058) is not supported.
RIP enables routers in an autonomous system to exchange routing information. It always uses the best path (the path with the fewest number of hops (i.e. routers)) available.
## General
Sub-menu:/routing rip instance
```
/routing rip instance
```
Property | Description
----------------------
name | name of the instance
vrf( Default:main) | whichVRFto use
afi(ipv4 | ipv6; Default:) | specifies which afi to use.
in-filter-chain(Default:) | input filter chain
out-filter-chain(Default:) | output filter chain
out-filter-select(Default:) | output filter select rule chain
redistribute(bgp, bgp-mpls-vpn, connected, dhcp, fantasy, modem, ospf, rip, static, vpn; Default:) | which routes to redistribute
originate-default( Default:) | whether to originate default route
routing-table( Default: main) | in which routing table the routes will be added
route-timeout(Default:) | route timeout
route-gc-timeout(Default:) | 
update-interval(time; Default:) | specifies time interval after which the route is considered invalid
Note:The maximum metric of RIP route is 15. Metric higher than 15 is considered 'infinity' and routes with such metric are considered unreachable. Thus RIP cannot be used on networks with more than 15 hops between any two routers, and using redistribute metrics larger that 1 further reduces this maximum hop count.
## Interface
Sub-menu:/routing rip interface-template
```
/routing rip interface-template
```
Property | Description
----------------------
name | name of the instance
instance | whichVRFto use
interfaces | specifies which afi to use.
source-addresses | input filter chain
cost(Default:) | output filter chain
split-horizon(no| yes) | 
poison-reverse(no| yes) | 
mode(passive| strict) | 
key-chain(name) | name of key-chain
password | password
Sub-menu:/routing rip interface
```
/routing rip interface
```
Read-only properties:
Property | Description
----------------------
instance(name) | name of the instance
address(address%interface) | IP address and interface name
## Neighbor
Sub-menu:/routing rip neighbor
```
/routing rip neighbor
```
This submenu is used to define a neighboring routers to exchange routing information with. Normally there is no need to add the neighbors, if multicasting is working properly within the network. If there are problems with exchanging routing information, neighbor routers can be added to the list. It will force the router to exchange the routing information with the neighbor using regular unicast packets.
Read-only properties:
Property | Description
----------------------
address(IP address) | IP address of neighboring router
routes | amount of routes
packets-total | amount of all packets
packets-bad | amount of bad packets
entries-bad | amount of bad entries
last-update(time) | time from last update
Sub-menu:/routing rip static-neighbor
```
/routing rip static-neighbor
```
Property | Description
----------------------
instance(name) | name of used instance
address(IP address) | IP address of neighboring router
## Keys
Sub-menu:/routing rip keys
```
/routing rip keys
```
MD5 authentication key chains.
Property | Description
----------------------
chain(string; Default:"") | chain name to place this key in.
key(string; Default:"") | authentication key. Maximal length 16 characters
key-id(integer:0..255; Default: ) | key identifier. This number is included in MD5 authenticated RIP messages, and determines witch key to use to check authentication for a specific message.
valid-from(date and time; Default: today's date and time:00:00:00) | key is valid from this date and time
valid-till(date and time; Default: today's date and time: 00:00:00) | key is valid until this date and time