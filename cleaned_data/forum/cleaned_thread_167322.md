# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 167322

# Discussion

## Initial Question
Author: Thu Oct 08, 2020 3:29 pm
``` /ip firewall filter add action=accept chain=input comment="allow established, related" connection-state=established, related add action=accept chain=input comment="aallowed to router" src-address-list=allowed_to_router add action=accept comment="allow ICMP" chain=input protocol=icmp add action=drop comment="drop everything else" chain=input /ip firewall address-list add address=10.10.10.1-10.10.10.254 list=allowed_to_router ``` Hello all! I installed one CRS112-8p-4s-in as internal PoE switch.I have set up some input protection, and was wondering if I also needed to put forward rules in the firewall?
```
Thanks
```