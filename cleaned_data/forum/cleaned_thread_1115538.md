# Thread Information
Title: Thread-1115538
Section: RouterOS
Thread ID: 1115538

# Discussion

## Initial Question
Hi, I have two sites which are connected to the Internet through ISP router. In each location there is a Mikrotik router creating its own subnet. I want to route traffic between one device behind one Mikrotik to another device behind the other Mikrotik. The two ISP router are connected trough a site-to-site VPN and I asked the IT guy who services both location to create a rule to route traffic between the subnet created by the two Mikrotik. Now from one Mikrotik I can ping the Mikrotik on the other side (on ether2 address) and vice versa, but I cannot ping the devices behind them. The only way to ping these devices is to disable to default firewall rule "drop all from WAN not DSTNATed". I tried setting up different nat rules, but none of them worked. The Mikrotik firewall configuration at both sites is the default one. What is the best way to route traffic between those two location without deleting the "drop all from WAN not DSTNATed" rule?scheme.png ---

## Response 1
So you have a VPN tunnel between Mikrotik A and Mikrotik B ? Which one ?Answers based on not seeing your config:What interface list is that VPN tunnel in ? I assume nothing.2 short options:explicitly allow traffic via firewall coming from that tunnel on both Mikrotik devicesoradd VPN interface to LAN interface list on both Mikrotik devicesMake sure on both ends to clear connection tracking in firewall before testing (or reboot, or wait some minutes).If you want more detailed responses from anyone, you may have to show your config for both ends. ---

## Response 2
He has no vpn tunnel between the mikrotiks, the tunnel is between the two ISP routers. ---

## Response 3
You're correct, I missed that line. ---

## Response 4
```
/interfacelistaddname=WANaddname=LAN/interfacelist memberaddinterface=ether1 list=WANaddinterface=ether2 list=LAN/ip addressaddaddress=192.168.1.10/24interface=ether1 network=192.168.1.0addaddress=10.0.1.1/24interface=ether2 network=10.0.1.0/ip firewall filteraddaction=accept chain=input comment="accept established,related,untracked"\
    connection-state=established,related,untrackedaddaction=drop chain=input comment="drop invalid"connection-state=invalidaddaction=accept chain=input comment="accept ICMP"protocol=icmpaddaction=accept chain=input comment="allow WinBox from LAN"\
    dst-port=8291in-interface-list=LAN protocol=tcpaddaction=drop chain=input comment="drop everything else"addaction=fasttrack-connection chain=forward comment=fasttrack \
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="drop invalid"connection-state=invalidaddaction=drop chain=forward comment="drop all from WAN not DSTNATed"\
    connection-nat-state=!dstnat connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnatout-interface-list=WAN/ip routeadddisabled=nodst-address=0.0.0.0/0gateway=192.168.1.1routing-table=main \
    suppress-hw-offload=noThis is the relevant part of the config for Mikrotik A, Mikrotik B shares the same config except for the IPs and subnets, which are shown in the diagram I posted earlier.Indeed, there is no VPN between the Mikrotiks, but there is between the ISP routers.Now, from 10.0.1.2 (on site A) I can ping 10.0.2.1 (Mikrotik B), but I can't ping 10.0.2.2, which is behind Mikrotik B. The same happens for site B: from 10.0.2.2 I can ping 10.0.1.1, but not 10.0.1.2. If i disable the last forward firewall rule ("drop all from WAN not DSTNATed"), from 10.0.1.2 I can ping 10.0.2.2 and vice versa. This makes me think that an appropriate dst-nat rule might allow the flow to work, but I can't figure out what this rule should look like.

---
```

## Response 5
Maybe this ?/ip firewall natadd action=src-nat chain=srcnat dst-address=10.0.1.0/24 out-interface=ether1 to-addresses=10.0.2.1Reverse for the other side. ---

## Response 6
Unfortunately, it doesn't work: the rules are never hit. ---

## Response 7
Obviously you need to move that rule to the top of NAT rules ...And make sure connection track table is empty or reset MT device (or wait). ---

## Response 8
Thank you for the help you are providing me, but still no luck.EDIT: I just tried to create this firewall rule on Mikrotik A
```
addaction=accept chain=forward dst-address=10.0.1.0/24in-interface-list=WANand this rule on Mikrotik B
```

```
addaction=accept chain=forward dst-address=10.0.2.0/24in-interface-list=WANand it works.Is this the right way to do it or is it preferable to use a dst-nat rule?

---
```

## Response 9
@jack14Take what I write below with a pinch (or better two) of salt, as I am not at all an expert in firewall rules, so the following may well be completely wrong, still:I don't think that the issue is with that default final drop rule.That rule simply does what it is supposed to do. i.e. drop connections that match three "filters":1) connection-nat-state=!dstnat2) connection-state=new3) in-interface-list=WANand it essentially prevents all connections originating from the WAN side of the router, it is the last one in the default firewall settings, and should remain as is.In alternate firewall settings the last rule is "drop all else".In theoryyou need, beforethat rule, a new one that explicitly accepts the connections from your other site.The questions are which matchers should this accept rule have to only allow your traffic from the other site and how does that traffic arrive.A (completely wrong! ONLY for test!) accept rule could be *something like* (on Mikrotik A):add action=accept chain=forward comment=this is wrong, only for test in-interface-list=WAN src-address=192.168.2.0/24 dst-address=10.0.1.0/24that should allow connection from the net 10.0.2.0 that is natted by the devices on site B to either 192.168.2.1 or 192.168.2.10 (I think the latter).If this is the case, and the above works, you can narrow it a little bit:add action=accept chain=forward comment=this is wrong, only for test in-interface-list=WAN src-address=192.168.2.10 dst-address=10.0.1.0/24But even this could be a huge hole in the firewall, there isn't AFAIK anything that can distinguish "your" 192.168.2.10 from anyone else's 192.168.2.10, unless your ISP router has a firewall that surely prevents any other connection with that source address.So the "right" way should be to establish some kind of VPN tunnel between the two Mikrotiks (Wireguard? IPSEC? Something else? cannot say).EDIT: oops, cross-posting. I now see you already found an (even wider than mine) accept rule (yours makes your whole LAN accessible for all the internetunless it is stopped by your ISP router firewall, of course). ---

## Response 10
You are right about the security issue. I was assured that the firewall on ISP routers is correctly configured. I hope it is true. ---

## Response 11
Yep, in any I think you should anyway "tighten" that firewall rule by src-address, to at least the originating subnet, but better to the actual natted source address.The suggestion by holvoeth to src-nat the specific dst-address (before the generic masquerade) seems to me like a good one, this way you have more control on the natted address, though in this case the masquerade should use anyway a "fixed" address, I think that this could allow to use a completely different subnet address, but it has to be tested. ---

## Response 12
I've the same setup in personnal usage.Both are behind a french ISP box, acting as router with 1 ipv4 addr and allow 8 ipv6 subnet to be "prefix delegation".For ipv4, "dmz" is set to the "wan" mkt addr and, it's a classic setup with nat masquerade, etc..., it's justFor ipv6, i've just use prefix delegation and nothing else than ipv6 firewall filterI set a wireguard between both sites with public dns names managed by mkt ip cloud.So, i can easily route between site2site with the wg interface. ---

## Response 13
Yep, in any I think you should anyway "tighten" that firewall rule by src-address, to at least the originating subnet, but better to the actual natted source address.The suggestion by holvoeth to src-nat the specific dst-address (before the generic masquerade) seems to me like a good one, this way you have more control on the natted address, though in this case the masquerade should use anyway a "fixed" address, I think that this could allow to use a completely different subnet address, but it has to be tested.Thank you for the suggestion, I improved the rule by including the source address.I would also prefer to use a NAT rule, but I have tried several without success. Unfortunately, the rule proposed by holvoetn does not work in this case. ---

## Response 14
Yep, but what it is the source address you added to the firewall filter rule?That address is - if I got the configuration right - 192.168.x.10.If this is the case. it is "created" by your current nat rule:/ip firewall natadd action=masquerade chain=srcnat out-interface-list=WANmasquerade is a command/action that essentially says to the router "nat all packets through the WAN to whatever address you see fit" (which in your case should be the current address of the WAN interface.A src-nat command/action *like* this:/ip firewall natadd action=src-nat chain=srcnat dst-address=10.0.1.0/24 out-interface-list=WAN to-addresses=10.0.2.1essentially says to the router "nat only the packets that go to 10.0.1.0/24 through the WAN to exactly the address 10.0.2.1"This could be IMHO an advantage in the sense that when/if you will change the address of ether1 you won't need to change on the "other" router the src-address of the accept rule. ---