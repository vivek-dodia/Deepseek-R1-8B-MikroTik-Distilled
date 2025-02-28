# Thread Information
Title: Thread-208937
Section: RouterOS
Thread ID: 208937

# Discussion

## Initial Question
Anyone using this version got mDNS working? If YES please tell me how ...I have CCR1009 with 5 vlans that's connected to my CRS326 switch where all my vlans reside either through ethernet or WiFiI want my printer that is AirPrint capable and sitting in vlan100 to be accessed by any apple device siting in vlan20This should be doable with mDNS but in my case the apple devices using vlan20 cannot communicate with the printer.According tonormisconfiguring mDNS is very simpleon my CCR1009 via terminal I issue:/ip/dns set mdns-repeat-ifaces=vlan100, vlan20is there something else thats needs to be configured using mDNS? because this does not work ... my apple devices cannot see the AirPrint capable printer ---

## Response 1
I've done a couple test and seems to work.But since mDNS just provides an IP address, one way it can go wrong is if the firewall blocks the resulting connection.On Mac (and some Linux and Windows with Bonjour installed), you can use:
```
dns-sd-B _ipp._tcpto see any mDNS records for printers (IPP), which help confirm mDNS is arriving.

---
```

## Response 2
Thanks Amm0 ... I have not had any luck so farMy understanding is that mDNS is crucial for facilitating device discovery and communication within local networks without the need for a dedicated DNS server ... but Tik have not explained how that is implemented under RoS ... why introduce a new feature without some form of direction that is not puzzling .... rhetorically stated ... ---

## Response 3
AFAIK, it looks like RouterOS just copies the mDNS UDP packets between the selected interface.It's roughly same approach asviewtopic.php?t=204025&hilit=mdns. Just implemented at a low-level.Basically RouterOS will look for mDNS if configured in /ip/dns, then re-broadcast any mDNS the router gets on ANY of the mDNS interface to ALL of the configuration mDNS interfaces.So it's not some flexible mDNS "router", at this point, it just copies/mirror/repeats everythingbi-directionally. The reason why this get more complex is if you want to define "one-way" repeating (i.e. mDNS flows uni-directionally). Right now, basically, you can create ONE mDNS discovery zone, that "shares" everything between the interfaces configured in /ip/dns. Perhaps more is planned, but I think that's what it does in beta3. ---

## Response 4
In fairness, I did one test of this... between a remote EoIP to my folk house. If enable this 7.16 mDNS repeat in /ip/dns, I can see and control a Roku TV at least. So we'll have to wait for Mikrotik to say more on what it should do... All I can see is what a 15 minute tested showed.The remote EoIP and local network are both just in "LAN" interface-list, so there are no VLAN restrictions. If you restrict VLANs... you have to allow both mDNS for input, and whatever protocol used by the device in forward. That part isn't changed by repeating mDNS, the firewall still has to allow whatever traffic, even multicast.While Apple AirPrintshould work find being "repeated". I'm not sure AirPlayworks if repeated due to DRM concerns - I dunno for sure (since a HomePod already deal with the apple things). So I didn't test AirPlay, but that not working, would not be a surprise. i.e. Apple AirPlay may need a src-nat NAT rule between VLANs (for AirPlay) since the source IP is unicast & I believe it enforces that AirPlay MUST be on same LAN. So repeating the mDNS doesn't help when trying to play music/movie – maybe this has changed. But testing AirPlay with this feature would not be a good "first test". ---

## Response 5
OT: @Amm0, have you connected two remote locations using EoIP with interface added to the Bridge (and eventually VLAN ID), or assigning an Address to EoIP and adding routing rule?MTU? Mangle rules?If you prefer I can be more specific with the question posting inviewtopic.php?t=206322 ---

## Response 6
Correct, in my test case. There RB1100AHx4 that hangs on my LAN that I use for mainly for testing beta/devices from work. I have one EoIP link on that RB1100 that is a /interface/bridge/port on BOTH sides - it bridges my folk's remote LAN bridge (from a cAPac that acts as both the AP and router, with an EoIP tunnel (to RB1100)). On the RB1100, there is a /ip/dhcp-client that pull my folk's LAN IPs on to the RB1100, and one additional port is tagged to same VLAN as EoIP.It seems to allow you set mDNS repeat on the EoIP interface, but unless both sides had that bridged with an /interface/vlan... I'm not sure there be a use case for repeating EoIP directly. Even though there is EoIP involved, it's bridged to a LAN/VLAN on both sides - so it's LAN/VLAN that needs to be included in mDNS repeating.FWIW, While I have no need for printer between these "sites"... I did verify my Mac on my local LAN see my Mom's printer, a 100 miles away, after enabling the *VLAN* associated with the EoIP tunnel in mDNS in /ip/dns... I can printer a web page on my Mom's inkjet. Without repeating mDNS, the printer would not show up as an option in the Print Dialog. After it I pick the HP in the dropdown. ---

## Response 7
With the new mDNS Proxy feature, I should just be able to add the 2 VLAN interfaces I want to broadcast between in IP/DNS and it should work correct? I had communication between my phone and Google Nests work with PIM for ages and for some reason it just stopped working so I want to give mDNS a try ---

## Response 8
My understanding is that mDNS is crucial for facilitating device discovery and communication within local networks without the need for a dedicated DNS server ... but Tik have not explained how that is implemented under RoS ... why introduce a new feature without some form of direction that is not puzzling .... rhetorically stated ...The key to successFor Meusing Tiks mDNS implementation was provided by @victorbayas in thefollowing postThe following Firewall filter rule was all that was needed to get my 2 isolated VLANS to work with my Apple AirPrint capable printer/ip firewall filter add action=accept chain=input comment="Allow mDNS" disabled=no dst-address=224.0.0.251 dst-port=5353 log-prefix=mDNS protocol=udp src-port=5353Thank YOU @victorbayasI did find that mDNS to be very chatty but that is expected ---

## Response 9
A question...Do you think mDNS could work through a Wireguard tunnel?I've been trying since this morning and it doesn't work, I would like to understand if it is a limitation of the wireguard protocol. ---

## Response 10
Wireguard does not support multicast, and mDNS needs multicast... so not possible. The mDNS support in 7.16 is just an "mDNS repeater", so the resulting "repeated" multicast can not be forwarded over WG.And why I've long argued that /ip/dns should act as mDNS/DNS-SD "Discovery Proxy" to deal with mDNS per RFC-8766. Essentially that means that a regular DNS server can resolve multicast mDNS lookups, so RFC-8766 "discovery proxy" support for unicast DNS is what's needed for mDNS across subnet to work over WG, and compliant with Bonjour specs ---

## Response 11
FWIW, in a quick google, tailscale does NOT offer a solution to mDNS over WG either:https://github.com/tailscale/tailscale/issues/1013 ---

## Response 12
Thank you Amm0, you are always a great help.I'll try with another VPN... ---

## Response 13
I'll try with another VPN...Well... the VPN does need to support multicast & that's the limiting factor to repeating mDNS. I don't think L2TP work with new mDNS proxy. So off top of my head, that be GRE+IPSec, EoIP+IPSec and ZeroTier - thatshouldwork with new mDNS repeater. ---

## Response 14
I was thinking about OpenVPN but now I see that the android/iOS app doesn't support TAP tunnel.So off top of my head, that be GRE+IPSec, EoIP+IPSec and ZeroTier - that should work with new mDNS repeater.OK, then I'll try with ZeroTier.Thanks again ---

## Response 15
Do you think mDNS could work through a Wireguard tunnel?Yes you can but it doesn't use the new mDNS repeater function. See this topic.viewtopic.php?t=194842 ---

## Response 16
Do you think mDNS could work through a Wireguard tunnel?Yes you can but it doesn't use the new mDNS repeater function. See this topic.viewtopic.php?t=194842Well... that's true. But still need EoIP to add the multicast to WG – but you're right the EoIP can run over an existing WG tunnel (and skip the IPSec stuff that's built in to EoIP). ---

## Response 17
Yes you can but it doesn't use the new mDNS repeater function. See this topic.viewtopic.php?t=194842Well... that's true. But still need EoIP to add the multicast to WG – but you're right the EoIP can run over an existing WG tunnel (and skip the IPSec stuff that's built in to EoIP).Actually, I wonder, it just might work using the new mDNS repeater if:* Both ends use EoIP over the Wireguard link (with no IPSEC).* End A connects it's EoIP port to the bridge/VLAN of interest.* End B *does not* connect it's EoIP port to a bridge - leave it isolated (actually you might need to put a DCHP client on it or set it's IP statically to have an valid IP address for end A's subnet).* End B uses the new mDNS repeater with the dangling EoIP and a VLAN or Bridge interface as members.Just a thought experiment but it might work. I'll try this experiment myself later when I have some time. ---

## Response 18
Well... that's true. But still need EoIP to add the multicast to WG – but you're right the EoIP can run over an existing WG tunnel (and skip the IPSec stuff that's built in to EoIP).* Both ends use EoIP over the Wireguard link (with no IPSEC).* End A connects it's EoIP port to the bridge/VLAN of interest.* End B *does not* connect it's EoIP port to a bridge - leave it isolated (actually you might need to put a DCHP client on it or set it's IP statically to have an valid IP address for end A's subnet).* End B uses the new mDNS repeater with the dangling EoIP and a VLAN or Bridge interface as members.Just a thought experiment but it might work. I'll try this experiment myself later when I have some time.I guess theoretically that might work, but it gets confusing. If you just keep both side EoIP bridged, use new /ip/dns/mdns-repeat on EoIP (+ local LAN/VLAN) on each router, and apply more simplified bridge filter to DROP anything NOT port 5353 from over the bridged EoIP+WG link. And you could further tweak it to be a more generic "multicast bridge over WireGuard" (using EoIP connecting over the WG IPs and bridged to desired LANs) by changing the filter rules to allow more/all multicast. ---

## Response 19
....I did find that mDNS to be very chatty but that is expectedI have just upgraded my MK to v.7.16, and I'd like to give this new mDNS feature a try.A Jellyfin container running on my linux server is on VLAN 20, ip 172.16.20.25My smart TV is on VLAN 30, ip 172.16.30.50. For the time being, the Smart TV can access media on the Jellyfin server only if I put bothon the same VLAN, but I don't want to do that for several reasons.So, what should I do to make this mDNS works?Thank you ---

## Response 20
In spite of the new mDNS feature, I haven't yet managed to make multicast work between two VLANs, that is, between the jellyfin server and a few clients on another VLAN. ---

## Response 21
Have you opened port 5353? ---

## Response 22
Have you opened port 5353?Yes, I added this rule:
```
/ip firewall filteraddaction=accept chain=input comment="Allow mDNS"disabled=nodst-address=224.0.0.251dst-port=5353log-prefix=mDNS protocol=udp src-port=5353Anyway, I disabled any reject or drop rule on the firewall temporarily. Same problem. It is like the multicast traffic doesn't propagate..maybe

---
```

## Response 23
```
/ip firewall filteraddaction=accept chain=input comment="Allow mDNS"disabled=nodst-address=224.0.0.251dst-port=5353log-prefix=mDNS protocol=udp src-port=5353In my highly restrictive local communication environment I had to add an addition forward rule like following:
```

```
/ip firewall filteraddaction=accept chain=forward comment="FORWARD FromDevices ToDevices"dst-address-list=ToDevicessrc-address-list=FromDevicesIn my case I have 2 address lists [FromDevices ] [ToDevices] these lists populate IP address of hosts that need to communicate with each otherThis rule would be placed just above FORWARD Drop allThat enabled multicast to work for the targeted VLANs and the hosts in question ...

---
```

## Response 24
```
/ip firewall filteraddaction=accept chain=input comment="Allow mDNS"disabled=nodst-address=224.0.0.251dst-port=5353log-prefix=mDNS protocol=udp src-port=5353In my highly restrictive local communication environment I had to add an addition forward rule like following:
```

```
/ip firewall filteraddaction=accept chain=forward comment="FORWARD FromDevices ToDevices"dst-address-list=ToDevicessrc-address-list=FromDevicesIn my case I have 2 address lists [FromDevices ] [ToDevices] these lists populate IP address of hosts that need to communicate with each otherThis rule would be placed just above FORWARD Drop allThat enabled multicast to work for the targeted VLANs and the devices in question ...I had already added a forward rule between the server and the smart TV in different VLANs. Thanks

---
```

## Response 25
It works perfectly for me between two VLANs even without the rule
```
/ip firewall filteraddaction=accept chain=input comment="Allow mDNS"disabled=nodst-address=224.0.0.251dst-port=5353log-prefix=mDNS protocol=udp src-port=5353I just created a forward rule to allow traffic between the two devices.Are you using Windows for testing?If so, temporarily disable the firewall.

---
```

## Response 26
It works perfectly for me between two VLANs even without the rule
```
/ip firewall filteraddaction=accept chain=input comment="Allow mDNS"disabled=nodst-address=224.0.0.251dst-port=5353log-prefix=mDNS protocol=udp src-port=5353I just created a forward rule to allow traffic between the two devices.Are you using Windows for testing?If so, temporarily disable the firewall.Nope. The server in which Jellyfin runs is a linux machine (firewall disabled) and the client is a smartv.

---
```

## Response 27
Nope. The server in which Jellyfin runs is a linux machine (firewall disabled) and the client is a smartv.I am not at all familiar with Jellyfin but in reading some stuff on the web I have hits stating that Jellyfin currently does not support multicasting ...https://features.jellyfin.org/posts/172 ... ew-a-streaI know that mDNS works well for me .... I know that most if not all Linux machines support multicasting but Jellyfin apparently does not but I could be wrong. ---

## Response 28
I am not at all familiar with Jellyfin but in reading some stuff on the web I have hits stating that Jellyfin currently does not support multicasting ...https://features.jellyfin.org/posts/172 ... ew-a-streaI know that mDNS works well for me .... I know that most if not all Linux machines support multicasting but Jellyfin apparently does not but I could be wrong.I don't know. It could.For the record Jellyfin runs a DLNA server. ---

## Response 29
Tested newmdns-repeat-ifacesfeature on ROS DNS using macOS and iOS screen mirroring (AirPlay) and cast from Google Chrome (Google Cast) from isolated VLAN to Android tv box on LAN and it works - discovery and streaming, but had to allow many ports on forward chain from vlan to TV box. ---

## Response 30
With the current implementation of mDNS I have my Sonos Speakers and Apple Airprint Printers all working flawlesslySonos and AirPrint Printer reside on vlan100 --- devices that need access to either one of these reside on vlan20 ...Using the 2 firewall rules mentioned in my posting here .... ---

## Response 31
Nope. The server in which Jellyfin runs is a linux machine (firewall disabled) and the client is a smartv.Ah OK, then why do you use mDNS instead ofPIM-SMfor DLNA/UPnP? ---

## Response 32
Using the 2 firewall rules mentioned in my posting here ....
```
/ip firewall filteraddaction=accept chain=forward comment="FORWARD FromDevices ToDevices"dst-address-list=ToDevicessrc-address-list=FromDevicesThis completely exposes hosts in list, more secure is to allow just needed ports for hosts in list.

---
```

## Response 33
Nope. The server in which Jellyfin runs is a linux machine (firewall disabled) and the client is a smartv.Ah OK, then why do you use mDNS instead ofPIM-SMfor DLNA/UPnP?I gave it a try too. It didn't work. ---

## Response 34
This completely exposes hosts in list, more secure is to allow just needed ports for hosts in list.in my situation I only allowone to onecommunication -nope, local hosts [and/or devices] are completely secure from each other unless permitted, I'm always ready to learn, however ... ---

## Response 35
Not to grave dig but one mistake I made as someone with very little experience with Mikrotik and bought my first device to learn and for 10gig. When I set up VLAN isolation and was blocking traffic between the VLAN's I didn't realize you could block established traffic. (I am coming from opnSense).User talks to IoT = PassIoT responds to User = BlockedChanging the VLAN block rule to only block the "new" connection state fixed my issue. ---

## Response 36
Normally, you should have this filter rule near the top of the forward chain:
```
/ip firewall filteraddaction=accept chain=forward connection-state=established,related,untrackedand for IPv6:
```

```
/ipv6 firewall filteraddaction=accept chain=forward connection-state=established,related,untrackedAnd in case fasttrack is needed:
```

```
/ip firewall filteraddaction=fasttrack-connection chain=forward connection-state=established,related hw-offload=yesaddaction=accept chain=forward connection-state=established,related,untrackedIt's like that in the standarddefconffirewall configuration or the example from the documentationhttps://help.mikrotik.com/docs/spaces/R ... theClients.Thoseacceptrules are placed above the rule that drops traffics. This also improves performance, because most of the normal traffics will be accepted by them and most packets will only need to be processed by a couple of rules.If you apply this, you won't need theconnection-state=newcondition on your drop rules anymore.

---
```

## Response 37
Wireguard does not support multicast, and mDNS needs multicast... so not possible. The mDNS support in 7.16 is just an "mDNS repeater", so the resulting "repeated" multicast can not be forwarded over WG.And why I've long argued that /ip/dns should act as mDNS/DNS-SD "Discovery Proxy" to deal with mDNS per RFC-8766. Essentially that means that a regular DNS server can resolve multicast mDNS lookups, so RFC-8766 "discovery proxy" support for unicast DNS is what's needed for mDNS across subnet to work over WG, and compliant with Bonjour specs@AMMO Did you submit your suggestion to MT for future implementation........ I mean your not inventing anything but reflecting a standard that exists correct??? ---