# Document Information
Title: Quality of Service
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/189497483/Quality+of+Service,

# Content
# Overview
This document definesQuality of Service (QoS)usage in RouterOS based onMarvell Prestera DX switch chips(CRS3xx, CRS5xx series switches, and CCR2116, CCR2216 routers).
QoS is a set of features in network switches that allow network administrators to prioritize traffic and allocate network resources to ensure that important data flows smoothly and with low latency.
The primary function of QoS in network switches is to manage network traffic in a way that meets the specific requirements of different types of network applications. For example, voice and video data require low latency and minimal packet loss to ensure high-quality communication, while file transfers and other data applications can tolerate higher levels of latency and packet loss.
QoS works by identifying the type of traffic flowing through the switch and assigning it a priority level based on its requirements. The switch can then use this information to alter packet headers and prioritize the flow of traffic, ensuring that higher-priority traffic is given preferential treatment over lower-priority traffic.
RouterOS v7.15+ is required to support all QoS features:
# QoS Terminology
These terms will be used throughout the article.
```
/in/eth/sw/
```
```
/interface/ethernet/switch/
```
# QoS Device Support
Model | Switch Chip | QoS Profiles | QoS Maps | Tx Managers | WRED | ECN | PFC Profiles3 | Port/Queue Usage Stats
-----------------------------------------------------------------------------------------------------------------
CCR2116-12G-4S+ | 98DX3255 | 1024 | 12 | 15 | ✔ | ✔ | 8 | Unreliable1
CCR2216-1G-12XS-2XQ | 98DX8525 | 1024 | 12 | 15 | ✔ | ✔ | 8 | Max fill2
CRS305-1G-4S+ | 98DX3236 | 128 | 1 | 8 |  |  | - | Current values
CRS309-1G-8S+ | 98DX8208 | 1024 | 12 | 15 | ✔ | ✔ | 8 | Unreliable
CRS310-1G-5S-4S+ | 98DX226S | 128 | 1 | 8 |  |  | - | Current values
CRS312-4C+8XG | 98DX8212 | 1024 | 12 | 15 | ✔ | ✔ | 8 | Unreliable
CRS317-1G-16S+ | 98DX8216 | 1024 | 12 | 15 | ✔ | ✔ | 8 | Unreliable
CRS318-1Fi-15Fr-2S | 98DX224S | 128 | 1 | 8 |  |  | - | Current values
CRS318-16P-2S+ | 98DX226S | 128 | 1 | 8 |  |  | - | Current values
CRS326-24G-2S+ | 98DX3236 | 128 | 1 | 8 |  |  | - | Current values
CRS326-24S+2Q+ | 98DX8332 | 1024 | 12 | 15 | ✔ | ✔ | 8 | Unreliable
CRS328-24P-4S+ | 98DX3236 | 128 | 1 | 8 |  |  | - | Current values
CRS328-4C-20S-4S+ | 98DX3236 | 128 | 1 | 8 |  |  | - | Current values
CRS354-48G-4S+2Q+, CRS354-48P-4S+2Q+ | 98DX3257 | 1024 | 12 | 15 | ✔ | ✔ | 85 | Unreliable
CRS504-4XQ | 98DX4310 | 1024 | 12 | 15 | ✔ | ✔ | 8 | Max fill
CRS510-8XS-2XQ | 98DX4310 | 1024 | 12 | 15 | ✔ | ✔ | 8 | Max fill
CRS518-16XS-2XQ | 98DX8525 | 1024 | 12 | 15 | ✔ | ✔ | 8 | Max fill
CRS520-4XS-16XQ | 98CX8410 | 1024 | 12 | 15 | ✔ | ✔ | 85 | Unavailable4
1Due to hardware limitations, some switch chip models may break traffic flow while accessing QoS port/queue usage data.
2The device gathers max queue fill statistics instead of displaying the current usage values. Use thereset-counterscommand to reset those stats.
3The devices without PFC profiles do not support Priority-based Flow Control.
4Usage data for individual queues on a port are unavailable, only the total usage for the entire port can be accessed.
5Due to hardware limitations, PFC settings cannot be configured on certain switch ports. ForCRS354series models, PFC is not supported on portsether37toether48. For theCRS520-4XS-16XQmodel, PFC is not supported on portsqsfp28-4-1toqsfp28-7-4.
# Applications and Usage Examples
# Basic Configuration Example
In this example, we define just one QoS level - VoIP (IP Telephony) on top of the standard "Best Effort" class. Let's imagine that we have a CRS326-24G-2S+ device where:
First, we need to define QoS profiles. Defineddscpandpcpvalues that will be used in forwarded packets on egress:
```
dscp
```
```
pcp
```
```
/interface ethernet switch qos profile
add dscp=46 name=voip pcp=5 traffic-class=5
```
Port-based QoS profile assignment on dedicated ports for IP phones applies to ingress traffic. Other Ethernet ports will use the defaultprofile(wheredscp=0andpcp=0):
```
profile
```
```
dscp=0
```
```
pcp=0
```
```
/interface ethernet switch qos port
set ether1 profile=voip
set ether2 profile=voip
set ether3 profile=voip
set ether4 profile=voip
set ether5 profile=voip
set ether6 profile=voip
set ether7 profile=voip
set ether8 profile=voip
set ether9 profile=voip
```
The trunk port receives both types of QoS traffic. We need to create VLAN priority mapping with the QoS profile and enabletrust-l2to differentiate them:
```
trust-l2
```
```
/interface ethernet switch qos map vlan
add pcp=5 profile=voip
/interface ethernet switch qos port
set sfp-sfpplus1 trust-l2=trust
```
Finally, enable QoS hardware offloading for the above settings to start working:
```
/interface ethernet switch
set switch1 qos-hw-offloading=yes
```
It is possible to verify the port QoS settings withprintcommand:
```
print
```
```
[admin@MikroTik] /interface/ethernet/switch/qos/port print
Columns: NAME, SWITCH, PROFILE, MAP, TRUST-L2, TRUST-L3
# NAME          SWITCH   PROFILE  MAP      TRUST-L2  TRUST-L3  TX-MANAGER
0 ether1        switch1  voip     default  ignore    ignore    default
1 ether2        switch1  voip     default  ignore    ignore    default
2 ether3        switch1  voip     default  ignore    ignore    default
3 ether4        switch1  voip     default  ignore    ignore    default
4 ether5        switch1  voip     default  ignore    ignore    default
5 ether6        switch1  voip     default  ignore    ignore    default
6 ether7        switch1  voip     default  ignore    ignore    default
7 ether8        switch1  voip     default  ignore    ignore    default
8 ether9        switch1  voip     default  ignore    ignore    default
9 ether10       switch1  default  default  ignore    ignore    default
10 ether11       switch1  default  default  ignore    ignore    default
11 ether12       switch1  default  default  ignore    ignore    default
12 ether13       switch1  default  default  ignore    ignore    default
13 ether14       switch1  default  default  ignore    ignore    default
14 ether15       switch1  default  default  ignore    ignore    default
15 ether16       switch1  default  default  ignore    ignore    default
16 ether17       switch1  default  default  ignore    ignore    default
17 ether18       switch1  default  default  ignore    ignore    default
18 ether19       switch1  default  default  ignore    ignore    default
19 ether20       switch1  default  default  ignore    ignore    default
20 ether21       switch1  default  default  ignore    ignore    default
21 ether22       switch1  default  default  ignore    ignore    default
22 ether23       switch1  default  default  ignore    ignore    default
23 ether24       switch1  default  default  ignore    ignore    default
24 sfp-sfpplus1  switch1  default  default  trust     ignore    default
25 sfp-sfpplus2  switch1  default  default  ignore    ignore    default
26 switch1-cpu   switch1
```
Now incoming packets on ports ether1-ether9 are marked with a Priority Code Point (PCP) value of 5 and a Differentiated Services Code Point (DSCP) value of 46, and incoming packets on ports ether10-ether24 are marked with PCP and DSCP values of 0. When packets are incoming to sfp-sfpplus1 port, any packets with a PCP value of 5 will retain their PCP value of 5 and DSCP value of 46, while all other packets will be marked with PCP and DSCP values of 0.
# Dante
Starting from RouterOS v7.15, allMikroTik QoS-Capable devicescomply with Dante.
Dante hardware use the following DSCP / Diffserv priority values for traffic prioritization.
Dante Priority | Usage | DSCP Label | DSCP Value
------------------------------------------------
High | Time critical PTP events | CS7 | 56
Medium | Audio, PTP | EF | 46
Low | (reserved) | CS1 | 8
None | Other traffic | BE | 0
The example assumes that the switch is using itsdefault configuration, which includes a default "bridge" interface and all Ethernet interfaces added as bridge ports, and any of these interfaces could be used for Dante.
First, create QoS Profiles to match Dante traffic classes, there is already a pre-existing "default" profile that corresponds to Dante's None priority.
```
/interface/ethernet/switch/qos/profile
add name=dante-ptp dscp=56 pcp=7 traffic-class=7
add name=dante-audio dscp=46 pcp=5 traffic-class=5
add name=dante-low dscp=8 pcp=1 traffic-class=0
```
Then, create a QoS mapping to match QoS profiles based on DSCP values.
```
/interface/ethernet/switch/qos/map/ip
add dscp=56 profile=dante-ptp
add dscp=46 profile=dante-audio
add dscp=8 profile=dante-low
```
Configure hardware queues to enforce QoS on Dante traffic.
```
/interface/ethernet/switch/qos/tx-manager/queue
set [find where traffic-class>=2] schedule=strict-priority
set [find where traffic-class<2] schedule=low-priority-group weight=1
```
Dante's High and Medium priority traffic is scheduled in strict order. The devices transmits time-critical PTP packets until queue7 gets empty, then proceed with audio (queue5). Low and other traffic gets transmitted only when PTP and audio queues are empty. Since Dante does not define priority order between Low and Other traffic (usually, CS1 has lower priority than Best Effort), and the Low traffic class is reserved for future use anyway, we treat both traffic types equally by putting both into the same group with the same weight. Feel free to change the CS1/BE traffic scheduling according to the requirements if some Dante hardware in your network uses the low-priority traffic class.
The next step is to enable trust mode for incoming Layer3 packets (IP DSCP field):
```
/interface/ethernet/switch/qos/port
set [find] trust-l3=keep
```
Finally, enable QoS hardware offloading for the above settings to start working:
```
/interface ethernet switch
set switch1 qos-hw-offloading=yes
```
When using Dante in multicast mode, it is beneficial to enable IGMP snooping on the switch. This feature directs traffic only to ports with subscribed devices, preventing unnecessary flooding. Additionally, enabling an IGMP querier (if not already enabled on another device in the same LAN), adjusting query intervals, and activating fast-leave can further optimize multicast performance.
```
/interface/bridge
set [find name=bridge] igmp-snooping=yes multicast-querier=yes query-interval=60s
/interface/bridge/port
set [find] fast-leave=yes
```
# RDMA over Converged Ethernet (RoCE)
RoCE allows you to directly access memory on remote storage systems using Ethernet networks without involving the host CPU. This capability significantly reduces latency and CPU overhead, making RoCE ideal for high-performance computing and data center environments. RoCE also enables a converged network, where various services (such as data storage, networking, and multimedia) run over a single Ethernet infrastructure. This simplifies network management and reduces the cost and complexity of maintaining separate networks.
RoCE achieves this through the use ofECNandPFCmechanisms. These features help prevent network congestion and packet loss, ensuring reliable, lossless communication. See thedevice feature tablefor compatible switches. Although switches can support RoCE environments, the end hosts must also be compatible with the RoCE protocol and equipped with RDMA-capable network interface cards (NICs).
There are two main versions of RoCE. RoCEv1 operates as an Ethernet link layer protocol and uses Ethertype 0x8915. RoCEv2 works over standard IP networks, using UDP destination port number 4791. ECN bits in the IP header are marked to signal network congestion, and a Congestion Notification Packet (CNP) is used to acknowledge congestion to the sender. For traffic prioritization, DSCP 26 is used for RoCEv2 traffic, while DSCP 48 for CNPs.
The following example can be used for lossless RoCEv2 with PFC and ECN and it assumes that the switch is using itsdefault configuration, which includes a default "bridge" interface and all Ethernet interfaces added as bridge ports. The minimal recommended RouterOS version is 7.17.
First, configure additional profiles. Non-RoCE traffic will be assigned to already existing "default" profile with traffic-class 1, RoCEv2 to traffic-class 3, and CNP to traffic-class 6.
```
/interface ethernet switch qos profile
add name=roce traffic-class=3
add name=cnp traffic-class=6
```
Create a QoS mapping to match QoS profiles based on DSCP values.
```
/interface ethernet switch qos map ip
add dscp=26 profile=roce
add dscp=48 profile=cnp
```
Configure hardware queues and scheduler. We are using ETS (schedule=high-priority-group) for traffic-class 1 and traffic-class 3 with 50% bandwith assigment each (weight=1), and strict priority scheduling for traffic-class 6. Additionally, configure a separate shared memory pool (shared-pool-index=1) for lossless traffic in traffic-class 3 and enable ECN (ecn=yes) to mark IP packets in the switch that experience congestion.
```
schedule=high-priority-group
```
```
weight=1
```
```
shared-pool-index=1
```
```
ecn=yes
```
```
/interface ethernet switch qos tx-manager queue
set 1 schedule=high-priority-group weight=1
set 3 schedule=high-priority-group weight=1 shared-pool-index=1 ecn=yes
set 6 schedule=strict-priority
```
Configure PFC profile for traffic-class 3 to ensure a lossless environment for RoCEv2 traffic.
```
/interface ethernet switch qos priority-flow-control
add name=pfc-tc3 rx=yes traffic-class=3 tx=yes
```
Set Layer3 trust mode (trust-l3=keep) on switch ports where RoCEv2 traffic is expected, set PFC (pfc=pfc-tc3) and egress-rate for queue3 to comply with PFC requirements (egress-rate-queue3=10.0Gbps). In this example, 10Gbps SFP+ interfaces are used, and the egress rate can be set to match the physical speed of the interface. Change this property depending on your interface speeds.
```
trust-l3=keep
```
```
pfc=pfc-tc3
```
```
egress-rate-queue3=10.0Gbps
```
```
/interface ethernet switch qos port
set sfp-sfpplus1 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus2 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus3 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus4 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
```
Enable QoS hardware offloading for the above settings to start working.
```
/interface ethernet switch
set switch1 qos-hw-offloading=yes
```
Enable theLLDP Data Center Bridging Capability Exchange Protocol (DCBX)to share QoS settings and capabilities with other neighboring devices.
```
/ip neighbor discovery-settings
set lldp-dcbx=yes
```
As an optional step, increase the L2MTU to accommodate larger data packets.
```
/interface ethernet
set [find switch=switch1] l2mtu=9500
```
# QoS Marking
# Understanding Map ranges
In order to avoid defining all possible PCP and DSCP mappings, RouterOS allows setting multiple values and ranges for PCP and DSCP values for QoS Profile mapping.
In the following example, PCP values 0 and 2 use the default QoS profile, 1, 3-4 - streaming, 5 - voip, and 6-7 - control.
```
/interface ethernet switch qos map vlan
add pcp=1,3-4 profile=streaming
add pcp=5 profile=voip
add pcp=6-7 profile=control
```
# Understanding Port, Profile, and Map relation
Each switch port has Layer2 and Layer3 trust settings that will change how ingress packets are classified into QoS profiles and what PCP and DSCP values will be used. Below are tables that describe all possible options:
qos-trust-l2 | qos-trust-l3 | Behavior
--------------------------------------
ignore | ignore | The port is considered untrusted. Both headers are ignored, and the port'sprofileis forced to all ingress packets. This is the default setting.
ignore | trust | Trust the Layer 3 header. Use the DSCP field from the IP header of ingress packets for QoS profile lookup (see/in/eth/sw/qos/map/ip). If the lookup fails (no QoS profiles are mapped to the given DSCP value), thedefaultQoS profile is used (not the switch port's QoS profile). The switch port'sprofilefield is used only for non-IP traffic.
ignore | keep | Trust the Layer 3 header. Use the DSCP field from the IP header of ingress packets for QoS profile lookup (see/in/eth/sw/qos/map/ip). If the lookup fails, thedefaultQoS profile is used. The switch port'sprofilefield is used only for non-IP traffic. If the forwarded/routed packet is VLAN-tagged, its PCP value is set from the selected QoS profile. However, the original DSCP value of the packet is kept intact.
trust | ignore | Trust the Layer 2 header, but ignore L3. If an ingress packet is VLAN-tagged, use the PCP field from the VLAN header for QoS profile lookup (see/in/eth/sw/qos/map/vlan). If the lookup fails (no QoS profiles are mapped to the given PCP value), thedefaultQoS profile is used. The switch port'sprofilefield is used only for untagged traffic.
trust | trust | Trust both headers, but Layer 3 has higher precedence. In the case of an IP packet, use the DSCP field for QoS profile lookup (see/in/eth/sw/qos/map/ip). If the DSCP-to-QoS lookup fails, use thedefaultprofile. If the packet is not an IP packet but is VLAN-tagged, use the PCP field from the VLAN header for QoS profile lookup (see/in/eth/sw/qos/map/vlan).  If the VLAN-to-QoS lookup fails, use thedefaultQoS profile. Non-IP untagged packets use the switch port'sprofile.
trust | keep | The same astrust+trust, but the original DSCP value is preserved in forwarded/routed packets.
keep | ignore | Trust the Layer 2 header but ignore L3. If an ingress packet is VLAN-tagged, use the PCP field from the VLAN header for QoS profile lookup (see/in/eth/sw/qos/map/vlan). If the lookup fails (no QoS profiles are mapped to the given PCP value), thedefaultQoS profile is used. The switch port'sprofilefield is used only for untagged traffic. If the packet is VLAN-tagged on both ingress and egress, the original PCP value is kept.
keep | trust | Trust both headers, but Layer 3 has higher precedence. In the case of an IP packet, use the DSCP field for QoS profile lookup (see/in/eth/sw/qos/map/ip). If the DSCP-to-QoS lookup fails, use thedefaultprofile. If the packet is not an IP packet but is VLAN-tagged, use the PCP field from the VLAN header for QoS profile lookup (see/in/eth/sw/qos/map/vlan).  If the VLAN-to-QoS lookup fails, use thedefaultQoS profile. Non-IP untagged packets use the switch port'sprofile. If the packet is VLAN-tagged on both ingress and egress, the original PCP value is kept. The DSCP value in forwarded/routed packets is set from the selected QoS profile.
keep | keep | Trust both headers, but Layer 3 has higher precedence. In the case of an IP packet, use the DSCP field for QoS profile lookup (see/in/eth/sw/qos/map/ip). If the DSCP-to-QoS lookup fails, use thedefaultprofile. If the packet is not an IP packet but is VLAN-tagged, use the PCP field from the VLAN header for QoS profile lookup (see/in/eth/sw/qos/map/vlan).  If the VLAN-to-QoS lookup fails, use thedefaultQoS profile. Non-IP untagged packets use the switch port'sprofile. Keep both the original PCP and/or DSCP values intact in cases of VLAN-tagged and/or IP packets, respectively.
```
/in/eth/sw/qos/map/ip
```
```
/in/eth/sw/qos/map/ip
```
```
/in/eth/sw/qos/map/vlan
```
```
/in/eth/sw/qos/map/ip
```
```
/in/eth/sw/qos/map/vlan
```
```
/in/eth/sw/qos/map/vlan
```
```
/in/eth/sw/qos/map/ip
```
```
/in/eth/sw/qos/map/vlan
```
```
/in/eth/sw/qos/map/ip
```
```
/in/eth/sw/qos/map/vlan
```
Port settings | The selected QoS profile and the source for PCP / DSCP field values in forwarded/routed packets | qos-trust-l2 | qos-trust-l3 | VLAN-Tagged IP | Untagged IP | VLAN-Tagged Non-IP | Untagged Non-IP | QoS Profile | PCP | DSCP | QoS Profile | PCP1 | DSCP | QoS Profile | PCP | DSCP | QoS Profile | PCP1 | DSCP
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ignore | ignore | profile | profile | profile | profile | profile | profile | profile | profile | - | profile | profile | -
ignore | trust | map/ip | map/ip | map/ip | map/ip | map/ip | map/ip | profile | profile | - | profile | profile | -
ignore | keep | map/ip | map/ip | original | map/ip | map/ip | original | profile | profile | - | profile | profile | -
trust | ignore | map/vlan | map/vlan | map/vlan | profile | profile | profile | map/vlan | map/vlan | - | profile | profile | -
trust | trust | map/ip | map/ip | map/ip | map/ip | map/ip | map/ip | map/vlan | map/vlan | - | profile | profile | -
trust | keep | map/ip | map/ip | original | map/ip | map/ip | original | map/vlan | map/vlan | - | profile | profile | -
keep | ignore | map/vlan | original | map/vlan | profile | profile | profile | map/vlan | original | - | profile | profile | -
keep | trust | map/ip | original | map/ip | map/ip | profile | map/ip | map/vlan | original | - | profile | profile | -
keep | keep | map/ip | original | original | map/ip | profile | original | map/vlan | original | - | profile | profile | -
1applies only when ingress traffic is untagged, but the egress needs to be VLAN-tagged.
# QoS Marking via Switch Rules (ACL)
Starting fromRouterOS v7.15, it is possible to assign QoS profiles viaSwitch Rules (ACL).
Sub-menu:/interface/ethernet/switch/rule
```
/interface/ethernet/switch/rule
```
New/Changed Properties | Description
------------------------------------
new-qos-profile(name) | The name of theQoS profileto assign to the matched packets.
keep-qos-fields(yes | no; Default:no) | Should the original values of QoS fields (PCP, DSCP) be kept (yes), or replace them with the ones from the assigned QoS profile (no)? Relevant only ifnew-qos-profileis set.
new-vlan-priority(0..7) | Deprecated and should be replaced with the respectivenew-qos-profile. Kept for backward compatibility. Relevant only if qos-hw-offloading=no.
The following example assigns a QoS profile based on the source MAC address.
```
/interface ethernet switch rule
add new-qos-profile=stream ports=ether1,ether2 src-mac-address=00:01:02:00:00:00/FF:FF:FF:00:00:00 switch=switch1
add new-qos-profile=voip ports=ether1,ether2 src-mac-address=04:05:06:00:00:00/FF:FF:FF:00:00:00 switch=switch1
```
# QoS Enforcement
# Hardware Queues
Each switch port has eight hardware transmission (tx) queues (queue0..queue7). Each queue corresponds to a traffic class (tc0..tc7) set by aQoS profile. Each ingress packet gets assigned to a QoS profile, which, in turn, determines the traffic class for tx queue selection on the egress port.
Hardware queues are of variable size - set by theTransmission Manager. Moreover, multiple ports and/or queues can share resources with each other (so-calledShared Buffers). For example, a device with 25 ports has memory (buffers) to queue 1200 packets in total. If we split the resources equally, each port gets 48 exclusive buffers with a maximum of 6 packets per queue (48/8) - which is usually insufficient to absorb even a short burst of traffic. However, choosing to share 50% of the buffers leaves each port with 24 exclusive buffers (3 per queue), but at the same time, a single queue can grow up to 603 buffers (3 exclusive + 600 shared).
RouterOS allows enabling/disabling the shared pool for each queue individually - for example, to prevent low-priority traffic from consuming the entire hardware memory. In addition, port buffer limits may prevent a single low-speed port from consuming the entire shared pool. SeeQoS SettingsandTransmission Managerfor details.
# Hardware Resources
The hardware (switch chips) has limited resources (memory). There are two main hardware resources that are relevant to QoS:
One packet descriptor may use multiple buffers (depending on the payload size); buffers may be shared by multiple descriptors - in cases of multicast/broadcast. If the hardware does not have enough free descriptors or buffers, the packet gets dropped (tail-drop).
Hardware resources can be limited per destination type (multicast/unicast), per port, and per each tx queue. If any limits are reached, no more packets can be enqueued for transmission, and further packets get dropped.
RouterOS obscures low-level hardware information, allowing to set resource limits either in terms of packets or a percentage of the total amount. RouterOS automatically calculates the required hardware descriptor and buffer count based on the user-specified packet limit and port's MTU. Moreover, RouterOS comes with preconfigured hardware resources, so there is no need to do a manual configuration in common QoS environments.
# Resource Saving
Since reallocating hardware resources in runtime is not an option, RouterOS cannot automatically free queue buffers reserved for inactive ports. Those buffers remain unused. However, if the user knows that the specific ports willneverbe used (e.g., stay physically disconnected), the respective queue resources can be manually freed by using the built-in "offline" tx-manager with minimum resources:
```
/interface/ethernet/switch/qos/port
set [find where !running] tx-manager=offline
```
# Traffic Prioritization
The hardware provides two types of traffic transmission prioritization:
Strict priorityqueues are straightforward. If the highest priority queue (Q7) has packets, those are transmitted first. When Q7 is empty, packets from Q6 get transmitted, and so on. The packets from the lowest priority queue (Q0) are transmitted only if all other queues are empty.
The downside of strict prioritization is increased latency in lower queues while "overprioritizing" higher queues. Suppose the acceptable latency of TC5 is 20ms, TC3 - 50ms. Traffic appearing in Q5 gets immediately transmitted due to the strict priority of the queue, adding extra latency to every packet in the lower queues (Q4..Q0). A packet burst in Q5 (e.g., a start of a voice call) may temporarily "paralyze" Q3, increasing TC3 latencies over the acceptable 50ms (or even causing packet drops due to full queue) while TC5 packets get transmitted at <1ms (way below the 20ms limit). Slightly sacrificing TC5 latency by transmitting TC3 packets in between would make everybody happy. ThatETSis for.
Enhanced Transmission Selection (ETS)schedule traffic for transmission from multiple queues (group members) in a weighted round-robin manner. A queue's weight sets the number of packets transmitted from the queue in each round. For example, if Q2, Q1, and Q0 are the group members, and their weights are 3, 2, and 1, respectively, the scheduler transmits 3 packets from Q2, 2 - from Q1, and 1 - from Q0. The actual Tx order is "Q2, Q1, Q0, Q2, Q1, Q2" - for even fairer scheduling.
There are two hardware groups:low-priority-groupandhigh-priority-group. There is a strict priority ordering between the two groups: the low-priority-group is transmitting only whenallqueues in the high-priority-group are empty. However, it is possible to use only one group for all queues.
```
low-priority-group
```
```
high-priority-group
```
The default (built-in) RouterOS queue setupis listed below. Q3-Q5 share the bandwidth within the high-priority group, where packets are transmitted while Q6 and Q7 are empty. Q0-Q2 are the members of the low-priority-group, where packets are transmitted while Q3-Q7 are empty.
```
[admin@MikroTik] /interface/ethernet/switch/qos/tx-manager/queue> print
Columns: TX-MANAGER, TRAFFIC-CLASS, SCHEDULE, WEIGHT, QUEUE-BUFFERS, USE-SHARED-BUFFERS
# TX-MANAGER  TRAFFIC-CLASS  SCHEDULE             WEIGHT  QUEUE-BUFFERS  USE-SHARED-BUFFERS
0  default     0              low-priority-group   1       auto           no
1  default     1              low-priority-group   2       auto           yes
2  default     2              low-priority-group   3       auto           yes
3  default     3              high-priority-group  3       auto           yes
4  default     4              high-priority-group  4       auto           yes
5  default     5              high-priority-group  5       auto           yes
6  default     6              strict-priority              auto           yes
7  default     7              strict-priority              auto           yes
```
# Active Queue Management (AQM)
# Weighted Random Early Detection (WRED)
WRED is a per-queue congestion control mechanism that signals congestion events to the end-points by dropping packets. WRED relies on the existence of rate throttling mechanisms in the end-points that react to packet loss, such as TCP/IP. WRED uses a randomized packet drop algorithm in an attempt to anticipate congestion events and respond to them by throttling traffic rates before the congestion actually happens. The randomness property of WRED prevents throughput collapse related to the global synchronization of TCP flows.
WRED can be enabled/disabled per each queue in eachTx Manager. Disable WRED for lossless traffic! Also, there is no reason to enable WRED on high-speed ports where congestion should not happen in the first place.
The behavior is controlled viaWRED threshold. WRED threshold is the maximum number of packets/bytes that can exceed the queue shared buffer limit (cap). A random packet drop begins when queue usage exceeds their respective capacities:
```
queueX-packet-use > queueX-shared-packet-cap
```
```
queueX-byte-use > queueX-shared-byte-cap
```
The more usage exceeds capacity, the higher the packet drop chance, reaching 100% atqueueX-shared-packet-cap + wred-packet-threshold(or byte).
```
queueX-shared-packet-cap + wred-packet-threshold
```
RouterOS automatically chooses the actual WRED threshold values according to queue or shared pool capacities. The user may shift the thresholds in one way or another viaQoS Settings.
Choosing a WRED threshold value is a tradeoff between congestion anticipation and burst absorption. Setting a higher WRED threshold may lead to earlier traffic rate throttling and, therefore, resolve congestion. On the other hand, a high threshold leads to packet drops in limited traffic bursts that could be absorbed by the queue buffers and transformed losslessly if WRED didn't kick in. For instance, initiating a remote database connection usually starts with heavier traffic ("packet burst") at the initialization phase; then, the traffic rate drops down to a "reasonable" level. Any packet drop during the initialization phase leads to nothing but a slower database connection due to the need for retransmission. Hence, lowering the WRED threshold or entirely disabling WRED on such traffic is advised. The opposite case is video streaming. Early congestion detection helps select a comfortable streaming rate without losing too much bandwidth on retransmission or/and "overshooting" by sacrificing the quality level by too much.
The following script only applies WRED to TCP/IP traffic by redirecting it to queue2. UDP and other packets are left in queue1 - since their end-points usually cannot respond to early drops. Queue1 and queue2 are scheduled equally - without prioritizing one queue over another.
```
/interface/ethernet/switch/qos/profile
add name=tcp-wred traffic-class=2 pcp=0 dscp=0
# move TCP traffic to queue2
/interface/ethernet/switch/rule
add new-qos-profile=tcp-wred ports=ether1,ether2,ether3,ether4 protocol=tcp switch=switch1
# set the same scheduling priority (weight) between queue1 and queue2
# apply WRED only to queue2 - TCP traffic
/interface/ethernet/switch/qos/tx-manager/queue/
set [find where traffic-class=1] weight=2 schedule=low-priority-group use-shared-buffers=yes shared-pool-index=0 wred=no
set [find where traffic-class=2] weight=2 schedule=low-priority-group use-shared-buffers=yes shared-pool-index=0 wred=yes
```
# Explicit Congestion Notification(ECN)
Some switch chips can perform ECN marking of IP packets on the hardware level, according to RFC 3168. Hardware ECN marking is based on theWREDmechanism, but instead of dropping IP packets, they are marked with CE (Congestion Experienced, binary 11) in the ECN field (two least significant bits in IPv4/TOS or IPv6/TrafficClass octet). Only ECN-Capable IP packets may be marked - those with the ECN field value of ECT(1) or ECT(0)  (binary 01 or 10, respectively). Not ECN-Capable Transport packets (ECN=00) never get marked. If a packet already has the CE mark (ECN=11), it never gets cleared, even if the device does not experience congestion.
Setecn=yesonTx Manager Queueto enable ECN marking.
The packet receives the CE mark if all conditions below are met:
```
queueX-packet-use > queueX-shared-packet-cap
```
```
queueX-byte-use > queueX-shared-byte-cap
```
# Priority-based Flow Control (PFC)
Priority-Based Flow Control (PFC) provides lossless operation for up to eight traffic classes, so that congestion in one traffic class does not pause other traffic classes. In addition, PFC enables co-existence of loss-sensitive traffic types with loss tolerant traffic type in the same network.
PFC-capable switch chips are complaint with IEEE 802.1Qbb PFC, meaning that the respective devices are capable of generating and responding to PFC frames. On the triggering part, the PFC frame is sent by the source port and traffic class experiencing the congestion. The timer values of the generated PFC frames are 0xFFFF for pause (XOFF) and 0x0 for resume (XON), and the appropriate bit in the priority enable vector is set. On the response part, the received PFC frame pauses the specific priority queues on the port that received the PFC frame for the duration specified by the PFC frame.
In RouterOS, PFC configuration is organized inprofiles, where each port can be assigned to a specific profile. A PFC profile defines the traffic classes to enable PFC on, pause/resume thresholds to send XOFF/XON PFC frames, respectively, and whenever the assigned ports should transmit or/and receive PFC frames.
While congestion occurs on egress ports, PFC is triggered on the ingress port. Shared buffers must be used to associate the amount of ingressed traffic with the respective packets waiting in Tx queues. For each PFC-enabled traffic class, setuse-shared-buffers=yesto the respectiveTx Queues. It is also recommended that a separate shared pool (shared-pool-index) be used for each PFC-enabled queue, especially not to mix it with PFC-disabled traffic classes.
When choosing pause and resume thresholds, consider a delay in transmitting a PFC frame and processing it by the other side. For example, device A experienced congestion at time T, transmitted a PFC pause frame to device B, and B processed the frame and halted transmission at time T+D. During the delta time D, device B still kept sending traffic. If device A has configured the pause threshold to 100%, it has no free buffers available, and, therefore, packets may drop, which is unacceptable for lossless traffic classes. Lowering the pause threshold, let's say, down to 80% issues a PFC pause frame while still having free memory to accumulate traffic during the delta time D. The same applies to resume threshold. Setting it to 0% keeps the device idle during the delta time, lowering the overall throughput.
PFC Rx requires setting the egress rate to all associated queues to calculate pause time, even if it matches the wire speed. For example, if PFC runs on traffic class 3, the assigned ports require theegress-rate-queue3setting.
```
egress-rate-queue3
```
```
/interface/ethernet/switch/qos/priority-flow-control add name=pfctc3 traffic-class=3 rx=yes
/interface/ethernet/switch/qos/port set sfp-sfpplus1,sfp-sfpplus2 pfc=pfctc3 egress-rate-queue3=10G
```
# Property Reference
# Switch settings
Sub-menu:/interface/ethernet/switch
```
/interface/ethernet/switch
```
Switch QoS settings (in addition to the existing ones).
Property | Description
----------------------
qos-hw-offloading(yes | no; Default:no) | Allows enabling QoS for the given switch chip (if the latter supports QoS).
# Port settings
Sub-menu:/interface/ethernet/switch/qos/port
```
/interface/ethernet/switch/qos/port
```
Switch port QoS settings. Assigns a QoS profile to ingress packets on the given port. The assigned profile can be changed via match rules if the port is considered trusted.
By default, ports are untrusted and receive the default QoS profile (Best-Effort, PCP=0, DSCP=0), where priority fields are cleared from the egress packets.
Property | Description
----------------------
egress-rate-queue0 .. egress-rate-queue7(integer: 0..18446744073709551615; Default!egress-rate-queuex) | Sets egress traffic limitation (bits per second) for specific output queue. It is possible to specify the limit using suffixes like k, M, or G to represent kbps, Mbps, or Gbps. This setting can be combined with the overall per-port limitegress-rate(see/in/eth/sw/port).
map(name; Default:default) | Allows user-definedQoS priority-to-profile mappingin the case of a trusted port or host (see/in/eth/sw/qos/map).
pfc(name; Default:disabled) | The name of thePFC profileto control ingress priority-based traffic flow (see/in/eth/sw/qos/priority-flow-control).
profile(name; Default:default) | The name of theQoS profileto assign to the ingress packets by default (see/in/eth/sw/qos/profile).
trust-l2(ignore | trust | keep; Default:ignore) | Whenever to trust the Layer 2 headers of the incoming packets (802.1p PCP field):ignore- ignore L2 header; use the port'sprofilevalue for all incoming packets;trust- use PCP field of VLAN-tagged packets for QoS profile lookup inmap. Untagged packets use the port'sprofilevalue. Forwarded VLAN or priority-tagged packets receive the PCP value from the selected QoS profile (overwriting the original value).keep- trust but keep the original PCP value in forwarded packets.
trust-l3(ignore | trust | keep; Default:ignore) | Whenever to trust the Layer 3 headers of the incoming packets (IP DSCP field):ignore- ignore L3 header; use either L2 header or the port'sprofile(depends ontrust-l2).trust- use DSCP field of IP packets for QoS profile lookup inmap. Forwarded/routed IP packets receive the DSCP value from the selected QoS profile (overwriting the original value).keep- trust but keep the original DSCP value in forwarded/routed packets.
tx-manager(name; Default:default) | The name of theTransmission Managerthat is responsible for enqueuing and transmitting packetsfromthe given port (see/in/eth/sw/qos/tx-manager).
```
/in/eth/sw/port
```
```
/in/eth/sw/qos/map
```
```
/in/eth/sw/qos/priority-flow-control
```
```
).
```
```
/in/eth/sw/qos/profile
```
Whenever to trust the Layer 2 headers of the incoming packets (802.1p PCP field):
Whenever to trust the Layer 3 headers of the incoming packets (IP DSCP field):
The name of theTransmission Managerthat is responsible for enqueuing and transmitting packetsfromthe given port (see/in/eth/sw/qos/tx-manager).
```
/in/eth/sw/qos/tx-manager
```
Commands.
Command | Description
---------------------
print | Print the above properties in a human-friendly format.
print stats | Print port statistics: total and per-queue transmitted/dropped packets/bytes.
reset-counters | Reset all counters in port statistics to zero.
print usage | Print queue usage/resources.
print pfc | Pring Priority Flow Control stats
print rates | Print per-queue egress traffic limitation (set byegress-rate-queueX)
# Port Stats
```
[admin@Mikrotik] /interface/ethernet/switch/qos/port> print stats where name=ether2
name:     ether2
tx-packet:      2 887
tx-byte:  3 938 897
drop-packet:      1 799
drop-byte:  2 526 144
tx-queue0-packet:         50
tx-queue1-packet:      1 871
tx-queue3-packet:        774
tx-queue5-packet:        192
tx-queue0-byte:      3 924
tx-queue1-byte:  2 468 585
tx-queue3-byte:  1 174 932
tx-queue5-byte:    291 456
drop-queue1-packet:      1 799
drop-queue1-byte:  2 526 144
```
Property | Description
----------------------
name | Port name.
tx-packet | The total number of packets transmitted via this port.
tx-byte | The total number of bytes transmitted via this port.
drop-packet | The total number of packets should have been transmitted via this port but were dropped due to a lack of resources (e.g., queue buffers) or QoS Enforcement.
drop-byte | The total number of bytes should have been transmitted via this port but were dropped.
tx-queue0-packet..tx-queue7-packet | The number of packets transmitted via this port from the respective queue.
tx-queue0-byte..tx-queue7-byte | The number of bytes transmitted via this port from the respective queue.
drop-queue0-packet..drop-queue7-packet | The number of packets dropped from the respective queue (or not enqueued at all due to lack of resources).
drop-queue0-byte..drop-queue7-byte | The number of bytes dropped from the respective queue.
tx-queue0-packet..tx-queue7-packet
tx-queue0-byte..tx-queue7-byte
drop-queue0-packet..drop-queue7-packet
drop-queue0-byte..drop-queue7-byte
# Port Resources/Usage
```
[admin@crs326] /interface/ethernet/switch/qos/port> print usage where name=ether2
name:  ether2
packet-cap:     136
packet-use:       5
byte-cap:  35 840
byte-use:   9 472
queue0-packet-cap:     130
queue0-packet-use:       1
queue1-packet-cap:       5
queue1-packet-use:       4
queue3-packet-cap:      65
queue3-packet-use:       2
queue0-byte-cap:  24 576
queue0-byte-use:     256
queue1-byte-cap:   7 680
queue1-byte-use:   6 144
queue3-byte-cap:  14 080
queue3-byte-use:   3 072
```
Property | Description
----------------------
name | Port name.
packet-cap | Port's packet capacity. The maximum number of packets that can be enqueued for transmission via the port.
packet-use1 | Port's packet usage. The number of packets that are currently enqueued in all port's queues.
byte-cap | Port's byte capacity (buffer size). The maximum number of bytes that can be enqueued for transmission via the port.
byte-use1 | Port's byte usage. The size of hardware buffers (in bytes) that are currently allocated for packets the enqueued packets. Since the buffers are allocated by blocks (usually - 256B each), the allocated buffer size can be bigger than the actual payload.
queue0-packet-cap..queue7-packet-cap2 | Individual queue capacity. The maximum number of packets that can be enqueued in the respective queues (unless theShared Buffersare enabled).
queue0-shared-packet-cap .. queue7-shared-packet-cap2 | Shared queue capacity (individual queue capacity + shared buffers). The maximum number of packets that can be enqueued in the respective queues.
queue0-packet-use..queue7-packet-use2 | Queue packet usage. The number of enqueued packets in the respective queues.
queue0-byte-cap..queue7-byte-cap2 | Individual queue capacity. The maximum number of bytes that can be enqueued in the respective queues (unless theShared Buffersare enabled).
queue0-shared-byte-cap .. queue7-shared-byte-cap2 | Shared queue capacity (individual queue capacity + shared buffers). The maximum number of bytes that can be enqueued in the respective queues.
queue0-byte-use..queue7-byte-use2 | Queue buffer usage (in bytes). The size of hardware buffers (in bytes) that are currently allocated for packets in the respective queues.
queue0-byte-max .. queue7-byte-max2 | Maximum queue buffer fill level (in bytes). Available only on devices that provide the queue statistics service. Use thereset-counterscommand to reset values.
1Port's packet/byte usage can exceed the capacity ifShared Buffersare enabled.
2Only the queues in use are printed.
# Port PFC Stats
```
[admin@crs317] /interface/ethernet/switch/qos/port> print pfc interval=1 where running
name:  sfp-sfpplus1 sfp-sfpplus2   ether1
pfc:          roce     disabled disabled
pfc-tx:            46
pfc-paused-tc:             3
pfc3-pause-threshold:     1 048 576
pfc3-resume-threshold:        10 240
pfc3-use:     1 075 200
```
Property | Description
----------------------
name | Port name.
pfc | PFC profile name.
pfc-rx | Received PFC frame count.
pfc-tx | Transmitted PFC frame count.
pfc-paused-tc | The list of traffic classes should be paused (from the sender's perspective). PFC pause frames (XOFF) are periodically sent with the listed timers set from this port.
pfc0-pause-threshold .. pfc7-pause-threshold | Pause thresholds of the respective traffic classes. Only PFC-enabled traffic classes are displayed.
pfc0-resume-threshold .. pfc7-resume-threshold | Resume thresholds of the respective traffic classes. Only PFC-enabled traffic classes are displayed.
pfc0-use .. pfc7-use | The current buffer usage of the respective traffic classes (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.
pfc-paused-tc
pfc0-use .. pfc7-use
# QoS Menu
Sub-menu:/interface/ethernet/switch/qos
```
/interface/ethernet/switch/qos
```
Almost the entire QoS HW configuration is located under/in/eth/sw/qos. Such an approach allows storing all QoS-related configuration items in one place, easy monitoring and exporting (/in/eth/sw/qos/export).
```
/in/eth/sw/qos
```
```
/in/eth/sw/qos/export
```
QoS entries have two major flags:
# QoS Settings
Sub-menu:/interface/ethernet/switch/qos/settings
```
/interface/ethernet/switch/qos/settings
```
Property | Description
----------------------
multicast-buffers(percent: 1..90; Default:10) | Maximum amount of packet buffers for multicast/broadcast traffic (% of the total buffer memory).
shared-buffers(percent: 0..90; Default:40) | Maximum amount of packet buffers that are shared between ports (% of the total buffer memory). Setting it to 0 disables buffer sharing. The remaining buffer memory is split between the ports.
shared-buffers-color(all | green-only | yellow-and-green; Default:all) | Restricts shared buffer usage for specific traffic colors only.
shared-pool0 .. shared-pool7(percent: 0..100; Default:auto) | If the device supports multiple shared buffer pools, these settings allows adjusting the size of each pool (% of thesharedbuffer memory, where 100% means all shared buffers allocated by theshared-bufferssetting). For example, if shared-buffers=40 and shared-pool0=50, the shared pool # 0 (the first one) receives 20% of the total buffer memory (50% of 40% or "0.5 * 0.4 = 0.2"). Auto mode tries to equally allocate available resources between pools that uses auto setting, and provides at least a minimum of 10% of the total shared buffer size if the sum of other manually configured pools are exceeded. The default setting (auto).
treat-yellow-as(green | red; Default:red) | For devices that support only two-color traffic marking (red/green). This setting allows using the same QoS profiles for the devices with two- and three-color traffic marking.
wred-threshold(low | medium | high;Default:medium) | A relative amount of packets above a shared queue cap ("queueX-shared-packet-cap" or "queueX-shared-byte-cap") where random drops take place. This threshold is applied only to queues with enabledWeighed Random Early Detection(wred=yes) that use shared buffers (use-shared-buffers=yes). The higher the queue buffer fill level, the higher the packet drop chance. Thelowthreshold means the random tail drop starts later; thehigh- sooner.
```
queueX-shared-packet-cap
```
```
queueX-shared-byte-cap
```
# QoS Monitor
Command:/interface/ethernet/switch/qos/monitor
```
/interface/ethernet/switch/qos/monitor
```
```
[admin@crs312] /interface/ethernet/switch/qos> monitor once
total-packet-cap: 11 480
total-packet-use: 454
total-byte-cap: 3072.0KiB
total-byte-use: 681.0KiB
multicast-packet-cap: 1 148
multicast-packet-use: 0
multicast-byte-cap: 307.0KiB
multicast-byte-use: 0
shared-pool0-packet-cap: 2 296
shared-pool0-packet-use: 0
shared-pool3-packet-cap: 2 296
shared-pool3-packet-use: 190
shared-pool0-byte-cap: 614.2KiB
shared-pool0-byte-use: 0
shared-pool3-byte-cap: 614.2KiB
shared-pool3-byte-use: 610.5KiB
wred-packet-cap: 512
wred-byte-cap: 128.0KiB
```
Monitors hardware QoS resources.
Property | Description
----------------------
total-packet-cap(integer) | Total packet capacity. The maximum number of hardware packet descriptors that the device can store is all queues.
total-packet-use(integer) | Total packet usage. The current number of packet descriptors residing in the hardware memory.
total-byte-cap(byte) | Total tx memory capacity.
total-byte-use(byte) | Total tx memory usage. The current number of bytes occupied by the packets in all tx queues.
multicast-packet-cap(integer) | Multicast packet capacity. The maximum number of hardware packet descriptors that can be used by multicast/broadcast traffic. Depends on themulticast-bufferssetting.
multicast-packet-use(integer) | Multicast packet usage. The hardware makes a copy of the packet descriptor for each multicast destination.
shared-packet-cap(integer) | Shared packet capacity. The maximum number of hardware packet descriptors that can be shared between ports and tx queues. Depends on theshared-bufferssetting.
shared-packet-use(integer) | Shared packet usage. The current number of shared packet descriptors used by all tx queues.
shared-byte-cap(byte) | Shared tx memory capacity. Depends on theshared-bufferssetting.
shared-byte-use(byte) | Shared tx memory usage. The current number of shared buffers occupied by the packets in all tx queues.
shared-pool0-packet-cap .. shared-pool7-packet-cap(integer) | Shared packet capacity of the each shared pool. Only the shared pools in use are displayed. These fields are omitted if the device does not support multiple shared pools.
shared-pool0-packet-use .. shared-pool7-packet-use(integer) | Per-pool shared packet usage. Only the shared pools in use are displayed. These fields are omitted if the device does not support multiple shared pools.
wred-packet-cap(integer) | The maximum packet count that a queue can use above the shared cap ("queueX-shared-packet-cap" in "/in/eth/sw/qos/port print usage") to trigger a random tail drop. For example, if "queue1-shared-packet-cap=3072" and "wred-packet-cap=512", WRED triggers whenqueue1-packet-useexceeds 3072, reaching 100% drop rate at 3072+512=3584 packets.
wred-byte-cap(integer) | The maximum byte count that a queue can use above the shared cap ("queueX-shared-byte-cap") to trigger a random tail drop. For example, if "queue1-shared-byte-cap=768KiB" and "wred-byte-cap=128KiB", WRED triggers whenqueue1-packet-useexceeds 768KiB, reaching 100% drop rate at 768+128=896KiB.
```
queueX-shared-packet-cap
```
```
/in/eth/sw/qos/port print usage
```
```
queue1-shared-packet-cap=3072
```
```
wred-packet-cap=512
```
```
queue1-packet-use
```
```
queueX-shared-byte-cap
```
```
queue1-shared-byte-cap=768KiB
```
```
wred-byte-cap=128KiB
```
```
queue1-packet-use
```
# QoS Profile
Sub-menu:/interface/ethernet/switch/qos/profile
```
/interface/ethernet/switch/qos/profile
```
QoS profiles determine priority field values (PCP, DSCP) for the forwarded/routed packets. Congestion avoidance/resolution is based on QoS profiles. Each packet gets a QoS profile assigned based on the ingress switch port QoS settings (see/in/eth/sw/port).
```
/in/eth/sw/port
```
Property | Description
----------------------
color(green | yellow | red; Default:green) | Traffic color for color-aware drop precedence management. Leave the default value (green) for color-blind drop precedence management.
dscp(integer: 0..63; Default:0) | IPv4/IPv6 DSCP field value for the egress packets assigned to the QoS profile.
name(string; Default: ) | The user-defined name of the QoS profile.
pcp(integer: 0..7; Default:0) | VLAN priority value (IEEE 802.1q PCP - Priority Code Point). Used only if the egress packets assigned to the QoS profile are VLAN-tagged (have the 802.1q header). The value can be further altered via the QoS Egress Map.
traffic-class(integer: 0..7; Default:0) | The traffic class determines the packet priority and the egress queue (seetx-manager). The queue number is usually the same as the traffic class (packets with tc0 go into queue0, tc1 - queue1, ... tc7 - queue7). Unlike pcp, where 0 means the default priority but 1 - the lowest one (and further customizable), traffic classes are strictly ordered. TC0 always selects the lowest priority, etc.
# QoS Mapping
Sub-menu:/interface/ethernet/switch/qos/map
```
/interface/ethernet/switch/qos/map
```
Priority-to-profile mapping table(-s) for trusted packets. All switch chips have one built-in map -default. In addition, some models allow the user to define custom mapping tables and assign different maps to various switch ports via theqos-mapproperty:
Property | Description
----------------------
name(string; Default: ) | The user-defined name of the mapping table.
# VLAN Map
```
VLAN Map
```
Sub-menu:/interface/ethernet/switch/qos/map/vlan
```
/interface/ethernet/switch/qos/map/vlan
```
Matches VLAN priorities (802.1p PCP/DEI fields) to QoS profiles. By default, all values are matched to the default QoS profile.
Property | Description
----------------------
dei-only(yes| no; Default:no) | Map only packets with DEI (formerly CFI) bit set in the VLAN header.
map(name; Default:default) | The name of the mapping table.
profile(name; Default: ) | The name of the QoS profile to assign to the matched packets.
pcp(range: 0..7; Default:0) | VLAN priority (PCP) value(-s) for the lookup.
# DSCP Map
Sub-menu:/interface/ethernet/switch/qos/map/ip
```
/interface/ethernet/switch/qos/map/ip
```
Matches DSCP values to QoS profiles.
Property | Description
----------------------
dscp(range: 0..63; Default:0) | DSCP value(-s) for the lookup.
map(name; Default:default) | The name of the mapping table. If not set, the standard (built-in) mapping table gets altered.
profile(name; Default: ) | The name of the QoS profile to assign to the matched packets.
# Transmission Manager
Sub-menu:/interface/ethernet/switch/qos/tx-manager
```
/interface/ethernet/switch/qos/tx-manager
```
Transmission (Tx) Manager controls packet enqueuing for transmission and packet tx order. Different switch ports can be assigned to different Tx managers. The maximum number of hardware Tx managers depends on the switch chip model.
Property | Description
----------------------
name(string; Default: ) | The user-defined name of the Tx Manager
queue-buffers(percent: 0%..100% | bytes | auto;Default:auto) | The total amount of hardware Tx buffers allocated to all ports linked to this Tx Manager. Any value butautois NOT scaled by the number of ports. For example, if queue-buffers=30%, and there are 3 ports using this Tx Manager, each respective port receives 10% of total available resources. Adding two more ports to the Tx Manager drops per-port buffers down to 6% (30/5).
# Transmission Queue Scheduler
Sub-menu:/interface/ethernet/switch/qos/tx-manager/queue
```
/interface/ethernet/switch/qos/tx-manager/queue
```
Each port has eight Tx queues. The assigned Tx Manager controls packet enqueuing and schedules transmission orders. Each queue can have either strict priority (where packets with the highest traffic class are always transmitted first) or grouped together for a weighted round-robin tx schedule.
Creating a Tx Manager automatically creates all eight respective queue schedulers.
Property | Description
----------------------
tx-manager(name;read-only) | The linked Tx Manager
traffic-class(integer: 0..7;read-only) | The traffic class (tc0..tc7) and the respective port queue (queue0..queue7) that the scheduler controls.
schedule(strict-priority | high-priority-group | low-priority-group) | strict-priority- packets in the respective queue are always scheduled before moving to lower traffic classes. Packets with lower traffic classes are not transmitted until the current queue is empty.high-priority-group- all queues in the group are scheduled together by using a weighted round-robin principle. For example, if TC5 has weight 4, TC4 - 3, and TC3 - 2, then the scheduler transmits 4 packets from queue5, 3 packets from Q4, and 2 packets from Q3 in a single round. To achieve lower latency, each round is "sliced" between all queues in the group. In other words, the packet order in each round of the above example is "Q5, Q4, Q3, Q5, Q4, Q3, Q5, Q4, Q5".low-priority-group- similar logic to the high-priority-group, but the low-priority-group is scheduled only when all queues in the high-priority-group are empty.
weight(integer: 0..255;Default:1) | The weight value for the traffic class if it is a member of a schedule group. The field is not used in the case of strict priority schedule.
queue-buffers(percent: 0%..100% | bytes | auto;Default:auto) | The amount of hardware Tx buffers allocated to this queue. Any value butautois NOT scaled by the number of ports, i.e., the value gets split on ports linked to the Tx Manager. When given in percent, it means percentage of the tx-manager's queue-buffers value.
use-shared-buffers(yes | no) | Allow the queue to use the shared buffer pool whenqueue-buffersare full. If the queue is full and the shared buffers are disabled, the packet gets dropped. If the shared buffers are enabled, the queue may use up toshared-packet-caporshared-poolX-packet-cap(seeQoS Settingsfor details) packets from the shared pool.
shared-pool-index(integer;Default:0) | The shared pool index for the queue to use. Relevant only ifuse-shared-buffers=yesand the device supports multiple shared pools.
wred(yes | no; Default:no) | Enables/disablesWeighted Random Early Detectionfor the given queue.
ecn (yes | no; Default:no) | Enables/disablesECN markingof the transmitted packets.
wred-actual(yes | no;  read-only) | The actual WRED value.
ecn-actual(yes | no;  read-only) | The actual ECN value.
# Priority-based Flow Control (PFC)
Sub-menu:/interface/ethernet/switch/qos/priority-flow-control
```
/interface/ethernet/switch/qos/priority-flow-control
```
PFCconfiguration is organized in profiles. Different switch ports can be assigned to different PFC profiles. The maximum number of hardware Tx managers depends on the switch chip model. The builtin profile named "disabled" cannot be changed.
Property | Description
----------------------
name(string; Default: ) | The user-defined name of the PFC profile
pause-threshold(percent: 0%..100% | bytes | auto;Default:auto) | Transmits a pause frame (XOFF) when the total size of enqueued packets reaches this threshold. Enqueued packets are counted per ingress port. Applies only whentx=yes. The value can be given either explicitly in bytes or percent of the respective shared pool size (shared-poolX-byte-cap).
resume-threshold(percent: 0%..100% | bytes | auto;Default:auto) | Transmits a resume frame (XON) when the total size of enqueued packets drops down to this threshold. Enqueued packets are counted per ingress port. Applies only whentx=yes. The value can be given either explicitly in bytes or percent of the respective shared pool size (shared-poolX-byte-cap).
rx(yes | no; Default:no) | Enables receiving of PFC frames. The received PFC frame pauses the specific priority queues on the port that received the PFC frame for the duration specified by the PFC frame. Disabling rx disables queue pausing.
traffic-class(integer array: 0..7) | The list of PFC-enabled traffic classes.
tx(yes | no; Default:no) | Enables transmition of PFC frames.