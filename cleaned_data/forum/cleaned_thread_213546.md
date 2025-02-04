# Thread Information
Title: Thread-213546
Section: RouterOS
Thread ID: 213546

# Discussion

## Initial Question
Hello!I have a Mikrotik RouterOS router with its LAN address 192.168.88.1. The whole home LAN is on network 192.168.88.0. Now, my camera recorder has address 192.168.88.156, and it is directly connected to the router. Now, the recorder has a few POE ports for cameras, and cameras are connected directly there (to the recorder). The recorder acts kind of like a router, having the cameras on the network 192.168.254.0 - the router's IP is 192.158.254.1.Okay, but what I want to achieve is to allow the access from my LAN to the cameras directly (because they have certain options which are available only when accessed directly, not through the NVR).What I did is the following:I connected one of the Mikrotik's ports to the NVR's LAN (so now there are 2 physical connections between NVR and router - one goes to the NVR's WAN and other one to the NVR's LAN).Once on the router's webos I can ping the NVR and all the cameras using their own LAN (so using the 192.168.254.0 network). It works! On the PC connected to the router's LAN 192.168.88.0 I can access the NVR using 192.168.254.1 address, but NOT any of the cameras.Traceroute from my PC:
```
traceroute to 192.168.254.1 (192.168.254.1), 64 hops max, 40 byte packets
 1  router.lan (192.168.88.1)  7.556 ms  2.926 ms  2.801 ms
 2  192.168.254.1 (192.168.254.1)  3.211 ms  3.094 ms  3.103 ms
```

```
traceroute to 192.168.254.2 (192.168.254.2), 64 hops max, 40 byte packets
 1  router.lan (192.168.88.1)  7.820 ms  2.997 ms  2.780 ms
 2  * * *
 3  * * *
 4  * * *Under IP / Addresses I added 192.168.254.254 address as my router's next to its primary address 192.168.88.1, both are on the same bridge. All of the router's LAN ports are grouped with one bridge (including the ports connected to the NVR's WAN and NVR's LAN).No special extra configurations, no VLANS, no firewall rules, no nothing.Could anyone give me any ideas what to do next?

---
```

## Response 1
Most probably you'll need NAT.
```
/ip/firewall/nat/add chain=srcnat src-address=192.168.88.0/24 dst-address=192.168.254.0/24 action=masquerade

---
```

## Response 2
That's it! Thank you! Works like a charm!Btw I wonder if there was any other option beside adding another physical connection between NVR's LAN and router. I don't think so since the NVR doesn't provide any access for routing tables etc. ---

## Response 3
hello mattie, I don't think so since the NVR doesn't provide any access for routing tables etc.if your nvr has wan port - it should have a default routing table to 0/0.
```
traceroute to 192.168.254.2 (192.168.254.2), 64 hops max, 40 byte packets
 1  router.lan (192.168.88.1)  7.820 ms  2.997 ms  2.780 ms
 2  * * *
 3  * * *looks like the nvr doing nat at its wan interface (on 88.x ip). I don't have any idea whether the nvr have built in firewalls - but before reaching 254.0 nvr lan network you should have a route to 254.0 in your mt router via nvr wan ip.ip route add dst add 254.0 via 88.x (nvr wan).don't forget to disable that 254.x ip on your mt router.

---
```