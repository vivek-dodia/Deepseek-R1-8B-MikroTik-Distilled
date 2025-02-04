# Thread Information
Title: Thread-214310
Section: RouterOS
Thread ID: 214310

# Discussion

## Initial Question
Hi all, this is my question:I have two interfaces: one with the internet (eth1-wan) and one with the local network (eth2-lan) without bridge.On the local network (eth2-lan) I have 50 hosts that do not need to access the internet. only one of the hosts must be able to access the internet.What kind of approach should I use?thanks ---

## Response 1
A simple firewall rule:
```
/ip firewall filteraddaction=drop chain=forwardin-interface=eth2-lanout-interface=eth1-wan src-address=!a.a.a.awherea.a.a.ais the IP of the specific host that needs to reach the internet

---
```

## Response 2
In the forward chain, remove the default ruleadd action=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \connection-state=new in-interface-list=WANReplace withadd chain=forward action=accept comment="host to internet" in-interface-list=LAN src-address=singlehost-IP out-interface-list=WANadd chain=forward action=accept comment="port forwarding" connection-nat-state=dstnat disabled=yes { enable if required, or remove }add chain=forward action=drop comment="Drop all else"If you decide to add more hosts that are allowed, simply turnsrc-address=singlehost-IPtosrc-address-list=internet-traffic/ip firewall address-listadd address=host1-allowed-IP list=internet-trafficadd address=host2-allowed-IP list=internet traffic...add address=hostN-allowed-IP list=internet traffic ---

## Response 3
I'll provide some more information.I have no default configurations or rules, at the moment the RB only has the two interfaces, both with static IP, without bridge between them.from the terminal I regularly ping the internet from the wan interface, and the local hosts on the lan interface.my goal now is to allow only one host to reach the internet.Soon I'll try the solution recommended by anav, then I'll updatethanks ---

## Response 4
Bad idea to connect any router to the internet without firewall rules in place. ---

## Response 5
I concur.Default firewall rules:
```
/ip firewall filteraddchain=input action=accept connection-state=established,related,untracked comment="defconf: accept established,related,untracked"addchain=input action=drop connection-state=invalid comment="defconf: drop invalid"addchain=input action=accept protocol=icmp comment="defconf: accept ICMP"addchain=input action=accept dst-address=127.0.0.1comment="defconf: accept to local loopback (for CAPsMAN)"addchain=input action=dropin-interface-list=!LAN comment="defconf: drop all not coming from LAN"addchain=forward action=accept ipsec-policy=in,ipsec comment="defconf: accept in ipsec policy"addchain=forward action=accept ipsec-policy=out,ipsec comment="defconf: accept out ipsec policy"addchain=forward action=fasttrack-connection connection-state=established,related comment="defconf: fasttrack"addchain=forward action=accept connection-state=established,related,untracked comment="defconf: accept established,related,untracked"addchain=forward action=drop connection-state=invalid comment="defconf: drop invalid"addchain=forward action=drop connection-state=newconnection-nat-state=!dstnatin-interface-list=WAN comment="defconf: drop all from WAN not DSTNATed"

---
```

## Response 6
we are on a company intranet, it is not possible to access from outside the company network.however, as soon as the configuration is executed and tested, I will create the default firewalling rules allowing only known hosts to connect to RBthanks! ---

## Response 7
So the device does not get a public IP but a private IP from an upstream company router?If so, correct one should still ensure access to:a. the router for config purposes is limited to admin IT staffb. access to any subnets (double nat) are limited to those requiring access etc... ---