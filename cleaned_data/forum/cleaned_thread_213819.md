# Thread Information
Title: Thread-213819
Section: RouterOS
Thread ID: 213819

# Discussion

## Initial Question
With ROS 7.17rc6 i can't connect L2TP with PSK to MikroTik router CCR2116-12G-4S+.I can connect to other MT routers with that verion, but NOT to CCR2116 with VLAN interfaces(see attached screenschot).VLAN1- is WAN, VLAN3- LAN. CCR2116 is connected to CRS305 with SFF interfaces.LOG from CCR2116:respond new phase 1 (Identity Protection): 83.xxx.xxx.xxx[500]<=>37.47.xxx.xxx[8730]ISAKMP-SA established 83.xxx.xxx.xxx[4500]-37.xxx.xxx.xxx[16146] spi:cc6366dae0274db6:4ef419c203705487first L2TP UDP packet received from 37.xxx.xxx.xxxfirst L2TP UDP packet received from 37.xxx.xxx.xxx<37.xxx.xxx.xxx>: authentication failed: peer didn't respond to CHAP challengepurging ISAKMP-SA 83.xxx.xxx.xxx[4500]<=>37.xxx.xxx.xxx[16146] spi=cc6366dae0274db6:4ef419c203705487.ISAKMP-SA deleted 83.xxx.xxx.xxx[4500]-37.xxx.xxx.xxx[16146] spi:cc6366dae0274db6:4ef419c203705487 rekey:1Please help. L2TP VPN is very important for me. ---

## Response 1
Something is wrong with IPSEC at ROS 7.17rc6...At another machine (x86) with ROS 7.17rc6 - there is non-stop 100% CPU (see screenschot) - when there is no VPN or any other IPSEC connetion to that router!!!Does anyone has problem with VPN's on taht ROS version? ---

## Response 2
MikroTik team repaired that problem, and now at ROS ver 7.17rc8 it works (L2TP with IPSEC on CCR2116). Thank You MikroTik! ---

## Response 3
Good dayI am having problems when I try to use IPsec with a L2TP connection, I have ports 4500, 500, 1701, protocol 50 (ipsec-esp) and 51 (ipsec-ah), phase 1 never passes. If I disable IPsec, the VPN works.I'm not sure what's going on with this new version of RouterOS.I really appreciate your help. ---