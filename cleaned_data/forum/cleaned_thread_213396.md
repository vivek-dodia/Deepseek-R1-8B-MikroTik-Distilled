# Thread Information
Title: Thread-213396
Section: RouterOS
Thread ID: 213396

# Discussion

## Initial Question
Hi there, I'm at the end of my wits...I need to set up VPN tunnel between two Mikrotiks, where one of them is behind FIOS router (see the pic)topo.jpgHere is MikrotikB config
```
# 2024-12-19 19:32:56 by RouterOS 7.15.2# software id = 7B8N-YHZ8## model = RB5009UG+S+/interfacebridgeaddadmin-mac=F4:1E:57:3D:7C:A0auto-mac=nocomment=defconf name=bridgeaddname=bridge2/interfacewireguardaddcomment=DDC_tunel listen-port=13231mtu=1420name=wireguard1/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LANaddname=LAN2/ip pooladdname=default-dhcp ranges=192.168.88.10-192.168.88.254addname=dhcp10/24ranges=192.168.10.10-192.168.10.254addname=dhcp2/24ranges=192.168.2.10-192.168.2.254/ip dhcp-serveraddaddress-pool=dhcp10/24interface=bridge name=defconfaddaddress-pool=dhcp2/24interface=bridge2 name=dhcp2/disk settingssetauto-media-interface=bridgeauto-media-sharing=yesauto-smb-sharing=yes/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=ether5addbridge=bridge comment=defconfinterface=ether6addbridge=bridge comment=defconfinterface=ether7addbridge=bridge2interface=ether8/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WANaddinterface=bridge2 list=LAN2addinterface=wireguard1 list=LAN/interfacewireguard peersaddallowed-address=10.10.10.0/24,10.2.2.1/32endpoint-address=XX.XX.XX.XX \
    endpoint-port=56000interface=wireguard1 name=DDC_tunnel \
    persistent-keepalive=25spublic-key=\"Gm4LSnGXWFjGWrLiEF/D+RxH3+soEO7H1OIcY9ThXU8="/ip addressaddaddress=192.168.10.1/24comment=defconfinterface=bridge network=\192.168.10.0addaddress=192.168.2.1/24interface=bridge2 network=192.168.2.0addaddress=10.2.2.14interface=wireguard1 network=10.2.2.0/ip dhcp-clientaddcomment=defconfinterface=ether1/ip dhcp-server networkaddaddress=192.168.2.0/24dns-server=1.1.1.1gateway=192.168.2.1addaddress=192.168.10.0/24dns-server=1.1.1.1gateway=192.168.10.1addaddress=192.168.88.0/24comment=defconf dns-server=192.168.88.1gateway=\192.168.88.1/ip dnssetallow-remote-requests=yes/ip dnsstaticaddaddress=192.168.10.1comment=defconf name=router.lan/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="Allow wireguard traffic"\
    dst-address-list=13231protocol=udpaddaction=accept chain=forward comment="DDC_tunnel allow"dst-address=\10.10.10.0/24in-interface=wireguard1addaction=accept chain=forward comment="DDC tunnel"out-interface=wireguard1 \
    src-address=10.10.10.0/24addaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip routeadddisabled=nodistance=1dst-address=10.10.10.0/24gateway=wireguard1 \
    routing-table=main suppress-hw-offload=no/ip servicesettelnet disabled=yessetftp disabled=yessetwww address=192.168.10.0/24setssh address=192.168.10.0/24setapi disabled=yessetwinbox address=192.168.10.0/24setapi-ssl disabled=yes/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
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
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/system notesetshow-at-login=no/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LANMikrotik A config
```

```
# 2024-12-19 19:41:35 by RouterOS 7.16.2# software id = HFQU-A853## model = CRS520-4XS-16XQ/interfacebridgeaddarp=proxy-arp name=bridge-lan-10addname=bridge1/interfaceethernetset[finddefault-name=ether1]advertise="10M-baseT-half,10M-baseT-full,100M\
    -baseT-half,100M-baseT-full,1G-baseT-full,2.5G-baseT"set[finddefault-name=ether2]advertise=\10M-baseT-full,100M-baseT-full,1G-baseT-full,2.5G-baseT rx-flow-control=\autotx-flow-control=autoset[finddefault-name=qsfp28-1-1]arp=proxy-arp fec-mode=fec91set[finddefault-name=qsfp28-3-1]fec-mode=fec91set[finddefault-name=sfp28-3]name="sfp28-3 NAS"set[finddefault-name=sfp28-4]name=sfp28-4NAS/interfacewireguardaddlisten-port=56000mtu=1420name=wireguard1/interfacebondingaddmode=802.3adname=NAS-bonding slaves="sfp28-3 NAS,sfp28-4NAS"/interfacelistaddname=LAN/ip pooladdname=dhcp_pool0 ranges=192.168.88.2-192.168.88.254addname=pool-lan-10ranges=10.10.10.5-10.10.10.254addname=pool-vpn ranges=10.1.1.2-10.1.1.50/ip dhcp-serveraddaddress-pool=dhcp_pool0interface=bridge1 name=dhcp1addadd-arp=yes address-pool=pool-lan-10bootp-support=noneinterface=\
    bridge-lan-10name=dhcp-lan-10/portset0name=serial0/ppp profileset*0local-address=10.1.1.1remote-address=pool-vpn/interfacebridge portaddbridge=bridge1interface=ether2addbridge=bridge-lan-10interface=qsfp28-1-1addbridge=bridge-lan-10interface=qsfp28-1-2addbridge=bridge-lan-10interface=qsfp28-1-3addbridge=bridge-lan-10interface=qsfp28-1-4addbridge=bridge-lan-10interface=ether1addbridge=bridge-lan-10interface=NAS-bondingaddbridge=bridge-lan-10comment="DP Desktop"interface=sfp28-2/ip neighbor discovery-settingssetlldp-med-net-policy-vlan=1/interfacelist memberaddinterface=bridge-lan-10list=LANaddinterface=wireguard1 list=LAN/interfacewireguard peersaddallowed-address=10.2.2.2/32interface=wireguard1 name=andreypublic-key=\"PcEfySo+eCNdlqYkhXl6pOzDeCo62ZjzniYKW6G6D0g="addallowed-address=10.2.2.14/24interface=wireguard1 name=andrey_tunnel \public-key="jG78OmgReQNVgZMGGPT1NK6+AMQpBCxa4MiybbNXvSc="/ip addressaddaddress=192.168.88.1/24interface=bridge1 network=192.168.88.0addaddress=10.10.10.1/24interface=bridge-lan-10network=10.10.10.0addaddress=10.2.2.1/24interface=wireguard1 network=10.2.2.0addaddress=10.10.10.241interface=NAS-bonding network=10.10.10.0/ip dhcp-clientaddinterface=sfp28-1/ip dhcp-server networkaddaddress=10.10.10.0/24dns-server=10.10.10.1domain=ddc.lan gateway=\10.10.10.1addaddress=192.168.88.0/24gateway=192.168.88.1/ip dnssetallow-remote-requests=yes servers=9.9.9.9,149.112.112.112/ip firewall filteraddchain=input port=1701,500,4500protocol=udpaddchain=input protocol=ipsec-espaddaction=accept chain=forward comment="Allow home network to DC network"\
    dst-address=10.10.10.0/24src-address=192.168.1.0/24addaction=accept chain=forward comment="Allowed communication for established\
    \_connections between DC and local networks"connection-state=\
    established,related dst-address=192.168.1.0/24src-address=10.10.10.0/24addaction=drop chain=forward comment=\"Don't allow new connections from DC to local network"connection-state=\
    invalid,newdst-address=192.168.1.0/24src-address=10.10.10.0/24addaction=accept chain=input comment="Allow Wireguard"disabled=yes \
    dst-port=56000protocol=udp/ip firewall nataddaction=masquerade chain=srcnatout-interface=sfp28-1/ip servicesettelnet disabled=yessetftp disabled=yessetssh address=10.1.1.0/24,192.168.1.0/24,10.2.2.0/24setapi disabled=yessetapi-ssl disabled=yes/system notesetshow-at-login=no/system routerboard settingssetenter-setup-on=delete-key etherboot-port=ether1FIOS router has a port forwarding to allow Wireguard traffic through, to the Mikrotik A.Interestingly, I can ping LAN 10.10.10.0/24 from Mikrotik A tools, but not from LAN 192.168.10.0/24.There is an attempt to hide LAN 192.168.1.0/24 from both 10.10.10.0/24 and 192.168.10.0/24, but I must be able to reach 10.10.10.0/24 from any other LANs.Also, a road warrior setup works just fine on Mikrotik A.Please help!Thank you!

---
```

## Response 1
ROUTERB1. Main problem is two bridges, dont need one and shouldnt have one, simply assign the second subnet to ether8.2. Why is .88 subnet hanging around??? You should get rid of all old stuff which becomes noise on the config. PLUS you are using .88 on Router A, so B should not have that at all.3. Wireguard allowed IPs for actual wireguard address should be subnet .0/24thus allowing any remote warriors to connect to A, and then connect to B. This is so the admin can remotely reach both routers for config purposes!!4. Ensure wireguard address is full subnet .14/245. forward chain rule for wireguard using a port is removed, it makes no sense.Instead I made a firewall address list you can use concept on both devices.ONLY the admin needs access to the routers for config purposes.6. Unless you have a good reason www under services should be disabled as its not a secure access method to router.7. Set IPV6 to disabled and remove all firewall rules and address lists.
```
# model = RB5009UG+S+/interfacebridgeaddadmin-mac=F4:1E:57:3D:7C:A0auto-mac=nocomment=defconf name=bridge/interfacewireguardaddcomment=DDC_tunel listen-port=13231mtu=1420name=wireguard1/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LANaddname=LAN2/ip pooladdname=dhcp10/24ranges=192.168.10.10-192.168.10.254addname=dhcp2/24ranges=192.168.2.10-192.168.2.254/ip dhcp-serveraddaddress-pool=dhcp10/24interface=bridge name=defconfaddaddress-pool=dhcp2/24interface=ether8 name=dhcp2/disk settingssetauto-media-interface=bridgeauto-media-sharing=yesauto-smb-sharing=yes/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=ether5addbridge=bridge comment=defconfinterface=ether6addbridge=bridge comment=defconfinterface=ether7/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=ether1 list=WANaddcomment=defconfinterface=bridge list=LANaddinterface=wireguard1 list=LANaddinterface=ether8  list=LAN2/interfacewireguard peersaddallowed-address=10.2.2.0/24,10.10.10.0/24,192.168.88.0/24endpoint-address=XX.XX.XX.XX \
    endpoint-port=56000interface=wireguard1 name=DDC_tunnel \
    persistent-keepalive=25spublic-key=\"Gm4LSnGXWFjGWrLiEF/D+RxH3+soEO7H1OIcY9ThXU8="/ip addressaddaddress=192.168.10.1/24comment=defconfinterface=bridge network=\192.168.10.0addaddress=192.168.2.1/24interface=ether8 network=192.168.2.0addaddress=10.2.2.14/24interface=wireguard1 network=10.2.2.0/ip dhcp-clientaddcomment=defconfinterface=ether1/ip dhcp-server networkaddaddress=192.168.2.0/24dns-server=1.1.1.1gateway=192.168.2.1addaddress=192.168.10.0/24dns-server=1.1.1.1gateway=192.168.10.1/ip dnssetallow-remote-requests=yes/ip dnsstaticaddaddress=192.168.10.1comment=defconf name=router.lan[i]/ip firewall address-list{usestaticdhcp leaseswhereapplicable}addaddress=192.168.10.XX/32list=AUTHORIZED comment="local admin pc"addaddress=192.168.10.YY/32list=AUTHORIZED comment="local admin smartphone/ipad/laptop"addaddress=10.2.2.2/32list=AUTHORIZED comment="remote admin laptop"addaddress=10.10.10.AB/32list=AUTHORIZED comment=" remote admin PC behind RouterA"addaddress=10.10.10.DE/32list=AUTHORIZED comment=" remote admin smartphone/ipad/laptop behind RouterA"[/i]addaddress=192.168.10.0/24list=SUBNETS comment="local subnet RouterB - bridge"addaddress=192.168.2.0/24list=SUBNETS comment="local subnet RouterB - ether2"addaddress10.10.10.0/24list=SUBNETS comment="remote subnet RouterA - bridge"addaddress=192.168.88.0/24list=SUBNETS comment="remote subnet RouterA - ether2"/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=accept chain=input comment="admin access"src-address-list=AUTHORIZEDaddaction=accept chain=input comment="users to services"in-interface-list=LAN dst-port=53protocol=udpaddaction=accept chain=input comment="users to services"in-interface-list=LAN dst-port=53protocol=tcpaddaction=drop chain=input comment="drop all else"++++++++++++++++++++++++++++++++++++++++++addaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=accept chain=forward comment="internet traffic"in-interface-list=LANout-interface-list=WANaddaction=accept chain=forward comment="admin to subnets"src-address-list=AUTHORIZED dst-address-list=SUBNETSaddaction=accept chain=forward comment="RouterA users to RouterB"in-interface=wireguard1 dst-address=192.168.10.10.0/24addaction=accept chain=forward comment="port forwarding"connection-nat-state=dstnataddaction=drop chain=forward comment="drop all else"/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip routeadddistance=1dst-address=10.10.10.0/24gateway=wireguard1 routing-table=mainadddistance=1dst-address=192.168.88.0/24gateway=wireguard1 routing-table=main/ip servicesettelnet disabled=yessetftp disabled=yessetwww address=192.168.10.0/24DISABLED=YESsetssh address=192.168.10.0/24setapi disabled=yessetwinbox address=192.168.10.0/24,10.10.10.0/24,10.2.2.2.0/24setapi-ssl disabled=yes/system notesetshow-at-login=no/tool mac-serversetallowed-interface-list=none/tool mac-server mac-winboxsetallowed-interface-list=LAN

---
```

## Response 2
ROUTERA1. Most points in Router B also applicable to Router A, changes made.Only rule to add is relay rule for wireguard so you can come in remotely on 10.2.2.2 and then reach routerB.2. Still need WAN list entry3. stick to standard neighours discovery for the most part........4. allowed ip for other router on wireguard settings is .14/325. Missing allowed IP for remote subnet wishing to access for local users on routerA to RouterBROUTERA
```
# model = CRS520-4XS-16XQ/interfacebridgeaddarp=proxy-arp name=bridge-lan-10/interfaceethernetset[finddefault-name=ether1]advertise="10M-baseT-half,10M-baseT-full,100M\
    -baseT-half,100M-baseT-full,1G-baseT-full,2.5G-baseT"set[finddefault-name=ether2]advertise=\10M-baseT-full,100M-baseT-full,1G-baseT-full,2.5G-baseT rx-flow-control=\autotx-flow-control=autoset[finddefault-name=qsfp28-1-1]arp=proxy-arp fec-mode=fec91set[finddefault-name=qsfp28-3-1]fec-mode=fec91set[finddefault-name=sfp28-3]name="sfp28-3 NAS"set[finddefault-name=sfp28-4]name=sfp28-4NAS/interfacewireguardaddlisten-port=56000mtu=1420name=wireguard1/interfacebondingaddmode=802.3adname=NAS-bonding slaves="sfp28-3 NAS,sfp28-4NAS"/interfacelistaddname=WANaddname=LANaddname=LAN2/ip pooladdname=dhcp_pool0 ranges=192.168.88.2-192.168.88.254addname=pool-lan-10ranges=10.10.10.5-10.10.10.254addname=pool-vpn ranges=10.1.1.2-10.1.1.50/ip dhcp-serveraddaddress-pool=dhcp_pool0 interfac=ether2 name=dhcp1addadd-arp=yes address-pool=pool-lan-10bootp-support=noneinterface=\
    bridge-lan-10name=dhcp-lan-10/portset0name=serial0/ppp profileset*0local-address=10.1.1.1remote-address=pool-vpn/interfacebridge portaddbridge=bridge-lan-10interface=qsfp28-1-1addbridge=bridge-lan-10interface=qsfp28-1-2addbridge=bridge-lan-10interface=qsfp28-1-3addbridge=bridge-lan-10interface=qsfp28-1-4addbridge=bridge-lan-10interface=ether1addbridge=bridge-lan-10interface=NAS-bondingaddbridge=bridge-lan-10comment="DP Desktop"interface=sfp28-2/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddinterface=bridge-lan-10list=LANaddinterface=wireguard1 list=LANaddether2 list=LAN2addsfp28-1list=WAN/interfacewireguard peersaddallowed-address=10.2.2.2/32interface=wireguard1 name=andreypublic-key=\"PcEfySo+eCNdlqYkhXl6pOzDeCo62ZjzniYKW6G6D0g="addallowed-address=10.2.2.14/32,192.168.10.0/24,192.168.2.0/24interface=wireguard1 name=andrey_tunnel \public-key="jG78OmgReQNVgZMGGPT1NK6+AMQpBCxa4MiybbNXvSc="/ip addressaddaddress=192.168.88.1/24interface=ether2 network=192.168.88.0addaddress=10.10.10.1/24interface=bridge-lan-10network=10.10.10.0addaddress=10.2.2.1/24interface=wireguard1 network=10.2.2.0addaddress=10.10.10.241interface=NAS-bonding network=10.10.10.0/ip dhcp-clientaddinterface=sfp28-1/ip dhcp-server networkaddaddress=10.10.10.0/24dns-server=10.10.10.1domain=ddc.lan gateway=\10.10.10.1addaddress=192.168.88.0/24gateway=192.168.88.1/ip dnssetallow-remote-requests=yes servers=9.9.9.9,149.112.112.112/ip firewall address-list{usestaticdhcp leaseswhereapplicable}addaddress=192.168.10.XX/32list=AUTHORIZED comment="remote admin pc behind RouterB"addaddress=192.168.10.YY/32list=AUTHORIZED comment="remote admin smartphone/ipad/laptop behind RouterB"addaddress=10.2.2.2/32list=AUTHORIZED comment="remote admin laptop"addaddress=10.10.10.AB/32list=AUTHORIZED comment="local admin PC "addaddress=10.10.10.DE/32list=AUTHORIZED comment="local admin smartphone/ipad/laptop"[/i]addaddress=192.168.10.0/24list=SUBNETS comment="remote subnet RouterB - bridge"addaddress=192.168.2.0/24list=SUBNETS comment="remote subnet RouterB - ether2"addaddress10.10.10.0/24list=SUBNETS comment="local subnet RouterA - bridge"addaddress=192.168.88.0/24list=SUBNETS comment="local subnet RouterA - ether2"/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=accept chain=input comment="wireguard handshake"dst-port=56000protocol=udpaddchain=input port=1701,500,4500protocol=udpaddchain=input protocol=ipsec-espaddaction=accept chain=input comment="admin access"src-address-list=AUTHORIZEDaddaction=accept chain=input comment="users to services"in-interface-list=LAN dst-port=53protocol=udpaddaction=accept chain=input comment="users to services"in-interface-list=LAN dst-port=53protocol=tcpaddaction=drop chain=input comment="drop all else"++++++++++++++++++++++++++++++++++++++++++addaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=accept chain=forward comment="internet traffic"in-interface-list=LANout-interface-list=WANaddaction=accept chain=forward comment="relay wireguard"in-interface=wireguard1out-interface=wireguard1addaction=accept chain=forward comment="admin to subnets"src-address-list=AUTHORIZED dst-address-list=SUBNETSaddaction=accept chain=forward comment="RouterA users to RouterB"out-interface=wireguard1 dst-address=192.168.10.0/24addaction=accept chain=forward comment="RouterB users to RouterA  in-interface=wireguard1 dst-address=10.10.10.0/24
add action=accept chain=forward comment="port forwarding" connection-nat-state=dstnat 
add action=drop chain=forward comment="drop allelse"
/ip firewall nat
add action=masquerade chain=srcnat out-interface-list=WAN
/ip route
add dst-address=192.168.10.0/24  gateway=wireguard1 table=main
add dst-address=192.168.2.0/24  gateway=wireguard1 table=main
/ip service
set telnet disabled=yes
set ftp disabled=yes
set ssh address=10.1.1.0/24,192.168.1.0/24,10.2.2.0/24
set api disabled=yes
set api-ssl disabled=yes
/system note
set show-at-login=no
/system routerboard settings
set enter-setup-on=delete-key etherboot-port=ether1

---
```

## Response 3
What was not clear to me was the purpose of the subnet on ether2 of both routers????/ ---

## Response 4
Anav, I appreciate the time you've spent answering my question.I added all the changes you've highlighted in your answers, yet I'm still where I was yesterday...A few questions:1. RouterA is behind a FIOS router and has only firewall rules that denies any connections from 10.10.10.0/24 to 192.168.1.0/24
```
[admin@MikroTik]/ip/firewall/filter>printFlags:X-disabled,I-invalid;D-dynamic0chain=input protocol=udp port=1701,500,45001chain=input protocol=ipsec-esp2;;;Allowhome network to DC network
      chain=forward action=accept src-address=192.168.1.0/24dst-address=10.10.10.0/243;;;Allowedcommunicationforestablished connections between DCandlocalnetworks
      chain=forward action=accept connection-state=established,related src-address=10.10.10.0/24dst-address=192.168.1.0/244;;;Don''t allownewconnectionsfromDC tolocalnetwork
      chain=forward action=drop connection-state=invalid,newsrc-address=10.10.10.0/24dst-address=192.168.1.0/245X;;;AllowWireguardchain=input action=accept protocol=udp dst-port=56000Do I really need to allow traffic from WG to 10.10.10.0/24 LAN?2. When I ping LAN 10.10.10.0/24 from router B, I can see itping.jpgI can't reach those machines from behind router B, LAN 192.168.10.0/24. So, I suspect the issue is in either routing or firewall or both on the Router B.
```

```
[admin@MikroTik]/ip/firewall/filter>printFlags:X-disabled,I-invalid;D-dynamic0D;;;special dummy rule to show fasttrack counters
      chain=forward action=passthrough1;;;defconf:accept established,related,untracked
      chain=input action=accept connection-state=established,related,untracked2;;;defconf:drop invalid
      chain=input action=drop connection-state=invalid3;;;defconf:accept ICMP
      chain=input action=accept protocol=icmp4;;;defconf:accept tolocalloopback(forCAPsMAN)chain=input action=accept dst-address=127.0.0.15;;;defconf:drop allnotcomingfromLAN
      chain=input action=dropin-interface-list=!LAN6;;;defconf:acceptinipsec policy
      chain=forward action=accept ipsec-policy=in,ipsec7X;;;Allowwireguard traffic
      chain=forward action=accept protocol=udp dst-address-list=13231log=nolog-prefix=""8;;;DDC_tunnel allow
      chain=forward action=accept dst-address=10.10.10.0/24in-interface=wireguard1 log=nolog-prefix=""9;;;DDC tunnel
      chain=forward action=accept src-address=10.10.10.0/24out-interface=wireguard1 log=nolog-prefix=""10;;;defconf:acceptoutipsec policy
      chain=forward action=accept ipsec-policy=out,ipsec11;;;defconf:fasttrack
      chain=forward action=fasttrack-connection hw-offload=yes connection-state=established,related12;;;defconf:accept established,related,untracked
      chain=forward action=accept connection-state=established,related,untracked13;;;defconf:drop invalid
      chain=forward action=drop connection-state=invalid14;;;defconf:drop allfromWANnotDSTNATedchain=forward action=drop connection-state=newconnection-nat-state=!dstnatin-interface-list=WANI found in some manual rules 8, 9 and not sure if they are right...Also, here are my routes:
```

```
[admin@MikroTik]/ip/route>printFlags:D-DYNAMIC;A-ACTIVE;c-CONNECT,s-STATIC,d-DHCPColumns:DST-ADDRESS,GATEWAY,DISTANCE#     DST-ADDRESS      GATEWAY       DISTANCEDAd0.0.0.0/0XX.XX.XX.XX1DAc10.2.2.0/24wireguard100As10.10.10.0/24wireguard11DAc68.118.192.0/21ether10DAc192.168.2.0/24ether80DAc192.168.10.0/24bridge0Hope this clarifies the issue a bit better.Thanks again!

---
```

## Response 5
Okay, the issue is solved, I missed on the Router A to add in allowed addresses the address of the LAN
```
addallowed-address=10.2.2.14/32,***192.168.10.0/24,192.168.2.0/24***interface=wireguard1 name=andrey_tunnel \public-key="jG78OmgReQNVgZMGGPT1NK6+AMQpBCxa4MiybbNXvSc="Thanks!

---
```