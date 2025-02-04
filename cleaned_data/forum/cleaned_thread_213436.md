# Thread Information
Title: Thread-213436
Section: RouterOS
Thread ID: 213436

# Discussion

## Initial Question
Hi everyone.I bought hAP ax Lite 6 for mobile router. I configure it but there is very strange problem with internet. I can ping google from router terminal but there is no internet on connected clients. I've checked firewall rules but I can't find solution. Anyone can help me??Config:
```
# 2024-12-22 12:26:49 by RouterOS 7.16.2
# software id = 1C94-WC90
#
# model = L41G-2axD&FG621-EA
# serial number = removed 
/interface bridge
add name=bridge
/interface lte
set [ find default-name=lte1 ] allow-roaming=yes band="" sms-protocol=auto \
    sms-read=no
/interface list
add name=LAN
add name=WAN
/interface lte apn
set [ find default=yes ] authentication=chap name=T-Mobile use-network-apn=no
/interface wifi channel
add band=2ghz-ax disabled=no frequency=2417 name="Kanal1 AX" width=20/40mhz
/interface wifi datapath
add bridge=bridge disabled=no name=datapath1
/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk disabled=no encryption=ccmp,gcmp \
    name=sec1
/interface wifi configuration
add channel="Kanal1 AX" country=Poland datapath=datapath1 disabled=no mode=ap \
    name=cfg1 security=sec1 ssid="ZENLan LTE AX"
/interface wifi
set [ find default-name=wifi1 ] channel.frequency=2417 configuration=cfg1 \
    configuration.mode=ap disabled=no
/ip pool
add name=pool1 ranges=192.168.10.2-192.168.10.254
/ip dhcp-server
add address-pool=pool1 interface=bridge lease-time=10m name=server1
/interface bridge port
add bridge=bridge interface=wifi1
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
add bridge=bridge interface=ether4
/ip neighbor discovery-settings
set discover-interface-list=!dynamic
/interface detect-internet
set internet-interface-list=WAN wan-interface-list=WAN
/interface list member
add interface=bridge list=LAN
add interface=lte1 list=WAN
/ip address
add address=192.168.10.1 interface=bridge network=192.168.10.0
/ip dhcp-server network
add address=192.168.10.0/24 gateway=192.168.10.1
/ip dns
set allow-remote-requests=yes servers=8.8.8.8
/ip firewall filter
add action=accept chain=input comment="Ruch poprawny" connection-state=\
    established,related,untracked
add action=accept chain=forward comment="Ruch poprawny" connection-state=\
    established,related,untracked
add action=accept chain=input comment="Ping routera z WAN" protocol=icmp
add action=accept chain=input comment=CAPSMAN dst-address=127.0.0.1
add action=fasttrack-connection chain=forward comment=FastTrack \
    connection-state=established,related hw-offload=yes
add action=drop chain=input comment="Ruch niepoprawny" connection-state=invalid
add action=drop chain=forward comment="Wszystko co niezdefiniowane" \
    connection-nat-state=!dstnat connection-state=new in-interface-list=WAN
add action=drop chain=input comment="Wszystko co nie LAN" in-interface-list=!LAN
/ip firewall nat
add action=masquerade chain=srcnat out-interface-list=WAN
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/system clock
set time-zone-name=Europe/Warsaw
/system identity
set name="ZENLan LTE"
/system note
set show-at-login=no

---
```

## Response 1
Couple of quick commentsDisable detect internet. Really.Adjust lease time of dhcp server. 10 minutes is really too short. 30m is default, I use 1hr or even 4hr.Set in APN use default route. ---

## Response 2
Thanks for suggestions. I made some changes. I cannot find in APN use default route, there is only add default route and this is checked. ---

## Response 3
Your APN settings from config don't look right.0. Although it look like APN is wrong. Wth LTE, you should make sure the /system/routerboard firmware is updated too. In winbox, you can check this in System > RouterBoard and hit "Update". Also, that the LTE modem firmware is updated, which can be check on the LTE interface in winbox.1. You need EITHER to set an APN, or check the "Use Network APN" button. If you google your carrier and country, you should be able to find the APN settings - e.g. Tmobile in US be fast.tmobile.com but not sure in Germany, etc. If you check the "Use network APN" box that essentially mean "read APN from SIM card" - some SIM/carrier support this, other do not (or APN on SIM is wrong for plan, etc., etc.). In general, it's better to leave network APN uncheck and use the carrier-provided APN information.2. You have an authentication method set ("chap") but no user or password. So you should likely set this to "none" unless you're sure of carrier's APN information suggest you need it - in which case there are typically also a user/password too. ---

## Response 4
I've checked all Your suggestions.1. Firmware is updated.2. APN settings are correct - I checked it with T-Mobile website.I can upgrade ROS, ping to google webiste from ROS terminal so internet connection should be ok. But I cannot ping google webiste from PC connected to hAP ax. DNS seems work because google.pl address is translated to IP address but ping doesn't reply any packages. ---

## Response 5
I've checked all Your suggestions.1. Firmware is updated.2. APN settings are correct - I checked it with T-Mobile website.I can upgrade ROS, ping to google webiste from ROS terminal so internet connection should be ok. But I cannot ping google webiste from PC connected to hAP ax. DNS seems work because google.pl address is translated to IP address but ping doesn't reply any packages.Did you upgrade the lte modem firmware to 16121.1034.00.01.01.08 version?The LTE is a second WAN or only main?Have you added a static route for 0.0.0.0/0 via lte1? ---

## Response 6
Yes I update LTE firmware to this version. LTE is main WAN.There is 0.0.0.0 static route rule via lte1. ---

## Response 7
Probably DHCP server is missing here for DHCP clients ?Set it the same as gateway.
```
/ip dhcp-server network
add address=192.168.10.0/24 gateway=192.168.10.1

---
```

## Response 8
What does/interface bridge port printshow? It makes me slightly nervous that you have adatapathconfigured for wifi1 and at the same wifi1 has been added as a port to the bridge manually, but it may be harmless, I just have nowhere to test right now.Other than that, I cannot spot any misconfiguration, so there may be some MTU issue or a contract/account settings issue, or something wrong at the PC side.So please run/tool sniffer quick ip-address=9.9.9.9in the command line window on the router (Winbox-Terminal or ssh) and start pinging 9.9.9.9 from the PC, limited for 2 attempts (-n 2on Windows). What does the sniffer show? ---

## Response 9
On PC, you can also run IPCONFIG / ALL (if Windoooos) so you can check if DHCP settings are correct on that end. ---

## Response 10
Probably DHCP server is missing here for DHCP clients ?Set it the same as gateway.
```
/ip dhcp-server network
add address=192.168.10.0/24 gateway=192.168.10.1IP config is OK - i think so.

---
```

## Response 11
What does/interface bridge port printshow? It makes me slightly nervous that you have adatapathconfigured for wifi1 and at the same wifi1 has been added as a port to the bridge manually, but it may be harmless, I just have nowhere to test right now.Other than that, I cannot spot any misconfiguration, so there may be some MTU issue or a contract/account settings issue, or something wrong at the PC side.So please run/tool sniffer quick ip-address=9.9.9.9in the command line window on the router (Winbox-Terminal or ssh) and start pinging 9.9.9.9 from the PC, limited for 2 attempts (-n 2on Windows). What does the sniffer show?I delete datapath option but problem still exist.This is respond from sniffer: ---

## Response 12
OK. I have missed this one. Change the own address of the router from just 192.168.10.1 to 192.168.10.1/24 and you should be OK. ---

## Response 13
You have RIGHT!!!!. Thanks for resolve this problem. I don't know how I missed it. ---

## Response 14
Radosnych Świąt. This kind of errors is very easy to make and miss, and sniffer is the best tool to find them ---

## Response 15
Thank You. Wesołych Świąt for everyone. ---