# Thread Information
Title: Thread-213991
Section: RouterOS
Thread ID: 213991

# Discussion

## Initial Question
Hi all, Just yesterday I received my RB5009UG+S+ and I am trying to set up Hardware offloading for Layer 3 routing. I upgraded to RouterOS 7.17.According to the online docs, I should be able to enter these commands in the terminal
```
/interface/ethernet/switch set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port set [find] l3-hw-offloading=yesBut instead I get this:
```

```
[admin@MikroTik] > /interface/ethernet/switch set 0 l3-hw-offloading=yes
expected end of command (line 1 column 34)So then I start entering parts of the command one by one.  I get to:
```

```
[admin@MikroTik] /interface/ethernet/switch> set 0 l3-hw-offloading=yes
expected end of command (line 1 column 7)I am thinking it might be the new firmware version since it's got a completely different web interface I am wondering if the CLI has changed as well.Anyhow, looking for help on getting the hardware offloading enabled for routing.  It's agonizingly slow right now.  And if this model won't support HW Offloading then this is going right back to Amazon...Thanks,Jon

---
```

## Response 1
rb5009 doesn't support hardware routing. ---

## Response 2
Thank you. Well that answers that...Back to Amazon it goes! ---

## Response 3
Then please let me know which Amazon platform you're returning it to – maybe I can grab the RB5009 at a good price in the Amazon resale section. One person's loss is another's gain. ---

## Response 4
I will be returning it to Amazon in the US.I’m bummed. This is a great router otherwise. But I need the L3 hardware acceleration. With my application, the way it is right now is just way to slow and unusable. I can’t even load a web page from a device on the second network. My previous $100 Ubiquiti Edge Router has hardware acceleration. Guess I will go back to that. Really surprised it does not have acceleration.Oh well…. ---

## Response 5
https://help.mikrotik.com/docs/spaces/R ... OffloadingIs Bridge Hardware Offloading enabled?Swutch Chip model 88E6393X ---

## Response 6
RB5009 do not supportL3HW offload ---

## Response 7
Thanks everyone for the replies. I appreciate it. This is really too bad. Great device otherwise. Already have it removed from my network and boxed up. ---

## Response 8
I can’t even load a web page from a device on the second network.Sounds more like another issue when not even loading a webpage works which hardware offloading - even when r5009 had it - wouldn't fix either. ---

## Response 9
Oh no. It was tremendously slow. Connectivity was there. Just extremely slow. Unless there is something more to do in this device than just setting a static route in the routing table.Put my EdgeRouter X back in (which has hardware offloading) and everything is working great.Really wanted to use this to take advantage of my available 2Gbit download speed. ---

## Response 10
And let's put it this way - if there's something else I need to do to speed up the routing across the router, then great. I would love to keep it.Let me explain my network.I have a main LAN in the 192.168.0.0/23 subnet.I have multiple VLANs that are all segments of the 10.0.0.0 subnet. These VLANs are all established on a Layer 3 managed switch with an IP of 192.168.1.198. The VLANs handle IGMP multicast video data.If I am entering a static route in Windows, it would be something like this:
```
route add 10.0.0.0 mask 255.0.0.0 192.168.1.198I set up a similar routing entry in the MikroTik router:
```

```
10.0.0.0/8 with a next hop of 192.168.1.198Routing into those VLANs was painfully slow.  Connections were there but it felt more like 300 baud dialup than gigabit ethernet.Exact same setup with my Ubiquity EdgeRouterX has no issue with speed.  The EdgeRouter X has hardware offloading and I remember I had a horrible speed issue with it until I enabled that.  Now it works great.  I just have multi-gigabit internet now and my cable modem has a 2.5Gbit connection.  So the MikroTik device was great - 2.5 Gbit from the modem to the router and 10 Gbit SFP down to my switch..Again, happy to give this thing another try before I ship it back if someone can point out something else I need to do with the routing setup.

---
```

## Response 11
weird. 5009 should handle 2gb of traffic like it's nothing.i vote misconfiguration. ---

## Response 12
weird. 5009 should handle 2gb of traffic like it's nothing.i vote misconfiguration.It's not 2gbit of traffic. It's handling the routing between my LAN and my VLANs. Speed across the LAN and out to the internet was fine. I was able to run speed tests from multiple computers and was easily getting close to 2 Gbit. It's the routing where it breaks down.And please suggest an idea of what you think it might be that was misconfigured. Here's all that was done on the unit:- changed the LAN IP address from 192.168.88.1 to 192.168.1.1- Set DNS entries- Set up DHCP server and DHCP address pool- changed my password- added the route in the IP -> route sectionThat's about it. ---

## Response 13
You seem likely to have done all of this already but just in case...Remove sfp+ from bridgeGive sfp+ an IP address, and switch port/vlan? at other end an IP address.Make the sfp+ interface a member of the LAN interface list.But if you need lots of gigs of intervlan routing, it isn't going to do it.You could maybe put your lan behind the L3 switch, and have the router justdoing gateway routing. ---

## Response 14
I haven't given IP addresses to the specific interfaces. When I'm using maximum data, I'm pulling a total of about 600 Mb/s from maybe 10 different VLANs.But your comment about basically making the L3 switch the LAN router has a lot of merit. The switch is obviously able to handle routing all the traffic and there's really no need to do my local routing through an extra interface. And the L3 switch has a 0.0.0.0 route to the gateway anyhow so any non-LAN traffic would get routed outward.I need to think about this as this changes my calculus somewhat... ---

## Response 15
I have no problems routing between VLANs at 2.5Gbps (the limit of ether1) on the RB5009. How did you configure the VLANs on it? Maybe you can post your configs here?Your EdgeRouter X has the hardware equivalent to the hEX RB750Gr3, with the same MediaTek MT7621 chip. ---

## Response 16
The VLANs are all on the switch. Just the routing table is on the gateway device. ---

## Response 17
But you still need to configure the VLAN interfaces on the router, plus the trunk port, if you want the RB5009 to route (L3) traffic between the VLANs. ---

## Response 18
No. I’m simply setting the route between subnets with the switch at the gateway. The L3 switch is doing the routing between VLANs.The router is redirecting any traffic for the 10.0.0.0 network to the L3 switch. ---

## Response 19
Hi, I think your current problem is that you are getting triangular routing.(which is probably why hardware offload is good, as it is likely not stateful)From Device on 192.168.1.x network to 10.0.0.0/8 likely goes from device to 5009 then to Switch then to 10.x.x.x device.(Hopefully often the 5009 will issue a redirect so traffic from device on 192.168.1.x will know to go direct to Switch, butdevice might well ignore it)Return traffic goes from 10.x.x.x to switch and then direct to the device on 192.168.1.x bypassing the 5009Assuming near default config.Triangular routing will cause the default invalid rule to drop packets.These connections never get properly completed in the 5009, as it never sees the return traffic.There are a couple of options:1. Rejig the network so the switch comes directly into the 5009 on a different subnet, so traffic in both directions has to traverse the 5009.2. You could try using a couple of raw rules to hopefully bypass most of the firewall.rule 1:in interface = bridge, src ip address=192.168.1.0/24 dest ip address = 10.0.0.0/8 action = notrackrule 2in interface = bridge, src ip address=10.0.0.0/8 dest ip address = 192.168.1.0/24 action = notrackThis with luck should cause the default filter fasttrack rule and accept rule (immediately after fasttrack rule) to process these packets.(And hopefully no other rules)These 2 default filter rules should by accept established, related and notrack packets.If not already done, you could perhaps put some sort of null route on the switch so you don't wind up with packets to unconnected 10.x.x.x subnetsjust bouncing between the switch and the router until their ttl runs out.ip route 10.0.0.0 255.0.0.0 Null0 200 ---

## Response 20
From Device on 192.168.1.x network to 10.0.0.0/8 likely goes from device to 5009 then to Switch then to 10.x.x.x device.(Hopefully often the 5009 will issue a redirect so traffic from device on 192.168.1.x will know to go direct to Switch, butdevice might well ignore it)That would be 100% correct. I've verified that with a trace route.Return traffic goes from 10.x.x.x to switch and then direct to the device on 192.168.1.x bypassing the 5009This, I don't know. The switch does have a route of 0.0.0.0 0.0.0.0 192.168.1.1 but since the switch is also a router and since the switch is sitting on the LAN, you may just be right...Ah, you may be on to something.....
```
/usr/local/bin # traceroute 192.168.1.16
traceroute to 192.168.1.16 (192.168.1.16), 30 hops max, 38 byte packets
 1  10.0.19.1 (10.0.19.1)  20.095 ms  1.253 ms  1.266 ms
 2  192.168.1.16 (192.168.1.16)  0.237 ms  0.282 ms  0.172 msThe trace route doesn't even show the switch IP as one of the interfaces being traversed.OK. OK.  I have some more work to do here before I just decide to return this thing....

---
```

## Response 21
OK so help me with the rules please:rule 1:in interface = bridge, src ip address=192.168.1.0/24 dest ip address = 10.0.0.0/8 action = notrackrule 2in interface = bridge, src ip address=10.0.0.0/8 dest ip address = 192.168.1.0/24 action = notrackHere's what I see in the router when setting up the rule. There's no action of "notrack" -I have also taken a look at the CLI interface but I am not having any luck there either. I'm assuming "lookup only in table" is the correct selection but not sure. ---

## Response 22
Hi there.I have deployed quite a few rb5009 devices and in fact I have used one for home use for a few years. I am very pleased with it. I think your device choice is spot on, this device is probably the best bang for buck if you have a multi-gig setup.As to what you can expect from this device:* in pure software routing (including NAT, stateful firewalling, policy routing, queueing - so all features available): around 4 Gbps* with what Mikrotik calls "fasttrack" - a software acceleration technique, that precludes the use of some features (policy routing, some queueing, etc.) but does NAT and stateful firewalling, expect 7-8 Gbps (what is different in the way Mikrotik does it compared to other vendors is that it can be applied to traffic selectively - so e.g. you can choose to accelerate inter-VLAN, but apply ACM queues for internet traffic, etc.)* with no stateful firewalling (e.g. the "notrack" thingy that was mentioned) you can get quite close to 10 GbpsThese speeds can be achieved on any combination of internet/vlan-tagged/untagged/inter-vlan etc. paths.So basically your routing is most probably somehow set up incorrectly. If you would give a detailed diagram, including the L3 switch, and include the setup of the L3 device, we could probably find out what your exact problem is or suggest an appropriate configuration. (Lots of other devices include/apply some settings "by default" or "automatically" - basically Mikrotik exposes the "ip" commands in Linux through a simplified interface, but the settings are just as detailed. You have to spell out things exactly - so simply saying that it works with something else configured somehow doesn't really help. Maybe the rb5009 has to be configured differently, maybe another device, maybe both...)One such "default" that can very easily be the source of your problems is that many manufacturers include a default "hairpin nat" rule, that is if an internal host addresses another internal host (sometimes only on the same network, sometimes for all internal networks... the exact form varies), then the source IP of the forwarded packet is changed from the sender to the address of the router. This does provide quite a bit of help in making otherwise incorrect configurations work, but it's best to fix what's broken instead of papering over it. (Mikrotik of course supports hairpin nat, it just has to be configures explicitly. In some cases it is considered necessary - and easier than correcting the network design - but generally networks designed from first principles do not need it.) Such a rule for example would solve the "triangular routing" problem . but again: it's better practice to configure routing properly.Please pay attention to the fact that the rb5009 comes with a default firewall configuration. This is only suitable for an "I have one internet and one home subnet" type configuration, so for yours it has to be modified. Did you do these modifications? Did you so them correctly?Posting a full config helps a lot. (A config export can be created in the terminal with the /export file=whatever.rsc command. This has to be downloaded to your computer afterwards for further use. Please review what you post, and mask any details that you don't wish to make public.) If you post a config please do it in a code block (the 5th icon in the forum interface.) You may - as you wish - post excerpts from your config (to accentuate a given part), but please always include the full one as well, because some configurations done in different parts of the config can easily affect each other.The "notrack" suggestion is not bogus. It instructs the OS not to lookup or create connection tracking entries for given packets, and as such has performance benefits. Of course without connection tracking only stateless filtering of traffic (what many manufacturers call ACLs) is available, and of course no NAT (only for the packets that are notracked). This is a firewall feature, so that is where you will find it (IP->Firewall) and it has to be placed in the RAW table and prerouting chain. (The option is available both in winbox, webfig and cli.)Just a suggestion: first fix the routing problem, and only after you reach the limitations that I have written above set out to optimize the design, e.g. use fasttrack, notrack, etc. While you have more serious problems these only confuse things.Sorry for the wall of text and good luck! ---

## Response 23
The things rplant suggested are firewall (raw) rules (in prerouting I believe), not routing rules (policy routing).https://help.mikrotik.com/docs/spaces/R ... 6/Firewall ---

## Response 24
If you actually want to get some answers, and fix the issue, the best place to start is providing your config./export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc.)(ps dont see any cheap RB5009s yet on amazon.com) ---

## Response 25
Thanks all, Let me look some more at the docs and see if I can figure some of this stuff out. Very informative.Right now, I don't have much of a config in the router as I had factory defaulted it. So let me start playing with it some more, make the changes and test it out. Then if needed, I can reply back with more info and the config... ---

## Response 26
OK. I think I found the spot in the firewall section to add the rules under RAW.There is also a section in firewall rules where you can set a fasttrack connection which has hardware offloading. Is that something to use as well?And when I now go into the routing table rule, it now shows the rule as hardware offloaded... ---

## Response 27
The rb5009does not doHW offload. The HW would be capable of it, but the limitations are so severe that it will probably never happen. See this post:viewtopic.php?p=925222#p925222Your route is showing the "HW offload" flag because the route is "unreachable". (This is a quirk in the interface...) ---

## Response 28
Sorry to be the bearer of bad news, but (IMHO) you won't get very far with GUI only tools, the Mikrotik configuration settings are already at the same time scattered all over the place and mixed up together that without some use of terminal/command line they are impossible or near to impossible to understand/set/review.Winbox (and/or webfig) have their use (besides launching a terminal), as some actions are much easier in the GUI, of course.Since you are seemingly a Linux terminal user you should not have much difficulty in getting used to the Mikrotik's one.Try opening a terminal and running in it:
```
/ip route printisn't it easier to read?And also to post as text (possibly inside code tags)?

---
```

## Response 29
Here's the route:
```
Flags: D - DYNAMIC; I - INACTIVE, A - ACTIVE; c - CONNECT, s - STATIC; H - HW-OFFLOADED
Columns: DST-ADDRESS, GATEWAY, DISTANCE
#      DST-ADDRESS      GATEWAY        DISTANCE
0  IsH 10.0.0.0/8       192.168.1.198         1
  DAc  192.168.88.0/24  bridgeSo far the Mikrotik CLI has not been very kind to me.  I've hard a hard time figuring out how to navigate it.Here's the relevant firewall section of the config (entire config attached):
```

```
add action=fasttrack-connection chain=input dst-address=10.0.0.0/8 \
    hw-offload=yes in-interface=bridge src-address=192.168.0.0/23
add action=fasttrack-connection chain=input dst-address=192.168.0.0/23 \
    hw-offload=yes in-interface=bridge src-address=10.0.0.0/8
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
/ip firewall raw
add action=notrack chain=prerouting dst-address=10.0.0.0/8 in-interface=\
    bridge src-address=192.168.0.0/23
add action=notrack chain=prerouting dst-address=192.168.0.0/23 src-address=\
    10.0.0.0/8
/ip route
add disabled=no dst-address=10.0.0.0/8 gateway=192.168.1.198 routing-table=\
    main suppress-hw-offload=noNow, I do have the following as well from when I was messing with the IP routing rules section.  Should this be removed?
```

```
/routing rule
add
add
add action=lookup-only-in-table disabled=no dst-address=10.0.0.0/8 interface=\
    bridge src-address=192.168.0.0/24 table=main
add action=lookup-only-in-table disabled=no dst-address=192.168.0.0/24 \
    interface=bridge src-address=10.0.0.0/8 table=main
addKeep in mind I have not changed the default IP on this back to my LAN yet.  So I have not yet tested anything...

---
```

## Response 30
Quick update...After applying these settings, I set the router up for my LAN address space, DHCP pool, static leases, etc. I then put it into the network...Wow. What a difference! It's now forwarding all the traffic beautifully! I don't know which if all the items I listed in the post above are all needed, but things are working very well right now at least on first look.... ---

## Response 31
Cool. What is *not* needed:* fasttrack cannot (and silently will not) be applied to notracked traffic (fasttrack modifies the conntrack entry, which is nonexistent for untracked) - for a given traffic it is either/or* the routing rules - the default is to look at the main table for any routing decision ---

## Response 32
Cool. What is *not* needed:* fasttrack cannot (and silently will not) be applied to notracked traffic (fasttrack modifies the conntrack entry, which is nonexistent for untracked) - for a given traffic it is either/or* the routing rules - the default is to look at the main table for any routing decisionOK. Both of these make sense. And basically notracked traffic is already fasttracked because it is not tracked if I understand it right.When you say the main table - are you talking about the firewall table then? ---

## Response 33
Table refers to Routing Table(s). There is the main table which holds the majority of routes ( associated with IP addresses and subnets ) WAN etc.Special Tables...... not in main, created by admin for the purposes of sending traffic out a different table than the normal routing tables normally used.Do not understand these rules as they are duplicate in nature ( already have a fastrack rule) and they refer to subnets that have nothing do to with your router??add action=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \connection-state=new in-interface-list=WANadd action=fasttrack-connectionchain=input dst-address=10.0.0.0/8\hw-offload=yes in-interface=bridge src-address=192.168.0.0/23add action=fasttrack-connectionchain=input dst-address=192.168.0.0/23\hw-offload=yes in-interface=bridge src-address=10.0.0.0/8Also should not be using Routing Rules unless you know what you are doing!!Also related is the unk reason for raw firewall rules............If I had to say it, one doesnt care about needed traffic but is mortally afraid, a phobia if you will, of two subnets. ---

## Response 34
[...]OK. Both of these make sense. And basically notracked traffic is already fasttracked because it is not tracked if I understand it right.I a sense yes. Just to make it perfectly clear:* in case of notrack, no conntrack entry is created (this means that no stateful rules can be applied to the packets)* in case of fasttrack, a conntrack entry is made normally and then a special flag is set on it. In this case, the first few packets go through the firewall normally, and what should be done to them is recorded in the conntrack entry. Further packets traverse a *very* shortened path. Some packets are still sent on the normal path anyway in order to update timers/timeouts. This means that fasttrack can do more than notrack, it can do stateful filtering and NAT. There are other things that are skipped: e.g. IPSec, policy routing, most queues. The main use case for fasttrack is for the home user who wants to use minimum hardware resources but wants NAT or for inter-vlan routing with stateful filtering.When you say the main table - are you talking about the firewall table then?No. I mean the main routing table (when adding routes you write: /ip/route add ... table=main ...) and then in routing rules (/routing/rules) you specify (lookup-only-in-table) to use the main routing table for these packets. The use of the main routing table is the default. Even if you have other routing tables (which you don't) main is still the default. You only have to use the routing rules if you have multiple routing tables. ---

## Response 35
When you say the main table - are you talking about the firewall table then?No.It Is the table you printed, containing routes.By default on Mikrotik there Is only one routing table, called "main".But more tables can be added.All traffic will use this main table, unless explicit modifiers are used.There are two such mechanisms:1) mangle ( firewall mangle rules)2) policy routing (routing rules)You can think at both of them as sieves that can filter traffic and change the routing table that will be used on the filtered packet.Loosely, routing rules are simpler and can filter only larger particles, while mangle rules are much more complex but can filter much smaller particles. ---

## Response 36
Just a little addendum: For now I would skip the raw rules entirely. Configure everything to your satisfaction. Verify. Measure. And if you want/need more performance, add them back in. ---

## Response 37
Table refers to Routing Table(s). There is the main table which holds the majority of routes ( associated with IP addresses and subnets ) WAN etc.Special Tables...... not in main, created by admin for the purposes of sending traffic out a different table than the normal routing tables normally used.Do not understand these rules as they are duplicate in nature ( already have a fastrack rule) and they refer to subnets that have nothing do to with your router??That's why I was asking if I needed them. And they absolutely refer to my subnets. 192.168.0.0/23 is my LAN and my VLANs all live in segments of 10.0.0.0/8.Also should not be using Routing Rules unless you know what you are doing!!Also related is the unk reason for raw firewall rules............If I had to say it, one doesnt care about needed traffic but is mortally afraid, a phobia if you will, of two subnets.I was just following along with what people said here that the rules to configure the interfaces are in the firewall.The things rplant suggested are firewall (raw) rules (in prerouting I believe), not routing rules (policy routing).https://help.mikrotik.com/docs/spaces/R... 6/Firewall ---

## Response 38
Just a little addendum: For now I would skip the raw rules entirely. Configure everything to your satisfaction. Verify. Measure. And if you want/need more performance, add them back in.OK. I'm confused.1.) Creating just the route by itself does not work well. That's why I am here.2.) rplant suggested a number of suggestions regarding notrack.3.) jaclaz says those settings in raw commands in the firewall.I've got some people telling me to do one thing and others to not do it....?? ---

## Response 39
To help us, and to help yourself, the clarity starts with you...a. identify all the users/devices (external, internal and including admin)b. identify all the traffic the above groups must accomplishc. detail the WAN ( how many, public, private static, dynamic etc, if more than one, load balance or failover etc. ) ---

## Response 40
I think I’ve done that. But for clarity:WAN is just cable internet. That’s it.Cable modem with 2.5 Gbit connection going to port 1 on the router.10 Gbit fiber connection to my L3 switch.LAN is on 192.168.0.0/23 subnet. I also have a number of VLANs that are all in the 10.0.0.0/8 subnet.The router is at IP 192.168.1.1. The switch has a LAN IP of 192.168.1.198 that is on a routable VLAN.The goal is to route traffic from the 192.168.0.0/23 subnet to the 10.0.0.0/8 subnet. For devices on the 10.0.0.0 VLANs their gateway is the VLAN IP address on the switch.Normal routing table goes:Destination: 10.0.0.0Mask: 255.0.0.0Gateway: 192.168.1.198Just making a normal route entry in the MikroTik resulted in extremely slow performance when trying to get to the 10.0.0.0 VLANs. Brutally slow.This should be sufficient to describe things. ---

## Response 41
Just a little addendum: For now I would skip the raw rules entirely. Configure everything to your satisfaction. Verify. Measure. And if you want/need more performance, add them back in.OK. I'm confused.1.) Creating just the route by itself does not work well. That's why I am here.2.) rplant suggested a number of suggestions regarding notrack.3.) jaclaz says those settings in raw commands in the firewall.I've got some people telling me to do one thing and others to not do it....??To clarify:1) Your routes (or other settings) were previously somehow messed up. You have reset the router. Things magically work- we will probably never know what was wrong. Neither routing/rules or raw firewall helped or will help you with that.2) The suggestion - as I have written - is not bogus. But it is an *optimization*. This router will happily route approx. 4 Gbps without any of it. If you later want more performance, add it. My suggestion is to first configure things *correctly*, then optimize - in that order.3) The routing/rules as in your export do absolutely nothing. They instruct the router to do what it would do anyway. For your case there is no need to touch routing/rules. They should be empty. ---

## Response 42
By the way the route:
```
/ip route
add disabled=no dst-address=10.0.0.0/8 gateway=192.168.1.198 routing-table=main suppress-hw-offload=nocreates a routing situation where packets may be (will be) sent back and forth between your Mikrotik and your L3 switch.Consider the case that on the 10.0.0.0/8 network you actually use 10.0.1.0/24, 10.0.2.0/24 and 10.0.3.0/24 for you devices. Now consider that a packet is sent to 10.0.222.3. Your Mikrotik (as per the 10.0.0.0/8 route) will forward it to your L3 switch. It in turn (because it has the default 0.0.0.0/0 route) will forward it to your Mikrotik. And so it goes until TTL is exhausted (roughly 64 times), consuming resources.Your routes should be:
```

```
/ip route
add disabled=no dst-address=10.0.1.0/24 gateway=192.168.1.198 routing-table=main suppress-hw-offload=no
add disabled=no dst-address=10.0.2.0/24 gateway=192.168.1.198 routing-table=main suppress-hw-offload=no
add disabled=no dst-address=10.0.3.0/24 gateway=192.168.1.198 routing-table=main suppress-hw-offload=no
add disabled=no dst-address=10.0.0.0/8 blackholeI'm just using these subnets as an example. That's why a network diagram detailing the addressing would be useful.EDITI've read your response to anav's question.Your setup is straightforward enough. What you wrote is all you need to set. This is a powerful router, so performance should have been (and will be) more than adequate. There are tricks to get even more, but your problem was some sort of misconfiguration (maybe in some other part of the config.)

---
```

## Response 43
GLuck, then, as you seem to have all well in hand. Not even sure why you posted. ---

## Response 44
By the way the route:
```
/ip route
add disabled=no dst-address=10.0.0.0/8 gateway=192.168.1.198 routing-table=main suppress-hw-offload=nocreates a routing situation where packets may be (will be) sent back and forth between your Mikrotik and your L3 switch.Consider the case that on the 10.0.0.0/8 network you actually use 10.0.1.0/24, 10.0.2.0/24 and 10.0.3.0/24 for you devices. Now consider that a packet is sent to 10.0.222.3. Your Mikrotik (as per the 10.0.0.0/8 route) will forward it to your L3 switch. It in turn (because it has the default 0.0.0.0/0 route) will forward it to your Mikrotik. And so it goes until TTL is exhausted (roughly 64 times), consuming resources.Yeah, I get that but the likelihood is incredibly small as the traffic being passed is all from an app that has the IP addresses of all the devices in the VLANs.  It's already setup in advance.  But you make a good point in general.I've read your response to anav's question.Your setup is straightforward enough. What you wrote is all you need to set. This is a powerful router, so performance should have been (and will be) more than adequate. There are tricks to get even more, but your problem was some sort of misconfiguration (maybe in some other part of the config.)I'm not certain what Anav's problem is.  I have been asking plenty of questions but just trying to get clarity on a few.Anyhow here is what I am going to do:1.) Remove ALL rules sans the port forward rule2.) Test performance3.) If performance is OK, then I must have had something mucked up the first time I had the router installed4.) If performance is not OK, then I will add these back in:
```

```
/ip firewall raw
add action=notrack chain=prerouting dst-address=10.0.0.0/8 in-interface=\
    bridge src-address=192.168.0.0/23
add action=notrack chain=prerouting dst-address=192.168.0.0/23 src-address=\
    10.0.0.0/8I will report back...Cool - I can just disable them without having to delete them.  Nice!

---
```

## Response 45
OK. Quick answer.Removed all but the route entries and performance slowed back to a crawl.Added back in the notrack RAW entries and it all is working fine:
```
/ip firewall raw
add action=notrack chain=prerouting dst-address=10.0.0.0/8 in-interface=\
    bridge src-address=192.168.0.0/23
add action=notrack chain=prerouting dst-address=192.168.0.0/23 src-address=\
    10.0.0.0/8So it looks like I have a situation where I have triangular routing. Packets from 192.168.0.0 go through the router but packets from 10.0.0.0 do not.These two rules definitely help.

---
```

## Response 46
Okay.You seem to misunderstand (or I'm not clear enough) what "rules" means:* there a routing rules (/routing/rules) - these you don't need* there are firewall rules (/ip/firewall):* * filter rules (/ip/firewall/filter) - these should be there* * nat rules (/ip/firewall/nat) - if NATing or port forwarding, etc. you need these* * mangle rules (/ip/firewall/mangle) - you don't need these* * raw rules (/ip/firewall/raw) - you don't need these, but can help with performance* and there are routes (/ip/route) - these you obviously needIf without the raw rules "performance grinds to a crawl", then you have some other misconfiguration. They may help, but on a correctly configured router they should at most increase performance 2-3x.Post another full export!EDITOhh, so you do have routing misconfigured. Triangular routing explains what you are seeing. And it explains why the raw rules solve it.Triangular routing should be eliminated. Even if currently raw rules solve it for you, it will cause headaches later on.I will post later on how to resolve it... ---

## Response 47
I’m all ears for how to solve that. Do I have something wrong on my switch? Traceroute from my 10.0.0.0 devices out to a LAN device does not go through the router. So seems like that’s where I need to fix this? ---

## Response 48
Just to rehash. The problem (triangular routing) is this:* The devices on the 192.168.0.0/23 - when sending to the 10.0.0.0/8 subnet - send it to the Mikrotik at 192.168.1.1 (resolving it via default), because they don't know where the router for the 10.0.0.0/8 subnet is located.* The devices in the 10.0.0.0/8 subbet - when sending to the 192.168.0.0/23 subnet - resolve it to the L3 switch, which in turn sees 192.168.0.0/23 as directly connected.There are two approaches to solve the situation:Solution 1Make the devices on 192.168.0.0/23 aware of the correct (shortest) route to 10.0.0.0/8. There is a dedicated DHCP option (121 - classless route) for just this purpose. From Google:"The DHCPv4 option Classless Static Route allows a DHCP server to pass a list of static routes to a DHCP client, which then enters those routes into its routing table."This is fully supported in the Mikrotik DHCP server.Please be aware that while most normal (Linux, BSD, Windows, MAC, Android, iOS) systems respect this option, some embedded (IoT, smart whatever) devices sometimes don't.Solution 2This is the one I would encourage. Configure the L3 switch to send traffic to 192.168.0.0/23 through the Mikrotik.This done by:* Allocate a subnet just for routing purposes. Let this be 192.168.111.8/30. This subnet has to be defined both on the Mikrotik and the L3 switch. This subnet is for routing purposes only.* Configure addressing: let Mikrotik take 192.168.111.9 and the L3 switch take 192.168.111.10* Correct the route on the Mikrotik to 10.0.0.0/8 via 192.168.111.10* Correct the route on the L3 switch to 192.168.0.0/23 via 192.168.111.9Please note that for this to work, on the Mikrotik side:* you have to remove the port that connects to the L3 switch from the bridge* add the port connecting to the L3 switch to the interface list LANUse no. 2. In all larger/well designed networks it is handled this way. ---

## Response 49
Just a guess, but regarding the triangular routing issue: NA9D, you mentioned having a Layer 3 switch configured with all your VLANs and your 192.x network. Is this switch capable of inter-VLAN routing? If so, it might help eliminate unnecessary hops and improve efficiency, as traffic between the VLANs would be routed directly on the switch instead of through the router. ---

## Response 50
Solution 2This is the one I would encourage. Configure the L3 switch to send traffic to 192.168.0.0/23 through the Mikrotik.This done by:* Allocate a subnet just for routing purposes. Let this be 192.168.111.8/30. This subnet has to be defined both on the Mikrotik and the L3 switch. This subnet is for routing purposes only.* Configure addressing: let Mikrotik take 192.168.111.9 and the L3 switch take 192.168.111.10* Correct the route on the Mikrotik to 10.0.0.0/8 via 192.168.111.10* Correct the route on the L3 switch to 192.168.0.0/23 via 192.168.111.9Please note that for this to work, on the Mikrotik side:* you have to remove the port that connects to the L3 switch from the bridge* add the port connecting to the L3 switch to the interface list LANUse no. 2. In all larger/well designed networks it is handled this way.So question - So create a new VLAN on the switch?Now I have both normal LAN traffic and the VLAN traffic on the switch. It seems like doing what you suggest will break the LAN connection between the 192.168.0.0 LAN and the switch. Are you talking about adding second connection between the switch and the router? Or a trunk? ---

## Response 51
Just a guess, but regarding the triangular routing issue: NA9D, you mentioned having a Layer 3 switch configured with all your VLANs and your 192.x network. Is this switch capable of inter-VLAN routing? If so, it might help eliminate unnecessary hops and improve efficiency, as traffic between the VLANs would be routed directly on the switch instead of through the router.Yes. It is capable of InterVLAN routing. I can set the L3 switch as the gateway for my LAN network and that works. And traffic between the 10.0.0.0 VLANs works fine. That's all good. It's just getting the routing correct between the 192.168.0.0 network and the 10.0.0.0 network. ---

## Response 52
So question - So create a new VLAN on the switch?Now I have both normal LAN traffic and the VLAN traffic on the switch. It seems like doing what you suggest will break the LAN connection between the 192.168.0.0 LAN and the switch. Are you talking about adding second connection between the switch and the router? Or a trunk?This is again where a diagram would be infinitely useful. It can be ascii art or whatever.What is the situation? Am I correct:* The thingies on the 10.0.0.0/8 subnet are connected to your L3 switch?What is the rest?* Clearly the L3 switch is connected to the Mikrotik. On one port only? 10Gbps?* Are the 192.168.0.0/23 devices connected to the other ports on the Mikrotik? Are they connected to the switch?Yes, what I suggest will break the direct (unrouted) link between the L3 switch and the 192.168.0, 0/23 subnet. That is precisely the goal. This connection leads to the triangular routing situation. The L3 switch should only send packets to this subnet through the Mikrotik.Depending on the exact make/model of the L3 switch this will probably mean creating a new VLAN. This can go out to the Mikrotik either as tagged (trunk) or untagged (access), depending on how you wish. If it is tagged, of course it will have to be untagged on the Mikrotik, but this is easily done. If untagged, you have the seemingly strange situation that the given VLAN exists only in the "imagination of the switch", but that is how most L3 switches are in fact configured, and it is correct.EDITAnother question: What is your goal exactly: Do you want the Mikrotik to serve only as a DHCP server and handle NAT? Or would you like it to do other things a well (filter traffic, so for example the 192.168.0.0/23 can "talk to" the 10.0.0.0/8 devices, but not vice versa, etc., or maybe provide a VPN gateway...)?Either way you will have to do this additional routing subnet thing. Just other configuration afterwards depends on this choice. ---

## Response 53
This is a really long post but you guys wanted to know the details so here you go....This is again where a diagram would be infinitely useful. It can be ascii art or whatever.See below and I'll explain in more detail after I answer your questionsWhat is the situation? Am I correct:* The thingies on the 10.0.0.0/8 subnet are connected to your L3 switch?Yes. CorrectWhat is the rest?* Clearly the L3 switch is connected to the Mikrotik. On one port only? 10Gbps?* Are the 192.168.0.0/23 devices connected to the other ports on the Mikrotik? Are they connected to the switch?The L3 switch is connected to the Mikrotik by a 10 Gbit SFP+ connection. It is the only connection at this time, but the open ports are there should I need them.Everything else is connected to the L3 switch. There is a second L2 switch that is also on the network and connected to the L3 switch.Another question: What is your goal exactly: Do you want the Mikrotik to serve only as a DHCP server and handle NAT? Or would you like it to do other things a well (filter traffic, so for example the 192.168.0.0/23 can "talk to" the 10.0.0.0/8 devices, but not vice versa, etc., or maybe provide a VPN gateway...)?Either way you will have to do this additional routing subnet thing. Just other configuration afterwards depends on this choice.I want the Mikrotik (or whatever router) to act as DHCP server, DNS relay, NAT, VPN gateway, firewall, router, etc.I "could" use the L3 switch as a "LAN" router where I set things up where it is the gateway for all the devices on my LAN. It works as I had it that way yesterday, but then anything on the LAN traversing to the outside world (most of the traffic) would need to be handled at the L3 level by both the switch and the router as opposed to if the router was the gateway, then the switch is only operating on L2 for any traffic to the outside world.Below is the network diagram scribbled by me. An artist I am not! Let me explain the VLANs as we use them as part of distributing IP video over a network. I write software to work with video devices from a company called Just Add Power (wwww.justaddpower.com). At a basic level there are two sorts of video devices - an encoder and a decoder. The encoder takes and HDMI signal from a video device (camera, cable box, AppleTV, Roku, etc) and encodes that into an IGMP multicast stream. On the other end the decoder, receives the IGMP multicast stream and converts it back to HDMI where it connects to a TV. Because we want video to have priority above all else on the network where the encoder resides, it is set up to basically just transmit data as fast as possible. If you were to put one of these devices on your LAN, it would take down your LAN very rapidly. So we isolate each different video source into its own VLAN. Now whatever decoders are in an encoder's VLAN receive its signal. If I want to watch something different I move the encoder connected to the TV I am watching to a different VLAN. We do all of our video switching at the Layer 2 level and we are actively changing the programming of the switch depending on what we want to watch. Using this topology we can build literally any size video system. Examples of places using this product are Ceasar's Palace in Las Vegas, multiple Twin Peaks and Buffalo Wild Wings restaurants. PGA Pro Superstores, and more. I personally manage a hockey arena in Florida that has something like 250 displays and 60 video sources spread across 8 switches. And we do similar routing with all of these and I have never had this issue show up at any customer nor have I had anyone complain to me. This situation I am having is unique and we have been building out these systems for the past 10 years in the manner I will explain. It's a little "non-standard" in terms of normal networking but it works.We set up ports on our switches to use "General" mode where you need to assign both a VLAN and a PVID. For those who don't know, the PVID is what is used as the "transmit" VLAN while listening happens on any other VLAN(s) assigned to that switch port. All traffic by the way is untagged.All the decoders are put into their own VLAN which we typically call VLAN 10. Their PVID is then 10. So in my network, all the decoders get an IP address in the 10.0.10.0/8 space. But here's where it gets interesting. The VLAN on the switch is set up as 10.0.10.1/24. And that's on purpose. Yes it break some rules but it works quite well for the way we do things. This way only traffic that is in the 10.0.10.1/24 network is allowed on the VLAN but the device can talk to any other device in the 10.0.0.0 subnet. Remember I said before that we move the decoders between transmitter VLANs to decide what we want to watch. But then I said they are on VLAN 10. This is the magic of "general" switchport mode. You can have that port in multiple VLANs. So the primary VLAN that device will transmit on is the PVID. But it will LISTEN on all other VLANs that it is connected do.Now the encoders we want to completely isolate. So they can be put into much smaller networks. I'm using pretty big and inefficient subnets here basically waisting a ton of addresses in a class A subnet. Who cares as it's a private network and I can configure it how I want! In our bigger installations we use much smaller subnets for everything (and actually have a pretty slick standard for how we do it), but the same concept still applies. Anyhow, the transmitters get a similar type of arrangement. In my case the first encoders gets assigned to VLAN 11 with an IP address of 10.0.11.100/8. VLAN 11 is given an address of 10.0.11.1/24. Now the port this encoder is connected to on the switch gets assigned to VLAN 11 with a PVID of all. But it also gets assigned to VLAN 10.Do you follow what is happening now? Transmitters talk to receivers on their VLAN and receivers talk back to transmitters on their VLAN. Where IGMP multicasting is in reality a single duplex one way form of communication, we've now enabled two way communication and ability for our devices to easily communicate with each other and the outside world.In a lot of commercial cases, what we call the "video switch" just handles only video and any control traffic on the LAN is just routed into it. We tell the IT people not to think of it as a network switch but a video appliance on the network that gets an IP and traffic routed to it like anything else. Now what they do on their routers to set the routes - I don't know. I've seen specific VLANs that they create just to put our switches on their network. In other cases it just goes on the LAN.In smaller places and like in my home, the switch shares both video traffic and normal LAN traffic.My diagram is below.IFullSizeRender.jpg ---

## Response 54
A further comment. So part of what I do that requires a lot of bandwidth is we can capture images on our devices and view them on the computer. This integrates well with my software that controls the system. The newest and highest end devices have an MJPEG stream option but we can still capture images nearly as fast as what you get from the MJPEG stream. But most devices are bitmap image captures that we then transfer across the network.The video below shows what this is like. It's not at all intended to be what you watch for high quality viewing. Instead it gives someone operating the system the ability to view what is playing where. We can't allow full quality decode on a computer because of copyright restrictions on the content.https://www.youtube.com/watch?v=jFMIzZ5XbUM ---

## Response 55
It actually makes sense now. Your network design with the mismatching prefix lengths and real-time switching of vlans is not networking best practice, but whatever works for you. Maybe if you haven't started out 10 years ago, you could make use of more modern multicast protocols, but you goal is obviously not to redesign the system, so I won't comment on it furtherSo you really want the the Mikrotik to route between both the internet, the 192.168.0.0/23 and 10.0.0.0/8 worlds. Gotcha.The EdgeSwitch is a bit limited in its L3 capabilities and the configuration is a bit nonstandard. I am not intimately familiar with it, so please take everything I say about configuring it with a grain of salt.Your best bet in this case is to make the connection between the Mikrotik and the switch a trunk connection with two vlans. One would be the vlan for the 192.168.0.0/23 subnet. On this vlan no routing whatsoever should take place on part of the switch; it should simply act as a managed switch, with untagged ports towards your devices and a tagged port to the Mikrotik. The other vlan should be the one carrying the routing subnet, and to this an address (in my exmaple 192.168.111.10) and a default route (in my example via 192.168.111.9) should be assigned. (Previously I wrote that a route to 192.168.0.0/23 should be added. I misspoke, obviously a default should be added.)It is possible to do this without vlan tagging and trunking, but this is the cleaner way.The Mikrotik should obviously be configured to accept these two vlans and make proper use of them.The simplest (but not best!) way to do this is to remove this (10G) port from the bridge, add two vlan interfaces to it (with the appropriate tags), put one (the one carrying the 192.168.0.0/23 subnet) back into the bridge, and on the other vlan an address should be assigned.While this should work for testing purposes, this is in fact not the correct design. The rb5009 includes a quite powerful Marvell switch chip, which has good vlan support. The nice design is to have all relevant ports bridged, enable VLAN filtering and use the managed switch the designers included according to its purpose.VLAN filtering on Mikrotiks is a topic in and of itself, and there are many tutorials on this forum available to help you. So I would suggest you to try out the first (non-optimal) approach, and then add VLAN filtering after its working. You seem quite familiar with linux, so a good place to learn about this is to read up on the linux DSA (Distributed Switching Architecture), because this is what enabling the setting "VLAN filtering" actually invokes. As with many other things, how you configure it on linux is exactly how you have to configure in the Mikrotik world. ---

## Response 56
It actually makes sense now. Your network design with the mismatching prefix lengths and real-time switching of vlans is not networking best practice, but whatever works for you. Maybe if you haven't started out 10 years ago, you could make use of more modern multicast protocols, but you goal is obviously not to redesign the system, so I won't comment on it furtherActually Just Add Power started doing this in 2010 but that was strictly L2 switching at the time. Yeah, you potentially could use more modern multicast protocols but this works and quality of video is the most important factor here. We are talking streaming bandwidths of as high as a gigabit.So you really want the the Mikrotik to route between both the internet, the 192.168.0.0/23 and 10.0.0.0/8 worlds. Gotcha.Ideally. Ubiquity's own help docs show a similar proposal to what you have made...Your best bet in this case is to make the connection between the Mikrotik and the switch a trunk connection with two vlans. One would be the vlan for the 192.168.0.0/23 subnet. On this vlan no routing whatsoever should take place on part of the switch; it should simply act as a managed switch, with untagged ports towards your devices and a tagged port to the Mikrotik. The other vlan should be the one carrying the routing subnet, and to this an address (in my exmaple 192.168.111.10) and a default route (in my example via 192.168.111.9) should be assigned. (Previously I wrote that a route to 192.168.0.0/23 should be added. I misspoke, obviously a default should be added.)OK. So the VLAN for the 192.168.0.0/23 stuff is easy as it's already on its own VLAN since you can't use the management VLAN for routing. So that's easy - add it to a trunk.Now the problem is the 10.0.0.0 data. I could add every VLAN to the trunk except now we are going to be passing gigabits of data up to the Mikrotik. That seems like it should not be necessary. I guess I create a second VLAN for the 10.0.00 L3 traffic and set a route on the Ubiquity switch to route into that subnet? I'm a little foggy on that one. I'll check the Ubiquity docs since they are very similar to what you propose.Edit: AND RATS!!!! The stupid Ubiquity has a maximum of 15 routable VLANs and I am already there. I can't add another... Grrr...VLAN filtering on Mikrotiks is a topic in and of itself, and there are many tutorials on this forum available to help you. So I would suggest you to try out the first (non-optimal) approach, and then add VLAN filtering after its working. You seem quite familiar with linux, so a good place to learn about this is to read up on the linux DSA (Distributed Switching Architecture), because this is what enabling the setting "VLAN filtering" actually invokes. As with many other things, how you configure it on linux is exactly how you have to configure in the Mikrotik world.When you say I am quite familiar with Linux, you are too kind! Honestly, I am pretty limited. But let me see if I can get this concept to work on the Mikrotik as you explained. I'm just at a loss as to why I have never had to jump through these hoops with every other router I have had. I just entered the route and off I went. I guess that still doesn't mean things were set up "correctly." It's clear that the routing from the LAN to the 10.0.0.0 subnet is going through the router. But the return traffic is not.Another Edit..Upon thinking about this further, I am thinking that the only way I can do this is to trunk ALL the VLANs up to the Mikrotik. There's still plenty of bandwidth in the 10 Gbit link. Then do all the routing there. Wish I didn't have to send the IGMP data up the trunk but I'm not sure how to do this otherwise... ---

## Response 57
Hi, A little off topic now maybe.I trialled a much simplified version of this system on a Hex (much slower/smaller), to verify some things I thought I knew...It turns out as mentioned by @lurker888, marking the packets as notrack does seem to mean they can't be fasttracked.(under ip settings you can see the fasttrack packet counters)They still get accepted in the next default rule usually, but all these packets have to traverse the full firewall.I then trialled forcing the return traffic exiting the switch to go via the router (hex) instead of direct to the device, (return via the router is how the router wants the traffic to go), and with the notrack rules disabled.This allowed the packets to be fasttracked, and its performance then was a worthwhile amount faster than using the notrack marking.I did have to jump through some hoops to get the network in a state to get these results though.By default, when trying to connect to devices behind the L3 Switch, the hex would send an icmp packet to my PC, saying if you want to get to that IP address, use this other gateway (the L3 switch). And my pc would then talk direct to the L3 switch, and it was quicker again, and no work needed by the router at all. But likely not compatible with all devices.The DHCP option mentioned by @lurker888 is likely to result in a similar outcome.I had to disable the send redirects, and secure redirects options (under ip settings) and then reboot the hex, before it would not send these.This resulted in maybe similar connectivity issues to the device on the other subnet to what you had. Tcp didn't seem to work, pings seemed fine.With notrack rules getting it to work quite well, and symmetric routing and fasttrack being better again. ---

## Response 58
The question is how do I force my switch to send all LAN subnet traffic to the router instead of direct. I tried adding a route and it didn't do anything. ---

## Response 59
The question is how do I force my switch to send all LAN subnet traffic to the router instead of direct. I tried adding a route and it didn't do anything.That's it. You can't. The route you add would conflict with the directly connected one. A separate subnet is the correct way.Especially if you are doing multicast stuff, there is no way around properly configured routing. ---

## Response 60
[...]OK. So the VLAN for the 192.168.0.0/23 stuff is easy as it's already on its own VLAN since you can't use the management VLAN for routing. So that's easy - add it to a trunk.Now the problem is the 10.0.0.0 data. I could add every VLAN to the trunk except now we are going to be passing gigabits of data up to the Mikrotik. That seems like it should not be necessary. I guess I create a second VLAN for the 10.0.00 L3 traffic and set a route on the Ubiquity switch to route into that subnet? I'm a little foggy on that one. I'll check the Ubiquity docs since they are very similar to what you propose.Edit: AND RATS!!!! The stupid Ubiquity has a maximum of 15 routable VLANs and I am already there. I can't add another... Grrr...Ok, you've lost me here.1. Why do we want to trunk all VLANs to the Mikrotik? Correctly addressed packets will get to it due to routing on the second VLAN. (I'm not saying you shouldn't do this - I just don't understand the reason.)2. Even if we wish to trunk all ports to the Mikrotik, this does not involve routing, simply make this port a tagged member of the given VLANs and the switch will direct appropriate packets there due to switching behavior.[...]When you say I am quite familiar with Linux, you are too kind! Honestly, I am pretty limited. But let me see if I can get this concept to work on the Mikrotik as you explained. I'm just at a loss as to why I have never had to jump through these hoops with every other router I have had. I just entered the route and off I went. I guess that still doesn't mean things were set up "correctly." It's clear that the routing from the LAN to the 10.0.0.0 subnet is going through the router. But the return traffic is not.Well... The reasons why Mikrotik is a bit different:* The rb5009 device that you bought incorporates *both* a managed switch and a router. Both pretty powerful. For things to work optimally, you have to basically configure two devices. Generally other vendors - even when they incorporate the same hardware (which at these price points is rare) - neuter the interface and either call themselves routers and present the switching component as SVIs, or call themselves switches and severely limit the routing part.* Other vendors' SOHO/SMB routers have a default "hairpin nat" rule, which changes the source IP of packets to that of the router, and therefore the router gets the reply packet as well. (Of course once receiving the reply, it changes the dst addr back...) This is not the correct way to do this, and - while it mostly works - breaks in unpredictable ways. (Although in some specific cases it is a necessary thing to do.)Another Edit..Upon thinking about this further, I am thinking that the only way I can do this is to trunk ALL the VLANs up to the Mikrotik. There's still plenty of bandwidth in the 10 Gbit link. Then do all the routing there. Wish I didn't have to send the IGMP data up the trunk but I'm not sure how to do this otherwise...This is the first time you mention that you use IGMPPlease be aware that multicast traffic is not routed by normal routing mechanisms. Some help is needed in these cases. This can be IGMP. Mikrotik does IGMP proxying (and snooping if needed). If you do trunk these VLANs to the Mikrotik, as I have proposed above, and IGMP snooping is turned on in your switch, then only the feeds that a device has subscribed to will actually flow to the Mikrotik. ---

## Response 61
Another slight possibility, I don't know if this will work at all, it depends a lot on the L3 switch.You could reconfigure the DHCP server on the 5009 to point the default route of the LAN network at the L3 switch IP Address.Then the devices would send their packets to the switch (for both internet traffic, and VLAN traffic)Andhopefullythe switch will just bounce internet traffic straight back to the 5009, while passing the VLAN traffic through.Then the 5009 would forward this traffic to the internet and forward the return traffic direct to the device.Still strictly triangle/asymmetric routing, however the switch will likely be stateless, and not care, and the 5009 doesn't see any asymmetric traffic.And Lan-Vlan traffic is purely between the device, the switch and the vlan, so should be very fast. ---

## Response 62
[...]OK. So the VLAN for the 192.168.0.0/23 stuff is easy as it's already on its own VLAN since you can't use the management VLAN for routing. So that's easy - add it to a trunk.Now the problem is the 10.0.0.0 data. I could add every VLAN to the trunk except now we are going to be passing gigabits of data up to the Mikrotik. That seems like it should not be necessary. I guess I create a second VLAN for the 10.0.00 L3 traffic and set a route on the Ubiquity switch to route into that subnet? I'm a little foggy on that one. I'll check the Ubiquity docs since they are very similar to what you propose.Edit: AND RATS!!!! The stupid Ubiquity has a maximum of 15 routable VLANs and I am already there. I can't add another... Grrr...Ok, you've lost me here.1. Why do we want to trunk all VLANs to the Mikrotik? Correctly addressed packets will get to it due to routing on the second VLAN. (I'm not saying you shouldn't do this - I just don't understand the reason.)2. Even if we wish to trunk all ports to the Mikrotik, this does not involve routing, simply make this port a tagged member of the given VLANs and the switch will direct appropriate packets there due to switching behavior.Agreed. It doesn't involve routing. But it passes a lot of traffic over the fiber link. My problem is the Ubiquity switch doesn't have any more routable VLANs available. So I can't create another VLAN to route all the 10.0.0.0 traffic into on the switch. If I brought all the VLANs up to the MikroTik, then I could handle all the routing between them there. That was my point. But I'd rather not do that.Well... The reasons why Mikrotik is a bit different:* The rb5009 device that you bought incorporates *both* a managed switch and a router. Both pretty powerful. For things to work optimally, you have to basically configure two devices. Generally other vendors - even when they incorporate the same hardware (which at these price points is rare) - neuter the interface and either call themselves routers and present the switching component as SVIs, or call themselves switches and severely limit the routing part.* Other vendors' SOHO/SMB routers have a default "hairpin nat" rule, which changes the source IP of packets to that of the router, and therefore the router gets the reply packet as well. (Of course once receiving the reply, it changes the dst addr back...) This is not the correct way to do this, and - while it mostly works - breaks in unpredictable ways. (Although in some specific cases it is a necessary thing to do.)That is actually really cool and you are right - for the price point that is great. I think my EdgerouterX is using a hairpin NAT. I'm not positive but I seem to remember something about that.Another Edit..Upon thinking about this further, I am thinking that the only way I can do this is to trunk ALL the VLANs up to the Mikrotik. There's still plenty of bandwidth in the 10 Gbit link. Then do all the routing there. Wish I didn't have to send the IGMP data up the trunk but I'm not sure how to do this otherwise...This is the first time you mention that you use IGMPI mentioned it earlier. That's what our hardware uses to send the video data. We don't use IGMP snooping or any of those sorts of protocols with it. It's all left on Layer 2. The reason is we don't want this traffic to be managed or controlled by the switch. We want it just to flow.Also, I don't want the MikroTick to manage any IGMP traffic. My point about all the traffic going to the MikroTik is that if I create the VLANs on the MikroTik and then trunk all the VLANs up to it, all the traffic on the VLANs will flow through the connection between the switch and the Mikrotik. This is roughly about 3 to 4 Gbit/sec of traffic. ---

## Response 63
Another slight possibility, I don't know if this will work at all, it depends a lot on the L3 switch.You could reconfigure the DHCP server on the 5009 to point the default route of the LAN network at the L3 switch IP Address.Then the devices would send their packets to the switch (for both internet traffic, and VLAN traffic)Andhopefullythe switch will just bounce internet traffic straight back to the 5009, while passing the VLAN traffic through.Then the 5009 would forward this traffic to the internet and forward the return traffic direct to the device.Still strictly triangle/asymmetric routing, however the switch will likely be stateless, and not care, and the 5009 doesn't see any asymmetric traffic.And Lan-Vlan traffic is purely between the device, the switch and the vlan, so should be very fast.Well, for that matter if I set the gateway IP in the DHCP server to be the IP address of the L3 switch, then it works. Maybe that's the easiest way to solve this. My only comment was that now internet traffic is going through an extra router hop (ie: the L3 switch) but it's probably very fast anyhow. Is this what you are saying to do?Edit: Looks like setting things this way adds about another 1 to 12 ms to get to the router. The router response is very fast - like 0.5 ms. The switch does seem to be somewhat slow, but now I have no routing issues. I guess it can work this way..Yes? ---

## Response 64
Okay. It seems we're making headwayLet me respond to several comments in one post. I will omit citations, it's just too much work.To IGMP/IGMP snooping. IGMP snooping actually *does* happen at L2. If you don't want to use it that's fine. Actually IGMP snooping implementations have well known interop issues, so maybe it's for the best. As I gather you're selling to clients who don't really mind a couple hundred dollars of additional equipment, but would be absolutely furious if a live event were to be disrupted by these issues. Again, none of my business.If your trunking scenario can be handled in L2, then the rb5009 is capable of handling wire speed on all ports, and this will not entail any CPU load - it's offloaded the the switch chip in the device.Designating the L3 switch as the gateway does solve the issue with triangular routing, but that means that you have no control over the traffic in the rb5009 device. To elaborate: you *do* have control the traffic between what's connected to the rb5009 and the 192.168.* and 10.* subnets, but between the 192.168.* and 10.* you have no control.I would assume (yeh, stupid me) that the higher latency of 12ms comes from some sort of traceroute. I would advise you not to take such measurements as a basis for assessing packet routing latency, because in L3 switches, routing is offloaded to hardware (ASIC), but to preserve silicon real estate these only includes functions for normal forwarding scenarios (incl. blackhole), and when some response such as TTL exceeded are needed - which traceroute relies on - it calls upon the CPU to get involved, which can be arbitrarily slow. This does not mean that other normal traffic would be similarly delayed.EDITI wrote:Another question: What is your goal exactly: Do you want the Mikrotik to serve only as a DHCP server and handle NAT? Or would you like it to do other things a well (filter traffic, so for example the 192.168.0.0/23 can "talk to" the 10.0.0.0/8 devices, but not vice versa, etc., or maybe provide a VPN gateway...)?You said that you want the second. If you designate the EdgeSwitch as the router for the 192.168.0.0/23 network, then you are going with the first. (Which may in fact be what you want... no harm in that, it's a solid design.) ---

## Response 65
Yes, we trade stability and performance for cost. You hit the nail on the head! You'd be amazed how funky people get about being able to view their TV!As for trunking up to the rb5009, it's not a concern of the hardware, it's more of the idea of the amount of constant traffic over the link. It runs pretty much a constant 3 to 5 Gb over the uplink. Since we have a 10Gb link, I guess that's no issue. Worth a shot and I might do it.Truthfully, I've made too many changes at once. I had a different switch that was doing my inter-VLAN routing and I removed that and switched routing to the Ubiquity switch the same time I swapped routers. And I'm seeing funky routing out of the Ubiquity switch. I think it's the Ubiquity switch since right now, I'm not using the rb5009 for the routing. So maybe it's a good idea to send everything up to the rb5009 and do all my routing there... ---

## Response 66
So I'm adding VLANs to the Mikrotik. Here's what I am seeing so far, but I am not sure I am doing it correctly:
```
/interface vlan
add interface=bridge mtu=9212 name=vlan10 vlan-id=10
......
/ip address
add address=192.168.1.1/23 comment=defconf interface=bridge network=\
    192.168.0.0
add address=10.0.10.1/8 interface=vlan10 network=10.0.0.0Do I create all the VLANs and put them on the bridge?  Or do I set the tag and assign them all to the SPF connection?Thanks.

---
```

## Response 67
Well... what you wrote may be correct, depending on other settings. The gist of it is there.Before commenting further, please answer this: are you aware of the behavior of bridges in Linux (the same in Mikrotik) to "enslave" the interfaces assigned to them? (You seem to be...) Are you setting VLAN filtering to enabled on the bridge? (If you are not, then please don't do so before creating a backup of your config - you can very easily lose full and all connectivity to the router) ---

## Response 68
I am not really aware of the behavior of bridges in Linux. I am aware of how VLANs work in systems like Cisco, HP, Ubiquity, etc.I know the bridge is basically the overall fabric of the switch.Right now, I have created all my VLANs, assigned IPs to them, but they are all just assigned to the bridge. I think what's I need to do is set the tagging on them and assign them to the SFP port which is my connection between the L3 switch and the Mikrotik. But I'm afraid that when I do that, if I do it wrong I will lose all connectivity. I don't know if the MicroTik has an RS-232 connection available through its USB port but I'm afraid of breaking things! So I want to proceed carefully. ---

## Response 69
I am not really aware of the behavior of bridges in Linux. I am aware of how VLANs work in systems like Cisco, HP, Ubiquity, etc.I know the bridge is basically the overall fabric of the switch.Right now, I have created all my VLANs, assigned IPs to them, but they are all just assigned to the bridge. I think what's I need to do is set the tagging on them and assign them to the SFP port which is my connection between the L3 switch and the Mikrotik. But I'm afraid that when I do that, if I do it wrong I will lose all connectivity. I don't know if the MicroTik has an RS-232 connection available through its USB port but I'm afraid of breaking things! So I want to proceed carefully.The way Cisco et al behaves is different from the way Linux does it.You are right in many ways:* assigning vlans to the bridge! Way to go!* you are way right to assume that you will lose all connectivity if you incorrectly configure the switch - you will. Again: way to go!You will have to pull the trigger on no. 2 sooner of later. What you can do to mitigate this:* create a backup of your confoguration* configure a port "off-bridge" - this means to remove e.g. ether8 from the bridge, and set up an address (otherwise unused) on it to access the router while troubleshooting (with def fw don't forget to add the port to the LAN iface list)If you follow the second advice, you have as long as it takes to get you VLAN config in order. Please follow the first, this is an assurance that if a total connectivity failure comes up, you can resume where you left off. (In Mikrotiks, pressing the reset button while under power cycle instructs the device to return to factory defaults, which allows you to try again. It's an inconvenience but it will not be bricked.) ---

## Response 70
OK. Trying to make this off-bridge port. Below is what I have set up, but if I disconnect the SFP port and connect port 8, I get no connectivity. I'm not able to ping 192.168.1.254...What am I doing wrong...
```
/interface ethernet
set [ find default-name=ether1 ] l2mtu=9216 mtu=9216
set [ find default-name=ether2 ] l2mtu=9216 mtu=9216
set [ find default-name=ether3 ] l2mtu=9216 mtu=9216
set [ find default-name=ether4 ] l2mtu=9216 mtu=9216
set [ find default-name=ether5 ] l2mtu=9216 mtu=9216
set [ find default-name=ether6 ] l2mtu=9216 mtu=9216
set [ find default-name=ether7 ] l2mtu=9216 mtu=9216
set [ find default-name=ether8 ] l2mtu=9216 mtu=9216
set [ find default-name=sfp-sfpplus1 ] l2mtu=9216 mtu=9216
/interface vlan
add interface=bridge mtu=9212 name=vlan10 vlan-id=10
add interface=bridge mtu=9212 name=vlan11 vlan-id=11
add interface=bridge mtu=9212 name=vlan12 vlan-id=12
add interface=bridge mtu=9212 name=vlan13 vlan-id=13
add interface=bridge mtu=9212 name=vlan14 vlan-id=14
add interface=bridge mtu=9212 name=vlan15 vlan-id=15
add interface=bridge mtu=9212 name=vlan16 vlan-id=16
add interface=bridge mtu=9212 name=vlan17 vlan-id=17
add interface=bridge mtu=9212 name=vlan18 vlan-id=18
add interface=bridge mtu=9212 name=vlan19 vlan-id=19
add interface=bridge mtu=9212 name=vlan20 vlan-id=20
add interface=bridge mtu=9212 name=vlan21 vlan-id=21
add interface=bridge mtu=9212 name=vlan121 vlan-id=121
add interface=bridge mtu=9212 name=vlan122 vlan-id=122
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/ip pool
add name=dhcp ranges=192.168.0.3-192.168.0.255
/ip dhcp-server
add address-pool=dhcp interface=bridge lease-time=1w name=defconf
/disk settings
set auto-media-interface=bridge auto-media-sharing=yes auto-smb-sharing=yes
/interface bridge port
add bridge=bridge comment=defconf interface=ether2
add bridge=bridge comment=defconf interface=ether3
add bridge=bridge comment=defconf interface=ether4
add bridge=bridge comment=defconf interface=ether5
add bridge=bridge comment=defconf interface=ether6
add bridge=bridge comment=defconf interface=ether7
add bridge=bridge comment=defconf interface=sfp-sfpplus1
add bridge=bridge comment=defconf interface=none
/ip neighbor discovery-settings
set discover-interface-list=LAN
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=ether8 list=LAN
/ip address
add address=192.168.1.1/23 comment=defconf interface=bridge network=\
    192.168.0.0
add address=10.0.10.1/24 interface=vlan10 network=10.0.10.0
add address=10.0.11.1/24 interface=vlan11 network=10.0.11.0
add address=10.0.12.1/24 interface=vlan12 network=10.0.12.0
add address=10.0.13.1/24 interface=vlan13 network=10.0.13.0
add address=10.0.14.1/24 interface=vlan14 network=10.0.14.0
add address=10.0.15.1/24 interface=vlan15 network=10.0.15.0
add address=10.0.16.1/24 interface=vlan16 network=10.0.16.0
add address=10.0.17.1/24 interface=vlan17 network=10.0.17.0
add address=10.0.18.1/24 interface=vlan18 network=10.0.18.0
add address=10.0.19.1/24 interface=vlan19 network=10.0.19.0
add address=10.0.20.1/24 interface=vlan20 network=10.0.20.0
add address=10.0.21.1/24 interface=vlan21 network=10.0.21.0
add address=10.0.121.1/24 interface=vlan121 network=10.0.121.0
add address=10.0.122.1/24 interface=vlan122 network=10.0.122.0
add address=192.168.1.254/23 interface=ether8 network=192.168.0.0Edit:And this is what I don't understand. If I have Ethernet 8 removed from the bridge, then if I have an IP address assigned to it but the port is not connected to my network, then I should not be able to ping that address.  But I can.  So I have something wrong...Seeems like I haven't really removed it from the bridge...

---
```

## Response 71
The things you might have missed:* You should assign an address/subnet to ether8 that is *different* from the one you use otherwise use e.g. 192.168.100.0.1/24* You should add ether8 to the interface list LAN, so the firewall doesn't block you* You should configure your PC to have a static address (not DHCP) with an address available such as 192.168.100.10 255.255.255.0 ---

## Response 72
The things you might have missed:* You should assign an address/subnet to ether8 that is *different* from the one you use otherwise use e.g. 192.168.100.0.1/24This I did not do. It was just an unused address in my regular subnet.* You should add ether8 to the interface list LAN, so the firewall doesn't block youI did do this:
```
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=ether8 list=LAN* You should configure your PC to have a static address (not DHCP) with an address available such as 192.168.100.10 255.255.255.0OK.  I will need to do that...Let me try that out....

---
```

## Response 73
Something isn't right. I cannot ping the new address at all - even when my computer is connected directly to port 8 on the router and I have an address in the 192.168.100.0 subnet...
```
/interface ethernet
set [ find default-name=ether1 ] l2mtu=9216 mtu=9216
set [ find default-name=ether2 ] l2mtu=9216 mtu=9216
set [ find default-name=ether3 ] l2mtu=9216 mtu=9216
set [ find default-name=ether4 ] l2mtu=9216 mtu=9216
set [ find default-name=ether5 ] l2mtu=9216 mtu=9216
set [ find default-name=ether6 ] l2mtu=9216 mtu=9216
set [ find default-name=ether7 ] l2mtu=9216 mtu=9216
set [ find default-name=ether8 ] l2mtu=9216 mtu=9216
set [ find default-name=sfp-sfpplus1 ] l2mtu=9216 mtu=9216
<snip>
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/ip pool
add name=dhcp ranges=192.168.0.3-192.168.0.255
/ip dhcp-server
add address-pool=dhcp interface=bridge lease-time=1w name=defconf
/disk settings
set auto-media-interface=bridge auto-media-sharing=yes auto-smb-sharing=yes
/interface bridge port
add bridge=bridge comment=defconf interface=ether2
add bridge=bridge comment=defconf interface=ether3
add bridge=bridge comment=defconf interface=ether4
add bridge=bridge comment=defconf interface=ether5
add bridge=bridge comment=defconf interface=ether6
add bridge=bridge comment=defconf interface=ether7
add bridge=bridge comment=defconf interface=sfp-sfpplus1
add bridge=bridge comment=defconf interface=none
/ip neighbor discovery-settings
set discover-interface-list=LAN
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=ether8 list=LAN
/ip address
add address=192.168.1.1/23 comment=defconf interface=bridge network=\
    192.168.0.0
<snip>
add address=192.168.100.254/24 interface=ether8 network=192.168.100.0Where am I doing it wrong??The 8th spot on the bridge is assigned to none:
```

```
add bridge=bridge comment=defconf interface=noneEthernet 8 is added to LAN:
```

```
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=ether8 list=LANAnd Ethernet 8 has an IP:
```

```
add address=192.168.100.254/24 interface=ether8 network=192.168.100.0

---
```

## Response 74
Post ping response. It is "ICMP dst unreachable" or timeout or something else?When you have item unknown in for example bridge config, that means that there are some messed up references in the configuration database (reference to an item that somehow no longer exists). You are best off deleting those entries. ---

## Response 75
```
jon@Jons-Mac-mini ~ % ping 192.168.100.254
PING 192.168.100.254 (192.168.100.254): 56 data bytes
Request timeout for icmp_seq 0
Request timeout for icmp_seq 1
Request timeout for icmp_seq 2
Request timeout for icmp_seq 3
ping: sendto: No route to host
Request timeout for icmp_seq 4
ping: sendto: Host is down
Request timeout for icmp_seq 5
ping: sendto: Host is down
Request timeout for icmp_seq 6OK.  I will completely remove the entry...

---
```

## Response 76
I deleted the last entry for the bridge. Still no dice.Full config attached. I really appreciate the help... ---

## Response 77
This means that there is a problem on your PC (Windows, I would assume.) The route is not correctly installed. If the route were installed you would get the message "unreachable".Maybe you have a connection from you PC both to WiFi, which provides Internet access, and to this network which does not, Consumer OS's have habit of preferring ones that do (and completely neglecting ones that don't) networks that don't provide Internet access. Try disconnecting wifi. Altogether: configure your PC for a static address *only* on the given interface. ---

## Response 78
It's a Mac. There's one NIC active. My WiFi is turned off. I don't have a route file.Screenshot 2025-01-20 at 3.29.45 PM.pngScreenshot 2025-01-20 at 3.30.55 PM.png ---

## Response 79
And still no ping. Do you get a ping/connectivity from elsewhere?EDITI mean connecting to another port of the router, etc.EDIT2:Reread the thing. Of course it's a mac. "no route" means that the route to directly connected is not installed. Although many developers do, I have never used a mac as my main machine. Why this would occur - no idea. ---

## Response 80
OK. This is weird. It is working on port 7 of the router....But ether7 is on the bridge. The port numbers in the config should match the physical ports yes?And my Mac is definitely on 192.168.100.0...
```
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 9000
	options=50b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV,CHANNEL_IO>
	ether 5c:1b:f4:7e:73:12
	inet6 fe80::82d:99c:7421:df8a%en0 prefixlen 64 secured scopeid 0x6 
	inet6 fd61:d1de:4416:9900:d5:ece:bb10:4ab2 prefixlen 64 autoconf secured 
	inet 192.168.100.16 netmask 0xffffff00 broadcast 192.168.100.255
	nd6 options=201<PERFORMNUD,DAD>
	media: 1000baseT <full-duplex>
	status: activeOK..  I can connect using the 192.168.100.0 subnet for ANY ethernet port on the router except ethernet port 8.  Was I doing it wrong connecting to port 8?

---
```

## Response 81
OK. This is weird. It is working on port 7 of the router....But ether7 is on the bridge. The port numbers in the config should match the physical ports yes?Actually this is the expected behavior. This means that the router is at least functioning as it should.The router responds on *all* of its addresses regardless of interface by default. This may be a bit confusing - and it is - but this is called weak/strong host model, and it is a thing. I dare you to look it up, follow what few references there are, and come back with your hair half torn out.Meanwhile this is a good sign.Post FULL config, I will take a look at what might be f***ing you up. ---

## Response 82
This may be a bit confusing - and it is - but this is called weak/strong host model, and it is a thing. I dare you to look it up, follow what few references there are, and come back with your hair half torn out.No thanks. I'll take your word on it!Attached is the full config... ---

## Response 83
OK. I have some good news. I have removed the VLANs from the bridge and added them as tagged to the SFP port. I have now configured a trunk on the Ubiquity switch and VLAN traffic is flowing to the Mikrotik! And I have not lost control of the Mikrotik either...However, I'm not sure how to route traffic into those VLANs that I have tagged. I'm afraid to assign the trunk to the bridge. I'm afraid that is going to flood it with the 3 Gbits of video streams... ---

## Response 84
Okay. I don't exactly understand everything, but I'm glad you1re gaining headway.I have a slow day, so if you wish, I'd be willing to help you clear up some things in a more interactive channel (by this I mean having a chat via Google Meets). By now I'm actually interested in who I'm talking to.Let me know if you're interested. ---

## Response 85
Sure. I'm good with that. I don't know if there's private messages available here. How do you want me to get you my info? ---

## Response 86
[removed] ---

## Response 87
[removed] ---

## Response 88
Sure. ---

## Response 89
I feel quite strange that when we talk about the L3 offload, the Mikrotik always talk about the enterprise level switch chip.But lots of CPU has the L3 accelerator, which can highly improve the device NAT/QOS.Including all Qualcomm's NPU, Packet Processor in ARMADA 7040, and hardware NAT in MT7621AThe only reason I can see the Mikrotik didn't support is that these chips are fragmentate in different types of devices. ---

## Response 90
Hi all, A quick update.Lurker888 and I have been working in a Google chat and we got everything working really well. The issue was the triangular routing. We have trunked all my VLANs up to the router and applied some filtering and it all works great! Very pleased.Lurker888 knows his stuff! Kudos to him! ---

## Response 91
Lurker888 knows his stuff! Kudos to him!Thank you for showing your appreciation; IMO Lurker and others add so much here the acknowledgment is well deserved. ---

## Response 92
Might be helpful for others to show what the end result is and what modifications made things work ---

## Response 93
Sure!Before we did anything we enabled setting the CPU frequency to a fixed, maximum frequency and making a second partition of the storage space so things could easily get reverted if they got mucked up.First of all - on the router, we created the VLANs that I needed to route intoSecond - Took port 8 of the router off the bridge and gave it an IP in a completely different subnet. That way if we lost connectivity when adding in the VLANs, we could still get access to the router.Third - gave IPs to the VLANsFourth - turned on VLAN filtering and set up tagging on the interfacesFifth - created the "LAN" VLAN and made sure that this was assigned to all ports on the switch and that DHCP hands out address on this VLAN.Sixth - Created the trunk VLAN on the fiber portSeventh - Created the trunk on the switchAt this point we got things tested out and working. The last step was setting a filtering rule so that we drop the multicast packets from my video streams so that the router doesn't have to mess with handling those - saves CPU time. There was some other minor stuff as well and just learning where things are at in all the different menus, etc. Somethings are intuitive and some are not (and example is how you filter the multicast).It might be easiest to post my config which is what I am doing here. It's a bit more work than I explained above (it sounds easy!). ---

## Response 94
I've created a step by step guide that will hopefully help others. I believe I captured all the steps. Please let me know if you find this helpful. ---

## Response 95
Thanks, Could you consider creating the new topic in the "Useful articles"viewforum.php?f=23and put that manual there? ---

## Response 96
Sure. Didn't know that existed! ---