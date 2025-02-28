# Thread Information
Title: Thread-1121708
Section: RouterOS
Thread ID: 1121708

# Discussion

## Initial Question
Hello, Not sure if any one of you have heard of CoreTransit yet, its about a year old but they give out IP space via an L2TP service.I'm running a hAP ac^2 on 7.15.3, which is what it shipped with, I tried updating it and it messed up everything so I reverted back and installed the wireless drivers.I was curious, does anyone else have a working l2tp configuration that routes traffic to the private interface that your private network is on.So all 192.168.88.1/24 traffic goes over the "regular" network, and any traffic destined for the network thats routed over the l2tp connection is also attached to the ether5 interface..soether1 - has charter dhcpl2pt-in - (client) has assigned public ( 216.146.17.57)ether5 has 192.168.xx.1 & the public of the routed ip's (216.146.17.128/29) .I understand that I might have todo some firewall/mangle voodoo, but I tried many things and it did not work. ---

## Response 1
A network diagram as well as stating your requirements in the form "which users are part of what network and what should they be able to reach from where" would be quite helpful ---

## Response 2
Hopefully this convey's what I'm setting out todo. See attached.CoreTransit.drawio.png ---

## Response 3
I still cannot comprehend the purpose of having local and public IPs on the same interface. Kindly clarify it ---

## Response 4
So the l2tp connection rides the spectrum connection as a separate interface. The bridgeLocal interface is assigned internal and the routed from core transit. I then setup mangle rules. Those however did not work.I hope this makes sense.... ---

## Response 5
You still haven't answered my question - why do public IPs and local ones need to be on the same interface? Do you want a specific device to have a public IP? Does it need to access the internet from it? Do you want to forward the addresses to another router? ---

## Response 6
I guess I don't understand. My request seems simple it's a simple routed setup but the routed ip's are coming over a l2tp connection and the internal interface bridgeLocal gets private and public. So yes. I would like for it to handle the routed subnet on the private lan.Thanks ---

## Response 7
Wait a second... Do you just want the LAN to go out to the internet through a public WAN IP and/or the other way around? If that's the case, it could be achieved with policy routing:
```
/ip addressaddaddress=216.146.17.129/29interface=lo/routing tableaddfib name=thr_l2tp/routing ruleaddaction=lookup-only-in-table dst-address=192.168.88.0/24src-address=192.168.88.0/24table=mainaddaction=lookup-only-in-table src-address=192.168.88.0/24table=thr_l2tp/ip routeadddistance=2dst-address=0.0.0.0/0gateway=l2tp-out1adddst-address=0.0.0.0/0gateway=l2tp-out1 routing-table=thr_l2tp/ip firewall nataddaction=src-nat chain=srcnatout-interface=l2tp-out1 place-before=0to-addresses=216.146.17.129Note: The lo interface, on which the public IP is assigned, is the loopback interfaceSecond note: dst-nat rules should be used for the other way around

---
```

## Response 8
Basically whatever is coming from 192.168.88.0/24 goes out the default route. (the spectrum main dhcp'd ip)Anything that comes over the l2tp connection say 216.146.17.128/29 goes out of the route of the l2tp connection but is another subnet on the bridgeLocal interface. ---

## Response 9
Why are you classing the 192.168.88.x/24 traffic, when it should be the 216.146.17.128/29 traffic, I'm making it simple stupid - I don't understand this part.Wait a second... Do you just want the LAN to go out to the internet through a public WAN IP and/or the other way around? If that's the case, it could be achieved with policy routing:
```
/ip addressaddaddress=216.146.17.129/29interface=lo/routing tableaddfib name=thr_l2tp/routing ruleaddaction=lookup-only-in-table dst-address=192.168.88.0/24src-address=192.168.88.0/24table=mainaddaction=lookup-only-in-table src-address=192.168.88.0/24table=thr_l2tp/ip routeadddistance=2dst-address=0.0.0.0/0gateway=l2tp-out1adddst-address=0.0.0.0/0gateway=l2tp-out1 routing-table=thr_l2tp/ip firewall nataddaction=src-nat chain=srcnatout-interface=l2tp-out1 place-before=0to-addresses=216.146.17.129Note: The lo interface, on which the public IP is assigned, is the loopback interfaceSecond note: dst-nat rules should be used for the other way around

---
```

## Response 10
A few folks made me aware of this post, so thank you to all of them!!This is best done with policy-based routing.https://help.mikrotik.com/docs/spaces/R ... cy+RoutingIn the case of Core Transit we've put together an example as well.https://client.coretransit.net/knowledg ... unnel.htmlHope that help! ---

## Response 11
Basically whatever is coming from 192.168.88.0/24 goes out the default route. (the spectrum main dhcp'd ip)Anything that comes over the l2tp connection say 216.146.17.128/29 goes out of the route of the l2tp connectionbut is another subnet on the bridgeLocal interface.That's the part where it gets ununderstandable - why should a public subnet be in conjunction with a local subneton the same interface? What should be achieved through this setup? ---

## Response 12
There is nothing technically incorrect having multiple subnets on a layer 2 network, you can set a client to an address from either. The main limitation is a DHCP server can only offer dynamic addresses for one of them.That said it isn't really good practice, having each subnet in it's own layer 2 network is better, typically implemented with VLANs. And depending on the use case for the public addresses being provided over the L2TP connection it is possible to use NAT to/from them too, e.g. forward ports from each public address to multiple servers with private addresses, or source NAT multiple private addresses to each of the public addresses. ---