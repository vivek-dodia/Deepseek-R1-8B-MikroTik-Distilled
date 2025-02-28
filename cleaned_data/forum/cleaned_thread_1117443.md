# Thread Information
Title: Thread-1117443
Section: RouterOS
Thread ID: 1117443

# Discussion

## Initial Question
Hello all, I am struggling to understand why I am getting DST NAT rule hits on traffic that is blocked by the firewall.For example, with following config:
```
/ip/firewall/filter/addchain=forward src-address=100.100.100.100dst-address=192.168.200.10dst-port=22protocol=tcp action=accept/ip/firewall/filter/addchain=forwardin-interface=WAN action=drop/ip/firewall/nat/addchain=dstnat dst-address=200.200.200.200dst-port=22protocol=tcpin-interface-list=WAN action=dst-nat to-addresses=192.168.200.10to-ports=22I have active logging on the third rule (DST NAT rule) and I keep seeing hits and traffic from random IPs getting NATted.I tested it with random public IPs -> session does not get established (as it shouldn't, since there is a whitelist), but hit counter goes up.Is this normal MT behavior? I would expect traffic getting blocked by the FW to not trigger any NAT activity.Thank you.Kind RegardsGomo

---
```

## Response 1
Can you share your complete firewall filter rules?You don't have this default rule?
```
/ip/firewall/filter/addchain=forward action=drop connection-state=newconnection-nat-state=!dstnatin-interface-list=WANBesides this...why would you want to open port 22?

---
```

## Response 2
I do have following (besides 3 mentioned ones)
```
/ip/firewall/filter/addchain=forward action=drop connection-nat-state=!dstnatin-interface-list=WANAnd, no, unfortunately I cannot share the whole config -> hence why I wrote example FW rules. I won't even go into "why would someone open ports" question.TLDR, this doesn't really answer my question.. are there supposed to be hits on DST NAT rules for traffic that is not permitted by the FW?

---
```

## Response 3
TLDR, this doesn't really answer my question.. are there supposed to be hits on DST NAT rules for traffic that is not permitted by the FW?It depends on the order of rules, if the rule I mentioned is above the others you mentioned it makes perfect sense.But you would have to answer that. ---

## Response 4
It was asked nicely to see the full config to make a proper assessment using facts and evidence. Like it or not, MT config elements are interrelated.No one is asking to see anything revealing./export file=anynameyouwish (minus router serial number, any public WANIP information, keys, long assed dhcp lease lists, unused ipv6 items etc.)If you need to change some names or other things then do so, but other then the above there is nothing usually to be concerned about. Ensure you check any scripts as well. ---

## Response 5
are there supposed to be hits on DST NAT rules for traffic that is not permitted by the FW?Yes, there are. According topacket flow, DST-NAT is part of pre-routing ... and firewall filter rules are part of either input or forward packet path ... which both come after pre-routing.Sometimes it's possible to construct DST-NAT rules in a way so they don't match traffic which is not allowed. But if that's not possible, then DST-NAT rules will be executed ... and forward filter rules (matching on DST-NATed values) can do the job afterwards. ---

## Response 6
are there supposed to be hits on DST NAT rules for traffic that is not permitted by the FW?Yes, there are. According topacket flow, DST-NAT is part of pre-routing ... and firewall filter rules are part of either input or forward packet path ... which both come after pre-routing.Sometimes it's possible to construct DST-NAT rules in a way so they don't match traffic which is not allowed. But if that's not possible, then DST-NAT rules will be executed ... and forward filter rules (matching on DST-NATed values) can do the job afterwards.Thanks, this info is really helpful! A bit annoying and uncommon to do security related filtering on the NAT side of things..Based on that, it looks like a lot of processing power is being wasted due to the architectural design.. but then again, I am not really knowledgeable enough / qualified to compare MT to other vendors and say they're doing a good / bad job. ---

## Response 7
We cannot change how RoS works.....As for filtering the forward chain typically should have a rule like.add chain=forward action=accept comment="port forwarding" connection-nat-state=dstnatThere is no security settings done typically in dstnat rules. However, if you wish to limit external access to the port forwarding rules, this is typically done in NAT rules by adding a source-address or source-address-list entry on the NAT rule. This besides limiting the external access also renders the ports invisible from scans VICE visible with state CLOSED.If more privacy is required, have users come in on VPN to access servers. ---

## Response 8
it looks like a lot of processing power is being wasted due to the architectural design..It's actually not that bad, and most things in life are tradeoffs. It is useful to filter traffic after a routing decision has been made (and thus after dst-nat has been made) because an out-interface has become known already, so you can use it to filter more precisely. The actual waste of CPU is not that big as you prevent many connections from even coming into existence by dropping the single packet that has a potential to establish the connection. Where the source cannot be prevented from sending more packets by rejecting or silently ignoring the first one, you can useaction=droprules in therawtable, which stands even before the dstnat. You can even combine the approaches, where rules in raw drop packets whose source address matches an address list, and rules in other tables populate that address list. Of course, a search through an address list also requires CPU but less than the search through the list of tracked connections, so overall it may make sense to userawthis way, i.e. to pre-filter the incoming traffic. ---

## Response 9
A bit annoying and uncommon to do security related filtering on the NAT side of things..One thing to keep in mind: NAT is not about security ... although it does seem to help some times. So one thing is to introduce NAT rules and a separate thing is to add appropriate firewall rules. It's up to admin to consider performance issues (as to where to add mathcing properties, to NAT rule or to firewall filter rule, in order to make whole setup as secure as possible while keeping performance at highest possible level). And considering packet flow charts definitely helps in this area.As to wasted processing: it's the way things are. Might be that some other vendors have it similarly behind the scenes, but they might construct pairs of NAT rules + firewall rules whereas in MT generally nothing is done implicitly (there are a few rare exceptions to that, but not in NAT/fw area). ---

## Response 10
This --> You can even combine the approaches, where rules in raw drop packets whose source address matches an address list, and rules in other tables populate that address listSpeaks to creating lists of addresses to block.I prefer knowing the incoming source address but you did give me additional food for thought to lighten the load so to speak on the router./ip firewall address-listadd address=fixedWANIP1 list=Authorized comment="server static user #1"add address=fixedWANIP2 list=Authorized comment="server user #2"....add address=fixedWANIPXY list=Authorized comment="server static user #XY"add address=dnydns-url1 list=Authorized comment="server dynamic user #1"....add address=dnydns-urlAB list=Authorized comment="server dynamic user #AB"/ip firewall natadd chain=dstnat action=dstnat dst-address=localWANIP dstport=serverport protocol=xxx to-address=local-Server-IP src-address-list=Authorized/ip firewall rawadd chain=prerouting action=drop in-interface=etherX dst-port=serverport src-address=!Authorized ---