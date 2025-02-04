# Thread Information
Title: Thread-1122715
Section: RouterOS
Thread ID: 1122715

# Discussion

## Initial Question
Hi all, Pulling my hear out on this one. I was working on a recursive WAN fail-over set-up. The main WAN for normal traffic, and an LTE WAN for backup. The main WAN has a dedicated dynamic Wireguard interface that connect to a static remote WG peer. The LTE WAN needs another (backup) dynamic WG interface/peer that is always up/accessible over LTE. Hence, even when the recursive fail-over is still using the main WAN. That turned out be become a multi-day dilemma...So I reset the whole device and started over. BTW I'm on 7.17.Turns out that the mangle routing rule also doen not work with an extremely basic config (not even using any recursive failover, wireguard interfaces, firewall rules etc)!wifi1 and wifi2 are the 2 WANs in this basic test set-up (no LTE modem in this case). Ether1 is the LAN. Bridge is unused.Either I'm completely stupid, or something weird is happening here. This is the basic config:
```
# 2025-01-29 19:45:50 by RouterOS 7.17
# software id = UXH4-3WB2
#
# model = L23UGSR-5HaxD2HaxD
# serial number = 
/interface bridge
add admin-mac=D4:01:C3:A9:D0:43 auto-mac=no comment=defconf fast-forward=no name=bridge
/interface ethernet
set [ find default-name=sfp1 ] advertise=10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full,1G-baseX
/interface wifi
set [ find default-name=wifi1 ] channel.band=2ghz-ax .skip-dfs-channels=10min-cac .width=20/40mhz configuration.mode=station .ssid=WIFI1 disabled=\
    no name=wifi1_WAN1 security.authentication-types=wpa2-psk .ft=yes .ft-over-ds=yes
set [ find default-name=wifi2 ] channel.band=5ghz-ax .skip-dfs-channels=10min-cac .width=20/40/80mhz configuration.antenna-gain=0 .chains=0,1 .country=\
    Netherlands .mode=station .ssid=WIFI2 .tx-chains=0,1 disabled=no name=wifi2_WAN2 security.authentication-types=wpa2-eap \
    .eap-certificate-mode=dont-verify-certificate .eap-methods=peap .eap-username=USERNAME .encryption="" .ft=yes .ft-over-ds=yes
/interface list
add name=WAN
/routing table
add disabled=no fib name=WAN2
/ipv6 settings
set disable-ipv6=yes
/interface list member
add interface=wifi1_WAN1 list=WAN
add interface=wifi2_WAN2 list=WAN
/ip dhcp-client
add add-default-route=no comment=" " interface=ether1 use-peer-dns=no use-peer-ntp=no
add add-default-route=no interface=wifi1_WAN1 use-peer-dns=no use-peer-ntp=no
add add-default-route=no interface=wifi2_WAN2 use-peer-dns=no use-peer-ntp=no
/ip firewall mangle
add action=mark-routing chain=prerouting dst-address=8.8.8.8 log=yes new-routing-mark=WAN2 passthrough=no
/ip firewall nat
add action=masquerade chain=srcnat log=yes out-interface-list=WAN
/ip route
add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=192.168.30.1 routing-table=main scope=30 suppress-hw-offload=no target-scope=10
add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=192.168.80.1 routing-table=WAN2 scope=30 suppress-hw-offload=no target-scope=10
/ip service
set telnet disabled=yes
set ftp disabled=yes
set api disabled=yes
set api-ssl disabled=yes
/routing rule
add action=lookup-only-in-table disabled=yes dst-address=8.8.8.8/32 table=WAN2
/system note
set show-at-login=noNote that when I use the 'routing rule' for policy based routing, it actually does work as expected. I left it in the config (as disabled) just for reference.The traffic (e.g. ping to 8.8.8.8 ) keeps going over the main WAN interface (wifi1). If I disable wifi1 no connection is being made to the second (wifi2) gateway.Any clue why this mangle rule refuses to work?

---
```

## Response 1
There is a bug with wireguard on second LAN interface, which is not fixable, something to do with how wireguard works. However there is a way around it, will post later. ---

## Response 2
You actually have two problemsWhen doing multi-wan, you should really study the packet flow diagram meticulously. A version of it is given in the Mikrotik docs, but this is often more suitable:https://stuffphilwrites.com/2014/09/ipt ... flowchart/As you can see, for locally originates packets (your ping) the "mangle prerouting" chain is never consulted (as documented)The other is wrt wireguard. Wireguard has a bit of a strange behavior in that it selects the source address for its packets based only on the main routing table. (As is quite clear from the diagram referenced.) And thus while routing is altered as a result of mangling later (and your packet is transmitted on the intended interface), its source address is incorrect.This can be helped with some ... ahem ... creative natting. The good news is that this behavior in your case is to your advantage. If you only use a singe wireguard connection, that will automagically continue on in case of a failover using your WAN2. The transition will happen within the wireguard persistent keepalive time (or if any traffic is sent into the tunnel on your side).As a side note. I did some quite involved digging around the "wireguard and mangling/routing" issue, and while the original writers of wg maintain that their solution works as intended, other say quite plainly that it "was rushed into the kernel when it wasn't ready", i.e. it did not consider all scenarios.Actually the normal linux implementation has a not-too-bad behavior around this, in that a wireguard interface can have an "fwmark" attribute attached (which means: tag all underlay outgoing packets related to this interface with this), and that can be matched in the routing rules. Mikrotik neither supports the wg fwmark, nor the matching it in routing rules behavior. (They referenced some time ago that "some solution" is on the roadmap. This is a *very* common question on both Mikrotik and general linux forums all over.) ---

## Response 3
You mention two wans (main and LTE) and what you show is actually three ( MAIN on ether1, WIFI1, WIFI2) and no LTE, so I decided to stop looking. ---

## Response 4
Ok, I'm really stupid...Tnx @lurker888 for your explanation. I have studied the Mikrotik documentation, especially these images where helpful:and the top right ofandAlso the 'MTCNA' of MikroTik Canada was helpful.Thanks for the hints.If I follow the packet flow I indeed now understand that packets originating from the router will not pass the prerouting chain. The do pass the output and postrouting chain, but that is after the 'routing decision', hence of no use. Makes sense!I also now understand that Wireguard is a bit different from other interfaces.A few small questions for my understanding:- you are referring to the Linux iptabels diagram. That is indeed much easier to read/decode. But how do you know that Mikrotik is following the iptables implementation?- below you mention "As is quite clear from the diagram referenced.". I assume you refer to the iptables diagram. Unfortunately I do not understand/see that. Could you nudge me in the right direction?The other is wrt wireguard. Wireguard has a bit of a strange behavior in that it selects the source address for its packets based only on the main routing table. (As is quite clear from the diagram referenced.) And thus while routing is altered as a result of mangling later (and your packet is transmitted on the intended interface), its source address is incorrect.- neither do I understand from the above Mikrotik diagrams how Wireguard fits in. Do you?@anav, my apologies that the situation is not clear enough from my original post. I tried to exlain that I started to build the dual WAN + dual Wireguard, which didn't work out. Then I resetted the whole device (actually used another one) to make a very basic config. That second setup has the dual wifi WAN, whereas the first has the dual WAN with wifi and LTE.But I guess you are both referring to the same issue regarding dual Wireguard interfaces on dual WAN. I hope I can figure it out do create the... ahem ... creative nattingthing. ---

## Response 5
If I follow the packet flow I indeed now understand that packets originating from the router will not pass the prerouting chain. The do pass the output and postrouting chain, but that is after the 'routing decision', hence of no use. Makes sense!Glad you understand. But I'm not sure you do so completely. When an output packet is generated it goes straight to the "routing decision" stage. It doesn't pass any sort of mangle chain before that. This has two consequences:* In tems of routing: If by some other means (application level software, TCP stack, etc.) the packet has a routing mark, then it will be observed, but otherwise the routing decision is based on the main table. *However* then it passes the "postrouting" chain where a routing mark can be assigned. Then there is a "routing adjustment" phase where routing is corrected based on any marks applied in postrouting. So if you mark your packets in "postrouting output", then the packet will undergo a next round of routing, and all will work out well for you: the packet will exit according to the routing rules/tables/vrfs that you would want. (BTW This leads to a strange behavior that if there is no route to a given dst in the main table, the packet will be instantly blackholed, even if - were it to go through postrouting and routing adjustment - it could be routed successfully. So a route in the main has to exist, even if it points nowhereBtw of btw: There is actually a remark about this in the Mikrotik docs, but if you don't know the full story, you would never notice.)* The *other* - and in your current case more important - story concerns the source address of packets. Source addresses are normally assigned either (1) by the application layer (e.g. a DNS server receives a UDP query, it should clearly specify (to the kernel) as the source address of the reply the address the query was received on), (2) by other networking layers, e.g. TCP will originate packets from the address the SYN was received on, or from which the SYN was sent during the handshake. But if still a packet has no source address (often referenced as the "address of last resort") the packet acquires the "pref src address" of the route it takes. And here's the strangeness: this assignment happens during the initial "routing decision" and is not (can't be) corrected in the "routing adjustment" phase. Wireguard - by its design - doesn't assign source addresses to its outgoing packets, which leads to a situation where if the packet is to be redirected in the "mangle postrouting" chain, it will go out on the correct interface, but with the wrong source address. Happy world.I also now understand that Wireguard is a bit different from other interfaces.A few small questions for my understanding:- you are referring to the Linux iptabels diagram. That is indeed much easier to read/decode. But how do you know that Mikrotik is following the iptables implementation?Because it is. If you look closely, they line up kind of perfectly. Just disregard the "security" chains, because they are only there when SELinux is used. Use both, whichever is clearer for the particular issue you are trying to resolve.There is one mismatch between the diagrams. The Mikrotik diagram is missing the (seldom used) "input src-nat" stage. This is an error in their diagram; their routers actually apply it correctly, as it is written in the kernel codebase.- below you mention "As is quite clear from the diagram referenced.". I assume you refer to the iptables diagram. Unfortunately I do not understand/see that. Could you nudge me in the right direction?The other is wrt wireguard. Wireguard has a bit of a strange behavior in that it selects the source address for its packets based only on the main routing table. (As is quite clear from the diagram referenced.) And thus while routing is altered as a result of mangling later (and your packet is transmitted on the intended interface), its source address is incorrect.- neither do I understand from the above Mikrotik diagrams how Wireguard fits in. Do you?I hope the above explanation clears up the quoted part of my post.As to how wireguard fits in. Wireguard is an application level service (although implemented in kernel space), so packets *to* it enter at I and exit at J, its output packets enter at K and exit at L.But I guess you are both referring to the same issue regarding dual Wireguard interfaces on dual WAN. I hope I can figure it out do create the... ahem ... creative nattingthing.It's not totally clear from your description, but I gather that both connections are initiated *from* your device. (I.e. it does not have to contend with incoming wireguard connections.) In this case - if you are willing to follow my recommendation of using a single wireguard tunnel that is automatically rerouted in case of failover - the "creative natting" is not necessary. (Automatically in this sense means that it will use the active default route and no special configuration is needed, so if your other traffic is working correctly - so will the wg tunnel) ---