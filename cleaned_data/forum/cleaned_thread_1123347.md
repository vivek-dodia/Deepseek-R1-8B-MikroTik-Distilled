# Thread Information
Title: Thread-1123347
Section: RouterOS
Thread ID: 1123347

# Discussion

## Initial Question
Hello all, I have a CCR as my root bridge and 2 CRS switches connected to it. The CRS switches are not connected to each other.Both CRS switches have a port-channel (bond) to the CCR. When 1 crs switch is connected to the ccr only, connectivity is fine. As soon as I connect the 2nd crs switch to the CCR, STP starts discarding traffic, then listens and forwards. It just goes in a constant circle. There is no physical loop so I'm not sure what is going on.I do have the bridge priority set on the CCR so that it becomes the root bridge but I don't believe anything else needs to be done.Can anyone give some insight?Screenshots attached showing the packetloss at the exact same time as well as the log showing the stp states. ---

## Response 1
Quick update:I removed the bond on the 2nd crs switch that goes to the CCR. Then things started working properly and spanning tree wasn't discarding traffic anymore...Does mikrotik not like having more than one bond?The CCR is currently on 7.8 and CRS's on 6.49.17. ---

## Response 2
Genrally multiple bonds work fine on ROS devices. So it might be domething about how you set them up ... both on CCR and both CRSes.If you post config from all 3 devices (the /interface part will probably be enough), we may spot domething off ... ---

## Response 3
CCR Interface export when both bonds were active and causing issues
```
/interface/bridge>printFlags:X-disabled,R-running0R name="bridge"mtu=autoactual-mtu=1500l2mtu=1596arp=enabled arp-timeout=automac-address=18:FD:74:B3:3C:BC protocol-mode=rstp fast-forward=yes 
     igmp-snooping=noauto-mac=yes ageing-time=5mpriority=0x8000max-message-age=20sforward-delay=15stransmit-hold-count=6vlan-filtering=yes 
     ether-type=0x8100pvid=1frame-types=admit-all ingress-filtering=yes dhcp-snooping=no/interfacebridgeaddname=bridge vlan-filtering=yes/interfacebondingaddmode=802.3adname=Po1slaves=ether15,ether16addmode=802.3adname=Po2slaves=ether13,ether14/interfacebridge portaddbridge=bridgeinterface=sfp-sfpplus1addbridge=bridgeinterface=sfp-sfpplus2addbridge=bridgeinterface=Po1addbridge=bridgeinterface=Po2CRS #1 Interface export
```

```
/interfacebridgeprintFlags:X-disabled,R-running0R name="bridge"mtu=autoactual-mtu=1500l2mtu=1584arp=enabled arp-timeout=automac-address=DC:2C:6E:BA:22:9Cprotocol-mode=rstp fast-forward=yes igmp-snooping=noauto-mac=yes ageing-time=5mpriority=0xFFFFmax-message-age=20sforward-delay=15stransmit-hold-count=6vlan-filtering=yes ether-type=0x8100pvid=1frame-types=admit-all ingress-filtering=nodhcp-snooping=no/interfacebondingaddmode=802.3adname=Po1slaves=ether23,ether24CRS #2 Interface export
```

```
/interfacebridgeprintFlags:X-disabled,R-running0R;;;defconf
     name="bridge"mtu=autoactual-mtu=1500l2mtu=1592arp=enabled arp-timeout=automac-address=48:A9:8A:21:8A:1Aprotocol-mode=rstp fast-forward=yes igmp-snooping=noauto-mac=noadmin-mac=48:A9:8A:21:8A:1Aageing-time=5mpriority=0xFFFFmax-message-age=20sforward-delay=15stransmit-hold-count=6vlan-filtering=yes ether-type=0x8100pvid=1frame-types=admit-all ingress-filtering=nodhcp-snooping=no/interfacebondingaddmode=802.3adname=Po1slaves=ether23,ether24

---
```

## Response 4
Why is the CRS priority set to 0xFFFF? The standard requires the lower 12 bits to be zero, e.g. 0xF000 to be the lowest priority. ---