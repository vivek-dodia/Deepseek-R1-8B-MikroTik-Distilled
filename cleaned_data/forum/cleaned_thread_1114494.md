# Thread Information
Title: Thread-1114494
Section: RouterOS
Thread ID: 1114494

# Discussion

## Initial Question
Sawadee...It's been 3 weeks of battle finding solution and error to our problem. We have 1gb internet cnn from our ISP. Bandwidth test inside the ccr1016 shows 600-800mbps but when using speedtest on pc on the classrooms get 90-150mbps. Wifi is worst like 2-15mbps in 2.4ghz using hap ac.Please help usHere is my config>>>
```
# may/17/2024 07:35:51 by RouterOS 6.49.13
# software id = C4F7-FG2G
#
# model = CCR1016-12G
# serial number = xxxxxxxxx
/caps-man channel
add band=2ghz-b/g/n control-channel-width=20mhz frequency=2412 name=\
    Channel-2G
add band=5ghz-a/n/ac control-channel-width=20mhz frequency=5180 name=\
    Channel-5G
/interface bridge
add admin-mac=06:6C:C4:1F:58:D0 auto-mac=no fast-forward=no name=\
    "COM-AP Bridge"
/interface ethernet
set [ find default-name=ether1 ] l2mtu=1590 speed=100Mbps
set [ find default-name=ether2 ] l2mtu=1590 speed=100Mbps
set [ find default-name=ether3 ] disabled=yes l2mtu=1590 speed=100Mbps
set [ find default-name=ether4 ] l2mtu=1590 speed=100Mbps
set [ find default-name=ether5 ] l2mtu=1590 name=ether5-ACAD speed=100Mbps
set [ find default-name=ether6 ] l2mtu=1590 name=ether6-WCBS speed=100Mbps
set [ find default-name=ether7 ] l2mtu=1590 name=ether7-COM speed=100Mbps
set [ find default-name=ether8 ] l2mtu=1590 name=ether8-DMZ-FF speed=100Mbps
set [ find default-name=ether9 ] l2mtu=1590 name=ether9-AP speed=100Mbps
set [ find default-name=ether10 ] l2mtu=1590 name=ether10-CCTV speed=100Mbps
set [ find default-name=ether11 ] l2mtu=1590 speed=100Mbps
set [ find default-name=ether12 ] l2mtu=1590 speed=100Mbps
/interface pppoe-client
add comment="Ping to check eth1 internet" disabled=no interface=ether1 name=\
    pppoe-out1 password=xxxx use-peer-dns=yes user=xxxxxxxxxx
add comment="Ping to check 3bb line and EoIP" disabled=no interface=ether4 \
    name="pppoe-out2 3bb" password=xxxxx use-peer-dns=yes user=\
    xxxxxxxxx
/interface pptp-server
add name=pptp-in1 user=""
/interface eoip
add disabled=yes !keepalive mac-address=02:4D:D5:95:F1:90 mtu=1500 name=\
    "Anglo31 EoIP" remote-address=xxx.xxx.xxx.xxx tunnel-id=5
add disabled=yes !keepalive local-address=xxx.xx.xxx.xx mac-address=\
    02:7B:98:2E:85:19 name="Anglo64 EoIP" remote-address=xxx.xx.xx.xxx \
    tunnel-id=6

/caps-man interface
add disabled=no mac-address=CC:2D:E0:79:13:5C master-interface=none name=cap1 \
    radio-mac=CC:2D:E0:79:13:5C radio-name=CC2DE079135C
add disabled=no mac-address=CC:2D:E0:79:15:5C master-interface=none name=cap2 \
    radio-mac=CC:2D:E0:79:15:5C radio-name=CC2DE079155C
add disabled=no mac-address=CC:2D:E0:79:13:5B master-interface=none name=cap3 \
    radio-mac=CC:2D:E0:79:13:5B radio-name=CC2DE079135B
add disabled=no mac-address=CC:2D:E0:79:19:24 master-interface=none name=cap4 \
    radio-mac=CC:2D:E0:79:19:24 radio-name=CC2DE0791924
add disabled=no mac-address=CC:2D:E0:79:19:23 master-interface=none name=cap5 \
    radio-mac=CC:2D:E0:79:19:23 radio-name=CC2DE0791923
add disabled=no mac-address=CC:2D:E0:AA:C9:79 master-interface=none name=cap6 \
    radio-mac=CC:2D:E0:AA:C9:79 radio-name=CC2DE0AAC979
add disabled=no mac-address=CC:2D:E0:AA:C9:78 master-interface=none name=cap7 \
    radio-mac=CC:2D:E0:AA:C9:78 radio-name=CC2DE0AAC978
add disabled=no mac-address=CC:2D:E0:A5:58:8B master-interface=none name=cap8 \
    radio-mac=CC:2D:E0:A5:58:8B radio-name=CC2DE0A5588B
add disabled=no mac-address=CC:2D:E0:A5:58:8A master-interface=none name=cap9 \
    radio-mac=CC:2D:E0:A5:58:8A radio-name=CC2DE0A5588A
add disabled=no mac-address=CC:2D:E0:7C:5B:03 master-interface=none name=\
    cap10 radio-mac=CC:2D:E0:7C:5B:03 radio-name=CC2DE07C5B03
add disabled=no mac-address=CC:2D:E0:7C:5B:02 master-interface=none name=\
    cap11 radio-mac=CC:2D:E0:7C:5B:02 radio-name=CC2DE07C5B02

/caps-man datapath
add bridge="COM-AP Bridge" name=AP
/caps-man security
add authentication-types=wpa2-psk encryption=aes-ccm name=aNglokorat \
    passphrase=aNglokorat
add name=nopass
/caps-man configuration
add channel=Channel-2G country=thailand datapath=AP mode=ap name=Anglo-WiFi \
    security=aNglokorat ssid=Anglo-WiFi
add channel=Channel-5G country=thailand datapath=AP mode=ap name=\
    Anglo-WiFi-5G security=aNglokorat ssid=Anglo-WiFi-5G
add channel=Channel-2G country=thailand datapath=AP mode=ap name=test \
    security=aNglokorat ssid=TEST
add channel=Channel-5G country=thailand datapath=AP mode=ap name=test-5g \
    security=aNglokorat ssid=TEST-5g
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip firewall layer7-protocol
add name=Youtube regexp="^.+(youtube.com|googlevideo.com).*\$."
add name=Fiwfans regexp="^.+(fiwfans.vip).*\$"
add name=Tiktok regexp="^.+(tiktok.com).*\$"
add name=Netflix regexp="^.+(netflix.com).*\$"
add name=Twitter regexp="^.+(twitter.com).*\$"
add name=Reddit regexp="^.+(reddit.com).*\$"
add name=Roblox regexp="^.+(roblox.com).*\$"
add name=Instagram regexp="^.+(instagram.com).*\$"
add name=Y8 regexp="^.+(y8.com).*\$"
add name=Onlyfans regexp="^.+(onlyfans.com).*\$"
add name=Disney regexp="^.+(disneyplus.com|hotstar.com).*\$"
add name=Facebook regexp="^.+(facebook.com).*\$"
/ip ipsec policy group
add name=ipsec+l2tp
/ip ipsec profile
add enc-algorithm=aes-256,aes-192,aes-128 name=profile_1
/ip ipsec peer
add name=peer3 passive=yes profile=profile_1
/ip ipsec proposal
set [ find default=yes ] enc-algorithms=aes-256-cbc,aes-128-cbc,3des \
    pfs-group=none

/ip pool
add name=ITpool10.6464 ranges=10.64.64.5-10.64.64.30
add name=CCTVPool2 ranges=10.20.2.1-10.20.2.254
add name=APPool2 ranges=10.10.2.1-10.10.2.254
add name="COM-AP Pool 2" ranges=10.0.2.1-10.0.3.244
add name=L2TPCCTV ranges=10.21.0.1-10.21.0.20
add name=VPN ranges=10.0.3.245-10.0.3.254

/ip dhcp-server

/ip pool
add name="COM-AP Pool 1" next-pool="COM-AP Pool 2" ranges=\
    10.0.0.100-10.0.1.254
add name=APPool1 next-pool=APPool2 ranges=10.10.1.1-10.10.1.254
add name=CCTVPool1 next-pool=CCTVPool2 ranges=10.20.1.1-10.20.1.254
/ip dhcp-server
add address-pool="COM-AP Pool 1" authoritative=after-2sec-delay disabled=no \
    interface="COM-AP Bridge" lease-time=8h name="COM-AP Network"
add address-pool=APPool1 authoritative=after-2sec-delay lease-time=8h name=\
    "AP Network"
add address-pool=CCTVPool1 authoritative=after-2sec-delay disabled=no \
    interface=ether10-CCTV lease-time=8h name="CCTV Network"
/ppp profile
add dns-server=10.0.0.1,8.8.8.8 local-address=10.0.0.1 name=koratVPN \
    remote-address=APPool1 use-compression=yes use-encryption=yes use-mpls=\
    yes
add change-tcp-mss=yes dns-server=10.0.0.1,8.8.8.8 local-address=10.20.0.2 \
    name=cctv remote-address=L2TPCCTV use-encryption=yes
/queue simple
add disabled=yes max-limit=5M/5M name=gold target=10.0.1.207/32
add disabled=yes max-limit=1M/1M name=queue3 target=10.0.1.230/32
add max-limit=5M/5M name=queue4 target=10.0.1.141/32
/queue tree
add disabled=yes name=queue1 parent=global
/queue type
add kind=pcq name=pcq_up pcq-classifier=dst-address pcq-dst-address6-mask=64 \
    pcq-rate=10M pcq-src-address6-mask=64
add kind=pcq name=pcq_down pcq-classifier=dst-address pcq-dst-address6-mask=\
    64 pcq-rate=20M pcq-src-address6-mask=64
/queue simple
add disabled=yes name=queue1 queue=pcq_up/pcq_down target="COM-AP Bridge"
/system logging action
set 3 remote=172.16.10.113
/caps-man manager
set enabled=yes
/caps-man provisioning
add action=create-dynamic-enabled identity-regexp=AP2-10 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:7C:55:A2
add action=create-dynamic-enabled identity-regexp=AP2-10 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:7C:55:A3
add action=create-dynamic-enabled identity-regexp=AP2-08 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:79:13:7B
add action=create-dynamic-enabled identity-regexp=AP2-05 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:79:15:9C
add action=create-dynamic-enabled identity-regexp=Audi5 master-configuration=\
    Anglo-WiFi name-format=identity radio-mac=CC:2D:E0:7C:5A:FC
add action=create-dynamic-enabled identity-regexp=AP-GYM3 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:AB:26:07
add action=create-dynamic-enabled identity-regexp=AP-GYM2 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:95:3B:F6
add action=create-dynamic-enabled identity-regexp=AP-GYM2 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:95:3B:F5
add action=create-dynamic-enabled identity-regexp=AP-AUDI \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:8C:5A:83
add action=create-dynamic-enabled identity-regexp=AP-AUDI2 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:8C:5A:C3
add action=create-dynamic-enabled identity-regexp=AP-AUDI \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:8C:5A:82
add action=create-dynamic-enabled identity-regexp=AP-GYM3 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:AB:26:06
add action=create-dynamic-enabled identity-regexp=AP-GYM1 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:8C:5D:63
add action=create-dynamic-enabled identity-regexp=AP-GYM1 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:8C:5D:62
add action=create-dynamic-enabled identity-regexp=AP-AUDI2 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:8C:5A:C2
add action=create-dynamic-enabled identity-regexp=AP2-14 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:79:15:5B
add action=create-dynamic-enabled identity-regexp=AP2-05 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:79:15:9B
add action=create-dynamic-enabled identity-regexp=AP2-13 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:86:BB:46
add action=create-dynamic-enabled identity-regexp=AP2-13 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:86:BB:47
add action=create-dynamic-enabled identity-regexp=AP2-11 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:79:19:24
add action=create-dynamic-enabled identity-regexp=AP2-11 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:79:19:23
add action=create-dynamic-enabled identity-regexp=AP2-02 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:7C:54:C3
add action=create-dynamic-enabled identity-regexp=AP2-01 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:79:0F:5C
add action=create-dynamic-enabled identity-regexp=AP2-12 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:79:14:2C
add action=create-dynamic-enabled identity-regexp=AP2-04 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:7C:5B:02
add action=create-dynamic-enabled identity-regexp=AP2-04 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:7C:5B:03
add action=create-dynamic-enabled identity-regexp=AP2-02 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:7C:54:C2
add action=create-dynamic-enabled identity-regexp=AP2-12 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:79:14:2B
add action=create-dynamic-enabled identity-regexp=AP1-23 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:A5:4E:E3
add action=create-dynamic-enabled identity-regexp=AP1-21 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:7C:5B:A2
add action=create-dynamic-enabled identity-regexp=AP1-19 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:8C:57:E3
add action=create-dynamic-enabled identity-regexp=AP1-18 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:A5:4F:3B
add action=create-dynamic-enabled identity-regexp=AP1-17 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:7C:56:E3
add action=create-dynamic-enabled identity-regexp=AP1-15 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:79:18:0B
add action=create-dynamic-enabled identity-regexp=AP1-11 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:79:17:9B
add action=create-dynamic-enabled identity-regexp=AP1-05 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:79:18:93
add action=create-dynamic-enabled identity-regexp=AP1-04 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:8C:57:AA
add action=create-dynamic-enabled identity-regexp=AP1-06 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:79:19:43
add action=create-dynamic-enabled identity-regexp=AP1-07 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:79:16:33
add action=create-dynamic-enabled identity-regexp=AP1-23 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:A5:4E:E2
add action=create-dynamic-enabled identity-regexp=AP1-19 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:8C:57:E2
add action=create-dynamic-enabled identity-regexp=AP1-18 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:A5:4F:3A
add action=create-dynamic-enabled identity-regexp=AP1-01 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:A5:53:0A
add action=create-dynamic-enabled identity-regexp=AP1-17 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:7C:56:E2
add action=create-dynamic-enabled identity-regexp=AP1-16 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:A5:58:8B
add action=create-dynamic-enabled identity-regexp=AP1-16 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:A5:58:8A
add action=create-dynamic-enabled identity-regexp=AP1-11 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:79:17:9C
add action=create-dynamic-enabled identity-regexp=AP1-12 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:79:16:54
add action=create-dynamic-enabled identity-regexp=AP1-12 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:79:16:53
add action=create-dynamic-enabled identity-regexp=AP1-05 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:79:18:94
add action=create-dynamic-enabled identity-regexp=AP1-07 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:79:16:34
add action=create-dynamic-enabled identity-regexp=AP1-06 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:79:19:44
add action=create-dynamic-enabled identity-regexp=AP1-04 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:8C:57:AB
add action=create-dynamic-enabled identity-regexp=AP1-03 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:8C:5B:13
add action=create-dynamic-enabled identity-regexp=AP1-03 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:8C:5B:12
add action=create-dynamic-enabled identity-regexp=AP1-02 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:8C:56:A3
add action=create-dynamic-enabled identity-regexp=AP1-02 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:8C:56:A2
add action=create-dynamic-enabled identity-regexp=AP1-01 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:A5:53:0B
add action=create-dynamic-enabled identity-regexp=AP1-21 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:7C:5B:A3
add action=create-dynamic-enabled identity-regexp=AP1-15 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:79:18:0C
add action=create-dynamic-enabled identity-regexp=AP2-08 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:79:13:7C
add action=create-dynamic-enabled identity-regexp=AP2-01 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:79:0F:5B
add action=create-dynamic-enabled identity-regexp=AP-GYM5 \
    master-configuration=Anglo-WiFi name-format=identity radio-mac=\
    CC:2D:E0:A5:54:8C
add action=create-dynamic-enabled identity-regexp=AP-GYM5 \
    master-configuration=Anglo-WiFi-5G name-format=identity radio-mac=\
    CC:2D:E0:A5:54:8B
/dude
set enabled=yes
/interface bridge port
add bridge="COM-AP Bridge" interface=ether5-ACAD
add bridge="COM-AP Bridge" hw=no interface=ether6-WCBS
add bridge="COM-AP Bridge" interface=ether7-COM
add interface=ether11
add bridge="COM-AP Bridge" interface=ether9-AP multicast-router=disabled
/interface bridge settings
set allow-fast-path=no
/ip neighbor discovery-settings
set discover-interface-list=!dynamic
/interface l2tp-server server
set enabled=yes
/interface pptp-server server
set enabled=yes
/ip address
add address=10.64.64.1/24 interface=ether3 network=10.64.64.0
add address=10.200.200.2/24 interface=ether2 network=10.200.200.0
add address=10.10.0.1/16 disabled=yes network=10.10.0.0
add address=10.20.0.1/16 interface=ether10-CCTV network=10.20.0.0
add address=10.0.0.1/22 interface="COM-AP Bridge" network=10.0.0.0
add address=10.200.3.2/24 interface="Anglo31 EoIP" network=10.200.3.0
add address=10.200.1.2/24 interface=gre-tunnel-singapore network=10.200.1.0
add address=10.0.0.2/22 disabled=yes interface="COM-AP Bridge" network=\
    10.0.0.0
add address=10.20.0.2/16 interface=ether10-CCTV network=10.20.0.0
/ip cloud
set ddns-enabled=yes
/ip dhcp-client
add add-default-route=no disabled=no interface=ether2
/ip dhcp-server lease
add address=10.20.1.254 mac-address=04:09:73:FD:25:3C server="CCTV Network"
add address=10.20.1.245 client-id=40b9.3c65.ee8c-Vlan-interface1 mac-address=\
    40:B9:3C:65:EE:8C server="CCTV Network"
add address=10.20.1.244 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:62 \
    comment="A236 Thai1" mac-address=94:E1:AC:C4:FD:62 server="CCTV Network"
add address=10.20.1.243 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:68 \
    comment="A238 Chinese2" mac-address=94:E1:AC:C4:FD:68 server=\
    "CCTV Network"
add address=10.20.1.242 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:5c \
    comment="A208 Roman1" mac-address=94:E1:AC:C4:FD:5C server="CCTV Network"
add address=10.20.1.241 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:58 \
    comment="A210 Egyptian1" mac-address=94:E1:AC:C4:FD:58 server=\
    "CCTV Network"
add address=10.20.1.240 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:55 \
    comment="A237 Thai1" mac-address=94:E1:AC:C4:FD:55 server="CCTV Network"
add address=10.20.1.239 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:5e \
    comment="A227 Music Room2" mac-address=94:E1:AC:C4:FD:5E server=\
    "CCTV Network"
add address=10.20.1.238 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:5f \
    comment="A221 StaffSec1" mac-address=94:E1:AC:C4:FD:5F server=\
    "CCTV Network"
add address=10.20.1.237 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:5d \
    comment="A232 ICT2" mac-address=94:E1:AC:C4:FD:5D server="CCTV Network"
add address=10.20.1.236 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:53 \
    comment="A231 Art Room2" mac-address=94:E1:AC:C4:FD:53 server=\
    "CCTV Network"
add address=10.20.1.235 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:66 \
    comment=A224-1 mac-address=94:E1:AC:C4:FD:66 server="CCTV Network"
add address=10.20.1.234 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:56 \
    comment="A225 Sec 1a" mac-address=94:E1:AC:C4:FD:56 server="CCTV Network"
add address=10.20.1.233 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:63 \
    comment="A211 Babylonian1" mac-address=94:E1:AC:C4:FD:63 server=\
    "CCTV Network"
add address=10.20.1.232 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:5a \
    comment="A220 Gen Lab1" mac-address=94:E1:AC:C4:FD:5A server=\
    "CCTV Network"
add address=10.20.1.231 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:59 \
    comment="A239 Chinese1" mac-address=94:E1:AC:C4:FD:59 server=\
    "CCTV Network"
add address=10.20.1.230 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:5b \
    comment="A209 Greek1" mac-address=94:E1:AC:C4:FD:5B server="CCTV Network"
add address=10.20.1.229 client-id=1:94:e1:ac:61:1:e comment=A239-2 \
    mac-address=94:E1:AC:61:01:0E server="CCTV Network"
add address=10.20.1.228 client-id=1:94:e1:ac:78:7a:3 comment=\
    "A229 IT Server1" mac-address=94:E1:AC:78:7A:03 server="CCTV Network"
add address=10.20.1.227 client-id=1:94:e1:ac:78:78:30 comment=\
    "A229 IT Server3" mac-address=94:E1:AC:78:78:30 server="CCTV Network"
add address=10.20.1.226 client-id=1:94:e1:ac:61:1:39 comment="A225 Sec1-2" \
    mac-address=94:E1:AC:61:01:39 server="CCTV Network"
add address=10.20.1.225 client-id=1:94:e1:ac:78:79:3a comment="Corridor Lab3" \
    mac-address=94:E1:AC:78:79:3A server="CCTV Network"
add address=10.20.1.224 client-id=1:94:e1:ac:78:79:66 comment=\
    "Corridor A220 Gen Lab" mac-address=94:E1:AC:78:79:66 server=\
    "CCTV Network"
add address=10.20.1.223 client-id=1:94:e1:ac:61:1:17 comment="A220 Gen Lab2" \
    mac-address=94:E1:AC:61:01:17 server="CCTV Network"
add address=10.20.1.222 client-id=1:4c:bd:8f:de:4c:38 comment="A219 Physics2" \
    mac-address=4C:BD:8F:DE:4C:38 server="CCTV Network"
add address=10.20.1.221 client-id=1:94:e1:ac:61:1:16 comment="A232 ICT1" \
    mac-address=94:E1:AC:61:01:16 server="CCTV Network"
add address=10.20.1.220 client-id=1:94:e1:ac:78:78:2d comment=\
    "Corridor ICT-MUSC" mac-address=94:E1:AC:78:78:2D server="CCTV Network"
add address=10.20.1.219 client-id=1:94:e1:ac:78:79:53 comment=\
    "Corridor Staff2" mac-address=94:E1:AC:78:79:53 server="CCTV Network"
add address=10.20.1.218 client-id=1:4c:bd:8f:de:4c:3 comment="A216 Chem Lab1" \
    mac-address=4C:BD:8F:DE:4C:03 server="CCTV Network"
add address=10.20.1.217 client-id=1:94:e1:ac:78:79:f5 comment=\
    "A204 Meeting Room" mac-address=94:E1:AC:78:79:F5 server="CCTV Network"
add address=10.20.1.216 client-id=1:94:e1:ac:78:78:95 comment="A240 IL" \
    mac-address=94:E1:AC:78:78:95 server="CCTV Network"
add address=10.20.1.215 client-id=1:94:e1:ac:78:79:3c comment=\
    "Corridor Staff Room" mac-address=94:E1:AC:78:79:3C server="CCTV Network"
add address=10.20.1.214 client-id=1:94:e1:ac:61:0:f9 comment=\
    "A226 Staff Room2" mac-address=94:E1:AC:61:00:F9 server="CCTV Network"
add address=10.20.1.213 client-id=1:94:e1:ac:61:1:c comment="A208 Roman2" \
    mac-address=94:E1:AC:61:01:0C server="CCTV Network"
add address=10.20.1.212 client-id=1:94:e1:ac:78:79:1f comment="Corridor A224" \
    mac-address=94:E1:AC:78:79:1F server="CCTV Network"
add address=10.20.1.211 client-id=1:94:e1:ac:78:79:40 comment=\
    "Corridor Lab Staff2" mac-address=94:E1:AC:78:79:40 server="CCTV Network"
add address=10.20.1.210 client-id=1:94:e1:ac:78:79:37 comment="Corridor IT" \
    mac-address=94:E1:AC:78:79:37 server="CCTV Network"
add address=10.20.1.209 client-id=1:94:e1:ac:78:78:ff comment="A207 Accrdtn2" \
    mac-address=94:E1:AC:78:78:FF server="CCTV Network"
add address=10.20.1.208 client-id=1:94:e1:ac:78:79:1d comment=\
    "Corridor Sec1 A212" mac-address=94:E1:AC:78:79:1D server="CCTV Network"
add address=10.20.1.207 client-id=1:94:e1:ac:61:1:0 comment="A209 Greek2" \
    mac-address=94:E1:AC:61:01:00 server="CCTV Network"
add address=10.20.1.206 client-id=1:94:e1:ac:61:1:25 comment=A224-2 \
    mac-address=94:E1:AC:61:01:25 server="CCTV Network"
add address=10.20.1.205 client-id=1:94:e1:ac:78:79:45 comment=\
    "Corridor Staff1" mac-address=94:E1:AC:78:79:45 server="CCTV Network"
add address=10.20.1.204 client-id=1:94:e1:ac:78:79:89 comment="F.exit A235" \
    mac-address=94:E1:AC:78:79:89 server="CCTV Network"
add address=10.20.1.203 client-id=1:94:e1:ac:78:79:42 comment="Corridor A210" \
    mac-address=94:E1:AC:78:79:42 server="CCTV Network"
add address=10.20.1.202 client-id=1:94:e1:ac:78:7a:6 comment="Corridor Lab2" \
    mac-address=94:E1:AC:78:7A:06 server="CCTV Network"
add address=10.20.1.201 client-id=1:94:e1:ac:78:79:cf comment="A203 Exam Rm2" \
    mac-address=94:E1:AC:78:79:CF server="CCTV Network"
add address=10.20.1.200 client-id=1:94:e1:ac:61:1:68 comment="A237 Thai2" \
    mac-address=94:E1:AC:61:01:68 server="CCTV Network"
add address=10.20.1.199 client-id=1:94:e1:ac:78:79:d5 comment=\
    "A207 Accreditation1" mac-address=94:E1:AC:78:79:D5 server="CCTV Network"
add address=10.20.1.198 client-id=1:94:e1:ac:78:7a:14 comment=\
    "Corridor Elev 2nd flr" mac-address=94:E1:AC:78:7A:14 server=\
    "CCTV Network"
add address=10.20.1.197 client-id=1:94:e1:ac:61:0:ef comment="A238 Chinese1" \
    mac-address=94:E1:AC:61:00:EF server="CCTV Network"
add address=10.20.1.196 client-id=1:94:e1:ac:78:78:e0 comment=\
    "A228 Back Stage" mac-address=94:E1:AC:78:78:E0 server="CCTV Network"
add address=10.20.1.195 client-id=1:94:e1:ac:78:79:fb comment="Corridor MPR" \
    mac-address=94:E1:AC:78:79:FB server="CCTV Network"
add address=10.20.1.194 client-id=1:94:e1:ac:78:78:5d comment="A215 Gas R A" \
    mac-address=94:E1:AC:78:78:5D server="CCTV Network"
add address=10.20.1.193 client-id=1:4c:bd:8f:de:4b:ec comment="A218 Biology2" \
    mac-address=4C:BD:8F:DE:4B:EC server="CCTV Network"
add address=10.20.1.192 client-id=1:94:e1:ac:61:1:2 comment="A210 Egypthian2" \
    mac-address=94:E1:AC:61:01:02 server="CCTV Network"
add address=10.20.1.191 client-id=1:94:e1:ac:78:79:3b comment="Corridor Lab" \
    mac-address=94:E1:AC:78:79:3B server="CCTV Network"
add address=10.20.1.190 client-id=1:94:e1:ac:61:1:74 comment=\
    "A226 Staff Room1" mac-address=94:E1:AC:61:01:74 server="CCTV Network"
add address=10.20.1.189 client-id=1:94:e1:ac:61:1:3e comment="A231 Art Room1" \
    mac-address=94:E1:AC:61:01:3E server="CCTV Network"
add address=10.20.1.188 client-id=1:94:e1:ac:61:1:5a comment="A221 StaffSec2" \
    mac-address=94:E1:AC:61:01:5A server="CCTV Network"
add address=10.20.1.187 client-id=1:94:e1:ac:78:7a:8a comment=\
    "A215 Prep Storage" mac-address=94:E1:AC:78:7A:8A server="CCTV Network"
add address=10.20.1.186 client-id=1:4c:bd:8f:de:4c:a comment="A219 Physics1" \
    mac-address=4C:BD:8F:DE:4C:0A server="CCTV Network"
add address=10.20.1.185 client-id=1:94:e1:ac:61:1:1e comment="A236 Thai2" \
    mac-address=94:E1:AC:61:01:1E server="CCTV Network"
add address=10.20.1.184 client-id=1:4c:bd:8f:de:4c:16 comment="A218 Biology1" \
    mac-address=4C:BD:8F:DE:4C:16 server="CCTV Network"
add address=10.20.1.183 client-id=1:94:e1:ac:78:79:16 comment=\
    "A229 IT Server2" mac-address=94:E1:AC:78:79:16 server="CCTV Network"
add address=10.20.1.182 client-id=1:94:e1:ac:61:1:67 comment=\
    "A227 Music Room1" mac-address=94:E1:AC:61:01:67 server="CCTV Network"
add address=10.20.1.181 always-broadcast=yes client-id=1:94:e1:ac:5a:d0:5d \
    comment=A134C mac-address=94:E1:AC:5A:D0:5D server="CCTV Network"
add address=10.20.1.180 always-broadcast=yes client-id=1:94:e1:ac:5a:d0:5b \
    comment="A126C Multimedia" mac-address=94:E1:AC:5A:D0:5B server=\
    "CCTV Network"
add address=10.20.1.179 always-broadcast=yes client-id=1:94:e1:ac:5a:d0:5a \
    comment="A132 Australia1" mac-address=94:E1:AC:5A:D0:5A server=\
    "CCTV Network"
add address=10.20.1.178 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:67 \
    comment="A123 Asia2" mac-address=94:E1:AC:C4:FD:67 server="CCTV Network"
add address=10.20.1.177 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:61 \
    comment="A112 Amazon Jungle2" mac-address=94:E1:AC:C4:FD:61 server=\
    "CCTV Network"
add address=10.20.1.176 always-broadcast=yes client-id=1:64:db:8b:7f:7a:ed \
    comment="A133 Africa1" mac-address=64:DB:8B:7F:7A:ED server=\
    "CCTV Network"
add address=10.20.1.175 always-broadcast=yes client-id=1:64:db:8b:6b:8b:bb \
    comment="A124 Europe1" mac-address=64:DB:8B:6B:8B:BB server=\
    "CCTV Network"
add address=10.20.1.174 always-broadcast=yes client-id=1:64:db:8b:6b:8b:b8 \
    comment="A131 South America1" mac-address=64:DB:8B:6B:8B:B8 server=\
    "CCTV Network"
add address=10.20.1.173 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:65 \
    comment="A114 Under the Sea2" mac-address=94:E1:AC:C4:FD:65 server=\
    "CCTV Network"
add address=10.20.1.172 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:60 \
    comment="A115 Autumn2" mac-address=94:E1:AC:C4:FD:60 server=\
    "CCTV Network"
add address=10.20.1.171 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:64 \
    comment="A125 North America2" mac-address=94:E1:AC:C4:FD:64 server=\
    "CCTV Network"
add address=10.20.1.170 always-broadcast=yes client-id=1:94:e1:ac:5a:d0:5c \
    comment="A110 Summer2" mac-address=94:E1:AC:5A:D0:5C server=\
    "CCTV Network"
add address=10.20.1.169 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:54 \
    comment="A105 Candy2" mac-address=94:E1:AC:C4:FD:54 server="CCTV Network"
add address=10.20.1.168 always-broadcast=yes client-id=1:94:e1:ac:c4:fd:57 \
    comment="A206 Pantry" mac-address=94:E1:AC:C4:FD:57 server="CCTV Network"
add address=10.20.1.167 client-id=1:94:e1:ac:b8:de:ef comment=Right6 \
    mac-address=94:E1:AC:B8:DE:EF server="CCTV Network"
add address=10.20.1.166 client-id=1:94:e1:ac:61:1:14 comment=\
    "A114 Under the Sea1" mac-address=94:E1:AC:61:01:14 server="CCTV Network"
add address=10.20.1.165 always-broadcast=yes client-id=1:94:e1:ac:5a:d0:5e \
    comment="A111 Winter1" mac-address=94:E1:AC:5A:D0:5E server=\
    "CCTV Network"
add address=10.20.1.163 client-id=1:94:e1:ac:c4:a5:89 comment=Aquarium2 \
    mac-address=94:E1:AC:C4:A5:89 server="CCTV Network"
add address=10.20.1.162 client-id=1:94:e1:ac:c4:a5:8b comment=Assembly9 \
    mac-address=94:E1:AC:C4:A5:8B server="CCTV Network"
add address=10.20.1.161 client-id=1:94:e1:ac:5a:30:a comment="Hallway KG7" \
    mac-address=94:E1:AC:5A:30:0A server="CCTV Network"
add address=10.20.1.160 client-id=1:94:e1:ac:5a:30:98 comment=Library3 \
    mac-address=94:E1:AC:5A:30:98 server="CCTV Network"
add address=10.20.1.159 client-id=1:94:e1:ac:b8:df:9 comment=Left2 \
    mac-address=94:E1:AC:B8:DF:09 server="CCTV Network"
add address=10.20.1.157 client-id=1:4c:bd:8f:de:4c:23 comment="A124 Europe2" \
    mac-address=4C:BD:8F:DE:4C:23 server="CCTV Network"
add address=10.20.1.156 client-id=1:94:e1:ac:c4:a5:78 comment=Assembly6 \
    mac-address=94:E1:AC:C4:A5:78 server="CCTV Network"
add address=10.20.1.155 client-id=1:94:e1:ac:5a:30:f comment=Lib.HW \
    mac-address=94:E1:AC:5A:30:0F server="CCTV Network"
add address=10.20.1.154 client-id=1:4c:bd:8f:de:4c:47 comment=\
    "A106 Noah's Ark1" mac-address=4C:BD:8F:DE:4C:47 server="CCTV Network"
add address=10.20.1.153 client-id=1:94:e1:ac:5a:30:d7 comment="A134 Acctg1" \
    mac-address=94:E1:AC:5A:30:D7 server="CCTV Network"
add address=10.20.1.152 client-id=1:94:e1:ac:c4:a5:65 comment=Right2 \
    mac-address=94:E1:AC:C4:A5:65 server="CCTV Network"
add address=10.20.1.151 client-id=1:94:e1:ac:5a:30:f2 comment="Stud Affairs4" \
    mac-address=94:E1:AC:5A:30:F2 server="CCTV Network"
add address=10.20.1.150 client-id=1:4c:bd:8f:de:4b:f8 comment=\
    "A117 Playroom1" mac-address=4C:BD:8F:DE:4B:F8 server="CCTV Network"
add address=10.20.1.149 client-id=1:94:e1:ac:5a:31:3 comment="Hallway KG8" \
    mac-address=94:E1:AC:5A:31:03 server="CCTV Network"
add address=10.20.1.148 client-id=1:4c:bd:8f:de:4c:2 comment=\
    "A132 Australia2" mac-address=4C:BD:8F:DE:4C:02 server="CCTV Network"
add address=10.20.1.147 client-id=1:94:e1:ac:5a:30:90 comment=A100 \
    mac-address=94:E1:AC:5A:30:90 server="CCTV Network"
add address=10.20.1.146 client-id=1:94:e1:ac:5a:30:bb comment="Stud Affairs3" \
    mac-address=94:E1:AC:5A:30:BB server="CCTV Network"
add address=10.20.1.145 client-id=1:4c:bd:8f:de:4c:5a comment=\
    "Entrance Lobby4" mac-address=4C:BD:8F:DE:4C:5A server="CCTV Network"
add address=10.20.1.144 client-id=1:94:e1:ac:78:78:a4 comment=\
    "A119 Infirmary2" mac-address=94:E1:AC:78:78:A4 server="CCTV Network"
add address=10.20.1.141 client-id=1:94:e1:ac:61:1:7 comment=\
    "A125 NorthAmerca1" mac-address=94:E1:AC:61:01:07 server="CCTV Network"
add address=10.20.1.140 client-id=1:94:e1:ac:78:79:9b comment=A134D \
    mac-address=94:E1:AC:78:79:9B server="CCTV Network"
add address=10.20.1.139 client-id=1:94:e1:ac:78:79:38 comment="A134 Acctg2" \
    mac-address=94:E1:AC:78:79:38 server="CCTV Network"
add address=10.20.1.138 client-id=1:4c:bd:8f:de:4b:dd comment=\
    "Entrance Lobby1" mac-address=4C:BD:8F:DE:4B:DD server="CCTV Network"
add address=10.20.1.137 client-id=1:94:e1:ac:5a:30:c7 comment="Stud Affairs2" \
    mac-address=94:E1:AC:5A:30:C7 server="CCTV Network"
add address=10.20.1.136 client-id=1:4c:bd:8f:de:4c:30 comment="A118 IL" \
    mac-address=4C:BD:8F:DE:4C:30 server="CCTV Network"
add address=10.20.1.135 client-id=1:94:e1:ac:5a:30:e9 comment="Hallway KG1" \
    mac-address=94:E1:AC:5A:30:E9 server="CCTV Network"
add address=10.20.1.134 client-id=1:94:e1:ac:5a:31:6 comment=A102 \
    mac-address=94:E1:AC:5A:31:06 server="CCTV Network"
add address=10.20.1.133 client-id=1:4c:bd:8f:de:4b:ef comment="A133 Africa2" \
    mac-address=4C:BD:8F:DE:4B:EF server="CCTV Network"
add address=10.20.1.132 client-id=1:94:e1:ac:5a:30:58 comment="Hallway KG6" \
    mac-address=94:E1:AC:5A:30:58 server="CCTV Network"
add address=10.20.1.131 client-id=1:94:e1:ac:b8:de:a8 comment=Right5 \
    mac-address=94:E1:AC:B8:DE:A8 server="CCTV Network"
add address=10.20.1.130 client-id=1:4c:bd:8f:de:4c:2c comment=\
    "A131 South America2" mac-address=4C:BD:8F:DE:4C:2C server="CCTV Network"
add address=10.20.1.129 client-id=1:94:e1:ac:b8:de:cf comment=\
    "Kinder Backyard5" mac-address=94:E1:AC:B8:DE:CF server="CCTV Network"
add address=10.20.1.128 client-id=1:4c:bd:8f:de:4c:11 comment="A123 Asia1" \
    mac-address=4C:BD:8F:DE:4C:11 server="CCTV Network"
add address=10.20.1.127 client-id=1:4c:bd:8f:de:4c:59 comment=\
    "A117 Playroom2" mac-address=4C:BD:8F:DE:4C:59 server="CCTV Network"
add address=10.20.1.126 client-id=1:94:e1:ac:5a:30:ef comment="Hallway KG3" \
    mac-address=94:E1:AC:5A:30:EF server="CCTV Network"
add address=10.20.1.125 client-id=1:4c:bd:8f:de:4b:f2 comment="A115 Autumn1" \
    mac-address=4C:BD:8F:DE:4B:F2 server="CCTV Network"
add address=10.20.1.124 client-id=1:94:e1:ac:5a:30:ff comment="Hallway Pri4" \
    mac-address=94:E1:AC:5A:30:FF server="CCTV Network"
add address=10.20.1.123 client-id=1:94:e1:ac:78:79:a5 comment="A126B Library" \
    mac-address=94:E1:AC:78:79:A5 server="CCTV Network"
add address=10.20.1.122 client-id=1:94:e1:ac:c4:a5:b2 comment=Assembly2 \
    mac-address=94:E1:AC:C4:A5:B2 server="CCTV Network"
add address=10.20.1.121 client-id=1:94:e1:ac:c4:a5:91 comment=Assembly5 \
    mac-address=94:E1:AC:C4:A5:91 server="CCTV Network"
add address=10.20.1.120 client-id=1:94:e1:ac:b8:de:bc comment=Right9 \
    mac-address=94:E1:AC:B8:DE:BC server="CCTV Network"
add address=10.20.1.119 client-id=1:94:e1:ac:5a:30:53 comment="Hallway KG5" \
    mac-address=94:E1:AC:5A:30:53 server="CCTV Network"
add address=10.20.1.118 client-id=1:94:e1:ac:c4:a5:af comment=Assembly8 \
    mac-address=94:E1:AC:C4:A5:AF server="CCTV Network"
add address=10.20.1.115 client-id=1:94:e1:ac:5a:30:c1 comment=A101 \
    mac-address=94:E1:AC:5A:30:C1 server="CCTV Network"
add address=10.20.1.114 client-id=1:94:e1:ac:5a:30:f1 comment="Stud Affairs1" \
    mac-address=94:E1:AC:5A:30:F1 server="CCTV Network"
add address=10.20.1.113 client-id=1:4c:bd:8f:de:4c:2d comment=\
    "Entrance Lobby6" mac-address=4C:BD:8F:DE:4C:2D server="CCTV Network"
add address=10.20.1.112 client-id=1:94:e1:ac:5a:30:ed comment="Hallway KG4" \
    mac-address=94:E1:AC:5A:30:ED server="CCTV Network"
add address=10.20.1.111 client-id=1:94:e1:ac:78:79:e comment="Hallway KG9" \
    mac-address=94:E1:AC:78:79:0E server="CCTV Network"
add address=10.20.1.110 client-id=1:4c:bd:8f:de:4c:40 comment=\
    "Entrance Lobby3" mac-address=4C:BD:8F:DE:4C:40 server="CCTV Network"
add address=10.20.1.109 client-id=1:94:e1:ac:5a:30:af comment=Library1 \
    mac-address=94:E1:AC:5A:30:AF server="CCTV Network"
add address=10.20.1.108 client-id=1:4c:bd:8f:de:4b:d7 comment=\
    "A112 Amazon Jungle1" mac-address=4C:BD:8F:DE:4B:D7 server="CCTV Network"
add address=10.20.1.107 client-id=1:4c:bd:8f:de:4b:cf comment=\
    "A119 Infirmary1" mac-address=4C:BD:8F:DE:4B:CF server="CCTV Network"
add address=10.20.1.106 client-id=1:94:e1:ac:b8:df:1f comment=\
    "Kinder Backyard2" mac-address=94:E1:AC:B8:DF:1F server="CCTV Network"
add address=10.20.1.105 client-id=1:94:e1:ac:78:79:a6 comment=A134B \
    mac-address=94:E1:AC:78:79:A6 server="CCTV Network"
add address=10.20.1.103 client-id=1:4c:bd:8f:de:4c:14 comment=\
    "Entrance Lobby2" mac-address=4C:BD:8F:DE:4C:14 server="CCTV Network"
add address=10.20.1.102 client-id=1:94:e1:ac:5a:30:51 comment=A103 \
    mac-address=94:E1:AC:5A:30:51 server="CCTV Network"
add address=10.20.1.101 client-id=1:94:e1:ac:b8:df:15 comment=\
    "Kinder Backyard3" mac-address=94:E1:AC:B8:DF:15 server="CCTV Network"
add address=10.20.1.100 client-id=1:94:e1:ac:b8:df:8 comment=Left4 \
    mac-address=94:E1:AC:B8:DF:08 server="CCTV Network"
add address=10.20.1.99 client-id=1:4c:bd:8f:de:4c:2a comment="A111 Winter2" \
    mac-address=4C:BD:8F:DE:4C:2A server="CCTV Network"
add address=10.20.1.98 client-id=1:94:e1:ac:5a:30:16 comment=Library2 \
    mac-address=94:E1:AC:5A:30:16 server="CCTV Network"
add address=10.20.1.97 client-id=1:94:e1:ac:b8:df:11 comment=\
    "Kinder Backyard1" mac-address=94:E1:AC:B8:DF:11 server="CCTV Network"
add address=10.20.1.96 client-id=1:4c:bd:8f:de:4b:d4 comment="A110 Summer1" \
    mac-address=4C:BD:8F:DE:4B:D4 server="CCTV Network"
add address=10.20.1.95 client-id=1:94:e1:ac:5a:30:1a comment=\
    "A104C Meeting Room" mac-address=94:E1:AC:5A:30:1A server="CCTV Network"
add address=10.20.1.94 client-id=1:94:e1:ac:5a:31:d comment="Hallway Pri2" \
    mac-address=94:E1:AC:5A:31:0D server="CCTV Network"
add address=10.20.1.93 client-id=1:94:e1:ac:b8:df:19 comment=Left1 \
    mac-address=94:E1:AC:B8:DF:19 server="CCTV Network"
add address=10.20.1.92 client-id=1:94:e1:ac:b8:de:b3 comment=Assembly7 \
    mac-address=94:E1:AC:B8:DE:B3 server="CCTV Network"
add address=10.20.1.91 client-id=1:94:e1:ac:78:79:f4 comment="Lobby Elevator" \
    mac-address=94:E1:AC:78:79:F4 server="CCTV Network"
add address=10.20.1.90 client-id=1:94:e1:ac:c4:a5:62 comment=Assembly4 \
    mac-address=94:E1:AC:C4:A5:62 server="CCTV Network"
add address=10.20.1.89 client-id=1:94:e1:ac:c4:a5:8d comment=Assembly3 \
    mac-address=94:E1:AC:C4:A5:8D server="CCTV Network"
add address=10.20.1.88 client-id=1:94:e1:ac:b8:df:e comment=Assembly1 \
    mac-address=94:E1:AC:B8:DF:0E server="CCTV Network"
add address=10.20.1.87 client-id=1:94:e1:ac:5a:30:17 comment=Library4 \
    mac-address=94:E1:AC:5A:30:17 server="CCTV Network"
add address=10.20.1.86 client-id=1:94:e1:ac:5a:30:fa comment="Hallway Pri1" \
    mac-address=94:E1:AC:5A:30:FA server="CCTV Network"
add address=10.20.1.85 client-id=1:94:e1:ac:61:1:69 comment="Entrance Lobby9" \
    mac-address=94:E1:AC:61:01:69 server="CCTV Network"
add address=10.20.1.84 client-id=1:94:e1:ac:5a:30:56 comment="Hallway KG2" \
    mac-address=94:E1:AC:5A:30:56 server="CCTV Network"
add address=10.20.1.83 client-id=1:4c:bd:8f:de:4b:e0 comment=\
    "Entrance Lobby7" mac-address=4C:BD:8F:DE:4B:E0 server="CCTV Network"
add address=10.20.1.82 client-id=1:94:e1:ac:5a:30:5e comment="Hallway Pri3" \
    mac-address=94:E1:AC:5A:30:5E server="CCTV Network"
add address=10.0.0.106 mac-address=EC:EB:B8:CF:52:F4 server="COM-AP Network"
add address=10.0.0.107 mac-address=EC:EB:B8:CF:F2:E4 server="COM-AP Network"
add address=10.0.0.108 mac-address=EC:EB:B8:CF:72:A4 server="COM-AP Network"
add address=10.0.0.109 mac-address=EC:EB:B8:CF:82:FC server="COM-AP Network"
add address=10.0.0.110 mac-address=EC:EB:B8:CF:82:E0 server="COM-AP Network"
add address=10.0.0.112 client-id=1:cc:2d:e0:7c:55:9c mac-address=\
    CC:2D:E0:7C:55:9C server="COM-AP Network"
add address=10.20.1.62 mac-address=04:09:73:99:F8:20 server="CCTV Network"
add address=10.20.1.61 mac-address=04:09:73:99:5D:CC server="CCTV Network"
add address=10.0.0.113 client-id=1:cc:2d:e0:8c:57:dc mac-address=\
    CC:2D:E0:8C:57:DC server="COM-AP Network"
add address=10.0.0.114 client-id=1:cc:2d:e0:79:18:8d mac-address=\
    CC:2D:E0:79:18:8D server="COM-AP Network"
add address=10.20.1.60 mac-address=04:09:73:99:8D:10 server="CCTV Network"
add address=10.20.1.59 mac-address=04:09:73:99:ED:58 server="CCTV Network"
add address=10.0.0.115 client-id=1:cc:2d:e0:a5:4f:34 mac-address=\
    CC:2D:E0:A5:4F:34 server="COM-AP Network"
add address=10.20.1.58 mac-address=04:09:73:99:2F:78 server="CCTV Network"
add address=10.20.1.56 mac-address=04:09:73:99:5D:54 server="CCTV Network"
add address=10.0.0.124 client-id=1:cc:2d:e0:8c:56:9c mac-address=\
    CC:2D:E0:8C:56:9C server="COM-AP Network"
add address=10.0.0.125 client-id=1:cc:2d:e0:79:16:4d mac-address=\
    CC:2D:E0:79:16:4D server="COM-AP Network"
add address=10.0.0.126 client-id=1:cc:2d:e0:79:19:3d mac-address=\
    CC:2D:E0:79:19:3D server="COM-AP Network"
add address=10.0.0.127 client-id=1:cc:2d:e0:a5:53:4 mac-address=\
    CC:2D:E0:A5:53:04 server="COM-AP Network"
add address=10.0.0.135 client-id=1:cc:2d:e0:8c:57:a4 mac-address=\
    CC:2D:E0:8C:57:A4 server="COM-AP Network"
add address=10.0.0.136 client-id=1:cc:2d:e0:79:16:2d mac-address=\
    CC:2D:E0:79:16:2D server="COM-AP Network"
add address=10.0.0.137 client-id=1:cc:2d:e0:7c:56:dc mac-address=\
    CC:2D:E0:7C:56:DC server="COM-AP Network"
add address=10.0.0.138 client-id=1:cc:2d:e0:a5:4e:dc mac-address=\
    CC:2D:E0:A5:4E:DC server="COM-AP Network"
add address=10.0.0.140 client-id=1:cc:2d:e0:8c:5b:c mac-address=\
    CC:2D:E0:8C:5B:0C server="COM-AP Network"
add address=10.0.0.146 client-id=1:cc:2d:e0:79:19:1d mac-address=\
    CC:2D:E0:79:19:1D server="COM-AP Network"
add address=10.0.0.147 client-id=1:cc:2d:e0:79:15:95 mac-address=\
    CC:2D:E0:79:15:95 server="COM-AP Network"
add address=10.0.0.148 client-id=1:cc:2d:e0:7c:5a:fc mac-address=\
    CC:2D:E0:7C:5A:FC server="COM-AP Network"
add address=10.0.0.128 client-id=1:cc:2d:e0:79:18:5 mac-address=\
    CC:2D:E0:79:18:05 server="COM-AP Network"
add address=10.0.0.151 always-broadcast=yes client-id=1:cc:2d:e0:86:bb:40 \
    mac-address=CC:2D:E0:86:BB:40 server="COM-AP Network"
add address=10.0.0.207 client-id=1:cc:2d:e0:7c:54:bc mac-address=\
    CC:2D:E0:7C:54:BC server="COM-AP Network"
add address=10.0.0.129 client-id=1:cc:2d:e0:79:13:75 mac-address=\
    CC:2D:E0:79:13:75 server="COM-AP Network"
add address=10.0.0.134 client-id=1:cc:2d:e0:79:15:55 mac-address=\
    CC:2D:E0:79:15:55 server="COM-AP Network"
add address=10.20.1.53 client-id=1:94:e1:ac:61:1:37 comment=MPR4 mac-address=\
    94:E1:AC:61:01:37 server="CCTV Network"
add address=10.20.1.52 client-id=1:94:e1:ac:61:1:15 comment=MPR2 mac-address=\
    94:E1:AC:61:01:15 server="CCTV Network"
add address=10.20.1.44 client-id=1:94:e1:ac:b8:de:e8 comment="Gym 1" \
    mac-address=94:E1:AC:B8:DE:E8 server="CCTV Network"
add address=10.20.1.43 client-id=1:94:e1:ac:b8:de:d1 comment="Gym 2" \
    mac-address=94:E1:AC:B8:DE:D1 server="CCTV Network"
add address=10.20.1.42 client-id=1:94:e1:ac:b8:de:c7 comment="Gym 3" \
    mac-address=94:E1:AC:B8:DE:C7 server="CCTV Network"
add address=10.20.1.41 client-id=1:94:e1:ac:b8:de:af comment="Gym 4" \
    mac-address=94:E1:AC:B8:DE:AF server="CCTV Network"
add address=10.20.1.40 client-id=1:94:e1:ac:b8:de:df comment="Gym 5" \
    mac-address=94:E1:AC:B8:DE:DF server="CCTV Network"
add address=10.20.1.39 client-id=1:94:e1:ac:c4:a5:a8 comment="Gym 6" \
    mac-address=94:E1:AC:C4:A5:A8 server="CCTV Network"
add address=10.20.1.38 always-broadcast=yes client-id=1:94:e1:ac:c4:a5:a7 \
    comment="Gym 7" mac-address=94:E1:AC:C4:A5:A7 server="CCTV Network"
add address=10.20.1.37 client-id=1:94:e1:ac:c4:a5:7f comment="Gym 8" \
    mac-address=94:E1:AC:C4:A5:7F server="CCTV Network"
add address=10.20.1.36 client-id=1:94:e1:ac:c4:a5:90 comment="Gym 9" \
    mac-address=94:E1:AC:C4:A5:90 server="CCTV Network"
add address=10.20.1.35 client-id=1:94:e1:ac:c4:a5:ac comment="Gym 10" \
    mac-address=94:E1:AC:C4:A5:AC server="CCTV Network"
add address=10.20.1.34 client-id=1:94:e1:ac:c4:a5:be comment="Pool 1" \
    mac-address=94:E1:AC:C4:A5:BE server="CCTV Network"
add address=10.20.1.33 client-id=1:94:e1:ac:c4:a5:bc comment="Pool 2" \
    mac-address=94:E1:AC:C4:A5:BC server="CCTV Network"
add address=10.20.1.32 client-id=1:94:e1:ac:c4:a5:83 comment="Pool 3" \
    mac-address=94:E1:AC:C4:A5:83 server="CCTV Network"
add address=10.20.1.31 client-id=1:94:e1:ac:c4:a5:76 comment="Outdoor 1" \
    mac-address=94:E1:AC:C4:A5:76 server="CCTV Network"
add address=10.20.1.30 client-id=1:94:e1:ac:c4:a5:a0 comment="Outdoor gym1" \
    mac-address=94:E1:AC:C4:A5:A0 server="CCTV Network"
add address=10.20.1.29 client-id=1:94:e1:ac:b8:df:1 comment="Outdoor gym 2" \
    mac-address=94:E1:AC:B8:DF:01 server="CCTV Network"
add address=10.20.1.28 client-id=1:94:e1:ac:c4:a5:70 comment="Outdoor gym 3" \
    mac-address=94:E1:AC:C4:A5:70 server="CCTV Network"
add address=10.20.1.27 client-id=1:94:e1:ac:b8:de:b8 comment="Outdoor gym 4" \
    mac-address=94:E1:AC:B8:DE:B8 server="CCTV Network"
add address=10.20.1.26 client-id=1:94:e1:ac:b8:de:fa comment="Outdoor gym 5" \
    mac-address=94:E1:AC:B8:DE:FA server="CCTV Network"
add address=10.20.1.25 client-id=1:94:e1:ac:b8:de:eb comment="Outdoor gym 6" \
    mac-address=94:E1:AC:B8:DE:EB server="CCTV Network"
add address=10.20.1.24 client-id=1:94:e1:ac:b8:de:fe comment="Outdoor gym 7" \
    mac-address=94:E1:AC:B8:DE:FE server="CCTV Network"
add address=10.20.1.23 client-id=1:94:e1:ac:b8:de:b5 comment="Topview Gym10" \
    mac-address=94:E1:AC:B8:DE:B5 server="CCTV Network"
add address=10.20.1.21 client-id=1:94:e1:ac:c4:a5:66 comment=Canteen7 \
    mac-address=94:E1:AC:C4:A5:66 server="CCTV Network"
add address=10.20.1.20 client-id=1:94:e1:ac:c4:a5:7e comment=\
    "Outdoor Canteen2" mac-address=94:E1:AC:C4:A5:7E server="CCTV Network"
add address=10.20.1.19 client-id=1:94:e1:ac:b8:de:e5 comment=Field4 \
    mac-address=94:E1:AC:B8:DE:E5 server="CCTV Network"
add address=10.20.1.18 client-id=1:94:e1:ac:c4:a5:9f comment=\
    "Canteen Backdoor" mac-address=94:E1:AC:C4:A5:9F server="CCTV Network"
add address=10.20.1.17 client-id=1:94:e1:ac:61:1:32 comment=\
    "A211 Babylonian2" mac-address=94:E1:AC:61:01:32 server="CCTV Network"
add address=10.20.1.16 client-id=1:94:e1:ac:b8:de:b6 comment=Field3 \
    mac-address=94:E1:AC:B8:DE:B6 server="CCTV Network"
add address=10.20.1.15 client-id=1:94:e1:ac:c4:a5:c1 comment=Right8 \
    mac-address=94:E1:AC:C4:A5:C1 server="CCTV Network"
add address=10.20.1.14 client-id=1:94:e1:ac:c4:a5:b9 comment=Field1 \
    mac-address=94:E1:AC:C4:A5:B9 server="CCTV Network"
add address=10.20.1.13 client-id=1:94:e1:ac:61:1:8 comment=Canteen4 \
    mac-address=94:E1:AC:61:01:08 server="CCTV Network"
add address=10.20.1.11 client-id=1:94:e1:ac:5a:30:f0 comment="Stud Affairs6" \
    mac-address=94:E1:AC:5A:30:F0 server="CCTV Network"
add address=10.20.1.9 client-id=1:94:e1:ac:c4:a5:75 comment="Canteen 2" \
    mac-address=94:E1:AC:C4:A5:75 server="CCTV Network"
add address=10.20.2.26 client-id=1:94:e1:ac:61:1:6d comment=Canteen4 \
    mac-address=94:E1:AC:61:01:6D server="CCTV Network"
add address=10.20.1.7 client-id=1:94:e1:ac:61:1:51 comment="canteen 3" \
    mac-address=94:E1:AC:61:01:51 server="CCTV Network"
add address=10.20.1.6 client-id=1:94:e1:ac:c4:a5:b0 comment="Outdoor f.field" \
    mac-address=94:E1:AC:C4:A5:B0 server="CCTV Network"
add address=10.20.2.213 client-id=1:94:e1:ac:c4:a5:77 comment="Gym plants2" \
    mac-address=94:E1:AC:C4:A5:77 server="CCTV Network"
add address=10.20.1.46 client-id=1:94:e1:ac:b8:df:1d comment=Aquarium1 \
    mac-address=94:E1:AC:B8:DF:1D server="CCTV Network"
add address=10.20.1.50 client-id=1:94:e1:ac:b8:df:d comment=Left5 \
    mac-address=94:E1:AC:B8:DF:0D server="CCTV Network"
add address=10.20.1.51 client-id=1:94:e1:ac:c4:a5:79 comment=Field5 \
    mac-address=94:E1:AC:C4:A5:79 server="CCTV Network"
add address=10.20.1.54 client-id=1:94:e1:ac:b8:de:cc comment="Gym Entrance" \
    mac-address=94:E1:AC:B8:DE:CC server="CCTV Network"
add address=10.20.1.55 client-id=1:4c:bd:8f:de:4c:3a comment="A117 Playroom4" \
    mac-address=4C:BD:8F:DE:4C:3A server="CCTV Network"
add address=10.20.1.64 client-id=1:94:e1:ac:78:79:f0 comment="A203 Mr. Sam" \
    mac-address=94:E1:AC:78:79:F0 server="CCTV Network"
add address=10.20.1.65 client-id=1:94:e1:ac:5a:31:5 comment="A104A Ms. Tum" \
    mac-address=94:E1:AC:5A:31:05 server="CCTV Network"
add address=10.20.1.66 client-id=1:94:e1:ac:61:1:82 comment=Canteen3 \
    mac-address=94:E1:AC:61:01:82 server="CCTV Network"
add address=10.20.1.67 client-id=1:94:e1:ac:78:78:2f comment=A202-A \
    mac-address=94:E1:AC:78:78:2F server="CCTV Network"
add address=10.20.1.68 client-id=1:94:e1:ac:78:79:d2 comment="Stairs 2nd/3rd" \
    mac-address=94:E1:AC:78:79:D2 server="CCTV Network"
add address=10.20.1.69 client-id=1:94:e1:ac:c4:a5:b7 comment=Field2 \
    mac-address=94:E1:AC:C4:A5:B7 server="CCTV Network"
add address=10.20.1.70 client-id=1:b4:a3:82:13:3:2 comment="360 1st entrnce" \
    mac-address=B4:A3:82:13:03:02 server="CCTV Network"
add address=10.20.1.72 client-id=1:b4:a3:82:13:2:cd comment="360 2nd flr" \
    mac-address=B4:A3:82:13:02:CD server="CCTV Network"
add address=10.0.0.143 always-broadcast=yes client-id=1:f8:bc:12:6b:3a:f2 \
    mac-address=F8:BC:12:6B:3A:F2 server="COM-AP Network"
add address=10.20.1.77 client-id=1:94:e1:ac:78:78:a7 comment="Stairs 3rd" \
    mac-address=94:E1:AC:78:78:A7 server="CCTV Network"
add address=10.20.1.78 client-id=1:94:e1:ac:78:79:ea comment="Library ctr1" \
    mac-address=94:E1:AC:78:79:EA server="CCTV Network"
add address=10.20.1.79 client-id=1:94:e1:ac:78:79:ff comment="Library ctr2" \
    mac-address=94:E1:AC:78:79:FF server="CCTV Network"
add address=10.20.1.249 client-id=1:94:e1:ac:61:1:3f comment=Lobby2 \
    mac-address=94:E1:AC:61:01:3F server="CCTV Network"
add address=10.20.1.252 client-id=1:94:e1:ac:61:1:d comment="Acctg Cashier" \
    mac-address=94:E1:AC:61:01:0D server="CCTV Network"
add address=10.20.1.253 client-id=1:94:e1:ac:61:1:63 comment=Lobby1 \
    mac-address=94:E1:AC:61:01:63 server="CCTV Network"
add address=10.20.1.71 client-id=1:94:e1:ac:5a:30:fd comment="Hallway KG10" \
    mac-address=94:E1:AC:5A:30:FD server="CCTV Network"
add address=10.20.1.73 client-id=1:94:e1:ac:c4:a5:6b comment=\
    "Kinder Backyard6" mac-address=94:E1:AC:C4:A5:6B server="CCTV Network"
add address=10.20.1.45 client-id=1:94:e1:ac:c4:a5:6e comment=\
    "Kinder Backyard4" mac-address=94:E1:AC:C4:A5:6E server="CCTV Network"
add address=10.20.1.8 client-id=1:94:e1:ac:c4:a5:68 comment=\
    "Pool Area t.view" mac-address=94:E1:AC:C4:A5:68 server="CCTV Network"
add address=10.20.2.254 client-id=1:94:e1:ac:c4:a5:ab comment=\
    "Outdoor Canteen3" mac-address=94:E1:AC:C4:A5:AB server="CCTV Network"
add address=10.20.2.253 client-id=1:94:e1:ac:c4:a5:b4 comment=\
    "Outdoor Canteen1" mac-address=94:E1:AC:C4:A5:B4 server="CCTV Network"
add address=10.20.2.250 client-id=1:94:e1:ac:5a:30:ba comment="F.exit A217" \
    mac-address=94:E1:AC:5A:30:BA server="CCTV Network"
add address=10.20.2.249 client-id=1:94:e1:ac:78:78:ea comment=\
    "A104B Mr. Charles" mac-address=94:E1:AC:78:78:EA server="CCTV Network"
add address=10.20.2.248 client-id=1:94:e1:ac:78:78:d5 comment="F.exit Field" \
    mac-address=94:E1:AC:78:78:D5 server="CCTV Network"
add address=10.20.2.247 client-id=1:4c:bd:8f:de:4c:25 comment="A105 Candy1" \
    mac-address=4C:BD:8F:DE:4C:25 server="CCTV Network"
add address=10.20.2.246 client-id=1:94:e1:ac:b8:de:ed comment=GH3 \
    mac-address=94:E1:AC:B8:DE:ED server="CCTV Network"
add address=10.20.2.245 client-id=1:94:e1:ac:b8:df:f comment=GH2 mac-address=\
    94:E1:AC:B8:DF:0F server="CCTV Network"
add address=10.20.2.244 client-id=1:94:e1:ac:b8:df:10 comment=GH4 \
    mac-address=94:E1:AC:B8:DF:10 server="CCTV Network"
add address=10.20.2.243 client-id=1:94:e1:ac:b8:de:dc comment=GH1 \
    mac-address=94:E1:AC:B8:DE:DC server="CCTV Network"
add address=10.0.1.151 client-id=1:cc:2d:e0:a5:54:8c mac-address=\
    CC:2D:E0:A5:54:8C server="COM-AP Network"
add address=10.0.0.179 client-id=1:cc:2d:e0:95:3b:ef mac-address=\
    CC:2D:E0:95:3B:EF server="COM-AP Network"
add address=10.0.1.168 client-id=1:cc:2d:e0:8c:5d:5c mac-address=\
    CC:2D:E0:8C:5D:5C server="COM-AP Network"
add address=10.20.2.240 client-id=1:94:e1:ac:c4:a5:9a comment=Assembly10 \
    mac-address=94:E1:AC:C4:A5:9A server="CCTV Network"
add address=10.20.1.74 client-id=1:94:e1:ac:b8:de:fd comment=Pool2 \
    mac-address=94:E1:AC:B8:DE:FD server="CCTV Network"
add address=10.20.2.236 client-id=1:94:e1:ac:b8:de:d0 comment="Topview Gym11" \
    mac-address=94:E1:AC:B8:DE:D0 server="CCTV Network"
add address=10.20.2.233 client-id=1:94:e1:ac:b8:de:c2 comment="Topview Gym13" \
    mac-address=94:E1:AC:B8:DE:C2 server="CCTV Network"
add address=10.20.2.231 client-id=1:94:e1:ac:b8:df:1b comment="Top View Ctn" \
    mac-address=94:E1:AC:B8:DF:1B server="CCTV Network"
add address=10.20.2.229 client-id=1:94:e1:ac:b8:de:bb comment="Topview Gym15" \
    mac-address=94:E1:AC:B8:DE:BB server="CCTV Network"
add address=10.20.2.228 client-id=1:94:e1:ac:78:78:57 comment="F.exit ctn" \
    mac-address=94:E1:AC:78:78:57 server="CCTV Network"
add address=10.20.2.225 client-id=1:94:e1:ac:78:78:b4 comment="F.exit KG" \
    mac-address=94:E1:AC:78:78:B4 server="CCTV Network"
add address=10.20.2.222 client-id=1:94:e1:ac:78:78:33 comment=\
    "A106 Noah Ark2" mac-address=94:E1:AC:78:78:33 server="CCTV Network"
add address=10.20.2.220 client-id=1:94:e1:ac:61:1:28 comment="A116 Spring2" \
    mac-address=94:E1:AC:61:01:28 server="CCTV Network"
add address=10.20.2.218 client-id=1:4c:bd:8f:de:4c:e comment="A116 Spring1" \
    mac-address=4C:BD:8F:DE:4C:0E server="CCTV Network"
add address=10.20.2.217 client-id=1:94:e1:ac:c4:a5:96 comment="Car Park1" \
    mac-address=94:E1:AC:C4:A5:96 server="CCTV Network"
add address=10.20.2.216 client-id=1:94:e1:ac:c4:a5:b5 comment="Car Park2" \
    mac-address=94:E1:AC:C4:A5:B5 server="CCTV Network"
add address=10.20.2.215 client-id=1:94:e1:ac:c4:a5:6d comment="Car Park4" \
    mac-address=94:E1:AC:C4:A5:6D server="CCTV Network"
add address=10.20.2.214 client-id=1:94:e1:ac:c4:a5:5f comment="Car Park3" \
    mac-address=94:E1:AC:C4:A5:5F server="CCTV Network"
add address=10.0.1.49 client-id=1:cc:2d:e0:79:17:95 mac-address=\
    CC:2D:E0:79:17:95 server="COM-AP Network"
add address=10.0.1.50 client-id=1:cc:2d:e0:8c:5a:7c mac-address=\
    CC:2D:E0:8C:5A:7C server="COM-AP Network"
add address=10.0.1.53 client-id=1:cc:2d:e0:ab:26:0 mac-address=\
    CC:2D:E0:AB:26:00 server="COM-AP Network"
add address=10.0.1.54 client-id=1:cc:2d:e0:8c:5a:bc mac-address=\
    CC:2D:E0:8C:5A:BC server="COM-AP Network"
add address=10.20.2.237 client-id=1:94:e1:ac:c4:a5:72 comment=Pool2 \
    mac-address=94:E1:AC:C4:A5:72 server="CCTV Network"
add address=10.20.2.232 client-id=1:94:e1:ac:c4:a5:8a comment=Pool1 \
    mac-address=94:E1:AC:C4:A5:8A server="CCTV Network"
add address=10.20.2.227 always-broadcast=yes client-id=1:94:e1:ac:c4:a5:a3 \
    comment=Pool2 mac-address=94:E1:AC:C4:A5:A3 server="CCTV Network"
add address=10.20.2.224 client-id=1:94:e1:ac:c4:a5:69 comment=Pool4 \
    mac-address=94:E1:AC:C4:A5:69 server="CCTV Network"
add address=10.20.2.221 client-id=1:94:e1:ac:c4:a5:ae comment="Pool Entrance" \
    mac-address=94:E1:AC:C4:A5:AE server="CCTV Network"
add address=10.20.2.212 client-id=1:94:e1:ac:78:78:a9 comment="Pool Hallway" \
    mac-address=94:E1:AC:78:78:A9 server="CCTV Network"
add address=10.20.2.210 client-id=1:94:e1:ac:c4:a5:a1 comment=Pool3 \
    mac-address=94:E1:AC:C4:A5:A1 server="CCTV Network"
add address=10.20.2.226 client-id=1:94:e1:ac:61:1:58 comment=Canteen8 \
    mac-address=94:E1:AC:61:01:58 server="CCTV Network"
add address=10.20.2.223 client-id=1:4c:bd:8f:de:4b:fa comment=\
    "A216 Chem lab2" mac-address=4C:BD:8F:DE:4B:FA server="CCTV Network"
add address=10.20.2.209 client-id=1:94:e1:ac:c4:a5:ba comment=Right1 \
    mac-address=94:E1:AC:C4:A5:BA server="CCTV Network"
add address=10.20.2.208 client-id=1:94:e1:ac:c4:a5:b6 comment=Canteen5 \
    mac-address=94:E1:AC:C4:A5:B6 server="CCTV Network"
add address=10.20.2.207 client-id=1:94:e1:ac:c4:a5:a4 comment="Top view GH" \
    mac-address=94:E1:AC:C4:A5:A4 server="CCTV Network"
add address=10.20.2.206 client-id=1:94:e1:ac:b8:de:f4 comment=Right3 \
    mac-address=94:E1:AC:B8:DE:F4 server="CCTV Network"
add address=10.20.1.104 mac-address=04:09:73:FD:B3:48 server="CCTV Network"
add address=10.0.0.118 always-broadcast=yes client-id=1:b4:74:9f:6d:74:87 \
    mac-address=B4:74:9F:6D:74:87 server="COM-AP Network"
add address=10.20.2.219 client-id=1:94:e1:ac:c4:a5:b1 comment=Canteen10 \
    mac-address=94:E1:AC:C4:A5:B1 server="CCTV Network"
add address=10.20.1.12 client-id=1:94:e1:ac:b8:df:c comment=Field8 \
    mac-address=94:E1:AC:B8:DF:0C server="CCTV Network"
add address=10.0.0.249 client-id=1:cc:2d:e0:7c:5b:9c mac-address=\
    CC:2D:E0:7C:5B:9C server="COM-AP Network"
add address=10.20.2.205 client-id=1:94:e1:ac:78:7a:8 comment=Library5 \
    mac-address=94:E1:AC:78:7A:08 server="CCTV Network"
add address=10.20.2.242 client-id=1:4c:bd:8f:5:3b:f3 comment="Stairs 1st/2nd" \
    mac-address=4C:BD:8F:05:3B:F3 server="CCTV Network"
add address=10.20.2.241 always-broadcast=yes client-id=1:94:e1:ac:b8:de:ca \
    comment="Topview Gym18" mac-address=94:E1:AC:B8:DE:CA server=\
    "CCTV Network"
add address=10.20.2.239 client-id=1:94:e1:ac:78:78:40 comment="F.exit 3rd" \
    mac-address=94:E1:AC:78:78:40 server="CCTV Network"
add address=10.20.2.203 client-id=1:94:e1:ac:78:79:24 comment="Hallway Pri5" \
    mac-address=94:E1:AC:78:79:24 server="CCTV Network"
add address=10.20.2.201 client-id=1:94:e1:ac:78:79:a comment=\
    "Corridor Staff-IT" mac-address=94:E1:AC:78:79:0A server="CCTV Network"
add address=10.20.2.199 client-id=1:94:e1:ac:c4:a5:a6 comment=Canteen9 \
    mac-address=94:E1:AC:C4:A5:A6 server="CCTV Network"
add address=10.20.2.197 client-id=1:94:e1:ac:b8:de:f5 comment=Left1 \
    mac-address=94:E1:AC:B8:DE:F5 server="CCTV Network"
add address=10.20.2.195 client-id=1:94:e1:ac:c4:a5:7d comment=\
    "Kinder Backyard8" mac-address=94:E1:AC:C4:A5:7D server="CCTV Network"
add address=10.20.2.193 client-id=1:94:e1:ac:b8:df:17 comment=\
    "Kinder Backyard7" mac-address=94:E1:AC:B8:DF:17 server="CCTV Network"
add address=10.20.2.191 client-id=1:4c:bd:8f:de:4b:cd comment=\
    "Entrance Lobby8" mac-address=4C:BD:8F:DE:4B:CD server="CCTV Network"
add address=10.20.2.189 client-id=1:94:e1:ac:78:79:9c comment="Library stock" \
    mac-address=94:E1:AC:78:79:9C server="CCTV Network"
add address=10.20.2.187 client-id=1:4c:bd:8f:de:4c:49 comment=\
    "A117 Playroom3" mac-address=4C:BD:8F:DE:4C:49 server="CCTV Network"
add address=10.20.1.76 client-id=1:4c:bd:8f:de:4c:2f comment=\
    "A226 Staff Room3" mac-address=4C:BD:8F:DE:4C:2F server="CCTV Network"
add address=10.20.2.196 client-id=1:94:e1:ac:b8:de:e1 comment=Right7 \
    mac-address=94:E1:AC:B8:DE:E1 server="CCTV Network"
add address=10.20.2.190 client-id=1:94:e1:ac:b8:df:2 comment="Gym plants1" \
    mac-address=94:E1:AC:B8:DF:02 server="CCTV Network"
add address=10.0.0.170 client-id=1:a4:83:e7:46:25:49 mac-address=\
    A4:83:E7:46:25:49 server="COM-AP Network"
add address=10.0.1.230 client-id=1:f0:76:1c:6c:29:8e mac-address=\
    F0:76:1C:6C:29:8E server="COM-AP Network"
add address=10.0.1.141 client-id=1:e4:b9:7a:f8:bd:8b mac-address=\
    E4:B9:7A:F8:BD:8B server="COM-AP Network"
add address=10.0.1.51 client-id=1:8c:ec:4b:5b:3b:d4 mac-address=\
    8C:EC:4B:5B:3B:D4 server="COM-AP Network"
add address=10.0.0.158 client-id=1:90:b1:1c:5d:35:9e mac-address=\
    90:B1:1C:5D:35:9E server="COM-AP Network"
add address=10.20.2.230 client-id=1:94:e1:ac:78:78:d9 comment=A202-B \
    mac-address=94:E1:AC:78:78:D9 server="CCTV Network"
add address=10.20.2.204 client-id=1:94:e1:ac:78:79:3d comment=A202 \
    mac-address=94:E1:AC:78:79:3D server="CCTV Network"
add address=10.20.2.202 client-id=1:94:e1:ac:78:7a:5c comment=\
    "Canteen Entrance" mac-address=94:E1:AC:78:7A:5C server="CCTV Network"
add address=10.0.1.206 client-id=1:2c:ea:7f:da:80:95 comment=\
    "Quickbook Server" mac-address=2C:EA:7F:DA:80:95 server="COM-AP Network"
add address=10.0.0.142 client-id=1:98:d8:63:76:89:a7 comment=\
    "Solar Man 3rd flr" mac-address=98:D8:63:76:89:A7 server="COM-AP Network"
add address=10.20.1.81 client-id=1:4c:bd:8f:de:4c:15 comment=\
    "Entrance Lobby5" mac-address=4C:BD:8F:DE:4C:15 server="CCTV Network"
add address=10.20.2.185 client-id=1:94:e1:ac:c4:a5:7c comment=S.Pool2 \
    mac-address=94:E1:AC:C4:A5:7C server="CCTV Network"
add address=10.0.1.74 client-id=1:8c:ec:4b:6d:59:b7 mac-address=\
    8C:EC:4B:6D:59:B7 server="COM-AP Network"
add address=10.0.0.176 mac-address=04:09:73:FD:F3:20 server="COM-AP Network"
add address=10.0.1.237 client-id=1:24:5e:be:51:73:a5 comment="QNAP Local" \
    mac-address=24:5E:BE:51:73:A5 server="COM-AP Network"
add address=10.0.0.111 mac-address=04:09:73:FD:F3:48 server="COM-AP Network"
add address=10.0.1.8 client-id=1:cc:2d:e0:79:f:55 mac-address=\
    CC:2D:E0:79:0F:55 server="COM-AP Network"
add address=10.20.2.198 client-id=1:94:e1:ac:78:78:49 comment="Solar Panel" \
    mac-address=94:E1:AC:78:78:49 server="CCTV Network"
add address=10.20.2.192 client-id=1:94:e1:ac:75:ba:53 comment=\
    "F.exit A230 IT" mac-address=94:E1:AC:75:BA:53 server="CCTV Network"
add address=10.0.0.120 mac-address=04:09:73:FD:6B:00 server="COM-AP Network"
add address=10.0.0.104 mac-address=EC:EB:B8:CF:92:04 server="COM-AP Network"
add address=10.0.0.105 mac-address=04:09:73:FD:5B:88 server="COM-AP Network"
add address=10.20.1.48 comment="CCTV Switch" mac-address=D0:67:26:A4:CA:D4 \
    server="CCTV Network"
add address=10.20.2.184 client-id=1:b4:a3:82:13:2:ce comment=\
    "360 1st drp off" mac-address=B4:A3:82:13:02:CE server="CCTV Network"
add address=10.0.0.145 client-id=1:cc:2d:e0:a5:58:84 mac-address=\
    CC:2D:E0:A5:58:84 server="COM-AP Network"
add address=10.20.1.49 mac-address=D0:67:26:A4:FB:2C server="CCTV Network"
add address=10.0.0.103 mac-address=04:09:73:FD:5B:B4 server="COM-AP Network"
add address=10.0.0.101 mac-address=EC:EB:B8:CF:03:AC server="COM-AP Network"
add address=10.20.2.194 client-id=4431.9206.8d41-Vlan-interface1 mac-address=\
    44:31:92:06:8D:41 server="CCTV Network"
add address=10.0.0.122 client-id=1:a0:2b:b8:a:87:60 mac-address=\
    A0:2B:B8:0A:87:60 server="COM-AP Network"
add address=10.20.2.183 client-id=1:94:e1:ac:b8:de:c3 comment=Right4 \
    mac-address=94:E1:AC:B8:DE:C3 server="CCTV Network"
add address=10.0.1.106 client-id=1:64:0:6a:36:10:52 mac-address=\
    64:00:6A:36:10:52 server="COM-AP Network"
add address=10.0.1.0 client-id=1:8c:ec:4b:6c:81:db mac-address=\
    8C:EC:4B:6C:81:DB server="COM-AP Network"
add address=10.20.2.186 client-id=1:94:e1:ac:c4:a5:9d comment=Left3 \
    mac-address=94:E1:AC:C4:A5:9D server="CCTV Network"
add address=10.20.1.75 mac-address=D0:67:26:A4:1E:9C server="CCTV Network"
add address=10.20.2.234 client-id=1:98:d8:63:3e:71:23 comment=\
    "Solar Man 2(gym)" mac-address=98:D8:63:3E:71:23 server="CCTV Network"
add address=10.0.0.226 client-id=1:cc:2d:e0:79:13:55 mac-address=\
    CC:2D:E0:79:13:55 server="COM-AP Network"
add address=10.20.2.179 client-id=1:94:e1:ac:78:79:59 comment="Hallway Acctg" \
    mac-address=94:E1:AC:78:79:59 server="CCTV Network"
add address=10.20.2.177 client-id=1:94:e1:ac:78:79:64 comment="Stud Affairs5" \
    mac-address=94:E1:AC:78:79:64 server="CCTV Network"
add address=10.20.2.238 mac-address=08:F1:EA:13:9A:8C server="CCTV Network"
add address=10.20.2.181 client-id=1:b4:a3:82:13:3:a comment="360 Auditorium" \
    mac-address=B4:A3:82:13:03:0A server="CCTV Network"
add address=10.20.2.175 client-id=1:94:e1:ac:75:ba:51 comment=A309 \
    mac-address=94:E1:AC:75:BA:51 server="CCTV Network"
add address=10.20.1.10 mac-address=D0:67:26:A4:BA:8C server="CCTV Network"
add address=10.0.1.250 client-id=1:8c:ec:4b:6d:e5:2e mac-address=\
    8C:EC:4B:6D:E5:2E server="COM-AP Network"
add address=10.0.1.152 client-id=1:8c:ec:4b:6d:53:6b mac-address=\
    8C:EC:4B:6D:53:6B server="COM-AP Network"
add address=10.0.0.236 client-id=1:8c:ec:4b:6d:54:bc mac-address=\
    8C:EC:4B:6D:54:BC server="COM-AP Network"
add address=10.0.1.58 client-id=1:8c:ec:4b:6d:54:90 comment=A115 mac-address=\
    8C:EC:4B:6D:54:90 server="COM-AP Network"
add address=10.0.1.131 client-id=1:8c:ec:4b:6d:6:ec mac-address=\
    8C:EC:4B:6D:06:EC server="COM-AP Network"
add address=10.0.0.219 client-id=1:8c:ec:4b:6d:58:c2 mac-address=\
    8C:EC:4B:6D:58:C2 server="COM-AP Network"
add address=10.0.1.179 client-id=1:90:b1:1c:5d:33:68 mac-address=\
    90:B1:1C:5D:33:68 server="COM-AP Network"
add address=10.0.1.97 client-id=1:8c:ec:4b:6c:80:2f comment=A114 mac-address=\
    8C:EC:4B:6C:80:2F server="COM-AP Network"
add address=10.0.1.223 client-id=1:48:4d:7e:be:9c:da mac-address=\
    48:4D:7E:BE:9C:DA server="COM-AP Network"
add address=10.0.1.33 client-id=1:8c:ec:4b:6c:82:ba mac-address=\
    8C:EC:4B:6C:82:BA server="COM-AP Network"
add address=10.0.1.190 client-id=1:8c:ec:4b:6d:58:d4 mac-address=\
    8C:EC:4B:6D:58:D4 server="COM-AP Network"
add address=10.0.1.90 client-id=1:8c:ec:4b:6d:5b:a comment=A110 mac-address=\
    8C:EC:4B:6D:5B:0A server="COM-AP Network"
add address=10.0.0.162 client-id=1:f8:bc:12:5b:f4:37 mac-address=\
    F8:BC:12:5B:F4:37 server="COM-AP Network"
add address=10.0.0.186 client-id=1:90:b1:1c:5d:30:63 mac-address=\
    90:B1:1C:5D:30:63 server="COM-AP Network"
add address=10.0.1.60 client-id=1:8c:ec:4b:6f:d6:26 mac-address=\
    8C:EC:4B:6F:D6:26 server="COM-AP Network"
add address=10.0.1.14 client-id=1:64:0:6a:3f:78:f6 mac-address=\
    64:00:6A:3F:78:F6 server="COM-AP Network"
add address=10.0.0.231 client-id=1:8c:ec:4b:6f:89:91 mac-address=\
    8C:EC:4B:6F:89:91 server="COM-AP Network"
add address=10.0.1.158 client-id=1:ec:b1:d7:42:c1:cf mac-address=\
    EC:B1:D7:42:C1:CF server="COM-AP Network"
add address=10.0.1.154 client-id=1:8c:ec:4b:6c:80:7 mac-address=\
    8C:EC:4B:6C:80:07 server="COM-AP Network"
add address=10.0.1.203 client-id=1:8c:ec:4b:6f:8a:78 mac-address=\
    8C:EC:4B:6F:8A:78 server="COM-AP Network"
add address=10.0.1.142 client-id=1:8c:ec:4b:6c:7e:bb comment=A116 \
    mac-address=8C:EC:4B:6C:7E:BB server="COM-AP Network"
add address=10.0.1.145 client-id=1:8c:dc:d4:52:43:b3 mac-address=\
    8C:DC:D4:52:43:B3 server="COM-AP Network"
add address=10.0.1.92 client-id=1:48:4d:7e:bf:40:be mac-address=\
    48:4D:7E:BF:40:BE server="COM-AP Network"
add address=10.0.1.57 client-id=1:f0:92:1c:58:c4:bc mac-address=\
    F0:92:1C:58:C4:BC server="COM-AP Network"
add address=10.0.1.251 client-id=1:8c:ec:4b:6f:8d:b5 mac-address=\
    8C:EC:4B:6F:8D:B5 server="COM-AP Network"
add address=10.0.1.156 client-id=1:8c:ec:4b:6b:91:25 mac-address=\
    8C:EC:4B:6B:91:25 server="COM-AP Network"
add address=10.0.1.119 client-id=1:8c:ec:4b:6d:58:ca mac-address=\
    8C:EC:4B:6D:58:CA server="COM-AP Network"
add address=10.0.1.159 client-id=1:8c:ec:4b:6c:84:2b mac-address=\
    8C:EC:4B:6C:84:2B server="COM-AP Network"
add address=10.0.0.149 client-id=1:f8:bc:12:6b:3b:1 mac-address=\
    F8:BC:12:6B:3B:01 server="COM-AP Network"
add address=10.0.0.250 client-id=1:f8:bc:12:69:c1:a6 mac-address=\
    F8:BC:12:69:C1:A6 server="COM-AP Network"
add address=10.0.1.135 client-id=1:f8:bc:12:5b:f6:de mac-address=\
    F8:BC:12:5B:F6:DE server="COM-AP Network"
add address=10.0.0.248 client-id=1:f8:bc:12:6a:76:cf mac-address=\
    F8:BC:12:6A:76:CF server="COM-AP Network"
add address=10.0.1.128 client-id=1:f8:bc:12:6b:2e:48 mac-address=\
    F8:BC:12:6B:2E:48 server="COM-AP Network"
add address=10.0.1.130 client-id=1:e4:b9:7a:ea:22:9f mac-address=\
    E4:B9:7A:EA:22:9F server="COM-AP Network"
add address=10.0.1.100 client-id=1:f8:bc:12:6a:76:b2 mac-address=\
    F8:BC:12:6A:76:B2 server="COM-AP Network"
add address=10.0.1.120 client-id=1:8c:ec:4b:5b:3b:a1 mac-address=\
    8C:EC:4B:5B:3B:A1 server="COM-AP Network"
add address=10.0.1.252 client-id=1:8c:ec:4b:6d:5a:53 mac-address=\
    8C:EC:4B:6D:5A:53 server="COM-AP Network"
add address=10.0.1.95 client-id=1:e4:b9:7a:f8:bb:cb mac-address=\
    E4:B9:7A:F8:BB:CB server="COM-AP Network"
add address=10.0.1.134 client-id=1:f8:bc:12:6a:78:2c mac-address=\
    F8:BC:12:6A:78:2C server="COM-AP Network"
add address=10.0.0.251 client-id=1:8c:ec:4b:6d:9:92 mac-address=\
    8C:EC:4B:6D:09:92 server="COM-AP Network"
add address=10.0.1.47 client-id=1:6c:3b:e5:2a:e0:cd mac-address=\
    6C:3B:E5:2A:E0:CD server="COM-AP Network"
add address=10.0.0.164 client-id=1:a6:74:f4:49:32:12 mac-address=\
    A6:74:F4:49:32:12 server="COM-AP Network"
add address=10.0.1.129 client-id=1:f8:bc:12:6b:3b:2a mac-address=\
    F8:BC:12:6B:3B:2A server="COM-AP Network"
add address=10.0.1.147 client-id=1:e4:b9:7a:f8:bc:af mac-address=\
    E4:B9:7A:F8:BC:AF server="COM-AP Network"
add address=10.0.1.105 client-id=1:e4:b9:7a:f8:bb:93 mac-address=\
    E4:B9:7A:F8:BB:93 server="COM-AP Network"
add address=10.0.1.208 client-id=1:f8:bc:12:6b:3b:f mac-address=\
    F8:BC:12:6B:3B:0F server="COM-AP Network"
add address=10.0.1.42 client-id=1:e4:b9:7a:e9:9a:a2 mac-address=\
    E4:B9:7A:E9:9A:A2 server="COM-AP Network"
add address=10.0.1.207 client-id=1:e4:b9:7a:f8:bd:4d mac-address=\
    E4:B9:7A:F8:BD:4D server="COM-AP Network"
add address=10.0.1.98 client-id=1:f8:bc:12:6a:23:7f mac-address=\
    F8:BC:12:6A:23:7F server="COM-AP Network"
add address=10.0.1.193 client-id=1:f8:bc:12:6a:26:8f mac-address=\
    F8:BC:12:6A:26:8F server="COM-AP Network"
add address=10.0.1.48 client-id=1:f8:bc:12:6b:3a:ff mac-address=\
    F8:BC:12:6B:3A:FF server="COM-AP Network"
add address=10.0.1.3 client-id=1:e4:b9:7a:e5:b0:ae mac-address=\
    E4:B9:7A:E5:B0:AE server="COM-AP Network"
add address=10.0.1.63 client-id=1:e4:b9:7a:f8:bb:49 mac-address=\
    E4:B9:7A:F8:BB:49 server="COM-AP Network"
add address=10.20.2.188 mac-address=D0:67:26:A4:DA:18 server="CCTV Network"
add address=10.0.1.114 client-id=1:64:0:6a:3f:e:78 mac-address=\
    64:00:6A:3F:0E:78 server="COM-AP Network"
add address=10.0.0.102 client-id=1:0:be:43:d3:3:1c mac-address=\
    00:BE:43:D3:03:1C server="COM-AP Network"
add address=10.0.1.19 client-id=1:8c:ec:4b:6c:7e:1c mac-address=\
    8C:EC:4B:6C:7E:1C server="COM-AP Network"
add address=10.0.1.177 client-id=1:cc:2d:e0:aa:c9:72 mac-address=\
    CC:2D:E0:AA:C9:72 server="COM-AP Network"
add address=10.20.2.180 client-id=1:94:e1:ac:c4:a5:ad comment=Auditorium2 \
    mac-address=94:E1:AC:C4:A5:AD server="CCTV Network"
add address=10.20.2.178 client-id=1:94:e1:ac:c4:a5:aa comment=Auditorium1 \
    mac-address=94:E1:AC:C4:A5:AA server="CCTV Network"
add address=10.20.2.174 client-id=1:94:e1:ac:c4:a5:6a comment=S.Pool3 \
    mac-address=94:E1:AC:C4:A5:6A server="CCTV Network"
add address=10.0.0.184 client-id=1:70:b5:e8:30:5b:3c mac-address=\
    70:B5:E8:30:5B:3C server="COM-AP Network"
add address=10.0.0.202 client-id=1:46:66:f2:7d:8d:37 mac-address=\
    46:66:F2:7D:8D:37 server="COM-AP Network"
add address=10.0.1.222 client-id=1:48:45:20:92:43:66 comment=MsPraew \
    mac-address=48:45:20:92:43:66 server="COM-AP Network"
add address=10.0.1.72 client-id=1:a0:ce:c8:e4:eb:bd mac-address=\
    A0:CE:C8:E4:EB:BD server="COM-AP Network"
add address=10.0.1.70 client-id=1:c0:18:50:30:f5:b mac-address=\
    C0:18:50:30:F5:0B server="COM-AP Network"
add address=10.0.1.121 client-id=1:6c:62:6d:c8:3c:9d mac-address=\
    6C:62:6D:C8:3C:9D server="COM-AP Network"
add address=10.20.2.172 client-id=1:94:e1:ac:75:ba:42 comment=A306 \
    mac-address=94:E1:AC:75:BA:42 server="CCTV Network"
add address=10.20.2.170 client-id=1:94:e1:ac:78:78:27 comment="F.exit A311" \
    mac-address=94:E1:AC:78:78:27 server="CCTV Network"
add address=10.20.2.169 client-id=1:94:e1:ac:c4:a5:88 comment=Field7 \
    mac-address=94:E1:AC:C4:A5:88 server="CCTV Network"
add address=10.0.0.216 client-id=1:6c:3c:8c:b:b:93 comment=IT-Jason \
    mac-address=6C:3C:8C:0B:0B:93 server="COM-AP Network"
add address=10.0.1.195 client-id=1:20:88:10:5d:cc:42 mac-address=\
    20:88:10:5D:CC:42 server="COM-AP Network"
add address=10.20.2.168 client-id=1:94:e1:ac:75:ba:2a comment="F.exit KG 2nd" \
    mac-address=94:E1:AC:75:BA:2A server="CCTV Network"
add address=10.20.2.167 client-id=1:94:e1:ac:78:7a:50 comment="Hallway KG11" \
    mac-address=94:E1:AC:78:7A:50 server="CCTV Network"
add address=10.20.2.182 client-id=1:64:e8:81:b1:37:73 comment="Aruba Switch" \
    mac-address=64:E8:81:B1:37:73 server="CCTV Network"
add address=10.20.1.250 client-id=1:94:e1:ac:61:1:77 comment=MPR3 \
    mac-address=94:E1:AC:61:01:77 server="CCTV Network"
add address=10.20.1.251 client-id=1:94:e1:ac:61:1:6b comment=MPR1 \
    mac-address=94:E1:AC:61:01:6B server="CCTV Network"
add address=10.20.1.80 client-id=1:94:e1:ac:78:78:2c comment="Auditorium HW1" \
    mac-address=94:E1:AC:78:78:2C server="CCTV Network"
add address=10.20.1.116 client-id=1:4c:bd:8f:5:3c:16 comment="Auditorium HW2" \
    mac-address=4C:BD:8F:05:3C:16 server="CCTV Network"
add address=10.20.1.117 client-id=1:94:e1:ac:78:78:dd comment=\
    "Auditorium HW3" mac-address=94:E1:AC:78:78:DD server="CCTV Network"
add address=10.20.1.158 client-id=1:94:e1:ac:5a:30:5b mac-address=\
    94:E1:AC:5A:30:5B server="CCTV Network"
add address=10.20.1.246 client-id=1:94:e1:ac:75:ba:4d mac-address=\
    94:E1:AC:75:BA:4D server="CCTV Network"
add address=10.0.0.4 client-id=1:0:1e:67:a1:e1:b0 mac-address=\
    00:1E:67:A1:E1:B0 server="COM-AP Network"
/ip dhcp-server network
add address=10.0.0.0/22 comment=COM dns-server=\
    10.0.0.1,208.67.222.123,208.67.220.123 domain=ANGLO gateway=10.0.0.1 \
    netmask=22
add address=10.0.5.0/24 comment=FIREFLY dns-server=208.67.220.123,10.0.5.1 \
    domain=ANGLO gateway=10.0.5.1 netmask=24
add address=10.10.0.0/16 comment=AP-WIFI dns-server=208.67.220.123,10.10.0.1 \
    domain=ANGLO gateway=10.10.0.1 netmask=16
add address=10.20.0.0/16 comment=CCTV dns-server=208.67.220.123,10.20.0.1 \
    domain=ANGLO gateway=10.20.0.1 netmask=16
add address=10.64.64.0/24 dns-server=8.8.8.8,10.64.64.1 domain=ANGLO gateway=\
    10.64.64.1 netmask=24
/ip dns
set allow-remote-requests=yes
/ip dns static
add address=10.0.5.4 name=ikorat.anglosingapore.ac.th
add address=172.16.10.8 name=intranet.anglosingapore.ac.th
/ip firewall address-list
add address=10.0.0.184 comment=IT-Jason list=IT-Dept
add address=10.0.1.47 comment=IT-Rc list=IT-Dept
add address=10.0.0.186 comment=IT-Mervin list=IT-Dept
add address=10.0.1.141 comment=ICT5 list=ICT-LabStudent
add address=10.0.1.58 comment="ICT-Teacher ICT22" list=2F-ClassPC
add address=10.0.1.130 comment=ICT3 list=ICT-LabStudent
add address=10.0.1.147 comment=ICT1 list=ICT-LabStudent
add address=10.0.1.105 comment=ICT10 list=ICT-LabStudent
add address=10.0.1.95 comment=ICT8 list=ICT-LabStudent
add address=10.0.0.164 comment=ICT7 list=ICT-LabStudent
add address=10.0.1.128 comment=ICT11 list=ICT-LabStudent
add address=10.0.1.129 comment=ICT13 list=ICT-LabStudent
add address=10.0.1.135 comment=ICT15 list=ICT-LabStudent
add address=10.0.0.248 comment=ICT16 list=ICT-LabStudent
add address=10.0.0.250 comment=ICT18 list=ICT-LabStudent
add address=10.0.1.100 comment=ICT20 list=ICT-LabStudent
add address=10.0.1.134 comment=ICT21 list=ICT-LabStudent
add address=10.0.1.63 comment=ICT4 list=ICT-LabStudent
add address=10.0.1.207 comment=ICT2 list=ICT-LabStudent
add address=10.0.1.3 comment=ICT9 list=ICT-LabStudent
add address=10.0.1.42 comment=ICT6 list=ICT-LabStudent
add address=10.0.1.193 comment=ICT12 list=ICT-LabStudent
add address=10.0.1.208 comment=ICT14 list=ICT-LabStudent
add address=10.0.1.98 comment=ICT17 list=ICT-LabStudent
add address=10.0.1.48 comment=ICT19 list=ICT-LabStudent
add address=10.0.1.252 comment=A238 list=2F-ClassPC
add address=10.0.0.158 comment=Accounting-PC1 list=Acctg-Dept
add address=10.0.0.179 comment=Accounting-PC2 list=Acctg-Dept
add address=10.0.1.51 comment=Accounting-PC3 list=Acctg-Dept
add address=10.0.1.223 comment=A224 list=2F-ClassPC
add address=10.0.1.154 comment=A225 list=2F-ClassPC
add address=10.0.1.158 comment=Exam1 list=2F-ExamPC
add address=10.0.1.152 comment=A239 list=2F-ClassPC
add address=10.0.0.251 comment=A240 list=2F-ClassPC
add address=10.0.1.203 comment=A216 list=2F-ClassPC
add address=10.0.1.250 comment=A219 list=2F-ClassPC
add address=10.0.1.156 comment=A211 list=2F-ClassPC
add address=10.0.1.251 comment=A210 list=2F-ClassPC
add address=10.0.1.119 comment=A209 list=2F-ClassPC
add address=10.0.1.97 comment=A114 list=1F-ClassPC
add address=10.0.1.58 comment=A115 list=1F-ClassPC
add address=10.0.1.90 comment=A110 list=1F-ClassPC
add address=10.0.1.142 comment=A116 list=1F-ClassPC
add address=10.0.1.33 comment=A105 list=1F-ClassPC
add address=10.0.1.159 comment=A131 list=1F-ClassPC
add address=10.0.0.231 comment=A118 list=1F-ClassPC
add address=10.0.0.149 comment=Nurse list=Infirmary
add address=10.0.1.92 comment=AngloStellar002 list=1F-Office
add address=10.0.1.114 comment=ackorat3-PC list=1F-Office
add address=10.0.0.162 comment=ackorat2-PC list=1F-Office
add address=10.0.1.14 comment=Admission1 list=1F-Office
add address=10.0.0.143 comment=Printer1 list=1F-Office
add address=10.0.1.106 comment=A132 list=1F-ClassPC
add address=10.0.1.60 comment=A123 list=1F-ClassPC
add address=10.0.1.0 comment=A124 list=1F-ClassPC
add address=10.0.0.219 comment=A133 list=1F-ClassPC
add address=10.0.1.145 comment=Library1 list=1F-ClassPC
add address=10.0.1.190 comment=A106 list=1F-ClassPC
add address=10.0.1.19 comment=A111 list=1F-ClassPC
add address=10.0.1.14 comment=Adm-MrBest list="Allow Facebook"
add address=10.0.1.222 comment=Adm-MsPraew list="Allow Facebook"
add address=10.0.1.57 comment=Mgmt-MsTum list="Allow Facebook"
add address=8.8.8.8 list=DNS
add address=8.8.4.4 list=DNS
add address=110.78.191.20 list=DNS
add address=110.78.191.21 list=DNS
add address=61.19.245.245 list=DNS
add address=10.0.1.47 comment=IT-MrRC list="Allow Facebook"
add address=10.0.0.184 comment=IT-MrMervin list="Allow Facebook"
add address=10.0.0.147 comment=IT-A333 list="Allow Facebook"
add address=10.0.0.216 comment=IT-MrJason list="Allow Facebook"
add address=10.0.0.3 comment=Srv-Academic list=SharedServers
add address=10.0.0.4 comment=Srv-WCBS list=SharedServers
add address=103.218.243.165 list=SuspiciousIPs
add address=107.170.225.13 list=SuspiciousIPs
add address=107.170.246.12 list=SuspiciousIPs
add address=110.77.236.214 list=SuspiciousIPs
add address=110.77.241.156 list=SuspiciousIPs
add address=111.4.141.82 list=SuspiciousIPs
add address=118.193.34.65 list=SuspiciousIPs
add address=136.226.56.205 list=SuspiciousIPs
add address=139.59.86.114 list=SuspiciousIPs
add address=162.142.125.225 list=SuspiciousIPs
add address=167.248.133.186 list=SuspiciousIPs
add address=198.199.104.67 list=SuspiciousIPs
add address=198.235.24.110 list=SuspiciousIPs
add address=202.112.238.254 list=SuspiciousIPs
add address=210.16.101.219 list=SuspiciousIPs
add address=212.83.8.77 list=SuspiciousIPs
add address=34.78.6.216 list=SuspiciousIPs
add address=47.89.213.160 list=SuspiciousIPs
add address=49.49.236.23 list=SuspiciousIPs
add address=61.164.153.188 list=SuspiciousIPs
add address=64.62.197.0/24 list=SuspiciousIPs
add address=65.49.1.52 list=SuspiciousIPs
add address=78.128.113.67 list=SuspiciousIPs
add address=91.191.209.234 list=SuspiciousIPs
add address=92.63.196.75 list=SuspiciousIPs
add address=94.102.61.29 list=SuspiciousIPs
add address=183.88.0.0/17 list=SuspiciousIPs
add address=208.67.222.123 list=DNS
add address=208.67.220.123 list=DNS
add address=10.0.0.1 list=DNS
add address=10.100.0.0/16 list=DNS
add address=172.16.10.7 comment=Srv64-AngloBooks list=Shared64Servers
add address=192.168.1.10 comment=Srv64-Intranet list=Shared64Servers
add address=192.168.1.11 comment=Srv64-OSTicket list=Shared64Servers
add address=172.16.10.4 comment=Srv64-Database list=Shared64Servers
add address=10.0.0.207 comment=A228-A231 list="Allow Facebook"
add address=10.0.0.217 comment=SA-MsDew list="Allow Facebook"
add address=10.0.0.184 comment=IT-MrChris disabled=yes list="Allow Tiktok"
/ip firewall filter
add action=accept chain=forward comment="Mr. Sam Macbook" layer7-protocol=\
    Facebook src-address=10.0.0.144
add action=accept chain=forward layer7-protocol=Facebook src-address=\
    10.0.1.116
add action=drop chain=forward comment="Block: SuspiciousIPs" \
    src-address-list=SuspiciousIPs
add action=drop chain=forward comment="Block: Suspicious Device" \
    src-mac-address=46:66:F2:7D:8D:37
add action=drop chain=forward comment="Disallow obecimso.net" content=\
    obecimso protocol=tcp
add action=drop chain=forward comment="Block UDP on Port 53" port=53 \
    protocol=udp
add action=drop chain=input protocol=udp src-port=500,1701,4500
add action=drop chain=forward protocol=udp src-address=10.0.5.4 src-port=389
add action=drop chain=forward dst-address=10.0.5.4 protocol=udp src-port=389
add action=accept chain=forward comment="Allow DNS Requests" \
    src-address-list=DNS
add action=accept chain=forward comment="Allow DNS Requests" \
    dst-address-list=DNS
add action=accept chain=forward comment="Allow Server Requests" \
    src-address-list=SharedServers
add action=accept chain=forward comment="Allow Server Requests" \
    dst-address-list=SharedServers
add action=accept chain=forward comment="Allow 64 Server Requests" \
    src-address-list=Shared64Servers
add action=accept chain=forward comment="Allow 64 Server Requests" \
    dst-address-list=Shared64Servers
add action=accept chain=forward comment="Allow Bing" content=.bing.com \
    log-prefix=Twinkl
add action=accept chain=forward comment="Allow FB - A228-A231" disabled=yes \
    dst-address-list=FacebookIPs src-mac-address=CC:2D:E0:7C:54:BC
add action=accept chain=forward comment="Allow FB A333" dst-address-list=\
    FacebookIPs src-address-list="" src-mac-address=CC:2D:E0:79:15:95
add action=accept chain=forward comment="Allow FB Users" disabled=yes \
    dst-address-list=FacebookIPs src-address-list="Allow Facebook"
add action=accept chain=forward comment="Allow FB - Mr Rc2" disabled=yes \
    dst-port=80,443 protocol=tcp src-mac-address=70:81:EB:79:33:02
add action=accept chain=forward comment="Allow All Mr Don" src-mac-address=\
    00:E0:4C:68:25:C6
add action=accept chain=forward comment="Allow FB - Mr Jason" content=\
    facebook disabled=yes dst-port=80,443 protocol=tcp src-mac-address=\
    6C:3C:8C:0B:0B:93
add action=accept chain=forward comment="Allow FB - Mr. Rc" content=facebook \
    disabled=yes dst-port=80,443 protocol=tcp src-mac-address=\
    6C:3B:E5:2A:E0:CD
add action=accept chain=forward comment="Allow FB - Ms. Pang" content=\
    facebook disabled=yes dst-port=80,443 protocol=tcp src-mac-address=\
    00:00:00:00:00:00
add action=accept chain=forward comment="Allow - twitter Mr. Chris" content=\
    twitter src-mac-address=70:B5:E8:30:5B:3C
add action=accept chain=forward comment="Allow FB AuditoriumRight" disabled=\
    yes dst-port=80,443 protocol=tcp src-mac-address=CC:2D:E0:A5:54:8C
add action=accept chain=forward comment="Allow FB - Auditorium" disabled=yes \
    dst-port=80,443 protocol=tcp src-mac-address=CC:2D:E0:7C:54:BC
add action=accept chain=forward comment="Allow FB - AuditoriumLeft" disabled=\
    yes dst-port=80,443 protocol=tcp src-mac-address=CC:2D:E0:AA:C9:72
add action=drop chain=forward comment="Block Facebook" content=.facebook.com \
    log-prefix=Facebook src-address-list="!Allow Facebook"
add action=drop chain=forward comment="Block Facebook" content=.fbcdn.net \
    disabled=yes log-prefix=Facebook src-address-list="!Allow Facebook"
add action=drop chain=forward comment="Block Facebook" content=.facebook.net \
    disabled=yes log-prefix=Facebook src-address-list="!Allow Facebook"
add action=drop chain=forward comment="Block Facebook" content=.fb.com \
    disabled=yes log-prefix=Facebook src-address-list="!Allow Facebook"
add action=drop chain=forward comment="Block Youtube - 1F Office" disabled=\
    yes dst-address=10.0.1.47 layer7-protocol=Youtube
add action=drop chain=forward comment="Block Youtube - Acctg Dept" disabled=\
    yes dst-address-list=Acctg-Dept layer7-protocol=Youtube log-prefix=\
    Youtube protocol=tcp
add action=drop chain=forward comment="Block Youtube - Infirmary" disabled=\
    yes dst-address-list=Infirmary layer7-protocol=Youtube log-prefix=Youtube \
    protocol=tcp
add action=drop chain=forward disabled=yes src-address=115.113.154.116
add action=accept chain=forward comment="Allow CCTV" dst-address=10.10.0.0/16 \
    src-address=10.64.64.0/24
add action=drop chain=forward comment="Deny CCTV" disabled=yes dst-address=\
    10.10.0.0/16
add action=accept chain=forward disabled=yes
add action=drop chain=forward dst-port=22 in-interface=ether1 protocol=tcp
add action=drop chain=forward comment="Block Tiktok" disabled=yes \
    layer7-protocol=Tiktok
add action=drop chain=forward comment="Block Onlyfans" disabled=yes \
    layer7-protocol=Onlyfans
add action=drop chain=forward comment="Block Instagram" layer7-protocol=\
    Instagram
add action=drop chain=forward comment="Block roblox" disabled=yes \
    layer7-protocol=Roblox
add action=drop chain=forward comment="Block Y8" disabled=yes \
    layer7-protocol=Y8
add action=drop chain=forward comment="Block Twitter" layer7-protocol=Twitter
add action=drop chain=forward comment="Block Disney" layer7-protocol=Disney
add action=drop chain=forward comment="Block Netflix" disabled=yes \
    layer7-protocol=Netflix
/ip firewall mangle
add action=mark-routing chain=prerouting comment=\
    "Always #0 Enable if Eth1/Public Line has issue" disabled=yes \
    new-routing-mark=CAT-Private passthrough=yes
add action=accept chain=prerouting comment=\
    "Enable if Private Line has issue (WCBS,Accounting,Firefly)"
add action=mark-routing chain=prerouting comment="PRIVATE - Ms. Nuch" \
    disabled=yes new-routing-mark=CAT-Private passthrough=yes src-address=\
    10.0.1.51
add action=mark-routing chain=prerouting comment="PRIVATE - Firefly" \
    disabled=yes new-routing-mark=CAT-Private passthrough=yes src-address=\
    10.0.5.4
add action=mark-routing chain=prerouting comment="PRIVATE - Ms. Pan" \
    disabled=yes new-routing-mark=CAT-Private passthrough=yes src-address=\
    10.0.0.158
add action=mark-routing chain=prerouting comment="PRIVATE - Mr. Rc" disabled=\
    yes new-routing-mark=CAT-Private passthrough=yes src-address=10.0.1.1
add action=mark-routing chain=prerouting comment="PRIVATE - WCBS" \
    new-routing-mark=CAT-Private passthrough=yes src-address=10.0.0.4
add action=mark-routing chain=prerouting comment="PRIVATE - Academic Server" \
    new-routing-mark=CAT-Private passthrough=yes src-address=10.0.0.3
add action=mark-routing chain=prerouting comment="PRIVATE - Microtik" \
    new-routing-mark=CAT-Private passthrough=yes src-address=10.0.0.1
add action=accept chain=prerouting comment=\
    "Always Last ALL PUBLIC-Always put last. do not disable"
add action=mark-routing chain=prerouting new-routing-mark=CAT-Private \
    passthrough=yes src-address=10.0.1.47
/ip firewall nat
add action=masquerade chain=srcnat out-interface="pppoe-out2 3bb"
add action=dst-nat chain=dstnat dst-address=122.154.149.91 src-address=\
    10.0.0.0/22 to-addresses=10.0.5.4
add action=accept chain=dstnat dst-address=122.154.149.91 to-addresses=\
    10.0.5.4
add action=masquerade chain=srcnat out-interface=pppoe-out1 src-address=\
    10.0.0.0/22
add action=masquerade chain=srcnat out-interface=ether2
add action=masquerade chain=srcnat disabled=yes out-interface=ether1
add action=masquerade chain=srcnat disabled=yes out-interface=pppoe-out1
add action=masquerade chain=srcnat disabled=yes dst-address=172.17.10.0/24 \
    src-address=10.0.0.0/9
add action=masquerade chain=srcnat disabled=yes dst-address=172.17.10.1 \
    src-address=10.0.0.0/9
add action=masquerade chain=srcnat disabled=yes dst-address=172.16.10.1 \
    src-address=10.0.0.0/9
add action=masquerade chain=srcnat disabled=yes dst-address=172.16.10.0/24 \
    src-address=10.0.0.0/9
add action=masquerade chain=srcnat disabled=yes dst-address=172.17.10.0/24 \
    src-address=10.0.1.0/24
add action=src-nat chain=srcnat disabled=yes dst-address=172.16.8.0/21 \
    src-address=10.0.0.0/9 to-addresses=172.17.0.0/24
add action=src-nat chain=srcnat disabled=yes dst-address=10.0.1.47 \
    to-addresses=172.17.10.0/24

/ip firewall service-port
set ftp disabled=yes
set tftp disabled=yes
set pptp disabled=yes
/ip ipsec identity
add generate-policy=port-strict peer=peer3 secret=12345678
/ip ipsec policy
set 0 dst-address=0.0.0.0/0 src-address=0.0.0.0/0
add dst-address=0.0.0.0/0 protocol=udp src-address=0.0.0.0/0 template=yes
/ip route
add check-gateway=ping comment="ISP 2 3BB" disabled=yes distance=1 gateway=\
    "pppoe-out2 3bb" routing-mark=to-ether4
add comment="ISP 1 CAT" disabled=yes distance=1 gateway=pppoe-out1 \
    routing-mark=to-ether1
add distance=1 gateway=10.200.200.1 routing-mark=CAT-Private
add distance=1 dst-address=10.0.0.0/22 gateway="COM-AP Bridge" pref-src=\
    10.0.0.1 routing-mark=CAT-Private scope=10
add distance=1 dst-address=10.20.0.0/16 gateway=ether10-CCTV pref-src=\
    10.20.0.1 routing-mark=CAT-Private scope=10
add disabled=yes distance=255 dst-address=10.64.64.0/24 gateway=ether3 \
    pref-src=10.64.64.1 routing-mark=CAT-Private scope=10
add disabled=yes distance=1 dst-address=10.200.1.0/24 gateway="Anglo64 EoIP" \
    pref-src=10.200.1.2 routing-mark=CAT-Private scope=10
add disabled=yes distance=1 dst-address=10.200.3.0/24 gateway="Anglo31 EoIP" \
    pref-src=10.200.3.2 routing-mark=CAT-Private scope=10
add distance=1 dst-address=10.200.200.0/24 gateway=ether2 pref-src=\
    10.200.200.2 routing-mark=CAT-Private scope=10
add distance=1 dst-address=172.16.0.0/20 gateway=10.200.1.1 routing-mark=\
    CAT-Private
add disabled=yes distance=1 dst-address=172.16.8.0/24 gateway=10.200.3.1 \
    routing-mark=CAT-Private
add disabled=yes distance=1 dst-address=172.16.10.0/24 gateway=10.200.3.1 \
    routing-mark=CAT-Private
add disabled=yes distance=1 dst-address=172.16.20.0/23 gateway=10.200.3.1 \
    routing-mark=CAT-Private
add disabled=yes distance=1 dst-address=192.168.0.0/16 gateway=10.200.1.1 \
    routing-mark=CAT-Private
add check-gateway=ping comment="ECMP Failover" distance=1 gateway=\
    "pppoe-out2 3bb"
add check-gateway=ping distance=2 gateway=pppoe-out1
add comment="ENABLE IF ETH 1 NOT WORKING" disabled=yes distance=1 gateway=\
    10.200.200.1
add distance=1 dst-address=172.16.0.0/20 gateway=10.200.1.1
add disabled=yes distance=1 dst-address=172.16.8.0/24 gateway=10.200.3.1
add disabled=yes distance=1 dst-address=172.16.10.0/24 gateway=10.200.3.1
add disabled=yes distance=1 dst-address=172.16.20.0/23 gateway=10.200.3.1
add disabled=yes distance=1 dst-address=192.168.0.0/16 gateway=10.200.1.1
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www port=6464
set ssh disabled=yes
set api disabled=yes
/ip ssh
set allow-none-crypto=yes forwarding-enabled=remote
/ip traffic-flow
set interfaces="COM-AP Bridge"
/lcd
set time-interval=hour

/system clock
set time-zone-name=Asia/Bangkok
/system identity
set name="Mikrotik Router"
/system logging
set 3 action=memory
add action=remote topics=system
add action=remote topics=firewall
add disabled=yes
add action=remote topics=ipsec
add action=remote topics=error
add action=remote topics=critical
add action=remote topics=info
add action=remote topics=warning
/system scheduler
add interval=5m name=DynDNS64-Sched on-event=DynDNS64 policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-time=startup
add interval=5m name=DynDNS31-Sched on-event=DynDNS31 policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-time=startup
/system script
add dont-require-permissions=no name=DynDNS64 owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    global Einterface64 \"Anglo64 EoIP\";\r\
    \n:global eoipdnsname64 \"bbab0b045c01.sn.mynetname.net\"\r\
    \n:global eodnsip64 [:resolve \$eoipdnsname64]\r\
    \n:global currentip64 [/interface eoip get \$Einterface64 remote-address]\
    \r\
    \n/interface eoip set \$Einterface64 remote-address=\$eodnsip64\r\
    \n:if (\$currentip64 != \$eodnsip64) do={ /interface eoip set \$Einterface\
    64 remote-address=\$eodnsip64}\r\
    \n"
add dont-require-permissions=no name=DynDNS31 owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    global Einterface31 \"Anglo31 EoIP\";\r\
    \n:global eoipdnsname31 \"574b058d8bd1.sn.mynetname.net\"\r\
    \n:global eodnsip31 [:resolve \$eoipdnsname31]\r\
    \n:global currentip31 [/interface eoip get \$Einterface31 remote-address]\
    \r\
    \n/interface eoip set \$Einterface31 remote-address=\$eodnsip31\r\
    \n:if (\$currentip31 != \$eodnsip31) do={ /interface eoip set \$Einterface\
    31 remote-address=\$eodnsip31}\r\
    \n"
/tool graphing interface
add
/tool graphing resource
add
/tool sniffer
set filter-ip-address=10.0.1.14/32

---
```

## Response 1
I see a 100Mbps speed interface. Can you force it to 1Gb interface? ---

## Response 2
I am on my phone and it is hard to read long configs but it looks like:You are missing the established and FastTrack rulesYou are doing a ton of l7 matchingBoth affect the throughput. There may be way to fix some of it. Will check. ---

## Response 3
See many static DHCP reservations so it implies that there are many possible users transfering during speedtest. Are you sure that the missing 300Mb is not consumed somehow by others? ---

## Response 4
Sawadee...It's been 3 weeks of battle finding solution and error to our problem. We have 1gb internet cnn from our ISP. Bandwidth test inside the ccr1016 shows 600-800mbps but when using speedtest on pc on the classrooms get 90-150mbps. Wifi is worst like 2-15mbps in 2.4ghz using hap ac.Please help usYour firewall configuration is quite problematic, to say the least. For example, there is no ruleestablished, relatedin any of the chains, which means that the rulebase is pretty much reevaluated every time. This may be one of the sources of your bandwidth issues. Any indication why you did it that way?Something else that is missing is theinterface listsection, while it is not mandatory, this is a good way to group interfaces in a logical way.To fix this, I recommend to proceed by increment so if there is an issue, backtracking will be easy or at least easier.First, can you create a few interface lists and populate them with what you have? This allows to use the interface-list in rules.For example, the interfacespppoe-out1andpppoe-out2are likelyWANlinks.
```
/interface list
add comment=defconf name=WAN

/interface list member
add interface=pppoe-out1 list=WAN
add interface=pppoe-out2 list=WANSecond, let's re-add the implicit rules for thechain=input(the communications back to the firewall). You will have to move them up to the top of the rulebase.
```

```
/ip/firewall/filter
add action=accept chain=input comment="Implicit - Permit established,related,untracked" connection-state=established,related,untracked
add action=drop chain=input comment="Implicit - Drop invalid" connection-state=invalidNow still on the topic of the input chain: you have at least winbox and the www services enabled but not limited to some IP ranges, and there is no rules in the firewall. This means that your device is open. It would be better to limit the access to just the network where you have the IT personnel.Do you have a schematic of your network I could use when I redo your rules?

---
```