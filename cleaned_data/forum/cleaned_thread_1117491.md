# Thread Information
Title: Thread-1117491
Section: RouterOS
Thread ID: 1117491

# Discussion

## Initial Question
Hello!The relevant help page states that the connection tracking table size has a hard limit of 1M (2**20) entries.I have a site where this limit could prove insufficient. For routers with 1G of memory this limit would be quite reasonable, but current ccrs have 4/16G.Is this limit still in place?It is mentioned that the size may increase as needed. Does anyone have experience with this?(When I searched for this in the forum, it was suggested that Mikrotik developers *might* take a look at this - have they?)Many manufacturers (e.g. opnsense) spec their devices with similar amounts of memory for 4/8/16M connections.Best regards. ---

## Response 1
Normally you shouldn't hit this limit even for a loaded box like 1036 or 2116 except for some misconfiguration like your router is on the edge doing NAT and OSPF without area range summary / aggregate things like that is common as a beginner mistake this is one of the scenario i've seen in live environment hitting this max entries having 1000+ active users, just my 0.02 $ ---

## Response 2
Thanks for the take- and I generally agree. I haven't yet gotten close to this limit, hence the questionYes, it would be a NAT box (according to its role, not due to misconfiguration.) Low traffic volume but lots of connections.The problem that I see is that more and more services use udp, with reliability/ordering managed at the application level, and these connections are only evicted with stream timeout. If you lower this below 3 min, you start seeing trouble with some applications (I usually use 6 min.)I know that I can safely tune the timeout, and even without that, it would probably not reach the limit, but it's sufficiently close for me not to be comfortable. If the memory is there, why not use it? Any linux/bsd allows me to set the limit to my liking. Yes, you have to increase the number of buckets, and yes, it is generally good to set it on system startup. But that's it: two sysctl values. And as far as I can tell, with Mikrotik it is the same limit as on v6, whereas typical ram sizes have increased heavily. ---

## Response 3
With EIM-NAT and netmap, Mikrotiks can be pretty good NAT boxes at a price that's hard to beat. I would also like to see max conntrack raised or configurable for the same reasons as OP.That said, I have only seen the hard limit hit once and that was from malware--I now limit client connections to 10, 000 per IP. ---

## Response 4
Although it does not directly solve my problem, limiting connections per ip generally seems to be a sensible idea.Thanks for the pointer! ---