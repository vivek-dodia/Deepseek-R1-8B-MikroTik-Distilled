# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213227

# Discussion

## Initial Question
Author: Thu Dec 12, 2024 4:49 am
``` [apl@MikroTik] > /interface/export # 2024-12-11 18:43:11 by RouterOS 7.16.2 # software id = 3DR6-S8V2 # # model = RB5009UPr+S+ # serial number = HEB08KRC0AH /interface bridge add frame-types=admit-only-vlan-tagged ingress-filtering=no name=BridgeShared port-cost-mode=short vlan-filtering=yes add admin-mac=48:A9:8A:9F:B4:69 auto-mac=no comment=defconf name=bridge port-cost-mode=short /interface ethernet set [ find default-name=ether1 ] name="[0] WAN Uplink" set [ find default-name=sfp-sfpplus1 ] name="[1] LAN 10G" set [ find default-name=ether2 ] name="[2] LAN 1G" set [ find default-name=ether3 ] name="[3] ether3" set [ find default-name=ether4 ] name="[4] ether4" set [ find default-name=ether5 ] name="[5] ether5" set [ find default-name=ether6 ] name="[6] ether6" set [ find default-name=ether7 ] name="[7] ether7" set [ find default-name=ether8 ] name="[8] MGMT" /interface vlan add interface=BridgeShared name=VLAN-10 vlan-id=10 add interface=BridgeShared name=VLAN-20 vlan-id=20 add interface=BridgeShared name=VLAN-25 vlan-id=25 add interface=BridgeShared name=VLAN-60 vlan-id=60 add interface=BridgeShared name=VLAN-70 vlan-id=70 add interface=BridgeShared name=VLAN-100 vlan-id=100 /interface list add comment=defconf name=WAN add comment=defconf name=LAN /interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik /interface bridge port add bridge=bridge comment=defconf interface="[8] MGMT" internal-path-cost=10 path-cost=10 add bridge=BridgeShared frame-types=admit-only-vlan-tagged interface="[1] LAN 10G" internal-path-cost=10 path-cost=10 add bridge=BridgeShared frame-types=admit-only-vlan-tagged interface="[2] LAN 1G" internal-path-cost=10 path-cost=10 add bridge=BridgeShared frame-types=admit-only-vlan-tagged interface="[3] ether3" internal-path-cost=10 path-cost=10 add bridge=BridgeShared interface="[4] ether4" internal-path-cost=10 path-cost=10 pvid=20 add bridge=BridgeShared frame-types=admit-only-untagged-and-priority-tagged interface="[5] ether5" internal-path-cost=10 path-cost=10 add bridge=BridgeShared frame-types=admit-only-untagged-and-priority-tagged interface="[6] ether6" internal-path-cost=10 path-cost=10 add bridge=BridgeShared frame-types=admit-only-untagged-and-priority-tagged interface="[7] ether7" internal-path-cost=10 path-cost=10 /interface bridge vlan add bridge=BridgeShared tagged="BridgeShared,[1] LAN 10G,[2] LAN 1G,[3] ether3,[5] ether5,[6] ether6,[7] ether7" untagged="[4] ether4" vlan-ids=10, 20, 25, 60, 70, 100 /interface detect-internet set detect-interface-list=all /interface list member add comment=defconf interface=bridge list=LAN add comment=defconf interface="[0] WAN Uplink" list=WAN add interface=VLAN-20 list=LAN add interface=VLAN-100 list=LAN add interface=VLAN-60 list=LAN ``` Hello, I need to configure port "Ether3" in mixed mode: untagged VLAN 20 and tagged VLANs 10 and 100.I've configured port "ether 4" for untagged "vlan 20", but i need tagged vlans 100 and 10 as well.Please advise.I have:
```
---
```

## Response 1
Author: [SOLVED]Thu Dec 12, 2024 10:57 am
``` /interface bridge vlan add bridge=BridgeShared tagged="BridgeShared,[1] LAN 10G,[2] LAN 1G,[3] ether3,[5] ether5,[6] ether6,[7] ether7" untagged="[4] ether4" vlan-ids=10, 20, 25, 60, 70, 100 ``` ``` /interface bridge vlan add bridge=BridgeShared tagged="BridgeShared,[1] LAN 10G,[2] LAN 1G,[3] ether3,[4] ether4[5] ether5,[6] ether6,[7] ether7" vlan-ids=10, 25, 60, 70, 100 ``` ``` /interface bridge vlan add bridge=BridgeShared tagged="BridgeShared,[1] LAN 10G,[2] LAN 1G,[3] ether3,[5] ether5,[6] ether6,[7] ether7" untagged="[4] ether4" vlan-ids=20 ``` Clear theUntaggedlist from this entry (keep itempty), and remove VLAN ID 20 from it:
```
You should never list anything underUntaggedfor a/interface bridge vlanentry withmultipleVLAN IDs! Add "[4] ether4" to theTaggedlist of that entry. So that it becomes:
```

```
Then add a separate entry for VLAN ID 20
```

```
Personally, I never group multiple VLAN IDs in the same entry for/interface bridge vlan. I create one separate entry for each VLAN ID instead.


---
```

## Response 2
Author: Thu Dec 12, 2024 3:11 pm
Nothing wrong with grouping multiple vlan-ids on a /interface bridge vlan setting, IF all the tagged ports are identical and there are no untagged ports. ---

## Response 3
Author: Thu Dec 12, 2024 4:29 pm
Yeah, but if we now re-read his requirements from the first post again, we'll see that he only wanted VLAN 10 and 100 to be tagged for ether4. Which means we'll now need to split the entry that specifies the whole "10, 25, 60, 70, 100" list again. Not only in this case: Usually when you group many VLAN IDs into one entry, it might look compact at first, but it suffices that your requirements slightly change, like some VLANs need to be removed from some ports, and it quickly becomes a mess, where you have to split, merge and reshuffle everything.That why I prefer organizing the/interface bridge vlantable from the beginning on like atable, with the individual VLAN IDs as primary key. You'll have something that ressembles the grid of checkboxes that the other OSes (including SwOS) use for VLAN management. ---

## Response 4
Author: Thu Dec 12, 2024 9:38 pm
Personally, I never group multiple VLAN IDs in the same entry for/interface bridge vlan. I create one separate entry for each VLAN ID instead.Thank you, this is a good point!will test this solution today.