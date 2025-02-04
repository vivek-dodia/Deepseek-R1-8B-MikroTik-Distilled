# Thread Information
Title: Thread-1117063
Section: RouterOS
Thread ID: 1117063

# Discussion

## Initial Question
Schermata del 2024-12-30 16.26.18.pngon ros 7.16.2 routerboarb rbm11 I can no longer do a full traceroute test, how can this be solved? ---

## Response 1
Does it look the same from the terminal window?/tool/traceroute 1.1.1.1 use-dns=yes ---

## Response 2
yesSchermata del 2024-12-30 22.19.02.pngfirewall_rules.txt ---

## Response 3
how about8.8.8.8or8.8.4.4? ---

## Response 4
/ip firewall mangleadd action=change-ttl chain=postrouting new-ttl=set:65 out-interface=lte1 passthrough=yesThis is the rule that makestracerouteshow you that "strange" result. The principle of operation oftracerouteis that it sends packets to the destination with TTL set to 1, 2, 3 etc. and expects to get an ICMP message "TTL expired" from the corresponding routers on the path to the destination address. By forcing TTL to 65, you make already the first packet (with TTL originally set to 1) reach the final destination; since you use ICMP echo (ping) to test, the actual destination sends a regular echo response, so you can see that single row. ---

## Response 5
thanks again sindy , disabling the rule works everything . Happy New Year ! ---