# Thread Information
Title: Thread-1123106
Section: RouterOS
Thread ID: 1123106

# Discussion

## Initial Question
I have an SSTP server that I use from time to time, and I had thought IPv6 was working over it, but it appears not to be and I'm not sure what the problem is. The clients are assigned a valid IPv6 address and the router has a route in place for it. But I can't ping the router across the tunnel and I can't access IPv6 sites on the internet.
```
[david@RoutyMcRouterson]>/ipv6 poolprintFlags:D-DYNAMICColumns:NAME,PREFIX,PREFIX-LENGTH,EXPIRES-AFTER#   NAME       PREFIX                    PREFIX-LENGTH  EXPIRES-AFTER0D ipv6-pool2600:1700:7c50:3790::/606447m12s[david@RoutyMcRouterson]/ipv6>addressprintFlags:D-DYNAMIC;G-GLOBAL,L-LINK-LOCALColumns:ADDRESS,FROM-POOL,INTERFACE,ADVERTISE#    ADDRESS                       FROM-POOL  INTERFACE        ADVERTISE0G fddc::100/64wireguard1no1G2600:1700:7c50:3790::1/64ipv6-pool  vlan-lan         yes2G2600:1700:7c50:3791::1/64ipv6-pool  vlan-guest       yes3DL fe80::bec1:da6a:de90:d3aa/64wireguard1no4D::1/128lono5DL fe80::4aa9:8aff:fed0:92e3/64vlan-guestno6DL fe80::4aa9:8aff:fed0:92e3/64vlan-lanno7DL fe80::4aa9:8aff:fed0:92e3/64bridge1no8DL fe80::5a60:d8ff:fe6f:4b31/64ATTbridgeno9DL fe80::5aee:eb12:f0:4b/64<sstp-davidvpn>no
```

```
[david@RoutyMcRouterson]>/ppp profileexport/ppp profileadddns-server=10.9.0.1interface-list=LANlocal-address=10.9.0.1name=sstp remote-address=sstp-vpn remote-ipv6-prefix-pool=ipv6-pooluse-encryption=requireduse-mpls=noWhen I connect, the client shows that its IPv6 router is fe80::4e9f:9bc1:f0:4b and that its IPv6 address is 26007c50b9af:4cba:b4fc:b6a9/64, which is one of the /64s I get delegated in the /60 the ISP issues. But I can't access any IPv6 sites and I can't even ping the router at its fe80 link local address. Does anyone know what might be the problem?

---
```

## Response 1
edit: never mind. It was a firewall issue.I tried deleting the post but got HTTP 500. ---