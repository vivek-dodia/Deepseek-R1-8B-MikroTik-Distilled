# Thread Information
Title: Thread-214080
Section: RouterOS
Thread ID: 214080

# Discussion

## Initial Question
1) Is there a plan to add this functionality to RouterOS?I know that by default the DHCPv6 request from the client does not contain the MAC address, but DUID. I have dual boot on few computers and when people boot Ubuntu, the DUID is different from Windows... painI played with dhcpy6d and it works great. But the problem is that I have to have X virtual interfaces on the server - to each VLAN.Next, I have one more question:2) If I get a prefix e.g. "fd3d540f::/48" from my ISP via a DHCPv6 client, I can't create my own IPv6 pool e.g. "fd3d540f:ffff::/64" - it prints an error "prefix of two pools cannot overlap!". How can this be solved? Thank you ---

## Response 1
2) If I get a prefix e.g. "fd3d540f::/48" from my ISP via a DHCPv6 client, I can't create my own IPv6 pool e.g. "fd3d540f:ffff::/64" - it prints an error "prefix of two pools cannot overlap!". How can this be solved? Thank youPD creates a dynamic pool that follows last delegation; allocate addresses from that dynamic pool. ---

## Response 2
That's not possible. I need to create /64 pools and assign addresses from them to clients within the VLAN. ---

## Response 3
I have a /60 delegation from Comcast:
```
[admin@c53uig] > /ipv6/pool/print detail without-paging
Flags: D - dynamic
 0 D name="Comcast" prefix=2601:642:xxxx:xxx0::/60 prefix-length=64 expires-after=3d13h41m4sAssign a /64 to four (4) VLAN:
```

```
/ipv6/address/add interface=vlan20 address=::1/64 from-pool=Comcast no-dad=yes advertise=yes
/ipv6/address/add interface=vlan21 address=::1/64 from-pool=Comcast no-dad=yes advertise=yes
/ipv6/address/add interface=vlan22 address=::1/64 from-pool=Comcast no-dad=yes advertise=yes
/ipv6/address/add interface=vlan23 address=::1/64 from-pool=Comcast no-dad=yes advertise=yes

---
```

## Response 4
This is how I currently have it as well, however I would like to convert it to DHCPv6 and it is not possible there. ---

## Response 5
DHCPv6 address assignment is new in v7.17, previous versions only supported prefix delegation, so there may be some rough edges to the implementation.In particular there doesn't appear to be any way to create an address delegation pool from the pool acquired from a DHCPv6 client PD request, suggest you open a support ticket with Mikrotik explaining the missing functionality.Note this only makes sense if the ISP-provided addresses are static. If they are dynamic, and change for whatever reason, any addresses you have handed out though DHCPv6 address assignment cannot be invalidated - the device using the address will continue to do so, and not have working IPv6, until it next attempts to renew at which point it will be given a new address. ---

## Response 6
Excerpt from RouterOS documenation:https://help.mikrotik.com/docs/spaces/R ... CPv6ServerRouterOS DHCPv6 server can only delegate IPv6 prefixes, not addresses.I can't say I fully understand but it does raise concerns here. ---

## Response 7
That certainly used to be the case, however there is now a section in the documentation specifically discussing address delegationhttps://help.mikrotik.com/docs/spaces/R ... delegation ---