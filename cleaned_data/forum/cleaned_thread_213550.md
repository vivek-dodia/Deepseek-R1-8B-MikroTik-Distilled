# Thread Information
Title: Thread-213550
Section: RouterOS
Thread ID: 213550

# Discussion

## Initial Question
This is my IPv6 config:
```
[admin@fw-xxx0-0]>/ipv6export# 2024-12-27 22:08:31 by RouterOS 7.14.3# software id = JLI2-LN5C## model = CCR1009-8G-1S-1S+# serial number = xxx/ipv6 addressaddaddress=::90from-pool=fiber6interface=vlan90/ipv6 dhcp-clientaddadd-default-route=yesinterface=wan10 pool-name=fiber6 pool-prefix-length=48request=address,prefix \use-peer-dns=no/ipv6 firewall filteraddaction=accept chain=input comment="allow established and related"connection-state=established,relatedaddaction=accept chain=input comment="accept ICMPv6"protocol=icmpv6addaction=accept chain=input comment="defconf: accept UDP traceroute"port=33434-33534protocol=udpaddaction=accept chain=input comment="accept DHCPv6-Client prefix delegation."dst-port=546protocol=udp \
    src-address=fe80::/16addaction=accept chain=input comment="allow allowed addresses"disabled=yes src-address-list=allowedaddaction=drop chain=inputaddaction=accept chain=forward comment=established,related connection-state=established,relatedaddaction=drop chain=forward comment=invalid connection-state=invalid log=yes log-prefix=ipv6,invalidaddaction=accept chain=forward comment=icmpv6 protocol=icmpv6addaction=accept chain=forward comment="local network"in-interface=!wan10addaction=drop chain=forward log-prefix=IPV6This is what my computer interface gets:
```

```
3:wlp3s0:<BROADCAST,MULTICAST,UP,LOWER_UP>mtu1500qdisc noqueue state UPgroupdefaultqlen1000link/ether04:cf:4b:1e:xx:xx brd ff:ff:ff:ff:ff:ff
    altname wlx04cf4b1e412d
    inet172.16.90.117/24brd172.16.90.255scopeglobaldynamicnoprefixroute wlp3s0
       valid_lft1186secpreferred_lft1186secinet62a02:xxxx:xxxx:0:7e4b:266:xxxx:xxxx/64scopeglobaldynamicnoprefixroute 
       valid_lft2591866secpreferred_lft604666secinet6 fe80::17fc:d894:xxxx:xxxx/64scope link noprefixroute 
       valid_lft forever preferred_lft foreverAny idea why it is in :0: instead of :90: as specified in the Mikrotik config?

---
```

## Response 1
address=::90 from-pool=fiber6specifies a local host address of0000:0000:0000:0090with a prefix from the pool. There is a longstanding gripe that you can't provide a prefix hint, e.g.::90:0:0:0:1 ---