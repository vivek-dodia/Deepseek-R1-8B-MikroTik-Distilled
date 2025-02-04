# Thread Information
Title: Thread-1115859
Section: RouterOS
Thread ID: 1115859

# Discussion

## Initial Question
Since v7.16.2 already test in 7.17rc2The IPv6 Advertisement are buggy.After sending a Router Advertisment ICMPv6 Type 134. The Default Route is set.After a few seconds (10 - 60) the default route disappears on the clients.With Wireshark i see then a duplicate Neighbor Advertisement from the Mikrotik. One with router bit set and without the router bit.
```
10.000000fe80::1ff02::1ICMPv6142RouterAdvertisementfrom52:54:00:40:44:8b3320.030562fe80::fefb:a4d0:5cfa:16a7fe80::1ICMPv686NeighborSolicitationforfe80::1from52:54:00:2b:d9:c83420.030922fe80::1fe80::fefb:a4d0:5cfa:16a7ICMPv678NeighborAdvertisementfe80::1(sol)3520.030922fe80::1fe80::fefb:a4d0:5cfa:16a7ICMPv678NeighborAdvertisementfe80::1(rtr,sol)8080.030469fe80::fefb:a4d0:5cfa:16a7fe80::1ICMPv686NeighborSolicitationforfe80::1from52:54:00:2b:d9:c88180.030908fe80::1fe80::fefb:a4d0:5cfa:16a7ICMPv678NeighborAdvertisementfe80::1(sol)8280.030908fe80::1fe80::fefb:a4d0:5cfa:16a7ICMPv678NeighborAdvertisementfe80::1(rtr,sol)9090.337640fe80::1ff02::1ICMPv6142RouterAdvertisementfrom52:54:00:40:44:8b119140.030428fe80::fefb:a4d0:5cfa:16a7fe80::1ICMPv686NeighborSolicitationforfe80::1from52:54:00:2b:d9:c8120140.030858fe80::1fe80::fefb:a4d0:5cfa:16a7ICMPv678NeighborAdvertisementfe80::1(sol)121140.030858fe80::1fe80::fefb:a4d0:5cfa:16a7ICMPv678NeighborAdvertisementfe80::1(rtr,sol)129157.862610fe80::1ff02::1ICMPv6142RouterAdvertisementfrom52:54:00:40:44:8b169200.030409fe80::fefb:a4d0:5cfa:16a7fe80::1ICMPv686NeighborSolicitationforfe80::1from52:54:00:2b:d9:c8170200.030795fe80::1fe80::fefb:a4d0:5cfa:16a7ICMPv678NeighborAdvertisementfe80::1(sol)171200.030795fe80::1fe80::fefb:a4d0:5cfa:16a7ICMPv678NeighborAdvertisementfe80::1(rtr,sol)192229.030445fe80::fefb:a4d0:5cfa:16a7fe80::1ICMPv686NeighborSolicitationforfe80::1from52:54:00:2b:d9:c8193229.030871fe80::1fe80::fefb:a4d0:5cfa:16a7ICMPv678NeighborAdvertisementfe80::1(sol)194229.030871fe80::1fe80::fefb:a4d0:5cfa:16a7ICMPv678NeighborAdvertisementfe80::1(rtr,sol)202250.030464fe80::fefb:a4d0:5cfa:16a7fe80::1ICMPv686NeighborSolicitationforfe80::1from52:54:00:2b:d9:c8203250.031038fe80::1fe80::fefb:a4d0:5cfa:16a7ICMPv678NeighborAdvertisementfe80::1(rtr,sol)204250.031629fe80::1fe80::fefb:a4d0:5cfa:16a7ICMPv678NeighborAdvertisementfe80::1(sol)205250.225836fe80::1ff02::1ICMPv6142RouterAdvertisementfrom52:54:00:40:44:8b

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