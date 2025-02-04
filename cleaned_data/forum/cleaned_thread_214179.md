# Thread Information
Title: Thread-214179
Section: RouterOS
Thread ID: 214179

# Discussion

## Initial Question
Hello all, I am wondering about the following and I have not been able to find an answer.Assume a Mikrotik router with three IP's - two are static, and the third is DHCP.My question is, which of the three WAN IP addresses will be attached as the "main" connection in the routing table?I think it has to be the one that is connected and configured first, since the distance "0" cannot be changed in the Route List.I'm fine if that is "the way it is" - it just means I have to keep that in mind to connect the WAN ports in a specific order. ---

## Response 1
Wrong, the order of WAN, primary, secondary, tertiary etc or all equal ( same distance - ECMP load balancing) is admin decision.Very flexible setup. ---