---
title: Traffic Eng
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/40992796/Traffic+Eng,
crawled_date: 2025-02-02T21:11:42.186132
section: mikrotik_docs
type: documentation
---

## Properties
Sub-menu:/interface traffic-eng
```
/interface traffic-eng
```
Property | Description
----------------------
affinity-exclude(integer; Default:not set) | Do not use interface ifresource-classmatches any of specified bits.
affinity-include-all(integer; Default:not set) | Use interface only ifresource-classmatches all of specified bits.
affinity-include-any(integer; Default:not set) | Use interface ifresource-classmatches any of specified bits.
auto-bandwidth-avg-interval(time; Default:5m) | Interval in which actual amount of data is measured, from which average bandwidth is calculated.
auto-bandwidth-range(Disabled | Min[bps][-Max[bps]]; Default:0bps) | Auto bandwidth adjustment range.Read more >>
auto-bandwidth-reserve(integer[%]; Default:0%) | Specifies percentage of additional bandwidth to reserve.Read more >>
auto-bandwidth-update-interval(time; Default:1h) | Interval during which tunnel keeps track of highest average rate.
bandwidth(integer[bps]; Default:0bps) | How much bandwidth to reserve for TE tunnel. Value is in bits per second.Read more >>
bandwidth-limit(disabled | integer[%]; Default:disabled) | Defines actual bandwidth limitation of TE tunnel. Limit is configured in percent of specified tunnelbandwidth.Read more >>
comment(string; Default: ) | Short description of the item
disable-running-check(yes | no; Default:no) | Specifies whether to detect if interface is running or not. If set tonointerface will always haverunningflag.
disabled(yes | no; Default:yes) | Defines whether item is ignored or used.
from-address(auto | IP; Default:auto) | Ingress address of the tunnel. If set toautoleast IP address is picked.
holding-priority(integer [0..7]; Default:not set) | Is used to decide whether this session can be preempted by another session. 0 sets the highest priority.
mtu(integer; Default:1500) | Layer3 Maximum Transmission Unit
name(string; Default: ) | Name of the interface
primary-path(string; Default: ) | Primary label switching paths defined in/mpls traffic-eng tunnel-pathmenu.
primary-retry-interval(time; Default:1m) | Interval after which tunnel will try to use primary path.
record-route(yes | no; Default:not set) | If enabled, the sender node will receive information about the actual route that the LSP tunnel traverses. Record Route is analogous to a path vector, and hence can be used for loop detection.
reoptimize-interval(time; Default:not set) | Interval after which tunnel will re-optimize current path. If current path is not the best path then after optimization best path will be used.Read more >>
secondary-paths(string[,string]; Default: ) | List of label switching paths used by TE tunnel if primary path fails. Paths are defined in/mpls traffic-eng tunnel-pathmenu.
setup-priority(integer[0..7]; Default:not set) | Parameter is used to decide whether this session can preempt another session. 0 sets the highest priority.
to-address(IP; Default:0.0.0.0) | Remote end of TE tunnel.
```
Read more >>
```
```
Read more >>
```
```
Read more >>
```
```
bandwidth
```
```
Read more >>
```
```
running
```
```
/mpls traffic-eng tunnel-path
```
```
Read more >>
```
```
/mpls traffic-eng tunnel-path
```
## Monitoring
To verify TE tunnel's statusmonitorcommand can be used.
```
monitor
```
```
/interface traffic-eng monitor 0 
tunnel-id: 12 
primary-path-state: on-hold 
secondary-path-state: established 
secondary-path: static 
active-path: static 
active-lspid: 3 
active-label: 66 
explicit-route: "S:192.168.55.10/32,L:192.168.55.13/32,L:192.168.55.17/32" 
recorded-route: "192.168.55.13[66],192.168.55.17[59],192.168.55.18[3]" 
reserved-bandwidth: 5.0Mbps
```
## Reoptimization
Path can be re-optimized manually by entering the command/interface traffic-eng reoptimize [id](where [id] is an item number or interface name). It allows network administrators to reoptimize the LSPs that have been established based on changes in bandwidth, traffic, management policy, or other factors.
```
/interface traffic-eng reoptimize [id]
```
Let's say TE tunnel chose another path after a link failure on best path. You can verify optimization by looking atexplicit-routeorrecorded-routevalues ifrecord-routeparameter is enabled.
```
explicit-route
```
```
recorded-route
```
```
/interface traffic-eng monitor 0 
tunnel-id: 12 
primary-path-state: established 
primary-path: dyn 
secondary-path-state: not-necessary 
active-path: dyn active-lspid: 1 
active-label: 67 
explicit-route: "S:192.168.55.10/32,S:192.168.55.13/32,S:192.168.55.14/32, 
S:192.168.55.17/32,S:192.168.55.18/32" 
recorded-route: "192.168.55.13[67],192.168.55.17[60],192.168.55.18[3]" 
reserved-bandwidth: 5.0Mbps
```
Whenever the link comes back, TE tunnel will use the same path even it is not the best path (unlessreoptimize-intervalis configured). To fix it we can manually reoptimize the tunnel path.
```
/interface traffic-eng reoptimize 0
```
```
/interface traffic-eng monitor 0 
tunnel-id: 12 
primary-path-state: established 
primary-path: dyn 
secondary-path-state: not-necessary 
active-path: dyn 
active-lspid: 2 active-label: 81 
explicit-route: "S:192.168.55.5/32,S:192.168.55.2/32,S:192.168.55.1/32" 
recorded-route: "192.168.55.2[81],192.168.55.1[3]" 
reserved-bandwidth: 5.0Mbps
```
Notice how explicit-route and recorded-route changed to a shorter path.