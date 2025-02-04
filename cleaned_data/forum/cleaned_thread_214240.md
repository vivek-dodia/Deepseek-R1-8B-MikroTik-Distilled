# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 214240

# Discussion

## Initial Question
Author: Mon Jan 27, 2025 12:15 pm
``` Flags: X - disabled, I - invalid; D - dynamic 0 ;;; WAN (Internet) chain=srcnat action=masquerade out-interface-list=WAN log=no log-prefix="" 1 ;;; PF: Caddy HTTP chain=dstnat action=dst-nat to-addresses=10.1.5.2 to-ports=80 protocol=tcp dst-address-list=public-ip dst-port=80 log=no log-prefix="" 2 ;;; PF: Caddy HTTPS chain=dstnat action=dst-nat to-addresses=10.1.5.2 to-ports=443 protocol=tcp dst-address-list=public-ip dst-port=443 log=no log-prefix="" ``` ``` public-ip ``` Hello, I have the following NAT/Port Forwarding rules and everything works fine when Cloudflare resolves my domain to my public ip. If I route my traffic through Cloudflare proxies, so no more forwarding the traffic directly to my public ip but instead using Cloudflare IPs, I cannot longer reach my network.
```
The
```

```
address list is just resolving my dynamic ip from my domain (that has a ddns updater).I put that to avoid Hairpin-NAT (because I still don't know how to implement it properly) and that's probably the cause of my problem due the NAT rules seeing that the IP of the request is from an address different from my public one.How can I implement Hairpin-NAT in an easy way and solve my problem?


---
```

## Response 1
Author: [SOLVED]Mon Jan 27, 2025 8:20 pm
``` public-ip ``` ``` In. Interface List ``` I've removed the
```
address list and set the
```

```
to my WAN and now it seems to work!
```