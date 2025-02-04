# Thread Information
Title: Thread-187759
Section: RouterOS
Thread ID: 187759

# Discussion

## Initial Question
Hi Guys, the Mikrotik device discovery tool on CRS326-24S+2Q+ and the broadcast daemon on hEX S have some issues when using VLAN with VLAN-Aware-Hardware. Both devices uses VLANs with the new configuration-style via BRIDGE-VLAN.So lets start with an example configuration on hEX S:bridge is native (pvid) on vlan 1580ether1 is native (pvid) on vlan 1580sfp1 is tagged with vlan 1580
```
/interfacebridgeaddadd-dhcp-option82=yes dhcp-snooping=yes fast-forward=noname=bridge1 protocol-mode=none pvid=1580vlan-filtering=yes/interfacebridge portaddbridge=bridge1 hw=nointerface=ether1 pvid=1580addbridge=bridge1 hw=nointerface=sfp1 pvid=1trusted=yes/interfacebridge settingssetallow-fast-path=nouse-ip-firewall=yesuse-ip-firewall-for-vlan=yes/ip neighbor discovery-settingssetdiscover-interface-list=!dynamic/interfacebridge vlanaddbridge=bridge1 tagged=sfp1 untagged=ether1 vlan-ids=1580Problem:hEXs Discovery Broadcast Daemon is only sending out the discovery frames on VLAN 1 instead of the bridge-interface. SFP1 is slave of bridge1 so the broadcast daemon should not send frames on a slave device.So lets start with an example configuration on CRS326-24S+2Q+:bridge is native (pvid) on vlan 1580bridge is tagged with vlan 1 and a vlan interface on bridge1 is addedcustomer-port is tagged with vlan 1580
```

```
/interfacebridgeaddadmin-mac=C4:AD:34:E3:73:70auto-mac=nocomment=defconf name=bridge protocol-mode=none pvid=1580vlan-filtering=yes/interfacevlanaddinterface=bridge name=vlan1.management vlan-id=1/interfacebridge portaddbridge=bridge ingress-filtering=yesinterface=sfp-sfpplus10/interfacebridge vlanaddbridge=bridge tagged="sfp-sfpplus10"vlan-ids=1580addbridge=bridge tagged=bridge vlan-ids=1Problem:This results in a neighbour list with interface name "vlan1.management" instead if the correspondencing switch interface (sfp-sfpplus10).This is the result of show neighs:
```

```
>ip neighborprintdetail1interface=vlan1.management address=172.16.18.70address4=172.16.18.70mac-address=2C:C8:1B:F3:88:01identity="cust.de.seeon.Altenmarkterstr-28.Wohnung-8.xxxxxxx"platform="MikroTik"version="6.49.1 (stable)"unpack=none age=22suptime=11w3d17h3m52ssoftware-id="RCHF-PT42"board="RB760iGS"interface-name="bridge1/sfp1"system-description="MikroTik RouterOS 6.49.1 (stable) RB760iGS"system-caps=bridge,router system-caps-enabled=bridge,router

---
```

## Response 1
There are numerous reports where implicitly defined interface lists don't work very well. Such as this configuration of yours:
```
/ip neighbor discovery-settingssetdiscover-interface-list=!dynamicTry to create explicit interface list and use it in this setting. Something like this:
```

```
/interfacelistaddname=MGMT/interfacelist membersaddlist=MGMTinterface=bridge1/ip neighbor discovery-settingssetdiscover-interface-list=MGMTBTW, my own preference is to use bridge as tagged-only entity whenever device is hit by VLANs ... so no pvid setting on brdigeinterface, rather use it as anchor for appropriate/interface vlanentity and making bridge tagged member of appropriate VLANs in/interface bridge vlan... this way it's entirely clear that we're talking aboutaccess window to particular VLANfor ROS.

---
```

## Response 2
Yeah, i had also thoughts this way, that i have to define an interface-list, but when i am doing this, then i can not see one single device in discovery.You are right, when not using PVID on bridge1, but using VLAN-Tagged on Bridge-Interface and adding a VLAN-Interface to bridge1 that will solve the issue. I also see that Beauvoir, but this is not the correct way it should go.In that fact, the MNDP / CDP Daemon has a wrong implementation. The daemon should aggregate more informations on how to send broadcast-messages on the correct Interface - so only send on Interfaces that are not slave.Mikrotiks hardware is VLAN-AWARE, why should i use CPU-VLAN instead of Hardware-VLAN-Capabilities, only because the MNDP/CDP is broken.This bug have to be fixed from the ROS-Team. ---

## Response 3
Does this problem still exist in Ros 7?I cannot delete PVID on the bridge interface. ---

## Response 4
Does this problem still exist in Ros 7?This problem never existed for me, neither in v6 nor in v7.I cannot delete PVID on the bridge interface.You can't delete PVID ... but if you set bridgeCPU-facing portwithframe-types=admit-only-vlan-tagged, then PVID setting will become irrelevant. After setting it, when running/interface/bridge/vlan/print, bridgeCPU-facing portis not listed as member of VID with same value as PVID any more. ---