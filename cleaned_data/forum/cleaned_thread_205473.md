# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 205473

# Discussion

## Initial Question
Author: Fri Mar 08, 2024 1:41 pm
Hello there!I recently got a single cAP ax for my homelab and am currently evaluating CAPsMAN for our office network. I got CAPsMAN setup with 3 cAP ax and everything is running smoothly so far. However, when it comes to steering neighbour groups with CAPsMAN, I am unsure if this is exptected behaviour or a possible bug. The documentation states that without explicitly configuring a steering neighbour group, a dynamic group is created with all APs with the same SSID. While this is true for my single AP setup at home, the office setup shows no neighbour group at all unless I explicitly configure it. Is this expected behaviour? ---

## Response 1
Author: Fri Mar 08, 2024 2:39 pm
Default following parameters are set in steering:neighbour-group based on SSIDrrm = yeswnm = yesIt's not because you do not see it that it is not working.That's the whole point of default values.Put it otherwise, how do you know it is not working ?Tip:open terminal and use /interface/wifi/steering/neighbor-group/printI think you will see something there. A dynamic entry. ---

## Response 2
Author: Tue Mar 12, 2024 10:51 am
``` 
```
[admin@ap001.of.kdk.network]>interface/wifi/actual-configuration/print0name="ap001.of.kdk.network-2G"l2mtu=1560mac-address=<mac>arp-timeout=autoradio-mac=<mac>configuration.mode=ap.ssid="KDK-mt".country=Germany.multicast-enhance=enabled 
   security.authentication-types=wpa2-eap,wpa3-eap.ft=yes.ft-over-ds=yes.connect-priority=0datapath.bridge=bridge 
   channel.frequency=2452.band=2ghz-ax.width=20mhzsteering.neighbor-group=ng1.rrm=yes.wnm=yes1name="ap001.of.kdk.network-5G"l2mtu=1560mac-address=<mac>arp-timeout=autoradio-mac=<mac>configuration.mode=ap.ssid="KDK-mt".country=Germany.multicast-enhance=enabled 
   security.authentication-types=wpa2-eap,wpa3-eap.ft=yes.ft-over-ds=yes.connect-priority=0datapath.bridge=bridge 
   channel.frequency=5500.band=5ghz-ax.width=20/40/80mhzsteering.neighbor-group=ng1.rrm=yes.wnm=yes2name="ap002.of.kdk.network-2G"mac-address=<mac>arp-timeout=autoradio-mac=<mac>configuration.mode=ap.ssid="KDK-mt".country=Germany.multicast-enhance=enabled 
   security.authentication-types=wpa2-eap,wpa3-eap.ft=yes.ft-over-ds=yes.connect-priority=0/1datapath.bridge=bridge 
   channel.frequency=2412.band=2ghz-ax.width=20mhzsteering.neighbor-group=ng1.rrm=yes.wnm=yes3name="ap002.of.kdk.network-5G"mac-address=<mac>arp-timeout=autoradio-mac=<mac>configuration.mode=ap.ssid="KDK-mt".country=Germany.multicast-enhance=enabled 
   security.authentication-types=wpa2-eap,wpa3-eap.ft=yes.ft-over-ds=yes.connect-priority=0/1datapath.bridge=bridge 
   channel.frequency=5260.band=5ghz-ax.width=20/40/80mhzsteering.neighbor-group=ng1.rrm=yes.wnm=yes4name="ap003.of.kdk.network-2G"mac-address=<mac>arp-timeout=autoradio-mac=<mac>configuration.mode=ap.ssid="KDK-mt".country=Germany.multicast-enhance=enabled 
   security.authentication-types=wpa2-eap,wpa3-eap.ft=yes.ft-over-ds=yes.connect-priority=0/1datapath.bridge=bridge 
   channel.frequency=2427.band=2ghz-ax.width=20mhzsteering.neighbor-group=ng1.rrm=yes.wnm=yes5name="ap003.of.kdk.network-5G"mac-address=<mac>arp-timeout=autoradio-mac=<mac>configuration.mode=ap.ssid="KDK-mt".country=Germany.multicast-enhance=enabled 
   security.authentication-types=wpa2-eap,wpa3-eap.ft=yes.ft-over-ds=yes.connect-priority=0/1datapath.bridge=bridge 
   channel.frequency=5580.band=5ghz-ax.width=20/40/80mhzsteering.neighbor-group=ng1.rrm=yes.wnm=yes
```

Hi holvoetn,that's exactly what I did. With the single AP setup at home, I can see the dynamic group when executing '/interface/wifi/steering/neighbor-group/print'. With the CAPsMAN setup, the list is empty unless I configure a neighbor-group explictly.My (sanitized) config looks like this:With 'steering.neighbor-group=ng1' a group is created and I can see all MAC addresses that are part of this group. Without this setting, no dynamic group is created.


---
```

## Response 3
Author: Tue Mar 12, 2024 1:24 pm
``` 
```
/interface/wifi/steering/neighbor-group/print
```

Silly question: the commandwhich returns an empty list is issued on the capsman device?


---
```

## Response 4
Author: Tue Mar 12, 2024 2:50 pm
Yes, in which case it is 'ap001' ---

## Response 5
Author: Tue Mar 12, 2024 3:00 pm
If you use capsman, you should check this on capsman controller.Don't set anything manual on AP since it will overwrite capsman settings. ---

## Response 6
Author: Tue Mar 12, 2024 3:12 pm
All configuration is done on the CAPsMAN controller and, like I said, did issue the command on the controller as well. Basically all I did on the CAPs was setting it into caps-mode and changed the password. ---

## Response 7
Author: Tue Mar 12, 2024 3:34 pm
Thus, am I right if I say that one of the cAP ax is the capsman controller (ap001) and the other twos are CAPs? (Sorry, I imagined that there was a 4th device involved.)Another probably silly question: how are the wifi interfaces configured on ap001? Using capsman or by directly applying the configurations to the interfaces?Moreover, do you mind to share your exported configuration? ---

## Response 8
Author: Tue Mar 12, 2024 3:44 pm
``` 
```
[admin@ap001.of.kdk.network]/interface/wifi>/export# 2024-03-12 14:41:57 by RouterOS 7.14# software id = LNBX-T6UL## model = cAPGi-5HaxD2HaxD# serial number = <serialnumber>/interfacebridgeaddadmin-mac=<mac>auto-mac=nocomment=defconf name=bridge port-cost-mode=shortvlan-filtering=yes/interfaceethernetset[finddefault-name=ether2]disabled=yes/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacewifi channeladdband=2ghz-ax disabled=nofrequency=2412name=2G_ch1 width=20mhzaddband=2ghz-ax disabled=nofrequency=2427name=2G_ch6 width=20mhzaddband=2ghz-ax disabled=nofrequency=2452name=2G_ch11 width=20mhzaddband=5ghz-ax disabled=nofrequency=5260name=5G_ch58 width=20/40/80mhzaddband=5ghz-ax disabled=nofrequency=5500name=5G_ch106 width=20/40/80mhzaddband=5ghz-ax disabled=nofrequency=5580name=5G_ch122 width=20/40/80mhz/interfacewifi datapathaddbridge=bridge disabled=noname=dyn_vlan/interfacewifi securityaddauthentication-types=wpa2-eap,wpa3-eap connect-priority=0/1disabled=noft=yes ft-over-ds=yes name=wpa-eap/interfacewifi steeringadddisabled=noname=steering1 neighbor-group=ng1 rrm=yes wnm=yes/interfacewifi configurationaddchannel=2G_ch1 country=Germanydatapath=dyn_vlan mode=ap multicast-enhance=enabled name=KDK_2G_ch1 security=wpa-eap ssid=KDK-mt steering=steering1addchannel=2G_ch6 country=Germanydatapath=dyn_vlan mode=ap multicast-enhance=enabled name=KDK_2G_ch6 security=wpa-eap ssid=KDK-mt steering=steering1addchannel=2G_ch11 country=Germanydatapath=dyn_vlan mode=ap multicast-enhance=enabled name=KDK_2G_ch11 security=wpa-eap ssid=KDK-mt steering=steering1addchannel=5G_ch58 country=Germanydatapath=dyn_vlan mode=ap multicast-enhance=enabled name=KDK_5G_ch58 security=wpa-eap ssid=KDK-mt steering=steering1addchannel=5G_ch106 country=Germanydatapath=dyn_vlan mode=ap multicast-enhance=enabled name=KDK_5G_ch106 security=wpa-eap ssid=KDK-mt steering=steering1addchannel=5G_ch122 country=Germanydatapath=dyn_vlan mode=ap multicast-enhance=enabled name=KDK_5G_ch122 security=wpa-eap ssid=KDK-mt steering=steering1/interfacewifiset[finddefault-name=wifi2]configuration=KDK_2G_ch11 configuration.mode=ap disabled=noname=ap001.of.kdk.network-2Gsecurity.connect-priority=0set[finddefault-name=wifi1]configuration=KDK_5G_ch58 configuration.mode=ap disabled=noname=ap001.of.kdk.network-5Gsecurity.connect-priority=0/interfacebridge portaddbridge=bridge comment=defconfinterface=ap001.of.kdk.network-5Ginternal-path-cost=10path-cost=10addbridge=bridge comment=defconfinterface=ap001.of.kdk.network-2Ginternal-path-cost=10path-cost=10addbridge=bridgeinterface=ether1internal-path-cost=10path-cost=10/ip firewall connection trackingsetudp-timeout=10s/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacebridge vlanaddbridge=bridge comment=kdk-of-cl01-303tagged=ether1,ap001.of.kdk.network-5G,ap001.of.kdk.network-2Gvlan-ids=303addbridge=bridge comment=kdk-of-dvc-305tagged=ether1,ap001.of.kdk.network-2G,ap001.of.kdk.network-5Gvlan-ids=305/interfacedot1x clientaddeap-methods=eap-peap identity="ap001\$"interface=ether1/interfacelist memberaddcomment=defconfinterface=bridge list=LAN/interfacewifi capsmansetca-certificate=autocertificate=autoenabled=yes interfaces=bridgepackage-path=""require-peer-certificate=noupgrade-policy=suggest-same-version/interfacewifi provisioningaddaction=create-dynamic-enabled comment=ap002_2G disabled=noidentity-regexp=ap002.of.kdk.network master-configuration=KDK_2G_ch1 name-format=%I-2Gsupported-bands=2ghz-axaddaction=create-dynamic-enabled comment=ap002_5G disabled=noidentity-regexp=ap002.of.kdk.network master-configuration=KDK_5G_ch106 name-format=%I-5Gsupported-bands=5ghz-axaddaction=create-dynamic-enabled comment=ap003_2G disabled=noidentity-regexp=ap003.of.kdk.network master-configuration=KDK_2G_ch6 name-format=%I-2Gsupported-bands=2ghz-axaddaction=create-dynamic-enabled comment=ap003_5G disabled=noidentity-regexp=ap003.of.kdk.network master-configuration=KDK_5G_ch122 name-format=%I-5Gsupported-bands=5ghz-ax/ip addressaddaddress=192.168.88.1/24comment=defconfinterface=bridge network=192.168.88.0/ip dhcp-client# DHCP client can not run on slave or passthrough interface!addcomment=defconfinterface=ether1/ip dnssetallow-remote-requests=yes/ip firewall filteraddaction=accept chain=forward comment="defconf: accept in ipsec policy"ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment="defconf: accept established,related, untracked"connection-state=established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"connection-state=invalidaddaction=drop chain=forward comment="defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"disabled=yes ipsec-policy=out,noneout-interface-list=WAN/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment="defconf: accept established,related,untracked"connection-state=established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=invalidaddaction=accept chain=input comment="defconf: accept ICMPv6"protocol=icmpv6addaction=accept chain=input comment="defconf: accept UDP traceroute"port=33434-33534protocol=udpaddaction=accept chain=input comment="defconf: accept DHCPv6-Client prefix delegation."dst-port=546protocol=udp src-address=fe80::/10addaction=accept chain=input comment="defconf: accept IKE"dst-port=500,4500protocol=udpaddaction=accept chain=input comment="defconf: accept ipsec AH"protocol=ipsec-ahaddaction=accept chain=input comment="defconf: accept ipsec ESP"protocol=ipsec-espaddaction=accept chain=input comment="defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=input comment="defconf: drop everything else not coming from LAN"in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept established,related,untracked"connection-state=established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"connection-state=invalidaddaction=drop chain=forward comment="defconf: drop packets with bad src ipv6"src-address-list=bad_ipv6addaction=drop chain=forward comment="defconf: drop packets with bad dst ipv6"dst-address-list=bad_ipv6addaction=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1"hop-limit=equal:1protocol=icmpv6addaction=accept chain=forward comment="defconf: accept ICMPv6"protocol=icmpv6addaction=accept chain=forward comment="defconf: accept HIP"protocol=139addaction=accept chain=forward comment="defconf: accept IKE"dst-port=500,4500protocol=udpaddaction=accept chain=forward comment="defconf: accept ipsec AH"protocol=ipsec-ahaddaction=accept chain=forward comment="defconf: accept ipsec ESP"protocol=ipsec-espaddaction=accept chain=forward comment="defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment="defconf: drop everything else not coming from LAN"in-interface-list=!LAN/radiusaddaddress=10.200.1.101comment=com01.of.kdk.network service=wirelessaddaddress=10.200.1.102comment=com02.of.kdk.network service=wireless/system clocksettime-zone-name=Europe/Berlin/system identitysetname=ap001.of.kdk.network/system notesetshow-at-login=no/system ntp clientsetenabled=yes/system ntp client serversaddaddress=ntp01.of.kdk.networkaddaddress=ntp02.of.kdk.network/system routerboard mode-buttonsetenabled=yes on-event=dark-mode/system scriptaddcomment=defconf dont-require-permissions=noname=dark-mode owner=*sys policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=\"\r\
    \n   :if ([system leds settings get all-leds-off] = \"never\") do={\r\
    \n     /system leds settings set all-leds-off=immediate \r\
    \n   } else={\r\
    \n     /system leds settings set all-leds-off=never \r\
    \n   }\r\
    \n "/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN
```

No problem, I could have been more specific with the general setup in the first place. Just to make this clear, you are correct: 'ap001' is the CAPsMAN controller, the other two cAP ax's are configured as CAPs, no other MT components involved. Configuration profiles of 'ap001' are configured directly on the interfaces.Here's a config export:


---
```

## Response 9
Author: Tue Mar 12, 2024 3:54 pm
If you go in Wifi / Steering, the button on the top with neighbor groups, doesn't it show a dynamic group ?I have nothing configured in steering nor configuration and all radios with the same SSID nicely come together in one single dynamic steering group. ---

## Response 10
Author: Tue Mar 12, 2024 3:57 pm
No, there are 0 items if I don't explicitly configure a neighbor-group. ---

## Response 11
Author: Tue Mar 12, 2024 4:08 pm
I don't have any specific suspect, as your configuration seems similar to mine (with 2 APs instead of 3) and I do have the expected dynamic neighbor groups.One possible (unrelated) error is the configuration of the dhcp client (which you probably have to remove)Some random pointers to check (probably unrelated, just the main differences with my config):You are using EAP, while I am using PSK. Can you try to change to WPA2-PSK?The SSID has a - Can you try to remove? (Maybe there is some bug...)I cannot understand your topology (how are the other APs connected? Via a switch?) and how you configured the VLANs/datapaths ---

## Response 12
Author: Tue Mar 12, 2024 4:22 pm
What exactly do you mean with configuration error of the DHCP client?The topology is as follows:all APs are managed within the same VLAN, which is the native VLAN configured on the switch portsall APs are getting a static DHCP leaseVLAN IDs for wireless clients are dynamically assigned by RADIUS attributes ---

## Response 13
Author: Tue Mar 12, 2024 4:40 pm
``` 
```
/ip dhcp-client# DHCP client can not run on slave or passthrough interface!addcomment=defconfinterface=ether1
```

I apologize if I was not clear. Your configuration includeswhile ether1 is part of the bridge. And I don't see how your APs (at least ap001) get their lease.I am not experienced enough to assess if your VLAN config is correct. I am expecting something different (for example, vlan-ids set in datapath, since you are using ax devices), but I cannot conclude that there are errors in the config. I apologize if my observation added noise to the discussion.Apart from my previous list (quite vague), I am out of ideas.


---
```

## Response 14
Author: Tue Mar 12, 2024 4:43 pm
You are using EAP, while I am using PSK. Can you try to change to WPA2-PSK?Aaand you got 100 points! As soon as I configured WPA-PSK as authentication mechanism, a dynamic neighbor-group is created. Thank you for helping me to pinpoint the problem! The next question is: What now? Is this something where I can open a support ticket at MT? ---

## Response 15
Author: Tue Mar 12, 2024 4:46 pm
Definitely.support AT mikrotik DOT com ---

## Response 16
Author: Tue Mar 12, 2024 4:48 pm
And please report back the outcome! ---

## Response 17
Author: Tue Mar 12, 2024 4:52 pm
Thank you guys, I will report back as soon as I have a reply. And thank you for pointing out the configuration error with the DHCP client. Now all I have to do is figure out a way to change the config without locking myself out xD ---

## Response 18
Author: Tue Apr 02, 2024 12:55 pm
It's been three weeks now without any response of MT support. Is this to be expected??Will keep you posted as soon as I know more. ---

## Response 19
Author: Tue Jul 02, 2024 12:08 am
I confirm, there isNO DYNAMIC entry when using CapsMan2.I have entered my own value, which I don't even know if it needs to be in a specific format or what. Don't know if it's working. ---

## Response 20
Author: Tue Jul 02, 2024 12:09 am
It's been three weeks now without any response of MT support. Is this to be expected??Will keep you posted as soon as I know more.It's also been months not hearing from you too. ---

## Response 21
Author: [SOLVED]Fri Sep 06, 2024 10:09 am
It's also been months not hearing from you too.True, can't comment anything when there's nothing new to share...I confirm, there is NO DYNAMIC entry when using CapsMan2.It only affects profiles with EAP authentication.MT support finally responded and confirmed that no steering group is automatically created if EAP is used as a authentication mechanism:That being said, regarding the original query. Feedback from developers currently is as follows:Dynamic neighbor groups are automatically created while using PSK, if the same SSID and PSK are used, these attributes tell us that interfaces have the same connection requirements, since we have this information, RouterOS can create a dynamic group for this scenario, for these specific interfaces.In the case of EAP, currently, it's not possible to create automatic neighbor groups, since there are no comparable attributes that would guarantee that the connection requirements are the same in all cases. Which, unfortunately, means that the network administrator needs to specify that interfaces are part of the same group.We might investigate in the future, if we can find some workaround that would allow dynamic neighbor steering groups for EAP, but currently, I can't give any guarantees regarding that.I asked them to add some information to the documentation, which they did right away:https://help.mikrotik.com/docs/display/ ... properties ---

## Response 22
Author: Mon Oct 21, 2024 9:40 pm
Which is great they added the line to the documentation. That's what brought me here. What they forgot to add is HOW do you add a neighbor group manually? I've been looking for a way to do this, but there isn't an ADD button and the CLI doesn't have an ADD command under neighbor-groups. ---

## Response 23
Author: Mon Oct 21, 2024 9:55 pm
You make a neighbour group in steering. Two locations (and from the GUI there is a tab steering:/interface/wifi/configuration/steering/interface/wifi/steering ---

## Response 24
Author: Tue Nov 19, 2024 10:43 pm
``` 
```
/interface/wifi/steering/neighbor-group>comment     edit     findprintresetset
```

You make a neighbour group in steering. Two locations (and from the GUI there is a tab steering:/interface/wifi/configuration/steering/interface/wifi/steeringThere is no option yet, even in CLI, to create neighbor group.


---
```

## Response 25
Author: Wed Nov 20, 2024 2:48 pm
thats the place you can print them. you define them one level up. ---

## Response 26
Author: Wed Nov 20, 2024 7:25 pm
No, you can't!? One level up you can define custom steering settings which can refer to an existing neighbor-group, but as far as I can tell there is no possibility to create your own custom neighbor-group. ---

## Response 27
Author: Wed Nov 20, 2024 11:25 pm
of course you can. ---

## Response 28
Author: Thu Nov 21, 2024 7:46 am
No, you can't!? One level up you can define custom steering settings which can refer to an existing neighbor-group, but as far as I can tell there is no possibility to create your own custom neighbor-group.Really ?/interface/wifi/steering> add neighbor-group=test name=testDONE.Don't confuse with dynamic neighbor-groups ... ---

## Response 29
Author: Thu Nov 21, 2024 8:43 am
/interface/wifi/steering> add neighbor-group=test name=testCan you actually display/print the neighbor-group (and its BSSIDs)? To me it appears that you just added a steering configuration with a reference to a non-existent neighbor-group.Edit: My bad, it works as described! As soon as you assign the steering configuration to a wifi interface, the referenced neighbor-group is created automatically. I never tried this before, as I was expecting to see an empty neighbor-group before assignment.