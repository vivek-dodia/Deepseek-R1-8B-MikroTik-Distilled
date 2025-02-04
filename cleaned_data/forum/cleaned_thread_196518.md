# Thread Information
Title: Thread-196518
Section: RouterOS
Thread ID: 196518

# Discussion

## Initial Question
I have a RB5009 running 7.9. I added a veth interface for a Pihole container. Even without the container running, the veth interface greatly slows internet.My nominal connection speed is 500/500. If I have the veth port disabled, I get about 590 Mbps down and 520 up. As soon as I enable the veth port I get 10-25Mbps down and 450-500 up.Can anyone help me troubleshoot this? Does a veth port run into some hardware offloading thing, but only for the download? ---

## Response 1
Giventhis prior post, I’ll guess that you’ve created a routing error, sending all traffic thru the container.Post the output of “/ip/route/print”. ---

## Response 2
I've got a similar setup (Rb5009 with containers running) and don't experience this. My WAN is inherently slower (100/100Mbps) but I get no apparent performance impact / slowdown on the native-side routing as a result of running the containers.. so yes, sounds like something config related? ---

## Response 3
@fragtion: Are you using the recommended NAT-based network configuration for your containers, or are you doing as the OP is doing and binding the veth straight to the bridge?I've done the latter for justifiable cause, and it can work, but I'm using these "routers" as glorified switches, so they aren't in the routing path for any inter-network traffic. ---

## Response 4
Ah okay. No, I'm using the recommended config of binding veth to a container bridge as a bridge port. The only NAT going on is srcnat/masquerading of traffic outbound from the container. I guess that is probably the key difference here ---

## Response 5
I'm using the 2nd bridge approach as shown by MT and don't experience any slowdown on my device.Also rb5009.Containers: pihole, openspeedtest, and then iperf3 and helloworld by tangent ---

## Response 6
So, I've determined that the issue happens when the veth interface is attached to the bridge with the LAN on it. Creating the veth interface on a new bridge doesn't produce the problem. I have deleted all the NAT rules. Just adding
```
disabled=yesto veth2 makes the problem go away.Full config:https://pastebin.com/8Y8dAuAcEven when veth2 is attached to bridge1, it seems hardware offload is still enabled and active:
```

```
[david@RoutyMcRouterson]>/interface/bridge/settings/printuse-ip-firewall:nouse-ip-firewall-for-vlan:nouse-ip-firewall-for-pppoe:noallow-fast-path:yes
      bridge-fast-path-active:yes
     bridge-fast-path-packets:6980829bridge-fast-path-bytes:4853024583bridge-fast-forward-packets:0bridge-fast-forward-bytes:0Also, when running a speed test the cpu usage generally stays below 10% though one of the cores spikes to about 40% for an instant.Unless I can find a fix I suppose I'll just buy a new power supply and sd card for my Raspberry Pi and run Pihole in that. Let the router route...thanks for help all.

---
```

## Response 7
My nominal connection speed is 500/500. If I have the veth port disabled, I get about 590 Mbps down and 520 up. As soon as I enable the veth port I get 10-25Mbps down and 450-500 up.The asymmetric results is what's a bit odd (e.g. up is rough same with VETH in bridge, only down is slow).... I'd say this seem like a MTU/fragmentation problem, somewhere –but VETH should be using stardard 1500 MTU. But I guess you can check the MTU of the bridge interface both with the VETH enable and not enable...see if it changes.It really should be okay to be put VETH in the main/vlan-filtering=yes bridge. I haven't seen these issue and never used a 2nd bridge for containers (only VLANs). ---

## Response 8
Or try a iperf test using UDP and see what speeds you get with VETH in the bridge? ---

## Response 9
Full config:https://pastebin.com/8Y8dAuAcMany questions:Where's that "/ip/route/print" output I asked for? Your config is too complicated for me to reconstruct the dynamic routing rules from the static commands. Until you post what result you got from all this, my only option is to duplicate your configuration on a local router, and I'm not willing to do that merely to save you some copy-and-paste work.What's all that VRRP stuff doing in there? You haven't said anything about redundant routers. If you do have a legitimate use for VRRP, why are you doing it only for IPv6?Have you tried a reboot between interface/bridge changes? If you don't, you must sometimes wait for the ARP timeout before the configuration re-settles on a new stable state. In the intermediate time, you've got stale information from the prior state interfering with the new configuration.Is the guest VLAN 10 or 15? Pick one.Having never set up PiHole — nor having any desire to do so — realize that I'm asking merely to prod you into double-checking your config when I ask, can you have a DNS server on the routerplusstatic DHCP reservationsplusupstream CloudFlare DoH/DNSplusPiHole? Maybe I'm speaking from ignorance, but this looks contorted at best and non-functional at worst. I don't see how one delegates smoothly to the next. Shouldn't you need them all to be in a strict chain somehow? Shouldn't the CloudFlare DNS configuration be inside PiHole, with the RouterOS DNS delegating to the PiHole, not CloudFlare? ---

## Response 10
Tangent on the pihole stuff, one can run a container or separate device for adguard dns, and at the same time run DOH on the router itself.You may wish some subnets to use one or the other for example.I worked recently on a config where the adguard container on mikrotik was strictly for three subnets going out third party wireguard, whereas the single subnet staying to local internet use the MT DOH server. So that is very possible..However concur if the OP has the usually bloated mess of a config, impossible to troubleshoot. ---

## Response 11
Sorry to necro an old thread. I have been facing the same problem. As soon as I add a VETH interface to my bridge, it tanks my download speeds, even if there is nothing using the interface.
```
/interfacevethaddaddress=10.0.200.200/32gateway=10.0.200.1gateway6=""name=veth1/interfacebridge portaddbridge=bridgeinterface=veth1Just adding those two commands is enough to cause it. There is nothing using the VETH interface or anything. Just it existing on the bridge is enough.

---
```

## Response 12
Try /24 as the veth IP address. It’s currently just /32. ---

## Response 13
It makes no difference. As soon as a VETH of any kind is added to the bridge, the slowdown happens. It is more apparent with Usenet as it open a lot more connections than a regular download. ---

## Response 14
IMHO that's a logical outcome. For many current (e.g. the RB5009 from this topic, RB4011, L009, CCR2xxx) and old (like the hEX/hEX S) MikroTik devices, the switch chip is capable of hardware offloading many bridge features:https://help.mikrotik.com/docs/display/ ... OffloadingAnd that's the reason why it's recommended to only create one bridge per switch chip to take advantage of the features and so that switching between the ports of the bridge can be done by the hardware at wire speed. Now when you add a software-based interface/port to that bridge, you break the 1:1 mapping between switch chip & bridge. The switch chip cannot handle the foreign port so features that previously was hardware offloaded now need the main CPU to be involved. Frames might also need to go outside of the switch chip and use the link between the switch chip and the main CPU. ---

## Response 15
Is there an alternative way to use containers without resorting to a second bridge? I mean, it "works" but a single bridge is very much the correct way as far as I know, and it's how my router is configured ---

## Response 16
Is there an alternative way to use containers without resorting to a second bridge?Yes. ---

## Response 17
Is there an alternative way to use containers without resorting to a second bridge?Yes.That's the problem I'm facing though. If I add the veth to my single bridge, it completely tanks my download speeds, although speed tests are at full speed for some reason. It doesn't even have to be be attached to a container. ---

## Response 18
I'll try the NAT way and compare speeds. ---

## Response 19
If I add the veth to my single bridge, it completely tanks my download speeds, although speed tests are at full speed for some reason.That doesn't happen here, but then, you haven't told us how you're determining this slowdown in a repeatable manner. You can tell us it's repeatable where you are, but a far better way to get help is to give us a test that's repeatable by everyone you would have help you with this.On a flyer, I shut down the iperf3 container on my gateway router and removed the veth it was using, and I see no difference in performance.Give me a reliably repeatable test. ---

## Response 20
How if first noticed it was download via newsgroups. downloading a 1Gb test file in sabNZBd without the VETH I can download at 13Mbps, as soon as I add the VETH, it peaks at 6Mbps and then drops to 2Mbps.
```
/interface/vethaddaddress=192.168.88.2/24gateway=192.168.88.1name=veth1/interfacebridge portaddbridge=bridge1interface=veth1Happens 100% of the time. Could it be because sabNZBd open 40 connections to the Usenet server at once?

---
```

## Response 21
I doubt there are many people in a position to "download from newsgroups" for you as a test, and even if there was one willing and able, that's not what I'd call a repeatable test. Which file, which group, which platform…?Here's what a repeatable test looks like: go tothis pageand download the 1.4 GB firmware file.(I am confident that Samsung will happily donate us some bandwidth for this test.)It came down here at as close to full line rate as I could ask for, both with and without the veth. Here's the bitrate graph proving it:cu8000-fw-dl-test.pngIf you can tell me which router configuration was operative at each point just from looking at the graph, you get a prize. ---

## Response 22
That's what I don't understand. When I have a VETH on my bridge, regular HTTP downloads, and speed tests are not affected, but Usenet 100% is, and I can reproduced it 100% of the time. The only difference is that sabNZBd opens 40 (or whatever the client is set to) connections to the Usenet server as opposed to a single one for HTTP. sabNZBd has a built in test file to download and that is what I am testing with, but I can grab any file and the result is the same.I have tested with sabNZBd running in Docker on my Unraid server and a desktop client Running a desktop client seems to work fine. My desktop and the Unraid server are on different VLANs.I can't work out what would cause adding a VETH to affect just the Unraid box, but I can see it happen in realtime just be enabling and disabling the VETH bridge port in Winbox.**EDIT** Reducing the number of connections to 1 does not help. ---

## Response 23
https://www.reddit.com/r/mikrotik/comme ... _internet/Seens like others have had a similar problem ---

## Response 24
.....It is OP over at reddit ---

## Response 25
Regardless, I can't work out why it would affect a single Docker container running on a single Unraid server on a completely different subnet, just by adding a VETH interface to the bridge. There's no CPU usage spikes on the router, or the server. All my bridge ports are still marked as Hardware offloaded.There has to be some strange interaction between the two, otherwise I would see the same problem when I run the client on a different PC. There's nothing out of the ordinary going on on the server or it's Docker setup, it's just a regular docker container running on the regular Unraid docker bridge. I've even download the Samsung firmware file using jDownloader in another docker container, running on the same Docker bridge and the speed is fine. ---

## Response 26
otherwise I would see the same problem when I run the client on a different PCThat's a detail you should have led with, not needed to have dragged out after days worth of back-and-forth. This thread's initial post implies that it affects all hosts on the network, and then you come along and claim you have "the same problem," only now we learn it affects this Usenet downloader container alone, not any other machines on the network. Have I got that straight, finally?If so, then by any chance is this container speaking across a WiFi link? Ihaveseen desperately slow bridged networking over WiFi before, but it was with Parallels VMs; the symptom goes away when you switch to "shared" mode, a variety of NAT that causes the VM to share the host's IP on the outside. It's adocumented issue, but when you go read it, please ignore the claim in the article that it's a Cisco-specific problem; I've also seen it on an 802.11ax Amplifi and on my hAP ax³.I believe the mechanism of action has to do with the point-to-point nature of WiFi, where the default assumption is that the client has a single wireless MAC that it will use over a given connection to the AP. When a second one appears, the AP gets confused, causing the slowdown.You can tell that this is what you're running into when the slowdown goes away after switching to a wired connection. In contrast with WiFi APs, Ethernet switches have no trouble with multiple client MACs appearing on a single port since they've got an FDB that is able to learn thousands of MACs per port, since it might be connected to an unknown fan-out of other network switches. Not only is there no need for an FDB with WiFi since all clients connect directly, I believe the client MAC is part of the encryption scheme, which affects how (or whether!) reply packets get back to the client.I suspect one can solve this by playing about withWDS, but I can't be bothered. I either switch the VM to shared networking while on WiFi, or plug the wired Ethernet adapter in when on a laptop that normally runs on WiFi.I've added awarning about this potential pitfallto the end of my article. ---

## Response 27
No WiFi. It's connected via the 2.5Gb ethernet port. ---

## Response 28
No WiFi. It's connected via the 2.5Gb ethernet port.Then I'm stuck.If the problem is as simple as you claim, why do I get 7 Gbit/sec tomy iperf3 containerwhen bridged to an RB4011? ---

## Response 29
That is the root of my problem. It shouldn't do what it is doing. I don't understand how only one container can be affected, but I've pretty much ruled out the Rb5009 at this point. I've it was something like losing HW Offload or something like that I would expect to see a CPU usage spike or something. I've posted in the Unraid and sanNZBd forums as well to see if the can shine some light on the matter. I've resorted to running my old Adguard container on my Unraid box and just directing clients to that.I appreciate the help though. I'm still new to the Mikrotik way of doing things, but I've got 99% of my setup done with help from the forums. ---

## Response 30
Just to follow up. I created a new VLAN just for docker containers and setup Unraid to use it for my docker containers and the speed problem has now gone. As soon as I move the containers back to the Unraid bridge network, the slowdown happens again. A strange interaction, and I still fail to see how it happens by adding a VETH interface to a bridge and subnet that Unraid isn't even a part of, and why only one container was affected, but for what it's worth, if anyone else find this thread......move your docker containers to their own VLAN ---

## Response 31
I'm having the same issue. Adding the veth to the lan bridge result in slow download speed.veth1 in container-bridge:Speedtest by OoklaServer: Digi (RCS & RDS) - Bucharest (id: 11494)ISP: Digi RomaniaIdle Latency: 1.05 ms (jitter: 0.55ms, low: 0.84ms, high: 2.16ms)Download: 863.38 Mbps (data used: 991.2 MB)4.99 ms (jitter: 0.97ms, low: 1.45ms, high: 9.30ms)Upload: 824.42 Mbps (data used: 1.1 GB)6.78 ms (jitter: 3.59ms, low: 3.67ms, high: 221.59ms)Packet Loss: 0.0%veth1 in lan-bridgeSpeedtest by OoklaServer: Digi (RCS & RDS) - Bucharest (id: 11494)ISP: Digi RomaniaIdle Latency: 1.26 ms (jitter: 1.09ms, low: 0.95ms, high: 3.73ms)Download: 52.67 Mbps (data used: 35.7 MB)1.63 ms (jitter: 0.55ms, low: 0.93ms, high: 3.86ms)Upload: 859.81 Mbps (data used: 537.5 MB)6.60 ms (jitter: 1.27ms, low: 3.48ms, high: 9.86ms)Packet Loss: 0.0% ---

## Response 32
Couple questions...1. Is the LAN bridge using auto-mac=no? – if it's =yes, then it's possible VETH become the "first interface" in the bridge, in which case it changes the bridge MAC address to be VETH, which may have some side-effects & using a admin-mac= is generally a best practice2. Is the LAN bridge's "actual MTU" 1500? — guessing it is, and while VETH should adjust its MTU... but the fact you have only a slow download, but same upload, suggests fragmentation. ---

## Response 33
Never bridge VETH interfaces with physical ports, it will disable hardware forwarding. ---

## Response 34
Never bridge VETH interfaces with physical ports, it will disable hardware forwarding."Never" is overly strong, but because it's a consideration worth taking into account, I've added it to thelist of consequencesat the end of the article where I recommend this practice. It already had the auto-MAC issue @Amm0 brought up, plus a third involving a bad interaction between multiple MACs and WiFi's point-to-point nature.I'm still not moving all my containers back to dedicated software bridges, but yes, it is a thing to be done only after due consideration. ---

## Response 35
Never bridge VETH interfaces with physical ports, it will disable hardware forwarding."Never" is overly strong, but because it's a consideration worth taking into account, I've added it to thelist of consequencesThe loss of HW forwarding is a good point, and a valid consideration. With @tangent that "never" is overly strong, i.e. if most traffic is to/from internet, HW forwarding may not be as important.While I'm not sure the various "same problem" posts are actually the same problem... The common thread does seem to beonedirection isdramaticallyslower. And I'm not sure losing HW offloading is going cause a 10x difference in an upload or download - especially on something like RB5009.Since we troubleshooting with some screenshot speed tests, from the looks of them (and that it uses TCP) my first guess be some "MTU problem"... Whether that it, IDK - but from limit data that kinda dramatic difference in TCP traffic is sometimes of symptom of MTU mismatch. And if so, whether a configuration issue, or perhaps container not responding to PMTUD, again unknowns...So is these speedtest are going over a WAN, and WAN has a lower MTU (i.e. some PPPoE providers) that be good to know here. Running a ping test of MTU inside the container might be something to try if so. ---