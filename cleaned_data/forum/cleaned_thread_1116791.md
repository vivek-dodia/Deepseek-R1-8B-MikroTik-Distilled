# Thread Information
Title: Thread-1116791
Section: RouterOS
Thread ID: 1116791

# Discussion

## Initial Question
I have a Routerboard Hex and just purchased a SXT LTE6 as backup internet feed.The Routerboard is set as Router and is connected in its Internet Port to a Starlink device. One Ethernet port is connected to a large Giga switch, which links a large network together, including (via microwave links) to a remote site.At this remote site I have installed the new SXT LTE6, connected to the cellular network.This is intended as a failover backup. What I want may not be possible, but:Is there any way I can program the Routerboard to start using the SXT LTE6 for Internet if the Starlink fails?I have seen the various failover scripts(?) but it is not clear to me how I can force the Routerboard router NOT to use its 'Internet' Port, but instead to use an IP address on the local LAN (via a single Ethernet port connected to the main Switch).An additional question: The SXT LTE6 is set up as a Bridge. But it still has an external 'Internet' IP address with a box called "Firewall Router". Is this some unique new system to mix a Bridge with a Router? ---

## Response 1
Well I suspect you will need to setup vlans, as the connection to the remote site ( the backup internet part ) will have to come on the same port and on a vlan to be terminated as a WAN connection on the HEX., ---

## Response 2
I see what you mean, that would be the start.You being a 'guru' can you give me advise how I could set this up on the Routerboard (v6.49.17) ? ---

## Response 3
I would probably upgrade to 7.16.2 but its not absolutely necessary.However doing so would allow you to remotely reach via BTH wireguard VPN, both the router and the LXT for configuration/troubleshooting issues.This is the bible on vlans....viewtopic.php?t=143620 ---

## Response 4
There are few ways to design this....But, if you want something basic without VLANs or "passthrough".... I don't see harm in leaving the hEX as is, and then put the SXT on the hEX LAN.i.e. assuming all have default configuration, the most basic failover be to:- set the ip address of SXT to 192.168.88.2- setup SXT as bridge: i.e. disabled dhcp-server, add ether1 to bridge ports, remove ether1 from WAN in /interface/list,- make sure LTE is in WAN in /interface/list and NAT masquerade rule exists for WAN (or lte1 directly)- then....connect to the SXT to a LAN port on hEX- on hEX, then you add a route to the SXT with a higher distance=, so "/ip/route add gateway=192.168.88.2 distance=2"That's IMO most basic way to start. And it will failover if you physically unplug the starlink with just the above. But it will not catch other network failures. Now above let you test something, then move on to actually do better failover detection once the basic plumbing is working, which get to be more involved depending on needs.Presumable your starlink is using DHCP client to get its address & using a public IP. In which case, you can add a "check-gateway=ping" to default route to starlink, which at least ping the earthstation to "test starlink is up". To do this, you can add a script to the /ip/dhcp-client for starlink on hEX
```
:if($bound=1)do={/ip routeset[/ip route find gateway=$"gateway-address"]check-gateway=ping}Finally, you could also perhaps use the SXT as a backup router using VRRP for your LAN – which means if SXT and HEX both were connect to LAN switch, then EITHER could provide routing for LAN even if one route hardware failed/powered-off/rebooted.  But this could always be added later too.

---
```

## Response 5
Thanks for all that, I will work my way through the VLAN issue first.Re the version: v6.49.17 was the latest update it just did, automatically.I am not sure if the hardware allows for a even later version, if I find a way to download it.I am scared to brick the unit.... ---

## Response 6
Amm0: Your post crossed mine I think; I will try your idea first.Thanks, Bart ---

## Response 7
hEX RB750Gr3 has enough RAM to run ROS 7, but maybe yours is actually one of the older RB750 versions? 64 MB of RAM is the minimum required.In any case, to upgrade to ROS 7 from ROS 6, you have to set the update channel toupgradebefore/system package update install. If successful, the first upgrade will take you to 7.12.* and set the update channel back tostable; you have to run/system packege update installagain to get to the latest stable 7.* (at the time of writing, 7.16.2).Regarding @Amm0's suggestion to connect the SXT to the LAN of the hEX - just bear in mind that under the hood it is not as simple as it seems. If a router (the hEX in your scenario) finds out that the in-interface and the out-interface are the same for a packet, it informs the sender of that packet, by means of an ICMP message, that a better route is available in the same network. So when your PC initiates a TCP connection towww.some.site, it sends its SYN packet to the hEX, which forwards it to the destination via the SXT but also tells the PC to send the subsequent packets for the address ofwww.some.siteto the hEX directly. Leaving aside all the firewall and NAT issues related to this, since they are irrelevant in this particular setup, some devices may not handle this properly. The probability that their connections fail is quite low as if the sender merely ignores the ICMP notification about availability of a better router, the hEX will keep forwarding the packets via SXT, i.e. the device has to misunderstand the notifications in a creative way to break its routing, but if some devices work OK when the Starlink connection is available and fail when it is not, this is the direction to dig in. Use of VRRP eliminates this as it makes the PC in the example above send already the first SYN packet to the SXT.Whatever the WAN failover scenario where NAT is involved:TCP connections fail at each WAN change, but new ones can be established without problems (depending on the particular application, some have to be re-established manually, though).UDP connections that get periodically refreshed (like SIP registrations, IPsec or Wireguard sessions) usually need specific treatment after a WAN change if they keep passing through a device that did the NAT for one WAN even while routed via the other WAN. So this will become interesting if you eventually choose the VLAN approach where the hEX will use a dedicated VLAN to send the traffic to internet via the SXT. ---

## Response 8
All true @sindy. I do normally use VRRP on the LANs, so forgot the ICMP would further delay "fail-back". My generalized worry is always over-engineering failover so that itself produces outages, like here starlink should be pretty reliable, so failover should be pretty rare... So if perhaps "reopening a tab" is needed after failover, that may not be end of world for some failover cases. If more rapid failover/failback is desired, all the approaches do start getting more involved/complex.Since we're talking about a hEX and SXT, neither are especially powerful routers & there is already a switch... So my thought be to use VRRP on LAN, so either SXT or HEX could be the "main" router", with the VRRP priority being on HEX. This has the add benefit if upgrade and/or end with messed up configuration, the other router allows the main LAN to still work. And the defaults on both routers have a firewall, WAN on ether1/lte1... so VRRP largely means change the default LAN IP address from .1 on each router to .2 and .3 & a new VRRP interface with 192.168.88.1. If VLANs are added, then those too need VRRP interface, and separate .2 and .3 IP address on the VLAN interface on each router. ---

## Response 9
@Cindy: It is a RB750 r2. I don't see the available memory. ---

## Response 10
/system resource print ---

## Response 11
@All: I am afraid most of this is going way over my head.I am familiar with basic routing etc; but not with the microtik / Winbox interface.I have changed the SXT to another IP /24 network (192.168.51.254) , Left everything as default (Bridge, radio interface at WAN). NAT is checked.I added an IP Route (Gateway) to it from the Hex, but I get a 'Not available' for the STX Gateway on 192.168.51.254. (It does show on the Winbox on my PC, but I cannot connect to it) ---

## Response 12
@Sindy: I do have 64 mb RAM. In my case, it it worth upgrading to 7.x? Are there major advantages for what I am trying to do? Thanks. ---

## Response 13
Unless you need Wireguard, OpenVPN over UDP, chacha20poly1305 encryption in IPsec, or json serialization/deserialization (or some other one of the many little improvements of the scripting language), I can see no reason to switch to ROS 7. ---

## Response 14
I have a Routerboard Hex and just purchased a SXT LTE6 as backup internet feed.The Routerboard is set as Router and is connected in its Internet Port to a Starlink device. One Ethernet port is connected to a large Giga switch, which links a large network together, including (via microwave links) to a remote site.At this remote site I have installed the new SXT LTE6, connected to the cellular network.This is intended as a failover backup. What I want may not be possible, but:Is there any way I can program the Routerboard to start using the SXT LTE6 for Internet if the Starlink fails?I have seen the various failover scripts(?) but it is not clear to me how I can force the Routerboard router NOT to use its 'Internet' Port, but instead to use an IP address on the local LAN (via a single Ethernet port connected to the main Switch).An additional question: The SXT LTE6 is set up as a Bridge. But it still has an external 'Internet' IP address with a box called "Firewall Router". Is this some unique new system to mix a Bridge with a Router?I have a very similar setup working perfectly.I have a rb5009 with Starlink in bypass mode as WAN1 and then the LHGG LTE6 as secondary backup with LTE Passthrough. I also have recursive routes setup and use Netwatch for the failover along with a script for telegram notifications when WAN1 is down.Starlink script in IP/DHCP Client/Ether1-WAN/Advanced:if ($bound=1) do={/ip route add distance=1 gateway=$"gateway-address" dst-address="192.5.5.241" scope=30 target-scope=31 comment="Starlink"/ip route add distance=3 gateway="192.5.5.241" check-gateway=ping scope=30 target-scope=32 comment="Starlink"} else={/ip route remove [/ip route find comment="Starlink"]}LHGG LTE6 script in IP/DHCP Client/ETHER8-WAN2/Advanced:if ($bound=1) do={/ip route add distance=1 gateway=$"gateway-address" dst-address="8.8.4.4" scope=30 target-scope=10 comment="ISP2"/ip route add distance=4 gateway="8.8.4.4" check-gateway=ping scope=30 target-scope=32 comment="ISP2"} else={/ip route remove [/ip route find comment="ISP2"]}Watch these two videos and follow exactly to set up lte passthrough on your SXT.https://www.youtube.com/watch?v=8cD1cGH0e3Yhttps://www.youtube.com/watch?v=IZFAeLbujsoLet me know if you need any more assistance with recursive routes. ---

## Response 15
@sk0003I managed to get SXT LTE6 "Ether1" into Passthrough Interface mode. I should still be able to reach it via Ether2 for programming.Its default IP address is still 192.168.188.1So how am I suppsed to connect to it? In your Starlink script, that IP address 192.5.5.241, where does that come from? It that the Starlink DHCP supplied address?If so, this could change any time? And the $"gateway-address", is that internally set or do I have to set it?Then, I have tried before to set a Route to the IP address of the SXT which is on another network. This does not work. It cannot reach it.You also seem to have a WAN2. I only have a single WAN. The SXT is on the LAN... Can I still use your system> ---

## Response 16
@sk0003I managed to get SXT LTE6 "Ether1" into Passthrough Interface mode. I should still be able to reach it via Ether2 for programming.Its default IP address is still 192.168.188.1So how am I suppsed to connect to it? In your Starlink script, that IP address 192.5.5.241, where does that come from? It that the Starlink DHCP supplied address?If so, this could change any time? And the $"gateway-address", is that internally set or do I have to set it?Then, I have tried before to set a Route to the IP address of the SXT which is on another network. This does not work. It cannot reach it.You also seem to have a WAN2. I only have a single WAN. The SXT is on the LAN... Can I still use your system>Once you have it in passthrough mode like in the videos, you should be able to see it in Winbox as a neighboring device through your router. You would access it through the management VLAN which was in the video.THe 192.5.5.241 is the IP that is being pinged in my recursive route for the primary. Instead of 8.8.8.8, Google's IP for example.This is what I have in my IP/Routes. You can see the primary is the one with the 192.5.5.241 and the secondary is with 8.8.4.4.
```
adddisabled=nodistance=1dst-address=192.5.5.241/32gateway=192.168.1.1\
    pref-src=""routing-table=main scope=30suppress-hw-offload=no\
    target-scope=31adddisabled=nodistance=1dst-address=8.8.4.4/32gateway=192.168.188.1\
    pref-src=""routing-table=main scope=30suppress-hw-offload=no\
    target-scope=31addcheck-gateway=ping disabled=nodistance=3dst-address=0.0.0.0/0gateway=\192.5.5.241pref-src=""routing-table=main scope=30suppress-hw-offload=\notarget-scope=32addcheck-gateway=ping disabled=nodistance=4dst-address=0.0.0.0/0gateway=\8.8.4.4pref-src=""routing-table=main scope=30suppress-hw-offload=no\
    target-scope=32Then in netwatch the following. It only checks the primary. If down, it auto switches over because of the ip/routes setup above and runs a script to send a message via a telegram bot.
```

```
/tool netwatchadddisabled=nodown-script="/system/script/run DOWN;"host=192.5.5.241\
    http-codes=""interval=1mpacket-count=10packet-interval=1sstart-delay=\3sstartup-delay=2mtest-script=""thr-avg=200mstimeout=3stype=icmp \
    up-s

---
```

## Response 17
@sk0003 and all;I spend 2 days on this, lost my entire system 8 times and had to reset to factory settings, etc.So what I got right now:- In the SXT LTE6 I set up a new Vlan called "net". As per video, I set the LTE in passtrhough to "net". I should not have to do anything else.- In the Hex, I also added the Vlan "net" and I added a Default Route to it with a distance of 3. Route shows as 'net reachable' in blue.I have NOT yet added any scripts; just manually testing.In the Hex, when I try to ping 8.8.8.8 from the Tools/Ping using the Interface "net" it does not work.When I ping 8.8.8.8 from my PC, and I pull the plug on the Starlink, I lose internet. When I plug it back on, it does not come back, and I have to reset my PC Ethernet interface.In all my tests, I have not been able to get from my Hex to the Internet via the SXT. Not when it is in default Bridge mode, and not when it is in Passthrough mode.SXT:/interface/lte/apn> pr# NAME APN ADD-DEFAULT-ROUTE DEFAULT-ROUTE-DISTANCE PASSTHROUGH-INTERFACE0 * default internet yes 2 netHex:/ip route> pr# DST-ADDRESS PREF-SRC GATEWAY DISTANCE0 ADS 0.0.0.0/0 192.168.1.1 11 S 0.0.0.0/0 net 32 ADC 192.168.1.0/24 192.168.1.195 ether1 03 ADC 192.168.50.0/24 192.168.50.254 bridge 04 ADC 192.168.188.0/24 192.168.188.2 net 0Any help welcome... ---

## Response 18
@sk0003 and all;I spend 2 days on this, lost my entire system 8 times and had to reset to factory settings, etc.So what I got right now:- In the SXT LTE6 I set up a new Vlan called "net". As per video, I set the LTE in passtrhough to "net". I should not have to do anything else.- In the Hex, I also added the Vlan "net" and I added a Default Route to it with a distance of 3. Route shows as 'net reachable' in blue.I have NOT yet added any scripts; just manually testing.In the Hex, when I try to ping 8.8.8.8 from the Tools/Ping using the Interface "net" it does not work.When I ping 8.8.8.8 from my PC, and I pull the plug on the Starlink, I lose internet. When I plug it back on, it does not come back, and I have to reset my PC Ethernet interface.In all my tests, I have not been able to get from my Hex to the Internet via the SXT. Not when it is in default Bridge mode, and not when it is in Passthrough mode.SXT:/interface/lte/apn> pr# NAME APN ADD-DEFAULT-ROUTE DEFAULT-ROUTE-DISTANCE PASSTHROUGH-INTERFACE0 * default internet yes 2 netHex:/ip route> pr# DST-ADDRESS PREF-SRC GATEWAY DISTANCE0 ADS 0.0.0.0/0 192.168.1.1 11 S 0.0.0.0/0 net 32 ADC 192.168.1.0/24 192.168.1.195 ether1 03 ADC 192.168.50.0/24 192.168.50.254 bridge 04 ADC 192.168.188.0/24 192.168.188.2 net 0Any help welcome...I am not seeing the “man” VLAN which is the management VLAN. That is how you access the LTE. Have you followed through the video exactly as it says? I will print the configs from mine in a bit. ---

## Response 19
@sk0003 and all;I spend 2 days on this, lost my entire system 8 times and had to reset to factory settings, etc.So what I got right now:- In the SXT LTE6 I set up a new Vlan called "net". As per video, I set the LTE in passtrhough to "net". I should not have to do anything else.- In the Hex, I also added the Vlan "net" and I added a Default Route to it with a distance of 3. Route shows as 'net reachable' in blue.I have NOT yet added any scripts; just manually testing.In the Hex, when I try to ping 8.8.8.8 from the Tools/Ping using the Interface "net" it does not work.When I ping 8.8.8.8 from my PC, and I pull the plug on the Starlink, I lose internet. When I plug it back on, it does not come back, and I have to reset my PC Ethernet interface.In all my tests, I have not been able to get from my Hex to the Internet via the SXT. Not when it is in default Bridge mode, and not when it is in Passthrough mode.SXT:/interface/lte/apn> pr# NAME APN ADD-DEFAULT-ROUTE DEFAULT-ROUTE-DISTANCE PASSTHROUGH-INTERFACE0 * default internet yes 2 netHex:/ip route> pr# DST-ADDRESS PREF-SRC GATEWAY DISTANCE0 ADS 0.0.0.0/0 192.168.1.1 11 S 0.0.0.0/0 net 32 ADC 192.168.1.0/24 192.168.1.195 ether1 03 ADC 192.168.50.0/24 192.168.50.254 bridge 04 ADC 192.168.188.0/24 192.168.188.2 net 0Any help welcome...Here is my LTE config
```
/interfacevlanaddinterface=ether1 name=man vlan-id=2addinterface=ether1 name=net vlan-id=3/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacelte apnaddapn=orange authentication=pap ip-type=ipv4 passthrough-interface=net \
    passthrough-mac=autouse-network-apn=yes user=orange/interfacelteset[finddefault-name=lte1]allow-roaming=yes apn-profiles=orange band=""\
    sms-protocol=autosms-read=no/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTik/ip pooladdname=default-dhcp ranges=192.168.188.10-192.168.188.254/ip dhcp-serveraddaddress-pool=default-dhcp disabled=yesinterface=ether1 lease-time=10m\
    name=defconf/portset0name=serial0/ip firewall connection trackingsetudp-timeout=10s/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacedetect-internetsetdetect-interface-list=WAN/interfacelist memberaddcomment=defconfinterface=ether1 list=LANaddcomment=defconfinterface=lte1 list=WANaddinterface=man list=LAN/ip addressaddaddress=192.168.188.1/24comment=defconf disabled=yesinterface=ether1 \
    network=192.168.188.0/ip dhcp-clientaddinterface=man/ip dhcp-server networkaddaddress=192.168.188.0/24comment=defconf dns-server=192.168.188.1\
    gateway=192.168.188.1/ip dnssetallow-remote-requests=yes/ip dnsstaticaddaddress=192.168.188.1comment=defconf name=router.lan type=A/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip hotspot profileset[finddefault=yes]html-directory=hotspot/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMPv6"protocol=\
    icmpv6addaction=accept chain=input comment="defconf: accept UDP traceroute"port=\33434-33534protocol=udpaddaction=accept chain=input comment=\"defconf: accept DHCPv6-Client prefix delegation."dst-port=546protocol=\
    udp src-address=fe80::/10addaction=accept chain=input comment="defconf: accept IKE"dst-port=500,4500\
    protocol=udpaddaction=accept chain=input comment="defconf: accept ipsec AH"protocol=\
    ipsec-ahaddaction=accept chain=input comment="defconf: accept ipsec ESP"protocol=\
    ipsec-espaddaction=accept chain=input comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=input comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LANaddaction=accept chain=forward comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop packets with bad src ipv6"src-address-list=bad_ipv6addaction=drop chain=forward comment=\"defconf: drop packets with bad dst ipv6"dst-address-list=bad_ipv6addaction=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1"\
    hop-limit=equal:1protocol=icmpv6addaction=accept chain=forward comment="defconf: accept ICMPv6"protocol=\
    icmpv6addaction=accept chain=forward comment="defconf: accept HIP"protocol=139addaction=accept chain=forward comment="defconf: accept IKE"dst-port=\500,4500protocol=udpaddaction=accept chain=forward comment="defconf: accept ipsec AH"protocol=\
    ipsec-ahaddaction=accept chain=forward comment="defconf: accept ipsec ESP"protocol=\
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/system clocksettime-zone-name=Europe/Skopje/system identitysetname="LHGG LTE6"/system notesetshow-at-login=no/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN/tool romonsetenabled=yesOn the main router. Also, remember to add "man" interface to your LAN interface list.
```

```
/interfacevlanaddinterface=ether8 name=man vlan-id=2addcomment=WAN2interface=ether8 name=net vlan-id=3adddisabled=yesinterface=bridge name=vlan20 vlan-id=20

---
```

## Response 20
@sk0003I would like to compare that with mine; how do you 'export' the config you are showing me? That 'Code All'? ---

## Response 21
@sk0003I would like to compare that with mine; how do you 'export' the config you are showing me? That 'Code All'?In Winbox, go to New Terminal and type in /export file=namefile.rscThen go to Files in the menu and right click the file that was created and Download to your PC. Then open that with a text editor. ---

## Response 22
Complete instructions here:viewtopic.php?t=203686#p1051720 ---

## Response 23
@jaclaz: Thanks, RTFM@sk0003:Okay, I feel that the problem is that I have a Bridge. None of that was mentioned in any of the videos, and I have no idea what effect this has.In this version, I have not disabled the IP address of 192.168.188.1, done that as well but made no difference (and I also don't see why it would need to be disabled?)... Update: I saw that you have a Bridge too, and it is disabled. I just disabled my Bridge, and lost all access, and now have to reboot to factory settings yet again...This is what I have/had:
```
# 2024-12-25 07:17:01 by RouterOS 7.15.1# software id = NH64-EMY2## model = SXTR/interfacebridgeaddadmin-mac=F4:1E:57:22:D7:B9auto-mac=nocomment=defconf name=bridge/interfacelteset[finddefault-name=lte1]allow-roaming=noband=""sms-read=no/interfacevlanaddinterface=ether1 name=man vlan-id=2addinterface=ether1 name=net vlan-id=3/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacelte apnset[finddefault=yes]passthrough-interface=net passthrough-mac=auto/ip pooladdname=default-dhcp ranges=192.168.188.10-192.168.188.254/queue typeaddfq-codel-ecn=nokind=fq-codel name=fq-codel-ethernet-default/queueinterfacesetether1 queue=fq-codel-ethernet-defaultsetether2 queue=fq-codel-ethernet-default/interfacebridge portaddbridge=bridge comment=defconfinterface=ether1addbridge=bridge comment=defconfinterface=ether2/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=lte1 list=WAN/ip addressaddaddress=192.168.188.1/24comment=defconfinterface=bridge network=\192.168.188.0/ip dhcp-serveraddaddress-pool=default-dhcp disabled=yesinterface=bridge name=defconf/ip dhcp-server networkaddaddress=192.168.188.0/24comment=defconf dns-server=192.168.188.1\
    gateway=192.168.188.1netmask=24/ip dnssetallow-remote-requests=yes/ip dnsstaticaddaddress=192.168.188.1comment=defconf name=router.lan

---
```

## Response 24
@Amm0Not sure if you are still around, but in the end after days of endless factory resets, I ended up with roughly what you proposed.I never ever got a VLAN to work, either with the SXT in default Bridge mode, or in passthrough.So now I left the SXT LTE6 as default, except I closed the DHCP server. Then I added the IP address manually from the Bridge to the *primary* /24 network, as 192.168.50.253.. 254 is the Hex main router, connected to the Starlink WAN.Then on the Hex I added a second route 0.0.0.0/0 to 192.168.50.253 distance 2.When I now pull the plug on the Starlink WAN, it re-routes to the SXT okay.But when I put it back in, some bad stuff happens.- I lose all ICMP connections from the Windows PC's to the Internet. However, other TCP connections work. UDP, don't know. To fix this, I need to restart the Ethernet interfaces on all Windows PC's.This problem does NOT occur on Android devices.A remote connection to the remote Windows PC in the shed in the paddock fails; I then have to also reset my reverse-SSH pipe system on a local Raspberry-PI router (which allows TCP access by Port to equipment on my local LAN via a VPS I have) .So while I do have a working secondary Internet system, there are problems which I do not fully understand.Also, I will need a script which can enable/disable the two Internet links based on a 'ping' system, but in such a way that it does not switch over on any small packet loss, which happens on Starlink quite a bit.Any ideas welcome, and any info on the ICMP Ping issues also... ---

## Response 25
Not @Amm0 but if I may, these are the issues I've mentioned a few posts ago. The following is anassumptionthat needs to be confirmed, but: echo requests (pings) have an ID which stays the same as long as the particular ping command is running, so the firewall treats them (and the responses to them that bear the same ID) as a single logical connection. When you start pinging while the Starlink uplink is down, the first ping request gets to the hEX which forwards it via the SXT, so no src-nat is activated for the connection. It also should send back a notification about the .253 (the SXT) being a better router than the .254 (itself) to the sender, so the sender should send the subsequent echo request packets directly via SXT, bypassing routing on the hEX, which the Androidsprobablydo and the Windowsprobablydon't. So the tracked connection in the hEX dies off within 10 seconds as it does not get updated by subsequent packets in the Android case, but stays alive as it keeps getting updated in the Windows case. Now once the Starlink path becomes available again, the incoming request packets keep hitting the existing tracked connection without src-nat activated but start getting routed out via Starlink; the Starlink router has no dedicated route towards 192.168.50.0/24 so even if it src-nats the requests to its WAN address (from the CGNAT range) and thus receives responses to them, after un-src-nating the responses their destination address becomes 192.168.5.x so the Starlink router sends them back to the sky.I usually don't care about pings since whatever daemon uses them for checking address or path availability doesn't send all of them with the same ID, but I do care about UDP in this regard, so I periodically run a housekeeping script that removes tracked connections whosereply-dst-addressdoes not match the one of currently activeout-interface.As for TCP connections, they give up within tens of seconds, and either the application automatically initiates a new connection from a different local port so it gets treated as a separate tracked connection, or it doesn't (like SSH) and you have to do that manually.All the above would work almost the same even if the SXT was connected using another subnet. Just instead of no src-nat at all, the connections that initially established via SXT would remeber a wrongreply-dst-address. ---

## Response 26
I usually don't care about pings since whatever daemon uses them for checking address or path availability doesn't send all of them with the same ID, but I do care about UDP in this regard, so I periodically run a housekeeping script that removes tracked connections whosereply-dst-addressdoes not match the one of currently activeout-interface.All the above would work almost the same even if the SXT was connected using another subnet. Just instead of no src-nat at all, the connections that initially established via SXT would remeber a wrongreply-dst-address.Thanks for that; I think the fact that I also seem to lose my remote control (called "Remote Utilities") is likely because it will use UDP.So based on what you describe, what can I do to clear the situation after a return to the Starlink WAN?Just to confirm, when I pull the plug on the Starlink WAN, the fallback to the SXT is immediate and works perfectly for most connected equipment, but it goes wrong on return to the Starlink.Is there a command / script which I can use to force/clear the previous connection, like your housecleaning script? ---

## Response 27
Unfortunately, all the devices where I have this script are currently offline, so I cannot copy-paste it.So the following is not tested:
```
:if([:len[/ip route find where dst-address=0.0.0.0/0active distance=1]]>0)do={:foreachconnin=[/ip firewall connection findwhere!srcnat!(dst-address~"^(192\\.168|10\\.|172\\.(1[6-9]|2|3[01])\\.)")]do={:docommand={/ip firewall connectionremove$conn}on-error={:nothing}}}EDIT:fixed a missing !

---
```

## Response 28
Only as a side-side note, I remember that rextended advised to use a "remaining time" filter of 60 seconds to avoid invalid results when removing connections:viewtopic.php?t=103812#p977354though it is aimed to more complex setups with lots of existing connections, while this should match only a handful of connections, and thus should be very fast in execution, a shorter time like 10 seconds may still be advisable to avoid issues.Only needed if you consistently get issues like " no such item (4)" when running the script by sindy. ---

## Response 29
@rextended is a very meticulous guy, and my script actually follows his other solution to the same issue, i.e. to use aforeachcycle rather than applying theremovecommand on the whole list, and to make sure that a failed attempt to remove an already non-existent individual item will not break the whole script by using the:do command on-errorconstruct. ---

## Response 30
Ahh, good to know, thanks, the trick is the "on error" , I didn't know that it actually allowed the prosecution of the loop in case of error. ---

## Response 31
Not @Amm0 but if I may, these are the issues I've mentioned a few posts ago.@BartKindtNZ - sorry just reading this. But @sindy offers better advice here. I put him in the "meticulous" category too.I was trying to get you up-and-running in few steps to be able to test/tweak... but I forgot that that new LTE devices use 192.168.188.1 as their default, which makes my quick routing+VRR{ suggestion slightly different. Basically I just a fan separating problems. i.e. make sure LTE work on SXT first, then move on to adding to hEX [either via routing or LTE passthrough], and then finally optimizing failover.But on checking starlink... the check-gateway=ping method should be okay. It's actually 3 pings in a row that have to fail, so takes a 30 second outage to failover to LTE. I'm not a fan of the "recursive routes" (i.e. adding routes with 8.8.8.8/etc) - at least to start – since it's very exacting config to get right. You can see in starlink app the length of longest outage, and if less than 30 seconds, the basic method should be okay.And to expand what @sindy points out the /ip/firewall/connection is what will effect recovery after "switching WANs". /ip/firewall/connections essentially "caches" connections - so if it remembers a connection it will send it out the dead WAN until it times out (or clear by script like one above). Stuff like TCP from web request recover by retry typically. But UDP does not have "connections", so /ip/firewall/connections has rules to "guess"* at UDP connections (*there are setting to control) so recovery speed for UDP depends on how the UDP-based application behaves - but it's typically UDP things that require scripting to clear connections if you want a faster failover. ---

## Response 32
So the following is not tested:
```
:if([:len[/ip route find where dst-address=0.0.0.0/0active distance=1]]>0)do={:foreachconnin=[/ip firewall connection findwhere!srcnat(dst-address~"^(192\\.168|10\\.|172\\.(1[6-9]|2|3[01])\\.)")]do={:docommand={/ip firewall connectionremove$conn}on-error={nothing}}}I am strugling to understand the IP address structure in the script; I am a Delphi Pascal programmer, and this script with all the escape characters etc. I find difficult to decode. Before I use it I first must check if the IP addresses are correct for my setup. That is: Default gataway is 192.168.1.1 ; Backup gateway is at 192.168.50.253. I will have to study the scripting language to make sense out of it.Big thanks to all who are helping!

---
```

## Response 33
The IP addresses are all the private ones (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) and thedst-addressattribute of a tracked connection is typically a socket (ip.add.re.ss:port), so the only possible way of matching is a regular expression. In regular expressions, a dot represents "any symbol", so it has to be escaped by a backslash in order to be interpreted literally (unless I have it wrong), but since it is within a string, you have to escape the backslash by another one so that a single backslash would make it to the regexpSo you can simplify that provided that all the private addresses you use in your LAN come from just one of the three RFC1918 ranges, but it's a forum so I prefer the examples to be universally applicable.So in plain language:
```
ifthe route viaStarlinkisactive{foreach item(conn)on a listoftracked connections that arenotsrc-natedandtheir destination addressisnotaprivateone{removethe itemfromthe connection tracking list,ignoring eventual errors}}Now the above is a great example of "rubber duck debugging", because as translating the script into plain English, I've noticed that while debugging the regular expression on my router, I removed the ! before the(dst-address ...)and forgot to put it back, so I'm editing that post now.

---
```

## Response 34
So in plain language:
```
ifthe route viaStarlinkisactive{foreach item(conn)on a listoftracked connections that arenotsrc-natedandtheir destination addressisnotaprivateone{removethe itemfromthe connection tracking list,ignoring eventual errors}}Big thanks for all that; Now the stupid question: Where do I insert this script?

---
```

## Response 35
Where do I insert this script?On the command line:/system script add name=housekeeper/system script edit housekeeper sourcepaste the script copied from my edited post above and press Ctrl-O to save it.Then imitate the outage of Starlink and its recovery, and use/system script run housekeeper- if that helps the strayed connections to start working again, it makes sense to add a/tool scheduleritem that will spawn it every minute or so. ---

## Response 36
@sindyThat works brilliantly, thanks!Now the last thing I need to sort out, is how to drop the Starlink WAN interface when it loses Internet connection. I can pull the plug on the Starlink WAN, and it switches over perfectly, but at the moment I do not yet have a test/ping to 8.8.8.8 which will then cause the STARLink WAN to drop.Would the script from sk0003 work in my case?Big thanks for all your help! ---

## Response 37
For detection of failure of starlink... Three+ choices:1. "check-gateway=ping", seehttps://help.mikrotik.com/docs/spaces/R ... verExample& post my aboveTo do this, you can add a script to the /ip/dhcp-client for starlink on hEX
```
:if($bound=1)do={/ip routeset[/ip route find gateway=$"gateway-address"]check-gateway=ping}2. "Recursive Routes", seehttps://help.mikrotik.com/docs/spaces/R ... WAN+Backup& @sk0003 series of posts, including the update script in /ip/dhcp-client::if ($bound=1) do={/ip route add distance=1 gateway=$"gateway-address" dst-address="192.5.5.241" scope=30  target-scope=31  comment="Starlink"/ip route add distance=3 gateway="192.5.5.241" check-gateway=ping scope=30  target-scope=32 comment="Starlink"} else={/ip route remove [/ip route find comment="Starlink"]}3. Netwatch scripts, seehttps://help.mikrotik.com/docs/spaces/R ... ickExample... which we don't cover in this thread but this requires custom scripts but netwatch allows a very flexible approach to detecting failures.4. BFD, seehttps://help.mikrotik.com/docs/spaces/R ... 299691/BFD... again not covered here, but it requires BGP and not usable in home/SMB situations, but its the "fastest" at detecting failurePick your poison.  Also note, you only need it on the starlink, since LTE will drop and is the "last choice" anyway.

---
```

## Response 38
If it can be adapted to your situation (and it seems to me it can), this:viewtopic.php?t=198999further simplified:viewtopic.php?t=198999&hilit=simpler#p1102129is IMHO the simplest method (using a simple Netwatch script that just enables and disables a route).I have read here and there that a Starlink connection can be problematic because it can disconnect temporarily for a few seconds several times a day to soon resume by itself, so I believe the timing of the failover method is important and a netwatch script (more complex than the one in the given example) or a "fine tuning" of the ICMP probe settings might be more suitable than the check gateway or recursive. ---

## Response 39
In my understanding, "check-gateway=ping" and "recursive next-hop search" mostly only make sense together. Usingnetwatchis fine as long as you use only a single canary IP per WAN; as soon as you want more of them, it requires quite some scripting to aggregate the results, so a full-size scheduled script becomes more useful as you can fine-tune it to your needs.Regarding the recursive next hop search, let me disagree with @Amm0 - while it is definitely more difficult to understand than a standalonenetwatch, I consider this method far simpler than a script, because you just add N /32 routes to canary addresses and N default routes, all with the samedistancebut each using another canary address asgateway, and that's it (if you set thescopeof the routes to canaries and thetarget-scopeof the default routes properly of course). You only need scripting if the DHCP server sometimes changes the gateway address. For Starlink in particular, you either get always 192.168.1.1 if using their bundled router or 100.64.0.1 if using a software or hardware bypass, so the recursive next-hop search comes script-free in your case. Yes, it does have that rigid failover time - 3 pings 10 seconds apart must get unresponded so that the canary was considered dead, but I haven't had a single case of a false positive caused by Starlink short-term loss of connection when using it, even with a single canary. What I did have, though, was 8.8.8.8 unreachability via Starlink for minutes, at multiple geographically distant sites simultaneously whilst other internet destinations were reachable alright, so to me, the use of multiple canaries definitely makes sense.There are cases where a failover after 30 seconds is way too late (some VPNs don't tolerate such an outage); there, a full-size scripting is the only way, but then you can ping the canary multiple times per second and fail over within two seconds.Regarding LTE - I'm not going to argue whether the LTE interface presents itself to the routing stack as being down if it loses the wireless connection - at least it doesn't when the issue is account balance or alike, but the Ethernet on the SXT definitely doesn't go down in such a case (well, unless you use scripting on the SXT to force it down but I don't think it is a good idea to cut off access to device management whenever the LTE uplink stops working). There is indeed no point in tracking the state of the "WAN of last resort" from the point of view of failover (if all WANs are down, you're offline, full stop), but for any redundancy setup, it makes a lot of sense to be informed about failures of the backup elements while the primary ones are alive - otherwise the unavailability of backup may remain unnoticed for months. So you may want to consider monitoring also the transparency of the LTE connection and using e-mail or Telegram to send notifications about the status changes. ---

## Response 40
@Amm0As usual, everything I try does not seem to work as advertized.I am trying to use the 'canary' system, but I cannot make it work.First this:
```
/ip firewall nataddchain=srcnat action=masqueradeout-interface=ether1addchain=srcnat action=masqueradeout-interface=bridge/ip routeadddst-address=9.9.9.9scope=10gateway=192.168.1.1adddst-address=8.8.4.4scope=10gateway=192.168.50.253adddistance=1gateway=9.9.9.9target-scope=11check-gateway=pingadddistance=2gateway=8.8.4.4target-scope=11check-gateway=pingNothing happens when 9.9.9.9 fails (when I disconnect the Starlink dish from the Starlink WIFI unit). I just lose all Internet, and the second gateway does not come online.So question: When the Ping to 9.9.9.9 fails after 3 times (?), what is actually supposed to happen?  Who decides that it should start using the second gateway, and how does it do this?When I then add this:
```

```
:if($bound=1)do={/ip routeadddistance=1gateway=192.168.1.1dst-address="9.9.9.9"scope=10target-scope=31comment="Starlink"/ip routeadddistance=3gateway=9.9.9.9check-gateway=ping scope=10target-scope=32comment="Starlink"}else={/log info"Failover: Deleting main route"/ip routeremove[/ip route find dst-address=0.0.0.0/0andgateway=192.168.1.1]}The interface is _always_ Bound. Even if the Starlink disk falls of the roof. So when does this delete main Route occur? Only when I pull the plug between the Starlink WIFI unit and the main Switch.Then, even IF this main route has been deleted, how do I get it back? Because my second Gateway is an IP address on the main LAN, and not part of a DHCP-Client.Sorry for all the questions...

---
```

## Response 41
When 9.9.9.9 is not pingable any more, the default route via 9.9.9.9 should stop being "active" after those 30 seconds (the A letter in the leftmost column should disappear). Is that not the case? Your configuration looks OK to me, but better show the complete output of/ip route print detail. ---

## Response 42
This is with the system live:
```
[admin@MikroTik]>/ip routeprintdetailFlags:X-disabled,A-active,D-dynamic,C-connect,S-static,r-rip,b-bgp,o-ospf,m-mme,B-blackhole,U-unreachable,P-prohibit0ADS  dst-address=0.0.0.0/0gateway=192.168.1.1gateway-status=192.168.1.1reachable via  ether1 distance=1scope=30target-scope=10vrf-interface=ether11S  dst-address=0.0.0.0/0gateway=192.168.50.253gateway-status=192.168.50.253reachable via  bridge check-gateway=ping 
        distance=2scope=30target-scope=102S  dst-address=0.0.0.0/0gateway=8.8.4.4gateway-status=8.8.4.4recursive via192.168.50.253bridge check-gateway=ping 
        distance=2scope=30target-scope=113S;;;Starlinkdst-address=0.0.0.0/0gateway=9.9.9.9gateway-status=9.9.9.9recursive via192.168.1.1ether1 check-gateway=ping 
        distance=3scope=10target-scope=324A S  dst-address=8.8.4.4/32gateway=192.168.50.253gateway-status=192.168.50.253reachable via  bridge distance=1scope=10target-scope=105S  dst-address=8.8.4.4/32gateway=192.168.50.253gateway-status=192.168.50.253reachable via  bridge distance=1scope=10target-scope=106A S;;;Starlinkdst-address=9.9.9.9/32gateway=192.168.1.1gateway-status=192.168.1.1reachable via  ether1 check-gateway=ping 
        distance=1scope=10target-scope=317ADC  dst-address=192.168.1.0/24pref-src=192.168.1.195gateway=ether1 gateway-status=ether1 reachable distance=0scope=108ADC  dst-address=192.168.50.0/24pref-src=192.168.50.254gateway=bridge gateway-status=bridge reachable distance=0scope=109A S  dst-address=192.168.50.253/32gateway=bridge gateway-status=bridge reachable distance=2scope=30target-scope=10[admin@MikroTik]>This is with the StarLink Dishy disconnected, after a few minutes:
```

```
[admin@MikroTik]>/ip routeprintdetailFlags:X-disabled,A-active,D-dynamic,C-connect,S-static,r-rip,b-bgp,o-ospf,m-mme,B-blackhole,U-unreachable,P-prohibit0ADS  dst-address=0.0.0.0/0gateway=192.168.1.1gateway-status=192.168.1.1reachable via  ether1 distance=1scope=30target-scope=10vrf-interface=ether11S  dst-address=0.0.0.0/0gateway=192.168.50.253gateway-status=192.168.50.253reachable via  bridge check-gateway=ping 
        distance=2scope=30target-scope=102S  dst-address=0.0.0.0/0gateway=8.8.4.4gateway-status=8.8.4.4recursive via192.168.50.253bridge check-gateway=ping 
        distance=2scope=30target-scope=113S;;;Starlinkdst-address=0.0.0.0/0gateway=9.9.9.9gateway-status=9.9.9.9recursive via192.168.1.1ether1 check-gateway=ping 
        distance=3scope=10target-scope=324A S  dst-address=8.8.4.4/32gateway=192.168.50.253gateway-status=192.168.50.253reachable via  bridge distance=1scope=10target-scope=105S  dst-address=8.8.4.4/32gateway=192.168.50.253gateway-status=192.168.50.253reachable via  bridge distance=1scope=10target-scope=106A S;;;Starlinkdst-address=9.9.9.9/32gateway=192.168.1.1gateway-status=192.168.1.1reachable via  ether1 check-gateway=ping 
        distance=1scope=10target-scope=317ADC  dst-address=192.168.1.0/24pref-src=192.168.1.195gateway=ether1 gateway-status=ether1 reachable distance=0scope=108ADC  dst-address=192.168.50.0/24pref-src=192.168.50.254gateway=bridge gateway-status=bridge reachable distance=0scope=109A S  dst-address=192.168.50.253/32gateway=bridge gateway-status=bridge reachable distance=2scope=30target-scope=10[admin@MikroTik]>According to the display, the link to 9.9.9.9 is still live, which is impossible as the entire hardware is disconnected.So at this state, I have no internet access.  The second interface is not used.  Only when I pull the plug on the WAN, if fails over to the second gateway.

---
```

## Response 43
Therouteto 9.9.9.9 is indeed active even if Starlink is dead because it does not check the gateway availability, that's OK. What is important that 9.9.9.9 cannot be actually pinged via 192.168.1.1 once Starlink dies, so thecheck-gatewayping fails.First, remove the script that adds and removes the default routes, you can use one or the other approach, not mix them.Next, set thedistanceof the default route withgateway=192.168.1.1to 10 and thedistanceof the default route withgateway=192.168.50.253to 11, and set thedistanceof the default routes withgateway=9.9.9.9to 1; keep thedistanceof the default route withgateway=8.8.4.4unchanged, i.e. 2.Then try again. While Starlink is connected, the default route withgateway=9.9.9.9will be active because the pings via 9.9.9.9 will keep succeeding; once the ping fails for long enough, it will become inactive and the route withgateway=8.8.4.4will take over. ---

## Response 44
Next, set thedistanceof the default route withgateway=192.168.1.1to 10 and thedistanceof the default route withgateway=192.168.50.253to 11, and set thedistanceof the default routes withgateway=9.9.9.9to 1; keep thedistanceof the default route withgateway=8.8.4.4unchanged, i.e. 2.Thanks, that worked immediately. But now it refuses to get back to the main WAN, and I lost access to the Starlink system.When I connect to the Starlink WIFI (which I normally never do) I have Internet connection, but via the Hex WAN to it, I cannot reach it.EDIT: Oops I see a mistake. Will try again.EDIT 2: No, I now have real problems. I completely lost access to the Starlink WAN. It says 192.168.1.1 Unreachable. Even after restarting the interface and restarting the Starlink WIFI unit.The interface exists and even shows traffic. The DHCP-Client shows it is Bound. The route says it is unreachable. I don't understand what is going on...Help? ---

## Response 45
change the 9.9.9.9 route's distance to 1, the dhcp one is not used since 0.0.0.0 routes to 9.9.9.9, which then routes to 192.168.168.1 - why it's called recursive routing: it goes through the route table twice. the one with distance 10 is in fact correctly not used/unavailable since a route with a higher distance= is available. ---

## Response 46
change the 9.9.9.9 route's distance to 1, the dhcp one is not used since 0.0.0.0 routes to 9.9.9.9, which then routes to 192.168.168.1 - why it's called recursive routing: it goes through the route table twice. the one with distance 10 is in fact correctly not used/unavailable since a route with a higher distance= is available.Thanks man, I have completely cleared the system, and re-entered the data in the right way. To much editing going on.I think I now have it working, going both ways.It still does not clear any 'pings' which I run from the two Windows PC's during testing.It stops pinging to a specific host, but when I switch pinging to another host it works. While at the sime time the other PC works exactly the other way aroundIt seems that Windows remembers an ICMP route to a specific IP address. This then fails after the switchover. But then pinging something else, it works.It is confusing when you try to determine if the switchover worked.Using an Android phone, pinging 8.8.8.8 continuousely, it continues without a single packet lost. Much better system.This screenshot from when it switched to the secondary gateway. ---

## Response 47
THE FINAL SIMPLE SOLUTION:Both the RouterBoard Hex and the SXT LTE6 are used in their *default* configurations.The Routerboard is in default Router mode, the LTE6 is in default Bridge mode.The main IP range used here is 192.168.50.0/24.The Routerboard IP address is 192.168.50.254, and its default Gateway is a Starlink at 192.168.1.1 on ether1 (From Starlink DHCP Server)The entire local network is on a single ethernet port on the Hex (because it connects to a huge Switch)In the LTE6 I disabled the DHCP Server. Its IP address is manually set to 192.168.50.253 (so on the main network). No VLAN's or LTE-Passthrough's are used.The failover is by setting the Distance for the primary and secondary Gateways to 10 and 11.In /ip dhcp-client, advanced, set the distance to 10.Then in the Terminal:
```
/ip route add 0.0.0.0/0gateway192.168.50.253distance11/ip firewall nataddchain=srcnat action=masqueradeout-interface=ether1/ip firewall nataddchain=srcnat action=masqueradeout-interface=bridge/ip routeadddst-address=9.9.9.9scope=10gateway=192.168.1.1/ip routeadddst-address=8.8.4.4scope=10gateway=192.168.50.253/ip routeadddistance=1gateway=9.9.9.9target-scope=11check-gateway=ping/ip routeadddistance=2gateway=8.8.4.4target-scope=11check-gateway=pingif the Ping to 9.9.9.9 fails, it falls back on the 192.168.50.253 gateway (which is simply on the main network).When the Ping works again, it switches back to the main Starlink gateway.In addition I added sindy's Houskeeping script to clean up old routes, but I am not quite sure how much this helps:
```

```
/system scriptaddname=housekeeper/system script edit housekeeper source:if([:len[/ip route find where dst-address=0.0.0.0/0active distance=1]]>0)do={:foreachconnin=[/ip firewall connection findwhere!srcnat!(dst-address~"^(192\\.168|10\\.|172\\.(1[6-9]|2|3[01])\\.)")]do={:docommand={/ip firewall connectionremove$conn}on-error={:nothing}}}Paste the script into the window and press Ctrl-O to save it.Execute:
```

```
/system script run housekeeperI used the scheduler to run it every minute.It now works fine here, without any complicated setup's.There are weird ICMP / Ping issues with connected Windows PC's, while Android devices seem to switch without trouble (Yay Linux!)BIG thanks for all who helped me and taught me a lot!

---
```