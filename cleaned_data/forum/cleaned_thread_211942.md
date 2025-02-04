# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211942

# Discussion

## Initial Question
Author: Tue Oct 22, 2024 11:59 am
``` 
```
# 1970-01-19 22:46:25 by RouterOS 7.14.3
# software id = #####
#
# model = C52iG-5HaxD2HaxD
# serial number = ######
/interface bridge
add frame-types=admit-only-vlan-tagged name=Bridge vlan-filtering=yes
/interface vlan
add interface=Bridge name=VLAN99-Management vlan-id=99
/interface wifi datapath
add bridge=Bridge disabled=no name=VLAN10-Default vlan-id=10
add bridge=Bridge client-isolation=yes disabled=no name=VLAN100-Guest \
    vlan-id=100
add bridge=Bridge disabled=no name=VLAN99-Management vlan-id=99
add bridge=Bridge disabled=no name=VLAN80-IoT vlan-id=80
/interface wifi
add configuration=geelenioIoT configuration.mode=ap datapath=VLAN80-IoT \
    datapath.bridge=Bridge .client-isolation=no disabled=no mac-address=\
    D6:01:##:##:##:3A master-interface=geelenioMngt_2.4GHz name=geelenIoT \
    security.authentication-types=wpa2-psk,wpa3-psk
set [ find default-name=wifi1 ] configuration=geelenio configuration.country=\
    Germany .mode=ap .ssid=geelenio datapath=VLAN10-Default disabled=no name=\
    geelenio security.authentication-types=wpa3-psk
add configuration=geelenioGuest configuration.mode=ap datapath=VLAN100-Guest \
    datapath.client-isolation=yes disabled=no mac-address=D6:01:##:##:##:39 \
    master-interface=geelenio name=geelenioGuest \
    security.authentication-types=wpa2-psk,wpa3-psk
add configuration=geelenioGuest_2.4Ghz configuration.mode=ap .ssid=\
    geelenioGuest_2.4GHz datapath=VLAN100-Guest disabled=no mac-address=\
    D6:01:##:##:##:3B master-interface=geelenioMngt_2.4GHz name=\
    geelenioGuest_2.4GHz security.authentication-types=wpa2-psk,wpa3-psk
add configuration=geelenioMngt configuration.mode=ap datapath=\
    VLAN99-Management datapath.vlan-id=99 disabled=no mac-address=\
    D6:01:##:##:##:38 master-interface=geelenio name=geelenioMngt \
    security.authentication-types=wpa3-psk
set [ find default-name=wifi2 ] configuration=geelenioMngt \
    configuration.country=Germany .mode=ap .ssid=geelenioMngt_2.4GHz \
    datapath=VLAN99-Management disabled=no name=geelenioMngt_2.4GHz \
    security.authentication-types=wpa3-psk
/interface bridge port
add bridge=Bridge interface=ether5 pvid=99
add bridge=Bridge interface=ether1
add bridge=Bridge interface=ether2 pvid=10
add bridge=Bridge interface=ether3 pvid=10
add bridge=Bridge interface=ether4 pvid=10
/ip neighbor discovery-settings
set discover-interface-list=!dynamic
/interface bridge vlan
add bridge=Bridge comment=Management tagged=Bridge,ether1 untagged=\
    ether5,*7,geelenioMngt_2.4GHz vlan-ids=99
add bridge=Bridge comment=General tagged=ether1,Bridge untagged=\
    ether2,ether3,ether4,*C vlan-ids=10
add bridge=Bridge comment=Guest tagged=ether1 untagged=*D vlan-ids=100
add bridge=Bridge comment=IoT tagged=Bridge,ether1 untagged=geelenIoT \
    vlan-ids=80
/interface wifi configuration
add country=Germany datapath=VLAN99-Management disabled=no name=geelenioMngt \
    security=*1 security.authentication-types=wpa2-psk,wpa3-psk ssid=\
    geelenioMngt
add datapath=VLAN100-Guest disabled=no name=geelenioGuest security=*3 ssid=\
    geelenioGuest
add datapath=VLAN100-Guest disabled=no name=geelenioGuest_2.4Ghz security=*3 \
    ssid=geelenioGuest_2.4Ghz
add datapath=VLAN100-Guest disabled=no name=geelenioIoT security=*3 ssid=\
    geelenioIoT
add datapath=VLAN10-Default disabled=no name=geelenio security=*2 ssid=\
    geelenio
/ip address
add address=10.0.99.3/24 interface=VLAN99-Management network=10.0.99.0
/ip dhcp-relay
add dhcp-server=10.0.99.1 disabled=no interface=VLAN99-Management name=\
    relay_VLAN99
/system note
set show-at-login=no
```

Hi there,I have set up a network and basically use the hAPx2 to broadcast multiple Wi-Fi access points, one for each VLAN. I have a 1 GBits internet connection from the ISP.* If I plug in an Ethernet cable into the hAPx2 I get 950 Mbits or so, which is probably the max I can expect.* If I use one of the 2.4 GHz I get about 120 Mbits* If I use one of the 5 GHz I get about 300 Mbits* If I broadcast the Wi-Fi with my FritzBox, I get speeds of up to 500 Mbits. Note that this is router is installed inside a metal cabinet, so I am surprised that it even has a signal coming out of it. Yet it is still faster than the hAPx2.. I disabled the fritzbox Wi-Fi for all tests with the hAPx2I've tested for all Wi-Fi networks with 2 different computers that have Wi-Fi 6 and Wi-Fi 6e adapters. The distance of the Wi-Fi is no more than 5 meters with a clear line of sight (It's the same room, on one side is the Router, the other is the computer. There is NOTHING in between the adapters.I get about -50 (sometimes -46) dB on my antenna according to the Wi-Fi -> Registration Tab. The rate is also “explained”, as it defines the rate to be 229.4 Mbps at the time of writing.  This varies occasionally. What worries me, is that I am in a crowded Office, with many other hotspots. But I mean, 5 GHz should be able to do 2.4 GBits, which is a far cry from 300 MBits. When I scan the 5 GHz network is see these networks:Screenshot From 2024-10-22 10-49-53.pngThe 2.4 Ghz is far more crowded:Screenshot From 2024-10-22 10-52-07.pngHere is my configuration of the hAPx2What am I doing wrong here?


---
```

## Response 1
Author: [SOLVED]Tue Oct 22, 2024 12:15 pm
Never mind, I used a different laptop, and with that, I get nearly 600 Mbits. I googled, and there is an issue with my motherboard.. Sorry for wasting your time.. ---

## Response 2
Author: Tue Oct 22, 2024 12:30 pm
But I mean, 5 GHz should be able to do 2.4 GBits. ---

## Response 3
Author: Tue Oct 22, 2024 3:00 pm
But I mean, 5 GHz should be able to do 2.4 GBits.I thought that that was the theoretical limit? ---

## Response 4
Author: Tue Oct 22, 2024 3:02 pm
But I mean, 5 GHz should be able to do 2.4 GBits.Let me rephrase: expecting 800 MBits or so for a distance of 4 meters is optimistic? ---

## Response 5
Author: Tue Oct 22, 2024 3:31 pm
In an optimum situation (line of sight, no interference, no other clients) that is about the max you can expect. You can play with frequency to select the least crowded channel (i.e.5660).