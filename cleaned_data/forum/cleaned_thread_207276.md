# Thread Information
Title: Thread-207276
Section: RouterOS
Thread ID: 207276

# Discussion

## Initial Question
I am having an issue where wireguard just stops handshaking. Despite that I see packets arriving to the wireguard "server" it won't handshake.It is weird because it may be working fine for weeks and suddenly it stops exhanging data. All I do to "solve" it temporarily is to change the port and immediately it is back for weeks again.What could I possibly check to prevent it from happening? ---

## Response 1
it is still doing it. It has happened something like 5 times since my initial post.It randomly stops communicating and all I have to do is change the port.To make it faster I have made a NAT rule that receives packets on 23231 and translates them to 13231 so the only thing I have to change is the peer port from 13231 to 23231.It works for something like 10 days and then it stops working. I then change the port back to 13231 and it starts again. After a few days that it stops again I change it to 23231 and it works again.Any ideas?I don't want to go back to sstp/l2tp which I have done already to some installations! ---

## Response 2
Not enough information.no config, no network diagramno understanding of what is at the two ends of the wireguard connectionetcetc ---

## Response 3
network config is huge.Let's say that the wg "server" is on the datacenter with a static IP and the client is behind CGNAT.Everything is working fine up until some point where I start getting Handshake for peer did not complete after 5 seconds, retrying (try 2).The server is listening at port 13108 and it is working fine up until the error comes and it won't handshake any more.I can see packages arriving at that port from the correct source ip but I get this error. Then what I do is I have a dst-nat from port 23108 udp to destination port 13108.The moment I change the peer in the client and set port 23108 it starts working fine... up until after days where it starts doing it in the 23108 port.Then all I do is change the port to the peer of the client back to 13108 and immediately it starts handshaking/working fine. Up until the customer calls me again to tell me that his VPN is not workingIt is not happening only in one customer. I have this probably in 10 different setups. Some of the I moved them back to l2tp because it has been breaking my... a lot.One of the things that I have tried is to disable and enable both the peers and the wg interfaces and clean all network connections of both end but it still didn't solve it.Other that that bloody wg works like a charm! ---

## Response 4
now on one that I had the issue I managed to make it working again by disabling the peer on the client wg and enabling it again without changing anything else.It just started working.Other times I even try to restart the client mt but it doesn't work. Now I disabled/enabled the peer and it started handshaking again ---

## Response 5
What version of RoS on the router?Does it resemble this error.......viewtopic.php?t=207686 ---

## Response 6
7.14.3 ---

## Response 7
Let's say that the wg "server" is on the datacenter with a static IP and the client is behind CGNAT.Are you completely sure that the network between both WG peers is as transparrent as you'd want it to be (i.e. the only thing playing games with packets is the CG NAT on the "client" side)? I can imagine some network operator which would drop any long-lasting connections due to some reason (1. just because they can; 2. these don't seem "legit" connections so let's save our users from being extensively hacked; 3. because some government agency tells them to do so; etc.)There was an ISP in my country, which provided (and still does) internet via PPPoE and it used to drop PPPoE connection every night just to force customer getting another IP address. Because static IP address is either a) function of business internet service or b) provided to residential customers for a surcharge ... ---

## Response 8
I have had my router to router wireguard connection stop working.Simple fix was to send pings across the link every so often. Hasn't dropped in months. ---

## Response 9
I have had my router to router wireguard connection stop working.Simple fix was to send pings across the link every so often. Hasn't dropped in months.????????????? That is called persistent keep alive ???????? ---

## Response 10
I have had my router to router wireguard connection stop working.Simple fix was to send pings across the link every so often. Hasn't dropped in months.????????????? That is called persistent keep alive ????????In all setups in the clients I do have persistent keep alive to 25" (seconds)I only skip it in the "server" end that is has external IP in the datacenter. Still in that case the "client" that connects to it has the keep alive set to 25" ---

## Response 11
I have persistent keep alive as default.But here is the netwach I added months ago.
```
/tool netwatchadddisabled=nodown-script=":log info \"!!!Warning VPN Down!!!\""host=\172.16.33.1http-codes=""interval=1mpacket-count=5test-script=""\
    thr-loss-count=5type=icmp up-script=":log info \"VPN to Home Up\""

---
```

## Response 12
Gotsprings, is that on a Router (client peer for handshake)?? ---

## Response 13
Wireguard hAP AC2 to Another hAP AC2 that is behind carrier grade NAT.I VPN to the office... The route lets me jump across the VPN to the other branch. ---

## Response 14
Why would you have the MT router (server for peer), be monitoring the client peer behind CGNAT??? ---

## Response 15
I have same issue on multiple locations every 1-2 days handshake stops, disabling/enabling interface doesn't help, only thing that helps me changing to any random port(client side) and immediately starts working, i can even return very same port which was before and still it will work fine.So i have script which checks last handshake and sends /interface/wireguard set 0 listen-port=0, which sets random port and fixes the tunnel..And i know this is ISP issue because i have this issue ONLY on that specific ISP, we even changed ISP in same cases without changing anything on router and issue disappears. ---

## Response 16
I also thought at first that it was the ISP but I checked the incoming traffic to the "server" wireguard and the I could see traffic at that certain port and if I would disable the client's wireguard it would stop.Unless the ISP modifies something to the packets while it routes to the destination which would be really weird.But indeed I am facing this exact issue where unless I change the port it won't handshake. Except 1/10 times (or less) that restarting the peer "fixes" it ---

## Response 17
Confirmed, I have a Mikrotik with 150 peers and every day one (or more tan one) of the peers loses connectivity and the log only says "Handshake for peer did not complete after 5 seconds, retrying (try 2)" infinitely.I have searched for the reason for the problem without success, I only know that it does not depend on the ISP, and I think it does not depend on the server either since the others peers remain connected without problems.It is only solved by restarting the peer device or assigning a 2nd port for the same interface on the server and using this new port on the peer and if loses conectivity again return to the primary port.MK guys, please review this problem... ---

## Response 18
Just been investigating a similar issue.Central RB5009 with multiple WG peers, on an AC3 250km away WG connection dropped dead, already some days ago.All other peers on that RB5009 remain functional.Both RB5009 and AC3 are on 7.15.1.That WG connection is only for management purposes, no signals from users something is wrong on that site (or I would have known earlier).When going to that AC3 (there is another tunnel from that device via IPSEC to Azure, from there I can get back in as well), no way to revive the WG connection EXCEPT for removing listen port on interface setting (on a remote peer ??) and setting it back as it was (which on itself is useless since it's an outgoing connection for that setup).And then traffic starts flowing again ...Restart probably could have done it as well but it's a rather busy device, so can't do that during business hours.Did anyone ever create a support ticket on this ?I am going to set up extra monitoring and alerting so I get informed sooner about this issue on that device. ---

## Response 19
Why would you have the MT router (server for peer), be monitoring the client peer behind CGNAT???The network at the office is INSIDE another companies network. So I can't do anything with it.The owners home has a public IP. So I set up a router with Wireguard there. Its the "server". The router at the office is a client. It calls the router at home. And the router at HOME is sending the pings to "keep the connection alive."VPN to the house... can reach the office.If he is home... he has access to the office resources by IP address. ---

## Response 20
Did anyone ever create a support ticket on this ?I dont think so. But its worth reporting.so it appear we have two wireguard bugs that MT is doing nothing about.a. dual wan leakage where wireguard response for handshake goes wrongly out primary WAN1, if the shake comes in on secondary WAN2, and this leakage bypasses any mangling.b. Perfectly setup connections between two MT routers drops for no reason...............Both IMHO are resultant bugs of their BTH added code. ---

## Response 21
I have several wireguard tunnels running on one RB5009. First with 7.14.3 and now with 7.15.2.I don't know about 7.14.3, but on 7.15.2 I do see those "Handshake for peer did not complete after 5 seconds, retrying (try 2)" lines. Difference is: the second try IS successful and the tunnel goes on.Two of these links I know have Mikrotiks on the other side (running 7.11 or newer), the other one is a Linux box. Those 3 have this same behavior. The other links I have no idea what they are using on the other side - and didn't see something on the logs. True, it was rotated today and I didn't look at the older one - maybe it's there. ---

## Response 22
So perhaps this was resolved in 7.15.2If anyone with less than 7.15.2, with the error, want to try 7.15.2 and see if the error persists??? ---

## Response 23
So perhaps this was resolved in 7.15.2I don´t think so: I'm getting those errors on 7.15.2 (as stated above), and used 7.14.3 for a long time - and my tunnels worked well there too. Don't know if it had the same log errors, but they worked. ---

## Response 24
So perhaps this was resolved in 7.15.2If anyone with less than 7.15.2, with the error, want to try 7.15.2 and see if the error persists???In my case, the server and 80% of peers are 7.15.2, I started upgrading from 7.12.1 and I see the same simptom y all versions.Please MK guys, review this problem. thanks in advance. ---

## Response 25
Send in trouble tickets or nothing gets done. ---

## Response 26
I just encountered the same problem. Handshake suddenly failing. Changing the listening port of the wireguard interface solved it. Thanks genesispro! The connection to the peer had been up for at least two weeks.In my case there are two Mullvad VPN interfaces. Only one was affected. ---

## Response 27
I'm posting to let everyone know I feel your pain.I too have been having this problem.In my experience the most exposed clients are those on high latency links. Low pings equals less hung wireguard connections. I have a particular client that's on a really bad link with 250 ms on a good day and crawling along at 700 ms in bad weather. That wireguard connection crashes every couple of hours. Which prompted me to setup the watchdog first but it would still not work after reboots. Finally like ivicast I setup a script to set 0 on the port to get a pseudorandom experience.Today a client on starlink dropped out and as it turns out I forgot to run the script on that one. WHYYY!?!?!?!?!? This will cost me a 400 km round trip next week.So this is definitely a bug that needs fixing. According to the changelog last work on Wireguard was on 7.15 and our main router is on 7.15.2. ---

## Response 28
I note on beta 7.17.rc - this line......*) bth - improved stability on system time change;Has anyone with this problem used the latest beta to see if this change fixes it???I am 100% convinced these slew of WG bugs were introduced with BTH changes...........just a theory. ---

## Response 29
Are we REALLY sure this isn't some ISP shenanigans? It would explain why is so serious and not affecting a lot of people at the same time.I mean, I run 8 wireguard tunnels on my RB5009 - 7 of them with latency over 190ms - and I'm not seeing it. Wireguard is quite popular - if it were really broken like reported here, we would have a lot of users complaining on the forum.Since we don't, looks to me like something very particular is happening on this case. If it is the ISP playing with UDP traffic... well, that would explain. ---

## Response 30
Your logic seems very reasonable. ---

## Response 31
We've spent quite some time on a similar case, and the culprit turned out to be the ISP router and daily re-establishment of its uplink connection, seeviewtopic.php?p=1110481#p1110481 ---

## Response 32
same problem for me alsoros to roshandshakes start failinginitializer
```
Handshakeforpeer didnotcomplete after5seconds,retrying(try2)responder
```

```
Handshakeforpeer didnotcomplete after20attempts,giving upon the responder the last handshake time is like some hours while on the initializer 0.disable/ enable the peer on the responder fixes the issue immediatelywhat i have noticed is that the peer on the responder is stuck to an old(previous) Current Endpoint Address, once i disable/ enable it gets the real(current) one.

---
```

## Response 33
@anav, no I haven't tried the beta. Unfortunately I don't have the equipment to spare and run betas parallel to production links.@Paternot no, we're not sure it's not the ISP's fault. But out of the two links that the problem most often presents itself on, on one we have a good relationship with the ISP, their setup is quite simple and transparent and as far as we can tell this is not on them. Whether or not there is something else doing mischief up stream we can't tell. On the other the ISP is Starlink. If they were purposefully blocking UDP or Wireguard I'd expect to have seen an outcry on reddit/other forums by now.@sindy As I said, we can't rule out ISP interference though I have a feeling that this is not related to the ISP purposefully or by accident filtering out UDP connections on certain ports. It might however be related to the changing of dynamic IP addresses when it happens in a certain way or time. For example with a DHCP NAK. Then the server leaves the wireguard connection up, the client drops it, tries to reconnect but the handshake fails.@td32 Are you saying that disabling and re enabling the interface on the responder ("server side" router) fixes it? If you are, that's not our experience at all... Only changing the port on the connecting (remote) peer resolves it for us.edit: typos ---

## Response 34
@td32 Are you saying that disabling and re enabling the interface on the responder ("server side" router) fixes it? If you are, that's not our experience at all... Only changing the port on the connecting (remote) peer resolves it for us.What happens if you disable wireguard completely on the responder, wait, then re-enable it a moment later? ---

## Response 35
What happens if you disable wireguard completely on the responder, wait, then re-enable it a moment later?Nothing. All the stats get set to zero: current endpoint address and port, rx and tx. Last handshake disappears from print detail in the terminal and in winbox it freezes at the last value when you disabled the interface. ---

## Response 36
Ok. This is kinda weird, since I have several Wireguard tunnels working. So, forgive me if this is redundant, but:1) The "server" has a static IP address2) The "server" waits for connections, but do not attempt to make one.3) The "clients" (road warriors?) have dynamic addresses.4) At some point, the connection is interrupted. When this happens, it is necessary to stop the wireguard interface on the server AND change the server port.5) When the connection is interrupted, the server didn't change the IP address at all.Just checking. ---

## Response 37
Paternot:Yeah it is. But great idea to gather precise data:1) Yes, the server has a static public ipv4 address2) Correct.3) Almost all clients have dynamic public ip addresses. Some even go through NAT.4) No, this is NOT the case. It suffices to change the listening port of the CLIENT.5) No, nothing changes server side. All other clients remain connected.Here´s my script:
```
# Remote address to ping. Intename, wireguard interface.:localremote"10.100.1.35";:localintname"wireguard1";:if([/ping $remote count=2interface=$intname]=0)do={:if([/ping $remote count=10interface=$intname]=0)do={:log error"$intname crashed. Resetting.";/interfacewireguardset$intname listen-port=0}}I run this script on the CLIENTS, every 5 minutes after startup.I've been thinking about this some more and here's where I stand:- Client side, thelistening portis the port from whichoutgoingconnections are made.- A hung connection still reads as running but waiting for handshake, server side.- Since a new connection attempt from the client originates fromthe same portand with the same encryption, server says "why are you trying to start a new connection if yours is still online?", the handshake fails, the client lets out a curse, a sigh, starts over and the same thing happens over and over.- As soon as the client connects from adifferent port, the server treats it as a new connection and everything starts working again.

---
```

## Response 38
I've been thinking about this some more and here's where I stand:- Client side, thelistening portis the port from whichoutgoingconnections are made.- A hung connection still reads as running but waiting for handshake, server side.- Since a new connection attempt from the client originates fromthe same portand with the same encryption, server says "why are you trying to start a new connection if yours is still online?", the handshake fails, the client lets out a curse, a sigh, starts over and the same thing happens over and over.- As soon as the client connects from adifferent port, the server treats it as a new connection and everything starts working again.Well, THIS is weird. Because, You see, Wireguard doesn't have the conception of connection. We say "they are connected" when the traffic flows, but it isn't strictly true. There is no handshake, there is no session tracking. There isn't even a session!What Wireguard do is this:https://www.wireguard.com/#cryptokey-routingOf special interest for our case is this part of documentation:"Built-in RoamingThe client configuration contains an initial endpoint of its single peer (the server), so that it knows where to send encrypted data before it has received encrypted data. The server configuration doesn't have any initial endpoints of its peers (the clients). This is because the server discovers the endpoint of its peers by examining from where correctly authenticated data originates. If the server itself changes its own endpoint, and sends data to the clients, the clients will discover the new server endpoint and update the configuration just the same. Both client and server send encrypted data to the most recent IP endpoint for which they authentically decrypted data. Thus, there is full IP roaming on both ends."It shouldn't matter if the client changes address. It would (should) see a small interruption and the the connection (here we go, talking about "connection" again) should just resume. I used Wireguard with dynamic address (me being the dynamic part), and the connection would just keep going. Not sure what the other side was using, but I was using (at the time) one hEX Gr3. RoS 7.14, or 7.15.Several clients have this problem. They use different ISPs? Even clients where the Mikrotik router is the one directly connected to the internet have this behavior? By the way: even clients without CGNat do this? ---

## Response 39
I fully agree with everything you said. And yes, wireguard is a stateless, with udp being the underlying protocol which is connectionless.And in my experience IP roaming works well.It's the originating port (client side) that makes the handshake fail server side. And as I said, not always. I would've thought that there is no correlation whatsoever between the ports and the handshake. I.e. the handshake is entirely based on the private and public keys.So what has the port got to do with the handshake? I'm guessing something to do with Mikrotik's implementation? Something about how the interface works perhaps? Or the way RouterOS keeps track of handshakes and keepalive or something like that? ---

## Response 40
So what has the port got to do with the handshake? I'm guessing something to do with Mikrotik's implementation? Something about how the interface works perhaps? Or the way RouterOS keeps track of handshakes and keepalive or something like that?This is an interesting line of thought.1) Do the peers with Mikrotik router directly exposed to the internet fail?2) If yes, do these peers have a public IP address or are they using NAT/CGNAT?3) Do the peers where the Mikrotik router is behind something else (and using NAT and maybe CGNAT too) fail too? More frequently than the others? Less frequently? About the same?What I'm thinking is: maybe we are facing with tracking table exhaustion? This is a classic when someone is running a torrent behind the NAT, and the table got filled up. It doesn't have to be a torrent client in your case - but the idea is the same.And why would cycling the connection solve this problem?Well, maybe it doesn't solve the problem per se. Maybe it's just the time the router needed to clear enough connections on the table, in order to work again. After You, do You just double click as fast as possible the enable/disable button? Or do You disable, wait a little and enable it again?AND if You are using CGNAT... well, it's a quite hardware intensive task on the ISP side. Make sense that they implemented something to clear "stuck" connections - even if, in this case, they aren't stuck. Could You be dealing with this? Would explain why the problem is so irregular: time has nothing to do with it. Only the type of network usage. ---

## Response 41
wireguard is a stateless, with udp being the underlying protocol which is connectionless.The "connectionless" is the key here. Since UDP is indeed connectionless, the stateful firewalls (and/or NATs) have to emulate the connection state using timers. Which means that retries from either side can keep such a tracked "connection" alive forever if they come often enough.Here, we found out that the issue was the ISP modem which, after restarting its uplink, creates a new tracked connection before it actualy gets the address, and the Wireguard client attempts keep updating this tracked connection so it cannot be created from scratch with the correct reply-dst address once the WAN got one unless you disable the client for long enough time (whose exact value depends on lifetime of a tracked UDP connection in the ISP device) or unless you change the port on the client side.I am 99.9% sure something similar happens in your case.As the exact time when it happens is unpredictable, the only solution I can imagine is to use a firewall rule that would add the peer address to an address list for 3m or so every time a packet arrives from the peer, and a script scheduled for every minute that would disable the peer in the Wireguard configuration until the next run if that address list is empty. ---

## Response 42
had similar issue today, connection works for many days then stopped this morning.tried:1. have tried disable wg peers on both side first, not work.2. connection restored immediately after I kill the connection in firewall (road warrior setup, on server side).(the connection should belongs to wg before ip changed)my setup is similar toviewtopic.php?t=210232both side version is 7.16.2update Jan 16: found another 2 peers in same situation, restored after kill connection in firewall. ---

## Response 43
Version 7.17 fixed this issue:MT.jpg ---