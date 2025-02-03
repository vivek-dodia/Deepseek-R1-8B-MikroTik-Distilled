---
title: /routing/id
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/59965506/routing+id,
crawled_date: 2025-02-02T21:12:24.337983
section: mikrotik_docs
type: documentation
---

Global Router ID election configuration. ID can be configured explicitly or set to be elected from one of the Routers IP addresses.
For each VRF table RouterOS adds dynamic ID instance, that elects the ID from one of the IP addresses belonging to a particular VRF:
```
[admin@rack1_b33_CCR1036] /routing/id> print 
Flags: D - DYNAMIC, I - INACTIVE
Columns: NAME, DYNAMIC-ID, SELECT-DYNAMIC-ID, SELECT-FROM-VRF
#   NAME   DYNAMIC-ID      SELECT-D   SELE
0 D main   111.111.111.2   only-vrf   main
```
### Configuration Options
Property | Description
----------------------
comment(string) | 
disabled(yes | no) | ID reference is not used.
id(IP) | Parameter to explicitly set the Router ID. If ID is not explicitly specified, then it can be elected from one of the configured IP addresses on the router. See parametersselect-dynamic-idandselect-from-vrf.
name(string) | Reference name
select-dynamic-id(any | lowest | only-active | only-loopback | only-static | only-vrf) | States what IP addresses to use for the ID election:any- any address found on the router can be elected as the Router ID.lowest- pick the lowest IP address.only-active- pick an ID only from active IP addresses.only-loopback- pick an ID only from loopback addresses (loopback address is considered any non point to point /32 address).only-vrf- pick an ID only from selected VRF. Works withselect-from-vrfproperty.
select-from-vrf(name) | VRF from which to select IP addresses for the ID election.
* any- any address found on the router can be elected as the Router ID.
* lowest- pick the lowest IP address.
* only-active- pick an ID only from active IP addresses.
* only-loopback- pick an ID only from loopback addresses (loopback address is considered any non point to point /32 address).
* only-vrf- pick an ID only from selected VRF. Works withselect-from-vrfproperty.
### Read-only Properties
Property | Description
----------------------
dynamic(yes | no) | 
dynamic-id(IP) | Currently selected ID.
inactive(yes | no) | If there was a problem to get a valid ID, then item can become inactive.