# Thread Information
Title: Thread-1115847
Section: RouterOS
Thread ID: 1115847

# Discussion

## Initial Question
Hi, today I had a bit of a nightmare. Coffee shop lost Internet. I tried to use a 4G stick that I have used before at other shops, although not for a while. I usually put them in the Draytek router, but also should work with Mikrotik.The stick is a Huawei E3372h-320.I could not get it to work in either a HEX (new Arm version, on RouterOS 7.15.x) or a Draytek Vigor 2860. The device works as a USB-NDIS ethernet. Both routers acquired a 192.168.3.x/24 IP and I was able to get to the Huawei page of the stick through the routers, however it has very few configuration options, and no Internet was available except DNS lookups worked (because the stick provided the responses, not the Internet, i.e. stick has connectivity but downstream routers don't.)The stick worked fine in my laptop, but I could not ping anywhere even from my laptop, which made it awkward to test things (for a while I thought it wasn't working but it was..).I *think* I eventually realised that the problem is that the stick was only providing Internet access over IPv6. When I disable IPv6 on my laptop, I don't have internet access.DNS lookups work, because they recurse up to the stick itself on 192.168.3.1, but traceroute, ping etc are no good from devices. At first I thought they might be blocking DNS lookups to 3rd party DNS servers, but no, seems it's IPv4 that is not working for Internet.The Draytek was apparently acquiring an IPv6 address, but still didn't work. I tried to enable DHCPv6 Client on the Mikrotik but it was just continually searching. I have basically zero knowledge of IPv6.Does anybody have any ideas? After a bad day, 1hr before closing time I went and bought a 5G router from EE and used that. ---

## Response 1
A DHCPv6 Client is not necessarily required by a host for a functioning IPv6 connection as information supplied by the upstream router via ICMPv6 is often sufficient.TBH don't see yet how is that an IPv6 or RouterOS problem. Get it to work on your laptop, then we can see what RouterOS config can match it. ---

## Response 2
My idea is that IPv6 can be made to work on the Mikrotik with that modem and SIM but that won't give you access to the whole internet as not all web sites support IPv6, so you might need to set up a tunnel to some device that has both IPv6 and IPv4 connectivity. Does it still make sense to you to debug the IPv6 on the Mikrotik with this LTE stick for future or has the issue been closed once forever using the EE 5G router? ---

## Response 3
My idea is that IPv6 can be made to work on the Mikrotik with that modem and SIM but that won't give you access to the whole internet as not all web sites support IPv6, so you might need to set up a tunnel to some device that has both IPv6 and IPv4 connectivity. Does it still make sense to you to debug the IPv6 on the Mikrotik with this LTE stick for future or has the issue been closed once forever using the EE 5G router?Well, I don't like to be defeated, and I have the stick here at home with me. I have tried a few times though and get nowhere with either DHCPv6 or SLAAC. For now I am simply trying to ping Cloudflare's ipv6 DNS server from the Mikrotik terminal. ---

## Response 4
Hehe. Did you tell the DHCPv6 client to ask for both a prefix and an address and got neither? ---

## Response 5
Hi, today I had a bit of a nightmare. Coffee shop lost Internet. I tried to use a 4G stick that I have used before at other shops, although not for a while. I usually put them in the Draytek router, but also should work with Mikrotik.The stick is a Huawei E3372h-320.Hi @carl0sI have exactly the same problem with Huawei E3372h-320. Modem is working good with PC directly, but there's no internet when it is connected to MikrotikHere is mypost:Did you have some progress with this problem? ---