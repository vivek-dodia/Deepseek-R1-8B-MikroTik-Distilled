# Thread Information
Title: Thread-213797
Section: RouterOS
Thread ID: 213797

# Discussion

## Initial Question
Hi, I want to connect a access point with 3 VLANs to one port oy my Mikrotik for testing.On the access point I configured the 3 VLANs as tagged.On the Mikrotik RB3011 I did the same.But when I change IP address to the VLAN interface (in menu addresses), the connection will be lost.Is there a tutorial with whole configuration?Thanks, very much. ---

## Response 1
When using Winbox in the normal way (using IP address) it is common to get kicked out when changing VLAN settings.Use Winbox MAC address or remove 1 port from your router off bridge and configure from there (setup small DHCP server on that port or again, use Winbox via MAC address). ---

## Response 2
The workflow I've settled on when making changes like you've described is to configure a management VLAN, set one of the physical router ports to be untagged on that VLAN, and connect my workstation to that physical port. Then I can change the other VLAN configurations to my heart's content without ever losing my connection. ---

## Response 3
Brand/Model of Access point?Config of MT router ( and ap if mt)/export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc. ) ---

## Response 4
UniFi: vlan 1, 400, 401 (tagged)Mikrotik port 4: tagged with vlan 1, 400, 401.vlan 400 and vlan 401 works fine (seperated dhcp servers on Mikrotik interfaces)But vlan 1 does not work - i I bind the ip address on Mikrotik to vlan 1 interface, the connection to the Unifi will be lost. ---

## Response 5
Why vlan1 on the unifi?Unifi typically accepts whatever traffic is coming to it untagged as the trusted or management vlan and the tagged vlans as data vlans.Therefore on the MT suggest you use three vlans and forget about using vlan1 for anything ( it works in the background )vlan10 - home ( wired and wireless)vlan20 - guest (wireless)vlan99 ( management)_ --- or simply use vlan10 as trusted vlan and dont use a management vlan.In all smart devices connected to MT router get their IP address on the management or trusted vlan.So unless you change ubiquiti default to something else, you will need to create a hybrid port on the MT to match the hybrid nature of the ubiquiti.Option One, with separate Management VLAN/interface bridge portadd bridge=bridge ingress-filtering=yes frame-types=admit-only-priority-and-untagged interface=ether2 pvid=10 comment="home PC - access port"add bridge=bridge ingress-filtering=yes frame-types=admit-only-vlan-tagged interface=ether3 comment="managed switch - trunk port"add bridge=bridge interface=ether4 pvid=99 comment="hybrid port to ubiquiti AP"add bridge=bridge ingress-filtering=yes frame-types=admit-only-priority-and-untagged interface=WLAN1 pvid=10 comment="home wifi 5ghz"add bridge=bridge ingress-filtering=yes frame-types=admit-only-priority-and-untagged interface=WLAN2 pvid=10 comment="home wifi 2ghz"/interface bridge vlanadd bridge=bridge tagged=bridge, ether3, ether4 untagged=ether2, WLAN1, WLAN2 vlan-ids=10add bridge=bridge tagged=bridge, ether3, ether4 vlan-ids=20add bridge=bridge tagged=bridge, ether3 untagged=ether4 vlan-id=99Option Two, using vlan10 as trusted vlan/interface bridge portadd bridge=bridge ingress-filtering=yes frame-types=admit-only-priority-and-untagged interface=ether2 pvid=10 comment="home PC - access port"add bridge=bridge ingress-filtering=yes frame-types=admit-only-vlan-tagged interface=ether3 comment="managed switch - trunk port"add bridge=bridge interface=ether4 pvid=10 comment="hybrid port to ubiquiti AP"add bridge=bridge ingress-filtering=yes frame-types=admit-only-priority-and-untagged interface=WLAN1 pvid=10 comment="home wifi 5ghz"add bridge=bridge ingress-filtering=yes frame-types=admit-only-priority-and-untagged interface=WLAN2 pvid=10 comment="home wifi 2ghz"/interface bridge vlanadd bridge=bridge tagged=bridge, ether3 untagged=ether2, ether4, WLAN1, WLAN2 vlan-ids=10add bridge=bridge tagged=bridge, ether3, ether4 vlan-ids=20The ubiquiti and managed switch in the above scenarios will either get an IP on the managerment subnet, or if none, the trusted subnet. ---

## Response 6
The issue is likely due to misconfigured VLAN tagging or missing bridge VLAN filtering. ---

## Response 7
UniFi: vlan 1, 400, 401 (tagged)Mikrotik port 4: tagged with vlan 1, 400, 401."Native VLANs" (whatever that means) should never be tagged on wires ... also devices on both ends of same cable have to have same config ... and in your case UniFi has "native" (whichever that is) VLAN untagged and you configured MT to pass VLAN 1 tagged. ---

## Response 8
Thanks for all the answers.VLAN 1 is the defautl setting on Unifi - I could not find an option that the configuration should be able via other VLAN.I tried following Mikrotik's bridges, because I thought that Unifi should hae a trunk connection with all 4 VLANS to the Mikrotik.
```
BridgeVLANIDscurrent tagged		current untagged001001vlan_001001400400vlan_400400401401vlan_401401402402vlan_402402If I set no static VLAN bridges, there will be added dynamically bridges.
```

```
BridgeVLANIDscurrent tagged		current untagged
xxx	xxx					vlan_xxx,xxxIn this case every VLAN gets it's own subnet and IP addresses from Mikrotik but all VLANS comes untagged to the Mikrotik port.But when I try to change the interface of ether4 (port to the Unifi access point) from the physical ether4 to VLAN 100 interface, I loose the connectio n to the Unifi.MT.png

---
```

## Response 9
UniFi: vlan 1, 400, 401 (tagged)Mikrotik port 4: tagged with vlan 1, 400, 401.vlan 400 and vlan 401 works fine (seperated dhcp servers on Mikrotik interfaces)But vlan 1 does not work - i I bind the ip address on Mikrotik to vlan 1 interface, the connection to the Unifi will be lost.Unifi expects VLAN 1 to be untagged on wire (because that's how it is with "native VLANs") ... so if you're using VLAN 1 on mikrotik (by default it's untagged on all ports and bridge so it should work just fine), then it should be untagged on ether4 (i.e. set pvid=1 and frame-types=admit-all ... both settings are default and thus not shown in export and possibly also in GUIs). ---

## Response 10
Thanks.Unifi offers the possibility to ovverride the network for every access point.But would it be the same, the management network must be untagged on Mikrotik to be able to access the access points?UniFi.pngI think the idea with default VLAN 1 as native VLAN should be easier for setup or what was their basic idea to do it like this? ---

## Response 11
Which is your management vlan.I see you have data vlans 401, 402 and 403 on the unifi and then vlan1.Since unifi expects the management vlan untagged, simply do the following. Lets assume on the MIKROK TIK you have a management vlan99.We simply untag this vlan to the unifi on a hybrid port with vlans 400, 401, 402 tagged for the data vlan side.The unifi will assume the untagged vlan is the management vlan etc. and all devices are happy.You will not have to change anything on the unifi./interface bridge portadd bridge=bridge interface=ether4 pvid=99 comment="hybrid port to ubiquiti AP"/interface bridge vlanadd bridge=bridge tagged=bridge untagged=4 vlan-ids=99add bridge=bridge tagged=bridge, ether4 vlan-ids=400, 401, 402 ---

## Response 12
Thanks, very much.Everything runs fine now.Why is it not sugestable to run a management vlan on vlan 1?I saw a lot of configurations, where people uses vlan 1, too. ---

## Response 13
MT users are not ordinary people. ---

## Response 14
Why is it not sugestable to run a management vlan on vlan 1?I saw a lot of configurations, where people uses vlan 1, too.There is nothing technically wrong with using VLAN 1 or running management on it, you just have to be very aware of how different vendors use VLAN 1.With Ubiquiti the UniFi default LAN is untagged and they reserve VLAN ID 1 for internal use, they also reserve VLAN IDs 4010-4094 for internal use in devices so in the controller Settings > Networks you can only create additional networks with VLAN IDs 2-4009.With Mikrotik there is no restriction on the VLAN IDs which can be specified for an/interface vlan, any permitted by the IEEE 802.1Q specification , i.e. 1-4094, can be used. ---

## Response 15
Sorry that I post here but I think that my question fits good here.In case of onlineuser, he created 4 bridges assigned to ether4 (port for wifi access points).Then there are 4 vlans, every points to a different bridge.Is this good practice on MT devices or should be one bridge enough which contains the 4 vlans?I am a little bit confused, when I saw this. ---

## Response 16
Since the introduction of VLAN-aware bridges some years ago a single bridge is the recommended method. There are various potential issues when using multiple bridgeshttps://help.mikrotik.com/docs/spaces/R ... figuration ---

## Response 17
Thanks for the tip.I thought that one bridge for vlans is only relevant when more than one ether port should be used.1.png2.pngSo, it really makes a difference if I assign the vlans to a bridge which is assigned to an ether port?And every vlan/bridge is bounded to it's own dhcp server.Can a dhcp server, which is assigned to a bridge which contains more than one vlan, occur troubles?In my case every dhcp server is assigned to a different bridge and vlan.I think it is also not possible to assign the same bridge as interface to different dhcp server with different ip pools. ---

## Response 18
If you willneverrequire the VLANs to be present on more than one physical port then you can attach an/interface vlandirectly to a port. The do not work as drawn, they merely add a VLAN tag for packets passing in one direction and remove it for packets passing in the other.Consider/interface vlanadd interface=ether4 name=vlan1 vlan-id=1add interface=ether4 name=vlan400 vlan-id=400add interface=ether4 name=vlan401 vlan-id=401add interface=ether4 name=vlan402 vlan-id=402When you add IP addresses, DHCP servers, etc. to thevlan1/400/401/402interfaces the packets have the corresponding VLAN tag added as they leave ether4. Foruntaggedpackets you would useether4directly, notvlan1, as untagged packets have no VLAN ID. Usingvlan1adds a tag with VLAN ID 1 for packets leavingether4, and will only accept packets tagged with VLAN ID 1 on entry.The main confusion arises when a switch chip or VLAN-aware bridge is used, these typically have no mechanism for handling untagged packets internally so manufacturers use/reserve one. Untagged packets have this reserved VLAN ID added on entry to the switch or bridge, and removed on exit.On Mikrotiks a VLAN-aware bridge behaves like a managed switch which is embedded within the Mikrotik, in addition to the external ports there is also a bridge-to-CPU port which can be configured as untagged only, hybrid or tagged only just like the external ports. Tagged traffic on this bridge-to-CPU port has to be handled by/interface vlanas the services provided by the CPU generally expect untagged traffic only.viewtopic.php?t=173692may be helpful. ---

## Response 19
Ok, now it's more clear.- Connectiong a /interface vlan directly to ether4 is clear.- /ip addresses is also clear - binding fist wifi ip pool to vlan 400 for example- but binding dhcp server to vlan 400 interface is not possible because it runs as slave device from ether 4.It is also not possible to bind two dhcp server on the same interface. ---

## Response 20
- but binding dhcp server to vlan 400 interface is not possible because it runs as slave device from ether 4.It is possible, the vlan400/interface vlanattached to ether4 is not a slave, this term applies to members of a bridge.It is also not possible to bind two dhcp server on the same interface.Correct, in this case you would have one server attached to ether4 to provide addresses on the untagged network, plus three more servers with each attached to one of vlan400/401/402. ---

## Response 21
When I create for every vlan a bridge it works (but I only use ether4 port for wifi)vlan.pngIf I try it with one bridge for all vlans, it will not work.vlan_1.png ---

## Response 22
Screenshots are not particularly helpful, post the configuration (the output of/exportfrom a terminal window) in a code block (the [] icon in the tools when composing a post to the forum) with any sensitive data redacted (serial number, any public IP addresses, etc.) ---

## Response 23
```
/interfacebridgeaddname=001vlan-filtering=yesaddname=400pvid=400vlan-filtering=yesaddname=401pvid=401vlan-filtering=yesaddname=402pvid=402vlan-filtering=yesadddisabled=yes name=bridge_wifi_vlansset[finddefault-name=ether4]comment="UniFi"name=\"ether4 - WLAN"/interfacevlanaddinterface="ether4 - WLAN"name=vlan_001 vlan-id=1addinterface="ether4 - WLAN"name=vlan_400 vlan-id=400addinterface="ether4 - WLAN"name=vlan_401 vlan-id=401addinterface="ether4 - WLAN"name=vlan_402 vlan-id=402addaddress-pool=wlan dhcp-option-set=wlan_options disabled=nointerface=\"ether4 - WLAN"lease-time=12hname=vlan001_ether4addaddress-pool=400disabled=nointerface=400lease-time=12hname=\
    vlan400_ether4addaddress-pool=401disabled=nointerface=401lease-time=12hname=\
    vlan401_ether4addaddress-pool=402disabled=nointerface=402lease-time=12hname=\
    vlan402_ether4/interfacebridge portaddbridge=001interface=vlan_001addbridge=400interface=vlan_400 pvid=400addbridge=401interface=vlan_401 pvid=401addbridge=402interface=vlan_402 pvid=402addbridge=bridge_wifi_vlans disabled=yesinterface="ether4 - WLAN"/interfacebridge vlanaddbridge=400comment="400 untagged for dhcp service"tagged=vlan_400 \
    vlan-ids=400addbridge=401comment="401 untagged for dhcp service"tagged=vlan_401 \
    vlan-ids=401addbridge=402comment="402 untagged for dhcp service"tagged=vlan_402 \
    vlan-ids=402addbridge=001comment=\"001 untagged for dhcp service (native vlan for UniFi)"tagged=vlan_001 \
    vlan-ids=1/ip addressaddaddress=11.11.11.1/27interface=vlan_400 network=11.11.11.0addaddress=11.11.12.1/27interface=vlan_401 network=11.11.12.0addaddress=11.11.13.1/27interface=vlan_402 network=11.11.13.0/ip dhcp-server networkaddaddress=11.11.11.0/27comment="VLAN 400"gateway=11.11.11.1addaddress=11.11.12.0/27comment="VLAN 401"gateway=11.11.12.1addaddress=11.11.13.0/27comment="VLAN 402"gateway=11.11.13.1This is the configuration with 4 bridges for 4 vlans. This works fine. The physical port for access points is ether4.Now I try fo change it with only one bridge so that I can use wifi vlans on ether4 and ether5.

---
```

## Response 24
I'm suprised that works, I suspect the managment traffic more by luck from side-effects than anything else./interface bridgeadd name=bridge_wifi_vlans frame-types=admit-all ingress-filtering=yes pvid=1 vlan-filtering=yes# hybrid bridge-to-CPU port with VLAN ID 1 untagged/interface vlanadd name=vlan_400 interface=bridge_wifi_vlans vlan-id=400add name=vlan_401 interface=bridge_wifi_vlans vlan-id=401add name=vlan_402 interface=bridge_wifi_vlans vlan-id=402/interface bridge portadd bridge=bridge_wifi_vlans interface=ether4 frame-types=admit-all ingress-filtering=yes pvid=1# hybrid port with VLAN ID 1 untaggedadd bridge=bridge_wifi_vlans interface=ether5 frame-types=admit-all ingress-filtering=yes pvid=1# hybrid port with VLAN ID 1 untagged/interface bridge vlan# add bridge=bridge_wifi_vlans untagged=bridge_wifi_vlans, ether4, ether5 pvid=1is created dynamically from thepvid=settings, but can also be set manuallyadd bridge=bridge_wifi_vlans tagged=bridge_wifi_vlans, ether4, ether5 pvid=400add bridge=bridge_wifi_vlans tagged=bridge_wifi_vlans, ether4, ether5 pvid=401add bridge=bridge_wifi_vlans tagged=bridge_wifi_vlans, ether4, ether5 pvid=402then attach each/ip addressand/ip dhcp-serverto the respectivevlan_400, vlan_401, vlan_402plusbridge_wifi_vlansfor AP managment traffic.For those who prefer the CPU-to-bridge port operating fully tagged (a.k.a. trunk) rather than hybrid:/interface bridgeadd name=bridge_wifi_vlans frame-types=admit-admit-only-vlan-tagged ingress-filtering=yes vlan-filtering=yes# trunk bridge-to-CPU port with all tagged/interface vlanadd name=vlan_001 interface=bridge_wifi_vlans vlan-id=1add name=vlan_400 interface=bridge_wifi_vlans vlan-id=400add name=vlan_401 interface=bridge_wifi_vlans vlan-id=401add name=vlan_402 interface=bridge_wifi_vlans vlan-id=402/interface bridge portadd bridge=bridge_wifi_vlans interface=ether4 frame-types=admit-all ingress-filtering=yes pvid=1# hybrid port with VLAN ID 1 untaggedadd bridge=bridge_wifi_vlans interface=ether5 frame-types=admit-all ingress-filtering=yes pvid=1# hybrid port with VLAN ID 1 untagged/interface bridge vlanadd bridge=bridge_wifi_vlans tagged=bridge_wifi_vlans pvid=1 # untagged=ether4, ether5setting is created dynamically from thepvid=settings, but can also be set manuallyadd bridge=bridge_wifi_vlans tagged=bridge_wifi_vlans, ether4, ether5 pvid=400add bridge=bridge_wifi_vlans tagged=bridge_wifi_vlans, ether4, ether5 pvid=401add bridge=bridge_wifi_vlans tagged=bridge_wifi_vlans, ether4, ether5 pvid=402then attach each/ip addressand/ip dhcp-serverto the respectivevlan_001, vlan_400, vlan_401, vlan_402 ---

## Response 25
Thanks, now it works.I took your second configuration.Thank you, so much.Now I also can connect ether5 to a trunk port on my managed switch to share the wifi-vlans to other building, can't it?What is the advantage of CPU-to-bridge port operating fully tagged (a.k.a. trunk) rather than hybrid?Is the trunk version more isolated than the hybrid version? ---

## Response 26
Now I also can connect ether5 to a trunk port on my managed switch to share the wifi-vlans to other building, can't it?Yes.What is the advantage of CPU-to-bridge port operating fully tagged (a.k.a. trunk) rather than hybrid?None really. It is cosmetic, some people seem to really dislike having to use the/interface vlanports for tagged but the parent/interface bridgefor untagged.There is a disadvantage in that bridge ingress port information is lost when packets are handled by an/interface vlan, one consequence being that neighbour discovery shows devices as being connected tovlanXXXXrather than the actualetherXport. Whilst this isn't particularly an issue for a small home setup it does make tracking devices down significantly more difficult if you have several hundred devices.Is the trunk version more isolated than the hybrid version?No. ---