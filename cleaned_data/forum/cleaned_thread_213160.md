# Thread Information
Title: Thread-213160
Section: RouterOS
Thread ID: 213160

# Discussion

## Initial Question
Hello, I am hoping to get some help from VLAN experts. Please see the diagram below. So my goal is to set up a VLAN on the Mikrotik 4011 to separate my IPTV traffic that I am receiving from the ISP Router's ETH4 to ETH5 on the 4011 router. The traffic is currently coming in untagged to the 4011 router but it comes tagged to the ISP router after which it is stripped of the tags. I have a Wireguard tunnel from the 4011 to a 5009 router which I use for my home network on the 5009 and an EOIP over Wireguard tunnel that I have in a bridge on both sides, on the 4011 with the inbound iptv multicast traffic coming from the ISP router and on the 5009 router it is outbound to ETH5, the IPTV STB which receives the multicast traffic and it's IP is received from the ISP router on connected to the 4011. The traffic is from other devices is mixing with the multicast traffic on the 4011 and that is why I would like to do this. Can anyone assist? ---

## Response 1
hello, I'm sorry we can't see your diagram in detail. it's too small and blurry.so... the bottom line is you want to have a setup similar to voice vlan? from 4011 to 5009 using eoip over wireguard? ---

## Response 2
You may need to enable the RTSP firewall helper for the IPTV. But if your using Spainish Movistar IPTV... I believe there are some issues IGMP proxy that block that from working.Also EOIP with WG is going to reduce the MTU, so I'm not 100% sure the IPTV packet fit over the lower MTU....so that may be another issue. ---

## Response 3
hello, I'm sorry we can't see your diagram in detail. it's too small and blurry.so... the bottom line is you want to have a setup similar to voice vlan? from 4011 to 5009 using eoip over wireguard?Sorry about that. Please see below. Yes, that is correct. When use torch on the interface, I am noticing all kinds of traffic from other devices on the network that are bogging down my multicast IPTV stream and it makes VOD content impossible to watch. ---

## Response 4
You may need to enable the RTSP firewall helper for the IPTV. But if your using Spainish Movistar IPTV... I believe there are some issues IGMP proxy that block that from working.Also EOIP with WG is going to reduce the MTU, so I'm not 100% sure the IPTV packet fit over the lower MTU....so that may be another issue.Hello. Thanks for your response. I do not know what you mean by RTSP firewall, I would need concrete config commands if possible, please.I'm not using Spanish Movistar IPTV or IGMP Proxy. It's just straight L2 bridging through the EOIP tunnel. It is Macedonian Telekom, most similar to Deutsche Telekom IPTV.I don't believe it's an MTU issue. Just seeing lots of devices on the interface with torch that should not be there at all, nothing to do with IPTV multicast. ---

## Response 5
@skhmm... aaa... you want to relay the iptv from isp1 to isp2?
```
isp1/iptv eoip ---> router1 --- eoip/wg --- router2 eoip ---> isp2/iptv??it's doable - but I don't know what will the quality be as it will travel via encrypted Tunnel. and first, let us not discuss about firewall.there are options - but first let us know whether that simple diagram is correct?

---
```

## Response 6
Just seeing lots of devices on the interface with torch that should not be there at all, nothing to do with IPTV multicast.If IPTV of Makedonski Telekom is anything similar to same thing of Telekom Slovenije, then VLAN for IPTV is switched for many IPTV customers ... and you will be able to see some traffic of other set top boxes (e.g. anything broadcasted, such as part of DHCP handshakes, etc.). And that part of traffic (which you can not control) will certainly mess with your wireguard bridge. ---

## Response 7
@skhmm... aaa... you want to relay the iptv from isp1 to isp2?
```
isp1/iptv eoip ---> router1 --- eoip/wg --- router2 eoip ---> isp2/iptv??it's doable - but I don't know what will the quality be as it will travel via encrypted Tunnel. and first, let us not discuss about firewall.there are options - but first let us know whether that simple diagram is correct?The diagram is correct and it works. I just need to separate the traffic on those eth ports from the rest of the network, like it is on the ISP router otherwise it bogs down the multicast traffic. I assume the best way to do this is a VLAN?

---
```

## Response 8
Just seeing lots of devices on the interface with torch that should not be there at all, nothing to do with IPTV multicast.If IPTV of Makedonski Telekom is anything similar to same thing of Telekom Slovenije, then VLAN for IPTV is switched for many IPTV customers ... and you will be able to see some traffic of other set top boxes (e.g. anything broadcasted, such as part of DHCP handshakes, etc.). And that part of traffic (which you can not control) will certainly mess with your wireguard bridge.I am seeing devices from my network on it, other devices that have nothing to do with it but they are on my network. Nothing else. I am not sure how it is with Slovenski Telekom..That is why I want to separate that traffic, same as it is on the ISP router. The traffic from the ISP router that goes to the IPTV STB is untagged when it comes to my Mikrotik 4011, I assume the ISP router removes the tags. I would like to retag it again with the 4011 so only traffic from that port goes through the EOIP tunnel and nothing else. Same thing when it gets to the 5009 router, I would like that eth5 port that is going to the IPTV STB to only get traffic from the eoip tunnel. ---

## Response 9
Can you set one of ISP router ports as trunk port? Routers, provided by Telekom Slovenije, have option to set each port as either "data", "IPTV" or "both" ... the later being trunk mode.This way you'll get IPTV already (natively) VLAN tagged (and internet probably untagged which is not a problem at all) ... and then you have to pass that VLAN via EOIP (over wireguard). No need to fuss with two ports towards ISP router. As long as both ends properly deal with VLANs, your LAN devices (which are not supposed to see IPTV network) won't see that traffic. ---

## Response 10
Can you set one of ISP router ports as trunk port? This way you'll get IPTV already (natively) VLAN tagged (and internet probably untagged which is not a problem at all) ... and then you have to pass that VLAN via EOIP (over wireguard). No need to fuss with two ports towards ISP router. As long as both ends properly deal with VLANs, your LAN devices (which are not supposed to see IPTV network) won't see that traffic.I cannot do that. There are no settings on the ISP router for such a thing. This is the only way I can do it, by emulating a physical connection and then transporting it via some tunnel. ---

## Response 11
@skaaa... I'm sorry i just realized that right part should go via internet.No need to fuss with two ports towards ISP router. As long as both ends properly deal with VLANs, your LAN devices (which are not supposed to see IPTV network) won't see that traffic.there you go... @mkx provided you with the details.hmm...1. make vlan 11, 12 for data and iptv and their corresponding physical ports (access mode).2. put the iptv eoip interface bridge member vlan12. the data interface is on vlan 113. put the eoip over wg interface bridge member of vlan 11, 12 (trunk mode). let the wg Interface as is.4. replicate mirror the config on router 2.5. don't forget to check some route.6. how about qinq or vxlan? ---

## Response 12
@skaaa... I'm sorry i just realized that right part should go via internet.No need to fuss with two ports towards ISP router. As long as both ends properly deal with VLANs, your LAN devices (which are not supposed to see IPTV network) won't see that traffic.there you go... @mkx provided you with the details.hmm...1. make vlan 11, 12 for data and iptv and their corresponding physical ports (access mode).2. put the iptv eoip interface bridge member vlan12. the data interface is on vlan 113. put the eoip over wg interface bridge member of vlan 11, 12 (trunk mode). let the wg Interface as is.4. replicate mirror the config on router 2.5. don't forget to check some route.6. how about qinq or vxlan?Can you please have concrete commands/steps that I need to do? This is not very understandable to me. What is the function of qinq or vxlan? ---

## Response 13
@skThe diagram is correct and it works. I just need to separate the traffic on those eth ports from the rest of the network, like it is on the ISP router otherwise it bogs down the multicast traffic. I assume the best way to do this is a VLAN?ok. let's break it down nice and slowly.you said currently it is in working state. can you give us your working config on both routers - so that we can analyze and adapt to your current working config?that ether 5 on 4011 - does it have any ip or nat? or just plain bridge ip and you bridge the eoip on that bridge? ---

## Response 14
@skThe diagram is correct and it works. I just need to separate the traffic on those eth ports from the rest of the network, like it is on the ISP router otherwise it bogs down the multicast traffic. I assume the best way to do this is a VLAN?ok. let's break it down nice and slowly.you said currently it is in working state. can you give us your working config on both routers - so that we can analyze and adapt to your current working config?that ether 5 on 4011 - does it have any ip or nat? or just plain bridge ip and you bridge the eoip on that bridge?Sure, please see the configs below. Eth5 on 4011 does not have an IP or NAT. Just plain bridge in which the EOIP is in it, the bridge does not have an IP set to it either. Please note the below config is with an EOIP over IKE2 from recently, I had this redacted config from before so I didn't want to have to do everything all over again just for switching the EOIP over WG. I can do it either way.Mikrotik 4011
```
# 2024-11-05 10:43:35 by RouterOS 7.16.1
# software id = (Redacted)
#
# model = RB4011iGS+
# serial number = (Redacted) 
/interface bridge
add disabled=yes name=br-EOIP
add disabled=yes name=br-OVPN
add name=br-VPN port-cost-mode=short
add admin-mac=(Redacted) auto-mac=no comment=defconf name=bridge-LAN
add name=bridge-loopback
/interface ethernet
set [ find default-name=ether1 ] name=ether1-WAN
set [ find default-name=ether2 ] name=ether2-VOIP-OUT
set [ find default-name=ether5 ] name=ether5-IPTV-IN
/interface eoip
add allow-fast-path=no local-address=10.0.88.1 mac-address=(Redacted) \
    name=eoip-tunnel-ike2 remote-address=10.0.88.3 tunnel-id=5
add disabled=yes mac-address=(Redacted) name=eoip-tunnel1 \
    remote-address=192.168.50.2 tunnel-id=1
/interface wireguard
add listen-port=13231 mtu=1412 name=wg1
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface lte apn
set [ find default=yes ] ip-type=ipv4 use-network-apn=no
/ip ipsec mode-config
add address=10.0.88.3 address-prefix-length=32 name=modeconf-ikev2-rb5009 \
    split-include=0.0.0.0/0 system-dns=no
/ip ipsec policy group
add name=IKEv2
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
add dh-group=modp4096 dpd-interval=15s enc-algorithm=aes-256 hash-algorithm=\
    sha256 name=ikev2 prf-algorithm=sha256
/ip ipsec peer
add exchange-mode=ike2 name=ikev2 passive=yes profile=ikev2
/ip ipsec proposal
set [ find default=yes ] enc-algorithms=aes-256-cbc,aes-192-cbc
add auth-algorithms=sha256 enc-algorithms=aes-256-cbc name=ikev2 pfs-group=\
    modp4096
/ip pool
add name=dhcp ranges=192.168.88.10-192.168.88.254
add name=l2tp-vpn ranges=192.168.89.2-192.168.89.255
add name=POOL-VPN ranges=10.10.0.1-10.10.0.255
add name=ovpn-pool ranges=192.168.77.10-192.168.77.20
add name=ikev2-pool ranges=10.0.88.2-10.0.88.254
/ip dhcp-server
add address-pool=dhcp interface=bridge-LAN lease-time=10m name=defconf
/ip ipsec mode-config
add address-pool=ikev2-pool address-prefix-length=32 name=modeconf-ikev2 \
    split-include=0.0.0.0/0 static-dns=10.0.88.1 system-dns=no
/ip smb users
set [ find default=yes ] disabled=yes
/port
set 0 name=serial0
set 1 name=serial1
/ppp profile
add bridge=br-VPN change-tcp-mss=yes local-address=192.168.89.1 name=l2tp \
    remote-address=l2tp-vpn use-ipv6=default
add bridge=br-OVPN local-address=192.168.77.1 name=ovpn remote-address=\
    ovpn-pool
set *FFFFFFFE bridge=br-VPN use-encryption=default use-ipv6=default use-upnp=\
    yes
/zerotier
set zt1 comment="ZeroTier Central controller - https://my.zerotier.com/" \
    disabled=yes disabled=yes name=zt1 port=9993
/zerotier interface
add allow-default=no allow-global=no allow-managed=yes disabled=yes instance=\
    zt1 name=zerotier1 network=(Redacted)
/interface bridge port
add bridge=bridge-LAN comment=defconf ingress-filtering=no interface=\
    ether2-VOIP-OUT
add bridge=bridge-LAN comment=defconf ingress-filtering=no interface=ether3
add bridge=bridge-LAN comment=defconf ingress-filtering=no interface=ether4
add bridge=br-VPN ingress-filtering=no interface=ether5-IPTV-IN
add bridge=bridge-LAN comment=defconf ingress-filtering=no interface=ether6
add bridge=bridge-LAN comment=defconf ingress-filtering=no interface=ether7
add bridge=bridge-LAN comment=defconf ingress-filtering=no interface=ether8
add bridge=bridge-LAN comment=defconf ingress-filtering=no interface=ether9
add bridge=bridge-LAN comment=defconf ingress-filtering=no interface=ether10
add bridge=bridge-LAN comment=defconf ingress-filtering=no interface=\
    sfp-sfpplus1
add bridge=br-EOIP interface=eoip-tunnel1
add bridge=bridge-loopback interface=eoip-tunnel-ike2
/ip firewall connection tracking
set udp-timeout=1m
/ip neighbor discovery-settings
set discover-interface-list=LAN
/ipv6 settings
set disable-ipv6=yes max-neighbor-entries=8192
/interface detect-internet
set detect-interface-list=WAN
/interface l2tp-server server
set authentication=mschap2 default-profile=l2tp enabled=yes mrru=1600 \
    use-ipsec=yes
/interface list member
add comment=defconf interface=bridge-LAN list=LAN
add comment=defconf interface=ether1-WAN list=WAN
add interface=wg1 list=LAN
/interface ovpn-server server
set auth=sha1 certificate=server cipher=aes256-cbc default-profile=ovpn \
    enabled=yes mode=ethernet port=443 require-client-certificate=yes
/interface pptp-server server
# PPTP connections are considered unsafe, it is suggested to use a more modern VPN protocol instead
set default-profile=*4 mrru=1600
/interface sstp-server server
set port=4430
/interface wireguard peers
add allowed-address=192.168.50.2/32,192.168.98.0/24,192.168.99.0/24 comment=\
    "to the home router" interface=wg1 name=peer1 private-key=\
    "(Redacted)" public-key=\
    "(Redacted)"
add allowed-address=192.168.50.101/32 comment="iPhone" interface=wg1 \
    name=peer2 private-key="(Redacted)" \
    public-key="(Redacted)"
add allowed-address=192.168.50.102/32 comment=DDD interface=wg1 name=peer3 \
    private-key="(Redacted)" public-key=\
    "(Redacted)"
add allowed-address=192.168.50.105/32 comment=KE interface=wg1 name=peer5 \
    private-key="(Redacted)" public-key=\
    "(Redacted)"
add allowed-address=192.168.50.110/32 comment=Z-Fold4 interface=wg1 \
    name=peer6 private-key="(Redacted)" \
    public-key="(Redacted)"
add allowed-address=192.168.50.3/32,192.168.188.0/24,192.168.199.0/24 \
    comment="Mikrotik LTE6 Travel Router" interface=wg1 name=peer8 \
    public-key="(Redacted)"
add allowed-address=192.168.50.4/32 comment="Mudi Travel Router" interface=\
    wg1 name=peer12 private-key=\
    "(Redacted)" public-key=\
    "(Redacted)"
/ip address
add address=192.168.88.1/24 comment=defconf interface=bridge-LAN network=\
    192.168.88.0
add address=192.168.50.1/24 interface=wg1 network=192.168.50.0
add address=172.16.0.1/30 interface=eoip-tunnel-ike2 network=172.16.0.0
add address=10.0.88.1/24 interface=bridge-loopback network=10.0.88.0
/ip cloud
set ddns-enabled=yes
/ip dhcp-client
add comment=defconf interface=ether1-WAN
/ip dhcp-server lease
add address=192.168.88.7 client-id=(Redacted) mac-address=\
    (Redacted) server=defconf
/ip dhcp-server network
add address=192.168.88.0/24 comment=defconf dns-server=192.168.88.1 gateway=\
    192.168.88.1
/ip dns
set allow-remote-requests=yes
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
/ip firewall address-list
add address=192.168.89.0/24 list=L2TP
add address=Redacted list=Trusted
add address=Redacted list=Trusted
add address=Redacted list=Trusted
add address=Redacted list=Trusted
add address=(Redacted) list=Trusted
add address=192.168.50.0/24 list=Trusted
/ip firewall filter
# zerotier1 not ready
# zerotier1 not ready
add action=accept chain=forward in-interface=zerotier1
# zerotier1 not ready
# zerotier1 not ready
add action=accept chain=input in-interface=zerotier1
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=forward comment="For TESTS" disabled=yes dst-address=\
    192.168.98.0/24
add action=accept chain=forward disabled=yes dst-address=8.8.8.8 log=yes \
    src-address=192.168.99.0/24
add action=accept chain=forward disabled=yes log=yes src-address=8.8.8.8
add action=accept chain=input comment="Allow WireGuard traffic" src-address=\
    192.168.50.0/24
add action=accept chain=input comment="Allow EOIP Traffic" src-address=\
    172.16.0.0/30
add action=accept chain=input dst-port=2000 protocol=tcp
add action=accept chain=input dst-port=8291 in-interface-list=WAN protocol=\
    tcp src-address-list=Trusted
add action=accept chain=input comment="Accept GRE" protocol=gre
add action=accept chain=input comment="Allow Winbox" dst-port=8291 \
    in-interface=ether1-WAN protocol=tcp
add action=accept chain=input comment=WG dst-port=13231 in-interface=\
    ether1-WAN protocol=udp
add action=accept chain=input dst-port=500 protocol=tcp
add action=accept chain=input protocol=ipsec-esp
add action=accept chain=input protocol=ipsec-ah
add action=accept chain=input comment="allow l2tp" dst-port=1701 protocol=udp
add action=accept chain=input comment="Allow L2TP TCP" dst-port=1701 \
    protocol=tcp
add action=accept chain=input dst-port=4500 protocol=tcp
add action=accept chain=input comment="allow IPsec NAT" dst-port=4500 \
    protocol=udp
add action=accept chain=input comment="allow IKE" dst-port=500 protocol=udp
add action=accept chain=input protocol=ipsec-esp
add action=accept chain=forward comment="defconf: accept in ipsec policy" \
    ipsec-policy=in,ipsec
add action=accept chain=forward comment="defconf: accept out ipsec policy" \
    ipsec-policy=out,ipsec
add action=accept chain=input comment="Allow OpenVPN Traffic" dst-port=1194 \
    in-interface=ether1-WAN protocol=tcp
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=accept chain=input comment="accept requests to mikrotik from vpn" \
    src-address-list=L2TP
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment=\
    "defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=drop chain=input comment="defconf: drop all not coming from LAN" \
    in-interface-list=!LAN
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
add action=accept chain=input dst-port=80,443 in-interface=all-ppp protocol=\
    tcp
/ip firewall mangle
add action=change-mss chain=forward disabled=yes new-mss=1400 out-interface=\
    wg1 passthrough=yes protocol=tcp tcp-flags=syn
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat comment="masq. vpn traffic" disabled=yes \
    out-interface=br-VPN src-address=192.168.89.0/24
add action=dst-nat chain=dstnat disabled=yes in-interface=ether5-IPTV-IN log=\
    yes to-addresses=192.168.50.1
/ip ipsec identity
add auth-method=digital-signature certificate=4011-ike2-server \
    generate-policy=port-strict match-by=certificate mode-config=\
    modeconf-ikev2-rb5009 peer=ikev2 policy-template-group=IKEv2 \
    remote-certificate=rb5009-ike2
/ip ipsec policy
add dst-address=10.0.88.0/24 group=IKEv2 proposal=ikev2 src-address=0.0.0.0/0 \
    template=yes
/ip route
add disabled=no dst-address=192.168.98.0/24 gateway=wg1 routing-table=main \
    suppress-hw-offload=no
add disabled=no distance=1 dst-address=192.168.99.0/24 gateway=wg1 pref-src=\
    "" routing-table=main scope=30 suppress-hw-offload=no target-scope=10
add disabled=no dst-address=192.168.188.0/24 gateway=wg1 routing-table=main \
    suppress-hw-offload=no
add disabled=no dst-address=192.168.199.0/24 gateway=wg1 routing-table=main \
    suppress-hw-offload=no
add disabled=no distance=1 dst-address=192.168.95.0/24 gateway=\
    eoip-tunnel-ike2 routing-table=main scope=30 suppress-hw-offload=no \
    target-scope=10
/ip service
set telnet disabled=yes
set www-ssl address=192.168.89.0/24 disabled=no
/ip smb shares
set [ find default=yes ] directory=/pub
/ip ssh
set always-allow-password-login=yes forwarding-enabled=both
/ip upnp
set enabled=yes
/ppp profile
add bridge=*10 local-address=10.10.0.0 name="SITE TO SITE L2VPN" \
    remote-address=POOL-VPN
/ppp secret
add name=vpn
add local-address=1.1.1.5 name=sstp1 remote-address=1.1.1.6
add local-address=192.168.12.1 name=mikrotik remote-address=192.168.12.2 \
    service=l2tp
add name=mikrotik-bcp profile="SITE TO SITE L2VPN" service=l2tp
add name=bcp profile="SITE TO SITE L2VPN" service=l2tp
add name=l2tp profile=default-encryption
add name=iphone profile=l2tp
add name=ovpnclient profile=ovpn
add comment="Mikrotik LTE6 Travel Router" name=l2tp1 profile=\
    default-encryption
/routing bfd configuration
add disabled=no interfaces=all min-rx=200ms min-tx=200ms multiplier=5
/routing igmp-proxy
set quick-leave=yes
/routing igmp-proxy interface
add alternative-subnets="172.16.0.0/16,172.26.0.0/16,(Redacted)/(Redacted)/28,(Redacted)/28,(Redacted)/16,0.0.0.0/0" disabled=yes \
    interface=ether5-IPTV-IN upstream=yes
add disabled=yes interface=wg1
/system clock
set time-zone-name=Europe
/system identity
set name=4011
/system logging
add disabled=yes topics=ipsec
/system note
set note="Test
/system ntp client
set enabled=yes
/system ntp client servers
add address=0.europe.pool.ntp.org
add address=1.europe.pool.ntp.org
/system routerboard settings
# Firmware upgraded successfully, please reboot for changes to take effect!
set auto-upgrade=yes
/tool graphing interface
add
/tool graphing resource
add
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN
/tool romon
set enabled=yes
/tool sniffer
set filter-interface=wg1 filter-stream=yes only-headers=yes \
    streaming-enabled=yes streaming-server=(Redacted)Mikrotik 5009
```

```
# 2024-11-05 11:00:48 by RouterOS 7.16.1
# software id = (Redacted)
#
# model = RB5009UG+S+
# serial number = (Redacted)
/interface bridge
add fast-forward=no name=br-EOIP
add disabled=yes name=br-OVPN
add name=br-VPN
add name=br_PBR port-cost-mode=short
add admin-mac=(Redacted) auto-mac=no comment=defconf name=bridge \
    port-cost-mode=short
/interface ethernet
set [ find default-name=ether1 ] name=ether1-WAN
set [ find default-name=ether2 ] name=ether2-LAN
set [ find default-name=ether3 ] name=ether3-WG-LAN
set [ find default-name=ether4 ] name=ether4-VOIP
set [ find default-name=ether5 ] name="ether5-IPTV STB"
set [ find default-name=ether8 ] comment="WAN2 MAN"
/interface l2tp-client
add connect-to=(Redacted) disabled=no name=l2tp-out1 use-ipsec=\
    yes user=l2tp
/interface eoip
add allow-fast-path=no local-address=10.0.88.3 mac-address=(Redacted) \
    name=eoip-tunnel-ike2 remote-address=10.0.88.1 tunnel-id=5
add disabled=yes mac-address=(Redacted) name=eoip-tunnel1 \
    remote-address=192.168.50.1 tunnel-id=1
/interface wireguard
add disabled=yes listen-port=13232 mtu=1420 name=DDD
add listen-port=13231 mtu=1412 name=wg1
/interface vlan
add interface=ether8 name=man vlan-id=2
add comment=WAN2 interface=ether8 name=net vlan-id=3
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface lte apn
set [ find default=yes ] ip-type=ipv4 use-network-apn=no
/interface wifi channel
add disabled=no frequency=2412 name="CH 1 (2412)" width=20mhz
add disabled=no frequency=2437 name="CH 6 (2437)" width=20mhz
add disabled=no frequency=2462 name="CH 11 (2462)" width=20mhz
add disabled=no frequency=5180 name="CH 36 (5180)" width=20/40/80mhz
add disabled=no frequency=5260 name="CH 52 (5260)" width=20/40/80mhz
add disabled=no frequency=5500 name="CH 100 (5500)" width=20/40/80mhz
add disabled=no frequency=5680 name="CH 136 (5680)" width=20/40/80mhz
/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk disabled=no ft=yes ft-over-ds=yes \
    name=sec1 wps=disable
/interface wifi configuration
add channel="CH 1 (2412)" channel.frequency=2412 country="North Macedonia" \
    disabled=no mode=ap name=AP1-2412 security=sec1 ssid=DOMA tx-power=8
add channel="CH 6 (2437)" channel.frequency=2437 country="North Macedonia" \
    disabled=no mode=ap name=AP2-2437 security=sec1 ssid=DOMA tx-power=9
add channel="CH 11 (2462)" channel.frequency=2462 country="North Macedonia" \
    disabled=no mode=ap name=AP3-2462 security=sec1 ssid=DOMA tx-power=19
add channel="CH 36 (5180)" channel.frequency=5180 country="North Macedonia" \
    disabled=no mode=ap name=AP1-5180 security=sec1 ssid=DOMA tx-power=17
add channel="CH 52 (5260)" channel.frequency=5260 country="North Macedonia" \
    disabled=no mode=ap name=AP2-5260 security=sec1 ssid=DOMA tx-power=13
add channel="CH 100 (5500)" channel.frequency=5500 country="North Macedonia" \
    disabled=no mode=ap name=AP3-5500 security=sec1 ssid=DOMA tx-power=13
/interface wifi
add configuration=AP3-5500 disabled=no name=cAP-ax-Bedroom-wifi radio-mac=\
    (Redacted)
add configuration=AP3-2462 disabled=no name=cAP-ax-Bedroom-wifi2 radio-mac=\
    (Redacted)
add configuration=AP1-2412 disabled=no name=hAP-ax-dnevna-wifi radio-mac=\
    (Redacted)
add configuration=AP1-5180 disabled=no name=hAP-ax-dnevna-wifi2 radio-mac=\
    (Redacted)
add configuration=AP2-2437 disabled=no name=hAp-ax2-Office-wifi radio-mac=\
    (Redacted)
add configuration=AP2-5260 disabled=no name=hAp-ax2-Office-wifi2 radio-mac=\
    (Redacted)
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip ipsec policy group
add name=ikev2
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
add dh-group=modp4096 enc-algorithm=aes-256 hash-algorithm=sha256 name=ikev2 \
    prf-algorithm=sha256
/ip ipsec peer
add address=(Redacted) exchange-mode=ike2 name=ikev2 profile=\
    ikev2
/ip ipsec proposal
add auth-algorithms=sha256 enc-algorithms=aes-256-cbc name=ikev2 pfs-group=\
    modp4096
/ip pool
add name=dhcp ranges=192.168.98.10-192.168.98.254
add name=dhcp_pool2 ranges=192.168.99.10-192.168.99.254
add name=dhcp_pool3_eoip ranges=192.168.95.10-192.168.95.254
/ip dhcp-server
add address-pool=dhcp interface=bridge lease-time=10m name=defconf
add address-pool=dhcp_pool2 interface=br_PBR lease-time=10m name=dhcp2
add address-pool=dhcp_pool3_eoip interface=br-EOIP name=dhcp_server_eoip
/ip smb users
set [ find default=yes ] disabled=yes
/ppp profile
add bridge=br-OVPN change-tcp-mss=yes name=OVPN use-ipv6=default
set *FFFFFFFE bridge=br-VPN use-encryption=default use-ipv6=default
/interface ovpn-client
add certificate=cert_export_client.crt_0 cipher=aes256-cbc connect-to=\
    (Redacted) disabled=yes mac-address=(Redacted) mode=\
    ethernet name=ovpn-out1 profile=OVPN user=ovpnclient
/queue simple
add max-limit=15M/200M name="ALL TRAFFIC" target=192.168.99.0/24
add max-limit=10M/50M name="MaxTV Android Box" parent="ALL TRAFFIC" priority=\
    1/1 target=192.168.99.21/32
add max-limit=3M/10M name="Asus Router" parent="ALL TRAFFIC" target=\
    192.168.99.155/32
/queue type
add kind=fq-codel name=fq_qodel-default
add cake-autorate-ingress=yes kind=cake name=cake
/queue tree
add bucket-size=0.01 disabled=yes max-limit=200M name=DOWN packet-mark=\
    WG-PACKET parent=global queue=default
add disabled=yes name="1. VOIP" packet-mark=VOIP parent=DOWN priority=1 \
    queue=default
add disabled=yes name="2. MAXTV" packet-mark=MaxTV parent=DOWN priority=2 \
    queue=default
add disabled=yes name="2. DNS" packet-mark=DNS parent=DOWN priority=2 queue=\
    default
add disabled=yes name="3. ACK" packet-mark=ACK parent=DOWN priority=3 queue=\
    default
add disabled=yes name="4. UDP" packet-mark=UDP parent=DOWN priority=3 queue=\
    default
add disabled=yes name="5. ICMP" packet-mark=ICMP parent=DOWN priority=4 \
    queue=default
add disabled=yes name="6. HTTP" packet-mark=HTTP parent=DOWN priority=5 \
    queue=default
add disabled=yes name="7. HTTP_BIG" packet-mark=HTTP_BIG parent=DOWN \
    priority=6 queue=default
add disabled=yes name="8. QUIC" packet-mark=QUIC parent=DOWN priority=7 \
    queue=default
add disabled=yes name="9. OTHER" packet-mark=OTHER parent=DOWN queue=default
add bucket-size=0.01 disabled=yes max-limit=15M name=UP packet-mark=\
    WG-PACKET-UP parent=wg1 queue=default
add disabled=yes name="1. VOIP_" packet-mark=VOIP parent=UP priority=1 queue=\
    default
add disabled=yes name="2. DNS_" packet-mark=DNS parent=UP priority=2 queue=\
    default
add disabled=yes name="3. ACK_" packet-mark=ACK parent=UP priority=3 queue=\
    default
add disabled=yes name="4. UDP_" packet-mark=UDP parent=UP priority=3 queue=\
    default
add disabled=yes name="5. ICMP_" packet-mark=ICMP parent=UP priority=4 queue=\
    default
add disabled=yes name="6. HTTP_" packet-mark=HTTP parent=UP priority=5 queue=\
    default
add disabled=yes name="7. HTTP_BIG_" packet-mark=HTTP_BIG parent=UP priority=\
    6 queue=default
add disabled=yes name="8. QUIC_" packet-mark=QUIC parent=UP priority=7 queue=\
    default
add disabled=yes name="9. OTHER_" packet-mark=OTHER parent=UP queue=default
add disabled=yes max-limit=15M name=cake-queue-upload parent=wg1 queue=cake
add disabled=yes name=cake-queue-download parent=wg1 queue=cake
add disabled=yes name="MaxTV Android Box" packet-mark=MAXTV-AndroidBox \
    parent=DOWN priority=2 queue=default
/routing bgp template
set default disabled=no output.network=bgp-networks
/routing ospf instance
add disabled=no name=default-v2
/routing ospf area
add disabled=yes instance=default-v2 name=backbone-v2
/routing table
add disabled=no fib name=wg
add disabled=no fib name=eoip
/zerotier
set zt1 comment="ZeroTier Central controller - https://my.zerotier.com/" \
    disabled=yes disabled=yes name=zt1 port=9993
/zerotier interface
add allow-default=no allow-global=no allow-managed=yes disabled=yes instance=\
    zt1 name=zerotier1 network=(Redacted)
/interface bridge port
add bridge=br_PBR comment=defconf ingress-filtering=no interface=ether2-LAN \
    internal-path-cost=10 path-cost=10
add bridge=br_PBR comment=defconf ingress-filtering=no interface=\
    ether3-WG-LAN internal-path-cost=10 path-cost=10
add bridge=br_PBR comment=defconf ingress-filtering=no interface=ether4-VOIP \
    internal-path-cost=10 path-cost=10
add bridge=br-VPN comment=defconf ingress-filtering=no interface=\
    "ether5-IPTV STB" internal-path-cost=10 path-cost=10
add bridge=br-OVPN disabled=yes interface=eoip-tunnel1
add bridge=br_PBR interface=ether6
add bridge=br_PBR interface=man
add bridge=br_PBR interface=ether7
/ip firewall connection tracking
set udp-timeout=1m
/ip neighbor discovery-settings
set discover-interface-list=all
/ipv6 settings
set disable-ipv6=yes max-neighbor-entries=8192
/interface detect-internet
set detect-interface-list=WAN
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=ether1-WAN list=WAN
add interface=wg1 list=LAN
add comment=defconf interface=br_PBR list=LAN
add comment=defconf interface=net list=WAN
add interface=man list=LAN
add interface=eoip-tunnel-ike2 list=LAN
add interface=br-EOIP list=LAN
/interface ovpn-server server
set auth=sha1,md5
/interface wifi capsman
set enabled=yes package-path=/ require-peer-certificate=no upgrade-policy=\
    none
/interface wifi configuration
add country="North Macedonia" disabled=yes mode=ap name=cfg1 \
    security.authentication-types=wpa2-psk,wpa3-psk .encryption=ccmp,gcmp \
    .ft=yes .ft-over-ds=yes ssid=(Redacted) steering=*1
/interface wifi provisioning
add action=create-dynamic-enabled disabled=yes master-configuration=cfg1
add action=create-enabled disabled=no master-configuration=AP1-2412 \
    name-format=%I-wifi radio-mac=(Redacted)
add action=create-enabled disabled=no master-configuration=AP2-2437 \
    name-format=%I-wifi radio-mac=(Redacted)
add action=create-enabled disabled=no master-configuration=AP3-2462 \
    name-format=%I-wifi radio-mac=(Redacted)
add action=create-enabled disabled=no master-configuration=AP1-5180 \
    name-format=%I-wifi radio-mac=(Redacted)
add action=create-enabled disabled=no master-configuration=AP2-5260 \
    name-format=%I-wifi radio-mac=(Redacted)
add action=create-enabled disabled=no master-configuration=AP3-5500 \
    name-format=%I-wifi radio-mac=(Redacted)
/interface wireguard peers
add allowed-address="0.0.0.0/0,192.168.50.0/24,192.168.88.0/24,172.16.0.0/16,1\
    (Redacted)/16,(Redacted)/28,(Redacted)/28" endpoint-address=\
    (Redacted) endpoint-port=13231 interface=wg1 name=peer8 \
    persistent-keepalive=25s public-key=\
    "(Redacted)"
add allowed-address=192.168.60.0/24 disabled=yes endpoint-address=\
    188.168.138.126 endpoint-port=13232 interface=DDD name=peer12 \
    persistent-keepalive=1s private-key=\
    "(Redacted)" public-key=\
    "(Redacted)"
/ip address
add address=192.168.98.1/24 comment=defconf interface=bridge network=\
    192.168.98.0
add address=192.168.50.2/24 interface=wg1 network=192.168.50.0
add address=192.168.99.1/24 interface=br_PBR network=192.168.99.0
add address=192.168.60.2/24 interface=DDD network=192.168.60.0
add address=172.16.0.2 interface=eoip-tunnel-ike2 network=172.16.0.1
add address=192.168.95.1/24 interface=br-EOIP network=192.168.95.0
/ip cloud
set ddns-enabled=yes
/ip dhcp-client
add add-default-route=no interface=ether1-WAN use-peer-dns=no
add add-default-route=no disabled=yes interface=br-VPN
add add-default-route=no disabled=yes interface=ether8 use-peer-dns=no
add add-default-route=no comment=WAN2 interface=net script=":if (\$bound=1) do\
    ={\
    \n/ip route add distance=1 gateway=\$\"gateway-address\" dst-address=\"8.8\
    .4.4\" scope=30 target-scope=10 comment=\"ISP2\"\
    \n/ip route add distance=4 gateway=\"8.8.4.4\" check-gateway=ping scope=30\
    \_target-scope=32 comment=\"ISP2\"\
    \n} else={\
    \n/ip route remove [/ip route find comment=\"ISP2\"]\
    \n} " use-peer-dns=no
/ip dhcp-server lease
add address=192.168.99.7 client-id=(Redacted) comment=\
    "Grandstream HT801" mac-address=(Redacted) server=dhcp2
add address=192.168.99.183 client-id=(Redacted) comment=\
    "Alienware PC" mac-address=(Redacted) server=dhcp2
add address=192.168.99.151 client-id=(Redacted) mac-address=\
    (Redacted) server=dhcp2
add address=192.168.99.155 client-id=(Redacted) comment=\
    "ASUS Router" mac-address=(Redacted) server=dhcp2
add address=192.168.99.190 client-id=(Redacted) comment=\
    "AVM Fritz Powerline 1260" mac-address=(Redacted) server=dhcp2
add address=192.168.99.91 client-id=(Redacted) comment=PS5 \
    mac-address=(Redacted) server=dhcp2
add address=192.168.99.21 client-id=(Redacted) comment=\
    MAXTV-Android-Box mac-address=(Redacted) server=dhcp2
add address=192.168.99.14 client-id=(Redacted) comment=SONY-TV-77 \
    mac-address=(Redacted) server=dhcp2
add address=192.168.99.169 mac-address=(Redacted) server=dhcp2
add address=192.168.99.35 comment="Motorola Nettvplus" mac-address=\
    (Redacted) server=dhcp2
add address=192.168.99.23 client-id=(Redacted) mac-address=\
    (Redacted) server=dhcp2
add address=192.168.99.20 client-id=(Redacted) mac-address=\
    (Redacted) server=dhcp2
add address=192.168.99.42 client-id=(Redacted) comment=\
    "Ubiquiti Switch" mac-address=(Redacted) server=dhcp2
/ip dhcp-server network
add address=192.168.95.0/24 comment=br_eoip_network dns-server=192.168.95.1 \
    gateway=192.168.95.1
add address=192.168.98.0/24 comment=defconf dns-server=192.168.98.1 gateway=\
    192.168.98.1
add address=192.168.99.0/24 dns-server=192.168.99.1 gateway=192.168.99.1
/ip dns
set allow-remote-requests=yes servers=192.168.50.1
/ip dns static
add address=192.168.88.1 comment=defconf disabled=yes name=router.lan type=A
add address=192.168.50.1 disabled=yes name=mk.wg type=A
/ip firewall address-list
add address=192.168.98.0/24 list=local
add address=192.168.50.0/24 list=Trusted
add address=(Redacted) list=Trusted
add address=192.168.60.0/24 list=Trusted
/ip firewall filter
add action=fasttrack-connection chain=forward comment="defconf: fasttrack" \
    connection-state=established,related disabled=yes hw-offload=yes
add action=drop chain=output comment="TEST WAN1 Failover to WAN2" disabled=\
    yes dst-address=8.8.8.8
add action=accept chain=forward connection-state=established,related
add action=accept chain=input dst-port=8291 in-interface-list=WAN protocol=\
    tcp src-address-list=Trusted
add action=accept chain=input src-address-list=Trusted
add action=accept chain=forward disabled=yes in-interface=zerotier1
add action=accept chain=input disabled=yes in-interface=zerotier1
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment="Accept IGMP" in-interface=br-VPN \
    protocol=udp
add action=accept chain=forward comment="Forward IGMP" in-interface=br-VPN \
    protocol=udp
add action=accept chain=input comment="Accept GRE" protocol=gre
add action=accept chain=input in-interface-list=WAN protocol=ipsec-esp
add action=accept chain=input in-interface-list=WAN protocol=ipsec-ah
add action=accept chain=input dst-port=500 in-interface-list=WAN protocol=tcp
add action=accept chain=input dst-port=4500 in-interface-list=WAN protocol=\
    tcp
add action=accept chain=forward comment="defconf: accept in ipsec policy" \
    ipsec-policy=in,ipsec
add action=accept chain=forward comment="defconf: accept out ipsec policy" \
    ipsec-policy=out,ipsec
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment=\
    "defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=drop chain=input comment="defconf: drop all not coming from LAN" \
    in-interface-list=!LAN
add action=accept chain=forward comment=\
    "defconf: accept established,related, untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \
    connection-state=new in-interface-list=WAN
/ip firewall mangle
add action=change-mss chain=forward disabled=yes new-mss=1300 out-interface=\
    wg1 passthrough=yes protocol=tcp tcp-flags=syn tcp-mss=1301-65535
add action=mark-routing chain=prerouting disabled=yes in-interface=br-VPN \
    log=yes new-routing-mark=wg passthrough=yes
add action=change-mss chain=forward comment="WG Required Rule (First One)" \
    disabled=yes new-mss=1352 passthrough=yes protocol=tcp tcp-flags=syn,rst \
    tcp-mss=1353-65535
add action=change-mss chain=forward comment="WG Required Rule 1/2" disabled=\
    yes new-mss=clamp-to-pmtu out-interface=wg1 passthrough=no protocol=tcp \
    tcp-flags=syn
add action=change-mss chain=forward comment="WG Required Rule 2/2" new-mss=\
    clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=syn
add action=change-mss chain=forward comment="Change MSS on L2TP bridge" \
    disabled=yes new-mss=clamp-to-pmtu out-interface=br-VPN passthrough=yes \
    protocol=tcp tcp-flags=syn
add action=change-mss chain=forward disabled=yes new-mss=1380 passthrough=yes \
    protocol=tcp tcp-flags=syn tcp-mss=1381-65535
add action=mark-connection chain=forward comment=WG-Down-Conn disabled=yes \
    in-interface=wg1 new-connection-mark=WG-CONN passthrough=yes
add action=mark-packet chain=forward comment=WG-Down-Packet connection-mark=\
    WG-CONN disabled=yes new-packet-mark=WG-PACKET passthrough=yes
add action=mark-connection chain=prerouting comment=WG-Up-Conn disabled=yes \
    in-interface=br_PBR new-connection-mark=WG-UP-CONN passthrough=yes
add action=mark-packet chain=prerouting comment=WG-Up-Packet connection-mark=\
    WG-UP-CONN disabled=yes new-packet-mark=WG-PACKET-UP passthrough=yes
add action=mark-connection chain=prerouting comment=L2TP-Marking disabled=yes \
    in-interface=br-VPN new-connection-mark=L2TP-CONN passthrough=yes
add action=mark-packet chain=prerouting connection-mark=L2TP-CONN disabled=\
    yes new-packet-mark=MaxTV passthrough=no
add action=mark-packet chain=forward comment="MaxTV Android Box" \
    connection-mark=WG-CONN disabled=yes dst-address=192.168.99.21 \
    new-packet-mark=MAXTV-AndroidBox passthrough=no
add action=mark-connection chain=prerouting comment=DNS connection-state=new \
    disabled=yes new-connection-mark=DNS passthrough=yes port=53 protocol=udp
add action=mark-packet chain=prerouting connection-mark=DNS disabled=yes \
    new-packet-mark=DNS passthrough=no
add action=mark-connection chain=postrouting connection-state=new disabled=\
    yes new-connection-mark=DNS passthrough=yes port=53 protocol=udp
add action=mark-packet chain=postrouting connection-mark=DNS disabled=yes \
    new-packet-mark=DNS passthrough=no
add action=mark-connection chain=prerouting comment=VOIP disabled=yes \
    new-connection-mark=VOIP passthrough=yes port=5060-5062,8560,10000-10050 \
    protocol=udp
add action=mark-packet chain=prerouting connection-mark=VOIP disabled=yes \
    new-packet-mark=VOIP passthrough=no
add action=mark-connection chain=prerouting comment=QUIC connection-state=new \
    disabled=yes new-connection-mark=QUIC passthrough=yes port=80,443 \
    protocol=udp
add action=mark-packet chain=prerouting connection-mark=QUIC disabled=yes \
    new-packet-mark=QUIC passthrough=no
add action=mark-connection chain=prerouting comment=UDP connection-state=new \
    disabled=yes new-connection-mark=UDP passthrough=yes protocol=udp
add action=mark-packet chain=prerouting connection-mark=UDP disabled=yes \
    new-packet-mark=UDP passthrough=no
add action=mark-connection chain=prerouting comment=ICMP connection-state=new \
    disabled=yes new-connection-mark=ICMP passthrough=yes protocol=icmp
add action=mark-packet chain=prerouting connection-mark=ICMP disabled=yes \
    new-packet-mark=ICMP passthrough=no
add action=mark-connection chain=postrouting connection-state=new disabled=\
    yes new-connection-mark=ICMP passthrough=yes protocol=icmp
add action=mark-packet chain=postrouting connection-mark=ICMP disabled=yes \
    new-packet-mark=ICMP passthrough=no
add action=mark-packet chain=postrouting comment=ACK disabled=yes \
    new-packet-mark=ACK packet-size=0-123 passthrough=no protocol=tcp \
    tcp-flags=ack
add action=mark-packet chain=prerouting disabled=yes new-packet-mark=ACK \
    packet-size=0-123 passthrough=no protocol=tcp tcp-flags=ack
add action=mark-connection chain=prerouting comment=HTTP connection-mark=\
    no-mark connection-state=new disabled=yes new-connection-mark=HTTP \
    passthrough=yes port=80,443 protocol=tcp
add action=mark-connection chain=prerouting connection-bytes=5000000-0 \
    connection-mark=HTTP connection-rate=2M-100M disabled=yes \
    new-connection-mark=HTTP_BIG passthrough=yes protocol=tcp
add action=mark-packet chain=prerouting connection-mark=HTTP_BIG disabled=yes \
    new-packet-mark=HTTP_BIG passthrough=no
add action=mark-packet chain=prerouting connection-mark=HTTP disabled=yes \
    new-packet-mark=HTTP passthrough=no
add action=mark-connection chain=prerouting comment=OTHER connection-state=\
    new disabled=yes new-connection-mark=POP3 passthrough=yes port=\
    995,465,587 protocol=tcp
add action=mark-packet chain=prerouting connection-mark=POP3 disabled=yes \
    new-packet-mark=OTHER passthrough=no
add action=mark-connection chain=prerouting connection-mark=no-mark disabled=\
    yes new-connection-mark=OTHER passthrough=yes
add action=mark-packet chain=prerouting connection-mark=OTHER disabled=yes \
    new-packet-mark=OTHER passthrough=no
add action=mark-packet chain=prerouting connection-mark=WG-UP-CONN disabled=\
    yes new-packet-mark=MaxTV-AndroidBox-Up passthrough=yes src-address=\
    192.168.99.21
/ip firewall nat
add action=masquerade chain=srcnat disabled=yes out-interface=lo
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat disabled=yes out-interface=br_PBR
add action=masquerade chain=srcnat disabled=yes out-interface=wg1
/ip firewall raw
add action=drop chain=output disabled=yes dst-address=8.8.4.4 src-address=\
    192.168.120.0/24
/ip ipsec identity
add auth-method=digital-signature certificate=rb5009-ike2 generate-policy=\
    port-strict match-by=certificate mode-config=request-only peer=ikev2 \
    policy-template-group=ikev2 remote-certificate=\
    4011-ike2-server.crt_0
/ip ipsec policy
add comment="ike2 policy template" dst-address=0.0.0.0/0 group=ikev2 \
    proposal=ikev2 src-address=10.0.88.0/24 template=yes
/ip route
add disabled=no distance=1 dst-address=192.168.88.0/24 gateway=wg1 \
    routing-table=main scope=10 suppress-hw-offload=no
add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=wg1 pref-src="" \
    routing-table=wg scope=30 suppress-hw-offload=no target-scope=10
add disabled=no distance=1 dst-address=192.5.5.241/32 gateway=192.168.3.1 \
    pref-src="" routing-table=main scope=30 suppress-hw-offload=no \
    target-scope=31
add disabled=no distance=1 dst-address=8.8.4.4/32 gateway=net pref-src="" \
    routing-table=main scope=30 suppress-hw-offload=no target-scope=31
add check-gateway=ping disabled=no distance=3 dst-address=0.0.0.0/0 gateway=\
    192.5.5.241 pref-src="" routing-table=main scope=30 suppress-hw-offload=\
    no target-scope=32
add check-gateway=ping disabled=yes distance=4 dst-address=0.0.0.0/0 gateway=\
    8.8.4.4 pref-src="" routing-table=main scope=30 suppress-hw-offload=no \
    target-scope=32
add comment=ISP2 distance=1 dst-address=8.8.4.4 gateway=10.137.85.105 scope=\
    30 target-scope=10
add check-gateway=ping comment=ISP2 distance=4 gateway=8.8.4.4 scope=30 \
    target-scope=32
add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=eoip-tunnel-ike2 \
    routing-table=eoip scope=30 suppress-hw-offload=no target-scope=10
/ip service
set telnet disabled=yes
set ftp disabled=yes
set api disabled=yes
set api-ssl disabled=yes
/ip smb shares
set [ find default=yes ] directory=/pub
/ip upnp
set enabled=yes
/mpls ldp
add disabled=no lsr-id=192.168.12.2 transport-addresses=192.168.12.2
/mpls ldp interface
add disabled=no interface="ether5-IPTV STB"
add disabled=no interface=lo
/ppp profile
add bridge=*E name=SITE-TO-SITE-L2VPN
/routing bfd configuration
add disabled=no interfaces=all min-rx=200ms min-tx=200ms multiplier=5
/routing igmp-proxy
set quick-leave=yes
/routing igmp-proxy interface
add alternative-subnets="172.16.0.0/16,172.26.0.0/16,(Redacted)/16,(Redacted)/28,(Redacted)/28,(Redacted)/28,0.0.0.0/0" disabled=yes \
    interface=wg1 upstream=yes
add disabled=yes interface="ether5-IPTV STB"
/routing rule
add action=lookup-only-in-table disabled=yes src-address=192.168.99.101/32 \
    table=main
add action=lookup comment="Alienware PC VPN Routing (Enable to bypass MK WG)" \
    disabled=yes src-address=192.168.99.183/32 table=main
add action=lookup comment="ASUS Router" disabled=no src-address=\
    192.168.99.155/32 table=main
add action=lookup-only-in-table disabled=no dst-address=192.168.99.0/24 \
    src-address=192.168.99.0/24 table=main
add action=lookup-only-in-table disabled=no src-address=192.168.99.0/24 \
    table=wg
add action=lookup-only-in-table disabled=no dst-address=192.168.95.0/24 \
    src-address=192.168.95.0/24 table=main
add action=lookup comment=\
    "AVM Fritz Powerline 1260 - Enable to bypass WG VPN" disabled=yes \
    src-address=192.168.99.190/32 table=main
add action=lookup comment="PS5 (Enable to bypass MK WG)" disabled=yes \
    src-address=192.168.99.91/32 table=main
add action=lookup comment="NettvPlus Motorola (Enable to bypass MK WG)" \
    disabled=yes src-address=192.168.99.35/32 table=main
add action=lookup comment="Macbook Pro" disabled=yes src-address=\
    192.168.99.23/32 table=main
add action=lookup comment="MaxTV box Enable to bypass MK WG" disabled=yes \
    src-address=192.168.99.21/32 table=main
add action=lookup-only-in-table disabled=no src-address=192.168.95.0/24 \
    table=eoip
/system clock
set time-zone-autodetect=no time-zone-name=Africa/Douala
/system identity
set name=5009
/system logging
add disabled=yes topics=ipsec
/system note
set show-at-login=no
/system script
add dont-require-permissions=yes name=UP owner=DDD policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/\
    tool fetch url=\"https://api.telegram.org/bot(Redacted)/sendmessage\?chat_id=(Redacted)&text=WAN1 is UP\""
add dont-require-permissions=yes name=DOWN owner=DDD policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    delay 20s;\r\
    \n/tool fetch url=\"https://api.telegram.org/bot(Redacted)/sendmessage\?chat_id=(Redacted)&text=WAN1 is DOWN\""
/tool graphing interface
add
/tool graphing resource
add
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN
/tool netwatch
add disabled=no down-script="/system/script/run DOWN;" host=192.5.5.241 \
    http-codes="" interval=1m packet-count=10 packet-interval=1s start-delay=\
    3s startup-delay=2m test-script="" thr-avg=200ms timeout=3s type=icmp \
    up-script="/system/script/run UP;"
add disabled=yes down-script="" host=1.1.1.1 http-codes="" interval=30s \
    packet-count=5 packet-interval=1s start-delay=3s test-script="" timeout=\
    1s type=icmp up-script=""
add disabled=yes down-script="/system/script/run DOWN;" host=8.8.8.8 \
    http-codes="" test-script="" type=simple up-script=\
    "/system/script/run UP;"
add disabled=yes down-script="" host=8.8.8.8 http-codes="" interval=30s \
    packet-count=5 packet-interval=1s src-address=192.168.1.24 start-delay=3s \
    test-script="" thr-avg=300ms timeout=1s type=icmp up-script=""
/tool romon
set enabled=yes
/tool sniffer
set filter-direction=tx filter-interface="ether5-IPTV STB" filter-stream=yes \
    only-headers=yes streaming-enabled=yes streaming-server=(Redacted)

---
```