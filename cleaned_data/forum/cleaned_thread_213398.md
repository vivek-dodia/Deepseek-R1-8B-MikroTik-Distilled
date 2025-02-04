# Thread Information
Title: Thread-213398
Section: RouterOS
Thread ID: 213398

# Discussion

## Initial Question
HelloThere is a LAN.The edge router is Mikrotik on OS 7.14.There are several VPNs for people working remotely.Question 1:How to create another VPN, but one that allows the employee to access only one host (one IP address) within the network?Question 2:How do I make it so that only specific ports work and that the ICMP protocol also works?--RegardsAdam. ---

## Response 1
High levelQ1: create VPN and using firewall rules and VPN interface in forward chain restrict access to only 1 destination device (allow to one dest, drop all the rest coming from that interface).Q2: similar approach.What VPN are you planning to add ? ---

## Response 2
High levelQ1: create VPN and using firewall rules and VPN interface in forward chain restrict access to only 1 destination device (allow to one dest, drop all the rest coming from that interface).ThanksQ2: similar approach.What VPN are you planning to add ?Probably L2TP. ---