# Thread Information
Title: Thread-212701
Section: RouterOS
Thread ID: 212701

# Discussion

## Initial Question
I contacted my ISP and they said that they give out only ::/64 IPv6 prefixes to customers. Which means I have no ability to create my own subnets in my network since IPv6 works on the 64 boundary. What are my options if I want to have 2 networks at home - my main network and guest network (for IoT devices for example)? I don't want to let my IoT devices on my main network. I also don't want to use IPv4 at all, this is a IPv6-only network. ---

## Response 1
What are my options if I want to have 2 networks at homeChange ISPRegister an ASN, rent /48 (or more) and announce with BGP via your ISPResign oneself ---

## Response 2
Without commenting on what I think of ISPs that give less than a /56 (or at least... one /60)...You can still create "subnets" of /68, for example, but all addresses must be assigned statically by DHCP and not based on MAC/EUI64.dead:beef:dead:beef:0000::/68 = dead:beef:dead:beef:0000:0000:0000:0000 ... dead:beef:dead:beefffff:ffff:ffffdead:beef:dead:beef:/68 = dead:beef:dead:beef0000:0000:0000 ... dead:beef:dead:beefffff:ffff:ffffdead:beef:dead:beef:/68 = dead:beef:dead:beef0000:0000:0000 ... dead:beef:dead:beefffff:ffff:ffffdead:beef:dead:beef:/68 = dead:beef:dead:beef0000:0000:0000 ... dead:beef:dead:beefffff:ffff:ffff[...]dead:beef:dead:beef:d000::/68 = dead:beef:dead:beef:d000:0000:0000:0000 ... dead:beef:dead:beef:dfff:ffff:ffff:ffffdead:beef:dead:beef:e000::/68 = dead:beef:dead:beef:e000:0000:0000:0000 ... dead:beef:dead:beef:efff:ffff:ffff:ffffdead:beef:dead:beef:f000::/68 = dead:beef:dead:beef:f000:0000:0000:0000 ... dead:beef:dead:beef:ffff:ffff:ffff:ffffOf course, VLANs & Co. need to be created, it's not enough to assign different IPs...Still possible use NATv6 for create internal IPv6 "subnets" and masquerade all with Router IPv6.This is needed also if ISP change often dead:beef:dead:beef:: parts, and you need to change everytime internals IPv6, or also for failover without reconfig internal IPv6 LAN...for example you can assign fd00:dead:beef:10::/64 for VLAN 10, fd00:dead:beef:20::/64 for VLAN 20, etc. all work with SLAAC and EIU64, then add a NATv6:from fd00:dead:beef:10::/64 to real IPv6 dead:beef:dead:beef::10/128from fd00:dead:beef:20::/64 to real IPv6 dead:beef:dead:beef::20/128from fd00:dead:beef:30::/64 to real IPv6 dead:beef:dead:beef::30/128and so on... ---

## Response 3
Unfortunately in case of dual stack network, using ULA instead of global v6 address makes the OS preferring IPv4 over IPv6.I didn’t know this until I needed to use fd00 addresses and found out all my clients preferred ipv4. Then I found this RFChttps://datatracker.ietf.org/doc/html/rfc6724#page-24that talks about it ---

## Response 4
Thank you for bringing this to my attention, I didn't know that...I hadn't noticed it yet...IPv4 are considered as IPv4-mapped IPv6 address...
```
Prefix            Precedence Label
::1/128           50          0    Localhost
::/0              40          1    Default unicast = Any other IPv6 not on this table
::ffff:0.0.0.0/96 35          4    IPv4-mapped IPv6 address = IPv4
2002::/16         30          2    6to4
2001::/32          5          5    Teredo tunneling
fc00::/7           3         13    Unique local address
::0.0.0.0/96       1          3    IPv4-compatible addresses (deprecated)
fec0::/10          1         11    Site-local address (deprecated)
3ffe::/16          1         12    6bone (returned)So... "simply"... no one forbid you to use internally any real global address unassigned...for example you can assign 4d00:dead:beef:10::/64 for VLAN 10, 4d00:dead:beef:20::/64 for VLAN 20, etc. all work with SLAAC and EIU64,then add a NATv6:from 4d00:dead:beef:10::/64 to real IPv6 dead:beef:dead:beef::10/128from 4d00:dead:beef:20::/64 to real IPv6 dead:beef:dead:beef::20/128from 4d00:dead:beef:30::/64 to real IPv6 dead:beef:dead:beef::30/128and so on...So, for one reason on next 20 years IPv6 are depleted and IANA assign 4d00::/12, you can change 4d with another unused block for the next 20 years....

---
```

## Response 5
Instead of using some unassigned prefix ranges, you can get a free account with Hurrricane Electric (tunnelbroker.net) and get two /64 and two /48 prefixes for yourself. No one force you to use the tunnels provided by HE, you can just use those prefixes internally within your network, and can be sure that the prefixes are not used by someone else. Unlike ULA, the prefixes are valid GUA ones and are preferred over IPv4.As for NATing when going out to the internet, I prefer netmap instead of masquerade or many src-nat rules for individual IP addresses. With one rule we can map an internal /64 or /60 prefix to the prefix assigned by the ISP to the outgoing interface. With SLAAC (including EUI64 and randomizations from privacy extension) there is almost no risks for the interface ID part (lower 64bit) of the different devices in LAN to clash. So all devices will also have individual global unicast addresses (with ISP prefix) when going out to the internet after the netmap operation. For my case, the ISP only give out dynamic IPv6 prefixes (change with each PPPoE redial) so I also have scripts (attached to DHCPv6 client) that automatically update the to-address part of the netmap rules with the new prefixes.netmap.pngMy ISP actually gives out /60 prefixes, so I still have enough /64 to assign to the individual VLANs. But I still use the HE prefixes for places where static prefixes are needed, like inside WireGuard tunnels or container bridges. ---

## Response 6
hello, contacted my ISP and they said that they give out only ::/64 IPv6 prefixes to customers. Which means I have no ability to create my own subnets in my network since IPv6 works on the 64 boundary.the isp was correct on their point of view about the /64 block. that is their block assignment boundaries - for clients.but you can divide that block to smaller ones as well - just like ipv4. let us say to some /96.the downside is that you need to have statically assign (or via dhcp6) those addresses to your clients. set the router lan interface addresses accordingly. the difference is that you don't need any NAT except specifying ipv6 gateway for each of your lan. ---

## Response 7
the isp was correct on their point of view about the /64 block. that is their block assignment boundaries - for clients.but you can divide that block to smaller ones as well - just like ipv4. let us say to some /96.the downside is that you need to have statically assign (or via dhcp6) those addresses to your clients. set the router lan interface addresses accordingly. the difference is that you don't need any NAT except specifying ipv6 gateway for each of your lan.No the ISP is not correct. Per RFC 7368https://www.rfc-editor.org/rfc/rfc7368#section-3.4.1:For a typical IPv6 homenet, it is not recommended that an ISP offers less than a /60 prefix, and it is highly preferable that the ISP offers at least a /56.Also, your solution doesn't work if OP has any Android devices at all. Android only supports SLAAC. ---

## Response 8
Instead of using some unassigned prefix ranges, you can get a free account with Hurrricane Electric (tunnelbroker.net) and get two /64 and two /48 prefixes for yourself. No one force you to use the tunnels provided by HE, you can just use those prefixes internally within your networkActually I'm currently using HE to get main IPv6 addresses as my ISP does not provide IPv6 at all (LTE connection) and I already have /48 from them.But I've never thought of using one of their 2001:470:: /64 to define an internal address to be routed elsewhere with another GUA IPv6 address.In my case, sometime, I needed to get on internet from a different IPv6 than HE's, due to geolocation issues with HE being US and I'm in Europe.So I have setup a wireguard tunnel with a CHR I have on the Cloud (but hosting provider unfortunately only offers /64 for each instance) so now I'm using one of the 2001:470: as internal address for the wireguard connection to send one of my VLAN out from my CHR instead of HE's tunnel.And so now those clients still see GUA address and prefer IPv6 again.Thanks for the hint on that one. ---

## Response 9
@cgg, No the ISP is not correct. Per RFC 7368it really depends on how you defined an isp. that rfc referring to which tier the isp belongs to, and in which country the isp operates. don't expect tier 2 or 3 isps will give you a full /48 without rent it from internet registry.probably android ipv6 support will be available in the future.hurricane only offered ipv6 blocks without underlying layer 2 link. actually a good offer if someone can tweak their own routers to tunnel to hurricane. ---

## Response 10
Well, that RFC is titled "IPv6 Home Networking Architecture Principles", not enterprise or datacenter; the ISP is expected to be the service provider for residential customers. Other than that section 1.1 of that RFC has the definition for the terminology "ISP". I see no excuses for only providing a /64 prefix even for the smallest provider. That RFC no longer recommends giving out /48, ISPs should just provide at least /60 as recommended.As for Android and DHCPv6: don't get your hopes up. The tracked issue is 12 years old and marked aswon't fix, https://issuetracker.google.com/issues/36949085?pli=1. The developers have commented multiple times there explaining why, here the last comment from Google devs from October 2023:https://issuetracker.google.com/issues/ ... comment407hurricane only offered ipv6 blocks without underlying layer 2 link. actually a good offer if someone can tweak their own routers to tunnel to hurricane.You don't have to touch their tunnel services. You just use the /48 prefix that they give you internally (and subdivide it into multiple /56, /60, /64 as you wish) like what you normally do with ULA addresses. They are GUA addresses that now are guaranteed to only be used by you and not anyone else. ---

## Response 11
you can get a free account with Hurrricane Electric (tunnelbroker.net) and get two /64 and two /48 prefixes for yourself.No one force you to use the tunnels provided by HE, you can just use those prefixes internally within your network, and can be sure that the prefixes are not used by someone else.BRAVO.Ottima idea.[Great Idea] ---

## Response 12
I didn't know that Hurricane gives a free /64. Obviously it is provided on the AS in their possession? or is it possible to register your own AS? I think that in this case perhaps a /48 is assigned ---

## Response 13
@abbi, yes you can request a /64 to hurricane - it's valid internet routable ipv6 address block - but as long as you use their tunnel service because those blocks are in their bgp as.but it is ok if you just want to use their ip internally for your lan (without going outside to the internet, which will be a little bit awkward).while the classic problem for isp given ipv6 is that you need to renumber your lan if you change your isp. almost similar to hurricane ipv6 blocks ---

## Response 14
Or simply, for internal LANs, I doubt that using4d00:dead:beef:<DECIMAL (V)LAN NUMBER>::/64cause problems on next 20 years... ---

## Response 15
But then you must also be careful because many systems maintain a list of "bogon" addresses and block them. Here is an example from my OPNsense installation: They have bogon list that is automatically and periodically fetched (currently with almost 150K entries) of all invalid and unassigned IPv6 ranges and the firewall will use them in their built-in drop rules (it's a checkbox in the settings). 4000::/2 is in the list. ---

## Response 16
My edge firewall work not on bogons, but only on allocated.Drop on output everything except my IPv6 pools, Drop on input all except allocated addresses:allocated IPv6 at 2024-11-23 codeadd address=2001:200::/23 comment=APNIC list=lista_ipv6_allocati add address=2001:400::/23 comment=ARIN list=lista_ipv6_allocati add address=2001:600::/23 comment=RIPE list=lista_ipv6_allocati add address=2001:800::/22 comment=RIPE list=lista_ipv6_allocati add address=2001:c00::/23 comment=APNIC list=lista_ipv6_allocati add address=2001:e00::/23 comment=APNIC list=lista_ipv6_allocati add address=2001:/23 comment=LACNIC list=lista_ipv6_allocati add address=2001:/22 comment=RIPE list=lista_ipv6_allocati add address=2001:/23 comment=ARIN list=lista_ipv6_allocati add address=2001:/23 comment=RIPE list=lista_ipv6_allocati add address=2001:/22 comment=RIPE list=lista_ipv6_allocati add address=2001:/19 comment=RIPE list=lista_ipv6_allocati add address=2001:4000::/23 comment=RIPE list=lista_ipv6_allocati add address=2001:4200::/23 comment=AFRINIC list=lista_ipv6_allocati add address=2001:4400::/23 comment=APNIC list=lista_ipv6_allocati add address=2001:4600::/23 comment=RIPE list=lista_ipv6_allocati add address=2001:4800::/23 comment=ARIN list=lista_ipv6_allocati add address=2001:4a00::/23 comment=RIPE list=lista_ipv6_allocati add address=2001:4c00::/23 comment=RIPE list=lista_ipv6_allocati add address=2001:5000::/20 comment=RIPE list=lista_ipv6_allocati add address=2001:8000::/19 comment=APNIC list=lista_ipv6_allocati add address=2001:a000::/20 comment=APNIC list=lista_ipv6_allocati add address=2001:b000::/20 comment=APNIC list=lista_ipv6_allocati add address=2003::/18 comment=RIPE list=lista_ipv6_allocati add address=2400::/12 comment=APNIC list=lista_ipv6_allocati add address=2600::/12 comment=ARIN list=lista_ipv6_allocati add address=2610::/23 comment=ARIN list=lista_ipv6_allocati add address=2620::/23 comment=ARIN list=lista_ipv6_allocati add address=2630::/12 comment=ARIN list=lista_ipv6_allocati add address=2800::/12 comment=LACNIC list=lista_ipv6_allocati add address=2a00::/12 comment=RIPE list=lista_ipv6_allocati add address=2a10::/12 comment=RIPE list=lista_ipv6_allocati add address=2c00::/12 comment=AFRINIC list=lista_ipv6_allocati add address=2410::/12 comment=APNIC list=lista_ipv6_allocatiLast addition: 2024-11-01 2410::/12 APNIC ---

## Response 17
rextended, My edge firewall work not on bogons, but only on allocated.well, aside from the real bogons - any legitimate ipv6 network leakage can be considered as bogons as well.but, i like this one - creating a sandboxthis is a simple and very powerful oneDrop on output everything except my IPv6 pools, Drop on input all except allocated addressesthat logic can be implemented for the @OP network. netwatch scripted:1. if gateway=lte, then dhcp=lte-pool, activate anti-bogons=use-lte-address.2. if gateway=hurricane, then dhcp=hurricane -pool, activate anti-bogons=use-hurricane-address.@OP, any ddns infrastructure could be helpful. ---

## Response 18
Unfortunately in case of dual stack network, using ULA instead of global v6 address makes the OS preferring IPv4 over IPv6.I didn’t know this until I needed to use fd00 addresses and found out all my clients preferred ipv4. Then I found this RFChttps://datatracker.ietf.org/doc/html/rfc6724#page-24that talks about itFor certain systems it is possible to address that issue, seepost #35 atNPTv6 / RFC 6296 Support?topic. ---