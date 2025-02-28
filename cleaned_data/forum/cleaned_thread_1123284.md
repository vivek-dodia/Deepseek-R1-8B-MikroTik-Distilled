# Thread Information
Title: Thread-1123284
Section: RouterOS
Thread ID: 1123284

# Discussion

## Initial Question
Hi everyone.I've recently changed my tp-link archer ax50 for hap ax3. Now I have some problems with 5GHz wireless. The firmware version is 7.15 Here's my config
```
1 M BR default-name="wifi1" name="wifi-5ghz" l2mtu=1560 mac-address=D4:01:C3:9D:86:32 arp-timeout=auto radio-mac=D4:01:C3:9D:86:32 configuration=home-private-cfg 
        configuration.mode=ap .ssid="MikroTik-Home" .country=United States .antenna-gain=0 
        security=home-private 
        security.authentication-types=wpa2-psk .passphrase="_removed_" .ft=yes .ft-over-ds=yes 
        channel=5ghz 
        channel.frequency=5180-5320,5660-5845 .band=5ghz-ax .width=20/40/80mhzThe problems are:1. MSI laptop ax-capable states that it connects using 802.11ac (was ax with archer).2. Random disconnects mostly under load. Windows shows full or 2/3 points signal and around 500Mbps transmit bandwidth.Here's log with debug enabled:
```

```
06-06 01:39:49 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -81
 06-06 01:39:49 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -81
 06-06 01:39:55 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength 20
 06-06 01:39:55 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength 20
 06-06 01:39:58 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -76
 06-06 01:39:58 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -76
 06-06 01:40:00 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength 20
 06-06 01:40:00 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength 20
 06-06 01:40:03 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -75
 06-06 01:40:03 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -75
 06-06 01:40:05 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength 21
 06-06 01:40:05 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength -73Here I can clearly see that MikroTik "thinks" there's bad signal, but it was ok with archer and Windows also think so, and the laptop is literally in the next room to the router without significant obstacles (i.e. there's even no door between rooms).I've started my config without country, antenna gain and "ft" parameters and with wpa3 enabled, going step by step with disabling wpa3, setting country, setting antenna gain, enabling ft - nothing solved the problem. Both Samsung android phones doesn't seem to have this problem, however I didn't pushed any significant network load on them, like YT or something.Do I miss something?

---
```

## Response 1
Here's my configIt would be clearer if you posted the sanitized output of "/interface/wifi/export", not "print" because that includes sub-items like the configuration and security sections.One thing this can show more clearly is when you have redundant or conflicting items in the "configuration" and "interface" sections, for example. The "configuration" should abstract as much as possible that is the same between the 2.4 and 5GHz radios, leaving the "interface" element to override only the unique parts.A clean implementation of that will look something like this:
```
/interface wifi configuration add country="United States" mode=ap name=homecfg security.authentication-types=wpa2-psk,wpa3-psk .ft=yes .ft-over-ds=yes .passphrase="nunyaBinness" ssid="Home WiFi"
/interface wifi set [ find default-name=wifi2 ] channel.band=2ghz-ax .width=20/40mhz configuration=homecfg
/interface wifi set [ find default-name=wifi1 ] channel.band=5ghz-ax .width=20/40/80mhz configuration=homecfgThe point is, there is only one "configuration" for both radios, and they differ only in the frequencies and such.MSI laptop ax-capable states that it connects using 802.11ac (was ax with archer).Then there is an incompatibility. It may be enough to explain everything else you're seeing. Your task is to find out what the laptop wants that the MT isn't providing. The fix may be a settings change away, or it may be a hard limit on one end or the other.
```

```
06-06 01:40:00 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength 20
 06-06 01:40:03 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -75
 06-06 01:40:03 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -75
 06-06 01:40:05 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength 21
 06-06 01:40:05 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength -73This isn't necessarily a problem. It is possible that all you're getting here is additional visibility into what's going on that your old router didn't tell you.A common reason for this type of behavior is bouncing between the 2.4 and 5GHz sides of the network.That said, I don't see a reconnection event immediately afterward on the other network, so…there's even no door between roomsWiFi doesn't use airborne transmission.The wall between the two rooms is likely more relevant to the router's operating conditions than the human-sized door frame and hallway between them.I've started my config without countryRouterOS has defaulted to "Latvia" for the last few releases, so unless that's where you live, you should always set the country.antenna gainUnless you're doing something advanced, you should leave this unset. Being the lowest legal value, "0" is likely wrong even if you do have good cause to be setting it.

---
```

## Response 2
Hi @tangent and thanks for your detailed answer!Here's export of wifi section
```
int wifi export
# 2024-06-06 13:21:28 by RouterOS 7.15
# software id = **ELIDED**
#
# model = C53UiG+5HPaxD2HPaxD
# serial number = **ELIDED**
/interface wifi channel
add band=5ghz-ax disabled=no frequency=5180,5220 name=5ghz skip-dfs-channels=all width=20/40/80mhz
/interface wifi configuration
add antenna-gain=0 country="United States" disabled=no name=home-private-cfg security.authentication-types="" .ft=no .ft-over-ds=no ssid=MikroTik-Home
/interface wifi security
add authentication-types=wpa2-psk disable-pmkid=yes disabled=no name=home-private
/interface wifi
set [ find default-name=wifi2 ] configuration=home-private-cfg configuration.mode=ap name=wifi-2.4ghz security=home-private security.authentication-types=wpa2-psk,wpa3-psk
set [ find default-name=wifi1 ] channel=5ghz configuration=home-private-cfg configuration.mode=ap disabled=no name=wifi-5ghz security=home-private security.authentication-types=wpa2-pskI have my 2.4G interface completely disabled for now, since I don't have any IoT yet, and that was the same on previous router. I don't need this band for now, so there's no switching between, old router is powered off. I did exactly as you described - everything in config is separated from the physical interface (except for authentication types - they seem to be ignored from security config, leaving my network "open", and only setting them to the physical interface did the job. This seems like a new bug for me, bcz it worked in ROS6).And about provided logs - at first, I just did configuration and started using network. However, I noticed frequent disconnects on the laptop, lasting for like 5-20 seconds or so to reconnect automatically. That's why I'd opened logs, and this is the events that are logged when disconnect occurs. Also, when disconnect happens, laptop shows 1/3 SSID signal strength and tries to reconnect, and when reconnect happens it becomes 3/3 again. Laptop is literally used as desktop now, with same positioning for itself and old router/new ax3. With old router I played online games no problems or disconnects.Also have to notice that wireless quality itself is perfect until it disconnects, i.e. surfing is omega-fast and smooth, no lags for youtube or twitch (or both at once).Things that I've also read from this forum or reddit before posting:1. Possible antenna damage - I had my antennas attached before power on2. Possible ROS7.15 wireless bugs - signal strength sometimes shows above zero, can firmware version be the cause of the problems?This is the log of one of disconnect events, showing this
```

```
13:39:32 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -75
 13:39:32 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -75
 13:39:34 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength 21
 13:39:35 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength 21
 13:46:40 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -76
 13:46:40 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -76
 13:46:43 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength 17
 13:46:43 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength 17
 13:46:49 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -71
 13:46:49 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -71
 13:46:51 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength 21
 13:46:51 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength 21
 13:46:53 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength 21
 13:46:53 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength 21
 13:46:55 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength 17
 13:46:56 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength 17
 13:46:58 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -74
 13:46:58 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -74
 13:46:59 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength 20
 13:46:59 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength 20
 13:47:01 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -74
 13:47:01 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -74
 13:47:03 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength 20
 13:47:03 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength 203. Wireless interfaces are bridged but should not be - they are, but doubt it affects wireless connectivity, since I did same config in ROS6.4. Tried to play with frequencies - leaving it blank sets channel to 5500, and SSID becomes invisible to Samsung S21

---
```

## Response 3
The antenna gain is incorrect, it should be 5 or 6 (in the manual it shows 5.5). Don't know what the default is, at least it is not 0. ---

## Response 4
The antenna gain is incorrect, it should be 5 or 6 (in the manual it shows 5.5). Don't know what the default is, at least it is not 0.Can't set it to decimal value, gonna try with 5 and respond back with results.Any ideas on why laptop is not recognizing ax protocol tho? Because Samsung shows "6" on the wireless icon, not sure if it's using ax but I think it is, while laptop is always at .11ac no matter what configs I did before ---

## Response 5
What exact wireless card is in the laptop? ---

## Response 6
What exact wireless card is in the laptop?Intel(R) Wi-Fi 6 AX201 160MHz ---

## Response 7
Strange, as the MikroTik is supplying and the laptop is capable. Have you checked with an app like Wifi Analyzer?I also notice you use "disable-pmkid=yes", can you start again from the basic configuration (disable current /interface wifi configuration and add a new one)? ---

## Response 8
authentication types - they seem to be ignored from security config, leaving my network "open"This is the kind of thing I meant in my first reply: you're setting it from two different places, creating a conflict:
```
/interface wifi configuration
add antenna-gain=0 country="United States" disabled=no name=home-private-cfg security.authentication-types="" .ft=no .ft-over-ds=no ssid=MikroTik-Home
/interface wifi security
add authentication-types=wpa2-psk disable-pmkid=yes disabled=no name=home-privateNote that "security.authentication" is set as blank on the first line and to "wpa2-psk" on the second.This is thesamesetting!Which one takes precedence? I dunno, but there's no reason to press your luck. If you're going to have an "/interface wifi security" entry, you shouldn't be including "security.ANYTHING" in your "/interface/wifi/configuration" entry. You can do it either way, however it makes sense to you, but don't try to do it from both directions.(There's a third potential method, doing it from the top "/interface/wifi" level, too.)

---
```

## Response 9
Which one takes precedence? I dunno, but there's no reason to press your luck. ...(There's a third potential method, doing it from the top "/interface/wifi" level, too.)When looking at Winbox, left to right on the tabs, that should be descending preference (so leftmost option where you can set it, has highest priority).Directly on interface is highest.Then configurationThen SecurityI (try to) make it a habit to never set anything on interface. Only apply configuration.And in configuration I only apply earlier made channels, security, ...But obviously when doing something QnD for testing, it can happen I set it all directly on interface ---

## Response 10
WiFi Analyzer tells this:Channel 136 5680 GHz (I've added some channels after another connection drop)Channel width 20 MHzProtocol 802.11ax (metro UI still shows 802.11ac, was also ax with tp-link) Dunno what to trust there now, reverting to old router shows ax proto in metro UI againAfter setting antenna gain to 5, I had another disconnect with laptop. Tried to forget the SSID and reconnect, gonna see what happens.On auth-types - since I did configuration with Winbox, the problem was that in /wifi/configuration I left auth types open, which produced the auth-types="" config and left the network open. Closing the auth types tab fixed this, so now it's set directly in security profile and working. A bit inconvenient but can move on with this. So the only thing that worry me now is constant disconnects.The config is now only different from stock with disabled pmkid and static 5ghz channels (auto sets channel 5500 which is invisible to my phones). Can try re-enable pmkid, or should I anyway create a new config?Can I also somehow see in winbox or terminal which 802.11 protocol clients are using? ---

## Response 11
Winbox (and terminal) will show with what rates devices are connected. That will indicate the protocol used (866 for ac, 1200 for ax).Adding a new config is not much of work (you can disable current if you want). Then you can be sure all settings are correct. But setting it to default manually will give the same result. ---

## Response 12
Here's my current configuration, now looks pretty simple./interface wifi channeladd band=5ghz-ax disabled=no frequency=5180, 5220, 5640-5730 name=5ghz skip-dfs-channels=all width=20/40/80mhz/interface wifi configurationadd antenna-gain=5 country="United States" disabled=no name=home-private-cfg ssid=MikroTik-Home/interface wifi securityadd authentication-types=wpa2-psk disabled=no name=home-private/interface wifiset [ find default-name=wifi2 ] configuration=home-private-cfg configuration.mode=ap name=wifi-2.4ghz security=home-privateset [ find default-name=wifi1 ] channel=5ghz configuration=home-private-cfg configuration.mode=ap disabled=no name=wifi-5ghz security=home-privateWinbox shows variable rates from 300 to 700 Mbps (sometimes dropping to 6 Mbps tho) at ~5m range. Signal is around -67..-77 for all devices. Can this be damaged hardware somehow? Since I got a decent discount from the shop for the device and now scared about it ---

## Response 13
And got another disconnect with above config.
```
20:01:47 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -75
 20:01:47 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -75
 20:02:15 wireless,debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength 24
 20:02:15 wireless,info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength 24

---
```

## Response 14
An optimistic update on the topic: I decided to rollback from 7.15 to factory firmware which is 7.14.1 and it seems to be no disconnects for some hours already. The bandwidth is still bad so there is a place for tweaks still. But at least it's stable now. ---

## Response 15
I also had many disconnects after upgrading my ax2 from 7.14.3 to 7.15.0For example, the music stream from the Google home-speakers was full of interruptions.After downgrading to 7.14.3 the disconnects are gone. ---

## Response 16
After contacting MikroTik support, they told me there's a bunch of feedback about 7.15 fw having disconnects, but they also told me there's some kind of problems reproducing this bug in their lab. So current solution for home devices is to revert back to latest 7.14.x, since in 7.15 there's qcom-driver update, and 7.15.1 doesn't fix that either. I also don't see anything related in beta branch, so it seems that this bug will stay for a while. It would be a good move from MT to make a separate branch with latest firmware and old stable driver until the problem is resolved. ---

## Response 17
I have the same problem. With support, I have already reset the router to factory settings 4 times and tried to select the configuration, but all to no avail. The only option is to roll back to 7.14.3. ---

## Response 18
7.15.2 out, seems still no fix. As I understand from reading through the pinned topic of 7.15 update, the issue is mostly related to ax devices. Has anyone tried beta branch, are there any changes? ---

## Response 19
Yes, this problem applies to AX devices. As far as I understand, there are several problems there. For some users, the problem was resolved when updating to 7.16beta ---

## Response 20
After many weeks of testing with different wireless devices and reading (+ testing) all the 7.15.X changelog, v7.14.3 was promoted as very stable for me, despite some "nice to have" features and no relevant fixes (for my use case) of latest release, I suggest to skip.v7.16beta seems nice to try. Good luck! ---

## Response 21
Yes, this problem applies to AX devices. As far as I understand, there are several problems there. For some users, the problem was resolved when updating to 7.16betaLatest 7.16beta4 does not solve the problem. ---

## Response 22
I'm also having wifi issues on my mikrotik ax3. Unfortunately 7.15.2 doesn't solve this problem... I'm still waiting for a solution from Mikrotik developers.Before the update to 7.15, everything worked fine and there were no such problems. I have already tried different settings, they do not solve the problem in any way.I would also like to point out that the programs (winbox, webfig, mobile application for iOS) for configuration have a different interface for the "Reselect Interval" parameter, which also complicates the configuration of the router and can even create random errors in the configuration.Знімок екрана 2024-07-15 о 23.47.33.pngЗнімок екрана 2024-07-16 о 08.01.25.pngfile_324.jpg2024-07-16 08.13.31.jpg ---

## Response 23
Hi, same behavior about reselect interval ---

## Response 24
Hi, Did you try changing security to WPA2-PSK only and Management Protection to disabled?I have had similar issues/inconsistencies and this seems to have helped (although it is certainly not an ideal solution). I am currently at 7.15.2, so I have yet to do more testing with newer ROS versions. ---

## Response 25
No, I didn't try. I have devices that do not support wpa3 and there are devices that support it, I want those devices that support wpa3 to work through wpa3, and those that do not also have the ability to connect to Wi-Fi. That's why I have wpa2 and 3 enabled. Control protection cannot be turned off if wpa 2 and 3 are used. ---

## Response 26
i have same problems with all of my cap ac xl with capsman, i have 4 ssids and see, that capsman made new wifi slave interfaces with same mac as the main wifi interface, other wifi slaves have not the same mac, i think there is a problem with mac adresses for the slaves. i hope mirkotik will fix this ---

## Response 27
Same here on my hAP ax2 (7.15.2) ---

## Response 28
Can you enable logging on your device 9D:08? maybe you see a reason there why it disconnects. ---

## Response 29
Can you enable logging on your device 9D:08? maybe you see a reason there why it disconnects.How I can enable logging for a device? ---

## Response 30
How I can enable logging for a device?Although "Can you do xxxx?" is frequently used as a polite form of "Do xxxx!", the same wording may surprisingly mean an actual questionSome devices support logging and some don't, and since the MAC address of your device in question is private, it is not possible to find out the vendor, so it is not possible for anyone but you to know whether it is a computer, a mobile phone, or an IoT device, and hence whether logging is supported.Other than that, is only that single MAC address affected in your case? ---

## Response 31
authentication types - they seem to be ignored from security config, leaving my network "open"This is the kind of thing I meant in my first reply: you're setting it from two different places, creating a conflict:NO he is not doing anything wrongWHY, because there is no PROPER process, nor guidance.Setting up wifi on AX is shit show of inconsistency.So please do not blame the poor user, thrown into the meat grinder of completely useless MMI performance. ---

## Response 32
Can you enable logging on your device 9D:08? maybe you see a reason there why it disconnects.How I can enable logging for a device?Depends on the device. If it is a PC or alike it may be easier to access log files than on an iphone (still possible IIRC). But to avoid confusion: I mean logging on the affected device itself. You see a regular disconnect in your AP logs. But you don't know why the client disconnected. That information is not available - except on the client itself. ---

## Response 33
Hi, Did you try changing security to WPA2-PSK only and Management Protection to disabled?I have had similar issues/inconsistencies and this seems to have helped (although it is certainly not an ideal solution). I am currently at 7.15.2, so I have yet to do more testing with newer ROS versions.This was one of suggestions of MikroTik support guy. I can tell that this didn't solve disconnect problem neither on 7.15 nor on 7.15.1 on hap ax3 device (haven't tried 7.15.2 yet, but since there are no changes to wifi-qcom driver, I don't see a reason to give it a shot). I did try a bunch of configurations starting from the one after reset button, ending with a bunch of tweaks and sending around 10-15 supout files - no luck. It now became inconvenient for me to reboot the router here and there to upgrade to 7.15 and rollback again to working firmware after another tweak didn't do the trick, so I gave up on this and now use 7.14.1 until some information on disconnects show up. The only consistent thing I've noticed is that the more load on the network was done, the more chances to disconnect occur. So the connection could be "stable" for hours if I just leave device working, and could drop each 15 minutes while e.g. watching YouTube. ---

## Response 34
Update 7.15.3 does not solve the problem ---

## Response 35
Update 7.15.3 does not solve the problemThis seems to not happen until "wifi-qcom" note appears in a patch-note (which is not the case for 7.15.3 nor beta branch) ---

## Response 36
Greetings!Here is my configuration. I haven't noticed any problems with it on either 7.15.x or 7.16.x versions of ROS. I use the same configuration with CAPsMAN.Laptop - Acer with Intel(R) Wi-Fi 6 AX201 160MHz network card.Drivers for the network card are the latest from Intel's site.
```
# 2024-08-05 16:52:47 by RouterOS 7.16beta7
# software id =
#
# model = C53UiG+5HPaxD2HPaxD
# serial number =

/interface wifi channel add band=2ghz-ax disabled=no name=Home-2.4GHz-auto-AX reselect-interval=1h..1h30m width=20/40mhz
/interface wifi channel add band=5ghz-ax disabled=no name=Home-5GHz-auto-AX reselect-interval=1h..2h skip-dfs-channels=10min-cac width=20/40/80mhz
/interface wifi datapath add bridge=bridge-LAN disabled=no name=datapath-loc
/interface wifi security add authentication-types=wpa2-psk,wpa3-psk connect-priority=0/1 disable-pmkid=yes disabled=no encryption=ccmp ft=yes ft-over-ds=yes group-key-update=1h management-protection=allowed name=secur-Home passphrase=xxxXXXxxx wps=disable
/interface wifi steering add disabled=no name=steering-Home neighbor-group=NG-Home rrm=yes wnm=yes
/interface wifi configuration add chains=0,1 channel=Home-2.4GHz-auto-AX country=Ukraine datapath=datapath-loc disabled=no mode=ap multicast-enhance=enabled name=Home-2ghz-AX qos-classifier=dscp-high-3-bits security=secur-Home ssid=MikroAP-Loc steering=steering-Home tx-chains=0,1
/interface wifi configuration add chains=0,1 channel=Home-5GHz-auto-AX country="United States" datapath=datapath-loc disabled=no dtim-period=3 mode=ap multicast-enhance=enabled name=Home-5ghz-AX qos-classifier=dscp-high-3-bits security=secur-Home ssid=MikroAP-Loc steering=steering-Home tx-chains=0,1
/interface wifi set [ find default-name=wifi1 ] configuration=Home-5ghz-AX configuration.manager=capsman-or-local .mode=ap disabled=no
/interface wifi set [ find default-name=wifi2 ] configuration=Home-2ghz-AX configuration.manager=capsman-or-local .mode=ap disabled=noBy the way.For other WiFi points at home I use this configuration (for cAP ac)
```

```
# 2024-08-05 16:52:46 by RouterOS 7.16beta7
# software id =
#
# model = RBcAPGi-5acD2nD
# serial number =

/interface wifi channel add band=2ghz-n disabled=no frequency=2412,2437,2462 name=Home-2.4GHz-1-6-11 width=20mhz
/interface wifi channel add band=5ghz-ac disabled=no frequency=5180,5260,5500,5580,5745 name=Home-5GHz-MAX reselect-interval=30m..1h skip-dfs-channels=10min-cac width=20/40/80mhz
/interface wifi datapath add bridge=bridge1 disabled=no name=datapath-loc
/interface wifi security add authentication-types=wpa2-psk,wpa3-psk disable-pmkid=yes disabled=no ft=yes ft-over-ds=yes management-protection=allowed name=sec-home passphrase=xxxXXXxxx wps=disable
/interface wifi steering add disabled=no name=steering-LAN neighbor-group=NBG-Group-LAN rrm=yes wnm=yes
/interface wifi configuration add chains=0,1 channel=Home-2.4GHz-1-6-11 country=Ukraine datapath=datapath-loc disabled=no mode=ap name=cfg-Home-2 qos-classifier=priority security=sec-home ssid=MikroAP-Loc steering=steering-LAN tx-chains=0,1
/interface wifi configuration add chains=0,1 channel=Home-5GHz-MAX country="United States" datapath=datapath-loc disabled=no mode=ap name=cfg-Home-5 qos-classifier=priority security=sec-home ssid=MikroAP-Loc steering=steering-LAN tx-chains=0,1
/interface wifi set [ find default-name=wifi1 ] configuration=cfg-Home-2 configuration.manager=capsman .mode=ap disabled=no
/interface wifi set [ find default-name=wifi2 ] configuration=cfg-Home-5 configuration.manager=capsman .mode=ap disabled=no

---
```

## Response 37
There is a linux kernel driver issue with intel ax201/ax210 cards..https://bugzilla.kernel.org/show_bug.cgi?id=203709 ---

## Response 38
What I did to “fix” disconnections on my hAP AX3 was increasing the DHCP lease time from 30 minutes to 1 day on all the interfaces. My iPhone was disconnecting all the time before doing this change. ---

## Response 39
Hi, I only use my HAPax3 device as AP, not router.Since 2/3 weeks, i've removed wpa3 (before wap2 and wp3 were allowed) from security profiles, no more problems. ---

## Response 40
What I did to “fix” disconnections on my hAP AX3 was increasing the DHCP lease time from 30 minutes to 1 day on all the interfaces. My iPhone was disconnecting all the time before doing this change.I've also tried this, (un)fortunately I'm not an Apple user, so all my devices work regardless of DHCP lease time being 30 minutes or more/lessHi, I only use my HAPax3 device as AP, not router.Since 2/3 weeks, I've removed wpa3 (before wap2 and wp3 were allowed) from security profiles, no more problems.There's no WPA3 in my configuration, so sadly this also doesn't solve problems for me. However, WPA3 works good for my devices, so maybe I'll bring it back when the main issue is resolved. ---

## Response 41
I have exactly the same problem after upgrading to 7.15 (7.15.2 at the moment). At first I thought someone was doing a deauthentication attack to speed up the handshake capture, but then I came across this thread.disassoc.PNG ---

## Response 42
I have exactly the same problem on my hAP ax2 at 7.15.3 and 7.16rc2. Laptop with Intel Wireless-AC 9461. Driver version 23.60.0 (i try the many oldest driver too). Random disconnects mostly under load.Changing security to WPA2-PSK only and Management Protection to disabled not resolve the issue.m.JPG ---

## Response 43
Same issues here on 7.15->7.15.3. Downgrade to 7.14.3 fixes the issue.It's maybe also worth noting that I've noticed some specific patterns. Namely, streaming video seems to be a big one: whenever I start a video call on Teams, or watch a movie on Plex on my Google Chromecast, the issue presents itself much more frequently.The worst case I have observed is the Chromecast being barely able to stream just a few seconds of video in between reconnects.It would be nice to have an official acknowledgement from MikroTik, documenting the temporary workaround of downgrading to 7.14.3 and the next steps the company is taking to fix this. (Maybe I have missed it -- in that case, could I kindly be pointed to it?) ---

## Response 44
Downgrade to 7.14.3 fixes the issue.Confirm this. Downgrade to 7.14.3 is the only one work solution for me. At 7.14.3 all works perfect! Mikrotik when you fix this? ---

## Response 45
Tired of waiting for a solution to the problem from the manufacturer, I also reverted to 7.14.3 and everything works fine. ---

## Response 46
Just to add additional feedback, I have a hEX S updated to 7.15.3 which works perfectly and a hAP ax3 stuck on 7.14.3 because it's the last version with which WiFi works well. ---

## Response 47
TL:DR; 7.16rc4 fixes all wifi related issues.I recently was trying to stream a remux to LG C2 via Plex and found out i was also running into the same problem. The Plex log was showing as device(WebOS tv) was constantly getting disconnected and reconnected which then continued the stream on tv. After upgrading to testing channel or beta 7.16rc4 it seems to have fixed the issues. ---

## Response 48
TL:DR; 7.16rc4 fixes all wifi related issues.I recently was trying to stream a remux to LG C2 via Plex and found out i was also running into the same problem. The Plex log was showing as device(WebOS tv) was constantly getting disconnected and reconnected which then continued the stream on tv. After upgrading to testing channel or beta 7.16rc4 it seems to have fixed the issues.I have exactly the same TV and HAP AX3 is 1m away from it, and also getting random dcs while watching plex, or router makes TV + multiple other devices roam from 5ghz to 2ghz exactly the same time for no reason which also interrupts my plex stream.All was on fine 7.14.3. ---

## Response 49
TL:DR; 7.16rc4 fixes all wifi related issues.I recently was trying to stream a remux to LG C2 via Plex and found out i was also running into the same problem. The Plex log was showing as device(WebOS tv) was constantly getting disconnected and reconnected which then continued the stream on tv. After upgrading to testing channel or beta 7.16rc4 it seems to have fixed the issues.I recently gave a shot for rc3 too. At first, it seemed to be that it fixes a problem, it was stable for like 2 days or so, so I decided to give a try for WPA2/3 also. And within an hour I got a bunch of problems with every single device on wireless network, related to SA Query timeouts and reauthenticating. Reverting WPA2/3 back to WPA2 only, however, brought wireless network to a more stable state, while Intel AX201 device returned to its "disconnect each 5 minutes" state. So, I decided to give up at this point and revert back to 7.14.3, reporting each stage of testing to my opened support ticket.Since they've pinged me with a bunch of questions in this ticket after a month of silence and me gave up at this point, I think they're doing a great job to investigate this issue, so I really hope for a real fix in 7.17beta (or at least, a temporary revert to a wifi driver). ---

## Response 50
TL:DR; 7.16rc4 fixes all wifi related issues.Can anyone else confirm that 7.16rc4 resolve issue with wi-fi 5Ghz random disconnects ? ---

## Response 51
TL:DR; 7.16rc4 fixes all wifi related issues.Can anyone else confirm that 7.16rc4 resolve issue with wi-fi 5Ghz random disconnects ?7.16rc4 does not solve the problem! 2 hours of work without failures, then the same problems appeared. Rolling back to 7.14.3 is the only solution so far. ---

## Response 52
Would be beneficial if all people with problems share their config (at least the /interface/wifi part) to validate settings.Additional tip: when going up and down in versions you might run into some strange problems. Actually, I did...hence some steps that might be of use.I would advise (in case you want to give it another try) to:Create a config (using export)Reset the device, no default settingsRestore the config (using import)Be aware that some settings aren't part of the export (i.e. users).My ax's and ac's are all working perfectly fine with 7.16 rc4At least, send supout.rif file to support. ---

## Response 53
7.15+ wifi-qcom drivers are instable with Intel clients. That is already known and confirmed even by Mikrotik ---

## Response 54
Yes, I know. And I'll tell my corporate laptop it should disconnect more often ---

## Response 55
I've sent a bunch of supouts already, the last advice is to set channel width to 20 Mhz which is kinda weird for a 5Ghz network. They also stated that the issue only reproduces with windows version of Intel drivers (Linux clients are stable) dunno if it is the case.It's also worth noting that windows begins producing eventID 6062 - Lso was triggered, if it means something. There's not much information I've found about this event on the Internet. ---

## Response 56
https://answers.microsoft.com/en-us/win ... c9c40f7491No help at all. Classic Microsoft Forum topic.Even if not related to wifi-qcom:On wifi-qcom-ac my Linux Notebook with AX200 very often refused to connect to 2.4ghz when channel was 40mhz or was not even able to connect. Can't remember exactly. It basically connected to 5ghz most of the time and I did not notice this issue for a long time. I may changed device orientation or something and the signal dropped a little, and notebook tried to roam to 2.4. But it resulted in no wifi connection, because of iwlwifi flooding the log with DEAUTH CLIENT LEAVING messages (don't remember exact wording). After switching to 20mhz channel on 2.4ghz the notebook now can connect to 2.4ghz as well. Really astonishing. But maybe some Bluetooth interference or something. ---

## Response 57
I've sent a bunch of supouts already, the last advice is to set channel width to 20 Mhz which is kinda weird for a 5Ghz network. They also stated that the issue only reproduces with windows version of Intel drivers (Linux clients are stable) dunno if it is the case.It's also worth noting that windows begins producing eventID 6062 - Lso was triggered, if it means something. There's not much information I've found about this event on the Internet.Everything happens exactly as you described. Laptop with Intel Wireless-AC 9461, Windows 11. Warning in the event log ID 6062 - Lso was triggered after which the disconnection occurs. This situation usually occurs under network load, such as streaming video, downloading large files. ---

## Response 58
I'm not sure, does it make sense to share my ticket here? Can other people see my supouts and so on? ---

## Response 59
Have you both installed the latest drivers from Intel?https://www.intel.com/content/www/us/en ... =[Wireless]WiFi Date: 08/20/2024 Version: 23.70.2Bluetooth Date: 08/20/2024Version: 23.70.3Advice is to use the .exe Don't just install the driver using device manager, if you did just run the .exe files from above.Search CMD right click Run as adminitrator using the following command.....netsh wlan show wlanreportIt will build a report @ C:\ProgramData\Microsoft\Windows\WlanReport\wlan-report-latest.htmlGot 3 Machines that will stay connected all day here on the qcom driver!p.s Don't forget to run the command to build a report each time! ---

## Response 60
I've updated the driver with MT support from Intel site, at the moment of ticket opening it was v. 23.30.something release date 01.24 latest driver and there was no success.I've downloaded the one from your link and it shows v. 23.70.2.3 release date 24.07.2024 (AX201). It seems releases occur less frequently for this series of adapters, according to release date you provided. Will give it a shot once again, probably today ---

## Response 61
It's all the same package!https://www.intel.com/content/www/us/en ... loads.html ---

## Response 62
I get Intel AX200 driver updates by Windows Update. Why the heck are you downloading drivers manually from Intel's website???? ---

## Response 63
I have a problem not only with Intel drivers. I have problems with AMlogic TV-box (BeeLink s912) on Android 9 and Lenovo tab on Android 13 when watching videos from MeGoGo or YouTube ---

## Response 64
I get Intel AX200 driver updates by Windows Update. Why the heck are you downloading drivers manually from Intel's website????Why would I get the latest updates/security updates, Really! ---

## Response 65
Driver/Firmware/Bios updates are optionally. You can install these via WU without installing regular updates AFAIK. ---

## Response 66
I get Intel AX200 driver updates by Windows Update. Why the heck are you downloading drivers manually from Intel's website????On more then one occasion I noticed Intel drivers where NOT updated by Windows Update. So don't count on it.I also have been chasing wifi issues not too long ago in the past only to find out a new driver was available directly on the supplier website which after installation fixed the issues I was having (not only with MT APs, also Symbol, Netgear, ...).I currently have AX211 in my laptop BTW. Zero problems. ---

## Response 67
Depends what channel you are in on Windows, IE your drivers will auto downgrade as well on some. Thats why i have Auto udates turned off on my PC's. ---

## Response 68
Turning of Auto-Updates is not the same as not updating your system at all. All these decades and Windows still hasn't managed to supply device drivers in a proper and easy way for users. ---

## Response 69
And where is the surprise ... ?After all, it's Microsoft we're referring to here ---

## Response 70
7.16rc4 and reducing the 5 GHz channel width to 20 MHz solves the problem, there are no WiFi breaks. ---

## Response 71
Maybe 20mhz channel width also resolves it on 7.15? ---

## Response 72
It would be nice to see what Signal ranges we are talking about here ?-70's/-80's or just any Signal range. ---

## Response 73
This is not a (permanent) solution since reducing channel width also lowers throughput. ---

## Response 74
This is not a (permanent) solution since reducing channel width also lowers throughput.I agree. It's stupid to buy an expensive router and cut the data transfer speed... But nevertheless, it works.I checked 20/40 MHz - it doesn't work. ---

## Response 75
Well, Mikrotik AX devices are all but expensive. ---

## Response 76
Hihas anyone tested 7.16? ---

## Response 77
Hihas anyone tested 7.16?7.16 does not solve the problem ---

## Response 78
Hihas anyone tested 7.16?I have updated.24 hours, everything is ok! ---

## Response 79
Hihas anyone tested 7.16?7.16 does not solve the problem7.17beta2 does not solve the problem to. I am very disappointed, I really wanted to buy a Mikrotik router, because it provides great flexibility of settings, but now I see that Mikrotik engineers can not cope even with basic tasks. Why should I, like an idiot, go through the firmware in the hope that they fixed the banal problem of disconnecting wifi on AX devices, which everyone has known about for a long time. If you can not solve it yourself, roll back the Qualcom driver. I am very disappointed. I use more than 400 Mikrotik devices in my work as a system administrator, and I always recommended them to my clients, but apparently this has come to an end. ---

## Response 80
I have same issues ---

## Response 81
I also notice this behavior, but mostly with only one device. In my case, with Chromecast with Google TV 4K. ---

## Response 82
7.16 does not solve the problem7.17beta2 does not solve the problem to. I am very disappointed, I really wanted to buy a Mikrotik router, because it provides great flexibility of settings, but now I see that Mikrotik engineers can not cope even with basic tasks. Why should I, like an idiot, go through the firmware in the hope that they fixed the banal problem of disconnecting wifi on AX devices, which everyone has known about for a long time. If you can not solve it yourself, roll back the Qualcom driver. I am very disappointed. I use more than 400 Mikrotik devices in my work as a system administrator, and I always recommended them to my clients, but apparently this has come to an end.I had the same problem on 7.15.3 and had to go back to 7.14.3 where everything worked fine.Yesterday I still dared to try 7.16 and everything works fine for me. ---

## Response 83
TLDR; The fix was to limit myself to only channels up to 124.I got a hap ax3 and ax2 and have literally 0 issues with AX ClientsI'm currently running 7.17beta2, but always been running the latest version since December 2023.Some of the issues here sound similar to mine when started deploying Intel AX210 and BE200 Cards.Anything above 5ghz Channel 124 they only wanted to connect to with 20mhz channel width. (the issues sometimes were that it only connected at 802.11n speeds and sometimes it wouldnt connect at all)Keeping in mind, I'm from Germany.And that i also had this issue with AC only APs from competitors.If anyone is interested in my findings with AX210 and BE200 cards regarding this issue, it's mostly on the Intel Forum:https://community.intel.com/t5/Wireless ... -p/1550533I don't have any AX210s anymore but I've attached a screenshot of my working FT, WPA3, AX, 80Mhz Setup:Untitled.pngFor reference, I tried these network cards and they all work flawlessly:Any Channel:Realtek RTL8852AEMediatek MT7922 (aka AMD RZ6XX)Below Channel 124:Intel AX210Intel BE200 (Windows + Linux)Qualcomm WCN685x (not sure which exact version it is) ---

## Response 84
TLDR; The fix was to limit myself to only channels up to 124.What's the ROS version you have where it works? ---

## Response 85
TLDR; The fix was to limit myself to only channels up to 124.What's the ROS version you have where it works?Currently, 7.17beta2.But the last version I was able to test the AX210 with was 7.14.2 I think.The BE200 I was able to test with all versions 7.13+ and it's been working perfectly fine (well, since working Linux drivers have been released)Since i only ever had the issue with the Intel AX Cards, and it even occurred with an AC only router (ZTE MF281. Its an ISP LTE Router) i never even checked the mikrotik forums about it. ---

## Response 86
is yours 2.4 or 5g??as i was having same problems but i dont have hardly any anymoreim on the 7.17 beta but i had it working and roaming before this betai found it is the 2.4 that seem to be having all the issuesbut i hardly get any now with my config changesI have same issues ---

## Response 87
is yours 2.4 or 5g??as i was having same problems but i dont have hardly any anymoreim on the 7.17 beta but i had it working and roaming before this betai found it is the 2.4 that seem to be having all the issuesbut i hardly get any now with my config changesI have same issuesSeems to be with both 2.4G and 5G ---

## Response 88
i have lots of screen shots to show you but i wont do it here on OPm8 go to wifi config and put DTIM period up to 8 on the 2.4 and 3 on the 5g try it works for me i get hardly any disconects nowif not i will do a new post with my config so you can try my settings ---

## Response 89
i have lots of screen shots to show you but i wont do it here on OPm8 go to wifi config and put DTIM period up to 8 on the 2.4 and 3 on the 5g try it works for me i get hardly any disconects nowif not i will do a new post with my config so you can try my settingsOk I will try this tonight, I'm limited on making changes because it's a live network and users will go ape. ---

## Response 90
dtim-period is "1" by default. Some have dedicated SSID for IoT devices - which are mostly battery powered. In such a case a DTIM period of 2 may improve batter life. Maybe it even helps with disconnects - but can't test as I do not have "flapping clients". ---

## Response 91
Note that Apple recommends DTIM interval of 4. ---

## Response 92
Apple recommends DTIM interval of 4.Where? Theircurrent recommendationsdo not speak of DTIM at all.For what it's worth, I've gone back and documentedmy hAP ax³ WiFi configurationin more detail thanmy post #2 above, which continues to work nicely with several Apple devices, and has done since 7.14rc2 back in February, when I installed it. I've installed many releases between, up to 7.17beta2 now, and I never noticed any serious regressions.I really don't understand all this moaning. I suppose y'all are doing something quite different than I am, and these differences materially affect the symptom. My article may help here, if only by providing baseline known-working configuration. ---

## Response 93
It happens with any kind of configuration, whether it's defconf or not, and support guy told me they replicated the problem with Intel AX in their lab. I haven't noticed any issues with 7.14.3. But any 7.15 onwards the disconnects are just waaaay to often. All stuff that we tried with support worked anyway in 7.14 and did not in 7.15+ and yes I do upgrade routerboard etc etc.I'm not sure if the problem is the same with other devices, since laptop with Intel AX is my main wireless device and all focus was to fix this. Other devices are rare to no disconnects, or I didn't notice them. It's even worse with WPA3 enabled.If you don't have a problem, doesn't mean no one also have it nor it means they are just retards. ---

## Response 94
…support guy told me they replicated the problem with Intel AX in their labI was speaking of Apple devices, which as far as I know, do not include the affected Intel AX chipsets. Regardless, I am not attempting to gainsay the MT engineers on this one; if they say the chipset has a bug that affects RouterOS compatibility, then I believe them.What I object to is this "everything is terrible" attitude I'm seeing while it's been working here, steadily, since February. There's a mismatch somewhere, and I'd like to try and resolve it, not fall into an endless moan-fest.If you don't have a problem, doesn't mean no one also have it nor it means they are just retards.I did not use that derogatory term, and as a moderator here, I caution you against using it again on this forum.Rather than name-call the others, I prefer to contribute positively, as with this article I've just written, presenting a working configuration for at least one person, me. How much broader does that go? I don't know, but it's objectively the case that everything isn't terrible for everyone. ---

## Response 95
Rather than name-call the others, I prefer to contribute positively, as with this article I've just written, presenting a working configuration for at least one person, me. How much broader does that go? I don't know, but it's objectively the case that everything isn't terrible for everyone.I didn't name-call others, I rather meant the opposite - pretty sure people do best effort to fix this, not just throw "everything is bad" messages. Same for me.I appreciate your effort and took time to inspect your config. This is actually the same as I get right after /sys/reset. The only moment is that device auto-select 5GHz channel 5500 which doesn't work for half of my devices, so I have to specify channels manually. And yes, one step with support was: "reset your device to just wifi+default gateway and check if you have problems" which didn't succeed.I've bought my device around week or two before 7.15 release, so all stuff was good until update. And as I said, every time support suggested me a config change, I did update to 7.15+, checked if it works or not and downgrade back (because of unusable device) leaving changed config. And whatever changes we did worked well in 7.14. And yes I update adapter drivers directly from Intel site, so they're latest. After all my attempts I gave up as one of latest firmwares introduced another bug for me which I've also reported to them, so it wasn't comfortable for me to upgrade back and forth as ax3 device is my only home router. Supports told me they'll notify on changes, so I'm confident I did what I could, and not just moan. ---

## Response 96
Apple recommends DTIM interval of 4.It used to be 3 quite a few years ago. But they have since updated their documents. Use DTIM that suits best for you.I really don't understand all this moaning. I suppose y'all are doing something quite different than I am, and these differences materially affect the symptom. My article may help here, if only by providing baseline known-working configuration.I have to +1 this, since it's working perfectly fine for me with newest (and older) intel Wi-Fi drivers (as documented on the intel forum).Also on the Intel Forums, there's also a lot of people having issues with Intel AX/BE Chips with non Mikrotik routers ^^Since my wifi conf is extremely simple i'll just drop it here:
```
name="conf_5" ssid="SECRET" country=Germany multicast-enhance=enabled security=common-auth 
     security.authentication-types=wpa2-psk,wpa3-psk .encryption="" .passphrase="SECRET" .wps=disable .ft=yes 
     datapath=VLAN0 
     datapath.bridge=bridge .vlan-id=1 
     channel.frequency=5160-5640 
name="conf_2.4" ssid="SECRET" country=Germany multicast-enhance=enabled security=common-auth 
     security.authentication-types=wpa2-psk,wpa3-psk .encryption="" .passphrase="SECRET" .wps=disable .ft=yes 
     datapath=VLAN0 
     datapath.bridge=bridge .vlan-id=1 
     channel.frequency=2412-2472 .width=20mhzEdit: as statet before i've been running this config since 7.13.X (dont remember exactly) and its been working perfectly ever since

---
```

## Response 97
```
/interface wifi channel
add band=5ghz-ax disabled=no frequency=5220,5180-5320,5660-5845 name=5ghz skip-dfs-channels=10min-cac width=20/40/80mhz
/interface wifi security
add authentication-types=wpa2-psk disabled=no management-protection=disabled name=home-private
/interface wifi
set [ find default-name=wifi1 ] channel=5ghz configuration=home-private-cfg configuration.mode=ap disabled=no name=wifi-5ghz
/interface wifi configuration
add country="United States" datapath=home-private-datapath disabled=no name=home-private-cfg security=home-private ssid=\
    xxx
/interface wifi datapath
add bridge=bridge disabled=no name=home-private-datapath vlan-id=100This is my current running config for 5GHz. Nothing special. Works on 7.14.3. Doesn't work 7.15+. Driver ver. 23.70.2.3. Works on any other router I've interfered with (d-link, tp-link, mikrotik 6.xx firmwares ap, ubiquity, some public wifi stuff and so on).

---
```

## Response 98
@tangentThe origin is (probably) a (I believe now lost forever) twitter post, cited here (which explains some of the reasons to increase DTIM interval for Apple devices):https://www.sniffwifi.com/2016/05/go-to ... sleep.htmlThe analysis seems to make sense, and this "set DTIM to 3" advice can be found in a lot of places, the DTIM 4 is new (at least to me). ---

## Response 99
```
/interface wifi channel
add band=5ghz-ax disabled=no frequency=5220,5180-5320,5660-5845 name=5ghz skip-dfs-channels=10min-cac width=20/40/80mhz
/interface wifi security
add authentication-types=wpa2-psk disabled=no management-protection=disabled name=home-private
/interface wifi
set [ find default-name=wifi1 ] channel=5ghz configuration=home-private-cfg configuration.mode=ap disabled=no name=wifi-5ghz
/interface wifi configuration
add country="United States" datapath=home-private-datapath disabled=no name=home-private-cfg security=home-private ssid=\
    xxx
/interface wifi datapath
add bridge=bridge disabled=no name=home-private-datapath vlan-id=100This is my current running config for 5GHz. Nothing special. Works on 7.14.3. Doesn't work 7.15+. Driver ver. 23.70.2.3. Works on any other router I've interfered with (d-link, tp-link, mikrotik 6.xx firmwares ap, ubiquity, some public wifi stuff and so on).You getting any issues with that setup?Does your devices roam without ft=yes ft-over-ds=yes?

---
```

## Response 100
This is my current running config for 5GHz. Nothing special. Works on 7.14.3. Doesn't work 7.15+. Driver ver. 23.70.2.3. Works on any other router I've interfered with (d-link, tp-link, mikrotik 6.xx firmwares ap, ubiquity, some public wifi stuff and so on).Mikrotik V6 doesn't support AX.You sure you were connected with AX for the others? ---

## Response 101
You getting any issues with that setup?Does your devices roam without ft=yes ft-over-ds=yes?Yes I had disconnects with Intel AX on that. Ax3 is a single stand-alone device, so there's nowhere to roam. Support told me that those options make no sense in my setup (but are enabled by default). In one of testing iterations I've disabled them. ---

## Response 102
Hey all, I had the same issues with disconnects on my hap ax2 and ax3 (capsman with FT), and just wanted to share that enabling tkip cipher helped. I know, weird, but it's working for me. I tested a lot of methods, 20mhz channel width, management protection, ft disabled etc. But only enabling tkip cipher in security works and my chromecast and macbook can connect to wifi now. ---

## Response 103
Ax3 is a single stand-alone device, so there's nowhere to roam.Sure there is: from 5 GHz to 2.4 and back when both radios have the same SSID. FTdoesapply in this case! ---

## Response 104
Ax3 is a single stand-alone device, so there's nowhere to roam.Sure there is: from 5 GHz to 2.4 and back when both radios have the same SSID. FTdoesapply in this case!I have 5GHz and 2.4GHz SSIDs separate as 5GHz covers area well enough, so I wanna make sure all devices use 5GHz all time ---

## Response 105
Today I got Wi-Fi disconnects on 7.16 with a channel width of 20 MHz.I see everything is bad with the new driversSent supout.rif to support ---

## Response 106
I've recently heard an opinion that connected USB3 device may affect wireless (friends who have ax3 had problems with usb and didn't have without). I had problems before I attached USB disk, and now there isn't much transfers (only error logs by now). Maybe it will be useful if anyone who has problems would also note in their messages if they use USB or not. ---

## Response 107
I've recently heard an opinion that connected USB3 device may affect wireless (friends who have ax3 had problems with usb and didn't have without). I had problems before I attached USB disk, and now there isn't much transfers (only error logs by now). Maybe it will be useful if anyone who has problems would also note in their messages if they use USB or not.There are know issues with USB 3.x devices, not only Mikrotik related, but they should be limited to the 2.4 GHz, because the frequencies are essentially the same and interferences happen, see:viewtopic.php?t=203470and official USB document.https://www.usb.org/sites/default/files/327216.pdf ---

## Response 108
old post i no but get one of these in 32g works perfetly on 7/17beta2 running my containrers and no wofo issuesModel Number: SDCZ430-016G-Z35SanDisk Ultra Fit USB 3.2 Flash Drive - 16GB ---

## Response 109
My dear friends, I am finally back to 7.14.3 againAt first, 7.16 worked fine, but then problems with turning off Wi-Fi started againI tried the test 7.17 beta 2, the situation is even worse there...I'm back on 7.14.3 ---

## Response 110
Stupid me tried to install 7.16 and I could not work with putty anymore.Downgrade to 7.15.3 works nicely for me.SIgnal is slow, I frequently roamin from 5G to 2.4G and back, but no disconnection like with 7.16 ---

## Response 111
Follow-up my hap ax3 / google chromecast gen3 / ROS > 7.14.3 problem.viewtopic.php?p=1078328#p1078328I tried any other ROS version post 7.14.3 and any WiFi workaround posted here.Unfortunately got the same behavior, in a few seconds after cast all the WiFi devices in the house get insta disconnected. Roll back to 7.14.3 every time.Today I managed to fix the problem for me.I bought an Ugreen 30985 external network card for Chromecast with micro USB / USB-A connectors, 100Mb/s, and now I use the chromecast wired.No more disconnects, v 7.16 stable. ---

## Response 112
I have the same issue on my hap ax3firmware is latest 7.16.1 ---

## Response 113
Downgrading to 7.14.3 solved the problem for me ---

## Response 114
7.17beta 4 no changes. 7 hours of work and wifi drops again ---

## Response 115
Currently running ROS 7.16.1.I was having issues with my "Intel(R) Wi-Fi 6 AX201 160MHz" card dropping connection since 7.15.I applied a critical Dell driver update yesterday and the issue seems to be resolved:Uptime 17.47:xxSignal -65Could it be an Intel driver issue and not a Mikrotik issue? ---

## Response 116
I'm on 7.16.1 for now, intel driver v. 23.70.2.3. I don't have time now to play games and so on, so it's hard for me to notice disconnects that I had before. But logs are filled with this:19:08:39 wireless, info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -7019:08:39 wireless, debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -7019:08:39 wireless, debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength -6619:08:39 wireless, info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength -6619:24:08 wireless, info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -7019:24:08 wireless, debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -7019:24:08 wireless, debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength -7119:24:08 wireless, info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength -7119:24:09 wireless, info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -7119:24:09 wireless, debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -7119:24:13 wireless, debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength -7019:24:13 wireless, info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength -7019:25:08 wireless, info 0C:7A:15:F5:D2:AF@wifi-5ghz disconnected, connection lost, signal strength -7319:25:08 wireless, debug 0C:7A:15:F5:D2:AF@wifi-5ghz disassociated, connection lost, signal strength -7319:25:11 wireless, debug 0C:7A:15:F5:D2:AF@wifi-5ghz associated, signal strength -7219:25:11 wireless, info 0C:7A:15:F5:D2:AF@wifi-5ghz connected, signal strength -71Windows logs are filled with netwtw10 warning 6062 and info message 7021. And this is only reproducible on a MikroTik router with 7.15+ firmware. ---

## Response 117
I have the very some problem, with many devices including my LG TV, NVIDIA Shield, my iPhone and iPad. I can’t watch movies from my Plex Media Server anymore because from time to time wifi keeps disconnecting on my ax3, I have to reconnect and restart the stream. Downgrading to 7.14.3 fixes everything, but it’s been months now and there’s no fix on newer firmware, what’s up with that, are we going to be stuck with 7.14.3? ---

## Response 118
Still the same for me : hap ax3 icw chromecast. Is disappointing: I bought a brand new ax3 this year, and now i'm stuck with v7.14.3When will this be solved ? ---

## Response 119
What is in itself the problem of remaining at 7.14.3 (at least for the time being)?Is there specific functionality missing that was introduced from 7.15 upwards? ---

## Response 120
What is in itself the problem of remaining at 7.14.3 (at least for the time being)?Is there specific functionality missing that was introduced from 7.15 upwards?7.15 patch notes include wifi-qcom driver update. ---

## Response 121
7.15 patch notes include wifi-qcom driver update.I thought that the issues were causedmainlyby that driver update, it doesn't sound like a desired new functionality ... ---

## Response 122
Currently running ROS 7.16.1.I was having issues with my "Intel(R) Wi-Fi 6 AX201 160MHz" card dropping connection since 7.15.I applied a critical Dell driver update yesterday and the issue seems to be resolved:Uptime 17.47:xxSignal -65Could it be an Intel driver issue and not a Mikrotik issue?No, I have tried many Intel drivers but the error is always the same. ---

## Response 123
Some horror here, every day several times, very unpleasant and only on 5GHz.I have Intel(R) Wi-Fi 6 AX201 160MHz work on 2GHz - no problems! ---

## Response 124
Is there a chance to escalate this issue? It seems that the developers of RouterOS 7.x do not know anything about this. ---

## Response 125
Is there a chance to escalate this issue? It seems that the developers of RouterOS 7.x do not know anything about this.As you know, assumption is the mother...etc.Just contact support to address your problem. ---

## Response 126
Is there a chance to escalate this issue? It seems that the developers of RouterOS 7.x do not know anything about this.I have contacted. No solution yet.Your request status has been changed to Waiting for support.18/Sep/24 9:10 AM ---

## Response 127
Looks like Intel new Wireless Bluetooth driver 23.90.0 and 7.17beta5 work fine for me. No more discconects under load. I'm testing about 3 hours. Can anybody else confirm that? ---

## Response 128
Looks like Intel new Wireless Bluetooth driver 23.90.0 and 7.17beta5 work fine for me. No more discconects under load. I'm testing about 3 hours. Can anybody else confirm that?What's the version is shown on WiFi dongle itself in the device manager? ---

## Response 129
Looks like Intel new Wireless Bluetooth driver 23.90.0 and 7.17beta5 work fine for me. No more discconects under load. I'm testing about 3 hours. Can anybody else confirm that?3 hours is too little, I was fine for a day, then the falls started again...wait 2-3 days, then say whether it's good or not. ---

## Response 130
Looks like Intel new Wireless Bluetooth driver 23.90.0 and 7.17beta5 work fine for me. No more discconects under load. I'm testing about 3 hours. Can anybody else confirm that?What's the version is shown on WiFi dongle itself in the device manager?23.70.2.3 ---

## Response 131
I'm at the same driver version but can't confirm this works on 7.16.x, not sure about beta ---

## Response 132
Looks like Intel new Wireless Bluetooth driver 23.90.0 and 7.17beta5 work fine for me. No more discconects under load. I'm testing about 3 hours. Can anybody else confirm that?7.17beta6 broken again?Im create ticket and send support.rif to mikrotik. ---

## Response 133
The issue is not only with intel adapters, some qualcomm xiaomi mobiles are disconnecting too. Also still sitting on 7.14.3 where everything works perfect. All the later firmware including 7.16.1 still cause disconnects. ---

## Response 134
This is slightly off topic, but can be interesting to read.Looking at this forum thread, I recognize a lot off the issues.But there is a difference in my experiences with AX.When the devices were released, I replaced all APs in my home. Then I noticed that the range is not as good as from the AC devices. To I doubled the number of APs. Each room has it's own AP. And the living room has two. One cap AX at 2.4 and 5, and a hap ax3 at 5 on a high channel with low power output (this is only for the dinner table).This setup works fine since the beginning, with all versions of routeros.Note that we only use Apple devices and just a few windows laptops from Lenovo for school and work. (I have a large family)I have 9 APs (5x cap ax, 1x wap ax, 3x hap ax3).The router is a CCR2004-16G-2S+.Current version is 7.16.1 on all devices.There are 7 ssids on different vlans.And on average 45 clients connected (including smart lights and sensors)Wpa3, wpa2, 802.11r (FT + FT over DS), 802.11k (steering rrm) and 801.11v (steering wnm) are all enabled (except on the ssid for smart lights). Used channels are 1, 5, 9, 13, 36, 40, 44, 48, 149, 153, 157.Vlan config, is tagged for all SSID's, but untagged for the capsman/management.It works fine, so it CAN work!But now comes the bad part...Keeping in mind that my AX system works, and that large AC setups were never a problem, I rolled out three large locations with AX.115x cap ax +- 400 clients44x cap ax +- 300 clients71x cap ax +- 500 clientsFrom the start I have many issues, like in this thread, disconnecting and reconnecting devices.Can you imagine what it's like to work on your laptop, sitting on the exact same spot for all day, having your wifi drop every 5 minutes?With the AP in sight?That is exactly what is happening!Many windows laptops just keep hanging on the worst AP they can find.Keep connecting and disconnecting from the wifi.While stationary!!!Old phones too, they just don't work.The range of the cap ax is less than the cap ac, maybe 6 meters at most.With new devices, things work better, more range, less disconnects.To make it at least usable, in the end I had to disable WPA3, FT, RRM and WNM. Also a good solution is to put an extra AP next to people with many complaints.I think at the MikroTik support desk, they only have the working AX, like I have at home.They can't imagine that their stuff doesn't work, but in some cases it doesn't.And it can't all be blamed on bad AP placement, wrong settings...Anyway, if you are out there having issues with your AX setup, keep in mind that it CAN work.And in the meantime, let's hope updates in the future will remove all issues like magic. ---

## Response 135
Thank you for this objective and informative insight. Things are not always black and white. ---

## Response 136
I have Zero issues with 7.17beta6 just WPA2 using capsman is very stable, I look forward to the release. it's far better than 7.16.1Also using the latest 11.11.2024 Intel driver with no problems.
```
Interface name: WiFi

    Driver                    : Intel(R) Wi-Fi 6E AX210 160MHz
    Vendor                    : Intel Corporation
    Provider                  : Intel
    Date                      : 26/09/2024
    Version                   : 23.90.0.2@sszbv I feel your pain brother, it's been a journey for sure!

---
```

## Response 137
FWIW I had AX3 and now wAP AX on my desk.Since I have that wAP AX I use my laptop only via wifi. Zero disconnects. And using Azure Remote Desktop when working from home I would know immediately ... that environment is HIGHLY allergic to disconnects, even for a split second.(Using AX3 I also have used that setup for testing, also there, no problems noticed)I do see sporadic loggings indicating so but no disconnects on the client device itself. ---

## Response 138
To make it at least usable, in the end I had to disable WPA3, FT, RRM and WNM. Also a good solution is to put an extra AP next to people with many complaints.I think at the MikroTik support desk, they only have the working AX, like I have at home.They can't imagine that their stuff doesn't work, but in some cases it doesn't.This is not a hardware problem, this is a software problem, on 7.14.3 everything works perfectly, for everyone. The problem started after 7.14.3, many on the forum think that it is related to the update of the Qualcomm driver. ---

## Response 139
I've also been suffering these disconnects for a while on my hAP ax3 but only on the 5G radio, I've been updating to latest ROS releases as they come out since I got it about a year ago and it seems like the issue has been getting progressively worse as the versions progressed. Since I remember noticing a little bit of issues at first, growing in severity until I finally got fed up and looked into it yesterday.Before yesterday I was on 7.16.3 and (without my chromecast connected) it would last for about a week tops and then start to get a bit unreliable. I also noticed that changing settings on the 5G interface would accelerate the degradation of its reliability. A reboot would fix it for a random amount of time. No different settings changed anything at all, I tried many variations of my own config, and also adopting configs that people have posted as "working configs", changing only the SSID, password and country. With my chromecast connected I noticed that if it was connected to 5G it would trigger the 5G radio to be rendered unusable (im talking repeating intervals of 15-45 seconds of it functioning followed by 30-120 seconds of being completely dysfunctional), even right after a reboot. With the chromecast connected to 2.4G, it was fine in that regard. However it would buffer alot and have quality reductions since my 20+ neighbours in wireless range have butchered the 2.4G band with overlapping and 80MHz wide channels, causing low speeds on 2.4G. I'm not attributing that to ROS issues since even with all that interference and noise the 2.4G interface doesn't drop out completely like 5G does, its just slow as hell.Another interesting thing I observed is that while the chomecast was causing the 5G interface to have a fit and barely work, it would also cause the 2.4G interface to have less performance (but not completely drop out) than it normally does. I didn't do any in depth analysis on it, I just noticed that both my phone and laptop would load websites noticeably slower (since I was researching the issue) while the chromecast was connected to 5G than when it was not. I have no idea if this is simply due to a software bug maxing out the hAP's CPU causing the slow downs or something else going on in the airwaves.Since I downgraded to 7.14.3 its been working perfectly fine even with my normal pre-debugging config with WPA2+3 and protected management frames enabled. The chromecast connects quickly (to 5G) when i turn it on unlike before where it took a long time. And both wifi bands function perfectly fine even after hours of watching stuff on the chromecast. I tried stress testing it to see if I could get it to break, by changing settings a bunch of times while saturating the connection with iperf and while reconnecting devices frequently, and I couldn't get it to fail on this version YET. It seems rock stable, but ive only had it running for 24 hours so far. I'll report back if time brings issues. ---

## Response 140
Some users which are testing 7.17rc versionviewtopic.php?t=212754are reporting, that on this version everything working ok and there are no disconnects. ---

## Response 141
Some users which are testing 7.17rc versionviewtopic.php?t=212754are reporting, that on this version everything working ok and there are no disconnects.No. Unfortunately, updating to 7.17rc2 didn't help me.Android devices started disconnecting 10 minutes after the update. ---

## Response 142
Hey guys, I just did an update to 7.16.2 after couple of months on 7.14.3I am facing similar wifi disconnection on 5Ghz interface.Can anyone recommend the latest stable version after 7.14.3 to keep the wifi stable ---

## Response 143
Can anyone recommend the latest stable version after 7.14.3 to keep the wifi stableThe issue still not fixed, we all sitting on downgraded to 7.14.3 firmware. ---

## Response 144
Thank God I found this thread because I was going crazy with the random disconnects.
```
2024-12-20 12:45:37	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 disconnected, connection lost, signal strength -63	
2024-12-20 12:45:38	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 connected, signal strength -57	
2024-12-20 12:45:42	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 disconnected, SA Query timeout, signal strength -58	
2024-12-20 12:45:50	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 connected, signal strength -57	
2024-12-20 12:45:52	memory	wireless, info	B0:3C:xx:xx:xx:xx@wifi1 disconnected, SA Query timeout, signal strength -59	
2024-12-20 12:46:00	memory	wireless, info	B0:3C:xx:xx:xx:xx@wifi1 connected, signal strength -59	
2024-12-20 12:51:01	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 disconnected, connection lost, signal strength -58	
2024-12-20 12:51:02	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 connected, signal strength -57	
2024-12-20 12:51:05	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 disconnected, connection lost, signal strength -56	
2024-12-20 12:51:09	memory	wireless, info	B0:3C:xx:xx:xx:xx@wifi1 disconnected, connection lost, signal strength -60	
2024-12-20 12:51:11	memory	wireless, info	B0:3C:xx:xx:xx:xx@wifi1 connected, signal strength -68	
2024-12-20 12:51:11	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 connected, signal strength -57	
2024-12-20 12:51:14	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 disconnected, connection lost, signal strength -62	
2024-12-20 12:51:15	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 connected, signal strength -57	
2024-12-20 12:51:18	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 disconnected, connection lost, signal strength -57	
2024-12-20 12:51:20	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 connected, signal strength -57	
2024-12-20 12:51:25	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 disconnected, SA Query timeout, signal strength -59	
2024-12-20 12:51:35	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 connected, signal strength -58	
2024-12-20 12:51:38	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 disconnected, connection lost, signal strength -59	
2024-12-20 12:51:41	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 connected, signal strength -57	
2024-12-20 12:51:42	memory	wireless, info	B0:3C:xx:xx:xx:xx@wifi1 disconnected, SA Query timeout, signal strength -58	
2024-12-20 12:51:44	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 disconnected, connection lost, signal strength -60	
2024-12-20 12:51:46	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 connected, signal strength -57	
2024-12-20 12:51:47	memory	wireless, info	B0:3C:xx:xx:xx:xx@wifi1 connected, signal strength -66	
2024-12-20 12:51:53	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi1 disconnected, connection lost, signal strength -57	
2024-12-20 12:51:53	memory	wireless, info	78:2B:xx:xx:xx:xx@wifi2 connected, signal strength -37This saddened me because I bought the router and I was happy for a while because of how stable wireless was and then all of a sudden it started doing this. I will downgrade to 7.14.3 and see if it helps! Thanks!

---
```

## Response 145
Had same issues, changed DTIM values to 3 for 5GHz (it was 10 by default), the same was proposed upper in the thread, 2 days - no disconnects so far. ---

## Response 146
Had same issues, changed DTIM values to 3 for 5GHz (it was 10 by default), the same was proposed upper in the thread, 2 days - no disconnects so far.Arandom threadfrom quite some time ago ... which concluded that DTIM interval longer than around 3 can (and will) cause problems with certain station devices and in certain usage scenarios.BTW, currentWiFi manualsays that default setting ofdtim-periodproperty is 1. So the value you saw might be older default which was kept on your device dince wifi-qcom(-ac) was first installed. ---

## Response 147
So the value you saw might be older default which was kept on your device dince wifi-qcom(-ac) was first installed.That's actually stange as device was purchased by me less than month ago + my first action was to update it. But it could highlight some issues in dev/build/release process. ---

## Response 148
Or a very recent change of default setting. ---

## Response 149
I have never changed the dtim-period setting, and currently its value is 0 on both wireless interfaces. With this value, I have clients constantly disconnecting on router OS versions greater than 7.14.3. ---

## Response 150
I have never changed the dtim-period setting, and currently its value is 0 on both wireless interfaces. With this value, I have clients constantly disconnecting on router OS versions greater than 7.14.3.That's strange as the range is from 1 to 255 (according to the documentation):dtim-period (integer 1..255; default: 1) ---

## Response 151
Mikrotik app for Android shows the following value of dtim-period setting:Screenshot_2024-12-24-10-46-42-492_com.mikrotik.android.tikapp.jpgScreenshot_2024-12-24-10-46-42-492_com.mikrotik.android.tikapp.jpg ---

## Response 152
The question is what the actual value is. I only trust the config (through cli export). Can you check what the value is through export?By the way, I usedtim-period=3 ---

## Response 153
Mikrotik app for Android shows the following value of dtim-period setting:It might be artifact (by Tik app) for not having property set at all ... in which case default value (1) would be used.When in doubt, always use CLI to verify ... and report a bug in UI to MT to get it fixed. ---

## Response 154
I have a hAP ax³ (now it only works as an AP) and although I set thedtim-periodvalue to 1, some clients (in particular two Android smartphones) keep disconnecting.Having reverted (for the umpteenth time) to 7.14.3, everything works perfectly.Honestly, for WiFi I'm starting to evaluate something else. ---

## Response 155
Honestly, for WiFi I'm starting to evaluate something else.dtim-period=1 is the default, you could try a bit higher, like 3.Why evaluate something else, if 7.14.3 is working for you. Why upgrade at all? ---

## Response 156
Security reasons? ---

## Response 157
Security reasons?I can think of a thousand and more reasons...want to know from @Marvitex. ---

## Response 158
7.14.x is not known to have any security related issues. See for more info here:https://mikrotik.com/supportsecOn the other hand, there are vulnerabilities not mentioned in the "security blog" at all. Instead Mikrotik silently fixed them. e.g.https://www.enricobassetti.it/2023/11/c ... -rest-api/ ---

## Response 159
Hi, With lot of AX devices, i've found (capsman mode) a way to have a fully working without any random disconnect.The way is simple, create a master hidden ssid with channel config and a long passkey and have all others ssid as slaves.
```
## CHANNEL CFG
/interface wifi channel
add disabled=no name=master_channel width=20/40mhz-Ce
add disabled=no name=slave_channel width=20/40/80mhz

## MASTER SSID
/interface wifi configuration
add channel=master_channel country=France disabled=no hide-ssid=yes mode=ap \
    multicast-enhance=enabled name=master_config \
    security.authentication-types=wpa3-psk .passphrase=RRRRRRRRRRR \
    .wps=disable ssid=master

## SLAVE SSID
/interface wifi configuration
add channel=slave_channel country=France datapath=vlan1049_datapath disabled=\
    no hide-ssid=no mode=ap multicast-enhance=enabled name=vlan1049_config \
    security=vlan1049_auth ssid=ZZZZZZI have wireless cams and no disconnect and roaming is fine. At this time, still stable since 18 days. Before this main change, they lost signal many times.

---
```

## Response 160
Honestly, for WiFi I'm starting to evaluate something else.dtim-period=1 is the default, you could try a bit higher, like 3.Why evaluate something else, if 7.14.3 is working for you. Why upgrade at all?First of all, it is psychologically degrading to think of having an up-to-date hEX S without any kind of problem and a hAP ax³ that, instead, has to stay with a version from almost the beginning of the year. For what reason then? We still don't understand where the problem lies, evidently.Security reasons?One of the most important reasons, regardless of whether there are security bugs or not.Security reasons?I can think of a thousand and more reasons...want to know from @Marvitex.Exactly, the reasons are many and there is no need to list them.But anyway, for example, I've been waiting for the PPSK for a while (since everything around WiFi features is slow, on MikroTik) and now that it arrives I can't try it out. ---

## Response 161
Thanks @Marvitex, new functionality makes perfect sense.Afaik MikroTik upgraded the Qualcom(?) driver, which seems to have influence for some users (for me only more logging is profided but no problems with stability). ---

## Response 162
Having the same issue on ax3, the latest version with stable wireless is 7.15beta8 ---

## Response 163
I see kind of oxymoron:stable+ 7.15beta8 despite the fact that production 7.15 is the older version. ---

## Response 164
I see kind of oxymoron:stable+ 7.15beta8 despite the fact that production 7.15 is the older version.As mentioned, stable wireless, not build. The latest from the point of view security updates - 7.15b8 is later than 7.14.3 ---

## Response 165
So, before Christmas i upgraded Intel WiFi driver to 23.100.0 for my AX201... no disconnection problem since, ok i had only few days of test because of the holidays , but before it happened daily at least once. you guys might like to give it a try.intel.png ---

## Response 166
So, before Christmas i upgraded Intel WiFi driver to 23.100.0 for my AX201... no disconnection problem since, ok i had only few days of test because of the holidays , but before it happened daily at least once. you guys might like to give it a try.intel.pngThe problem doesn't occur only with Intel network cards. ---

## Response 167
The problem doesn't occur only with Intel network cards.I think he didn't mention that, he just informed us about an updated Intel driver that seems to give him better stability. ---

## Response 168
The problem doesn't occur only with Intel network cards.I think he didn't mention that, he just informed us about an updated Intel driver that seems to give him better stability.Sure, useful for those with an Intel network card, although personally I wouldn't be comfortable with it anyway. ---

## Response 169
ROS - 7.16.2 and 7.17.RC7Intel drivers 23.100.04Wireless reconnections continue, problem not resolved ---

## Response 170
ROS - 7.16.2 and 7.17.RC7Intel drivers 23.100.04Wireless reconnections continue, problem not resolved7.17 Stable - Ax3Intel AX200 160MhzIntel 23.160.1.2 Driver -Problem persists.WPA2 and WPA3 enabled. Connected to master interface. WPA3 Connection.Win 11 Event Viewer shows "7021 - Connection telemetry fields and analysis usage" around the time of the disconnect.Will try disabling WPA3 and report back... ---

## Response 171
Problem still present in 7.17rc8, only using WPA2.Disconnects on my Google chromecast tv, google mini speakers, Lenovo laptop. Laptop is using intel wifi chip, not sure about other devices.Had to downgrade back to 7.14.3 ---

## Response 172
Still getting disconnected on latest 7.17 version, I am starting to doubt this issue is even looked at, it’s been over 6 months now, some of you trying upgrading intel drivers when issue is clearly on mikrotik’s side, come on, you shouldn’t even do anything at all for it to work normally as it gets disconnected on default settings with minimalistic setup… ---

## Response 173
I have same WiFi disconnects issues, even 7.17 and 7.17RC8 not helps at all, and I can’t roll back to 7.14.3 because Factory firmware for my board is 7.15.2.Why Mikrotik engineers can’t solve this mass problem for so long?UDP: I finally downgraded it, but don’t want staying on 7.14.3 forever, because safety issues( ---

## Response 174
@elussivealex @eNET1 @vovikDid you generate and send the supout file to MikroTik support before downgrade?It seems that it is not easy to understand the cause and it does not happen to everyone.For example, I have no disconnections with hAP ax3 (CAPsMAN) + hAP ax2 (cAP) and about 50 clients using WPA2 / WPA3.Maybe you're doing something wrong in your configuration? ---

## Response 175
ROS - 7.16.2 and 7.17.RC7Intel drivers 23.100.04Wireless reconnections continue, problem not resolvedSupport don't read the forum threads, (not that I can see or they are being selective)Everyone seems to be complaining, and come on this thread to post about the issues, but is anyone actually sending the required supout.rif to support? ---

## Response 176
Everyone seems to be complaining, and come on this thread to post about the issues, but is anyone actually sending the required supout.rif to support?I keep sending files to the ticket SUP-157262, which I opened.https://help.mikrotik.com/servicedesk/s ... SUP-157262No result yet.It seems that support has reached a dead end and has no solution.Because the proposed solutions are to update the drivers for Intel adapters. But my TV Boxes and Android phones are also disconnecting.But if someone else opens similar tickets, it will give the developers more information to analyze the problem and solve it faster.https://help.mikrotik.com/servicedesk/s ... 1/create/5 ---

## Response 177
but is anyone actually sending the required supout.rif to support?I sents.Got various options for settings to fix the problem but it didn't help.I continue to use 7.14.3 ---

## Response 178
It seems that it is not easy to understand the cause and it does not happen to everyone.For example, I have no disconnections with hAP ax3 (CAPsMAN) + hAP ax2 (cAP) and about 50 clients using WPA2 / WPA3.Maybe you're doing something wrong in your configuration?It is possible, I too have the random disconnects and SA query timeouts and I have tried a lot of different wifi settings. Would you care to share your wifi config so people can compare it with a tested working setup? ---

## Response 179
Sure this is my configuration, very simple because at the moment I don't use VLAN at home.
```
# 2025-01-21 08:17:32 by RouterOS 7.17
# software id = BH9H-NUQS
#
# model = C53UiG+5HPaxD2HPaxD
# serial number = HDG00000000

/interface wifi channel
add band=5ghz-ax disabled=no frequency=5500 name=100 skip-dfs-channels=\
    10min-cac
add band=2ghz-ax disabled=no frequency=2412,2437 name=1-6 width=20/40mhz
/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk connect-priority=0/1 \
    disable-pmkid=yes disabled=no ft=yes ft-over-ds=yes name=SecWiFi-1 wps=\
    disable
/interface wifi steering
add disabled=no name=steering1 neighbor-group=dynamic-MikroTik-b8e24291 rrm=\
    yes wnm=yes
/interface wifi configuration
add channel=1-6 country=Italy disabled=no mode=ap name="2.4 GHz" security=\
    SecWiFi-1 ssid=MikroTik steering=steering1
add channel=100 country=Italy disabled=no mode=ap name="5 GHz" security=\
    SecWiFi-1 ssid=MikroTik steering=steering1
/interface wifi
# operated by CAP 48:A9:8A:39:34:A4%bridge, traffic processing on CAP
add configuration="5 GHz" configuration.manager=local .mode=ap disabled=no \
    name=cap-wifi1 radio-mac=48:A9:8A:39:34:A8
# operated by CAP 48:A9:8A:39:34:A4%bridge, traffic processing on CAP
add configuration="2.4 GHz" configuration.manager=local .mode=ap disabled=no \
    name=cap-wifi2 radio-mac=48:A9:8A:39:34:A9
set [ find default-name=wifi1 ] configuration="5 GHz" configuration.manager=\
    local .mode=ap disabled=no
set [ find default-name=wifi2 ] configuration="2.4 GHz" \
    configuration.manager=local .mode=ap disabled=no

/interface wifi capsman
set enabled=yes interfaces=bridge package-path="" require-peer-certificate=no \
    upgrade-policy=none
/interface wifi provisioning
add action=create-dynamic-enabled disabled=no master-configuration="2.4 GHz" \
    supported-bands=2ghz-ax
add action=create-dynamic-enabled disabled=no master-configuration="5 GHz" \
    supported-bands=5ghz-ax

/ip dhcp-server
add address-pool=default-dhcp interface=bridge lease-time=12h name=defconfAs you can see I added "connect-priority=0/1" because do some old Chinese smartphones when using WPA3 remain hooked to a cAP and do not roam, by activating I solved it.Another change is the DHCP server lease which is 12 hours.In another location I have a 5009 (CAPsMAN) with 4 wAPs AX (cAP), similar configuration but also with VLAN, here too no disconnections with about 60 wireless clients.

---
```

## Response 180
I've been having these issues as well using my HAP ax2 running ROS > 7.14.3. Been through the hoops with MT support using minimum configuration and trying to identify what devices cause WIFI disconnects. What we have found is that my Google Nest Speakers (Audio and Mini) cause regular and temporary WIFI drop-out for most, if not all all connected WIFI devices. Removing the Google Nest Speakers (Audio and Mini) increases WIFI stability significantly.Trying to re-configure ROS based on Mikrotik Support and forum recommended settings has been a rabbit hole for me with zero improvement to stability.Instead of trying to change the ROS configuration. Try to identify what devices are causing the issue by temporality removing them. Like Android TV, Google Nests and other similar devices. It's tedious, but could be bring valuable information to MK support.Since my issue cannot be reproduced on ROS <= 7.14.3, my conclusion is that this is a Mikrotik issue. ---

## Response 181
@mndtrpOut of curiosity, how long is the lease time of the DHCP server? 10 minutes? ---

## Response 182
@mndtrpOut of curiosity, how long is the lease time of the DHCP server? 10 minutes?I’ve tried 10 minutes, 1 hour and 24 hours. Lease time has no effect. ---

## Response 183
Instead of trying to change the ROS configuration. Try to identify what devices are causing the issue by temporality removing them. Like Android TV, Google Nests and other similar devices. It's tedious, but could be bring valuable information to MK support.Since my issue cannot be reproduced on ROS <= 7.14.3, my conclusion is that this is a Mikrotik issue.As I have already mentioned in another thread here:viewtopic.php?p=1117893&sid=06afa00c0c7 ... c99f05563cI am pretty certain my issues started after I introduced WiiM Streamer into my network. Before that, my phone was the only device permanently connected on 5Ghz with occasional temporary connections of laptops. No issues observed. After connecting WiiM on 5GHz, the phone, perfectly working up till then for almost a year, started giving me SA query timeouts at least once a day randomly.And yes, most likely it is Mikrotik issue, since in 7.15 the Qualcomm Wifi driver was updated, so it is pretty clear what is behind all this mess. Just rollback of the driver should fix it, but Mikrotik does not wanna hear about it apparently. So we are stuck with broken Wifi. ---

## Response 184
Sure this is my configuration, very simple because at the moment I don't use VLAN at home.In another location I have a 5009 (CAPsMAN) with 4 wAPs AX (cAP), similar configuration but also with VLAN, here too no disconnections with about 60 wireless clients.Thanks, I suppose you are using same SSID for 2 and 5GHz and use roaming between the 2, correct? Since I see you have FT enabled.I have 2 and 5Ghz separated on different SSIDs, and connect devices directly where I want them to, and I have FT disabled, but otherwise basically the same setup (I even tried the connect priority setting with no impact), and with only 2 devices (my phone and WiiM Ultra), my phone gets SA query timeouts. Crazy to think you have no issues whatsoever with dozens of devices at the same time. ---

## Response 185
Thanks, I suppose you are using same SSID for 2 and 5GHz and use roaming between the 2, correct? Since I see you have FT enabled.Yes, it's correct.Crazy to think you have no issues whatsoever with dozens of devices at the same time.Yes indeed it's curious... consider that I also have 3 Sonos One, 2 Chromecast and a Google Nest Audio and they never disconnect. ---

## Response 186
Today I tried to update to 7.17 and set up local WiFi interfaces via local CapsMan.I understand that this is a hack and an excessive solution, but it works for Massinia.The solution worked for 3 hours and my TV box started reconnecting to WiFi again ---

## Response 187
For the record, never had the problem here (around 10-11 devices, 2.4 anf 5ghz)... ---

## Response 188
Since, i've fixed channel width AND create a "fake master hidden ssid"I've no disconnect except roaming on a building with 4 floors and 12 hap ax3 running 7.17.This my capsman cfg :
```
/interface wifi channel
add disabled=no name=master_channel width=20/40mhz-Ce
add disabled=no name=slave_channel width=20/40/80mhz
/interface wifi configuration
add channel=master_channel country=France disabled=no hide-ssid=yes mode=ap multicast-enhance=enabled name=master_config \
    security.authentication-types=wpa3-psk ssid=master
/interface wifi datapath
add bridge=bridge1 bridge-cost=10 client-isolation=no disabled=no interface-list=guest name=vlan1049_datapath vlan-id=1049
add bridge=bridge1 bridge-cost=10 client-isolation=no disabled=no interface-list=lan name=vlan1050_datapath vlan-id=1050
add bridge=bridge1 bridge-cost=10 client-isolation=no disabled=no interface-list=guest name=vlan1069_datapath vlan-id=1069
add bridge=bridge1 bridge-cost=10 client-isolation=no disabled=no interface-list=lan name=vlan1070_datapath vlan-id=1070
/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk disabled=no ft=yes ft-mobility-domain=0x1049 ft-over-ds=yes name=vlan1049_auth wps=disable
add authentication-types=wpa2-psk,wpa3-psk disabled=no ft=yes ft-mobility-domain=0x1050 ft-over-ds=yes name=vlan1050_auth wps=disable
add authentication-types=wpa2-psk,wpa3-psk disabled=no ft=yes ft-mobility-domain=0x1069 ft-over-ds=yes name=vlan1069_auth wps=disable
add authentication-types=wpa2-psk,wpa3-psk disabled=no ft=yes ft-mobility-domain=0x1070 ft-over-ds=yes name=vlan1070_auth wps=disable
/interface wifi configuration
add channel=slave_channel country=France datapath=vlan1049_datapath disabled=no hide-ssid=no mode=ap multicast-enhance=enabled name=\
    vlan1049_config security=vlan1049_auth ssid=1049
add channel=slave_channel country=France datapath=vlan1050_datapath disabled=no hide-ssid=no mode=ap multicast-enhance=enabled name=\
    vlan1050_config security=vlan1050_auth ssid=1050
add channel=slave_channel country=France datapath=vlan1069_datapath disabled=no hide-ssid=no mode=ap multicast-enhance=enabled name=\
    vlan1069_config security=vlan1069_auth ssid=1069
add channel=slave_channel country=France datapath=vlan1070_datapath disabled=no hide-ssid=no mode=ap multicast-enhance=enabled name=\
    vlan1070_config security=vlan1070_auth ssid=1070
/interface wifi capsman
set ca-certificate=auto certificate=auto enabled=yes interfaces=vlan1067 package-path="" require-peer-certificate=no upgrade-policy=none
/interface wifi provisioning
add action=create-dynamic-enabled comment=wifi-5g disabled=no master-configuration=master_config name-format=wifi-5g-%I slave-configurations=\
    vlan1049_config,vlan1050_config,vlan1069_config,vlan1070_config slave-name-format=%m%v supported-bands=5ghz-a,5ghz-n,5ghz-ac,5ghz-ax
add action=create-dynamic-enabled comment=wifi-2g disabled=no master-configuration=master_config name-format=wifi-2g-%I slave-configurations=\
    vlan1049_config,vlan1050_config,vlan1069_config,vlan1070_config slave-name-format=%m%v supported-bands=2ghz-ax,2ghz-g,2ghz-n

---
```

## Response 189
Tested 7.18beta2 today and the issue is still not completely fixed. Though it has been reduced a lot since the 7.16-7.17 builds I find. It's actually almost entirely usable now where as before I HAD to be on 7.14.3 to actually have a usable connection on the 5GHz interface. The two devices I have that trigger the problem do still cause the 5GHz interface to drop, but it's only when they first connect and its for a much shorter period of time. ---

## Response 190
I understand that this is a hack and an excessive solution, but it works for Massinia.The solution worked for 3 hours and my TV box started reconnecting to WiFi againWhich hack? It is the correct way.On device with CAPsMAN active the cAPs interfaces are local managed, otherwise fast roaming can never work.CAPsMAN.pngIn the CAPs instead they are managed by CAPsMANcAP.png ---

## Response 191
Which hack? It is the correct way.This is the right way if you have additional access points and need centralized network management.But in my case there is only one hAP AX3 router and running CapsMan is a redundant solution. But this, unfortunately, does not work either. ---

## Response 192
Tested 7.18beta2 today and the issue is still not completely fixed. Though it has been reduced a lot since the 7.16-7.17 builds I find. It's actually almost entirely usable now where as before I HAD to be on 7.14.3 to actually have a usable connection on the 5GHz interface. The two devices I have that trigger the problem do still cause the 5GHz interface to drop, but it's only when they first connect and its for a much shorter period of time.I agree with this. I also have fewer interruptions on this version, and on Windows computers, instead of interruptions, there are sometimes delays in data transfer. But unfortunately, watching YouTube or Netflix is ​​interrupted on TVBox and tablets. ---

## Response 193
Still no improvements for me on 7.18, soundbar, tv, tablets, getting disconnected for no reason even next to router on desk under full signal... ---

## Response 194
People, please, let's help the developers solve our common problem with WiFi.Please open tickets on the support portalhttps://help.mikrotik.com/servicedesk/s ... r/portal/1describe the problem and attach the Supout.rif file.This will help the developers collect more information and solve the problem faster.Because more than half a year has passed, and the problem is not solved. ---

## Response 195
People, please, let's help the developers solve our common problem with WiFi.Please open tickets on the support portalDone that, SUP-177122 opened on 22/01, still in "waiting for support". ---

## Response 196
Here is what I see when trying to connect my old Wyze Cam v1. Camera continuously sends 'Probe Request' but router is silent.I simplified configuration 2.4GHz to next:
```
1 M B  default-name="wifi2" name="wifi2" l2mtu=1560 mac-address=xxxx arp-timeout=auto radio-mac=xxxx
        configuration.mode=ap .ssid="ssid1" .dtim-period=3 
        security.authentication-types=wpa2-psk .encryption=ccmp .passphrase="xxx"  
        channel.frequency=2437 .secondary-frequency=disabled .band=2ghz-g .width=20mhz 

 3   BI name="wifi4" l2mtu=1560 mac-address=xxxx arp-timeout=auto master-interface=wifi2 
        configuration.mode=ap .ssid="ssid2" .dtim-period=3 
        security.authentication-types=wpa2-psk .encryption=ccmp .passphrase="xxx"  
        channel.frequency=2437 .band=2ghz-gBut still silence form router. In logs it looks like that (2nd image), but I cannot see those connections and associations in Wireshark. May be some packets are filtered and I need to buy USB WiFi module that can be put into monitor mode to properly log WiFi communication.. I don't know.

---
```

## Response 197
ROS 7.18.beta4 no changesAndroid devices start disconnects after 15 minutes ((( ---