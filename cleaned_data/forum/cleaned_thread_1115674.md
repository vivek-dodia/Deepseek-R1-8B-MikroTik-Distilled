# Thread Information
Title: Thread-1115674
Section: RouterOS
Thread ID: 1115674

# Discussion

## Initial Question
Hi, i have a RB4011iGS+ (vers 7.16.2) - and following scenario:VLAN 1 (untagged vlan)VLAN 150 (guest)VLAN 160 (iot)trunk Port ether10 (uplink)trunk Port ether5 (downlink)accessPorts VLAN 160 - eth4, eth7, eth8accessPorts VLAN 150 - eth2Now when i create a VLAN Interface for 150 and put it to birdge1 and set up en DHCP Client there is no lease.When i put one for 160 all works great.I can Ping from the Box both gateways 150 and 160, but when i select the bridge the 150 won't ping when i set to vlan-eth-160 then i can ping both Gateway 150 and 160.I thought that on 7.1 and above i chan set up the vlan on bridge.But now i am confused. Or is the box done?I have reset the box to 0 and configured all once again. But no luck.Can somone give me a hint?ThxHuetty ---

## Response 1
Don't use VLAN ID 1...ever!Want to read more:viewtopic.php?t=143620 ---

## Response 2
I do not use VLAN 1 as tagged - my 'VLAN1' is always untagged so i have a untagged LAN and two tagged VLANS. In the GUI the dynamic VLAN untagged shows with No. 1.But thank you for the hint. I did read this before, but somehow is didn't recognize this section.Can it also make trouble, when i let one VLAN untagged?Thx for support!HuettyEdit: I didn't change the default PVID of the Interfaces in Bridge, so from here is the VLAN 1 - but why is there a 1 as default when it uses 0? ---

## Response 3
Before too much confusion, simply post your current config, sounds like you are fine./export file=anynameyouwish ( minus router serial#, any public WANIP information, keys etc. ) ---

## Response 4
Ok Thanks, here ist the configbest regardsHuetty ---

## Response 5
Lots of blank holes have to guess at as config is not clear in intentions.but assuming ethe1 is the wan port and the Bridge LAN, now vlan10 is the TRUSTED subnet.Where are the rest of the rules.......... firewall rules, dhcp server, pool etc..............Is this not a router facing the internet.......??? or did you mean for this solely to be a switch??
```
# model = RB4011iGS+# serial number = xxx/interfacebridgeaddingress-filtering=noname=bridge1 port-cost-mode=shortvlan-filtering=yes/interfaceethernetset[finddefault-name=ether2]comment=Stexxxset[finddefault-name=ether3]comment="Downlink 66-3"set[finddefault-name=ether4]comment=Jaxxset[finddefault-name=ether5]comment="wlan IOT"set[finddefault-name=ether6]comment="Bxx"set[finddefault-name=ether7]comment=Doxxset[finddefault-name=ether10]comment="Uplinkxxx"/interfacevlanaddinterface=bridge1 name=vlan150 vlan-id=150addinterface=bridge1 name=vlan160 vlan-id=160addinterface=bridge1 name=VLAN10-lan vlan-id=10/portset0name=serial0set1name=serial1/interfacebridge portaddbridge=bridge1 ingress-filtering=yes frame-type=admit-only-priority-and-untaggedinterface=ether2  pvid=150addbridge=bridge1 ingress-filtering=yes frame-type=admit-only-priority-and-untaggedinterface=ether3 pvid=10addbridge=bridge1 ingress-filtering=yes frame-type=admit-only-priority-and-untaggedinterface=ether4  pvid=160addbridge=bridge1 ingress-filtering=yes frame-type=admit-only-vlan-taggedinterface=ether5 comment="trunk port to???"addbridge=bridge1 ingress-filtering=yes frame-type=admit-only-priority-and-untaggedinterface=ether6 pvid=10addbridge=bridge1 ingress-filtering=yes frame-type=admit-only-priority-and-untaggedinterface=ether7  pvid=160addbridge=bridge1 ingress-filtering=yes frame-type=admit-only-priority-and-untaggedinterface=ether8  pvid=160addbridge=bridge1 ingress-filtering=yes frame-type=admit-only-priority-and-untaggedinterface=ether9  pvid=10addbridge=bridge1 ingress-filtering=yes frame-type=admit-only-vlant-taggedinterface=ether10  comment="trunk port to???"/ip firewall connection trackingsetudp-timeout=10s/interfacebridge vlanaddbridge=bridge1 tagged=bridge1,ether5,ether10  untagged=ether3,ether6,ether9  vlan-ids=10comment="management/trusted vlan"addbridge=bridge1 tagged=bridge1,ether5,ether10,untagged=ether2 vlan-ids=150addbridge=bridge1 tagged=bridge1,ether5,ether10,untagged=ether4,ether7,ether8 vlan-ids=160/interfaceovpn-server serversetauth=sha1,md5/ip dhcp-clientadddisabled=yesinterface=vlan160adddisabled=yesinterface=vlan150/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/system identitysetname=Hallxxx/system note

---
```

## Response 6
Sorry about that.Yes it is just used as a switch. The uplink ist eth10 (to an Wifi 60G) - behind the 60G the vlan 150 is OK and works. The device is connected to 60 G Wlan an then comes the network with the WAN Port and Firewall.The vlan 160 is for iot devices, the 150 for guest and '1' is the LAN.Now i have configured to use vlan 160 so i can move on with the work, but i want to give our employees the guest Network (vlan 150) as WLAN.Sorry that i didn't write this sooner. ---

## Response 7
So the MT device incoming trunk port (from upstream) is on etherX and on that port incoming is 2 vlans and 1 untagged flow of data?So its getting a hybrid port from the 60G?Is there a trunk port exiting the MT device, aka is it feeding any other smart devices and if so which ports......Assuming your LAN is the trusted subnet........ ---