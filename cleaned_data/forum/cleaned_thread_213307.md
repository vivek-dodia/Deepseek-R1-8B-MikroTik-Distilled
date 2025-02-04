# Thread Information
Title: Thread-213307
Section: RouterOS
Thread ID: 213307

# Discussion

## Initial Question
I have a RB5009. It is a fairly regular setup. 1 port is connected to a switch, and 2 ports are connected to two separate WANs (1gbit each).Everything works as usual. However after a while under 1 hour, the routing speed reduces. I can see about 20mbit on speedtest.net.When I restart the router. I can see 1gbit on speedtest.net speed tests instantly.To diagnose, when the routing is slowed down, I unplugged the switch, which removed all of the clients. I disabled all firewall and all mangle rules. It didn't speed up.How is this possible? What could be the bottleneck? I have almost zero configuration that should impact the speed and no clients.How can I diagnose this? How come turning off all rules and 0 clients doesn't bring back the routing speed. Only restart seems to fix it.Is it faulty hardware? I have almost same setup in 1 other router, no issues as all. ---

## Response 1
I have almost same setup in 1 other router, no issues as all.Are both of the routers on the same software and firmware versions?Do some tests:Swap these 2 router configs. Put the config from router-1 onto router-2, and put the config from router-2 onto router-1. Does the issue follow the router or does the issue follow the configuration? ---