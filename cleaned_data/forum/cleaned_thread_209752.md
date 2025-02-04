# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 209752

# Discussion

## Initial Question
Author: Thu Aug 01, 2024 5:29 pm
Hello, I have internet connection in one room and all my homelab with another with no option to move cable there.Therefore I have decided to set-up a wirless bridge between those two room. It must be completely transparent as one server in my homelab is a router firewall.[ LAN ] -- router@homelab ------ /wired/ ----- Mikrotik cAP AC [2] ---- (wireless brige) ---- Mikrotik cAP AC [1] ------ /wired/ ----- Internet provider's router in bridge modeAll works fine but I am disappointed with performance and I am not able to pin down the issue.All in all from router@homelab I can access internet (and router itself is assigned public IP from provider) but only with speed (average) up to 150Mbp/s DL and 50 Mbit/s UL.As internet provider delivers 450Mb/s DL and 50Mb/s UP, I would expect ~ 300Mbit/s DL, especially that when I connect directly to modem (wire) I get ~ 450Mb/s DL and 50 Mbit/s UL.I have tired different 5Ghz channels, also NV2 protocol w/o effect.Question: Any hints for troubleshooting?How to measure from where the slow down takes place?Connection between both routers seems to be OK:Tx Rate 585Mbps-80MHz/2S/SGIRx Rate 520Mbps-80MHz/2S/SGI (it is changing up/down to 390Mbps-80MHz/2S/SGI)Tx/Rx Signal Strength -51/-57 dBmTx/Rx Signal Strength Ch0 -52/-61 dBmTx/Rx Signal Strength Ch1 -59/-60 dBmNoise Floor -107 dBmSignal To Noise 50 dBTx/Rx CCQ 95/68Overall Tx CCQ 95 %RouterOS Version 7.15.3 ---

## Response 1
Author: Thu Aug 01, 2024 6:34 pm
Follow this:viewtopic.php?t=203686#p1051720and post current configuration of both devices. ---

## Response 2
Author: Mon Aug 26, 2024 12:15 pm
``` 
```
# 2024-08-25 22:13:03 by RouterOS 7.15.3
# software id = ******
#
# model = RBcAPGi-5acD2nD
# serial number = ******
/interface bridge
add name=WLAN_BRIDGE protocol-mode=none
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface wireless channels
add band=5ghz-onlyac comment=Normal extension-channel=eCee frequency=5280 \
    list=skierka.net name=5280_SKIGR width=20
add band=5ghz-onlyac extension-channel=Ceee frequency=5520 list=skierka.net \
    name=5520_SKIGR width=20
add band=5ghz-onlyac comment=DFS disabled=yes extension-channel=Ceee \
    frequency=5600 list=skierka.net name=5600_SKIGR width=20
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
add authentication-types=wpa2-psk disable-pmkid=yes eap-methods=\
    eap-ttls-mschapv2 group-ciphers=tkip,aes-ccm mode=dynamic-keys \
    mschapv2-username=wbridge name=wbridge supplicant-identity=wbridge \
    unicast-ciphers=tkip,aes-ccm
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-onlyn channel-width=20/40mhz-XX \
    country=poland distance=indoors frequency=auto installation=indoor mode=\
    bridge nv2-security=enabled security-profile=wbridge ssid=wbridge2.4 \
    tdma-period-size=auto wireless-protocol=802.11 wmm-support=enabled
set [ find default-name=wlan2 ] band=5ghz-onlyac channel-width=\
    20/40/80mhz-Ceee country=poland disabled=no distance=indoors frequency=\
    5520_SKIGR installation=indoor max-station-count=5 mode=bridge \
    nv2-cell-radius=10 nv2-downlink-ratio=80 nv2-security=enabled \
    preamble-mode=short scan-list=skierka.net security-profile=wbridge \
    skip-dfs-channels=10min-cac ssid=wbridge.skierka.net tdma-period-size=\
    auto tx-power=18 tx-power-mode=all-rates-fixed wireless-protocol=802.11 \
    wmm-support=enabled wps-mode=disabled
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
add name=dhcp_pool1 ranges=10.10.10.2-10.10.10.254
/interface bridge port
add bridge=WLAN_BRIDGE interface=ether1
add bridge=WLAN_BRIDGE interface=wlan2
add bridge=WLAN_BRIDGE interface=wlan1
/ip neighbor discovery-settings
set discover-interface-list=LAN
/ipv6 settings
set disable-ipv6=yes
/interface list member
add comment=defconf interface=*4 list=LAN
add comment=defconf disabled=yes interface=ether1 list=WAN
/ip address
add address=192.168.88.1/24 comment=defconf interface=*4 network=192.168.88.0
/ip dhcp-client
# DHCP client can not run on slave or passthrough interface!
add comment=defconf interface=ether1
add interface=ether2
/ip dhcp-server network
add address=10.10.10.0/24 gateway=10.10.10.1
add address=192.168.88.0/24 comment=defconf dns-server=192.168.88.1 gateway=\
    192.168.88.1
/ip dns
set allow-remote-requests=yes
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan
/ip firewall filter
add action=accept chain=input in-interface=ether2 src-address=0.0.0.0
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
/ip firewall service-port
set ftp disabled=yes
/ip hotspot profile
set [ find default=yes ] html-directory=hotspot
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www address=0.0.0.0/0,192.168.15.0/24
set ssh address=192.168.15.0/24,192.168.20.0/24
set www-ssl address=0.0.0.0/0 disabled=no
set api disabled=yes
set winbox disabled=yes
set api-ssl disabled=yes
/ipv6 firewall address-list
add address=::/128 comment="defconf: unspecified address" list=bad_ipv6
add address=::1/128 comment="defconf: lo" list=bad_ipv6
add address=fec0::/10 comment="defconf: site-local" list=bad_ipv6
add address=::ffff:0.0.0.0/96 comment="defconf: ipv4-mapped" list=bad_ipv6
add address=::/96 comment="defconf: ipv4 compat" list=bad_ipv6
add address=100::/64 comment="defconf: discard only " list=bad_ipv6
add address=2001:db8::/32 comment="defconf: documentation" list=bad_ipv6
add address=2001:10::/28 comment="defconf: ORCHID" list=bad_ipv6
add address=3ffe::/16 comment="defconf: 6bone" list=bad_ipv6
/ipv6 firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=input comment="defconf: accept UDP traceroute" \
    dst-port=33434-33534 protocol=udp
add action=accept chain=input comment=\
    "defconf: accept DHCPv6-Client prefix delegation." dst-port=546 protocol=\
    udp src-address=fe80::/10
add action=accept chain=input comment="defconf: accept IKE" dst-port=500,4500 \
    protocol=udp
add action=accept chain=input comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=input comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=input comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=input comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
add action=accept chain=forward comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop packets with bad src ipv6" src-address-list=bad_ipv6
add action=drop chain=forward comment=\
    "defconf: drop packets with bad dst ipv6" dst-address-list=bad_ipv6
add action=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1" \
    hop-limit=equal:1 protocol=icmpv6
add action=accept chain=forward comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=forward comment="defconf: accept HIP" protocol=139
add action=accept chain=forward comment="defconf: accept IKE" dst-port=\
    500,4500 protocol=udp
add action=accept chain=forward comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=forward comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=forward comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=forward comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
/system identity
set name=cAP_AC_1
/system note
set show-at-login=no
/system routerboard mode-button
set enabled=yes on-event=dark-mode
/system script
add comment=defconf dont-require-permissions=no name=dark-mode owner=*sys \
    policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    source="\r\
    \n   :if ([system leds settings get all-leds-off] = \"never\") do={\r\
    \n     /system leds settings set all-leds-off=immediate \r\
    \n   } else={\r\
    \n     /system leds settings set all-leds-off=never \r\
    \n   }\r\
    \n "
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN
```

```
```

```
# 2024-08-26 10:29:17 by RouterOS 7.15.3
# software id = ******
#
# model = RBcAPGi-5acD2nD
# serial number = *******
/interface bridge
add name=WLAN_BRIDGE port-cost-mode=short protocol-mode=none
/interface ethernet
set [ find default-name=ether2 ] poe-out=off rx-flow-control=auto \
    tx-flow-control=auto
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface lte apn
set [ find default=yes ] ip-type=ipv4 use-network-apn=no
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
add authentication-types=wpa2-psk eap-methods="" group-ciphers=tkip,aes-ccm \
    mode=dynamic-keys name=wbridge supplicant-identity=wbridge \
    unicast-ciphers=tkip,aes-ccm
/interface wireless
set [ find default-name=wlan1 ] adaptive-noise-immunity=ap-and-client-mode \
    band=2ghz-onlyn channel-width=20/40mhz-XX country=poland distance=indoors \
    frequency=auto installation=indoor mode=station-bridge nv2-security=\
    enabled preamble-mode=short security-profile=wbridge ssid=wbridge2.4 \
    wireless-protocol=802.11 wmm-support=enabled
set [ find default-name=wlan2 ] band=5ghz-onlyac channel-width=\
    20/40/80mhz-XXXX country=poland disabled=no distance=indoors frequency=\
    auto installation=indoor mode=station-bridge nv2-security=enabled \
    preamble-mode=short security-profile=wbridge ssid=wbridge.skierka.net \
    wireless-protocol=nv2-nstreme-802.11 wmm-support=enabled wps-mode=\
    disabled
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
/ip smb users
set [ find default=yes ] disabled=yes
/routing bgp template
set default disabled=no output.network=bgp-networks
/routing ospf instance
add disabled=no name=default-v2
/routing ospf area
add disabled=yes instance=default-v2 name=backbone-v2
/ip smb
set enabled=no
/interface bridge port
add bridge=WLAN_BRIDGE ingress-filtering=no interface=wlan2 \
    internal-path-cost=10 path-cost=10
add bridge=WLAN_BRIDGE ingress-filtering=no interface=ether1 \
    internal-path-cost=10 path-cost=10
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=LAN
/ip settings
set max-neighbor-entries=8192
/ipv6 settings
set disable-ipv6=yes max-neighbor-entries=8192
/interface list member
add comment=defconf interface=*5 list=LAN
add comment=defconf interface=ether1 list=WAN
/interface ovpn-server server
set auth=sha1,md5
/interface wireless align
set audio-max=-30 audio-monitor=D4:01:C3:01:3D:B0 filter-mac=\
    D4:01:C3:01:3D:B0 receive-all=yes ssid-all=yes
/ip dhcp-client
add interface=ether2
/ip dhcp-server network
add address=192.168.88.0/24 comment=defconf gateway=192.168.88.1
/ip dns
set allow-remote-requests=yes
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan
/ip firewall filter
add action=accept chain=input in-interface=ether2 src-address=192.168.20.0/24
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www address=192.168.15.0/24
set ssh address=192.168.15.0/24
set www-ssl address=192.168.15.0/24,192.168.20.0/24 disabled=no
set api disabled=yes
set winbox disabled=yes
set api-ssl disabled=yes
/ip smb shares
set [ find default=yes ] directory=/flash/pub
/routing bfd configuration
add disabled=no interfaces=all min-rx=200ms min-tx=200ms multiplier=5
/system clock
set time-zone-name=Europe/Warsaw
/system identity
set name=cAP_AC_2
/system note
set show-at-login=no
/system ntp client
set enabled=yes
/system ntp client servers
add address=192.168.15.1 comment=pfsense
/system routerboard mode-button
set enabled=yes on-event=dark-mode
/system script
add comment=defconf dont-require-permissions=no name=dark-mode owner=*sys \
    policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    source="\r\
    \n   :if ([system leds settings get all-leds-off] = \"never\") do={\r\
    \n     /system leds settings set all-leds-off=immediate \r\
    \n   } else={\r\
    \n     /system leds settings set all-leds-off=never \r\
    \n   }\r\
    \n "
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN
```

cAP AC 1 configuration:cAP AC 2 configuration:


---
```

## Response 3
Author: Mon Aug 26, 2024 2:11 pm
Do you send the traffic over the 2.4 wireless bridge? ---

## Response 4
Author: Mon Aug 26, 2024 2:51 pm
You are running wireless PtP on non-directional equipment with a (or more?) wall in between. Your results seems fine to me. ---

## Response 5
Author: Mon Aug 26, 2024 3:08 pm
Question: Any hints for troubleshooting?How to measure from where the slow down takes place?You can use BTest to check what throughput the 2 caps are getting to each other.https://help.mikrotik.com/docs/display/ ... width+TestEdit: Keep in mind that this might reach the limit of the caps before the interface is fully utilized like the page mentions.CPU usage is shown while running a BTest ---

## Response 6
Author: Mon Aug 26, 2024 4:48 pm
Question: Any hints for troubleshooting?How to measure from where the slow down takes place?You can use BTest to check what throughput the 2 caps are getting to each other.https://help.mikrotik.com/docs/display/ ... width+TestEdit: Keep in mind that this might reach the limit of the caps before the interface is fully utilized like the page mentions.CPU usage is shown while running a BTestI cannot measure directly connection between cAP AC 1 and cAP AC 2 as its point-to-point L2 bridge, wireless interfaces does not have IP addresses. I have link both of them via ETH port temporarily to other VLAN (to not have routing loop) so I can manage them. I have tested iperf from laptop linked directly to cAP AC 2 to iperf server on edge of WAN provider network and I run the same test with laptop linked to WAN router directly (by-pass cAP AC 1). For laptop - modem it's around 450Mbit/s download for laptop - cAP AC 2 it is 120-150Mb/its. ---

## Response 7
Author: Mon Aug 26, 2024 4:51 pm
You are running wireless PtP on non-directional equipment with a (or more?) wall in between. Your results seems fine to me.It is what I am trying to figure out. Yes it's non-directional equipment but there is 7-10 m line across two walls in which the wooden doors are.I do not expect to get theoretical 867 Mbit/s but I have expected something around 300Mbit/s. I have merely half of it.Edit:I think I move cAP 2 with long UTP cable to the floor so there is clear line of sign (through two open doors to the cAP 1) and see if this make a difference. ---

## Response 8
Author: Mon Aug 26, 2024 4:55 pm
Do you send the traffic over the 2.4 wireless bridge?No it's only 5Ghz, the 2.4Ghz is not used due to number of networks around. ---

## Response 9
Author: Mon Aug 26, 2024 6:50 pm
I do not expect to get theoretical 867 Mbit/s but I have expected something around 300Mbit/s. I have merely half of it.With legacy wireless driver in use, it's impossible to get more than around half of theoretical throughput ... in ideal radio conditions (that would be around 430Mbps). And then non-ideal radio conditions kick in and with 7m distance and two walls in between getting around one third of practical maximum is still quite fine.Beware that cAP ac have circular antenna pattern with minima in directions perpendicular to overall device shape. So for best signal strength and best MIMO perfromance, make sure that devices "see" each other to the side of case, like this (it can be vertical direction as well):andnotlike this:Since your both devices are cAP ac, you could replace wireless with wifi-qcom-ac ... these drivers perform much better (in ideal radio conditions it's possible to get up to 75% of theoretical throughput), many AC devices perform quite much better also in non-ideal radio conditions. But you'll have to re-do the config from scratch. ---

## Response 10
Author: Mon Aug 26, 2024 9:51 pm
I do not expect to get theoretical 867 Mbit/s but I have expected something around 300Mbit/s. I have merely half of it.With legacy wireless driver in use, it's impossible to get more than around half of theoretical throughput ... in ideal radio conditions (that would be around 430Mbps). And then non-ideal radio conditions kick in and with 7m distance and two walls in between getting around one third of practical maximum is still quite fine.Beware that cAP ac have circular antenna pattern with minima in directions perpendicular to overall device shape. So for best signal strength and best MIMO perfromance, make sure that devices "see" each other to the side of case, like this (it can be vertical direction as well):andnotlike this:Since your both devices are cAP ac, you could replace wireless with wifi-qcom-ac ... these drivers perform much better (in ideal radio conditions it's possible to get up to 75% of theoretical throughput), many AC devices perform quite much better also in non-ideal radio conditions. But you'll have to re-do the config from scratch.I have changed position of cAP ac slightly (I am not able to match them side be side on the line of sigh) and I get solid 180Mbit/s Upload. I have not tried wifi-qcom-ac drivers as all Mikrotik is a little bit mystery for me. As I understand it would require to do entire PtP configuration via WiFi tab and not Wireless / Wireless tab.Do you think that switching to directed 60Ghz bases solution like Mikrotik wireless wire would make sense here? I cannot use cables and need to connect these two points with reliable at least 300Mibt/s upload / 50 Mbit/s link. ---

## Response 11
Author: [SOLVED]Mon Aug 26, 2024 11:52 pm
60 GHz needs direct line of sight, no ifs, no buts.If you have that, go for it, but if you have even a japanese style paper wall between the two devices 60 GHz won't work properly.Devices like the Cube Pro have a backup at 5 GHz because fog or relatively heavy rain can break the 60 GHz connection. ---

## Response 12
Author: Thu Jan 30, 2025 5:09 pm
Just a short update after a while.I have upgraded my both cAP ac to routeos 7.17 and switched to wifi-qcom-ac 7.17 as a result I have stable 280Mb/s throughput which is 25% more than the best I could get using legacy drivers (@peak performance) but it is really stable.