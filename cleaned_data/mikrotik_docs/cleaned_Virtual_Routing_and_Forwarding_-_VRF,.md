# Document Information
Title: Virtual Routing and Forwarding - VRF
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328206/Virtual+Routing+and+Forwarding+-+VRF,

# Content
# Description
RouterOS allows to create multiple Virtual Routing and Forwarding instances on a single router. This is useful for BGP-based MPLS VPNs. Unlike BGP VPLS, which is OSI Layer 2 technology, BGP VRF VPNs work in Layer 3 and as such exchange IP prefixes between routers. VRFs solve the problem of overlapping IP prefixes and provide the required privacy (via separated routing for different VPNs).
It is possible to set up vrf-lite setups or use multi-protocol BGP with VPNv4 address family to distribute routes from VRF routing tables - not only to other routers, but also to different routing tables in the router itself.
# Configuration
VRF table is created in/ip vrfmenu. After the VRF config is created routing table mapping is added (a dynamic table with the same name is created). Each active VRF will always have a mapped routing table.
```
/ip vrf
```
```
[admin@arm-bgp] /ip/vrf> print
Flags: X - disabled; * - builtin
0  * name="main" interfaces=all
[admin@arm-bgp] /routing/table> print
Flags: D - dynamic; X - disabled, I - invalid; U - used
0 D   name="main" fib
```
Note that the order of the added VRFs is significant. To properly match which interface will belong to the VRF care must be taken to place VRFs in the correct order (matching is done starting from the top entry, just like firewall rules).
Let's look at the following example:
```
[admin@arm-bgp] /ip/vrf> print
Flags: X - disabled; * - builtin
0  * name="main" interfaces=all
1    name="myVrf" interfaces=lo_vrf
```
Since the first entry is matching all the interfaces, the second VRF will not have any interfaces added. To fix the problem order of the entries must be changed.
```
[admin@arm-bgp] /ip/vrf> move 1 0
[admin@arm-bgp] /ip/vrf> print
Flags: X - disabled; * - builtin
0    name="myVrf" interfaces=lo_vrf
1  * name="main" interfaces=all
```
Connected routes from the interfaces assigned to the VRF will be installed in the right routing table automatically.
For example, let's make an SSH service to listen for connections on the interfaces belonging to the VRF:
```
[admin@arm-bgp] /ip/service> set ssh vrf=myVrf
[admin@arm-bgp] /ip/service> print
Flags: X, I - INVALID
Columns: NAME, PORT, CERTIFICATE, VRF
# NAME     PORT  CERTIFICATE  VRF
0   telnet     23               main
1   ftp        21
2   www        80               main
3   ssh        22               myVrf
4 X www-ssl   443  none         main
5   api      8728               main
6   winbox   8291               main
7   api-ssl  8729  none         main
```
Adding routes to the VRF is as simple as specifying the routing-table parameter when adding the route and specifying in which routing table to resolve the gateway by specifying@nameafter the gateway IP:
```
/ip route add dst-address=192.168.1.0/24 gateway=172.16.1.1@myVrf routing-table=myVrf
```
Traffic leaking between VRFs is possible if the gateway is explicitly set to be resolved in another VRF, for example:
```
# add route in the myVrf, but resolve the gateway in the main table
/ip route add dst-address=192.168.1.0/24 gateway=172.16.1.1@main routing-table=myVrf
# add route in the main table, but resolve the gateway in the myVrf
/ip route add dst-address=192.168.1.0/24 gateway=172.16.1.1@myVrf
```
# Supported features
Different services can be placed in specific VRF on which the service is listening for incoming or creating outgoing connections. By default, all services are using themaintable, but it can be changed with a separatevrfparameter or by specifying the VRF name separated by "@" at the end of the IP address.
```
main
```
```
vrf
```
Below is the list of supported services.
Feature | Support | Comment
---------------------------
BGP | + | /routing bgp template
add name=bgp-template1 vrf=vrf1
/routing bgp vpls
add name=bgp-vpls1 site-id=10 vrf=vrf1
/routing bgp vpn
add label-allocation-policy=per-vrf vrf=vrf1
E-mail | + | /tool e-mail
set address=192.168.88.1 vrf=vrf1
IP Services | + | VRF is supported fortelnet,www,ssh,www-ssl,api,winbox,api-sslservices. Theftpservice does not support changing the VRF./ip service
set telnet vrf=vrf1
L2TP Client | + | /interface l2tp-client
add connect-to=192.168.88.1@vrf1 name=l2tp-out1 user=l2tp-client
MPLS | + | /mpls ldp
add vrf=vrf1
Netwatch | + | /tool netwatch
add host=192.168.88.1@vrf1
NTP | + | /system ntp client
set vrf=vrf1
/system ntp server
set vrf=vrf1
OSPF | + | /routing ospf instance
add disabled=no name=ospf-instance-1 vrf=vrf1
ping | + | /ping 192.168.88.1 vrf=vrf1
RADIUS | + | /radius add address=192.168.88.1@vrf1
/radius incoming set vrf=vrf1
RIP | + | /routing rip instance
add name=rip-instance-1 vrf=vrf1
RPKI | + | /routing rpki
add vrf=vrf1
SNMP | + | /snmp
set vrf=vrf1
EoIP | + | /interface eoip
add remote-address=192.168.1.1@vrf1
IPIP | + | /interface ipip
add remote-address=192.168.1.1@vrf1
GRE | + | /interface gre
add remote-address=192.168.1.1@vrf1
SSTP-client | + | /interface sstp-client
add connect-to=192.168.1.1@vrf1
OVPN-client | + | /interface ovpn-client
add connect-to=192.168.1.1@vrf1
L2TP-ether | + | /interface l2tp-ether
add connect-to=192.168.2.2@vrf
VXLAN | + | /interface vxlan
add vni=10 vrf=vrf1
Fetch | + | /tool/fetch
address=10.155.28.236@vrf1 mode=ftp src-path=my_file.pcap user=admin password=""
DNS | +Starting from RouterOS v7.15 | /ip dns set vrf=vrf1
DHCP-Relay | +Starting from RouterOS v7.15 | /ip dhcp-relay set dhcp-server-vrf=vrf1If dhcp-client is in vrf - special parameter in"ip dhcp-relay" configuration is not needed
Feature
Support
Comment
```
/routing bgp template
add name=bgp-template1 vrf=vrf1
/routing bgp vpls
add name=bgp-vpls1 site-id=10 vrf=vrf1
/routing bgp vpn
add label-allocation-policy=per-vrf vrf=vrf1
```
```
/tool e-mail
set address=192.168.88.1 vrf=vrf1
```
VRF is supported fortelnet,www,ssh,www-ssl,api,winbox,api-sslservices. Theftpservice does not support changing the VRF.
```
telnet
```
```
www
```
```
ssh
```
```
www-ssl
```
```
api
```
```
winbox
```
```
api-ssl
```
```
ftp
```
```
/ip service
set telnet vrf=vrf1
```
```
/interface l2tp-client
add connect-to=192.168.88.1@vrf1 name=l2tp-out1 user=l2tp-client
```
```
/mpls ldp
add vrf=vrf1
```
+
```
/tool netwatch
add host=192.168.88.1@vrf1
```
+
```
/system ntp client
set vrf=vrf1
/system ntp server
set vrf=vrf1
```
+
```
/routing ospf instance
add disabled=no name=ospf-instance-1 vrf=vrf1
```
+
```
/ping 192.168.88.1 vrf=vrf1
```
+
```
/radius add address=192.168.88.1@vrf1
/radius incoming set vrf=vrf1
```
+
```
/routing rip instance
add name=rip-instance-1 vrf=vrf1
```
+
```
/routing rpki
add vrf=vrf1
```
+
```
/snmp
set vrf=vrf1
```
+
```
/interface eoip
add remote-address=192.168.1.1@vrf1
```
+
```
/interface ipip
add remote-address=192.168.1.1@vrf1
```
+
```
/interface gre
add remote-address=192.168.1.1@vrf1
```
+
```
/interface sstp-client
add connect-to=192.168.1.1@vrf1
```
+
```
/interface ovpn-client
add connect-to=192.168.1.1@vrf1
```
+
```
/interface l2tp-ether
add connect-to=192.168.2.2@vrf
```
+
```
/interface vxlan
add vni=10 vrf=vrf1
```
+
```
/tool/fetch
address=10.155.28.236@vrf1 mode=ftp src-path=my_file.pcap user=admin password=""
```
+
Starting from RouterOS v7.15
```
/ip dns set vrf=vrf1
```
+
Starting from RouterOS v7.15
```
/ip dhcp-relay set dhcp-server-vrf=vrf1
```
# VRF interfaces in firewall
Started from version 7.14 when interfaces are added in VRF - virtual VRF interface is created automatically. If it is needed to match traffic which belongs to VRF interface, VRF virtual interface should be used in firewall filters, for example:
```
/ip vrf add interfaces=ether5 name=vrf5
/ip firewall filter add chain=input in-interface=vrf5 action=accept
```
If there are several interfaces in one VRF but it is needed to match only one of these interfaces - marks should be used. For example:
```
/ip vrf add interface=ether15,ether16 vrf=vrf1516
/ip firewall mangle
add action=mark-connection chain=prerouting connection-state=new in-interface=ether15 new-connection-mark=input_allow passthrough=yes
/ip firewall filter
add action=accept chain=input connection-mark=input_allow
```
# Examples
# Simple VRF-Lite setup
Let's consider a setup where we need two customer VRFs that require access to the internet:
```
/ip address
add address=172.16.1.2/24 interface=public
add address=192.168.1.1/24 interface=ether1
add address=192.168.2.1/24 interface=ether2
/ip route
add gateway=172.16.1.1
# add VRF configuration
/ip vrf
add name=cust_a interface=ether1 place-before 0
add name=cust_b interface=ether2 place-before 0
# add vrf routes
/ip route
add gateway=172.16.1.1@main routing-table=cust_a
add gateway=172.16.1.1@main routing-table=cust_b
# masquerade local source
/ip firewall nat add chain=srcnat out-interface=public action=masquerade
```
It might be necessary to ensure that packets coming in the "public" interface can actually reach the correct VRF.This can be solved by marking new connections originated by the VRF customers and steering the traffic by routing marks of incoming packets on the "public" interface.
```
# mark new customer connections
/ip firewall mangle
add action=mark-connection chain=prerouting connection-state=new new-connection-mark=\
cust_a_conn src-address=192.168.1.0/24 passthrough=no
add action=mark-connection chain=prerouting connection-state=new new-connection-mark=\
cust_b_conn src-address=192.168.2.0/24 passthrough=no
# mark routing
/ip firewall mangle
add action=mark-routing chain=prerouting connection-mark=cust_a_conn \
in-interface=public new-routing-mark=cust_a
add action=mark-routing chain=prerouting connection-mark=cust_b_conn \
in-interface=public new-routing-mark=cust_b
```
# Static inter-VRF routes
In general, it is recommended that all routes between VRF should be exchanged using BGP local import and export functionality. If that is not enough, static routes can be used to achieve this so-called route leaking.
There are two ways to install a route that has a gateway in a different routing table than the route itself.
The first way is to explicitly specify the routing table in the gateway field when adding a route. This is only possible when leaking a route and gateway from the "main" routing table to a different routing table (VRF). Example:
```
# add route to 5.5.5.0/24 in 'vrf1' routing table with gateway in the main routing table
add dst-address=5.5.5.0/24 gateway=10.3.0.1@main routing-table=vrf1
```
The second way is to explicitly specify the interface in the gateway field. The interface specified can belong to a VRF instance. Example:
```
# add route to 5.5.5.0/24 in the main routing table with gateway at 'ether2' VRF interface
add dst-address=5.5.5.0/24 gateway=10.3.0.1%ether2 routing-table=main
# add route to 5.5.5.0/24 in the main routing table with 'ptp-link-1' VRF interface as gateway
add dst-address=5.5.5.0/24 gateway=ptp-link-1 routing-table=main
```
As can be observed, there are two variations possible - to specify gateway asip_address%interfaceor to simply specifyaninterface. The first should be used for broadcast interfaces in most cases. The second should be used for point-to-point interfaces, and also for broadcast interfaces, if the route is a connected route in some VRF. For example, if you have an address1.2.3.4/24on interfaceether2that is put in a VRF, there will be a connected route to1.2.3.0/24in that VRF's routing table. It is acceptable to add a static route1.2.3.0/24in a different routing table with an interface-only gateway, even thoughether2is a broadcast interface:
```
1.2.3.4/24
```
```
1.2.3.0/24
```
```
1.2.3.0/24
```
```
add dst-address=1.2.3.0/24 gateway=ether2 routing-table=main
```
# Static VRF-Lite Connected route leaking
Sometimes it is necessary to access directly connected resources from another vrf. In our example setup we have two connected networks each in its own VRF. And we want to allow client1 to be able to access client2.
```
+-----------------+
|+-vrf1-+ +-vrf2-+|
client1(*.2)-------||ip *.1| |ip *.1||-------client2(*.2)
(10.11.0.0/24)  |+------+ +------+|   (10.12.0.0/24)
+-----------------+
```
```
/ip address
add address=10.11.0.1/24 interface=sfp-sfpplus1
add address=10.12.0.1/24 interface=sfp-sfpplus2
# add VRF configuration
/ip vrf
add name=vrfTest1 interface=sfp-sfpplus1 place-before 0
add name=vrfTest2 interface=sfp-sfpplus2 place-before 0
```
We can say that connected network is reachable on specific vrf by setting gateway "interface@vrf"
```
# add vrf routes
/ip route
add dst-address=10.11.0.0/24 gateway="sfp-sfpplus1@vrfTest1" routing-table=vrfTest2
add dst-address=10.12.0.0/24 gateway="sfp-sfpplus2@vrfTest2" routing-table=vrfTest1
```
Verify routes and reachability:
```
[admin@CCR2004_2XS] /ip/route> print detail
Flags: D - dynamic; X - disabled, I - inactive, A - active;
c - connect, s - static, r - rip, b - bgp, o - ospf, i - is-is, d - dhcp, v - vpn, m - modem, y - bgp-mpls-vpn; H - hw-offloaded; + - ecmp
DAc   dst-address=111.11.0.0/24 routing-table=vrfTest1 gateway=sfp-sfpplus1@vrfTest1 immediate-gw=sfp-sfpplus1 distance=0 scope=10 suppress-hw-offload=no
local-address=111.11.0.1%sfp-sfpplus1@vrfTest1
1  As   dst-address=111.12.0.0/24 routing-table=vrfTest1 pref-src="" gateway=vrfTest2 immediate-gw=vrfTest2 distance=1 scope=30 target-scope=10
suppress-hw-offload=no
2  As   dst-address=111.11.0.0/24 routing-table=vrfTest2 pref-src="" gateway=vrfTest1 immediate-gw=vrfTest1 distance=1 scope=30 target-scope=10
suppress-hw-offload=no
DAc   dst-address=111.12.0.0/24 routing-table=vrfTest2 gateway=sfp-sfpplus2@vrfTest2 immediate-gw=sfp-sfpplus2 distance=0 scope=10 suppress-hw-offload=no
local-address=111.12.0.1%sfp-sfpplus2@vrfTest2
```
```
[admin@cl2] > /ping 111.11.0.2 src-address=111.12.0.2
SEQ HOST                                     SIZE TTL TIME       STATUS
0 111.11.0.2                                 56  64 67us
1 111.11.0.2                                 56  64 61us
sent=2 received=2 packet-loss=0% min-rtt=61us avg-rtt=64u
```
But now what if we want to access routers local address located in another vrf?
```
[admin@cl2] > /ping 111.11.0.1 src-address=111.12.0.2
SEQ HOST                                     SIZE TTL TIME       STATUS
0 111.11.0.1                                                   timeout
1 111.11.0.1                                                   timeout
sent=2 received=0 packet-loss=100%
```
Approach with "interface@vrf" gateways works only when router is forwarding packets. To access local vrf addresses we need to route to the vrf interface.
```
# add vrf routes
/ip route
add dst-address=10.11.0.0/24 gateway=vrfTest1@vrfTest1 routing-table=vrfTest2
add dst-address=10.12.0.0/24 gateway=vrfTest2@vrfTest2 routing-table=vrfTest1
```
```
[admin@cl2] > /ping 111.11.0.1 src-address=111.12.0.2
SEQ HOST                                     SIZE TTL TIME       STATUS
0 111.11.0.1                                 56  64 67us
1 111.11.0.1                                 56  64 61us
sent=2 received=2 packet-loss=0% min-rtt=61us avg-rtt=64u
```
# Dynamic Vrf-Lite route leaking
With large enough setups static route leaking is not sufficient. Let's consider we have the same setup as in static route leaking example plus ipv6 addresses, just for demonstration.
```
/ip address
add address=10.11.0.1/24 interface=sfp-sfpplus1
add address=10.12.0.1/24 interface=sfp-sfpplus2
# add VRF configuration
/ip vrf
add name=vrfTest1 interface=sfp-sfpplus1 place-before 0
add name=vrfTest2 interface=sfp-sfpplus2 place-before 0
/ipv6 address
add address=2001:1::1 advertise=no interface=sfp-sfpplus1
add address=2001:2::1 advertise=no interface=sfp-sfpplus2
```
We can use BGP VPN to leak local routes without actually establishing BGP session.
```
/routing bgp vpn
add export.redistribute=connected .route-targets=1:1 import.route-targets=1:2 label-allocation-policy=per-vrf name=bgp-mpls-vpn-1 \
route-distinguisher=1.2.3.4:1 vrf=vrfTest1
add export.redistribute=connected .route-targets=1:2 import.route-targets=1:1 label-allocation-policy=per-vrf name=bgp-mpls-vpn-2 \
route-distinguisher=1.2.3.4:1 vrf=vrfTest2
```
Now we can see that connected routes between VRFs are exchanged
```
[admin@CCR2004_2XS] > /routing route print where dst-address in 111.0.0.0/8 && afi=ip4
...
Ac   afi=ip4 contribution=active dst-address=111.11.0.0/24 routing-table=vrfTest1 gateway=sfp-sfpplus1@vrfTest1 immediate-gw=sfp-sfpplus1 distance=0 scope=10
belongs-to="connected" local-address=111.11.0.1%sfp-sfpplus1@vrfTest1
debug.fwp-ptr=0x202421E0
Ay   afi=ip4 contribution=best-candidate dst-address=111.12.0.0/24 routing-table=vrfTest1 label=17 gateway=vrfTest2@vrfTest2 immediate-gw=sfp-sfpplus2
distance=200 scope=40 target-scope=10 belongs-to="bgp-mpls-vpn-1-bgp-mpls-vpn-2-connected-export-import"
bgp.ext-communities=rt:1:2 .atomic-aggregate=no .origin=incomplete
debug.fwp-ptr=0x202425A0
Ay   afi=ip4 contribution=best-candidate dst-address=111.11.0.0/24 routing-table=vrfTest2 label=16 gateway=vrfTest1@vrfTest1 immediate-gw=sfp-sfpplus1
distance=200 scope=40 target-scope=10 belongs-to="bgp-mpls-vpn-2-bgp-mpls-vpn-1-connected-export-import"
bgp.ext-communities=rt:1:1 .atomic-aggregate=no .origin=incomplete
debug.fwp-ptr=0x202424E0
Ac   afi=ip4 contribution=active dst-address=111.12.0.0/24 routing-table=vrfTest2 gateway=sfp-sfpplus2@vrfTest2 immediate-gw=sfp-sfpplus2 distance=0 scope=10
belongs-to="connected" local-address=111.12.0.1%sfp-sfpplus2@vrfTest2
debug.fwp-ptr=0x20242240
```
And IPv6 too:
```
[admin@CCR2004_2XS] /routing/route> print detail where dst-address in 2001::/8 && afi=ip6
...
Ac   afi=ip6 contribution=active dst-address=2001:1::/64 routing-table=vrfTest1 gateway=sfp-sfpplus1@vrfTest1 immediate-gw=sfp-sfpplus1 distance=0 scope=10
belongs-to="connected" local-address=2001:1::1%sfp-sfpplus1@vrfTest1
debug.fwp-ptr=0x20242300
Ay   afi=ip6 contribution=active dst-address=2001:2::/64 routing-table=vrfTest1 label=17 gateway=vrfTest2@vrfTest2 immediate-gw=sfp-sfpplus2 distance=200
scope=40 target-scope=10 belongs-to="bgp-mpls-vpn-1-bgp-mpls-vpn-2-connected-export-import"
bgp.ext-communities=rt:1:2 .atomic-aggregate=no .origin=incomplete
debug.fwp-ptr=0x202425A0
Ay   afi=ip6 contribution=active dst-address=2001:1::/64 routing-table=vrfTest2 label=16 gateway=vrfTest1@vrfTest1 immediate-gw=sfp-sfpplus1 distance=200
scope=40 target-scope=10 belongs-to="bgp-mpls-vpn-2-bgp-mpls-vpn-1-connected-export-import"
bgp.ext-communities=rt:1:1 .atomic-aggregate=no .origin=incomplete
debug.fwp-ptr=0x202424E0
Ac   afi=ip6 contribution=active dst-address=2001:2::/64 routing-table=vrfTest2 gateway=sfp-sfpplus2@vrfTest2 immediate-gw=sfp-sfpplus2 distance=0 scope=10
belongs-to="connected" local-address=2001:2::1%sfp-sfpplus2@vrfTest2
debug.fwp-ptr=0x20242360
```
# Dynamic Vrf-Lite route leaking (old workaround)
Before ROS v7.14 there were no mechanism to leak routes from one VRF instance to another within the same router.
As a workaround, it was possible to create a tunnel between two locally configure loopback addresses and assign each tunnel endpoint to its own VRF. Then it is possible to run either dynamic routing protocols or set up static routes to leak between both VRFs.
The downside of this approach is that tunnel must be created between each VRF where routes should be leaked (create a full mesh), which significantly complicates configuration even if there are just several VRFs, not to mention more complicated setups.
For example, to leak routes between 5 VRFs it would requiren * ( n – 1) / 2 connections, which will lead to the setup with 20 tunnel endpoints and 20 OSPF instances on one router.
Example config with two VRFs of this method:
```
/interface bridge
add name=dummy_custC
add name=dummy_custB
add name=lo1
add name=lo2
/ip address
add address=111.255.255.1 interface=lo1 network=111.255.255.1
add address=111.255.255.2 interface=lo2 network=111.255.255.2
add address=172.16.1.0/24 interface=dummy_custC network=172.16.1.0
add address=172.16.2.0/24 interface=dummy_custB network=172.16.2.0
/interface ipip
add local-address=111.255.255.1 name=ipip-tunnel1 remote-address=111.255.255.2
add local-address=111.255.255.2 name=ipip-tunnel2 remote-address=111.255.255.1
/ip address
add address=192.168.1.1/24 interface=ipip-tunnel1 network=192.168.1.0
add address=192.168.1.2/24 interface=ipip-tunnel2 network=192.168.1.0
/ip vrf
add interfaces=ipip-tunnel1,dummy_custC name=custC
add interfaces=ipip-tunnel2,dummy_custB name=custB
/routing ospf instance
add disabled=no name=i2_custB redistribute=connected,static,copy router-id=192.168.1.1 routing-table=custB vrf=custB
add disabled=no name=i2_custC redistribute=connected router-id=192.168.1.2 routing-table=custC vrf=custC
/routing ospf area
add disabled=no instance=i2_custB name=custB_bb
add disabled=no instance=i2_custC name=custC_bb
/routing ospf interface-template
add area=custB_bb disabled=no networks=192.168.1.0/24
add area=custC_bb disabled=no networks=192.168.1.0/24
```
Result:
```
[admin@rack1_b36_CCR1009] /routing/ospf/neighbor> print
Flags: V - virtual; D - dynamic
0  D instance=i2_custB area=custB_bb address=192.168.1.1 priority=128 router-id=192.168.1.2 dr=192.168.1.1 bdr=192.168.1.2
state="Full" state-changes=6 adjacency=41m28s timeout=33s
1  D instance=i2_custC area=custC_bb address=192.168.1.2 priority=128 router-id=192.168.1.1 dr=192.168.1.1 bdr=192.168.1.2
state="Full" state-changes=6 adjacency=41m28s timeout=33s
[admin@rack1_b36_CCR1009] /ip/route> print where routing-table=custB
Flags: D - DYNAMIC; A - ACTIVE; c, s, o, y - COPY
Columns: DST-ADDRESS, GATEWAY, DISTANCE
DST-ADDRESS       GATEWAY                         DISTANCE
DAo 172.16.1.0/24     192.168.1.1%ipip-tunnel2@custB       110
DAc 172.16.2.0/24     dummy_custB@custB                      0
DAc 192.168.1.0/24    ipip-tunnel2@custB                     0
[admin@rack1_b36_CCR1009] > /ip route/print where routing-table=custC
Flags: D - DYNAMIC; A - ACTIVE; c, o, y - COPY
Columns: DST-ADDRESS, GATEWAY, DISTANCE
DST-ADDRESS       GATEWAY                         DISTANCE
DAc 172.16.1.0/24     dummy_custC@custC                      0
DAo 172.16.2.0/24     192.168.1.2%ipip-tunnel1@custC       110
DAc 192.168.1.0/24    ipip-tunnel1@custC                     0
```
# The simplest MPLS VPN setup
In this example, a rudimentary MPLS backbone (consisting of two Provider Edge (PE) routers PE1 and PE2) is created and configured to forward traffic between Customer Edge (CE) routers CE1 and CE2 routers that belong tocust-oneVPN.
# CE1 Router
```
/ip address add address=10.1.1.1/24 interface=ether1
# use static routing
/ip route add dst-address=10.3.3.0/24 gateway=10.1.1.2
```
# CE2 Router
```
/ip address add address=10.3.3.4/24 interface=ether1
/ip route add dst-address=10.1.1.0/24 gateway=10.3.3.3
```
# PE1 Router
```
/interface bridge add name=lobridge
/ip address add address=10.1.1.2/24 interface=ether1
/ip address add address=10.2.2.2/24 interface=ether2
/ip address add address=10.5.5.2/32 interface=lobridge
/ip vrf add name=cust-one interfaces=ether1
/mpls ldp add enabled=yes transport-address=10.5.5.2 lsr-id=10.5.5.2
/mpls ldp interface add interface=ether2
/routing bgp template set default as=65000
/routing bgp vpn
add vrf=cust-one \
route-distinguisher=1.1.1.1:111 \
import.route-targets=1.1.1.1:111 \
import.router-id=cust-one \
export.redistribute=connected \
export.route-targets=1.1.1.1:111 \
label-allocation-policy=per-vrf
/routing bgp connection
add template=default remote.address=10.5.5.3 address-families=vpnv4 local.address=10.5.5.2
# add route to the remote BGP peer's loopback address
/ip route add dst-address=10.5.5.3/32 gateway=10.2.2.3
```
# PE2 Router (Cisco)
```
ip vrf cust-one
rd 1.1.1.1:111
route-target export 1.1.1.1:111
route-target import 1.1.1.1:111
exit
interface Loopback0
ip address 10.5.5.3 255.255.255.255
mpls ldp router-id Loopback0 force
mpls label protocol ldp
interface FastEthernet0/0
ip address 10.2.2.3 255.255.255.0
mpls ip
interface FastEthernet1/0
ip vrf forwarding cust-one
ip address 10.3.3.3 255.255.255.0
router bgp 65000
neighbor 10.5.5.2 remote-as 65000
neighbor 10.5.5.2 update-source Loopback0
address-family vpnv4
neighbor 10.5.5.2 activate
neighbor 10.5.5.2 send-community both
exit-address-family
address-family ipv4 vrf cust-one
redistribute connected
exit-address-family
ip route 10.5.5.2 255.255.255.255 10.2.2.2
```
Results
Check that VPNv4 route redistribution is working:
```
[admin@PE1] /routing/route> print detail where afi="vpn4"
Flags: X - disabled, F - filtered, U - unreachable, A - active;
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, a - ldp-address, l - l
dp-mapping, g - slaac, y - bgp-mpls-vpn;
H - hw-offloaded; + - ecmp, B - blackhole
Ab   afi=vpn4 contribution=active dst-address=111.16.0.0/24&1.1.1.1:111 routing-table=main label=16
gateway=111.111.111.4 immediate-gw=111.13.0.2%ether9 distance=200 scope=40 target-scope=30
belongs-to="bgp-VPN4-111.111.111.4"
bgp.peer-cache-id=*2C00011 .as-path="65511" .ext-communities=rt:1.1.1.1:111 .local-pref=100
.atomic-aggregate=yes .origin=igp
debug.fwp-ptr=0x202427E0
[admin@PE1] /routing/bgp/advertisements> print
0 peer=to-pe2-1 dst=10.1.1.0/24 local-pref=100 origin=2 ext-communities=rt:1.1.1.1:111 atomic-aggregate=yes
```
Check that the 10.3.3.0 is installed in IP routes, in the cust-one route table:
```
[admin@PE1] > /ip route print where routing-table="cust-one"
Flags: D - DYNAMIC; A - ACTIVE; c, b, y - BGP-MPLS-VPN
Columns: DST-ADDRESS, GATEWAY, DISTANCE
# DST-ADDRESS     GATEWAY         DISTANCE
0 ADC 10.1.1.0/24 ether1@cust-one        0
1 ADb 10.3.3.0/24 10.5.5.3              20
```
Let's take a closer look at IP routes in cust-one VRF. The 10.1.1.0/24 IP prefix is a connected route that belongs to an interface that was configured to belong to cust-one VRF. The 10.3.3.0/24 IP prefix was advertised via BGP as a VPNv4 route from PE2 and is imported in this VRF routing table, because our configuredimport-route-targetsmatched the BGP extended communities attribute it was advertised with.
```
[admin@PE1] /routing/route> print detail where routing-table="cust-one"
Flags: X - disabled, F - filtered, U - unreachable, A - active;
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, a - ldp-address, l - l
dp-mapping, g - slaac, y - bgp-mpls-vpn;
H - hw-offloaded; + - ecmp, B - blackhole
Ac   afi=ip4 contribution=active dst-address=10.1.1.0/24 routing-table=cust-one
gateway=ether1@cust-one immediate-gw=ether1 distance=0 scope=10 belongs-to="connected"
local-address=10.1.1.2%ether1@cust-one
debug.fwp-ptr=0x202420C0
Ay   afi=ip4 contribution=active dst-address=10.3.3.0/24 routing-table=cust-one label=16
gateway=10.5.5.3 immediate-gw=10.2.2.3%ether2 distance=20 scope=40 target-scope=30
belongs-to="bgp-mpls-vpn-1-bgp-VPN4-10.5.5.3-import"
bgp.peer-cache-id=*2C00011 .ext-communities=rt:1.1.1.1:111 .local-pref=100
.atomic-aggregate=yes .origin=igp
debug.fwp-ptr=0x20242840
[admin@PE1] /routing/route> print detail where afi="vpn4"
Flags: X - disabled, F - filtered, U - unreachable, A - active;
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, a - ldp-address, l - l
dp-mapping, g - slaac, y - bgp-mpls-vpn;
H - hw-offloaded; + - ecmp, B - blackhole
Ay   afi=vpn4 contribution=active dst-address=10.1.1.0/24&1.1.1.1:111 routing-table=main label=19
gateway=ether1@cust-one immediate-gw=ether1 distance=200 scope=40 target-scope=10
belongs-to="bgp-mpls-vpn-1-connected-export"
bgp.ext-communities=rt:1.1.1.1:1111 .atomic-aggregate=no .origin=incomplete
debug.fwp-ptr=0x202426C0
Ab   afi=vpn4 contribution=active dst-address=10.3.3.0/24&1.1.1.1:111 routing-table=main label=16
gateway=10.5.5.3 immediate-gw=10.2.2.3%ether2 distance=200 scope=40 target-scope=30
belongs-to="bgp-VPN4-10.5.5.3"
bgp.peer-cache-id=*2C00011 .ext-communities=rt:1.1.1.1:111 .local-pref=100
.atomic-aggregate=yes .origin=igp
debug.fwp-ptr=0x202427E0
```
The same for Cisco:
```
PE2# show ip bgp vpnv4 all
BGP table version is 5, local router ID is 10.5.5.3
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete
Network Next Hop Metric LocPrf Weight Path
Route Distinguisher: 1.1.1.1:111 (default for vrf cust-one)
PE2# show ip route vrf cust-one
Routing Table: cust-one
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 - OSPF external type 2
i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
ia - IS-IS inter area, * - candidate default, U - per-user static route
o - ODR, P - periodic downloaded static route
Gateway of last resort is not set
10.0.0.0/24 is subnetted, 1 subnets
B 10.1.1.0 [200/0] via 10.5.5.2, 00:05:33
10.0.0.0/24 is subnetted, 1 subnets
C 10.3.3.0 is directly connected, FastEthernet1/0
```
You should be able to ping from CE1 to CE2 and vice versa.
```
[admin@CE1] > /ping 10.3.3.4
10.3.3.4 64 byte ping: ttl=62 time=18 ms
10.3.3.4 64 byte ping: ttl=62 time=13 ms
10.3.3.4 64 byte ping: ttl=62 time=13 ms
10.3.3.4 64 byte ping: ttl=62 time=14 ms
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 13/14.5/18 ms
```
# A more complicated setup (changes only)
As opposed to the simplest setup, in this example, we have two customers: cust-one and cust-two.
We configure two VPNs for them, cust-one and cust-two respectively, and exchange all routes between them. (This is also called "route leaking").
Note that this could be not the most typical setup, because routes are usually not exchanged between different customers. In contrast, by default, it should not be possible to gain access from one VRF site to a different VRF site in another VPN. (This is the "Private" aspect of VPNs.) Separate routing is a way to provide privacy, and it is also required to solve the problem of overlapping IP network prefixes. Route exchange is in direct conflict with these two requirements but may sometimes be needed (e.g. temp. solution when two customers are migrating to a single network infrastructure).
# CE1 Router,cust-one
```
/ip route add dst-address=10.4.4.0/24 gateway=10.1.1.2
```
# CE2 Router,cust-one
```
/ip route add dst-address=10.4.4.0/24 gateway=10.3.3.3
```
CE1 Router,cust-two
```
/ip address add address=10.4.4.5 interface=ether1
/ip route add dst-address=10.1.1.0/24 gateway=10.3.3.3
/ip route add dst-address=10.3.3.0/24 gateway=10.3.3.3
```
# PE1 Router
```
# replace the old BGP VPN with this:
/routing bgp vpn
add vrf=cust-one \
export.redistribute=connected \
route-distinguisher=1.1.1.1:111 \
import.route-targets=1.1.1.1:111,2.2.2.2:222  \
export.route-targets=1.1.1.1:111
```
PE2 Router (Cisco)
```
ip vrf cust-one
rd 1.1.1.1:111
route-target export 1.1.1.1:111
route-target import 1.1.1.1:111
route-target import 2.2.2.2:222
exit
ip vrf cust-two
rd 2.2.2.2:222
route-target export 2.2.2.2:222
route-target import 1.1.1.1:111
route-target import 2.2.2.2:222
exit
interface FastEthernet2/0
ip vrf forwarding cust-two
ip address 10.4.4.3 255.255.255.0
router bgp 65000
address-family ipv4 vrf cust-two
redistribute connected
exit-address-family
```
# Variation: replace the Cisco with another MT
# PE2 Mikrotik config
```
/interface bridge add name=lobridge
/ip address
add address=10.2.2.3/24 interface=ether1
add address=10.3.3.3/24 interface=ether2
add address=10.4.4.3/24 interface=ether3
add address=10.5.5.3/32 interface=lobridge
/ip vrf
add name=cust-one interfaces=ether2
add name=cust-two interfaces=ether3
/mpls ldp add enabled=yes transport-address=10.5.5.3
/mpls ldp interface add interface=ether1
/routing bgp template set default as=65000
/routing bgp vpn
add vrf=cust-one \
export.redistribute=connected \
route-distinguisher=1.1.1.1:111 \
import.route-targets=1.1.1.1:111,2.2.2.2:222 \
export.route-targets=1.1.1.1:111 \
add vrf=cust-two \
export.redistribute=connected \
route-distinguisher=2.2.2.2:222 \
import.route-targets=1.1.1.1:111,2.2.2.2:222 \
export.route-targets=2.2.2.2:222 \
/routing bgp connection
add template=default remote.address=10.5.5.2 address-families=vpnv4 local.address=10.5.5.3
# add route to the remote BGP peer's loopback address
/ip route add dst-address=10.5.5.2/32 gateway=10.2.2.2
```
Results
The output of/ip route printnow is interesting enough to deserve detailed observation.
```
[admin@PE2] /ip route> print
Flags: X - disabled, A - active, D - dynamic,
C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme,
B - blackhole, U - unreachable, P - prohibit
# DST-ADDRESS PREF-SRC GATEWAY DISTANCE
0 ADb 10.1.1.0/24 10.5.5.2 recurs... 20
1 ADC 10.3.3.0/24 10.3.3.3 ether2 0
2 ADb 10.4.4.0/24 20
3 ADb 10.1.1.0/24 10.5.5.2 recurs... 20
4 ADb 10.3.3.0/24 20
5 ADC 10.4.4.0/24 10.4.4.3 ether3 0
6 ADC 10.2.2.0/24 10.2.2.3 ether1 0
7 A S 10.5.5.2/32 10.2.2.2 reacha... 1
8 ADC 10.5.5.3/32 10.5.5.3 lobridge 0
```
The route 10.1.1.0/24 was received from a remote BGP peer and is installed in both VRF routing tables.
The routes 10.3.3.0/24 and 10.4.4.0/24 are also installed in both VRF routing tables. Each is a connected route in one table and a BGP route in another table. This has nothing to do with their being advertised via BGP. They are simply being "advertised" to the local VPNv4 route table and locally reimported after that. Import and exportroute-targetsdetermine in which tables they will end up.
This can be deduced from its attributes - they don't have the usual BGP properties. (Route 10.4.4.0/24.)
```
[admin@PE2] /routing/route> print detail where routing-table=cust-one
...
```
# References
RFC 4364: BGP/MPLS IP Virtual Private Networks (VPNs)
MPLS Fundamentals, chapter 7,Luc De Ghein, Cisco Press 2006