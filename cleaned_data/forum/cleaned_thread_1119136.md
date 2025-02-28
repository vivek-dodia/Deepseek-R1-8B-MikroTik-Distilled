# Thread Information
Title: Thread-1119136
Section: RouterOS
Thread ID: 1119136

# Discussion

## Initial Question
HelloI’m experiencing some puzzling behavior on a CRS326-24S+2Q+ running RouterOS 7.12.1, and I hope someone here might have insights. It's a simple setup and shouldn't really cause any problems. It's more or less just like the 'VLAN Example - Trunk and Access Ports' examplein the documentation found here. But there's obviously something at my end that's different but I cannot see it nor pinpoint it. Been at it for way to long and can't make sense of it.Any help is much appreciated.Here’s the situation:1. Setup OverviewOne trunk with two vlans (vlan10 and vlan475) connects to the MikroTikVLAN filtering is enabled.Two VLANs are configured:VLAN 475: Main client VLAN, operating on a 10GbE interface.VLAN 10: Auxiliary management VLAN, operating on multiple 1GbE interfaces.Both VLANs are tagged on a trunk port (qsfpplus2-1) connecting to a Cisco switch.2. Issues ObservedThroughput on VLAN 475 (10GbE)Incoming traffic reaches near 10Gbps, but outgoing traffic caps at ~400Mbps.CPU usage spikes to 50% during outbound traffic; profiling shows high usage in “Networking” (42%), “Unclassified” (24%), and “Bridging” (5.5%).Hardware offloading (hw=yes) is enabled for all interfaces.VLAN 10Devices on VLAN 10 can communicate locally but cannot access upstream networks, even though the gateway (192.168.47.1) is reachable.Outbound pings from VLAN 10 fail with “host unreachable,” despite correct routes and ARP entries.Sniffer shows ICMP packets entering the bridge with VLAN 10 but exiting the trunk without a tag.3. Troubleshooting Steps TakenVerified VLAN filtering and bridge port settings (pvid, ingress-filtering, frame-types) for all interfaces.Cleared ARP entries and ensured proper routes are set.Disabled IGMP snooping, checked firewall rules (none active), and ensured correct tagging on the Cisco trunk.Hardware offloading is active on all interfaces, but the CPU still processes traffic.4. QuestionsWhy does traffic on VLAN 475 cap at ~400Mbps outbound when hardware offloading is enabled?On VLAN 10, why do packets lose their tag on the trunk port and fail to reach the upstream gateway?Could there be additional steps to debug the high “Networking” CPU usage and ensure proper VLAN tagging on the trunk?Any guidance would be greatly appreciated! I’ve included relevant configs and outputs below. Please let me know if there’s more information I can provide.
```
/ip routeprint0As0.0.0.0/0192.168.47.1931DAc192.168.47.0/26vlan100DAc192.168.47.192/27vlan4750
```

```
/interfacebridge vlanprintdetailFlags:X-disabled,D-dynamic0bridge=bridge vlan-ids=475tagged=qsfpplus2-1,bridge untagged=""current-tagged=bridge,qsfpplus2-1current-untagged=sfp-sfpplus101bridge=bridge vlan-ids=10tagged=qsfpplus2-1,bridge untagged=sfp-sfpplus4,sfp-sfpplus2 current-tagged=bridge,qsfpplus2-1current-untagged=sfp-sfpplus2,sfp-sfpplus42D bridge=bridge vlan-ids=1tagged=""untagged=""current-tagged=""current-untagged=bridge
```

```
/interfacebridge portprintdetailwhereinterface=qsfpplus2-1interface=qsfpplus2-1bridge=bridge priority=0x80path-cost=10internal-path-cost=10edge=autopoint-to-point=autolearn=autohorizon=none hw=yesauto-isolate=norestricted-role=norestricted-tcn=nopvid=1frame-types=admit-only-vlan-tagged ingress-filtering=yes unknown-unicast-flood=yes unknown-multicast-flood=yes broadcast-flood=yes tag-stacking=nobpdu-guard=notrusted=nomulticast-router=temporary-query fast-leave=no
```

```
/tool sniffer quickinterface=sfp-sfpplus2 ip-protocol=icmpColumns:INTERFACE,TIME,NUM,DIR,SRC-MAC,DST-MAC,VLAN,SRC-ADDRESS,DST-ADDRESS,PROTOCOL,SIZE,CPU
INTERFACE     TIME   NUM  DIR  SRC-MAC            DST-MAC            VLAN  SRC-ADDRESS     DST-ADDRESS     PROTOCOL  SIZE  CPU
sfp-sfpplus27.2351->18:FD:74:49:FB:1EEC:71:DB:B7:7D:6710192.168.47.200192.168.47.45ip:icmp1020sfp-sfpplus27.2362<-EC:71:DB:B7:7D:6718:FD:74:49:FB:1E192.168.47.45192.168.47.200ip:icmp980sfp-sfpplus28.2413->18:FD:74:49:FB:1EEC:71:DB:B7:7D:6710192.168.47.200192.168.47.45ip:icmp1020sfp-sfpplus28.2414<-EC:71:DB:B7:7D:6718:FD:74:49:FB:1E192.168.47.45192.168.47.200ip:icmp980

---
```

## Response 1
No network diagram?Which vlan is the management or trusted vlan ---

## Response 2
I don't use a separate vlan for mgmt and instead in-band management and the ip of vlan475 (if that was what you meant?).Screenshot 2025-01-13 at 06.24.30.pngNo network diagram?Which vlan is the management or trusted vlan ---

## Response 3
/export file=anynameyouwish ( minus device serial number ) ---

## Response 4
```
# 2025-01-13 17:47:22 by RouterOS 7.12.1# software id = 4RZJ-MY29## model = CRS326-24S+2Q+/interfacebridgeaddadmin-mac=18:FD:74:49:FB:1Eauto-mac=nocomment=defconf name=bridge \
    vlan-filtering=yes/interfaceethernetset[finddefault-name=ether1]disabled=yesset[finddefault-name=qsfpplus1-1]disabled=yesset[finddefault-name=qsfpplus1-2]disabled=yesset[finddefault-name=qsfpplus1-3]disabled=yesset[finddefault-name=qsfpplus1-4]disabled=yesset[finddefault-name=qsfpplus2-1]advertise=40G-baseSR4-LR4,40G-baseCR4 \
    comment="*** trunk 40GbE * vlan475 ***"loop-protect=off \
    rx-flow-control=on tx-flow-control=onset[finddefault-name=sfp-sfpplus1]auto-negotiation=nodisabled=yes \
    speed=1G-baseXset[finddefault-name=sfp-sfpplus2]auto-negotiation=nocomment=\"*** cam01 * VLAN 10 ***"rx-flow-control=autospeed=1G-baseT-full \
    tx-flow-control=autoset[finddefault-name=sfp-sfpplus3]auto-negotiation=nodisabled=yesset[finddefault-name=sfp-sfpplus4]auto-negotiation=nocomment=\"*** env01 * VLAN 10 ***"speed=1G-baseT-fullset[finddefault-name=sfp-sfpplus5]disabled=yesset[finddefault-name=sfp-sfpplus6]disabled=yesset[finddefault-name=sfp-sfpplus7]disabled=yesset[finddefault-name=sfp-sfpplus8]disabled=yesset[finddefault-name=sfp-sfpplus9]disabled=yesset[finddefault-name=sfp-sfpplus10]auto-negotiation=nocomment=\"*** client vlan475 ***"rx-flow-control=on speed=10G-baseT \
    tx-flow-control=onset[finddefault-name=sfp-sfpplus11]disabled=yesset[finddefault-name=sfp-sfpplus12]disabled=yesset[finddefault-name=sfp-sfpplus13]disabled=yesset[finddefault-name=sfp-sfpplus14]disabled=yesset[finddefault-name=sfp-sfpplus15]disabled=yesset[finddefault-name=sfp-sfpplus16]disabled=yesset[finddefault-name=sfp-sfpplus17]disabled=yesset[finddefault-name=sfp-sfpplus18]disabled=yesset[finddefault-name=sfp-sfpplus19]disabled=yesset[finddefault-name=sfp-sfpplus20]disabled=yesset[finddefault-name=sfp-sfpplus21]disabled=yesset[finddefault-name=sfp-sfpplus22]disabled=yesset[finddefault-name=sfp-sfpplus23]disabled=yesset[finddefault-name=sfp-sfpplus24]auto-negotiation=nodisabled=yes/interfacevlanaddcomment="*** VLAN10 ***"interface=bridge name=vlan10 vlan-id=10addcomment="*** VLAN475 - 192.168.47.192/27 ***"\interface=bridge name=vlan475 vlan-id=475/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTik/portset0name=serial0/snmp communityset[finddefault=yes]disabled=yesaddaddresses=::/0authentication-protocol=SHA1 encryption-protocol=AES name=\
    mikrodicksucker security=authorized/interfacebridge portaddbridge=bridge comment=defconf disabled=yesinterface=ether1addbridge=bridge comment="*** client test * vlan475 ***"frame-types=\
    admit-only-untagged-and-priority-taggedinterface=sfp-sfpplus10 pvid=475addbridge=bridge comment="*** trunk to Cisco switch ***"\
    frame-types=admit-only-vlan-taggedinterface=qsfpplus2-1addbridge=bridge comment="*** PoE SWITCH for MISC DEVICES ***"frame-types=\
    admit-only-untagged-and-priority-taggedinterface=sfp-sfpplus2 pvid=10addbridge=bridge frame-types=admit-only-untagged-and-priority-tagged \interface=sfp-sfpplus4 pvid=10addbridge=bridge disabled=yes ingress-filtering=nointerface=all \
    multicast-router=disabled/interfacebridge vlanaddbridge=bridge tagged=qsfpplus2-1,bridge vlan-ids=475addbridge=bridge tagged=qsfpplus2-1,bridge untagged=\
    sfp-sfpplus4,sfp-sfpplus2 vlan-ids=10/ip addressaddaddress=192.168.47.194/27interface=vlan475 network=192.168.47.192addaddress=192.168.47.3/26interface=vlan10 network=192.168.47.0/ip routeadddistance=1dst-address=0.0.0.0/0gateway=192.168.47.193/system loggingaddtopics=interface,bridgeaddtopics=bridgeaddtopics=debug,bridge/system notesetshow-at-login=no/system routerboard settingssetboot-os=router-os/export file=anynameyouwish ( minus device serial number )

---
```

## Response 5
-Why do you not show spf-sfpplus4 connection on diagram???-Added ingress filtering to /interface bridge port settings-you have the wrong vlan tagged with the bridge, if 475 is your trusted vlan, then only it needs to have bridge tagged in /interface bridge vlan-not absolutely necessary but add sfp-sfpplus10 as untagged for 475. Its consistent with 10 config and I prefer to see the untaggings.....-ONLY the trusted vlan has an IP address- added a few items, single interface list etc...-cannot fathom what weird setup you have for network numbers for vlan475 ( but I trust my lack of knowledge means its just fine LOL)......
```
/interfacebridgeaddadmin-mac=18:FD:74:49:FB:1Eauto-mac=nocomment=defconf name=bridge \
    vlan-filtering=yes/interfaceethernetset[finddefault-name=ether1]name=OffBridge1comment="safe spot to configure"set[finddefault-name=qsfpplus1-1]disabled=yesset[finddefault-name=qsfpplus1-2]disabled=yesset[finddefault-name=qsfpplus1-3]disabled=yesset[finddefault-name=qsfpplus1-4]disabled=yesset[finddefault-name=qsfpplus2-1]advertise=40G-baseSR4-LR4,40G-baseCR4 \
    comment="*** trunk 40GbE * vlan475 ***"loop-protect=off \
    rx-flow-control=on tx-flow-control=onset[finddefault-name=sfp-sfpplus1]auto-negotiation=nodisabled=yes \
    speed=1G-baseXset[finddefault-name=sfp-sfpplus2]auto-negotiation=nocomment=\"*** cam01 * VLAN 10 ***"rx-flow-control=autospeed=1G-baseT-full \
    tx-flow-control=autoset[finddefault-name=sfp-sfpplus3]auto-negotiation=nodisabled=yesset[finddefault-name=sfp-sfpplus4]auto-negotiation=nocomment=\"*** env01 * VLAN 10 ***"speed=1G-baseT-fullset[finddefault-name=sfp-sfpplus5]disabled=yesset[finddefault-name=sfp-sfpplus6]disabled=yesset[finddefault-name=sfp-sfpplus7]disabled=yesset[finddefault-name=sfp-sfpplus8]disabled=yesset[finddefault-name=sfp-sfpplus9]disabled=yesset[finddefault-name=sfp-sfpplus10]auto-negotiation=nocomment=\"*** client vlan475 ***"rx-flow-control=on speed=10G-baseT \
    tx-flow-control=onset[finddefault-name=sfp-sfpplus11]disabled=yesset[finddefault-name=sfp-sfpplus12]disabled=yesset[finddefault-name=sfp-sfpplus13]disabled=yesset[finddefault-name=sfp-sfpplus14]disabled=yesset[finddefault-name=sfp-sfpplus15]disabled=yesset[finddefault-name=sfp-sfpplus16]disabled=yesset[finddefault-name=sfp-sfpplus17]disabled=yesset[finddefault-name=sfp-sfpplus18]disabled=yesset[finddefault-name=sfp-sfpplus19]disabled=yesset[finddefault-name=sfp-sfpplus20]disabled=yesset[finddefault-name=sfp-sfpplus21]disabled=yesset[finddefault-name=sfp-sfpplus22]disabled=yesset[finddefault-name=sfp-sfpplus23]disabled=yesset[finddefault-name=sfp-sfpplus24]auto-negotiation=nodisabled=yes/interfacelistaddname=TRUSTED/interfacevlanaddcomment="*** VLAN10 ***"interface=bridge name=vlan10 vlan-id=10addcomment="*** VLAN475 - 192.168.47.192/27 ***"\interface=bridge name=vlan475 vlan-id=475/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTik/portset0name=serial0/snmp communityset[finddefault=yes]disabled=yesaddaddresses=::/0authentication-protocol=SHA1 encryption-protocol=AES name=\
    mikrodicksucker security=authorized/interfacebridge portaddbridge=bridge comment="*** client test * vlan475 ***"ingress-filtering=yes frame-types=\
    admit-only-untagged-and-priority-taggedinterface=sfp-sfpplus10 pvid=475addbridge=bridge comment="*** trunk to Cisco switch ***"\
    ingress-filtering=yes frame-types=admit-only-vlan-taggedinterface=qsfpplus2-1addbridge=bridge comment="*** PoE SWITCH for MISC DEVICES ***"ingress-filtering=yes frame-types=\
    admit-only-untagged-and-priority-taggedinterface=sfp-sfpplus2 pvid=10addbridge=bridge ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged \interface=sfp-sfpplus4 pvid=10/interfacelist memberaddinterface=vlan457  list=TRUSTEDaddinterface=OffBridge1list=TRUSTED/interfacebridge vlanaddbridge=bridge tagged=bridge,qsfpplus2-1untagged=sfp-sfpplus10 vlan-ids=475addbridge=bridge tagged=qsfpplus2-1untagged=sfp-sfpplus4,sfp-sfpplus2 vlan-ids=10/ip addressaddaddress=192.168.47.194/27interface=vlan475 network=192.168.47.192comment="trusted vlan"addaddress=192.168.77.1/30interface=OffBridge1network=192.168.77.0comment="off bridge access"/ip routeadddistance=1dst-address=0.0.0.0/0gateway=192.168.47.193/ip dnsaddserver=192.168.47.193/ip neighbor discovery-settingssetdiscover-interface-list=TRUSTED/system loggingaddtopics=interface,bridgeaddtopics=bridgeaddtopics=debug,bridge/system notesetshow-at-login=no/system routerboard settingssetboot-os=router-os/system ntp clientsetenabled=yes/system ntp client serversaddaddress=192.168.47.193/tool mac-serversetallowed-interface-list=none/tool mac-server mac-winboxsetallowed-interface-list=TRUSTED....The additional address for ether1 simply means all you have to do is plug your laptop into ether1 on the switch, then change your IPV4 settings on the laptop to 192.168.77.2 and you should be able to access the router for config purposes safely off the bridge.

---
```

## Response 6
maybe in your switch the config end up doing L3 forwarding, if you need that you must configure L3 Hardware OffloadingL3 Hardware Offloadinghttps://help.mikrotik.com/docs/spaces/R ... Offloading ---

## Response 7
maybe in your switch the config end up doing L3 forwarding, if you need that you must configure L3 Hardware OffloadingL3 Hardware Offloadinghttps://help.mikrotik.com/docs/spaces/R ... Offloadingfor a 300 series switch??? What L3............... its all layer 2 ---

## Response 8
maybe in your switch the config end up doing L3 forwarding, if you need that you must configure L3 Hardware OffloadingL3 Hardware Offloadinghttps://help.mikrotik.com/docs/spaces/R ... Offloadingchechito! You're a genius!Thanks a bunch!That actually helped with the speed. Now near line speed in and out on that vlan. But that doesn't solve the vlan10 issues and the odd vlan tagging though. Thinking that I might have to abandon multiple vlans. But it shouldn't really be an issue or even hard. So strange.Screenshot 2025-01-13 at 21.03.35.pngScreenshot 2025-01-13 at 21.03.57.pngfor a 300 series switch??? What L3............... its all layer 2THis switch model is actually listed on that URL, and it did actually solve that issue. Still have the vlan tagging issue though and there is something that I have misconfigured that I'm not seeing. ---

## Response 9
I surrendered. That switch and this config have taken too much time of my life. I removed vlan10 and streamlined it to only run one vlan. I obviously missed something simple but the easy route (no pun intended) is to just deal with it and move on. ---

## Response 10
actually the switch setting is NOT needed, hw offloading happens automagically on the 326 when setting up bridge vlan filtering ---

## Response 11
I just helped a chap setup his 326 and it works like butta.Chechito needs stop eating some many chitos LOL, they are preventing synapses from firing. ---

## Response 12
actually the switch setting is NOT needed, hw offloading happens automagically on the 326 when setting up bridge vlan filteringThen something in my config was missed or there was/is a bug or something, it did not work properly until activated as per the instructions in that manual. ---

## Response 13
I just helped a chap setup his 326 and it works like butta.Cool! And do / did you see something in my config that differs that's a potential issue? ---

## Response 14
The setup I gave you is gold and will work 100%,Just work from an OffBridgePort to complete the configuration. ---

## Response 15
The setup I gave you is gold and will work 100%,Just work from an OffBridgePort to complete the configuration.Oh dang! Apologies. I had totally missed that you posted that. Will look at it. ---

## Response 16
No worries,,,,,,,,,, THe only thing I do not understand is the weird networking schema./ip addressadd address=192.168.47.194/27interface=vlan475 network=192.168.47.192comment="trusted vlan"I cannot netmask myself out of a paper bag and if it doesnt look like this, i get easily confusedadd address=192.168.47.194/24interface=vlan475 network=192.168.47.0comment="trusted vlan"IM sure its just fine!!and then the gateway being 192.168.47.193 LOL ( I would have expected 192.168.47.1 or 192.168.47.254 ) ---

## Response 17
So looks like ingress filtering on the brigde side of things might have been the issue then.I'll try to find the time to test that config. Many many many thanks for taking your time with this! Much appreciated.Sipcalc is your/our friend =)
```
sipcalc192.168.47.192/27-[ipv4:192.168.47.192/27]-0[CIDR]Hostaddress-192.168.47.192Hostaddress(decimal)-3232247744Hostaddress(hex)-C0A82FC0Networkaddress-192.168.47.192Networkmask-255.255.255.224Networkmask(bits)-27Networkmask(hex)-FFFFFFE0Broadcastaddress-192.168.47.223Ciscowildcard-0.0.0.31Addressesinnetwork-32Networkrange-192.168.47.192-192.168.47.223Usablerange-192.168.47.193-192.168.47.222Then, there's also some logic to the madness you pointed out regarding naming. 192.168.47.0/24 is vlan47, named after the third octet. But, that c-net is split in to multiple subnets. This one then being the fifth, which adds the 5 after 47... vlan475. So not only logical, but also intuitive.No worries,,,,,,,,,, THe only thing I do not understand is the weird networking schema./ip addressadd address=192.168.47.194/27interface=vlan475 network=192.168.47.192comment="trusted vlan"I cannot netmask myself out of a paper bag and if it doesnt look like this, i get easily confusedadd address=192.168.47.194/24interface=vlan475 network=192.168.47.0comment="trusted vlan"IM sure its just fine!!and then the gateway being 192.168.47.193 LOL  ( I would have expected     192.168.47.1   or   192.168.47.254 )

---
```