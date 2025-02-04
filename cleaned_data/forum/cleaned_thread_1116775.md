# Thread Information
Title: Thread-1116775
Section: RouterOS
Thread ID: 1116775

# Discussion

## Initial Question
I'm trying to setup a vpn connection over L2TP/IPSEC for vpn client access to my local network. (Road warrior)I can connect from my vpn client to the vpn-server running on mikrotik , but cant get access to the home network.Can someone take a look at this to help me?See my config below:
```
# RouterOS 6.42.12/interfacebridgeaddadmin-mac=B8:69:F4:8E:04:17arp=proxy-arpauto-mac=nocomment=defconf \
    name=bridge/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTikaddauthentication-types=wpa-psk,wpa2-psk eap-methods=""\
    management-protection=allowed mode=dynamic-keys name=hap_wpa \
    supplicant-identity=""wpa-pre-shared-key=wifipass \
    wpa2-pre-shared-key=wifipass/interfacewirelessset[finddefault-name=wlan1]antenna-gain=2band=2ghz-b/g/n channel-width=\20/40mhz-Cecountry=belgium disabled=nodistance=indoors frequency=auto\
    frequency-mode=regulatory-domain mode=ap-bridge security-profile=hap_wpa \
    ssid=Haptx-power=15tx-power-mode=all-rates-fixedwireless-protocol=\802.11wps-mode=disabled/ip pooladdname=dhcp ranges=10.0.0.10-10.0.0.99addname=vpn ranges=10.0.0.200-10.0.0.220/ip dhcp-serveraddaddress-pool=dhcp disabled=nointerface=bridge name=defconf/ppp profileset*FFFFFFFElocal-address=10.0.0.200remote-address=vpn/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=wlan1/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacel2tp-server serversetenabled=yes ipsec-secret=vpnsecretuse-ipsec=yes/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WAN/interfacesstp-server serversetdefault-profile=default-encryption/ip addressaddaddress=10.0.0.1/24comment=defconfinterface=ether2 network=10.0.0.0/ip cloudsetddns-enabled=yes/ip dhcp-clientadddhcp-options=hostname,clientid disabled=nointerface=ether1/ip dhcp-server networkaddaddress=10.0.0.0/24comment=defconf gateway=10.0.0.1/ip dnssetallow-remote-requests=yes/ip dnsstaticaddaddress=10.0.0.1name=router.lan/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=accept chain=input comment="allow IPsec NAT"dst-port=4500\
    protocol=udpaddaction=accept chain=input comment="allow IKE"dst-port=500protocol=udpaddaction=accept chain=input comment="allow l2tp"dst-port=1701protocol=udpaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,relatedaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf:  drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip servicesettelnet address=10.0.0.0/24disabled=yessetftp disabled=yessetwww address=10.0.0.0/24setssh address=10.0.0.0/24setapi address=10.0.0.0/24setwinbox address=10.0.0.0/24setapi-ssl address=10.0.0.0/24/ppp secretaddname=vpn password=vpnpass service=l2tp/system clocksettime-zone-name=Europe/Brussels/systempackageupdatesetchannel=long-term/tool graphing resourceaddallow-address=10.0.0.0/24/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN

---
```

## Response 1
Anyone that can take a look at my config? ---

## Response 2
Maybe you can try set ip address of your lan to bridge not to ether2 and your local address for VPN user should be ip address of the bridgehttps://wiki.mikrotik.com/wiki/Manual:Interface/L2TP ---

## Response 3
But in my config above the vpn user has same subnet as my Lan and Lan is already in the bridge
```
/interfacelist memberaddcomment=defconfinterface=bridge list=LAN

---
```

## Response 4
Every ip address should be on top interface in your case bridge that for your config. For l2tp cannot access lan ->viewtopic.php?t=92543 ---

## Response 5
I've read the links you provided but I'm still clueless.Can you help me what I need to change in my config? ---

## Response 6
Change ip address 10.0.0.1/24 to bridge interface, and for ppp user local address to 10.0.0.1. and test, for me is working that way with same config as yours ---

## Response 7
Don't change anything else ---

## Response 8
```
# Change to bridge below/ip addressaddaddress=10.0.0.1/24comment=defconfinterface=[b]bridge[/b]network=10.0.0.0# Is this ok?/ppp profileset*FFFFFFFElocal-address=10.0.0.1remote-address=vpn

---
```

## Response 9
Remote-address is the IP address for user and you already defined them with DHCP lease from 10.0.0.200 to 220 ---

## Response 10
Now is ok ---

## Response 11
Please test now ---

## Response 12
still no access , no ping reply ---

## Response 13
Post config ---

## Response 14
```
# RouterOS 6.42.12/interfacebridgeaddadmin-mac=B8:69:F4:8E:04:17arp=proxy-arpauto-mac=nocomment=defconf \
    name=bridge/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTikaddauthentication-types=wpa-psk,wpa2-psk eap-methods=""\
    management-protection=allowed mode=dynamic-keys name=hap_wpa \
    supplicant-identity=""wpa-pre-shared-key=wifipass \
    wpa2-pre-shared-key=wifipass/interfacewirelessset[finddefault-name=wlan1]antenna-gain=2band=2ghz-b/g/n channel-width=\20/40mhz-Cecountry=belgium disabled=nodistance=indoors frequency=auto\
    frequency-mode=regulatory-domain mode=ap-bridge security-profile=hap_wpa \
    ssid=Haptx-power=15tx-power-mode=all-rates-fixedwireless-protocol=\802.11wps-mode=disabled/ip pooladdname=dhcp ranges=10.0.0.10-10.0.0.99addname=vpn ranges=10.0.0.200-10.0.0.220/ip dhcp-serveraddaddress-pool=dhcp disabled=nointerface=bridge name=defconf/ppp profileset*FFFFFFFElocal-address=10.0.0.1remote-address=vpn/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=wlan1/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacel2tp-server serversetenabled=yes ipsec-secret=vpnsecretuse-ipsec=yes/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WAN/ip addressaddaddress=10.0.0.1/24comment=defconfinterface=bridge network=10.0.0.0/ip cloudsetddns-enabled=yes/ip dhcp-clientadddhcp-options=hostname,clientid disabled=nointerface=ether1/ip dhcp-server networkaddaddress=10.0.0.0/24comment=defconf gateway=10.0.0.1/ip dnssetallow-remote-requests=yes/ip dnsstaticaddaddress=10.0.0.1name=router.lan/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=accept chain=input comment="allow IPsec NAT"dst-port=4500\
    protocol=udpaddaction=accept chain=input comment="allow IKE"dst-port=500protocol=udpaddaction=accept chain=input comment="allow l2tp"dst-port=1701protocol=udpaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,relatedaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf:  drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip servicesettelnet address=10.0.0.0/24disabled=yessetftp disabled=yessetwww address=10.0.0.0/24setssh address=10.0.0.0/24setapi address=10.0.0.0/24setwinbox address=10.0.0.0/24setapi-ssl address=10.0.0.0/24/ppp secretaddname=vpn password=vpnpass service=l2tp/system clocksettime-zone-name=Europe/Brussels/systempackageupdatesetchannel=long-term/tool graphing resourceaddallow-address=10.0.0.0/24/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN

---
```

## Response 15
Everything look ok, maybe firewall ? Can you disable all drop rules and test? And if work start enable them one by one. Only that cane to my mind ---

## Response 16
Because your VPN addresses overlap with the LAN IP addressing you need to enable Proxy-ARP on the LAN bridge.Alternatively give your VPN clients a different IP range and change the PPP local address. This would be the preferred option. Proxy-ARP comes with some security issues. ---

## Response 17
- In my current config (see above) proxy-arp is enabled on the bridge but i still can't ping other devices in my lan from my vpn client- The reason i chose to get them in the same range was to avoid adding routing to be able to ping from subnet A to subnet B.- How can I change my config for that? ---

## Response 18
did you solve the problem bro? i have the same problem :( ---

## Response 19
you should add this
```
/interfacelistaddinclude=dynamicname=LANaddname=WAN

---
```

## Response 20
you should add this
```
/interfacelistaddinclude=dynamicname=LANaddname=WANnoooo .. wrong suggestion

---
```

## Response 21
Use wireguard if you have access to a public IP, or can get a port forwarded from upstream router with public IP.Oopsie, of course one would have to upgrade the router firmware out of the stone age. ---

## Response 22
Anyone that can take a look at my config?You cannot assign local network addresses to VPN clients! The local address on the interface is 10.0.0.1/24. This means that switching will work to determine the connection, not routing! Do you understand how to fix it? And secondly, there is no rule in the Firewall in chain=forward that allows traffic from VPN clients to enter the local network! ---