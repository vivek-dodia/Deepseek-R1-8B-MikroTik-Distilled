# Document Information
Title: Failover (WAN Backup)
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/26476608/Failover+WAN+Backup,

# Content
# Introduction
In this article, we will look at another advanced method of failover using recursive routing and scopes from the routing section. Recursive routing occurs when a route (either static or dynamically learned) has a next-hop that is not directly connected to the local router. It is necessary to restrict a set of routes that can be used to look up immediate next-hops. Nexthop values of RIP or OSPF routes, for example, are supposed to be directly reachable and should be looked up only using connected routes. This is achieved using a scope and target-scope properties.
# Setup Overview
Let's assume that our gateway has two public network uplinks ("ISP1", "ISP2"). First uplink should be preferred and second one should act as a backup.
Then we mark traffic in two parts, one with the name "ISP1" and the second as "ISP2" which goes through the ether1 and ether2 accordingly. In this setup, we want to monitor two hosts: Host1 and Host2. We will use Google DNS servers with IP 8.8.8.8 (Host1) and 8.8.4.4 (Host2), but it is not mandatory to use specifically these addresses.
# Configuration
# Basic failover
First things first, since we have a local address space we need to masquerade LAN traffic on both uplinks:
```
/ip/firewall/nat
add chain=srcnat action=masquerade out-interface=ether1
add chain=srcnat action=masquerade out-interface=ether2
```
Next we want to pick tow hosts on the internet and make them reachable each on its own uplink. Generally you would pick hosts that are always supposed to be reachable, accepts ICMP, in this example we will use google DNS servers (8.8.8.8 and 8.8.4.4).
```
/ip/route/
add dst-address=8.8.8.8 scope=10 gateway=10.111.0.1
add dst-address=8.8.4.4 scope=10 gateway=10.112.0.1
```
And add default routes recursively resolved over both hosts with ISP1 being the primary one (by having smaller distance):
```
/ip/route/
add distance=1 gateway=8.8.8.8 target-scope=11 check-gateway=ping
add distance=2 gateway=8.8.4.4 target-scope=11 check-gateway=ping
```
# Improve detection reliability
At this point we are relying link reachability on a single host. Even though google services are very rarely down we can still improve reliability by adding a second host on each link.
```
/ip/route
add dst-address=208.67.222.222 gateway=10.111.0.1 scope=10
add dst-address=208.67.220.220 gateway=10.112.0.1 scope=10
add distance=1 gateway=208.67.222.222 target-scope=11 check-gateway=ping
add distance=2 gateway=208.67.220.220 target-scope=11 check-gateway=ping
```
Essentially what it does is creates ECMP default route and if only one of the gateways is not reachable default route on the first link will still be active. Complete switchover to second link will happen only if all the gateways become unreachable.