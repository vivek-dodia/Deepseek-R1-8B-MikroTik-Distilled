# Thread Information
Title: Thread-213901
Section: RouterOS
Thread ID: 213901

# Discussion

## Initial Question
I've got a RB5009 and two VLANs. I've had IPv6 working fine for months on it. I request a /60 from my ISP and each vlan gets a /64 off of that /60. Lately, I've noticed that devices take a while to pick up an IPv6 address when connecting to either VLAN. It seems to take anywhere from 30 seconds to a few minutes. It didn't do this on previous versions of the router firmware. I am pretty sure it's new in 7.16.2.I ran Torch on either interface to capture traffic with a destination address of ff02::/16, which as I understand it is the IPv6 multicast address that devices should send a solicitation to to get a prefix. I see a single packet show up in Torch at the exact time the IPv6 address appears on the device. This tells me that the device is sending a router solicit, but it is just waiting a while after connecting to do so. Is that right? It happens on iPad, iPhone, and Windows 11. But I have neighbor discovery set to 30s-3m, which matches pretty closely with the timing I'm seeing it takes to get an IPv6 address. So maybe somehow the devices aren't sending the solicitation and are just waiting for the multicast RA?Does anyone have an idea of why it takes so long for devices to pick up an IPv6 address? I created an accept all firewall rule from both VLANs on the input chain, so I'm sure it isn't a firewall issue. Some config which might be useful:
```
/ipv6 nd
set [ find default=yes ] advertise-dns=no interface=vlan-lan ra-interval=30s-3m \
    ra-lifetime=10m
add advertise-dns=no interface=vlan-guest ra-interval=30s-3m ra-lifetime=10m
/ipv6 nd prefix default
set preferred-lifetime=10m valid-lifetime=10m

---
```

## Response 1
I'm having some issue too, with the same router and IPv6 on 7.16.2I got IPs from my prefix immediatly but I lost IPv6 funtionality. I can see packet from my client to router increase the match counter on firewall by I get no response at all.I'll try to downgrade to 7.16.1 ---

## Response 2
If you have enabled IGMP Snooping on the bridge, try to turn it off. It's still not compatible with the multicast traffic needed for IPv6 (even in 7.17rc7 with the supposed workaround). ---

## Response 3
If you have enabled IGMP Snooping on the bridge, try to turn it off. It's still not compatible with the multicast traffic needed for IPv6 (even in 7.17rc7 with the supposed workaround).That does indeed seem to fix it! ---