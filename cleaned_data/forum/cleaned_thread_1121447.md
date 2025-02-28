# Thread Information
Title: Thread-1121447
Section: RouterOS
Thread ID: 1121447

# Discussion

## Initial Question
I'm trying to figure out why L2TP or OVPN connections are slow for TCP when device CPU is not overloaded. I setup a test using UDP OVPN between two routers. The routers are directly connected via 1Gb ethernet port. I setup the OVPN client to use null auth and null cipher.Client Router - CCR2004 (ROS 7.16.2)Server Router - CCR2116 (ROS 7.16.1)When I run a bandwidth test between them (both directions) from Client router, I get:TX/RX Total Average: 396.5 Mbps/62.8 MbpsClient router CPU during test:# CPU LOAD IRQ DISK0 cpu0 31% 11% 0%1 cpu1 47% 19% 0%2 cpu2 45% 30% 0%3 cpu3 44% 13% 0%Server router CPU during test:# CPU LOAD IRQ DISK0 cpu0 3% 0% 0%1 cpu1 1% 0% 0%2 cpu2 3% 0% 0%3 cpu3 6% 0% 0%4 cpu4 0% 0% 0%5 cpu5 8% 0% 0%6 cpu6 33% 21% 0%7 cpu7 7% 0% 0%8 cpu8 5% 0% 0%9 cpu9 2% 0% 0%10 cpu10 6% 0% 0%11 cpu11 1% 0% 0%12 cpu12 3% 0% 0%13 cpu13 4% 0% 0%14 cpu14 56% 31% 0%15 cpu15 0% 0% 0%What is the bottleneck causing these devices with ~50% free CPU to not handle more traffic? I have tried:- Added a change MSS rule applied to the TCP traffic to set MSS at 1400 or 1360.- Tried connection count of 20, 40 and 80. No significant difference between these ---

## Response 1
Slow L2TP or OVPN performance for TCP traffic often results from a combination of protocol inefficiencies, network conditions, and system configuration. By understanding and addressing the specific causes, such as TCP-over-TCP issues, MTU mismatches, or encryption overhead, you can significantly improve connection speeds. Consider modern protocols like WireGuard for performance issues. ---

## Response 2
In regard to flintham's suggestions:1. TCP-over-TCP issues - This is a UDP tunnel so there is no TCP over TCP2. MTU mismatches - MTU is 1500 on upstream connection. MSS on TCP bandwidth tests was restricted to reserve 100 bytes to VPN overhead which is more than enough for this protocol3. Encryption overhead - Encryption is disabled on the tunnel4. Consider modern protocols like WireGuard for performance issues - This is not helpful. Wiregard requires static IP address on both ends. I run thousands of tunnels from locations without static IP addresses and am looking for a way to improve speed on these. It would require a large cost to convert and this makes no sense when there is clearly some kind of unnecessary software bottleneck contributing to this problem. ---

## Response 3
4. Consider modern protocols like WireGuard for performance issues - This is not helpful. Wiregard requires static IP address on both ends.No, it does not:https://www.wireguard.com/#built-in-roaming ---