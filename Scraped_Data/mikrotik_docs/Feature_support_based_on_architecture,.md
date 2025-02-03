---
title: Feature support based on architecture
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/146440194/Feature+support+based+on+architecture,
crawled_date: 2025-02-02T20:25:05.107036
section: mikrotik_docs
type: documentation
---

All devices support the same features, with a few exceptions, clarified in the below table:
Architecture | Not supported | Exclusively supported
ARM |  | Zerotier, Container, BTH
ARM64 |  | Zerotier, Container, BTH
MIPSBE | Zerotier, Dude server | 
MMIPS | Zerotier | 
SMIPS | Zerotier, DOT1X, BGP, MPLS, PIMSM, Dude server, User manager | 
TILE | Zerotier | BTH
PPC | Zerotier, Dude server | 
X86 PC | Zerotier, Cloud | Container
CHR VM |  | 
Apart from features, there are also a few differences in hardware capabilities, based on the specific model of device. For these differences, please see the below articles:
* Wifi - new driver implementation for 802.11ax devices and supported older deviceshttps://help.mikrotik.com/docs/display/ROS/Wifi
* L3 Hardware offloadinghttps://help.mikrotik.com/docs/display/ROS/L3+Hardware+Offloading#L3HardwareOffloading-L3HWDeviceSupport
* PTPhttps://help.mikrotik.com/docs/display/ROS/Precision+Time+Protocol
* Switch chip featureshttps://help.mikrotik.com/docs/display/ROS/Switch+Chip+Features
Switch chip featureshttps://help.mikrotik.com/docs/display/ROS/Switch+Chip+Features