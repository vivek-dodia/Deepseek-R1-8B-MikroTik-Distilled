---
title: IPv6 PD over PPP
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/132350040/IPv6+PD+over+PPP,
crawled_date: 2025-02-02T21:13:13.588466
section: mikrotik_docs
type: documentation
---

* 1Summary1.1Configuration1.2Server1.3Client1.4Testing status
* 1.1Configuration
* 1.2Server
* 1.3Client
* 1.4Testing status
# Summary
This example demonstrates how to set up PPPoE server and client to use IPv6 Prefix Delegation.
IPv6 Prefixes can be delegated over PPP interfaces. When client connects, PPP will automatically add dynamicDHCPv6-PD server. This allows to run DHCPv6 client on PPP interfaces.
## Configuration
## Server
dhcpv6-pd-pool parameter under PPP Profiles is used to enable PPP-PD. PPP will use specifiedIPv6 poolto create a dynamic DHCP server.
So first step is to add IPv6 pool:
```
/ipv6 pool
add name=myPool prefix=2001:db8:7501:ff00::/60 prefix-length=62
```
Now we can configure PPP profile and add PPPoE server
```
/ppp profile set default dhcpv6-pd-pool=myPool
/interface pppoe-server server 
add service-name=test interface=ether1
```
## Client
On client side we need to set up PPPoE client interface and run DHCP client on it.
```
/interface pppoe-client
add name=client-test interface=ether1 user=a1 service-name=test
/ipv6 dhcp-client 
add interface=client-test pool-name=ppp-test pool-prefix-length=64
```
## Testing status
On server side check if dynamic DHCP server is added and prefix is bound to specific client:
```
[admin@RB1100] /ipv6 dhcp-server> print 
Flags: D - dynamic, X - disabled, I - invalid 
 #    NAME              INTERFACE            ADDRESS-POOL            LEASE-TIME
 0 D  <pppoe-a1>        <pppoe-a1>           myPool                  3d        
[admin@RB1100] /ipv6 dhcp-server binding> print 
Flags: X - disabled, D - dynamic 
 #   ADDRESS                                        DU       IAID SER.. STATUS 
 1 D 2001:db8:7501:ff04::/62                                  247 <pp.. bound
```
On client side, check if DHCP client is bound and pool is added:
```
[admin@x86-test] /ipv6 dhcp-client> print 
Flags: D - dynamic, X - disabled, I - invalid 
 #    INTERFACE           STATUS        PREFIX                            EXPIRES-AFTER  
0    client-test          bound         2001:db8:7501:ff04::/62           2d23h18m17s  
[admin@x86-test] /ipv6 pool> print 
Flags: D - dynamic 
 #   NAME                        PREFIX                                   PREFIX-LENGTH
 0 D ppp-test                    2001:db8:7501:ff04::/62                             64
```