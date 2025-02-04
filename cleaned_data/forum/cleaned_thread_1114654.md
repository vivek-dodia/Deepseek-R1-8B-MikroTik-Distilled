# Thread Information
Title: Thread-1114654
Section: RouterOS
Thread ID: 1114654

# Discussion

## Initial Question
Hi.Is there a way to set up romon over 1 mikrotik that is vpn server and others that are vpn clients? ---

## Response 1
RoMON works over Layer 2 but you can connect to a router via Layer3 over a VPN and use RoMON to access the routers behind a VPN gateway that are reachable via RoMON.ZeroTier or L2TP are good choice if you also want to be able to connect via RoMON at L2 over a VPN. ---

## Response 2
i need specific vpn or i can also with sstp? ---

## Response 3
For L3 access (connect via IPv4/IPv6)to a MIkroTik router that can reach RoMON enabled devices behind itAny VPN will workFor L2 access (Connect via MAC address)to a MikroTik router that can reach RoMON enabled devices behind itL2TP, EoIP or ZeroTier will work. ---

## Response 4
i have sstp connected to another mikrotik .now what i need to do? maybe with routes? to have access via romon?sorry for question ---

## Response 5
Enable RoMON on the VPN router
```
tool/romon/setenabled=yesThen use the same command to enable RoMON on any router connected to the VPN router or reachable to the VPN mikrotik via routing.Watching the MikroTik official video on RoMON will help:https://www.youtube.com/watch?v=Peg6UcSJ_eA

---
```

## Response 6
i d id that i also have enebled on vpn server-client romon but i cant see each other. i can ping each other rom terminal i set also routes i am done rom these ... i dont know why dont see via romon ---

## Response 7
Do you have a drawing of your network? ---

## Response 8
router A (vpn server office ) :192.168.71.0/24 (vpn range)router B (vpn client home) :192.168.71.3 (vpn ip)on neigbors i can see the vpn client but only with ip not mac adress as said on video ... ---

## Response 9
do you know if the problem is cause one router has 6.48 and other 7.7? ---

## Response 10
You cannot connect via MAC address over SSTP as it is a Layer3 VPNYou need to use what is called a Layer 2 overlay - examples are: L2TP, EoIP or ZeroTier. Then you will be able to connect via MAC between those locations. ---

## Response 11
i dont want mac adress .. i want just to connect with romon ... need any other settings to do that please>? ---

## Response 12
Where is the device you want to connect to with RoMON - on the home network or work network?How is it connected to the VPN client or server? ---

## Response 13
i need specific vpn or i can also with sstp?Yes you can.But going to a remote RouterOS over routed IP with WinBox, and use that remote ROS as RoMon bridgehead to see the rest via RoMon is easy. As already suggested here.If you want to have L2 access to the remote site, use BCP over that SSTP VPN.The wiki only gives the PPTP exemple, but SSTP is also BCP capable.https://wiki.mikrotik.com/wiki/Manual:B ... _bridging)With BCP you have a local bridge and a remote bridge that is L2 connected. Creating an extra bridge for this L2 access can make it easier to manage. It also avoids the need for EoIP or MPLS/VPLS tunnels inside the SSTP tunnel. ---

## Response 14
i need romon on the router of home networkvpn server is on my work . and client is home .. at this time i am in my work .these 2 routers are connected over sstp . and has routes to access all the network of each other. ---

## Response 15
i dont want mac adress .. i want just to connect with romonAFAIK RoMon is L2 (MAC) only. ---

## Response 16
i need romon on the router of home networkFrom work, connect with WinBox by using "Connect to RoMon" with the home router IP as selected device. In that RoMon/Winbox session select from "RoMon Neighbors" tab. Use "Connect"L2/MAC is only home, Home-Work is L3 IP. ---

## Response 17
i connect with ip on romon but i didnt see anything :S ---

## Response 18
lets take it from start.Router A office VPN SERVERRouter B home VPN CLIENTlaptop VPN CLIENThow from my laptop access HOME router over romon of OFFICE router that i connected with vpn from my laptop ---

## Response 19
Laptop WinBox connects to Router B Home with "Connect to RoMON"Klembord-3.jpgThat session opens, and then select the TAB "RoMON Neighbors"If RoMON is configured on the HOME devices , see (if no Firewall is blocking, RoMON is enabled with same secret, and devices are on the same L2 network,) and select the Router you want WinBox to be connected to.Klembord-2.jpgTrying with a good IP address at HOME will fail with:Klembord-4.jpg. RoMON is not via IP. ---

## Response 20
i dont want mac adress .. i want just to connect with romon ... need any other settings to do that please>?vpn server is on my work . and client is home .. at this time i am in my work .these 2 routers are connected over sstp . and has routes to access all the network of each other.Why would you use RoMON , if you have routes to access all the network. ???????Confused between WinBox and RoMON ??? Access with just WinBox via IP address , if there are IP routes and the needed FW rules to allow that traffic (TCP port 8291) ---

## Response 21
i did this and nothing happens..from my laptop i connected on office via vpn .from home connected on office via vpnfrom laptop connect romon on office router ipbut office ---> home is also remote so l3 and no l2 this is that i want to fix and acess ---

## Response 22
i dont want mac adress .. i want just to connect with romon ... need any other settings to do that please>?vpn server is on my work . and client is home .. at this time i am in my work .these 2 routers are connected over sstp . and has routes to access all the network of each other.Why would you use RoMON , if you have routes to access all the network. ???????Confused between WinBox and RoMON ??? Access with just WinBox via IP address , if there are IP routes and the needed FW rules to allow that traffic (TCP port 8291)because i have different sites with central routers and i want to connect to central router and have romon the others of the specific network ---

## Response 23
Make sure you can ping home router from your laptop. (IP routes must be OK in laptop, Office router, Home router, or OFFICE router could use NAT)Then use WinBox to access Home Router. If you can Ping but not WinBox, check firewall rules on OFFICE and HOME router.RoMON is not usable for these L3 connections, and not needed. ---

## Response 24
i can ping all from all and winbox all from all but not romon ... ---

## Response 25
What does RoMON do more than what Winbox can???????Add/Set your WinBox sessions, and have a list with all your routers including credentials (better view with WinBox Tools in "Advanced Mode".)RoMON is only a WinBox session forwarder via L2 broadcasts/multicasts, not using IP (L3). ---

## Response 26
ok ok but why i cant connect with romon ?? is there an answer? ---

## Response 27
i can ping all from all and winbox all from all but not romon ...It sounds like maybe you don't understand why RoMON exists and what it's used for.RoMON was added to RouterOS in 2015 to make it easier to manage routers using L2 only. Previously if you had a routing issue and needed to mac telnet to a router several hops away, you would need to login to each router in the path and mac-telnet to the next router until you reached the router with an issue.This was very time consuming and so MikroTik created RoMON which allows you to access a router several hops away even if routing is not configured or has been mis-configured.Since then, RoMON has become a very popular management tool for everyday use, however, it's not required when all routers are reachable via routing and the goal is simply to use winbox. ---

## Response 28
A romon connection is between 2 routers that have RoMON enabled and communicate over a L2 connection.WinBOX can connect toRoMON Agentof one of those routers via IP or L2 (MAC) , because it is the same connection as the regular WinBox connection on port TCP/8291.If you can connect with WinBox, you can connect to the RoMON Agent if RoMON is activated, and you use the correct RoMON Secret. Also via MAC if allowed on that interface (Tools/MAC Server/MAC Winbox Server). Connectable WinBox ports should appear in IP/Neighbors, also over a SSTP VPN. If not connectable via L2/MAC then MAC will be all zero's.Klembord-2.jpg ---

## Response 29
btw thanks for all . i am sorry . ---

## Response 30
Wow. Lots of highly technical responses, but no one actually gave him the answer. Hopefully he reads this:First, to those who ask "why you want ROMON when you've got a direct VPN to the other network?" This is the old why did the chicken cross the road question. To get to the other network. In this case, the other network would be ones you have no routes to. It is also a great way to reset things like static addresses/routes on devices that are not directly reachable. Turn on ROMON, connect using it, then mess with IP addresses on the device without fear of losing access.I was not always a fan of ROMON, especially since I have LOTS of VLANS in my networks and ROMON is layer 2. But one of my customers relies on it 100% for supporting his network and I've gotten used to it. There are a number of issues like winbox failing to reconnect if you reboot the remote router and changing your connection address to the mac address so you have to re-enter the address of the ROMON server, but these are things we live with.So to start...as correctly pointed out ROMON uses layer 2 not layer 3. So to ROMON, your connection is by MAC address, with the connected routers forwarding packets until it gets to your destination and then back. You don't care about your MAC address, but ROMON does.ROMON works very well over VPNs that are layer 2 based, such as L2TP. Everything just works. But SSTP is layer 3, so this fails. But there is a VERY EASY FIX. Simply create an ethernet over IP tunnel (one of Miktrotik's greatest features!) between the two IP addresses used for the SSTP tunnel.For example, if your router that is the SSTP server has a local address on the SSTP interface of 10.9.8.1 and the SSTP client is being given 10.9.8.2, just create an EOIP interface on the router with a local address of 10.9.8.1 and a remote address of 10.9.8.2 and give it a unique tunnel ID. I tend to use the last two octets of the IP address for mine, so in this case I'd use 82. On the client side, the EOIP interface would have a local address of 10.9.8.2 and a remote address of 10.9.8.1 with the same tunnel ID.Of course this solution ONLY works if your SSTP connection is being assigned the same IP address each time and is not grabbing one from a pool.It is also VERY IMPORTANT to remember to set the MTU to 1500 on both EOIP interfaces. I've seen issues with ROMON connections hopping across several networks if an MTU somewhere gets wonky. There won't be much fragmentation, but if there is it won't hurt us. All the rest of the options can just be the default values.So five minutes and you're done. BUT...This will increase traffic slightly over the VPN as it randomly broadcasts the ROMON identification packets. If you have a lot of devices using ROMON, you may want to segment them by using different secrets. You can then limit what is sent/listened to over a VPN by adding the interface to the "ports" list in tools/romon and limiting it to the secrets you want to pass. The documentation is pretty good on this, but it does expect you understand what layer 2 and layer 3 are, which is not something everyone wants to learn.I have about 20 of the 400+ Mikrotiks I manage using ROMON, so my VPN traffic here is not affected horribly. But long lists are also difficult to keep organized, so naming your devices in a manner that tells you what/where they are is a good idea.Hopefully this answer was not too technical and helps with your issue. ---

## Response 31
I think the simple way to explain it is that we assume you're using winbox, behind a L3 VPN (e.g. SSTP here)... you use the IP address but still use "connect to RoMON". After connection, the Layer2 RoMON neighbors are visible in winbox. You the pick one of those to use. As long as the first router you used for the "Connect to RoMON" has RoMON enabled and Layer2 to the other routers, it will proxy the winbox protocol data back your winbox behind SSTP.If you use a Layer2 VPN (ZeroTier, L2TP, or EoIP/GRE, etc), the only difference is you can use MAC address with the first "Connect to RoMON". But that's not needed, since it's router your connected that will do the Layer2 via RoMON, and then proxy that back... so Layer2 all the back your winbox isn't needed, it's already being proxied by the router you used in "Connect to RoMON".e.g. You still connect some router on the RoMON network using winbox using the "Connect to RoMON", and it's the connected router that presents it's view of the RoMON "neighbors". Whether you access the first router via IP or MAC, it still return the same list of RoMON routers. ---

## Response 32
But very good point: 100% right, RoMON does not like MTU below 1500. ---

## Response 33
I tend to connect directly from winbox, but I keep ROMON for "emergencies" and for things like what I'm working on today, where I'm duplicating a production network into a test network to work on MSTP. We've got 6 10Gb fiber connections for about 35 VLANS and we're adding a 10Gb radio and a second pair of MSTP switches (317s) so we will have multiple failover paths in the event that someone takes out the pier to the ship or rats eat the fiber (again). I also hate losing the entire ship for a minute or more multiple times when we update RouterOS. And unfortunately, there have been a LOT of fixes to MSTP recently.Of course creating a duplicate test network (after waiting nearly a month for a half dozen 317s and some 326/328s to arrive!) requires starting with a blank device and using import/export, but I'm working 30 miles and 5 VPN hops away. Turn on ROMON, export/import, and away we go!So yes, as you mentioned and hopefully the person who asked the original question realizes, you connect to a reachable Mikrotik using connect to ROMON and go from there. ---

## Response 34
Yeah it's two-step dance in using it ... and a bit convoluted in winbox's UI. But RoMON gets a bad wrap.I'd perfer to use ZeroTier for out-of-band management. But RoMON helps a bunch... since there is no ZeroTier on MIPSx devicesSo as long as there is some ARM router with ZeroTier-enabled & RoMON enabled, I have that as a backup path. While less than ideal, RoMON works pretty well IMO. ---

## Response 35
... you connect to a reachable Mikrotik using connect to ROMON and go from there.This.Connect using direct, VPN, EOIP, Zerotier, EOIP over WG (), ... whatever.And the whole Mikrotik L2 network will unfold using ROMON. ---

## Response 36
I have not tried zero tier on Mikrotiks. Most of my routers are tile. Lots of arm in the field, mostly 3011/4011, but everything else is a 1009, 1036 or 1072. And I have just put my original 1200 back in service. I bought it/them when they were released. Must be a dozen years old. Pulled six of them off the shelf and three still worked. Emptying the bottom shelves in the NOC to build the test network. Even put a pair of 2011s up.Rule 1: never throw out obsolete Mikrotiks! ---

## Response 37
I would like to setup RoMON between two Mikrotik on two sites as emergency path.The two sites are linked with some L3 "tunnels" and also ZeroTier, i.e. both have an interface on the same ZT network.Simply enabling RoMON on all interfaces via settings seems not enough: discovery doens't find anything.Something else is needed?What to check? ---

## Response 38
ForZeroTier with RoMON, you need to modify the flow rules to allow it on at my.zerotier.com. RoMON uses a non-standard ether-type at Layer 2, so this needs to be allowed in the "Flow Rules" for the ZT network. Specifically adding the following at very TOP of the rules (before the drop rules):
```
## Allow RoMON.#accept
	ethertype0x88bf;

---
```

## Response 39
The above rule is needed for ZeroTier + RoMON.But I recently wrote up steps forEoIP + IPSec with RoMONhere – since not all routers support ZeroTier:viewtopic.php?t=206322 ---

## Response 40
What if you wanted to do EoIP on top of wireguard and add RoMON? ---

## Response 41
What if you wanted to do EoIP on top of wireguard and add RoMON?Ask and answered below. SoEoIP + WG with RoMONis discussed here:viewtopic.php?t=203137&hilit=romon+wg#p1046880 ---

## Response 42
ForZeroTier with RoMON, you need to modify the flow rules to allow it on at my.zerotier.com. RoMON uses a non-standard ether-type at Layer 2, so this needs to be allowed in the "Flow Rules" for the ZT network. Specifically adding the following at very TOP of the rules (before the drop rules):
```
## Allow RoMON.#accept
	ethertype0x88bf;Does this still work?   I've tested this today, and romon doesn't seem to work between 2 tiks with ZT between them.   both same subnet, both can ping each other fine as well, but when I do a pcap on both tiks, I see ethertype 0x88bf, but it does not reference the DST-MAC 01:80:c2:00:88:bf.   (I do see this mac on romon interfaces that are NOT ZT though)

---
```