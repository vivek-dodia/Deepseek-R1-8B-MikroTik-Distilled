# Thread Information
Title: Thread-210301
Section: RouterOS
Thread ID: 210301

# Discussion

## Initial Question
Hey all, I have an XGS-PON 8/8Gbit connection via my ISP, using PPPoE through an SFP+ module in my CCR2116.The best I can seem to get in throughput is 2.5 Gbit/s. I know the connection can do more, but I can't figure out what the bottleneck is on the network.If I bypass my Mikrotik completely I get substantially higher speeds.I know doing multi-gig isn't super common place yet, especially on PPPoE, but I'm hoping someone out there knows what might be the cause of this. ---

## Response 1
Did you solve this? I have a similar problem with a pppoe connection, only the link should be 1G but i can squeeze down only 400M ---

## Response 2
Bottleneck is probably because PPPoE is a single-threaded process stuck on 1 CPU-core (out of 16) when it comes to encapsulation/decapsulation and therefore you are probably hitting its limit. ---

## Response 3
Take a look at the port speed. 2, 5Gbps is a classical option. Maybe your XGS-PON is synchronized at 2, 5Gbps? ---

## Response 4
how much is your throughput without PPPoE ? ---

## Response 5
Did you solve this? I have a similar problem with a pppoe connection, only the link should be 1G but i can squeeze down only 400MNo, I never did. I'm still stuck at 2.5ish Gbps. It seems to be because PPPoE is single threaded on RouterOS, and as a result only a single core is used and it hits 100%. ---

## Response 6
Take a look at the port speed. 2, 5Gbps is a classical option. Maybe your XGS-PON is synchronized at 2, 5Gbps?No, this is definitely not it. It's PPPoE slamming out only a single core. ---

## Response 7
how much is your throughput without PPPoE ?Pretty close to line speed.I picked up a TP-Link router that can easily max out the connection because it does hardware offloading of PPPoE. Unfortunately it's a TP-Link router so it doesn't do what I need it to do. ---

## Response 8
So why on my RB5009 PPPoE getting 2.0Gbit/s (full speed) with just 20% CPU load and almost all cores are equal?viewtopic.php?t=213701 ---

## Response 9
The bottleneck is likely due to the PPPoE process being CPU-intensive, especially at multi-gigabit speeds. The CCR2116, while powerful, may still struggle with PPPoE at such high throughputs due to single-threaded limitations of the PPPoE process in RouterOS.To improve performance, try the following:1. Enable FastPath or FastTrack: These can offload traffic processing and increase throughput, though they may not work with all configurations.2. Optimize Firewall Rules: Reduce unnecessary rules or re-order them to minimize processing.3. Offload PPPoE: If possible, terminate PPPoE on another device or consider using a hardware PPPoE accelerator.4. Update RouterOS: Ensure you're on the latest version, as performance improvements are regularly introduced.5. Check MTU Settings: Verify that the MTU is optimized for your ISP's requirements.If these steps don't resolve the issue, the CCR2116 may not be ideal for handling multi-gigabit PPPoE connections, and a more specialized solution might be necessary. ---

## Response 10
PPPoE is horrible unfortunally and RouterOS has no hardware-offload for it. It's strange some ISPs hold on to 20 year old concepts. ---

## Response 11
It's strange some ISPs hold on to 20 year old concepts.I guess it suits them well for a few purposes ... one of them is user management (less fuss to e.g. assign static IP address and IPv6 prefix). And obviously they don't bother about (under)performance of 3rd party routers, they just care about performance of "their" equipment (ISP-provided CPEs/routers and certainly their PPPoE servers).I guess no new ISP starts their network with PPPoE ... but for legacy ISPs it might be a big step to ditch it (a huge disturbance in their operations for dubious gains). ---