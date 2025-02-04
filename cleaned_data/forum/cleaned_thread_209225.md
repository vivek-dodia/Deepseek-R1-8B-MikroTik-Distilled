# Thread Information
Title: Thread-209225
Section: RouterOS
Thread ID: 209225

# Discussion

## Initial Question
HiWe have some Switches where we would like to have this configuration:Management Port (eg ether49) with dedicated IP 192.168.0.10/24VLAN 1 with IP 192.168.0.11/24Gateway is 192.168.0.1The trunk (uplink) to the core switch is on sfp-sfpplus2 port.
```
/interfacebridgeaddname=bridge1 vlan-filtering=yes/interfacebridge portaddbridge=bridge1 comment="(ansible)"frame-types=admit-only-untagged-and-priority-taggedinterface=sfp-sfpplus2/ip addressaddaddress=192.168.1.10/24comment="(ansible) Management"interface=ether49 network=192.168.1.0/ip addressaddaddress=192.168.1.11/24comment="(ansible) IP via VLAN"interface=vlan1 network=192.168.1.0/ip routeadddisabled=nodistance=1dst-address=0.0.0.0/0gateway=192.168.0.1routing-table=main suppress-hw-offload=noThe ether49 shouldn't assigned to any bridge, so complete independent, connected to a management switch.If I configure it, 192.168.1.10 is reachable inside of the 192.168.1.0/24 subnet, but not from the other side of the gateway, the 192.168.1.11 is unreachable.The idea behind is, that the switch is manageable via 192.168.1.10 and 192.168.1.11.Thanks for helpIvo

---
```

## Response 1
You cannot use the same IP subnet on multiple layer2 / ethernet interfaces, the device would have no idea of which interface to send ARP requests to. ---

## Response 2
The way to deal with such scenario is to use VRF's.Note however that VRF's are somewhat broken in ROS 7.x so not all services supports VRF's once you choose to go that path.For example the /ip/dns service doesnt support VRF (it claims it does since 7.15 but its broken), same with ip/ftp (no support at all) and remote logging isnt VRF-aware either. ---

## Response 3
Also, as a general rule of thumb, it can be an issue using VLAN 1. Although for your specific application it should not be a problem, but many other devices treat VLAN 1 as "special" and do various undesired things with it. Best just to avoid it. ---

## Response 4
I wish everytime someone tried to create vlan1 on the router, it would spit out an audio recording of this............https://www.youtube.com/watch?v=EfYtMLe7gqI ---

## Response 5
I wish everytime someone tried to create vlan1 on the router, it would spit out an audio recording of this............https://www.youtube.com/watch?v=EfYtMLe7gqIOr like thishttps://www.youtube.com/watch?v=nP_JN6TKQFw&t=37 ---

## Response 6
Thanks a lot for all your answers. I have to think, how we deal with it. ---

## Response 7
...okay first something for the VLAN 1 guys - thanks for that not very professional and not very respect full answers... The code was an example to obfuscate client's configuration, also VLAN 1. So or so, your comments has nothing to do with the solution...The solution was to assign the IP 192.168.1.11/24 not to the VLAN, it should be on the bridge... ---

## Response 8
As the saying goes, garbage in garbage out.By the way your conclusion is wrong, but since you seem content with it......... ---