# Thread Information
Title: Thread-1122270
Section: RouterOS
Thread ID: 1122270

# Discussion

## Initial Question
Hi, I am using a RB760iGS running 7.16.2 packages and firmware.I have a LAN bridge configured on ether2&3 and the SFP socket subnet 172.16.23.0/24I have a DMZ configured on ether4 subnet 172.16.24.0/28I have a Raspberry pi running Network UPS Tools on 172.16.23.4:3493 and I am trying (without any sucess) to allow a NUT Client on my Ubuntu server (172.16.24.in the DMZ to communicate to the RPi.I used to run OpnSense firewall and this was known as a pinhole between networks and was easy to setup through the web interface as it would write the firewall rules for you.The firewall rules from the config are below. I am sure its something simple that my lack of knowledge is missing or knowing the right phrase to search for. Any help would be greatly appreciated. If there are any good references for learning the RouterOS firewall that would be great as I am using a lot of the hex routers for work and seem to be muddling through.
```
/ip firewall filteraddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=forwardin-interface-list=DMZaddaction=accept chain=input comment="defconf: accept ICMP"\in-bridge-port-list=LAN protocol=icmpaddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=accept chain=input comment="OVPN Pass"dst-port=1194protocol=tcpaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward connection-state=newin-interface="DMZ Port"\out-interface=LAN_bridgeaddaction=drop chain=forwardin-interface=ether5out-interface=LAN_bridgeaddaction=drop chain=forwardin-interface=VLAN_SCS_WORKSHOPout-interface=\
    LAN_bridgeaddaction=drop chain=forwardin-interface=VLAN_SCS_WAN2out-interface=\
    LAN_bridgeaddaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WANaddaction=drop chain=input dst-port=53in-interface=ether1 protocol=tcpaddaction=drop chain=input dst-port=53in-interface=ether1 protocol=udp/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WANaddaction=dst-nat chain=dstnat comment="NAT Incoming Mail "dst-address=\212.159.16.166dst-port=587protocol=tcp to-addresses=172.16.24.8\
    to-ports=587addaction=dst-nat chain=dstnat comment="NAT SMTPS Incoming Mail "\
    dst-address=212.159.16.166dst-port=465protocol=tcp to-addresses=\172.16.24.8to-ports=465addaction=dst-nat chain=dstnat comment="NAT SMTP Incoming Mail "\
    dst-address=212.159.16.166dst-port=25protocol=tcp to-addresses=\172.16.24.8to-ports=25addaction=dst-nat chain=dstnat comment="NAT HTTP to the web server"\
    dst-address=212.159.16.166dst-port=80protocol=tcp to-addresses=\172.16.24.8to-ports=80addaction=dst-nat chain=dstnat comment=\"NAT HTTP to the web server for webmail"dst-address=212.159.16.166\
    dst-port=8081protocol=tcp to-addresses=172.16.24.8to-ports=8081addaction=dst-nat chain=dstnat dst-address=212.159.16.166dst-port=110\
    protocol=tcp to-addresses=172.16.24.8to-ports=110addaction=dst-nat chain=dstnat dst-address=212.159.16.166dst-port=143\
    protocol=tcp to-addresses=172.16.24.8to-ports=143addaction=dst-nat chain=dstnat comment="NAT IMAP to mail Server "\
    dst-address=212.159.16.166dst-port=993protocol=tcp to-addresses=\172.16.24.8to-ports=993addaction=dst-nat chain=dstnat comment="NAT HTTPS to Web Server "\
    dst-address=212.159.16.166dst-port=443protocol=tcp to-addresses=\172.16.24.8to-ports=443addaction=masquerade chain=srcnatout-interface=ether1

---
```

## Response 1
Detailed network diagram would help understand. ---

## Response 2
Hi, Network diagram attached. ---

## Response 3
So you have servers on one subnet.a. are users coming to the servers from external?b. are users coming from same subnet as servers?c. are users coming from the other subnet (where pi is located)So no traffic ORIGINATED at severs, only responses to incoming requests??( except for NUT client originating traffic to PI ??? ).Full config required./export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc. ) ---

## Response 4
Hi, The servers are web and mail. They have traffic from WAN and LAN going to DMZ. User PCs, NAS, and general LAN is where the pi is located. The only thing originated from the server would be outboud mail but all of that is working fine with dst-nat.NUT client is running on the server to monitor the UPS for power failure. The NUT server is running on the Pi in the LAN. This is a home network so I have 1 ups running the LAN side and the 1 small web and mail server.Config file attached.Thanks for your help ---

## Response 5
When you are willing to change your config to the optimal one bridge approach - all vlans associated with bridge, will be happy to assist.viewtopic.php?t=143620 ---

## Response 6
Thanks but I am looking for help on firewall rules not rebuilding the config.There seems to be many ways to configure the RouterOS and your answer seems a bit "my way is best" and misses the question completely. ---

## Response 7
Understood, no worries. Most are not picky like me. ---

## Response 8
There seems to be many ways to configure the RouterOS and your answer seems a bit "my way is best" and misses the question completely.You misunderstand, @anav was polite whereas I will say "your way is worse and you've killed your performance",seeLayer2 misconfiguration - Bridges on a single switch chipMT forum users generally ignore bad practice requests. ---

## Response 9
No offence was intended to anyone.@anav - thanks for the information regarding VLANs. It was my misunderstanding of the hardware I am using, i presumed each port was a separtate NIC instead of part of a switch.@ConradPino - thanks for pointing out in a more blunt and to the point way that my current config and config design principles are killing the performance of the router.I have taken onboard the principles and am working to build a new config.Is dsnat still the prefered method for allowing WAN access to servers / services (web and mail) within a VLAN or is there a better solution? ---

## Response 10
The party line:https://www.youtube.com/watch?v=a_8AV6vIDYQhttps://www.youtube.com/shorts/LEjg54S_C0Mhttps://www.youtube.com/watch?v=-kNHtlOb5n0&t=52s ---

## Response 11
I am working on rebuilding the config and wondered if there were any examples of how to make this more granular?# Allow VLANs to access router services like DNS, Winbox. Naturally, you SHOULD make it more granular.add chain=input action=accept in-interface-list=VLAN comment="Allow VLAN" ---

## Response 12
Do I have to explicitly create drop firewall rules to stop traffic between vlans?How do I allow the OpenVPN Client access to the LAN? I had this working in the old bad method not using VLANs, copied the config over and I am not able to access clients on the LAN side through the VPN as I did. ---

## Response 13
Everything was looking normal until you decided to add an undocumented immigrant in your config.Where did vlan16 come from??Also you stated you want nut client to reach pi...... dmz to lan.however in the diagram it states nut client LISTENing on port 3498, which IMPLIES that the pi is going to contact the nut client on that port, not the other way round???I dont see any opvn settings on the router input chain aka port?? Assuming this is a router service how do you expect to connect??.Too many interface lists for needs described/ip interfaceadd name=WANadd name=LANadd name=TRUSTED/interface list membersadd interface=ether1 list=WANadd interface=LAN_VLAN list=LANadd interface=DMZ_VLAN list=LANadd interface=LAN_VLAN list=TRUSTEDadd interface=OpenVPN_CLient list=TRUSTED/ip firewall address-listadd address=192.168.100.X list=Authorizedcomment="local admin device 1"add address=192.168.100.Y list=Authorized comment="local admin device 2"add address=OVPN address ( or subnet ) list=Authorized comment="admin remote vpn"/ip firewall filteradd action=accept chain=input connection-state=established, related, untrackedadd action=drop chain=input connection-state=invalidadd action=accept chain=input protocol=icmp { enabled !! }add action=accept chain=input in-interface-list=TRUSTEDsrc-address-list=Authorizedadd action=accept chain=input comment="users to services" dst-port=53 in-interface-list=LAN protocol=udpadd action=accept chain=input comment="users to services" dst-port=53 in-interface-list=LAN protocol=tcpadd action=drop chain=input comment="Drop all else" { add this rule last }add action=fasttrack-connection chain=forward connection-state=established, related hw-offload=yesadd action=accept chain=forward connection-state=established, related, untrackedadd action=drop chain=forward connection-state=invalidadd action=accept chain=forward comment="internet traffic" in-interface-list=LAN out-interface-list=WANadd action=accept chain=forward comment="nut client to pi" in-interface=DMZ_VLAN src-address=172.16.24.8/32 out-interface=LAN_VLAN dst-address=172.16.23.4/32add action=accept chain=forward comment="admin to LAN" in-interface-list=TRUSTED src-address-list=Authorized out-interface-list=LANadd action=accept chain=forward comment="port forwarding" connection-nat-state=dstnatadd action=drop chain=forward comment="Drop all else"ether5 removed until vlan16 mystery cleared up, but missing sfp1/interface bridge portadd bridge=br1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged interface=ether2 pvid=10add bridge=br1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged interface=ether3 pvid=10add bridge=br1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged interface=ether4 pvid=20add bridge=br1 ingress-filtering=yes frame-types=admit-only-vlan-taggedinterface=spf1 comment="trunk to switch"/interface bridge vlanadd bridge=br1 tagged=br1, sfp1 untagged=ether2, ether3 vlan-ids=10add bridge=br1 tagged=br1, sfp1 untagged=ether4 vlan-ids=20/tool mac-serverset allowed-interface-list=none/tool mac-server mac-winboxset allowed-interface-list=TRUSTED/ip neighbor discovery-settingsset discover-interface-list=TRUSTED ---

## Response 14
Sorry I was trying to run before i could walkEther5 is a hybrid port for some development. I have it in my current config which is we copying across.I have removed it and just stuck with the basics. If i can get that working I can add to it, hopefully... ---

## Response 15
I have removed the vpn server for the moment as its not that important.I have worked up all the VLANs etc but it doesnt seem to be working. I have loaded it onto the hex and I am not able to get traffic from the LAN to wan and DMZ to wan is very slow. WiFi on the LAN and SCS-Wireless stop completely.It is probably something really simple, fingers crossed.THanks in advance ---

## Response 16
Please post config in normal export format, its very difficult trying to read your work otherwise./export file=anynameyouwish (minus router serial number, any public WANIP information, keys etc.)Note: I read recently that auto-mac for bridge is best set to manual NOT AUTO. ---