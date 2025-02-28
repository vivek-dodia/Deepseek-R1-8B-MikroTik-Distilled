# Thread Information
Title: Thread-103986
Section: RouterOS
Thread ID: 103986

# Discussion

## Initial Question
Please add support of MPTCP in RouterOShttp://mptcp.info.ucl.ac.be/pmwiki.phphttps://datatracker.ietf.org/wg/mptcp/documents/Thanks ---

## Response 1
MPTCP is an end-to-end protocol, so the router doesn't need to know anything about it in order for it to work - the endpoint (client PC) needs to have two (or more) interfaces on it in order for mptcp to work. If you can route two internal networks with policy-based routing to the Internet via multiple ISPs, then MPTCP would work if your client machine supports it.There is nothing in the spec (as far as I'm aware) on routers inserting themselves into the mix - in fact, there are some crypto-hash sequencing features of the protocol which should prevent a nat router from being able to fidget with a single-thread TCP session and turn it transparently into MPTCP. Otherwise, any malicious router could add channels to TCP sessions and then remove the original stream from the bundle, thus giving them the ability to MITM attack users, or hijack sockets that were opened by legitimate clients and gain access to servers that would otherwise decline access.Of course, the Mikrotik could make use of mptcp itself for fetch operations, winbox access, etc.... but I'm sure that's not what you're looking for. ---

## Response 2
MPTCP is an end-to-end protocol, so the router doesn't need to know anything about it in order for it to workTrue!the endpoint (client PC) needs to have two (or more) interfaces on it in order for mptcp to work.False, as it can be done with one interface and several IPs ad subnets.But MPTCP + simple TCP proxy(like haproxy in TCP mode) would be great so i wont need to create multiple subnets on client and router to make it work.I used MPTCP as client behind my router so it's a bit tricky but possible.With MPTCP support in router+TCP proxy there it would be really great and easy to use ^_^ ---

## Response 3
its more frequently referenced in "high-bandwidth" applications/uses, despite security issues.combined with ad-hoc routing protocols, like HWMP and especially CJDNS - make "networking" Enteriely DIFFERENT in Many respects, thanks to soft hand-over/roaming, WHEN its matured to "secure" state.personally was slightly more care about SCTP future in ROS. and Disabled(yet)ECN support in ROS, that render other tech such as DCTCP not working aswell.or buggy/quirky linux netfliter processing of TCP handshakes/negotiation, caused both performance and more importantly, security issues(which isn't MT work, but eventually affect ALL of use, depending on that toolchain and kernel and logic, performance, concerning, thus). ---

## Response 4
Two big use cases for MPTCP are link aggregation (load balancing) and link redundancy (fail over).While it is true it is end to end, it does not mean that it cannot be useful starting from the router.How ?On the "aggregation" router, establish a TCP tunnel with a "provider" router. If both endpoints of the tunnels are MPTCP-enabled, then the tunnel will use any links configured for MPTCP. Then you just have to simply route customer traffic over that TCP tunnel, just like with any other tunnel.Since Mikrotik implements OpenVPN TCP or SSTP, it can use MPTCP.Many companies that use MPTCP as described do it with Linux-based "blackboxes":-https://www.ovhtelecom.fr/overthebox/(funny, there is a Mikrotik Cloud Router Switch on the picture)-http://www.linefactory.net/-http://www.tessares.net/Why does it make sense to add MPTCP to RouterOS ?Current implementations are meant to be an addition to the existing routing infrastructure. You add the MPTCP device in front of the current router and use it as the gateway of the existing router as if it were a new and unique ISP.With RouterOS, the existing router could do the TCP tunnel and the aggregation using MPTCP, so no extra hardware. ---

## Response 5
I agree+1 ---

## Response 6
Then you just have to simply route customer traffic over that TCP tunnel, just like with any other tunnel.Bad idea. Any tunnel over TCP solution is bad (and should only be used if nothing else works for any reason). Read what TCP over TCP meltdown problem is. ---

## Response 7
makes all the sense to support from my pov. As example to setup VPN server in Mikrotik with MPTCP to manage different links (can be a local ISP connection and 5G connection).Where we are in the MPTCP at Mikrotik? ---

## Response 8
MPTCP is necessary only on the end devices unless it was a specific service in ROS that you were considering? ---

## Response 9
On the subject of the period table element, 'UNOBTANIUM",I would like to make the request to add...... drumroll please..............." DPI of encrypted packets " ---

## Response 10
... drumroll please..............." DPI of encrypted packets "Would make the gear very expensive and not their market ...Yes it would be very nice to have but all the Cheap Basterds that love this TiK would have to go elsewhere for an adorable solution ... ---

## Response 11
You are absolutely right. I am looking forward to MPTCP integration in RouterOS. This will give Mikrtotik a strong competitive edge ---

## Response 12
Hey @8023, what's your use case?MPTCPdoesn't need any special support in the router itself, it's generally used between the app connection endpoints like from a mobile device or car to a central service. ---

## Response 13
@Larsa what folks are talking about is using MPTCP for "multi-wan" support.So the way I view the request is that MPTCP can be used a tunnel interface between two RouterOS using multiple/different paths. e.g. you had Mikrotik with two LTE modems, that connected to CHR at some VPS, with MPTCP sub-flows per modem to the VPS.While 100% agree with @Larsa's point... MPTCP was not designed to be middleware in a router. And there are not RFCs for that either. It was for apps at a higher ISO layers than a router to use. Apple's Siri being the quintenstial example of MPTCP usage. i.e. iOS creates MPTCP sub-flows for BOTH cell and wi-fi to lower latency to cloud by using ALL local interfaces... So if wifi was RouterOS, it does not care if it just a sub-flow MPTCP since that's how MPTCP should work.I get if RouterOS wi-fi router had multiple WANs, an iPhone wouldn't know the wi-fi itself had multiple paths since to iPhone it's all wi-fi. But there is no standard for advertising upstream interface in MPTCP. So I'm not sure what Mikrotik can do since the MPTCP standard are designed so it passes through "normal" routers, which it does.So if we come to the "use cases"...Two big use cases for MPTCP are link aggregation (load balancing) and link redundancy (fail over).I'd agree that RouterOS does lack any "bonding" support for asymmetric WANs (e.g. multiple LTE modems). And I get the use general use case to combine multiple WAN to make one bigger WAN. But I'm not sure MPTCP be the most efficient nor best way to do it.And failover is totally possible today and doesn't involve MPTCP, so that part is confusing to me.Plus there is /container, so any of the existing MPTCP proxys/tunnels/etc things for Linux should run as a container if one wanted to experiment. ---

## Response 14
Well, L3 multipath/bonding shouldn't be mixed up with MPTCP which was mainly developed as an endpoint (app) protocol to facilitate transparent handover/failover/bonding.Sure, there are some special hacks to use it as a more general communication protocol but that's not very common ie you won’t find it as an checkbox option to enable on any major brands.https://www.cisco.com/c/en/us/support/d ... cp-00.htmlhttps://datatracker.ietf.org/doc/html/rfc6824https://en.wikipedia.org/wiki/Multipath_TCP ---

## Response 15
Isn't this the very thing that is done with peplink?I think usecase can be very good for critical services u want to protect and give high availability without having to do it on each server. ---

## Response 16
Peplink does not use MPTCP to do WAN bonding. While possible to do same WAN bonding using subflows and proxy, the standards around MPTCP aggregation are all about client-server communication, not networking bonding. And, I'm not sure there is too much value in /tool/fetch being MPTCP aware which is the original use cases conceived by the RFCsCloudflare's blog recent posted an article about MPTCP does a good walk-through how it work:https://blog.cloudflare.com/multi-path- ... at-a-time/with the conclusion being roughly same as the thread:In my opinion for any serious out-of-the-box use case, we're not there yet. I'm optimistic that Linux can develop a good MPTCP client story relatively soon, and the possibility of implementing the Path manager and Scheduler in BPF is really enticing.Time will tell if MPTCP succeeds — it's been 15 years in the making. In the meantime, Multi-Path QUIC is under active development, but it's even further from being usable at this stage.We're not quite sure if it makes sense for Cloudflare to support MPTCP. Reach out if you have a use case in mind! ---