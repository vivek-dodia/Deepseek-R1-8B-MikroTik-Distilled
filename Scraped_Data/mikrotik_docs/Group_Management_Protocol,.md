---
title: Group Management Protocol
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/131366949/Group+Management+Protocol,
crawled_date: 2025-02-02T21:12:16.015217
section: mikrotik_docs
type: documentation
---

* 1Introduction
* 2Configuration options
* 3Examples
# Introduction
The Group Management Protocol allows any of the interfaces to become a receiver for the multicast stream. It allows testing the multicast routing and switching setups without using dedicated IGMP or MLD clients. The option is available since RouterOS v7.4 and it supports IGMP v1, v2, v3 and MLD v1, v2 protocols.
Interfaces are using IGMP v3 and MLD v2 by default. In case IGMP v1, v2 or MLD v1 queries are received, the interfaces will fall back to the appropriate version. Once Group Management Protocol is created on the interface, it will send an unsolicited membership report (join) packet and respond to query messages. If the configuration is removed or disabled, the interface will send a leave message.
# Configuration options
This section describes the Group Management Protocol configuration options.
Sub-menu:/routing gmp
```
/routing gmp
```
Property | Description
----------------------
groups(IPv4 | IPv6; Default: ) | The multicast group address to be used by the interface, multiple group addresses are supported.
interfaces(name; Default:) | Name of the interface, multiple interfaces and interface lists are supported.
exclude(Default:) | Whenexcludeis set, the interface expects to reject multicast data from the configuredsources. When this option is not used, the interfaces will emit source specific join for the configuredsources.
sources(IPv4 | IPv6; Default: ) | The source address list used by the interface, multiple source addresses are supported.This setting has an effect when IGMPv3 or MLDv2 protocols are active.
Property
Description
Whenexcludeis set, the interface expects to reject multicast data from the configuredsources. When this option is not used, the interfaces will emit source specific join for the configuredsources.
```
exclude
```
```
sources
```
```
sources
```
# Examples
This example shows how to configure a simple multicast listener on the interface.
First, add an IP address on the interface:
```
/ip address
add address=192.168.10.10/24 interface=ether1 network=192.168.10.0
```
Then configure Group Management Protocol on the same interface:
```
/routing gmp
add groups=229.1.1.1 interfaces=ether1
```
It is now possible to check your multicast network to see if routers or switches have created the appropriate multicast forwarding entries and whether multicast data is being received on the interface (see the interface stats, or use aPacket SnifferandTorch).