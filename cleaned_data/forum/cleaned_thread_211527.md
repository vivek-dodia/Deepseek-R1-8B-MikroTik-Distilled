# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211527

# Discussion

## Initial Question
Author: Sun Oct 06, 2024 2:03 pm
``` 
```
RB5009UG(CAPsMAN,DHCP,etc.)hAPax2(CAP#1)              hAPax2 (CAP#2)VLAN1(management)192.168.1.1/24<->192.168.1.2/24<->192.168.1.3/24VLAN10(private)192.168.10.1/24<->192.168.10.2/24<->192.168.10.3/24VLAN20(devices)192.168.20.1/24<->x<->x
VLAN30(guests)192.168.30.1/24<->x<->x->allEthernetPortsconfiguredasfollowing:VLAN1,20,30tagged
    VLAN10untagged
```

```
```

```
Interface:Wifi:Datapath:Add:Name:dpath_wlan-privateBridge:vlan-bridge
                VLAN:10Add:Name:dpath_wlan-devicesBridge:vlan-bridge
                VLAN:20Add:Name:dpath_wlan-guestsBridge:vlan-bridge
                VLAN:30SecurityAdd:Name:sec_wlan-privateAuth.Types:wpa2-psk,wpa3-pskPassphrase:xxxx
                FTEnabled:enabled
                FT over DS:enabledAdd:Name:sec_wlan-devicesAuth.Types:wpa2-psk,wpa3-pskPassphrase:xxxx
                FTEnabled:enabled
                FT over DS:enabledAdd:Name:sec_wlan-guestsAuth.Types:wpa2-psk,wpa3-pskPassphrase:xxxx
                FTEnabled:enabled
                FT over DS:enabledChannel:Add:Name:chan_2GHz-AXBand:2GHzAXChannelWidth:20MHzFrequency:2300-7300ReselectInterval:00:30:00-01:00:00Add:Name:chan_5GHz-AXBand:5GHzAXChannelWidth:20/40MHzFrequency:5150-5350,5470-5725ReselectInterval:00:30:00-01:00:00Configuration:Add:Name:cfg_2G_wlan-privateSSID:wlan-privateChannel:chan_2GHz-AXSecurity:sec_wlan-privateDatapath:<-notset!!(but whyisit only workingthisway????)Add:Name:cfg_2G_wlan-devices
                SSID:wlan-devicesChannel:chan_2GHz-AXSecurity:sec_wlan-devicesDatapath:dpath_wlan-devicesAdd:Name:cfg_2G_wlan-guests
                SSID:wlan-guestsChannel:chan_2GHz-AXSecurity:sec_wlan-guestsDatapath:dpath_wlan-guestsRemoteCAP:CAPsMAN:Enabled:trueInterfaces:VLAN-Interface_1Provisioning:Add:Enabled:trueSupportedBands:2GHzAXAction:createdynamicenabledMasterConfigur.:cfg_2G_wlan-privateSlaveConfigur.:cfg_2G_wlan-devices,cfg_2G_wlan-guests
```

```
```

```
...vlan-bridge(vlan-id=1,admit all,vlan filtering enabled)......VLAN-Interface_1forVLAN1andVLAN-Interface_10forVLAN10,connectedwiththelocalvlan-bridgeforsetting IP-sddresses......all ETH-ports:VLAN1/20/30tagged,VLAN10untagged...Interface:Wifi:Datapath:Add:Name:dpath_capBridge:vlan-bridge#local bridge, without VLAN-IDWifi:edit wifi1:name:wifi1_5GConfiguration.Manager:capsmanDatapath:dpath_cap
            edit wifi2:name:wifi2_2GConfiguration.Manager:capsmanDatapath:dpath_capWifi-CAP:Enabled:trueDiscoveryInterfaces:VLAN-Interface_1#vlan-bridge in here was not workingSlavesDatapath:dpath_cap
```

Hello together,I'm running a central Router RB5009UG (as CAPsMAN) and two hAPax2 (as CAPs) and I'm a little bit struggling about the CAPsMAN datapath configurations.Basic informations:The Router itself and both APs are all configured with a central vlan-bridge (VLAN-ID=1; vlan-filtering enabled) and different VLAN-interfaces to get specific IP addresses (4 on the router, 2 on the APs):The ethernet port configuration is the same for every ETH port so I don't have to worry about what port is for what purpose - and every connected device is straight in my "private" network.(is a tagged management VLAN over ETH the right way for CAPsMAN?)The VLAN network itself is working correctly, no issues there. Wifi without CAPsMAN was also working correctly. But now I wanted to switch to CAPsMAN.My current CAPsMAN configuration on Router side (focus on 2,4GHz to not make it unnecessary complex):RB5009UG (CAPsMAN):and the configuration for both CAPs:hAPax2 (CAPs):So, right now it's working somehow... but why?The strange behaviour is, if I set the datapath "dpath_wlan-private" into configuration "cfg_2G_wlan-private" on CAPsMAN side, there is following behaviour:> wlan-private  > devices can join the network, but will not get an IP address from DHCP / there is no connectivity> wlan-devices > working correct> wlan-guests  > working correctIf I then switch the master/slave configuration under provisioning in CAPsMAN (master = cfg_2G_wlan-devices; slave = cfg_2G_wlan-private, cfg_2G_wlan-guests)> wlan-private  > working correct> wlan-devices > devices can join the network, but will not get an IP address from DHCP / there is no connectivity> wlan-guests  > working correctSo the not working SSID is glued to the wifi master configuration - why?Did I do anything wrong? Is there any obvious misconfiguration?


---
```

## Response 1
Author: Sun Oct 06, 2024 10:39 pm
rule #1 - never use VLAN 1bridge is always local entity, CAPsMAN can NOT see/access bridges on CAPs and vice versa. So, datapath configuration profile shouldn't point to any bridge. That must be done on CAPs themselfs. It exists only on device where it was defined.....and it's best to post raw output ofexport ---

## Response 2
Author: Mon Oct 07, 2024 12:27 am
``` 
```
# 2024-10-06 22:23:55 by RouterOS 7.16# software id = P16G-U29N## model = RB5009UG+S+# serial number = HF6095ZRZTP/interfacebridgeaddcomment=VLAN-Bridgename=vlan-bridge port-cost-mode=shortvlan-filtering=\
    yes/interfaceethernetset[finddefault-name=ether1]name=ether1_trunkset[finddefault-name=ether2]name=ether2_trunkset[finddefault-name=ether3]name=ether3_trunkset[finddefault-name=ether4]l2mtu=1568mac-address=xx:xx:xx:xx:xx:xx \
    name=ether4_trunkset[finddefault-name=ether5]l2mtu=1568mac-address=xx:xx:xx:xx:xx:xx \
    name=ether5_trunkset[finddefault-name=ether6]l2mtu=1568mac-address=xx:xx:xx:xx:xx:xx \
    name=ether6_trunkset[finddefault-name=ether7]l2mtu=1568mac-address=xx:xx:xx:xx:xx:xx \
    name=ether7_trunkset[finddefault-name=ether8]l2mtu=1568mac-address=xx:xx:xx:xx:xx:xx \
    name=ether8_WANset[finddefault-name=sfp-sfpplus1]name=sfp-sfpplus1_trunk/interfacewifiaddname=cap-wifi1 radio-mac=xx:xx:xx:xx:xx:xxaddname=cap-wifi2 radio-mac=xx:xx:xx:xx:xx:xx/interfacevethaddaddress=172.19.19.2/24,172.19.19.2/24gateway=172.19.19.1gateway6=""\
    name=mDNSTrunkaddaddress=172.19.19.2/24gateway=172.19.19.1gateway6=""name=mDNSTrunk/interfacewireguardaddlisten-port=13231mtu=1420name=wireguard_10_private/interfacevlanaddinterface=vlan-bridge name=VLAN-Interface_1vlan-id=1addinterface=vlan-bridge name=VLAN-Interface_10vlan-id=10addinterface=vlan-bridge name=VLAN-Interface_20vlan-id=20addinterface=vlan-bridge name=VLAN-Interface_30vlan-id=30/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacewifi channeladdband=2ghz-ax disabled=nofrequency=2300-7300name=chan_2GHz-AX \
    reselect-interval=30m..1hwidth=20mhzaddband=5ghz-ax disabled=nofrequency=5150-5350,5470-5725name=chan_5GHz-AX \
    reselect-interval=30m..1hskip-dfs-channels=all width=20/40/80mhz/interfacewifi datapathaddbridge=vlan-bridge disabled=noname=dpath_wlan-privatevlan-id=10addbridge=vlan-bridge disabled=noname=dpath_wlan-devices vlan-id=20addbridge=vlan-bridge disabled=noname=dpath_wlan-guests vlan-id=30/interfacewifi securityaddauthentication-types=wpa2-psk,wpa3-psk connect-priority=0disabled=noft=\
    yes ft-over-ds=yes name=sec_wlan-privateaddauthentication-types=wpa2-psk,wpa3-psk connect-priority=0disabled=noft=\
    yes ft-over-ds=yes name=sec_wlan-devicesaddauthentication-types=wpa2-psk,wpa3-psk connect-priority=0disabled=noft=\
    yes ft-over-ds=yes name=sec_wlan-guests/interfacewifi configurationaddchannel=chan_2GHz-AX channel.reselect-interval=30m..1hcountry=Germany\
    disabled=noname=cfg_2G_wlan-privatesecurity=sec_wlan-private\
    security.connect-priority=0ssid=wifi-privateaddchannel=chan_5GHz-AX channel.frequency=5150-5350,5470-5725\.reselect-interval=30m..1hcountry=Germanydisabled=yes name=\
    cfg_5G_wlan-privatesecurity=sec_wlan-privatesecurity.connect-priority=0\
    ssid=wifi-private_5Gaddchannel=chan_2GHz-AX channel.reselect-interval=30m..1hcountry=Germany\
    datapath=dpath_wlan-devices disabled=noname=cfg_2G_wlan-devices \
    security=sec_wlan-devices security.connect-priority=0ssid=wifi-devicesaddchannel=chan_5GHz-AX channel.frequency=5150-5350,5470-5725\.reselect-interval=30m..1hcountry=Germanydatapath=dpath_wlan-devices \
    disabled=yes name=cfg_5G_wlan-devices security=sec_wlan-devices \
    security.connect-priority=0ssid=wifi-devices_5Gaddchannel=chan_2GHz-AX channel.reselect-interval=30m..1hcountry=Germany\
    datapath=dpath_wlan-guests disabled=noname=cfg_2G_wlan-guests security=\
    sec_wlan-guests security.connect-priority=0ssid=wifi-guestsaddchannel=chan_5GHz-AX channel.frequency=5150-5350,5470-5725\.reselect-interval=30m..1hdatapath=dpath_wlan-guests disabled=yes name=\
    cfg_5G_wlan-guests security=sec_wlan-guests security.connect-priority=0\
    ssid=wifi-guests_5G/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTik/ip pooladdname=dhcp_pool_private_10 ranges=192.168.10.100-192.168.10.254addname=dhcp_pool_guests_30 ranges=192.168.30.100-192.168.30.254addname=dhcp_pool_devices_20 ranges=192.168.20.100-192.168.20.254addname=dhcp_pool_management_1 ranges=192.168.1.100-192.168.1.254addname=wireguard_pool_private ranges=10.10.10.1-10.10.10.99/ip dhcp-serveraddaddress-pool=dhcp_pool_private_10interface=VLAN-Interface_10lease-time=\23hname=dhcp_private_10addaddress-pool=dhcp_pool_devices_20interface=VLAN-Interface_20lease-time=\23hname=dhcp_devices_20addaddress-pool=dhcp_pool_guests_30interface=VLAN-Interface_30lease-time=\4hname=dhcp_devices_30addaddress-pool=dhcp_pool_management_1interface=VLAN-Interface_1\
    lease-time=23hname=dhcp_router_1 relay=192.168.1.1/ip smb usersset[finddefault=yes]disabled=yes/portset0name=serial0/containeraddenvlist=mdns hostname=mDNSinterface=mDNSTrunk logging=yes root-dir=\
    docker/container/mdns_repeater start-on-boot=yes/container envsaddkey=VLANS name=mdnsvalue="10 20 30"/interfacebridge portaddbridge=vlan-bridge comment="defconf - TRUNK"interface=ether1_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment="defconf - TRUNK"interface=ether2_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment="defconf - TRUNK"interface=ether3_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment="defconf - TRUNK"interface=ether4_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment="defconf - TRUNK"interface=ether5_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment="defconf - TRUNK"interface=ether6_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment="defconf - TRUNK"interface=sfp-sfpplus1_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment="defconf - TRUNK"interface=ether7_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment=mDNSTrunkinterface=mDNSTrunk \internal-path-cost=10path-cost=10/ip firewall connection trackingsetudp-timeout=10s/ip neighbor discovery-settingssetdiscover-interface-list=LAN/ipv6 settingssetmax-neighbor-entries=15360/interfacebridge vlanaddbridge=vlan-bridge comment=VLAN-Tagging-1tagged="vlan-bridge,sfp-sfpplus1\
    _trunk,ether1_trunk,ether2_trunk,ether3_trunk,ether4_trunk,ether5_trunk,et\
    her6_trunk,ether7_trunk,mDNSTrunk"vlan-ids=1addbridge=vlan-bridge comment=VLAN-Tagging-10tagged=\
    vlan-bridge,mDNSTrunk vlan-ids=10addbridge=vlan-bridge comment=VLAN-Tagging-20tagged="vlan-bridge,sfp-sfpplus\
    1_trunk,ether1_trunk,ether2_trunk,ether3_trunk,ether4_trunk,ether5_trunk,e\
    ther6_trunk,ether7_trunk,mDNSTrunk"vlan-ids=20addbridge=vlan-bridge comment=VLAN-Tagging-30tagged="vlan-bridge,sfp-sfpplus\
    1_trunk,ether1_trunk,ether2_trunk,ether3_trunk,ether4_trunk,ether5_trunk,e\
    ther6_trunk,ether7_trunk,mDNSTrunk"vlan-ids=30/interfacelist memberaddcomment=defconfinterface=VLAN-Interface_1list=LANaddcomment=defconfinterface=ether8_WAN list=WANaddinterface=VLAN-Interface_10list=LAN/interfacewifi capsmansetenabled=yes interfaces=VLAN-Interface_1package-path=""\require-peer-certificate=noupgrade-policy=suggest-same-version/interfacewifi provisioningaddaction=create-dynamic-enabled comment=2GHz-Banddisabled=no\
    master-configuration=cfg_2G_wlan-privateslave-configurations=\
    cfg_2G_wlan-devices,cfg_2G_wlan-guests supported-bands=2ghz-axaddaction=create-dynamic-enabled comment=5GHz-Band_#2 disabled=yes \master-configuration=cfg_5G_wlan-privateradio-mac=48:A9:8A:53:14:BB \
    slave-configurations=cfg_5G_wlan-devices,cfg_5G_wlan-guests \
    slave-name-format=""supported-bands=5ghz-axaddaction=create-dynamic-enabled comment=5GHz-Band_#3 disabled=yes \master-configuration=cfg_5G_wlan-privateradio-mac=48:A9:8A:CE:56:B7 \
    slave-configurations=cfg_5G_wlan-devices,cfg_5G_wlan-guests \
    supported-bands=5ghz-ax/interfacewireguard peersaddallowed-address=10.10.10.3/32interface=wireguard_10_private \
    name=peer2 preshared-key="xxxxx"public-key="xxxxx"addallowed-address=10.10.10.2/32interface=wireguard_10_private \
    name=peer3 preshared-key="xxxxx"public-key="xxxxx"addallowed-address=10.10.10.10/32interface=wireguard_10_private \
     name=peer5 preshared-key="xxxxx"private-key="xxxxx"public-key="xxxxx"/ip addressaddaddress=192.168.1.1/24interface=VLAN-Interface_1network=192.168.1.0addaddress=192.168.10.1/24interface=VLAN-Interface_10network=192.168.10.0addaddress=192.168.20.1/24interface=VLAN-Interface_20network=192.168.20.0addaddress=192.168.30.1/24interface=VLAN-Interface_30network=192.168.30.0addaddress=10.10.10.1/24interface=wireguard_10_private network=10.10.10.0/ip dhcp-clientaddcomment=defconfinterface=ether8_WAN/ip dhcp-server networkaddaddress=192.168.1.0/24gateway=192.168.1.1addaddress=192.168.10.0/24comment=defconf dns-server=192.168.10.10gateway=\192.168.10.1netmask=24addaddress=192.168.20.0/24comment=devices dns-server=192.168.10.10gateway=\192.168.20.1addaddress=192.168.30.0/24comment=guests dns-server=192.168.10.10gateway=\192.168.30.1/ip dnssetallow-remote-requests=yes servers=9.9.9.9,149.112.112.112use-doh-server=\
    https://dns.quad9.net/dns-query verify-doh-cert=yes/ip dnsstaticaddaddress=192.168.10.1comment=defconf name=router.lan type=A/ip firewall address-listaddaddress=0.0.0.0/8comment=RFC6890 list=not_in_internetaddaddress=172.16.0.0/12comment=RFC6890 list=not_in_internetaddaddress=192.168.0.0/16comment=RFC6890 list=not_in_internetaddaddress=10.0.0.0/8comment=RFC6890 list=not_in_internetaddaddress=169.254.0.0/16comment=RFC6890 list=not_in_internetaddaddress=127.0.0.0/8comment=RFC6890 list=not_in_internetaddaddress=224.0.0.0/4comment=Multicastlist=not_in_internetaddaddress=198.18.0.0/15comment=RFC6890 list=not_in_internetaddaddress=192.0.0.0/24comment=RFC6890 list=not_in_internetaddaddress=192.0.2.0/24comment=RFC6890 list=not_in_internetaddaddress=198.51.100.0/24comment=RFC6890 list=not_in_internetaddaddress=203.0.113.0/24comment=RFC6890 list=not_in_internetaddaddress=100.64.0.0/10comment=RFC6890 list=not_in_internetaddaddress=240.0.0.0/4comment=RFC6890 list=not_in_internetaddaddress=192.88.99.0/24comment="6to4 relay Anycast [RFC 3068]"list=\
    not_in_internet/ip firewall filteraddaction=accept chain=forward comment="# ENABLE for transparent firewall"\
    disabled=yesaddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=drop chain=forward comment=\"drop access to clients behind NAT from WAN"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WANaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"disabled=yes \
    dst-address=127.0.0.1addaction=accept chain=input comment="accept Wireguard"\
    dst-port=13231in-interface-list=WAN protocol=udpaddaction=accept chain=input disabled=yes src-address=10.10.10.0/24addaction=accept chain=forward dst-address=192.168.10.10dst-port=53\in-interface=wireguard_10_private protocol=tcpaddaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WANaddaction=accept chain=forward comment=\"ENABLE - allow DNSserver connection (UDP)"dst-address=192.168.10.10\
    dst-port=53protocol=udpaddaction=accept chain=forward comment=\"ENABLE - allow DNSserver connection (TCP)"dst-address=192.168.10.10\
    dst-port=53protocol=tcpaddaction=accept chain=forward comment=\"ENABLE - devices on device subnet to reach each other"dst-address=\192.168.20.0/24in-interface=VLAN-Interface_20src-address=\192.168.20.0/24addaction=accept chain=forward comment=\"ENABLE - Spotify Connect for guests -> devices"dst-port=1400,7000,33499\in-interface=VLAN-Interface_30out-interface=VLAN-Interface_20protocol=\
    tcpaddaction=accept chain=forward comment=\"ENABLE - Airplay for guests -> devices"in-interface=VLAN-Interface_30\out-interface=VLAN-Interface_20port=80,443,554,3689,4070,49152-65535\
    protocol=tcpaddaction=accept chain=forward comment=\"ENABLE - Airplay for guests -> devices"dst-port=30000-65535\in-interface=VLAN-Interface_30out-interface=VLAN-Interface_20protocol=\
    udpaddaction=drop chain=forward comment="devices - no access to private network"\
    dst-address-list=not_in_internet log-prefix=DROP_REQ_20->x src-address=\192.168.20.0/24addaction=drop chain=forward comment="guests - no access to private network"\
    dst-address-list=not_in_internet log-prefix=DROP_REQ_30->x src-address=\192.168.30.0/24/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WANaddaction=masquerade chain=srcnat dst-address=192.168.20.15/ip route/ip servicesettelnet disabled=yessetftp disabled=yessetssh disabled=yessetapi-ssl disabled=yes/ip smb sharesset[finddefault=yes]directory=/pub/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMPv6"protocol=\
    icmpv6addaction=accept chain=input comment="defconf: accept UDP traceroute"port=\33434-33534protocol=udpaddaction=accept chain=input comment=\"defconf: accept DHCPv6-Client prefix delegation."dst-port=546protocol=\
    udp src-address=fe80::/10addaction=accept chain=input comment="defconf: accept IKE"dst-port=500,4500\
    protocol=udpaddaction=accept chain=input comment="defconf: accept ipsec AH"protocol=\
    ipsec-ahaddaction=accept chain=input comment="defconf: accept ipsec ESP"protocol=\
    ipsec-espaddaction=accept chain=input comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=input comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LANaddaction=accept chain=forward comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop packets with bad src ipv6"src-address-list=bad_ipv6addaction=drop chain=forward comment=\"defconf: drop packets with bad dst ipv6"dst-address-list=bad_ipv6addaction=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1"\
    hop-limit=equal:1protocol=icmpv6addaction=accept chain=forward comment="defconf: accept ICMPv6"protocol=\
    icmpv6addaction=accept chain=forward comment="defconf: accept HIP"protocol=139addaction=accept chain=forward comment="defconf: accept IKE"dst-port=\500,4500protocol=udpaddaction=accept chain=forward comment="defconf: accept ipsec AH"protocol=\
    ipsec-ahaddaction=accept chain=forward comment="defconf: accept ipsec ESP"protocol=\
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/system clocksettime-zone-name=Europe/Berlin/system identitysetname=MikroTik-#1/system ledsset0leds=""type=poe-out/system notesetshow-at-login=no/system ntp clientsetenabled=yes/system ntp client serversaddaddress=ptbtime1.ptb.deaddaddress=ptbtime2.ptb.deaddaddress=ptbtime3.ptb.de/tool mac-serversetallowed-interface-list=none/tool mac-server mac-winboxsetallowed-interface-list=none/tool mac-server pingsetenabled=no
```

```
```

```
# 2024-10-06 22:27:07 by RouterOS 7.16# software id = EE37-T5A7## model = C52iG-5HaxD2HaxD# serial number = HEH08HPHFZ0/interfacebridgeaddcomment=VLAN-Bridgename=vlan-bridge port-cost-mode=shortvlan-filtering=\
    yes/interfaceethernetset[finddefault-name=ether1]name=ether1_trunkset[finddefault-name=ether2]name=ether2_trunkset[finddefault-name=ether3]name=ether3_trunkset[finddefault-name=ether4]name=ether4_trunkset[finddefault-name=ether5]name=ether5_trunk/interfacevlanaddinterface=vlan-bridge name=VLAN-Interface_1vlan-id=1addinterface=vlan-bridge name=VLAN-Interface_10vlan-id=10addinterface=vlan-bridge name=VLAN-Interface_20vlan-id=20addinterface=vlan-bridge name=VLAN-Interface_30vlan-id=30/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacewifi datapathaddbridge=vlan-bridge disabled=noname=dpath_cap/interfacewifi# managed by CAPsMANset[finddefault-name=wifi1]configuration.manager=capsman.mode=ap \
    datapath=dpath_cap disabled=nomac-address=xx:xx:xx:xx:xx:xx name=\
    wifi1_5.0Gsecurity.connect-priority=0# managed by CAPsMAN# mode: AP, SSID: wifi-private, channel: 2462/axset[finddefault-name=wifi2]\
    configuration.manager=capsman.mode=ap datapath=dpath_cap disabled=no\
    name=wifi2_2G security.connect-priority=0/ip smb usersset[finddefault=yes]disabled=yes/portset0name=serial0/interfacebridge portaddbridge=vlan-bridge comment=defconfinterface=ether2_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment=defconfinterface=ether3_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment=defconfinterface=ether4_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment="defconf - TRUNK"interface=ether1_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-taggedinterface=wifi1_5.0G\internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-taggedinterface=wifi2_2G \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridgeinterface=ether5_trunkinternal-path-cost=10\
    path-cost=10pvid=10/ip firewall connection trackingsetudp-timeout=10s/ip neighbor discovery-settingssetdiscover-interface-list=LAN/ipv6 settingssetmax-neighbor-entries=15360/interfacebridge vlanaddbridge=vlan-bridge comment=VLAN-Tagging-1tagged="vlan-bridge,ether1_trunk\
    ,ether2_trunk,ether3_trunk,ether4_trunk,ether5_trunk"vlan-ids=1addbridge=vlan-bridge comment=VLAN-Tagging-10tagged=vlan-bridge vlan-ids=10addbridge=vlan-bridge comment=VLAN-Tagging-20tagged="vlan-bridge,ether1_trun\
    k,ether2_trunk,ether3_trunk,ether4_trunk,ether5_trunk"vlan-ids=20addbridge=vlan-bridge comment=VLAN-Tagging-30tagged="vlan-bridge,ether1_trun\
    k,ether2_trunk,ether3_trunk,ether4_trunk,ether5_trunk"vlan-ids=30/interfacelist memberaddcomment=defconfinterface=VLAN-Interface_1list=LANaddinterface=VLAN-Interface_10list=LAN/interfacewifi capsetdiscovery-interfaces=VLAN-Interface_1enabled=yes slaves-datapath=\
    dpath_cap/ip addressaddaddress=192.168.1.3/24interface=VLAN-Interface_1network=192.168.1.0addaddress=192.168.10.3/24interface=VLAN-Interface_10network=192.168.10.0addaddress=192.168.20.3/24disabled=yesinterface=VLAN-Interface_20network=\192.168.20.0addaddress=192.168.30.3/24disabled=yesinterface=VLAN-Interface_30network=\192.168.30.0/ip dnsstaticaddaddress=192.168.10.1comment=defconf name=router.lan type=A/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip routeadddisabled=nodistance=1dst-address=0.0.0.0/0gateway=192.168.1.1\
    pref-src=""routing-table=main scope=30suppress-hw-offload=no\
    target-scope=10/ip servicesettelnet disabled=yessetftp disabled=yessetssh disabled=yessetapi-ssl disabled=yes/ip smb sharesset[finddefault=yes]directory=/pub/system clocksettime-zone-name=Europe/Berlin/system identitysetname=MikroTik-#3/system notesetshow-at-login=no/system ntp clientsetenabled=yes/system ntp client serversaddaddress=ptbtime1.ptb.deaddaddress=ptbtime2.ptb.deaddaddress=ptbtime3.ptb.de/tool mac-serversetallowed-interface-list=none/tool mac-server mac-winboxsetallowed-interface-list=none/tool mac-server pingsetenabled=no
```

Thanks for your reply.Why do you think the use of VLAN 1 is no good idea?A reference to a bridge can only be done locally, thats clear. My bridge on CAPsMAN Router has the same naming as the bridge on the CAPs ("vlan-bridge").I thought it would be better to simplify the topic. If full configuration is helpful, here it is:Router (CAPsMAN):2x hAPax2 (CAPs):


---
```

## Response 3
Author: Mon Oct 07, 2024 8:05 pm
``` 
```
/interfacewifi capsetdiscovery-interfaces=VLAN-Interface_1enabled=yes slaves-datapath=\
    dpath_cap
```

```
```

```
/interfacewifiset[finddefault-name=wifi1]configuration.manager=capsman.mode=ap \
    datapath=dpath_cap disabled=nomac-address=xx:xx:xx:xx:xx:xx name=\
    wifi1_5.0Gsecurity.connect-priority=0
```

```
```

```
/interfacebridge portaddbridge=vlan-bridge comment=defconfinterface=ether2_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment=defconfinterface=ether3_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment=defconfinterface=ether4_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment="defconf - TRUNK"interface=ether1_trunk \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-taggedinterface=wifi1_5.0G\internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-taggedinterface=wifi2_2G \internal-path-cost=10path-cost=10pvid=10addbridge=vlan-bridgeinterface=ether5_trunkinternal-path-cost=10\
    path-cost=10pvid=10
```

Reason why it was working as described isslaves-datapathunderinterface wifi cap. By default slave interfaces inherit datapath from master interface, anyway setup script, for some reason, creates bridge, then datapath and then sets this datapath toslaves-datapath. So it overrides default behavior but initially the result is same.If you screwed your datapath.bridge configuration for your master interface, slaves were working because they were using different setting.You surely played with those, because it's renamed. Question is, it's now working or not?There is now datapath.bridge set on master interface... Was it like this initially?I will completely avoid VLANs, because I think it's wrong, but if you are sure what are you doing...I would also change:Set identities to something more meaningful, like RB5009, hAP-ax2-01 and so on..Setname-formatin provisioning to something like%I-2G-wifi, that way you will end up with nice list of interfaces..Stop usingreselect-interval, I would rather use frequency that I want..And for that you will need to provision your interfaces withcreate-enabledinstead ofcreate-dynamic-enabledso you can manually adjust interface settings..And looking on your config again (CAP):It looks like you manually added wifi interfaces as ports to your bridge, this should be done dynamically by... surprise surprise datapath.bridge on the interface itself.And another look, don't you have wireless package on your RB5009? You don't need it for AX devices...


---
```

## Response 4
Author: Wed Oct 09, 2024 8:16 pm
``` 
```
on capsman side:Interface:Wifi:Datapath:Add:# added this datapath, deleted all others.# This datapath is then used for the wifi configurations for provisioning.Name:dpath_bridgeBridge:vlan-bridgeRemoteCAP:CAPsMAN:Edit:Enabled:trueInterfaces:VLAN-Interface_1on CAP side:...manually created wifi slave interfaces......manually added all wifi interfacesasbridge ports+untaggedthisinterfaces underBridge->VLAN...Interface:Wifi-CAP:Enabled:trueDiscoveryInterfaces:VLAN-Interface_1SlavesStatic:true# added this settingSlavesDatapath:-# so no datapath at all on CAP side
```

Thanks a lot again!So first of all great hint regarding the naming of the wifi-interfaces - that bothered me a lot..I read your comment in detail and tried to understand it - it gave me a good hint.I then read threw the "old" mikrotik "wiki":https://wiki.mikrotik.com/Manual:CAPsMANSub-menu: /caps-man configurationdatapath.bridge :   Bridge to which particular interface should be automatically added as port. Required only when local-forwarding is not used.Then AGAIN read threw the new mikrotik "Help" for Capsman (from new wifi package)https://help.mikrotik.com/docs/display/ ... propertiesThey distinguish between configs for AC- and AX-devices. I tried to understand the difference.>>   The AX-example doesn't configure VLANs on CAP side at all, speaking only with CAPSMAN over the "untagged ethernet line". (?)In this example the CAPsMAN config has datapaths to his own bridge (with VLAN tags) -> to inject the traffic on CAPsMAN side to the right VLAN (like the behavior of the old wireless capsman if local-forwarding was disabled). (?)>> The AC-example does configure the full vlan-functionality on CAPs side, create wifi slaves / add them manually to the local bridge.So VLAN assignment is done on CAP side and traffic is injected to the VLANs there.What I did in my config (more like the AC-config):So now it is working as intended. Even if I don't know if I'm completely right.I've one additional question regarding the provisioning option "create-enabled".Where should I set the fixed frequency? I set the frequency from the wifi interface overview on my RB5009 (CAPsMAN).Two problems with this solution:- when the device restarts / new provisioning occur the setting is lost and I have to set the frequency again.- The fixed frequency is provisioned, but is not used. See following image ((1) for provisioned frequency, (2) current used frequency) - image from the CAPs own wifi list


---
```

## Response 5
Author: Wed Oct 09, 2024 10:31 pm
Just few hints...Wiki is/was for ROS 6 only, so it's obsolete for ROS 7 and especially for WiFi CAPsMAN. Old Wireless CAPsMAN had two modes, local forwarding and manager forwarding and you have to be careful when you are looking at configs on internet because most of the users took manager forwarding as standard. New WiFi CAPsMAN has only one mode, local forwarding. That means that each AP have to decide what will happen with each packed that it handles.>>1 That's not how it works, local forwarding... everything is decided on CAP side, period.>>2 wifi-qcom-ac is basically afterthought and not every feature is available there, notably for CAPsMAN, it can not asign VLAN dynamically. You don't have any AC device, so you don't have to care...Provisioning should be used "ONCE", it is NOT "configuration propagation". It is basically introduction of new interface and that's it. If you re-provision interface all settings made manually will be lost, that is expected, but again it should be used just once, so it shouldn't be issue. This shouln't happen on reboot! If it does, there is something wrong...For the naming, nice try but you should follow my advice to the letter.%Iis variable, capital i as identity, it will be replaced by... device identity. So you can get something like hAP-ax2-01-wifi1Anyway... if you want help or check config post your configs ....in raw formatJust as addition, this is how it looks when you have (D) dynamically assigned VLANs by datapathbrdynvlan.png ---

## Response 6
Author: [SOLVED]Sun Feb 02, 2025 2:35 pm
Solution:I tried again to change my capsman configuration to what it should be.After some retry and seeing the same weird behavior I realized something important, "Wireless" package was installed on my capsman Router.If capsman should only talk to AX-devices there should be NO "wireless" package installed (nor "wifi-qcom", if the Router has no wifi itself).Hint to:https://preview.redd.it/replacing-wirel ... 4e54b97cdfAfter uninstalling the package - and configuring capsman how it's described in the mikrotik support page - the wifi's were created on the CAP + bridged with the right VLAN-Address to the bridge!What I've done differently in my config, compared to the manual:- configuring the VLAN for all ether ports manually on the CAPs- it worked only if discovery interface = VLAN-Interface-1 on capsman&cap side (instead of bridges)Thanks for support!