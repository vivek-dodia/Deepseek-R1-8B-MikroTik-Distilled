# Thread Information
Title: Thread-1119568
Section: RouterOS
Thread ID: 1119568

# Discussion

## Initial Question
Hi All, I'm a newbie who would like to enter the Mikrotik community and would appreciate some help getting there (yes, I have been through this forum and google, but still learning how to do it).I would like to setup a simple WireGuard client on my router (hAP ax2- RouterOS 7.16).How should I connect a hAP with a WireGuard to a VPN provider for all the connected devices to access the internet only through a VPN tunnel?I'm starting with a standard MT config:DHCP 192.168.88.1/24DNS 192.168.88.1WAN is on address 192.168.10.100Setup info from AirVPN
```
[Interface]Address=10.150.xx.12/32,fd7d:xxxx:xxxx:xxxx::xxxx:822/128PrivateKey=MyPrivateKeyFromAirVPNMTU=1320DNS=10.128.10.1,fd7d:xxxx:xxxx:xxxx::1[Peer]PublicKey=MyPublicKeyFromAirVPNPresharedKey=MyPresharedKeyFromAirVPNEndpoint=nl3.vpn.airdns.org:1637AllowedIPs=0.0.0.0/0,::/0PersistentKeepalive=15My setup (not a working one - no internet) following forum and google (I can ping 1.1.1.1, but can't ping DNS):
```

```
/interfacewireguardaddlisten-port=51820name=wireguard1 mtu=1320private-key="MyPrivateKeyFromAirVPN"comment="WireGuard VPN"/interfacewireguard peersaddallowed-address=0.0.0.0/0endpoint-address=nl3.vpn.airdns.org endpoint-port=1637interface=wireguard1 persistent-keepalive=15mpublic-key="MyPublicKeyFromAirVPN"preshared-key="MyPresharedKeyFromAirVPN"comment="WireGuard VPN"/ip addressaddaddress=10.150.xx.12/32interface=wireguard1 comment="WireGuard VPN"/ip routeadddst-address=0.0.0.0/0gateway=wireguard1 comment="WireGuard VPN"/ip/dhcp-server/network/setdns-server=10.128.10.10/ip firewall filteraddchain=input protocol=udp dst-port=1637action=acceptI am not realy sure where to put DNS server information.What else am I missing?In the browser I'm getting following errors:google.com’s server IP address could not be found.Try:Checking the proxy, firewall, and DNS configurationRunning Windows Network DiagnosticsDNS_PROBE_FINISHED_BAD_CONFIGorgoogle.com’s DNS address could not be found. Diagnosing the problem.Try running Windows Network Diagnostics.DNS_PROBE_STARTED

---
```

## Response 1
Complete mikrotik config please./export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc. ) ---

## Response 2
This might be missleading, but I would guess it's problem with DNS.
```
# 2024-10-05 08:26:50 by RouterOS 7.16# software id = HNDE-941S## model = C52iG-5HaxD2HaxD# serial number = xx/interfacebridgeaddadmin-mac=xx:xx:xx:xx:xx:xxauto-mac=nocomment=defconf name=bridge/interfacewifiset[finddefault-name=wifi1]channel.band=5ghz-ax.skip-dfs-channels=\10min-cac.width=20/40/80mhzconfiguration.mode=ap.ssid=MikroTik-CC494B \
    disabled=nosecurity.authentication-types=wpa2-psk,wpa3-psk.ft=yes \.ft-over-ds=yesset[finddefault-name=wifi2]channel.band=2ghz-ax.skip-dfs-channels=\10min-cac.width=20/40mhzconfiguration.mode=ap.ssid=MikroTik-CC494B \
    disabled=nosecurity.authentication-types=wpa2-psk,wpa3-psk.ft=yes \.ft-over-ds=yes/interfacewireguardaddcomment="WireGuard VPN"listen-port=51820mtu=1320name=wireguard1private-key="private-key"/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/ip pooladdname=default-dhcp ranges=192.168.88.10-192.168.88.254/ip dhcp-serveraddaddress-pool=default-dhcpinterface=bridge name=defconf/disk settingssetauto-media-interface=bridgeauto-media-sharing=yesauto-smb-sharing=yes/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=ether5addbridge=bridge comment=defconfinterface=wifi1addbridge=bridge comment=defconfinterface=wifi2/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WAN/interfacewireguard peersaddallowed-address=0.0.0.0/0comment="WireGuard VPN"endpoint-address=\
    nl3.vpn.airdns.org endpoint-port=1637interface=wireguard1 name=peer1 \
    persistent-keepalive=15mpreshared-key=\"preshared-key"public-key="public-key"/ip addressaddaddress=192.168.88.1/24comment=defconfinterface=bridge network=\192.168.88.0addaddress=10.xx.xx.12comment="WireGuard VPN"interface=wireguard1 \
    network=10.xx.xx.12/ip dhcp-clientaddcomment=defconfinterface=ether1/ip dhcp-server networkaddaddress=192.168.88.0/24comment=defconf dns-server=10.128.0.1gateway=\192.168.88.1/ip dnssetallow-remote-requests=yes/ip dnsstaticaddaddress=192.168.88.1comment=defconf name=router.lan type=A/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WANaddaction=accept chain=input dst-port=1637protocol=udp/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip routeaddcomment="WireGuard VPN"dst-address=0.0.0.0/0gateway=wireguard1/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
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
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/system clocksettime-zone-name=Europe/xx/system notesetshow-at-login=no/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN

---
```

## Response 3
```
/ip routeadddst-address=wireguardIP/32gateway=ISP gatewayand add wireguard1 to WAN interface list/ip dhcp-server networkadd address=192.168.88.0/24 comment=defconf dns-server=10.128.0.1gateway=\192.168.88.1What kind of DNS is this? Remove it.Put DNS 1.1.1.1 in /ip dns

---
```

## Response 4
Thank you for helping.I have added suggested lines (ip route, wireguard to WAN list) and changed DNS to 1.1.1.1, does this mean that VPN's DNS is not needed (10.128.0.1)?This config is now working. Is everything set correctly? How can I do additional tests? Already tested withhttps://ipleak.net/and it seems to be ok.
```
# 2024-10-05 11:00:05 by RouterOS 7.16# software id = HNDE-941S## model = C52iG-5HaxD2HaxD/interfacebridgeaddadmin-mac=xx:xx:xx:xx:xx:xxauto-mac=nocomment=defconf name=bridge/interfacewifiset[finddefault-name=wifi1]channel.band=5ghz-ax.skip-dfs-channels=\10min-cac.width=20/40/80mhzconfiguration.mode=ap.ssid=MikroTik-CC494B \
    disabled=nosecurity.authentication-types=wpa2-psk,wpa3-psk.ft=yes \.ft-over-ds=yesset[finddefault-name=wifi2]channel.band=2ghz-ax.skip-dfs-channels=\10min-cac.width=20/40mhzconfiguration.mode=ap.ssid=MikroTik-CC494B \
    disabled=nosecurity.authentication-types=wpa2-psk,wpa3-psk.ft=yes \.ft-over-ds=yes/interfacewireguardaddcomment="WireGuard VPN"listen-port=51820mtu=1320name=wireguard1/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/ip pooladdname=default-dhcp ranges=192.168.88.10-192.168.88.254/ip dhcp-serveraddaddress-pool=default-dhcpinterface=bridge name=defconf/disk settingssetauto-media-interface=bridgeauto-media-sharing=yesauto-smb-sharing=yes/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=ether5addbridge=bridge comment=defconfinterface=wifi1addbridge=bridge comment=defconfinterface=wifi2/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WANaddinterface=wireguard1 list=WAN/interfacewireguard peersaddallowed-address=0.0.0.0/0comment="WireGuard VPN"endpoint-address=\
    nl3.vpn.airdns.org endpoint-port=1637interface=wireguard1 name=peer1 \
    persistent-keepalive=15mpreshared-key=\"xx"public-key="xx="/ip addressaddaddress=192.168.88.1/24comment=defconfinterface=bridge network=\192.168.88.0addaddress=10.xx.xx.12comment="WireGuard VPN"interface=wireguard1 \
    network=10.xx.xx.12/ip dhcp-clientaddcomment=defconfinterface=ether1/ip dhcp-server networkaddaddress=192.168.88.0/24comment=defconf dns-server=1.1.1.1gateway=\192.168.88.1/ip dnssetallow-remote-requests=yes/ip dnsstaticaddaddress=192.168.88.1comment=defconf name=router.lan type=A/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WANaddaction=accept chain=input dst-port=1637protocol=udp/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip routeaddcomment="WireGuard VPN"dst-address=0.0.0.0/0gateway=wireguard1adddisabled=yes distance=1dst-address=10.xx.xx.12/32gateway=192.168.10.1\
    routing-table=main scope=30suppress-hw-offload=notarget-scope=10/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
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
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/system clocksettime-zone-name=Europe/xx/system notesetshow-at-login=no/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN

---
```

## Response 5
Yes, VPN's DNS is not needed. If everything is ok, then everything works) ---

## Response 6
Hmmm. Something is still off.https://ipleak.net/- shows ip from VPN, buthttps://whatismyipaddress.com/- is listing my real IP address.And if I connect to WiFi, clients are not routed through WireGuard.now, if I add this, will be opposite. ipleak will show my real IP, but whatismyipaddress will show VPN's IP
```
/ip routeadddisabled=nodistance=1dst-address=10.152.91.12/32gateway=192.168.10.1\
    routing-table=main scope=30suppress-hw-offload=notarget-scope=10full setup:
```

```
# 2024-10-05 11:29:09 by RouterOS 7.16# software id = HNDE-941S## model = C52iG-5HaxD2HaxD/interfacebridgeaddadmin-mac=xx:xx:xx:xx:xx:xxauto-mac=nocomment=defconf name=bridge/interfacewireguardaddcomment="WireGuard VPN"listen-port=51820mtu=1320name=wireguard1 \private-key="xx"/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacewifi channeladdband=2ghz-ax disabled=noname=channel2 width=20mhzaddband=5ghz-ax disabled=noname=channel5 width=20mhz/interfacewifi securityaddauthentication-types=wpa2-psk,wpa3-psk disabled=noname=security passphrase=xx wps=disable/interfacewifi configurationaddchannel=channel2 disabled=noname=cfg2 security=security ssid=MT_VPNaddchannel=channel5 disabled=noname=cfg5 security=security ssid=MT_VPN/interfacewifiset[finddefault-name=wifi1]configuration=cfg5 configuration.mode=ap \
    disabled=nosecurity.ft=yes.ft-over-ds=yesset[finddefault-name=wifi2]configuration=cfg2 configuration.mode=ap \
    disabled=nosecurity.ft=yes.ft-over-ds=yes/ip pooladdname=default-dhcp ranges=192.168.88.10-192.168.88.254/ip dhcp-serveraddaddress-pool=default-dhcpinterface=bridge name=defconf/disk settingssetauto-media-interface=bridgeauto-media-sharing=yesauto-smb-sharing=yes/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=ether5addbridge=bridge comment=defconfinterface=wifi1addbridge=bridge comment=defconfinterface=wifi2/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WANaddinterface=wireguard1 list=WAN/interfacewireguard peersaaddallowed-address=0.0.0.0/0comment="WireGuard VPN"endpoint-address=\
    nl3.vpn.airdns.org endpoint-port=1637interface=wireguard1 name=peer1 \
    persistent-keepalive=15mpreshared-key=\"xx"public-key=\"xx"/ip addressaddaddress=192.168.88.1/24comment=defconfinterface=bridge network=\192.168.88.0addaddress=10.xx.xx.12comment="WireGuard VPN"interface=wireguard1 \
    network=10.xx.xx.12/ip dhcp-clientaddcomment=defconfinterface=ether1/ip dhcp-server networkaddaddress=192.168.88.0/24comment=defconf dns-server=1.1.1.1gateway=\192.168.88.1/ip dnssetallow-remote-requests=yes/ip dnsstaticaddaddress=192.168.88.1comment=defconf name=router.lan type=A/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WANaddaction=accept chain=input dst-port=1637protocol=udp/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip routeaddcomment="WireGuard VPN"dst-address=0.0.0.0/0gateway=wireguard1/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
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
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/system clocksettime-zone-name=Europe/xx/system notesetshow-at-login=no/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN

---
```

## Response 7
Yes, VPN's DNS is not needed. If everything is ok, then everything works)Hi, How is it in case i'm using with this VPN - IP hole and i have 2x DNS over there?Should i use only Pihole IP and keep the "former" DNS servers or should i add also the one from AirVPN 10.128.0.1 ?Thanks ---