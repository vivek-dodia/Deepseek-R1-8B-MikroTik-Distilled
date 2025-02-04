# Thread Information
Title: Thread-1120008
Section: RouterOS
Thread ID: 1120008

# Discussion

## Initial Question
Is it possible to make configuration on Mikrotik like this (Cisco):
```
interfaceGigabitEthernet0/2.801description-NACNxxxxSPVLAN-801()---encapsulation dot1Q801second-dot1q801-4000interfaceGigabitEthernet0/2.802description-NACNxxxxSPVLAN-802()---encapsulation dot1Q802second-dot1q801-4000or like this (JUNOSe):
```

```
vlan bulk-config"spvlan_801-812"profile vlan bulk-config"spvlan_801-812""profile_vlan_base_nvsk"vlan bulk-config"spvlan_801-812"svlan-range8018128014000

---
```

## Response 1
http://wiki.mikrotik.com/wiki/Manual:In ... LAN#Q-in-Q ---

## Response 2
http://wiki.mikrotik.com/wiki/Manual:In ... LAN#Q-in-QWrong...Example in wiki is not like my examples... As you can see - Cisco config uses one S-VLAN and massive C-VLANs, or we can use any vlan id for C-VLAN and one S-VLAN. Juniper config is more complex - any combination is possible... ---

## Response 3
bda is looking for a way to have SP-vlans dynamically created, or created in blocks such as in the examples.This is a pretty common requirement, im suprised it's not already a feature. ---

## Response 4
bda is looking for a way to have SP-vlans dynamically created, or created in blocks such as in the examples.This is a pretty common requirement, im suprised it's not already a feature.Yes... I am waiting for this feature long time.... but no hope... ---

## Response 5
bda is looking for a way to have SP-vlans dynamically created, or created in blocks such as in the examples.This is a pretty common requirement, im suprised it's not already a feature.Yes... I am waiting for this feature long time.... but no hope...Sorry for bump, but any news? ---

## Response 6
Maybe put in a formal feature request tosupport@mikrotik.comand put it on the Feature Requests page on the wiki. ---

## Response 7
Any news about this in the new versions of RouterOS ? ---

## Response 8
there is no news about this? I checked a same request in a post of 2006, I don't know why mikrotik didn't develop this until now. ---