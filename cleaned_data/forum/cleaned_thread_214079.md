# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 214079

# Discussion

## Initial Question
Author: Tue Jan 21, 2025 6:59 pm
Situation: Mikrotik 3011 connected through WireGuard to a 4011. I have another 5009 where I am physically connected to the 4011 and I can access both the 4011 and 3011’s LANs. The 5009 and 4011 are both with public IPs. The 3011 gets its WAN access through a third party router connected to eth1. I would like to be able to access it for management.3011’s LAN: 192.168.5.0/24Third party router LAN: 192.168.158.0/24The 3011 gets 192.168.158.1 IP.Any ideas? ---

## Response 1
Author: [SOLVED]Tue Jan 21, 2025 8:37 pm
Disregard. Solved by adding the subnet to the wireguard/peer on the 4011 and then added the route.