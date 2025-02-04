# Thread Information
Title: Thread-214014
Section: RouterOS
Thread ID: 214014

# Discussion

## Initial Question
MikroTik default WAN port does not have a bridge assigned to it. When changing WAN port, it appears to require creation of a bridge for it. Is there a way to strip bridge from a newly re-assigned WAN port? Is there any particular problem with having a bridge for WAN port when Bridge IP Firewall is enabled? ---

## Response 1
Well, there may be some confusion in terminology.A bridge is an interface that contains interface(s), i.e. you don't assign a bridge to an interface, you add the interface(s) to the bridge.You can then strip the interface from the bridge, not viceversa.If you prefer an interface (like ether1 for example) has its own characteristics, but can be "wrapped" into a bridge, thus inheriting some of the characteristics of this outer shell. ---

## Response 2
Normally, the WAN need not be part of any bridge.Depends on the circumstances, and typically in vlan filtering there is only one bridge. ---