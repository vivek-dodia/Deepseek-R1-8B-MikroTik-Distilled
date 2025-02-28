# Thread Information
Title: Thread-214291
Section: RouterOS
Thread ID: 214291

# Discussion

## Initial Question
When creating a MLAG on CRS3xx/CRS5xx (using RouterOS v7.15.x or later) series you normally:- Create a bond for the MLAG-PEER.- Configure "bridge mlag" to use the above as peer-port.- Define a pvid (for example 4094) on the MLAG-PEER interface to be used for ICCP traffic.- Define "mlag-id" for the LAGs to be the same on both devices (like when creating a LAG-UPLINK the LAG-UPLINK on both devices should be the same mlag-id).I assume the above gives that the "interface bridge add" should then have "frame-types=admit-all" rather than "frame-types=admit-only-vlan" if vlan-filtering is enabled?Or does that depend on how you choose to define the vlans?For example if this is being used:
```
/interfacebridge vlanaddbridge=bridge1 tagged=bridge1,MLAG-PEER,LAG-UPLINK,LAG-DOWNLINK vlan-ids=123That is can you use "frame-types=admit-only-vlan-tagged" for the bridge interface as long as you also define the ICCP pvid as being tagged such as this?
```

```
/interfacebridge vlanaddbridge=bridge1 tagged=bridge1,MLAG-PEER,LAG-UPLINK,LAG-DOWNLINK vlan-ids=4094Or should the ICCP always be untagged which gives if you use MLAG then the "interface bridge" shall always be "frame-types=admit-all"?

---
```

## Response 1
If vlan-filtering on bridge is disabled, then all the vlan-related stuff is ignored by bridge. Which means that PVID won't get applied to untagged frames on ingress, VLAN headr won't be stripped on egress and no vlan-filtering is done (so effectively asframe-types=admit-alland allowed VLANs are 1-4094).If you enable vlan-filtering on bridge, then PVID setting actually does have effect, also different frame-types settings. I strongly suggest you to go all-vlan, meaning no PVID on MLAG-peer interface (frame-types=admit-only-vlan-tagged) and for security reasons only VLAN IDs which are actually needed. And obviously configuration has to be identical on both sides of the link. ---

## Response 2
So something like this should then work?In below example LAG-UPLINK and LAG-DOWNLINK are untagged VLAN100:
```
/interfacebridgeaddframe-types=admit-only-vlan-tagged name=bridge1 vlan-filtering=yes/interfacebondingaddlacp-rate=1secmode=802.3adname=MLAG-PEER slaves=qsfpplus1-1,qsfpplus2-1transmit-hash-policy=layer-3-and-4/interfacebondingaddlacp-rate=1secmlag-id=101mode=802.3adname=LAG-UPLINK slaves=sfp-sfpplus1 transmit-hash-policy=layer-3-and-4/interfacebondingaddlacp-rate=1secmlag-id=102mode=802.3adname=LAG-DOWNLINK slaves=sfp-sfpplus2 transmit-hash-policy=layer-3-and-4/interfacebridge mlagsetbridge=bridge1 peer-port=MLAG-PEER/interfacebridge portaddbridge=bridge1 frame-types=admit-only-vlan-taggedinterface=MLAG-PEER pvid=4094/interfacebridge portaddbridge=bridge1 frame-types=admit-only-untagged-and-priority-taggedinterface=LAG-UPLINK pvid=100/interfacebridge portaddbridge=bridge1 frame-types=admit-only-untagged-and-priority-taggedinterface=LAG-DOWNLINK pvid=100/interfacebridge vlanaddbridge=bridge1 tagged=bridge1,MLAG-PEER vlan-ids=4094/interfacebridge vlanaddbridge=bridge1 tagged=bridge1,MLAG-PEER untagged=LAG-UPLINK,LAG-DOWNLINK vlan-ids=100While if I want VLAN 101 and 102 to be tagged (and not allow untagged traffic) on LAG-UPLINK and LAG-DOWNLINK then it should look like this (Im setting PVID to an unused VLAN)?
```

```
/interfacebridgeaddframe-types=admit-only-vlan-tagged name=bridge1 vlan-filtering=yes/interfacebondingaddlacp-rate=1secmode=802.3adname=MLAG-PEER slaves=qsfpplus1-1,qsfpplus2-1transmit-hash-policy=layer-3-and-4/interfacebondingaddlacp-rate=1secmlag-id=101mode=802.3adname=LAG-UPLINK slaves=sfp-sfpplus1 transmit-hash-policy=layer-3-and-4/interfacebondingaddlacp-rate=1secmlag-id=102mode=802.3adname=LAG-DOWNLINK slaves=sfp-sfpplus2 transmit-hash-policy=layer-3-and-4/interfacebridge mlagsetbridge=bridge1 peer-port=MLAG-PEER/interfacebridge portaddbridge=bridge1 frame-types=admit-only-vlan-taggedinterface=MLAG-PEER pvid=4094/interfacebridge portaddbridge=bridge1 frame-types=admit-only-vlan-taggedinterface=LAG-UPLINK pvid=100/interfacebridge portaddbridge=bridge1 frame-types=admit-only-vlan-taggedinterface=LAG-DOWNLINK pvid=100/interfacebridge vlanaddbridge=bridge1 tagged=bridge1,MLAG-PEER vlan-ids=4094/interfacebridge vlanaddbridge=bridge1 tagged=bridge1,MLAG-PEER untagged=LAG-UPLINK,LAG-DOWNLINK vlan-ids=101/interfacebridge vlanaddbridge=bridge1 tagged=bridge1,MLAG-PEER untagged=LAG-UPLINK,LAG-DOWNLINK vlan-ids=102

---
```

## Response 3
If you setframe-types=admit-only-vlan-tagged, thenpvidproperty of bridge port is entirely ignored ... so you can either leave it unset (in which case default setting of pvid=1 remains) or you can set it to some distinct unused value to have visual cue about that. Just be careful if you set same PVID to multiple ports and you happen to change frame-types setting, then those port suddenly start to allow untagged communication between devices connected to those ports.In below example LAG-UPLINK and LAG-DOWNLINK are untagged VLAN100:This part seems right to me.Also the next one is mostly fine (as explained, pvid setting will be ignored on both LAG-UPLINK and LAG-DOWNLINK) ... but I don't like see setting which might make sense if another property is set slightly differently ... I'd go with pvid=4093 on LAG-UPLINK and pvid=4092 on LAG-DOWNLINK ... just in case.But:While if I want VLAN 101 and 102 to be tagged (and not allow untagged traffic) on LAG-UPLINK and LAG-DOWNLINK then it should look like this (Im setting PVID to an unused VLAN)?<snip>/interface bridge vlan add bridge=bridge1 tagged=bridge1, MLAG-PEER untagged=LAG-UPLINK, LAG-DOWNLINK vlan-ids=101/interface bridge vlan add bridge=bridge1 tagged=bridge1, MLAG-PEER untagged=LAG-UPLINK, LAG-DOWNLINK vlan-ids=102you actually want to add LAG-UPLINK and LAG-DOWNLINK astaggedmembers of vlan-ids 101 and 102. ---