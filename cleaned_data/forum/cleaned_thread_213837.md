# Thread Information
Title: Thread-213837
Section: RouterOS
Thread ID: 213837

# Discussion

## Initial Question
Hello, I'm migrating from a RB750Gr3 router to rb5009ug_s_in. I've exported the configuration from one device and imported it in the new one and I can see that the router is able to connect to internet, since I checked for updates and I was able to download/upgrade the router. The issue I'm facing is that I'm not able to reach internet from any of the LAN ports connected to the router. I'm able to see the rest of devices in the same LAN, but I don't seem to be able to reach WAN. Since the rb5009ug_s_in router has a dedicated switch, I'm not sure if I need to configure anything else there in order to be able to fix this issue.I'm checking that there are some remnants of the default IP in the configuration (192.168.88.1), not sure if that could be also a problem aside the routing.This is the current configuration:
```
# 2025-01-10 19:28:49 by RouterOS 7.16.2
#
# model = RB5009UG+S+
/interface bridge
add admin-mac=F4:1E:57:83:0C:94 auto-mac=no comment=defconf name=local port-cost-mode=short
/interface ethernet
set [ find default-name=ether1 ] name=ether_isp
/interface vlan
add interface=ether_isp name=vlan_isp vlan-id=20
/interface pppoe-client
add add-default-route=yes disabled=no interface=vlan_isp name=pppoe-out1 use-peer-dns=yes user=pppoe-user
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface lte apn
set [ find default=yes ] ip-type=ipv4 use-network-apn=no
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
/ip smb users
set [ find default=yes ] disabled=yes
/disk settings
set auto-media-interface=local auto-media-sharing=yes auto-smb-sharing=yes
/interface bridge port
add bridge=local comment=defconf interface=ether2
add bridge=local comment=defconf interface=ether3
add bridge=local comment=defconf interface=ether4
add bridge=local comment=defconf interface=ether5
add bridge=local comment=defconf interface=ether6
add bridge=local comment=defconf interface=ether7
add bridge=local comment=defconf interface=ether8
add bridge=local comment=defconf interface=sfp-sfpplus1
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=none
/ip settings
set tcp-syncookies=yes
/ipv6 settings
set disable-ipv6=yes max-neighbor-entries=8192
/interface list member
add comment=defconf interface=local list=LAN
add comment=defconf interface=ether_isp list=WAN
/ip address
add address=192.168.3.1/23 interface=local network=192.168.2.0
/ip cloud
set update-time=no
/ip dhcp-client
add comment=defconf interface=ether_isp
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,1.0.0.1
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
/ip firewall address-list
add address=192.168.3.2-192.168.3.254 list=allowed_to_router
add address=0.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=172.16.0.0/12 comment=RFC6890 list=not_in_internet
add address=192.168.0.0/16 comment=RFC6890 list=not_in_internet
add address=10.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=169.254.0.0/16 comment=RFC6890 list=not_in_internet
add address=127.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=224.0.0.0/4 comment=Multicast list=not_in_internet
add address=198.18.0.0/15 comment=RFC6890 list=not_in_internet
add address=192.0.0.0/24 comment=RFC6890 list=not_in_internet
add address=192.0.2.0/24 comment=RFC6890 list=not_in_internet
add address=198.51.100.0/24 comment=RFC6890 list=not_in_internet
add address=203.0.113.0/24 comment=RFC6890 list=not_in_internet
add address=100.64.0.0/10 comment=RFC6890 list=not_in_internet
add address=240.0.0.0/4 comment=RFC6890 list=not_in_internet
add address=192.88.99.0/24 comment="6to4 relay Anycast [RFC 3068]" list=not_in_internet
/ip firewall filter
add action=accept chain=input comment="default configuration" connection-state=established,related \
    disabled=yes
add action=accept chain=input disabled=yes src-address-list=allowed_to_router
add action=accept chain=input disabled=yes protocol=icmp
add action=accept chain=input disabled=yes dst-port=51215 protocol=udp
add action=accept chain=input disabled=yes src-address=192.168.100.0/24 src-address-list=""
add action=drop chain=input disabled=yes
add action=fasttrack-connection chain=forward comment=FastTrack connection-state=established,related \
    disabled=yes hw-offload=yes
add action=accept chain=forward comment="Established, Related" connection-state=established,related \
    disabled=yes
add action=drop chain=forward comment="Drop invalid" connection-state=invalid disabled=yes log-prefix=\
    invalid
add action=drop chain=forward comment="Drop incoming packets that are not NAT`ted" connection-nat-state=\
    !dstnat connection-state=new disabled=yes in-interface=ether_isp log=yes log-prefix=!NAT
add action=jump chain=forward comment="jump to ICMP filters" disabled=yes jump-target=icmp protocol=icmp
add action=drop chain=forward comment="Drop incoming from internet which is not public IP" disabled=yes \
    in-interface=ether_isp log=yes log-prefix=!public src-address-list=not_in_internet
add action=accept chain=icmp comment="echo reply" disabled=yes icmp-options=0:0 protocol=icmp
add action=accept chain=icmp comment="net unreachable" disabled=yes icmp-options=3:0 protocol=icmp
add action=accept chain=icmp comment="host unreachable" disabled=yes icmp-options=3:1 protocol=icmp
add action=accept chain=icmp comment="host unreachable fragmentation required" disabled=yes icmp-options=\
    3:4 protocol=icmp
add action=accept chain=icmp comment="allow echo request" disabled=yes icmp-options=8:0 protocol=icmp
add action=accept chain=icmp comment="allow time exceed" disabled=yes icmp-options=11:0 protocol=icmp
add action=accept chain=icmp comment="allow parameter bad" disabled=yes icmp-options=12:0 protocol=icmp
add action=drop chain=icmp comment="deny all other types" disabled=yes
/ip firewall nat
add action=masquerade chain=srcnat out-interface-list=WAN
add action=dst-nat chain=dstnat dst-port=50010 in-interface-list=WAN protocol=tcp to-addresses=\
    192.168.3.111 to-ports=50010
add action=dst-nat chain=dstnat dst-port=50101 in-interface-list=WAN protocol=tcp to-addresses=\
    192.168.3.111 to-ports=50101
add action=dst-nat chain=dstnat dst-port=52100 in-interface-list=WAN protocol=tcp to-addresses=\
    192.168.3.111 to-ports=52100
add action=dst-nat chain=dstnat dst-port=52112 in-interface-list=WAN protocol=tcp src-port="" to-addresses=\
    192.168.3.111 to-ports=52112
add action=dst-nat chain=dstnat dst-port=51015 in-interface-list=WAN protocol=tcp to-addresses=\
    192.168.3.111 to-ports=51015
add action=dst-nat chain=dstnat dst-port=50001-50009 in-interface-list=WAN protocol=udp to-addresses=\
    192.168.3.111 to-ports=50001-50009
add action=dst-nat chain=dstnat dst-port=50001-50009 in-interface-list=WAN protocol=tcp to-addresses=\
    192.168.3.111 to-ports=50001-50009
add action=dst-nat chain=dstnat dst-port=55111 in-interface-list=WAN protocol=tcp to-addresses=\
    192.168.3.111 to-ports=55111
add action=dst-nat chain=dstnat dst-port=80 in-interface-list=WAN protocol=tcp to-addresses=192.168.3.111 \
    to-ports=80
add action=dst-nat chain=dstnat disabled=yes dst-port=443 in-interface-list=WAN protocol=tcp to-addresses=\
    192.168.3.111 to-ports=443
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set ssh address=192.168.3.0/24
set api disabled=yes
set winbox address=192.168.3.0/24
set api-ssl disabled=yes
/ipv6 firewall address-list
add address=::/128 comment="defconf: unspecified address" list=bad_ipv6
add address=::1/128 comment="defconf: lo" list=bad_ipv6
add address=fec0::/10 comment="defconf: site-local" list=bad_ipv6
add address=::ffff:0.0.0.0/96 comment="defconf: ipv4-mapped" list=bad_ipv6
add address=::/96 comment="defconf: ipv4 compat" list=bad_ipv6
add address=100::/64 comment="defconf: discard only " list=bad_ipv6
add address=2001:db8::/32 comment="defconf: documentation" list=bad_ipv6
add address=2001:10::/28 comment="defconf: ORCHID" list=bad_ipv6
add address=3ffe::/16 comment="defconf: 6bone" list=bad_ipv6
/ipv6 firewall filter
add action=accept chain=input comment="defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=invalid
add action=accept chain=input comment="defconf: accept ICMPv6" protocol=icmpv6
add action=accept chain=input comment="defconf: accept UDP traceroute" dst-port=33434-33534 protocol=udp
add action=accept chain=input comment="defconf: accept DHCPv6-Client prefix delegation." dst-port=546 \
    protocol=udp src-address=fe80::/10
add action=accept chain=input comment="defconf: accept IKE" dst-port=500,4500 protocol=udp
add action=accept chain=input comment="defconf: accept ipsec AH" protocol=ipsec-ah
add action=accept chain=input comment="defconf: accept ipsec ESP" protocol=ipsec-esp
add action=accept chain=input comment="defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=input comment="defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
add action=accept chain=forward comment="defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" connection-state=invalid
add action=drop chain=forward comment="defconf: drop packets with bad src ipv6" src-address-list=bad_ipv6
add action=drop chain=forward comment="defconf: drop packets with bad dst ipv6" dst-address-list=bad_ipv6
add action=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1" hop-limit=equal:1 protocol=icmpv6
add action=accept chain=forward comment="defconf: accept ICMPv6" protocol=icmpv6
add action=accept chain=forward comment="defconf: accept HIP" protocol=139
add action=accept chain=forward comment="defconf: accept IKE" dst-port=500,4500 protocol=udp
add action=accept chain=forward comment="defconf: accept ipsec AH" protocol=ipsec-ah
add action=accept chain=forward comment="defconf: accept ipsec ESP" protocol=ipsec-esp
add action=accept chain=forward comment="defconf: accept all that matches ipsec policy" ipsec-policy=\
    in,ipsec
add action=drop chain=forward comment="defconf: drop everything else not coming from LAN" \
    in-interface-list=!LAN
/system clock
set time-zone-name=Europe/Madrid
/system note
set show-at-login=no
/system ntp client
set enabled=yes
/system ntp client servers
add address=0.europe.pool.ntp.org
add address=1.europe.pool.ntp.org
add address=2.europe.pool.ntp.org
add address=3.europe.pool.ntp.org
/tool bandwidth-server
set enabled=no
/tool mac-server
set allowed-interface-list=none
/tool mac-server mac-winbox
set allowed-interface-list=none
/tool mac-server ping
set enabled=no

---
```

## Response 1
Your configuration is a bit confusing to me.The onlyaction=masqueraderule in thesrcnatchain of/ip firewall natmatches onout-interface-list=WAN, and the only member of interface list WAN isether_isp, to which a DHCP client is also attached. So if this is the actual WAN, the LAN hosts should be able to access the internet. But there is also an/interface pppoe-client name=pppoe-out1that is attached to/interface vlanattached toether_isp; if the PPPoE client interface is the actual WAN interface that receives an address from the ISP, then you have to makepppoe-out1a member of interface list WAN rather thanether_isp. ---

## Response 2
You cannot successfully take one configuration from one model and import it into another.The best case is copying bits of the config at a time from the /export file and pasting into the new router.Your subnet is all over the map 192.168.88 or 192.168.3 or 192.168.2 LOLEnable your fricken firewall rules.# model = RB5009UG+S+/ip neighbor discovery-settingsset discover-interface-list=LAN/ip settingsset tcp-syncookies=no/interface list memberadd comment=defconf interface=local list=LANadd comment=defconf interface=ether_isp list=WANadd interface=pppoe-out1 list=WAN/ip addressadd address=192.168.88.1/24 interface=local network=192.168.88.0/ip dhcp-clientadd comment=defconf interface=ether_isp disabled=yes/ip firewall address-listadd address=192.168.88.0/24 list=allowed_to_router/ip firewall filteradd action=accept chain=input connection-state=established, related, untrackedadd action=drop chain=input protocol=invalidadd action=accept chain=input protocol=icmpadd action=accept chain=input dst-port=51215 protocol=udpadd action=accept chain=input in-interface-list=LAN src-address-list=allowed_to_routeradd action=drop chain=input comment="drop all else" { put this rule in last }add action=fasttrack-connection chain=forward comment=FastTrack connection-state=established, related \disabled=yes hw-offload=yesadd action=accept chain=forward comment="Established, Related" connection-state=established, related \disabled=yesadd action=drop chain=forward comment="Drop invalid" connection-state=invalidadd action=accept chain=forward comment="internet traffic" in-interface-list=LAN out-interface-list=WANadd action=accept chain=forward comment="port forwarding" connection-nat-state=dstnatadd action action=drop chain=forward comment="Drop all else"/ip serviceset telnet disabled=yesset ftp disabled=yesset www disabled=yesset ssh address=192.168.88.0/24set api disabled=yesset winbox address=192.168.88.0/24set api-ssl disabled=yes/tool mac-serverset allowed-interface-list=none/tool mac-server mac-winboxset allowed-interface-list=LAN ---

## Response 3
What a mess...I didn't import the whole configuration, but copied some bits of it. I'm not sure if this this router model or the RouterOS version, but it seems it now has several defaults set that I don't remember having when I first configured the RB750Gr3. I think this might be the case of all those different IP values. I think it would be best to start from scratch and review all values, since as you have already pointed out, there are several issues in the configuration I wasn't aware.Thanks for your help. ---