# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213842

# Discussion

## Initial Question
Author: Fri Jan 10, 2025 11:11 pm
``` 
```
/interfacebridgeaddadmin-mac=78:9A:18:73:8E:51auto-mac=nocomment=defconf name=bridge/interfacelteset[finddefault-name=lte1]allow-roaming=noband=""disabled=yes \
    sms-protocol=autosms-read=no/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacewifi channeladdband=2ghz-n disabled=nofrequency=2412name=Hotelwifi/interfacewifi securityadddisabled=noname=Hotelwifi/interfacewifi configurationaddchannel=Hotelwifichannel.band=2ghz-n.frequency=2414disabled=nomode=ap \
    name=HotelWifisecurity=Hotelwifisecurity.authentication-types=wpa2-psk \
    ssid=Hotel/interfacewifiset[finddefault-name=wifi1]channel=Hotelwifichannel.frequency=2412\
    configuration=HotelWificonfiguration.mode=ap disabled=nosecurity=\Hotelwifisecurity.ft=yes.ft-over-ds=yes/ip pooladdname=default-dhcp ranges=192.168.88.10-192.168.88.254/ip dhcp-serveraddaddress-pool=default-dhcpinterface=bridge name=defconf/portset0name=serial0/queue typeaddfq-codel-ecn=nokind=fq-codel name=fq-codel-ethernet-default/queueinterfacesetether1 queue=fq-codel-ethernet-defaultsetether2 queue=fq-codel-ethernet-defaultsetether3 queue=fq-codel-ethernet-defaultsetether4 queue=fq-codel-ethernet-default/disk settingssetauto-media-interface=bridgeauto-media-sharing=yesauto-smb-sharing=yes/interfacebridge portaddbridge=bridge comment=defconfinterface=ether1addbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=lte1 list=WAN/ip addressaddaddress=192.168.88.1/24comment=defconfinterface=bridge network=\192.168.88.0/ip dhcp-client# Interface not activeaddinterface=*9/ip dhcp-server networkaddaddress=192.168.88.0/24comment=defconf dns-server=192.168.88.1gateway=\192.168.88.1/ip dnssetallow-remote-requests=yes/ip dnsstaticaddaddress=192.168.88.1comment=defconf name=router.lan type=A/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMPv6"protocol=\
    icmpv6addaction=accept chain=input comment="defconf: accept UDP traceroute"\
    dst-port=33434-33534protocol=udpaddaction=accept chain=input comment=\"defconf: accept DHCPv6-Client prefix delegation."dst-port=546protocol=\
    udp src-address=fe80::/10addaction=accept chain=input comment="defconf: accept IKE"dst-port=500,4500\
    protocol=udpaddaction=accept chain=input comment="defconf: accept ipsec AH"protocol=\
    ipsec-ahaddaction=accept chain=input comment="defconf: accept ipsec ESP"protocol=\
    ipsec-espaddaction=accept chain=input comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=input comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LANaddaction=accept chain=forward comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop packets with bad src ipv6"src-address-list=bad_ipv6addaction=drop chain=forward comment=\"defconf: drop packets with bad dst ipv6"dst-address-list=bad_ipv6addaction=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1"\
    hop-limit=equal:1protocol=icmpv6addaction=accept chain=forward comment="defconf: accept ICMPv6"protocol=\
    icmpv6addaction=accept chain=forward comment="defconf: accept HIP"protocol=139addaction=accept chain=forward comment="defconf: accept IKE"dst-port=\500,4500protocol=udpaddaction=accept chain=forward comment="defconf: accept ipsec AH"protocol=\
    ipsec-ahaddaction=accept chain=forward comment="defconf: accept ipsec ESP"protocol=\
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/system loggingaddtopics=dhcpaddtopics=wireless/system notesetshow-at-login=no
```

Hello guys, so i am trying to setup my mikrotik router a client to Hotel's Wifi so that i can use a vpn to protect my privacy. However, the interface stays at "Bound" no matter what i do, the DHCP client stays "Invalid" and there is no traffic in or out. Here is my configuration:Any help would be appreciated! thank you.


---
```

## Response 1
Author: [SOLVED]Sat Jan 11, 2025 12:03 pm
If you want to use hAP ax as client to hotel's wireless network, then wifi interface has to be running in mode=station. Also channel settings have to be on default (auto) settings.And then there are higher-level settings which are wrong/missing, e.g. DHCP client tunning on wifi1 interface (now it's bound to nonexistant interface), etc. ---

## Response 2
Author: Sat Jan 11, 2025 4:09 pm
It works!, thank you very much. it seems that i have ap mode and station mode mixed up in the tutorials i read. Regarding the rest of the configurations, i haven't set those yet i was playing around with wifi at first.