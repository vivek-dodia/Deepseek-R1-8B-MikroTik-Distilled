# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211915

# Discussion

## Initial Question
Author: Mon Nov 04, 2024 11:51 pm
``` /interface bridge add ingress-filtering=no name=bridgecap vlan-filtering=no /interface ethernet set [ find default-name=ether2 ] name=OffBridge2 /interface list add name=TRUSTED /interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik add authentication-types=wpa2-psk disable-pmkid=yes eap-methods="" \ management-protection=allowed mode=dynamic-keys name=guest_Security \ supplicant-identity="" /interface wireless set [ find default-name=wlan2 ] ampdu-priorities=0, 1, 2, 3, 4, 5 band=5ghz-a/n/ac \ channel-width=20/40mhz-Ce country=canada disabled=no frequency=5220 \ guard-interval=long mode=ap-bridge name=homeWLan5 security-profile=\ home_Security skip-dfs-channels=all ssid=5GHz-connection wireless-protocol=802.11 \ wmm-support=enabled wps-mode=disabled set [ find default-name=wlan1 ] ampdu-priorities=0, 1, 2, 3, 4, 5 band=2ghz-g/n \ basic-rates-b="" country=canada frequency=2437 guard-interval=long mode=\ ap-bridge name=homeWLan2 rate-set=configured security-profile=\ media_Security skip-dfs-channels=all ssid=2GHZ-connection supported-rates-b=\ 11Mbps wireless-protocol=802.11 wmm-support=enabled wps-mode=disabled /interface bridge port add bridge=bridgecap interface=homeWLan2 add bridge=bridgecap interface=homeWLan5 /ip neighbor discovery-settings set discover-interface-list=TRUSTED /ip settings set max-neighbor-entries=8192 /ipv6 settings set disable-ipv6=yes max-neighbor-entries=819 /interface detect-internet set detect-interface-list=NONE /interface list member add interface=bridgecap list=TRUSTED add interface=OffBridge2 list=TRUSTED /ip address add address=X.X.10.185/24 interface=bridgecap network=X.X.10.0 add address=192.168.55.1/30 interface=OffBridge2 network=192.168.55.0 /ip dns set servers=X.X.10.1 /ip route add dst-address=0.0.0.0/0 gateway=X.X.10.1 routing-table=main /tool mac-server set allowed-interface-list=none /tool mac-server mac-winbox set allowed-interface-list=TRUSTED ``` As was stated, we understand your request, the problem is you dont understand how basic networking functions..............If you want all to be on the same network........... then do the following. Otherwise, suggesting on the main router to create a separate subnet, best done through vlans.
```
Use ether2, for what I call Offbridge access, direct access without any bridge affiliation, perhaps not as critical since not doing vlans but still recommended.Just connect your laptop to ether2 and change IPV4 settings to 192.168.55.2  and you will get access.If the capac is easily accessible, then easy to attach a temp cable.IF not easily accessible at least wire a second ethenet cable to a location where you can reach  it with your laptop.....


---
```

## Response 1
Author: Wed Nov 06, 2024 5:52 pm
``` [...] /ipv6 settings set disable-ipv6=yes max-neighbor-entries=819 [...] /ip route add dst-address=0.0.0.0/0 gateway=X.X.10.1 routing-table=main ``` As was stated, we understand your request, the problem is you dont understand how basic networking functions..............If you want all to be on the same network........... then do the following. Otherwise, suggesting on the main router to create a separate subnet, best done through vlans.
```
Use ether2, for what I call Offbridge access, direct access without any bridge affiliation, perhaps not as critical since not doing vlans but still recommended.Just connect your laptop to ether2 and change IPV4 settings to 192.168.55.2  and you will get access.If the capac is easily accessible, then easy to attach a temp cable.IF not easily accessible at least wire a second ethenet cable to a location where you can reach  it with your laptop.....The fact that I do not understand networking is obvious (that is why I posted in Beginner Basics) but thanks a lot for your patience and the script.The two command I left in your quoted code above did not work.Anyway I got something to work after adding few routes and the DHCP server for the wireless clients. The Bonjour printer discovery also work which is great.It is still kind of slow and unstable so I guess I will have to dig a bit deeper but thanks for providing a very good start.


---
```

## Response 2
Author: Thu Nov 07, 2024 7:06 pm
``` /interface bridge add name=bridgecap /interface ethernet set [ find default-name=ether2 ] name=OffBridge2 /interface list add comment=lab name=TRUSTED /interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik add authentication-types=wpa2-psk disable-pmkid=yes management-protection=\ allowed mode=dynamic-keys name=lab_Security supplicant-identity="" /interface wireless set [ find default-name=wlan1 ] ampdu-priorities=0, 1, 2, 3, 4, 5 band=2ghz-g/n \ basic-rates-b="" comment=lab country=france disabled=no distance=indoors \ frequency=2437 guard-interval=long installation=indoor mode=ap-bridge \ name=labWLan2 rate-set=configured security-profile=lab_Security \ skip-dfs-channels=all ssid=pw2 supported-rates-b=11Mbps \ wireless-protocol=802.11 wmm-support=enabled wps-mode=disabled set [ find default-name=wlan2 ] ampdu-priorities=0, 1, 2, 3, 4, 5 band=5ghz-a/n/ac \ channel-width=20/40mhz-eC comment=lab country=france disabled=no \ distance=indoors frequency=5320 guard-interval=long installation=indoor \ mode=ap-bridge name=labWLan5 security-profile=lab_Security \ skip-dfs-channels=all ssid=pw wireless-protocol=802.11 wmm-support=\ enabled wps-mode=disabled /ip pool add name=default-dhcp ranges=192.168.88.10-192.168.88.254 add name=labpool ranges=X.X.10.186-X.X.10.189 /ip dhcp-server add address-pool=labpool interface=bridgecap name=lab /interface bridge port add bridge=bridgecap comment=lab interface=labWLan2 add bridge=bridgecap comment=lab interface=labWLan5 add bridge=bridgecap interface=ether1 /ip neighbor discovery-settings set discover-interface-list=TRUSTED /ipv6 settings set disable-ipv6=yes max-neighbor-entries=8192 /interface list member add comment=lab interface=ether1 list=TRUSTED add comment=lab interface=bridgecap list=TRUSTED add comment=lab interface=OffBridge2 list=TRUSTED /ip address add address=X.X.10.185/24 interface=bridgecap network=X.X.10.0 add address=192.168.55.1/30 interface=OffBridge2 network=192.168.55.0 /ip dhcp-client # DHCP client can not run on slave or passthrough interface! add comment=defconf interface=ether1 /ip dhcp-server network add address=X.X.10.0/24 comment=lab dns-server=X.X.10.1 domain=\ xxxxx gateway=X.X.10.254 /ip dns set allow-remote-requests=yes servers=X.X.10.1 /ip route add dst-address=0.0.0.0/0 gateway=X.X.10.254 routing-table=main add dst-address=0.0.0.0/0 gateway=X.X.10.254 routing-table=main /system clock set time-zone-name=Europe/Paris /system note set show-at-login=no /system routerboard mode-button set enabled=yes on-event=dark-mode /tool mac-server set allowed-interface-list=none /tool mac-server mac-winbox set allowed-interface-list=TRUSTED ``` Please post your latest complete config and I will have a look.Thanks for asking. Here it is.It works but is horribly slowNote that ether1 r(whose MAC is known to the main server) eceives a DHCP address from the main network. The DHCP server is on X.X.10.75 and does NAT as required for the lab laptops which are known and trusted on the wired network.Any advice would be more than welcome.Cheersp.
```
---
```

## Response 3
Author: Fri Nov 08, 2024 1:00 pm
``` /ip/dns/set mdns-repeat-ifaces=ether1, bridgecap ``` 1- when configured as router with the usual subnet 192.168…. we loose some access to the rest of the network and most importantly all access to Bonjour printers so that in particular people with phones or tablets can’t print. Very frustratingI can't tell from the absence of the setting whether you tried my advice up-thread to enable the mDNS repeater and had it fail, or did not try at all. It's a single-line addition to your configuration:
```
I was forced to guess on the proper interface names since your posted config is not for this #1 setup, but for #2 or #3, to use your list's numbering. Adjust to suit.Another thing not clear from your posted config is that when you have multiple DHCP servers on a single subnet, you need to arrange for them to not conflict. You can do that with a combination of firewall rules, use of RouterOS's DHCP snooping feature, and setting up non-overlapping address pools. As you have it now, your server and the other will fight.


---
```

## Response 4
Author: Fri Nov 08, 2024 2:24 pm
``` /ip/dns/set mdns-repeat-ifaces=ether1, bridgecap ``` enable the mDNS repeater and had it fail, or did not try at all. It's a single-line addition to your configuration:
```
If I understand I should try this after a Quick Setup with the usual subnet for WiFiand eth1 having its DHCP address from the main network right ? And that could solve the printers problem. I will try that
```