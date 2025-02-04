# Thread Information
Title: Thread-1113992
Section: RouterOS
Thread ID: 1113992

# Discussion

## Initial Question
I have HEX RB750Gr3 running on RouterOS 7.16.2My setup is:Two WAN: PPPoE (ether1)+ DHCP client(ether2)I configured the PCC load balance and recursive failover.Everything is working fine, all LAN devices can use both WANs and failover. The only two things that are not working are: Routeros-tool-ping-- cannot ping any IP on internet(also can not check for package update)Also, I had setup wireguard server that also do not work.The thing is that the RouterOS can ping the internet only if I add a default route on main routing table.But then PCC load balance breaks. I tried every solution out there on the internet but nothing fix this.Posting my configuration here, please have a look and help me.
```
/ip firewall mangle print

Flags: X - disabled, I - invalid; D - dynamic

0 D ;;; special dummy rule to show fasttrack counters

chain=prerouting action=passthrough



1 D ;;; special dummy rule to show fasttrack counters

chain=forward action=passthrough



2 D ;;; special dummy rule to show fasttrack counters

chain=postrouting action=passthrough



3 chain=prerouting action=mark-connection new-connection-mark=WAN1 passthrough=yes

connection-state=new connection-mark=no-mark in-interface=pppoe-out1 log=no log-prefix=""



4 chain=prerouting action=mark-connection new-connection-mark=WAN2 passthrough=yes

connection-state=new connection-mark=no-mark in-interface=ether2 log=no log-prefix=""



5 chain=output action=mark-routing new-routing-mark=via-ISP1 passthrough=no

dst-address-type=!local connection-mark=WAN1 log=no log-prefix=""



6 chain=output action=mark-routing new-routing-mark=via-ISP2 passthrough=no

dst-address-type=!local connection-mark=WAN2 log=no log-prefix=""



7 chain=prerouting action=mark-connection new-connection-mark=WAN1 passthrough=yes

connection-state=new dst-address-type=!local connection-mark=no-mark in-interface=bridge

per-connection-classifier=src-address-and-port:2/0 log=no log-prefix=""



8 chain=prerouting action=mark-connection new-connection-mark=WAN2 passthrough=yes

connection-state=new dst-address-type=!local connection-mark=no-mark in-interface=bridge

per-connection-classifier=src-address-and-port:2/1 log=no log-prefix=""



9 chain=prerouting action=mark-routing new-routing-mark=via-ISP1 passthrough=yes

connection-mark=WAN1 in-interface=bridge log=no log-prefix=""



10 chain=prerouting action=mark-routing new-routing-mark=via-ISP2 passthrough=yes

connection-mark=WAN2 in-interface=bridge log=no log-prefix=""



/ip route print

Flags: D - DYNAMIC; I - INACTIVE, A - ACTIVE; c - CONNECT, s - STATIC; H - HW-OFFLOADED

Columns: DST-ADDRESS, GATEWAY, DISTANCE

# DST-ADDRESS GATEWAY DISTANCE

;;; isp2

0 As 1.1.1.1/32 192.168.1.1 1

;;; isp1

1 As 8.8.8.8/32 117.1xx.x.x 1

DAc 10.0.2.0/24 wireguard1 0

DAc 117.1xx.x.x/32 pppoe-out1 0

DAc 172.16.33.0/24 bridge 0

DAc 192.168.1.0/24 ether2 0

DAc 192.168.2.1/32 ether1 0

2 s 0.0.0.0/0 1.1.1.1 2

3 As 0.0.0.0/0 8.8.8.8 1

4 IsH 8.8.8.8/32 8.8.8.8 1

5 As 192.168.2.1/32 192.168.2.1 1



/ip firewall filter print

Flags: X - disabled, I - invalid; D - dynamic

0 D ;;; special dummy rule to show fasttrack counters

chain=forward action=passthrough



1 ;;; allow WireGuard

chain=input action=accept protocol=udp dst-port=13231 log=no log-prefix=""



2 ;;; defconf: accept established,related,untracked

chain=input action=accept connection-state=established,related,untracked



3 ;;; defconf: drop invalid

chain=input action=drop connection-state=invalid



4 ;;; defconf: accept ICMP

chain=input action=accept protocol=icmp



5 ;;; defconf: accept to local loopback (for CAPsMAN)

chain=input action=accept dst-address=127.0.0.1



6 ;;; defconf: drop all not coming from LAN

chain=input action=drop in-interface-list=!LAN



7 ;;; defconf: accept in ipsec policy

chain=forward action=accept ipsec-policy=in,ipsec



8 ;;; defconf: accept out ipsec policy

chain=forward action=accept ipsec-policy=out,ipsec



9 ;;; defconf: fasttrack

chain=forward action=fasttrack-connection hw-offload=yes

connection-state=established,related log=no log-prefix=""



10 ;;; defconf: accept established,related, untracked

chain=forward action=accept connection-state=established,related,untracked



11 ;;; defconf: drop invalid

chain=forward action=drop connection-state=invalid



12 ;;; defconf: drop all from WAN not DSTNATed

chain=forward action=drop connection-state=new connection-nat-state=!dstnat

in-interface-list=WAN

---
```

## Response 1
There are two distinct major issues - the routing of router's own outgoing traffic in general and the unique behavior of the Wireguard stack.The default route in tablemainis mandatory for the own traffic of the router to get sent due to the way how this locally originated traffic is treated. Any packet the router itself sends is first routed using routing table main, and if it is not a response packet, its source address is chosen and assigned as part of the routing process. And only then the packet hits the mangle rules in chain output. If the packet obtains a routing mark there, it gets routed again according to that routing mark, but its source address is not automatically changed in this second round of rouiting, so you need thesrc-natormasqueraderules to take care of that.When you say that adding the default route to table main breaks the PCC-based distribution of the traffic, do you have in mind the distribution of the forwarded traffic (from LAN devices to internet) or the distribution of router's own traffic? I cannot see why the forwarded traffic should be affected, but since theip route printdoes not show therouting-tableproperties of the routes, I cannot be sure. Please use a properexportof the complete configuration rather thanprint. But without hesitation I can tell you to get rid of the two routes that saydst-address=8.8.8.8/32 gateway=8.8.8.8anddst-address=192.168.2.1/32 gateway=192.168.2.1, they make no sense.The next major issue is the unique behavior of the Wireguard stack that apparently does not set the source address for its outgoing packets even if they are responses to incoming ones on the application level, and lets the routing choose their source addresses. So it is not enough that you assign connection marks to connections initiated from the internet depending on theirin-interfaceand then translate thisconnection-markto arouting-markinoutput; you also have to use a dst-nat rule that redirects the request to the own address of the router that the routing will assign to outgoing packets that do not have any yet. If that address is not assigned statically, it requires a more convoluted workaround.Lastly, there is a minor issue that is currently shadowed by the major ones but it will pop up once you sort them out. You prevent somemark-routingandmark-connectionrules from acting by letting them match ondst-address-type=!local. This is sufficient to prevent them from acting on traffic for the router itself, which is probably why this is shown in so many topics here and so many video tutorials. But this approach is insufficient if you use more than one "internal" subnet, because you don't want those rules to affect the routing of the traffic between your internal subnets either. So once your Wireguard connections start working again, you will find out that the current PCC rules redirect also the Wireguard payload. So instead of letting those rules match ondst-address-type=!local, create an address listmy-subnets, put all the internal subnets to it, and let the rules match ondst-address-list=!my-subnets. ---

## Response 2
As requested/export file=anynameyouwish ( remove router serial number, any public WANIP information, vpn keys etc.)Should be quick to fix once seen. ---

## Response 3
As asked here is the full config
```
# 2024-12-09 03:57:50 by RouterOS 7.16.2
# software id = QCAY-BVGA
#
# model = RB750Gr3
# serial number = Hgggggggg
/disk
set usb1 media-interface=none media-sharing=no
/interface bridge
add admin-mac=48:39:83:23B:50:E0 auto-mac=no comment=defconf name=bridge \
    port-cost-mode=short
/interface ethernet
set [ find default-name=ether1 ] mac-address=1C:3B:F3:B3:F8:27
/interface lte
set [ find default-name=lte1 ] sms-protocol=auto sms-read=no
/interface pppoe-client
add comment="BSNL Internet" disabled=no interface=ether1 name=pppoe-out1 \
    user=aas12412121313
/interface wireguard
add listen-port=13231 mtu=1420 name=wireguard1
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface lte apn
set [ find default=yes ] ip-type=ipv4 use-network-apn=no
/ip pool
add name=dhcp ranges=172.16.33.100-172.16.33.200
/ip dhcp-server
add address-pool=dhcp interface=bridge lease-time=10m name=defconf
/port
set 0 name=serial0
/queue type
add kind=fq-codel name="FQ Codel"
add kind=cake name=cake
/routing table
add disabled=no fib name=via-ISP1
add disabled=no fib name=via-ISP2
/system logging action
add disk-file-name=usb1/log name=USB target=disk
/interface bridge port
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether2 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf ingress-filtering=no interface=ether3 \
    internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf ingress-filtering=no interface=ether4 \
    internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf ingress-filtering=no interface=ether5 \
    internal-path-cost=10 path-cost=10
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=LAN
/ipv6 settings
set max-neighbor-entries=8192
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=pppoe-out1 list=WAN
add interface=wireguard1 list=LAN
add comment=zepbyte interface=ether2 list=WAN
/interface ovpn-server server
set auth=sha1,md5
/interface wireguard peers
add allowed-address=10.0.2.2/32,fd00:321:421::2/128 interface=wireguard1 \
    name=wg0 public-key="*******************************************"
add allowed-address=10.0.2.3/32,fd00:321:421::3/128 interface=wireguard1 \
    name="hp laptop" public-key=\
    "************************************"
/ip address
add address=172.16.33.1/24 comment=defconf interface=bridge network=\
    172.16.33.0
add address=10.0.2.1/24 comment="wireguard server" interface=wireguard1 \
    network=10.0.2.0
add address=192.168.2.5 comment="ONT device" interface=ether1 network=\
    192.168.2.1
/ip dhcp-client
add comment=defconf disabled=yes interface=ether1
add add-default-route=no interface=ether2 use-peer-dns=no use-peer-ntp=no
/ip dhcp-server lease
add address=172.16.33.2 client-id=1:c0:25:2f:e1:84:80 comment=Halo1 \
    mac-address=C0:25:2F:E1:84:80 server=defconf
add address=172.16.33.12 client-id=1:20:a6:c:3c:c4:9d comment="Poco F1" \
    mac-address=20:A6:0C:3C:C4:9D server=defconf
add address=172.16.33.14 client-id=1:84:1b:77:36:18:34 comment=Colt \
    mac-address=84:1B:77:36:18:34 server=defconf
add address=172.16.33.3 client-id=1:c0:25:2f:e1:90:5c comment=Halo2 \
    mac-address=C0:25:2F:E1:90:5C server=defconf
add address=172.16.33.11 client-id=1:12:4c:70:a6:2d:b9 comment=\
    "office laptop" mac-address=12:4C:70:A6:2D:B9 server=defconf
add address=172.16.33.4 client-id=1:9c:9d:7e:80:ed:9b comment=Pawan \
    mac-address=9C:9D:7E:80:ED:9B server=defconf
add address=172.16.33.10 client-id=1:54:bf:64:6b:8c:97 comment=Server \
    mac-address=54:BF:64:6B:8C:97 server=defconf
add address=172.16.33.13 client-id=1:3c:b0:ed:11:2b:9c comment=CMF \
    mac-address=3C:B0:ED:11:2B:9C server=defconf
add address=172.16.33.20 comment=NVR mac-address=1C:61:B4:3D:FA:C7 server=\
    defconf
/ip dhcp-server network
add address=172.16.33.0/24 comment=defconf dns-server=8.8.8.8 gateway=\
    172.16.33.1 netmask=24
/ip dns
set allow-remote-requests=yes servers=8.8.8.8
/ip dns static
add address=10.0.0.1 comment=defconf name=router.lan type=A
/ip firewall address-list
add address=10.0.0.0/8 list=LOCAL
add address=172.16.0.0/12 list=LOCAL
add address=192.168.0.0/16 list=LOCAL
/ip firewall filter
add action=accept chain=input comment="allow WireGuard" dst-port=13231 \
    protocol=udp
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment=\
    "defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=drop chain=input comment="defconf: drop all not coming from LAN" \
    in-interface-list=!LAN
add action=accept chain=forward comment="defconf: accept in ipsec policy" \
    ipsec-policy=in,ipsec
add action=accept chain=forward comment="defconf: accept out ipsec policy" \
    ipsec-policy=out,ipsec
add action=fasttrack-connection chain=forward comment="defconf: fasttrack" \
    connection-state=established,related hw-offload=yes
add action=accept chain=forward comment=\
    "defconf: accept established,related, untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \
    connection-state=new in-interface-list=WAN
/ip firewall mangle
add action=log chain=dummy comment=dummy
add action=mark-connection chain=prerouting connection-mark=no-mark \
    connection-state=new dst-address-type=!local in-interface=bridge \
    new-connection-mark=WAN1 passthrough=yes per-connection-classifier=\
    src-address-and-port:2/0
add action=mark-routing chain=prerouting connection-mark=WAN1 in-interface=\
    bridge new-routing-mark=via-ISP1 passthrough=no
add action=mark-connection chain=prerouting connection-mark=no-mark \
    connection-state=new dst-address-type=!local in-interface=bridge \
    new-connection-mark=WAN2 passthrough=yes per-connection-classifier=\
    src-address-and-port:2/1
add action=mark-routing chain=prerouting connection-mark=WAN2 in-interface=\
    bridge new-routing-mark=via-ISP2 passthrough=no
add action=log chain=dummy comment=dummy
add action=mark-connection chain=prerouting connection-mark=no-mark \
    connection-state=new in-interface=ether2 new-connection-mark=WAN2 \
    passthrough=yes
add action=mark-routing chain=output connection-mark=WAN1 dst-address-type=\
    !local new-routing-mark=via-ISP1 passthrough=no
add action=mark-connection chain=prerouting connection-mark=no-mark \
    connection-state=new in-interface=pppoe-out1 new-connection-mark=WAN1 \
    passthrough=yes
add action=mark-routing chain=output connection-mark=WAN2 dst-address-type=\
    !local new-routing-mark=via-ISP2 passthrough=no
add action=log chain=dummy comment=dummy
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=dst-nat chain=dstnat comment=tailscale dst-port=41641 protocol=udp \
    to-addresses=172.16.33.10 to-ports=41641
add action=dst-nat chain=dstnat comment="qbittorrent port open" dst-port=\
    50206 protocol=tcp to-addresses=172.16.33.10 to-ports=50206
add action=dst-nat chain=dstnat comment=nginx disabled=yes dst-port=443 \
    in-interface-list=WAN protocol=tcp to-addresses=172.16.33.10 to-ports=443
# lte1 not ready
add action=masquerade chain=srcnat out-interface=lte1
/ip hotspot profile
set [ find default=yes ] html-directory=hotspot
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/ip route
add comment=isp1 disabled=no distance=1 dst-address=8.8.8.8/32 gateway=\
    11x.xxx.xx.x routing-table=main scope=10 suppress-hw-offload=no \
    target-scope=10
add comment=isp2 disabled=no distance=1 dst-address=1.1.1.1/32 gateway=\
    192.168.1.1 routing-table=main scope=10 suppress-hw-offload=no \
    target-scope=10
add check-gateway=ping disabled=no distance=1 dst-address=0.0.0.0/0 gateway=\
    8.8.8.8 routing-table=via-ISP1 scope=10 suppress-hw-offload=no \
    target-scope=11
add check-gateway=ping disabled=no distance=1 dst-address=0.0.0.0/0 gateway=\
    1.1.1.1 routing-table=via-ISP2 scope=10 suppress-hw-offload=no \
    target-scope=11
add check-gateway=ping disabled=no distance=2 dst-address=0.0.0.0/0 gateway=\
    1.1.1.1 routing-table=via-ISP1 scope=10 suppress-hw-offload=no \
    target-scope=11
add check-gateway=ping disabled=no distance=2 dst-address=0.0.0.0/0 gateway=\
    8.8.8.8 routing-table=via-ISP2 scope=10 suppress-hw-offload=no \
    target-scope=11
add comment="route to ont" disabled=yes distance=1 dst-address=192.168.2.1/32 \
    gateway=192.168.2.1 routing-table=via-ISP1 scope=30 suppress-hw-offload=\
    no target-scope=10
add comment="route to ont" disabled=yes distance=1 dst-address=192.168.2.1/32 \
    gateway=192.168.2.1 routing-table=via-ISP2 scope=30 suppress-hw-offload=\
    no target-scope=10
add comment="route to vinod ont" disabled=yes distance=1 dst-address=\
    192.168.1.1/32 gateway=192.168.1.1 routing-table=via-ISP1 scope=30 \
    suppress-hw-offload=no target-scope=10
add comment="route to vinod ont" disabled=yes distance=1 dst-address=\
    192.168.1.1/32 gateway=192.168.1.1 routing-table=via-ISP2 scope=30 \
    suppress-hw-offload=no target-scope=10
/ipv6 address
add address=fd00:420:530::1 comment=ULA interface=bridge
add address=fd00:321:421::1 advertise=no comment="wireguard prefix" \
    interface=wireguard1
# address pool error: pool not found: bsnl (4)
add address=::1 comment=BSNL from-pool=bsnl interface=bridge
/ipv6 dhcp-client
add add-default-route=yes disabled=yes interface=pppoe-out1 pool-name=bsnl \
    request=prefix use-peer-dns=no
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
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=accept chain=input comment="allow wireguard" dst-port=13231 \
    protocol=udp
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=input comment="defconf: accept UDP traceroute" port=\
    33434-33534 protocol=udp
add action=accept chain=input comment=\
    "defconf: accept DHCPv6-Client prefix delegation." dst-port=546 protocol=\
    udp src-address=fe80::/10
add action=accept chain=input comment="defconf: accept IKE" dst-port=500,4500 \
    protocol=udp
add action=accept chain=input comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=input comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=input comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=input comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
add action=accept chain=forward comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop packets with bad src ipv6" src-address-list=bad_ipv6
add action=drop chain=forward comment=\
    "defconf: drop packets with bad dst ipv6" dst-address-list=bad_ipv6
add action=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1" \
    hop-limit=equal:1 protocol=icmpv6
add action=accept chain=forward comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=forward comment="defconf: accept HIP" protocol=139
add action=accept chain=forward comment="defconf: accept IKE" dst-port=\
    500,4500 protocol=udp
add action=accept chain=forward comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=forward comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=forward comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=forward comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
/ipv6 firewall nat
add action=masquerade chain=srcnat comment=\
    "Allow wireguard client ipv6 internet" src-address=fd00:321:421::/64
/routing bfd configuration
add disabled=no interfaces=all min-rx=200ms min-tx=200ms multiplier=5
/routing rule
add action=lookup disabled=no routing-mark=via-ISP1 table=via-ISP1
add action=lookup disabled=no routing-mark=via-ISP2 table=via-ISP2
/system clock
set time-zone-name=Asia/Kolkata
/system logging
set 0 action=USB
set 1 action=USB
set 2 action=USB
/system note
set show-at-login=no
/system routerboard settings
set auto-upgrade=yes silent-boot=yes
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN

---
```

## Response 4
As the configuration without any default route in table main is not very typical, I'm not sure whether this explains why you say that PCC works without it and doesn't without, but: the essence of fastpath & fasttrack handling of packets is skipping of some stages of packet processing, one of which is mangling. So for all connections that initially establish via the WAN that is not the preferred one in routing tablemainyou have to make sure that no packet of such connections, no matter the direction, will ever match theaction=fasttrack-connectionrule. Since you already do use connection marks, the easiest way is to add a match conditionconnection-mark=no-mark, which will currently prevent all forwarded connections from getting fasttracked because you mark all of them, but you can fine tune that later.The rest of what I wrote before remains valid. ---

## Response 5
I'm so sorry but I have no clue what you said. I am new to routeros and don't know any of this.Can you please tell me what to change and what to add?. ---

## Response 6
OK, simple terms:/interface pppoe-client set [find] default-route-distance=10/ip route add gateway=8.8.8.8 distance=1 check-gateway=ping/ip route add gateway=1.1.1.1 distance=2 check-gateway=pingTo allow the Mikrotik itself to communicate, theremustbe routes in routing tablemain, there's no way to avoid that. But the "side effects" can be removed./ip firewall filter set [find action=fasttrack-connection] connection-mark=no-markThis should make the PCC distribution work again even though default routes in tablemainexist.we shall get to the Wireguard functionality later, it is a complicated issue.ip firewall/mangle/set [find where dst-address-type~"!local"] !dst-address-type dst-address-list=LOCALThis fixes an issue you haven't bumped into yet because Wireguard is not working.Once you do this, check that your Mikrotik can ping the world and check for updates and that PCC of the forwarded traffic still works and report back. No matter the result, post an export of the configuration after the changes. ---

## Response 7
First of all, thank you so much. Everything seems to work as I intended.what worked for me:
```
/interface pppoe-client set [find] default-route-distance=10
 /ip firewall filter set [find action=fasttrack-connection] connection-mark=no-markthese two changes worked for me. Wireguard is also working.I also want to explain something. I want routeros to reach internet with pppoe connection only and intend to use wireguard with pppoe connection. Both of these things are working with above config.A few questions.1. What is the use of these two routes?
```

```
/ip route add gateway=8.8.8.8 distance=1 check-gateway=ping
/ip route add gateway=1.1.1.1 distance=2 check-gateway=ping2. After modifying this, I was not able to use both connections simultaneously, i.e., the load was not distributed between the two connections, hence I reverted this change.
```

```
ip firewall/mangle/set [find where dst-address-type~"!local"] !dst-address-type dst-address-list=LOCAL

---
```

## Response 8
1. What is the use of these two routes?
```
/ip route add gateway=8.8.8.8 distance=1 check-gateway=ping
/ip route add gateway=1.1.1.1 distance=2 check-gateway=pingAs you took the effort to monitor the transparency of both uplinks using the recursive next-hop search for the routes you use for load distribution, it seemed logical to me to do the same also for the own traffic of the Mikrotik. So if access to internet via pppoe-out1 breaks, the Mikrotik itself will still be able to talk to the internet. But if you inisist on using only pppoe-out1 for Mikrotik's own access to internet and don't mind that it loses access completely if that ISP has problems, you do not need those two routes and you can also set the default route distance back to 1 in the pppoe client settings. In most of my installations with more than one WAN I let the Mikrotik inform me about eventual issues so I automatically include its own traffic into the failover handling, so it is kind of an obvious thing to do for me.2. After modifying this, I was not able to use both connections simultaneously, i.e., the load was not distributed between the two connections, hence I reverted this change.
```

```
ip firewall/mangle/set [find where dst-address-type~"!local"] !dst-address-type dst-address-list=LOCALThat's because I forgot the exclamation mark before LOCAL. It should actually have read
```

```
ip firewall/mangle/set [find where dst-address-type~"!local"] !dst-address-type dst-address-list=!LOCALIn your current configuration, the only effect of this change would be that connections from LAN hosts towards Wireguard clients would not get misrouted via WAN. If you do not plan on using this type of connections, the rules can stay as they are.

---
```

## Response 9
I really appreciate your thorough reply. I learned something new today. You solved my issue in a day when the internet couldn't help me for weeks. ---

## Response 10
one more observation.after connection-mark=no-markfasttrack seems to be not working. CPU usage shoots up to 100% on high bandwidth utilization. whereas this was not the case previously. ---

## Response 11
Indeed, that's the price to pay for load distribution using mangle rules. By changing that toconnection-mark=!WAN2you can have 50 % of the traffic fasttracked, but you cannot fasttrack all connections.Instead of PCC mangle rules, you can use ECMP to distribute the LAN->internet traffic, as fasttracking skipsmanglerule processing but doesn't skiproutingrule processing. ---

## Response 12
then why does fasttrack+pcc works when I remove default route? ---

## Response 13
That's what I do not understand because such a configuration is so unusual that I have never tested it. ---

## Response 14
is this limited to OS v7 or the same in v6 also? ---

## Response 15
I really appreciate your thorough reply. I learned something new today. You solved my issue in a day when the internet couldn't help me for weeks.sindy 1internet: 0Go, sindy, go! ---

## Response 16
make it @sindy 2 - @internet 0and a cup of coffeefor @sindy as well@trextom, have a readviewtopic.php?t=142401@mkx and beloved mt members have solid discussion about pcc and fasttrack ---

## Response 17
is this limited to OS v7 or the same in v6 also?If you mean the fact that most fasttracked packets skip mangle rules, that was the case ever since fasttracking has been introduced, if not in ROS 5 then in early ROS 6, as skipping part of packet processing steps is the very essence of fasttracking.If you mean that fasttracking together with mangle did work for you while no route was present in table main, it would be an unusual configuration in both ROS 6 and ROS 7 so I haven't tested it in either of them.In fact the thing is even more complicated - when a connection begins, it takes some time until it reaches theestablishedstate, so the initial packet of the LAN->internet connection always takes the slow path, and so does the first response to it, at least until it passes throughpreroutingtofilter. So the choice of WAN for the whole connection is always done. Later, most packets belonging to the connection take the fast path, but some of them take the slow one so that the counters could be updated. So dependning on many factors, the result may vary from connections failing through very slow TCP connections to seemingly normal connections occupying the bandwidth of the primary WAN as per tablemainif the provider of that WAN does not care about source address. But all this is related to the case when there is a route inmain. If there is none, a packet without a routing mark assigned cannot get routed anywhere, so I still cannot see how it can work that way, I'll need to do some tests to find out.In general, you only need to usemanglerules to control routing in advanced scenarios; in simple ones, routingrules and ECMP routing, which are both compatible with fasttracking, are sufficient. Routing rules cannot take connection state, protocols, and ports into account, but that doesn't seem to be necessary in your setup as you said you only want to use one WAN for incoming connections. ECMP can only distribute the connections evenly among routes, i.e. you cannot say "send 3/4 of connections via WAN 1 and 1/4 via WAN 2" using ECMP. But your current PCC rules distribute connections evenly between both WANs, so replacing PCC by ECMP will cause no limitation.So I would place default routes via both WANs to a routing table namedxyz, both with the samedistancevalue (e.g.1), disable themark-routingrules in mangle, and use a singleroutingruleinterface=bridge action=lookup table=xyz. If that turns out to work the way you want, you can disable or remove all the mangle rules and remove the now uselessconnection-mark=no-markmatch condition from theaction=fasttrack-connectionrule. ---

## Response 18
and port forwarding is not working.update: fixed with the help of this thread.viewtopic.php?f=2&t=49581 ---

## Response 19
@trextom, and port forwarding is not working.update: fixed with the help of this thread. viewtopic.php?f=2&t=49581greatbut - no offense - which part of your problems has been fixed? pcc? fasttrack? port forwarding? ---

## Response 20
The thread fixed the issue with port forwarding. Previous posts fixed PCC and somewhat fasttrack. However, I'm still having an issue with fasttrack. ---

## Response 21
As always please post the full and most current config for review./export file=anynameyouwish ( minus router serial number, any public WANIP information, keys, long assed dhcp lease lists, unecessary and not used IPV6 crapola ) ---

## Response 22
edit- duplicate ---