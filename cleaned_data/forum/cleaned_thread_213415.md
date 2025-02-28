# Thread Information
Title: Thread-213415
Section: RouterOS
Thread ID: 213415

# Discussion

## Initial Question
Hi, I created a 802.03ad bonding on 3 interfaces, then tag it to a VLAN, and I need to apply a CoS priority on some packets :set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no loop-protect=off \name=ONT speed=2.5G-baseX/interface bondingadd lacp-rate=1sec mode=802.3ad name=Router slaves=ether3, ether5, ether7 \transmit-hash-policy=layer-2-and-3The issue is that the bond is not usable like a port in the switch rules; so for having the priority and today I use a bridge filter which is not the best case as all packets have the priority applied./interface bridge vlanadd bridge=bridgeWAN tagged=Router, ONT vlan-ids=832add bridge=bridgeWAN tagged=Router, ONT vlan-ids=840/interface bridge filteradd action=set-priority chain=forward mac-protocol=vlan new-priority=6 \passthrough=yes vlan-id=832Do anybody knows how to not use the bridge filter to apply the new priority only on ARP and DHCP packets ? ---

## Response 1
Unfortunately, bridge filter rules cannot match on the IP and TCP/UDP headers inside VLAN-tagged frames, so you would have to create a separate bridge for each VLAN to be able to set the priority field value for DHCP in particular. But what Mikrotik model are we talking about? Maybe it supports switch chip rules that could be used for this, as these often allow to match port numbers in VLAN-tagged frames? ---

## Response 2
I'm using a CRS326-24G-2S+ ---

## Response 3
Try/interface ethernet switch ruleadd switch=switch1 ports=ether3, ether5, ether7 vlan-id=852 mac-protocol=arp new-vlan-priority=6add switch=switch1 ports=ether3, ether5, ether7 vlan-id=852 protocol=udp dst-port=67 new-vlan-priority=6At worst it will just not work. ---

## Response 4
looks like in 7.17 will be possiblehttps://mikrotik.com/download/changelogsWhat's new in 7.17rc3 (2024-Dec-10 09:40):..*) switch - allow bond interfaces in switch rules for CRS3xx, CRS5xx, CCR2116 and CCR2216 devices;documentation also was updatedhttps://help.mikrotik.com/docs/spaces/R ... Rules(ACL) ---