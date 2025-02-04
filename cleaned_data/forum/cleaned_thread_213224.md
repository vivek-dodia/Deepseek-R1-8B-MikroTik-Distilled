# Thread Information
Title: Thread-213224
Section: RouterOS
Thread ID: 213224

# Discussion

## Initial Question
I have a bit of a lab network setup. I have a small pool of public IP addresses that I'm providing to individual subnets behind my router (RB3011). The main thing I wanted was for each subnet to have it's own separate public IP when it connects out. I did this previously with mangle rules, but that had some limitations and it looked like Routing Tables in ROS7 would be a cleaner way to implement this. I've built the following config and got everything working as expected there.I'm just a little stuck at routing between my networks. I want to be able to ping devices between 172.16.200.0/24 on ether6 and 172.16.30.0/24 devices on ether7. I made a pair of firewall rules for this and added routes to all three routing tables, but I'm unable to fully pass my traffic. I can see the stat counters go up on one side of the rule, but not the response side. I'm hoping someone can take a look at my config here to point out what I'm doing wrong.
```
# 2024-12-11 09:52:57 by RouterOS 7.16.2# software id = TCVA-I1D0## model = RB3011UiAS# serial number = E7EA0EAD4BBB/interfacebridgeaddadmin-mac=2C:C8:1B:F5:F2:E9auto-mac=nocomment=defconf name=bridge/interfaceethernetset[finddefault-name=ether1]comment=wan-1set[finddefault-name=ether2]comment=wan-2set[finddefault-name=ether3]comment=wan-3set[finddefault-name=ether4]comment=wan-4set[finddefault-name=ether5]comment=client02-internal-networkset[finddefault-name=ether6]comment=client01-internal-networkset[finddefault-name=ether7]comment=client01-proxmox-internalset[finddefault-name=ether8]comment=client01-proxmox-hostedset[finddefault-name=ether10]comment=cellular-failover/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/ip pooladdname=default-dhcp ranges=192.168.88.10-192.168.88.254addname=client01-internalranges=172.16.200.10-172.16.200.254addname=client02-internalranges=192.168.1.10-192.168.1.254addname=proxmox-network ranges=10.0.0.10-10.0.0.254addname=proxmox-internalranges=172.16.30.10-172.16.30.50/ip dhcp-serveraddaddress-pool=default-dhcpinterface=bridge name=defconfaddadd-arp=yes address-pool=client01-internalinterface=ether6 name=\
    client01-internaladdaddress-pool=client02-internalinterface=ether5 name=\
    client02-internaladdadd-arp=yes address-pool=proxmox-internalinterface=ether7 name=\
    proxmox-internal/portset0name=serial0/routing tableadddisabled=nofib name=WAN-1adddisabled=nofib name=WAN-2adddisabled=nofib name=WAN-3adddisabled=nofib name=WAN-4/zerotiersetzt1 comment="ZeroTier Central controller - https://my.zerotier.com/"\
    name=zt1 port=9993/disk settingssetauto-media-interface=bridgeauto-media-sharing=yesauto-smb-sharing=yes/interfacebridge portaddbridge=bridge comment=defconfinterface=ether9addbridge=bridge comment=defconfinterface=sfp1/ip firewall connection trackingsetenabled=yes udp-stream-timeout=10mudp-timeout=10m/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WANaddinterface=ether2 list=WANaddinterface=ether3 list=WANaddinterface=ether4 list=WANaddinterface=ether6 list=LANaddinterface=ether5 list=LANaddinterface=ether7 list=LANaddinterface=ether8 list=LANaddcomment=cellular-backupinterface=ether10 list=WAN/ip addressaddaddress=192.168.88.1/24comment=defconfinterface=bridge network=\192.168.88.0addaddress=172.16.200.1/24comment=client01-internalinterface=ether6 \
    network=172.16.200.0addaddress=192.168.1.1/24comment=client02-internalinterface=ether5 \
    network=192.168.1.0addaddress=172.16.30.1/24comment=proxmox-internalinterface=ether7 network=\172.16.30.0addaddress=10.0.0.1/24comment=proxmox-hostedinterface=ether8 network=\10.0.0.0/ip cloudsetddns-enabled=yes ddns-update-interval=5m/ip dhcp-clientaddadd-default-route=nocomment=client01-waninterface=ether1addadd-default-route=nocomment=spare-waninterface=ether2addadd-default-route=nocomment=spare-waninterface=ether3addadd-default-route=nocomment=client02-waninterface=ether4addadd-default-route=nocomment=cellular-backupinterface=ether10/ip dhcp-server leaseaddaddress=192.168.1.11client-id=1:c4:5a:b1:9e:84:2amac-address=\
    C4:5A:B1:9E:84:2Aserver=client02-internaladdaddress=192.168.1.12client-id=1:0:15:5d:58:f3:0mac-address=\00:15:5D:58:F3:00server=client02-internaladdaddress=172.16.200.30client-id=1:78:2b:cb:32:61:0mac-address=\78:2B:CB:32:61:00server=client01-internaladdaddress=172.16.200.34client-id=1:90:b1:1c:14:70:6emac-address=\90:B1:1C:14:70:6Eserver=client01-internaladdaddress=192.168.1.100client-id=1:0:20:6b:7e:10:81mac-address=\00:20:6B:7E:10:81server=client02-internaladdaddress=172.16.30.48client-id=1:fa:6e:dd:63:fa:5fmac-address=\
    FA:6E:DD:63:FA:5Fserver=proxmox-internal/ip dhcp-server networkaddaddress=10.0.0.0/24comment=proxmox-hosted dns-server=8.8.8.8gateway=\10.0.0.1addaddress=172.16.30.0/24comment=proxmox-internaldns-server=8.8.8.8\
    gateway=172.16.30.1addaddress=172.16.200.0/24comment=client01-internaldns-server=\8.8.8.8,1.1.1.1gateway=172.16.200.1netmask=24addaddress=192.168.1.0/24comment=client02-internaldns-server=\192.168.1.11gateway=192.168.1.1netmask=24addaddress=192.168.88.0/24comment=defconf dns-server=192.168.88.1gateway=\192.168.88.1/ip dnssetservers=8.8.8.8/ip dnsstaticaddaddress=192.168.88.1comment=defconf name=router.lan type=A/ip firewall filteraddaction=accept chain=forward comment=\"client01-internal <--> proxmox-internal"dst-address=172.16.30.0/24log=\
    yes log-prefix="To-30: "src-address=172.16.200.0/24addaction=accept chain=forward comment=\"proxmox-internal <--> client01-internal"dst-address=172.16.200.0/24log=\
    yes log-prefix="To-200: "src-address=172.16.30.0/24addaction=accept chain=input comment=zerotierin-interface=zerotier1addaction=accept chain=forward comment=zerotierin-interface=zerotier1addaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"disabled=yes \
    protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related disabled=yes hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip firewall service-portsetsip disabled=yes/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/ip routeaddcheck-gateway=ping disabled=nodistance=10dst-address=0.0.0.0/0gateway=\66.183.191.1%ether1 routing-table=main suppress-hw-offload=noaddcheck-gateway=ping disabled=nodistance=10dst-address=0.0.0.0/0gateway=\66.183.191.1%ether4 routing-table=WAN-4scope=30suppress-hw-offload=no\
    target-scope=10addcheck-gateway=ping disabled=nodistance=10dst-address=0.0.0.0/0gateway=\66.183.191.1%ether1 routing-table=WAN-1scope=30suppress-hw-offload=no\
    target-scope=10addcheck-gateway=ping disabled=nodistance=10dst-address=0.0.0.0/0gateway=\66.183.191.1%ether2 routing-table=WAN-2scope=30suppress-hw-offload=no\
    target-scope=10addcheck-gateway=ping disabled=nodistance=10dst-address=0.0.0.0/0gateway=\66.183.191.1%ether3 routing-table=WAN-3scope=30suppress-hw-offload=no\
    target-scope=10addcheck-gateway=ping disabled=nodistance=1dst-address=172.16.30.0/24\
    gateway=ether7 routing-table=WAN-1suppress-hw-offload=noaddcheck-gateway=ping disabled=nodistance=1dst-address=172.16.200.0/24\
    gateway=ether6 routing-table=WAN-1suppress-hw-offload=noaddcheck-gateway=ping disabled=nodistance=20dst-address=0.0.0.0/0gateway=\10.100.0.1%ether10 routing-table=main suppress-hw-offload=noaddcheck-gateway=ping disabled=nodistance=1dst-address=172.16.30.0/24\
    gateway=ether7 routing-table=WAN-2suppress-hw-offload=noaddcheck-gateway=ping disabled=nodistance=1dst-address=172.16.200.0/24\
    gateway=ether6 routing-table=WAN-2suppress-hw-offload=no/ip servicesetwww address=172.16.200.0/24,0.0.0.0/0,172.25.0.0/16setwinbox address=0.0.0.0/0/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
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
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/lcdsetcolor-scheme=light/routing ruleaddaction=lookup disabled=nointerface=ether6 table=WAN-1addaction=lookup disabled=nointerface=ether7 table=WAN-2addaction=lookup-only-in-table disabled=nointerface=ether8 table=WAN-3addaction=lookup-only-in-table disabled=nointerface=ether5 table=WAN-4/system clocksettime-zone-name=America/Vancouver/system notesetshow-at-login=no/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN

---
```

## Response 1
I think your missing a /routing/rule that says traffic NOT to internet should use "main" routing table (i.e. the 0.0.0.0/0 route, which is represented as min-prefix=0). This rule should be list FIRST - before the WAN-per-interface route rules - otherwise local traffic is ALSO route to WAN's default gateway, which won't work...
```
/routing/ruleaddmin-prefix=0action=lookup table=mainThere may be other issues since I didn't disect the rest of the config, but the above (or alternative multiple rules to with "dst-address=<lan-subnet> table=main" — but the min-prefix=0 should cover all your local subnets in one line)

---
```

## Response 2
Right on! That was exactly what I needed. Pinging between networks as expected now. Thank you! ---

## Response 3
Good to hear. It's a bit confusing at first... FWIW rules run from top to bottom, first match wins. So when you create a broad rule (i.e. all traffic on an interface), it does mean send ALL traffic, including local ones, to the specific routing table=. Why adding your local routes as rule to "main" is needed (which the min-prefix=0 rule does) - since each WAN routing table does NOT have any local routes defined, anything in that goes to WAN table goes that specific WAN's gateway... But it's not obvious at first. ---