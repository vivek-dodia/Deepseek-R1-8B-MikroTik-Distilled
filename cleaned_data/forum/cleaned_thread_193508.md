# Thread Information
Title: Thread-193508
Section: RouterOS
Thread ID: 193508

# Discussion

## Initial Question
Has anyone attempted to access and stream something likeNetflix over zerotier?I am thinking of a couple of issues.......a. is the throughput viable and good enough..........b. does it bypass the issues of standard VPN streaming.......... (geofencing etc.)If I am away from home and want to stream netflix over my laptop, but have to appear as if I am coming from home is the typical scenario.Thus far the only viable candidate worth pursuing that I am aware of thus far isa. unencrypted L2TP running over wireguard. ( allows one to monkey with MLPPP ) *****b. ?????? (maybe zerotier?)*** A genius I know informed me that one of MLPPPs features, is that it provides a way to deliver large payload packets using small transport ones by splitting them at application level instead of using fragmentation of the transport ones at IP level. ( Also helps maintain MTU at 1500 )Other discussion point. Ease of use.a. requires MT devices at both ends.b. may only require MT at one end. ---

## Response 1
I can't speak for zero tier but I do this quite successfully via standard Wireguard VPN and policy based routing (routing/rules) after creating the requisite table and address list/firewall rules. Works on my laptop in a traditional client to server setup as well as over specific home network devices via a site to site. 7000 miles away from the US but you'd never know. Except the latency of course which doesn't matter for streaming. ---

## Response 2
Referring to IPTV or NETFLIX?? ---

## Response 3
Amazon prime video, Disney+ (I gotta have my princess movies), Netflix, few other streaming services that verify US presence. ---

## Response 4
Lets be honest, those disney movies are for adults....disguised as kids movies.......... Donkee!!!!! ---

## Response 5
From henceforth, we're all to be known as Team Alpha Super Awesome Cool Dynamite Wolf Squadron.Hellz yeah! ---

## Response 6
I see, so basically maybe its third party VPN providers that dont work (regardless of vpn type) but home to home, or road to home wireguard works fine ????? ---

## Response 7
Damnit llama stop rejiggering your posts!Yes third party providers and data centers (alas I used to use linode for this) all have know IP blocks and so the streaming providers just blacklisted them. It was (maybe is) a game of wackamole trying to use a server that hadn't been blocked yet. For a home connection you are just that, a regular home connection versus a commercial entity. I've been streaming this way since 2013 or so when they first started blocking things. ---

## Response 8
Works great for me but I've also got a data center to send it to and my own IPv4 / IPv6 space. It's also going over a gig symmetric pipe in both locations.I use an RB5009 as a ZeroTier gw at home and a CCR2004-1G-12S+2XS in the data center so i can typically get several hundred meg between the two.Latency is about 40ms on average between the two locations. ---

## Response 9
I'll trade your 40 ms latency for my mid 2xx ms latency. The big hop across the great waters hurts AND my internet is serviced with an LTaP LTE6 using the local cell provider. Get 100+ Mbps down / 50 Mbps up. Service works well enough but the latency sucks. I'm rocking at CCR2004 PC version at the remote end and an RB5009 on the local end. Actual two of them in VRRP config. ---

## Response 10
Works great for me but I've also got a data center to send it to and my own IPv4 / IPv6 space. It's also going over a gig symmetric pipe in both locations.I use an RB5009 as a ZeroTier gw at home and a CCR2004-1G-12S+2XS in the data center so i can typically get several hundred meg between the two.Latency is about 40ms on average between the two locations.I have the same hardware. Can you tell me what kind of speeds you get across the connection (from lan to lan, not reaching out to the internet)? Have you set up other tunnel types to compare? IPSEC, Wireguard? ---

## Response 11
IPANET, so you can confirm that lets say I am on the road ( be it iphone or laptop ) can connect via zerotier to my home and go out the home internet?The advantage of both zerotier and wireguard is that one only needs one MT at the home end!The advantage of zerotier alone is that one never needs a publicly accessible WANIP correct?The disadvantage of zerotier (for some) is reliance upon a third party.(Edit: dont laugh at my number 3, if zerotier was owned by a chinese company, would your ISPs, be so happy ) ---

## Response 12
Typically 400 to 500 Mbps. Until ZeroTier is updated for multi-core in MikroTik's implementation, you won't see much beyond 700 to 800 Mbps which is what I got when I tested locally between the two 2216s we have in the lab.I don't use wireguard / ipsec as much anymore becuase most of the clients I work with care more about ease of use / tunnel management than pure speed, so ZeroTier is heavily favored in ISPs/DCs/Enterprises. ---

## Response 13
IPANET, so you can confirm that lets say I am on the road ( be it iphone or laptop ) can connect via zerotier to my home and go out the home internet?Yup, my public IPv4 and IPv6 flip to the datacenter when I use ZeroTier either with a router at home or with the ZT client on the road.You have check the "default route override" box on the ZT net. And you also need to create a default route in the ZeroTier contoller on the ZT net you're using. ---

## Response 14
Re Netflix/Hulu/DisneyXXX, video is streamed via TCP/HTTP. So imagine ZT be roughly same as any other VPN – it's just not that much traffic even at 4K.Re IPTV... that's a pretty broad term. Let's assume you mean some cable/fiber provider that bundles "cable TV" with the ISP service. That's typically done using multicast IP to delivery video (e.g. the "TV channels"). For this case, it's here were ZT could be useful since you can bridge the LAN, including IPTV multicast, via ZeroTier – so you can bring your "cable TV package" anywhere using ZT. (I haven't tired it, but should work)But one generic advantage of ZeroTier (that I think gets ignored) is that the MTU is higher – so standard ethernet packets never get fragmented – that can in some case have real performance benefits. In your "streaming" cases, this would help more with UDP+RTP-based MPEG streams, since you can squeeze more frames-per-packet with higher MTU – but RTP isn't common in consumer streaming AFAIK. ---

## Response 15
Has anyone attempted to access and stream something likeNetflix over zerotier?Works great, especially when I'm traveling and want to watch streaming services that are geo-locked. ZeroTier is also extremely easy to install, configure and use on all types of operating systems and devices. Full HD requires about 3, 5/6 Mbps and 4K 15/32 Mbps (H.265/H.264).https://www.synopi.com/bandwidth-requir ... d-4k-videoJust create a network the using the web based ZeroTier admin center (my.zerotier.com) and use the network-id when installing all the clients. Then enable which clients that are allowed to connect to the network using the web manager. That's it. ---

## Response 16
One caveat, zerotier is only on arm devices right............... wireguard is on all devices........wait for it......tis coming......its here!!another reason why zero trust cloudflare tunnel should be an options package available to ALL DEVICES............ ---

## Response 17
I was wondering when that plug would be dropped. Was beginning to think you'd acquired an arm model ---

## Response 18
He's not selfish and wants everyone to have same fun. ---

## Response 19
duplicate post.....skills!! ---

## Response 20
Too funny, I do have an arm ax3 now, but my main router is a tile CCR1009. Orphan POS apparently.Sob is correct, this is about equality and justice for all owners, and specifically for all the home users that attempt to setup servers on MT devices.The zerotrust cloudflare tunnel would accomplish two very important things.a. provide a safe secure method for home users (not experienced) to add servers ( this is not just a few users it seems to be a HUGE population )b. there would be no need for the stupid foray into raw rules, bogons, 20 ICMP rules etc etc that these newbie folks always fall into and encouraged by crappy ill advised MT doc pages........that want to make me puke.c. this would ease the burden on support for MT (cough cough) , and alas I would have less people to help in the long run, very unselfish dont you think......... ---

## Response 21
Well CCR does support ROSE, so it could be a NAS. So I guess for your "local streaming" needs you can use the CCR to store media content.If you add the hAPax3 running a Plex (or similar DNLA thing) container, you'd be able stream movies from your own library (e.g. container using NFS on hAP to get CCR files).With ZeroTier on the hAPax3, you'd be able to remotely access the both the NAS and Plex container from anywhere as an additional "streaming-with-zerotier" case.Now, I'd sell that CCR on eBay (someone still wants them), and get the RB5009 to replace. ---

## Response 22
So you want me to buy another MT product ..............who do you work forNo simply add zero trust cloudflare tunnel as an option package, access to servers then becomes much safer without too much fuss. ---

## Response 23
this is about equality and justice for all owners, and specifically for all the home users that attempt to setup servers on MT devices.Well you're not wrong on MT's egalitarian "all features, all platforms" is lost. Some fair reasons why, but still. On TILE, Tilera and the market and mainline linux support abandoned them long before Mikrotik. And the writing has been on thewallARM for a while.If you re-map your "New User A...Z" to a containerize ZeroTrust – Mikrotik might be more interested in packaging it IF people were using it. Although unlike ZeroTier, the Cloudflare tunnels doesn't do any probing (and doesn't need to with anycast DNS)... so it being in a container isn't as much of a problem. Likely why ZT is a package, since it needs direct access to interfaces. ---

## Response 24
No simply add zero trust cloudflare tunnel as an option package, access to servers then becomes much safer without too much fuss.Well some of those same problems are solved with ZeroTier too. Any device, any where can be on your home LAN... And since all the ethernet things (Layer 2) are passed by ZeroTier, that works for a lot of things. Now...home servers with open access, that's where something like ZeroTrust is super useful. ---

## Response 25
If you add the hAPax3 running a Plex (or similar DNLA thing) container, you'd be able stream movies from your own library (e.g. container using NFS on hAP to get CCR files).I'm already doing this on my CCR2116 at home. I put a 512GB nvme drive in it and loaded the plex container. It's also tied into ZeroTier so that if I want to access it from the office or elsewhere, it's super simple because ZeroTier just works. ---

## Response 26
You guys are smooth and experienced. Zerotier is not that easy and its only an ARM interoperable package.Its why wireguard, part of ROS is superior, available to all devices? Dont have to learn complex containers either.........You guys remind me of politicians in Washington, dont have a sweet clue what its like to be in a newbies/middle class shoes anymore. ;-PP ---

## Response 27
Zerotier is not that easyIn close to three decades of doing this stuff I don't think I've ever found a VPN as easy as Zerotier for non-technical users or entry level tech people.Curious what parts of ZeroTier you find to be complicated to operate/configure? ---

## Response 28
ZeroTier doesn't have to be hard. If you start with QuickSet config ("Home AP"), and ignore all the vlan-filtering=yes stuff, the mechanics of ZeroTier to bridge the default 192.168.88.0/24 subnet are just a few steps.1. Install the ZT from extra-package on ARM device, reboot etc.2a. Enable ZeroTeroinstanceon RouterOS (e.g. in Instance tab, from ZeroTier, in winbox)2b. Change the /ip/pool for dhcp1 to use a smaller range to avoid colliding with ZT, so 192.16 88.101-192.168.88.1993a. Create account at my.zerotier.com3b. On ZT web console, create a network and edit as followed3c. Remove all managed routes & add 192.168.88.0/24 with 192.168.88.1 and 0.0.0.0/0 with 192.168.88.13d. Set IP auto-assign to use Advanced, and use 192.168.88.201 to 192.168.88.249 as range4a. Back in RouterOS, create a new ZTinterface(the main "ZeroTier" tab in winbox).4b. Use network ID from my.zerotier.com and uncheck "Allow Managed", and enable it.4c. Add the zerotier1 as a port on bridge1 (/interface/bridge/port)5a. Back in ZT console, the Mikrotik should appear under "Members"...5b. Check the box under "Auth?" next the RouterOS, assign a name/desc to your liking5c. Tap the Gear icon (next to checkbox) to then check "Allow Ethernet Briding"5d. [ No need to "Save" – all the setting happen live. ]6a. If you now add ZeroTier app to a smartphone/desktop...6b. In ZT client, join the same network using the network ID from my.zerotier.com, same used by the Mikrotik6c. On ZT web console, check the same "Auth?" box. BUT you do NOT need to check "Allow Ethernet Bridging"6d*. To enable "streaming" via the Mikrotik over ZT from the client (assuming it NOT on same LAN), in the client check the box for "Allow Default Route Override". This will cause the ZeroTier connection on smartphone/desktop to "send all traffic" to the remote mikrotik at 192.168.88.1. And all the firewall stuff etc follows from there. *optional if you just need remote access to devices on your LAN & do NOT want all ZT client's internet traffic going through the Mikrotik's WAN – but required if your trying to use your home connection for another country to bypass streaming service's country restrictionsIt's a few steps, but at this point the remote device should be identical to the default LAN in the default Mikrotik configure (for a "Home AP"). ---

## Response 29
Curious what parts of ZeroTier you find to be complicated to operate/configure?To me it's the ZeroTier central UI that focuses on routes/IP address (e.g. at the top of the page). But those JUST client "policies" that get pushed to desktop/mobile (or RouterOS with allow-Managed=yes). But that's give the impression that ZeroTier is doing stuff at IP/Layer 3, when it's not – it's just a L2 bridge in the sky.And the fact there isn't some "Passthough DHCP" option would really simply Mikrotik bridging to ZT network, instead of assigning clients IP based on my.zerotier.com. ---

## Response 30
As for ZeroTier in general, it's just acting like a virtual switch (vSwitch) and you can do whatever you like with the end-points just like with any regular switch.Normally you don't need to do anything else but to install the ZeroTier client and assign the network id. The rest is managed using the TZ web interface. The same goes for ZeroTier on Mikrotik but as it is a router you normally want to add routing, firewall rules and so forth. ZeroTier might do stuff with L3 like push out routes and more advanced thing using "Flow Rules".A couple of things tho that I think might be confusing are 1) all the drivel about Planets, Moons and Roots 2) The Mikrotik ZeroTier manual:1) ZeroTier is just a normal WAN (although private and virtual) where all the clients are controlled using small daemon on the device from a central web interface. That's all.2) The Mikrotik documentation overcomplicates things and tries to be both a reference manual and a user's guide in a "blissful mess". In addition, it is unclear that the part that deals with Mikrotik being able to act as "Controller" is completely optional. If Mikrotik could drop the entire "Controller" part (or split it into a separate package) the ZeroTier client would probably fit in the smaller non-ARM based devices, Regarding DHCP, I'm not sure what you mean or want to accomplish? ---

## Response 31
Regarding DHCP, I'm not sure what you mean or want to accomplish?ZeroTier's desktop/mobile clients won't accept an address via a DHCP server on the same (e.g. if Mikrotik is bridged to ZT network, it be better if ZT client has "leases" on the Mikrotik side). As it works today, it is pretty simple the" route & /IP address(es) are "injected" based on my.zerotier.com (and ZeroTierOne client flags too).On linux, you can attached dhclient/dnsmasq/etc on the linux's ZT interface....but on mobile/Mac/Windows, it's not so easy. ---

## Response 32
I'm not entirely sure I understand it correctly (Sunday brain) but you want to assign your own ip address from DHCP on a Mikrotik TZ endpoint that differs from the subnet created on the central controller? ---

## Response 33
It comes up if you're using ZeroTier and bridging it to a Mikrotik bridge/VLAN/etc... If you look at the bridging instructions I wrote above, 1/3 of the steps involve setting up IP ranges tomatches for bridging. If the ZT client (ZeroTierOne) had an option for Mac/Windows/mobile for "Use DHCP Client" options, it be even simpler to setup with Mikrotik. No reason ZeroTier has to be involved in Layer 3 – the DHCP Server on Mikrotik can provide IP address and even routes with DHCP Option 249 or similar..If your treating ZT as a NEW subnet and using only IP routing, issue doesn't come up – e.g. ZT client are a unique subnet which is what you'd want if using routing (i.e. NOT bridging a MT subnet to ZT network). ---

## Response 34
So you all have piqued my interest as I had not previously seen a reason to try something aside from ipsec or wireguard for my remote network access and streaming needs. I am trying to wrap my head around the zerotier concept as it differs a bit from a traditional vpn solution. Just to be certain, I can use zerotier to take two routers with internal subnets of 10.20.0.0/16 and 10.10.0.0/18 and "tunnel" traffic between them (for device access and streaming)? I don't want to do the bridging or have the zerotier subnet the same etc, I ultimately just want the two routers to exist on one ZT network connected via a different tunnel subnet and be able to access devices on the other side or policy route certain devices for streaming etc. My wireguard setup is working outstanding but I see some definite ease of use enhancements possible, not to mention how easy this appears to be to scale. Not looking for someone to give me a solution. Just want to be sure I'm not expecting something ZT wasn't meant to do as I envision. Thanks! ---

## Response 35
My question for the gurus, if I have a wireguard connection between two places or from iphone to home, what would adding zerotier bring to the mix that I cannot already do ??For me if the home device had a non public IP, there would be the immediate case for zerotier. ---

## Response 36
latency. ---

## Response 37
Very true WG is almost certainly going to have low latency.But WG doesn't do multicast, so no mDNS or other discovery protocols. ---

## Response 38
Examples of mDNS or discovery protocols I would need ???? Trying to situate the estimate......... ---

## Response 39
My question for the gurus, if I have a wireguard connection between two places or from iphone to home, what would adding zerotier bring to the mix that I cannot already do ??It’s a virtual private switch in the cloud … so anything that you attach to that switch is now accessibleFor system integrators it solves branch to HQ issues easily plus they can make money when many dispersed devices need to collaborate….WireGuard is however the cats meow ---

## Response 40
Examples of mDNS or discovery protocols I would need ???? Trying to situate the estimate.........Light bulbs and printers. Some home audio systems. Browsing network file shares on the LAN. Apps for "smart" TVs*. Security cameras, too*.And also winbox neighbors and RoMON**. Even some linux desktop VNC servers also use mDNS*** to broadcast their presence.And certainly anything Apple (AirPlay, "screen sharing", HomeKit, etc.) uses mDNS***.*these typically use SSDP or newer DIAL protocol, not mDNS, but that's also multicast**with flow rule changes in ZT***or, unicast DNS-SD, which does work over WG but requires setup in DNS ---

## Response 41
i'm sending over ZeroTier only the traffic watch i want to be sent, not all the traffic.e.g. my pipe is 100/40 , if i send whole traffic over ZeroTier, ill be getting 8/1. ---

## Response 42
Thanks for the support !My need would be to maintain different LAN subnets, each with its own DHCP server in order to make them independent.Is this possible with Zerotier? ---

## Response 43
I've had some experience with VPNs and streaming when traveling, and ZeroTier is actually a pretty solid choice for stuff like bypassing geo-restrictions. It's been easy in my setup to simulate being at home by routing traffic through my home network. WireGuard worked well for most things, but for uses like stream-enabled devices or services that want LAN-style discovery or multicast, ZeroTier worked better—especially for smart TVs or IPTV.For movies, gadgets can be hit or miss. Whenever I want quick access to a variety of films without hassle, I just use123moviesfree.netfor streaming. It’s fast, simple, and doesn’t bother me with sign-ups. ---