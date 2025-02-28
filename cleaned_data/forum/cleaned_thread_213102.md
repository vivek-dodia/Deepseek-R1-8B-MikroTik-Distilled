# Thread Information
Title: Thread-213102
Section: RouterOS
Thread ID: 213102

# Discussion

## Initial Question
Hello, I would like to block traffic to internet from my Reolink camera. At first I wanted to build a separate vlan etc... but for now I think just blocking access to internet seem sufficient and I still don't know how to do that.I tried to add the following rule to drop everything to give it a try :
```
/ip firewall filteraddchain=forward src-mac-address=ec:71:db:f2:b5:58action=dropFor me this should prevent everyconnection, but I still can access the video so ... it's not workingSo I am not ready to just drop connection going to WANMy confing is pretty simple cause it is basicly the default one, I know a little about networking theory but I barely have practical experience and each time I try something I have issuesHere is my config for the firewall:
```

```
Flags:X-disabled,I-invalid,D-dynamic0D;;;special dummy rule to show fasttrack counters
      chain=forward action=passthrough1;;;defconf:drop allfromWANnotDSTNATedchain=forward action=drop connection-state=newconnection-nat-state=!dstnatin-interface-list=WAN2;;;defconf:accept established,related,untracked
      chain=input action=accept connection-state=established,related,untracked3;;;defconf:drop invalid
      chain=input action=drop connection-state=invalid4;;;defconf:accept ICMP
      chain=input action=accept protocol=icmp5;;;defconf:accept tolocalloopback(forCAPsMAN)chain=input action=accept dst-address=127.0.0.16;;;defconf:drop allnotcomingfromLAN
      chain=input action=dropin-interface-list=!LAN7;;;defconf:acceptinipsec policyIf you want more info I can provide... If someone can help me it would be really nice

---
```

## Response 1
Yes, drop by mac address doesn't work at the router stage.You could connect only the Reolink to a specific ethernet port on the router, and block based on port.You could give the Reolink a static lease from the DHCP server, and block based on IP address.(From winbox, go to ip dhcp server, the leases, select the Reolink, and click on Make Static)Probably block in forward when out-interface-list=WAN and in-interface=port, or src-address=ip-address. ---

## Response 2
Yes, drop by mac address doesn't work at the router stage.Not exactly true. If the router can see the
```
src-macon the packet, then it will match it fine. The problem can be if the packet is L3 forwarded from somewhere else (but that is not the case here) or if it was already allowed in another rule. I use mac matching in fw rules all the time so I know the matcher works as expected.You could connect only the Reolink to a specific ethernet port on the router, and block based on port.It would be better to set up IOT/CCTV network with VLAN and then assign the port into it. I know- this opens whole can of worms, but setting stuff by physical port is hard to maintain and not future-proof (not scalable)@bloudman:The rule you created is IMHO correct, but your command will add the rule on the end which is not great because the traffic could be allowed in any of previous rules - router goes one-by-one from top to bottom until it matches the packet with rule. If the traffic is allowed in some rule, it will no longer evaluate subsequent rules. Without further info, I can only guess - either this is the issue or the connection was already established and fasttracked and therefore subsequent packets are passed through without even hitting the firewall. I would start by moving your rule higher in the list of FW rules (even on the top for test purpose) and then restarting the reolink (or clear all established connections in RouterOS) - that should kill existing connection.We could understand bit better if you share whole firewall - seems it got cut off around rule number 7. Preferably, if you could share whole
```

```
/ip firewallexport(that should include filter+nat+raw+mangle so that we cover all bases). If you find any confidential info (public IP, domain etc...  feel free to mask it with XXXXXXXX)

---
```

## Response 3
Works fine on my RB5009 (tested with my Internet radio) but your problem probably is the position of the rule in the forward chain!Move it up!You can always temporary enable logging and check the output. ---

## Response 4
Thanks a lot for your great replies !I tried to put the rule on top of everything but nothing happenedI should maybe do something about VLAN for now I use the default config for most of the stuff ...not great especially with IOT sharing the space of my servers/computers I will try to make something this afternoon
```
Flags:X-disabled,I-invalid,D-dynamic0D;;;special dummy rule to show fasttrack counters
      chain=forward action=passthrough1;;;defconf:drop allfromWANnotDSTNATedchain=forward action=drop connection-state=newconnection-nat-state=!dstnatin-interface-list=WAN2;;;defconf:accept established,related,untracked
      chain=input action=accept connection-state=established,related,untracked3;;;defconf:drop invalid
      chain=input action=drop connection-state=invalid4;;;defconf:accept ICMP
      chain=input action=accept protocol=icmp5;;;defconf:accept tolocalloopback(forCAPsMAN)chain=input action=accept dst-address=127.0.0.16;;;defconf:drop allnotcomingfromLAN
      chain=input action=dropin-interface-list=!LAN7;;;defconf:acceptinipsec policyThis is the full list of my firewall rules without rules that were not working i did add it at begining at the end none was working

---
```

## Response 5
>> For me this should prevent everyconnection, but I still can access the video so ... it's not workingHow do access the video-feed ? Are you using app on your smartphone on the local WIFI-network ? Are you testing externally with your phone on 4G/5G?Is the REOLINK cabled directly into the Mikrotik ?Please provide some info on this. Your use-case is the most simple one and must work. ---