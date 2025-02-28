# Thread Information
Title: Thread-1119165
Section: RouterOS
Thread ID: 1119165

# Discussion

## Initial Question
We have a disaster - we basically just changed our firewall to a Mikrotik CCR1009-8G-1S-1S+ currently running 7.16.1 *tonight we we'll upgrade to 7.16.2 but the notes don't suggest that it will fix it. Short of going back to our old firewall - we'd prefer to get the Mikrotik working.Its as if there's a limit on connections and sessions and so when that limit is being reached the connection is being dropped.Or the high outbound ports numbers are restricted or limited or something.The IssueRandomly the Mikrotik will drop the RDP connection - this is something in the order of several times a day all day per person but its disconnecting someone every several minutes just choosing different users. The user then see's a black screen, reconnecting and then gets in for about several hours until its their turn. Only using TCP for my RDP. Its across older servers 2012r2 and newer server Windows 2019The Windows servers reports "Session XX has been disconnected, reason code 0"My NetworkWe have several public IP address's on one WAN port. We have several inbound RDP servers on different Public IP.We cant use VPN to our customers.So therefore there is a DSTNAT rule to link the Public IP address to the private server via the port.add action=dst-nat chain=dstnat comment=" (Rule 249) " \dst-address=PublicAddress.01 dst-port=3389 in-interface=sfp1 log=yes \log-prefix=RULE249 protocol=tcp src-address-list=SAFELIST \to-addresses=192.168.200.64 to-ports=3389As i want to also want to have traffic that's leaving that server to be coming from its own public IP - i also have a SCRNAT.add action=src-nat chain=srcnat comment= "(Rule 249)" out-interface=sfp1 \src-address=192.168.200.64 to-addresses=PublicAddress.01Also have a forwarding ruleadd action=accept chain=forward comment="(Rule 249)" dst-address=\192.168.200.64 dst-port=3389 in-interface=sfp1 log-prefix=\"Default Internet DNS" protocol=tcpEach server are setup the same way on different IP.So Ive looked at the timeouts and increased themenabled: autoactive-ipv4: yesactive-ipv6: notcp-syn-sent-timeout: 30stcp-syn-received-timeout: 30stcp-established-timeout: 1dtcp-fin-wait-timeout: 10stcp-close-wait-timeout: 10stcp-last-ack-timeout: 10stcp-time-wait-timeout: 10stcp-close-timeout: 10stcp-max-retrans-timeout: 5mtcp-unacked-timeout: 5mloose-tcp-tracking: yesudp-timeout: 20sudp-stream-timeout: 3micmp-timeout: 10sgeneric-timeout: 10mmax-entries: 1048576total-entries: 3179I have "block invalid forward traffic" was being fired some traffic on other servers - anyway I've change block to logSo there could be something this - maybe. Here's the rule anyway.add action=drop chain=forward comment="Drop invalid connections" \connection-state=invalid log=yes log-prefix="Drop invalid"The client also has a Mikrotik- thats been there for ever - its only on our side that's been changed.Basically getting a whole bunch of upset usersPS: Many thanks in advance your help ---

## Response 1
I would perhaps actively block udp to and from 3389, (if only to see if it changes anything) ---

## Response 2
Hi there!Some notes -The "error code 0" is the generic "there is an error somewhere", aka "Microsoft useful."1. Can you permit both tcp/3389 and udp/3389? RDP tries to use UDP to stream more efficiently. Add a second rule both for the DST NAT and FILTER to permit that from the safe sources.2. If not present, create a NAT and FILTER rules to permit ICMP/ECHO from the safe list to the RDP server. In case of issues, you can ask the user to ping the server.There may be additional considerations though - what was the old firewall? What type of internet uplink do you have? ---

## Response 3
Also, can you share your config with the sensitive bits removed? ---

## Response 4
Let me start many thanks - lots of pressure over here.@rplant UDP is blocked and never was opened - ie: including on the previous firewall - which was Securepoint.@vingjfg - the entire setup that means the GPO all setup to only work on TCP - for years (like over 15years) - that includes the workstations.Its been flawless. The MT does some things that Securepoint doesnt and we cant buy the new version in Australia.There's no ping drop outs. Both ends have business grade quality internet fibre - even on the MT interface status shows there's no errors and more than 500GB of traffic has passed through in 2.5 weeks. The router capacity shows its not even breaking a sweat.The uplink is 700Mbps and the RDP traffic barely hits 30Mbps - so not bandwidth or jitter issues.Its as if the data stream changes the TCP the port mid session say via NAT.Or it drops the port and so the RDP servers disconnect the user. Its not a Microsoft issue.Can that happen? Can it re-organise or change an open TCP NAT or DNAT port mid way?We did put in a wireguard VPN and we dont see the disconnections although we arent always in the RDP - again pushing me to a DNAT, NAT issue.In the old days we could specify a limit on amount of port we couldThe config - cut down to only the RDP servers and rules around it.
```
/interfacebridgeaddcomment="DMZ Zone"name=bridge1/interfaceethernetset[finddefault-name=ether1]disabled=yesset[finddefault-name=ether2]comment="SWITCH"set[finddefault-name=ether3]comment="SWITCH"set[finddefault-name=ether4]comment="SWITCH"set[finddefault-name=ether5]disabled=yesset[finddefault-name=ether7]disabled=yesset[finddefault-name=ether8]disabled=yesset[finddefault-name=sfp1]auto-negotiation=nocomment=\"INTERNET"#ignore the VPN/interfacewireguardaddlisten-port=13231mtu=1420name=WG_Interface/interfacelistaddname=WANaddname=LAN/interfacelte apnset[finddefault=yes]ip-type=ipv4use-network-apn=no/ip pooladdcomment="DMZ DHCP Pool"name=DMZ-POOL ranges=\192.168.0.241-192.168.0.254/ip dhcp-serveraddaddress-pool=DMZ-POOL bootp-support=noneinterface=bridge1 lease-time=\2h30mname=FW-DHCP/portset0name=serial0set1name=serial1/ppp profileaddname=profileuse-compression=yesuse-ipv6=no/queue simpleaddcomment="TOTAL INTERNET SPEED"disabled=yes max-limit=400M/1Gname=\"ALL BANDWIDTH"target=sfp1addmax-limit=10M/10Mname="techsupport"target=MyOfficeIPaddcomment="Protect DMZ traffic back to customer"max-limit=20M/20Mname=\
    DC_DMZ_ACCESS target=OtherCustomerIPaddcomment="10MBPS/10MBPS Webservers"max-limit=10M/10Mname=WEBSERVERS \
    target=192.168.0.21/32addcomment="20MBPS/20MBPS RULE19"dst=sfp1 max-limit=20M/20Mname=20MBPS\
    target=192.168.0.170/32addmax-limit=10M/10Mname=SMTP-INBOUND target=192.168.0.176/32adddisabled=yes name=TERMINAL parent="ALL BANDWIDTH"priority=2/2target=\192.168.0.148/32/queue typeaddkind=fq-codel name=fq_codel/queue simpleaddbucket-size=0.005/0.005comment="Buffer Bloat Testing"disabled=yes \
    max-limit=400M/1Gname=FQ_CODEL-QOS priority=1/1queue=fq_codel/fq_codel \
    target=sfp1 total-queue=fq_codel/interfacebridge portaddbridge=bridge1 comment="SWITCH"interface=ether2addbridge=bridge1 comment="SWITCH"interface=ether3addbridge=bridge1 comment="SWITCH"interface=ether4addbridge=bridge1 disabled=yesinterface=ether5addbridge=bridge1 disabled=yesinterface=ether6addbridge=bridge1 disabled=yesinterface=ether7addbridge=bridge1 disabled=yesinterface=ether8addbridge=bridge1 disabled=yesinterface=ether1/ip firewall connection trackingsettcp-syn-received-timeout=30stcp-syn-sent-timeout=30sudp-timeout=20s/ip settingssetmax-neighbor-entries=8192/ipv6 settingssetdisable-ipv6=yes max-neighbor-entries=8192/interfacedetect-internetsetdetect-interface-list=WAN internet-interface-list=WAN lan-interface-list=\
    LAN wan-interface-list=WAN/interfacel2tp-server serversetaccept-proto-version=l2tpv2 allow-fast-path=yesdefault-profile=default/interfacelist memberaddinterface=bridge1 list=LANaddinterface=sfp1 list=WAN/interfaceovpn-server serversetauth=sha1,md5/interfacewireguard peersaddallowed-address=etc etc/ip addressaddaddress=192.168.0.1/24comment=Networkinterface=bridge1 network=\192.168.0.0addaddress=200.200.200.30/27comment="INTERNET CONNECTION"interface=sfp1 \
    network=200.200.200.28addaddress=200.200.200.31/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.32/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.33/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.34/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.35/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.36/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.37/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.38/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.39/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.40/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.41/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.42/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.43/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.44/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.45/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.46/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.47/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.48/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.49/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.50/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.51/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.52/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.53/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.54/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.55/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.56/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.57/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.58/27interface=sfp1 network=200.200.200.28#Wireguard stuffaddaddress=192.168.1.1/24interface=WG_Interface network=192.168.1.0/ip dhcp-clientadddisabled=yesinterface=sfp-sfpplus1/ip dhcp-server networkaddaddress=192.168.0.0/24dns-server=192.168.0.23,192.168.0.22domain=\
    domain.localgateway=192.168.0.1netmask=24ntp-server=\192.168.0.76/ip dnssetservers=192.168.0.22/ip firewall address-listaddaddress=0.0.0.0/8comment=RFC6890 list=not_in_internetaddaddress=172.16.0.0/12comment=RFC6890 list=not_in_internetaddaddress=192.168.0.0/16comment=RFC6890 list=not_in_internetaddaddress=10.0.0.0/8comment=RFC6890 list=not_in_internetaddaddress=169.254.0.0/16comment=RFC6890 list=not_in_internetaddaddress=127.0.0.0/8comment=RFC6890 list=not_in_internetaddaddress=224.0.0.0/4comment=Multicastlist=not_in_internetaddaddress=198.18.0.0/15comment=RFC6890 list=not_in_internetaddaddress=192.0.0.0/24comment=RFC6890 list=not_in_internetaddaddress=192.0.2.0/24comment=RFC6890 list=not_in_internetaddaddress=198.51.100.0/24comment=RFC6890 list=not_in_internetaddaddress=203.0.113.0/24comment=RFC6890 list=not_in_internetaddaddress=100.64.0.0/10comment=RFC6890 list=not_in_internetaddaddress=240.0.0.0/4comment=RFC6890 list=not_in_internetaddaddress=192.88.99.0/24comment="6to4 relay Anycast [RFC 3068]"list=\
    not_in_internetaddaddress=MyofficePubliclist=techsupport#the RDP serversaddaddress=192.168.0.148comment=SERVER03 list=TERMINALSERVICESaddaddress=192.168.0.120comment=SERVER07 list=TERMINALSERVICESaddaddress=192.168.0.164comment=SERVER12 list=TERMINALSERVICESaddaddress=192.168.0.188comment=SERVER25 list=TERMINALSERVICES

etc
etc/ip firewall filteraddaction=fasttrack-connection chain=forward comment=\"fasttrack - disables QUEUES bandwidth"connection-state=\
    established,related hw-offload=yesaddaction=accept chain=forward comment="=====established, related"\
    connection-state=established,related log-prefix="RULE 60 Establish"#disabled at the momentaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=add-src-to-address-list address-list=PortScanDetected\
    address-list-timeout=none-dynamicchain=input comment="Port Scan Detect"\in-interface=sfp1 log=yes log-prefix="Port Scan Detect"protocol=tcp psd=\21,3s,3,1addaction=drop chain=input comment="Black List Attackers"in-interface=sfp1 \
    src-address-list=black_listaddaction=drop chain=input comment="Block PortScanners"in-interface=sfp1 \
    src-address-list=PortScanDetectedaddaction=accept chain=input comment="dont allow pings"in-interface=sfp1 \
    limit=50,2:packet protocol=icmp src-address=networkmonitoringaddressaddaction=drop chain=input comment="dont allow pings"in-interface=sfp1 \
    limit=50,2:packet log-prefix="IMCP Rule20"protocol=icmpaddaction=accept chain=input comment="lan access to router"disabled=yes \in-interface-list=LAN src-address-list=LANaddaction=accept chain=input comment="lan access to router"disabled=yesaddaction=drop chain=input comment=\"drop everything else - including firmware upgrade"in-interface-list=\!LAN log-prefix="Rule 22 !LAN"addaction=drop chain=forward comment="Drop invalid connections"\
    connection-state=invalid log=yes log-prefix="Drop invalid"addaction=accept chain=forward comment="Inbound RULE23"dst-address=\192.168.0.180dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcp src-address-list=TS_Whitelistaddaction=accept chain=forward comment="Inbound RULE25"dst-address=\192.168.0.188dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcp src-address-list=TS_Whitelistaddaction=accept chain=forward comment="Inbound RULE07"dst-address=\192.168.0.120dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcp src-address-list=TS_Whitelistaddaction=accept chain=forward comment="Inbound RULE25"dst-address=\192.168.0.188dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound RULE23"dst-address=\192.168.0.180dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound RULE07"dst-address=\192.168.0.120dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound RULE03"dst-address=\192.168.0.148dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound RULE12"dst-address=\192.168.0.164dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound RULE24"dst-address=\192.168.0.198dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment=\"Rule 210 - default Internet browsing"dst-port=80,443,25,53,21\out-interface=sfp1 protocol=tcp src-address-list=TERMINALSERVICESaddaction=drop chain=forward comment="=====Black List Attackers"\
    src-address-list=black_listaddaddaction=accept chain=forward comment="Default forwarding rule (DISABLE)"\
    disabled=yes log=yes log-prefix="Rule 51 LAN"src-address-list=LANaddaction=drop chain=forward comment=\"drop tries to reach not public addresses from LAN"dst-address-list=\
    not_in_internetin-interface-list=LAN log-prefix=\"!public_from_LAN Rule 58"out-interface-list=!LANaddaction=drop chain=forward comment=\"drop incoming packets that are not NAT`ted"connection-nat-state=!dstnat \
    connection-state=newdisabled=yesin-interface-list=WAN log-prefix=\"!NAT Rule 59"addaction=drop chain=forward comment=\"drop incoming from internet which is not public IP"disabled=yes \in-interface-list=WAN log-prefix="!public Rule 60"src-address-list=\
    not_in_internetaddaction=drop chain=forward comment=\"drop packets from LAN that do not have LAN IP"in-interface-list=LAN \
    log-prefix="DROP LAN_!LAN Rule 70"src-address=!192.168.0.0/24addaction=drop chain=forward comment="drop all else"log-prefix=\"DROP_ALL Rule 71"/ip firewall nataddaction=src-nat chain=srcnat comment=SERVER19 log-prefix=\"dnat RULE19"out-interface=sfp1 src-address=192.168.0.170\
    to-addresses=200.200.200.33addaction=src-nat chain=srcnat comment=SERVER07out-interface=sfp1 \
    src-address=192.168.0.120to-addresses=200.200.200.37addaction=src-nat chain=srcnat comment=SERVER03out-interface=sfp1 \
    src-address=192.168.0.148to-addresses=200.200.200.34addaction=src-nat chain=srcnat comment=SERVER25out-interface=sfp1 \
    src-address=192.168.0.188to-addresses=200.200.200.41addaction=src-nat chain=srcnat comment=SERVER12out-interface=sfp1 \
    src-address=192.168.0.164to-addresses=200.200.200.40addaction=masquerade chain=srcnat comment="General DMZ Internet Access"\
    log-prefix=MASQUERADEout-interface-list=WAN src-address-list=LANaddaction=dst-nat chain=dstnat comment="SERVER03 (Rule 249) "\
    dst-address=200.200.200.34dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=CountryIPAustraliato-addresses=192.168.0.148\
    to-ports=3389addaction=dst-nat chain=dstnat comment="SERVER07 (Rule 249) "\
    dst-address=200.200.200.37dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=CountryIPAustraliato-addresses=192.168.0.120\
    to-ports=3389addaction=dst-nat chain=dstnat comment="SERVER12 (Rule 249) "\
    dst-address=200.200.200.40dst-port=3389in-interface=sfp1 log=yes \
    log-prefix=RULE12 protocol=tcp src-address-list=CountryIPAustralia\
    to-addresses=192.168.0.164to-ports=3389addaction=dst-nat chain=dstnat comment="SERVER12 (Rule 249) "\
    dst-address=200.200.200.40dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=TS_Whitelist to-addresses=192.168.0.164to-ports=3389addaction=dst-nat chain=dstnat comment="SERVER25 (Rule 249) "\
    dst-address=200.200.200.41dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=CountryIPAustraliato-addresses=192.168.0.188\
    to-ports=3389addaction=dst-nat chain=dstnat comment="SERVER23 (Rule 249) "\
    dst-address=200.200.200.38dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=CountryIPAustraliato-addresses=192.168.0.180\
    to-ports=3389addaction=dst-nat chain=dstnat comment=SERVER24 dst-address=200.200.200.42\
    dst-port=3389in-interface=sfp1 protocol=tcp src-address-list=\CountryIPAustraliato-addresses=192.168.0.198to-ports=3389addaction=dst-nat chain=dstnat comment="SERVER23 (Rule 249) "\
    dst-address=200.200.200.38dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=TS_Whitelist to-addresses=192.168.0.180to-ports=3389addaction=dst-nat chain=dstnat comment="SERVER25 (Rule 249) "\
    dst-address=200.200.200.41dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=TS_Whitelist to-addresses=192.168.0.188to-ports=3389/ip firewall service-portsetftp disabled=yessettftp disabled=yesseth323 disabled=yessetsip disabled=yessetpptp disabled=yes/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/lcdsetenabled=notouch-screen=disabled/routing bfd configurationadddisabled=nointerfaces=all min-rx=200msmin-tx=200msmultiplier=5

---
```

## Response 5
re: : 2. If not present, create a NAT and FILTER rules to permit ICMP/ECHO from the safe list to the RDP server. In case of issues, you can ask the user to ping the server.There are 20 users from one location connecting to the RDP server - meaning if it was network issue we'd expect that all the users would all experience the disconnect at the same time.Its "randomly" disconnecting users - i dont have the data on when some connected vs when they've disconnected to see if there's a pattern.So its looks like this[ 20 users ] -> MT (Nat) -> internet (tcp 3389) -> MT (new firewall) -> [ RDP server ] ---

## Response 6
It doesn't necessarily have to be the router that's the main problem. A tip is to troubleshoot using the Windows Event Log on both the RDP clients and the server. A good place to start is the guide "Microsoft - Troubleshoot Remote Desktop Disconnected Errors".This might also be useful: "Gather information by using TSS for user experience-related issues (remote-desktop-disconnection)" ---

## Response 7
The configuration refers to a PPP profile, is this something else? Or are you using PPPoE? The configuration refers to sfp1 and at places to the WAN interface list - can this be standardized to the interface list wherever possible, at least in all the ip firewall sections?In your configuration (consider using the code tag next time), I see you do the NAT by creating additional IP addresses on the interface. Nothing wrong with that, keep in mind that everything that is not natted hits the firewall itself. For example, while you DSTNAt tcp/3389, ping to the same public IP would go to the firewall. I strongly suggest adding a rule to DSTNAT to the servers for icmp (from the same sources if you want), for the sake of pmtu discovery.I saw a few things that are probably mistakes
```
addaction=accept chain=forward comment="=====established, related"\
connection-state=established,related log-prefix="RULE 60 Establish"This is going to log every single packet in an established connection, unless it is caught by the fasttrack rule above. Not something you want to do.
```

```
addaction=accept chain=input comment="dont allow pings"in-interface=sfp1 \
limit=50,2:packet protocol=icmp src-address=networkmonitoringaddressaddaction=drop chain=input comment="dont allow pings"in-interface=sfp1 \
limit=50,2:packet log-prefix="IMCP Rule20"protocol=icmpThe first one will permit ICMP packets with a maximum of 50 over 2 seconds (fine) the second drops at most 50 packets over 2 seconds. Everything above that is caught by a subsequent rule.I think you meant the second one to drop all ICMP, without limits.I do not see an "established" rule in the input chain - did you remove it? If so, can you re-add it?

---
```

## Response 8
FIRST:!!! Use a RDSGW (with also UDP enabled for better performance) - never expose a RDS /terminal directly on 3389. it will get hit hard... !!!..Second:Even if you say you dont use UDP steam this seems to be a 'kwown UDP-stream issue' to me.Try to increase it to 30 seconds (default on v7) instead of 20 seconds. That most likely fix the problem atleast in my experience.Seems like the router has been upgraded with a v6 config which makes it happen that udp-stream too low. ---

## Response 9
Many thanks for looking into this..re: a PPP profile, This has been shutdown and was for testing purposes. I'll clean up the config.re: I understand about RDSGW and also RDS being hit hardI hear your point I don't believe its the cause to the dropouts - there've only started to happen with the replacement of the firewall.In our mind the issue is with the firewall or we've made an error in our config.We been doing this for over 15 years and seen all the attacks long before the advice was to remove RDP from the internet etc etcWe've designed and built our own security systems to protect RDP. They work and didn't want to complicate this ticket.re: UDP timeoutyes we had experienced that almost immediately once we've connected it - freezing with the UDP.I believe the OS7 had it at 15s we've changed it 20s and seem to go away.We did try 30s it work fine too. But we've never had udp ports open and only ever used RDP.This is a preferred option as many home users have 3rd world internet connections.re: ICMP packetsSorry thats us "50 over 2 seconds" is normally disabled - we just turning things on as part of our troubleshooting.But thanks good eye.re: RULE 60 Establishsame as above normally off - it was just on for quick testing - but thank you.re: for the sake of pmtu discovery.ok i'll try it cant hurt - saying that ICMP off has always been the norm.re: established" rule in the input chainWas missing now in place, and dragged to the top made no difference...re: Microsoft documentyes read all them and all the troubleshooting points back to the router. The RDP server see's the connection dropped and so disconnects the user.(as opposed to the say the use logging off or the user disconnecting). On the user end, it freezes for 5 seconds and then retries and gets back in.But i'll re-read them just in case ive missed something. ---

## Response 10
re: a PPP profile, This has been shutdown and was for testing purposes. I'll clean up the config.OK, so not PPP and the usual MTU issue then. Do you have a different MTU for your internet fiber than you have for the internal network?re: ICMP packetsSorry thats us "50 over 2 seconds" is normally disabled - we just turning things on as part of our troubleshooting.But thanks good eye.No worries.re: for the sake of pmtu discovery.ok i'll try it cant hurt - saying that ICMP off has always been the norm.Let's see where that leads. Check the counter to see if you see some form of increase.re: established" rule in the input chainWas missing now in place, and dragged to the top made no difference...It won't hurt - and will help smooth out things from the router - but I suspect this by itself is not going to solve the whole issue, as there may be a combination of factors at play for now.Can you repost the firewall rules (/ip/firewall/filter) after you made the changes? ---

## Response 11
re: Do you have a different MTUWell for the fibre its actual MTU 1500 and the L2 MTU 1580 while the bridge is 1500 & 1578 respectively.Whats the PPP MTU issues?When i did install a L2TP PPP the speed was horrible - not thats in place anymore.We using Wireguard. So we've added a VPN between our servers and the customer. Look like its ok while they are in the office but problem persists while they are home - without the VPN.re: pmtu discoveryI added it the counters went to 70.4KB and hasnt changed.re: config
```
# 2024-12-05 22:50:39 by RouterOS 7.16.2/interfacebridgeaddcomment="DMZ Zone"name=bridge1/interfaceethernetset[finddefault-name=ether1]disabled=yesset[finddefault-name=ether2]comment="SWITCH"set[finddefault-name=ether3]comment="SWITCH"set[finddefault-name=ether4]comment="SWITCH"set[finddefault-name=ether5]disabled=yesset[finddefault-name=ether7]disabled=yesset[finddefault-name=ether8]disabled=yesset[finddefault-name=sfp-sfpplus1]comment=DISABLED disabled=yesset[finddefault-name=sfp1]auto-negotiation=nocomment=\"INTERNET PORT 400MBPS"/interfacewireguardaddlisten-port=retracted mtu=1420name=WG/interfacelistaddname=WANaddname=LAN/interfacelte apnset[finddefault=yes]ip-type=ipv4use-network-apn=no/ip pooladdcomment="DMZ DHCP Pool"name=DMZ-POOL ranges=\192.168.0.241-192.168.0.254/ip dhcp-serveraddaddress-pool=DMZ-POOL bootp-support=noneinterface=bridge1 lease-time=\2h30mname=FW-DHCP/portset0name=serial0set1name=serial1/queue simpleaddcomment="TOTAL INTERNET SPEED"disabled=yes max-limit=400M/1Gname=\"ALL BANDWIDTH"target=sfp1addmax-limit=10M/10Mname="OFFICE"target=retractedaddcomment="Protect DMZ traffic back to customer"disabled=yes max-limit=\20M/20Mname=queue1 target=retractedaddcomment="10MBPS/10MBPS Webservers"max-limit=10M/10Mname=WEBSERVERS \
    target=192.168.0.21/32addcomment="50MBPS/50MBPS SERVER19"dst=sfp1 max-limit=20M/20Mname=20MBPS\
    target=192.168.0.70/32addmax-limit=10M/10Mname=SMTP-INBOUND target=192.168.0.76/32adddisabled=yes name=TERMINAL parent="ALL BANDWIDTH"priority=2/2target=\192.168.0.48/32/queue typeaddkind=fq-codel name=fq_codel/queue simpleaddbucket-size=0.005/0.005comment="Buffer Bloat Testing"disabled=yes \
    max-limit=400M/1Gname=FQ_CODEL-QOS priority=1/1queue=fq_codel/fq_codel \
    target=sfp1 total-queue=fq_codel/interfacebridge portaddbridge=bridge1 comment="switch"interface=ether2addbridge=bridge1 comment="Switch"interface=ether3addbridge=bridge1 comment="Switch"interface=ether4addbridge=bridge1 disabled=yesinterface=ether5addbridge=bridge1 disabled=yesinterface=ether6addbridge=bridge1 disabled=yesinterface=ether7addbridge=bridge1 disabled=yesinterface=ether8addbridge=bridge1 disabled=yesinterface=ether1/ip firewall connection trackingsettcp-syn-received-timeout=30stcp-syn-sent-timeout=30sudp-timeout=20s/ip settingssetarp-timeout=1mmax-neighbor-entries=8192/ipv6 settingssetdisable-ipv6=yes max-neighbor-entries=8192/interfacedetect-internetsetdetect-interface-list=WAN internet-interface-list=WAN lan-interface-list=\
    LAN wan-interface-list=WAN/interfacel2tp-server serversetaccept-proto-version=l2tpv2 allow-fast-path=yesdefault-profile=default/interfacelist memberaddinterface=bridge1 list=LANaddinterface=sfp1 list=WAN/interfaceovpn-server serversetauth=sha1,md5/interfacewireguard peersaddallowed-address=etc etc/ip addressaddaddress=192.168.0./24comment=Networkinterface=bridge1 network=\192.168.0.0addaddress=200.200.200.30/27comment="INTERNET CONNECTION"interface=sfp1 \
    network=200.200.200.28addaddress=200.200.200.31/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.32/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.33/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.34/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.35/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.36/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.37/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.38/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.39/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.40/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.41/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.42/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.43/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.44/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.45/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.46/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.47/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.48/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.49/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.50/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.51/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.52/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.53/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.54/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.55/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.56/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.57/27interface=sfp1 network=200.200.200.28addaddress=200.200.200.58/27interface=sfp1 network=200.200.200.28addaddress=192.168.99.1/24interface=WG network=192.168.99.0/ip dhcp-clientadddisabled=yesinterface=sfp-sfpplus1/ip dhcp-server networkaddaddress=192.168.0.0/24dns-server=192.168.0.20,192.168.0.21domain=\
    domain.localgateway=192.168.0.1netmask=24ntp-server=\192.168.0.76/ip dnssetservers=192.168.0.20/ip firewall address-listaddaddress=0.0.0.0/8comment=RFC6890 list=not_in_internetaddaddress=172.16.0.0/12comment=RFC6890 list=not_in_internetaddaddress=192.168.0.0/16comment=RFC6890 list=not_in_internetaddaddress=10.0.0.0/8comment=RFC6890 list=not_in_internetaddaddress=169.254.0.0/16comment=RFC6890 list=not_in_internetaddaddress=127.0.0.0/8comment=RFC6890 list=not_in_internetaddaddress=224.0.0.0/4comment=Multicastlist=not_in_internetaddaddress=198.18.0.0/15comment=RFC6890 list=not_in_internetaddaddress=192.0.0.0/24comment=RFC6890 list=not_in_internetaddaddress=192.0.2.0/24comment=RFC6890 list=not_in_internetaddaddress=198.51.100.0/24comment=RFC6890 list=not_in_internetaddaddress=203.0.113.0/24comment=RFC6890 list=not_in_internetaddaddress=100.64.0.0/10comment=RFC6890 list=not_in_internetaddaddress=240.0.0.0/4comment=RFC6890 list=not_in_internetaddaddress=192.88.99.0/24comment="6to4 relay Anycast [RFC 3068]"list=\
    not_in_internetaddaddress=192.168.0.48comment=SRV-SERVER03 list=TERMINALSERVICESaddaddress=192.168.0.20comment=SRV-SERVER07 list=TERMINALSERVICESaddaddress=192.168.0.64comment=SRV-SERVER12 list=TERMINALSERVICESaddaddress=192.168.0.88comment=SRV-SERVER25 list=TERMINALSERVICESaddaddress=192.168.0.00comment=SRV-SERVER04 list=TERMINALSERVICESaddaddress=192.168.0.98comment=SRV-SERVER24 list=TERMINALSERVICESaddaddress=192.168.0.80comment=SRV-SERVER23 list=TERMINALSERVICESaddaddress=192.168.0.74list=PROXYaddaddress=192.168.0.20comment=SERVER02 list=DMZ_WEBSERVERSaddaddress=192.168.0.50comment=SERVER08 list=DMZ_WEBSERVERSaddaddress=192.168.0.21comment=SERVER09 list=DMZ_WEBSERVERSaddaddress=192.168.0.66comment=SERVER11 list=DMZ_WEBSERVERSaddaddress=192.168.0.70comment=SERVER19 list=DMZ_WEBSERVERSaddaddress=192.168.0.44comment=SERVER21 list=DMZ_WEBSERVERSaddaddress=192.168.0.46comment=SERVER01 list=VPN_ACCESSABLEaddaddress=192.168.0.20comment=SERVER02 list=VPN_ACCESSABLEaddaddress=192.168.0.52comment=SERVER05 list=VPN_ACCESSABLEaddaddress=192.168.0.50comment=SERVER14 list=VPN_ACCESSABLEaddaddress=192.168.0.21comment=SERVER21 list=VPN_ACCESSABLEaddaddress=192.168.0.70comment=SERVER19 list=VPN_ACCESSABLEaddaddress=192.168.0.80comment=SERVER23 list=VPN_ACCESSABLEaddaddress=192.168.0.88comment=SERVER25 list=VPN_ACCESSABLEaddaddress=192.168.0.0/24list=LANaddaddress=192.168.0.20list=DNSaddaddress=192.168.0.21list=DNSaddaddress=192.168.0.98comment=SERVER24 list=VPN_ACCESSABLEaddaddress=192.168.0.98comment=SERVER24 list=VOIP_ACCESS/ip firewall filteraddaction=fasttrack-connection chain=forward comment=\"fasttrack - disables QUEUES bandwidth"connection-state=\
    established,related hw-offload=yes log-prefix="FTract Enabled Rule1"addaction=accept chain=forward comment="=====established, related"\
    connection-state=established,related log-prefix="RULE 60 Establish"addaction=accept chain=input comment=\"Accept related and established connections"connection-state=\
    established,related log-prefix="input established rule 3"addaction=accept chain=input comment=WIREGUARD dst-port=retracted protocol=udp \
    src-address-list=VPN_EXTERNAL_INTaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=drop chain=input comment="Black List"in-interface=sfp1 \
    src-address-list=black_listaddaction=accept chain=input comment="allow pings from customers"dst-address-list=\
    VPN_EXTERNAL_INTin-interface=sfp1 limit=50,2:packet log=yes log-prefix=\"IMCP traffic Rule 21"protocol=icmpaddaction=drop chain=input comment="dont allow pings"in-interface=sfp1 \
    limit=50,2:packet log-prefix="IMCP Rule20"protocol=icmpaddaction=drop chain=input comment=\"drop everything else - including firmware upgrade"in-interface-list=\!LAN log-prefix="Rule 22 !LAN"addaction=accept chain=forward comment="Inbound SERVER23"disabled=yes \
    dst-address=192.168.0.80dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcp src-address-list=TS_Whitelistaddaction=accept chain=forward comment="Inbound SERVER25"disabled=yes \
    dst-address=192.168.0.88dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcp src-address-list=TS_Whitelistaddaction=accept chain=forward comment="Inbound SERVER07"disabled=yes \
    dst-address=192.168.0.20dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcp src-address-list=TS_Whitelistaddaction=accept chain=forward comment="Inbound SERVER24"disabled=yes \
    dst-address=192.168.0.98dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcp src-address-list=TS_Whitelistaddaction=accept chain=forward comment="Inbound SERVER25"dst-address=\192.168.0.88dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound SERVER23"dst-address=\192.168.0.80dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound SERVER07"dst-address=\192.168.0.20dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound SERVER03"dst-address=\192.168.0.48dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound SERVER12"dst-address=\192.168.0.64dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound SERVER24"dst-address=\192.168.0.98dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment=\"Rule 210 - default Internet browsing"dst-port=80,443,25,53,21\out-interface=sfp1 protocol=tcp src-address-list=TERMINALSERVICESaddaction=accept chain=forward comment="Rule 33 - default Internet browsing"\
    dst-port=80,443,25,21log-prefix="rule 33 Default Internet"\out-interface=sfp1 protocol=tcp src-address-list=DMZ_WEBSERVERSaddaction=accept chain=forward comment="Rule 33 - default DNS"dst-port=53\
    log-prefix="Default Internet DNS"protocol=udp src-address-list=\
    DMZ_WEBSERVERSaddaction=drop chain=forward comment="=====Black List Attackers"\
    src-address-list=black_listaddaction=accept chain=forward comment="Inbound SRVDB03"dst-address=\192.168.0.90dst-port=443in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Rule 253 - All Internet browsing"\
    src-address-list=PROXYaddaction=accept chain=forward comment="Rule 280 - Internet Access"\out-interface=sfp1 src-address-list="Servers"addaction=accept chain=forward comment="Rule 161 SRV Access DMZ Servers"\
    log-prefix=SRVtoDMZsrc-address=retractedaddaction=accept chain=forward comment="Rule 161 SRV Access DMZ Servers"\
    disabled=yes dst-address=retracted log-prefix=SRVtoDMZsrc-address=\192.168.0.0/24addaction=accept chain=forward comment="Rule 274 Clients Access DMZ Servers"\
    dst-address-list=VPN_ACCESSABLE src-address-list=VPN_SITE_LANaddaction=accept chain=forward comment="Rule 275 Clients Access DMZ Servers"\
    dst-address-list=VPN_SITE_LAN log-prefix=VPN_LAN src-address-list=\
    VPN_ACCESSABLEaddaction=log chain=forward comment="Drop invalid connections"\
    connection-state=invalid disabled=yes log=yes log-prefix=\"Drop invalid RULE 68"addaction=drop chain=forward comment=\"drop tries to reach not public addresses from LAN"dst-address-list=\
    not_in_internetin-interface-list=LAN log-prefix=\"!public_from_LAN Rule  70"out-interface-list=!LANaddaction=drop chain=forward comment=\"drop incoming from internet which is not public IP"in-interface-list=\
    WAN log-prefix="!public Rule 60"src-address-list=not_in_internetaddaction=drop chain=forward comment=\"drop packets from LAN that do not have LAN IP"in-interface-list=LAN \
    log-prefix="DROP LAN_!LAN Rule 73"src-address=!192.168.0.0/24addaction=drop chain=forward comment="drop all else"log-prefix=\"DROP_ALL Rule 74"/ip firewall nataddaction=src-nat chain=srcnat comment=SRV-SERVER07out-interface=sfp1 \
    src-address=192.168.0.20to-addresses=200.200.200.37addaction=src-nat chain=srcnat comment="SRV-SERVER09\r\
    \n"out-interface=sfp1 src-address=192.168.0.21to-addresses=\200.200.200.36addaction=src-nat chain=srcnat comment=SRV-SERVER03out-interface=sfp1 \
    src-address=192.168.0.48to-addresses=200.200.200.34addaction=src-nat chain=srcnat comment=SRV-SERVER25out-interface=sfp1 \
    src-address=192.168.0.88to-addresses=200.200.200.41addaction=src-nat chain=srcnat comment=SRV-SERVER23out-interface=sfp1 \
    src-address=192.168.0.80to-addresses=200.200.200.38addaction=src-nat chain=srcnat comment=SRV-SERVER24out-interface=sfp1 \
    src-address=192.168.0.98to-addresses=200.200.200.42addaction=src-nat chain=srcnat comment=SRV-SERVER12out-interface=sfp1 \
    src-address=192.168.0.64to-addresses=200.200.200.40addaction=masquerade chain=srcnat comment="General DMZ Internet Access"\
    log-prefix=MASQUERADEout-interface-list=WAN src-address-list=LANaddaction=dst-nat chain=dstnat comment="SRV-SERVER03 (Rule 249) "\
    dst-address=200.200.200.34dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=safelist to-addresses=192.168.0.48\
    to-ports=3389addaction=dst-nat chain=dstnat comment="SRV-SERVER07 (Rule 249) "\
    dst-address=200.200.200.37dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=safelist to-addresses=192.168.0.20\
    to-ports=3389addaction=dst-nat chain=dstnat comment="SRV-SERVER12 (Rule 249) "\
    dst-address=200.200.200.40dst-port=3389in-interface=sfp1 log-prefix=\
    SERVER12 protocol=tcp src-address-list=safelist to-addresses=\192.168.0.64to-ports=3389addaction=dst-nat chain=dstnat comment="SRV-SERVER12 (Rule 249) "\
    dst-address=200.200.200.40dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=TS_Whitelist to-addresses=192.168.0.64to-ports=3389addaction=dst-nat chain=dstnat comment="SRV-SERVER12 (Rule 249) "\
    dst-address=200.200.200.42dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=TS_Whitelist to-addresses=192.168.0.98to-ports=3389addaction=dst-nat chain=dstnat comment="SRV-SERVER25 (Rule 249) "\
    dst-address=200.200.200.41dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=safelist to-addresses=192.168.0.88\
    to-ports=3389addaction=dst-nat chain=dstnat comment="SRV-SERVER23 (Rule 249) "\
    dst-address=200.200.200.38dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=safelist to-addresses=192.168.0.80\
    to-ports=3389addaction=dst-nat chain=dstnat comment=SRV-SERVER24 dst-address=200.200.200.42\
    dst-port=3389in-interface=sfp1 protocol=tcp src-address-list=\
    safelist to-addresses=192.168.0.98to-ports=3389addaction=dst-nat chain=dstnat comment="SRV-SERVER23 (Rule 249) "\
    dst-address=200.200.200.38dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=TS_Whitelist to-addresses=192.168.0.80to-ports=3389addaction=dst-nat chain=dstnat comment="SRV-SERVER25 (Rule 249) "\
    dst-address=200.200.200.41dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=TS_Whitelist to-addresses=192.168.0.88to-ports=3389/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/ip routeaddcomment="DEFAULT GW"disabled=nodistance=1dst-address=0.0.0.0/0\
    gateway=200.200.200.29routing-table=main scope=30suppress-hw-offload=no\
    target-scope=10/ip servicesettelnet disabled=yessetftp disabled=yessetwww disabled=yessetssh disabled=yessetapi disabled=yessetapi-ssl disabled=yes/routing bfd configurationadddisabled=nointerfaces=all min-rx=200msmin-tx=200msmultiplier=5/system clock/system health settingssetuse-fan=auxiliary/system identitysetname=SRVFW/system notesetshow-at-login=no/tool bandwidth-serversetenabled=no

---
```

## Response 12
Hi there.Regarding the rules, chain input:Remove the logging for the first rule (established/related)
```
addaction=accept chain=input comment=\"Accept related and established connections"connection-state=\
established,related log-prefix="input established rule 3"Move this one below the rule that drops the invalid connections.
```

```
addaction=accept chain=input comment=WIREGUARD dst-port=retracted protocol=udp \
src-address-list=VPN_EXTERNAL_INTRemove thelimit=59,2from this one.
```

```
addaction=drop chain=input comment="dont allow pings"in-interface=sfp1 \
limit=50,2:packet log-prefix="IMCP Rule20"protocol=icmpConsider removing the logging from this one. Can be quite noisy.
```

```
addaction=drop chain=input comment=\"drop everything else - including firmware upgrade"in-interface-list=\!LAN log-prefix="Rule 22 !LAN"Regarding chain=forward:Remove the logging for the first rule, fasttracked connections.
```

```
addaction=fasttrack-connection chain=forward comment=\"fasttrack - disables QUEUES bandwidth"connection-state=\
established,related hw-offload=yes log-prefix="FTract Enabled Rule1"Remove the logging for the second rule, established/related connections.
```

```
addaction=accept chain=forward comment="=====established, related"\
connection-state=established,related log-prefix="RULE 60 Establish"Might be worth adding the source and destination interfaces for this one.
```

```
addaction=accept chain=forward comment="Rule 161 SRV Access DMZ Servers"\
log-prefix=SRVtoDMZsrc-address=retractedThis one should ideally be near the very top, like number 3 or 4
```

```
addaction=log chain=forward comment="Drop invalid connections"\
connection-state=invalid disabled=yes log=yes log-prefix=\"Drop invalid RULE 68"Consider removing the logging from the last rule, as this will just be noise.
```

```
addaction=drop chain=forward comment="drop all else"log-prefix=\"DROP_ALL Rule 74"

---
```

## Response 13
many thanks - looking at the config ive posted it suggests logging is on but its not bar one rule - which ive turned off.However, i dont see it changing any of the dropouts.re: this ruleadd action=log chain=forward comment="Drop invalid connections" \connection-state=invalid disabled=yes log=yes log-prefix=\"Drop invalid RULE 68"Its actually disabled as it breaks things - as i can see allot of RST - so far only non RDP serversDrop invalid RULE 68 forward: in:bridge1 out:sfp1, connection-state:invalid src-mac 18:a9:05:41:60:0a, proto TCP (RST), 192.168.0.174:59052->162.247.243.29:443, len 40Drop invalid RULE 68 forward: in:bridge1 out:sfp1, connection-state:invalid src-mac d8:d3:85:60:80:1e, proto TCP (RST), 192.168.0.176:443->14.200.38.198:49902, len 40 ---

## Response 14
The question is whether the second config you posted is after the changes: I don't see any of the icmp rules you wrote you created.The situation you mention with the rst packet is known, some servers reply with a rst instead of fin to immediately tear down the connection. I remember mentions of that being related to ecn - you can try disabling it on the server with
```
netshinttcpsetglobalecncapability=disabledAnd see if it helps. There is a way to create a mangle rule to remove the ECN, I will look into that later.

---
```

## Response 15
hmmm re: netsh int tcp set global ecncapability=disabled ok sure i'll give it a try.What about on the RDP servers?Is this the imcp rule? This is only allowing icmp from my customers. This is in place - not allot of traffic recorded on the counters. (40KB)add action=accept chain=input comment="allow pings from customers" src-address-list=\CUSTOMERS in-interface=sfp1 packet log=yes log-prefix=\"IMCP traffic Rule 21" protocol=icmp ---

## Response 16
On Windows servers, you can disable the ecncapability without issue.For the rule, yes but don't forget the NAT rules - something that looks like
```
/ip firewall nat...addaction=dst-nat chain=dstnat comment="SERVER03 (Rule 249bis) "\
dst-address=200.200.200.34in-interface=sfp1 protocol=icmp \
src-address-list=CountryIPAustraliato-addresses=192.168.0.148addaction=dst-nat chain=dstnat comment="SERVER07 (Rule 249bis) "\
dst-address=200.200.200.37in-interface=sfp1 protocol=icmp \
src-address-list=CountryIPAustraliato-addresses=192.168.0.120What you want is the path MTU to be established all the way, not just to your firewall.Can you repost a full configuration with the changes? Between code tags, please-

---
```

## Response 17
will do - just addressing users temperatures ---

## Response 18
Still RDP drop outs - random times sometimes 1min apart through to 10minutes. ---

## Response 19
```
# 2024-12-27 18:53:47 by RouterOS 7.16.2# software id = X9ST-QB7H## model = CCR1009-8G-1S-1S+/interfacebridgeaddcomment="DMZ Zone"name=bridge1/interfaceethernetset[finddefault-name=ether1]disabled=yesset[finddefault-name=ether2]comment="HPE OfficeConnect Switch 1920S 24G"set[finddefault-name=ether3]comment="HP Switch"set[finddefault-name=ether4]comment="LinkSys Switch"set[finddefault-name=ether5]disabled=yesset[finddefault-name=ether7]disabled=yesset[finddefault-name=ether8]disabled=yesset[finddefault-name=sfp-sfpplus1]comment=DISABLED disabled=yesset[finddefault-name=sfp1]auto-negotiation=nocomment=\"INTERNET PORT"/interfacewireguardaddlisten-port=13231mtu=1420name=WG_Interface/interfacelistaddname=WANaddname=LAN/interfacelte apnset[finddefault=yes]ip-type=ipv4use-network-apn=no/ip pooladdcomment="DMZ DHCP Pool"name=DMZ-POOL ranges=\192.168.0.241-192.168.0.254/ip dhcp-serveraddaddress-pool=DMZ-POOL bootp-support=noneinterface=bridge1 lease-time=\2h30mname=FW-DHCP/portset0name=serial0set1name=serial1/queue simpleaddcomment="TOTAL INTERNET SPEED"disabled=yes max-limit=400M/1Gname=\"ALL BANDWIDTH"target=sfp1addcomment="Protect DMZ traffic back to customer"max-limit=20M/20Mname=\
    DC_DMZ_ACCESS target=LAN1/24,LAN2/24,LAN3/24addcomment="10MBPS/10MBPS Webservers"max-limit=10M/10Mname=WEBSERVERS \
    target=192.168.0.21/32adddisabled=yes name=TERMINAL parent="ALL BANDWIDTH"priority=2/2target=\192.168.0.148/32addcomment="retracted printing"disabled=yes max-limit=5M/5Mname=\
    retractedPrinting target=CLIENTWAMIP/32/queue typeaddkind=fq-codel name=fq_codel/queue simpleaddbucket-size=0.005/0.005comment="Buffer Bloat Testing"disabled=yes \
    max-limit=400M/1Gname=FQ_CODEL-QOS priority=1/1queue=fq_codel/fq_codel \
    target=sfp1 total-queue=fq_codel/interfacebridge portaddbridge=bridge1 comment="HP POE Switch"interface=ether2addbridge=bridge1 comment="HPE Switch"interface=ether3addbridge=bridge1 comment="Linksys 48 Port"interface=ether4addbridge=bridge1 disabled=yesinterface=ether5addbridge=bridge1 disabled=yesinterface=ether6addbridge=bridge1 disabled=yesinterface=ether7addbridge=bridge1 disabled=yesinterface=ether8addbridge=bridge1 disabled=yesinterface=ether1/ip firewall connection trackingsettcp-syn-received-timeout=30stcp-syn-sent-timeout=30sudp-timeout=20s/ip settingssetarp-timeout=1mmax-neighbor-entries=8192/ipv6 settingssetdisable-ipv6=yes max-neighbor-entries=8192/interfacedetect-internetsetdetect-interface-list=WAN internet-interface-list=WAN lan-interface-list=\
    LAN wan-interface-list=WAN/interfacel2tp-server serversetaccept-proto-version=l2tpv2 allow-fast-path=yesdefault-profile=default/interfacelist memberaddinterface=bridge1 list=LANaddinterface=sfp1 list=WAN/interfaceovpn-server serversetauth=sha1,md5/interfacewireguard peersaddallowed-address=retractedaddallowed-address=retractedaddallowed-address=retracted/ip addressaddaddress=192.168.0.1/24comment=Networkinterface=bridge1 network=\192.168.0.0addaddress=200.200.200.130/27comment="INTERNET CONNECTION"interface=sfp1 \
    network=200.200.200.128addaddress=200.200.200.131/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.132/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.133/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.134/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.135/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.136/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.137/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.138/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.139/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.140/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.141/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.142/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.143/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.144/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.145/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.146/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.147/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.148/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.149/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.150/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.151/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.152/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.153/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.154/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.155/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.156/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.157/27interface=sfp1 network=200.200.200.128addaddress=200.200.200.158/27interface=sfp1 network=200.200.200.128addaddress=192.168.201.1/24interface=WG_Interface network=192.168.201.0/ip dhcp-clientadddisabled=yesinterface=sfp-sfpplus1/ip dhcp-server networkaddaddress=192.168.0.0/24dns-server=192.168.0.20,192.168.0.21domain=\
    retractedolutions.localgateway=192.168.0.1netmask=24ntp-server=\192.168.0.176/ip dnssetservers=192.168.0.20/ip firewall address-listaddaddress=0.0.0.0/8comment=RFC6890 list=not_in_internetaddaddress=172.16.0.0/12comment=RFC6890 list=not_in_internetaddaddress=192.168.0.0/16comment=RFC6890 list=not_in_internetaddaddress=10.0.0.0/8comment=RFC6890 list=not_in_internetaddaddress=169.254.0.0/16comment=RFC6890 list=not_in_internetaddaddress=127.0.0.0/8comment=RFC6890 list=not_in_internetaddaddress=224.0.0.0/4comment=Multicastlist=not_in_internetaddaddress=198.18.0.0/15comment=RFC6890 list=not_in_internetaddaddress=192.0.0.0/24comment=RFC6890 list=not_in_internetaddaddress=192.0.2.0/24comment=RFC6890 list=not_in_internetaddaddress=198.51.100.0/24comment=RFC6890 list=not_in_internetaddaddress=203.0.113.0/24comment=RFC6890 list=not_in_internetaddaddress=100.64.0.0/10comment=RFC6890 list=not_in_internetaddaddress=240.0.0.0/4comment=RFC6890 list=not_in_internetaddaddress=192.88.99.0/24comment="6to4 relay Anycast [RFC 3068]"list=\
    not_in_internetaddaddress=192.168.0.148comment=retracted-SERVER03 list=TERMINALSERVICESaddaddress=192.168.0.120comment=retracted-SERVER07 list=TERMINALSERVICESaddaddress=192.168.0.164comment=retracted-SERVER12 list=TERMINALSERVICESaddaddress=192.168.0.188comment=retracted-SERVER25 list=TERMINALSERVICESaddaddress=192.168.0.174comment=retracted list=PROXYaddaddress=192.168.0.154comment=retracted list=retractedaddaddress=retracted comment="retracted Melbourne External"list=\
    VPN_EXTERNAL_INTaddaddress=192.168.0.176comment=retracted-retracted list=DMZ_WEBSERVERSaddaddress=192.168.0.180comment=retracted-SERVER23 list=TERMINALSERVICESaddaddress=192.168.0.168comment="retracted-SERVER16 BROKER"disabled=yes list=\
    TERMINALSERVICESaddaddress=192.168.0.0/24list=LANaddaddress=192.168.0.20list=DNSaddaddress=192.168.0.21list=DNSaddaddress=192.168.0.100comment=retracted-SERVER04 list=TERMINALSERVICESaddaddress=192.168.0.198comment=retracted-SERVER24 list=TERMINALSERVICES/ip firewall filteraddaction=fasttrack-connection chain=forward comment=\"fasttrack - disables QUEUES bandwidth"connection-state=\
    established,related hw-offload=yes log-prefix="FTract Enabled Rule1"addaction=accept chain=forward comment="=====established, related"\
    connection-state=established,related log-prefix="RULE 60 Establish"addaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment=WIREGUARD dst-port=13231protocol=udp \
    src-address-list=VPN_EXTERNAL_INTaddaction=log chain=forward comment="Drop invalid connections"\
    connection-state=invalid disabled=yes log=yes log-prefix=\"Drop invalid RULE 68"addaction=accept chain=input comment=\"Accept related and established connections"connection-state=\
    established,related log-prefix="input established rule 3"addaction=accept chain=input comment=\"Allow ACL=retracted WINBOX to the router EXTERNAL"dst-port=8291protocol=tcp \
    src-address-list=retracted_supportaddaction=accept chain=input comment=\"Allow ACL=retracted WINBOX to the router LAN"dst-port=8291protocol=tcp \
    src-address-list=LANaddaction=accept chain=input comment="allow pings from customers"\in-interface=sfp1 log-prefix="IMCP traffic Rule 21"protocol=icmp \
    src-address-list=VPN_EXTERNAL_INTaddaction=drop chain=input comment="dont allow pings"in-interface=sfp1 \
    log-prefix="IMCP Rule20"protocol=icmpaddaction=accept chain=input comment="lan access to router"disabled=yes \in-interface-list=LAN src-address-list=LANaddaction=drop chain=input comment=\"drop everything else - including firmware upgrade"in-interface-list=\!LAN log-prefix="Rule 22 !LAN"addaction=accept chain=forward comment="Inbound SERVER25"dst-address=\192.168.0.188dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound SERVER23"dst-address=\192.168.0.180dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound SERVER07"dst-address=\192.168.0.120dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound SERVER03"dst-address=\192.168.0.148dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound SERVER12"dst-address=\192.168.0.164dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Inbound SERVER24"dst-address=\192.168.0.198dst-port=3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment=\"Rule 210 - default Internet browsing"dst-port=80,443,25,53,21\out-interface=sfp1 protocol=tcp src-address-list=TERMINALSERVICESaddaction=accept chain=forward comment="Rule 210 - ALL OUTBOUND"log-prefix=\"ALL OUTBOUND"out-interface=sfp1 protocol=tcp src-address-list=\
    TERMINALSERVICESaddaction=accept chain=forward comment="Rule 33 - default Internet browsing"\
    dst-port=80,443,25,21log-prefix="rule 33 Default Internet"\out-interface=sfp1 protocol=tcp src-address-list=DMZ_WEBSERVERSaddaction=accept chain=forward comment="Rule 33 - default DNS"dst-port=53\
    log-prefix="Default Internet DNS"protocol=udp src-address-list=\
    DMZ_WEBSERVERSaddaction=accept chain=forward comment="Inbound SERVER27"dst-address=\192.168.0.131dst-port=80,443,3389in-interface=sfp1 log-prefix=\"Default Internet DNS"protocol=tcpaddaction=accept chain=forward comment="Rule 253 - All Internet browsing"\
    src-address=192.168.0.174addaction=accept chain=forward comment="Rule 274 Clients Access DMZ Servers"\
    dst-address-list=VPN_ACCESSABLE src-address-list=VPN_SITE_LANaddaction=accept chain=forward comment="Rule 275 Clients Access DMZ Servers"\
    dst-address-list=VPN_SITE_LAN log-prefix=VPN_LAN src-address-list=\
    VPN_ACCESSABLEaddaction=accept chain=forward comment=\"Access external VOIP Services UDP 12662"disabled=yes dst-port=5060,6250\
    log-prefix="Default Internet"protocol=udp src-address-list=VOIP_ACCESSaddaction=accept chain=forward comment=Speedtestdisabled=yes dst-port=8080\
    log-prefix="Default Internet"protocol=tcpaddaction=accept chain=forward comment="Default forwarding rule (DISABLE)"\
    disabled=yes log=yes log-prefix="Rule 70 LAN to internet"\
    src-address-list=LANaddaction=drop chain=forward comment=\"drop tries to reach not public addresses from LAN"dst-address-list=\
    not_in_internetin-interface-list=LAN log-prefix=\"!public_from_LAN Rule  70"out-interface-list=!LANaddaction=drop chain=forward comment=\"drop incoming packets that are not NAT`ted"connection-nat-state=!dstnat \
    connection-state=newdisabled=yesin-interface-list=WAN log-prefix=\"!NAT Rule 59"addaction=drop chain=forward comment=\"drop incoming from internet which is not public IP"in-interface-list=\
    WAN log-prefix="!public Rule 60"src-address-list=not_in_internetaddaction=drop chain=forward comment=\"drop packets from LAN that do not have LAN IP"in-interface-list=LAN \
    log-prefix="DROP LAN_!LAN Rule 73"src-address=!192.168.0.0/24addaction=drop chain=forward comment="drop all else"log-prefix=\"DROP_ALL Rule 74"/ip firewall nataddaction=src-nat chain=srcnat comment=retracted-SERVER07out-interface=sfp1 \
    src-address=192.168.0.120to-addresses=200.200.200.137addaction=src-nat chain=srcnat comment=retracted-SERVER03out-interface=sfp1 \
    src-address=192.168.0.148to-addresses=200.200.200.134addaction=src-nat chain=srcnat comment=retracted-SERVER25out-interface=sfp1 \
    src-address=192.168.0.188to-addresses=200.200.200.141addaction=src-nat chain=srcnat comment=retracted-SERVER23out-interface=sfp1 \
    src-address=192.168.0.180to-addresses=200.200.200.138addaction=src-nat chain=srcnat comment=retracted-SERVER24out-interface=sfp1 \
    src-address=192.168.0.198to-addresses=200.200.200.142addaction=src-nat chain=srcnat comment=retracted-SERVER12out-interface=sfp1 \
    src-address=192.168.0.164to-addresses=200.200.200.140addaction=masquerade chain=srcnat comment="General DMZ Internet Access"\
    log-prefix=MASQUERADEout-interface-list=WAN src-address-list=LANaddaction=dst-nat chain=dstnat comment="retracted-SERVER03 (Rule 249) "\
    dst-address=200.200.200.134dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=to-addresses=192.168.0.148to-ports=3389addaction=dst-nat chain=dstnat comment="retracted-SERVER07 (Rule 249) "\
    dst-address=200.200.200.137dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=to-addresses=192.168.0.120\
    to-ports=3389addaction=dst-nat chain=dstnat comment="retracted-SERVER12 (Rule 249) "\
    dst-address=200.200.200.140dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=to-addresses=192.168.0.164to-ports=3389addaction=dst-nat chain=dstnat comment="retracted-SERVER12 (Rule 249) "\
    dst-address=200.200.200.142dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=to-addresses=192.168.0.198to-ports=3389addaction=dst-nat chain=dstnat comment=retracted-SERVER24 dst-address=200.200.200.142\
    dst-port=3389in-interface=sfp1 protocol=tcp src-address-list=\
     to-addresses=192.168.0.198to-ports=3389addaction=dst-nat chain=dstnat comment="retracted-SERVER23 (Rule 249) "\
    dst-address=200.200.200.138dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=to-addresses=192.168.0.180to-ports=3389addaction=dst-nat chain=dstnat comment="retracted-SERVER25 (Rule 249) "\
    dst-address=200.200.200.141dst-port=3389in-interface=sfp1 protocol=tcp \
    src-address-list=to-addresses=192.168.0.188to-ports=3389addaction=dst-nat chain=dstnat comment="retracted-SERVER27 (Rule 268) "\
    dst-address=200.200.200.157dst-port=80,443in-interface=sfp1 log-prefix=\
    retracted-SERVER27 protocol=tcp to-addresses=192.168.0.131/ip firewall service-portsetftp disabled=yessettftp disabled=yesseth323 disabled=yessetsip disabled=yessetpptp disabled=yes/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/ip routeaddcomment="DEFAULT GW"disabled=nodistance=1dst-address=0.0.0.0/0\
    gateway=200.200.200.129routing-table=main scope=30suppress-hw-offload=no\
    target-scope=10/ip servicesettelnet disabled=yessetftp disabled=yessetwww disabled=yessetssh disabled=yessetapi disabled=yessetwinbox address=retractedsetapi-ssl disabled=yes/lcdsetenabled=notouch-screen=disabled/routing bfd configurationadddisabled=nointerfaces=all min-rx=200msmin-tx=200msmultiplier=5/system clocksettime-zone-name=retracted/system health settingssetuse-fan=auxiliary/system identitysetname=retractedFW/system notesetshow-at-login=no/system scheduler/system script/tool bandwidth-serversetenabled=no

---
```

## Response 20
You still haven't:Permitted icmp to reach the servers.Used the code tags when posting your config.Do the first one, post the updated config using the second one and check if you still have disconnections. ---

## Response 21
You still haven't:,,,Used the code tags when posting your config.,,,,Twice ---

## Response 22
Thanks but what am i missing. I have a rule that blocks ICMP hitting the WAN interface - basically turn that off and allow ICMP?On my previous firewall ive always been able to keep it off but happy to turn it back on and see what happens ---

## Response 23
Thanks but what am i missing. I have a rule that blocks ICMP hitting the WAN interface - basically turn that off and allow ICMP?On my previous firewall ive always been able to keep it off but happy to turn it back on and see what happensJust for the Nats to the servers and the firewall rules.
```
/ip firewall nat...addaction=dst-nat chain=dstnat comment="SERVER03 (Rule 249bis) "\
dst-address=200.200.200.34in-interface=sfp1 protocol=icmp \
src-address-list=CountryIPAustraliato-addresses=192.168.0.148addaction=dst-nat chain=dstnat comment="SERVER07 (Rule 249bis) "\
dst-address=200.200.200.37in-interface=sfp1 protocol=icmp \
src-address-list=CountryIPAustraliato-addresses=192.168.0.120

---
```

## Response 24
@vingjfg, I am a bit confused regarding how you expect these two rules to eliminate the RDP outages.The connection tracking normally identifies all ICMP messages that provide feedback regarding packets that belong to existing TCP or UDP connections, applies the appropriate src-nat and/or dst-nat treatment on them, and sets theirconnection-stateattribute torelated, so theconnection-state=established, relatedaction=acceptrule in filter allows them to pass. Can you elaborate on the purpose of those rules you suggest? ---

## Response 25
@vingjfg, I am a bit confused regarding how you expect these two rules to eliminate the RDP outages.The connection tracking normally identifies all ICMP messages that provide feedback regarding packets that belong to existing TCP or UDP connections, applies the appropriate src-nat and/or dst-nat treatment on them, and sets theirconnection-stateattribute torelated, so theconnection-state=established, relatedaction=acceptrule in filter allows them to pass. Can you elaborate on the purpose of those rules you suggest?@Sindy, I don't expect these rules to eliminate the outages, but to provide the possibility to ping the servers from the outside, and thus to check the MTU boundaries or see whether there is a reply to ping when one of the OP's clients is having issues. ---

## Response 26
try
```
udp-timeout:30s

---
```

## Response 27
try
```
udp-timeout:30s@chechito, good thinking: the first recommendation was to open UDP/3389 in addition to TCP/3389 as RDP uses UDP to stream faster, but OP said it was not open and did not want to open it.

---
```

## Response 28
Just to provide more context. Its happening to all my customers ever since ive replaced the firewall and only replace the firewall.We've never opened UDP for RDP. Its always TCP infact we've hard coded for TCP. So to be clear its NOT a network issue - meaning its not internet services or anything like as there's no CRC errors reported on any of the interfaces - including at our customerS sites.We did install a wireguard VPN and that seem to stop the drop outs. The Wireguard does allow UDP traffic but its also non NATed traffic. Thats ok from that at their Office - but not home users.PS: we increased the timeout for UDP as the very first options. ---

## Response 29
It is a PITA, but would you be able to start capturing traffic using Wireshark at both the RDP server and the RDP client (filtering on tcp to/from the address of the remote one as seen locally plus icmp from any source), set up the connection, stop the sniffing once the connection breaks, and then compare the last, say, 200 packets of the connection from both ends? There should be some failed retransmission attempts that might hint where to dig further. ---

## Response 30
Thats like really hard.. You cant just add wireshark on a switchin without all the configuration of ensuing we setup a "mirroring/monitoring" port. Surely others must have also experienced the same drop outs on TCP RDP traffic ---

## Response 31
I know nothing about multiple WANIPs coming in a single port, but think using srcnat to direct where the servers are sending traffic to is the wrong approach??Or did I just misunderstand the intent of sourcenat for this niche case???As i want to also want to have traffic that's leaving that server to be coming from its own public IP - i also have a SCRNAT.add action=src-nat chain=srcnat comment= "(Rule 249)" out-interface=sfp1 \src-address=192.168.200.64 to-addresses=PublicAddress.01As with the rest of my suggestions, consider only and do not change anything as others may have appropriate feedback to confirm or refute them!I will now look at the config.1. Set this toNONE, it is known to cause weird issues, probably not yours but no harm in setting to none!!!/interface detect-internetset detect-interface-list=WAN internet-interface-list=WAN lan-interface-list=\LAN wan-interface-list=WAN2. AVOID making port forwarding rules in both forward chain and dstnat chain.Forward chain only needs one allow rule for dstnat. KISS !!Also, due to queuing I think the fast track rule should be disabled./ip firewall address-listadd address=192.168.0.X list=Authorizedcomment="local admin desktop - static dhcp lease"add address=192.168.0.AB list=Authorized comment="local admin wifi device - static DHCP lease"add address=192.168.1.Y list=Authorized comment="remote admin device - wg"etc. as required./ip firewall filteradd action=accept chain=input connection-state=established, related, untrackedadd action=drop chain=input comment="defconf: drop invalid" connection-state=invalidadd action=accept chain=input protocol=icmpadd action=accept chain=input comment="admin access" src-address-list=Authorizedadd action=accept chain=input comment="users to services" in-interface-list=LAN dst-port=53 protocol=udpadd action=accept chain=input comment="users to services" in-interface-list=LAN dst-port=53 protocol=tcpadd action=drop chain=input comment="drop all else"+++++++++++++++++++add action=fasttrack-connection chain=forwarddisabled=yescomment=\"fasttrack - disables QUEUES bandwidth" connection-state=\established, related hw-offload=yesadd action=accept chain=forward comment="=====established, related, untracked" \connection-state=established, related, untrackedlog-prefix="RULE 60 Establish"add action=drop chain=forward comment="Drop invalid connections" \connection-state=invalid log=yes log-prefix="Drop invalid"add action=accept chain=forward comment="internet traffic" in-interface-list=LAN out-interface-list=WANadd action=accept chain=forward comment="port forwarding" connection-nat-state=dstnatadd action=accept chain=forward comment="wireguard admin to LAN" in-interface=WG_Interface dst-address=192.168.0.0/24add action=drop chain=forward comment="drop all else"Note I didnt understand the following rule and thus have a more standard allow LAN to WAN rule for LAN users above.add action=accept chain=forward dst-port=80, 443, 25, 53, 21 out-interface=sfp1 protocol=tcp \src-address-list=TERMINALSERVICES comment="Rule 210 - default Internet browsing"There is no reason why an RDP server is initiating/originating any traffic to the internet ???????????3. For all the dstnat rules, remove the in-interface=sfp1For static WANIPS, only the dst-address of the WAN is required.4. To go along with initial comments above.I believe you need to mangle at least for traffic to servers from externala. traffic to to the router over each WAN to dst ports and servers should be marked ( connection and then routing) to go out same WANThus regardless of server they are going to, the WAN used to come in, will be the WAN return server traffic goes back out.Question: How do external users know which WAN to connect to. I am assuming they all have a particular DYNDNS they have been given which corresponds to a specific WANIP.OR users are given the actual static WANIP. In which case, the router mangling will ensure traffic hitting the server on that WANIP goes back out the same WANIP. Isnt that the simplest approach?Thus need special routes for each of the WAN Ips and a table as well.+++++++++++++++++++++You have a lot of extra paranoi rules on the firewall which were removed but will add back in some raw rules./ip firewall address-listadd address=countryIPAustralia...1 list=PERMITTEDadd address=countryIPAustralia...n list=PERMITTEDadd address=TS-WHITE LIST....1 list=PERMITTEDadd address=TS-WHITE LIST....n list=PERMITTED(every DST NAT RULE should have a src-address-list=PERMITTED or at least one of the individual ones, either white list or IPAustralia)To be used with caution......../ip firewall rawadd action=drop chain=prerouting comment="drop inbound without legit source address" in-interface=sfp1 src-address-list=not_in_internet/ip firewall rawadd chain=prerouting action=drop comment="drop inbound not trusted to servers" in-interface=sfp1 dst-port=ServerPorts src-address-list=!PERMITTED/ip firewall rawadd chain=prerouting action=drop comment="drop inbound to non-existing local WANIP" in-interface=sfp1 dst-address-list=!complete_list_local_WAN_IPs{ where list=200.200.200.30-200.200.200.58 }/ip firewall rawadd action=drop chain=prerouting comment="drop non-legit traffic coming from LAN" in-interface-list=LAN src-address-list=!expected-address-from-LAN \{ in this case could simply be 192.168.0.0/24 but I would make a list that includes the wireguard subnet as well ) ---