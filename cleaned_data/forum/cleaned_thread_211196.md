# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211196

# Discussion

## Initial Question
Author: Wed Sep 25, 2024 2:32 pm
``` 
```
# 2024-09-25 13:22:43 by RouterOS 7.15.3# software id = 7UAI-U0HI## model = RB5009UG+S+# serial number =/caps-man channeladdband=2ghz-b/g/n control-channel-width=20mhzextension-channel=disabled \
    frequency=2412name=2412secondary-frequency=disabled tx-power=14addband=2ghz-b/g/n control-channel-width=20mhzextension-channel=disabled \
    frequency=2437name=2437secondary-frequency=disabled tx-power=14addband=2ghz-b/g/n control-channel-width=20mhzextension-channel=disabled \
    frequency=2462name=2462secondary-frequency=disabled tx-power=14addband=5ghz-onlyac control-channel-width=20mhzextension-channel=XX name=\5Ghzreselect-interval=1hsave-selected=yes skip-dfs-channels=no\
    tx-power=20addband=2ghz-onlyn control-channel-width=20mhzextension-channel=disabled \
    frequency=2412,2437,2462name=2.4Ghzsecondary-frequency=disabled \
    tx-power=14/interfacebridgeaddarp=proxy-arp name=Bridge-LAN/interfaceethernetset[finddefault-name=ether1]arp=proxy-arp name=ether1-WANset[finddefault-name=ether2]name=ether2-LANset[finddefault-name=ether3]name="ether3-Admin AP"set[finddefault-name=ether4]name="ether4-Hallway AP"set[finddefault-name=ether5]name="ether5-Blue AP"set[finddefault-name=ether6]name="ether6-Green_Orange AP"set[finddefault-name=ether8]name="ether8 - LTE Fail Over"/interfacepppoe-clientaddadd-default-route=yes disabled=nointerface=ether1-WAN name=\"Internet In-Web Africa"use-peer-dns=yes user=********/interfacewireguardaddlisten-port=13231mtu=1450name=Pepla_WG/caps-man datapathaddbridge=Bridge-LAN client-to-client-forwarding=nolocal-forwarding=yes \
    name=Internet/caps-man securityaddauthentication-types=wpa2-psk encryption=aes-ccmgroup-encryption=aes-ccm \group-key-update=40mname="WiFi Security"/caps-man configurationaddchannel=2.4Ghzchannel.frequency=2412,2437,2462country="south africa"\
    datapath=Internetdatapath.bridge=Bridge-LAN installation=indoor mode=ap \
    name="Config 2.4Ghz"rx-chains=0,1security="WiFi Security"ssid=Pepla\
    tx-chains=0,1addchannel=5Ghzcountry="south africa"datapath=Internetdatapath.bridge=\Bridge-LAN installation=indoor mode=ap name="Config 5Ghz"rx-chains=0,1\
    security="WiFi Security"ssid="Pepla 5G"tx-chains=0,1/interfacelistaddname=LANaddname=WAN/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTik/ip ipsec proposalset[finddefault=yes]auth-algorithms=sha512/ip pooladdname=DHCP-LAN ranges=192.168.0.11-192.168.0.239/ip dhcp-serveraddaddress-pool=DHCP-LANinterface=Bridge-LAN lease-time=2dname=DHCP/routing tableaddcomment="Table for WireGuard - JPB"disabled=nofib name=WG-Pepla/caps-man access-listaddaction=accept allow-signal-out-of-range=10sdisabled=yes signal-range=\-85..120ssid-regexp=""addaction=reject allow-signal-out-of-range=10sdisabled=yes signal-range=\-120..-86ssid-regexp=""/caps-man managersetca-certificate=autocertificate=autoenabled=yes/caps-man provisioningaddaction=create-dynamic-enabled master-configuration="Config 2.4Ghz"\
    name-format=identityaddaction=create-dynamic-enabled master-configuration="Config 5Ghz"\
    name-format=identity/interfacebridge portaddbridge=Bridge-LANinterface="ether3-Admin AP"addbridge=Bridge-LANinterface="ether4-Hallway AP"addbridge=Bridge-LANinterface="ether5-Blue AP"addbridge=Bridge-LANinterface="ether6-Green_Orange AP"addbridge=Bridge-LANinterface=ether2-LAN/ip firewall connection trackingsetenabled=yes udp-timeout=10s/ip neighbor discovery-settingssetdiscover-interface-list=!dynamic/interfacel2tp-server serversetdefault-profile=defaultuse-ipsec=yes/interfacelist memberaddinterface=Bridge-LAN list=LANaddinterface="Internet In-Web Africa"list=WAN/interfacewireguard peersaddallowed-address=192.168.89.3/32client-dns=192.168.0.1interface=Pepla_WG\
    name="user1"persistent-keepalive=30sprivate-key=\"******************* public-key=\
    "*******************"
add allowed-address=192.168.89.2/32 client-dns=8.8.8.8 interface=Pepla_WG \
    name="user2" persistent-keepalive=30s private-key=\
    "*******************" public-key=\
    "*******************"
add allowed-address=192.168.89.4/32 interface=Pepla_WG name="User3" \
    persistent-keepalive=30s private-key=\
    "*******************" public-key=\
    "*******************"
add allowed-address=192.168.89.5/32 interface=Pepla_WG name="User4" \
    persistent-keepalive=30s private-key=\
    "*******************" public-key=\
    "*******************"
add allowed-address=192.168.0.6/32 interface=Pepla_WG name=\
    "User5" persistent-keepalive=30s private-key=\
    "*******************" public-key=\
    "*******************"
/ip address
add address=192.168.0.1/24 interface=Bridge-LAN network=192.168.0.0
add address=41.132.65.127 disabled=yes interface="InternetIn-WebAfrica" \
    network=168.210.4.66
add address=192.168.89.1/24 comment=Pepla_WG interface=Pepla_WG network=\
    192.168.89.0
/ip dhcp-server network
add address=192.168.0.0/24 dns-server=192.168.0.1 gateway=192.168.0.1 \
    ntp-server=154.73.32.1,154.73.32.2
/ip dns
set allow-remote-requests=yes servers=192.168.0.1
/ip firewall address-list
add address=154.73.32.0/22 disabled=yes list=iewc-ip4s
add address=165.16.200.0/21 disabled=yes list=iewc-ip4s
add address=192.168.0.0/24 disabled=yes list=MGMT-RANGES
add address=192.168.88.0/24 disabled=yes list=MGMT-RANGES
add address=192.168.0.0/24 list=Local-LAN
add address=192.168.89.0/24 list="WIRE GUARD"
/ip firewall filter
add action=accept chain=input comment=\
    "Allow:Established,Related,Untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="DropInvalid" connection-state=invalid
add action=accept chain=input comment="defconf:accept ICMP" protocol=icmp
add action=accept chain=input comment=\
    "defconf:accept tolocalloopback(forCAPsMAN)" disabled=yes \
    dst-address=127.0.0.1
add action=accept chain=input comment="WireGuardHandshake" dst-port=13231 \
    protocol=udp
add action=accept chain=input comment="WinboxRouterAccess" dst-port=8291 \
    protocol=tcp src-address=192.168.89.0/24
add action=accept chain=input comment="admin access" in-interface=Bridge-LAN \
    src-address=192.168.0.0/24
add action=accept chain=input comment="users services" dst-port=53 \
    in-interface=Bridge-LAN protocol=udp
add action=accept chain=input comment="users services" dst-port=53 \
    in-interface=Bridge-LAN protocol=tcp
add action=drop chain=input comment="drop allelse"
add action=fasttrack-connection chain=forward comment="defconf:fasttrack" \
    connection-mark=no-mark connection-state=established,related hw-offload=\
    yes
add action=accept chain=forward comment=\
    "AllowEstablished,Related,Untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="DropInvalid" connection-state=invalid
add action=accept chain=forward comment="InternetTraffic" in-interface=\
    Bridge-LAN out-interface="InternetIn-WebAfrica"
add action=accept chain=forward comment="WireGuardto LAN" in-interface=\
    Pepla_WG out-interface="InternetIn-WebAfrica"
add action=accept chain=forward comment=\
    "AllowLocalSubnetToEnterTheWireGuardInterface" out-interface=\
    Pepla_WG src-address=192.168.0.0/24
add action=accept chain=forward disabled=yes dst-port=19001 protocol=tcp
add action=accept chain=forward comment="PortForwarding" \
    connection-nat-state=dstnat disabled=yes
add action=drop chain=forward comment="Dropallelse" connection-state=""
/ip firewall mangle
add action=accept chain=prerouting disabled=yes dst-address=192.168.0.0/24
/ip firewall nat
add action=masquerade chain=srcnat
add action=masquerade chain=srcnat comment="WireGuardNAT" disabled=yes \
    out-interface=Pepla_WG src-address=192.168.89.0/24
/ip firewall service-port
set tftp disabled=yes
set irc disabled=no
set h323 disabled=yes
set sip disabled=yes
/ip ipsec profile
set [ find default=yes ] dh-group=modp2048 enc-algorithm=aes-256 \
    hash-algorithm=sha512
/ip service
set ftp disabled=yes
/ppp secret
add disabled=yes name=vpn profile=*2
add disabled=yes name=JP profile=*2
/routing rule
add action=lookup disabled=no src-address=192.168.89.0/24 table=WG-Pepla
add action=lookup disabled=yes src-address=192.168.89.2/32 table=WG-Pepla
add action=lookup disabled=yes src-address=192.168.89.3/32 table=WG-Pepla
/system clock
set time-zone-name=Africa/Johannesburg
/system identity
set name="CoreRouter"
/system note
set show-at-login=no
```

```
```

```
# 2024-09-25 13:22:22 by RouterOS 7.15.3# software id = 24LS-K6LZ## model = RBcAPGi-5acD2nD# serial number =/interfacebridgeaddadmin-mac=48:8F:5A:38:73:B3auto-mac=nocomment=defconf name=bridgeLocal/interfacewifi datapathaddbridge=bridgeLocal comment=defconf disabled=noname=capdp/interfacewifi# no connection to CAPsMANaddconfiguration.manager=capsman datapath=capdp radio-mac=48:8F:5A:38:73:B5# no connection to CAPsMANaddconfiguration.manager=capsman datapath=capdp radio-mac=48:8F:5A:38:73:B6/interfacebridge portaddbridge=bridgeLocal comment=defconfinterface=ether1addbridge=bridgeLocal comment=defconfinterface=ether2/interfacewifi capsetcaps-man-addresses=192.168.0.1certificate=request discovery-interfaces=\
    bridgeLocal enabled=yes slaves-datapath=capdp slaves-static=no/ip dhcp-clientaddcomment=defconfinterface=bridgeLocal/system clocksettime-zone-name=Africa/Johannesburg/system notesetshow-at-login=no
```

Hi all, as the title implies, when setting up a cap on CAPsMAN, I get an error message "no connection to CAPsMAN" I'm not sure if there is a firewall rule that might be blocking the traffic? I can ping the CapsMan router from the cap and visa versa. I'm at my ends here.The Caps are directly connected to the router, from ether3-ether6Any help would be greatly appreciated.Router ConfigCaps Config


---
```

## Response 1
Author: Wed Sep 25, 2024 2:42 pm
Your firewall is quite strict at dropping anything not allowed. Which is good. But you have to allow capsman protocol. From a note in documentation for capsman v2 (the old wireless capsman):Note: CAPsMAN uses UDP port 5246 for manager traffic and UDP port 5247 for data trafficI didn't find similar information for the new capsman (wifi version), it could use different protocol and/or ports ... probably it doesn't use port 5247 since the new capsman doesn't support capsman forwarding. ---

## Response 2
Author: Wed Sep 25, 2024 3:24 pm
``` 
```
addaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"disabled=yes \
    dst-address=127.0.0.1
```

Sure this has to be disabled?


---
```

## Response 3
Author: Wed Sep 25, 2024 3:31 pm
Originally, I thought that this rule needs to be disabled as the Router itself, doesn't have WiFi capabilities and doesn't possess WiFi interfaces. Unless I misunderstood that xD ---

## Response 4
Author: Wed Sep 25, 2024 3:31 pm
Sure this has to be disabled?If CAP and CAPsMAN are different devices, then they won't communicate using address of 127.0.0.1 (neither of them) ... hence this rule doesn't apply.Or is it? If CAPsMAN communicates with itself (another process perhaps), then it might use 127.0.0.1 ... @JPbarries, try to enable the rule and see if that makes any difference. My bet would still be the UDP port 5246, mentioned in my previous post, but can't find the rule which would either allow it or drop it (there's one which allows everything through bridge-IN and with corresponding src-address, so that one should allow it). ---

## Response 5
Author: Wed Sep 25, 2024 3:48 pm
Sure this has to be disabled?If CAP and CAPsMAN are different devices, then they won't communicate using address of 127.0.0.1 (neither of them) ... hence this rule doesn't apply.Or is it? If CAPsMAN communicates with itself (another process perhaps), then it might use 127.0.0.1 ... @JPbarries, try to enable the rule and see if that makes any difference. My bet would still be the UDP port 5246, mentioned in my previous post, but can't find the rule which would either allow it or drop it (there's one which allows everything through bridge-IN and with corresponding src-address, so that one should allow it).Doesn't seem as if any traffic is hitting that rule. If you could perhaps guide me on how to create the rule that uses the specified ports in your previous post please.I'm guessing it's an input rule with protocol upd and src. port to be 5246, 5247 ---

## Response 6
Author: Wed Sep 25, 2024 3:48 pm
``` 
```
addaction=accept chain=input comment="admin access"in-interface=Bridge-LAN \
    src-address=192.168.0.0/24
```

You are absolutely right, @mkx!Checked everything (I could), I doubt if this rule is correct:Can you, at least as a test, remove the in-interface?


---
```

## Response 7
Author: Wed Sep 25, 2024 3:52 pm
@erlinden.Thanks for your responseI've disabled that rule, not quite sure what the purpose of this rule was. I was instructed from one of my other posts to have that rule created. However, the Cap still states " no connection to CAPsMAN" after I disabled the admin access rule. ---

## Response 8
Author: Wed Sep 25, 2024 3:58 pm
By disabling the accept rule is disabled (and it is no longer accepting traffic). Instead, enable it and remove the in-interface. Again...just for testing. You can enable logging to see which traffic is passing that rule. ---

## Response 9
Author: Wed Sep 25, 2024 4:10 pm
@erlindenI've removed the in-inteface, but the Cap still states "no connection to CAPsMAN" I even reset the CAP again to make sure :/ ---

## Response 10
Author: [SOLVED]Wed Sep 25, 2024 4:24 pm
``` 
```
/caps-man
```

```
```

```
#create a security profile/interfacewifi securityaddauthentication-types=wpa3-psk name=sec1 passphrase=HaveAg00dDay#create configuraiton profiles to use for provisioning/interfacewifi configurationaddcountry=Latvianame=5ghzsecurity=sec1 ssid=CAPsMAN_5addname=2ghzsecurity=sec1 ssid=CAPsMAN2addcountry=Latvianame=5ghz_v security=sec1 ssid=CAPsMAN5_v#configure provisioning rules, configure band matching as needed/interfacewifi provisioningaddaction=create-dynamic-enabled master-configuration=5ghzslave-configurations=5ghz_v supported-bands=\5ghz-naddaction=create-dynamic-enabled master-configuration=2ghzsupported-bands=2ghz-n#enable CAPsMAN service/interfacewifi capsmansetca-certificate=autoenabled=yes
```

Aaah...sorry it took me this longYou have the wireless package installed and are configuring the old CAPsMAN:Remove the wireless package, it's useless.Then, follow the guide:


---
```

## Response 11
Author: Wed Sep 25, 2024 4:48 pm
@erlindenI thought that it might have been something in line with this. As our previous router (hAP ac2) -whch did work with the existing CAPS, even after I've upgraded the RouterOS 6 to 7 - was replaced with the RB5009UG+S+. and now that I want to configure CAPsMAN again, I started running into these issues. I've set for uninstall. Just need to wait for everyone to leave the office before I can restart the routerBut thanks to you and mkx for your continued support. I will attend to this and revert back ---

## Response 12
Author: Wed Sep 25, 2024 5:23 pm
As a side note:whenever you change something in firewall rules, clear connections table or restart.Or it might take a while before you see the effect.But wireless/wifi-qcom confusion is going to be the winner here.As of ROS7.13, you don't even need to load wifi-qcom driver anymore for capsman controller.Those hooks are there by default in base ROS package. ---

## Response 13
Author: Wed Sep 25, 2024 5:26 pm
The reboot is not necessary for implementing CAPsMAN, it's just for clean up purposes.Do you still have the config of the hAP ac2? Then it would be sufficient to just import the /interface wifi part of that device (ewxcepot for any local config). ---

## Response 14
Author: Thu Sep 26, 2024 9:54 am
``` 
```
Flags:X-disabled0name="WiFi Sec"authentication-types=wpa2-psk,wpa3-psk passphrase="test123"
```

```
```

```
Flags:X-disabled0name="2.4Ghz"ssid="Pepla"country=SouthAfricasecurity=WiFiSecsecurity.authentication-types=wpa2-psk,wpa3-psk.passphrase="test123"1name="5Ghz"ssid="Pepla 5G"country=SouthAfricasecurity=WiFiSecsecurity.authentication-types=wpa2-psk,wpa3-psk.passphrase="test123"
```

```
```

```
Columns:ACTION,MASTER-CONFIGURATION#  ACTION                  MASTER-CONFIGURATION0create-dynamic-enabled5Ghz1create-dynamic-enabled2.4Ghz
```

```
```

```
[admin@CoreRouter]/interface/wifi/capsman>printenabled:no
```

The reboot is not necessary for implementing CAPsMAN, it's just for clean up purposes.Do you still have the config of the hAP ac2? Then it would be sufficient to just import the /interface wifi part of that device (ewxcepot for any local config).I do, however the RouterOS is still that of 6.49.17.I also did change the config as you suggested, however, the CAP is still not able to see the capsman. Still getting no Connection to CapsMan, unless I did something wrong#create a security profile#create configuraiton profiles to use for provisioning#configure provisioning rules, configure band matching as needed#enable CAPsMAN serviceEDIT: LOL, As I went through the steps again, as I didn't use the command in the terminal to do the setup, but rather used the User Interface (UI) I found that the CAPsMAN was enabled on the router as there was a tick box, but as I typed in the above code to get the response and to paste the results here, I saw that the CAPsMAN was disabled, but in the UI the tick box was marked. And then as soon as I ran the code to enable the CAPsMAN on the router, BOOM!! The CAP was able to identify the CAPsMAN!!! Thank you erlinden!!!


---
```

## Response 15
Author: Thu Sep 26, 2024 9:57 am
Good find! You are very welcome, enjoy it! ---

## Response 16
Author: Thu Sep 26, 2024 10:27 am
So, if I get this right, the CAPSMAN appeared enabled in Winbox/Webfig while it was actually disabled in the actual (CLI/terminal) configuration?It seems like a bug that can deceive/trick lots of people. ---

## Response 17
Author: Thu Sep 26, 2024 10:57 am
So, if I get this right, the CAPSMAN appeared enabled in Winbox/Webfig while it was actually disabled in the actual (CLI/terminal) configuration?It seems like a bug that can deceive/trick lots of people.That is correctOne of the reasons I started to pull my hair out of my head. But as I went through the terminal to retrieve the code to paste in my reply, I noticed that the terminal stated that the CAPsMAN was disabled. yet the UI said it was enabled. After enabling it in the terminal the CAP immediately started to register with the CAPsMAN.