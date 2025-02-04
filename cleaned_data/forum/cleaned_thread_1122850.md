# Thread Information
Title: Thread-1122850
Section: RouterOS
Thread ID: 1122850

# Discussion

## Initial Question
I have a firewall INPUT rule that fires every now and then.
```
input:in:loout:(unknown0),connection-state:invalid proto ICMP(type137,code0),fe80::3:510d:9220->fe80::3:510d:9220The ipv6 address corresponds to a 6to4 tunnel interface on the same MT device for which neighbor discovery is not enabled.Could anyone make sense of that ? Should I continue to drop those packets ? I am still on 7.15.3 and would likely upgrade to 7.17.1 once it's out.

---
```

## Response 1
What is the firewall rule? ---

## Response 2
This is the rule I have in place:
```
/ipv6 firewall filteraddaction=log chain=input comment="Logging before ipv6-drop-input"dst-address-type=!multicastin-interface-list=!wan6 log-prefix=ipv6-drop-input-internalHowever, I believe I’ve identified the culprit. It turns out I had an ipv4 rule that was performing a DST-NAT to the router itself.It is a bit surprising it could possibly affect ipv6 traffic but I don't need this ipv4 rule anymore anyway, so I’ve removed it. No packets loggued for 4 days now.

---
```

## Response 3
If it returns, please sniff the packet. ---