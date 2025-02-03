---
title: Default configurations
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/167706788/Default+configurations ,
crawled_date: 2025-02-02T20:25:11.640462
section: mikrotik_docs
type: documentation
---

* 1CPE Router
* 2LTE CPE AP router
* 3AP Router
* 4PTP Bridge, W60G Bridge:
* 5WISP Bridge
* 6Switch
* 7IP Only
* 8CAP
All MikroTik devices come with some kind of default configuration. There are several different configurations depending on board type:
* CPE Router;
* LTE CPE AP router;
* AP Router (single or dual-band);
* PTP Bridge,W60G Bridge(AP or CPE);
* WISP Bridge (AP in ap_bridge mode);
* Switch;
* IP Only;
* CAP.
You can run the command/system default-configuration printto see the exact applied default configuration commands.
```
/system default-configuration print
```
# CPE Router
In this type of configuration, the router is configured as a wireless client device. WAN interface is aWirelessinterface. WAN port has configured DHCP client, is protected by IP firewall and MAC discovery/connection is disabled.
List of routers using this type of configuration:
* RB 711,911,912,921,922 - with level3 license
* SXT
* QRT
* SEXTANT
* LHG
* LDF
* DISC
* Groove
* Metal
# LTE CPE AP router
This configuration type is applied to routers that have both LTE and wireless interfaces. LTE interface is considered a WAN port protected by a firewall and MAC discovery/connection disabled. The IP address on the WAN port is acquired automatically. Wireless is configured as an access point and bridged with all available Ethernet ports.
List of routers using this type of configuration:
* wAP LTE Kit
* SXT LTE
* LtAP 4G kit
* LtAP LTE kit
* Chateau
# AP Router
This type of configuration is applied to home access point routers to be used straight out of the box without additional configuration (except router passwords and wireless keys)
First Ethernet is always configured as a WAN port (protected by a firewall, enabled DHCP client, and disabled MAC connection/discovery). Other Ethernet ports and wireless interfaces are added to the local LAN bridge with 192.168.88.1/24 address set and configured DHCP server. In the case of dual-band routers, one wireless is configured as a 5 GHz access point and the other as a 2.4 GHz access point.
List of routers using this type of configuration:
* RB 450,751,850,951,953,2011,3011,4011
* hEX, PowerBox
* mAP
* wAP, wAP R (without LTE card)
* hAP
* cAP
* OmniTIK
* CRS series with wireless interface
* L009 series
* Audience
* Knot
* PWR
# PTP Bridge, W60G Bridge:
Bridged Ethernet with a wireless interface. The default IP address 192.168.88.1/24 is set on the bridge interface. There are two possible options - CPE and AP. For CPE wireless interface is set in "station-bridge" mode, and for AP "bridge" mode is used.W60G Bridge -This configuration type is applied to routers that have a 60 GHz point-to-point link.
List of routers using this type of configuration:
* DynaDish - as CPE
List of routers using this type of configuration:
* Cube, Cube Pro
* nRAY, Dish
* Wireless Wire Dish, nRAY, Cube, Cube Pro
* Wireless Wire kit
* wAP 60G - with level3 license
# WISP Bridge
The configuration is the same as PTP Bridge in AP mode, except that wireless mode is set to ap_bridge for PTMP setups. The router can be accessed directly using a MAC address. If the device is connected to the network with an enabled DHCP server, configured DHCP client configured on the bridge interface will get the IP address, that can be used to access the router.
List of routers using this type of configuration:
* RB 911,912,921,922 - with Level4 license
* Groove A, RB 711 A
* BaseBox, NetBox
* mANTBox, NetMetal
* wAP 60G AP - with level4 license
* LtAP
* CME
# Switch
This configuration utilizes switch chip features to configure a basic switch. All Ethernet ports are added to switch group and default IP address 192.168.88.1/24 is set on bridge interface.
List of routers using this type of configuration:
* FiberBox
* CRS without wireless interface
# IP Only
When no specific configuration is found, IP address 192.168.88.1/24 is set on ether1, or combo1, or sfp1.
List of routers using this type of configuration:
* RB 411,433,435,493,800,M11,M33,1100
* CCR
# CAP
This type of configuration is used when a device needs to be used as a wireless client device controlled byCAPsMAN.
When CAP default configuration is loaded, ether1 is considered a management port with DHCP client configured. All other Ethernet interfaces are bridged and wlan1 is set to be managed by CAPsMAN.
To load CAP configuration refer toReset Button manual.