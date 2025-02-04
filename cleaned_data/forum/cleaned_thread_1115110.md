# Thread Information
Title: Thread-1115110
Section: RouterOS
Thread ID: 1115110

# Discussion

## Initial Question
Hi, i setup a OpenVPN Server on a RB to connect some IoT devices with our network. The IP adresses for the IoT devices should provided via a DHCP-Server. But if i try to setup the DHCP Server i get everytime the messages DHCP invalid. Could somebody take a look to the config and could give a hint.Thanks + Regards
```
# 2024-12-12 14:28:39 by RouterOS 7.15.3# software id = W0EM-SE0S## model = RB750Gr3/interfacebridgeaddadmin-mac=D4:01:C3:87:6E:9Aarp=proxy-arpauto-mac=nocomment=defconf \
    ingress-filtering=noname=bridge port-cost-mode=shortvlan-filtering=yes/interfaceovpn-serveraddname=ovpn-in1 user=""/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacelte apnset[finddefault=yes]ip-type=ipv4use-network-apn=no/ip pooladdname=default-dhcp ranges=192.168.88.10-192.168.88.254addname=dhcp-vpn ranges=172.20.1.10-172.20.1.100/ppp profileaddbridge=bridgelocal-address=0.0.0.0name=vpn-srv01use-encryption=yes \use-ipv6=no/snmp communityset[finddefault=yes]addresses=0.0.0.0/0addaddresses=0.0.0.0/0name=lesen/interfacebridge portaddbridge=bridge comment=defconf ingress-filtering=nointerface=ether2 \internal-path-cost=10path-cost=10addbridge=bridge comment=defconf ingress-filtering=nointerface=ether3 \internal-path-cost=10path-cost=10addbridge=bridge comment=defconf ingress-filtering=nointerface=ether4 \internal-path-cost=10path-cost=10addbridge=bridge comment=defconf ingress-filtering=nointerface=ether5 \internal-path-cost=10path-cost=10addbridge=bridgeinterface=ovpn-in1/ip firewall connection trackingsetudp-timeout=10s/ip neighbor discovery-settingssetdiscover-interface-list=LAN/ipv6 settingssetdisable-ipv6=yes max-neighbor-entries=8192/interfacebridge vlanaddbridge=bridge untagged=ether5,bridge vlan-ids=1600/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WAN/interfaceovpn-server serversetauth=sha1,md5 certificate=sww_server-cert cipher=aes128-cbc,aes192-cbc \
    enabled=yesrequire-client-certificate=yes/ip addressaddaddress=192.168.88.1/24comment=defconfinterface=bridge network=\192.168.88.0addaddress=10.241.31.4/29comment="xxx"interface=ether5 network=\10.241.31.0addaddress=172.31.1.11/29comment="yyy"interface=ether1 \
    network=172.31.1.8addaddress=172.27.1.1/24disabled=yesinterface=ovpn-in1 network=172.27.1.0/ip cloudsetddns-enabled=yes ddns-update-interval=1h/ip dhcp-clientaddcomment=defconf disabled=yesinterface=ether1/ip dhcp-serveraddaddress-pool=dhcp-vpninterface=ovpn-in1 lease-time=12hname=dhcp-vpn/ip dhcp-server networkaddaddress=172.20.1.0/24gateway=172.20.1.1netmask=24addaddress=192.168.88.0/24comment=defconf dns-server=192.168.88.1gateway=\192.168.88.1netmask=24addaddress=192.168.200.0/32dns-none=yes gateway=192.168.200.1netmask=25/ip dnssetallow-remote-requests=yes servers=1.1.1.1,8.8.8.8,172.31.1.9/ip dnsstaticaddaddress=1.1.1.1name=Cloudflare/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=accept chain=input comment="accept input OpenVPN"dst-port=1194\in-interface-list=WAN log=yes log-prefix=ovpn protocol=tcpaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip hotspot profileset[finddefault=yes]html-directory=hotspot/ip routeaddcheck-gateway=ping comment="Standard Internet Route"disabled=no\
    distance=1dst-address=0.0.0.0/0gateway=172.31.1.9routing-table=main \
    scope=30suppress-hw-offload=notarget-scope=10addcomment="MGM"disabled=nodistance=1dst-address=172.27.1.0/28\
    gateway=10.241.31.1routing-table=main scope=30suppress-hw-offload=no\
    target-scope=10/ppp secretaddname=c1 profile=vpn-srv01 service=ovpnaddname=c2 profile=vpn-srv01 service=ovpn/routing bfd configurationadddisabled=nointerfaces=all min-rx=200msmin-tx=200msmultiplier=5/system clocksettime-zone-name=Europe/Berlin/system identitysetname=r-vpn/system loggingset0topics=info,ovpnaddtopics=debug,ovpn/system notesetshow-at-login=no/system ntp clientsetenabled=yes/system ntp client serversaddaddress=0.pool.ntp.orgaddaddress=1.pool.ntp.orgaddaddress=172.31.1.9/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN

---
```

## Response 1
Most VPNs are IP / layer 3, not ethernet / layer 2 and have their own mechanisms for client IP address assignment, they do not use DHCP. If the IoT devices are using their own inbuilt OpenVPN client the address will be provided from the pool or explicit addresses in the server PPP profile or secrets during the VPN connection setup. ---

## Response 2
So i need to assign a remote-address in the ppp profile for the openvpn server, correct? But if i do this, the dhcp-server ist still invalid.I changed the interface from dhcp-server from "ovpn-in1" to "bridge" and know the dhcp-server is active and not invalid. ---

## Response 3
So i need to assign a remote-address in the ppp profile for the openvpn server, correct? But if i do this, the dhcp-server ist still invalid.Yes. Creating a DHCP server is not necessary.I changed the interface from dhcp-server from "ovpn-in1" to "bridge" and know the dhcp-server is active and not invalid.Attaching the server to the bridge provides DHCP service through ethernet interfaces which are members of the bridge.You have specified a bridge in the PPP profile - this is only necessary to enable layer 2 bridging using BCP in PPP-based VPN protcols (PPTP, L2TP, SSTP), and likely only required when using layer2 OpenVPN (ethernet / tap) rather than layer 3 (IP / tun). ---

## Response 4
I think i try first to setup a normal OpenVPN connection from a client to a Mikrotik Router with username und password. If this is working, i try to figure out how to get a connection without username und password.For the moment i stuck on this messages on the router side:
```
usernamenotprovided

---
```