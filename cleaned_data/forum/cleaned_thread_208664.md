# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 208664

# Discussion

## Initial Question
Author: Sat Jun 22, 2024 2:40 pm
``` ############################################################################### # Topic: Using RouterOS to VLAN your network # Example: Router-Switch-AP all in one device # Web: https://forum.mikrotik.com/viewtopic.php?t=143620 # RouterOS: 6.47.10 # Date: February 17, 2023 # Notes: Start with a reset (/system reset-configuration) # Thanks: mkx, sindy ############################################################################### .... ####################################### # VLAN Security ####################################### # Only allow ingress packets without tags on Access Ports /interface bridge port set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether2] set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether3] set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether4] set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether5] set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=wlan1] set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=wlan2] ``` Update: So all appears to work as desired.if I do a torch on the wifi interface then the traffic indeed is tagged as VLAN id 12. So allowing only tagged traffic is the right option.So now why is that correct? I tried to understand VLANs mainly by this guide:viewtopic.php?t=143620However in the RouterSwitchAP post there is clearly "admit-only-untagged-and-priority-tagged" selected. What was my oversight here?
```
Edit: I'll mark this as answered as soon as I understand why the "frame-types" setting is inverted to my expectation.
```