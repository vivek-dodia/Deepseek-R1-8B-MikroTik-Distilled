# Thread Information
Title: Thread-1116849
Section: RouterOS
Thread ID: 1116849

# Discussion

## Initial Question
Hello everyone, I have a question, I would like to ask for your opinion to make a decision, I want to do full BGP routing, the 1072 doesn't allow it, so I was thinking if I could use the brute force of a server 24 CPUs x Intel(R) Xeon(R) Silver 4116 CPU @ 2.10GHz with 128GB of RAM and a 100Gbps PCI-express card with x86 routers, I have had that idea because I see on social networks that they are promoting and selling x86 hardware with routers indicating that they are more powerful, on the other hand I just saw the CCR2216-1G-12XS-2XQ and I wonder if having this HW offloading will be better? I have consulted several colleagues and we did not reach a consensus, so I turn to you, I will be very attentive to the comments. ---

## Response 1
The issue with "full BGP" routing *in hardware* is that the current full Internet table doesn't fit in anything under $30, 000. The CCR2216 can't fit the whole Internet-table in hardware.The issue with 100GbE and x86 is that is needs VPP/DPDK in order to handle that kind o traffic, regardless of CPU used. And RouterOS has no support for that. ---

## Response 2
If I install ESXI on the x86 server and install RouterOS on it, I could use VPP/DPDK. Thank you very much for your reply. ---

## Response 3
No, it doesn't work that way. You have to run an routing-software that supports VPP/DPDK and make PCIe-passtrough. ---

## Response 4
The CCR2216 can't fit the whole Internet-table in hardware.Since it offloads those routes with most traffic, offloading all routes at all time might be unnecessary (expensive) in most scenarios.CCR2216 can offload 60-120k ipv4 and 15-20k ipv6 routes. So if you're not going to exceed 60-120k ipv4 connections to different prefixes, or 15-20k to different ipv6 prefixes, you should be safe... ---

## Response 5
I was told that CCR2216 doesn't use the L3HW as a cache/acceleration function. The first ~120k routes goes into hardware, the rest stays in software.The most useful would probably be to use the L3HW as a acceleration feature with the most used and active routes. ---

## Response 6
I was told that CCR2216 doesn't use the L3HW as a cache/acceleration function. The first ~120k routes goes into hardware, the rest stays in software.What I do is I tell it to offload the most demanding prefixes and can also be done with as-path with most traffic like prefixes for google, akami, meta/Facebook, amazon and the rest I keep in cpuThe result is many gbps with only around 2-3% CPU ---