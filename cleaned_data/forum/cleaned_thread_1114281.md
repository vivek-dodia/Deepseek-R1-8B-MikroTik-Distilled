# Thread Information
Title: Thread-1114281
Section: RouterOS
Thread ID: 1114281

# Discussion

## Initial Question
I'm wanting to block end users from manually assigning IP addresses to their routers, thereby potentially causing conflicts with my DHCP server. I believe the way to accomplish this is via arp=reply-only on the router interfaces facing the customers, and add-arp=yes on the DHCP server. My question is this - if the interfaces are all on a bridge, do I just set the bridge to arp=reply-only, and leave the interfaces themselves alone? Or do I need to set it on both the bridge and the interfaces? Or just the interfaces?Thanks! ---

## Response 1
Only on the bridge, as that's what the IP stack is linked to. The Ethernet interfaces are just member ports of the bridge in this setup. ---

## Response 2
Only on the bridge, as that's what the IP stack is linked to. The Ethernet interfaces are just member ports of the bridge in this setup.... which also means that access to other networks (including internet) can be controlled in this way. But: communication between devices on same IP subnet (even if passing bridge between two member ports) will still work. ---

## Response 3
Only on the bridge, as that's what the IP stack is linked to. The Ethernet interfaces are just member ports of the bridge in this setup.Got it, this makes sense. Thank you! ---