# Thread Information
Title: Thread-213603
Section: RouterOS
Thread ID: 213603

# Discussion

## Initial Question
Hi, my mikrotik hAP ax² is behind a fritzbox cable and works generally fine. I can download files and watch videos, with no problems, at a normal speed. But when I try to download a file from download.mikrotik.com (behind the hAP ax²) it slows down and stops the download, even if it is a tiny file. Behind the fritzbox it works fine.In the screenshot, you can see the behaviour. The download speed starts good but is quick slowing down until it goes to zero and the download fails.I think the firewall rules are fine because other files, even bigger, are working and I have more or less the default/factory firewall rules.I am on RouterOS 7.16.2Any hints to help me?ThanxLuBeDa ---

## Response 1
I think the firewall rules are fine because other files, even bigger, are working and I have more or less the default/factory firewall rules.Any hints to help me?The answer is the same as always, you can think what you like and give an opinion but we need the facts...........(evidence - aka FULL CONFIG)Thus/export file=anynameyouwish (minus router serial number, any public WANIP info, keys etc. ---

## Response 2
Here is the cleaned config:
```
# 2024-12-30 21:46:08 by RouterOS 7.16.2# model = C52iG-5HaxD2HaxD/interfacebridgeaddadmin-mac=D4:01:C3:XX:XX:XXauto-mac=nocomment=defconf name=bridge-LAN/interfacewifiset[finddefault-name=wifi1]channel.skip-dfs-channels=10min-cac \
    configuration.country=Germany.mode=ap.ssid=Luke\
    security.authentication-types=wpa2-psk,wpa3-psk.ft=yes.ft-over-ds=yesset[finddefault-name=wifi2]channel.skip-dfs-channels=10min-cac \
    configuration.country=Germany.mode=ap.ssid=Luke\
    security.authentication-types=wpa2-psk,wpa3-psk.ft=yes.ft-over-ds=yesaddconfiguration.mode=ap.ssid=Leiamac-address=D6:01:C3:XX:XX:XX \
    master-interface=wifi1 name=wifi3addconfiguration.mode=ap.ssid=Leiamac-address=D6:01:C3:XX:XX:XX \
    master-interface=wifi2 name=wifi4/interfacewireguardaddcomment=wireguard-VPN listen-port=13231mtu=1420name=wireguard1/interfacevlanaddcomment="GUest VLAN"interface=bridge-LAN name=VLAN107 vlan-id=107/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/ip pooladdname=dhcp ranges=192.168.178.17-192.168.178.254addname=dhcp_pool1 ranges=192.168.176.2-192.168.176.254/ip dhcp-serveraddaddress-pool=dhcpinterface=bridge-LAN lease-time=1dname=defconfaddaddress-pool=dhcp_pool1interface=VLAN107 lease-time=1hname=dhcp1/queue simpleaddcomment="XBOX-oben auf 20Mbit/s"max-limit=20480k/20480kname=\
    queue_xbox_ff target=192.168.178.83/32addcomment="Leo-PC auf 20Mbit/s"max-limit=20480k/20480kname=queue1 target=\192.168.178.59/32/disk settingssetauto-media-interface=bridge-LAN/interfacebridge filter# wifi3 not ready# in/out-bridge-port matcher not possible when interface (wifi3) is not slaveaddaction=drop chain=forwardin-interface=wifi3# wifi3 not ready# in/out-bridge-port matcher not possible when interface (wifi3) is not slaveaddaction=drop chain=forwardout-interface=wifi3# wifi4 not ready# in/out-bridge-port matcher not possible when interface (wifi4) is not slaveaddaction=drop chain=forwardin-interface=wifi4# wifi4 not ready# in/out-bridge-port matcher not possible when interface (wifi4) is not slaveaddaction=drop chain=forwardout-interface=wifi4/interfacebridge portaddbridge=bridge-LAN comment=defconfinterface=ether2addbridge=bridge-LAN comment=defconfinterface=ether3addbridge=bridge-LAN comment=defconfinterface=ether4addbridge=bridge-LAN comment=defconfinterface=ether5addbridge=bridge-LAN comment=defconfinterface=wifi1addbridge=bridge-LAN comment=defconfinterface=wifi2addbridge=bridge-LANinterface=wifi3addbridge=bridge-LANinterface=wifi4/ip neighbor discovery-settingssetdiscover-interface-list=all lldp-mac-phy-config=yes lldp-vlan-info=yes/interfacebridge vlanaddbridge=bridge-LAN comment="GuestVLAN auf Uplink"tagged=ether2 vlan-ids=\107/interfacelist memberaddcomment=defconfinterface=bridge-LAN list=LANaddcomment=defconfinterface=ether1 list=WAN/interfacewireguard peersaddallowed-address=192.168.177.2/32client-address=192.168.177.2/32\
    client-dns=192.168.178.1client-endpoint=sell-e.de client-listen-port=\13231comment=Dienstdings13interface=wireguard1 name=Dienstdings13\private-key="XX"public-key=\"XX"/ip addressaddaddress=192.168.178.1/24comment=defconfinterface=bridge-LAN network=\192.168.178.0addaddress=192.168.177.1/24comment=Wireguardinterface=wireguard1 network=\192.168.177.0addaddress=192.168.176.1/24comment=Guest_VLANinterface=VLAN107 network=\192.168.176.0/ip dhcp-clientaddcomment=defconfinterface=ether1/ip dhcp-server leaseaddaddress=192.168.178.47client-id=homeassistant comment=\"Reservation Homeassistant"server=defconf/ip dhcp-server networkaddaddress=192.168.176.0/24gateway=192.168.176.1addaddress=192.168.178.0/24comment=defconf dns-server=192.168.178.1\
    gateway=192.168.178.1netmask=24/ip dnssetallow-remote-requests=yes cache-size=30720KiBservers=\8.8.8.8,1.1.1.1,9.9.9.9/ip dns adlistaddssl-verify=nourl=\
    https://raw.githubusercontent.com/StevenBlack/hosts/master/hostsaddssl-verify=nourl="https://raw.githubusercontent.com/StevenBlack/hosts/mas\
    ter/alternates/porn-only/hosts"/ip dnsstaticaddaddress=192.168.178.196comment=Wildcardmatch-subdomain=yes name=\
    home.xxxx.xx type=A/ip firewall address-listaddaddress=192.168.178.1-192.168.178.14comment=\"Switche Router und NAS-Hardware"list=IPs_Infrastrukturaddaddress=192.168.178.33-192.168.178.126comment="Alle IoTs"list=IPs_IoTaddaddress=192.168.177.2comment="Wireguard Dienstding13"list=Trusted-VPNaddaddress=192.168.177.0/24comment="Wireguard alle"list=All-VPN/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=accept chain=input comment="Wireguard  UDP accept"dst-port=13231\
    protocol=udpaddaction=accept chain=input comment="Wireguard VPN traffic"src-address=\192.168.177.0/24addaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment=\"defconf: accept ICMP from LAN (bridge)"in-interface=bridge-LAN \
    protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=accept chain=input comment="LAN => FW |  erlauben"in-interface=\
    bridge-LANaddaction=drop chain=input comment="drop ping over WAN"in-interface=ether1 \
    protocol=icmpaddaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=noaddaction=accept chain=forward comment="LAN-> WAN | alles erlauben"\in-interface=bridge-LANout-interface=ether1addaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WANaddaction=dst-nat chain=dstnat comment="Forwarding http to nginx"disabled=\
    yes dst-port=80in-interface=ether1 protocol=tcp to-addresses=\192.168.178.2to-ports=80addaction=dst-nat chain=dstnat comment="Forwarding https  to nginx"\
    dst-port=443in-interface=ether1 protocol=tcp to-addresses=192.168.178.2\
    to-ports=443/ip servicesettelnet disabled=yessetftp disabled=yessetwww disabled=yessetwww-ssl certificate="Self signed for API"disabled=nosetapi-ssl certificate="Self signed for API"/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
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
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/snmpsetcontact=LuBeDaenabled=yes location=Office/system clocksettime-zone-autodetect=notime-zone-name=Europe/Berlin/system identitysetname=MIC_RT_GF/system notesetshow-at-login=no/system ntp clientsetenabled=yes/system ntp serversetenabled=yes/system ntp client serversaddaddress=192.168.180.1/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN

---
```

## Response 3
In a trace i found a lot of retransmits and duplicated ack. So its clear that there is a problem, but i can't find the reason why. ---

## Response 4
I cannot spot anything wrong, even anything too unusual (the order of firewall rules in ipv4 firewall filter is not optimal but neither is it wrong) in the configuration; the sniffing is a good idea but you should do it on the Mikrotik itself without filtering by interface, only by the remote address. The goal is to see whether there is some issue on the Mikrotik itself and the packet doesn't make it from WAN to LAN or whether interworking between Mikrotik and Friztbox is not OK. Could it be that you have set the MTU of Fritzbox LAN to be higher than the one of Mikrotik's WAN (which is the default 1500)?When sniffing without filtering on interface, the TCP dissector of Wireshark gets confused so don't jump to conclusions, just check whether there are packets whose dst-mac-address is the one of ether1 that have no "twins" whose src-mac-address is the one of bridge-LAN. Of course, if the Fritzbox supports sniffing, it would be ideal to have sniffs from the same attempt from both devices. ---

## Response 5
Maybe it's coincidence maybe not but in the morning I had troubles connecting to Mikrotik forum. Ngnix errors so your problems could had been a sign of trouble. Even now post "submit" is a liitle slow paced.EDIT: I see even HTTP 500 now. ---

## Response 6
I cannot spot anything wrong, even anything too unusualI will investigate further, although I found a solution (hopefully it will stay working). I changed the uplink port on the fritz box to LAN3 and all worked fine, changing back to LAN4 the error was there again. Setting LAN4 on the fritz box to Guest-Mode and it worked.I am not sure what is going on, I will take a look next yearThanx for the support. ---