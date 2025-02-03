---
title: Spanning Tree Protocol
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/21725254/Spanning+Tree+Protocol,
crawled_date: 2025-02-02T21:10:22.248775
section: mikrotik_docs
type: documentation
---

* 1Summary
* 2Monitoring
* 3STP and RSTP3.1Default values3.2Election process3.3Examples3.3.1Root path cost example3.3.2STP example
* 4Multiple Spanning Tree Protocol4.1MSTP Regions4.2Election process4.3MST Instance4.4MST Override4.5Monitoring4.6MSTP example
* 3.1Default values
* 3.2Election process
* 3.3Examples3.3.1Root path cost example3.3.2STP example
* 3.3.1Root path cost example
* 3.3.2STP example
* 4.1MSTP Regions
* 4.2Election process
* 4.3MST Instance
* 4.4MST Override
* 4.5Monitoring
* 4.6MSTP example
# Summary
The purpose of the spanning tree protocol is to provide the ability to create loop-free Layer 2 topologies while having redundant links. While connecting multiple bridges or just cross-connecting bridge ports, it's possible to create network loops that can severely impact the stability of the network. Spanning tree protocol aims to resolve this problem by introducing the concept of the root bridge, all bridges in the same Layer 2 domain will exchange information about the shortest path to the root bridge. Afterward, each bridge will negotiate which ports to use to reach the root bridge. This information exchange is done with the help of Bridge Protocol Data Units (BPDUs). STP will disable certain ports for each bridge to avoid loops, while still ensuring that all bridges can communicate with each other. For an in-depth description of protocol please refer to IEEE 802.1D.
As a best practice, itis always recommended to manually set up each bridge's priority, port priority, and port path cost to ensure proper Layer2 functionality at all times. Leaving STP related values to defaults is acceptable for a network that consists of 1 to 2 bridges running with (R/M)STP enabled, but it is highly recommended to manually set these values for larger networks. Since STP elects a root bridge and root ports by checking STP related values from bridges over the network, then leaving STP settings to automatic may elect an undesired root bridge and root ports and in case of a hardware failure can result in an inaccessible network.
# Monitoring
You can check the STP status of a bridge by using the/interface bridge monitorcommand, for example:
```
/interface bridge monitor
```
```
/interface bridge monitor bridge1
                  state: enabled
    current-mac-address: B8:69:F4:30:19:FE
            root-bridge: no
         root-bridge-id: 0x1000.B8:69:F4:30:19:FD
         root-path-cost: 4000
              root-port: sfp-sfpplus2
             port-count: 2
  designated-port-count: 1
           fast-forward: yes
```
Note that the root bridge doesn't have any root ports, only designated ports.
You can check the STP status of a bridge port by using the/interface bridge port monitorcommand, for example:
```
/interface bridge port monitor
```
```
/interface bridge port monitor [find interface=sfp-sfpplus2]
               interface: sfp-sfpplus2
                  status: in-bridge
             port-number: 1
                    role: root-port
               edge-port: no
     edge-port-discovery: yes
     point-to-point-port: yes
            external-fdb: no
            sending-rstp: yes
                learning: yes
              forwarding: yes
               path-cost: 2000
          root-path-cost: 4000
       designated-bridge: 0x8000.DC:2C:6E:9E:11:1C
         designated-cost: 2000
  designated-port-number: 2
```
Note thatroot-bridge-idconsists of the bridge priority and the bridge's MAC address, for non-root bridges the root bridge will be shown asdesignated-bridge.
```
root-bridge-id
```
```
designated-bridge
```
# STP and RSTP
STP and Rapid STP are used widely across many networks, but almost all networks have switched over to using only RSTP because of its benefits. STP is a very old protocol and has a convergence time (the time needed to fully learn network topology changes and to continue properly forwarding traffic) of up to 50 seconds. RSTP has a lot of smaller convergence time, a few seconds or even a few milliseconds. It is recommended to use RSTP instead of STP since it is a lot faster and is also backward compatible with STP. One of the reasons why RSTP is faster is because of reduced possible port states, below is a list of possible STP port states:
* Forwarding- port participates in traffic forwarding and is learning MAC addresses, and is receiving BPDUs.
* Listening- port does not participate in traffic forwarding and is not learning MAC addresses, is receiving BPDUs.
* Learning- port does not participate in traffic forwarding but is learning MAC addresses.
* Blocking- port is blocked since it is causing loops but is receiving BPDUs.
* Disabled- port is disabled or inactive.
In RSTP the disabled, listening, and blocking port states are replaced with just one state called theDiscardingstate:
* Forwarding- port participates in traffic forwarding and is learning MAC addresses, is receiving BPDUs (forwarding=yes).
* Learning- port does not participate in traffic forwarding but is learning MAC addresses (learning=yes).
* Discarding- port does not participate in traffic forwarding and is not learning MAC addresses, is receiving BPDUs (forwarding=no).
In STP ports are primarily categorized by states (e.g., Forwarding, Listening, Learning, Blocking, Disabled). Port behavior is determined dynamically based on the spanning tree algorithm but without explicitly assigning roles. The logic of forwarding or blocking traffic is derived from the calculation of Root Bridge, Root Ports, and Designated Ports, but these are considered part of the spanning tree topology rather than formalized port roles.RSTP explicitly defined port roles and introduces the concept of backup paths, which are explicitly represented through the Alternate Port and Backup Port roles. These roles did not exist in STP because STP treated blocked ports generically, without distinguishing their function as potential backups.
Here is a breakdown of the port roles for RSTP protocols:
* Root Port- port that is facing towards the root bridge and has the best (lowest cost) path to the root bridge. Only one root port is elected per bridge (except the root bridge itself).
* Designated Port- port that is facing away from the root bridge and forwards traffic away from the root bridge to downstream devices.
* Alternate Port- port that is facing towards the root bridge, but is not going to forward traffic. Port provides a backup path to the root bridge if the current root port fails.
* Backup Port- port that is facing away from the root bridge, but is going to forward traffic. Port that serves as a backup for a designated port on the same segment.
* Disabled Port- disabled or inactive port.
Alternate Port- port that is facing towards the root bridge, but is not going to forward traffic. Port provides a backup path to the root bridge if the current root port fails.
Backup Port- port that is facing away from the root bridge, but is going to forward traffic. Port that serves as a backup for a designated port on the same segment.
Disabled Port- disabled or inactive port.
In STP connectivity between bridges is determined by sending and receiving BPDUs between neighbor bridges. Designated ports are sending BPDUs to root ports. If a BPDU is not received 3 times theHelloTimein a row, then the connection is considered as unavailable and network topology convergence will commence. IT is possible to reduce STP convergence time in certain scenarios by reducing theforward-delaytimer, which is responsible for how long can the port be in the learning/listening state.
```
forward-delay
```
In RouterOS, it is possible to specify which bridge ports are edge ports. Edge ports are ports that are not supposed to receive any BPDUs, this is beneficial since this allows STP to skip the learning and the listening state and directly go to the forwarding state. This feature is sometimes calledPortFast· You can leave this parameter to the default value, which isauto, but you can also manually specify it, you can set a port as an edge port manually for ports that should not have any more bridges behind it, usually these are access ports.
Additionally, bridge portpoint-to-point,specifies if a bridge port is connected to a bridge using a point-to-point link for faster convergence in case of failure. By setting this property toyes, you are forcing the link to be a point-to-point link, which will skip the checking mechanism, which detects and waits for BPDUs from other devices from this single link, by setting this property tono, you are implying that a link can receive BPDUs from multiple devices. By setting the property toyes, you are significantly improving (R/M)STP convergence time. In general, you should only set this property tono,if it is possible that another device can be connected between a link, this is mostly relevant to Wireless mediums and Ethernet hubs. If the Ethernet link is full-duplex,autoenables point-to-point functionality. This property has no effect whenprotocol-modeis set tonone.
```
point-to-point
```
```
yes
```
```
no
```
```
yes
```
```
no
```
```
auto
```
```
protocol-mode
```
```
none
```
## Default values
When creating a bridge or adding a port to the bridge the following are the default values that are assigned by RouterOS:
* Default bridge priority:32768/0x8000
* Default bridge port path cost:based on interface speed
* Default bridge port priority:0x80
* BPDU message age increment:1
* HelloTime:2
* Default max message age:20
The bridge interface settingport-cost-modechanges the portpath-costandinternal-path-costmode for bridged ports, utilizing automatic values based on interface speed. This setting does not impact bridged ports with manually configuredpath-costorinternal-path-costproperties. Below are examples illustrating the path-costs corresponding to specific data rates (with proportionate calculations for intermediate rates):
```
port-cost-mode
```
```
path-cost
```
```
internal-path-cost
```
```
path-cost
```
```
internal-path-cost
```
Data rate | Long | Short
------------------------
10 Mbps | 2,000,000 | 100
100 Mbps | 200,000 | 19
1 Gbps | 20,000 | 4
10 Gbps | 2,000 | 2
25 Gbps | 800 | 1
40 Gbps | 500 | 1
50 Gbps | 400 | 1
100 Gbps | 200 | 1
For bonded interfaces, the highestpath-costamong all bonded member ports is applied, this value remains unaffected by the total link speed of the bonding. For virtual interfaces (such asVLAN, EoIP, VXLAN), as well as wifi, wireless, and 60GHz interfaces, apath-costof 20,000 is assigned for long mode, and 10 for short mode. For dynamically bridged interfaces (e.g. wifi, wireless, PPP, VPLS), thepath-costdefaults to 20,000 for long mode and 10 for short mode. However, this can be manually overridden by the service that dynamically adds interfaces to bridge, for instance, by using the CAPsMANdatapath.bridge-costsetting. RouterOS versions prior to 7.13 does not change port path cost based on the link speed, for 10M, 100M, 1000M, and 10000M link speeds the default path cost value when a port is added to a bridge was always10.
```
path-cost
```
```
path-cost
```
```
path-cost
```
```
datapath.bridge-cost
```
The age of a BPDU is determined by how many bridges have the BPDU passed times the message age since RouterOS uses1as the message age increment, then the BPDU packet can pass as many bridges as specified in themax-message-ageparameter. By default this value is set to20, this means that after the 20th bridge the BPDU packet will be discarded and the next bridge will become a root bridge, note that ifmax-message-age=20is set, then it is hard to predict which ports will be the designated port on the 21st bridge and may result in traffic not being able to be forwarded properly.
```
max-message-age
```
```
max-message-age=20
```
## Election process
To properly configure STP in your network you need to understand the election process and which parameters are involved in which order. In RouterOS, the root bridge will be elected based on the smallest priority and the smallest MAC address in this particular order:
* Bridge priority (lowest)
* Bridge MAC address (lowest)
In RouterOS root ports are elected based on the lowest Root port path cost, lowest bridge identifier, and lowest bridge port ID in this particular order:
* Root port path cost (lowest)
* Bridge identifier (lowest)
* Bridge port ID (lowest)
First, when the device considers which of its ports to elect as the root port, it will check theroot path costseen by its ports. If the root path cost is the same for two or more ports then theBridge identifierof theupstreamdevice will be checked and the port connected to the lowest bridge identifier will become the root port. If the same bridge identifier is seen on two or more ports, thentheBridge port IDoftheupstreamdevice will be checked.
Explanation of attributes:
Root path cost, all bridges have a Root Path Cost. The root bridge has a root path cost of 0. For all other Bridges, it is the sum of the Port Path Costs on the least-cost path to the Root Bridge. You can modify the local port path cost under "/interface bridge port".
```
/interface bridge port
```
The bridge identifier is a combination of "bridge priority" and "bridge MAC", configurable under "/interface bridge"
```
/interface bridge
```
Bridge port ID is a combination of "unique ID" and "bridge port priority", the unique ID is automatically assigned to the bridge port upon adding it to the bridge, it cannot be edited. It can be seen in WinBox under the "Bridge Port" "Port Number" column, or with "/interface bridge port monitor", as "port-number".
```
/interface bridge port monitor
```
```
port-number
```
## Examples
### Root path cost example
This example outlines how the root path cost works. SW1 will be the root bridge, due to it having the lowest priority of 0x1000, as the root bridge. Each bridge will calculate the path cost to the root bridge. When calculating root path cost bridges take into account the configured path cost on their ports + root path cost advertised by neighboring bridges.
SW1: due to it being the root bridge, it advertises a root path cost of 0 to its neighbors, even though it has a configured path cost of 10.
SW2:ether1. has a root path cost of 0 + 25=25. On theether2path cost will be 10+10+10+0=30
SW3:ether2, has a root path cost of 0 + 10=10. On theether4path cost will be 10+5+25+0=40
SW4:ether1, has a root path cost of 0+25+5=30. Onether4path cost will be 10+10+0=20
The Port with the lowest path cost will be elected as the root port. Every bridge in STP topology needs a path to the root bridge, after the best path has been found, the redundant path will be blocked, in this case, the path between SW2 and SW4.
### STP example
In this example, we want to ensure Layer2 redundancy for connections from ServerA to ServerB. If a port is connected to a device that is not a bridge and not running (R)STP, then this port is considered as an edge port, in this case, ServerA and ServerB are connected to an edge port. This is possible by using STP in a network. Below are configuration examples for each switch.
* Configuration for SW1:
```
/interface bridge
add name=bridge priority=0x1000
/interface bridge port
add bridge=bridge interface=ether1 priority=0x60
add bridge=bridge interface=ether2 priority=0x50
add bridge=bridge interface=ether3 priority=0x40
add bridge=bridge interface=ether4 priority=0x30
add bridge=bridge interface=ether5
```
* Configuration for SW2:
```
/interface bridge
add name=bridge priority=0x2000
/interface bridge port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
```
* Configuration for SW3:
```
/interface bridge
add name=bridge priority=0x3000
/interface bridge port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
```
* Configuration for SW4:
```
/interface bridge
add name=bridge priority=0x4000
/interface bridge port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2 path-cost=20
add bridge=bridge interface=ether3
```
In this example,SW1is the root bridge since it has the lowest bridge priority.SW2andSW3have ether1,ether2 connected to the root bridge, and ether3 is connected toSW4. When all switches are working properly, the traffic will be flowing from ServerA through SW1_ether2, through SW2, and through SW4 to ServerB. In the case ofSW1failure, theSW2becomes the root bridge because of the next lowest priority, indicated by the dotted line in the diagram. Below is a list of ports and their role for each switch:
* root-port- SW2_ether2, SW3_ether2, SW4_ether1
* alternate-port- SW2_ether1, SW3_ether1, SW4_ether2
* designated-port- SW1_ether1, SW1_ether2, SW1_ether3, SW1_ether4, SW1_ether5, SW2_ether3, SW2_ether3, SW4_ether3
# Multiple Spanning Tree Protocol
Multiple Spanning Tree Protocol (MSTP) is used on a bridge interface to ensure loop-free topology across multiple VLANs, MSTP can also provide Layer2 redundancy and can be used as a load balancing technique for VLANs since it has the ability to have different paths across different VLANs. MSTP is operating very similarly to (R)STP and many concepts from (R)STP can be applied to MSTP and it is highly recommended to understand the principles behind (R)STP before using MSTP, but there are some differences that must be taken into account when designing an MSTP enabled network.
In case (R)STP is used, the BPDUs are sent across all physical interfaces in a bridge to determine loops and stop ports from being able to forward traffic if it causes a loop. In case there is a loop inside a certain VLAN, (R)STP might not be able to detect it. Some STP variants solve this problem by running an STP instance on every single VLAN (PVST), but this has been proven to be inefficient and some STP variants solve this problem by running a single STP instance across all VLANs (CST), but it lacks the possibility to do load balancing for each VLAN or VLAN group. MSTP tends to solve both problems by using MST instances that can define a group of VLANs (VLAN mapping) that can be used for load balancing and redundancy, this means that each VLAN group can have a different root bridge and a different path. Note that it is beneficial to group multiple VLANs in a single instance to reduce the amount of CPU cycles for each network topology change.
## MSTP Regions
MSTP works in groups called regions, for each region there will be a regional root bridge, and between regions, there will be a root bridge elected. MSTP will use an Internal Spanning Tree (IST) to build the network topology inside a region and a Common Spanning Tree (CST) outside a region to build the network topology between multiple regions, MSTP combines these two protocols into Common and Internal Spanning Tree (CIST), which holds information about topology inside a region and between regions. From CST's perspective, a region will seemingly be as a single virtual bridge, because of this MSTP is considered very scalable for large networks. For bridges to be in the same region, their configuration must match, BPDUs will not include VLAN mappings since they can be large, rather a computed hash is being transmitted. If a bridge receives a BPDU through a port and the configuration does not match, then MSTP will consider that port as a boundary port and that it can be used to reach other regions. Below is a list of parameters that need to match for MSTP to consider a BPDU from the same region:
* Region name
* Region revision
* VLAN mappings to MST Instance IDs (computed hash)
It is possible to create MSTP enabled network without regions, though to be able to do load balancing per VLAN group it is required for a bridge to receive a BPDU from a bridge that is connected to it with the same parameters mentioned above. In RouterOS the default region name is empty and the region revision is 0, which are valid values, but you must make sure that they match to get multiple bridges in a single MSTP region. A region cannot exist if its bridges are scattered over the network, these bridges must be connected at least in one way, in which they can send and receive BPDUs without leaving the region, for example, if a bridge with different region related parameters is between two bridges that have the same region related parameters, then there will exist at least 3 different MSTP regions.
The downside of running every single bridge in a single MSTP region is the excess CPU cycles. In comparison, PVST(+) creates a Spanning Tree Instance for each VLAN ID that exists on the network, since there will be very limited paths that can exist in a network, then this approach creates a lot of overhead and unnecessary CPU cycles, this also means that this approach does not scale very well and can overload switches with not very powerful CPUs. MSTP solves this problem by dividing the network into MSTP regions, where each bridge inside this region will exchange and process information about VLANs that exist inside the same region, but will run a single instance of Spanning Tree Protocol in the background to maintain the network topology between regions. This approach has been proven to be much more effective and much more scalable, this means that regions should be used for larger networks to reduce CPU cycles.
In regions, you can define MST Instances, which are used to configure load balancing per VLAN group and to elect the regional root bridge. It is worth mentioning that in each region there exists a pre-defined MST Instance, in most documentations, this is called asMSTI0· This MST Instance is considered as the default MST Instance, there are certain parameters that apply to this special MST Instance. When traffic passes through an MSTP enabled bridge, MSTP will look for an MST Instance that has a matching VLAN mapping, but if a VLAN mapping does not exist for a certain VLAN ID, then traffic will fall underMSTI0.
## Election process
The election process in MSTP can be divided into two sections, intra-region and inter-region. For MSTP to work properly there will always need to be a regional root, that is the root bridge inside a region, and a CIST root, that is the root bridge between regions. A regional root is the root bridge inside a region, regional root bridge will be needed to properly set up load balancing for VLAN groups inside a region. CIST root will be used to configure which ports will be alternate/backup ports (inactive) and which ports will be root ports (active).
* The following parameters are involved in electing a regional root bridge or root ports inside a MSTP region:
Property | Description
----------------------
priority(integer: 0..65535 decimal format or 0x0000-0xffff hex format; Default:32768 / 0x8000) | /interface bridge msti, MST Instance priority, used to elect a regional root inside an MSTP region.
internal-path-cost(integer: 1..200000000; Default: ) | /interface bridge port, path cost to the regional root for unknown VLAN IDs (MSTI0), used on a root port inside an MSTP region.
priority(integer: 0..240; Default:128) | /interface bridge port mst-override, MST port priority for a defined MST Instance, used on a bridge port on the regional root bridge.
internal-path-cost(integer: 1..200000000; Default: ) | /interface bridge port mst-override, MST port path cost for a defined MST Instance, used on a non-root bridge port inside an MSTP region.
* The following parameters are involved in electing a CIST root bridge or CIST root ports:
Property | Description
----------------------
priority(integer: 0..65535 decimal format or 0x0000-0xffff hex format; Default:32768 / 0x8000) | /interface bridge, CIST bridge priority, used to elect a CIST root bridge.
priority(integer: 0..240; Default:128) | /interface bridge port, CIST port priority, used on a CIST root bridge to elect CIST root ports.
path-cost(integer: 1..200000000; Default: ) | /interface bridge port, CIST port path cost, used on a CIST non-root bridge port to elect CIST root ports.
## MST Instance
Sub-menu:/interface bridge msti
```
/interface bridge msti
```
This section is used to group multiple VLAN IDs into a single instance to create a different root bridge for each VLAN group inside an MSTP region.
Property | Description
----------------------
bridge(text; Default: ) | Bridge to which assigns an MST instance.
identifier(integer: 1..31; Default: ) | MST instance identifier.
priority(integer: 0..65535 decimal format or 0x0000-0xffff hex format; Default:32768 / 0x8000) | MST instance priority, is used to determine the root bridge for a group of VLANs in an MSTP region.
vlan-mapping(integer: 1..4094; Default: ) | The list of VLAN IDs to assign to MST instance. This setting accepts the VLAN ID range, as well as comma, separated values. E.g.vlan-mapping=100-115,120,122,128-130
```
vlan-mapping=100-115,120,122,128-130
```
## MST Override
Sub-menu:/interface bridge port mst-override
```
/interface bridge port mst-override
```
This section is used to select the desired path for each VLAN mapping inside an MSTP region.
Property | Description
----------------------
disabled(yes | no; Default:no) | Whether the entry is disabled.
internal-path-cost(integer: 1..200000000; Default: ) | Path cost for an MST instance's VLAN mapping, used on VLANs that are facing towards the root bridge to manipulate path selection, lower path cost is preferred.
identifier(integer: 1..31; Default: ) | MST instance identifier.
priority(integer: 0..240; Default:128) | The priority of an MST instance's VLAN, used on VLANs that are facing away from the root bridge to manipulate path selection, lower priority is preferred.
interface(name; Default: ) | Name of the port on which use configured MST instance's VLAN mappings and defined path cost and priority.
## Monitoring
Similarly to (R)STP, it is also possible to monitor MSTP status. By monitoring the bridge interface itself it is possible to see the current CIST root bridge and the current regional root bridge for MSTI0, it is also possible to see the computed hash of MST Instance identifiers and VLAN mappings, this is useful when making sure that certain bridges are in the same MSTP region. Below you can find an example of monitoring an MSTP bridge:
```
/interface bridge monitor bridge
                    state: enabled
      current-mac-address: 6C:3B:6B:7B:F0:AA
              root-bridge: no
           root-bridge-id: 0x1000.64:D1:54:24:23:72
  regional-root-bridge-id: 0x4000.6C:3B:6B:7B:F0:AA
           root-path-cost: 10
                root-port: ether4
               port-count: 5
    designated-port-count: 3
        mst-config-digest: 74edbeefdbf82cf63a70cf60e43a56f3
```
In MSTP it is possible to monitor the MST Instance, this is useful to determine the current regional root bridge for a certain MST Instance and VLAN group, below you can find an example to monitor an MST Instance:
```
/interface bridge msti monitor 1
                    state: enabled
               identifier: 2
      current-mac-address: 6C:3B:6B:7B:F0:AA
              root-bridge: no
           root-bridge-id: 0.00:00:00:00:00:00
  regional-root-bridge-id: 0x1002.6C:3B:6B:7B:F9:08
           root-path-cost: 0
                root-port: ether2
               port-count: 5
    designated-port-count: 1
```
It is also possible to monitor a certain MST Override entry, this is useful to determine the port role for a certain MST Instance when configuring root ports and alternate/backup ports in an MSTP region, below you can find an example to monitor an MST Override entry:
```
/interface bridge port mst-override monitor 1
                      port: ether3
                    status: active
                identifier: 2
                      role: alternate-port
                  learning: no
                forwarding: no
   internal-root-path-cost: 15
         designated-bridge: 0x1002.6C:3B:6B:7B:F9:08
  designated-internal-cost: 0
    designated-port-number: 130
```
## MSTP example
Let's say that we need to design topology and configure MSTP in a way that VLAN 10,20 will be forwarded in one path, but VLAN 30,40 will be forwarded in a different path, while all other VLAN IDs will be forwarded in one of those paths. This can easily be done by setting up MST Instances and assigning port path costs, below you can find a network topology that needs to do load balancing per VLAN group with 3 separate regions as an example:
The topology of an MSTP-enabled network with load balancing per VLAN group
Start by adding each interface to a bridge, initially, you should create a (R)STP bridge without VLAN filtering enabled, this is to prevent losing access to the CPU. Each device in this example is named by the region that it is in (Rx) and a device number (_x). For larger networks configuring MSTP can be confusing because of the number of links and devices, we recommend usingThe Dudeto monitor and design a network topology.
* Use the following commands onR1_1,R1_3,R2_1,R2_3,R3_1,R3_3:
```
/interface bridge
add name=bridge protocol-mode=rstp vlan-filtering=no
/interface bridge port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
add bridge=bridge interface=ether4
```
* Use the following commands onR1_2,R2_2,R3_2:
```
/interface bridge
add name=bridge protocol-mode=rstp vlan-filtering=no
/interface bridge port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
```
* Make sure you allow the required VLAN IDs on these devices, here we will consider that each device will receive tagged traffic that needs to be load balanced per VLAN group, use these commands onR1_1,R1_3,R2_1,R2_3,R3_1,R3_3:
```
/interface bridge vlan
add bridge=bridge tagged=ether1,ether2,ether3,ether4 vlan-ids=10,20,30,40
```
* Use the following commands onR1_2,R2_2,R3_2:
```
/interface bridge vlan
add bridge=bridge tagged=ether1,ether2 vlan-ids=10,20,30,40
```
We need to assign a region name for each bridge that we want to be in a single MSTP region, you can also specify the region revision, but it is optional, though they need to match. In this example, if all bridges will have the same region name, then they will all be in a single MSTP bridge. In this case, we want to separate a group of 3 bridges in a different MSTP region to do load balancing per VLAN group and to create diversity and scalability.
* Set the appropriate region name (and region revision) for each bridge, and use the following commands on each device (change the region name!):
```
/interface bridge
set bridge region-name=Rx region-revision=1
```
After we have created 3 different MSTP regions, we need to decide which device is going to be a regional root for each VLAN group. For consistency, we are going to set the first device (_1) in each region as the regional root for VLAN 10,20 and the third device (_3) in each region as the regional root for VLAN 30,40. This can be done by creating an MST Instance for each VLAN group and assigning a bridge priority to it. The MST Instance identifier is only relevant inside an MSTP region, outside an MSTP region these identifiers can be different and mapped to a different VLAN group.
* Use the following commands onR1_1,R2_1,R3_1:
```
/interface bridge msti
add bridge=bridge identifier=1 priority=0x1000 vlan-mapping=10,20
add bridge=bridge identifier=2 priority=0x3000 vlan-mapping=30,40
```
* Use the following commands onR1_3,R2_3,R3_3:
```
/interface bridge msti
add bridge=bridge identifier=1 priority=0x3000 vlan-mapping=10,20
add bridge=bridge identifier=2 priority=0x1000 vlan-mapping=30,40
```
* Use the following commands onR1_2,R2_2,R3_2:
```
/interface bridge msti
add bridge=bridge identifier=1 priority=0x2000 vlan-mapping=10,20
add bridge=bridge identifier=2 priority=0x2000 vlan-mapping=30,40
```
Now we need to override the portpath-costand/or port priority for each MST Instance. This can be done by adding an MST-Override entry for each port and each MST Instance. To achieve that for a certain MST Instance the traffic flow path is different, we simply need to make sure that the port path cost and/or priority is larger. We can either increase the port path cost or decrease the port path cost to ports that are facing toward the regional root bridge. It doesn't matter if you increase or decrease all values, it is important that in the end, one port's path cost is larger than the other's.
```
path-cost
```
* Use the following commands onR1_1,R2_1,R3_1:
```
/interface bridge port mst-override
add identifier=2 interface=ether1 internal-path-cost=5
add identifier=2 interface=ether2 internal-path-cost=15
```
* Use the following commands onR1_2,R2_2,R3_2:
```
/interface bridge port mst-override
add identifier=1 interface=ether1 internal-path-cost=5
add identifier=2 interface=ether2 internal-path-cost=9
```
* Use the following commands onR1_3,R2_3,R3_3:
```
/interface bridge port mst-override
add identifier=1 interface=ether2 internal-path-cost=5
add identifier=1 interface=ether3 internal-path-cost=9
```
In this case for VLAN 10,20 to reach the third device from the first device, it would choose between ether1 and ether2, one port will be blocked and set as an alternate port, and ether1 will have path cost as5+9=14and ether2 will have path cost as10, ether2 will be elected as the root port for MSTI1 on the third device. In case for VLAN 30,40 to reach the first device from the third device, ether1 will have path cost as5+9=14and ether2 will have path cost as15, ether1 will be elected as the root port for MSTI2 on the third device.
```
5+9=14
```
```
10
```
```
5+9=14
```
```
15
```
Now we can configure the root ports forMSTI0, which will fall under all VLANs that are not assigned to a specific MST Instance, like in our example VLAN 10,20, and VLAN 30,40. To configure this special MST Instance, you will need to specifyinternal-path-costto a bridge port. This value is only relevant to MSTP regions, it does not have any effect outside an MSTP region. In this example will choose that all unknown VLANs will be forwarded over the same path as VLAN 30,40, we will simply increase the path cost on one of the ports.
```
internal-path-cost
```
* Use the following commands onR1_3,R2_3,R3_3:
```
/interface bridge port
set [find where interface=ether3] internal-path-cost=25
```
At this point, a single region MSTP can be considered as configured, and in general, MSTP is fully functional. It is highly recommended to configure the CIST part, but for testing purposes, it can be left with the default values. Before doing any tests, you need to enable MSTP on all bridges.
* Use the following commands onalldevices:
```
/interface bridge
set bridge protocol-mode=mstp vlan-filtering=yes
```
When MSTP regions have been configured, you can check if they are properly configured by forwarding traffic, for example, send tagged traffic from the first device to the third device and change the VLAN ID for the tagged traffic to observe different paths based on VLAN ID. When this is working as expected, then you can continue to configure CIST related parameters to elect a CIST root bridge and CIST root ports. For consistency we will choose the first device in the first region to be the CIST root bridge and to ensure consistency in case of failure we can set a higher priority to all other bridges.
* Use the following commands onR1_1:
```
/interface bridge
set bridge priority=0x1000
```
* Use the following commands onR1_2:
```
/interface bridge
set bridge priority=0x2000
```
* ...
* Use the following commands onR3_3:
```
/interface bridge
set bridge priority=0x9000
```
We also need to elect a root port on each bridge, for simplicity we will choose the port that is closest toŖ1_1as the root port and has the least hops. At this point, the procedure to elect root ports is the same as the procedure in (R)STP.
* Use the following commands onR3_3:
```
/interface bridge port
set [find where interface=ether2] path-cost=30
set [find where interface=ether3] path-cost=40
set [find where interface=ether4] path-cost=20
```
* Use the following commands onR1_3andR2_3:
Use the following commands onR1_3andR2_3:
```
/interface bridge port
set [find where interface=ether2] path-cost=20
set [find where interface=ether3] path-cost=30
```
* Use the following commands onR1_2:
```
/interface bridge port
set [find where interface=ether1] path-cost=30
```