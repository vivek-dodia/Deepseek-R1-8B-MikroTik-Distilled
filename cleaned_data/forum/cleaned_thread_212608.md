# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212608

# Discussion

## Initial Question
Author: Thu Nov 14, 2024 7:41 pm
``` 
```
/interfacebridgeaddauto-mac=noname=bridge port-cost-mode=shortvlan-filtering=yes/interfacevlanaddinterface=bridge name=vlan_Viesi vlan-id=20/interfacebridge portaddbridge=bridgeinterface=ether1internal-path-cost=10path-cost=10addbridge=bridgeinterface=ether2internal-path-cost=10path-cost=10addbridge=bridgeinterface=ether3internal-path-cost=10path-cost=10addbridge=bridgeinterface=ether4internal-path-cost=10path-cost=10addbridge=bridgeinterface=ether5internal-path-cost=10path-cost=10
```

```
```

```
addbridge=bridgeinterface=*4Apvid=20addbridge=bridgeinterface=*4Bpvid=20/interfacebridge vlanaddbridge=bridge tagged=bridge,ether1,ether2,ether3,ether4,ether5 vlan-ids=20
```

```
```

```
/interfacewifi datapathaddbridge=bridge name=DP_AC/interfacewifi securityaddauthentication-types=wpa2-.......*/interfacewifi configurationaddcountry=*****datapath=DP_AC disabled=nomode=ap name=MAIN-2Ghzsecurity=S*****a ssid=*****addchannel.skip-dfs-channels=all country=*****datapath=DP_AC disabled=nomode=ap name=MAIN-5Ghzsecurity=*****ssid=*****addcountry=*****datapath=DP_AC disabled=noname=Guest-2Ghzsecurity=*****ssid=*****addchannel.skip-dfs-channels=all country=*****datapath=DP_AC disabled=noname=Guest-5Ghzsecurity=*****ssid=*****
```

```
```

```
/interfacewifi capsmansetenabled=yesrequire-peer-certificate=noupgrade-policy=none/interfacewifi provisioningaddaction=create-dynamic-enabled disabled=nomaster-configuration=MAIN-2Ghzname-format=2Ghz-%I slave-configurations=Guest-2Ghzsupported-bands=2ghz-naddaction=create-dynamic-enabled disabled=nomaster-configuration==MAIN-5Ghzname-format=5Ghz-%I slave-configurations=Guest-5Ghz
```

Hi!With help fromhttps://help.mikrotik.com/docs/spaces/R ... onexample:I did manage perfectly fine wifi-qcom-ac environment where CAPsMAN is RB4011iGS+ which has no Wifi it self.In home environment I have Chateau 5G as main router and tried to move all CAP’s and Chateau itself on wifi-qcom-ac and . I successfully can get correct VLAN’s on CAP’s, but I cannot get VLAN on Chateau 5G itself. Is this even possible? Where is the catch?and here i have 1st problem. I did created under wifi1 wifi21, but it disappeared and bridge interface went as *4A./interface wifiadd disabled=no master-interface=wifi1 name=wifi21add disabled=no master-interface=wifi2 name=wifi22and untagged dispier.tried with and without this/interface wifi capset discovery-interfaces=bridge enabled=yes slaves-static=yes


---
```

## Response 1
Author: Thu Nov 14, 2024 8:31 pm
The intention is that local wifi interfaces are not provisiobed by CAPsMAN (running on same device). With new wifi, CAPsMAN and local wifi setup share same configuration profiles, one can apply same profile (e.g. security) both to CAPsMAN and local interfaces. Local radios will still work with other CAP devices with regard to mobility features (because it's the same wifi core process communicating both with local and remote radios). ---

## Response 2
Author: [SOLVED]Sun Dec 08, 2024 5:16 pm
``` 
```
/interfacelistaddname=wifiliste_guest/interfacebridge portaddbridge=bridgeinterface=wifiliste_guest pvid=20/interfacewifi datapathaddbridge=none disabled=nointerface-list=wifiliste_guest name=Local_VLAN
```

hi!With help form MT support as it turs out it can be achieved only after 7.17rc1.You should do as per instructions in help but with this twist on CAPsMANWhere add bridge=none is only CLI.And then this datapath is configured and provision only to local CAPsMAN wifi onlyMany thanks to MT support!
```