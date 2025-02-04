# Thread Information
Title: Thread-1123458
Section: RouterOS
Thread ID: 1123458

# Discussion

## Initial Question
hello, I have the following configuration:3 VLANs in the same bridge: Home, IOT, Guest, with 3 respective networks 10.0.20.0/24, 10.0.30.0/24, 10.0.10.0/24right now I have the following firewall rules that I need to access HA and make HA accessible from an host outside the mikrotik nets:add action=masquerade chain=srcnat ipsec-policy=out, none out-interface-list=WANadd action=dst-nat chain=dstnat comment=HA dst-port=7171 in-interface-list=WAN protocol=tcp to-addresses=10.0.30.214 to-ports=7171add action=dst-nat chain=dstnat comment="Allarme (UDP)" dst-port=3061 in-interface-list=WAN protocol=udp to-addresses=10.0.30.214 to-ports=3061As you can see I can connect from any host in VLAN Home to any host in VLAN IOT and vice-versa. Keeping in mind that I have Home Assistant, Pihole and a couple of other things in VLAN IOT that I need to access from VLAN Home, how can I make sure that only certain hosts in Home VLAN can access to hosts in IOT on given ports only?thanks in advance, sw ---

## Response 1
Typically one only puts allow rules for specific traffic between vlans needed.Then at the end of the forward chain simply putadd chain=forward action=drop comment="drop all else".Firewall rules are designed to stop layer3 traffic, so by port does not really apply. ---

## Response 2
I don't get what do you mean with "Firewall rules are designed to stop layer3 traffic, so by port does not really apply."so if I add, for exampleadd action=accept chain=forward in-interface=Home dst-address=10.0.30.21 dst-port=53 protocol=udpadd action=accept chain=forward in-interface=Home dst-address=10.0.30.21 dst-port=53 protocol=tcpadd chain=forward action=drop comment="drop all else"does it mean that Home VLAN can access the ip 10.0.30.21 in IOT VLAN on port 53 (my dns)? ---

## Response 3
hahah, I thought you meant etherport ...............Allowing all users to your pi server is perfectly legit. ---

## Response 4
so, returning back to the original question, I can implement the firewall like:
```
addaction=accept chain=forwardin-interface=Homedst-address=$HA_IP dst-port=$HA_port protocol=tcpaddaction=accept chain=forwardin-interface=Homedst-address=$Pihole_IP dst-port=53protocol=udpaddaction=accept chain=forwardin-interface=Homedst-address=$Pihole_ip dst-port=53protocol=tcpaddaction=accept chain=forwardin-interface=Homedst-address=$NAS_ip dst-port=$NAS_port protocol=tcp...andso onforother esceptionsfromhome vlan to iot...addchain=forward action=drop comment="drop all the rest"now I have this:
```

```
addaction=dst-nat chain=dstnat comment="Allarme (UDP)"dst-port=3061in-interface-list=WAN protocol=udp to-addresses=10.0.30.214to-ports=3061it will continue to work if it is defined before the forward action=drop rule? Or I need to add:
```

```
addaction=accept chain=forwardin-interface=WAN dst-address=10.0.30.214dst-port=3061protocol=udpand also the Home, Guest and IOT VLANs are still able to connect to internet?

---
```

## Response 5
The ONLY rule needed to allow port forwarding, required in the forward chain, and putting just before the drop all rule is fine.add chain=forward action=accept comment="port forwarding" connection-nat-state=dstnatSince MT decided not to provide zerotrust cloudflare in an options package as part of RoS ( which removes port exposure on the www )your best options area. at least try to put source address list on each dstnat rule to limit external access ( most users have fixed wanip or at least can get a free dyndns url for the WANIP which you can use )b. if you have a public IP get users to come in on wireguard vpn giving access to just your serversc. if you dont have a public IP rent a cloud server and get a CHR license and have people VPN through the CHR.d. consider using zerotier to provide access to your servers...... ---