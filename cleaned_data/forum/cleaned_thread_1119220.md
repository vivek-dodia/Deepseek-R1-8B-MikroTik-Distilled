# Thread Information
Title: Thread-1119220
Section: RouterOS
Thread ID: 1119220

# Discussion

## Initial Question
I'm not having success in establishing an l2TP tunnel over IPV6 from a windows client to my Mikrotik router. I can get it to work fine over IPv4. I think that IPV6 is working properly on the router because I can connect to it remotely (assuming I temporarily open the winbox port in the IPV6 firewall). I can ping the router remotely using IPV6 and make outbound IPV6 connections through the router.When I try to start a L2TP tunnel to the router over IPV6 (either from the outside or from the inside), the IPSEC session start successfully based on the log data, the first L2TP packet is received as shown in the log data, but then I keep getting LCP timeouts during authentication and eventually the connection attempt fails.I have upd port 1701 open in the IPv6 firewall and it logs the first packet as L2TP tries to start.I can find no pointers to configuring L2TP over IPV6 in any Google searches. When I opened a ticket with Mikrotik, all they did was point me to the generic IPSEC configuration information which is based on IPV4 and does not address my issue. I have specified my IPV6 prefix pool for the policy for L2TP, but I suspect I might be missing something else.I can post a full configuration if desired. Does anyone have any comments or pointers to some good documentation for setting up L2TP over IPV6?I'm running RouterOS 7.16. ---

## Response 1
Did you solve the problem?I have the same ---