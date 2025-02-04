# Thread Information
Title: Thread-1123152
Section: RouterOS
Thread ID: 1123152

# Discussion

## Initial Question
Topology :R1 (ether2) <> (ether1) R2 (ether2) <> (ether2) R3
```
---R1Config:---/interfacevlanaddinterface=ether2 name=vlan1111 vlan-id=1111/ip addressaddaddress=192.168.251.1/30interface=vlan1111 network=192.168.251.0---R2Config:---/interfacebridgeaddname=bridge1/interfacebridge portaddbridge=bridge1 frame-types=admit-only-untagged-and-priority-taggedinterface=ether1 pvid=1111/interfacebridge portaddbridge=bridge1 frame-types=admit-only-vlan-taggedinterface=ether2 pvid=69/interfacebridge vlanaddbridge=bridge1 tagged=ether2 untagged=ether1 vlan-ids=1111/interfacebridge vlanaddbridge=bridge1 tagged=ether2,bridge1 vlan-ids=69/interfacevlanaddinterface=bridge1 name=Managementvlan-id=69/ip addressaddaddress=192.168.252.2/28interface=Managementnetwork=192.168.252.0/ip routeaddgateway=192.168.252.1---R3Config:---/interfacebridgeaddframe-types=admit-only-vlan-tagged name=bridge1 protocol-mode=mstp pvid=69vlan-filtering=yes/interfacevlanaddinterface=bridge1 name=Managementvlan-id=69/interfacevlanaddinterface=bridge1 name=vlan1111 vlan-id=1111/interfacebridge portaddbridge=bridge1 frame-types=admit-only-vlan-taggedinterface=ether2 pvid=69/interfacebridge vlanaddbridge=bridge1 tagged=bridge1,ether2 vlan-ids=1111/interfacebridge vlanaddbridge=bridge1 tagged=ether2,bridge1 vlan-ids=69/ip addressaddaddress=192.168.251.2/30interface=vlan1111 network=192.168.251.0/ip addressaddaddress=192.168.252.1/28interface=Managementnetwork=192.168.252.0/ip firewall nataddaction=src-nat chain=srcnat src-address=192.168.252.0/28to-addresses=192.168.251.2/ip routeaddgateway=192.168.251.1Achieve :R3 can ping to R1Problem :With this config everything works, i can ping from R3 to R1, but when i set vlan-filtering=yes in R2, ping from R3 to R1 fail immediately, why is it ?

---
```

## Response 1
I dont look at part configs so all three are needed and what is the relationship and type of devices R1, R2, R3/export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc.)ensure also you read this guidance on vlans:viewtopic.php?t=143620 ---

## Response 2
I dont look at part configs so all three are needed and what is the relationship and type of devices R1, R2, R3/export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc.)ensure also you read this guidance on vlans:viewtopic.php?t=143620Thank you for coming, I've put all of the config inside the code, it start with the --- R1 Config : --- --- R2 Config : --- --- R3 Config : ---Could you recheck. ---

## Response 3
I dont look at part configs so all three are needed and what is the relationship and type of devices R1, R2, R3/export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc.)ensure also you read this guidance on vlans:viewtopic.php?t=143620Thank you for coming, I've put all of the config inside the code, it start with the --- R1 Config : --- --- R2 Config : --- --- R3 Config : ---Could you recheck.Solved by research and reading, thanks. ---