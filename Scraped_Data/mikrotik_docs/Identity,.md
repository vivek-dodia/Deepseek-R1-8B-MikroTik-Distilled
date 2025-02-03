---
title: Identity
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/40992856/Identity,
crawled_date: 2025-02-02T21:12:41.534611
section: mikrotik_docs
type: documentation
---

# Overview
Setting the System's Identity provides a unique identifying name for when the system identifies itself to other routers in the network and when accessing services such as DHCP, Neighbour Discovery, and default wireless SSID. The default system Identity is set to 'MikroTik'.
# Configuration
To set system identity in RouterOS:
```
[admin@MikroTik] > /system identity set name=New_Identity 
[admin@New_Identity] >
```
The current System Identity is always displayed after the logged-in account name and with the print command:
```
[admin@New_Identity] /system identity>print
name: New_Identity
[admin@New_Identity] /system identity>
```
## SNMP
It is also possible to change the router system identity by SNMP set command:
```
snmpset -c public -v 1 192.168.0.0 1.3.6.1.2.1.1.5.0 s New_Identity
```
snmpset- Linux based SNMP application used for SNMP SET requests to set information on a network entity;
* public- router's community name;
* 192.168.0.0- IP address of the router;
* 1.3.6.1.2.1.1.5.0- SNMP value for router's identity;