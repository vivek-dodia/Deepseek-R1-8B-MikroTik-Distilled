# Repository Information
Name: Mikrotik_conf

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/adm-dv/Mikrotik_conf.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: ADM-DV_main_router
================================================
# aug/04/2018 13:47:25 by RouterOS 6.42.1
# software id = ULJ5-UBPS
#
# model = RouterBOARD 952Ui-5ac2nD
# serial number = 7C3008AD1E1F
/interface bridge
add admin-mac=CC:2D:E0:2D:6A:27 auto-mac=no comment=defconf name=bridge
add name=bridge_WiFi
/interface ethernet
set [ find default-name=ether1 ] comment=WAN
set [ find default-name=ether2 ] comment=PC_PSM name=ether2-master
set [ find default-name=ether3 ] comment=TV_PSM
set [ find default-name=ether5 ] comment=VmWare_srv
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n bridge-mode=disabled channel-width=20/40mhz-Ce country=russia disabled=no distance=indoors frequency=auto frequency-mode=regulatory-domain mode=ap-bridge ssid=\
    MikroTik-2D6A2C wireless-protocol=802.11 wps-mode=disabled
set [ find default-name=wlan2 ] band=5ghz-a/n/ac channel-width=20/40/80mhz-Ceee country=russia disabled=no distance=indoors frequency=auto frequency-mode=regulatory-domain mode=ap-bridge ssid=MikroTik-2D6A2B \
    wireless-protocol=802.11 wps-mode=disabled
/interface vlan
add comment=SRV interface=ether5 name=VLAN_56 vlan-id=56
add comment=EVE_NG interface=ether5 name=VLAN_200 vlan-id=200
add comment=TESTs_VALN interface=ether5 name=VLAN_220 vlan-id=220
/interface list
add exclude=dynamic name=discover
add name=mactel
add name=mac-winbox
/interface wireless security-profiles
set [ find default=yes ] authentication-types=wpa2-psk mode=dynamic-keys supplicant-identity=MikroTik wpa-pre-shared-key=cmux4RByLbA wpa2-pre-shared-key=cmux4RByLbA
/ip hotspot profile
set [ find default=yes ] html-directory=flash/hotspot
/ip pool
add name=dhcp ranges=192.168.0.1-192.168.0.29
add name=srv_pool ranges=192.168.56.1-192.168.56.200
add name=wifi_pool ranges=192.168.20.1-192.168.20.200
add name=EVE_NG ranges=192.168.200.1-192.168.200.25
add name=TESTs_VLAN ranges=192.168.220.100-192.168.220.200
/ip dhcp-server
add address-pool=dhcp disabled=no interface=bridge name=defconf
add address-pool=srv_pool disabled=no interface=VLAN_56 name=srv_dhcp
add address-pool=wifi_pool disabled=no interface=bridge_WiFi name=wifi_dhcp
add address-pool=EVE_NG disabled=no interface=VLAN_200 name=EVE_NG_dhcp
add address-pool=TESTs_VLAN disabled=no interface=VLAN_220 name=TESTs_VALN
/queue tree
add limit-at=50M max-limit=50M name=PROD_IN parent=global
add limit-at=50M max-limit=50M name=PROD_OUT parent=global
add limit-at=10M max-limit=50M name=queue_V_56_IN packet-mark=56_IN parent=PROD_IN queue=hotspot-default
add limit-at=10M max-limit=50M name=queue_V_56_OUT packet-mark=56_OUT parent=PROD_OUT queue=hotspot-default
add limit-at=10M max-limit=50M name=queue_V_200_IN packet-mark=200_IN parent=PROD_IN queue=hotspot-default
add limit-at=10M max-limit=50M name=queue_V_200_OUT packet-mark=200_OUT parent=PROD_OUT queue=hotspot-default
add max-limit=10M name=queue_V_220_IN packet-mark=220_OUT parent=PROD_IN queue=default
add max-limit=10M name=queue_V_220_OUT packet-mark=220_OUT parent=PROD_OUT queue=default
add name=queue_V_20_IN packet-mark=20_IN parent=PROD_IN queue=hotspot-default
add name=queue_V_20_OUT packet-mark=20_OUT parent=PROD_OUT queue=hotspot-default
/snmp community
set [ find default=yes ] addresses=192.168.56.50/32
/interface bridge port
add bridge=bridge comment=defconf interface=ether2-master
add bridge=bridge_WiFi comment=WiFi_2.4G interface=wlan1
add bridge=bridge_WiFi comment=WiFi_5G interface=wlan2
add bridge=bridge interface=ether3
add bridge=bridge interface=ether4
add bridge=bridge interface=ether5
/ip neighbor discovery-settings
set discover-interface-list=discover
/interface list member
add interface=ether2-master list=discover
add interface=ether3 list=discover
add interface=ether4 list=discover
add interface=ether5 list=discover
add interface=wlan1 list=discover
add interface=wlan2 list=discover
add interface=bridge list=discover
add interface=bridge list=mactel
add interface=bridge list=mac-winbox
/ip address
add address=192.168.0.30/27 comment=defconf interface=ether2-master network=192.168.0.0
add address=192.168.56.254/24 comment=SRV_VLAN interface=VLAN_56 network=192.168.56.0
add address=192.168.20.254/24 comment=WiFi_VLAN interface=bridge_WiFi network=192.168.20.0
add address=192.168.200.30/27 comment=EVE_NG interface=VLAN_200 network=192.168.200.0
add address=192.168.220.254/24 comment=TESTs_VLAN interface=VLAN_220 network=192.168.220.0
/ip cloud
set ddns-enabled=yes
/ip dhcp-client
add comment=defconf dhcp-options=hostname,clientid disabled=no interface=ether1
/ip dhcp-server lease
add address=192.168.0.5 always-broadcast=yes client-id=1:bc:ae:c5:1b:b7:d0 mac-address=BC:AE:C5:1B:B7:D0 server=defconf
add address=192.168.56.10 client-id=1:0:c:29:8c:ad:e5 mac-address=00:0C:29:8C:AD:E5 server=srv_dhcp
add address=192.168.56.70 client-id=1:0:c:29:9b:b9:7c comment=Win_KMS mac-address=00:0C:29:9B:B9:7C server=srv_dhcp
add address=192.168.56.40 mac-address=00:0C:29:FB:F7:8A server=srv_dhcp
add address=192.168.56.50 mac-address=00:0C:29:72:A5:32 server=srv_dhcp
add address=192.168.56.100 mac-address=00:0C:29:DF:5A:FD server=srv_dhcp
add address=192.168.56.30 mac-address=00:0C:29:F8:74:00 server=srv_dhcp
add address=192.168.200.20 always-broadcast=yes client-id=1:0:c:29:be:c2:8c mac-address=00:0C:29:BE:C2:8C server=EVE_NG_dhcp
add address=192.168.56.80 client-id=1:0:c:29:8d:bb:c comment=Veeam_SRV mac-address=00:0C:29:8D:BB:0C server=srv_dhcp
add address=192.168.56.90 client-id=1:0:c:29:16:34:a1 mac-address=00:0C:29:16:34:A1 server=srv_dhcp
add address=192.168.56.110 mac-address=00:0C:29:C6:18:EA server=srv_dhcp
add address=192.168.56.60 client-id=1:0:c:29:65:96:e7 mac-address=00:0C:29:65:96:E7 server=srv_dhcp
add address=192.168.56.65 mac-address=00:0C:29:7D:4F:0D server=srv_dhcp
add address=192.168.200.25 mac-address=00:0C:29:F4:72:83 server=EVE_NG_dhcp
add address=192.168.56.75 comment=OTRS_srv mac-address=00:0C:29:4A:98:DF server=srv_dhcp
add address=192.168.200.15 client-id=1:0:c:29:2:3f:c mac-address=00:0C:29:02:3F:0C server=EVE_NG_dhcp
add address=192.168.220.190 mac-address=00:0C:29:61:10:34 server=TESTs_VALN
/ip dhcp-server network
add address=192.168.0.0/27 comment=defconf gateway=192.168.0.30 netmask=27
add address=192.168.20.0/24 comment=WiFi gateway=192.168.20.254 netmask=24
add address=192.168.56.0/24 comment=SRV gateway=192.168.56.254 netmask=24
add address=192.168.200.0/24 comment=EVE_NG gateway=192.168.200.30 netmask=27
add address=192.168.220.0/24 comment=SRV gateway=192.168.220.254 netmask=24
/ip dns
set allow-remote-requests=yes
/ip dns static
add address=192.168.0.30 name=router.adm-dv.local
add address=192.168.56.40 name=adm-dv.local
add address=192.168.56.30 name=torii.local
add address=192.168.56.10 name=adm-srv-01.adm-dv.local
add address=192.168.56.60 name=freenas.adm-dv.local
add address=192.168.56.65 name=graylog.adm-dv.local
add address=192.168.200.25 name=eve-ng.adm-dv.local
add address=192.168.0.20 name=vm-node-01.adm-dv.local
add address=192.168.56.70 name=kms.adm-dv.local
add address=192.168.220.190 name=www.car-id.adm-dv.ru
/ip firewall address-list
add address=103.21.244.0/22 list=CloudFlare
add address=103.22.200.0/22 list=CloudFlare
add address=103.31.4.0/22 list=CloudFlare
add address=104.16.0.0/22 list=CloudFlare
add address=108.162.192.0/18 list=CloudFlare
add address=131.0.72.0/22 list=CloudFlare
add address=141.101.64.0/18 list=CloudFlare
add address=162.158.0.0/15 list=CloudFlare
add address=172.64.0.0/13 list=CloudFlare
add address=173.245.48.0/20 list=CloudFlare
add address=188.114.96.0/20 list=CloudFlare
add address=190.93.240.0/20 list=CloudFlare
add address=197.234.240.0/22 list=CloudFlare
add address=198.41.128.0/17 list=CloudFlare
add address=78.140.128.228 list=Adm_L3
/ip firewall filter
add action=drop chain=input comment="dropping port scanners" log=yes log-prefix=Scan_Drop src-address-list="port scanners"
add action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w chain=input comment="Port scanners to list " protocol=tcp psd=21,3s,3,1
add action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w chain=input comment="SYN/FIN scan" protocol=tcp tcp-flags=fin,syn
add action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w chain=input comment="SYN/RST scan" protocol=tcp tcp-flags=syn,rst
add action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w chain=input comment="FIN/PSH/URG scan" protocol=tcp tcp-flags=fin,psh,urg,!syn,!rst,!ack
add action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w chain=input comment="NMAP NULL scan" protocol=tcp tcp-flags=!fin,!syn,!rst,!psh,!ack,!urg
add action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w chain=input comment="ALL/ALL scan" protocol=tcp tcp-flags=fin,syn,rst,psh,ack,urg
add action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w chain=input comment="NMAP FIN Stealth scan" protocol=tcp tcp-flags=fin,!syn,!rst,!psh,!ack,!urg
add action=drop chain=input comment="drop ssh brute forcers" dst-port=222 in-interface=ether1 protocol=tcp src-address-list=ssh_blacklist
add action=add-src-to-address-list address-list=ssh_blacklist address-list-timeout=1w3d chain=input connection-state=new dst-port=222 in-interface=ether1 protocol=tcp src-address-list=ssh_stage3
add action=add-src-to-address-list address-list=ssh_stage3 address-list-timeout=1m chain=input connection-state=new dst-port=222 in-interface=ether1 protocol=tcp src-address-list=ssh_stage2
add action=add-src-to-address-list address-list=ssh_stage2 address-list-timeout=1m chain=input connection-state=new dst-port=222 in-interface=ether1 protocol=tcp src-address-list=ssh_stage1
add action=add-src-to-address-list address-list=ssh_stage1 address-list-timeout=1m chain=input connection-state=new dst-port=222 in-interface=ether1 protocol=tcp
add action=accept chain=input comment="defconf: accept established,related" connection-state=established,related
add action=accept chain=input comment=Allow_VLAN56 connection-state=new in-interface=VLAN_56
add action=accept chain=input comment=Mikrotik_SSH connection-nat-state="" connection-state=new dst-port=222 in-interface=ether1 protocol=tcp
add action=accept chain=input comment=TMP_Proxy connection-state=new disabled=yes dst-port=8081 in-interface=ether1 protocol=tcp src-address=5.100.104.9
add action=accept chain=input comment=IPTV connection-state=new protocol=igmp
add action=accept chain=input comment="defconf: accept ICMP" in-interface=ether1 protocol=icmp src-address-list=Adm_L3
add action=drop chain=input comment=Drop_All
add action=accept chain=forward comment="defconf: accept established,related" connection-state=established,related
add action=accept chain=forward connection-state=new in-interface=VLAN_220 out-interface=ether1 src-address=192.168.220.0/24
add action=accept chain=forward connection-state=new dst-address=192.168.220.0/24 in-interface=ether1 out-interface=VLAN_220
add action=accept chain=forward connection-state=new in-interface=VLAN_200 src-address=192.168.200.0/24
add action=accept chain=forward connection-state=new dst-address=192.168.200.0/24 out-interface=VLAN_200 src-address=!192.168.220.0/24
add action=accept chain=forward connection-state=new in-interface=VLAN_56 src-address=192.168.56.0/24
add action=accept chain=forward connection-state=new dst-address=192.168.56.0/24 out-interface=VLAN_56 src-address=!192.168.220.0/24
add action=accept chain=forward connection-state=new src-address=192.168.20.0/24
add action=accept chain=forward connection-state=new dst-address=192.168.20.0/24 src-address=!192.168.220.0/24
add action=accept chain=forward connection-state=new src-address=192.168.0.0/27
add action=accept chain=forward connection-state=new dst-address=192.168.0.0/27 src-address=!192.168.220.0/24
add action=accept chain=forward comment=IPTV connection-state=new protocol=udp src-port=1234
add action=accept chain=forward comment=IPTV connection-state=new dst-port=1234 protocol=udp
add action=drop chain=forward comment="defconf: drop invalid" connection-state=invalid disabled=yes log=yes log-prefix=drop_forward
add action=drop chain=forward comment="defconf:  drop all from WAN not DSTNATed" connection-nat-state=!dstnat connection-state=new disabled=yes in-interface=ether1 log=yes log-prefix=drop_DSTNATed
add action=drop chain=forward comment=DROP_ALL
/ip firewall mangle
add action=mark-packet chain=forward in-interface=VLAN_220 new-packet-mark=220_OUT out-interface=ether1 passthrough=yes src-address=192.168.220.0/24
add action=mark-packet chain=forward dst-address=192.168.220.0/24 in-interface=ether1 new-packet-mark=220_IN out-interface=VLAN_220 passthrough=yes
add action=mark-packet chain=forward in-interface=VLAN_56 new-packet-mark=56_OUT out-interface=ether1 passthrough=yes src-address=192.168.56.0/24
add action=mark-packet chain=forward dst-address=192.168.56.0/24 in-interface=ether1 new-packet-mark=56_IN out-interface=VLAN_56 passthrough=yes
add action=mark-packet chain=forward in-interface=VLAN_200 new-packet-mark=200_OUT out-interface=ether1 passthrough=yes src-address=192.168.200.0/24
add action=mark-packet chain=forward dst-address=192.168.20.0/24 in-interface=ether1 new-packet-mark=20_IN out-interface=bridge_WiFi passthrough=yes
add action=mark-packet chain=forward in-interface=bridge_WiFi new-packet-mark=20_OUT out-interface=ether1 passthrough=yes src-address=192.168.20.0/24
add action=mark-packet chain=forward dst-address=192.168.200.0/24 in-interface=ether1 new-packet-mark=200_IN out-interface=VLAN_200 passthrough=yes
/ip firewall nat
add action=dst-nat chain=dstnat comment=RDP_adm_srv dst-address=109.110.63.198 dst-port=45800 in-interface=ether1 log=yes log-prefix=RDP_svr_con protocol=tcp to-addresses=192.168.56.10 to-ports=3389
add action=dst-nat chain=dstnat comment=FTP_srv disabled=yes dst-address=109.110.63.198 dst-port=20-21 in-interface=ether1 log=yes log-prefix=RDP_pc_PSM protocol=tcp src-address=78.140.128.228 to-addresses=\
    192.168.56.60
add action=dst-nat chain=dstnat comment=FTP_srv_TMP disabled=yes dst-address=109.110.63.198 dst-port=20-21 in-interface=ether1 log=yes log-prefix=RDP_pc_PSM protocol=tcp src-address=85.95.146.45 to-addresses=\
    192.168.56.60
add action=dst-nat chain=dstnat comment=RDP_ASUS_booker_srv dst-address=109.110.63.198 dst-port=45600 in-interface=ether1 log-prefix=RDP_svr_con protocol=tcp src-address=!85.95.146.45 to-addresses=\
    192.168.200.20 to-ports=3389
add action=dst-nat chain=dstnat comment=RDP_pc_PSM dst-address=109.110.63.198 dst-port=45816 in-interface=ether1 log=yes log-prefix=RDP_pc_PSM protocol=tcp to-addresses=192.168.0.5 to-ports=3389
add action=dst-nat chain=dstnat comment=RDP_v_smolin dst-address=109.110.63.198 dst-port=45000 in-interface=ether1 log=yes log-prefix=RDP_v_smolin protocol=tcp to-addresses=192.168.56.90 to-ports=3389
add action=dst-nat chain=dstnat comment=RDP_v.voroshilov dst-address=109.110.63.198 dst-port=45820 in-interface=ether1 log=yes log-prefix=RDP_v.voroshilov protocol=tcp to-addresses=192.168.200.15 to-ports=\
    3389
add action=dst-nat chain=dstnat comment=Proxy_Zabbix dst-port=10051 in-interface=ether1 protocol=tcp to-addresses=192.168.56.50 to-ports=10051
add action=dst-nat chain=dstnat comment=HTTPS_Proxy dst-address=109.110.63.198 dst-port=443 in-interface=ether1 protocol=tcp src-address-list=CloudFlare to-addresses=192.168.56.100 to-ports=443
add action=dst-nat chain=dstnat comment=HTTP_Proxy dst-address=109.110.63.198 dst-port=80 in-interface=ether1 protocol=tcp src-address-list=CloudFlare to-addresses=192.168.56.100 to-ports=80
add action=dst-nat chain=dstnat comment=HTTPs_EVE dst-address=109.110.63.198 dst-port=8086 in-interface=ether1 protocol=tcp to-addresses=192.168.200.25 to-ports=443
add action=dst-nat chain=dstnat comment=HTTP_EVE_SSH dst-address=109.110.63.198 dst-port=8087 in-interface=ether1 protocol=tcp to-addresses=192.168.200.25 to-ports=22
add action=dst-nat chain=dstnat comment="HTTP_EVE_Telnet POD0" dst-address=109.110.63.198 dst-port=32769-32896 in-interface=ether1 protocol=tcp to-addresses=192.168.200.25
add action=dst-nat chain=dstnat comment="HTTP_EVE_Telnet POD1" dst-address=109.110.63.198 dst-port=32897-33024 in-interface=ether1 protocol=tcp to-addresses=192.168.200.25
add action=dst-nat chain=dstnat comment="HTTP_EVE_Telnet POD2" dst-address=109.110.63.198 dst-port=33025-33152 in-interface=ether1 protocol=tcp to-addresses=192.168.200.25
add action=dst-nat chain=dstnat comment="HTTP_EVE_Telnet POD3" dst-address=109.110.63.198 dst-port=33153-33280 in-interface=ether1 protocol=tcp to-addresses=192.168.200.25
add action=dst-nat chain=dstnat comment="HTTP_EVE_Telnet POD4" disabled=yes dst-address=109.110.63.198 dst-port=33281-33408 in-interface=ether1 protocol=tcp to-addresses=192.168.200.25
add action=dst-nat chain=dstnat comment=HTTP_Proxy dst-address=109.110.63.198 dst-port=8080 in-interface=ether1 protocol=tcp src-address-list=CloudFlare to-addresses=192.168.56.100 to-ports=80
add action=dst-nat chain=dstnat comment=SSH_Torii dst-address=109.110.63.198 dst-port=22 in-interface=ether1 log=yes log-prefix=Torii_con protocol=tcp to-addresses=192.168.56.30 to-ports=22
add action=dst-nat chain=dstnat comment=SSH_NPA_temp disabled=yes dst-address=109.110.63.198 dst-port=22221 in-interface=ether1 log=yes protocol=tcp to-addresses=192.168.220.199 to-ports=22
add action=dst-nat chain=dstnat comment=SSH_SAD_temp dst-address=109.110.63.198 dst-port=22225 in-interface=ether1 log=yes protocol=tcp to-addresses=192.168.220.198 to-ports=22
add action=masquerade chain=srcnat comment="defconf: masquerade" out-interface=ether1
/ip proxy
set anonymous=yes port=8081 src-address=109.110.63.198
/ip service
set ssh port=222
/ip traffic-flow
set interfaces=VLAN_56
/ip traffic-flow target
add dst-address=192.168.56.110 version=5
/ip upnp
set enabled=yes
/ip upnp interfaces
add interface=bridge type=internal
add interface=ether1 type=external
add interface=VLAN_200 type=internal
/routing igmp-proxy
set quick-leave=yes
/routing igmp-proxy interface
add alternative-subnets=192.168.0.0/16 interface=ether1 upstream=yes
add interface=bridge
/snmp
set contact=it@adm-srv.ru enabled=yes location=Vladivostok trap-version=2
/system clock
set time-zone-name=Asia/Vladivostok
/system logging
set 0 action=echo
set 1 action=disk
set 3 action=disk
/system ntp server
set enabled=yes
/system routerboard settings
set silent-boot=no
/tool mac-server
set allowed-interface-list=mactel
/tool mac-server mac-winbox
set allowed-interface-list=mac-winbox
================================================

File: README.md
================================================
# Mikrotik_conf
Configuration files
================================================