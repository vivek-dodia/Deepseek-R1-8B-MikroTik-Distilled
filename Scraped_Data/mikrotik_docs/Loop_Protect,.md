---
title: Loop Protect
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/23396469/Loop+Protect,
crawled_date: 2025-02-02T21:10:19.269933
section: mikrotik_docs
type: documentation
---

The loop protect feature can prevent Layer2 loops by sending loop protect protocol packets and shutting down interfaces in case they receive loop protect packets originating from themselves. The feature works by checking the source MAC address of the received loop-protect packet against the MAC addresses of loop-protect enabled interfaces. If the match is found, loop protect disables the interface that received the loop protect packet. Log message warns about this event and the interface is marked with a loop protect comment by the system. The RouterOS loop protect feature can be used on bridged interfaces as well as on Ethernet interfaces which are set for switching in RouterBoard switch chips.
Loop Protect works on Ethernet, VLAN, EoIP, VxLAN interfaces and its packets are encapsulated with EtherType 0x9003.There the loop protect packet interval and interface disable time can be adjusted. Configuration changes or expiration of disable time, resets loop protection on an interface.
Sub-menu:/interface ethernet;/interface vlan;/interface eoip;/interface eoipv6; /interface vxlan
```
/interface ethernet;
```
```
/interface vlan;
```
```
/interface eoip;
```
```
/interface eoipv6; /interface vxlan
```
Property | Description
----------------------
loop-protect(on | off | default; Default:default) | Enables or disables loop protect on the selected interface.defaultworks as turned off.
loop-protect-send-interval(time interval; Default:5s) | Sets how often loop protect packets are sent on the selected interface.
loop-protect-disable-time(time interval | 0; Default:5m) | Sets how long the selected interface is disabled when a loop is detected.0- forever.
Read-only properties
Property | Description
----------------------
loop-protect-status(on | off | disable) | on- loop-protect feature is turned on, the interface is sending and listening for loop protect packetsoff- loop-protect feature is turned offdisable- loop-protect feature is turned on, the interface has received loop protect packet and disabled itself to prevent loop.
* on- loop-protect feature is turned on, the interface is sending and listening for loop protect packets
* off- loop-protect feature is turned off
* disable- loop-protect feature is turned on, the interface has received loop protect packet and disabled itself to prevent loop.