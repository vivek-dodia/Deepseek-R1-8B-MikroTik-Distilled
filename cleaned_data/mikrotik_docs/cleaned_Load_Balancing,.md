# Document Information
Title: Load Balancing
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/4390920/Load+Balancing,

# Content
# Introduction
Network load balancing is the ability to balance traffic across two or more links without using dynamic routing protocols.
There are two type of balancing methods:
Method | Per-connection | Per-packet
------------------------------------
Firewall Mangle | Nth | Yes | Yes
PCC (Per Connection Classifier) | Yes | No
Other matchers | Yes | Yes
ECMP (Equal Cost Multi-Path) | Yes | No
Bonding | No | Yes
OSPF | Yes | No
BGP | Yes | No
Firewall Mangle
# Simple Failover Example
Simplest failover setup would be to use multiple gateways when one gateway is active and another one takes over when the first one fails.
To make this work, configure largerdistancevalue for the secondary one, andcheck-gatewayfor the first one:
```
/ip route add gateway=192.168.1.1 distance=1 check-gateway=ping
/ip route add gateway=192.168.2.1 distance=2
```
Thecheck-gatewaywill make sure the gateway is up only when actual traffic can reach the gateway. When the ping fails the first gateway will become inactive and the second one will take over,  and when the first gateway recovers  it will become active and make the second gateway to work again as a backup.