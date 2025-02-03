---
title: Traceroute
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/130220138/Traceroute,
crawled_date: 2025-02-02T21:15:13.725224
section: mikrotik_docs
type: documentation
---

* 1Overview
* 2Quick Example
# Overview
Sub-menu:/tool traceroute
```
/tool traceroute
```
Traceroutedisplays the list of the routers that packet travels through to get to a remote host. Thetracerouteortracepathtool is available on practically all Unix-like operating systems andtracerton Microsoft Windows operating systems.
Traceroute operation is based on TTL value and ICMP “Time Exceeded” message. Remember that TTL value in IP header is used to avoid routing loops. Each hop decrements TTL value by 1. If the TTL reaches zero, the packet is discarded and ICMP Time Exceeded message is sent back to the sender when this occurs.
Initially by traceroute, the TTL value is set to 1 when next router finds a packet with TTL = 1 it sets TTL value to zero, and responds with an ICMP "time exceeded" message to the source. This message lets the source know that the packet traverses that particular router as a hop. Next time TTL value is incremented by 1 and so on. Typically, each router in the path towards the destination decrements the TTL field by one unit TTL reaches zero.
Using this command you can see how packets travel through the network and where it may fail or slow down. Using this information you can determine the computer, router, switch or other network device that possibly causing network issues or failures.
# Quick Example
```
[admin@MikroTik] > tool traceroute 10.255.255.1
     ADDRESS                                    STATUS
   1       10.0.1.17 2ms 1ms 1ms 
   2    10.255.255.1 5ms 1ms 1ms
[admin@MikroTik] >
```