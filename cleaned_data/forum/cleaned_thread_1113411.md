# Thread Information
Title: Thread-1113411
Section: RouterOS
Thread ID: 1113411

# Discussion

## Initial Question
Ive just got SXT LTE Kit. Standard setup works absolutely great. But the main router (RB3011) needs the LTE WAN address in my setup so Ive tried using passthrough mode and it works to a point but I cant actually get any working internet over the interface.Ive setup SXT on my LAN by using DHCP client on the SXT bridge with eth1+2 so I can get to it easy for configuration. Ive then setup EoIP between SXT and RB3011 with EoIP as the passthrough interface and on the RB3011 a DHCP-CLIENT.DHCP client on RB3011 gets the LTE WAN addresses as expected but I cant get any traffic or working internet over it. Ive got masquerading on the EoIP interface on the RB3011 and appropriate routes setup. It should work but doesn't.Ive also tried using eth2 on the SXT as passthrough port and a wire to the RB3011 - same issue.What am I doing wrong? Anyone any experience, any gotchas with this type of setup? ---

## Response 1
Which RouterOS version do you have on both devices ?I have a WAP LTE Kit connected to an OPNSense firewall, which lost internet access after upgrading to RoS 6.43. After that, i did a downgrade back to 6.42.7 and the connection was back online.I think this change in 6.43 caused or is related to the issue:*) lte - use "/32" address for the Passthrough feature when R11e-LTE module is used;With 6.43 the network interface of the opnsense gets a /32 IP-adress, with 6.42.7 it's a /28.So, if you are on 6.43 try a downgrade to 6.42.7 on the SXT LTE ---

## Response 2
Better print here diagram and export your config with hiding sensitive info. ---

## Response 3
Well spotted about the /32 addressing.I just noticed that 6.44beta6 was out and guess what is in the release notes:lte - fixed DHCP relay packet forwarding when in passthrough mode;Will test and report back. ---

## Response 4
Doesnt work with 6.44beta6 or 6.42.7 or 6.43Heres my export:[admin@SXT-LTE] > export# sep/12/2018 23:51:56 by RouterOS 6.42.7# software id = CF7Q-26RP## model = RBSXTR# serial number = XXXXXXXXXXXXXX/interface bridgeadd admin-mac=B8:69:F4:01:2F:47 auto-mac=no comment=defconf name=bridge/interface eoipadd mac-address=02:97:27:9C:A5:46 name=eoip-tunnel1 remote-address=172.16.123.1 tunnel-id=4/interface listadd comment=defconf name=WANadd comment=defconf name=LAN/interface lte apnset [ find default=yes ] default-route-distance=1add apn=internet name=bridge-to-ether passthrough-interface=eoip-tunnel1 passthrough-mac=auto/interface lteset [ find ] apn-profiles=bridge-to-ether mac-address=AC:FF:FF:00:00:00 mtu=1500 name=lte1/interface wireless security-profilesset [ find default=yes ] supplicant-identity=MikroTik/ip hotspot profileset [ find default=yes ] html-directory=flash/hotspot/ip pooladd name=default-dhcp ranges=192.168.88.10-192.168.88.254/ip dhcp-serveradd address-pool=default-dhcp interface=bridge name=defconf/interface bridge portadd bridge=bridge comment=defconf interface=ether1add bridge=bridge comment=defconf interface=ether2/ip neighbor discovery-settingsset discover-interface-list=LAN/interface list memberadd comment=defconf interface=bridge list=LANadd comment=defconf disabled=yes interface=lte1 list=WANadd interface=ether1 list=LANadd interface=ether2 list=LAN/ip addressadd address=192.168.88.1/24 comment=defconf disabled=yes interface=bridge network=192.168.88.0/ip dhcp-clientadd default-route-distance=2 dhcp-options=hostname, clientid disabled=no interface=bridge/ip dhcp-server networkadd address=192.168.88.0/24 comment=defconf gateway=192.168.88.1/ip dnsset allow-remote-requests=yes/ip dns staticadd address=192.168.88.1 name=router.lan/ip firewall filteradd action=accept chain=input comment="defconf: accept established, related, untracked" connection-state=established, related, untrackedadd action=drop chain=input comment="defconf: drop invalid" connection-state=invalidadd action=accept chain=input comment="defconf: accept ICMP" protocol=icmpadd action=drop chain=input comment="defconf: drop all not coming from LAN" in-interface-list=!LANadd action=accept chain=forward comment="defconf: accept in ipsec policy" ipsec-policy=in, ipsecadd action=accept chain=forward comment="defconf: accept out ipsec policy" ipsec-policy=out, ipsecadd action=fasttrack-connection chain=forward comment="defconf: fasttrack" connection-state=established, relatedadd action=accept chain=forward comment="defconf: accept established, related, untracked" connection-state=established, related, untrackedadd action=drop chain=forward comment="defconf: drop invalid" connection-state=invalidadd action=drop chain=forward comment="defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat connection-state=new in-interface-list=\WAN/ip firewall natadd action=masquerade chain=srcnat comment="defconf: masquerade" ipsec-policy=out, none out-interface-list=WAN/system clockset time-zone-name=Europe/London/system identityset name=SXT-LTE/system leds# using RSRP, modem-signal-treshold ignoredset 0 interface=lte1 type=modem-signal/system loggingadd topics=lte,!rawadd disabled=yes topics=debug/system routerboard settingsset auto-upgrade=yes silent-boot=no/tool mac-serverset allowed-interface-list=LAN/tool mac-server mac-winboxset allowed-interface-list=LAN[admin@SXT-LTE] > ---

## Response 5
Just wanted to ping this as Im still know where on with this.The setup is real simple. SXT-LTE and RB3011 on same /24 subnet. SXT-LTE on .4 and RB3011 on .1. There is EoIP tunnel between the two with the tunnel interface selected as the passthrough interface on the SXT-LTE APN. DHCP client sat on the corresponding EoIP interface on the RB3011.Ive tried many many things to no avail. Has anyone any experience with this. Mikrotik support said they set this up and it worked so Im stumped as to what I might be doing wrong.If I setup the SXT-LTE in the traditional way traffic flows nicely. ---

## Response 6
Yeah I'm not sure, I'm no expert, but your config looks right...but passthrough is pretty weird, too. You can try setting the MAC address in the APN, that might help, but not sure. Whenever I've tried to do something, other than assign passthrough to a physical port, it never "just" worked - but setting the MAC address almost always worked (although if MAC isn't always known, you can't just set it in the APN)The end of this video speak of an alternative approach to use passthrough on your ethernet jack, with mgmt LAN as a VLAN on top:https://www.youtube.com/watch?v=BSJrplxIs6w&t=1534sBasically it reverses your EoIP approach...use ether1 as passthrough, but add a VLAN with management lan. That video also give a clue at what's going on under-the-covers with LTE passthrough. ---

## Response 7
I got passthrough working on a brand new setup. LHG-LTE6 with Audience. I set it up as ether1 passthrough and a vlan for management. Worked first time.Tried the same setup on the SXT-LTE + RB3011 and still no traffic flow but DHCP received the WAN address as before. So scratching head. I happened to have a new hAPac2 so I set that up with the SXT-LTE and it works! Sooooo... Its something on the RB3011. Ive no idea what could stop it working. ---

## Response 8
Just revisiting this as I have an office wanting a 4G connection. They have RB3011 with very basic config - no joy getting it to work. Been trying all sorts with my own RB3011 - no joy. ** BRIDGING DOES NOT WORK WITH RB3011 ** and I suspect others too! The strangest thing is that when you torch the port on the router (RB3011) you only see the vlan traffic after he initial wan DHCP exchange. When I run a ping from the port I don't see it in torch.I wish Mikrotik support would pitch in on this. Ive been using port 10 as that conveniently has PoE on it and is for this exact purpose. I also tried port 9. I should try port 5 and port 1 too. I'll report back on those. I have spare RB2011, need to test with that too.Where I have got this to work with other Tiks, the best setup seems to be minimal settings on the LTE end - ether1 assigned as bridge port in LTE APN and vlan hanging off ether1 with DHCP client or fixed address for admin. At router end, a port not part of the bridge with DHCP client on it to receive LTE wan address, and hanging off that a matching vlan for admin, and this vlan can be added to the local bridge.But what's going on with RB3011? I even tried putting a switch in between but then nothing worked which in itself is a bit odd. For sanity check I had hap ac2 with default config, port 1 as wan and mods as above for admin, and that worked.What is everyone else experience? ---

## Response 9
For administration, you tried using a loopback interface?Regards. ---

## Response 10
Just revisiting this as I have an office wanting a 4G connection. They have RB3011 with very basic config - no joy getting it to work. Been trying all sorts with my own RB3011 - no joy. ** BRIDGING DOES NOT WORK WITH RB3011 ** and I suspect others too! The strangest thing is that when you torch the port on the router (RB3011) you only see the vlan traffic after he initial wan DHCP exchange. When I run a ping from the port I don't see it in torch.I wish Mikrotik support would pitch in on this. Ive been using port 10 as that conveniently has PoE on it and is for this exact purpose. I also tried port 9. I should try port 5 and port 1 too. I'll report back on those. I have spare RB2011, need to test with that too.Where I have got this to work with other Tiks, the best setup seems to be minimal settings on the LTE end - ether1 assigned as bridge port in LTE APN and vlan hanging off ether1 with DHCP client or fixed address for admin. At router end, a port not part of the bridge with DHCP client on it to receive LTE wan address, and hanging off that a matching vlan for admin, and this vlan can be added to the local bridge.But what's going on with RB3011? I even tried putting a switch in between but then nothing worked which in itself is a bit odd. For sanity check I had hap ac2 with default config, port 1 as wan and mods as above for admin, and that worked.What is everyone else experience?LTE firmware is updated?for check:
```
/interfacelte firmware-upgrade lte1for run the upgrade
```

```
/interfacelte firmware-upgrade lte1 upgrade=yesFor me all is working as expected:LTE side SXT R have 6.46.8 on both RouterOS and RouterBOOT, LTE firmware is MikroTik_CP_2.160.000_v018
```

```
/interfacevlanaddinterface=ether1 name=vlan1 vlan-id=10/interfacelte apnaddapn=mobile.vodafone.it name="test passthrough"passthrough-interface=vlan1 passthrough-mac=autopassthrough-subnet-selection=p2p/interfacelteset[find]apn-profiles="test passthrough"band=1,3,7,20mac-address=AC:FF:FF:00:00:00name=lte1 network-mode=lte

---
```

## Response 11
Ok interesting - you are using the vlan for the wan passthrough not ether1 itself? Im sure I tried this combination and it didnt work. I will try...About LTE firmware Im on R11e-LTE6_V027 (I updated my R11e card in SXT-R) the SXT is currently on 6.49beta44, Ive tried all versions. I guess I could roll back to same as yours.Update: Tried it. Doesn't work. I noted you had p2p selected in the APN but Ive tried auto and p2p in every configuration Ive tried ---

## Response 12
RB3011 is just netinstalled on 6.47.9 for you...Try to do the same... ---

## Response 13
I managed to get hold of CCR1009-7G-1C-1S+. Works first time with my standard config on the SXT-LTE6 which is ether1 as passthrough port, and vlan hanging off that for management!Next I will try to default the RB3011 and try again. ---

## Response 14
Further info on this.The problem seems to be when you have LTE passthorugh as a second WAN. Ive tested on several devices now and when you have a LTE or DHCP or PPPOE primary wan (distance=1) and then add an LTE connection as backup (distance=2) then it doesnt work, no traffic flows.Even using /tool ping to say 8.8.8.8 and setting the interface to use as the LTE interface you get nothing accept timeout and not route to host. If I disable the primary WAN then it suddenly springs to life.This is odd because Ive had PPTP WANs setup for years and Im able to use /tool ping on any of those and ping works as expected. I can even route single devices on the LAN to use those VPNs for outbound traffic but the same rules dont work for an LTE passthrough WAN.Is this some undocumented routing table quirk? ---

## Response 15
I konw this is an old post but just for the record, setting passthrough mode as p2p in apn setting under lte interface menu, might solve this problem. ---