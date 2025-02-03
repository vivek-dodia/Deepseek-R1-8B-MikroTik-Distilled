---
title: Ping
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/8323183/Ping,
crawled_date: 2025-02-02T21:15:05.183982
section: mikrotik_docs
type: documentation
---

* 1Summary1.1Quick Example1.2MAC Ping
* 1.1Quick Example
* 1.2MAC Ping
# Summary
Ping uses the Internet Control Message Protocol (ICMP) Echo messages to determine if a remote host is active or inactive and to determine the round-trip delay when communicating with it. Ping tool sends ICMP (type 8) message to the host and waits for the ICMP echo-reply (type 0). The interval between these events is called a round trip. If the response (that is called pong) has not come until the end of the interval, we assume it has timed out. The second significant parameter reported is TTL (Time to Live). Is decremented at each machine in which the packet is processed. The packet will reach its destination only when the TTL is greater than the number of routers between the source and the destination.
## Quick Example
RouterOS Ping tool allows you to configure various additional parameters like:
* arp-ping;
* address;
* src-address;
* count;
* dscp;
* interface;
* interval;
* routing-table;
* size;
* ttl;
Let's take a look ar very simple example:
```
[admin@MikroTik] > /tool/ping address=10.155.126.252 count=5 interval=200ms  
  SEQ HOST                                     SIZE TTL TIME  STATUS                                                                                                                                                                              
    0 10.155.126.252                             56  64 0ms  
    1 10.155.126.252                             56  64 0ms  
    2 10.155.126.252                             56  64 0ms  
    3 10.155.126.252                             56  64 0ms  
    4 10.155.126.252                             56  64 0ms  
    sent=5 received=5 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms
```
The same we can achieve with more shorter CLI command:
```
[admin@MikroTik] > /ping 10.155.126.252 count=5 interval=50ms               
  SEQ HOST                                     SIZE TTL TIME  STATUS                                                                                                                                                                              
    0 10.155.126.252                             56  64 0ms  
    1 10.155.126.252                             56  64 0ms  
    2 10.155.126.252                             56  64 0ms  
    3 10.155.126.252                             56  64 0ms  
    4 10.155.126.252                             56  64 0ms  
    sent=5 received=5 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms
```
It is also possible to ping multicast address to discover all hosts belonging to multicast group:
```
[admin@MikroTik] > /ping ff02::1
HOST                                    SIZE  TTL TIME  STATUS                                         
fe80::20c:42ff:fe49:fceb                56    64  1ms   echo reply                                     
fe80::20c:42ff:fe72:a1b0                56    64  1ms   echo reply                                     
fe80::20c:42ff:fe28:7945                56    64  1ms   echo reply                                     
fe80::21a:4dff:fe5d:8e56                56    64  3ms   echo reply                                     
    sent=1 received=4 packet-loss=-300% min-rtt=1ms avg-rtt=1ms max-rtt=3ms
```
Ping by DNS name:
```
[admin@MikroTik]  > /ping www.google.com count=5 interval=50ms
  SEQ HOST                                     SIZE TTL TIME  STATUS                                                                                                                                                                              
    0 216.58.207.228                             56  51 14ms 
    1 216.58.207.228                             56  51 13ms 
    2 216.58.207.228                             56  51 13ms 
    3 216.58.207.228                             56  51 13ms 
    4 216.58.207.228                             56  51 13ms 
    sent=5 received=5 packet-loss=0% min-rtt=13ms avg-rtt=13ms max-rtt=14ms
```
## MAC Ping
This submenu allows enabling the mac ping server.
When mac ping is enabled, other hosts on the same broadcast domain can use the ping tool to ping mac address:
```
[admin@MikroTik]  > /tool mac-server ping set enabled=yes
```
Ping MAC address:
```
[admin@MikroTik]  > /ping 00:0C:42:72:A1:B0
HOST                                    SIZE  TTL TIME  STATUS                                         
00:0C:42:72:A1:B0                       56        0ms  
00:0C:42:72:A1:B0                       56        0ms  
    sent=2 received=2 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms
```