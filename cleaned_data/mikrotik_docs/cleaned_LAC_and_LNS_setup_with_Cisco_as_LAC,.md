# Document Information
Title: LAC and LNS setup with Cisco as LAC
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/9863181/LAC+and+LNS+setup+with+Cisco+as+LAC,

# Content
# Overview
LAC/LNS setup or otherwise known as Virtual Private DialUp Network (VPDN) allows long-distance point-to-point connection between remote dial-up users and private networks.
Dial-up client uses PPPOE to connect to a L2TP access concentrator (LAC), LAC determines that session should be forwarded through a IP network to the L2TP Network Server (LNS), creates L2TP tunnel and forwards PPP frames to the server where client is authenticated and session established (see diagram below).
At the time of writing this article RouterOS cannot be used in LAC role. For this reason article will demonstrate how to set up very basic network with RouterOS as LNS and Cisco router as LAC.
# Configuration
We will be using simple configuration to demonstrate very basics of VPDN setup. Lets assume that LAC will forward to the LNS clients with FQDN name containingmt.lvdomain.
# Client
For the sake of simplicity lets assume that client is RouterOS router:
```
/interface pppoe-client add interface=ether1 user=good_worker@mt.lv password=strongpass
```
# LAC
Lets assume that client is connected to the GigabitEthernet1 port and IP address of the LNS server is 10.155.101.231
```
aaa new-model
!
aaa authentication ppp default local
!
vpdn enable
vpdn aaa attribute nas-ip-address vpdn-nas
vpdn search-order domain dnis
!
vpdn-group LAC
request-dialin
protocol l2tp
domain mt.lv
initiate-to ip 10.155.101.231
source-ip 10.155.101.216
local name LAC
l2tp tunnel password 0 tunnelpass
!
bba-group pppoe MAIN-BBA
virtual-template 1
!
interface GigabitEthernet1
pppoe enable group MAIN-BBA
!
interface Virtual-Template1
description pppoe MAIN-BBA
no ip address
no peer default ip address
ppp mtu adaptive
ppp authentication chap
!
```
Note that this setup does not authenticate client nor locally nor via RADIUS, does not actually check domain name, does not control L2 access for the sake of simplicity. If you want to use those features refer to Cisco configuration manuals.
# LNS
On the LNS we need to enable L2TP server and set up method to authenticate the L2TP connection from the LAC.
```
/interface l2tp-server server
set enabled=yes
/ppp l2tp-secret
add address=10.155.101.216/32 secret=tunnelpass
```
Now the actual user authentication. In this case we will be using local authentication method for the sake of simplicity.
```
/ip pool
add name=pool0 ranges=192.168.99.2-192.168.99.99
/ppp profile
set default local-address=192.168.99.1 remote-address=pool0
/ppp secret
add name=good_worker@mt.lv password=strongpass
```
# Status Check
On the LNS you can see all successfully connected clients by checking l2tp server interfaces or checking active ppp connections:
```
[admin@CHR_v6_bgp] /interface l2tp-server> print
Flags: X - disabled, D - dynamic, R - running
# NAME USER MTU CLIENT-ADDRESS UPTIME ENCODING
0 DR <l2tp-... good_worker@mt.lv 1450 10.155.101.216 6h13m49s
[admin@CHR_v6_bgp] /ppp active> print
Flags: R - radius
# NAME SERVICE CALLER-ID ADDRESS UPTIME ENCODING
0 good_worker@mt.lv l2tp 10.155.101.216 192.168.99.2 6h15m57s
```
On the LAC we can also see active client sessions and active L2TP tunnel between LAC and LNS:
```
csrLAC# show vpdn
L2TP Tunnel and Session Information Total tunnels 1 sessions 1
LocTunID RemTunID Remote Name State Remote Address Sessn L2TP Class/
Count VPDN Group
26090 11 CHR_v6_bgp est 10.155.101.231 50 LAC
LocID RemID TunID Username, Intf/ State Last Chg Uniq ID
Vcid, Circuit
18521 16 26090 good_worker@mt.lv, Gi1 est 06:17:07 571
```
# Session Establishment
Lets look closely on how clients sessions gets authenticated and established over the LAC.
* IP Control Protocol (IPCP) phase is performed, IP addresses and routes are installed. At this point sessions is considered established.