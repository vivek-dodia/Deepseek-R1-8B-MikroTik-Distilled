# Thread Information
Title: Thread-1117011
Section: RouterOS
Thread ID: 1117011

# Discussion

## Initial Question
Hello, As base config I useUsing RouterOS to VLAN your networkviewtopic.php?t=143620&sid=8d57615ae14b ... b348b28fb8My simple system looks like "Router-Switch-AP (all in one)" (and this works great) + 1 Unifi AP AC LR, which is configured manually with main MainWiFi on "default" network and guests GuestWiFi which I attach to "guestNetwork", as GREEN VLAN 20. UniFi AP I attached to ether2 and it gets address from BLUE VLAN. MainWiFi works, GuestWiFi not (even not get DHCP address) and I guess that is from
```
[..]# VLAN Security# Only allow ingress packets without tags on Access Ports/interfacebridge portsetbridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged[findinterface=ether2]setbridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged[findinterface=ether3]setbridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged[findinterface=ether4]setbridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged[findinterface=ether5]setbridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged[findinterface=wlan1]setbridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged[findinterface=wlan2]then how I must configure Mikrotik and UniFi AP to establish safe and stable guest WiFi?thanks,Saules Ieleja

---
```

## Response 1
If/interface bridge port set bridge=BR1 [find interface=ether2] frame-types=admit-alldoesn't help, post the export of the complete configuration. ---

## Response 2
"admit-all" doesn't help, config:
```
# 2024-12-22 20:44:24 by RouterOS 7.16.2# software id = 5DWL-EDZZ## model = RB751G-2HnD# serial number = hidden as 'anav' requested/interfacebridgeaddname=BR1 protocol-mode=none vlan-filtering=yes/interfacewirelessset[finddefault-name=wlan1]band=2ghz-b/g/n country=latvia frequency=auto\
    mode=ap-bridge ssid=BLUE/interfacevlanaddinterface=BR1 name=BASE_VLAN vlan-id=99addinterface=BR1 name=BLUE_VLAN vlan-id=10addinterface=BR1 name=GREEN_VLAN vlan-id=20/interfacelistaddname=WANaddname=VLANaddname=BASE/interfacewireless security-profilesset[finddefault=yes]authentication-types=wpa2-psk mode=dynamic-keys \
    supplicant-identity=MikroTikaddauthentication-types=wpa2-psk mode=dynamic-keys name=guest \
    supplicant-identity=MikroTik/interfacewirelessaddmac-address=02:0C:42:FB:C7:4Bmaster-interface=wlan1 name=wlan2 \
    security-profile=guest ssid=GREEN/ip pooladdname=BLUE_POOL ranges=10.0.10.2-10.0.10.254addname=GREEN_POOL ranges=10.0.20.2-10.0.20.254/ip dhcp-serveraddaddress-pool=BLUE_POOLinterface=BLUE_VLAN name=BLUE_DHCPaddaddress-pool=GREEN_POOLinterface=GREEN_VLAN name=GREEN_DHCP/interfacebridge portaddbridge=BR1interface=ether2 pvid=10addbridge=BR1 frame-types=admit-only-untagged-and-priority-taggedinterface=\
    ether3 pvid=10addbridge=BR1 frame-types=admit-only-untagged-and-priority-taggedinterface=\
    wlan1 pvid=10addbridge=BR1 frame-types=admit-only-untagged-and-priority-taggedinterface=\
    ether4 pvid=20addbridge=BR1 frame-types=admit-only-vlan-taggedinterface=wlan2 pvid=20addbridge=BR1 frame-types=admit-only-untagged-and-priority-taggedinterface=\
    ether5 pvid=99/interfacebridge settingssetuse-ip-firewall-for-vlan=yes/ip neighbor discovery-settingssetdiscover-interface-list=BASE/ip settingssetallow-fast-path=no/interfacebridge vlanaddbridge=BR1 tagged=BR1 vlan-ids=10addbridge=BR1 tagged=BR1 vlan-ids=20addbridge=BR1 tagged=BR1 vlan-ids=99/interfacelist memberaddinterface=ether1 list=WANaddinterface=BASE_VLAN list=VLANaddinterface=BLUE_VLAN list=VLANaddinterface=GREEN_VLAN list=VLANaddinterface=BASE_VLAN list=BASE/ip addressaddaddress=192.168.0.1/24interface=BASE_VLAN network=192.168.0.0addaddress=10.0.10.1/24interface=BLUE_VLAN network=10.0.10.0addaddress=10.0.20.1/24interface=GREEN_VLAN network=10.0.20.0/ip dhcp-clientaddinterface=ether1/ip dhcp-server networkaddaddress=10.0.10.0/24dns-server=192.168.0.1gateway=10.0.10.1addaddress=10.0.20.0/24dns-server=192.168.0.1gateway=10.0.20.1/ip dnssetallow-remote-requests=yes servers=9.9.9.9/ip firewall filteraddaction=accept chain=input comment="Allow Estab & Related"\
    connection-state=established,relatedaddaction=accept chain=input comment="Allow VLAN"in-interface-list=VLANaddaction=accept chain=input comment="Allow Base_Vlan Full Access"\in-interface=BASE_VLANaddaction=drop chain=input comment=Dropaddaction=accept chain=forward comment="Allow Estab & Related"\
    connection-state=established,relatedaddaction=accept chain=forward comment="VLAN Internet Access only"\
    connection-state=newin-interface-list=VLANout-interface-list=WANaddaction=drop chain=forward comment=Drop/ip firewall nataddaction=masquerade chain=srcnat comment="Default masquerade"\out-interface-list=WAN/system clocksettime-zone-name=Europe/Riga/system identitysetname=RouterSwitchAP/system notesetshow-at-login=no/system ntp clientsetenabled=yes/system ntp client serversaddaddress=ntp.org/tool mac-serversetallowed-interface-list=BASE/tool mac-server mac-winboxsetallowed-interface-list=BASE

---
```

## Response 3
/interface bridge vlan set [find vlan-ids=20] tagged=BR1, ether2 ---

## Response 4
/interface bridge vlan set [find vlan-ids=20] tagged=BR1, ether2doesn't help, device not get address from GREEN DHCP, but assigns AutoIP from 169.x.x.x ---

## Response 5
First: Please remove router serial number from your post!Second: Config is incomplete, the base subnet is missing typical networking items, ip pool etc.....THird:removeor set toNOthe ip bridge firewall settings! This is an advanced menu that is normally not needed.Fourth: Normally "allow fast path" is set to yes.. Why did you set it to NO??Fifth: Ether2 should be a hybrid port to the UNIFI..... the untagged vlan should be the base vlan ( the management vlan and the unifis IP should be 192.168.0.X ) PVID of 99, and the other two vlans, main and guest should be tagged as data vlans.Sixth: Firewall rules need work...............
```
# model = RB751G-2HnD# serial number = XXXXXXXXXX/interfacebridgeaddname=BR1 protocol-mode=none vlan-filtering=yes/interfacewirelessset[finddefault-name=wlan1]band=2ghz-b/g/n country=latvia frequency=auto\
    mode=ap-bridge ssid=BLUE/interfacevlanaddinterface=BR1 name=BASE_VLAN vlan-id=99addinterface=BR1 name=BLUE_VLAN vlan-id=10addinterface=BR1 name=GREEN_VLAN vlan-id=20/interfacelistaddname=WANaddname=VLANaddname=BASE/interfacewireless security-profilesset[finddefault=yes]authentication-types=wpa2-psk mode=dynamic-keys \
    supplicant-identity=MikroTikaddauthentication-types=wpa2-psk mode=dynamic-keys name=guest \
    supplicant-identity=MikroTik/interfacewirelessaddmac-address=02:0C:42:FB:C7:4Bmaster-interface=wlan1 name=wlan2 \
    security-profile=guest ssid=GREEN/ip pooladdname=BLUE_POOL ranges=10.0.10.2-10.0.10.254addname=GREEN_POOL ranges=10.0.20.2-10.0.20.254addname=BASE_POOL ranges=192.168.0.2-192.168.0.10/ip dhcp-serveraddaddress-pool=BLUE_POOLinterface=BLUE_VLAN name=BLUE_DHCPaddaddress-pool=GREEN_POOLinterface=GREEN_VLAN name=GREEN_DHCPaddaddress-pool=BASE_POOLinterface=BASE_VLAN name=BASE_DHCP/interfacebridge portaddbridge=BR1interface=ether2 pvid=99comment="hybrid port to UNIFI"addbridge=BR1 ingress-filtering=yes frame-type=admit-only-priority-and-untaggedinterface=ether3 pvid=10addbridge=BR1 ingress-filtering=yes frame-type=admit-only-priority-and-untaggedinterface=ether4 pvid=20addbridge=BR1 ingress-filtering=yes frame-type=admit-only-priority-and-untaggedinterface=ether5 pvid=99addbridge=BR1 ingress-filtering=yes frame-type=admit-only-priority-and-untaggedinterface=wlan1 pvid=10addbridge=BR1 ingress-filtering=yes frame-type=admit-only-priority-and-untaggedinterface=wlan2 pvid=20/interfacebridge settingssetuse-ip-firewall-for-vlan=no/ip neighbor discovery-settingssetdiscover-interface-list=BASE/ip settingssetallow-fast-path=yes/interfacebridge vlanaddbridge=BR1 tagged=BR1,ether2  untagged=ether3,wlan1  vlan-ids=10addbridge=BR1 tagged=BR1,ether2  untagged=ether4,wlan2  vlan-ids=20addbridge=BR1 tagged=BR1  untagged=ether2,ether5  vlan-ids=99/interfacelist memberaddinterface=ether1 list=WANaddinterface=BASE_VLAN list=VLANaddinterface=BLUE_VLAN list=VLANaddinterface=GREEN_VLAN list=VLANaddinterface=BASE_VLAN list=BASE/ip addressaddaddress=192.168.0.1/24interface=BASE_VLAN network=192.168.0.0addaddress=10.0.10.1/24interface=BLUE_VLAN network=10.0.10.0addaddress=10.0.20.1/24interface=GREEN_VLAN network=10.0.20.0/ip dhcp-clientaddinterface=ether1/ip dhcp-server networkaddaddress=10.0.10.0/24dns-server=192.168.0.1gateway=10.0.10.1addaddress=10.0.20.0/24dns-server=192.168.0.1gateway=10.0.20.1addaddress=192.168.0.0/24dns-server=192.168.0.1gateway=192.168.0.1/ip dnssetallow-remote-requests=yes servers=9.9.9.9/ip firewall filteraddaction=accept chain=input comment="Allow Estab, Related & untracked"\
    connection-state=established,related,untrackedaddaction=drop chain=input connection-state=invalidaddaction=accept chain=input protocol=icmpaddaction=accept chain=input comment="Allow admin"in-interface-list=BASEaddaction=accept chain=input comment="users to services"in-interface-list=VLAN dst-port=53,123protocol=udpaddaction=accept chain=input comment="users to services"in-interface-list=VLAN dst-port=53protocol=tcpaddaction=drop chain=input comment="Drop all else"{putthisruleinlast}+++++++++++++++++++++++addaction=fasttrack-connection chain=forward connection-state=established,relatedaddaction=accept chain=forward comment="Allow Estab,Related & Untracked"\
    connection-state=established,related,untrackedaddaction=accept chain=forward comment="internet traffic"in-interface-list=VLANout-interface-list=WANaddaction=accept chain=forward comment="admin to vlans"in-interface-list=BASEout-interface-list=VLANaddaction=accept chain=forward comment="port forwarding"connection-nat-state=dstnat disabled=yes{enableorremoveifnotrequired}addaction=drop chain=forward comment="Drop all else"/ip firewall nataddaction=masquerade chain=srcnat comment="Default masquerade"\out-interface-list=WAN/system clocksettime-zone-name=Europe/Riga/system identitysetname=RouterSwitchAP/system notesetshow-at-login=no/system ntp clientsetenabled=yes/system ntp client serversaddaddress=ntp.org/tool mac-serversetallowed-interface-list=none/tool mac-server mac-winboxsetallowed-interface-list=BASE

---
```

## Response 6
Both the changes I have asked you to do were necessary, just apparently not sufficient. Does it behave the same if you try to connect using the wlan2 interface of the Mikrotik itself? ---

## Response 7
if you try to connect using the wlan2 interface of the Mikrotik itself?if I enable Mikrotik wlan, then all (BLUE and GREEN wifi) works with initial configuration.UniFi AP connected to ether2;UniFi configuration: "Guest" network, connected to 20 VLAN ID, GREEN wifi connected to "Guest" network. ---

## Response 8
If it works when you enable wlan2 on the Mikrotik itself, the IP configuration seems to be ok.So as the next step, disable wlan2 again, open a command line window as wide as your screen allows, and do the following:/interface bridge port set [find interface=ether2] hw=no/tool sniffer quick interface=ether2 port=68and then let some client device try to connect to the guest network that is broadcast from the Ubiquiti.If the/tool sniffer ...shows anything, copy-paste it here. ---

## Response 9
If the/tool sniffer ...shows anything, copy-paste it here.two iOS devices, one android
```
Columns:INTERFACE,TIME,NUM,DIR,SRC-MAC,DST-MAC,VLAN,SRC-ADDRESS,DST-ADDRESS,PROTOCOL,SIZE,CPU
INTERFACE  TIME    NUM  DIR  SRC-MAC            DST-MAC            VLAN  SRC-ADDRESS          DST-ADDRESS                  PROTOCOL  SIZE  CPU
ether255.41211<-72:BD:A1:23:63:30FF:FF:FF:FF:FF:FF200.0.0.0:68(bootpc)255.255.255.255:67(bootps)ip:udp3460ether256.04112<-22:F3:5D:F0:6A:77FF:FF:FF:FF:FF:FF200.0.0.0:68(bootpc)255.255.255.255:67(bootps)ip:udp3460ether257.69213<-22:F3:5D:F0:6A:77FF:FF:FF:FF:FF:FF200.0.0.0:68(bootpc)255.255.255.255:67(bootps)ip:udp3460ether259.47914<-72:BD:A1:23:63:30FF:FF:FF:FF:FF:FF200.0.0.0:68(bootpc)255.255.255.255:67(bootps)ip:udp3460ether264.88115<-5C:51:81:B0:E2:AD  FF:FF:FF:FF:FF:FF200.0.0.0:68(bootpc)255.255.255.255:67(bootps)ip:udp3540

---
```

## Response 10
OK, so it comes alright from the Unifi, but I cannot spot an issue in the configuration. Post the current output of/interface bridge exportafter all the changes you've made so far, please. ---

## Response 11
```
# 2024-12-22 18:28:41 by RouterOS 7.16.2# software id = 5DWL-EDZZ## model = RB751G-2HnD# serial number = xxxxxxxxxxxx/interfacebridgeaddname=BR1 protocol-mode=none vlan-filtering=yes/interfacebridge portaddbridge=BR1 frame-types=admit-only-untagged-and-priority-taggedinterface=ether3 pvid=10addbridge=BR1 frame-types=admit-only-untagged-and-priority-taggedinterface=wlan1 pvid=10addbridge=BR1 frame-types=admit-only-untagged-and-priority-taggedinterface=ether4 pvid=20addbridge=BR1 frame-types=admit-only-untagged-and-priority-taggedinterface=wlan2 pvid=20addbridge=BR1 frame-types=admit-only-untagged-and-priority-taggedinterface=ether5 pvid=99addbridge=BR1 hw=nointerface=ether2 pvid=10/interfacebridge settingssetuse-ip-firewall-for-vlan=yes/interfacebridge vlanaddbridge=BR1 tagged=BR1 vlan-ids=10addbridge=BR1 tagged=BR1,ether2 vlan-ids=20addbridge=BR1 tagged=BR1 vlan-ids=99[ieladmin@RouterSwitchAP]>what about "anav" recommendations?my configuration was almost copy/paste from:Using RouterOS to VLAN your networkviewtopic.php?t=143620&sid=8d57615ae14b ... b348b28fb8Second: Config is incomplete, the base subnet is missing typical networking items, ip pool etc.....Fifth: Ether2 should be a hybrid port to the UNIFI..... the untagged vlan should be the base vlan ( the management vlan and the unifis IP should be 192.168.0.X ) PVID of 99, and the other two vlans, main and guest should be tagged as data vlans.

---
```

## Response 12
/interface bridge settings set use-ip-firewall-for-vlan=nothen try again.I did not analyze all @anav's recommendations as most of them are not relevant to the primary issue, but I agree with him on the above one, the purpose of this setting is different from what you assume - its name is misleading. ---

## Response 13
/interface bridge settings set use-ip-firewall-for-vlan=noAfter change, all start working, but after few minutes devices disconnect and now don't connect to guest at all.Tomorrow try to reset and start again from scratch... ---

## Response 14
Tomorrow try to reset and start again from scratch...If they cannot even connect to the WiFi, I don't think it is a Mikrotik issue any more. So before starting from scratch, I'd suggest to save a backup and an export of the current configuration so that you have something known good to return to. ---

## Response 15
I'd suggest to save a backup and an export of the current configuration so that you have something known good to return to.Done all such way.But I reconfigure bit original configuration:- ether1 - WAN,- ether2 - BLUE VLAN,- ether3 - GREEN VLAN,- ether4, ether5 - BASE VLANconnect internet to ether1, notebook to ether4, UniFi AP to ether5reset UniFi AP, it gets IP from BASE DHCPthen
```
/interfacebridge portsetbridge=BR1[findinterface=ether5]frame-types=admit-alland
```

```
/interfacebridge vlanset[find vlan-ids=10]tagged=BR1,ether5/interfacebridge vlanset[find vlan-ids=20]tagged=BR1,ether5booth WiFi, guest and main now works on UniFi AP through VLANsAlso setup some speed limiting via Queues on guest WiFip.s.my guess about previous problems is that UniFi AP be need to connected to BASE LAN, not BLUE as I do at first.

---
```

## Response 16
p.s.my guess about previous problems is that UniFi AP be need to connected to BASE LAN, not BLUE as I do at first.Stated clearly in post 6 of this thread............First: Please remove router serial number from your post!Second: Config is incomplete, the base subnet is missing typical networking items, ip pool etc.....THird: remove or set to NO the ip bridge firewall settings! This is an advanced menu that is normally not needed.Fourth: Normally "allow fast path" is set to yes.. Why did you set it to NO??Fifth: Ether2 should be a hybrid port to the UNIFI.....the untagged vlan should be the base vlan( the management vlan and the unifis IP should be 192.168.0.X ) PVID of 99, and the other two vlans, main and guest should be tagged as data vlans.Sixth: Firewall rules need work............... ---

## Response 17
Stated clearly in post 6 of this thread............It's hard to follow two advisers in time, but thanks for your post! ---

## Response 18
Sindy is the expert, I am just learning.However, his level of genius is not always needed for basic config issues.I am searching for the big lump of cow poop in the haystack, his eyes are trained to look for needles....... He might not even notice the cow poop LOLUnless its very fresh) ---