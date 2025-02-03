---
title: Precision Time Protocol
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/64127015/Precision+Time+Protocol,
crawled_date: 2025-02-02T21:12:50.014124
section: mikrotik_docs
type: documentation
---

# 2Summary3General Properties4Configuration4.1Create a PTP Profile4.2Assign Ports to the PTP Profile4.3PTP on VLAN Ports4.4PTP with IGMP Snooping5Monitoring5.1Monitor Properties6Supported Devices
* 2Summary
* 3General Properties
* 4Configuration4.1Create a PTP Profile4.2Assign Ports to the PTP Profile4.3PTP on VLAN Ports4.4PTP with IGMP Snooping
* 5Monitoring5.1Monitor Properties
* 6Supported Devices
* 4.1Create a PTP Profile
* 4.2Assign Ports to the PTP Profile
* 4.3PTP on VLAN Ports
* 4.4PTP with IGMP Snooping
* 5.1Monitor Properties
# Summary
The Precision Time Protocol (PTP), developed by the Institute of Electrical and Electronics Engineers (IEEE), is a protocol used to synchronize clocks across a local area network. It is essential in industries and applications where precise timing is critical, such as telecommunications, finance, and industrial automation. PTP typically ensures time accuracy in the sub-microsecond range, but nanosecond-level accuracy is also achievable when hardware requirements are met. MikroTik’s implementation of PTP supports IEEE 1588-2008 (PTPv2) and includes hardware timestamping capabilities that ensure synchronization within the nanosecond range. For additional details on MikroTik’s PTP features, please refer to the list below.
Supported Features:
* Two-step Ordinary Clock and Boundary Clock.
* Hardware timestamping, ensuring clock syncronization in nanosecond(ns) range.
* IPv4 and Layer 2 (L2) multicast transport modes.
* End-to-End (E2E) and Peer-to-Peer (P2P) delay mechanisms.
* IEEE 1588-2008 (PTPv2)
* Profile Support for:802.1AS: Audio Video Bridging (AVB) and Time-Sensitive Networking (TSN).AES67: High-performance audio-over-IP interoperability.G.8275.1: Frequency and phase synchronization in PTP-aware networks.SMPTE: Audio/video synchronization in professional broadcast environments
* 802.1AS: Audio Video Bridging (AVB) and Time-Sensitive Networking (TSN).
* AES67: High-performance audio-over-IP interoperability.
* G.8275.1: Frequency and phase synchronization in PTP-aware networks.
* SMPTE: Audio/video synchronization in professional broadcast environments
# General Properties
Sub-menu:/system ptp
```
/system ptp
```
Property | Description
----------------------
port | Sub-menu used for adding, removing, or viewing assigned ports.
status | Sub-menu that shows PTP ports, their state, and delay on slave ports.
comment(string; Default: ) | Short description of the PTP profile.
name(string; Default: ) | Name of the PTP profile.
domain(integer [0..255];Default:auto) | Identifier used to separate different PTP instances.
delay-mode(auto | e2e | p2p; Default:auto) | auto - selects the delay mode automatically depending on the profile being used.e2e - utilizes the delay request-response mechanism.ptp - utilizes the peer delay mechanism.
priority1(integer [0..255]; auto;Default:auto) | Parameter which takes part in the election of a grandmaster clock.
priority2(integer [0..255]; auto;Default:auto) | Parameter which takes part in the election of a backup grandmaster clock.
profile(802.1as; aes67; g8275.1; smpte; default;Default:default) | Each profile comes with its own predefined auto values for PTP operating parameters and options:802.1as is an adaptation of PTP for use with Audio Video Bridging and Time-Sensitive Networking.Defaultvalues:priority1=246,priority2=248,transport=l2-non-forwardable,delay-mode=p2p.aes67 profile is for high-performance audio-over-IP interoperability.Defaultvalues:priority1=128, priority2=128, domain=0, transport=ipv4, delay-mode=e2e.g8275.1 profile is for frequency and phase synchronization in a fully PTP-aware network.Defaultvalues:priority1=128, priority2=128, domain=24, transport=l2-non-forwardable, delay-mode=e2e.smpte profile is for the synchronization of audio/video equipment in a professional broadcast environment.Defaultvalues:priority1=128, priority2=128, domain=127, transport=ipv4, delay-mode=e2e.default profile, PTPv2 default configuration, allows for more configuration options than other profiles.Default values:priority1=128, priority2=128, domain=0, transport=ipv4, delay-mode=e2e.
transport(auto; ipv4; l2-forwardable; l2-non-forwardable;Default:auto) | Transport protocol to be used:auto - automatically selects the transport mode based on the PTP profile in use.ipv4 - uses the IPv4 multicast addresses 224.0.1.129 for PTP primary messages and 224.0.0.107 for PTP peer delay messages.l2-forwardable - uses the multicast MAC address01-1B-19-00-00-00, which is being forwarded through PTP-unaware network equipment.l2-non-forwardable - uses the multicast MAC address01-80-C2-00-00-0E, ensuring that PTP messages are not forwarded through PTP-unaware network equipment.
Short description of the PTP profile.
* auto - selects the delay mode automatically depending on the profile being used.
* e2e - utilizes the delay request-response mechanism.
* ptp - utilizes the peer delay mechanism.
priority1(integer [0..255]; auto;Default:auto)
priority2(integer [0..255]; auto;Default:auto)
Each profile comes with its own predefined auto values for PTP operating parameters and options:
* 802.1as is an adaptation of PTP for use with Audio Video Bridging and Time-Sensitive Networking.Defaultvalues:priority1=246,priority2=248,transport=l2-non-forwardable,delay-mode=p2p.
* aes67 profile is for high-performance audio-over-IP interoperability.Defaultvalues:priority1=128, priority2=128, domain=0, transport=ipv4, delay-mode=e2e.
* g8275.1 profile is for frequency and phase synchronization in a fully PTP-aware network.Defaultvalues:priority1=128, priority2=128, domain=24, transport=l2-non-forwardable, delay-mode=e2e.
* smpte profile is for the synchronization of audio/video equipment in a professional broadcast environment.Defaultvalues:priority1=128, priority2=128, domain=127, transport=ipv4, delay-mode=e2e.
* default profile, PTPv2 default configuration, allows for more configuration options than other profiles.Default values:priority1=128, priority2=128, domain=0, transport=ipv4, delay-mode=e2e.
Transport protocol to be used:
* auto - automatically selects the transport mode based on the PTP profile in use.
* ipv4 - uses the IPv4 multicast addresses 224.0.1.129 for PTP primary messages and 224.0.0.107 for PTP peer delay messages.
* l2-forwardable - uses the multicast MAC address01-1B-19-00-00-00, which is being forwarded through PTP-unaware network equipment.
* l2-non-forwardable - uses the multicast MAC address01-80-C2-00-00-0E, ensuring that PTP messages are not forwarded through PTP-unaware network equipment.
```
01-1B-19-00-00-00
```
```
01-80-C2-00-00-0E
```
# Configuration
Configuring Precision Time Protocol (PTP) on MikroTik devices is a straightforward process. The primary steps involve creating a PTP profile and assigning the relevant ports to this profile for PTP operation.
### Create a PTP Profile
To create a PTP profile, use the following command. In this example, we use the 802.1as profile, but you can select from other available profiles as needed:
```
/system ptp add name=ptp1 profile=802.1as
```
To verify that the profile has been created successfully, execute:
```
/system ptp print
```
The output will display the created profile with its current settings:
```
Flags: I - inactive, X - disabled 
 0   name="ptp1" priority1=auto priority2=auto delay-mode=auto transport=auto profile=802.1as domain=auto
```
### Assign Ports to the PTP Profile
As the final step, assign the ports that will participate in PTP. For example, lets include few sfp28 interfaces. sfp28-12 is the one that's connected to the grandmaster clock and sfp28-1, sfp28-2 connected to an ordinary clock/slave:
```
/system ptp port add interface=sfp28-1 ptp=ptp1
/system ptp port add interface=sfp28-2 ptp=ptp1
/system ptp port add interface=sfp28-12 ptp=ptp1
```
### PTP on VLAN Ports
When PTP ports are also part of VLANs on your boundary clock device, you must add a bridge interface as an untagged port in theBridge VLAN Tablefor every entry that includes a PTP port.
This is necessary because the bridge interface functions as a bridge port towards the CPU. Therefore, it must be included in the VLAN table along with the PTP ports ensuring that packets can be correctly received from the physical port and forwarded to the CPU via the bridge. Let's continue with our previous configuration to make this clearer:
```
# Create a new bridge interface
/interface/bridge/add name=bridge1
# Assign the ports that will be part of this bridge
/interface/bridge/port add bridge=bridge1 interface=sfp28-1 pvid=10
/interface/bridge/port add bridge=bridge1 interface=sfp28-2 pvid=20
# Create new entries for Bridge VLAN Table
/interface bridge vlan add bridge=bridge1 vlan-ids=10 untagged=bridge1,sfp28-1
/interface bridge vlan add bridge=bridge1 vlan-ids=20 untagged=bridge1,sfp28-2
```
### PTP with IGMP Snooping
If IGMP snooping is enabled on your bridge and VLANs are configured as shown in the previous example, you must manually add static Multicast Database (MDB) entries for each VLAN containing PTP ports that use IPv4 (224.0.1.129) as their transport modes. This ensures proper forwarding of PTP multicast traffic.
```
/interface bridge/mdb add group=224.0.1.129 bridge=bridge1 ports=bridge1 vid=10
/interface bridge/mdb add group=224.0.1.129 bridge=bridge1 ports=bridge1 vid=20
```
# Monitoring
To monitor the status and performance of the PTP profile, use the following command:
```
/system ptp monitor 0
```
The output will provide detailed information about the profile's operational status:
```
name: ptp1
clock-id: 64:D1:54:FF:FE:EB:AD:C7
priority1: 246
priority2: 248
i-am-gm: no
gm-clock-id: 64:D1:54:FF:FE:EB:AE:C3
gm-priority1: 100
gm-priority2: 248
master-clock-id: 64:D1:54:FF:FE:EB:AE:C3
slave-port: ether1
freq-drift: 2690 ppb
offset: 3 ns
hw-offset: -889419842 ns
slave-port-delay: 306 ns
```
This information includes critical details such as the clock IDs, priority values, and timing offsets, which are essential for monitoring the accuracy and synchronization of your PTP setup.
### Monitor Properties
Property | Description
----------------------
clock-id: | Local clock identifier, used to uniquely identify the clock within the PTP network.
priority1: | The priority parameter used in the election of the grandmaster clock. A lower value indicates higher priority.
priority2: | The priority parameter used in the election of the backup grandmaster clock. A lower value indicates higher priority.
i-am-gm:yes | no | Indicates if the device is a grandmaster clock (yes) or not (no).
gm-clock-id: | Identifier of the grandmaster clock. This is the clock providing the primary time source.
gm-priority1: | Thepriority1value of the grandmaster clock as seen from the slave device.
gm-priority2: | Thepriority2value of the grandmaster clock as seen from the slave device.
master-clock-id: | Identifier of the master clock in the PTP communication path. This may be a grandmaster clock or a boundary clock, depending on the network topology.
slave-port: | The port on the device that is connected to the master or grandmaster clock.
freq-drift: | The frequency drift between the master and slave clocks, measured in parts per billion (ppb). This indicates how much the slave clock's frequency deviates from the master clock's frequency.
offset: | The time difference between the master and slave clocks, measured in nanoseconds (ns). This reflects the synchronization accuracy.
hw-offset: | Offset difference from the hardware clock.
slave-port-delay: | The time delay for packets traveling between two devices, measured in nanoseconds (ns). This delay can be influenced by the quality of cables and transceivers used in the network.
```
yes
```
```
no
```
```
priority1
```
```
priority2
```
# Supported Devices
Important:Devices not listed in this section do not support Precision Time Protocol.
* CRS326-24G-2S+:Supported only on Gigabit Ethernet ports.
* CRS328-24P-4S+:Supported only on Gigabit Ethernet ports.
* CRS317-1G-16S+:Supported on all ports.
* CRS326-24S+2Q+:Supported on SFP+ and QSFP+ interfaces.
* CRS312-4C+8XG:Supported on all ports.
* CRS318-16P-2S+:Supported only on Gigabit Ethernet ports.
* CRS318-1Fi-15Fr-2S:Supported only on Gigabit Ethernet ports.
PTP Support Added in RouterOS Version 7.16 and Later:
* CCR2116-12G-4S+:Supported on all ports.
* CCR2216-1G-12XS-2XQ:Supported on all ports.
* CRS518-16XS-2XQ:Supported on all ports.
* CRS504-4XQ:Supported on all ports.
* CRS510-8XS-2XQ:Supported on all ports.
* CRS520-4XS-16XQ:Supported on all ports.
PTP Support Added in RouterOS Version 7.17 and Later:
* CRS320-8P-8B-4S+RM:Supported only on Gigabit Ethernet ports.
* CRS326-4C+20G+2Q+:Supported on all ports.