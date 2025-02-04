# Document Information
Title: /routing/route
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/59965493/routing+route,

# Content
A read-only table that listsroutes from all the address families as well as all filtered routes with all possible route attributes.
Default example output of the table with various route types:
```
[admin@MikroTik] /routing/route> print
Flags: A - ACTIVE; c, s, a, l, y - COPY; H - HW-OFFLOADED
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
DST-ADDRESS                 GATEWAY           AFI   D  SCOPE  TA  IMMEDIATE-GW
lH 10.0.0.0/8                                    ip4   0
;;; defconf
As  10.0.0.0/8                  10.155.130.1      ip4   1     30  10  10.155.130.1%ether1
lH 10.155.130.0/25                               ip4   0
Ac  10.155.130.0/25             ether1            ip4   0     10      ether1
aH 10.155.130.12/32                              ip4   0
lH 111.13.0.0/24                                 ip4   0
Ac  111.13.0.0/24               ether2            ip4   0     10      ether2
aH 111.13.0.1/32                                 ip4   0
Ac  111.111.111.2/32            loopback@vrfTest  ip4   0     10      loopback
Ac  2111:4::/64                 ether2            ip6   0     10      ether2
Ac  fe80::%ether1/64            ether1            ip6   0     10      ether1
Ac  fe80::%ether2/64            ether2            ip6   0     10      ether2
Ac  fe80::%ether3/64            ether3            ip6   0     10      ether3
Ac  fe80::%ether4/64            ether4            ip6   0     10      ether4
Ac  3333::2/128                 loopback@vrfTest  ip6   0     10      loopback
Ac  fe80::%loopback/64          loopback@vrfTest  ip6   0     10      loopback
Ay  111.111.111.2/32&65530:100  loopback@vrfTest  vpn4  0     10   5  loopback
Ay  3333::2/128&65530:100       loopback@vrfTest  vpn6  0     10   5  loopback
A H ether1                                        link  0
A H ether2                                        link  0
A H ether3                                        link  0
A H ether4                                        link  0
A H loopback                                      link  0
```
Detailed example output with some BGP, OSPF, and other routes:
```
[admin@MikroTik] /routing/route> print detail
Flags: X - disabled, F - filtered, U - unreachable, A - active;
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, a - ldp-address, l - ldp-mapping, y - copy; H - hw-offloaded;
+ - ecmp, B - blackhole
o   afi=ip4 contribution=best-candidate dst-address=0.0.0.0/0 routing-table=main gateway=10.155.101.1%ether1 immediate-gw=10.155.101.1%ether1
distance=110 scope=20 target-scope=10 belongs-to="OSPF route"
ospf.metric=2 .tag=111 .type=ext-type-1
debug.fwp-ptr=0x203425A0
Ad + afi=ip4 contribution=active dst-address=0.0.0.0/0 routing-table=main pref-src="" gateway=10.155.101.1 immediate-gw=10.155.101.1%ether1
distance=1 scope=30 target-scope=10 vrf-interface=ether1 belongs-to="DHCP route"
debug.fwp-ptr=0x20342060
As + afi=ip4 contribution=active dst-address=0.0.0.0/0 routing-table=main pref-src="" gateway=10.155.101.1 immediate-gw=10.155.101.1%ether1
distance=1 scope=30 target-scope=10 belongs-to="Static route"
debug.fwp-ptr=0x20342060
Fb   afi=ip4 contribution=filtered dst-address=1.0.0.0/24 routing-table=main gateway=10.155.101.1 immediate-gw=10.155.101.1%ether1 distance=20
scope=40 target-scope=10 belongs-to="BGP IP routes from 10.155.101.217" rpki=valid
bgp.peer-cache-id=*B000002 .aggregator="13335:172.68.180.1" .as-path="65530,100,9002,13335" .atomic-aggregate=yes .origin=igp
debug.fwp-ptr=0x20342960
```
Property | Description
----------------------
active(yes | no) | A flag indicates whether the route is elected as Active and eligible to be added to the FIB.
afi(ip4 | ip6 | link) | Address family this route belongs to.
belongs-to(string) | Descriptive info showing from where the route was received.
bgp(yes | no) | A flag indicates whether this route was added by theBGPprotocol.
bgp -a group of parameters associated with theBGPprotocol
| .as-path(string) | value of the AS_PATHBGPattribute
| .aggregator(string) |
| .atomic-aggregate(yes | no) |
| .cluster-list(string) |
| .communities(string) | value of the COMMUNITIES BGP attribute
| .ext-communities(string) | value of the EXTENDED_COMMUNITIES BGP attribute
| .igp-metric(string) | value of the IGP_METRIC BGP attribute
| .large-communities(string) | value of the LARGE_COMMUNITIES BGP attribute
| .local-pref(string) | value of the LOCAL_PREF BGP attribute
| .med(string) | value of the MED BGP attribute
| .nexthop(string) |
| .origin(string) |
| .originator-id(string) |
| .out-nexthop(string) |
| .peer-cache-id(string) | The ID of theBGPsession that installed the route. See/routing/bgp/sessionmenu.
| .unknown(string) | hex blob of unknownBGPattributes
| .weight(string) |
blackhole(yes | no) | A flag indicates whether it is a blackhole route
check-gateway(ping | arp | bfd) | Currently used check-gateway option.
comment(string) |
connect(yes | no) | A flag indicates whether it is a connected network route.
contribution(string) | Shows the route status contributing to the election process, e.g "filtered, active, candidate"
copy(yes | no) | A flag indicates a copy of the route to be redistributed as the L3VPN route. VPNv4/6 related attributes are attached to this "copy" route.
create-time(string) |
debug -a group of debugging parameters
|  |
dhcp(yes | no) | A flag indicates whether the route was added by the DHCP service.
disabled(yes | no) | A flag indicates whether the route is disabled.
distance(integer) |
dst-address(prefix) | Route destination.
ecmp(yes | no) | A flag indicates whether the route is added as an Equal-Cost Multi-Path route in the FIB.Read more>>
filtered(yes | no) | A flag indicates whether the route was filtered by routing filters and excluded from being used as the best route.
gateway(string) | Configured gateway, for the actually resolved gateway, seeimmediate-gwparameter.
hw-offloaded(yes | no) | Indicates whether the route is eligible to be hardware offloaded on supported hardware.
immediate-gw(string) | Shows actual (resolved) gateway and interface that will be used for packet forwarding. Displayed in format[ip%interface].
label(integer) |
ldp-address(yes | no) | A flag indicates whether the route entry is an LDP address.
ldp-mapping(yes | no) | A flag indicates whether the route entry is the LDP mapping
ldp- a group of parameters associated with the LDP protocol
| .label(integer) | LDP mapped MPLS label.
| .peer-id() |
local-address(IP) | Local IP address of the connected network.
modem(yes | no) | A flag indicates whether the route is added by the LTE or 3g modems.
mpls- group of generic parameters associated with the MPLS
| .in-label() | Mapped MPLS ingress label
| .labels() |
| .out-label() | Mapped MPLS egress label
nexthop-id() |
ospf(yes | no) | A flag indicates whether the route was added by theOSPFrouting protocol.
ospf- group of parameters associated with the OSPF protocol
| .metric(integer) |
| .type(string) |
pref-src() |
received-from() |
rip(yes | no) | A flag indicates whether the route was added by the RIP routing protocol
rip- group of parameters associated with the RIP protocol
| .metric() |
| .route-tag() |
route-cost() |
routing-table() | Routing table this route belongs to.
rpki(valid | invalid | unknown) | Current status of the prefix from theRPKIvalidation process.
scope(integer) | Scope used in the next-hop lookup process.Read more>>
static(yes | no) | A flag indicates statically added routes.
target-scope(integer) | Target scope used in next-hop lookup process.Read more>>
te-tunnel-id() | Traffic Engineering tunnel ID
total-cost() |
unreachable(yes | no) | A flag indicates whether the route next-hop is unreachable.
update-time() |
| ve-block-offset |
| ve-block-size |
| ve-id |
vpn(yes | no) | A flag indicates whether the route was added by one of the VPN protocols (PPPoE, L2TP, SSTP, etc.)
vrf-interface() | Internal use only parameter which allows identifying to which VRF route should be added. Used by services that add routes dynamically, for example, DHCP client. Shown for debugging purposes.
```
/routing/bgp/session
```
```
immediate-gw
```
```
[ip%interface]
```