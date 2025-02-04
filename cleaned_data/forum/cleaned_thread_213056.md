# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213056

# Discussion

## Initial Question
Author: Wed Dec 04, 2024 7:16 pm
``` addaction=dst-nat chain=netmap dst-address=192.168.1.200to-addresses=10.1.1.20addaction=dst-nat chain=netmap dst-address=192.168.1.201to-addresses=10.1.1.20 ``` ``` addaction=netmap chain=dst-nat dst-address=192.168.1.200to-addresses=10.1.1.20addaction=netmap chain=dst-nat dst-address=192.168.1.201to-addresses=10.1.1.20 ``` ``` /ip addressaddaddress=192.168.1.1/24interface=ether1 network=192.168.1.0addaddress=10.1.1.1/24interface=ether2 network=10.1.1.0addaddress=192.168.1.200interface=ether1 network=192.168.1.0addaddress=192.168.1.201interface=ether1 network=192.168.1.0addaddress=10.1.1.1/24interface=ether3 network=10.1.1.0.../ip firewall mangleaddaction=mark-connection chain=prerouting dst-address=192.168.1.200new-connection-mark=port1addaction=mark-connection chain=prerouting dst-address=192.168.1.201new-connection-mark=port2addaction=mark-routing chain=prerouting connection-mark=port1new-routing-mark=port1 passthrough=noaddaction=mark-routing chain=prerouting connection-mark=port2new-routing-mark=port2 passthrough=no.../ip firewall nataddaction=netmap chain=dst-nat dst-address=192.168.1.200to-addresses=10.1.1.20addaction=netmap chain=dst-nat dst-address=192.168.1.201to-addresses=10.1.1.20addaction=masquerade chain=srcnatout-interface=ether2addaction=masquerade chain=srcnatout-interface=ether3.../ip routeadddistance=1dst-address=10.1.1.0/24gateway=ether2 routing-mark=port1adddistance=1dst-address=10.1.1.0/24gateway=ether3 routing-mark=port2 ``` Thank you both for your answer.I started following the first thread, and had some issues until I realized there was a small typo in the firewall nat rules, where action and chain are swapped.Once this was fixed, the solution was working as intended.The issue is here:
```
which should be:
```

```
Edit:Here is the full working config in case someone has the same issue:
```

```
---
```

## Response 1
Author: Thu Dec 05, 2024 12:13 pm
``` /ip addressaddaddress=192.168.1.1/24interface=ether1 network=192.168.1.0addaddress=10.1.1.1/24interface=ether2 network=10.1.1.0addaddress=192.168.1.200interface=ether1 network=192.168.1.0addaddress=192.168.1.201interface=ether1 network=192.168.1.0addaddress=10.1.1.1/24interface=ether3 network=10.1.1.0.../ip firewall mangleaddaction=mark-routing chain=prerouting dst-address=192.168.1.200in-interface=ether1new-routing-mark=via-ether2 passthrough=yesaddaction=mark-routing chain=prerouting dst-address=192.168.1.201in-interface=ether1new-routing-mark=via-ether3 passthrough=yes.../interfacelistaddname=DEVICES/interfacelist memberaddinterface=ether2 list=DEVICESaddinterface=ether3 list=DEVICES.../ip firewall nataddaction=dst-nat chain=dstnat dst-address=192.168.1.200-192.168.1.201in-interface=ether1 to-addresses=10.1.1.20addaction=masquerade chain=srcnatout-interface-list=DEVICES.../ip routeadddistance=1dst-address=10.1.1.0/24gateway=ether2 routing-mark=via-ether2adddistance=1dst-address=10.1.1.0/24gateway=ether3 routing-mark=via-ether3 ``` ``` /ip route>printFlags:X-disabled, A-active, D-dynamic, C-connect, S-static, r-rip, b-bgp, o-ospf, m-mme, B-blackhole, U-unreachable, P-prohibit# DST-ADDRESS PREF-SRC GATEWAY DISTANCE0A S10.1.1.0/24ether211A S10.1.1.0/24ether312ADC10.1.1.0/2410.1.1.1ether20ether33ADC192.168.1.0/24192.168.1.1ether10 ``` I checked sindy proposal and it indeed simplify the configuration a bit (less firewall rules).Here is the updated config:
```
As you pointed out, both variants with netmap and dst-nat are working in this case.Sandy explained the difference more in detail in this post >viewtopic.php?t=167814#p823606I noticed a weird behavior with both versions though:* if I remove the connection (pull the cable) on ether2, the PC will display the page of the second machine on 192.168.1.200 instead of timing out.It looks like the default dynamic route is used when the interface is not reachable.How can I prevent this ?edit: my routes are:
```

```
---
```

## Response 2
Author: Thu Dec 05, 2024 3:13 pm
What are the routes (/ip route print) at the time the machine is disconnected (pull the cable)?Very likely the routing rule (that is for "new-routing-mark=port1") that in your posted output is #0 is not anymore AS (Active, Static) but becomes just S or IS (Inactive), and either the "generic" route takes precedence or (for whatever reason) the other identical route (which should be for "new-routing-mark=port2" only) is used.I suspect the first, the router tries desperately to reach destination, but cannot say for sure.In these cases usually a blackhole rule is added with a higher distance, you would need two of them, *like*:/ip routeadd blackhole distance=2 dst-address=10.1.1.0/24 routing-mark=via-ether2add blackhole distance=2 dst-address=10.1.1.0/24 routing-mark=via-ether3The idea is that since distance is 2 these two are never actually used when the devices are present and working.But when one (or both) the routes with distance 1 become inactive, the rules with higher distance become instantly in use. ---

## Response 3
Author: [SOLVED]Thu Dec 05, 2024 3:44 pm
``` /ip addressaddaddress=192.168.1.1/24interface=ether1 network=192.168.1.0addaddress=192.168.1.200/24interface=ether1 network=192.168.1.0addaddress=192.168.1.201/24interface=ether1 network=192.168.1.0addaddress=10.1.1.1/24interface=ether2 network=10.1.1.0addaddress=10.1.1.1/24interface=ether3 network=10.1.1.0.../ip firewall mangleaddaction=mark-routing chain=prerouting dst-address=192.168.1.200in-interface=ether1new-routing-mark=via-ether2 passthrough=yesaddaction=mark-routing chain=prerouting dst-address=192.168.1.201in-interface=ether1new-routing-mark=via-ether3 passthrough=yes.../interfacelistaddname=DEVICES/interfacelist memberaddinterface=ether2 list=DEVICESaddinterface=ether3 list=DEVICES.../ip firewall nataddaction=dst-nat chain=dstnat dst-address=192.168.1.200-192.168.1.201in-interface=ether1 to-addresses=10.1.1.20addaction=masquerade chain=srcnatout-interface-list=DEVICES.../ip routeadddistance=1dst-address=10.1.1.0/24gateway=ether2 routing-mark=via-ether2adddistance=2dst-address=10.1.1.0/24routing-mark=via-ether2 type=blackholeadddistance=1dst-address=10.1.1.0/24gateway=ether3 routing-mark=via-ether3adddistance=2dst-address=10.1.1.0/24routing-mark=via-ether3 type=blackhole ``` What are the routes (/ip route print) at the time the machine is disconnected (pull the cable)?Very likely the routing rule (that is for "new-routing-mark=port1") that in your posted output is #0 is not anymore AS (Active, Static) but becomes just S or IS (Inactive), and either the "generic" route takes precedence or (for whatever reason) the other identical route (which should be for "new-routing-mark=port2" only) is used.I suspect the first, the router tries desperately to reach destination, but cannot say for sure.In these cases usually a blackhole rule is added with a higher distance, you would need two of them, *like*:/ip routeadd blackhole distance=2 dst-address=10.1.1.0/24 routing-mark=via-ether2add blackhole distance=2 dst-address=10.1.1.0/24 routing-mark=via-ether3The idea is that since distance is 2 these two are never actually used when the devices are present and working.But when one (or both) the routes with distance 1 become inactive, the rules with higher distance become instantly in use.Thanks for the explanation. It was indeed the default rule that took precedence (#0 became S when cable is unplugged).Adding the 2 blackholes rules solves this issue and is required to maintain clear separation between the 2 machines when one of them is unplugged.Here the full working config in case someone needs it:
```
---
```

## Response 4
Author: Tue Dec 10, 2024 11:35 pm
``` /ip firewall mangleaddaction=mark-routing chain=prerouting dst-address=192.168.1.200in-interface=ether1new-routing-mark=via-ether2 passthrough=yesaddaction=mark-routing chain=prerouting dst-address=192.168.1.201in-interface=ether1new-routing-mark=via-ether3 passthrough=yes ``` ``` addaction=dst-nat chain=dstnat dst-address=192.168.1.200-192.168.1.201in-interface=ether1 to-addresses=10.1.1.20 ``` Very good.The syntax I posted was for Ros 7, sorry, but I see you adapted it to your Ros 6.x just fine.Thanks for your help. It was indeed quite easy to convert it to Ros 6.It is tested and working perfectly fineAlmost caught up. Just trying to follow the traffic flow starting at the controller. My logic is missing something in these steps.1. How does the controller know to look for a machine at 192.168.200 or 192.168.201.> As I understand it, the mangle rule tell to route the trafic for either 192.168.1.200 or 201 directly to the interface ether2 or 3.
```
2. Assuming it knows for some reason,  following the bouncing ball...........Since mangling happens first, we capture the traffic originating in ether1 heading for   an IP address in the same subnet.Is that even possible?  Its within the same subnet so my thought was it could not be captured by a router (since its mac address traffic not requiring IP???)The NAT rule will rewrite the destination IP from 192.168.1.200 or 201 to 10.1.1.20 (which is the same on both interface).
```