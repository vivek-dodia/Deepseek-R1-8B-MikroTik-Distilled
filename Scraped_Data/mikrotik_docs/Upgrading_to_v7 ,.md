---
title: Upgrading to v7
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/115736772/Upgrading+to+v7 ,
crawled_date: 2025-02-02T20:25:24.497053
section: mikrotik_docs
type: documentation
---

## Introduction
This document describes the recommended steps for upgrading RouterOS to v7 major release and the possible caveats when doing so.
Upgrading from v6 to v7 happens the same way, as upgrading within v6 releases. Please follow theUpgrade manualfor more detailed steps. If you are currently running RouterOS version 6 or older, we first suggest upgrading to the latest stable or long-term release in v6.
## Feature list compatibility
As previously stated, nearly all RouterOS systems can use the "Check for updates" functionality and upgrade to v7 in a few clicks, but there are some features, where extra steps may be required:
Feature | Status
----------------
CAPsMAN | OK
Interfaces | OK
Wireless | OK
Bridge/Switching | OK
Tunnels/PPP | OK
IPv6 | OK
BGP | OK, but attention is required*
OSPF | OK, but attention is required**
MPLS | OK, but attention is required***
Routing filters | OK, but attention is required****
PIM-SM | Seenotes
IGMP Proxy | OK
Tools | OK
Queues | OK
Firewall | OK
HotSpot | OK
Static Routing | OK
User Manager | Seenotes
Wireless
OK
BGP
OK, but attention is required*
Routing filters
PIM-SM
IGMP Proxy
Queues
OK
## Notes
## BGP
All known configurations will upgrade from 6.x to 7.x successfully. But keep in mind that there is a complete redesign of the configuration. v7 BGP implementation provides withconnection,templateandsessionmenus.
```
connection
```
```
template
```
```
session
```
Templatecontains all BGP protocol-related configuration options. It can be used as a template for dynamic peers and apply a similar config to a group of peers. Most of the parameters are similar to the previous implementation except that some are grouped in the output and input section making the config more readable and easier to understand whether the option is applied on input or output.
```
Template
```
BGPconnectionminimal set of parameters areremote.address,template,connect,listenandlocal.roleConnect and listen to parameters specify whether peers will try to connect and listen to a remote address or just connect or just listen. It is possible that in setups where peer uses the multi-hop connectionlocal.addressmust be configured too. Peer role is now a mandatory parameter, for basic setups, you can just use ibgp, ebgp.
```
connection
```
```
remote.address
```
```
template,connect
```
```
listen
```
```
local.role
```
```
local.address
```
Now you can monitor the status of all connected and disconnected peers from/routing bgp sessionmenu.Other great debugging information on all routing processes can be monitored from/routing statsmenu.
```
/routing bgp session
```
```
/routing stats
```
Networks are added to the firewall address-list and referenced in the BGPconnectionconfiguration.
```
connection
```
OSPF
All known configurations will upgrade from 6.x to 7.x successfully.OSPFv2 and OSPFv3 are now merged into one single menu/routing ospf. At the moment there are no default instances and areas. To start OSPF you need to create an instance and then add area to the instance.
```
/routing ospf
```
RouterOSv7 uses templates to match the interface against the template and apply configuration from the matched template. OSPF menusinterfaceandneighborcontains read-only entries for status monitoring.
```
interface
```
```
neighbor
```
MPLS
Upgrade MPLS setups with caution, and make sure to backup configuration before the upgrade.
Routing filters
All supported options are upgraded without any issue, in the case of an unsupported option - an empty entry is created. The routing filter configuration is changed to a script-like configuration.
The rule now can have "if .. then" syntax to set parameters or apply actions based on conditions from the "if" statement.
Multiple rules without action are stacked in a single rule and executed in order like a firewall, the reason is that the "set" parameter order is important, and writing one "set"s per line, allows for an easier understanding from top to bottom on what actions were applied.
More RouterOSv7 routing filter examples arehere.
PIM-SM
Upgrading RouterOS to v7 will not preserve PIM-related configuration. After the upgrade, multicast routing configuration will be available under the/routing/pimsmmenu and an additional "multicast" package is not required anymore. More information is availablehere.
```
/routing/pimsm
```
User Manager
RouterOSv7 provides the new and redesigned implementation of User Manager, configuration is now integrated into RouterOS WinBox and console (WEB admin configuration interface is not available), more information is availablehere. Direct migration from older User Manager is not possible, it is possible to migrate older database from/user-manager/database/migrate-legacy-dbHowever, it might be a good idea to start configuration from the scratch.
```
/user-manager/database/migrate-legacy-db
```
## New features
A New Kernel is implemented in RouterOSv7, which leads to performance changes due to route cache, as well some tasks might require higher CPU and RAM usage for different processes.
* completely new NTP client and server implementation
* merged individual packages, only bundle and a few extra packages remain(dropped support for LCD and KVM packages)
* new Command Line Interface (CLI) style (RouterOS v6 commands are still supported)
* support for Let's Encrypt certificate generation
* support for REST API
* support for UEFI boot mode on x86
* CHR FastPath support for "vmxnet3" and "virtio-net" drivers
* support for "Cake" and "FQ_Codel" type queues
* support for IPv6 NAT
* support for Layer 3 hardware acceleration on all CRS3xx devices
* support for MBIM driver with basic functionality support for all modems with MBIM mode
* support for MLAG on CRS3xx devices
* support for VRRP grouping and connection tracking data synchronization between nodes
* support for Virtual eXtensible Local Area Network (VXLAN)
* support for L2TPv3
* support for OpenVPN UDP transport protocol
* support for WireGuard
* support for hardware offloaded VLAN filtering on RTL8367 (RB4011, RB100AHx4) and MT7621 (hEX, hEX S, RBM33G) switches
* support for ZeroTier on ARM and ARM64 devices
* completely new alternative wireless package "wifiwave2" with 802.11ac Wave2, WPA3, and 802.11w management frame protection support (requires ARM CPU and 256MB RAM)
* support for hardware offloaded VLAN filtering on RTL8367 (RB4011, RB100AHx4) and MT7621 (hEX, hEX S, RBM33G) switches
* support CPU frequency scaling for x86 devices
## Dropped support
In RouterOS v7 has been dropped support for:
* LCD package
* KVM package