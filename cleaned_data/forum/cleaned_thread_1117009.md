# Thread Information
Title: Thread-1117009
Section: RouterOS
Thread ID: 1117009

# Discussion

## Initial Question
Hello, I am having difficulty connecting to the internet from my CRS328. I am a radio engineer, not an IP engineer, so I am only in boot camp learning this stuff. (apologies in advance). I have 3 VLANs that I want to connect to the internet, VL600 (Management) VL630 (LAN) VL710 (IOT). So far VL630 works some of the time. the other two appear to be connected (as shown by the system tray icon on the end user device) but go nowhere. Ping doesn't work. I can get to the gateway but not beyond.Here are my firewall rules:
```
/ip dns
set allow-remote-requests=yes cache-size=4096KiB max-concurrent-queries=200 max-udp-packet-size=8192 servers=127.0.0.1,31.22.13.211
/ip firewall filter
add action=fasttrack-connection chain=forward comment="Fasttrack DNS (tcp)" connection-state=established,related,new dst-port=53 hw-offload=yes protocol=tcp
add action=fasttrack-connection chain=forward comment="Fasttrack DNS (udp)" connection-state=established,related,new dst-port=53 hw-offload=yes protocol=udp
add action=fasttrack-connection chain=forward comment="Fasttrack Connected" connection-state=established,related hw-offload=yes
add action=accept chain=forward comment="Allow LAN (80.144.10.0/24)" connection-state=established,related,new log=yes src-address=80.144.10.0/24
add action=accept chain=forward comment="Allow MAN (80.144.1.0/24)" connection-state=established,related,new src-address=80.144.1.0/24
add action=accept chain=forward comment="Allow IOT (80.145.80.0/24)" connection-state=established,related src-address=80.145.80.0/24
add action=drop chain=input comment="Drop invalid (input)" connection-state=invalid
add action=drop chain=forward comment="Drop invalid (Forward)" connection-state=invalid
add action=accept chain=input comment="Accept ICMP input" connection-state=established,related,new protocol=icmp
add action=accept chain=forward comment="Accept ICMP forward" connection-state=established,related,new protocol=icmp
add action=accept chain=input comment="Accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=accept chain=forward comment="*TEST* forward DNS (tcp)" connection-state=new dst-port=53 protocol=tcp src-address=80.144.10.0/24
add action=accept chain=forward comment="*TEST* forward DNS (udp)" connection-state=new dst-port=53 protocol=udp src-address=80.144.10.0/24
/ip firewall nat
add action=masquerade chain=srcnat comment="NAT: Masquerade for VL600 to WAN" out-interface-list=WAN src-address=80.144.1.0/24
add action=masquerade chain=srcnat comment="NAT: Masquerade for VL630 to WAN" out-interface-list=WAN src-address=80.144.10.0/24
add action=masquerade chain=srcnat comment="NAT: Masquerade for VL710 to WAN" out-interface-list=WAN src-address=80.145.80.0/24
add action=masquerade chain=srcnat comment="NAT: Masquerade For VL638 to WAN" out-interface-list=WAN src-address=80.144.20.0/24

---
```

## Response 1
small additional information - the device immediately upstream of the CRS328 is a PFSense Firewall, and I am much more adept with that, but the system logs there dont show anything untoward. ---

## Response 2
```
/ip dns
set allow-remote-requests=yes cache-size=4096KiB max-concurrent-queries=200 max-udp-packet-size=8192 servers=127.0.0.1,31.22.13.211By setting 127.0.01. you are referring the router to itself, and that is incorrect. Just remove it and leave 31.22.13.211:
```

```
/ip dns
set allow-remote-requests=yes cache-size=4096KiB max-concurrent-queries=200 max-udp-packet-size=8192 servers=31.22.13.211

---
```

## Response 3
Did that, and the connection still times out. ---

## Response 4
You need to show full config, not only parts where you think it's wrong.It is not working so there is a config mistake somewhere but probably not in the place you are showing. ---

## Response 5
```
# 2024-12-30 13:00:13 by RouterOS 7.16.2
# software id = J40J-I127
#
# model = CRS328-4C-20S-4S+
# serial number = HDC085CWMCN
/interface bridge
add comment="Master Bridge with VLAN Filtering Enabled" name=CRS328-Master-Bridge pvid=600 vlan-filtering=yes
/interface ethernet
set [ find default-name=combo1 ] comment=VL600-MAN
set [ find default-name=combo2 ] comment=VL630-LAN
set [ find default-name=combo3 ] comment=VL710-IOT
set [ find default-name=sfp-sfpplus1 ] comment=Uplink
set [ find default-name=sfp-sfpplus2 ] comment=R740
set [ find default-name=sfp-sfpplus3 ] comment=R640
set [ find default-name=sfp-sfpplus4 ] comment=R630
set [ find default-name=sfp1 ] auto-negotiation=no
set [ find default-name=sfp2 ] auto-negotiation=no comment=KVM2
set [ find default-name=sfp3 ] auto-negotiation=no comment="CRS109-3(Lounge)"
set [ find default-name=sfp4 ] auto-negotiation=no comment=KVM2
set [ find default-name=sfp5 ] auto-negotiation=no comment="CRS109-2(Lounge)"
set [ find default-name=sfp6 ] auto-negotiation=no comment=KVM3
set [ find default-name=sfp7 ] auto-negotiation=no comment="CRS109-1(Office)"
set [ find default-name=sfp8 ] auto-negotiation=no comment=KVM4
set [ find default-name=sfp9 ] auto-negotiation=no comment="Google Wifi"
set [ find default-name=sfp10 ] auto-negotiation=no comment="NZ Server"
set [ find default-name=sfp11 ] auto-negotiation=no comment=iDRAC1-R740
set [ find default-name=sfp12 ] auto-negotiation=no comment=Z820
set [ find default-name=sfp13 ] auto-negotiation=no comment=iDRAC2-R640
set [ find default-name=sfp14 ] auto-negotiation=no comment="AWTG Machine"
set [ find default-name=sfp15 ] auto-negotiation=no comment=iDRAC3-R630
set [ find default-name=sfp16 ] auto-negotiation=no comment="Boldyn Machine"
set [ find default-name=sfp17 ] auto-negotiation=no comment=NAS
set [ find default-name=sfp18 ] auto-negotiation=no comment=Growatt+Printer
set [ find default-name=sfp19 ] auto-negotiation=no comment="Mail Machine"
/interface vlan
add comment=V1-S5-VL600-MAN interface=CRS328-Master-Bridge name=V1-S5-VL600-MAN vlan-id=600
add comment="V2-S4-LAN VLAN" interface=CRS328-Master-Bridge name=V2-S4-VL630-LAN vlan-id=630
add comment="V3-S5-SEC VLAN" interface=CRS328-Master-Bridge name=V3-S5-VL638-SEC vlan-id=638
add comment="V5-S3-KVM VLAN" interface=CRS328-Master-Bridge name=V5-Sx-VL646-KVM vlan-id=646
add comment="V6-S4-IDR VLAN" interface=CRS328-Master-Bridge name=V6-S4-VL654-IDR vlan-id=654
add comment="V7-S2-JAP VLAN" interface=CRS328-Master-Bridge name=V7-S2-VL662-JAP vlan-id=662
add comment="V8-S1-IOT VLAN" interface=CRS328-Master-Bridge name=V8-S1-VL710-IOT vlan-id=710
/caps-man datapath
add bridge=CRS328-Master-Bridge local-forwarding=yes name=DATAPATH1-VL630-LAN vlan-id=630 vlan-mode=use-tag
add bridge=CRS328-Master-Bridge local-forwarding=yes name=DATAPATH2-VL710-IOT vlan-id=710 vlan-mode=use-tag
/caps-man security
add authentication-types=wpa2-psk encryption=aes-ccm name=SEC1-VL630-LAN
add authentication-types=wpa2-psk encryption=aes-ccm name=SEC2-VL710-IOT
/caps-man configuration
add datapath.bridge=CRS328-Master-Bridge .vlan-id=630 .vlan-mode=use-tag mode=ap name=WLANCFG1-VL630-LAN security=SEC1-VL630-LAN ssid=W1-S4-VL630-LAN-2
add datapath.bridge=CRS328-Master-Bridge .vlan-id=710 .vlan-mode=use-tag mode=ap name=WLANCFG2-VL710-IOT security=SEC2-VL710-IOT ssid=W2-S1-VL710-IOT-2
/caps-man interface
add comment=CRS109-1-WL1-VL630-2.4Ghz configuration=WLANCFG1-VL630-LAN configuration.country="united kingdom" datapath=DATAPATH1-VL630-LAN disabled=no l2mtu=1600 mac-address=2C:C8:1B:AD:26:0A master-interface=none name=\
    CRS109-1 radio-mac=2C:C8:1B:AD:26:0A radio-name=2CC81BAD260A
add comment=CRS109-1-WL2-VL710-2.4Ghz configuration=WLANCFG2-VL710-IOT configuration.country="united kingdom" datapath=DATAPATH2-VL710-IOT disabled=no l2mtu=1600 mac-address=2E:C8:1B:AD:26:0A master-interface=CRS109-1 name=\
    CRS109-1-1 radio-mac=00:00:00:00:00:00 radio-name=2EC81BAD260A
/interface list
add name=WAN
add name=MAN
add name=LAN
add name=IOT
add name=KVM
add name=IDR
add name=JAP
add name=SEC
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip hotspot profile
set [ find default=yes ] html-directory=hotspot
/ip pool
add comment="DHCP Pool for VLAN600" name=DP1-VL600-MAN ranges=80.144.1.64/26
add comment="DHCP Pool for VLAN630" name=DP2-VL630-LAN ranges=80.144.10.64/26
add comment="DHCP Pool for VLAN638" name=DP3-VL638-SEC ranges=80.144.20.64/29
add comment="DHCP Pool for VLAN646" name=DP5-VL646-KVM ranges=80.144.30.64/29
add comment="DHCP Pool for VLAN654" name=DP6-VL654-IDR ranges=80.144.40.64/29
add comment="DHCP Pool for VLAN662" name=DP7-VL662-JAP ranges=80.145.50.64/29
add comment="DHCP Pool for VLAN710" name=DP8-VL710-IOT ranges=80.145.80.0/25
/ip dhcp-server
add add-arp=yes address-pool=DP1-VL600-MAN comment="DHCP Server for VLAN600" interface=V1-S5-VL600-MAN lease-time=1d name=DS1-VL600-MAN
add add-arp=yes address-pool=DP2-VL630-LAN comment="DHCP Server for VLAN630" interface=V2-S4-VL630-LAN lease-time=1d name=DS2-VL630-LAN
add add-arp=yes address-pool=DP3-VL638-SEC comment="DHCP Server for VLAN638" interface=V3-S5-VL638-SEC lease-time=1d name=DS3-VL638-SEC
add add-arp=yes address-pool=DP5-VL646-KVM comment="DHCP Server for VLAN646" interface=V5-Sx-VL646-KVM lease-time=1d name=DS5-VL646-KVM
add add-arp=yes address-pool=DP6-VL654-IDR comment="DHCP Server for VLAN654" interface=V6-S4-VL654-IDR lease-time=1d name=DS6-VL654-IDR
add add-arp=yes address-pool=DP7-VL662-JAP comment="DHCP Server for VLAN662" interface=V7-S2-VL662-JAP lease-time=1d name=DS7-VL662-JAP
add add-arp=yes address-pool=DP8-VL710-IOT comment="DHCP Server for VLAN710" interface=V8-S1-VL710-IOT lease-time=1d name=DS8-VL710-IOT
/port
set 0 name=serial0
/caps-man manager
set enabled=yes
/caps-man provisioning
add action=create-enabled master-configuration=WLANCFG1-VL630-LAN name-format=prefix name-prefix=CRS109- slave-configurations=WLANCFG2-VL710-IOT
/interface bridge port
add bridge=CRS328-Master-Bridge comment="Add sfp1 to Bridge" interface=sfp1 pvid=630
add bridge=CRS328-Master-Bridge comment=KVM1 interface=sfp2 pvid=646
add bridge=CRS328-Master-Bridge comment="CRS109-3(Upstairs)" interface=sfp3 pvid=600
add bridge=CRS328-Master-Bridge comment=KVM2 interface=sfp4 pvid=646
add bridge=CRS328-Master-Bridge comment="CRS109-2(Lounge)" interface=sfp5 pvid=600
add bridge=CRS328-Master-Bridge comment=KVM3 interface=sfp6 pvid=646
add bridge=CRS328-Master-Bridge comment="CRS109-1(Office)" interface=sfp7 pvid=600
add bridge=CRS328-Master-Bridge comment=KVM4 interface=sfp8 pvid=646
add bridge=CRS328-Master-Bridge comment="Google Wifi" interface=sfp9 pvid=630
add bridge=CRS328-Master-Bridge comment="NZ Server" interface=sfp10 pvid=630
add bridge=CRS328-Master-Bridge comment=iDRAC1-R740 interface=sfp11 pvid=654
add bridge=CRS328-Master-Bridge comment=Z820 interface=sfp12 pvid=630
add bridge=CRS328-Master-Bridge comment=iDRAC2-R640 interface=sfp13 pvid=654
add bridge=CRS328-Master-Bridge comment="AWTG Machine" interface=sfp14 pvid=630
add bridge=CRS328-Master-Bridge comment=iDRAC3-R630 interface=sfp15 pvid=654
add bridge=CRS328-Master-Bridge comment="Boldyn Machine" interface=sfp16 pvid=630
add bridge=CRS328-Master-Bridge comment=NAS interface=sfp17 pvid=630
add bridge=CRS328-Master-Bridge comment="Growatt and DS Printer" interface=sfp18 pvid=630
add bridge=CRS328-Master-Bridge comment="Mail Machine" interface=sfp19 pvid=630
add bridge=CRS328-Master-Bridge comment="Add sfp20 to Bridge" interface=sfp20 pvid=630
add bridge=CRS328-Master-Bridge comment="MAN Controller" interface=combo1 pvid=600
add bridge=CRS328-Master-Bridge comment="LAN Controller" interface=combo2 pvid=630
add bridge=CRS328-Master-Bridge comment="IOT Controller" interface=combo3 pvid=710
add bridge=CRS328-Master-Bridge comment=R740 interface=sfp-sfpplus2 pvid=638
add bridge=CRS328-Master-Bridge comment=R640 interface=sfp-sfpplus3 pvid=638
add bridge=CRS328-Master-Bridge interface=sfp-sfpplus4 pvid=638
/ipv6 settings
set disable-ipv6=yes
/interface bridge vlan
add bridge=CRS328-Master-Bridge comment="VLAN600 Access Port" tagged=CRS328-Master-Bridge untagged=combo1,sfp3,sfp7,sfp5 vlan-ids=600
add bridge=CRS328-Master-Bridge comment="VLAN630 Tagged Ports" tagged=sfp3,CRS328-Master-Bridge,sfp5,sfp7 untagged=sfp10,sfp1,sfp9,sfp12,sfp14,sfp16,sfp17,sfp18,sfp19,combo2 vlan-ids=630
add bridge=CRS328-Master-Bridge comment="VLAN638 Access Port" tagged=CRS328-Master-Bridge untagged=sfp-sfpplus2,sfp-sfpplus3,sfp-sfpplus4 vlan-ids=638
add bridge=CRS328-Master-Bridge comment="VLAN646 Access Ports" tagged=CRS328-Master-Bridge untagged=sfp2,sfp4,sfp6,sfp8 vlan-ids=646
add bridge=CRS328-Master-Bridge comment="VLAN654 Access Ports" tagged=CRS328-Master-Bridge untagged=sfp15,sfp11,sfp13 vlan-ids=654
add bridge=CRS328-Master-Bridge comment="VLAN662 Tagged Ports" tagged=sfp3,CRS328-Master-Bridge,sfp5 vlan-ids=662
add bridge=CRS328-Master-Bridge comment="VLAN710 Tagged Ports" tagged=sfp3,CRS328-Master-Bridge,sfp5,sfp7 untagged=combo3 vlan-ids=710
/interface list member
add interface=sfp-sfpplus1 list=WAN
add interface=V1-S5-VL600-MAN list=MAN
add interface=V2-S4-VL630-LAN list=LAN
add interface=V3-S5-VL638-SEC list=SEC
add interface=V5-Sx-VL646-KVM list=KVM
add interface=V6-S4-VL654-IDR list=IDR
add interface=V7-S2-VL662-JAP list=JAP
add interface=V8-S1-VL710-IOT list=IOT
/ip address
add address=80.144.1.1/24 comment="V1-S5-VL600-MAN Gateway" interface=V1-S5-VL600-MAN network=80.144.1.0
add address=80.144.10.1/24 comment="V2-S4-VL630-LAN Gateway" interface=V2-S4-VL630-LAN network=80.144.10.0
add address=80.144.20.1/24 comment="V3-S5-SEC Gateway" interface=V3-S5-VL638-SEC network=80.144.20.0
add address=80.144.30.1/24 comment="V5-S3-KVM Gateway" interface=V5-Sx-VL646-KVM network=80.144.30.0
add address=80.144.40.1/24 comment="V6-S4-IDR Gateway" interface=V6-S4-VL654-IDR network=80.144.40.0
add address=80.145.50.1/24 comment="V7-S2-JAP Gateway" interface=V7-S2-VL662-JAP network=80.145.50.0
add address=80.145.80.1/24 comment="V8-S1-IOT Gateway" interface=V8-S1-VL710-IOT network=80.145.80.0
add address=80.144.1.2/24 comment="combo1 IP for VLAN600" interface=combo1 network=80.144.1.0
add address=80.144.10.2/24 comment="combo2 IP for VLAN630" interface=combo2 network=80.144.10.0
add address=80.145.80.2/24 comment="combo3 IP for VLAN710" interface=combo3 network=80.145.80.0
/ip dhcp-client
add interface=sfp-sfpplus1
/ip dhcp-server network
add address=80.144.1.0/24 comment="Network for VLAN600" dns-server=100.48.48.1,127.0.0.1,8.8.8.8 gateway=80.144.1.1 netmask=24
add address=80.144.10.0/24 comment="Network for VLAN630" dns-server=100.48.48.1,127.0.0.1,8.8.8.8 gateway=80.144.10.1 netmask=24
add address=80.144.20.0/24 comment="Network for VLAN638" dns-server=100.48.48.1 gateway=80.144.20.1 netmask=24
add address=80.144.30.0/24 comment="Network for VLAN646" dns-server=100.48.48.1 gateway=80.144.30.1 netmask=24
add address=80.144.40.0/24 comment="Network for VLAN654" dns-server=100.48.48.1 gateway=80.144.40.1 netmask=24
add address=80.145.50.0/24 comment="Network for VLAN662" dns-server=100.48.48.1 gateway=80.145.50.1 netmask=24
add address=80.145.80.0/24 comment="Network for VLAN710" dns-server=100.48.48.1,127.0.0.1,8.8.8.8 gateway=80.145.80.1 netmask=24
/ip dns
set allow-remote-requests=yes cache-size=4096KiB max-concurrent-queries=200 max-udp-packet-size=8192 servers=31.22.13.211
/ip firewall filter
add action=fasttrack-connection chain=forward comment="Fasttrack DNS (tcp)" connection-state=established,related,new dst-port=53 hw-offload=yes protocol=tcp
add action=fasttrack-connection chain=forward comment="Fasttrack DNS (udp)" connection-state=established,related,new dst-port=53 hw-offload=yes protocol=udp
add action=fasttrack-connection chain=forward comment="Fasttrack Connected" connection-state=established,related hw-offload=yes
add action=accept chain=forward comment="Allow LAN (80.144.10.0/24)" connection-state=established,related,new log=yes src-address=80.144.10.0/24
add action=accept chain=forward comment="Allow MAN (80.144.1.0/24)" connection-state=established,related,new src-address=80.144.1.0/24
add action=accept chain=forward comment="Allow IOT (80.145.80.0/24)" connection-state=established,related src-address=80.145.80.0/24
add action=drop chain=input comment="Drop invalid (input)" connection-state=invalid
add action=drop chain=forward comment="Drop invalid (Forward)" connection-state=invalid
add action=accept chain=input comment="Accept ICMP input" connection-state=established,related,new protocol=icmp
add action=accept chain=forward comment="Accept ICMP forward" connection-state=established,related,new protocol=icmp
add action=accept chain=input comment="Accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=accept chain=forward comment="*TEST* forward DNS (tcp)" connection-state=new dst-port=53 protocol=tcp src-address=80.144.10.0/24
add action=accept chain=forward comment="*TEST* forward DNS (udp)" connection-state=new dst-port=53 protocol=udp src-address=80.144.10.0/24
/ip firewall nat
add action=masquerade chain=srcnat comment="NAT: Masquerade for VL600 to WAN" out-interface-list=WAN src-address=80.144.1.0/24
add action=masquerade chain=srcnat comment="NAT: Masquerade for VL630 to WAN" out-interface-list=WAN src-address=80.144.10.0/24
add action=masquerade chain=srcnat comment="NAT: Masquerade for VL710 to WAN" out-interface-list=WAN src-address=80.145.80.0/24
add action=masquerade chain=srcnat comment="NAT: Masquerade For VL638 to WAN" out-interface-list=WAN src-address=80.144.20.0/24
/system clock
set time-zone-name=Europe/London
/system identity
set name=CRS328-Master
/system logging
add action=echo topics=bridge
add topics=route
add topics=firewall
/system note
set show-at-login=no
/system ntp client
set enabled=yes
/system ntp client servers
add address=0.pool.ntp.org
/system swos
set allow-from-vlan=600
[admin@CRS328-Master] >

---
```

## Response 6
All 3 CRS109's are currently disconnected as I troubleshoot this issue. ---

## Response 7
Also, clients won't connect to 127.0.0.1 as DNS server, remove that IP from /ip dhcp-server network:
```
/ip dhcp-server network
add address=80.144.1.0/24 comment="Network for VLAN600" dns-server=100.48.48.1,127.0.0.1,8.8.8.8 gateway=80.144.1.1 netmask=24
add address=80.144.10.0/24 comment="Network for VLAN630" dns-server=100.48.48.1,127.0.0.1,8.8.8.8 gateway=80.144.10.1 netmask=24
add address=80.144.20.0/24 comment="Network for VLAN638" dns-server=100.48.48.1 gateway=80.144.20.1 netmask=24
add address=80.144.30.0/24 comment="Network for VLAN646" dns-server=100.48.48.1 gateway=80.144.30.1 netmask=24
add address=80.144.40.0/24 comment="Network for VLAN654" dns-server=100.48.48.1 gateway=80.144.40.1 netmask=24
add address=80.145.50.0/24 comment="Network for VLAN662" dns-server=100.48.48.1 gateway=80.145.50.1 netmask=24
add address=80.145.80.0/24 comment="Network for VLAN710" dns-server=100.48.48.1,127.0.0.1,8.8.8.8 gateway=80.145.80.1 netmask=24Though possible, leave bridges pvid=1:
```

```
/interface bridge
add comment="Master Bridge with VLAN Filtering Enabled" name=CRS328-Master-Bridge pvid=600 vlan-filtering=yesAs spf1 is your WAN interface, have it removed from the bridge:
```

```
/interface bridge port
add bridge=CRS328-Master-Bridge comment="Add sfp1 to Bridge" interface=sfp1 pvid=630Still looking through the firewall filter rules (and their order)...If you want to know a bit more about VLAN, please have a look at this great topic:viewtopic.php?t=143620

---
```

## Response 8
First:have you ever read this excellent guide on setting up VLAN ?It is considered the Bible around here:viewtopic.php?t=143620What 3 CRS109 ?How do they relate to this CRS328 ?Maybe we also need a network drawing ...First comments after seeing config:- pvid on bridge is useless. How are frame-types defined ? Since it's not in your export, I assume it's set to admit-all ? Should be "admit only vlan tagged"- while troubleshooting, it might be recommended to get 1 port away from bridge so you can always get in via that port using Winbox/Mac.- pools are possibly defined wrong (unless that notation is also possible, don't know about it).From documentation:ranges (IP; Default: ) IP address list of non-overlapping IP address ranges in the form of: from1-to1, from2-to2,...,fromN-toN. For example, 10.0.0.1-10.0.0.27, 10.0.0.32-10.0.0.47- you have serious inconsistencies in your pool definition and IP address definitionsE.g./ip pooladd comment="DHCP Pool for VLAN600" name=DP1-VL600-MAN ranges=80.144.1.64/26/ip addressadd address=80.144.1.1/24 comment="V1-S5-VL600-MAN Gateway" interface=V1-S5-VL600-MAN network=80.144.1.0/26 on pool and /24 on IP address ?? Align for all addresses/pools.- Same on DHCP network settings/ip dhcp-server networkadd address=80.144.1.0/24comment="Network for VLAN600" dns-server=100.48.48.1, 127.0.0.1, 8.8.8.8 gateway=80.144.1.1netmask=24What should it be for Management VLAN ? /24 or /26 ??Fix for all definitions.- Same on firewall NAT rules/ip firewall natadd action=masquerade chain=srcnat comment="NAT: Masquerade for VL600 to WAN" out-interface-list=WAN src-address=80.144.1.0/24Correct those things first please.UNLESS you are deliberately restricting pool sizes for those subnets ? ---

## Response 9
Adding:when defining those IP pools, make sure the manually added addresses are NOT included, which currently is the case. ---

## Response 10
Answers inline below:First:have you ever read this excellent guide on setting up VLAN ?It is considered the Bible around here:viewtopic.php?t=143620[Julian] YepWhat 3 CRS109 ?How do they relate to this CRS328 ?Maybe we also need a network drawing ...[Julian] they are 3 satellite routers, fiber connected to the CRS328 to provide connectivity throughout the house (being a radio engineer, I use wires and fibers wherever possible... just saying)First comments after seeing config:- pvid on bridge is useless. How are frame-types defined ? Since it's not in your export, I assume it's set to admit-all ? Should be "admit only vlan tagged"[Julian] Done- while troubleshooting, it might be recommended to get 1 port away from bridge so you can always get in via that port using Winbox/Mac.[Julian] Done- pools are possibly defined wrong (unless that notation is also possible, don't know about it).[Julian] The pool ranges were deliberately reducedFrom documentation:ranges (IP; Default: ) IP address list of non-overlapping IP address ranges in the form of: from1-to1, from2-to2,...,fromN-toN. For example, 10.0.0.1-10.0.0.27, 10.0.0.32-10.0.0.47- you have serious inconsistencies in your pool definition and IP address definitionsE.g./ip pooladd comment="DHCP Pool for VLAN600" name=DP1-VL600-MAN ranges=80.144.1.64/26/ip addressadd address=80.144.1.1/24 comment="V1-S5-VL600-MAN Gateway" interface=V1-S5-VL600-MAN network=80.144.1.0/26 on pool and /24 on IP address ?? Align for all addresses/pools.[Julian] I have aligned them all back to /24 for consistency whilst I test it- Same on DHCP network settings/ip dhcp-server networkadd address=80.144.1.0/24 comment="Network for VLAN600" dns-server=100.48.48.1, 127.0.0.1, 8.8.8.8 gateway=80.144.1.1 netmask=24[Julian] Could you please elaborate these, I'm not sure I completely understand youWhat should it be for Management VLAN ? /24 or /26 ??Fix for all definitions.- Same on firewall NAT rules/ip firewall natadd action=masquerade chain=srcnat comment="NAT: Masquerade for VL600 to WAN" out-interface-list=WAN src-address=80.144.1.0/24Correct those things first please.UNLESS you are deliberately restricting pool sizes for those subnets ?[Julian] as above - yes ---

## Response 11
I have 3 VLANs that I want to connect to the internet, VL600 (Management) VL630 (LAN) VL710 (IOT). So far VL630 works some of the time. the other two appear to be connected (as shown by the system tray icon on the end user device) but go nowhere. Ping doesn't work. I can get to the gateway but not beyond.which device is doing the intervlan routing? the pfsense or the switch?why bother doing nat on the switch if that switch isn't an immediate device to the internet?if your lan device can ping pfsense ip (assuming allowed) then try to resolve the problem on your pfsense firewall.btw, why would you put 127.0.0.1 as dns server? ---

## Response 12
Looks like you have triple NAT-ting, if the Edgerouter is an additional device. In the end, the CRS is not a router, though it can be configured as a router. But performance will be very poor.Can you supply us with a networkdiagram that also contains the VLAN's?Can you also have a look at my remarks, through this link:viewtopic.php?p=1116969#p1116969That will also show that the WAN interface is part of the bridge. And that is far from good.At last: please don't quote complete posts, it is waisting a lot of unneccesary bits. ---

## Response 13
The WAN port definitely is not part of the bridge. It's sfp-sfplus1 and its by itself. ---

## Response 14
The WAN port definitely is not part of the bridge. It's sfp-sfplus1 and its by itself.Indeed, sfp1 is not the same as sfp-plus1... ---