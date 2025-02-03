---
title: L3 Hardware Offloading
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/62390319/L3+Hardware+Offloading,
crawled_date: 2025-02-02T21:09:54.804682
section: mikrotik_docs
type: documentation
---

* 1Introduction
* 2Switch Configuration2.1Switch Port Configuration2.2L3HW Settings2.2.1Basic Settings2.2.2Advanced Settings2.2.3Monitor2.2.4Advanced Monitor2.3Interface Lists2.4MTU2.5Layer 2 Dependency2.6MAC telnet2.7Inter-VLAN Routing2.8L3HW MAC Address Range Limitation (DX2000/DX3000 series only)
* 3Route Configuration3.1Suppressing HW Offload3.2Routing Filters3.3Offloading Fasttrack Connections3.4Stateless Hardware Firewall3.5Switch Rules (ACL) vs. Fasttrack HW Offloading
* 4Configuration Examples4.1Inter-VLAN Routing with Upstream Port Behind Firewall/NAT
* 5Typical Misconfiguration5.1VLAN interface on a switch port or bond5.2Not adding the bridge interface to /interface/bridge/vlan/5.3Creating multiple bridges5.4Using ports that do not belong to the switch5.5Relying on Fasttrack HW Offloading too much5.6Trying to offload slow-path connections
* 6L3HW Feature Support
* 7L3HW Device Support7.1CRS3xx: Switch DX3000 and DX2000 Series7.2CRS3xx, CRS5xx: Switch DX8000 and DX4000 Series7.3CCR2000
* 2.1Switch Port Configuration
* 2.2L3HW Settings2.2.1Basic Settings2.2.2Advanced Settings2.2.3Monitor2.2.4Advanced Monitor
* 2.3Interface Lists
* 2.4MTU
* 2.5Layer 2 Dependency
* 2.6MAC telnet
* 2.7Inter-VLAN Routing
* 2.8L3HW MAC Address Range Limitation (DX2000/DX3000 series only)
* 2.2.1Basic Settings
* 2.2.2Advanced Settings
* 2.2.3Monitor
* 2.2.4Advanced Monitor
* 3.1Suppressing HW Offload
* 3.2Routing Filters
* 3.3Offloading Fasttrack Connections
* 3.4Stateless Hardware Firewall
* 3.5Switch Rules (ACL) vs. Fasttrack HW Offloading
* 4.1Inter-VLAN Routing with Upstream Port Behind Firewall/NAT
* 5.1VLAN interface on a switch port or bond
* 5.2Not adding the bridge interface to /interface/bridge/vlan/
* 5.3Creating multiple bridges
* 5.4Using ports that do not belong to the switch
* 5.5Relying on Fasttrack HW Offloading too much
* 5.6Trying to offload slow-path connections
* 7.1CRS3xx: Switch DX3000 and DX2000 Series
* 7.2CRS3xx, CRS5xx: Switch DX8000 and DX4000 Series
* 7.3CCR2000
# Introduction
Layer 3 Hardware Offloading(L3HW, otherwise known as IP switching or HW routing) allows to offload some router features onto the switch chip. This allows reaching wire speeds when routing packets, which would simply not be possible with the CPU.
# Switch Configuration
To enable Layer 3 Hardware Offloading, setl3-hw-offloading=yesfor the switch:
```
l3-hw-offloading=yes
```
```
/interface/ethernet/switch set 0 l3-hw-offloading=yes
```
## Switch Port Configuration
Layer 3 Hardware Offloading can be configured for each physical switch port. For example:
```
/interface/ethernet/switch/port set sfp-sfpplus1 l3-hw-offloading=yes
```
Note that l3hw settings for switch and ports are different:
* Settingl3-hw-offloading=nofor the switch completely disables offloading - all packets will be routed by CPU.
* However, settingl3-hw-offloading=nofor a switch port only disables hardware routing from/to this particular port. Moreover, the port can still participate in Fastrack connection offloading.
```
l3-hw-offloading
```
```
=no
```
```
l3-hw-offloading
```
```
=no
```
To enable full hardware routing, enable l3hw on all switch ports:
```
/interface/ethernet/switch set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port set [find] l3-hw-offloading=yes
```
To make all packets go through the CPU first, and offload only the Fasttrack connections, disable l3hw on all ports but keep it enabled on the switch chip itself:
```
/interface/ethernet/switch set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port set [find] l3-hw-offloading=no
```
The next example enables hardware routing on all ports but the upstream port (sfp-sfpplus16). Packets going to/from sfp-sfpplus16 will enter the CPU and, therefore, subject to Firewall/NAT processing.
```
/interface/ethernet/switch set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port set [find] l3-hw-offloading=yes
/interface/ethernet/switch/port set sfp-sfpplus16 l3-hw-offloading=no
```
## L3HW Settings
### Basic Settings
The L3HW Settings menu has been introduced in RouterOS version 7.6.
Sub-menu:/interface ethernet switch l3hw-settings
```
/interface ethernet switch l3hw-settings
```
Property | Description
----------------------
autorestart(yes | no; Default:no) | Automatically restarts the l3hw driver in case of an error. Otherwise, if an error occurs,l3-hw-offloadinggets disabled, and the error code is displayed in the switch settings and#monitor. Autorestart does not work for system failures, such as OOM (Out Of Memory).
fasttrack-hw(yes | no; Default:yes(if supported)) | Enables or disables FastTrack HW Offloading. Keep it enabled unless HW TCAM memory reservation is required, e.g., for dynamic switch ACL rules creation. Not all switch chips support FastTrack HW Offloading (seehw-supports-fasttrack).
ipv6-hw(yes | no; Default:no) | Enables or disables IPv6 Hardware Offloading. Since IPv6 routes occupy a lot of HW memory, enable it only if IPv6 traffic speed is significant enough to benefit from hardware routing.
icmp-reply-on-error(yes | no; Default:yes) | Since the hardware cannot send ICMP messages, the packet must be redirected to the CPU to send an ICMP reply in case of an error (e.g., "Time Exceeded", "Fragmentation required", etc.). Enabling icmp-reply-on-errorhelps with network diagnostics but may open potential vulnerabilities for DDoS attacks. Disabling icmp-reply-on-error silently drops the packets on the hardware level in case of an error.
Property
Description
```
l3-hw-offloading
```
Read-Only Properties
Property | Description
----------------------
hw-supports-fasttrack(yes | no) | Indicates if the hardware (switch chip) supports FastTrack HW Offloading.
Property
Description
### Advanced Settings
This menu allows tweaking l3hw settings for specific use cases.
Sub-menu:/interface ethernet switch l3hw-settingsadvanced
```
/interface ethernet switch l3hw-settings
```
Property | Description
----------------------
route-queue-limit-high(number; Default:256) | The switch driver stops route indexing whenroute-queue-size(see#monitor) exceeds this value. Lowering this value leads to faster route processing but increases the lag between a route's appearance in RouterOS and hardware memory.Settingroute-queue-limit-high=0disables route indexing when there are any routes in the processing queue -  the most efficient CPU usage but the longest delay before hardware offloading. Useful when there are static routes only. Not recommended together with routing protocols (such as BGP or OSPF) when there are frequent routing table changes.
route-queue-limit-low(number; Default:0) | Re-enable route indexing whenroute-queue-sizedrops down to this value. Must not exceed the high limit.Settingroute-queue-limit-low=0tells the switch driver to process all pending routes before the next hw-offloading attempt. While this is the desired behavior, it may completely block the hw-offloading under a constant BGP feed.
shwp-reset-counter(number; Default:128) | Reset the Shortest HW Prefix (seeipv4-shortest-hw-prefix/ipv6-shortest-hw-prefixin#monitor) and try the full route table offloading after this amount of changes in the routing table. At a partial offload, when the entire routing table does not fit into the hardware memory and shorter prefixes are redirected to the CPU, there is no need to try offloading route prefixes shorter than SHWP since those will get redirected to the CPU anyway, theoretically. However, significant changes to the routing table may lead to a different index layout and, therefore, a different amount of routes that can be hw-offloaded. That's why it is recommended to do the full table re-indexing occasionally.Lowering this value may allow more routes to be hw-offloaded but increases CPU usage and vice-versa. Settingshwp-reset-counter=0always does full re-indexing after each routing table change.This setting is used only during Partial Offloading and has no effect whenipv4-shortest-hw-prefix=0(and ipv6, respectively).
partial-offload-chunk(number; Default:1024, min: 16) | The minimum number of routes for incremental adding in Partial Offloading. Depending on the switch chip model, routes are offloaded either as-is (each routing entry in RouterOS corresponds to an entry in the hardware memory) or getting indexed, and the index entries are the ones that are written into the hardware memory. This setting is used only for the latter during Partial Offloading.Depending on index fragmentation, a single IPv4 route addition can occupy from -3 to +6 LPM blocks of HW memory (some route addition may lower the amount of required HW memory thanks to index defragmentation). Hence, it is impossible to predict the exact number of routes that may fit in the hardware memory. The switch driver uses a binary split algorithm to find the maximum number of routes that fit in the hardware.Let's imagine 128k routes, all of them not fitting into the hardware memory. The algorithm halves the number and tries offloading 64k routes. Let's say offloading succeeded. In the next iteration, the algorithm picks 96k, let's say it fails; then 80k - fails again, 72k - succeeds, 76k, etc. until the difference between succeeded and failed numbers drops below thepartial-offload-chunkvalue.Lowering thepartial-offload-chunkvalue increases the number of hw-offloaded routes but also raises CPU usage and vice-versa.
route-index-delay-min(time; Default:1s) | The minimum delay between route processing and its offloading. The delay allows processing more routes together and offloading them at once, saving CPU usage. It also makes offloading the entire routing table faster by reducing the per-route processing work. On the other hand, it slows down the offloading of an individual route.If an additional route is received during the delay, the latter resets to theroute-index-delay-minvalue.Adding more and more routes within the delay keeps resetting the timer until theroute-index-delay-maxis reached.
route-index-delay-max(time; Default:10s) | The maximum delay between route processing and its offloading. When the maximum delay is reached, the processed routes get offloaded despite more routes pending. However,route-queue-limit-highhas higher priority than this, meaning that the indexing/offloading gets paused anyway when a certain queue size is reached.
neigh-keepalive-interval(time; Default:15s, min: 5s) | Neighbor (host) keepalive interval. When a host (IP neighbor) gets hw-offloaded, all traffic from/to it is routed by the switch chip, and RouterOS may think the neighbor is inactive and delete it. To prevent that, the switch driver must keep the offloaded neighbors alive by sending periodical refreshes to RouterOS.
neigh-discovery-interval(time; Default:1m37s, min: 30s) | Unfortunately, switch chips do not provide per-neighbor stats. Hence, the only way to check if the offloaded host is still active is by sending occasional ARP (IPv4) / Neighbor Discovery (IPv6) requests to the connected network. Increasing the value lowers the broadcast traffic but may leave inactive hosts in hardware memory for longer.Neighbor discovery is triggered within the neighbor keepalive work. Hence, the discovery time is rounded up to the next keepalive session. Choose a value forneigh-discovery-intervalnot dividable byneigh-keepalive-intervalto send ARP/ND requests in various sessions, preventing broadcast bursts.
neigh-discovery-burst-limit(number; Default:64) | The maximum number of ARP/ND requests that can be sent at once.
neigh-discovery-burst-delay(time; Default:300ms, min: 10ms) | The delay between ARP/ND subsequent bursts if the number of requests exceedsneigh-discovery-burst-limit.
Property
Description
The switch driver stops route indexing whenroute-queue-size(see#monitor) exceeds this value. Lowering this value leads to faster route processing but increases the lag between a route's appearance in RouterOS and hardware memory.
Settingroute-queue-limit-high=0disables route indexing when there are any routes in the processing queue -  the most efficient CPU usage but the longest delay before hardware offloading. Useful when there are static routes only. Not recommended together with routing protocols (such as BGP or OSPF) when there are frequent routing table changes.
Re-enable route indexing whenroute-queue-sizedrops down to this value. Must not exceed the high limit.
Settingroute-queue-limit-low=0tells the switch driver to process all pending routes before the next hw-offloading attempt. While this is the desired behavior, it may completely block the hw-offloading under a constant BGP feed.
Reset the Shortest HW Prefix (seeipv4-shortest-hw-prefix/ipv6-shortest-hw-prefixin#monitor) and try the full route table offloading after this amount of changes in the routing table. At a partial offload, when the entire routing table does not fit into the hardware memory and shorter prefixes are redirected to the CPU, there is no need to try offloading route prefixes shorter than SHWP since those will get redirected to the CPU anyway, theoretically. However, significant changes to the routing table may lead to a different index layout and, therefore, a different amount of routes that can be hw-offloaded. That's why it is recommended to do the full table re-indexing occasionally.
Lowering this value may allow more routes to be hw-offloaded but increases CPU usage and vice-versa. Settingshwp-reset-counter=0always does full re-indexing after each routing table change.
This setting is used only during Partial Offloading and has no effect whenipv4-shortest-hw-prefix=0(and ipv6, respectively).
The minimum number of routes for incremental adding in Partial Offloading. Depending on the switch chip model, routes are offloaded either as-is (each routing entry in RouterOS corresponds to an entry in the hardware memory) or getting indexed, and the index entries are the ones that are written into the hardware memory. This setting is used only for the latter during Partial Offloading.
Depending on index fragmentation, a single IPv4 route addition can occupy from -3 to +6 LPM blocks of HW memory (some route addition may lower the amount of required HW memory thanks to index defragmentation). Hence, it is impossible to predict the exact number of routes that may fit in the hardware memory. The switch driver uses a binary split algorithm to find the maximum number of routes that fit in the hardware.
Let's imagine 128k routes, all of them not fitting into the hardware memory. The algorithm halves the number and tries offloading 64k routes. Let's say offloading succeeded. In the next iteration, the algorithm picks 96k, let's say it fails; then 80k - fails again, 72k - succeeds, 76k, etc. until the difference between succeeded and failed numbers drops below thepartial-offload-chunkvalue.
Lowering thepartial-offload-chunkvalue increases the number of hw-offloaded routes but also raises CPU usage and vice-versa.
The minimum delay between route processing and its offloading. The delay allows processing more routes together and offloading them at once, saving CPU usage. It also makes offloading the entire routing table faster by reducing the per-route processing work. On the other hand, it slows down the offloading of an individual route.
If an additional route is received during the delay, the latter resets to theroute-index-delay-minvalue.Adding more and more routes within the delay keeps resetting the timer until theroute-index-delay-maxis reached.
The maximum delay between route processing and its offloading. When the maximum delay is reached, the processed routes get offloaded despite more routes pending. However,route-queue-limit-highhas higher priority than this, meaning that the indexing/offloading gets paused anyway when a certain queue size is reached.
Neighbor (host) keepalive interval. When a host (IP neighbor) gets hw-offloaded, all traffic from/to it is routed by the switch chip, and RouterOS may think the neighbor is inactive and delete it. To prevent that, the switch driver must keep the offloaded neighbors alive by sending periodical refreshes to RouterOS.
Unfortunately, switch chips do not provide per-neighbor stats. Hence, the only way to check if the offloaded host is still active is by sending occasional ARP (IPv4) / Neighbor Discovery (IPv6) requests to the connected network. Increasing the value lowers the broadcast traffic but may leave inactive hosts in hardware memory for longer.
Neighbor discovery is triggered within the neighbor keepalive work. Hence, the discovery time is rounded up to the next keepalive session. Choose a value forneigh-discovery-intervalnot dividable byneigh-keepalive-intervalto send ARP/ND requests in various sessions, preventing broadcast bursts.
The maximum number of ARP/ND requests that can be sent at once.
The delay between ARP/ND subsequent bursts if the number of requests exceedsneigh-discovery-burst-limit.
### Monitor
The L3HW Monitor feature has been introduced in RouterOS version 7.10. It allows monitoring of switch chip and driver stats related to L3HW.
```
/interface/ethernet/switch/l3hw-settings/monitor
        ipv4-routes-total: 99363
           ipv4-routes-hw: 61250
          ipv4-routes-cpu: 38112
  ipv4-shortest-hw-prefix: 24
               ipv4-hosts: 87
        ipv6-routes-total: 15
           ipv6-routes-hw: 11
          ipv6-routes-cpu: 4
  ipv6-shortest-hw-prefix: 0
               ipv6-hosts: 7
         route-queue-size: 118
     fasttrack-ipv4-conns: 2031
   fasttrack-hw-min-speed: 0
              nexthop-cap: 8192
            nexthop-usage: 93
    vxlan-mtu-packet-drop: 0
```
Stats
Property | Description
----------------------
ipv4-routes-total | The total number of IPv4 routes handled by the switch driver.
ipv4-routes-hw | The number of hardware-offloaded IPv4 routes (a.k.a. hardware routes)
ipv4-routes-cpu | The number of IPv4 routes redirected to the CPU (a.k.a. software routes)
ipv4-shortest-hw-prefix | Shortest Hardware Prefix (SHWP)for IPv4. If the entire IPv4 routing table does not fit into the hardware memory,partial offloadingis applied, where the longest prefixes are hw-offloaded while the shorter ones are redirected to the CPU. This field shows the shortest route prefix (/x) that is offloaded to the hardware memory. All prefixes shorter than this are processed by the CPU. "ipv4-shortest-hw-prefix=0" means the entire IPv4 routing table is offloaded to the hardware memory.
ipv4-hosts | The number of hardware-offloaded IPv4 hosts (/32 routes)
ipv6-routes-total1 | The total number of IPv6 routes handled by the switch driver.
ipv6-routes-hw1 | The number of hardware-offloaded IPv6 routes (a.k.a. hardware routes)
ipv6-routes-cpu1 | The number of IPv6 routes redirected to the CPU (a.k.a. software routes)
ipv6-shortest-hw-prefix1 | Shortest Hardware Prefix (SHWP)for IPv6. If the entire IPv6 routing table does not fit into the hardware memory,partial offloadingis applied, where the longest prefixes are hw-offloaded while the shorter ones are redirected to the CPU. This field shows the shortest route prefix (/x) that is offloaded to the hardware memory. All prefixes shorter than this are processed by the CPU. "ipv6-shortest-hw-prefix=0" means the entire IPv6 routing table is offloaded to the hardware memory.
ipv6-hosts1 | The number of hardware-offloaded IPv6 hosts (/128 routes)
route-queue-size | The number of routes in the queue for processing by the switch chip driver. Under normal working conditions, this field is 0, meaning that all routes are processed by the driver.
nexthop-cap | The nexthop capacity.
nexthop-usage | The number of currently used nexthops.
vxlan-mtu-packet-drop | The number of dropped VXLAN packets due to exceeded interface MTU settings.
fasttrack-ipv4-conns2 | The number of hardware-offloaded FastTrack connections.
fasttrack-hw-min-speed2 | When the hardware memory for storing FastTrack is full, this field shows the minimum speed (in bytes per second) of a hw-offloaded FastTrack connection. Slower connections are routed by the CPU.
Property
Description
```
ipv4-shortest-hw-prefix=0
```
```
ipv6-shortest-hw-prefix=0
```
1IPv6 stats appear only when IPv6 hardware routing is enabled (ipv6-hw=yes)
```
ipv6-hw=yes
```
2FastTrack stats appear only when hardware offloading of FastTrack connections is enabled (fasttrack-hw=yes)
```
=yes
```
### Advanced Monitor
An enhanced version of Monitor with extra telemetry data for advanced users. Advanced Monitor contains all data from the basic monitorplus the fields listed below.
```
/interface/ethernet/switch/l3hw-settings/advanced> monitor once
        ipv4-routes-total: 29968
           ipv4-routes-hw: 29957
          ipv4-routes-cpu: 11
  ipv4-shortest-hw-prefix: 0
               ipv4-hosts: 3
        ipv6-routes-total: 4
           ipv6-routes-hw: 0
          ipv6-routes-cpu: 4
  ipv6-shortest-hw-prefix: 0
               ipv6-hosts: 0
         route-queue-size: 0
         route-queue-rate: 0
       route-process-rate: 0
     fasttrack-ipv4-conns: 0
     fasttrack-queue-size: 0
     fasttrack-queue-rate: 0
   fasttrack-process-rate: 0
   fasttrack-hw-min-speed: 0
   fasttrack-hw-offloaded: 0
    fasttrack-hw-unloaded: 0
                  lpm-cap: 54560
                lpm-usage: 31931
             lpm-bank-cap: 2728
           lpm-bank-usage: 46,0,0,0,2589,2591,1983,0,2728,2728,2728,2728,2728,2728,2728,2728,2728,170,0,0
                  pbr-cap: 8192
                pbr-usage: 0
             pbr-lpm-bank: 3
                nat-usage: 0
              nexthop-cap: 8192
            nexthop-usage: 85
```
Stats
Property | Description
----------------------
route-queue-rate | The rate at which routes are added to the queue for the switch driver processing. In other words, the growth rate ofroute-queue-size(routes per second)
route-process-rate | The rate at which previously queued routes are processed by the switch driver. In other words, the shrink rate ofroute-queue-size(routes per second)
fasttrack-queue-size | The number of FastTrack connections in the queue for processing by the switch chip driver.
fasttrack-queue-rate | The rate at which FastTrack connections are added to the queue for the switch driver processing. In other words, the growth rate offasttrack-queue-size(connections per second)
fasttrack-process-rate | The rate at which previously queued FastTrack connections are processed by the switch driver. In other words, the shrink rate offasttrack-queue-size(connections per second)
fasttrack-hw-offloaded | The number of FastTrack connections offloaded to the hardware. The counter resets every second (or every monitor interval).
fasttrack-hw-unloaded | The number of FastTrack connections unloaded from the hardware (redirected to software routing). The counter resets every second (or every monitor interval).
lpm-cap | The size of the LPM hardware table (LPM = Longest Prefix Match). LPM stores route indexes for hardware routing. Not every switch chip model uses LPM. Others use TCAM.
lpm-usage | The number of used LPM blocks.lpm-usage/lpm-cap= usage percentage.
lpm-bank-cap | LPM memory is organized in banks - special memory units. The bank size depends on the switch chip model. This value shows the size of a single bank (in LPM blocks).lpm-cap/lpm-bank-cap= the number of banks (usually, 20).
lpm-bank-usage | Per-bank LPM usage (in LPM blocks)
pbr-cap | The size of the Policy-Based Routing (PBR) hardware table. PBR is used for NAT offloading of FastTrack connections.
pbr-usage | The number of used PBR entries.pbr-usage/pbr-cap= usage percentage.
pbr-lpm-bank | PBR shares LPM memory banks with routing tables. This value shows the LPM bank index shared with PBR (0 = the first bank).
nat-usage | The number of used NAT hardware entries (for FastTrack connections).
Property
Description
## Interface Lists
It is impossible to use interface lists directly to controll3-hw-offloadingbecause an interface list may contain virtual interfaces (such as VLAN) while thel3-hw-offloadingsetting must be applied to physical switch ports only. For example, if there are two VLAN interfaces (vlan20 and vlan30) running on the same switch port (trunk port), it is impossible to enable hardware routing on vlan20 but keep it disabled on vlan30.
```
l3-hw-offloading
```
```
l3-hw-offloading
```
However, an interface list may be used as a port selector. The following example demonstrates how to enable hardware routing on LAN ports (ports that belong to the "LAN" interface list) and disable it on WAN ports:
```
:foreach i in=[/interface/list/member/find where list=LAN] do={
    /interface/ethernet/switch/port set [/interface/list/member/get $i interface] l3-hw-offloading=yes
}
:foreach i in=[/interface/list/member/find where list=WAN] do={
    /interface/ethernet/switch/port set [/interface/list/member/get $i interface] l3-hw-offloading=no
}
```
Please take into account that since interface lists are not directly used in hardware routing control.,modifying the interface list also does not automatically reflect in l3hw changes. For instance, adding a switch port to the "LAN" interface list does not automatically enablel3-hw-offloadingon it. The user has to rerun the above script to apply the changes.
```
l3-hw-offloading
```
## MTU
The hardware supports up to 8 MTU profiles, meaning that the user can set up to 8 different MTU values for interfaces: the default 1500 + seven custom ones.
```
/interface/ethernet/switch set 0 l3-hw-offloading=no
/interface set sfp-sfpplus1 mtu=9000 l2mtu=9022
/interface set sfp-sfpplus2 mtu=9000 l2mtu=9022
/interface set sfp-sfpplus3 mtu=10000 l2mtu=10022
/interface/ethernet/switch set 0 l3-hw-offloading=yes
```
## Layer 2 Dependency
Layer 3 hardware processing lies on top of Layer 2 hardware processing. Therefore, L3HW offloading requires L2HW offloading on the underlying interfaces. The latter is enabled by default, but there are some exceptions. For example, CRS3xx devices support only one hardware bridge. If there are multiple bridges, others are processed by the CPU and are not subject to L3HW.
Another example is ACL rules. If a rule redirects traffic to the CPU for software processing, then hardware routing (L3HW) is not triggered:
```
/interface/ethernet/switch/rule/add switch=switch1 ports=ether1 redirect-to-cpu=yes
```
To make sure that Layer 3 is in sync with Layer 2 on both the software and hardware sides, we recommend disabling L3HW while configuring Layer 2 features. The recommendation applies to the following configuration:
* adding/removing/enabling/disabling bridge;
* adding/removing switch ports to/from the bridge;
* bonding switch ports / removing bond;
* changing VLAN settings;
* changing MTU/L2MTU on switch ports;
* changing ethernet (MAC) addresses.
In short, disablel3-hw-offloadingwhile making changes under/interface/bridge/and/interface/vlan/:
```
l3-hw-offloading
```
```
/interface/bridge/
```
```
/interface/vlan/
```
```
/interface/ethernet/switch set 0 l3-hw-offloading=no
/interface/bridge
# put bridge configuration changes here
/interface/vlan
# define/change VLAN interfaces
/interface/ethernet/switch set 0 l3-hw-offloading=yes
```
## MAC telnet
There is a limitation for MAC telnet when L3HW offloading is enabled on98DX8xxx,98DX4xxx,or98DX325xswitch chips. Packets from MAC Telnet are dropped and do not reach the CPU, thus access to the device will fail.
If MAC telnet is desired in combination with L3HW, certain ACL rule can be created to force these packets to the CPU.
For example, if MAC telnet access on sfp-sfpplus1 and sfp-sfpplus2 is needed, you will need to add this ACL rule. It is possible to select even more interfaces with theportssetting.
```
ports
```
```
/interface ethernet switch rule
add dst-port=20561 ports=sfp-sfpplus1,sfp-sfpplus2 protocol=udp redirect-to-cpu=yes switch=switch1
```
## Inter-VLAN Routing
Since L3HW depends on L2HW, and L2HW is the one that does VLAN processing, Inter-VLANhardwarerouting requires a hardware bridge underneath. Even if a particular VLAN has only one tagged port member, the latter must be a bridge member. Do not assign a VLAN interface directly on a switch port! Otherwise, L3HW offloading fails and the traffic will get processed by the CPU:
/interface/vlan add interface=ether2 name=vlan20 vlan-id=20
```
/interface/vlan add interface=ether2 name=vlan20 vlan-id=20
```
Assign the VLAN interface to the bridge instead. This way, VLAN configuration gets offloaded to the hardware, and, with L3HW enabled, the traffic is subject to inter-VLAN hardware routing.
```
/interface/ethernet/switch set 0 l3-hw-offloading=no
/interface/bridge/port add bridge=bridge interface=ether2
/interface/bridge/vlan add bridge=bridge tagged=bridge,ether2 vlan-ids=20
/interface/vlan add interface=bridge name=vlan20 vlan-id=20
/ip/address add address=192.0.2.1/24 interface=vlan20
/interface/bridge set bridge vlan-filtering=yes
/interface/ethernet/switch set 0 l3-hw-offloading=yes
```
## L3HW MAC Address Range Limitation (DX2000/DX3000 series only)
Marvell Prestera DX2000 and DX3000 switch chips have a hardware limitation that allows configuring only the last (least significant) octet of the MAC address for each interface. The other five (most significant) octets are configured globally and, therefore, must be equal for all interfaces (switch ports, bridge, VLANs). In other words, the MAC addresses must be in the format "XX:XX:XX:XX:XX:??", where:
* "XX:XX:XX:XX:XX" part is common for all interfaces.
* "??" is a variable part.
This requirement applies only to Layer 3 (routing).Layer 2 (bridging) does not use the switch's ethernet addresses. Moreover, it does not apply to bridge ports because they use the bridge's MAC address.
The requirement for common five octets applies to:
* Standalone switch ports (not bridge members) with hardware routing enabled (l3-hw-offloading=yes).
* Bridge itself.
* VLAN interfaces (those that use the bridge's MAC address by default).
```
l3-hw-offloading=yes
```
# Route Configuration
## Suppressing HW Offload
By default, all the routes are participating to be hardware candidate routes. To further fine-tune which traffic to offload, there is an option for each route to disable/enablesuppress-hw-offload.
```
suppress-hw-offload
```
For example, if we know that the majority of traffic flows to the network where servers are located, we can enable offloading only to that specific destination:
```
/ip/route set [find where static && dst-address!="192.168.3.0/24"] suppress-hw-offload=yes
```
Now only the route to 192.168.3.0/24 has H-flag, indicating that it will be the only one eligible to be selected for HW offloading:
```
[admin@MikroTik] > /ip/route print where static
Flags: A - ACTIVE; s - STATIC, y - COPY; H - HW-OFFLOADED
Columns: DST-ADDRESS, GATEWAY, DISTANCE
#     DST-ADDRESS       GATEWAY         D
0 As  0.0.0.0/0         172.16.2.1      1
1 As  10.0.0.0/8        10.155.121.254  1
2 AsH 192.168.3.0/24    172.16.2.1      1
```
## Routing Filters
For dynamic routing protocols like OSFP and BGP, it is possible to suppress HW offloading usingrouting filters. For example, to suppress HW offloading on all OSFP instance routes, use "suppress-hw-offload yes" property:
```
suppress-hw-offload yes
```
```
/routing/ospf/instance
set [find name=instance1] in-filter-chain=ospf-input
/routing/filter/rule
add chain="ospf-input" rule="set suppress-hw-offload yes; accept"
```
## Offloading Fasttrack Connections
Firewall filter rules havehw-offloadoption for Fasttrack, allowing fine-tuning connection offloading. Since the hardware memory for Fasttrack connections is very limited, we can choose what type of connections to offload and, therefore, benefit from near-the-wire-speed traffic. The next example offloads only TCP connections while UDP packets are routed via the CPU and do not occupy HW memory:
```
hw-offload
```
```
/ip/firewall/filter
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=yes protocol=tcp
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=no
add action=accept chain=forward connection-state=established,related
```
## Stateless Hardware Firewall
While connection tracking and stateful firewalling can be performed only by the CPU, the hardware can perform stateless firewalling viaswitch rules (ACL). The next example prevents (on a hardware level) accessing a MySQL server from the ether1, and redirects to the CPU/Firewall packets from ether2 and ether3:
```
/interface ethernet switch rule
add switch=switch1 dst-address=10.0.1.2/32 dst-port=3306 ports=ether1 new-dst-ports=""
add switch=switch1 dst-address=10.0.1.2/32 dst-port=3306 ports=ether2,ether3 redirect-to-cpu=yes
```
## Switch Rules (ACL) vs. Fasttrack HW Offloading
Some firewall rules may be implemented both viaswitch rules (ACL)and CPUFirewall Filter+ Fasttrack HW Offloading. Both options grant near-the-wire-speed performance. So the question is which one to use?
First,not all devices support Fasttrack HW Offloading, and without HW offloading, Firewall Filter uses only software routing, which is dramatically slower than its hardware counterpart. Second, even if Fasttrack HW Offloading is an option, a rule of thumb is:
Switch rules share the hardware memory with Fastrack connections. However, hardware resources are allocated for each Fasttrack connection while a single ACL rule can match multiple connections. For example, if you have a guest WiFi network connected to sfp-sfpplus1 VLAN 10 and you don't want it to access your internal network, simply create an ACL rule:
```
/interface/ethernet/switch/rule
add switch=switch1 ports=sfp-sfpplus1 vlan-id=10 dst-address=10.0.0.0/8 new-dst-ports=""
```
The matched packets will be dropped on the hardware level. It is much better than lettingallguest packets to the CPU for Firewall filtering.
Of course, ACL rules cannot match everything. For instance, ACL rules cannot filter connection states: accept established, drop others. That is where Fasttrack HW Offloading gets into action - redirect the packets to the CPU by default for firewall filtering, then offload the established Fasttrack connections. However, disablingl3-hw-offloadingfor the entire switch, port is not the only option.
```
l3-hw-offloading
```
# Configuration Examples
## Inter-VLAN Routing with Upstream Port Behind Firewall/NAT
This example demonstrates how to benefit from near-to-wire-speed inter-VLAN routing while keeping Firewall and NAT running on the upstream port. Moreover, Fasttrack connections to the upstream port get offloaded to hardware as well, boosting the traffic speed close to wire-level. Inter-VLAN traffic is fully routed by the hardware, not entering the CPU/Firewall, and, therefore, not occupying the hardware memory of Fasttrack connections.
We use theCRS317-1G-16S+model with the following setup:
* sfp1-sfp4 - bridged ports, VLAN ID 20, untagged
* sfp5-sfp8 - bridged ports, VLAN ID 30, untagged
* sfp16 - the upstream port
* ether1 - management port
Setup interface lists for easy access:
```
/interface list
add name=LAN
add name=WAN
add name=MGMT 
/interface list member
add interface=sfp-sfpplus1 list=LAN
add interface=sfp-sfpplus2 list=LAN
add interface=sfp-sfpplus3 list=LAN
add interface=sfp-sfpplus4 list=LAN
add interface=sfp-sfpplus5 list=LAN
add interface=sfp-sfpplus6 list=LAN
add interface=sfp-sfpplus7 list=LAN
add interface=sfp-sfpplus8 list=LAN
add interface=sfp-sfpplus16 list=WAN
add interface=ether1 list=MGMT
```
```
/interface bridge
add name=bridge vlan-filtering=yes
/interface bridge port
add bridge=bridge interface=sfp-sfpplus1 pvid=20
add bridge=bridge interface=sfp-sfpplus2 pvid=20
add bridge=bridge interface=sfp-sfpplus3 pvid=20
add bridge=bridge interface=sfp-sfpplus4 pvid=20
add bridge=bridge interface=sfp-sfpplus5 pvid=30
add bridge=bridge interface=sfp-sfpplus6 pvid=30
add bridge=bridge interface=sfp-sfpplus7 pvid=30
add bridge=bridge interface=sfp-sfpplus8 pvid=30
/interface bridge vlan
add bridge=bridge tagged=bridge untagged=sfp-sfpplus1,sfp-sfpplus2,sfp-sfpplus3,sfp-sfpplus4 vlan-ids=20
add bridge=bridge tagged=bridge untagged=sfp-sfpplus5,sfp-sfpplus6,sfp-sfpplus7,sfp-sfpplus8 vlan-ids=30
```
Routing requires dedicated VLAN interfaces. For standard L2 VLAN bridging (without inter-VLAN routing), the next step can be omitted.
```
/interface vlan
add interface=bridge name=vlan20 vlan-id=20
add interface=bridge name=vlan30 vlan-id=30
/ip address
add address=192.168.20.17/24 interface=vlan20 network=192.168.20.0
add address=192.168.30.17/24 interface=vlan30 network=192.168.30.0
```
Configure management and upstream ports, a basic firewall, NAT, and enable hardware offloading of Fasttrack connections:
```
/ip address
add address=192.168.88.1/24 interface=ether1
add address=10.0.0.17/24 interface=sfp-sfpplus16
/ip route
add gateway=10.0.0.1
/ip firewall filter
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=yes
add action=accept chain=forward connection-state=established,related
/ip firewall nat
add action=masquerade chain=srcnat out-interface-list=WAN
```
At this moment, all routing still is performed by the CPU. Enable hardware routing on the switch chip:
```
# Enable full hardware routing on LAN ports
:foreach i in=[/interface/list/member/find where list=LAN] do={ 
    /interface/ethernet/switch/port set [/interface/list/member/get $i interface] l3-hw-offloading=yes 
} 
# Disable full hardware routing on WAN or Management ports
:foreach i in=[/interface/list/member/find where list=WAN or list=MGMT] do={ 
    /interface/ethernet/switch/port set [/interface/list/member/get $i interface] l3-hw-offloading=no 
}
# Activate Layer 3 Hardware Offloading on the switch chip
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```
Results:
* Within the same VLAN (e.g., sfp1-sfp4), traffic is forwarded by the hardware on Layer 2(L2HW).
* Inter-VLAN traffic (e.g. sfp1-sfp5) is routed by the hardware on Layer 3(L3HW).
* Traffic from/to the WAN port gets processed by the CPU/Firewall first. Then Fasttrack connections get offloaded to the hardware(Hardware-Accelerated L4 Stateful Firewall).NAT applies both on CPU- and HW-processed packets.
* Traffic to the management port is protected by the Firewall.
# Typical Misconfiguration
Below are typical user errors in configuring Layer 3 Hardware Offloading.
## VLAN interface on a switch port or bond
```
/interface/vlan
add name=vlan10 vlan-id=10 interface=sfp-sfpplus1
add name=vlan20 vlan-id=20 interface=bond1
```
VLAN interface must be set on the bridge due to Layer 2 Dependency. Otherwise, L3HW will not work. The correct configuration is:
```
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=bond1 frame-types=admit-only-vlan-tagged
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=bridge1,bond1 vlan-ids=20
/interface/vlan
add name=vlan10 vlan-id=10 interface=bridge1
add name=vlan20 vlan-id=20 interface=bridge1
```
## Not adding the bridge interface to /interface/bridge/vlan/
For Inter-VLAN routing, the bridge interface itself needs to be added to the tagged members of the given VLANs. In the next example, Inter-VLAN routing works between VLAN 10 and 11, but packets are NOT routed to VLAN 20.
```
/interface bridge vlan
add bridge=bridge1 vlan-ids=10 tagged=bridge1,sfp-sfpplus1
add bridge=bridge1 vlan-ids=11 tagged=bridge1 untagged=sfp-sfpplus2,sfp-sfpplus3 
add bridge=bridge1 vlan-ids=20 tagged=sfp-sfpplus1 untagged=sfp-sfpplus4,sfp-sfpplus5
```
The above example does not always mean an error. Sometimes, you may want the device to act as a simple L2 switch in some/all VLANs. Just make sure you set such behavior on purpose, not due to a mistake.
## Creating multiple bridges
The devices support only one hardware bridge. If there are multiple bridges created, only one gets hardware offloading. While for L2 that means software forwarding for other bridges, in the case of L3HW, multiple bridges may lead to undefined behavior.
## Using ports that do not belong to the switch
Some devices have two switch chips or the management port directly connected to the CPU. For example,CRS312-4C+8XGhasanether9port connected to a separate switch chip. Trying to add this port to a bridge or involve it in the L3HW setup leads to unexpected results. Leave the management port for management!
```
[admin@crs312] /interface/ethernet/switch> print
Columns: NAME, TYPE, L3-HW-OFFLOADING
# NAME     TYPE              L3-HW-OFFLOADING
0 switch1  Marvell-98DX8212  yes            
1 switch2  Atheros-8227      no   
[admin@crs312] /interface/ethernet/switch> port print
Columns: NAME, SWITCH, L3-HW-OFFLOADING, STORM-RATE
 # NAME         SWITCH   L3-HW-OFFLOADING  STORM-RATE
 0 ether9       switch2                             
 1 ether1       switch1  yes                      100
 2 ether2       switch1  yes                      100
 3 ether3       switch1  yes                      100
 4 ether4       switch1  yes                      100
 5 ether5       switch1  yes                      100
 6 ether6       switch1  yes                      100
 7 ether7       switch1  yes                      100
 8 ether8       switch1  yes                      100
 9 combo1       switch1  yes                      100
10 combo2       switch1  yes                      100
11 combo3       switch1  yes                      100
12 combo4       switch1  yes                      100
13 switch1-cpu  switch1                           100
14 switch2-cpu  switch2
```
## Relying on Fasttrack HW Offloading too much
Since Fasttrack HW Offloading offers near-the-wire-speed performance at zero configuration overhead, the users are tempted to use it as the default solution. However, the number of HW Fasttrack connections is very limited, leaving the other traffic for the CPU. Try using the hardware routing as much as possible, reduce the CPU traffic to the minimum via switch ACL rules, and then fine-tune which Fasttrack connections to offload with firewall filter rules.
## Trying to offload slow-path connections
Using certain configurations (e.g. enabling bridge "use-ip-firewall" setting, creating bridge nat/filter rules) or running specific features like sniffer or torch can disable RouterOSFastPath, which will affect the ability to properly FastTrack and HW offload connections. If HW offloaded Fasttrack is required, make sure that there are no settings that disable the FastPath and verify that connections are getting the "H" flag or use the L3HWmonitorcommand to see the amount of HW offloaded connections.
# L3HW Feature Support
* HW- the feature is supported and offloaded to the hardware.
* CPU- the feature is supported but performed by software (CPU)
* N/A- the feature is not available together with L3HW. Layer 3 hardware offloading must be completely disabled (switchl3-hw-offloading=no) to make this feature work.
* FW- the feature requiresl3-hw-offloading=nofor a givenswitch port. On theswitchlevel,l3-hw-offloading=yes.
```
l3-hw-offloading=no
```
```
l3-hw-offloading
```
```
=no
```
```
l3-hw-offloading=yes
```
Feature | Support | Comments | Release
--------------------------------------
IPv4 Unicast Routing | HW |  | 7.1
IPv6 Unicast Routing | HW | /interface/ethernet/switch/l3hw-settings/set ipv6-hw=yes | 7.6
IPv4 Multicast Routing | CPU |  | 
IPv6 Multicast Routing | CPU |  | 
ECMP | HW | Multipath routing | 7.1
Blackholes | HW | /ip/route add dst-address=10.0.99.0/24 blackhole | 7.1
gateway=<interface_name> | CPU/HW | /ip/route add dst-address=10.0.0.0/24 gateway=ether1This works only for directly connected networks. Since HW does not know how to send ARP requests,CPU sends an ARP request and waits for a reply to find out the DST MAC address on the first received packet of the connection that matches a DST IP address.After DST MAC is determined, HW entry is added and all further packets will be processed by the switch chip. | 7.1
Bridge | HW | Routing from/tohardware-offloaded bridgeinterface. | 7.1
VLAN | HW | Routing between VLAN interfaces that are created on hardware-offloaded bridge interface withvlan-filtering./interface/vlan | 7.1
Bonding | HW | Routing between bonding interfaces./interface/bondingOnly802.3adandbalance-xorbonding modes are hardware offloaded. | 7.1
IPv4 Firewall | FW | Users must choose either HW-accelerated routing or firewall.Firewall rules get processed by the CPU.Fasttrackconnections get offloaded to HW. | 7.1
IPv4 NAT | FW | NAT rules applied to the offloadedFasttrackconnections get processed by HW too. | 7.1
MLAG | N/A |  | 
VRF | N/A | Only themainrouting table gets offloaded. If VRF is used together with L3HW and packets arrive on a switch port withl3-hw-offloading=yes, packets can be incorrectly routed through the main routing table. To avoid this, disable L3HW on needed switch ports or use ACL rules to redirect specific traffic to the CPU. | 
VRRP | N/A |  | 
Controller Bridge and Port Extender | N/A |  | 
VXLAN | CPU |  | 
MTU | HW | The hardware supports up to 8 MTU profiles. | 7.1
QinQ Routing | CPU | Stacked routable VLAN interfaces will lose L3HW offloading, while routable VLAN interfaces created directly on the bridge interface can still use HW offloading. | 
```
/interface/ethernet/switch/l3hw-settings/set ipv6-hw=yes
```
```
/ip/route add dst-address=10.0.99.0/24 blackhole
```
```
/ip/route add dst-address=10.0.0.0/24 gateway=ether1
```
This works only for directly connected networks. Since HW does not know how to send ARP requests,CPU sends an ARP request and waits for a reply to find out the DST MAC address on the first received packet of the connection that matches a DST IP address.After DST MAC is determined, HW entry is added and all further packets will be processed by the switch chip.
Routing between VLAN interfaces that are created on hardware-offloaded bridge interface withvlan-filtering.
```
/interface/vlan
```
Routing between bonding interfaces.
```
/interface/bonding
```
Only802.3adandbalance-xorbonding modes are hardware offloaded.
```
802.3ad
```
```
balance-xor
```
```
l3-hw-offloadin
```
```
g=yes
```
Only the devices listed in the table below support L3 HW Offloading.
# L3HW Device Support
Only the devices listed in the table below support L3 HW Offloading.
## CRS3xx: Switch DX3000 and DX2000 Series
The devices below are based onMarvell98DX224S, 98DX226S, or98DX3236switch chip models.
Below are some important features that these devices are missing when compared to other switch models:
* Fasttrack and NAT connection offloading;
* per-VLAN packet and byte counters.
Model | Switch Chip | Release | IPv4 Route Prefixes1 | IPv6 Route Prefixes2 | Nexthops | ECMP paths per prefix3
---------------------------------------------------------------------------------------------------------------
CRS305-1G-4S+ | 98DX3236 | 7.1 | 13312 | 3328 | 4K | 8
CRS310-1G-5S-4S+ | 98DX226S | 7.1 | 13312 | 3328 | 4K | 8
CRS310-8G+2S+ | 98DX226S | 7.1 | 13312 | 3328 | 4K | 8
CRS318-1Fi-15Fr-2S | 98DX224S | 7.1 | 13312 | 3328 | 4K | 8
CRS318-16P-2S+ | 98DX226S | 7.1 | 13312 | 3328 | 4K | 8
CRS320-8P-8B-4S+RM | 98DX226S | 7.1 | 13312 | 3328 | 4K | 8
CRS326-24G-2S+ | 98DX3236 | 7.1 | 13312 | 3328 | 4K | 8
CRS328-24P-4S+ | 98DX3236 | 7.1 | 13312 | 3328 | 4K | 8
CRS328-4C-20S-4S+ | 98DX3236 | 7.1 | 13312 | 3328 | 4K | 8
1Since the total amount of routes that can be offloaded is limited, prefixes with higher netmask are preferred to be forwarded by hardware (e.g., /32, /30, /29, etc.), any other prefixes that do not fit in the HW table will be processed by the CPU. Directly connected hosts are offloaded as /32 (IPv4) or /128 (IPv6) route prefixes. The number of hosts is also limited by max-neighbor-entries inIP Settings/IPv6 Settings.
2IPv4 and IPv6 routing tables share the same hardware memory.
3If a route has more paths than the hardware ECMP limit (X), only the first X paths get offloaded.
## CRS3xx, CRS5xx: Switch DX8000 and DX4000 Series
The devices below are based onMarvell 98DX8xxx,98DX4xxxswitch chips, or98DX325xmodel.
Model | Switch Chip | Release | IPv4 Routes1 | IPv4 Hosts7 | IPv6 Routes8 | IPv6 Hosts7 | Nexthops | Fasttrackconnections2,3,4 | NAT entries2,5
-----------------------------------------------------------------------------------------------------------------------------------------------
CRS309-1G-8S+ | 98DX8208 | 7.1 | 16K - 36K | 16K | 4K - 6K | 8K | 8K | 4.5K | 3.9K
CRS312-4C+8XG | 98DX8212 | 7.1 | 16K - 36K | 16K | 4K - 6K | 8K | 8K | 2.25K | 2.25K
CRS317-1G-16S+ | 98DX8216 | 7.1 | 120K - 240K | 64K | 30K - 40K | 32K | 8K | 4.5K | 4K
CRS326-24S+2Q+ | 98DX8332 | 7.1 | 16K - 36K | 16K | 4K - 6K | 8K | 8K | 2.25K | 2.25K
CRS326-4C+20G+2Q+ | 98DX8332 | 7.1 | 16K - 36K | 16K | 4K - 6K | 8K | 8K | 2.25K | 2.25K
CRS354-48G-4S+2Q+, CRS354-48P-4S+2Q+ | 98DX32576 | 7.1 | 16K - 36K | 16K | 4K - 6K | 8K | 8K | 2.25K | 2.25K
CRS504-4XQ | 98DX4310 | 7.1 | 60K - 120K | 64K | 15K - 20K | 32K | 8K | 4.5K | 4K
CRS510-8XS-2XQ | 98DX4310 | 7.3 | 60K - 120K | 64K | 15K - 20K | 32K | 8K | 4.5K | 4K
CRS518-16XS-2XQ | 98DX8525 | 7.3 | 60K - 120K | 64K | 15K - 20K | 32K | 8K | 4.5K | 4K
CRS520-4XS-16XQ-RM | 98CX8410 | 7.3 | 120K - 240K | 64K | 30K - 40K | 32K | 8K | 4.5K | 4K
1Depends on the complexity of the routing table. Whole-byte IP prefixes (/8, /16, /24, etc.) occupy less HW space than others (e.g., /22). Starting withRouterOS v7.3, when the Routing HW table gets full, only routes with longer subnet prefixes are offloaded (/30, /29, /28, etc.) while the CPU processes the shorter prefixes. In RouterOS v7.2 and before, Routing HW memory overflow led to undefined behavior. Users can fine-tune what routes to offload via routing filters (for dynamic routes) or suppressing hardware offload of static routes. IPv4 and IPv6 routing tables share the same hardware memory.
2When the HW limit of Fasttrack or NAT entries is reached, other connections will fall back to the CPU. MikroTik's smart connection offload algorithm ensures that the connections with the most traffic are offloaded to the hardware.
3Fasttrack connections share the same HW memory with ACL rules. Depending on the complexity, one ACL rule may occupy the memory of 3-6 Fasttrack connections.
4MPLS shares the HW memory with Fasttrack connections. Moreover, enabling MPLS requires the allocation of the entire memory region, which could otherwise store up to 768 (0.75K) Fasttrack connections. The same applies to the Bridge Port Extender. However, MPLS and BPE may use the same memory region, so enabling them both doesn't double the limitation of Fasttrack connections.
5If a Fasttrack connection requires Network Address Translation, a hardware NAT entry is created. The hardware supports both SRCNAT and DSTNAT.
6The switch chip has a feature set of the DX8000 series.
7DX4000/DX8000 switch chips store directly connected hosts, IPv4 /32, and IPv6 /128 route entries in the FDB table rather than the routing table. The HW memory is shared between regular FDB L2 entries (MAC), IPv4, and IPv6 addresses. The number of hosts is also limited by max-neighbor-entries inIP Settings/IPv6 Settings.
8IPv4 and IPv6 routing tables share the same hardware memory.
## CCR2000
Model | Switch Chip | Release | IPv4 Routes | IPv4 Hosts | IPv6 Routes | IPv6 Hosts | Nexthops | Fasttrackconnections | NAT entries
-----------------------------------------------------------------------------------------------------------------------------------
CCR2116-12G-4S+ | 98DX32551 | 7.1 | 16K - 36K | 16K | 4K - 6K | 8K | 8K | 2.25K | 2.25K
CCR2216-1G-12XS-2XQ | 98DX8525 | 7.1 | 60K - 120K | 64K | 15K - 20K | 32K | 8k | 4.5K | 4K
1The switch chip has a feature set of the DX8000 series.