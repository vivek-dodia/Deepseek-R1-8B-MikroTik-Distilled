# Thread Information
Title: Thread-213497
Section: RouterOS
Thread ID: 213497

# Discussion

## Initial Question
I have 2 WAN connectıons. I used to use mangle rules for load balancing. This limited my fasttrack capabilities naturally. So I removed all mangle rules and converted to load balancing through routes.
```
/ip routeadddistance=1dst-address=8.8.4.4/32gateway=192.168.10.1scope=10addblackhole distance=20dst-address=8.8.4.4/32adddistance=1dst-address=8.8.8.8/32gateway=192.168.20.1scope=10addblackhole distance=20dst-address=8.8.8.8/32adddistance=1dst-address=208.67.220.220/32gateway=192.168.1.40scope=10addblackhole distance=20dst-address=208.67.220.220/32adddistance=1dst-address=208.67.222.222/32gateway=192.168.1.30scope=10addblackhole distance=20dst-address=208.67.222.222/32addcheck-gateway=ping disabled=nodistance=1dst-address=0.0.0.0/0gateway=208.67.222.222routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=11addcheck-gateway=ping disabled=nodistance=1dst-address=0.0.0.0/0gateway=208.67.220.220routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=11addcheck-gateway=ping disabled=nodistance=2dst-address=0.0.0.0/0gateway=8.8.8.8routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=11addcheck-gateway=ping disabled=nodistance=2dst-address=0.0.0.0/0gateway=8.8.4.4routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=11The load balancing works. However it only works with a specific fasttrack configraiton. If I keep it like this, it does fasttrack but only for LAN (as expected)
```

```
addaction=fasttrack-connection chain=forward comment="fasttrack all communication from device networks"connection-state=\
    established,related dst-address-list=FIBER-INTERNET-LIST hw-offload=yes log-prefix=DEVICE-NETWORKS src-address-list=\
    FIBER-INTERNET-LISTaddaction=accept chain=forward comment="defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedif I remove dst-address-list=FIBER-INTERNET-LIST and src-address-list=\FIBER-INTERNET-LIST my network slows down so much that it is apperant that there is a problem. So effectively it breaks. Does anyone know why? I thought fasttrack could also work for WAN connections. Is it only meant to be for LAN?My mangle rules are emptymy address list is as below
```

```
addaddress=10.4.0.0/16list=FIBER-INTERNET-LISTaddaddress=10.5.0.0/16list=FIBER-INTERNET-LISTaddaddress=10.6.0.0/16list=FIBER-INTERNET-LIST

---
```

## Response 1
What is your device model, i.e. does it actually support routing in hardware?WAN<->LAN traffic can normally indeed be fasttracked, and fasttracking is indeed compatible with ECMP load balancing, so one thing to come to my mind is that ECMP in hardware might not work on your device, as the table in the documentation regarding L3HW indicates some ECMP limitations for one group of device models and is totally silent about ECMP for another group.Another thing is that your routing configuration is a bit incomprehensible to me. You mention two WANs but your /32 routes use 4 distinct gateways. Normally, I would set one Google DNS address and one OpenDNS one as the canaries for each WAN, both with the samegateway, and I would set the samedistancefor all the default routes using the individual canaries asgatewayaddreses. Maybe it is just an incorrect obfuscation because the gateway addresses are public ones?I do realize that if the issue is this, it should affect also the traffic that is not fasttracked, but so far I cannot see any reason why allowing fasttracking for all the traffic should have such a detrimental effect on your router's throughput. ---

## Response 2
What is your device model, i.e. does it actually support routing in hardware?I have a RB 5009Another thing is that your routing configuration is a bit incomprehensible to me. You mention two WANs but your /32 routes use 4 distinct gateways. Normally, I would set one Google DNS address and one OpenDNS one as the canaries for each WAN, both with the same gateway, and I would set the same distance for all the default routes using the individual canaries as gateway addreses. Maybe it is just an incorrect obfuscation because the gateway addresses are public ones?Before I had 4 WANs. But I stopped using 2 of them. I just forgot to remove the routing rules. So you are right about it.I want to use fasttrack mainly because of the LAN traffic. I have lots of cameras that use inter VLAN routing, and I also want to have some firewall rules being applied. Before fasttrack, CPU utilizaiton was a lot. So just by getting LAN fasttrack to work, I actually increased to the performance I need.Having said that I was curious, why I have issues with fasttracking WAN connections. I was thinking that it would work pretty much the same. ---

## Response 3
I have a RB 5009OK, so we may completely forget about the L3HW as a possible cause.Having said that I was curious, why I have issues with fasttracking WAN connections. I was thinking that it would work pretty much the same.At the moment I can only say that I am curious too, as it makes little sense to me so far. Can you post the complete configuration export, of course after obfuscating the identifying details? ---