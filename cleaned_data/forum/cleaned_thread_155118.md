# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 155118

# Discussion

## Initial Question
Author: Sat Dec 28, 2019 6:46 pm
``` /interface bridge add name=bridge /interface bridge port add bridge=bridge interface=ether1 hw=yes add bridge=bridge interface=sfp-sfpplus1 hw=yes add bridge=bridge interface=sfpplus2 hw=yes /interface ethernet switch ingress-vlan-translation add ports=ether1 customer-vid=0 new-customer-vid=1 sa-learning=yes add ports=sfp-sfpplus1 customer-vid=0 new-customer-vid=1 sa-learning=yes add ports=sfpplus2 customer-vid=0 new-customer-vid=1 sa-learning=yes /interface ethernet switch egress-vlan-tag add tagged-ports=ether1sfp-sfpplus1, sfpplus2 vlan-id=1 add tagged-ports=ether1, sfp-sfpplus1, sfpplus2 vlan-id=2 /interface ethernet switch vlan add ports=ether1, sfp-sfpplus1, sfpplus2 vlan-id=1 learn=yes add ports=ether1, sfp-sfpplus1, sfpplus2 vlan-id=2 learn=yes /interface vlan add interface=bridge vlan-id=1 name=vlan1 add interface=bridge vlan-id=2 name=vlan2 /ip address add address=192.168.2.254/24 interface=vlan2 /interface ethernet switch set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether1, sfp-sfpplus1, sfpplus2 ``` Hi, after spending many hours, in which I crashed my home network many times, I need your help. I want to configure one new VLAN in addition to my existing untagged VLAN. Both networks should be able to communicate via InterVLAN Routing through my RouterOS switch. I'm using multiple SwOS switches and one RouterOS switch.Issues:- Clients in VLAN 2, connected to my SwOS access switch, are not able to reach the RouterOS IP in VLAN 2- Connection of untagged traffic stops working, as soon as I configure "set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports"Physical connection of my hardware, used for testing:- PC in untagged VLAN --> Mikrotik CRS305 (SwOS) --> Mikrotik CRS210 (RouterOS) --> Internet Gateway- PC in VLAN 2 --> Mikrotik CRS305 (SwOS) --> Mikrotik CRS210 (RouterOS) --> Internet Gateway- Both PCs connected to the same Access Switch, SwOS VLAN config worksSwOS Config (Access Switch on RouterOS port sfp-sfpplus1)- Port 1 (ETH0) = PC untagged in VLAN 2- Port 2 (SFP1) = PC untagged (should be VLAN 1, since PVID is 1?)- Port 3 (SFP2) = Uplink to RouterOSRouterOS Config- Port ether1 = Uplink to Internet GW- Port sfp-sfpplus1= Uplink to my first SwOS switch- Port sfpplus2= Uplink to my second SwOS switch
```
Following guide was used for my RouterOS configuration:https://wiki.mikrotik.com/wiki/Manual:B ... s_switches


---
```

## Response 1
Author: [SOLVED]Tue Dec 31, 2019 11:05 am
Problem solved.It was needed to add "switch1-cpu", to get InterVLAN routing working.Following config changes were made:# Add VLAN to ports/interface ethernet switch vlanadd ports=switch1-cpu, ether1, sfp-sfpplus1, sfpplus2 vlan-id=1 learn=yesadd ports=switch1-cpu, ether1, sfp-sfpplus1, sfpplus2 vlan-id=2 learn=yes# Add trunk ports/interface ethernet switch egress-vlan-tagadd tagged-ports=switch1-cpu, ether1sfp-sfpplus1, sfpplus2 vlan-id=1add tagged-ports=switch1-cpu, ether1, sfp-sfpplus1, sfpplus2 vlan-id=2