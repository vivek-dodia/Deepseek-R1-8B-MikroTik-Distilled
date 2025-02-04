# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212727

# Discussion

## Initial Question
Author: Fri Nov 22, 2024 7:21 am
``` # 2024-11-22 06:19:30 by RouterOS 7.16.1# software id =## model =# serial number =/interfacebridgeaddadmin-mac=auto-mac=nocomment=defconf name=bridge/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacewifi configurationaddcountry=Polanddisabled=noname=cfg1 security.authentication-types=\ wpa2-psk, wpa3-psk ssid=gromek/interfacewifiset[finddefault-name=wifi1]channel.band=5ghz-ax.skip-dfs-channels=\10min-cac.width=20/40/80mhzconfiguration=cfg1 configuration.mode=ap \ disabled=nosecurity.authentication-types=wpa2-psk, wpa3-psk.ft=yes \.ft-over-ds=yesset[finddefault-name=wifi2]channel.band=2ghz-ax.skip-dfs-channels=\10min-cac.width=20/40mhzconfiguration=cfg1 configuration.mode=ap \ disabled=nosecurity.ft=yes.ft-over-ds=yes/ip pooladdname=default-dhcp ranges=192.168.88.10-192.168.88.254/ip dhcp-serveraddaddress-pool=default-dhcpinterface=bridge name=defconf/disk settingssetauto-media-interface=bridgeauto-media-sharing=yesauto-smb-sharing=yes/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=ether1addbridge=bridge comment=defconfinterface=wifi1addbridge=bridge comment=defconfinterface=wifi2/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether5 list=WAN/interfacewifi provisioningaddaction=create-dynamic-enabled disabled=nomaster-configuration=cfg1/ip addressaddaddress=192.168.88.1/24comment=defconfinterface=bridge network=\192.168.88.0addaddress=10.221.215.2/24interface=ether5 network=10.221.215.0/ip dhcp-clientaddcomment=defconfinterface=ether5/ip dhcp-server networkaddaddress=192.168.88.0/24comment=defconf dns-server=192.168.88.1gateway=\192.168.88.1/ip dnssetallow-remote-requests=yes servers=1.1.1.1/ip dnsstaticaddaddress=192.168.88.1comment=defconf name=router.lan type=A/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established, related, untracked"connection-state=\ established, related, untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\ invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\ ipsec-policy=in, ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\ ipsec-policy=out, ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\ connection-state=established, related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established, related, untracked"connection-state=\ established, related, untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\ connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \ connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\ ipsec-policy=out, noneout-interface-list=WAN/ip routeadddisabled=nodst-address=0.0.0.0/0gateway=10.221.215.1routing-table=main \ suppress-hw-offload=no/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established, related, untracked"connection-state=\ established, related, untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\ invalidaddaction=accept chain=input comment="defconf: accept ICMPv6"protocol=\ icmpv6addaction=accept chain=input comment="defconf: accept UDP traceroute"\ dst-port=33434-33534protocol=udpaddaction=accept chain=input comment=\"defconf: accept DHCPv6-Client prefix delegation."dst-port=546protocol=\ udp src-address=fe80::/10addaction=accept chain=input comment="defconf: accept IKE"dst-port=500, 4500\ protocol=udpaddaction=accept chain=input comment="defconf: accept ipsec AH"protocol=\ ipsec-ahaddaction=accept chain=input comment="defconf: accept ipsec ESP"protocol=\ ipsec-espaddaction=accept chain=input comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in, ipsecaddaction=drop chain=input comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LANaddaction=accept chain=forward comment=\"defconf: accept established, related, untracked"connection-state=\ established, related, untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\ connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop packets with bad src ipv6"src-address-list=bad_ipv6addaction=drop chain=forward comment=\"defconf: drop packets with bad dst ipv6"dst-address-list=bad_ipv6addaction=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1"\ hop-limit=equal:1protocol=icmpv6addaction=accept chain=forward comment="defconf: accept ICMPv6"protocol=\ icmpv6addaction=accept chain=forward comment="defconf: accept HIP"protocol=139addaction=accept chain=forward comment="defconf: accept IKE"dst-port=\500, 4500protocol=udpaddaction=accept chain=forward comment="defconf: accept ipsec AH"protocol=\ ipsec-ahaddaction=accept chain=forward comment="defconf: accept ipsec ESP"protocol=\ ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in, ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/system clocksettime-zone-name=Europe/Warsaw/system notesetshow-at-login=no/system routerboard mode-buttonsetenabled=yes on-event=dark-mode/system routerboard wps-buttonsetenabled=yes on-event=wps-accept/system scriptaddcomment=defconf dont-require-permissions=noname=dark-mode owner=*sys \ policy=ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon \ source="\r\ \n :if ([system leds settings get all-leds-off] = \"never\") do={\r\ \n /system leds settings set all-leds-off=immediate \r\ \n } else={\r\ \n /system leds settings set all-leds-off=never \r\ \n }\r\ \n "addcomment=defconf dont-require-permissions=noname=wps-accept owner=*sys \ policy=ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon \ source="\r\ \n :foreach iface in=[/interface/wifi find where (configuration.mode=\"a\ p\" && disabled=no)] do={\r\ \n /interface/wifi wps-push-button \$iface;}\r\ \n "/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN ``` I think I managed to set it up. I have reset the config and started from sratch via winbox (no Quick Set this time).I have set it up on ether5.So I changed the following:Interface List WAN -> replaced ether1 with ether5bridge ports -> replaced ether5 with ether1IP DHCP Client: change client to ether5I have also added the internet provider required setup (IP address, gateway).It seems to work fine.Can you please check the setup if I am missing something or maybe I can improve anything?
```
---
```

## Response 1
Author: Fri Nov 22, 2024 7:49 am
``` /ip addressprint ``` It looks mostly fine to me, the only thing you should re-check is:/ip addressadd address=192.168.88.1/24 comment=defconf interface=bridge network=\192.168.88.0add address=10.221.215.2/24interface=ether5network=10.221.215.0/ip dhcp-clientadd comment=defconfinterface=ether5ether5 hasbotha static address and a dhcp client running.Open a terminal and issue the command:
```
cannot say if ether5 gets two addresses or not, in any case (and your ISP modem/router settings are involved in this) if there is a DHCP server running on the ISP modem/router you don't need the static address or viceversa, if there is no DHCP server running you can remove or disable the dhcp client.If you do not need all 4 ports in the bridge a common advice is to keep a port (unused) outside of the bridge for emergency connection, but it is of minor relevance.


---
```

## Response 2
Author: Fri Nov 22, 2024 7:58 am
``` Flags:D-DYNAMICColumns:ADDRESS, NETWORK, INTERFACE# ADDRESS NETWORK INTERFACE;;;defconf0192.168.88.1/24192.168.88.0bridge110.221.215.2/2410.221.215.0ether52D10.221.215.118/2410.221.215.0ether5 ``` ``` Columns:ADDRESS, NETWORK, INTERFACE# ADDRESS NETWORK INTERFACE;;;defconf0192.168.88.1/24192.168.88.0bridge110.221.215.2/2410.221.215.0ether5 ``` It looks mostly fine to meThanks a lot for checking!
```
After disabling DHCP client it shows like this:
```

```
---
```

## Response 3
Author: Fri Nov 22, 2024 11:07 am
``` /ip routeprint ``` Yep, but you probably should do the reverse.Remove the static address and let the DHCP client run.Since the DHCP server is managed (I believe) by your ISP if they change it (for whatever reason) to another subnet your static assigned address will become m00t.Moreover the DHCP server will provide other data (DNS) and it will (should) add a default route (whichbeing dynamic should have distance 0normally have distance 1, i.e. havethe maximuma rather highpriority), as well in case of changes your static settings may become invalid.Try checking "as is" the command:
```
thenre-enable the dhcp client (leave the static address enabled) and check the routes again.If you have a dynamic route with distance01, you can disable the static one you have and then disable also the static address of ether5, as everything will be managed by the DHCP server on the ISP modem/router.EDIT: corrected wrong distance on dhcp originated routes


---
```

## Response 4
Author: Fri Nov 22, 2024 1:58 pm
``` Flags:D-DYNAMIC;A-ACTIVE;c-CONNECT, s-STATICColumns:DST-ADDRESS, GATEWAY, DISTANCE# DST-ADDRESS GATEWAY DISTANCE0As0.0.0.0/010.221.215.11DAc10.221.215.0/24ether50DAc192.168.88.0/24bridge0 ``` ``` Flags:D-DYNAMIC;A-ACTIVE;c-CONNECT, s-STATIC, d-DHCP;+-ECMPColumns:DST-ADDRESS, GATEWAY, DISTANCE# DST-ADDRESS GATEWAY DISTANCE0As+0.0.0.0/010.221.215.11DAd+0.0.0.0/010.221.215.11DAc+10.221.215.0/24ether50DAc+10.221.215.0/24ether50DAc192.168.88.0/24bridge0 ``` Try checking "as is" the command:
```
then re-enable the dhcp client (leave the static address enabled) and check the routes again.
```

```
I should delete this AP address, that I have added manually? So this one here?MT_IP.jpg


---
```

## Response 5
Author: [SOLVED]Fri Nov 22, 2024 5:06 pm
``` lags:D-DYNAMIC;A-ACTIVE;c-CONNECT, s-STATIC, d-DHCP;+-ECMPColumns:DST-ADDRESS, GATEWAY, DISTANCE# DST-ADDRESS GATEWAY DISTANCEDAd0.0.0.0/010.221.215.11DAc10.221.215.0/24ether50DAc192.168.88.0/24bridge0 ``` Yes, that one (with no marker) is static, the one below it is coming from the DHCP and is marked with D (Dynamic).And then you can remove the (only) static rule, the markings on the first:# DST-ADDRESS GATEWAY DISTANCE0 As+ 0.0.0.0/0 10.221.215.1 1mean that it is #0 (i.e. you can remove it) then A (Active) and s (static)The one below has no # (meaning that you cannot remove it), then D (Dynamic) A (Active) and d (coming from dhcp):DAd+ 0.0.0.0/0 10.221.215.1 1Both have distance 1 (I remembered wrongly that dhcp originated routes had 0, the DAc ones have it) and point to the same destination address (0.0.0.0/0, i.e. *everything*) so they have the little + sign that essentially means that they are the same.then you have three other routes:DAc+ 10.221.215.0/24 ether5 0DAc+ 10.221.215.0/24 ether5 0DAc 192.168.88.0/24 bridge 0all D (Dynamic) A (Active) c (connected), the first two of them are a consequence of the two Ip addresses you have (one Static 10.221.215.2/234, one Dynamic 10.221.215.119/24), and as well have the + sign because both lead to the same destination (10.221.215.0/24), the third one is the consequence of the static address you have on the bridge.Once you will have removed the static address on ether1 and the static route, /ip route print should show just three routes like:
```
clear and simple, and all dynamic.


---
```

## Response 6
Author: Mon Nov 25, 2024 4:44 pm
``` Flags:D-DYNAMIC;A-ACTIVE;c-CONNECT, s-STATIC, d-DHCP;+-ECMPColumns:DST-ADDRESS, GATEWAY, DISTANCE# DST-ADDRESS GATEWAY DISTANCE0As+0.0.0.0/010.221.215.11DAd+0.0.0.0/010.221.215.11DAc10.221.215.0/24ether50DAc192.168.88.0/24bridge0 ``` Static IP address removed.DCH client enabled.IP route shows the following:
```
---
```

## Response 7
Author: Mon Nov 25, 2024 4:54 pm
``` Flags:D-DYNAMIC;A-ACTIVE;c-CONNECT, d-DHCPColumns:DST-ADDRESS, GATEWAY, DISTANCE DST-ADDRESS GATEWAY DISTANCEDAd0.0.0.0/010.221.215.11DAc10.221.215.0/24ether50DAc192.168.88.0/24bridge0 ``` I have also deleted now this one entry here:MT_ROUTE gateway.jpgAnd now ip route shows as you have described it:
```
THANK YOU!!!
```