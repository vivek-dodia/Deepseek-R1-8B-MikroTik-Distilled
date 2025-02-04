# Thread Information
Title: Thread-1113783
Section: RouterOS
Thread ID: 1113783

# Discussion

## Initial Question
My router has a total of three ISP exits. I tried using ISP1 and ISP2 as ECMP routing tables and allowed some devices within the local network to use this ECMP routing table outgoing gateway. The other devices use the default main outgoing gateway.However, the problem is that after I set everything up, this specific device(10.0.0.130) did not follow the expected ECMP routing table and instead accessed the internet through the default gateway(pppoe-out8).I checked many times, but still couldn't find out where the problem was, and the mikrotik help documents also did not have any relevant guidance.I hope that experts within the community can help me out. Below is my configuration.
```
@MikroTik] > export
# 2024-12-07 21:13:40 by RouterOS 7.16.2
# software id = xxxxxxxxx
#
# model = CCR1036-12G-4S
# serial number = xxxxxxxxxx


/interface ethernet
set [ find default-name=ether1 ] disabled=yes
set [ find default-name=ether2 ] disabled=yes
set [ find default-name=ether3 ] disabled=yes
set [ find default-name=ether4 ] disabled=yes
set [ find default-name=ether7 ] disabled=yes
set [ find default-name=ether8 ] disabled=yes
set [ find default-name=ether9 ] disabled=yes
set [ find default-name=ether10 ] disabled=yes
set [ find default-name=sfp3 ] disabled=yes
set [ find default-name=sfp4 ] disabled=yes
/interface pppoe-client
add disabled=no interface=sfp2 name=pppoe-out8 user=<pppoe-username>
/interface macvlan
add interface=ether5 mac-address=B2:54:05:89:BA:8B mode=private name=macvlan1
add interface=ether5 mac-address=F6:4F:AA:AD:82:B6 mode=private name=macvlan2
add interface=ether6 mac-address=42:DB:28:D3:57:FB mode=private name=macvlan3
add interface=ether6 mac-address=DE:E8:E3:5F:A8:00 mode=private name=macvlan4
/interface bonding
add mode=802.3ad name=bonding1 slaves=ether11,ether12
/interface pppoe-client
add disabled=no interface=macvlan1 name=pppoe-out1 user=<pppoe-username>
add disabled=no interface=macvlan2 name=pppoe-out2 user=<pppoe-username>
/interface list
add name=WAN
add name=LAN
add name=LB
/ip pool
add name=dhcp ranges=10.0.0.150-10.0.0.240
/ip dhcp-server
add address-pool=dhcp interface=bonding1 name=dhcp1
/routing table
add disabled=no fib name=ecmp
add disabled=no fib name=CMIP_route
/ip settings
set ipv4-multipath-hash-policy=l4
/interface list member
add interface=sfp1 list=WAN
add interface=pppoe-out8 list=WAN
add interface=pppoe-out1 list=LB
add interface=pppoe-out2 list=LB
add interface=bonding1 list=LAN
/ip address
add address=10.0.0.1/24 comment=defconf interface=bonding1 network=10.0.0.0
/ip dhcp-server network
add address=10.0.0.0/24 dns-server=119.29.29.29,223.5.5.5 gateway=10.0.0.1 netmask=24
/ip dns
set servers=119.29.29.29,119.28.28.28,2402:4e00::,2402:4e00:1::
/ip firewall filter
add action=accept chain=input comment="accept established,related,untracked" connection-state=\
    established,related,untracked disabled=yes
add action=drop chain=input comment="drop invalid" connection-state=invalid disabled=yes
add action=accept chain=input comment="accept ICMP" disabled=yes in-interface-list=WAN protocol=icmp
add action=accept chain=input comment="allow Winbox" disabled=yes in-interface-list=WAN port=8291 protocol=tcp
add action=accept chain=input comment="allow SSH" disabled=yes in-interface-list=WAN port=22 protocol=tcp
add action=drop chain=input comment="block everything else" disabled=yes in-interface-list=WAN
/ip firewall nat
add action=masquerade chain=srcnat out-interface-list=LB
add action=masquerade chain=srcnat out-interface-list=WAN
/ip route
add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out1 routing-table=ecmp scope=30 suppress-hw-offload=\
    no target-scope=10
add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out2 routing-table=ecmp scope=30 suppress-hw-offload=\
    no target-scope=10
add disabled=no distance=10 dst-address=0.0.0.0/0 gateway=pppoe-out8 routing-table=main scope=30 \
    suppress-hw-offload=no target-scope=10
/ip service
set telnet disabled=yes
set ftp disabled=yes
set ssh address=10.0.0.0/24
set api disabled=yes
set winbox address=10.0.0.0/24
set api-ssl disabled=yes
/ip ssh
set host-key-type=ed25519 strong-crypto=yes
/lcd
set enabled=no
/routing rule
add action=lookup disabled=no min-prefix=0 src-address=10.0.0.130/32 table=ecmp
add action=drop disabled=no dst-address=10.0.0.100/32 min-prefix=0 src-address=10.0.0.130/32
/system clock
set time-zone-name=Asia/Shanghai
/system logging
set 0 topics=info,!dhcp
/system note
set show-at-login=no
/system routerboard settings
set enter-setup-on=delete-key
/tool bandwidth-server
set enabled=no
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN

---
```

## Response 1
Your configuration export doesn't show any reason why 10.0.0.130 should use routing tablemain, however, as of current (7.16.x), there are issues with handling of themin-prefixvalue in configuration. So unless you have added the first routing rule already with that value specified, add the same rule before (above) it using command line and then remove the existing one:
```
/ip route rule {
  :local myRule [find where table=ecmp]
  add copy-from=$myRule place-before=$myRule
  remove $myRule
}and do notmodifythe routing rules later - if you need to change something in a routing rule,adda new one before the one that needs change, and then remove the old one.Your second routing rule makes little sense to me as it says "drop the packet from 10.0.0.130 to 10.0.0.100 if the only route to 10.0.0.100 in routing tablemainis the default one", whereas a) there is a route with dst-address=10.0.0.0/24 and b) a packet from 10.0.0.130 to 10.0.0.100 is bridged, not routed, unless you have done some voodoo on the device that has 10.0.0.130 itself. What was the idea behind this rule?

---
```

## Response 2
1. Your pool isadd name=dhcp ranges=10.0.0.150-10.0.0.240Why is any device getting a LANIP of .130 ????2. Routes look messed u ( or maybe I dont understand how to apply ecmp )Should be...... at least for Version 7.Assumes ecmp is the primary and a few need to go out pppoe8 ( Edit, now I realize thats backwards see next block of code )/ip routeadd distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out1 routing-table=mainadd distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out2 routing-table=mainadd distance=10 dst-address=0.0.0.0/0 gateway=pppoe-out8 routing-table=mainadd dst-address=0.0.0.0/0 gateway=pppoe-out8 routing-table=ecmpThus, lets reflect your needs./ip routeadd dst-address=0.0.0.0/0 gateway=pppoe-out8 routing-table=main comment="Primary WAN3"add dst-address=0.0.0.0/0 gateway=pppoe-out1 routing-table=ecmpadd dst-address=0.0.0.0/0 gateway=pppoe-out2 routing-table=ecmpBetter with recursive checking of connectivity/ip routeadd dst-address=0.0.0.0/0 gateway=pppoe-out8 routing-table=main comment="Primary WAN3"add check-gateway=ping dst-address=0.0.0.0/0 gateway=1.1.1.1 routing-table=ecmp scope=10 target-scope=12 comment=ISP1add check-gateway=ping dst-address=0.0.0.0/0 gateway=9.9.9.9 routing-table=ecmp scope=10 target-scope=12 comment=ISP2add dst-address=1.1.1.1/32 gateway=pppoe-out1 routing-table=ecmp scope=10 target-scope=11add dst-address=9.9.9.9/32 gateway=pppoe-out2 routing-table=ecmp scope=10 target-scope=113. This is aSECURITY PROBLEM, never allow access to winbox from the www. ONLY from internal users, be they on LAN or after coming in on VPN.add action=accept chain=input comment="allow Winbox" disabled=yes in-interface-list=WAN port=8291 protocol=tcpEdit: I see its disabled. ( same same for ssh )4. Your input chain is still not safe due to using block vice allow and block all else.For example having this rule is weak!!add action=drop chain=input comment="block everything else" disabled=yes in-interface-list=WANThe fact that this is disabled is also very alarming!!!This is betteradd action=accept chain=input comment="allow LAN users only" in-interface-list=LANadd action=drop chain=input comment="drop all else"Now you tell me the difference between your rule and these two....?????????Notice you fail to block incoming traffic on WAN3, as your wan interface only describes WAN1 and WAN2.Its ALWAYS BETTER, to allow needed traffic and block everything else, than to think you know all the traffic that must be blocked and allow everything else..................5. WHY do you not have any forward chain rules?????????????6. Finally, WHY DO you not explain what the heck you are doing with the single IP address at the beginning??You mention a few addresses to use the ECMP but then DO NOT identify any such users, either by firewall address list OR mangling.So with a single subnet how do you propose to identify a bunch of users to use ECMP??There is some missing information and config here????7. As far as routing rules go............. okay to use for a small number of users...... this should be what you have..add action=lookup-only-in-table src-address=10.0.0.130 table=ecmp ---

## Response 3
Wow... it did not come to my mind to look that low into your config.Bothpppoe-out1andpppoe-out2are attached tomacvlaninterfaces, which in turn are attached toether5, andether5is disabled (at least in the export you have posted). Disablingether5means that all traffic, not only IP one, that would physically pass through it, is down. Sopppoe-out1andpppoe-out2are down too, and due to that, also the routes through them become inactive.And now the difference betweenaction=lookupandaction=lookup-only-in-tablein the routing rules comes into play: if noactiveroute whatsoever is available for the destination address of the packet in the routing table the rule chooses, withlookup, the packet is routed using routing tablemain; withlookup-only-in-table, the packet is dropped. ---

## Response 4
I'm not sure purpose behind using the intermediate macvlan in the first place...Also, you cannot just add a route to routing table unless same route exists in the main routing table, which may be first order problem in OP's approach. ---

## Response 5
I'm not sure purpose behind using the intermediate macvlan in the first place...It may be necessary to use a different MAC address for each PPPoE client connecting to the same ISP using the same physical interface, and macvlan is one of few ways to ensure this. I haven't tested yet, though, whether it actually works.you cannot just add a route to routing table unless same route exists in the main routing tableCan you elaborate on why should doing so be a problem? ---

## Response 6
Re macvlan, it might be useful in some cases... but adds more complexity if it's not actually needed was my point.you cannot just add a route to routing table unless same route exists in the main routing tableCan you elaborate on why should doing so be a problem?The docs onPolicy Routinghave one of the callouts that say that:For a user-created table to be able to resolve the destination, the main routing table should be able to resolve the destination too.and in my experience that's accurate... ---

## Response 7
the main routing table should be able to resolve the destination too.Yup, but a default route inmainis sufficient to meet this requirement. ---

## Response 8
Your configuration export doesn't show any reason why 10.0.0.130 should use routing table main, however, as of current (7.16.x), there are issues with handling of the min-prefix value in configuration.Actually, my intention is only to let the device with IP 10.0.0.130 use the ecmp outgoing, while other devices use the default route.and do not modify the routing rules later - if you need to change something in a routing rule, add a new one before the one that needs change, and then remove the old one.I am not yet familiar with RouterOS scripts, and I tried running the code you provided in the terminal, but it failed. In the end, I manually added new routing rules and deleted the old ones.But it still cannot be routed correctly.1. Your pool isadd name=dhcp ranges=10.0.0.150-10.0.0.240Why is any device getting a LANIP of .130 ????Please check the beginning of this reply, and the IP address of the .130 device is manually set by me, not through DHCP.Thus, lets reflect your needs./ip routeadd dst-address=0.0.0.0/0 gateway=pppoe-out8 routing-table=main comment="Primary WAN3"add dst-address=0.0.0.0/0 gateway=pppoe-out1 routing-table=ecmpadd dst-address=0.0.0.0/0 gateway=pppoe-out2 routing-table=ecmpI have already done that.SECURITY PROBLEMAt that time, I completed the configuration by referring to this linkhttps://help.mikrotik.com/docs/spaces/R ... figuration, but I haven't confirmed the purpose of each item in detail. Since it is still in the development stage, it is not important for the time being. And I also clearly know that winbox cannot be exposed to the internet. If there are better security-related configurations, please provide them.ot have any forward chain rulesWill this cause my ecmp to not be able to take on traffic, for now I have all filter rules disabled to avoid problems due to filters. I will set it up again when my routing rules stabilize.6. Finally, WHY DO you not explain what the heck you are doing with the single IP address at the beginning??In the production environment, I may only have one to two devices that need to use the ecmp outgoing, and in my configuration, only one device is set to use the ecmp, which is .130.Both pppoe-out1 and pppoe-out2 are attached to macvlan interfacesYou are right, because I need to dial the same interface twice. And I might increase it to four dials, respectively on ether5 and ether6. And each dial cannot have the same MAC address. In the past, I would use vrrp, but later I learned about macvlan.For a user-created table to be able to resolve the destination, the main routing table should be able to resolve the destination too.I don't quite understand this sentence. I'll try to explain, meaning that if I create a command like`add disabled=yes distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out1 routing-table=ecmp`, do I have to create another one in the main routing table at the same time? ---

## Response 9
No worries, if macvlan works and is appropriate for your ISP setup.Fix the the routing rule and see what happens.Post config again after changes.Note the only change on routes is I added recursive but not necessary.also no need to make main route have distance anything but the default of 1. ---

## Response 10
Both pppoe-out1 and pppoe-out2 are attached to macvlan interfacesYou are right, because I need to dial the same interface twice.That's OK, I've even tested that if the pppoe interface is attached to a macvlan, the pppoe-discover frames are indeed sent via the physical interface with the source MAC address of the macvlan one, so all good here. But I have missed that ether5 was in factnotdisabled, so the whole conclusion was based on wrong input.So to start from somewhere, are the two routes in tableecmpshown as active? ---

## Response 11
You are right, because I need to dial the same interface twice.That's OK, I've even tested that if the pppoe interface is attached to a macvlan, the pppoe-discover frames are indeed sent via the physical interface with the source MAC address of the macvlan one, so all good here. But I have missed that ether5 was in factnotdisabled, so the whole conclusion was based on wrong input.So to start from somewhere, are the two routes in tableecmpshown as active?yes, all are in active status, and also show the ecmp [+] mark.But it still doesn't work, I'm not sure if it's affected by other configurations, but for policy routing, I only have the one strategy that we have discussed so far.Tomorrow, I plan to use another router, hAP ax3, to test it separately and see the results.
```
[user@MikroTik] /ip/route> print 
Flags: D - DYNAMIC; A - ACTIVE; c - CONNECT, s - STATIC; + - ECMP
Columns: DST-ADDRESS, GATEWAY, DISTANCE
#      DST-ADDRESS       GATEWAY        DISTANCE
0  As  0.0.0.0/0         pppoe-out8           10
  DAc  10.0.0.0/24       bonding1              0
  DAc  10.152.16.1/32    pppoe-out8            0
  DAc+ 113.x.x.1/32   pppoe-out1            0
  DAc+ 113.x.x.1/32   pppoe-out2            0
1  As+ 0.0.0.0/0         pppoe-out1            1
2  As+ 0.0.0.0/0         pppoe-out2            1

[user@MikroTik] /ip/route> /rou rule pr
Flags: X - disabled, I - inactive 
 0   src-address=10.0.0.130 action=lookup table=ecmp min-prefix=0And I would like to ask if there is any way to observe if a routing rule has been hit or not.For the firewall I can turn on logging to debug, but I can't see the routing rules.

---
```

## Response 12
I'm not sure if it's affected by other configurations, but for policy routing, I only have the one strategy that we have discussed so far.This remark makes me cautious, but I assume you haven't removed any mangle rules from the export before posting it? I cannot imagine anything else to have an impact.And I would like to ask if there is any way to observe if a routing rule has been hit or not.For the firewall I can turn on logging to debug, but I can't see the routing rules.Unfortunately, there isn't, neither logging nor packet&byte counters work for routes and routing rules. But that brings me to a question, how do you determine which path the packets from 10.0.0.130 actually take? By checking the public address using myip.wtf or a similar site, by sniffing traffic on the pppoe-out1 and pppoe-out2 interfaces, in some other way? ---

## Response 13
publish latest config/export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc. )Full config not what you think we need to see............ ---

## Response 14
This remark makes me cautious, but I assume you haven't removed any mangle rules from the export before posting it? I cannot imagine anything else to have an impact.publish latest configmy last configuration, I have only deleted a large number of/ip dhcp-server lease.
```
# 2024-12-08 16:11:04 by RouterOS 7.16.2
# software id = xxxx
#
# model = CCR1036-12G-4S
# serial number = xxxx
/interface ethernet
set [ find default-name=ether1 ] disabled=yes
set [ find default-name=ether2 ] disabled=yes
set [ find default-name=ether3 ] disabled=yes
set [ find default-name=ether4 ] disabled=yes
set [ find default-name=ether7 ] disabled=yes
set [ find default-name=ether8 ] disabled=yes
set [ find default-name=ether9 ] disabled=yes
set [ find default-name=ether10 ] disabled=yes
set [ find default-name=sfp3 ] disabled=yes
set [ find default-name=sfp4 ] disabled=yes
/interface bonding
add mode=802.3ad name=bonding1 slaves=ether11,ether12
/interface macvlan
add interface=ether5 mac-address=B2:54:05:89:BA:8B mode=private name=macvlan1
add interface=ether5 mac-address=F6:4F:AA:AD:82:B6 mode=private name=macvlan2
add interface=ether6 mac-address=42:DB:28:D3:57:FB mode=private name=macvlan3
add interface=ether6 mac-address=DE:E8:E3:5F:A8:00 mode=private name=macvlan4
/interface list
add name=WAN
add name=LAN
add name=LB
/interface list member
add interface=pppoe-out8 list=WAN
add interface=pppoe-out1 list=LB
add interface=pppoe-out2 list=LB
add interface=pppoe-out3 list=LB
add interface=pppoe-out4 list=LB
add interface=bonding1 list=LAN
add interface=sfp1 list=WAN
/interface pppoe-client
add disabled=no interface=sfp2 name=pppoe-out8 user=<username>
/interface pppoe-client
add disabled=no interface=macvlan1 name=pppoe-out1 user=<username>
add disabled=no interface=macvlan2 name=pppoe-out2 user=<username>
add interface=macvlan3 name=pppoe-out3 user=<username>
add interface=macvlan4 name=pppoe-out4 user=<username>
/ip dhcp-server option
add code=3 name="Surge Gateway" value="'10.0.0.100'"
add code=6 name="Surge DNS" value="'198.18.0.2'"
/ip dhcp-server option sets
add name=Surge options="Surge Gateway,Surge DNS"
/ip pool
add name=dhcp ranges=10.0.0.150-10.0.0.240
/ip dhcp-server
add address-pool=dhcp interface=bonding1 name=dhcp1
/port
set 0 name=serial0
set 1 name=serial1
/routing table
add disabled=no fib name=ecmp
add disabled=no fib name=CMIP_route
add disabled=no fib name=CT1
add disabled=no fib name=CT2
/ip settings
set ipv4-multipath-hash-policy=l4
/ip address
add address=10.0.0.1/24 comment=defconf interface=bonding1 network=10.0.0.0
add address=120.x.x.x/28 interface=sfp1 network=120.x.x.x
/ip dhcp-server network
add address=10.0.0.0/24 dns-server=119.29.29.29,223.5.5.5 gateway=10.0.0.1 \
    netmask=24
/ip dns
set servers=119.29.29.29,119.28.28.28,2402:4e00::,2402:4e00:1::
/ip firewall address-list
add address=10.0.0.100 comment="mac mini" disabled=yes list=CMIP
add address=10.0.0.8 comment=freepbx disabled=yes list=CMIP
add address=10.0.0.93 comment=ss list="PORT FORWARDING"
add address=10.0.0.94 comment=ss list="PORT FORWARDING"
/ip firewall filter   # all filter rules has been disabled
add action=accept chain=input comment="accept established,related,untracked" \
    connection-state=established,related,untracked disabled=yes
add action=drop chain=input comment="drop invalid" connection-state=invalid \
    disabled=yes
add action=accept chain=input comment="accept ICMP" disabled=yes \
    in-interface-list=WAN protocol=icmp
add action=drop chain=input comment="block everything else" disabled=yes \
    in-interface-list=WAN
/ip firewall mangle
add action=mark-connection chain=prerouting disabled=yes new-connection-mark=CMIP_conn passthrough=yes src-address-list=CMIP
add action=mark-routing chain=prerouting connection-mark=CMIP_conn disabled=yes new-routing-mark=CMIP_route passthrough=no src-address-list=CMIP
add action=mark-connection chain=prerouting comment="ss connection fallback" new-connection-mark=CMIP_conn passthrough=yes protocol=tcp src-address-list="PORT FORWARDING" src-port=23001,23002
add action=mark-routing chain=prerouting comment="ss connection fallback" connection-mark=CMIP_conn new-routing-mark=CMIP_route passthrough=no src-address-list="PORT FORWARDING"
add action=mark-connection chain=prerouting new-connection-mark=CT1_conn passthrough=yes src-address=10.0.0.93
add action=mark-routing chain=prerouting connection-mark=CT1_conn new-routing-mark=CT1 passthrough=no src-address=10.0.0.93
add action=mark-connection chain=prerouting new-connection-mark=CT2_conn passthrough=yes src-address=10.0.0.94
add action=mark-routing chain=prerouting connection-mark=CT2_conn new-routing-mark=CT2 passthrough=no src-address=10.0.0.94
/ip firewall nat
add action=dst-nat chain=dstnat comment="surge mac ponte" dst-address=120.x.x.x dst-port=6208 protocol=udp to-addresses=10.0.0.100 to-ports=6208
add action=dst-nat chain=dstnat comment=ss dst-address=120.x.x.x dst-port=23001 protocol=tcp to-addresses=10.0.0.93 to-ports=23001
add action=dst-nat chain=dstnat comment=ss dst-address=120.x.x.x dst-port=23002 protocol=tcp to-addresses=10.0.0.94 to-ports=23002
add action=dst-nat chain=dstnat comment=freepbx dst-address=120.x.x.x dst-port=10000-10100,5060 protocol=udp to-addresses=10.0.0.8
add action=dst-nat chain=dstnat comment=freepbx dst-address=120.x.x.x dst-port=5060 protocol=tcp to-addresses=10.0.0.8 to-ports=5060
add action=masquerade chain=srcnat out-interface-list=LB
add action=masquerade chain=srcnat out-interface-list=WAN
/ip route
add disabled=no distance=10 dst-address=0.0.0.0/0 gateway=pppoe-out8 routing-table=main scope=30 suppress-hw-offload=no target-scope=10
add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=120.x.x.x routing-table=CMIP_route scope=30 suppress-hw-offload=yes target-scope=10
add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out2 routing-table=CT2 scope=30 suppress-hw-offload=no target-scope=10
add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out1 routing-table=CT1 scope=30 suppress-hw-offload=no target-scope=10
add gateway=pppoe-out1 routing-table=ecmp
add gateway=pppoe-out2 routing-table=ecmp
/ip service
set telnet disabled=yes
set ftp disabled=yes
set ssh address=10.0.0.0/24
set api disabled=yes
set winbox address=10.0.0.0/24
set api-ssl disabled=yes
/ip ssh
set host-key-type=ed25519 strong-crypto=yes
/lcd
set enabled=no
/routing rule
add action=lookup min-prefix=0 src-address=10.0.0.130 table=ecmp
/system clock
set time-zone-name=Asia/Shanghai
/system logging
set 0 topics=info,!dhcp
/system note
set show-at-login=no
/system routerboard settings
set enter-setup-on=delete-key
/tool bandwidth-server
set enabled=no
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN
/tool sniffer
set filter-stream=yes streaming-enabled=yesBy checking the public address using myip.wtf or a similar site, by sniffing traffic on the pppoe-out1 and pppoe-out2 interfaces, in some other way?Yes, I also use a similar method, I executecurl ip.sbon a Linux system with the IP address 10.0.0.130, and the returned IP address is always the public IP address of pppoe-out8.

---
```

## Response 15
So you did filter out some of the configuration previously, but it was indeed unrelated, OK.First I would change theactionin the only routing rule fromlookuptolookup-only-in-tableand remove themin-prefixcompletely (but usingremoveandadd, for the reason explained before). If that changes nothing about the behavior, it means that the routing rule is ignored; if you stop getting any response, it means the rules are respected but the routing using tableecmpfails.If the routing rule is actually ignored, I'd remove it and try to use a mangle rule instead to achieve the same effect. Since ROS 7.6 or so, routing marks assigned by mangle rules have precedence over those assigned by routing rules, so removing the routing rule should be just an additional protection if they do act but in an unexpected way. ---

## Response 16
I tested again with a restored factory configured ax3 router and when I tried to configure one of the following two rules, neither could hit the ecmp routing table and all traffic went through the main table.
```
/routing rule
add action=lookup min-prefix=0 src-address=192.168.88.0/24 table=ecmp

/routing rule
add action=lookup min-prefix=0 src-address=192.168.88.252 table=ecmpThe full configuration is in the following:
```

```
# 2024-12-08 17:36:30 by RouterOS 7.16.1
# software id = xxxxxx
#
# model = C53UiG+5HPaxD2HPaxD
# serial number = xxxxxx
/disk
set usb1 media-interface=none media-sharing=no
/interface bridge
add admin-mac=D4:01:C3:44:04:3F auto-mac=no comment=defconf name=bridge
/interface wifi
set [ find default-name=wifi1 ] channel.skip-dfs-channels=10min-cac \
    configuration.mode=ap .ssid=MikroTik-440443 disabled=no \
    security.authentication-types=wpa2-psk,wpa3-psk .ft=yes .ft-over-ds=yes
set [ find default-name=wifi2 ] channel.skip-dfs-channels=10min-cac \
    configuration.mode=ap .ssid=MikroTik-440443 disabled=no \
    security.authentication-types=wpa2-psk,wpa3-psk .ft=yes .ft-over-ds=yes
/interface pppoe-client
add disabled=no interface=ether1 name=pppoe-out1 user=<user>
/interface macvlan
add interface=ether1 mac-address=DA:95:72:F9:87:12 mode=private name=macvlan1
/disk
set usb2 media-interface=bridge media-sharing=yes smb-sharing=yes smb-user=\
    guest
/interface pppoe-client
add disabled=no interface=macvlan1 name=pppoe-out2 user=<user>
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
/ip dhcp-server
add address-pool=default-dhcp interface=bridge name=defconf
/routing table
add disabled=no fib name=ecmp
/routing rule
add action=lookup min-prefix=0 src-address=192.168.88.0/24 table=ecmp
/zerotier
set zt1 comment="ZeroTier Central controller - https://my.zerotier.com/" \
    disabled=yes disabled=yes name=zt1 port=9993
/disk settings
set auto-media-interface=bridge auto-media-sharing=yes auto-smb-sharing=yes
/interface bridge port
add bridge=bridge comment=defconf interface=ether2
add bridge=bridge comment=defconf interface=ether3
add bridge=bridge comment=defconf interface=ether4
add bridge=bridge comment=defconf interface=ether5
add bridge=bridge comment=defconf interface=wifi1
add bridge=bridge comment=defconf interface=wifi2
/ip neighbor discovery-settings
set discover-interface-list=LAN
/ip settings
set ipv4-multipath-hash-policy=l4
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=ether1 list=WAN
add interface=pppoe-out1 list=WAN
add interface=pppoe-out2 list=WAN
/ip address
add address=192.168.88.1/24 comment=defconf interface=bridge network=\
    192.168.88.0
/ip dhcp-client
add comment=defconf disabled=yes interface=ether1
/ip dhcp-server network
add address=192.168.88.0/24 comment=defconf dns-server=192.168.88.1 gateway=\
    192.168.88.1
/ip dns
set allow-remote-requests=yes servers=119.29.29.29,223.5.5.5
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
/ip firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment=\
    "defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=drop chain=input comment="defconf: drop all not coming from LAN" \
    in-interface-list=!LAN
add action=accept chain=forward comment="defconf: accept in ipsec policy" \
    ipsec-policy=in,ipsec
add action=accept chain=forward comment="defconf: accept out ipsec policy" \
    ipsec-policy=out,ipsec
add action=fasttrack-connection chain=forward comment="defconf: fasttrack" \
    connection-state=established,related hw-offload=yes
add action=accept chain=forward comment=\
    "defconf: accept established,related, untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \
    connection-state=new in-interface-list=WAN
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=dst-nat chain=dstnat comment=ss dst-port=23001 in-interface-list=\
    WAN protocol=tcp to-addresses=192.168.88.10 to-ports=23001
/ip route
add disabled=no dst-address=0.0.0.0/0 gateway=pppoe-out1 routing-table=ecmp \
    suppress-hw-offload=no
add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out2 \
    routing-table=ecmp scope=30 suppress-hw-offload=no target-scope=10
add disabled=no distance=10 dst-address=0.0.0.0/0 gateway=pppoe-out1 \
    routing-table=main scope=30 suppress-hw-offload=no target-scope=10
/ip upnp
set enabled=yes
/ip upnp interfaces
add interface=bridge type=internal
add interface=pppoe-out1 type=external
/ipv6 firewall address-list
add address=::/128 comment="defconf: unspecified address" list=bad_ipv6
add address=::1/128 comment="defconf: lo" list=bad_ipv6
add address=fec0::/10 comment="defconf: site-local" list=bad_ipv6
add address=::ffff:0.0.0.0/96 comment="defconf: ipv4-mapped" list=bad_ipv6
add address=::/96 comment="defconf: ipv4 compat" list=bad_ipv6
add address=100::/64 comment="defconf: discard only " list=bad_ipv6
add address=2001:db8::/32 comment="defconf: documentation" list=bad_ipv6
add address=2001:10::/28 comment="defconf: ORCHID" list=bad_ipv6
add address=3ffe::/16 comment="defconf: 6bone" list=bad_ipv6
/ipv6 firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=input comment="defconf: accept UDP traceroute" \
    dst-port=33434-33534 protocol=udp
add action=accept chain=input comment=\
    "defconf: accept DHCPv6-Client prefix delegation." dst-port=546 protocol=\
    udp src-address=fe80::/10
add action=accept chain=input comment="defconf: accept IKE" dst-port=500,4500 \
    protocol=udp
add action=accept chain=input comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=input comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=input comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=input comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
add action=accept chain=forward comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop packets with bad src ipv6" src-address-list=bad_ipv6
add action=drop chain=forward comment=\
    "defconf: drop packets with bad dst ipv6" dst-address-list=bad_ipv6
add action=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1" \
    hop-limit=equal:1 protocol=icmpv6
add action=accept chain=forward comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=forward comment="defconf: accept HIP" protocol=139
add action=accept chain=forward comment="defconf: accept IKE" dst-port=\
    500,4500 protocol=udp
add action=accept chain=forward comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=forward comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=forward comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=forward comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
/system clock
set time-zone-name=Asia/Shanghai
/system note
set show-at-login=no
/system routerboard mode-button
set enabled=yes on-event=dark-mode
/system routerboard wps-button
set enabled=yes on-event=wps-accept
/system script
add comment=defconf dont-require-permissions=no name=dark-mode owner=*sys \
    policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    source="\r\
    \n   :if ([system leds settings get all-leds-off] = \"never\") do={\r\
    \n     /system leds settings set all-leds-off=immediate \r\
    \n   } else={\r\
    \n     /system leds settings set all-leds-off=never \r\
    \n   }\r\
    \n "
add comment=defconf dont-require-permissions=no name=wps-accept owner=*sys \
    policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    source="\r\
    \n   :foreach iface in=[/interface/wifi find where (configuration.mode=\"a\
    p\" && disabled=no)] do={\r\
    \n     /interface/wifi wps-push-button \$iface;}\r\
    \n "
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN

---
```

## Response 17
First I would change the action in the only routing rule from lookup to lookup-only-in-table and remove the min-prefix completelyAs you said on ax3, when I deleted all the routing rules and did not usemin-prefix, ecmp took effect immediately, but it also prevented me from logging into winbox again.Because I usedsrc-address=192.168.88.0/24But why does ecmp not work when I use mini-prefix, and I cannot access the 192.168.88.0/24 subnet, even the gateway times out, when I do not use mini-prefix.Next, I will test it on ccr1036.Edit: I think the ecmp has been work. ---

## Response 18
I'd remove it and try to use a mangle rule instead to achieve the same effect.I have a question, now it seems that ecmp is already working.When I use routing rules for routing, will it be more CPU resource-saving than using mangle? Because when I used mangle with pcc before, if the PT client was downloading, the speed would not reach full capacity, and it seems that the firewall is only using one CPU core to process the mangle rules. And I also saw an option in/routing/settingwhether to enable single process. ---

## Response 19
So it was a configuration after all. Whatmin-prefixactually does is that it takes a look which route in the indicated table would be used for the packet, and if the length of thedst-addressprefix of that route is smaller than or equal to themin-prefixvalue, the rule returns a non-match so the packet processing commences to the next rule. So you have used it in a reverse way, it should have said instead:/routing/ruleadd min-prefix=0 action=lookup table=mainadd src-address=10.0.0.130 action=lookup-only-in-table table=ecmpTry this pair of routing rules instead of the mangle rule, please. ---

## Response 20
For anyone later that follows this thread;;;;;;;In this case since there is only one subnet and the prefix rule is basically doing the equivalent to:/routiing ruleadd action=lookup-only-in-table src-address=192.168.88.0/24 dst-address=192.168.88.0/24 table=mainThe value in using the min-prefix=0 is that it allows any local subnet to subnet traffic to occur ( from or to source address )++++++++++Without any variation of the above rules, such traffic originating from source or responding from source goes out the next "force traffic to somewhere" routing rule.So the variation is required prior to the force rule. ---

## Response 21
Sorry @anav, but your wording is so advanced that it is confusing even for me, although I know what you actually intended to say.So let me try myself in a simpler language with more details: In most cases, we need to prevent the traffic towards local destinations from using other routing table thanmain. Until recently, the only way to do that using routing rules alone was to put (one or several) rules withdst-addressmatching the local subnets withaction=lookup table=mainbefore (above) the rule that matched onsrc-addressand/orinterfaceandaction=lookup-only-in-tabletable=something-else-than-main. So traffic towards local destinations never reached the rule telling it to use another routing table.The value of themin-prefixattribute is that it allows to use just a single rule for the same purpose, which is universal in terms that you do not need to specify thedst-addressto match to manually; instead, it uses thedst-addressof the existing routes in the routing table, taking their prefix length (a.k.a. subnet mask) into account.As an example, let routing tablemaincontain one default route provided by a DHCP client and three routes to "connected subnets":dst-address, gateway, distance0.0.0.0/0, 10.0.0.1, 1192.168.88.0/24, bridge1, 0192.168.44.0/24, bridge2, 010.11.0.0/22, bridge3, 0To make sure that traffic towards any of these three local subnets will be routed using tablemain, we need three rules:dst-address=192.168.88.0/24 action=lookup table=maindst-address=192.168.44.0/24 action=lookup table=maindst-address=10.11.0.0/22 action=lookup table=mainIf it is OK to usemainfor all private destinations, this can be reduced to just two rules:dst-address=192.168.0.0/16 action=lookup table=maindst-address=10.0.0.0/8 action=lookup table=mainBut withmin-prefix, a single rule is sufficient:min-prefix=0 action=lookup table=mainIt will look into tablemain, find the best matching route for the packet being processed, and if the prefix length (subnet mask) of thedst-addressof that route is higher than themin-prefixvalue, it will tell the routing to use that routing table for the packet; otherwise, it will hand the packet over to the next routing rule as if it did not match it. ---

## Response 22
Better with recursive checking of connectivity/ip routeadd dst-address=0.0.0.0/0 gateway=pppoe-out8 routing-table=main comment="Primary WAN3"add check-gateway=ping dst-address=0.0.0.0/0 gateway=1.1.1.1 routing-table=ecmp scope=10 target-scope=12 comment=ISP1add check-gateway=ping dst-address=0.0.0.0/0 gateway=9.9.9.9 routing-table=ecmp scope=10 target-scope=12 comment=ISP2add dst-address=1.1.1.1/32 gateway=pppoe-out1 routing-table=ecmp scope=10 target-scope=11add dst-address=9.9.9.9/32 gateway=pppoe-out2 routing-table=ecmp scope=10 target-scope=11After ECMP becomes working, I am considering how to configure failover. Here is my config(bold part is the main section):/ip routeadd disabled=yes distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out8 routing-table=main scope=30 suppress-hw-offload=no target-scope=10add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=120.x.x.x routing-table=cmip_route scope=30 suppress-hw-offload=no target-scope=10add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out2 routing-table=ct2 scope=30 suppress-hw-offload=no target-scope=10add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out1 routing-table=ct1 scope=30 suppress-hw-offload=no target-scope=10add gateway=pppoe-out1 routing-table=ecmpadd gateway=pppoe-out2 routing-table=ecmpadd disabled=no distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out3 routing-table=ecmp scope=30 suppress-hw-offload=no target-scope=10add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=pppoe-out4 routing-table=ecmp scope=30 suppress-hw-offload=no target-scope=10add disabled=no distance=1 dst-address=119.29.29.29/32 gateway=pppoe-out8 routing-table=main scope=10 suppress-hw-offload=no target-scope=10add disabled=no distance=1 dst-address=119.28.28.28/32 gateway=pppoe-out1 routing-table=main scope=10 suppress-hw-offload=no target-scope=10add check-gateway=ping distance=1 gateway=119.29.29.29 target-scope=11add check-gateway=ping distance=2 gateway=119.28.28.28 target-scope=11And you mentioned what the addition of recursive checking of connectivity on ecmp does? Why do all people have to plus one to target-scope when using recursive routing?Finally I have a requirement that I don't know if I can implement, currently my configuration failover will transfer all traffic to pppoe-out1 but I would like to transfer it directly to ECMP's load balancing instead of taking over all traffic through pppoe-out1 alone, after pppoe-out8 fails.Another ROS issue I don't understand is why the two things/routing/rulesand/ip/routewere separated after the 7.x release. ---

## Response 23
Slow down, manLeaving aside that the topic title has become totally misleading already long ago, and that you have changed the objective all of a sudden, your bold rules are either incomplete or incorrect.The whole idea of using the recursive next-hop search to monitor route transparency is to prevent the router from sending traffic via faulty routes. So if the goal is to use the route viapppoe-out8as long as it works, and if that one has a problem, to evenly distribute the traffic among all the functional pppoe-out1 to pppoe-out4 routes using ECMP, you must monitor all those routes individually. So the overall setup would bedst-address=ca.na.ry.1/32 gateway=pppoe-out1dst-address=ca.na.ry.2/32 gateway=pppoe-out2dst-address=ca.na.ry.3/32 gateway=pppoe-out3dst-address=ca.na.ry.4/32 gateway=pppoe-out4dst-address=ca.na.ry.8/32 gateway=pppoe-out8dst-address=0.0.0.0/0 gateway=ca.na.ry.8 distance=1check-gateway=ping target-scope=11dst-address=0.0.0.0/0 gateway=ca.na.ry.1 distance=2check-gateway=ping target-scope=11dst-address=0.0.0.0/0 gateway=ca.na.ry.2 distance=2check-gateway=ping target-scope=11dst-address=0.0.0.0/0 gateway=ca.na.ry.3 distance=2check-gateway=ping target-scope=11dst-address=0.0.0.0/0 gateway=ca.na.ry.4 distance=2check-gateway=ping target-scope=11ca.na.ry.Xmust be a unique address for each WAN. ---

## Response 24
Also its nice to tells us different requirements, but if you dont post the most update config, we have no idea where things are at.Thus everytime you make changes post the new config/export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc..)Also state all the requirements (the whole plan) as opposed to bits and pieces. ---

## Response 25
@sindy @anavFirst of all, thank you very much for your help.I am in the process of refining my configuration, when I will post a new topic and describe my configuration and my corresponding needs.I hope I can get your guidance to make my configuration more robust. ---

## Response 26
@Amm0, Yup, but a default route inmainis sufficient to meet this requirement.Also, I'm pretty sure that statement in the documentation is a simplification the author has used to avoid the need to explain that this requirement (for some route to exist inmain) is only related to own outgoing traffic of the router, which indeed has to be routed using tablemainfirst, in order to ever get to mangle and eventually hit a rule there that tells it to run through routing again, using some other routing table this time. ---

## Response 27
@Amm0, Yup, but a default route inmainis sufficient to meet this requirement.Also, I'm pretty sure that statement in the documentation is a simplification the author has used to avoid the need to explain that this requirement (for some route to exist inmain) is only related to own outgoing traffic of the router, which indeed has to be routed using tablemainfirst, in order to ever get to mangle and eventually hit a rule there that tells it to run through routing again, using some other routing table this time.I haven't looked at this recently...so pretty sure you're right. Now I do want to say I got invalid routes in some past V7 RouterOS versions with the rule was violated...My usual setup is failover in main (distance=1...x, with some combo of 0-2x "ethernet" WAN + 1-2x LTE links), using routing table per WAN plus an "ecmp" route table as here. So it doesn't come up in practice, since all WANs are in main routing table. Also LTE is an interface route, that might affect the logic too, IDK. I'll run a test since you have me curious on exactly what works here. ---

## Response 28
Interesting, ECMP sure is much less complex in terms of sharing the load in case one of the WANs is not available.In load balancing, it can turn into a huge nightmare of extra mangles and routes.I am not convinced your recursive is correct I would do it this way.dst-address=0.0.0.0/0 gateway=ca.na.ry.8 distance=1 check-gateway=ping scope=10 target-scope=12 comment=WAN08dst-address=0.0.0.0/0 gateway=ca.na.ry.1 distance=2 check-gateway=ping scope=10 target-scope=12dst-address=0.0.0.0/0 gateway=ca.na.ry.2 distance=2 check-gateway=ping scope=10 target-scope=12dst-address=0.0.0.0/0 gateway=ca.na.ry.3 distance=2 check-gateway=ping scope=10 target-scope=12dst-address=0.0.0.0/0 gateway=ca.na.ry.4 distance=2 check-gateway=ping scope=10 target-scope=12++++++++++++++++++++++++++++++++dst-address=ca.na.ry.8/32 gateway=pppoe-out8 distance=1 scope=10 target-scope=11dst-address=ca.na.ry.1/32 gateway=pppoe-out1 distance=2 scope=10 target-scope=11dst-address=ca.na.ry.2/32 gateway=pppoe-out2 distance=2 scope=10 target-scope=11dst-address=ca.na.ry.3/32 gateway=pppoe-out3 distance=2 scope=10 target-scope=11dst-address=ca.na.ry.4/32 gateway=pppoe-out4 distance=2 scope=10 target-scope=11I do appreciate the detail in ca.na.ry.x though. ---