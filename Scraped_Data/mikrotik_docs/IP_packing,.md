---
title: IP packing
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/139526171/IP+packing,
crawled_date: 2025-02-02T21:15:39.372117
section: mikrotik_docs
type: documentation
---

# Overview
IP Packing provides packet packaging service on network links. It allows simple packet aggregation into larger packets and compression of the contents of packets.
# Requirements
Packet packing is part of the system package and has to have a discovery protocol enabled on an interface.
## Configuration
```
/ip packing
```
It required to have a configuration in two places, both routers should be set up symmetrically:
* /ip packing- to enable packet aggregation and/or compression on an interface
* /ip neighbor discovery- to enablediscoveryprotocol on the interface
```
/ip packing
```
```
/ip neighbor discovery
```
## Packing configuration
Property | Description
----------------------
aggregated-size (20 .. 16384 default:1500) | size of an aggregated packet that packing will try to achieve before sending a packet over the network
disabled (yes|no) | state of packing rule, if a value isyesit will be ignored and will not be part of the active configuration
interface (interface name) | packing will try to aggregate and/or compress packets from this interface
packing (simple|compress-all|compress-headers|none) | the action it should perform when a packet is leaving the interface packing rule is configured:simple- do just aggregate packetscompress-all- do aggregation and attempt to compress headers and payload of a packetcompress-headers- do aggregation and attempt to compress headers and leave the payload of a packet as isnone- send packets as is
unpacking (simple|compress-all|compress-headers|none) | the action should be performed when a packet is received on the interface packing rule is configured on:simple- unpack received packets from aggregated packets received from the interfacecompress-all- unpack aggregated packet and uncompress headers and payload of a packetcompress-headers- unpack aggregated packets and decompress headers of a packetnone- do nothing with a received packet
* simple- do just aggregate packets
* compress-all- do aggregation and attempt to compress headers and payload of a packet
* compress-headers- do aggregation and attempt to compress headers and leave the payload of a packet as is
* none- send packets as is
```
simple
```
```
compress-all
```
```
compress-headers
```
```
none
```
* simple- unpack received packets from aggregated packets received from the interface
* compress-all- unpack aggregated packet and uncompress headers and payload of a packet
* compress-headers- unpack aggregated packets and decompress headers of a packet
* none- do nothing with a received packet
```
simple
```
```
compress-all
```
```
compress-headers
```
```
none
```
# Example
Router-A and Router-B are connected with cable with interface ether1 on Router-A and ether3 on Router-B. This example will aggregate packets coming from Router-A, but will leave packets from Router-B intact On Router-A:
Make sure discovery is enabled:
```
/ip neighbor discovery set ether1 discover=yes
```
Add packing rule for the interface:
```
/ip packing add interface=ether1 aggregated-size=1500 packing=simple unpacking=none
```
On Router-B:
Make sure discovery is enabled:
```
/ip neighbor discovery set ether3 discover=yes
```
Add packing rule for the interface:
```
/ip packing add interface=ether3 aggregated-size=1500 packing=none unpacking=simple
```