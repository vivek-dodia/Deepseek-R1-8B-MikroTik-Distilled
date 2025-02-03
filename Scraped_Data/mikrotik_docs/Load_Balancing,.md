---
title: Load Balancing
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/4390920/Load+Balancing,
crawled_date: 2025-02-02T21:11:08.301251
section: mikrotik_docs
type: documentation
---

* Failover (WAN Backup)
* Per connection classifier
# Introduction
Network load balancing is the ability to balance traffic across two or more links without using dynamic routing protocols.
There are two type of balancing methods:
* per-packet - each packet of a single stream can be forwarded over different links. This method will work reliably especially on TCP and secure connections only when you are able to control both balancing endpoints.
* per-connection - all packets of the same connection (stream) is always sent over one link. This method is mandatory in setups where only one end of the balancing is under our control, for example, home router with multiple WAN connections.
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