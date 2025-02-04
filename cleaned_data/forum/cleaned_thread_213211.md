# Thread Information
Title: Thread-213211
Section: RouterOS
Thread ID: 213211

# Discussion

## Initial Question
Since v7.16.2 already test in 7.17rc2The IPv6 Advertisement are buggy.After sending a Router Advertisment ICMPv6 Type 134. The Default Route is set.After a few seconds (10 - 60) the default route disappears on the clients.With Wireshark i see then a duplicate Neighbor Advertisement from the Mikrotik. One with router bit set and without the router bit.
```
1	0.000000	fe80::1		ff02::1			ICMPv6	142	Router Advertisement from 52:54:00:40:44:8b
33	20.030562	fe80::fefb:a4d0:5cfa:16a7	fe80::1	ICMPv6	86	Neighbor Solicitation for fe80::1 from 52:54:00:2b:d9:c8
34	20.030922	fe80::1	fe80::fefb:a4d0:5cfa:16a7	ICMPv6	78	Neighbor Advertisement fe80::1 (sol)
35	20.030922	fe80::1	fe80::fefb:a4d0:5cfa:16a7	ICMPv6	78	Neighbor Advertisement fe80::1 (rtr, sol)
80	80.030469	fe80::fefb:a4d0:5cfa:16a7	fe80::1	ICMPv6	86	Neighbor Solicitation for fe80::1 from 52:54:00:2b:d9:c8
81	80.030908	fe80::1	fe80::fefb:a4d0:5cfa:16a7	ICMPv6	78	Neighbor Advertisement fe80::1 (sol)
82	80.030908	fe80::1	fe80::fefb:a4d0:5cfa:16a7	ICMPv6	78	Neighbor Advertisement fe80::1 (rtr, sol)
90	90.337640	fe80::1		ff02::1			ICMPv6	142	Router Advertisement from 52:54:00:40:44:8b
119	140.030428	fe80::fefb:a4d0:5cfa:16a7	fe80::1	ICMPv6	86	Neighbor Solicitation for fe80::1 from 52:54:00:2b:d9:c8
120	140.030858	fe80::1	fe80::fefb:a4d0:5cfa:16a7	ICMPv6	78	Neighbor Advertisement fe80::1 (sol)
121	140.030858	fe80::1	fe80::fefb:a4d0:5cfa:16a7	ICMPv6	78	Neighbor Advertisement fe80::1 (rtr, sol)
129	157.862610	fe80::1		ff02::1			ICMPv6	142	Router Advertisement from 52:54:00:40:44:8b
169	200.030409	fe80::fefb:a4d0:5cfa:16a7	fe80::1	ICMPv6	86	Neighbor Solicitation for fe80::1 from 52:54:00:2b:d9:c8
170	200.030795	fe80::1	fe80::fefb:a4d0:5cfa:16a7	ICMPv6	78	Neighbor Advertisement fe80::1 (sol)
171	200.030795	fe80::1	fe80::fefb:a4d0:5cfa:16a7	ICMPv6	78	Neighbor Advertisement fe80::1 (rtr, sol)
192	229.030445	fe80::fefb:a4d0:5cfa:16a7	fe80::1	ICMPv6	86	Neighbor Solicitation for fe80::1 from 52:54:00:2b:d9:c8
193	229.030871	fe80::1	fe80::fefb:a4d0:5cfa:16a7	ICMPv6	78	Neighbor Advertisement fe80::1 (sol)
194	229.030871	fe80::1	fe80::fefb:a4d0:5cfa:16a7	ICMPv6	78	Neighbor Advertisement fe80::1 (rtr, sol)
202	250.030464	fe80::fefb:a4d0:5cfa:16a7	fe80::1	ICMPv6	86	Neighbor Solicitation for fe80::1 from 52:54:00:2b:d9:c8
203	250.031038	fe80::1	fe80::fefb:a4d0:5cfa:16a7	ICMPv6	78	Neighbor Advertisement fe80::1 (rtr, sol)
204	250.031629	fe80::1	fe80::fefb:a4d0:5cfa:16a7	ICMPv6	78	Neighbor Advertisement fe80::1 (sol)
205	250.225836	fe80::1		ff02::1			ICMPv6	142	Router Advertisement from 52:54:00:40:44:8b

---
```

## Response 1
Thanks for finding this.. has been driving me nuts.. I've had to hardcode the gateway on all the windows machines. Linux seems to cope with it. It's present in 7.16 as well. ---

## Response 2
I also struggled with this for a while, but tonight I finally discovered the issue: the RA Lifetime must be set to a value greater than 0; otherwise, the gateway (aka router) will immediately disappear. This might not technically be a bug, but RouterOS should ideally have a minimum default value.iShot_2024-12-15_03.11.41.png ---

## Response 3
but RouterOS should ideally have a minimum default value.But the default value is 30 minutes. If you create a new ND entry in Winbox, the 1800s value is prefilled. Also, both this default value and the meaning of RA Lifetime = 0 are documented:https://help.mikrotik.com/docs/spaces/R ... Propertiesra-lifetime (none | time; Default: 30m) Sets the RA lifetime. A Lifetime of 0 indicates that the router is not a default router. (see Section 6.2.3 of RFC 4861) ---

## Response 4
You can use Wireshark to capture packets, with the filter set toicmpv6.type == 134. In the latest version7.17rc3, the current results are as expected. ---

## Response 5
It is not the RA-Lifetime. This ist automatic set to 1800.This is on all windows clients.Linux clients can handle this, but not all.The Bug is also in v7.17.rc3 .The Problem is the Neighbor Advertisement without the Router Bit.This deletes the default Route, when it comes from the default gateway ip. ---