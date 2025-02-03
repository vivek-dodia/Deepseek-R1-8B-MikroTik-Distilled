---
title: Detect Internet
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/8323187/Detect+Internet,
crawled_date: 2025-02-02T21:14:50.802832
section: mikrotik_docs
type: documentation
---

# Introduction
Detect Internet is a tool that categorizes monitored interfaces into the following states -Internet,WAN,LAN,unknown, andno-link.
## State
This submenu displays status of all monitored interfaces defined by thedetect-interface-listparameter:
```
interface/detect-internet/state/print
```
## LAN
All layer 2 interfaces initially have this state.
## WAN
Any L3 tunnel and LTE interfaces will initially have this state. Layer 2 interfaces can obtain this state if the following conditions are met:
* an interface has an active route to 8.8.8.8 in main routing table.
* an interface can obtain (dynamic DHCP client is created) or has obtained an address from DHCP (does not apply if DHCP server is also running Detect Internet on the DHCP server interface).
## Internet
WANinterfaces that can reach cloud.mikrotik.com using UDP protocol port 30000 can obtain this state. Reachability is checked every minute. If a cloud is not reached for 3 minutes, the state falls back toWAN.
# Configuration
```
/interface detect-internet
```
Property | Description
----------------------
detect-interface-list(interface list; Default:none) | All interfaces in the list will be monitored by Detect Internet
internet-interface-list(interface list; Default:none) | Interfaces with state Internet will be dynamically added to this list
lan-interface-list(interface list; Default:none) | Interfaces with state Lan will be dynamically added to this list
wan-interface-list(interface list; Default:none) | Interfaces with state Wan will be dynamically added to this list
```
[admin@MikroTik] > interface/detect-internet/print 
detect-interface-list: none
lan-interface-list: none
wan-interface-list: none
internet-interface-list: none
[admin@MikroTik] > interface/detect-internet/set internet-interface-list=all wan-interface-list=all lan-interface-list=all detect-interface-list=all 
[admin@MikroTik] > interface/detect-internet/state/print 
Columns: NAME, STATE, STATE-CHANGE-TIME, CLOUD-RTT
# NAME STATE STATE-CHANGE-TIME CLO
0 ether1 internet dec/22/2020 13:46:18 5ms
```