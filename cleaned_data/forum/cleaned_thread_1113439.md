# Thread Information
Title: Thread-1113439
Section: RouterOS
Thread ID: 1113439

# Discussion

## Initial Question
Hello Guys, I have questions, how do I pass all traffic into WireGuard Cloudflare VPN?I follow this tutorialhttps://www.youtube.com/watch?v=2pFcVRaoscE, but when I add mangle or routing rule, my winbox disconnects from the router and cannot connect via IP.In that tutorial, the wireguard traffic is only for a specific range of IP addresses, and some websites like this forum cannot be accessed.I try to ask chat GPT, to help me, but none the answer work.https://chatgpt.com/share/671ac348-32ac ... 0cbbb24294==== ==== ==== ==== ==== ====Winbox cannot connect through an IP address.Winbox can connect through an IP address.Tplink Switch Vlan configuration.the rsc config
```
# 2024-10-25 05:18:02 by RouterOS 7.16.1
# software id = #
#
# model = RB941-2nD
# serial number = #
/interface bridge
add admin-mac=# auto-mac=no comment=defconf \
    ingress-filtering=no name=bridge port-cost-mode=short vlan-filtering=yes
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=20/40mhz-XX \
    country=indonesia distance=indoors frequency=auto installation=indoor \
    mode=ap-bridge ssid=Scale wireless-protocol=802.11
/interface wireguard
add comment="Cloudflare WireGuard" listen-port=13231 mtu=1420 name=wireguard1
/interface vlan
add comment=guestconf interface=bridge name=vlan22 vlan-id=22
/interface bonding
add name=bonding1 slaves=ether3,ether4
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface wireless security-profiles
set [ find default=yes ] authentication-types=wpa-psk,wpa2-psk eap-methods="" \
    mode=dynamic-keys supplicant-identity=MikroTik
add eap-methods="" name=guest supplicant-identity=""
/interface wireless
add keepalive-frames=disabled mac-address=# master-interface=\
    wlan1 multicast-buffering=disabled name=wlan2 security-profile=guest \
    ssid="Scale Guest" wds-cost-range=0 wds-default-cost=0 wps-mode=disabled
/ip kid-control
add fri=0s-1d mon=0s-1d name=system-dummy sat=0s-1d sun=0s-1d thu=0s-1d tue=\
    0s-1d tur-fri=0s-1d tur-mon=0s-1d tur-sat=0s-1d tur-sun=0s-1d tur-thu=\
    0s-1d tur-tue=0s-1d tur-wed=0s-1d wed=0s-1d
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
add name=guest-dhcp ranges=192.168.84.2-192.168.84.8
/ip dhcp-server
add address-pool=default-dhcp interface=bridge lease-time=10m name=defconf
add address-pool=guest-dhcp interface=vlan22 lease-time=10m name=guestconf
/queue simple
add max-limit=1M/1M name=queue-guest target=vlan22
/routing ospf instance
add disabled=no name=default-v2
/routing ospf area
add disabled=yes instance=default-v2 name=backbone-v2
/routing table
add comment="Cloudflare WireGuard" disabled=no fib name=to-Cloudflare
/interface bridge port
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether2 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether3 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether4 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf ingress-filtering=no interface=pwr-line1 \
    internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf ingress-filtering=no interface=wlan1 \
    internal-path-cost=10 path-cost=10
add bridge=bridge ingress-filtering=no interface=bonding1 internal-path-cost=\
    10 path-cost=10
add bridge=bridge ingress-filtering=no interface=wlan2 internal-path-cost=10 \
    path-cost=10 pvid=22
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=LAN
/ip settings
set max-neighbor-entries=8192
/ipv6 settings
set disable-ipv6=yes max-neighbor-entries=8192
/interface bridge vlan
add bridge=bridge tagged=bridge,bonding1 untagged=wlan2 vlan-ids=22
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=ether2 list=WAN
/interface ovpn-server server
set auth=sha1,md5
/interface wireguard peers
add allowed-address=0.0.0.0/0 comment="Cloudflare WireGuard" \
    endpoint-address=engage.cloudflareclient.com endpoint-port=2408 \
    interface=wireguard1 name="cloudflare wireguard" persistent-keepalive=35s \
    public-key="#"
/ip address
add address=192.168.88.1/24 comment=defconf interface=bridge network=\
    192.168.88.0
add address=192.168.84.1/28 comment=guestconf interface=vlan22 network=\
    192.168.84.0
add address=192.168.100.100/24 comment=wan1 interface=ether1 network=\
    192.168.100.0
add address=192.168.2.100/24 comment=wan2 interface=ether2 network=\
    192.168.2.0
add address=172.16.0.2 comment="Cloudflare WireGuard" interface=wireguard1 \
    network=172.16.0.0
/ip dhcp-client
add comment=defconf disabled=yes interface=ether1
add comment=defconf disabled=yes interface=ether2
/ip dhcp-server lease
add address=192.168.88.2 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.6 mac-address=# server=defconf
add address=192.168.88.3 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.4 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.5 mac-address=# server=defconf
/ip dhcp-server network
add address=192.168.84.0/28 comment=guestconf gateway=192.168.84.1
add address=192.168.88.0/24 comment=defconf gateway=192.168.88.1
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,1.0.0.1
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
add address=192.168.100.1 name=wan1.logi.lo type=A
add address=192.168.2.1 name=wan2.logi.lo type=A
add address=192.168.88.6 name=stb1.logi.lo type=A
add address=127.0.0.1 name=stb2.logi.lo type=A
add address=192.168.88.4 name=eap1.logi.lo type=A
add address=192.168.100.254 name=cpe1.logi.lo type=A
add address=192.168.88.2 name=switch1.logi.lo type=A
add address=192.168.88.3 name=switch2.logi.lo type=A
add address=192.168.88.5 name=tlmr1.logi.lo type=A
/ip firewall filter
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
add action=drop chain=forward comment="guestconf: drop to ether2" \
    in-interface=vlan22 out-interface=ether2
/ip firewall mangle
add action=change-mss chain=forward comment="Cloudflare WireGuard" new-mss=\
    1380 out-interface=wireguard1 passthrough=no protocol=tcp tcp-flags=syn \
    tcp-mss=1381-65535
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat comment="Cloudflare WireGuard" \
    out-interface=wireguard1
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/ip kid-control device
add mac-address=# name="Redmi-10C;2" user=""
add mac-address=# name="ESP-67B077;6" user=""
/ip route
add check-gateway=ping comment=Recursive disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=8.8.8.8 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=12
add check-gateway=ping comment=Main disabled=no distance=1 dst-address=\
    8.8.8.8/32 gateway=192.168.100.1 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=11
add check-gateway=ping comment=Backup disabled=no distance=2 dst-address=\
    0.0.0.0/0 gateway=192.168.2.1 routing-table=main scope=30 \
    suppress-hw-offload=no target-scope=10
add comment="Cloudflare WireGuard" disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=wireguard1 routing-table=to-Cloudflare scope=30 \
    suppress-hw-offload=no target-scope=10
/routing bfd configuration
add disabled=no interfaces=all min-rx=200ms min-tx=200ms multiplier=5
/routing rule
add action=lookup-only-in-table comment="Cloudflare WireGuard" disabled=no \
    min-prefix=0 table=main
add action=lookup-only-in-table disabled=no src-address=192.168.88.0/24 \
    table=to-Cloudflare
add action=lookup-only-in-table disabled=no src-address=192.168.84.0/28 \
    table=to-Cloudflare
/system clock
set time-zone-name=Asia/Jakarta
/system note
set show-at-login=no
/system scheduler
add interval=2d name=reboot on-event="/system reboot" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:32:56
add interval=2h name="dns clear" on-event="/ip dns cache flush" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:35:12
add comment="trigger duckdns updater" interval=1m name="duckdns updater" \
    on-event="/system script run duckdns" policy=read,write,policy,test \
    start-time=startup
/system script
add comment="duckdns updater" dont-require-permissions=no name=duckdns owner=\
    admin policy=read,write,policy,test source=":local resolvedIP [:resolve \"\
    #.duckdns.org\"];\
    \n:local currentIP [/ip cloud get public-address];\
    \n:local currentIP [:pick \$currentIP 0 [:find \$currentIP \"/\"]];\
    \n\
    \n:if (\$resolvedIP != \$currentIP) do={\
    \n    :log info (\"Trying to update DuckDNS with actual IP \".\$currentIP.\
    \", resolved IP is \".\$resolvedIP);\
    \n    :local response [/tool fetch url=(\"https://www.duckdns.org/update\?\
    domains=#&token=\
    \#&ip=\".\$currentIP) check-certificat\
    e=yes as-value output=user];\
    \n    :if (\$response->\"status\" = \"finished\") do={\
    \n        :if (\$response->\"data\" = \"OK\") do={\
    \n            :log info (\"Successfully updated DuckDNS with new IP \".\$c\
    urrentIP);\
    \n        } else={\
    \n            :log error (\"Failed to update DuckDNS with new IP \".\$curr\
    entIP);\
    \n        }\
    \n    }\
    \n}"
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN==== ====any suggestions?I'm still learning about network forgive me if I do lot of mistakes, thanksMy network configuration is figured in the attachments.

---
```

## Response 1
# model = RB941-2nD# serial number = #/interface bridgeadd admin-mac=# auto-mac=no comment=defconf \ingress-filtering=no name=bridge port-cost-mode=short vlan-filtering=yes/interface wirelessset [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=20/40mhz-XX \country=indonesia distance=indoors frequency=auto installation=indoor \mode=ap-bridge ssid=Scale wireless-protocol=802.11/interface wireguardadd comment="Cloudflare WireGuard" listen-port=13231 mtu=1420 name=wireguard1/interface vlanadd comment=guestconf interface=bridge name=vlan22 vlan-id=22add interface=bridge name=home-vlan10 vlan-id=10/interface bondingadd name=bonding1 slaves=ether3, ether4/interface listadd comment=defconf name=WANadd comment=defconf name=LAN/interface wireless security-profilesset [ find default=yes ] authentication-types=wpa-psk, wpa2-psk eap-methods="" \mode=dynamic-keys supplicant-identity=MikroTikadd eap-methods="" name=guest supplicant-identity=""/interface wirelessadd keepalive-frames=disabled mac-address=# master-interface=\wlan1 multicast-buffering=disabled name=wlan2 security-profile=guest \ssid="Scale Guest" wds-cost-range=0 wds-default-cost=0 wps-mode=disabled/ip kid-controladd fri=0s-1d mon=0s-1d name=system-dummy sat=0s-1d sun=0s-1d thu=0s-1d tue=\0s-1d tur-fri=0s-1d tur-mon=0s-1d tur-sat=0s-1d tur-sun=0s-1d tur-thu=\0s-1d tur-tue=0s-1d tur-wed=0s-1d wed=0s-1d/ip pooladd name=default-dhcp ranges=192.168.88.10-192.168.88.254add name=guest-dhcp ranges=192.168.84.2-192.168.84.8/ip dhcp-serveradd address-pool=default-dhcpinterface=home-vlan10lease-time=10m name=defconfadd address-pool=guest-dhcp interface=vlan22 lease-time=10m name=guestconf/queue simpleadd max-limit=1M/1M name=queue-guest target=vlan22/routing ospf instanceadd disabled=no name=default-v2/routing ospf areaadd disabled=yes instance=default-v2 name=backbone-v2/routing tableadd comment="Cloudflare WireGuard" disabled=no fib name=to-Cloudflare/interface bridge portadd bridge=bridge ingress-filtering=yes frame-types=admit-untagged-and-priority-tagged interface=wlan1 pvid=10add bridge=bridge ingress-filtering=yes frame-types=admit-untagged-and-priority-tagged interface=wlan2 pvid=22add bridge=bridge ingress-filtering=yes frame-types=admit-untagged-and-priority-tagged interface=bonding1 pvid=10add bridge=bridge ingress-filtering=yes frame-types=admit-untagged-and-priority-tagged interface=ether4 pvid=10add bridge=bridge ingress-filtering=yes frame-types=admit-untagged-and-priority-tagged interface=pwr-line1 pvid=10/ip firewall connection trackingset udp-timeout=10s/ip neighbor discovery-settingsset discover-interface-list=LAN/ip settingsset max-neighbor-entries=8192/ipv6 settingsset disable-ipv6=yes max-neighbor-entries=8192/interface bridge vlanadd bridge=bridge tagged=bridge untagged=bonding1, wlan1, ether4 vlan-ids=10add bridge=bridge tagged=bridge untagged=wlan2 vlan-ids=22/interface list memberadd comment=defconf interface=home-vlan10list=LANadd interface=vlan22 list=LANadd comment=defconf interface=ether1 list=WANadd interface=ether2 list=WAN/interface ovpn-server serverset auth=sha1, md5/interface wireguard peersadd allowed-address=0.0.0.0/0 comment="Cloudflare WireGuard" \endpoint-address=engage.cloudflareclient.com endpoint-port=2408 \interface=wireguard1 name="cloudflare wireguard" persistent-keepalive=35s \public-key="#"/ip addressadd address=192.168.88.1/24 comment=defconfinterface=home-vlan10network=\192.168.88.0add address=192.168.84.1/28 comment=guestconf interface=vlan22 network=\192.168.84.0add address=192.168.100.100/24 comment=wan1 interface=ether1 network=\192.168.100.0add address=192.168.2.100/24 comment=wan2 interface=ether2 network=\192.168.2.0add address=172.16.0.2/24comment="Cloudflare WireGuard" interface=wireguard1 \network=172.16.0.0/ip dhcp-clientadd comment=defconf disabled=yes interface=ether1add comment=defconf disabled=yes interface=ether2/ip dhcp-server leaseadd address=192.168.88.2 client-id=# mac-address=\# server=defconfadd address=192.168.88.6 mac-address=# server=defconfadd address=192.168.88.3 client-id=# mac-address=\# server=defconfadd address=192.168.88.4 client-id=# mac-address=\# server=defconfadd address=192.168.88.5 mac-address=# server=defconf/ip dhcp-server networkadd address=192.168.84.0/28 comment=guestconf gateway=192.168.84.1add address=192.168.88.0/24 comment=defconf gateway=192.168.88.1/ip dnsset allow-remote-requests=yes servers=1.1.1.1, 1.0.0.1/ip dns static {FOR WHAT PURPOSEall the below static settings??? }add address=192.168.88.1 comment=defconf name=router.lan type=Aadd address=192.168.100.1 name=wan1.logi.lo type=Aadd address=192.168.2.1 name=wan2.logi.lo type=Aadd address=192.168.88.6 name=stb1.logi.lo type=Aadd address=127.0.0.1 name=stb2.logi.lo type=Aadd address=192.168.88.4 name=eap1.logi.lo type=Aadd address=192.168.100.254 name=cpe1.logi.lo type=Aadd address=192.168.88.2 name=switch1.logi.lo type=Aadd address=192.168.88.3 name=switch2.logi.lo type=Aadd address=192.168.88.5 name=tlmr1.logi.lo type=A/ip firewall filteradd action=accept chain=input comment=\"defconf: accept established, related, untracked" connection-state=\established, related, untrackedadd action=drop chain=input comment="defconf: drop invalid" connection-state=\invalidadd action=accept chain=input comment="defconf: accept ICMP" protocol=icmpadd action=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1add action=drop chain=input comment="defconf: drop all not coming from LAN" \in-interface-list=!LANadd action=accept chain=forward comment="defconf: accept in ipsec policy" \ipsec-policy=in, ipsecadd action=accept chain=forward comment="defconf: accept out ipsec policy" \ipsec-policy=out, ipsecadd action=fasttrack-connection chain=forward comment="defconf: fasttrack" \connection-state=established, related hw-offload=yesadd action=accept chain=forward comment=\"defconf: accept established, related, untracked" connection-state=\established, related, untrackedadd action=drop chain=forward comment="defconf: drop invalid" \connection-state=invalidadd action=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \connection-state=new in-interface-list=WANadd action=drop chain=forward comment="guestconf: drop to ether2" \in-interface=vlan22 out-interface=ether2/ip firewall mangleadd action=change-mss chain=forward comment="Cloudflare WireGuard" new-mss=\1380 out-interface=wireguard1 passthrough=no protocol=tcp tcp-flags=syn \tcp-mss=1381-65535/ip firewall natadd action=masquerade chain=srcnat comment="defconf: masquerade" \ipsec-policy=out, none out-interface-list=WANadd action=masquerade chain=srcnat comment="Cloudflare WireGuard" \out-interface=wireguard1/ip ipsec profileset [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5/ip kid-control deviceadd mac-address=# name="Redmi-10C;2" user=""add mac-address=# name="ESP-67B077;6" user=""/ip routeadd check-gateway=ping comment=Recursive disabled=no distance=1 dst-address=\0.0.0.0/0 gateway=8.8.8.8 routing-table=main scope=10 \suppress-hw-offload=no target-scope=12add check-gateway=ping comment=Main disabled=no distance=1 dst-address=\8.8.8.8/32 gateway=192.168.100.1 routing-table=main scope=10 \suppress-hw-offload=no target-scope=11add check-gateway=ping comment=Backup disabled=no distance=2 dst-address=\0.0.0.0/0 gateway=192.168.2.1 routing-table=main scope=30 \suppress-hw-offload=no target-scope=10add comment="Cloudflare WireGuard" disabled=no distance=1 dst-address=\0.0.0.0/0 gateway=wireguard1 routing-table=to-Cloudflare scope=30 \suppress-hw-offload=no target-scope=10/routing bfd configuration {FOR WHATpurpose is this rule ???}add disabled=no interfaces=all min-rx=200ms min-tx=200ms multiplier=5/routing ruleadd action=lookup-only-in-table comment="Cloudflare WireGuard" disabled=no \min-prefix=0 table=mainadd action=lookup-only-in-table disabled=no src-address=192.168.88.0/24 \table=to-Cloudflareadd action=lookup-only-in-table disabled=no src-address=192.168.84.0/28 \table=to-Cloudflare{WHAT IS the purpose of this rule??? Where did this subnet come from??/system clockset time-zone-name=Asia/Jakarta/system noteset show-at-login=no/system scheduleradd interval=2d name=reboot on-event="/system reboot" policy=\ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon \start-date=2021-02-28 start-time=16:32:56add interval=2h name="dns clear" on-event="/ip dns cache flush" policy=\ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon \start-date=2021-02-28 start-time=16:35:12add comment="trigger duckdns updater" interval=1m name="duckdns updater" \on-event="/system script run duckdns" policy=read, write, policy, test \start-time=startup/system scriptadd comment="duckdns updater" dont-require-permissions=no name=duckdns owner=\admin policy=read, write, policy, test source=":local resolvedIP [:resolve \"\#.duckdns.org\"];\\n:local currentIP [/ip cloud get public-address];\\n:local currentIP [:pick \$currentIP 0 [:find \$currentIP \"/\"]];\\n\\n:if (\$resolvedIP != \$currentIP) do={\\n :log info (\"Trying to update DuckDNS with actual IP \".\$currentIP.\\", resolved IP is \".\$resolvedIP);\\n :local response [/tool fetch url=(\"https://www.duckdns.org/update\?\domains=#&token=\\#&ip=\".\$currentIP) check-certificat\e=yes as-value output=user];\\n :if (\$response->\"status\" = \"finished\") do={\\n :if (\$response->\"data\" = \"OK\") do={\\n :log info (\"Successfully updated DuckDNS with new IP \".\$c\urrentIP);\\n } else={\\n :log error (\"Failed to update DuckDNS with new IP \".\$curr\entIP);\\n }\\n }\\n}"/tool mac-serverset allowed-interface-list=LAN/tool mac-server mac-winboxset allowed-interface-list=LAN ---

## Response 2
I'm following your configuration, but i got ERR:Could not connect, MacConnection syn timeout. Why ?And why i should make new home vlan and add it on bridge ?Now i cant get access to my router board, with Mac address on all port or ip ---

## Response 3
The config was not intended for you to blindly copy and get into trouble, it was there to generate questions and discussions.Until you understand what I touched upon and answered the ambiguities and questions, there is no point in changing any of the config.In terms of making changes to the config on any MT device I highly recommend using a port NOT on the bridge ( might have to take one off the bridge temporarily).Give it an IP address, and make it part of the LAN or Trusted interface list and do all the config from that port, especially if monkeying with bridge and vlans./interface ethernetset [ find default-name=ether5 ] name=OffBridge5/ip addressadd address=192.168.68.1/30 interface=OffBridge5 network=192.168.68.0/Interface list membersadd interface=OffBridge5 list=TRUSTEDSimply change ipv4 settings on laptop to match 192.168.68.2 and you should be able to config the router. ---

## Response 4
My router RB941-2ND only has 4 ports.- ether 1 > wan 1- ether 2 > wan 2- ether 3, 4 > bonding to a TP-Link switch.because you say when I'm trying to try config, I need one port dedicated to 'offBridge' / debugging purposes. Then I chose port 4, and because of it, I should unbound ports 3 and 4.==== ====here is the new configuration# 2024-10-28 02:57:36 by RouterOS 7.16.1# software id = ### model = RB941-2nD# serial number = #/interface bridgeadd admin-mac=# auto-mac=no comment=defconf \ingress-filtering=no name=bridge port-cost-mode=short vlan-filtering=yes/interface wirelessset [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=20/40mhz-XX \country=indonesia distance=indoors frequency=auto installation=indoor \mode=ap-bridge ssid=Scale wireless-protocol=802.11/interface ethernetset [ find default-name=ether4 ] comment=debugging/interface wireguardadd comment="Cloudflare WireGuard" listen-port=13231 mtu=1420 name=wireguard1/interface vlanadd comment=guestconf interface=bridge name=guest-vlan22 vlan-id=22add comment=default-home-conf interface=bridge name=home-vlan10 vlan-id=10/interface bondingadddisabled=yesname=bonding1 slaves=ether3, ether4/interface listadd comment=defconf name=WANadd comment=defconf name=LAN/interface wireless security-profilesset [ find default=yes ] authentication-types=wpa-psk, wpa2-psk eap-methods="" \mode=dynamic-keys supplicant-identity=MikroTikadd eap-methods="" name=guest supplicant-identity=""/interface wirelessadd keepalive-frames=disabled mac-address=# master-interface=\wlan1 multicast-buffering=disabled name=wlan2 security-profile=guest \ssid="Scale Guest" wds-cost-range=0 wds-default-cost=0 wps-mode=disabled/ip kid-controladd fri=0s-1d mon=0s-1d name=system-dummy sat=0s-1d sun=0s-1d thu=0s-1d tue=\0s-1d tur-fri=0s-1d tur-mon=0s-1d tur-sat=0s-1d tur-sun=0s-1d tur-thu=\0s-1d tur-tue=0s-1d tur-wed=0s-1d wed=0s-1d/ip pooladd name=default-dhcp ranges=192.168.88.10-192.168.88.254add name=guest-dhcp ranges=192.168.84.2-192.168.84.8/ip dhcp-serveradd address-pool=default-dhcp interface=home-vlan10 lease-time=10m name=\defconfadd address-pool=guest-dhcp interface=guest-vlan22 lease-time=10m name=\guestconf/queue simpleadd max-limit=1M/1M name=queue-guest target=guest-vlan22/routing ospf instanceadd disabled=no name=default-v2/routing ospf areaadd disabled=yes instance=default-v2 name=backbone-v2/routing tableadd comment="Cloudflare WireGuard" disabled=no fib name=to-Cloudflare/interface bridge portadd bridge=bridge comment=defconfdisabled=yesingress-filtering=no \interface=ether2 internal-path-cost=10 path-cost=10add bridge=bridge comment=defconf interface=ether3 internal-path-cost=10 \path-cost=10-> this port connect into a switch, pvid 1, frame types admit all, 'because when i put pvid 10 and frame types admit-only-untagged-and-priority-tagged its not working, the switch and access point can't read the vlan. in this port i let through vlan 10 home and 22 guest'add bridge=bridge comment=defconfdisabled=yesingress-filtering=no \interface=ether4 internal-path-cost=10 path-cost=10add bridge=bridge comment=defconf interface=pwr-line1 internal-path-cost=10 \path-cost=10-> i don't know which port that use in here ?add bridge=bridge comment=defconf frame-types=\admit-only-untagged-and-priority-tagged interface=wlan1 \internal-path-cost=10 path-cost=10 pvid=10add bridge=bridgedisabled=yesingress-filtering=no interface=bonding1 \internal-path-cost=10 path-cost=10 ->temporary disable, since port 4 as debugging purposeadd bridge=bridge frame-types=admit-only-untagged-and-priority-tagged \interface=wlan2 internal-path-cost=10 path-cost=10 pvid=22/ip firewall connection trackingset udp-timeout=10s/ip neighbor discovery-settingsset discover-interface-list=LAN/ip settingsset max-neighbor-entries=8192/ipv6 settingsset disable-ipv6=yes max-neighbor-entries=8192/interface bridge vlanadd bridge=bridge tagged=bridge, ether3 untagged=wlan2 vlan-ids=22add bridge=bridge tagged=bridge, ether3 untagged=wlan1 vlan-ids=10-> if i put ether 3 untagged the vlan not working, then i put it in tagged as far i know its called trunk port, do im wrong here ?/interface list memberadd comment=defconf interface=bridge list=LANadd comment=defconf interface=ether1 list=WANadd interface=ether2 list=WANadd comment=debugging interface=ether4 list=LANadd comment=mynet interface=home-vlan10 list=LANadd interface=guest-vlan22 list=LAN/interface ovpn-server serverset auth=sha1, md5/interface wireguard peersadd allowed-address=0.0.0.0/0 comment="Cloudflare WireGuard" \endpoint-address=engage.cloudflareclient.com endpoint-port=2408 \interface=wireguard1 name="cloudflare wireguard" persistent-keepalive=35s \public-key="#"/ip addressadd address=192.168.88.1/24 comment=defconf interface=home-vlan10 network=\192.168.88.0add address=192.168.84.1/28 comment=guestconf interface=guest-vlan22 network=\192.168.84.0add address=192.168.100.100/24 comment=wan1 interface=ether1 network=\192.168.100.0add address=192.168.2.100/24 comment=wan2 interface=ether2 network=\192.168.2.0add address=172.16.0.2/24comment="Cloudflare WireGuard" interface=wireguard1 \network=172.16.0.0add address=192.168.68.1/30comment=debugginginterface=ether4 network=\192.168.68.0/ip dhcp-clientadd comment=defconf disabled=yes interface=ether1add comment=defconf disabled=yes interface=ether2/ip dhcp-server leaseadd address=192.168.88.2 client-id=# mac-address=\# server=defconfadd address=192.168.88.6 mac-address=# server=defconfadd address=192.168.88.3 client-id=# mac-address=\# server=defconfadd address=192.168.88.4 client-id=# mac-address=\# server=defconfadd address=192.168.88.5 mac-address=# server=defconf/ip dhcp-server networkadd address=192.168.84.0/28 comment=guestconf gateway=192.168.84.1add address=192.168.88.0/24 comment=defconf gateway=192.168.88.1/ip dnsset allow-remote-requests=yes servers=1.1.1.1, 1.0.0.1/ip dns static-> is this affect the network ? as far as i know im set this because i want that devices can be access by URL name not only IP address. is this the wrong way ?add address=192.168.88.1 comment=defconf name=router.lan type=Aadd address=192.168.100.1 name=wan1.logi.lo type=Aadd address=192.168.2.1 name=wan2.logi.lo type=Aadd address=192.168.88.6 name=stb1.logi.lo type=Aadd address=127.0.0.1 name=stb2.logi.lo type=Aadd address=192.168.88.4 name=eap1.logi.lo type=Aadd address=192.168.100.254 name=cpe1.logi.lo type=Aadd address=192.168.88.2 name=switch1.logi.lo type=Aadd address=192.168.88.3 name=switch2.logi.lo type=Aadd address=192.168.88.5 name=tlmr1.logi.lo type=A/ip firewall filteradd action=accept chain=input comment=\"defconf: accept established, related, untracked" connection-state=\established, related, untrackedadd action=drop chain=input comment="defconf: drop invalid" connection-state=\invalidadd action=accept chain=input comment="defconf: accept ICMP" protocol=icmpadd action=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1add action=drop chain=input comment="defconf: drop all not coming from LAN" \in-interface-list=!LANadd action=accept chain=forward comment="defconf: accept in ipsec policy" \ipsec-policy=in, ipsecadd action=accept chain=forward comment="defconf: accept out ipsec policy" \ipsec-policy=out, ipsecadd action=fasttrack-connection chain=forward comment="defconf: fasttrack" \connection-state=established, related hw-offload=yesadd action=accept chain=forward comment=\"defconf: accept established, related, untracked" connection-state=\established, related, untrackedadd action=drop chain=forward comment="defconf: drop invalid" \connection-state=invalidadd action=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \connection-state=new in-interface-list=WANadd action=drop chain=forward comment="guestconf: drop to ether2" \in-interface=guest-vlan22 out-interface=ether2-> i don't want guest to access the backup network, so i dropped it./ip firewall mangleadd action=change-mss chain=forward comment="Cloudflare WireGuard" new-mss=\1380 out-interface=wireguard1 passthrough=no protocol=tcp tcp-flags=syn \tcp-mss=1381-65535/ip firewall natadd action=masquerade chain=srcnat comment="defconf: masquerade" \ipsec-policy=out, none out-interface-list=WANadd action=masquerade chain=srcnat comment="Cloudflare WireGuard" \out-interface=wireguard1/ip ipsec profileset [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5/ip kid-control deviceadd mac-address=# name="Redmi-10C;2" user=""add mac-address=# name="ESP-67B077;6" user=""/ip routeadd check-gateway=ping comment=Recursive disabled=no distance=1 dst-address=\0.0.0.0/0 gateway=1.1.1.1 routing-table=main scope=10 \suppress-hw-offload=no target-scope=12add check-gateway=ping comment=Main disabled=no distance=1 dst-address=\1.1.1.1/32 gateway=192.168.100.1 routing-table=main scope=10 \suppress-hw-offload=no target-scope=11add check-gateway=ping comment=Backup disabled=no distance=2 dst-address=\0.0.0.0/0 gateway=192.168.2.1 routing-table=main scope=30 \suppress-hw-offload=no target-scope=10add comment="Cloudflare WireGuard" disabled=no distance=1 dst-address=\0.0.0.0/0 gateway=wireguard1 routing-table=to-Cloudflare scope=30 \suppress-hw-offload=no target-scope=10#error exporting "/ip/upnp" (timeout)/routing bfd configurationadddisabled=yesinterfaces=all min-rx=200ms min-tx=200ms multiplier=5-> i don't know the purpose of this config, since my config is edited from default/factory configuration when the mikrotik first-time boot/after factory reset./routing ruleadd action=lookup-only-in-table comment="Cloudflare WireGuard" disabled=no \min-prefix=0 table=mainadd action=lookup-only-in-table disabled=no src-address=192.168.88.0/24 \table=to-Cloudflareadd action=lookup-only-in-table disabled=no src-address=192.168.84.0/28 \table=to-Cloudflare-> i add this because i think it make guest network will flow through the VPN too./system clockset time-zone-name=Asia/Jakarta/system noteset show-at-login=no#error exporting "/system/ntp/client" (timeout)/system scheduleradd interval=2d name=reboot on-event="/system reboot" policy=\ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon \start-date=2021-02-28 start-time=16:32:56add interval=2h name="dns clear" on-event="/ip dns cache flush" policy=\ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon \start-date=2021-02-28 start-time=16:35:12add comment="trigger duckdns updater" interval=1m name="duckdns updater" \on-event="/system script run duckdns" policy=read, write, policy, test \start-time=startup/system scriptadd comment="duckdns updater" dont-require-permissions=no name=duckdns owner=\admin policy=read, write, policy, test source=":local resolvedIP [:resolve \"\#.duckdns.org\"];\\n:local currentIP [/ip cloud get public-address];\\n:local currentIP [:pick \$currentIP 0 [:find \$currentIP \"/\"]];\\n\\n:if (\$resolvedIP != \$currentIP) do={\\n :log info (\"Trying to update DuckDNS with actual IP \".\$currentIP.\\", resolved IP is \".\$resolvedIP);\\n :local response [/tool fetch url=(\"https://www.duckdns.org/update\?\domains=#.duckdns.org&token=\\#&ip=\".\$currentIP) check-certificat\e=yes as-value output=user];\\n :if (\$response->\"status\" = \"finished\") do={\\n :if (\$response->\"data\" = \"OK\") do={\\n :log info (\"Successfully updated DuckDNS with new IP \".\$c\urrentIP);\\n } else={\\n :log error (\"Failed to update DuckDNS with new IP \".\$curr\entIP);\\n }\\n }\\n}"/tool mac-serverset allowed-interface-list=LAN/tool mac-server mac-winboxset allowed-interface-list=LAN==== ====after all of that, Still cannot access the router via IP address. same as before. why ? any suggestions ? ---

## Response 5
On accessing the router by IP address....... do you mean using winbox, I always use macaddress for the very simple reason its easier and available and just need to click on it.If I use IP address I have to actually physically type in the IP address and remember also the winbox port ( one of the first things I do is change the default winbox port ).To confirm you want all traffic both vlan10 home users and vlan22 users to go out wireguard for internet.If so, why are you concerned about vlan22 (guests using wan2) by the forward firewall rule (blocking it) . We will be sending all its traffic out wireguard not wan1 or wan2 ????Does this imply that if the wireguard is NOT available for some issue at the other end ( not your local WAN ), they you want your home users to then access local internet?These types of requirements details affect config design!!Also confusing is why are you using two wans. If all lan traffic is going out WAN1 through the wireguard tunnel, why waste money on WAN2.You are leaving out key information, especially on the purpose of the WANs. ---

## Response 6
As for the TP link switch is configured incorrectly but you left out some of the other TP link config screens to confirm either way???The single or bonded ports on the router/interface bridge portsadd bridge=bridge ingress-filtering=yes frame-types=admit-only-vlan-tagged interface=ether3( or bonding1 ) is correct its a trunk port to the switch./interface bridge vlansadd bridge=bridge tagged=bridge, ether3 ( or bonded1) untagged=wlan1 vlan-ids=10is correctadd bridge=bridge tagged=bridge, ether3 ( or bonded1) untagged=wlan2 vlan-ids=22On the Switch I expect to see.VLANID1 ----> default: Tagged member on trunk ports ( aka port coming from router, and any port going to another smart device )10 ----> home: Tagged member on trunk ports, untagged for any ports going to dumb home devices22 -----> guest: Tagged member on trunk port coming from router, Untagged for any ports going to dumb guest devices.Port PVID settings.For any dumb port you sent the vlan ID of the vlan on that port (either 10 or 22 ).For any dumb port not yet assigned, use vlan ID of 1 ( should already be set as default anyway )Thus vlan1 is NOT a member of any ports going to dumb devices.For any smart ports assigned, thepvidremains vlan ID1 the default.SO, basically pvid=1, unless the port is an access port for a vlan ( aka going to a dumb device ).What I cannot recall off the top of my head is whether the trunk ports are left tagged or untagged for vlan1..........you might want to play with that to confirm. ---

## Response 7
On accessing the router by IP address....... do you mean using winbox, I always use macaddress for the very simple reason its easier and available and just need to click on it.If I use IP address I have to actually physically type in the IP address and remember also the winbox port ( one of the first things I do is change the default winbox port ).Mac address cannot be use in Mikrotik Home App, and that app is very simple UI to monitoring the router, thats why I need IP address to access the router., and why with this vpn implemented it's not working?, I'm trying to experiment on Routing->Rules, on 192.168.88.0/24 subnet, I add marking to main table then route lookup to-Cloudflare tables, but this is not stable, sometimes I can access sometimes not, also the connection looks like ambiguous, why ?==== ====To confirm you want all traffic both vlan10 home users and vlan22 users to go out wireguard for internet.If so, why are you concerned about vlan22 (guests using wan2) by the forward firewall rule (blocking it) . We will be sending all its traffic out wireguard not wan1 or wan2 ????In here I just want to share my main internet 'ether1/wan1' to my neighbors using guest access, but if the main internet down the neighbors will be restricted to access to backup internet/ether2/wan2 because in here backup is using quota limit/ the internet access is limited by the provider and expensive.==== ====Does this imply that if the wireguard is NOT available for some issue at the other end ( not your local WAN ), they you want your home users to then access local internet?These types of requirements details affect config design!!No, I just want all internet is through to vpn, home/guest will use vpn, because I think it's more secureIf something happens with that VPN, in client devices simply disconnect from this network, and directly connect into wan, because both of the wan spread wireless network.This mikrotik network will be act like vpn firewall maybe ?I mean, If I want internet that using vpn, simply I connect my client devices into this network==== ====Also confusing is why are you using two wans. If all lan traffic is going out WAN1 through the wireguard tunnel, why waste money on WAN2.You are leaving out key information, especially on the purpose of the WANs.The Wan2 it's connect to a mobile 4g devices, it's only use if the main internet fiber optic Wan1 is down.I have 8 iot devices that connect into this home network, if wan1 down I can't controll those devices, so why I still need wan2 as backup, because it's very hard if I should reconnect those iot devices into my mobile 4g networkAny suggestions? ---

## Response 8
As for the TP link switch is configured incorrectly but you left out some of the other TP link config screens to confirm either way???I'm sorry, the switch that I use only one, and I need adjustable for the new config. Here is the new config for the switch. Is that correct ?tplink switch, vlan1 should be remain untagged.PNGOn the switch port, the port 1 and 5 is directly to a client devices, and i want that client to get IP from home subnet, then i untagged port 1 and 5 for vlan 10 its should be correct right ? but why i get unidentifying network on my laptop ?The single or bonded ports on the router/interface bridge portsadd bridge=bridge ingress-filtering=yes frame-types=admit-only-vlan-tagged interface=ether3( or bonding1 ) is correct its a trunk port to the switch.It's should be pvid=1 right ?, I try change frame-types from admit-all to admit-only-vlan-tagged, then it's not working, admit-only-vlan-tagged it's mean only for vlan 1 ? but this port should through vlan 10 and 22, why admit-only-vlan-tagged ?/interface bridge vlansadd bridge=bridge tagged=bridge, ether3 ( or bonded1) untagged=wlan1 vlan-ids=10is correctadd bridge=bridge tagged=bridge, ether3 ( or bonded1) untagged=wlan2 vlan-ids=22==On the Switch I expect to see.VLANID1 ----> default: Tagged member on trunk ports ( aka port coming from router, and any port going to another smart device )10 ----> home: Tagged member on trunk ports, untagged for any ports going to dumb home devices22 -----> guest: Tagged member on trunk port coming from router, Untagged for any ports going to dumb guest devices.tagged means if any incoming / outcoming port for many vlan, while untagged mean single port for single vlan ? am I correct ?Port PVID settings.For any dumb port you sent the vlan ID of the vlan on that port (either 10 or 22 ).For any dumb port not yet assigned, use vlan ID of 1 ( should already be set as default anyway )Thus vlan1 is NOT a member of any ports going to dumb devices.For any smart ports assigned, thepvidremains vlan ID1 the default.SO, basically pvid=1, unless the port is an access port for a vlan ( aka going to a dumb device ).What I cannot recall off the top of my head is whether the trunk ports are left tagged or untagged for vlan1..........you might want to play with that to confirm.should vlan 1 be tagged into all ports? default configuration on the switch and bridge vlan is untagged for vlan1, is this correct?mikrotik, vlan1 should be remain untagged.PNG==== ? ====- What's the different between my first configuration ? My first configuration, the bridge directly connected on the subnet 192.168.88.0/24. But in new configuration that subnet is connected to home-vlan 10, what the difference of this configuration ? ---

## Response 9
Okay, I think I understand.All LAN traffic will go through VPN.VPN will use WAN1.If WAN1 goes down, you want only HOME users to be able to access WAN2 during this time.Please confirm that WAN2 traffic should also go out VPN for internet and not directly WAN2 to www.On the TPLINK Switch1. VLANID1 is NOT a member of port 1 and 5.PVID of port1 and port5 should 10.VLAN10 should be an UNTAGGED member of port 1 and 5.2. VlanID1 is NOT a member of port 2PVID of port2 is 22VLAN22 should be an UNTAGGED member of port23. VLAN10 Should be a tagged member of port3, port4 ( or bonded lag )VLAN22 should be a tagged member or port3, port4 ( or bonded lag )VLAN1 should be an untagged member of port3 and port4 ( or bonded lag ) ---

## Response 10
Your bridge diagram doesnt seem quite correct yet...However the config it came from would have been better to view./export file=anynameyouwish (minus router serial number, any public WANIP information, keys etc..)The IOT devices should not be a problem. The VPN should move to WAN2 in case of failover...... ---

## Response 11
This is correct until you add back in etherport 4, but lets get the rest of the config up and working first, all vlans, and wireguard working, then worry about bringing ether4 and lag/bond back up!!!/interface bridge portsadd bridge=bridge ingress-filtering=yes frame-types=admit-only-vlan-tagged interface=ether3/interface bridge vlansadd bridge=bridge tagged=bridge, ether3 untagged=wlan1 vlan-ids=10add bridge=bridge tagged=bridge, ether3 untagged=wlan2 vlan-ids=22Now we need to see rest of config.By the way use config quote marks at start and end of config to keep it short...... the black square with white parenthesise on teh same line as Bold and Italics!!Assuming cloudflare wireguard provided endpoint address endpoint port and private key and used the private key provided when creating the Mikrotik wireguard instance correct?Also did they provide any DNS information to use?? ---

## Response 12
Okay, I think I understand.All LAN traffic will go through VPN.VPN will use WAN1.If WAN1 goes down, you want only HOME users to be able to access WAN2 during this time.Please confirm that WAN2 traffic should also go out VPN for internet and not directly WAN2 to www.Yes that's right, VPN also use in WAN2.On the TPLINK Switch1. VLANID1 is NOT a member of port 1 and 5.PVID of port1 and port5 should 10.VLAN10 should be an UNTAGGED member of port 1 and 5.2. VlanID1 is NOT a member of port 2PVID of port2 is 22VLAN22 should be an UNTAGGED member of port23. VLAN10 Should be a tagged member of port3, port4 ( or bonded lag )VLAN22 should be a tagged member or port3, port4 ( or bonded lag )VLAN1 should be an untagged member of port3 and port4 ( or bonded lag )on tp-link switch, port2 is used by tplink access point to spread the network, since the ap is support vlan, I should tagged on port2 right ?is this new configuration correct ?, but why I still get unidentified network when I connect my laptop into port 1 or 5 ?tplink switch, 30102024.PNG==== ====I figured it out, I should set pvid on the switch pvid menu settings, I just realized that pvid is stands for "Port VLAN ID" and is used to tag untagged traffic that enters a switch port.Now ports 1 and 5 on the switch can provide internet access to my laptop.But still, I can't connect Winbox/Mikrotik home app through IP address into the router. why ??? ---

## Response 13
Here is the new Mikrotik configuration.
```
# 2024-10-30 00:44:50 by RouterOS 7.16.1
# software id = #
#
# model = RB941-2nD
# serial number = #
/interface bridge
add admin-mac=# auto-mac=no comment=defconf \
    ingress-filtering=no name=bridge port-cost-mode=short vlan-filtering=yes
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=20/40mhz-XX \
    country=indonesia distance=indoors frequency=auto installation=indoor \
    mode=ap-bridge ssid=Scale wireless-protocol=802.11
/interface ethernet
set [ find default-name=ether4 ] comment=debugging
/interface wireguard
add comment="Cloudflare WireGuard" listen-port=13231 mtu=1420 name=wireguard1
/interface vlan
add comment=guestconf interface=bridge name=guest-vlan22 vlan-id=22
add comment=default-home-conf interface=bridge name=home-vlan10 vlan-id=10
/interface bonding
add disabled=yes name=bonding1 slaves=ether3,ether4
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface wireless security-profiles
set [ find default=yes ] authentication-types=wpa-psk,wpa2-psk eap-methods="" \
    mode=dynamic-keys supplicant-identity=MikroTik
add eap-methods="" name=guest supplicant-identity=""
/interface wireless
add keepalive-frames=disabled mac-address=# master-interface=\
    wlan1 multicast-buffering=disabled name=wlan2 security-profile=guest \
    ssid="Scale Guest" wds-cost-range=0 wds-default-cost=0 wps-mode=disabled
/ip kid-control
add fri=0s-1d mon=0s-1d name=system-dummy sat=0s-1d sun=0s-1d thu=0s-1d tue=\
    0s-1d tur-fri=0s-1d tur-mon=0s-1d tur-sat=0s-1d tur-sun=0s-1d tur-thu=\
    0s-1d tur-tue=0s-1d tur-wed=0s-1d wed=0s-1d
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
add name=guest-dhcp ranges=192.168.84.2-192.168.84.8
/ip dhcp-server
add address-pool=default-dhcp interface=home-vlan10 lease-time=10m name=\
    defconf
add address-pool=guest-dhcp interface=guest-vlan22 lease-time=10m name=\
    guestconf
/queue simple
add max-limit=1M/1M name=queue-guest target=guest-vlan22
/routing ospf instance
add disabled=no name=default-v2
/routing ospf area
add disabled=yes instance=default-v2 name=backbone-v2
/routing table
add comment="Cloudflare WireGuard" disabled=no fib name=to-Cloudflare
/interface bridge port
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether2 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf frame-types=admit-only-vlan-tagged \
    interface=ether3 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether4 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf interface=pwr-line1 internal-path-cost=10 \
    path-cost=10
add bridge=bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-tagged interface=wlan1 \
    internal-path-cost=10 path-cost=10 pvid=10
add bridge=bridge disabled=yes ingress-filtering=no interface=bonding1 \
    internal-path-cost=10 path-cost=10
add bridge=bridge frame-types=admit-only-untagged-and-priority-tagged \
    interface=wlan2 internal-path-cost=10 path-cost=10 pvid=22
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=LAN
/ip settings
set max-neighbor-entries=8192
/ipv6 settings
set disable-ipv6=yes max-neighbor-entries=8192
/interface bridge vlan
add bridge=bridge tagged=bridge,ether3 untagged=wlan2 vlan-ids=22
add bridge=bridge tagged=bridge,ether3 untagged=wlan1 vlan-ids=10
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=ether2 list=WAN
add comment=debugging interface=ether4 list=LAN
add comment=mynet interface=home-vlan10 list=LAN
add interface=guest-vlan22 list=LAN
/interface ovpn-server server
set auth=sha1,md5
/interface wireguard peers
add allowed-address=0.0.0.0/0 comment="Cloudflare WireGuard" \
    endpoint-address=engage.cloudflareclient.com endpoint-port=2408 \
    interface=wireguard1 name="cloudflare wireguard" persistent-keepalive=35s \
    public-key="#"
/ip address
add address=192.168.88.1/24 comment=defconf interface=home-vlan10 network=\
    192.168.88.0
add address=192.168.84.1/28 comment=guestconf interface=guest-vlan22 network=\
    192.168.84.0
add address=192.168.100.100/24 comment=wan1 interface=ether1 network=\
    192.168.100.0
add address=192.168.2.100/24 comment=wan2 interface=ether2 network=\
    192.168.2.0
add address=172.16.0.2/24 comment="Cloudflare WireGuard" interface=wireguard1 \
    network=172.16.0.0
add address=192.168.68.1/30 comment=debugging interface=ether4 network=\
    192.168.68.0
/ip dhcp-client
add comment=defconf disabled=yes interface=ether1
add comment=defconf disabled=yes interface=ether2
/ip dhcp-server lease
add address=192.168.88.2 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.6 mac-address=# server=defconf
add address=192.168.88.3 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.4 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.5 mac-address=# server=defconf
/ip dhcp-server network
add address=192.168.84.0/28 comment=guestconf gateway=192.168.84.1
add address=192.168.88.0/24 comment=defconf gateway=192.168.88.1
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,1.0.0.1
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
add address=192.168.100.1 name=wan1.logi.lo type=A
add address=192.168.2.1 name=wan2.logi.lo type=A
add address=192.168.88.6 name=stb1.logi.lo type=A
add address=127.0.0.1 name=stb2.logi.lo type=A
add address=192.168.88.4 name=eap1.logi.lo type=A
add address=192.168.100.254 name=cpe1.logi.lo type=A
add address=192.168.88.2 name=switch1.logi.lo type=A
add address=192.168.88.3 name=switch2.logi.lo type=A
add address=192.168.88.5 name=tlmr1.logi.lo type=A
/ip firewall filter
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
add action=drop chain=forward comment="guestconf: drop to ether2" \
    in-interface=guest-vlan22 out-interface=ether2
/ip firewall mangle
add action=change-mss chain=forward comment="Cloudflare WireGuard" new-mss=\
    1380 out-interface=wireguard1 passthrough=no protocol=tcp tcp-flags=syn \
    tcp-mss=1381-65535
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat comment="Cloudflare WireGuard" \
    out-interface=wireguard1
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/ip kid-control device
add mac-address=# name="Redmi-10C;2" user=""
add mac-address=# name="ESP-67B077;6" user=""
/ip route
add check-gateway=ping comment=Recursive disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=1.1.1.1 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=12
add check-gateway=ping comment=Main disabled=no distance=1 dst-address=\
    1.1.1.1/32 gateway=192.168.100.1 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=11
add check-gateway=ping comment=Backup disabled=no distance=2 dst-address=\
    0.0.0.0/0 gateway=192.168.2.1 routing-table=main scope=30 \
    suppress-hw-offload=no target-scope=10
add comment="Cloudflare WireGuard" disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=wireguard1 routing-table=to-Cloudflare scope=30 \
    suppress-hw-offload=no target-scope=10
/routing bfd configuration
add disabled=yes interfaces=all min-rx=200ms min-tx=200ms multiplier=5
/routing rule
add action=lookup-only-in-table comment="Cloudflare WireGuard" disabled=no \
    min-prefix=0 table=main
add action=lookup-only-in-table disabled=no src-address=192.168.88.0/24 \
    table=to-Cloudflare
add action=lookup-only-in-table disabled=no src-address=192.168.84.0/28 \
    table=to-Cloudflare
/system clock
set time-zone-name=Asia/Jakarta
/system note
set show-at-login=no
/system scheduler
add interval=2d name=reboot on-event="/system reboot" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:32:56
add interval=2h name="dns clear" on-event="/ip dns cache flush" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:35:12
add comment="trigger duckdns updater" interval=1m name="duckdns updater" \
    on-event="/system script run duckdns" policy=read,write,policy,test \
    start-time=startup
/system script
add comment="duckdns updater" dont-require-permissions=no name=duckdns owner=\
    admin policy=read,write,policy,test source=":local resolvedIP [:resolve \"\
    #.duckdns.org\"];\
    \n:local currentIP [/ip cloud get public-address];\
    \n:local currentIP [:pick \$currentIP 0 [:find \$currentIP \"/\"]];\
    \n\
    \n:if (\$resolvedIP != \$currentIP) do={\
    \n    :log info (\"Trying to update DuckDNS with actual IP \".\$currentIP.\
    \", resolved IP is \".\$resolvedIP);\
    \n    :local response [/tool fetch url=(\"https://www.duckdns.org/update\?\
    domains=#.duckdns.org&token=\
    \#&ip=\".\$currentIP) check-certificat\
    e=yes as-value output=user];\
    \n    :if (\$response->\"status\" = \"finished\") do={\
    \n        :if (\$response->\"data\" = \"OK\") do={\
    \n            :log info (\"Successfully updated DuckDNS with new IP \".\$c\
    urrentIP);\
    \n        } else={\
    \n            :log error (\"Failed to update DuckDNS with new IP \".\$curr\
    entIP);\
    \n        }\
    \n    }\
    \n}"
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN

---
```

## Response 14
Assuming cloudflare wireguard provided endpoint address endpoint port and private key and used the private key provided when creating the Mikrotik wireguard instance correct?Also did they provide any DNS information to use??yes I'm using thishttps://github.com/ViRb3/wgcfto generate cloudflare VPN warp connection for wireguard.cloudflare also provide 1.1.1.1 1.0.0.1 dns. ---

## Response 15
Changes onlyBY the way your bridge ports were not adjusted, if you dont apply recommended changes we cannot progress, and note that taking ether4 off the bridge means NOT having it as bridge port!Also removed ref to powerline, your router doesnt have an extra powerline connection that I am aware of......... how do you connect to powerline products???You didnt remove bridge from interface list.You didnt add in extra security!!TRUSTEDinterface etc...........Forgetting the input chain rules I recommended at least change the forward chain as per below........Rule of thumb is do not use same dns address as being used for recursive so will use other.........After more thought, its a bit trickier than first imagined.The complexity is that we want to allow guest to use WAN1 but not WAN2BUT, we want all traffic to go out wireguard for internet.Thus the WAN being used is transparent to the user and in a way to the router.So have to figure out how to block user from wireguard access if the routing is via WAN2......I suspect will need netwatch to monitor WAN and use that to modify firewall rule.That will be in next post not this one.# 2024-10-30 00:44:50 by RouterOS 7.16.1# software id = ### model = RB941-2nD# serial number = #/interface bridgeadd admin-mac=# auto-mac=no comment=defconf \ingress-filtering=no name=bridge port-cost-mode=short vlan-filtering=yes/interface wirelessset [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=20/40mhz-XX \country=indonesia distance=indoors frequency=auto installation=indoor \mode=ap-bridge ssid=Scale wireless-protocol=802.11/interface ethernetset [ find default-name=ether4 ] comment=debugging/interface wireguardadd comment="Cloudflare WireGuard" listen-port=13231 mtu=1420 name=wireguard1/interface vlanadd comment=guestconf interface=bridge name=guest-vlan22 vlan-id=22add comment=default-home-conf interface=bridge name=home-vlan10 vlan-id=10/interface bondingadd disabled=yes name=bonding1 slaves=ether3, ether4/interface listadd comment=defconf name=WANadd comment=defconf name=LANadd name=TRUSTED/interface wireless security-profilesset [ find default=yes ] authentication-types=wpa-psk, wpa2-psk eap-methods="" \mode=dynamic-keys supplicant-identity=MikroTikadd eap-methods="" name=guest supplicant-identity=""/interface wirelessadd keepalive-frames=disabled mac-address=# master-interface=\wlan1 multicast-buffering=disabled name=wlan2 security-profile=guest \ssid="Scale Guest" wds-cost-range=0 wds-default-cost=0 wps-mode=disabled/ip kid-controladd fri=0s-1d mon=0s-1d name=system-dummy sat=0s-1d sun=0s-1d thu=0s-1d tue=\0s-1d tur-fri=0s-1d tur-mon=0s-1d tur-sat=0s-1d tur-sun=0s-1d tur-thu=\0s-1d tur-tue=0s-1d tur-wed=0s-1d wed=0s-1d/ip pooladd name=default-dhcp ranges=192.168.88.10-192.168.88.254add name=guest-dhcp ranges=192.168.84.2-192.168.84.8/ip dhcp-serveradd address-pool=default-dhcp interface=home-vlan10 lease-time=10m name=\defconfadd address-pool=guest-dhcp interface=guest-vlan22 lease-time=10m name=\guestconf/queue simpleadd max-limit=1M/1M name=queue-guest target=guest-vlan22disable=yes{to isolate this from any current issues, apply later}/routing ospf instanceadd disabled=no name=default-v2/routing ospf areaadd disabled=yes instance=default-v2 name=backbone-v2/routing tableadd comment="Cloudflare WireGuard" disabled=no fib name=to-Cloudflare/interface bridge portadd bridge=bridge ingress-filtering=yes frame-types=admit-untagged-and-priority-tagged interface=wlan1 pvid=10add bridge=bridge ingress-filtering=yes frame-types=admit-untagged-and-priority-tagged interface=wlan2 pvid=22add bridge=bridge ingress-filtering=yes frame-types=admit-untagged-and-priority-tagged interface=ether3 pvid=10/ip firewall connection trackingset udp-timeout=10s/ip neighbor discovery-settingsset discover-interface-list=TRUSTED/ip settingsset max-neighbor-entries=8192/ipv6 settingsset disable-ipv6=yes max-neighbor-entries=8192/interface bridge vlanadd bridge=bridge tagged=bridge, ether3 untagged=wlan2 vlan-ids=22add bridge=bridge tagged=bridge, ether3 untagged=wlan1 vlan-ids=10/interface list memberadd comment=defconf interface=ether1 list=WANadd interface=ether2 list=WANadd comment=debugging interface=ether4 list=LANadd comment=mynet interface=home-vlan10 list=LANadd interface=guest-vlan22 list=LANadd interface=home-vlan10 list=TRUSTED/interface ovpn-server serverset auth=sha1, md5/interface wireguard peersadd allowed-address=0.0.0.0/0 comment="Cloudflare WireGuard" \endpoint-address=engage.cloudflareclient.com endpoint-port=2408 \interface=wireguard1 name="cloudflare wireguard" persistent-keepalive=35s \public-key="#"/ip addressadd address=192.168.88.1/24 comment=defconf interface=home-vlan10 network=\192.168.88.0add address=192.168.84.1/28 comment=guestconf interface=guest-vlan22 network=\192.168.84.0add address=192.168.100.100/24 comment=wan1 interface=ether1 network=\192.168.100.0add address=192.168.2.100/24 comment=wan2 interface=ether2 network=\192.168.2.0add address=172.16.0.2/24 comment="Cloudflare WireGuard" interface=wireguard1 \network=172.16.0.0add address=192.168.68.1/30 comment=debugging interface=ether4 network=\192.168.68.0/ip dhcp-clientadd comment=defconf disabled=yes interface=ether1add comment=defconf disabled=yes interface=ether2/ip dhcp-server leaseadd address=192.168.88.2 client-id=# mac-address=\# server=defconfadd address=192.168.88.6 mac-address=# server=defconfadd address=192.168.88.3 client-id=# mac-address=\# server=defconfadd address=192.168.88.4 client-id=# mac-address=\# server=defconfadd address=192.168.88.5 mac-address=# server=defconf/ip dhcp-server networkadd address=192.168.84.0/28 comment=guestconf gateway=192.168.84.1dns-server=1.1.1.1, 1.0.0.1add address=192.168.88.0/24 comment=defconf gateway=192.168.88.1dns-server=1.1.1.1, 1.0.0.1/ip dnsset allow-remote-requests=yes servers=1.1.1.1, 1.0.0.1/ip dns staticadd address=192.168.88.1 comment=defconf name=router.lan type=Aadd address=192.168.100.1 name=wan1.logi.lo type=Aadd address=192.168.2.1 name=wan2.logi.lo type=Aadd address=192.168.88.6 name=stb1.logi.lo type=Aadd address=127.0.0.1 name=stb2.logi.lo type=Aadd address=192.168.88.4 name=eap1.logi.lo type=Aadd address=192.168.100.254 name=cpe1.logi.lo type=Aadd address=192.168.88.2 name=switch1.logi.lo type=Aadd address=192.168.88.3 name=switch2.logi.lo type=Aadd address=192.168.88.5 name=tlmr1.logi.lo type=A/ip firewall filteradd action=accept chain=input comment=\"defconf: accept established, related, untracked" connection-state=\established, related, untrackedadd action=drop chain=input comment="defconf: drop invalid" connection-state=\invalidadd action=accept chain=input comment="defconf: accept ICMP" protocol=icmpadd action=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1add action=drop chain=input comment="defconf: drop all not coming from LAN" \in-interface-list=!LANadd action=fasttrack-connection chain=forward comment="defconf: fasttrack" \connection-state=established, related hw-offload=yesadd action=accept chain=forward comment=\"defconf: accept established, related, untracked" connection-state=\established, related, untrackedadd action=drop chain=forward comment="defconf: drop invalid" \connection-state=invalidadd action=accept chain=forward comment="internet" in-interface-list=LAN out-interface=wireguard1add action=accept chain=forward comment="guest-WAN1-only" in-interface=guest-vlan22 out-interface=wireguard1add action=drop chain=forward commment="drop all else"/ip firewall mangleadd action=change-mss chain=forward comment="Cloudflare WireGuard" new-mss=\1380 out-interface=wireguard1 passthrough=no protocol=tcp tcp-flags=syn \tcp-mss=1381-65535/ip firewall natadd action=masquerade chain=srcnat comment="defconf: masquerade" \ipsec-policy=out, none out-interface-list=WANadd action=masquerade chain=srcnat comment="Cloudflare WireGuard" \out-interface=wireguard1add action=dst-nat chain=dstnat in-interface=home-vlan10 dst-port=53 to-address=172.16.0.1add action=dst-nat chain=dstnat in-interface=home-vlan22 dst-port=53 to-address=172.16.0.1{ ensuring dns request goes through the tunnel vice local }/ip ipsec profileset [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5/ip kid-control deviceadd mac-address=# name="Redmi-10C;2" user=""add mac-address=# name="ESP-67B077;6" user=""/ip routeadd check-gateway=ping comment=Recursive disabled=no distance=1 dst-address=\0.0.0.0/0 gateway=9.9.9.9routing-table=main scope=10 \suppress-hw-offload=no target-scope=12add check-gateway=ping comment=Main disabled=no distance=1 dst-address=\9.9.9.9/32gateway=192.168.100.1 routing-table=main scope=10 \suppress-hw-offload=no target-scope=11add check-gateway=ping comment=Backup disabled=no distance=2 dst-address=\0.0.0.0/0 gateway=192.168.2.1 routing-table=main scope=30 \suppress-hw-offload=no target-scope=10add comment="Cloudflare WireGuard" disabled=no distance=1 dst-address=\0.0.0.0/0 gateway=wireguard1 routing-table=to-Cloudflare scope=30 \suppress-hw-offload=no target-scope=10/routing bfd configurationadd disabled=yes interfaces=all min-rx=200ms min-tx=200ms multiplier=5/routing ruleadd action=lookup-only-in-table comment="Cloudflare WireGuard" disabled=no \min-prefix=0 table=mainadd action=lookup-only-in-table disabled=no src-address=192.168.88.0/24 \table=to-Cloudflareadd action=lookup-only-in-table disabled=no src-address=192.168.84.0/28 \table=to-Cloudflare/system clockset time-zone-name=Asia/Jakarta/system noteset show-at-login=no/system scheduleradd interval=2d name=reboot on-event="/system reboot" policy=\ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon \start-date=2021-02-28 start-time=16:32:56add interval=2h name="dns clear" on-event="/ip dns cache flush" policy=\ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon \start-date=2021-02-28 start-time=16:35:12add comment="trigger duckdns updater" interval=1m name="duckdns updater" \on-event="/system script run duckdns" policy=read, write, policy, test \start-time=startup/system scriptadd comment="duckdns updater" dont-require-permissions=no name=duckdns owner=\admin policy=read, write, policy, test source=":local resolvedIP [:resolve \"\#.duckdns.org\"];\\n:local currentIP [/ip cloud get public-address];\\n:local currentIP [:pick \$currentIP 0 [:find \$currentIP \"/\"]];\\n\\n:if (\$resolvedIP != \$currentIP) do={\\n :log info (\"Trying to update DuckDNS with actual IP \".\$currentIP.\\", resolved IP is \".\$resolvedIP);\\n :local response [/tool fetch url=(\"https://www.duckdns.org/update\?\domains=#.duckdns.org&token=\\#&ip=\".\$currentIP) check-certificat\e=yes as-value output=user];\\n :if (\$response->\"status\" = \"finished\") do={\\n :if (\$response->\"data\" = \"OK\") do={\\n :log info (\"Successfully updated DuckDNS with new IP \".\$c\urrentIP);\\n } else={\\n :log error (\"Failed to update DuckDNS with new IP \".\$curr\entIP);\\n }\\n }\\n}/tool mac-serverset allowed-interface-list=NONE/tool mac-server mac-winboxset allowed-interface-list=TRUSTED ---

## Response 16
Changes onlyBY the way your bridge ports were not adjusted, if you dont apply recommended changes we cannot progress, and note that taking ether4 off the bridge means NOT having it as bridge port!Also removed ref to powerline, your router doesnt have an extra powerline connection that I am aware of......... how do you connect to powerline products???You didnt remove bridge from interface list.You didnt add in extra security!!TRUSTEDinterface etc...........Forgetting the input chain rules I recommended at least change the forward chain as per below........Rule of thumb is do not use same dns address as being used for recursive so will use other.........After more thought, its a bit trickier than first imagined.The complexity is that we want to allow guest to use WAN1 but not WAN2BUT, we want all traffic to go out wireguard for internet.Thus the WAN being used is transparent to the user and in a way to the router.So have to figure out how to block user from wireguard access if the routing is via WAN2......I suspect will need netwatch to monitor WAN and use that to modify firewall rule.That will be in next post not this one.I connect powerline product using 5v micro usb port.add action=accept chain=forward comment="internet" in-interface-list=LAN out-interface=wireguard1add action=accept chain=forward comment="guest-WAN1-only" in-interface=guest-vlan22 out-interface=wireguard1add action=drop chain=forward commment="drop all else"why should I add guest-WAN1-only, if the guest-vlan22 is part of the interface list LAN? it should use the 'internet' filter rules right?why drop all else?add action=dst-nat chain=dstnat in-interface=home-vlan10 dst-port=53 to-address=172.16.0.1add action=dst-nat chain=dstnat in-interface=home-vlan22 dst-port=53 to-address=172.16.0.1{ ensuring dns request goes through the tunnel vice local }I tried the code above and got this
```
failure: ports can be specified if proto is tcp,udp,udp-lite,dccp,sctperror, so I assume is TCP protocol.Now I cannot connect to my network, even don't even get an IP address.Here is the new configuration.
```

```
# 2024-10-30 22:06:28 by RouterOS 7.16.1
# software id = #
#
# model = RB941-2nD
# serial number = #
/interface bridge
add admin-mac=# auto-mac=no comment=defconf \
    ingress-filtering=no name=bridge port-cost-mode=short vlan-filtering=yes
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=20/40mhz-XX \
    country=indonesia distance=indoors frequency=auto installation=indoor \
    mode=ap-bridge ssid=Scale wireless-protocol=802.11
/interface ethernet
set [ find default-name=ether4 ] comment=debugging
/interface wireguard
add comment="Cloudflare WireGuard" listen-port=13231 mtu=1420 name=wireguard1
/interface vlan
add comment=guestconf interface=bridge name=guest-vlan22 vlan-id=22
add comment=homeconf interface=bridge name=home-vlan10 vlan-id=10
/interface bonding
add disabled=yes name=bonding1 slaves=ether3,ether4
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
add comment=extraconf name=TRUSTED
/interface wireless security-profiles
set [ find default=yes ] authentication-types=wpa-psk,wpa2-psk eap-methods="" \
    mode=dynamic-keys supplicant-identity=MikroTik
add eap-methods="" name=guest supplicant-identity=""
/interface wireless
add keepalive-frames=disabled mac-address=# master-interface=\
    wlan1 multicast-buffering=disabled name=wlan2 security-profile=guest \
    ssid="Scale Guest" wds-cost-range=0 wds-default-cost=0 wps-mode=disabled
/ip kid-control
add fri=0s-1d mon=0s-1d name=system-dummy sat=0s-1d sun=0s-1d thu=0s-1d tue=\
    0s-1d tur-fri=0s-1d tur-mon=0s-1d tur-sat=0s-1d tur-sun=0s-1d tur-thu=\
    0s-1d tur-tue=0s-1d tur-wed=0s-1d wed=0s-1d
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
add name=guest-dhcp ranges=192.168.84.2-192.168.84.8
/ip dhcp-server
add address-pool=default-dhcp interface=home-vlan10 lease-time=10m name=\
    defconf
add address-pool=guest-dhcp interface=guest-vlan22 lease-time=10m name=\
    guestconf
/queue simple
add disabled=yes max-limit=1M/1M name=queue-guest target=guest-vlan22
/routing ospf instance
add disabled=no name=default-v2
/routing ospf area
add disabled=yes instance=default-v2 name=backbone-v2
/routing table
add comment="Cloudflare WireGuard" disabled=no fib name=to-Cloudflare
/interface bridge port
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether2 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-tagged interface=ether3 \
    internal-path-cost=10 path-cost=10 pvid=10
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether4 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf disabled=yes interface=pwr-line1 \
    internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-tagged interface=wlan1 \
    internal-path-cost=10 path-cost=10 pvid=10
add bridge=bridge disabled=yes ingress-filtering=no interface=bonding1 \
    internal-path-cost=10 path-cost=10
add bridge=bridge frame-types=admit-only-untagged-and-priority-tagged \
    interface=wlan2 internal-path-cost=10 path-cost=10 pvid=22
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=TRUSTED
/ip settings
set max-neighbor-entries=8192
/ipv6 settings
set disable-ipv6=yes max-neighbor-entries=8192
/interface bridge vlan
add bridge=bridge tagged=bridge,ether3 untagged=wlan2 vlan-ids=22
add bridge=bridge tagged=bridge,ether3 untagged=wlan1 vlan-ids=10
/interface list member
add comment=defconf interface=home-vlan10 list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=ether2 list=WAN
add comment=debugging interface=ether4 list=LAN
add comment=guestconf interface=guest-vlan22 list=LAN
add comment=extraconf interface=home-vlan10 list=TRUSTED
add interface=ether4 list=TRUSTED
/interface ovpn-server server
set auth=sha1,md5
/interface wireguard peers
add allowed-address=0.0.0.0/0 comment="Cloudflare WireGuard" \
    endpoint-address=engage.cloudflareclient.com endpoint-port=2408 \
    interface=wireguard1 name="cloudflare wireguard" persistent-keepalive=35s \
    public-key="#"
/ip address
add address=192.168.88.1/24 comment=defconf interface=home-vlan10 network=\
    192.168.88.0
add address=192.168.84.1/28 comment=guestconf interface=guest-vlan22 network=\
    192.168.84.0
add address=192.168.100.100/24 comment=wan1 interface=ether1 network=\
    192.168.100.0
add address=192.168.2.100/24 comment=wan2 interface=ether2 network=\
    192.168.2.0
add address=172.16.0.2/24 comment="Cloudflare WireGuard" interface=wireguard1 \
    network=172.16.0.0
add address=192.168.68.1/30 comment=debugging interface=ether4 network=\
    192.168.68.0
/ip dhcp-client
add comment=defconf disabled=yes interface=ether1
add comment=defconf disabled=yes interface=ether2
/ip dhcp-server lease
add address=192.168.88.2 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.6 mac-address=# server=defconf
add address=192.168.88.3 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.4 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.5 mac-address=# server=defconf
/ip dhcp-server network
add address=192.168.84.0/28 comment=guestconf dns-server=1.1.1.1,1.0.0.1 \
    gateway=192.168.84.1
add address=192.168.88.0/24 comment=defconf dns-server=1.1.1.1,1.0.0.1 \
    gateway=192.168.88.1
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,1.0.0.1
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
add address=192.168.100.1 name=wan1.logi.lo type=A
add address=192.168.2.1 name=wan2.logi.lo type=A
add address=192.168.88.6 name=stb1.logi.lo type=A
add address=127.0.0.1 name=stb2.logi.lo type=A
add address=192.168.88.4 name=eap1.logi.lo type=A
add address=192.168.100.254 name=cpe1.logi.lo type=A
add address=192.168.88.2 name=switch1.logi.lo type=A
add address=192.168.88.3 name=switch2.logi.lo type=A
add address=192.168.88.5 name=tlmr1.logi.lo type=A
/ip firewall filter
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
add action=accept chain=forward comment="Cloudflare WireGuard" \
    in-interface-list=LAN out-interface=wireguard1
add action=accept chain=forward in-interface=guest-vlan22 out-interface=\
    wireguard1
add action=drop chain=forward comment="drop all else"
/ip firewall mangle
add action=change-mss chain=forward comment="Cloudflare WireGuard" new-mss=\
    1380 out-interface=wireguard1 passthrough=no protocol=tcp tcp-flags=syn \
    tcp-mss=1381-65535
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat comment="Cloudflare WireGuard" \
    out-interface=wireguard1
add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \
    protocol=tcp to-addresses=172.16.0.1
add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \
    protocol=tcp to-addresses=172.16.0.1
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/ip kid-control device
add mac-address=# name="Redmi-10C;2" user=""
add mac-address=# name="ESP-67B077;6" user=""
/ip route
add check-gateway=ping comment=Recursive disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=9.9.9.9 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=12
add check-gateway=ping comment=Main disabled=no distance=1 dst-address=\
    9.9.9.9/32 gateway=192.168.100.1 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=11
add check-gateway=ping comment=Backup disabled=no distance=2 dst-address=\
    0.0.0.0/0 gateway=192.168.2.1 routing-table=main scope=30 \
    suppress-hw-offload=no target-scope=10
add comment="Cloudflare WireGuard" disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=wireguard1 routing-table=to-Cloudflare scope=30 \
    suppress-hw-offload=no target-scope=10
/routing bfd configuration
add disabled=yes interfaces=all min-rx=200ms min-tx=200ms multiplier=5
/routing rule
add action=lookup comment="Cloudflare WireGuard" disabled=no min-prefix=0 \
    table=main
add action=lookup disabled=no dst-address=192.168.88.0/24 min-prefix=0 \
    src-address=192.168.88.0/24 table=main
add action=lookup-only-in-table disabled=no src-address=192.168.88.0/24 \
    table=to-Cloudflare
add action=lookup-only-in-table disabled=no src-address=192.168.84.0/28 \
    table=to-Cloudflare
/system clock
set time-zone-name=Asia/Jakarta
/system note
set show-at-login=no
/system scheduler
add interval=2d name=reboot on-event="/system reboot" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:32:56
add interval=2h name="dns clear" on-event="/ip dns cache flush" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:35:12
add comment="trigger duckdns updater" interval=1m name="duckdns updater" \
    on-event="/system script run duckdns" policy=read,write,policy,test \
    start-time=startup
/system script
add comment="duckdns updater" dont-require-permissions=no name=duckdns owner=\
    admin policy=read,write,policy,test source=":local resolvedIP [:resolve \"\
    #.duckdns.org\"];\
    \n:local currentIP [/ip cloud get public-address];\
    \n:local currentIP [:pick \$currentIP 0 [:find \$currentIP \"/\"]];\
    \n\
    \n:if (\$resolvedIP != \$currentIP) do={\
    \n    :log info (\"Trying to update DuckDNS with actual IP \".\$currentIP.\
    \", resolved IP is \".\$resolvedIP);\
    \n    :local response [/tool fetch url=(\"https://www.duckdns.org/update\?\
    domains=#.duckdns.org&token=\
    \#&ip=\".\$currentIP) check-certificat\
    e=yes as-value output=user];\
    \n    :if (\$response->\"status\" = \"finished\") do={\
    \n        :if (\$response->\"data\" = \"OK\") do={\
    \n            :log info (\"Successfully updated DuckDNS with new IP \".\$c\
    urrentIP);\
    \n        } else={\
    \n            :log error (\"Failed to update DuckDNS with new IP \".\$curr\
    entIP);\
    \n        }\
    \n    }\
    \n}"
/tool mac-server
set allowed-interface-list=TRUSTED
/tool mac-server mac-winbox
set allowed-interface-list=TRUSTED

---
```

## Response 17
The good news is that you still can access the router ( hopefully via ether4 ) as you can provide a config.Yes Sorry it should be four rules.add action=dst-nat chain=dstnat in-interface=home-vlan10 dst-port=53protocol=udpto-address=172.16.0.1add action=dst-nat chain=dstnat in-interface=home-vlan22 dst-port=53protocol=udpto-address=172.16.0.1add action=dst-nat chain=dstnat in-interface=home-vlan10 dst-port=53protocol=tcpto-address=172.16.0.1add action=dst-nat chain=dstnat in-interface=home-vlan22 dst-port=53protocol=tcpto-address=172.16.0.1How does the usb micro port show up as a selectable option on the r outer???If it does then yes by all means add it back to /interface bridge ports and bridge vlans++++++++++++++++++++++++++++++++If you noticed, we didNOTadd guest vlan to the LAN interface list for a couple of reasons..a. This specifically prevents the vlan from accessing the local routers WAN because its not permitted to access the router DNS services and thus would never go out of WAn1 or Wan2 ( the only way out would be via VPN WAN )b. No usual LAN interface to WAN interface list rule, so that no users can go out local WAN(instead its LAN to WIREGUARD only)c. we create an extra rule just for guest-vlan because we will disable this single rule using netwatch when WAN1 goes down.......... ---

## Response 18
1. Why are all your bridge ports disabled??? only ether4 should be disabled ( for now ) in any case cleaned up all.......Why is ether2 on the bridge at all, its one of the WAN ports right?Ether3 is a trunk port going to the TPLINK switch, it has no PVID.Lets fix it....../interface bridge portadd bridge=bridge ingress-filtering=yes frame-types=admit-only-tagged-vlan interface=ether3add bridge=bridge ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged interface=wlan1 pvid=10add bridge=bridge ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged interface=wlan2 pvid=22add bridge=bridge ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged interface=pwr-line1 pvid=102. Adjust for pwr-line/interface bridge vlanadd bridge=bridge tagged=bridge, ether3 untagged=wlan2 vlan-ids=22add bridge=bridge tagged=bridge, ether3 untagged=wlan1, pwr-line1vlan-ids=103. remove guest vlan from LAN interface list...../interface list memberadd comment=defconf interface=ether1 list=WANadd interface=ether2 list=WANadd comment=defconf interface=home-vlan10 list=LANadd comment=debugging interface=ether4 list=LANadd comment=extraconf interface=home-vlan10 list=TRUSTEDadd interface=ether4 list=TRUSTED4. You didnt get rid of the default rule which we replaced with other rules.......add action=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \connection-state=new in-interface-list=WANSo should simply look like this:add action=fasttrack-connection chain=forward comment="defconf: fasttrack" \connection-state=established, related hw-offload=yesadd action=accept chain=forward comment=\"defconf: accept established, related, untracked" connection-state=\established, related, untrackedadd action=drop chain=forward comment="defconf: drop invalid" \connection-state=invalidadd action=accept chain=forward comment="Cloudflare WireGuard" \in-interface-list=LAN out-interface=wireguard1add action=accept chain=forward in-interface=guest-vlan22 out-interface=\wireguard1add action=drop chain=forward comment="drop all else"5. Dont need ping check on second rule of recursive./ip routeadd check-gateway=ping comment=Recursive dst-address=0.0.0.0/0 gateway=9.9.9.9 routing-table=main scope=10 target-scope=12add dst-address=9.9.9.9/32 gateway=192.168.100.1 routing-table=main scope=10 target-scope=11add check-gateway=ping comment=Backup distance=2 dst-address=0.0.0.0/0 gateway=192.168.2.1 routing-table=mainadd comment="Cloudflare WireGuard" dst-address=0.0.0.0/0 gateway=wireguard1 routing-table=to-Cloudflare6. Routing rules seem to have been changed, reworked to this.../routing ruleadd action=lookup-only-in-table comment="maintain local connectivity" min-prefix=0 table=mainadd action=lookup-only-in-table src-address=192.168.88.0/24 table=to-Cloudflareadd action=lookup-only-in-table src-address=192.168.84.0/28 table=to-Cloudflare7. Only winbox variant is encrypted, so/tool mac-serverset allowed-interface-list=NONE/tool mac-server mac-winboxset allowed-interface-list=TRUSTED ---

## Response 19
How does the usb micro port show up as a selectable option on the r outer???If it does then yes by all means add it back to /interface bridge ports and bridge vlansI don't know, it just shows on default/factory configuration, but the micro usb port only for power, not data, I think so.add action=dst-nat chain=dstnat in-interface=home-vlan10 dst-port=53 protocol=udp to-address=172.16.0.1add action=dst-nat chain=dstnat in-interface=home-vlan22 dst-port=53 protocol=udp to-address=172.16.0.1add action=dst-nat chain=dstnat in-interface=home-vlan10 dst-port=53 protocol=tcp to-address=172.16.0.1add action=dst-nat chain=dstnat in-interface=home-vlan22 dst-port=53 protocol=tcp to-address=172.16.0.1Why should add these ? how about if website request another ports that not provided ?4. You didnt get rid of the default rule which we replaced with other rules.......add action=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \connection-state=new in-interface-list=WANSo should simply look like this:add action=fasttrack-connection chain=forward comment="defconf: fasttrack" \connection-state=established, related hw-offload=yesadd action=accept chain=forward comment=\"defconf: accept established, related, untracked" connection-state=\established, related, untrackedadd action=drop chain=forward comment="defconf: drop invalid" \connection-state=invalidadd action=accept chain=forward comment="Cloudflare WireGuard" \in-interface-list=LAN out-interface=wireguard1add action=accept chain=forward in-interface=guest-vlan22 out-interface=\wireguard1add action=drop chain=forward comment="drop all else"I need to disable this
```
"defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \
connection-state=new in-interface-list=WANright ?Now I can get IP address from the router, but no internet connection.
```

```
# 2024-10-31 06:44:06 by RouterOS 7.16.1
# software id = #
#
# model = RB941-2nD
# serial number = #
/interface bridge
add admin-mac=# auto-mac=no comment=defconf \
    ingress-filtering=no name=bridge port-cost-mode=short vlan-filtering=yes
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=20/40mhz-XX \
    country=indonesia distance=indoors frequency=auto installation=indoor \
    mode=ap-bridge ssid=Scale wireless-protocol=802.11
/interface ethernet
set [ find default-name=ether4 ] comment=debugging
/interface wireguard
add comment="Cloudflare WireGuard" listen-port=13231 mtu=1420 name=wireguard1
/interface vlan
add comment=guestconf interface=bridge name=guest-vlan22 vlan-id=22
add comment=homeconf interface=bridge name=home-vlan10 vlan-id=10
/interface bonding
add disabled=yes name=bonding1 slaves=ether3,ether4
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
add comment=extraconf name=TRUSTED
/interface wireless security-profiles
set [ find default=yes ] authentication-types=wpa-psk,wpa2-psk eap-methods="" \
    mode=dynamic-keys supplicant-identity=MikroTik
add eap-methods="" name=guest supplicant-identity=""
/interface wireless
add keepalive-frames=disabled mac-address=# master-interface=\
    wlan1 multicast-buffering=disabled name=wlan2 security-profile=guest \
    ssid="Scale Guest" wds-cost-range=0 wds-default-cost=0 wps-mode=disabled
/ip kid-control
add fri=0s-1d mon=0s-1d name=system-dummy sat=0s-1d sun=0s-1d thu=0s-1d tue=\
    0s-1d tur-fri=0s-1d tur-mon=0s-1d tur-sat=0s-1d tur-sun=0s-1d tur-thu=\
    0s-1d tur-tue=0s-1d tur-wed=0s-1d wed=0s-1d
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
add name=guest-dhcp ranges=192.168.84.2-192.168.84.8
/ip dhcp-server
add address-pool=default-dhcp interface=home-vlan10 lease-time=10m name=\
    defconf
add address-pool=guest-dhcp interface=guest-vlan22 lease-time=10m name=\
    guestconf
/queue simple
add disabled=yes max-limit=1M/1M name=queue-guest target=guest-vlan22
/routing ospf instance
add disabled=no name=default-v2
/routing ospf area
add disabled=yes instance=default-v2 name=backbone-v2
/routing table
add comment="Cloudflare WireGuard" disabled=no fib name=to-Cloudflare
/interface bridge port
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether2 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf frame-types=admit-only-vlan-tagged \
    interface=ether3 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether4 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-tagged interface=pwr-line1 \
    internal-path-cost=10 path-cost=10 pvid=10
add bridge=bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-tagged interface=wlan1 \
    internal-path-cost=10 path-cost=10 pvid=10
add bridge=bridge disabled=yes ingress-filtering=no interface=bonding1 \
    internal-path-cost=10 path-cost=10
add bridge=bridge frame-types=admit-only-untagged-and-priority-tagged \
    interface=wlan2 internal-path-cost=10 path-cost=10 pvid=22
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=TRUSTED
/ip settings
set max-neighbor-entries=8192
/ipv6 settings
set disable-ipv6=yes max-neighbor-entries=8192
/interface bridge vlan
add bridge=bridge tagged=bridge,ether3 untagged=wlan2 vlan-ids=22
add bridge=bridge tagged=bridge,ether3 untagged=wlan1,pwr-line1 vlan-ids=10
/interface list member
add comment=defconf interface=home-vlan10 list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=ether2 list=WAN
add comment=debugging interface=ether4 list=LAN
add comment=extraconf interface=home-vlan10 list=TRUSTED
add interface=ether4 list=TRUSTED
/interface ovpn-server server
set auth=sha1,md5
/interface wireguard peers
add allowed-address=0.0.0.0/0 comment="Cloudflare WireGuard" \
    endpoint-address=engage.cloudflareclient.com endpoint-port=2408 \
    interface=wireguard1 name="cloudflare wireguard" persistent-keepalive=35s \
    public-key="#"
/ip address
add address=192.168.88.1/24 comment=defconf interface=home-vlan10 network=\
    192.168.88.0
add address=192.168.84.1/28 comment=guestconf interface=guest-vlan22 network=\
    192.168.84.0
add address=192.168.100.100/24 comment=wan1 interface=ether1 network=\
    192.168.100.0
add address=192.168.2.100/24 comment=wan2 interface=ether2 network=\
    192.168.2.0
add address=172.16.0.2/24 comment="Cloudflare WireGuard" interface=wireguard1 \
    network=172.16.0.0
add address=192.168.68.1/30 comment=debugging interface=ether4 network=\
    192.168.68.0
/ip dhcp-client
add comment=defconf disabled=yes interface=ether1
add comment=defconf disabled=yes interface=ether2
/ip dhcp-server lease
add address=192.168.88.2 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.6 mac-address=# server=defconf
add address=192.168.88.3 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.4 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.5 mac-address=# server=defconf
/ip dhcp-server network
add address=192.168.84.0/28 comment=guestconf dns-server=1.1.1.1,1.0.0.1 \
    gateway=192.168.84.1
add address=192.168.88.0/24 comment=defconf dns-server=1.1.1.1,1.0.0.1 \
    gateway=192.168.88.1
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,1.0.0.1
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
add address=192.168.100.1 name=wan1.logi.lo type=A
add address=192.168.2.1 name=wan2.logi.lo type=A
add address=192.168.88.6 name=stb1.logi.lo type=A
add address=127.0.0.1 name=stb2.logi.lo type=A
add address=192.168.88.4 name=eap1.logi.lo type=A
add address=192.168.100.254 name=cpe1.logi.lo type=A
add address=192.168.88.2 name=switch1.logi.lo type=A
add address=192.168.88.3 name=switch2.logi.lo type=A
add address=192.168.88.5 name=tlmr1.logi.lo type=A
/ip firewall filter
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
    connection-state=new disabled=yes in-interface-list=WAN
add action=accept chain=forward comment="Cloudflare WireGuard" \
    in-interface-list=LAN out-interface=wireguard1
add action=accept chain=forward in-interface=guest-vlan22 out-interface=\
    wireguard1
add action=drop chain=forward comment="drop all else"
/ip firewall mangle
add action=change-mss chain=forward comment="Cloudflare WireGuard" new-mss=\
    1380 out-interface=wireguard1 passthrough=no protocol=tcp tcp-flags=syn \
    tcp-mss=1381-65535
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat comment="Cloudflare WireGuard" \
    out-interface=wireguard1
add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \
    protocol=tcp to-addresses=172.16.0.1
add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \
    protocol=udp to-addresses=172.16.0.1
add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \
    protocol=tcp to-addresses=172.16.0.1
add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \
    protocol=udp to-addresses=172.16.0.1
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/ip kid-control device
add mac-address=# name="Redmi-10C;2" user=""
add mac-address=# name="ESP-67B077;6" user=""
/ip route
add check-gateway=ping comment=Recursive disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=9.9.9.9 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=12
add check-gateway=ping comment=Main disabled=no distance=1 dst-address=\
    9.9.9.9/32 gateway=192.168.100.1 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=11
add check-gateway=ping comment=Backup disabled=no distance=2 dst-address=\
    0.0.0.0/0 gateway=192.168.2.1 routing-table=main scope=30 \
    suppress-hw-offload=no target-scope=10
add comment="Cloudflare WireGuard" disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=wireguard1 routing-table=to-Cloudflare scope=30 \
    suppress-hw-offload=no target-scope=10
/routing bfd configuration
add disabled=yes interfaces=all min-rx=200ms min-tx=200ms multiplier=5
/routing rule
add action=lookup-only-in-table comment="maintain local connectivity" \
    disabled=no min-prefix=0 table=main
add action=lookup-only-in-table comment="Cloudflare WireGuard" disabled=no \
    src-address=192.168.88.0/24 table=to-Cloudflare
add action=lookup-only-in-table disabled=no src-address=192.168.84.0/28 \
    table=to-Cloudflare
/system clock
set time-zone-name=Asia/Jakarta
/system note
set show-at-login=no
/system scheduler
add interval=2d name=reboot on-event="/system reboot" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:32:56
add interval=2h name="dns clear" on-event="/ip dns cache flush" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:35:12
add comment="trigger duckdns updater" interval=1m name="duckdns updater" \
    on-event="/system script run duckdns" policy=read,write,policy,test \
    start-time=startup
/system script
add comment="duckdns updater" dont-require-permissions=no name=duckdns owner=\
    admin policy=read,write,policy,test source=":local resolvedIP [:resolve \"\
    #.duckdns.org\"];\
    \n:local currentIP [/ip cloud get public-address];\
    \n:local currentIP [:pick \$currentIP 0 [:find \$currentIP \"/\"]];\
    \n\
    \n:if (\$resolvedIP != \$currentIP) do={\
    \n    :log info (\"Trying to update DuckDNS with actual IP \".\$currentIP.\
    \", resolved IP is \".\$resolvedIP);\
    \n    :local response [/tool fetch url=(\"https://www.duckdns.org/update\?\
    domains=#.duckdns.org&token=\
    \#&ip=\".\$currentIP) check-certificat\
    e=yes as-value output=user];\
    \n    :if (\$response->\"status\" = \"finished\") do={\
    \n        :if (\$response->\"data\" = \"OK\") do={\
    \n            :log info (\"Successfully updated DuckDNS with new IP \".\$c\
    urrentIP);\
    \n        } else={\
    \n            :log error (\"Failed to update DuckDNS with new IP \".\$curr\
    entIP);\
    \n        }\
    \n    }\
    \n}"
/tool mac-server
set allowed-interface-list=none
/tool mac-server mac-winbox
set allowed-interface-list=TRUSTED

---
```

## Response 20
Yes for the nth time get rid of this rule.add action=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \connection-state=new disabled=yes in-interface-list=WANOther than that not sure why its not working. ---

## Response 21
Yes for the nth time get rid of this rule.add action=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \connection-state=newdisabled=yesin-interface-list=WANI already disable that rules, mean same as remove it right ?Other than that not sure why its not working.Hmm, I'm sorry, I try again, I get internet connection, but, the devices say there is "no internet connection", why?https://ibb.co.com/nc90wwvadd action=dst-nat chain=dstnat in-interface=home-vlan10 dst-port=53 to-address=172.16.0.1add action=dst-nat chain=dstnat in-interface=home-vlan22 dst-port=53 to-address=172.16.0.1 { ensuring dns request goes through the tunnel vice local }Ahh I just already realize, that this for dns, and website it's using dns to get to their server, and it's use port 53, as you said that this to ensure dns request goes through the vpn, According, to this postviewtopic.php?t=148077, that devices like android, is check internet connection by checking the dns, then it's should be okay right ?, but why I'm my case I still get notifications that "no internet connection" but I still can browsing through internet? HmmI'm using WiFiMan by ubiquity to check ping, and I got N/A result on gateway 192.168.88.1, hmm is there something I miss ?https://ibb.co.com/VqHbGR3And still, I can't connect to router via IP addresshttps://ibb.co.com/BzFQMSd ---

## Response 22
I just realized that the Nat firewall is provided wrong IP address of wireguard, the IP address that assigned to wireguard interface is 172.16.0.2, so I change from 172.16.0.1 to 172.16.0.2, now my internet connection work, and no notification "no internet connection" on my devices.But still I can't connect to my router through IP address, and Mikrotik App on smartphone not working.I just try to trace why this happens, and I found out that "routing -> rules", that's make the host/client devices cannot communicate to gateway 192.168.88.1, even ping will produce request time out that's why it make any app Winbox Desktop / Mobile version can't connect to router via IP address, then how do I solve this ? Any suggestions? ---

## Response 23
Post your latest config and please explain a bit more clearly what is NOT working yet . ---

## Response 24
Post your latest config and please explain a bit more clearly what is NOT working yet .Before that, I want to say thank you for helping and guiding me to understand the Mikrotik configurationFirst, I can surf into internet, but some websites like this forum can't be loaded.mikrotik wireguard, some website cannot be access.PNGSecond, I can't ping into gateway 192.168.88.1 or 192.168.86.1, and cannot connect the Winbox desktop or mobile version to the router via IP address.mikrotik winbox, cannot connect router via ip address.PNGThird, If try to disable routing -> rules, it will become normal, I can ping into the gateway and get access Winbox to the router via IP address.mikrotik winbox, disable routing rules make ping normal to gateway.PNGHere is the new configuration.
```
# 2024-11-01 07:34:57 by RouterOS 7.16.1
# software id = #
#
# model = RB941-2nD
# serial number = #
/interface bridge
add admin-mac=# auto-mac=no comment=defconf \
    ingress-filtering=no name=bridge port-cost-mode=short vlan-filtering=yes
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=20/40mhz-XX \
    country=indonesia distance=indoors frequency=auto installation=indoor \
    mode=ap-bridge ssid=Scale wireless-protocol=802.11
/interface ethernet
set [ find default-name=ether4 ] comment=debugging
/interface wireguard
add comment="Cloudflare WireGuard" listen-port=13231 mtu=1420 name=wireguard1
/interface vlan
add comment=guestconf interface=bridge name=guest-vlan22 vlan-id=22
add comment=homeconf interface=bridge name=home-vlan10 vlan-id=10
/interface bonding
add disabled=yes name=bonding1 slaves=ether3,ether4
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
add comment=extraconf name=TRUSTED
/interface wireless security-profiles
set [ find default=yes ] authentication-types=wpa-psk,wpa2-psk eap-methods="" \
    mode=dynamic-keys supplicant-identity=MikroTik
add eap-methods="" name=guest supplicant-identity=""
/interface wireless
add keepalive-frames=disabled mac-address=# master-interface=\
    wlan1 multicast-buffering=disabled name=wlan2 security-profile=guest \
    ssid="Scale Guest" wds-cost-range=0 wds-default-cost=0 wps-mode=disabled
/ip kid-control
add fri=0s-1d mon=0s-1d name=system-dummy sat=0s-1d sun=0s-1d thu=0s-1d tue=\
    0s-1d tur-fri=0s-1d tur-mon=0s-1d tur-sat=0s-1d tur-sun=0s-1d tur-thu=\
    0s-1d tur-tue=0s-1d tur-wed=0s-1d wed=0s-1d
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
add name=guest-dhcp ranges=192.168.84.2-192.168.84.8
/ip dhcp-server
add address-pool=default-dhcp interface=home-vlan10 lease-time=10m name=\
    defconf
add address-pool=guest-dhcp interface=guest-vlan22 lease-time=10m name=\
    guestconf
/queue simple
add disabled=yes max-limit=1M/1M name=queue-guest target=guest-vlan22
/routing ospf instance
add disabled=no name=default-v2
/routing ospf area
add disabled=yes instance=default-v2 name=backbone-v2
/routing table
add comment="Cloudflare WireGuard" disabled=no fib name=to-Cloudflare
/interface bridge port
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether2 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf frame-types=admit-only-vlan-tagged \
    interface=ether3 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether4 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-tagged interface=pwr-line1 \
    internal-path-cost=10 path-cost=10 pvid=10
add bridge=bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-tagged interface=wlan1 \
    internal-path-cost=10 path-cost=10 pvid=10
add bridge=bridge disabled=yes ingress-filtering=no interface=bonding1 \
    internal-path-cost=10 path-cost=10
add bridge=bridge frame-types=admit-only-untagged-and-priority-tagged \
    interface=wlan2 internal-path-cost=10 path-cost=10 pvid=22
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=TRUSTED
/ip settings
set max-neighbor-entries=8192
/ipv6 settings
set disable-ipv6=yes max-neighbor-entries=8192
/interface bridge vlan
add bridge=bridge tagged=bridge,ether3 untagged=wlan2 vlan-ids=22
add bridge=bridge tagged=bridge,ether3 untagged=wlan1,pwr-line1 vlan-ids=10
/interface list member
add comment=defconf interface=home-vlan10 list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=ether2 list=WAN
add comment=debugging interface=ether4 list=LAN
add comment=extraconf interface=home-vlan10 list=TRUSTED
add interface=ether4 list=TRUSTED
/interface ovpn-server server
set auth=sha1,md5
/interface wireguard peers
add allowed-address=0.0.0.0/0 comment="Cloudflare WireGuard" \
    endpoint-address=engage.cloudflareclient.com endpoint-port=2408 \
    interface=wireguard1 name="cloudflare wireguard" persistent-keepalive=35s \
    public-key="#"
/ip address
add address=192.168.88.1/24 comment=defconf interface=home-vlan10 network=\
    192.168.88.0
add address=192.168.84.1/28 comment=guestconf interface=guest-vlan22 network=\
    192.168.84.0
add address=192.168.100.100/24 comment=wan1 interface=ether1 network=\
    192.168.100.0
add address=192.168.2.100/24 comment=wan2 interface=ether2 network=\
    192.168.2.0
add address=172.16.0.2/24 comment="Cloudflare WireGuard" interface=wireguard1 \
    network=172.16.0.0
add address=192.168.68.1/30 comment=debugging interface=ether4 network=\
    192.168.68.0
/ip dhcp-client
add comment=defconf disabled=yes interface=ether1
add comment=defconf disabled=yes interface=ether2
/ip dhcp-server lease
add address=# client-id=# mac-address=\
    # server=defconf
add address=192.168.88.6 mac-address=# server=defconf
add address=192.168.88.3 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.4 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.5 mac-address=# server=defconf
/ip dhcp-server network
add address=192.168.84.0/28 comment=guestconf dns-server=1.1.1.1,1.0.0.1 \
    gateway=192.168.84.1
add address=192.168.88.0/24 comment=defconf dns-server=1.1.1.1,1.0.0.1 \
    gateway=192.168.88.1
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,1.0.0.1
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
add address=192.168.100.1 name=wan1.logi.lo type=A
add address=192.168.2.1 name=wan2.logi.lo type=A
add address=192.168.88.6 name=stb1.logi.lo type=A
add address=127.0.0.1 name=stb2.logi.lo type=A
add address=192.168.88.4 name=eap1.logi.lo type=A
add address=192.168.100.254 name=cpe1.logi.lo type=A
add address=192.168.88.2 name=switch1.logi.lo type=A
add address=192.168.88.3 name=switch2.logi.lo type=A
add address=192.168.88.5 name=tlmr1.logi.lo type=A
/ip firewall filter
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
    connection-state=new disabled=yes in-interface-list=WAN
add action=accept chain=forward comment="Cloudflare WireGuard" \
    in-interface-list=LAN out-interface=wireguard1
add action=accept chain=forward in-interface=guest-vlan22 out-interface=\
    wireguard1
add action=drop chain=forward comment="drop all else"
/ip firewall mangle
add action=change-mss chain=forward comment="Cloudflare WireGuard" new-mss=\
    1380 out-interface=wireguard1 passthrough=no protocol=tcp tcp-flags=syn \
    tcp-mss=1381-65535
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat comment="Cloudflare WireGuard" \
    out-interface=wireguard1
add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \
    protocol=tcp to-addresses=172.16.0.2
add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \
    protocol=udp to-addresses=172.16.0.2
add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \
    protocol=tcp to-addresses=172.16.0.2
add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \
    protocol=udp to-addresses=172.16.0.2
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/ip kid-control device
add mac-address=# name="Redmi-10C;2" user=""
add mac-address=# name="ESP-67B077;6" user=""
/ip route
add check-gateway=ping comment=Recursive disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=9.9.9.9 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=12
add check-gateway=ping comment=Main disabled=no distance=1 dst-address=\
    9.9.9.9/32 gateway=192.168.100.1 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=11
add check-gateway=ping comment=Backup disabled=no distance=2 dst-address=\
    0.0.0.0/0 gateway=192.168.2.1 routing-table=main scope=30 \
    suppress-hw-offload=no target-scope=10
add comment="Cloudflare WireGuard" disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=wireguard1 routing-table=to-Cloudflare scope=30 \
    suppress-hw-offload=no target-scope=10
/routing bfd configuration
add disabled=yes interfaces=all min-rx=200ms min-tx=200ms multiplier=5
/routing rule
add action=lookup-only-in-table comment="maintain local connectivity" \
    disabled=no min-prefix=0 table=main
add action=lookup-only-in-table comment="Cloudflare WireGuard" disabled=no \
    src-address=192.168.88.0/24 table=to-Cloudflare
add action=lookup-only-in-table disabled=no src-address=192.168.84.0/28 \
    table=to-Cloudflare
/system clock
set time-zone-name=Asia/Jakarta
/system note
set show-at-login=no
/system scheduler
add interval=2d name=reboot on-event="/system reboot" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:32:56
add interval=2h name="dns clear" on-event="/ip dns cache flush" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:35:12
add comment="trigger duckdns updater" interval=1m name="duckdns updater" \
    on-event="/system script run duckdns" policy=read,write,policy,test \
    start-time=startup
/system script
add comment="duckdns updater" dont-require-permissions=no name=duckdns owner=\
    admin policy=read,write,policy,test source=":local resolvedIP [:resolve \"\
    #.duckdns.org\"];\
    \n:local currentIP [/ip cloud get public-address];\
    \n:local currentIP [:pick \$currentIP 0 [:find \$currentIP \"/\"]];\
    \n\
    \n:if (\$resolvedIP != \$currentIP) do={\
    \n    :log info (\"Trying to update DuckDNS with actual IP \".\$currentIP.\
    \", resolved IP is \".\$resolvedIP);\
    \n    :local response [/tool fetch url=(\"https://www.duckdns.org/update\?\
    domains=#.duckdns.org&token=\
    \#&ip=\".\$currentIP) check-certificat\
    e=yes as-value output=user];\
    \n    :if (\$response->\"status\" = \"finished\") do={\
    \n        :if (\$response->\"data\" = \"OK\") do={\
    \n            :log info (\"Successfully updated DuckDNS with new IP \".\$c\
    urrentIP);\
    \n        } else={\
    \n            :log error (\"Failed to update DuckDNS with new IP \".\$curr\
    entIP);\
    \n        }\
    \n    }\
    \n}"
/tool mac-server
set allowed-interface-list=none
/tool mac-server mac-winbox
set allowed-interface-list=TRUSTEDAny suggestions?

---
```

## Response 25
1. Confirm when you are surfing the net, the source is the home router IP??? aka through wireguard!!1.Confirm cannot connect via winboxa. using wifi connectionb. using ethernet4if you changed the winbox port from default then you need to put in IPaddress:port#I always use mac address.2. Change these to reflect the IP address of the third party so should be.add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \protocol=tcp to-addresses=172.16.0.1add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \protocol=udp to-addresses=172.16.0.1add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \protocol=tcp to-addresses=172.16.0.1add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \protocol=udp to-addresses=172.16.0.13. Modify DNS to/ip dnsset server=1.1.1.1, 1.0.0.14. Remove second check-gateway=ping on recursive routes so should look likeadd check-gateway=ping comment=Recursive dst-address=0.0.0.0/0 gateway=9.9.9.9 routing-table=main scope=10 target-scope=12add comment=Main dst-address=9.9.9.9/32 gateway=192.168.100.1 routing-table=main scope=10 target-scope=115. Cannot see anything that would be preventing access?6. Replace and Change Mangle rule to and see if that works better on difficult websites.add action=change-mss chain=forward new-mss=1380 out-interface=wireguard1 protocol=tcp tcp-flags=syn tcp-mss=1381-65535 ---

## Response 26
Also, what do you mean you cannot ping the subnets..........Ping from where???So the major changes are dstnat rules IP address is the remote address 172.16.0.1and the IP DNS settings are simplyadd server=1.1.1.1, 1.0.0.1Once we get everything working THEN we will do the failover changes!!! ---

## Response 27
1. Confirm when you are surfing the net, the source is the home router IP??? aka through wireguard!!Yes, the client device's laptop/phone is connected to a Mikrotik router that uses wireguard.1.Confirm cannot connect via winboxa. using wifi connectionb. using ethernet4Using ethernet4 is normal.But using wifi or ethernet is not normal. I assume because somehow routing -> rules that make this not working. because if I disable the config for subnet 192.168.88.0/24 or 192.168.86.0/24 it will work. But if it is enabled then it's not working even if I can't ping to gateway.mikrotik winbox, winbox cannot connect router via ip address.PNGif you changed the winbox port from default then you need to put in IPaddress:port#I always use mac address.I didn't change anything. Also I want Mikrotik Home App on android is working, because is very nice GUI to monitor the Mikrotik devices.2. Change these to reflect the IP address of the third party so should be.add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \protocol=tcp to-addresses=172.16.0.1add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \protocol=udp to-addresses=172.16.0.1add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \protocol=tcp to-addresses=172.16.0.1add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \protocol=udp to-addresses=172.16.0.1I change this to-addresses 172.168.0.1, the internet connection not working, the internet status is "no internet connection".3. Modify DNS to/ip dnsset server=1.1.1.1, 1.0.0.1I already set this.4. Remove second check-gateway=ping on recursive routes so should look likeadd check-gateway=ping comment=Recursive dst-address=0.0.0.0/0 gateway=9.9.9.9 routing-table=main scope=10 target-scope=12add comment=Main dst-address=9.9.9.9/32 gateway=192.168.100.1 routing-table=main scope=10 target-scope=11Okay, I set this.5. Cannot see anything that would be preventing access?I didn't know why.6. Replace and Change Mangle rule to and see if that works better on difficult websites.add action=change-mss chain=forward new-mss=1380 out-interface=wireguard1 protocol=tcp tcp-flags=syn tcp-mss=1381-65535Okay, I set this.Also, what do you mean you cannot ping the subnets..........Ping from where???So the major changes are dstnat rules IP address is the remote address 172.16.0.1and the IP DNS settings are simplyadd server=1.1.1.1, 1.0.0.1Once we get everything working THEN we will do the failover changes!!!Please review the attachment image. ---

## Response 28
Please post the current config for review. ---

## Response 29
Please post the current config for review.Here is the new configuration.
```
# 2024-11-03 03:27:47 by RouterOS 7.16.1
# software id = #
#
# model = RB941-2nD
# serial number = #
/interface bridge
add admin-mac=# auto-mac=no comment=defconf \
    ingress-filtering=no name=bridge port-cost-mode=short vlan-filtering=yes
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=20/40mhz-XX \
    country=indonesia distance=indoors frequency=auto installation=indoor \
    mode=ap-bridge ssid=Scale wireless-protocol=802.11
/interface ethernet
set [ find default-name=ether4 ] comment=debugging
/interface wireguard
add comment="Cloudflare WireGuard" listen-port=13231 mtu=1420 name=wireguard1
/interface vlan
add comment=guestconf interface=bridge name=guest-vlan22 vlan-id=22
add comment=homeconf interface=bridge name=home-vlan10 vlan-id=10
/interface bonding
add disabled=yes name=bonding1 slaves=ether3,ether4
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
add comment=extraconf name=TRUSTED
/interface wireless security-profiles
set [ find default=yes ] authentication-types=wpa-psk,wpa2-psk eap-methods="" \
    mode=dynamic-keys supplicant-identity=MikroTik
add eap-methods="" name=guest supplicant-identity=""
/interface wireless
add keepalive-frames=disabled mac-address=# master-interface=\
    wlan1 multicast-buffering=disabled name=wlan2 security-profile=guest \
    ssid="Scale Guest" wds-cost-range=0 wds-default-cost=0 wps-mode=disabled
/ip kid-control
add fri=0s-1d mon=0s-1d name=system-dummy sat=0s-1d sun=0s-1d thu=0s-1d tue=\
    0s-1d tur-fri=0s-1d tur-mon=0s-1d tur-sat=0s-1d tur-sun=0s-1d tur-thu=\
    0s-1d tur-tue=0s-1d tur-wed=0s-1d wed=0s-1d
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
add name=guest-dhcp ranges=192.168.84.2-192.168.84.8
/ip dhcp-server
add address-pool=default-dhcp interface=home-vlan10 lease-time=10m name=\
    defconf
add address-pool=guest-dhcp interface=guest-vlan22 lease-time=10m name=\
    guestconf
/queue simple
add disabled=yes max-limit=1M/1M name=queue-guest target=guest-vlan22
/routing ospf instance
add disabled=no name=default-v2
/routing ospf area
add disabled=yes instance=default-v2 name=backbone-v2
/routing table
add comment="Cloudflare WireGuard" disabled=no fib name=to-Cloudflare
/interface bridge port
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether2 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf frame-types=admit-only-vlan-tagged \
    interface=ether3 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether4 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-tagged interface=pwr-line1 \
    internal-path-cost=10 path-cost=10 pvid=10
add bridge=bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-tagged interface=wlan1 \
    internal-path-cost=10 path-cost=10 pvid=10
add bridge=bridge disabled=yes ingress-filtering=no interface=bonding1 \
    internal-path-cost=10 path-cost=10
add bridge=bridge frame-types=admit-only-untagged-and-priority-tagged \
    interface=wlan2 internal-path-cost=10 path-cost=10 pvid=22
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=TRUSTED
/ip settings
set max-neighbor-entries=8192
/ipv6 settings
set disable-ipv6=yes max-neighbor-entries=8192
/interface bridge vlan
add bridge=bridge tagged=bridge,ether3 untagged=wlan2 vlan-ids=22
add bridge=bridge tagged=bridge,ether3 untagged=wlan1,pwr-line1 vlan-ids=10
/interface list member
add comment=defconf interface=home-vlan10 list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=ether2 list=WAN
add comment=debugging interface=ether4 list=LAN
add comment=extraconf interface=home-vlan10 list=TRUSTED
add interface=ether4 list=TRUSTED
/interface ovpn-server server
set auth=sha1,md5
/interface wireguard peers
add allowed-address=0.0.0.0/0 comment="Cloudflare WireGuard" \
    endpoint-address=engage.cloudflareclient.com endpoint-port=2408 \
    interface=wireguard1 name="cloudflare wireguard" persistent-keepalive=35s \
    public-key="#"
/ip address
add address=192.168.88.1/24 comment=defconf interface=home-vlan10 network=\
    192.168.88.0
add address=192.168.84.1/28 comment=guestconf interface=guest-vlan22 network=\
    192.168.84.0
add address=192.168.100.100/24 comment=wan1 interface=ether1 network=\
    192.168.100.0
add address=192.168.2.100/24 comment=wan2 interface=ether2 network=\
    192.168.2.0
add address=172.16.0.2/24 comment="Cloudflare WireGuard" interface=wireguard1 \
    network=172.16.0.0
add address=192.168.68.1/30 comment=debugging interface=ether4 network=\
    192.168.68.0
/ip dhcp-client
add comment=defconf disabled=yes interface=ether1
add comment=defconf disabled=yes interface=ether2
/ip dhcp-server lease
add address=192.168.88.2 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.6 mac-address=# server=defconf
add address=192.168.88.3 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.4 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.5 mac-address=# server=defconf
/ip dhcp-server network
add address=192.168.84.0/28 comment=guestconf dns-server=1.1.1.1,1.0.0.1 \
    gateway=192.168.84.1
add address=192.168.88.0/24 comment=defconf dns-server=1.1.1.1,1.0.0.1 \
    gateway=192.168.88.1
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,1.0.0.1
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
add address=192.168.100.1 name=wan1.logi.lo type=A
add address=192.168.2.1 name=wan2.logi.lo type=A
add address=192.168.88.6 name=stb1.logi.lo type=A
add address=127.0.0.1 name=stb2.logi.lo type=A
add address=192.168.88.4 name=eap1.logi.lo type=A
add address=192.168.100.254 name=cpe1.logi.lo type=A
add address=192.168.88.2 name=switch1.logi.lo type=A
add address=192.168.88.3 name=switch2.logi.lo type=A
add address=192.168.88.5 name=tlmr1.logi.lo type=A
/ip firewall filter
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
    connection-state=new disabled=yes in-interface-list=WAN
add action=accept chain=forward comment="Cloudflare WireGuard" \
    in-interface-list=LAN out-interface=wireguard1
add action=accept chain=forward in-interface=guest-vlan22 out-interface=\
    wireguard1
add action=drop chain=forward comment="drop all else"
/ip firewall mangle
add action=change-mss chain=forward comment="Cloudflare WireGuard" new-mss=\
    1380 out-interface=wireguard1 passthrough=yes protocol=tcp tcp-flags=syn \
    tcp-mss=1381-65535
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat comment="Cloudflare WireGuard" \
    out-interface=wireguard1
add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \
    protocol=tcp to-addresses=172.16.0.1
add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \
    protocol=udp to-addresses=172.16.0.1
add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \
    protocol=tcp to-addresses=172.16.0.1
add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \
    protocol=udp to-addresses=172.16.0.1
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/ip kid-control device
add mac-address=# name="Redmi-10C;2" user=""
add mac-address=# name="ESP-67B077;6" user=""
/ip route
add check-gateway=ping comment=Recursive disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=9.9.9.9 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=12
add check-gateway=ping comment=Main disabled=no distance=1 dst-address=\
    9.9.9.9/32 gateway=192.168.100.1 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=11
add check-gateway=ping comment=Backup disabled=yes distance=2 dst-address=\
    0.0.0.0/0 gateway=192.168.2.1 routing-table=main scope=30 \
    suppress-hw-offload=no target-scope=10
add comment="Cloudflare WireGuard" disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=wireguard1 routing-table=to-Cloudflare scope=30 \
    suppress-hw-offload=no target-scope=10
/routing bfd configuration
add disabled=yes interfaces=all min-rx=200ms min-tx=200ms multiplier=5
/routing rule
add action=lookup-only-in-table comment="maintain local connectivity" \
    disabled=no min-prefix=0 table=main
add action=lookup-only-in-table comment="Cloudflare WireGuard" disabled=no \
    src-address=192.168.88.0/24 table=to-Cloudflare
add action=lookup-only-in-table disabled=no src-address=192.168.84.0/28 \
    table=to-Cloudflare
/system clock
set time-zone-name=Asia/Jakarta
/system note
set show-at-login=no
/system scheduler
add interval=2d name=reboot on-event="/system reboot" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:32:56
add interval=2h name="dns clear" on-event="/ip dns cache flush" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:35:12
add comment="trigger duckdns updater" interval=1m name="duckdns updater" \
    on-event="/system script run duckdns" policy=read,write,policy,test \
    start-time=startup
/system script
add comment="duckdns updater" dont-require-permissions=no name=duckdns owner=\
    admin policy=read,write,policy,test source=":local resolvedIP [:resolve \"\
    #.duckdns.org\"];\
    \n:local currentIP [/ip cloud get public-address];\
    \n:local currentIP [:pick \$currentIP 0 [:find \$currentIP \"/\"]];\
    \n\
    \n:if (\$resolvedIP != \$currentIP) do={\
    \n    :log info (\"Trying to update DuckDNS with actual IP \".\$currentIP.\
    \", resolved IP is \".\$resolvedIP);\
    \n    :local response [/tool fetch url=(\"https://www.duckdns.org/update\?\
    domains=#.duckdns.org&token=\
    \#&ip=\".\$currentIP) check-certificat\
    e=yes as-value output=user];\
    \n    :if (\$response->\"status\" = \"finished\") do={\
    \n        :if (\$response->\"data\" = \"OK\") do={\
    \n            :log info (\"Successfully updated DuckDNS with new IP \".\$c\
    urrentIP);\
    \n        } else={\
    \n            :log error (\"Failed to update DuckDNS with new IP \".\$curr\
    entIP);\
    \n        }\
    \n    }\
    \n}"
/tool mac-server
set allowed-interface-list=none
/tool mac-server mac-winbox
set allowed-interface-list=TRUSTED

---
```

## Response 30
Since ether4 works, suspect the switch may be the culprit.Reviewing the latest config.... ---

## Response 31
Since ether4 works, suspect the switch may be the culprit.Nope, the switch is not a problem. I try directly connect my laptop to the router via ether3, I set ether3 pvid=10 admit=all, still I can't ping / connect my winbox into router via IP address.Reviewing the latest config....Any idea ? ---

## Response 32
The only thing that proves is that you cannot hook up a dumb device (laptop) and get traffic from a trunk port..........Ether3 is going to the switch and thus cannot be terminated on a laptop.Sure you may have changed the /interface bridge port settings, but did you change the /interface bridge vlan setting as well???/interface bridge vlanadd bridge=bridge tagged=bridge untagged=wlan2 vlan-ids=22add bridge=bridge tagged=bridge untagged=ether3, wlan1, pwr-line1 vlan-ids=10However, can you confirm please that you can log into ether4 with the laptop ( gain access to the config) but then try to browse the internet.a. can you reach the internetb. what WANIP do you see ( whats my ip ) on the browser.If you can reach the internet from ether4, then I think the first thing to do is disable all those static DNS entries for he 192.168.88 subnetSome combination of DNS settings will work.So will think about that while you do your ethernet4 internet test ---

## Response 33
The only thing that proves is that you cannot hook up a dumb device (laptop) and get traffic from a trunk port..........Ether3 is going to the switch and thus cannot be terminated on a laptop.Sure you may have changed the /interface bridge port settings, but did you change the /interface bridge vlan setting as well???/interface bridge vlanadd bridge=bridge tagged=bridge untagged=wlan2 vlan-ids=22add bridge=bridge tagged=bridge untagged=ether3, wlan1, pwr-line1 vlan-ids=10Yeah I already set pvid, and bridge vlan to untagged ether3 for vlan10. Still not working, winbox cannot access router via IP address.However, can you confirm please that you can log into ether4 with the laptop ( gain access to the config) but then try to browse the internet.a. can you reach the internetb. what WANIP do you see ( whats my ip ) on the browser.I can get access winbox to router via IP address. buta. cannot connect internetb. no internet connection then I can't access browsermikrotik winbox, winbox can access router via ip address ether4, but no internet connection.PNGIf you can reach the internet from ether4, then I think the first thing to do is disable all those static DNS entries for he 192.168.88 subnetSome combination of DNS settings will work.So will think about that while you do your ethernet4 internet testI already try to disable all static DNS, except for router.lan that into 192.168.88.1, still no internet access.any idea ? ---

## Response 34
Lost as you are............Going back to basics.Have you ever had a WIREGUARD connection ........ ??Not that this will make a difference but modify/ip routeadd check-gateway=ping comment=Recursive disabled=no distance=1 dst-address=\0.0.0.0/0 gateway=9.9.9.9 routing-table=main scope=10 \suppress-hw-offload=no target-scope=12addcheck-gateway=pingcomment=Main disabled=no distance=1 dst-address=\9.9.9.9/32 gateway=192.168.100.1 routing-table=main scope=10 \suppress-hw-offload=no target-scope=11addcheck-gateway=pingcomment=Backup disabled=yes distance=2 dst-address=\0.0.0.0/0 gateway=192.168.2.1 routing-table=main scope=30 \suppress-hw-offload=no target-scope=10TO:/ip routeadd check-gateway=ping comment=Recursive dst-address=0.0.0.0/0 gateway=9.9.9.9 routing-table=main scope=10 target-scope=12add comment=Main dst-address=9.9.9.9/32 gateway=192.168.100.1 routing-table=main scope=10 target-scope=11add comment=Backup disabled=NOdistance=2 dst-address=0.0.0.0/0 gateway=192.168.2.1 routing-table=main ---

## Response 35
Lost as you are............Going back to basics.Where should I start?Have you ever had a WIREGUARD connection ........ ??I never heard wireguard until Mikrotik announced a new feature, so I excited what new, I read I found wireguard connection is a new VPN protocol connection, but for a few years I've been using Cloudflare 1.1.1.1 DNS that provides a warp connection feature I'm trying to play with then I realize this warp connection use wireguard.Not that this will make a difference but modify/ip routeadd check-gateway=ping comment=Recursive disabled=no distance=1 dst-address=\0.0.0.0/0 gateway=9.9.9.9 routing-table=main scope=10 \suppress-hw-offload=no target-scope=12addcheck-gateway=pingcomment=Main disabled=no distance=1 dst-address=\9.9.9.9/32 gateway=192.168.100.1 routing-table=main scope=10 \suppress-hw-offload=no target-scope=11addcheck-gateway=pingcomment=Backup disabled=yes distance=2 dst-address=\0.0.0.0/0 gateway=192.168.2.1 routing-table=main scope=30 \suppress-hw-offload=no target-scope=10TO:/ip routeadd check-gateway=ping comment=Recursive dst-address=0.0.0.0/0 gateway=9.9.9.9 routing-table=main scope=10 target-scope=12add comment=Main dst-address=9.9.9.9/32 gateway=192.168.100.1 routing-table=main scope=10 target-scope=11add comment=Backup disabled=NOdistance=2 dst-address=0.0.0.0/0 gateway=192.168.2.1 routing-table=mainThe only change is I turn on the Backup route right? I already set this, no difference?what should I do? ---

## Response 36
At this point, probably insert a chip into my brain and sever anytime I spend working on configs.........Probably get up on discord and skype and use teamviewer or something to look at config and try things live.What time zone you in?? ---

## Response 37
At this point, probably insert a chip into my brain and sever anytime I spend working on configs.........Probably get up on discord and skype and use teamviewer or something to look at config and try things live.What time zone you in??Hehe I'm sorry for thatMaybe discord i think ?I'm in Indonesia TimeZone Jakarta (GMT+7) ---

## Response 38
Yikes, going to bed soon but will figure out when I am available and then I can give you some contact info........ ---

## Response 39
Just post here when you are around and I will watch out for it and respond if available. ---

## Response 40
Its 9:31pm your time, you there........? ---

## Response 41
Okay another one to try........ Its testing if the min prefix is stopping outgoing wan from router itself traffic,,,,very weird......We think the min=-prefix command, not well understood may be getting in the way.Try this simple fix and see! We are adding another rule, as last rule so no need to frig with rule order./routing ruleadd action=lookup-only-in-table min-prefix=0 table=mainadd action=lookup-only-in-table src-address=192.168.88.0/24 table=to-Cloudflareadd action=lookup-only-in-table src-address=192.168.84.0/28 table=to-Cloudflareadd action=lookup-only-in-table table=main+++++++++++++++++++++++++++++++++++++++IF that doesn work, then will resort to my older method......../routing ruleadd action=lookup-only-in-table dst-address=192.168.88.0/24 table=mainadd action=lookup-only-in-table dst-address=192.168.84.0/24 table=mainadd action=lookup-only-in-table src-address=192.168.88.0/24 table=to-Cloudflareadd action=lookup-only-in-table src-address=192.168.84.0/28 table=to-CloudflareEasy way to do this in winbox is to choose the first rule and modify it so it looks like the first rule here.Then just delete the last rule..... voila done. ---

## Response 42
Just post here when you are around and I will watch out for it and respond if available.Yeah, I'm sorry I'm late, maybe what time will you be around here? I will prepare for that ---

## Response 43
Okay another one to try........ Its testing if the min prefix is stopping outgoing wan from router itself traffic,,,,very weird......We think the min=-prefix command, not well understood may be getting in the way.Try this simple fix and see! We are adding another rule, as last rule so no need to frig with rule order./routing ruleadd action=lookup-only-in-table min-prefix=0 table=mainadd action=lookup-only-in-table src-address=192.168.88.0/24 table=to-Cloudflareadd action=lookup-only-in-table src-address=192.168.84.0/28 table=to-Cloudflareadd action=lookup-only-in-table table=main+++++++++++++++++++++++++++++++++++++++IF that doesn work, then will resort to my older method......../routing ruleadd action=lookup-only-in-table dst-address=192.168.88.0/24 table=mainadd action=lookup-only-in-table dst-address=192.168.84.0/24 table=mainadd action=lookup-only-in-table src-address=192.168.88.0/24 table=to-Cloudflareadd action=lookup-only-in-table src-address=192.168.84.0/28 table=to-CloudflareEasy way to do this in winbox is to choose the first rule and modify it so it looks like the first rule here.Then just delete the last rule..... voila done.I try both configurationon ether3 -> winbox still cannot access router via IP address, no internet connection tooon ether4 -> winbox can connect router via IP address, no internet connection too ---

## Response 44
Thanks for the updates........ still thinking....... ---

## Response 45
The newest export posted here is more than two weeks old. If you still haven't resolved it, please post a current one. ---

## Response 46
The newest export posted here is more than two weeks old. If you still haven't resolved it, please post a current one.Yeah still not working.- I can't ping to default gateway and winbox can't access router via IP address.- Sometimes Website can't be opened- Even my router sometimes after a few days get error I can't connect into wifi, I should reboot the router then work, but it's maybe because I used rosv7 on my low end mikrotik rb9421-2nd.here is the new configuration
```
# 2024-12-01 16:35:32 by RouterOS 7.16.1
# software id = #
#
# model = RB941-2nD
# serial number = #
/interface bridge
add admin-mac=# auto-mac=no comment=defconf \
    ingress-filtering=no name=bridge port-cost-mode=short vlan-filtering=yes
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=20/40mhz-XX \
    country=indonesia disabled=no distance=indoors frequency=auto \
    installation=indoor mode=ap-bridge ssid=Scale wireless-protocol=802.11
/interface ethernet
set [ find default-name=ether4 ] comment=debugging
/interface wireguard
add comment="Cloudflare WireGuard" listen-port=13231 mtu=1420 name=wireguard1
/interface vlan
add comment=guestconf interface=bridge name=guest-vlan22 vlan-id=22
add comment=homeconf interface=bridge name=home-vlan10 vlan-id=10
/interface bonding
add disabled=yes name=bonding1 slaves=ether3,ether4
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
add comment=extraconf name=TRUSTED
/interface wireless security-profiles
set [ find default=yes ] authentication-types=wpa-psk,wpa2-psk eap-methods="" \
    mode=dynamic-keys supplicant-identity=MikroTik
add eap-methods="" name=guest supplicant-identity=""
/interface wireless
add keepalive-frames=disabled mac-address=# master-interface=\
    wlan1 multicast-buffering=disabled name=wlan2 security-profile=guest \
    ssid="Scale Guest" wds-cost-range=0 wds-default-cost=0 wps-mode=disabled
/ip kid-control
add fri=0s-1d mon=0s-1d name=system-dummy sat=0s-1d sun=0s-1d thu=0s-1d tue=\
    0s-1d tur-fri=0s-1d tur-mon=0s-1d tur-sat=0s-1d tur-sun=0s-1d tur-thu=\
    0s-1d tur-tue=0s-1d tur-wed=0s-1d wed=0s-1d
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
add name=guest-dhcp ranges=192.168.84.2-192.168.84.8
add name=dhcp_pool3 ranges=192.168.68.2
/ip dhcp-server
add address-pool=default-dhcp interface=home-vlan10 lease-time=10m name=\
    defconf
add address-pool=guest-dhcp disabled=yes interface=guest-vlan22 lease-time=\
    10m name=guestconf
add address-pool=dhcp_pool3 comment=debugging interface=ether4 name=dhcp1
/queue simple
add disabled=yes max-limit=1M/1M name=queue-guest target=guest-vlan22
/routing ospf instance
add disabled=no name=default-v2
/routing ospf area
add disabled=yes instance=default-v2 name=backbone-v2
/routing table
add comment="Cloudflare WireGuard" disabled=no fib name=to-Cloudflare
/interface bridge port
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether2 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf interface=ether3 internal-path-cost=10 \
    path-cost=10 pvid=10
add bridge=bridge comment=defconf disabled=yes ingress-filtering=no \
    interface=ether4 internal-path-cost=10 path-cost=10
add bridge=bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-tagged interface=pwr-line1 \
    internal-path-cost=10 path-cost=10 pvid=10
add bridge=bridge comment=defconf frame-types=\
    admit-only-untagged-and-priority-tagged interface=wlan1 \
    internal-path-cost=10 path-cost=10 pvid=10
add bridge=bridge disabled=yes ingress-filtering=no interface=bonding1 \
    internal-path-cost=10 path-cost=10
add bridge=bridge frame-types=admit-only-untagged-and-priority-tagged \
    interface=wlan2 internal-path-cost=10 path-cost=10 pvid=22
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=TRUSTED
/ip settings
set max-neighbor-entries=8192
/ipv6 settings
set disable-ipv6=yes max-neighbor-entries=8192
/interface bridge vlan
add bridge=bridge tagged=bridge,ether3 untagged=wlan2 vlan-ids=22
add bridge=bridge tagged=bridge,ether3 untagged=wlan1,pwr-line1 vlan-ids=10
/interface list member
add comment=defconf interface=home-vlan10 list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=ether2 list=WAN
add comment=debugging interface=ether4 list=LAN
add comment=extraconf interface=home-vlan10 list=TRUSTED
add interface=ether4 list=TRUSTED
/interface ovpn-server server
set auth=sha1,md5
/interface wireguard peers
add allowed-address=0.0.0.0/0 comment="Cloudflare WireGuard" \
    endpoint-address=engage.cloudflareclient.com endpoint-port=2408 \
    interface=wireguard1 name="cloudflare wireguard" persistent-keepalive=35s \
    public-key="#"
/ip address
add address=192.168.88.1/24 comment=defconf interface=home-vlan10 network=\
    192.168.88.0
add address=192.168.84.1/28 comment=guestconf interface=guest-vlan22 network=\
    192.168.84.0
add address=192.168.100.100/24 comment=wan1 interface=ether1 network=\
    192.168.100.0
add address=192.168.2.100/24 comment=wan2 interface=ether2 network=\
    192.168.2.0
add address=172.16.0.1/24 comment="Cloudflare WireGuard" interface=wireguard1 \
    network=172.16.0.0
add address=192.168.68.1/30 comment=debugging interface=ether4 network=\
    192.168.68.0
/ip dhcp-client
add comment=defconf disabled=yes interface=ether1
add comment=defconf disabled=yes interface=ether2
/ip dhcp-server lease
add address=192.168.88.2 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.6 mac-address=# server=defconf
add address=192.168.88.3 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.4 client-id=# mac-address=\
    # server=defconf
add address=192.168.88.5 mac-address=# server=defconf
/ip dhcp-server network
add address=192.168.68.0/30 comment=debugging gateway=192.168.68.1
add address=192.168.84.0/28 comment=guestconf dns-server=1.1.1.1,1.0.0.1 \
    gateway=192.168.84.1
add address=192.168.88.0/24 comment=defconf dns-server=1.1.1.1,1.0.0.1 \
    gateway=192.168.88.1
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,1.0.0.1
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
add address=192.168.100.1 disabled=yes name=wan1.logi.lo type=A
add address=192.168.2.1 disabled=yes name=wan2.logi.lo type=A
add address=192.168.88.6 disabled=yes name=stb1.logi.lo type=A
add address=127.0.0.1 disabled=yes name=stb2.logi.lo type=A
add address=192.168.88.4 disabled=yes name=eap1.logi.lo type=A
add address=192.168.100.254 disabled=yes name=cpe1.logi.lo type=A
add address=192.168.88.2 disabled=yes name=switch1.logi.lo type=A
add address=192.168.88.3 disabled=yes name=switch2.logi.lo type=A
add address=192.168.88.5 disabled=yes name=tlmr1.logi.lo type=A
/ip firewall filter
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
    connection-state=new disabled=yes in-interface-list=WAN
add action=accept chain=forward comment="Cloudflare WireGuard" \
    in-interface-list=LAN out-interface=wireguard1
add action=accept chain=forward in-interface=guest-vlan22 out-interface=\
    wireguard1
add action=drop chain=forward comment="drop all else"
/ip firewall mangle
add action=change-mss chain=forward comment="Cloudflare WireGuard" new-mss=\
    1380 out-interface=wireguard1 passthrough=yes protocol=tcp tcp-flags=syn \
    tcp-mss=1381-65535
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat comment="Cloudflare WireGuard" \
    out-interface=wireguard1
add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \
    protocol=tcp to-addresses=172.16.0.1
add action=dst-nat chain=dstnat dst-port=53 in-interface=home-vlan10 \
    protocol=udp to-addresses=172.16.0.1
add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \
    protocol=tcp to-addresses=172.16.0.1
add action=dst-nat chain=dstnat dst-port=53 in-interface=guest-vlan22 \
    protocol=udp to-addresses=172.16.0.1
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/ip kid-control device
add mac-address=# name="Redmi-10C;2" user=""
add mac-address=# name="ESP-67B077;6" user=""
/ip route
add check-gateway=ping comment=Recursive disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=9.9.9.9 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=12
add check-gateway=ping comment=Main disabled=no distance=1 dst-address=\
    9.9.9.9/32 gateway=192.168.100.1 routing-table=main scope=10 \
    suppress-hw-offload=no target-scope=11
add check-gateway=ping comment=Backup disabled=no distance=2 dst-address=\
    0.0.0.0/0 gateway=192.168.2.1 routing-table=main scope=30 \
    suppress-hw-offload=no target-scope=10
add comment="Cloudflare WireGuard" disabled=no distance=1 dst-address=\
    0.0.0.0/0 gateway=wireguard1 routing-table=to-Cloudflare scope=30 \
    suppress-hw-offload=no target-scope=10
/routing bfd configuration
add disabled=yes interfaces=all min-rx=200ms min-tx=200ms multiplier=5
/routing rule
add action=lookup comment="Cloudflare WireGuard" disabled=no routing-mark=\
    main src-address=192.168.88.0/24 table=to-Cloudflare
add action=lookup disabled=no routing-mark=main src-address=192.168.84.0/28 \
    table=to-Cloudflare
add action=lookup-only-in-table comment="maintain local connectivity" \
    disabled=no dst-address=192.168.88.1/24 min-prefix=0 src-address=\
    192.168.88.0/24 table=main
add action=lookup-only-in-table disabled=no dst-address=192.168.84.1/28 \
    src-address=192.168.84.0/28 table=main
/system clock
set time-zone-name=Asia/Jakarta
/system note
set show-at-login=no
/system scheduler
add interval=2d name=reboot on-event="/system reboot" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:32:56
add interval=2h name="dns clear" on-event="/ip dns cache flush" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=2021-02-28 start-time=16:35:12
add comment="trigger duckdns updater" interval=1m name="duckdns updater" \
    on-event="/system script run duckdns" policy=read,write,policy,test \
    start-time=startup
/system script
add comment="duckdns updater" dont-require-permissions=no name=duckdns owner=\
    admin policy=read,write,policy,test source=":local resolvedIP [:resolve \"\
    #.duckdns.org\"];\
    \n:local currentIP [/ip cloud get public-address];\
    \n:local currentIP [:pick \$currentIP 0 [:find \$currentIP \"/\"]];\
    \n\
    \n:if (\$resolvedIP != \$currentIP) do={\
    \n    :log info (\"Trying to update DuckDNS with actual IP \".\$currentIP.\
    \", resolved IP is \".\$resolvedIP);\
    \n    :local response [/tool fetch url=(\"https://www.duckdns.org/update\?\
    domains=#.duckdns.org&token=\
    \#&ip=\".\$currentIP) check-certificat\
    e=yes as-value output=user];\
    \n    :if (\$response->\"status\" = \"finished\") do={\
    \n        :if (\$response->\"data\" = \"OK\") do={\
    \n            :log info (\"Successfully updated DuckDNS with new IP \".\$c\
    urrentIP);\
    \n        } else={\
    \n            :log error (\"Failed to update DuckDNS with new IP \".\$curr\
    entIP);\
    \n        }\
    \n    }\
    \n}"
/tool mac-server
set allowed-interface-list=TRUSTED
/tool mac-server mac-winbox
set allowed-interface-list=TRUSTED

---
```

## Response 47
- I can't ping to default gateway and winbox can't access router via IP address.Here, by "default gateway" you mean the one from the point of view of the PC (or phone), i.e. the own address of the Mikrotik in the subnet from which the client has got its address via DHCP?- Sometimes Website can't be openedfrom the same PC or phone as above, they can be open most of the time but occasionally not?- Even my router sometimes after a few days get error I can't connect into wifi, I should reboot the router then work, but it's maybe because I used rosv7 on my low end mikrotik rb9421-2nd.hAP lite is indeed not powerful enough to run ROS 7 without trouble, but that does not explain the other issues.Looking at the configuration, you should be able to connect to the router using its IP address if you are connected via ether4, is that the case? You cannot connect to the IP of the router if connected via wlan1 (VLAN 10) due to wrong order of the routing rules, the one withmin-prefix=0must be the first (topmost) one in the list in order to act before the one which is the first one at the moment.It seems it would be worth an online session as multiple iterations are likely to be required, but it might be complicated to find a time when we are both awake. ---

## Response 48
- I can't ping to default gateway and winbox can't access router via IP address.Here, by "default gateway" you mean the one from the point of view of the PC (or phone), i.e. the own address of the Mikrotik in the subnet from which the client has got its address via DHCP?Yeah, if example my client device connect into vlan10, it's get network on subnet 192.168.88.0/254, and default gateway of the mikrotik is 192.168.88.1, my client can't ping / connect winbox to the ip 192.168.88.1- Sometimes Website can't be openedfrom the same PC or phone as above, they can be open most of the time but occasionally not?As far as i remember, example this website, I can open in my phone but not on my laptop. but if connect to another network, bot devices work properly.- Even my router sometimes after a few days get error I can't connect into wifi, I should reboot the router then work, but it's maybe because I used rosv7 on my low end mikrotik rb9421-2nd.hAP lite is indeed not powerful enough to run ROS 7 without trouble, but that does not explain the other issues.Yeah i read a thread discuss about that, but i think for my case this router i think still can handle, i just only have 14 client connected, most of them is iot devices, like smart plug or smart bulb.Looking at the configuration, you should be able to connect to the router using its IP address if you are connected via ether4, is that the case? You cannot connect to the IP of the router if connected via wlan1 (VLAN 10) due to wrong order of the routing rules, the one withmin-prefix=0must be the first (topmost) one in the list in order to act before the one which is the first one at the moment.ether4 can connect winbox through ip address.but vlan10 or vlan22 guest, can't. even ping.It seems it would be worth an online session as multiple iterations are likely to be required, but it might be complicated to find a time when we are both awake.That's it, My habbit not good, so sometimes i sleep on morning, sometimes i sleep on night. but mostly i online on 10pm on my gmt+7 ---

## Response 49
So time zones play little role and it is basically a random process, OK.If you want to give it a try, follow the instructions inthis post. ---