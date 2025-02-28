# Thread Information
Title: Thread-205278
Section: RouterOS
Thread ID: 205278

# Discussion

## Initial Question
I have a conceptual question regarding WireGuard in a multi-WAN environment using dynamic addresses.Problem: in ROS, when a passive WireGuard peer receives its initial handshake (i.e., when connection-state = new), the state machine doesn't keep track of either the destination address or the inbound interface. Consequently, the peer sends its handshake reply through the default gateway which breaks functionality in a multi-WAN environment where the ingress and egress addresses must match. This also renders Mangle Connection Marking useless for WireGuard since the handshake must complete before the connection state becomes established.Question: are there any smarter and cleaner ways to handle policy routing for dynamic WAN addresses, rather than relying on a shaky DHCP script to set the /routing/rule src-address for each interface table?ps...EDIT: By shaky, I mean that the script might break if a developer once again and completely unnecessarily decides to change the script compatibility (as someone did with the date format).Note to myself: ask r&d to add src-interface as a routing rule option. ---

## Response 1
It is not clear what scenario you are talking about, no diagram?? no config ??Seriously, what do you mean when a passive peer receives its initial handshake.What do you mean by passive?What do you mean by peer?The wireguard peer ( client for handshake) aggressivelyy sends out a wireguard handshake and its the peer (server for handshake) that receives the in coming traffic.If you are talking BTH scenario, best handled by someone who uses it.If talking standard wireguard, this is the exact reason you have mangle rules to ensure traffic to WANX, then leaves the router on WANX, pretty standard fare.Do you want the input / output version , or the preouting /output version ??? ---

## Response 2
G'day Anav, my sincere apologies if this is a bit to complex for you!I meant precisely what I wrote: a conceptual question regarding issues with the internal WireGuard handshake process in a multi-WAN environment with no specific scenario in mind.One challenge with the WireGuard initial handshake is that it occurs in the "new" connection state, ie before connection tracking is established. This means regular connection tracking mechanisms like connection marks won't help manage inbound/outbound traffic to complete the handshake and setting the connection state to "etablished". The bottom line is that connection and routing marks are of no use at all when it comes to setting up passive (inbound) multi-WAN WireGuard tunnels.Also, without policy-based routing all initial WireGuard handshake replies will be sent through the standard default route resulting in a mismatch if it originates from another WAN address (similar to asymmetric routing issues).Feel free to read my queston again, and then you are more than welcome to return with questions focusing on the handshake process issue and a possible "cleaner" policy routing without scripting, which was my primary objective with the question.EDIT:By Passive Peer I mean a WireGuard Peer without a configured endpoint address that will passively wait for an incoming connection. ---

## Response 3
Perhaps you should use more standard terminology vice the magical language you learn at Santa HQ.Your question has been answered, its only you that remains in the dark.I have no problems mangling to ensure Wireguard connections respond appropriately.As a matter of fact even in a failover situation with two reachable public IPs the aggressive peer will still find the secondary receiving peer as long as one has setup the mangling properly there is no issue. ---

## Response 4
Thanks for the response but that wasn't a particularly good suggestion for a cleaner policy routing to address the issue with multiple WAN addresses.As I've mentioned several times now:1) you are not able to make use of mangling during the handshake process until it is completed.2) To complete the handshake, you need proper policy routing to avoid asymmetric routing issues when using multiple wan addresses.3) Once the handshake is completed and the session state is 'established', you have no use for mangling anymore.4) Bottom line, you have no use for mangling at all in a multi-WAN WireGuard environment with passive peers.Did you really understand what I meant, or are you just happy to have an adult conversation? ---

## Response 5
I guess I dont understand your point then, wish I could help but its beyond my knowledge scope. ---

## Response 6
I guess I dont understand your point then, wish I could help but its beyond my knowledge scope.It isn't that complicated. Here's a brief illustration of how the issue with WireGuard differs from a built-in service like FTP that works as expected.Let's use a couple of examples to show the handshake process flow for two different services on a router equipped with three Internet-facing WAN ports: WAN1 (IP 111), WAN2 (IP 222), and WAN3 (IP 333), where WAN1 is the default gateway.Example 1 - An FTP client connects to the router's built-in FTP server using WAN3 (which is working as expected)The FTP client opens TCP port 21 on WAN3, initiating the TCP handshake (TCP SYN) sent to the input chain. Information about the inbound interface and its associated address is stored internally.The router sends back a TCP handshake reply (SYN-ACK) to the FTP client using the stored information. This means egress occurs through WAN3 with the source address 333, as intended.When the TCP handshake process is complete, the connection state is set to 'established' by the connection tracker.Example 2 - A WireGuard client initiates a connection to the router's WAN3 interface (not working as explected)A WireGuard client sends a handshake initiation packet to the router's endpoint (port 15200). This packet is sent down the input chain, and information about the inbound interface and its associated address is stored internally.The router sends a handshake response packet back to the client. However, the stored information about the inbound interface is not used, meaning the output chain assigns the default gateway (WAN1) as the outbound interface with the egress IP address 111.The WireGuard client rejects the response packet since the IP address 111 doesn't match the initiation packet's IP address 333.The only way to make the handshake process complete in step 2 above, is to use routing rules to force the routing back to WAN3.EDIT: This cannot be fixed with connection and route marking because the connection state is still ongoing, i.e. state "new". The handshake process must first complete with the connection state set to "established" before mangling can be utilized (Catch-22!).IMO, this design seems flawed. It's likely caused by a developer mistakenly omitting the interface source address setting. ---

## Response 7
I'm sorry, but I don't understand what you mean by "user/group policy" and "User333 belongs to vpn333 group connect to wan333" ?? How does this in any way relate to the asymmetric routing issues that I described earlier in example 2? ---

## Response 8
Let me just start by stating, that in general, DSTNAT ( normal port forwarding), in your simple case works quite the opposite.Incoming traffic to a LAN server on WAN3, via DYNDNS URL (or Ip itself) where WAN1 is the primary WAN will fail.The return traffic will go out WAN1, the original sender will drop the return traffic as the source address on the return is different from the destination address.In other words, regarding traffic leaving the router, routes prevail!!Or stated differently, internal connection tracking is for internal purposes NOT for deciding where traffic leaves the router.Hopefully we have dispelled illusions and myths that you operate within.I am hesitant to say this is fully the case with your FTP example because it was not clear whether or not you use the FTP ALG and I am unsure of what other side functionality that may or may not include. I tend to think that it should be the same as Ive described above, but its a very edge case I am not as confident about.The methodology to ensure LAN servers return traffic to the same WAN it came in on is straight forward.:add chain=forward action=mark-connection connection-mark=no-mark in-interface=WAN1 \new-connection-mark=external-ISP1 passthrough=yesadd chain=forward action=mark-connection connection-mark=no-mark in-interface=WAN2 \new-connection-mark=external-ISP2 passthrough=yesadd chain=forward action=mark-connection connection-mark=no-mark in-interface=WAN3 \new-connection-mark=external-ISP3 passthrough=yesadd chain=prerouting action=mark-route connection-mark=external-ISP1 in-interface-list=Servers \new-routing-mark=use-WAN1 passthrough=noadd chain=prerouting action=mark-route connection-mark=external-ISP2 in-interface-list=Servers \new-routing-mark=use-WAN2 passthrough=noadd chain=prerouting action=mark-route connection-mark=external-ISP3 in-interface-list=Servers \new-routing-mark=use-WAN3 passthrough=no/routing table add fib name=use-WAN1/routing table add fib name=use-WAN2/routing table add fib name=use-WAN3/ip routeadd dst-address=0.0.0.0/0 gateway=ISP1-gatewayIP routing-table=use-WAN1add dst-address=0.0.0.0/0 gateway=ISP2-gatewayIP routing-table=use-WAN2add dst-address=0.0.0.0/0 gateway=ISP3-gatewayIP routing-table=use-WAN3NOTE:One can use either forward chain or prerouting for marking connections. ---

## Response 9
Wireguard handshake is a completely different animal, in this case the return traffic is NOT coming from LAN servers but from the router itself.However the same logic applies, if the WG initiates a handshake on WAN3, with WAN1 being primary.................then the handshake will fail.Again easily fixed...........add chain=input action=mark-connection connection-mark=no-mark in-interface=WAN1 \new-connection-mark=external-ISP1 passthrough=yesadd chain=input action=mark-connection connection-mark=no-mark in-interface=WAN2 \new-connection-mark=external-ISP2 passthrough=yesadd chain=input action=mark-connection connection-mark=no-mark in-interface=WAN3 \new-connection-mark=external-ISP3 passthrough=yesadd chain=output action=mark-route connection-mark=external-ISP1 \new-routing-mark=use-WAN1 passthrough=noadd chain=ouput action=mark-route connection-mark=external-ISP2 \new-routing-mark=use-WAN2 passthrough=noadd chain=ouput action=mark-route connection-mark=external-ISP3 \new-routing-mark=use-WAN3 passthrough=no/routing table add fib name=use-WAN1/routing table add fib name=use-WAN2/routing table add fib name=use-WAN3/ip routeadd dst-address=0.0.0.0/0 gateway=ISP1-gatewayIP routing-table=use-WAN1add dst-address=0.0.0.0/0 gateway=ISP2-gatewayIP routing-table=use-WAN2add dst-address=0.0.0.0/0 gateway=ISP3-gatewayIP routing-table=use-WAN3NOTE:One can use either input chain or prerouting for marking connections. ---

## Response 10
@wfburton, please create a seperate thread if you are not intressed in this specific topic.@Anav, all that dst-nat, prerouting, and connection marking stuff you posted about is completely irrelevant when it comes to the handshake dilemma. Are you sure you understand where the issue occurs according to example 2?And as I've tried to explain several times earlier, during the initial handshake, the connection and route marking are useless since the handshake process is still ongoing (i.e when connection state is "new"). The handshake process must first complete and then the connection state set to "established" before mangling takes effect (ie no complete handshake, no use of mangling)In order to facilitate the handshake to complete in a multi-WAN environment (when the inbound interface is not the default gateway) youMUSTuse policy routing; otherwise the response packet is handed out through the default gateway which makes the handshake fail it the. Okay?And on top of that, you have to cope with dynamic IP addresses on the WAN interfaces. I'm intrigued by what your "easily fixed" solution will look like. ---

## Response 11
Yup, of course if its dynamic, extra work is required, but remember pppoe dynamic, a script is not normally required, pppoe-out1 suffices !!!The router is working as designed.Mangling ( marking connections and marking routes )works just fine for Wireguard handshakes.Please join the borg!It would appear your inventing issues that simply dont exist ?? ---

## Response 12
Well, NO! but let me get back to you with a full trace FYI.I dare you to set up your own lab environment with just two WAN interfaces and test it yourself. You don't have to bother using dynamic IP addresses. The task you are to perform is to connect a WireGuard client with a fully functioning connection (handshake ticking) to a WAN interface that is not the default gateway and without policy routing. Then show me that "easy fix".Btw, you didn't answer my question if you understand the root cause as in example 2? ---

## Response 13
Sorry WB, not a clue why you are showing logs of I dunno what.As for Larsa, If I connect to a WAN interface with distance 3, without any other rules setup, there will be no tunnel established.The only thing that using an improperly configured setup accomplishes is that the peer client will reach the WAN with distance 3, a handsshake will ensue, and then the return traffic will die a quick death. The return traffic will get rejected by the peer client device upon arrival as the source address is not recognized and will be dropped hence no tunnel.Nothing surprising at all, that just normal routing behaviour and normal responses. ---

## Response 14
The question is far to general. Could the sky be blue? Sure if its daytime and not obscured by clouds ???There is no one size fits all approach.Depends....... mostly on the DETAILED requirements for desired traffic flow for users/devices. ---

## Response 15
In order to facilitate the handshake to complete in a multi-WAN environment (when the inbound interface is not the default gateway) youMUSTuse policy routing; otherwise the response packet is handed out through the default gateway which makes the handshake fail it the. Okay?And on top of that, you have to cope with dynamic IP addresses on the WAN interfaces. I'm intrigued by what your "easily fixed" solution will look like.Never throught about this. Same problem in ZeroTier (and IPSec) — the tunnel establishment part get's tricky through the packet flow diagram. So kinda make sense that WG handshakes are "before new".It is a bit unclear. So all works okay today & you're basically looking foralternativesto a DHCP script. And it's WAN DHCP clients that do do some update to /routing/rule? And...the underlying concern is your script could break, unexpectedly, if Mikrotik decide to change something in scripting. If so, I share the latter worry & I know scripting pretty well. One wrong/tiny change to how scripting works in future could cause all WANs not to work...Now I'm not sure of alternatives. Other than potentially worse/complex things, that may not work, generally using some indirect private IPs (recursive routes in reverse, MACVLAN and bridge nat, etc.). I think it be better to "harden" the DHCP script (e.g. handle all error cases, carefully check/convert types e.g. always use a :tostr :toip etc.).But the DHCP client could use some "built in" things — since scripting something critical like WAN IPs and default routes add more risk than a config setting.... e.g. I put a feature request a while back for a "default-check-gateway" option in DHCP client — so you can avoid scripting just to add the check-gateway=ping to the default route. Still waiting...The secondary issue is exactly how the WG handshake is handled is not cover by Packet Flow diagram: ---

## Response 16
The WG crypto routing engine is not detailed in the flow diagrams.THere is no issue with dynamic IPs for WANs, as a persons dyndnsURL will keep the WANIP relevant if it changes and I believethe crypto routing process will keep the client peer in step with the new WANIP...........Also take a scenario where WAN1 is primary and WAN2 is secondary, and WG tunnel is established via WAN1, and WAN1 drops off line.The WG process will switch the client peer to WAN2 automatically is my understanding. Also outside the MT flow diagrams.Built-in RoamingThe client configuration contains an initial endpoint of its single peer (the server), so that it knows where to send encrypted data before it has received encrypted data. The server configuration doesn't have any initial endpoints of its peers (the clients). This is becausethe server discovers the endpoint of its peers by examining from where correctly authenticated data originates. If the server itself changes its own endpoint, and sends data to the clients, the clients will discover the new server endpoint and update the configuration just the same. Both client and server send encrypted data to the most recent IP endpoint for which they authentically decrypted data.Thus, there is full IP roaming on both ends.Note: on flow diagrams, we use output chain to keep WAN traffic within WANs as that is the last step at which to affect change in routing from the router itself. ---

## Response 17
I think the issue is other side also knows about the 3 WANs – it's not a smartphone/desktop wanting VPN access. It's the far-end wants to steer some traffic down a particular WAN(s), that may not be the "primary"*. I don't think DDNS/etc solve this issue —somehowthe dynamic public IP address needs to make it into a /routing/rule. And /routing/rule is based on IP/subnetwithoutany address-list or interface-list support... so options are limited.Perhaps an example: have some VPS with CHR, and that's where these 3 WAN WG tunnels go to then route from VPS. Then say you want to manually use one of the non-primary WG tunnels for management from VPS to the 3xWAN-Mikrotik. And it's there where you need the policy rules – you need to match the dst-address, to put the heartbeat in the right routing table to go back to same one it came in on.@Larsa, even if theoretically, some diagram of topology would help here.Ifthere is some better solution ... a picture may help find it.*FWIW, you'd have an even worse problem with ECMP routes, than three WANs with different distances case, since it be random which one it uses. Updating /routing/rule based WAN dst-address does fix both, bu ---

## Response 18
@Anav, unfortunately you're still missing the point but Ammo seems to grasp it.In short, ROS connection tracker mishandles WireGuard handshakes. It forces response packets through the default gateway, breaking the protocol if the initial handshake came from a different interface. See Example 2 for reference.ROS connection tracker, which monitors inbound interfaces and addresses, is based on standard Linux functionality customized by the Mikrotik developers using features like connection tracker "helpers" and "hooks". On a regular linux machine, this can be accomplished using flexible configuration files but since ROS is locked there are no other alternatives than using separate routing policys for each and every WAN interface. ---

## Response 19
Well, on Linux, WireGuard also makes heavy use of scripts and routing rules. If you look at the bash script for wg-quick, maybe the DHCP rule doesn't look so bad.Perhaps there is bug here... in RouterOS, @anav's logicshouldhold true for a tunnel/interface. But WG needing /routing/rule on RouterOS is not surprising either... since that's how it works on Linux (e.g. you do not use the firewall/conntrack/etc to configure WG). ---

## Response 20
One wouldn't need specialized DHCP scripts if Mikrotik fixed its connection tracker to use the incoming interface address as the outgoing source address.I'll try to create a simple diagram and some packet traces that illustrate the whole thing, but considering your previous response you seem to have understood the basic idea.ECMP routes are good example of ROS lacking sufficient flexibility or perhaps simpler tools to manage seemingly simple routing problems. Just something as simple as using logical interfaces instead of addresses would make things much easier. With routing rules, one would like to be able to add interfaces as sources like this: /routing/rule add action=lookupsrc-interface=ether2table=ether2 ---

## Response 21
Well... If you're looking for affirmation there is a potential bug... @anav should be right on the logic, but I believe your results.The whole idea is RouterOS abstracts away Linux kernel details into the unified config scheme and packet flow diagram. Here, I suspect it's the kernel doing the keepalive internally and it's using the kernel's routing table to do it. And since kernel does know about routing rules, it's why those work. Since Mikrotik builds the kernel, the behavior is under their control.I'll try to create a simple diagram and some packet traces that illustrate the whole thing, but considering your previous response you seem to have understood the basic idea.It's not me you'd have to convince, but likely Mikrotik in a bug report. And they won't believe anything without supout.rif and ideally some traces. ---

## Response 22
Similar things happen on ZeroTier, where it's tunnels (e.g. "zt1" instance/process) do appear in the firewall... but without an interface e.g. (unknown) — since there the outer VL1, not the zerotier1 inner traffic (where zerotier1 does appear as interface in firewall). Peers are dynamic, but constructing firewall marking rules from /zerotier/peer via script would be error-prone at best. But this make doing QoS on ZT'stunnelsgoing out specific WAN where there really isn't a solution. (You can QoS zerotier1 but it's too late if the idea to favor ZeroTier's tunnels out specific WANs.Also other stuff like PMTUD happens entirely in kernel without touching firewall – stuff like this make sense. So make similar sense that WG keepalive be in kernel – but this has the side-effect you find here...But these "escapes" from firewall connection tracking should, at least, be documented. ---

## Response 23
I'm pretty sure the standard response would be it's a feature, not a bug!But it is the kernel that actually stores, manages, and executes the routing rules using nftables, it's just the configuration hassle that occurs in userland, i.e. ROS. The connection tracker is tightly coupled to the nftables routing engine.Assume that connection tracking wouldn't work for any of ROS's built-in services like WinBox, OSPF, BGP, etc. In a multi-WAN environment, you would then need to set up policy routes for each WAN interface and individual service that doesn't arrive through the default gateway.A purely philosophical question then arises: is this a bug or just a very flexible router? I mean, after all, it can still be fixed even if it becomes very cumbersome every time you need to add or modify a WAN interface.. ---

## Response 24
A purely philosophical question then arises: is this a bug or just a very flexible router?Both? ---

## Response 25
Haha, but of course! My personal take on this is that all built-in services should behave the same when it comes to routing and connection tracking. I see no obvious reason why they shouldn't. ---

## Response 26
Assume that connection tracking wouldn't work for any of ROS's built-in services like WinBox, OSPF, BGP, etc. In a multi-WAN environment, you would then need to set up policy routes for each WAN interface and individual service that doesn't arrive through the default gateway.These built-ins do start/end from userland. WG is mainly in kernel.And why I do see ZeroTier tunnels and probes in firewall connection – ZT is also in userland.But I 100% agree WG should be treat same as rest. ---

## Response 27
@ AMMO, I did not know you were a fiction writer. ;-PI think the issue is other side also knows about the 3 WANs – it's not a smartphone/desktop wanting VPN access. It's the far-end wants to steer some traffic down a particular WAN(s), that may not be the "primary"*. I don't think DDNS/etc solve this issue — somehow the dynamic public IP address needs to make it into a /routing/rule. And /routing/rule is based on IP/subnet without any address-list or interface-list support... so options are limited.The client peer has no shmucks about 3 wans. It only knows what IP address (or potentially dyndns url) that is sitting in the Allowed IP settings along with a port.Beside its not how wireguard is designed which as I stated above is for the peers to continue communicating to each other about the endpoints, after establishing the initial tunnel!@LARSAWhy are you trying to inform ROS how to behave instead of accepting how it behaves and working from that realistic contsruct??In short, ROS connection tracker mishandles WireGuard handshakes. It forces response packets through the default gateway, breaking the protocol if the initial handshake came from a different interface.WRONG!, RoS is acrtually following correctly its Operating System code on how to route traffic. Its your unreasonable expectation that MIkrotik would create additional code, not in the Wireguard Design, to take into account every possible scenario. One simply uses the available tools to move traffic as necessary. As Ammo alluded to, others have designed ADDITIONAL helper programs to streamline such additional ( although agree common sense ) functionalities. Personally, I think MTs work at BTH is far more important and groundbreaking and useful!!!A basic script for IP routes ( gateway IP ) is not much of a bother and necessary when one cannot know the future WAN information. It does not affect fixed static IPs, or pppoe-out1 interfaces, and even my straight cable connection works great. Its just some IP DHCP client setups (like my fiber connection) need help.My conclusion, is that you will be happier to sticking toopen sourcelinux based routers! ---

## Response 28
@ AMMO, I did not know you were a fiction writer. ;-PI just believe in Santa Claus.To @anav's point, WG is trying to create it's own peer-to-peer tree, so you are "fighting" WG when trying to get Mikrotik involved in it's routing. It was designed to use route rules.My conclusion, is that you will be happier to sticking toopen sourcelinux based routers!Or, just use IPSec with IKEv2 in tunnel mode – I believe – that would let you do this "script-less" using IPSec. But WG was invented since configuring IPSec is hard... but that likely be "script-less", perhaps even faster depending on router.I get @Larsa's frustration. Multi-WAN is unnecessarily hard. Pepwave sell routers for 3X the $$$ at same performance as Mikrotik & all they do put a friendly HTML with dropdown to pick all the "MultiWAN" stuff. Not suggestion Mikrotik change WG to fix @Larsa's issue – but all the approaches involve some fragile things, somewhere. And idea with having multiple WANs is to INCREASE reliability...My conclusion is just always "pick-your-poison" with Multi-WAN. The RFCs really never conceived of "Multi-WAN", outside of BGP in E2E world - so there not some standard to guide how this should work. ---

## Response 29
@anav: RoS is acrtually following correctly its Operating System code on how to route traffic.I'm sorry, but there is no such thing! The Linux network engine is configured and controlled dynamically entirely by ROS. That's how Linux-based routers operates. It does whatever you tell it to do. If you instruct it to behave badly, it will. And the WireGuard handshake is behaving badly.Btw, I'm testing another workaround besides policy routing as we speak but I'm not done testing just yet. How about that 'easy fix' you promised me? ---

## Response 30
Well its not a fix, its simply using the tools available properly (already posted in detail )By the way in a three WAN scenario where 1 fails to 2, fails to 3.If the wireguard is set to look for WAN1 to establish an initial handshake connection, and does so, then WG will gracefully handle any combination of WAN failures............Its only if the starting point initial handshake connection is not to the primary WAN, that we need to do some funky stuff. ---

## Response 31
Yup, it's the starting point itself that creates the initial hurdle in a multi-WAN environment.I'm trying to identify how different configurations behave, for example by using different subnets on the WAN interfaces.One test I've performed is with ether1 as the default gateway and five WAN interfaces on a separate subnet. Suddenly, one of the WAN interfaces sends the response packet back the proper way which completes the handshake, while the rest is sent through the default gateway (and the handshake fails). Very strange! There's probably a logical explanation for this, but it's about finding the root cause that might be pretty cumbersome. I plan to make a clean install to see if I can repeat this behavior. ---

## Response 32
WireGuard, like IPsec, doesn't appear as a service like FTP, they have separate configuration menus. Btw, what are you trying to say using the VyOS commands? ---

## Response 33
You'll probably have a greater chance of getting assistance in connecting VyOS with ROS if you open a separate thread for it. ---

## Response 34
If using public ip's wouldn't this work?And that's the rub here... They're public IP, but may change since via DHCP. So some static Linux route rules need to get updated when that public changes (where in VyOS or RSC). The solution (on RouterOS) is to use a script from within DHCP client to update the /routing/rule if those public changes. @Larsa AFAIK is trying to avoid using a DHCP script. ---

## Response 35
Yep, that sounds about right! The whole exercise has currently resulted in two different issues:Q1. Why are WireGuard handshake responses sent through default gateway rather than the originating interface?My initial research indicates this is a known issue with some proposed fixes already sent upstreams to the WireGuard devs. Additionally, there are some workarounds that help the connection tracker with proper routing. I'll get back when something interesting pops up.Q2. Is there a convenient workaround for the above issue that doesn't rely on a DHCP script when multiple WAN interfaces with dynamic IP addresses are used as WireGuard responders? Well, currently this seems pretty difficult since ROS route control is purely based on static IP addresses rather than the logical interface names that are available in the kernel (e.g. "ip rule add fromDEVICEtable table-name"). However, I've got an idea that I haven't had the chance to test yet. ---

## Response 36
Well I think you've distilledthe core issue here:ROS route control is purely based on static IP addresses rather than the logical interface namesthat are available in the kernel(e.g. "ip rule add fromDEVICEtable table-name").The route rules are easier than firewall things in general IMO. But what you lose is the address-list and interface-list... Even just an plain interface ("DEVICE") matcher in /routing/rule would go a long away. ...assuming kernel does know about interface (since it's curious Mikrotik didn't include it already).The other issue in "dynamic WAN address, without using scripting" category is "check-gateway=ping". It is having one tiny setting in the /ip/dhcp-client that could add a check-gateway=<ping|bfd> to the dynamic default route added by DHCP (e.g. check-gateway=ping). That gets even more in the way of "script-less" multiwan setup (with DHCP WANs). ---

## Response 37
@wfburton/Amm0, I have a similar idea that doesn't involve separate routing tables. ---

## Response 38
I don't known what version your running but keep an eye out for check gateway options. It has one for ping.Of course. BUT again you need use astaticroute to set. e.g. the check-gateway=ping cannot be added todynamicdefault route from DHCP client, without using a script. And, since this a common task... cut-and-paste some script and carefully commenting routing is a PITA. The script+comment approach makes multi-wan just a few more steps difficult – and dealing with multiple WAN is already hard.Some dropdown with "Check Reachability" with ping, etc.@Larsa, I had a feature request open on "check-gateway" in dhcp-client for over a year (SUP-118400). The most recent response wasWe will consider implementing such a feature.Unfortunately, giving any ETA for when the feature will be implemented is impossible.We're talking about one option in a dropdown box.... So I don't think WG heartbeats in kernel is changing anytime soon ---

## Response 39
I get folks think @Larsa is overly pedantic about using scripts for adjusting routing rules.... but the release thread highlight the non-theoritical side-effects of using script for stuff like WAN routing:viewtopic.php?p=1061545#p1061520All my router use dhcp-client scripts & most router are remote... so I'm more sympathetic to the problem. I even know script really well! But I cannot control Mikrotik changing something in how scripting works... ---

## Response 40
Considering the recent fiasco where the change of date format broke script compatibility we want to minimize script use in production environments whenever possible.And the sad thing is, the date format could have been easily fixed without breaking script compatibility. This 'small' oversight makes the implementation seem... exceptionally well-thought-out. ---

## Response 41
Could improvements be made, sure!Can we implement working configs now, yes!+++++++++++++++++++++++++++++++++++++++++++++Yep, that sounds about right! The whole exercise has currently resulted in two different issues:No they have not.There is nothing new in this discussionand the first item is the lack of understanding how routing is accomplished on the router and how it is accomplished within wireguard.Q1.Why are WireGuard handshake responses sent through default gateway rather than the originating interface?My initial research indicates this is a known issue with some proposed fixes already sent upstreams to the WireGuard devs. Additionally, there are some workarounds that help the connection tracker with proper routing. I'll get back when something interesting pops up.Q2. Is there a convenient workaround for the above issue that doesn't rely on a DHCP script when multiple WAN interfaces with dynamic IP addresses are used as WireGuard responders? Well, currently this seems pretty difficult since ROS route control is purely based on static IP addresses rather than the logical interface names that are available in the kernel (e.g. "ip rule add from DEVICE table table-name"). However, I've got an idea that I haven't had the chance to test yet.This issue has nothing to do with wireguard, and its disengenuous to imply so. Its an obstacle to any service be it on the router or on the LAN, if you dont understand how MT routing works.As to the DHCP item, not MTs issue that some providers dont auto update their gateway IP upon renewing a lease.I have plain cable, the client updates automatically both the IP DHCP client located paramaters and all my manual routes........ How > F knows!!!My fiber connection does not, hence I have an IP DHCP script for that.Also one can use interface name for certain dynamic connections like my cable above and also pppoe. ---

## Response 42
Can we implement working configs now, yes!....Geez, a little harsh... @Larsa has something working — his problem is clear: "we want to minimize script use in production environments whenever possible".It's not a "lack of understanding". May not agree with problem, or think it foolhardy – but no need to post just to attack. ---

## Response 43
I disagree, he inventing a problem thats not a problem. There are working solutions.Add to the list the million of suggestions to make life easier for users.................While you all mull it over obsessively, I will continue to help others and stop by once in a while, to refute anything stated that is bogus. ---

## Response 44
@wfburton/Amm0, I have a similar idea that doesn't involve separate routing tables.The main route table can deal with interface as gateway... Perhaps add'l IPs in-between WG and WAN that use recursive routes and masquerade rules... e.g re-route WG through the main routing table (which interface-based gateways are supported) using a "fake WAN" address? ---

## Response 45
Ammo's suggestion appears to work.I made a new bridge, added an IP address to it, put a dst-nat rule for the wireguard traffic to listen on a different port, and forward to the new IP address, and correct wireguard port.Then routing rule to route from new IP address to wan via correct table.
```
/interface bridge
add name=brwg

/ip address
add address=192.168.44.1 interface=brwg network=192.168.44.1

/routing rule
add action=lookup comment="min-prefix=0, all except 0.0.0.0/0" disabled=no min-prefix=0 table=main
add action=lookup comment="return path for wg/openvpn into .44.1" disabled=no src-address=192.168.44.1/32 table=Rvia93

/ip firewall nat
add action=dst-nat chain=dstnat in-interface=wan1 dst-port=20131 protocol=udp to-addresses=192.168.44.1 to-ports=13534I have also recently found (as used above) the following rule is very handy before other routing rules.
```

```
/routing rule
add action=lookup comment="min-prefix=0, all except 0.0.0.0/0" disabled=no min-prefix=0 table=mainAny route that we have in route table except 0.0.0.0/0 gets routed via main.Then 0.0.0.0/0 can be handled specially.Saves having to list all the local subnets in your routing rules, yay.Edit: Maybe not, still need interface next hop address

---
```

## Response 46
@Anav - I'm biding my time by exploring possible alternatives since I have no need for quick fixes. Meanwhile, I do appreciate and rely on your tireless effort to make life easier for the users in this forum!@Amm0: You read my mind! I was thinking of testing that along with some variations of nat/masq if I get some spare time this weekend.@rplant: yeah, that's about what I had in mind. We'll see what I manage to do over the weekend. ---

## Response 47
I'm blushing!!In the meantime, you should help the dude in this thread, he has issues with fastrack and queues.viewtopic.php?t=205474Why dont you come up with a way to solve thatissue... I mean it should just work without any need for additional steps...............Not sure what MT is thinking by making it so hard to add queues.......Cannot wait to see what contortionist solutions you come up with............ I am hoping to be blown away by your innovation!! ---

## Response 48
I'm blushing!!I didn't mean to attack-the-attacker either. @anav you do good work here. Just solving some of these "non-problems" is what sometimeseventuallyyields tosimpler"pathways to success". But always a lot of complaining and arguing before that. ---

## Response 49
For example, unrelated to WG, @rplant's point:I have also recently found (as used above) the following rule is very handy before other routing rules.
```
/routing rule
add action=lookup comment="min-prefix=0, all except 0.0.0.0/0" disabled=no min-prefix=0 table=mainAny route that we have in route table except 0.0.0.0/0 gets routed via main.Then 0.0.0.0/0 can be handled specially.Saves having to list all the local subnets in your routing rules, yay.My uglier approach is:/routing rule {add action=lookup disabled=$norules dst-address=10.0.0.0/8 table=mainadd action=lookup disabled=$norules dst-address=172.16.0.0/12 table=mainadd action=lookup disabled=$norules dst-address=192.168.0.0/16 table=main}I did that because I didn't want to have more script update rules to track specific subnet, or have to manually update when a new subnet is added.  Clearly never thought about "min-prefix=0".

---
```

## Response 50
@Amm0: You read my mind! I was thinking of testing that along with some variations of nat/masq if I get some spare time this weekend.@rplant: yeah, that's about what I had in mind. We'll see what I manage to do over the weekend.Yeah I'm not sure exactly HOW... but somehow "lying" to WG may be the solution to avoid a script.What kinda annoying here is in V6 the old"dynamic-in" routingfiltercould have modified the DHCP client added routes, including next-hop, with CONFIG:dynamic-in - predefined filter chain for all other dynamic routes, i.e. all dynamic routes except (1) those added by routing protocols and (2) connected routes. In this category falls routes added by some external program, for example PPP daemon.Despite name "filter", there were various set-XXX operators since it was BGP thing (although did NOT require BGP being enabled). I could use set-check-gateway=ping on /routing/filter in V6 — without a script. Feature was lost with the new V7 BGP engine. ---

## Response 51
Hi Ammo, you know I am a little slow, what are the practical effect of using $norules or "min-prefix=0.What is it that they do in simple terms........ ---

## Response 52
Hi Ammo, you know I am a little slow, what are the practical effect of using $norules or "min-prefix=0.What is it that they do in simple terms........Nothing to do with WG. It's about how to keep the routing rules "readable" for multiwan.Say the main route table has some typical multiwan failover setup: WAN1 and WAN2. And have 2 route tables for them and the FW marking. You also have some VLANs and bridging etc. per @anav/@pcunite. No PCC (or ECMP), just failover.Now you have some device on some VLAN that you want use only WAN2, and not follow "main" distance= failover. Starting with no rules, you can't just say/routing/rule add dst-address=0.0.0.0/0 src-address=10.10.10.10 table=WAN2as that will do as it says, and NOT use "main" even for local LANs. Only the main routing tables know about connected route to other VLAN/interfaces. So need SOME rule before that identifies the local LAN subnets that has a table=main...One way to add "if local LAN, use main" rule is to just add a more specific dst-address= rule for each subnet your using BEFORE the rules to control WAN selection (e.g. dst-address=0.0.0.0/0 ones)./routing/rule add dst-address=10.10.10.0/24 table=main/routing/rule add dst-address=10.20.20.0/24 table=mainAnd this totally works.But as the number of subnets, and # of routers, add up... maintaining the routing rules with any new VLAN gets to be a PITA. But needed since /routing/rule is so handy for send specific IP/subnet out a WAN. Since /routing/rules ONLY deal with IP/subnet (thus @Larsa's feature request for an interface= matcher in /routing/rule), the approach I came up with just saying any private address go to main BEFORE any specific rule for outbound WAN traffic – the three rules above.But @rplant is more cleaver, since it's one rule to be place first:
```
/routing rule add action=lookup comment="min-prefix=0, all except 0.0.0.0/0" disabled=no min-prefix=0 table=mainI'll have to try it, but looks right.

---
```

## Response 53
Just to finish from @anav POV. You can also do any inter-VLAN/etcblockingin /routing/rule's BEFORE the "min-prefix=0 table=main" rule to based on those IP. e.g. action=drop or action=unreachable. As alternative to doing it in firewall...e.g. In order:1. Any drops rules...2. Send local traffic to main rule (@rplant way, "all private IP", or specific subnets)3. Specific WAN routing rules ---

## Response 54
Okay so that is clear to understand.I have run across this already and solved it by ensuring the subnets were designed with this in mind before config.If you have all your subnets in 192.168.0.0 to 192.168.15.0 range, you could simply do/routing rule add dst-address=192.168.0.0/20 action=lookup-only-in-table table=mainHowever I like this seemingly elegant approach with apparently no downsides!/routing rule add action=lookup-only-in-table min-prefix=0 table=mainBased on the MT Docs --> table for routing rules....min-prefix (integer [0..4294967295]) Equivalent to Linux IP rule suppress_prefixlength .For example to suppress the default route in the routing decision set the value to 0.All good and well, but what is a min-prefix. what does it describe and how does using 0, somehow state send to all private IP addresses?( as an aside, I would personally refrain from using routing rules as a substitute for FW rules, they should be used for routing purposes and ONLY used for other purposes if regular FW dont work ). ---

## Response 55
You didnt comment on$norules??Please describe what this does and it was not in the MT docs by the way, so its more interesting to me ---

## Response 56
You didnt comment on$norules??Please describe what this does and it was not in the MT docs by the way, so its more interesting to meI would guess that it would be a (global) variable that is set to either yes or no to enable or disable all the routing rules in a single quick, swift, move.Now you see them rules, now you don't see 'em anymore. ---

## Response 57
You didnt comment on$norules??Please describe what this does and it was not in the MT docs by the way, so its more interesting to meThat was just a typo. I just cut-and-paste from default configuration files, with a bunch of variables at top. My bad. e.g. If there is no multiwan, I don't want any rules enabled. So imagine some variable at top of config::global norules "no"So when going to setup a router, there are a few variable at top of defconf script that can be tweaked before /system/reset-configuration file=.And to that point, when you try to have a generic defconf script usable to setup multiple routers.... you do start looking "tricks" to keep the config customizations minimal without large :if (routerA) do={}. ---

## Response 58
However I like this seemingly elegant approach with apparently no downsides!/routing rule add action=lookup-only-in-table min-prefix=0 table=mainOnly place I'd worry a bit is with recursive routes — there is the canary 8.8.8.8/32 (or similar) in between. Should work since that's internal to routing... but testing always good. ---

## Response 59
Now you have me confused???I was talking about this you posted........My uglier approach is:/routing rule {add action=lookup disabled=$norules dst-address=10.0.0.0/8 table=mainadd action=lookup disabled=$norules dst-address=172.16.0.0/12 table=mainadd action=lookup disabled=$norules dst-address=192.168.0.0/16 table=main}WTF is $norules I dont see that in docs, so what does it do. ---

## Response 60
See #68 above (viewtopic.php?t=205278#p1061800)If it was a export the "three rule way" is:
```
/routing rule
add action=lookup dst-address=10.0.0.0/8 table=main
add action=lookup dst-address=172.16.0.0/12 table=main
add action=lookup dst-address=192.168.0.0/16 table=main
[...]That covers the usual private address space (e.g. RFC-1918).Ignoring the "esoteric" RFC private blocks (RFC-5737) ones – which per spec should not be routable anyway

---
```

## Response 61
This is what I was asking before. Couldn't you use network address other than 0.0.0.0/0.I think that's what they're working on... There are a few moving parts in re-mapping. The where/how take some testing I think. ---

## Response 62
Okay just to be clear there is no such thing as $norules ??? ---

## Response 63
Okay just to be clear there is no such thing as $norules ???Correct. It just a scripting variable that get REPLACED in acustomized:import script – all config is scripting after all. If you did an :export after it just be "disabled=no". Please ignore it.But on this topic of $norules, one of the benefits of RouterOS is the ability to script setup. I use "templates" with functions to setup a router. Perhaps if applied to @pcunite's VLAN the variables might make sense:
```
:global pcvlan do={
/interface vlan add interface=$bridge name="$name_VLAN" vlan-id=[:tonum $pvid]
/ip address add interface="$name_VLAN" address="10.0.$pvid.1/24"
/ip pool add name="$name_POOL" ranges="10.0.$pvid.2-10.0.$pvid.254"
/ip dhcp-server add address-pool="$name_POOL" interface="$name_VLAN" name="$name_DHCP" disabled=no
/ip dhcp-server network add address="10.0.$pvid.0/24" dns-server="$dns" gateway="10.0.$pvid.1"
}

$pcvlan name=BLUE pvid=10 bridge=BR1 dns=192.168.0.1
$pcvlan name=GREEN pvid=20 bridge=BR1 dns=192.168.0.1 
$pcvlan name=RED pvid=30 bridge=BR1 dns=192.168.0.1e.g. @Larsa etc idea is to use one more subnet to "lie" to WG heartbeat.  They'll be even more lines of config needing to be right.  If you use a variables, there are no accidents in managing all the various numbers.When you get to multiwan setup with multiple routers, there are a lot of subnets  to keep track of so scripting is WONDERFUL for CREATING config.  So have a more complex function that deals with adding rules for WAN, where $norules is a parameter to it.But when scripting is used ondatapath – like getting an WAN IP to connect to the internet – that's where you start looking to see if you make some static configuration.  If asetupscript doesn't work... well, your there setting it up... easy to fix.  But some future upgrade breaks regular expression that look for comment in a dhcp-client script...  That when scripting is not so helpful...

---
```

## Response 64
Isn't the parameter name 'min-prefix' confusing?I would believe that it means that the lookups in the table are done for prefixes with a MINimum length of what you set it to.Setting it to 0 would then result in that a length 0 (i.e. the default route 0.0.0.0/0) is included as well.To exclude the default route you would instead logically set min-prefix=1.The only mentioning in the documentation of this is onhttps://help.mikrotik.com/docs/display/ ... cy+Routingwhere it clearly states that "Equivalent to Linux IP rule suppress_prefixlength . For example to suppress the default route in the routing decision set the value to 0."I guess my rant is that the parameter would better be named 'suppress-prefix' to be clearer..Another distraction is that a 0 is only showed in winbox as an active but greyed out field../end rant ---

## Response 65
Isn't the parameter name 'min-prefix' confusing?[...]The only mentioning in the documentation of this is onhttps://help.mikrotik.com/docs/display/ ... cy+Routingwhere it clearly states that "Equivalent to Linux IP rule suppress_prefixlength . For example to suppress the default route in the routing decision set the value to 0."Clearly it's confusing. But at least min-prefix= is documented, so there's that. And not sure "suppress-prefix" make a difference, once you understand what it does (e.g. it's a matcher after all in /routing/rule, so "suppress" is kinda odd to use in an == equality check too).But it is following CIDR. e.g. "1" means a route that's half the IPv4 internet (not useful, but logical)More examples in docs of policy routing be my rant. If had see min-prefix=0 being used, it be even more clear. @rplant must be a careful reader — I just assumed min-prefix was used in some BGP tricks, never thought could use for default route. Does make sense now however. ---

## Response 66
flatbat is correct, The name and function are rather bizarre and MUST have more explanation. The fact that you are almost incoherent trying to explain it speaks volumes.The integer ref is also confusing............how does this relate to for example IPV6 which is 128 bits long ................. ---

## Response 67
Well 128 is an integer, but you're right that a larger value than that makes little sense in this context, so whoever edited the document was maybe a little overly pedantic..My rant was more about the choice of name.If this now is just a use of the standard Linux suppress_prefixlength, then this is documented in many other places and can easily be googled with no further explanation.Using this with routing rules is a typical way of doing load balancing, where you want to first process the main table, except for its default route ("suppress all routes with a length of 0"), followed by processing another table with a default gateway unique to some traffic.Maybe in RouterOS something like;/routing rule add action=lookup table=main min-prefix=0/routing rule add action=lookup routing-mark=wan1 table=wan1/routing rule add action=lookup routing-mark=wan2 table=wan2 ---

## Response 68
Well I see it as an elegant way of simply stating: Ensure local traffic is not captured out the the tunnel by subsquent routing rules.When one starts having multiple subnets, this simplifies the config.While looking for linux stuff, found this WG QUICK script LOL -https://ro-che.info/articles/2021-02-27-linux-routingand of course the bible ref:https://www.procustodibus.com/blog/2022 ... all-rules/and another -->https://www.wireguard.com/netns/In other words, its scripted up the ying yang and nothing is automatic....... ---

## Response 69
What's new in 7.15beta8 (2024-Mar-21 09:12):*) wireguard - added option to mark peer as responder only (CLI only);*) route - rework of route attributes;Regrettably, I haven't spent as much time on testing as I planed, but wonder if this might possibly solve the issue with the handshake response only going out via the default gateway. The LinuxWireGuard kernel driverhas an 'fwmark' option that affects how 'send4/6(...)' in the driver sends the egress data. I wonder if that's what they're using here. Anyhow, I'll test it when I get some spare time.Besides, the only working solution I've found so far is using DHCP scripting to add policy routing with separate routing table and routing rule for each inbound interface, i.e. add table fib, add rule src-address table, add route 0.0.0.0 table. Mangle using connection/routing marks is redundant. ---

## Response 70
Drats, I though this one had gotten buried in the sands of time LOL.The first item I think responds to EFFECTS created via BTH and having both client and server devices being able to try and poke holes through non-public IPs using the BTH code and MT provided cloud hole poking server. ( think this was a problem on the device acting as server for handshake but not sure)Remember the first iteration of this was............. and it didnt quite work........*) wireguard - do not attempt to connect to peer without specified endpoint-address;The second items is more interesting as it may have wider ranging effects but I dont think it will bypass current Routing Policies, but I am speculating....I note its also on the previous beta as well and is not specific to wireguard, aka its a general entry*) route - rework of route attributes; ---

## Response 71
Sadly I may have run into what you are talking recently. -->viewtopic.php?t=206511I;m convinced (without proof really) that its due to BTH coding as I could have sworn it worked before on version 7 early days!! ---

## Response 72
I guess I just hit this problem. "Passive" peer behind CGNAT initiates wg tunnel to public IP peer (WAN1). Works great until I have multi-wan and WAN2 has higher priority (shorter path). With mangle and policy-based routing (as described in many discussions here) I steer the traffic via WAN1, but wan1 -> passive peer packets look (double) src-natted! The src port is wrong — not the one on which WAN1 peer listens. I'm very confident this confuses the peer and it drops the packets (and reports zero incoming packets). Verified with packet sniffer.When WAN1 is default route, WAN1 -> peer packets src port == WAN1 listen port.Funny thing is I've seen many times same symptom in MT <--> Ubuntu WG tunnel that'snotmulti-wan.On the same multi-wan box, I have two more WG tunnels, but active-active and never had problems with them. Only when passive peer is involved.I wish I could find proper diagram and explanation of the flow in such cases so I could understand. ---

## Response 73
I'm having a very similar problem and wondering how you guys solved it... I'm on ROS 7.16.2.I have two ISPs (2 WANs) on the router and want to enable wireguard peers to connect to any of the WAN IP addresses. Found out the hard way that this doesn't work. Wireguard clients (or, more precisely, peers on the WAN side, the ones that are initiating the tunnel) can only connect if they connect to the WAN interface that has the prefered route in main routing table. If they try to connect to any other WAN interface, which are not the preferred ones in the main routing table - that connecting peer won't t receive any traffic. Standard mangle rules ("if you get a packet on this interface send it back on that interface" used in prerouting/input + output) don't t help here - I found this surprising and confusing.Now thanks to posts from Larsa - I understand why this is happening.Also I don't understand why this is not seen something that should to be fixed (at least not by some members). To me: a service on the router that is not able to work from just any interface that's... unexpected, to say the least.But the question is: how to setup Mikrotik so that wireguard peers can connect using any WAN IP ? Is there a way ? Could you share ideas if you know ? ---

## Response 74
MT knows, they have not put it high on their priority list to fix I guess?The fix........ one still needs to mangle but add a dst nat rule. -viewtopic.php?p=1092192&hilit=wireguard ... x#p1092255The thread is this one..viewtopic.php?t=210218 ---

## Response 75
Nice little hackWill try and see if it works, thank you ! ---

## Response 76
This hack only works in the "trivial" case that your multiple WANs are in the main routing table.I have a setup where I establish my WAN uplinks via VPNs (also wireguard). Then you need policy routing (VRFs don't work because not implemented) and everything goes nuts.If you have that setup, check my solution:viewtopic.php?t=212887PS: But I am close to abandoning wireguard altogether. I think it's nice for a trivial client-server setup. But once you bring PBR/VRFs etc into play it's just a mess and their "design decisions" not made with these in mind. For example, a service that insists to bind on every single address on the system is just plain bad. ---

## Response 77
Sorry your trivial case nonsense is pure BS. Many folks that come here for assistance have normal multi-wan setups, not all can have specialized, niche vpn WAN only setups. ---

## Response 78
Sorry your trivial case nonsense is pure BS. Many folks that come here for assistance have normal multi-wan setups, not all can have specialized, niche vpn WAN only setups.It's not trivial. Mikrotik has plenty of users that use iBGP/OSPF/etc. One could also equally argue that Mikrotik focus on home users needs is actually the problem.They built their own routing engine, yet leave WireGuard was not really considered in the design. ---

## Response 79
And the horse you rode in on AMMO. I never said that other than multiwan setups on the main routing tables was trivial..............There is a need for multiple approaches for the very basic through to BGB/OSPF VRP etc..........Nor did I say that Mikrotik focussing on either home users or advanced users was a problem.Before you start know your audience,,,,,, stepping on my toes will not get you far. ---

## Response 80
Yet still "not all can have specialized, niche vpn WAN only setups" as an argument that a broken design is "OK" is a fairly bad excuse. At least the issue should be acknowledged, rather than downplaying it.It should not matter if a WAN uplink is Ethernet, a VLAN device, a bridge or, as in my case, a VPN. ---

## Response 81
niche in the sense that its for experts only doing more complex configs and they are not trivial nor a small number of cases.As for a broken config, that is the reason for the hack!!If the hack doesnt work for a more complex case, then stop being lazy and come up with a better hack. ---

## Response 82
Then please just ignore my answer.I am sure sooner or later someone will find this post and has the same issue and will appreciate the pointer to a more universal solution.I spent the last week working around RouterOS shortcomings and I’m happy to save someone else the same hassle. ---

## Response 83
Nothing prevents you from going to a different vendor, or using a different VPN then wireguard. Just suggestions..........Perhaps other vendors handle wireguard differently so that its not a problem for the more complex routing subnets? ---

## Response 84
Nothing prevents you from going to a different vendor, or using a different VPN then wireguard. Just suggestions..........Or, Mikrotik fixes their implementation to work like the rest of RouterOS. ---

## Response 85
Nothing prevents you from going to a different vendor, or using a different VPN then wireguard. Just suggestions..........Or, Mikrotik fixes their implementation to work like the rest of RouterOS.That is my first choice too! Why wireguard is allowed to deviate from standard Mangle practices is beyond me?? an WTF is taking so long to fix it.By the way while they are knee deep in that code branch, for the love of tranquility add amnesia ---

## Response 86
I have a conceptual question regarding WireGuard in a multi-WAN environment using dynamic addresses.Problem: in ROS, when a passive WireGuard peer receives its initial handshake (i.e., when connection-state = new), the state machine doesn't keep track of either the destination address or the inbound interface. Consequently, the peer sends its handshake reply through the default gateway which breaks functionality in a multi-WAN environment where the ingress and egress addresses must match. This also renders Mangle Connection Marking useless for WireGuard since the handshake must complete before the connection state becomes established.Question: are there any smarter and cleaner ways to handle policy routing for dynamic WAN addresses, rather than relying on a shaky DHCP script to set the /routing/rule src-address for each interface table?ps...EDIT: By shaky, I mean that the script might break if a developer once again and completely unnecessarily decides to change the script compatibility (as someone did with the date format).Note to myself: ask r&d to add src-interface as a routing rule option.I see that this issue is very recurrent. It is not a problem in my environments, but I think I can help. Wireguard initially needs the IP of a single endpoint, and the opposite endpoint is persistently trying to connect. My solution is: Configure in /ip route each client IP with the corresponding WAN gateway (assuming they are fixed IP). Example: if a client only connects through WAN 1, route the IP of that client to the gateway of that WAN. In case they are dynamic clients (RoadWarrior) Create a script that regularly reads the corresponding peer endpoint and will update the route if it detects a change. I suppose that it is not a definitive solution, until Mikrotik deigns to improve the WG options, such as an interface selector. And I understand that all the solutions proposed with mangles, tables, routing, etc., have not worked. I leave below a script that should help for dynamic clients.
```
/system script add name="update-wireguard-route" source="{
    :local peerEndpoint [/interface wireguard peers get [find where public-key=\"<PUBLIC_KEY_OF_THE_PEER>\"] endpoint];
    :local clientIP [:pick $peerEndpoint 0 [:find $peerEndpoint \":\"]];
    :local existingRoute [/ip route find where dst-address=\"$clientIP/32\"];
    
    # If the route exists, update the gateway; if not, create a new one.
    if ($existingRoute) do={
        /ip route set $existingRoute gateway=<Gateway_WAN1>;
    } else={
        /ip route add dst-address=\"$clientIP/32\" gateway=<Gateway_WAN1>;
    }
}"

---
```