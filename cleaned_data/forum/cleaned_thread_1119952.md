# Thread Information
Title: Thread-1119952
Section: RouterOS
Thread ID: 1119952

# Discussion

## Initial Question
Hello MikroTik Community, I am trying to configure my MikroTik router to route incoming traffic based on the destination CNAME address to specific internal IP addresses and ports. Here's the scenario:Traffic destined for app1.mydomain.dk on port 443 should be routed to 10.1.1.10:30087.Traffic destined for app2.mydomain.dk on port 443 should be routed to 10.1.1.10:30089.10.1.1.10 hosts a truenass server with some applications on it that I want to expose.I understand that RouterOS operates primarily on IP-level rules, but since app1.mydomain.dk and app2.mydomain.dk are CNAMEs, I'm unsure how to correctly set up rules that will achieve this.Could anyone guide me on how to handle this? For example:Should I use Layer 7 Protocol rules to inspect the HTTP(S) hostname?Would handling it with nginx proxy manager be a better approach?Any help, examples, or suggestions would be greatly appreciated!Thank you, thedbpedit: I figured it out, I'm routing my traffic through nginx proxy manager that handles the domain based routing ---

## Response 1
Just to be precise:edit: I figured it out, I'm routing my traffic through nginx proxy manager that handles the domain based routingnginx doesn't "domain route" traffic, it (reverse) proxies it. Which is L7 operation - contrasted to routing which is L3 operation. ---