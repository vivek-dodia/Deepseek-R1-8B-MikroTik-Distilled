# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211009

# Discussion

## Initial Question
Author: [SOLVED]Wed Sep 18, 2024 4:31 pm
My spouse recently updated her iPhone SE to iOS 18. Since then, she can't connect to the Wi-Fi network. Whenever I try to connect, it prompts for the Wi-Fi password, I enter it correctly, but then it immediately says unable to connect. Nothing at the router or Wi-Fi AP level has changed. When I look at the logs, I can see it tries to connect then disconnects and just repeats the same error. There is no access list in use at the AP, nothing restricting the devices from connecting. Every other Wi-Fi device in the house is connected and working, including my own iPhone which is still on iOS 17.Has anyone else encountered Wi-Fi issues since upgrading to iOS 18? I've already tried resetting the network settings on her device to no avail.Can someone point me to instructions for enabling wireless debug logging? ---

## Response 1
Author: Wed Sep 18, 2024 4:49 pm
Can someone point me to instructions for enabling wireless debug logging?/system logging rulesAdd Topics :debug & wireless, Actions: memory.That's it.Can you share the wireless part of the config? Just to check current settings. ---

## Response 2
Author: Wed Sep 18, 2024 6:16 pm
what type of wireless encryption do you use? WPA2+WPA3? ---

## Response 3
Author: Thu Sep 19, 2024 12:39 am
``` 
```
/interface wifi
set [ find default-name=wifi1 ] channel.frequency=2401-5835 \
    .skip-dfs-channels=all configuration.country="United States" .mode=ap \
    .ssid=MikroTik disabled=no security.authentication-types=\
    wpa2-psk,wpa3-psk .connect-priority=0/1 .encryption=\
    ccmp,gcmp,ccmp-256,gcmp-256 .ft=yes .ft-over-ds=yes .group-key-update=1d \
    .wps=disable
set [ find default-name=wifi2 ] channel.frequency=2401-5835 \
    .skip-dfs-channels=all configuration.country="United States" .mode=ap \
    .ssid=MikroTik disabled=no security.authentication-types=\
    wpa2-psk,wpa3-psk .connect-priority=0/1 .encryption=\
    ccmp,gcmp,ccmp-256,gcmp-256 .ft=yes .ft-over-ds=yes .group-key-update=1d \
    .wps=disable
set [ find default-name=wifi3 ] channel.frequency=2401-5835 \
    .skip-dfs-channels=all configuration.country="United States" .hide-ssid=\
    yes .mode=ap .ssid=MikroTik-Mesh disabled=no \
    security.authentication-types=wpa3-psk .connect-priority=0/1 .encryption=\
    ccmp,gcmp,ccmp-256,gcmp-256 .ft=yes .ft-over-ds=yes .group-key-update=1d \
    .wps=disable
```

Can someone point me to instructions for enabling wireless debug logging?/system logging rulesAdd Topics :debug & wireless, Actions: memory.That's it.Can you share the wireless part of the config? Just to check current settings.I've tried changing the authentication from wpa2-psk to both wpa2-psk and wpa3-psk to no avail. This Audience uses wifi3 to communicate in mesh back to another Audience on wifi3.


---
```

## Response 4
Author: Thu Sep 19, 2024 1:26 am
@k2dI5umrD9VO: It’s not related to ROS. This is a known issue with iOS 18 (and also in the previews) but no one has figured out the root cause or how to fix it:https://www.google.com/search?q=%22iOS+ ... reddit.com ---

## Response 5
Author: Thu Sep 19, 2024 1:52 am
@k2dI5umrD9VO: It’s not related to ROS. This is a known issue with iOS 18 (and also in the previews) but no one has figured out the root cause or how to fix it:https://www.google.com/search?q=%22iOS+ ... reddit.comNormally I'd agree, but the spouse took the phone to other locations with public Wi-Fi and it allegedly worked fine. Bring it back home to the MikroTik network and no luck. ---

## Response 6
Author: Thu Sep 19, 2024 1:59 am
I had the same issue and I fixed it by following a suggestion I found on Reddit: just disable the private address, forget the network, reconnect, and then re-enable the private address again. Anyway, no one seems to know exactly why this happens with iOS 8. ---

## Response 7
Author: Thu Sep 19, 2024 2:43 am
Trying now with debug logging on for the wireless. Phone claims the password is incorrect, logs show attached screen captures when attempting to connect.Makes absolute zero sense. No clear explanation in the logs.Screenshot 2024-09-18 194217.jpgScreenshot 2024-09-18 194243.jpgI've noticed that if I keep tapping "Join" on the phone, eventually the screen locks up at the password prompt. When it locks up, I can see it connected to the AP. Of course, the phone is useless if it just locks up since you have to force close the Settings app and then it doesn't connect.Screenshot 2024-09-18 194554.jpgScreenshot 2024-09-18 194604.jpg ---

## Response 8
Author: Thu Sep 19, 2024 2:59 am
Did you try forgetting the network and then reconnecting, or is that when you ran into another issue? ---

## Response 9
Author: Thu Sep 19, 2024 3:02 am
Did you try forget network and then reconnect?Yes, same result. ---

## Response 10
Author: Thu Sep 19, 2024 3:14 am
Alright, I’m not sure then. You could check the iOS Wi-Fi logs to find the cause, or if all else fails, roll back to iOS 17.Look for the section “Wi-Fi for iOS/iPadOS” iniOS Profiles and Logs ---

## Response 11
Author: Thu Sep 19, 2024 7:37 am
or if all else fails, roll back to iOS 17.Or... try wifi configuration using defaults (only country is required) - just to see if work with iOS 18. Specifically trying ft=no, since that seems an area that could be broken. Or, perhaps try the 7.16rc "testing" with your current configuration to see if some random fix in RouterOS fixes this - there are always some wifi tweaks in each release. Both might be good step before giving up to downgrade.I have an iPhone 12 with iOS 18 that connects to wAPacR with wifi-qcom-ac (and defaults with DFS disabled) - so I don't think it's a generic problem. Still could be a bug here, just figuring if it's iOS (since it just came out) or Mikrotik isn't so easy for random wi-fi issues. ---

## Response 12
Author: Thu Sep 19, 2024 7:52 am
Yeah, forgot to mention we're using 7.15.3 with FT enabled. I remember some Apple devices (at least in the past) could have issues with mixed languages on APs within the same SSID domain. Anyway, troubleshooting Wi-Fi on Apple devices can be pretty tricky so instead of wasting time with trial and error it's usually faster to check the device logs to find the real problem.OT: it really bugs me that Apple require an A17 chip to enable ChatGPT integration in iOS 18. It’s so very typical of Apple always finding new ways to push people to upgrade their hardware. ---

## Response 13
Author: Thu Sep 19, 2024 9:25 am
I have had lots of problems when setting encryption to everything except TKIP (Android and Windows). Can you give it a try (assuming you use Winbox) by unselecting everything, and collaps the encryption part? ---

## Response 14
Author: Thu Sep 19, 2024 10:43 am
Like I said earlier, it's an intermittent issue withApple iOS 18. And honestly, why waste time with pointless trial and error when you can just check the device Wi-Fi logs to find the real problem faster? ---

## Response 15
Author: Thu Sep 19, 2024 10:49 am
I remember some Apple devices (at least in the past) could have issues with mixed languages on APs within the same SSID domain.What do you mean with mixed languages? ---

## Response 16
Author: Thu Sep 19, 2024 10:57 am
OT: it really bugs me that Apple require an A17 chip to enable ChatGPT integration in iOS 18. It’s so very typical of Apple always finding new ways to push people to upgrade their hardware.The same company which added a deliberate slowing down of older HW and it still surprises you ?What do you think MS is doing with their Co-Pilot story ? Same purpose. Push HW sales ... (MS license will come with it).They all use these tricks ...Carry on ![/OT] ---

## Response 17
Author: Thu Sep 19, 2024 11:25 am
Hi, I have the same problem and I think it's worth finding a solution.It doesn't work with my Mikrotik environment, other router hardware has worked.I already had an iPhone15 running the iOS 18.1 beta, I still have NO problems with this phone.But all other devices that were updated to iOS 18 yesterday cannot connect.I also have the problem with a MacBook on MacOS 15 and the behavior is the same.I have already completely reinstalled the MacBook, but unfortunately this does not solve the problem. ---

## Response 18
Author: Thu Sep 19, 2024 11:52 am
What do you mean by mixed languages?@erlinden: Sorry, I meant to say regional settings.The same company that added deliberate slowdowns to older hardware and it still surprises you? What do you think MS is doing with their Co-Pilot story? Same purpose—push hardware sales (MS license will come with it). They all use these tricks...@holvoetn: Yeah, no surprise there! But it still bugs the hell out of me every time it pops up..Hi, I have the same problem and I think it's worth finding a solution.@dude2k: check out the WiFi logs and help others by analyze the root cause. Btw, what build are you using? Fwiw, I’m still running macOS 15 RC on an M2 MBA with no issues (so far anyway!) using AX with FT. ---

## Response 19
Author: Thu Sep 19, 2024 12:10 pm
Only as a side note, in the few "official" videos from Mikrotik I have watched (I simply cannot bear videos, but that's just me) I have noticed that the good Mikrotik guys often use Macs, so I believed that they are "Apple users" (last time I had a Mac and an iPad I was practically forced to also get an iPhone because of the interconnectedness of all things Apple, soon after I thankfully managed to quit the addiction ), thus I expected that Apple devices were common enough among Mikrotik developers and were tested much more than other "random" Android devices. ---

## Response 20
Author: Thu Sep 19, 2024 12:18 pm
Only as a side note, ...(I simply cannot bear videos, but that's just me) ...You're not alone.I prefer a good old searchable manual anytime over whatever video which usually is a waste of time for the most part (to me). ---

## Response 21
Author: Thu Sep 19, 2024 12:22 pm
``` 
```
add country=Germany datapath=datapath2-vlan30-gast disabled=no mode=ap name=cfg3-gast security=sec3-gast security.authentication-types=wpa2-psk,wpa3-psk .connect-priority=0/1 .encryption=ccmp,gcmp,ccmp-256,gcmp-256 ssid=gast
    
add authentication-types=wpa2-psk,wpa3-psk connect-priority=0/1 disabled=no encryption=ccmp,gcmp,ccmp-256,gcmp-256 ft=yes ft-over-ds=yes ft-preserve-vlanid=no name=sec3-gast wps=disable
```

[@dude2k: check out the WiFi logs and help others by analyze the root cause. Btw, what build are you using? Fwiw, I’m still running macOS 15 RC on an M2 MBA with no issues (so far anyway!) using AX with FT.Hi, I'm using 7.15.3 on all Mikrotik APs and Routers. Before iOS18 I had no  problem, also roaming was working fine.My Wifi Debug Logs are looking exactly like the logs k2dI5umrD9VO already posted.I Have AC and AX APs and use FT and "FT over DS". WPA2-PSK and WPA3-PSK (But also tested only WPA2-PSK, but didn't work)Examples:


---
```

## Response 22
Author: Thu Sep 19, 2024 12:34 pm
As already written: ROS logs are not helpful. You all need to capture your client logs.Look for the section “Wi-Fi for iOS/iPadOS” iniOS Profiles and Logs ---

## Response 23
Author: Thu Sep 19, 2024 12:47 pm
I Have AC and AX APs and use FT and "FT over DS". WPA2-PSK and WPA3-PSK (But also tested only WPA2-PSK, but didn't work)Does it connect when you disable FT and reboot ? ---

## Response 24
Author: Thu Sep 19, 2024 1:01 pm
Does it connect when you disable FT and reboot ?Tried a few minutes ago, no changes, does not work ---

## Response 25
Author: Thu Sep 19, 2024 1:15 pm
Same iPhone, upgraded to iOS 18; nothing changed with WiFi on ax^3. ---

## Response 26
Author: Thu Sep 19, 2024 1:16 pm
``` 
```
/interface wifi export
```

Same iPhone, upgraded to iOS 18; nothing changed with WiFi on ax^3.Then it might be helpfull to share your (wireless) configRemove serial and any other private info.


---
```

## Response 27
Author: Thu Sep 19, 2024 1:27 pm
Hey folks! Want to know what's really going on when your Apple device is having Wi-Fi issues??IfYES, then check the wifi logs on yourDEVICE:1.iOS Profiles and LogsWi-Fi for iOS/iPadOS InstructionsProfile2.macOS Profiles and LogsDirect link:Wi-Fi Logs For macOS Wi-Fi issues, please follow the instructions to gather a Wi-Fi Diagnostics Report.IfNO, feel free to keep using 'trial and error' but (I'll say this nicely) please don't waste others' time with random guesses, especially if you're not using an Apple device. Thanks! ---

## Response 28
Author: Thu Sep 19, 2024 1:44 pm
As already written: ROS logs are not helpful. You all need to capture your client logs.Link to Driver Log TXT-File from Macbook:https://1drv.ms/t/s!AsOJquxuP-h5hewWtvJ ... Q?e=yTxxJA ---

## Response 29
Author: Thu Sep 19, 2024 1:57 pm
``` 
```
/interface wifi export
```

```
```

```
2024-09-19 12:54:01 by RouterOS 7.15.3
# software id = EBTN-KIA3
#
# model = C53UiG+5HPaxD2HPaxD
# serial number = xxx
/interface wifi channel
add disabled=no frequency=2412,2432,2472 name=ch-2ghz \
    reselect-interval=1d skip-dfs-channels=disabled width=20mhz
add disabled=no frequency=5490-5730 name=ch-5ghz skip-dfs-channels=\
    disabled width=20/40/80mhz
/interface wifi security
add authentication-types=wpa2-psk connect-priority=0/1 disabled=no \
    encryption=ccmp ft=yes ft-over-ds=yes management-protection=\
    allowed name=wifi-security wps=disable
add authentication-types=wpa2-psk connect-priority=0/1 disabled=no \
    encryption=ccmp ft=yes ft-over-ds=yes management-protection=\
    allowed name=wifi-security-iot wps=disable
/interface wifi configuration
add channel=ch-2ghz country=Poland disabled=no dtim-period=3 name=\
    wifi-config security=wifi-security ssid=xxx
add channel=ch-2ghz country=Poland disabled=no dtim-period=3 \
    hide-ssid=yes name=wifi-iot security=wifi-security-iot \
    security.ft=yes .ft-over-ds=yes ssid=xxx
/interface wifi
set [ find default-name=wifi2 ] channel=ch-2ghz channel.frequency=\
    2412,2432,2472 configuration=wifi-config configuration.mode=ap \
    disabled=no name=wifi-2ghz security=wifi-security
add channel.frequency=2412,2432,2472 configuration=wifi-iot \
    configuration.mode=ap disabled=no mac-address=xx:xx:xx:xx:xx:xx \
    master-interface=wifi-2ghz mtu=1500 name=wifi-2ghz-iot security=\
    wifi-security-iot
set [ find default-name=wifi1 ] channel=ch-5ghz channel.frequency=\
    5490-5730 configuration=wifi-config configuration.mode=ap \
    disabled=no name=wifi-5ghz security=wifi-security
```

Same iPhone, upgraded to iOS 18; nothing changed with WiFi on ax^3.Then it might be helpfull to share your (wireless) configRemove serial and any other private info.


---
```

## Response 30
Author: Thu Sep 19, 2024 2:04 pm
As already written: ROS logs are not helpful. You all need to capture your client logs.Link to Driver Log TXT-File from Macbook:https://1drv.ms/t/s!AsOJquxuP-h5hewWtvJ ... Q?e=yTxxJAIs d4:01:c3:d2:48:d9 your APs bssid? ---

## Response 31
Author: Thu Sep 19, 2024 2:08 pm
Yes, d4:01:c3:d2:48:d9 is a "cAPGi-5HaxD2HaxD" which has best distance to my Macbook during this testDon't get confused beacuse SSID might be "cisco" this is just because I've switched to Mikrotik. ---

## Response 32
Author: Thu Sep 19, 2024 3:34 pm
Link to Driver Log TXT-File from Macbook:https://1drv.ms/t/s!AsOJquxuP-h5hewWtvJ ... Q?e=yTxxJAJust a suggestion; when sharing a log this big, try giving a hint about when the issue happened so people know where to start looking. Also, this log is primarily meant for the Apple Developer forums or Apple Support but if you’re lucky someone here might have time to help you out. ---

## Response 33
Author: Thu Sep 19, 2024 4:40 pm
Link to Driver Log TXT-File from Macbook:https://1drv.ms/t/s!AsOJquxuP-h5hewWtvJ ... Q?e=yTxxJAJust a suggestion; when sharing a log this big, try giving a hint about when the issue happened so people know where to start looking. Also, this log is primarily meant for the Apple Developer forums or Apple Support but if you’re lucky someone here might have time to help you out.Appreciate the input, but I don't even have an Apple Developer account. At this point, it's a problem that requires the attention of engineers between MikroTik and Apple. We shouldn't be in the middle of it, especially when iOS 18 betas have been out *for months* and both of these companies had plenty of time to do testing. That's the part that frustrates me the most. Customers are stuck sitting on their hands because no one *wants* to tear out their Wi-Fi infrastructure and replace it with a competing product simply because iOS 18 is causing problems.I've already submitted a formal support ticket with MikroTik and referenced this forums thread. ---

## Response 34
Author: Thu Sep 19, 2024 5:25 pm
I am with you. It is up to Mikrotik to give feedback to Apple or Qualcomm or fix it themselves. None of our business. ---

## Response 35
Author: Thu Sep 19, 2024 5:34 pm
@k2dI5umrD9VO: As I tried to explain earlier, since the issue originates from your iOS device, you should contact Apple Support and let them handle the matter accordingly.I mean, if it worked with iOS 17 but not with iOS 18, you can’t blame MikroTik for it, can you? ---

## Response 36
Author: Thu Sep 19, 2024 5:59 pm
Have those of you having issues tried older versions of RouterOS?I have been running the iOS 18 betas on my phone since WWDC. I have also installed dozens of hAP AX3's since then, which I test from my phone or M1 MacBook Pro (which has been running the Sequoia betas).I netinstall 7.14.x (2 or 3, forget which) on the AX3's at each install, then test for throughput (and have the customer connect). I haven't seen any issues connecting from my phone or laptop via WiFi. Since 18 just came out, I don't have any reports from customers with these routers (yet).There could very well be an 18/7.15.3 combination that's wonky for some.On my default config files, all I set is country, SSID, password, and limit channels to 2400-5825 (AX2's like to use the new 5.8-5.9 space that most devices don't support).WPA2+3 are both enabled, but sometimes I have to go back and disable WPA3 if they complain about random disconnects. ---

## Response 37
Author: Thu Sep 19, 2024 6:26 pm
I'm also using Beta of iOS 18 since the beginning. Was working fine. Right now I've 18.1 beta 3 installed. Also without a Problem.Only iOS 18, iPad OS 18 and MacOS 15y is making problems.WatchOS 11 is also working fine. ---

## Response 38
Author: Thu Sep 19, 2024 6:32 pm
RB4011iGS+5HacQ2HnD-IN running ROS 7.15.3, upgrade iPhone's 12 Pro and Pro Max to iOS 18, no issues. ---

## Response 39
Author: Thu Sep 19, 2024 6:40 pm
Could you please post your wifi config for testing? ---

## Response 40
Author: Thu Sep 19, 2024 6:46 pm
I'm also using Beta of iOS 18 since the beginning. Was working fine. Right now I've 18.1 beta 3 installed. Also without a Problem.Only iOS 18, iPad OS 18 and MacOS 15y is making problems.WatchOS 11 is also working fine.Interesting- so the beta releases, Wi-Fi worked fine, but now that's it final, it doesn't? ---

## Response 41
Author: Thu Sep 19, 2024 6:51 pm
This is strange. I have no problems with iOS 18, I specifically checked on different iPhones. But, definitely, if the problem exists, it is not in RouterOS ---

## Response 42
Author: Thu Sep 19, 2024 7:16 pm
In order to give you the full picture:Mikrotik Hardware:3x MikroTik cAP ax (cAPGi-5HaxD2HaxD) ROS 7.15.31x MikroTik hAP ax³ (C53UiG+5HPaxD2HPaxD) ROS 7.15.31xMikroTik hAP ax² (C52iG-5HaxD2HaxD-TC) ROS 7.15.32x Mikrotik wAP AC (RBwAPG-5HacD2HnD) ROS 7.15.3Apple Hardware tested:- MacBook Air M1 - MacOS 15 - Not working (with MacOS 14 - working fine); testes fresh reinstall of MacOS15- Apple Watch Series 9 - WatchOS 11 - working fine- iPhone 15 Pro Max - iOS 18 beta starting from WWDC up to today 18.1 beta 3 - working fine (didn't try beta 4 because it's my daily device and I'm afraid now)- iPhone 11 - iOS 18 - Not working (with 17.X - working fine); tested reset of network information- iPad Pro M1 - iPadOS 18 - not working ( with 17.X - working fine)With all Apple Devices wich have problems I can connect to a WiFi Hotspot on an iPhone and I can connect to other routers like for example AVM FritzBox ---

## Response 43
Author: Thu Sep 19, 2024 7:16 pm
It's not a RouterOS problem.iPhone with iOS 18:- 2x TP-Link AP - OK- 1x AX TP-Link AP - not working after update, previously fine- 3x UBNT AX AP - fine- 1x UBNT AC AP - previously fine, not working after update- 2x Grandstream AC AP - previously fine, not working after updateI don't understand the UBNT AP situation at all, the configuration is identical, frequency and bandwidth the sameEdit: Todays test:On most APs, it helped to disable WPA3 and leave only WPA2-AES. After that, the iPhone started working.But with UBNT, I don't understand why it worked at some places and not others. I changed the settings to WPA2-only and the phone wouldn't connect. I changed it to WPA3 and the phone connected. I then changed it back to WPA2-only and the phone miraculously works.Hence, I don't give a damn about WPA3, so far it has caused me more problems than good. Good thing I only use it on my test networks and not in production. I'm planning to deploy 6 GHz and I can't do without it there ---

## Response 44
Author: Thu Sep 19, 2024 7:18 pm
Yeah, beginning to sound more like an Apple problem. Wonderful. ---

## Response 45
Author: Thu Sep 19, 2024 7:26 pm
@m4rk3Jgood input, thank you, very interesting. ---

## Response 46
Author: Thu Sep 19, 2024 7:45 pm
Despite advertising: Apple also has bugs. lol ---

## Response 47
Author: Thu Sep 19, 2024 8:02 pm
``` 
```
[admin@MikroTik] > /interface wireless export
# 2024-09-19 18:49:15 by RouterOS 7.15.3
# software id = KT6A-4P99
#
# model = RB4011iGS+5HacQ2HnD
# serial number = xxxxx

/interface wireless security-profiles
set [ find default=yes ] eap-methods="" supplicant-identity=MikroTik
add authentication-types=wpa2-psk disable-pmkid=yes eap-methods="" mode=dynamic-keys name=public-sp supplicant-identity=""
add authentication-types=wpa2-psk disable-pmkid=yes eap-methods="" mode=dynamic-keys name=2&5GHz-ap supplicant-identity=""
add authentication-types=wpa2-psk disable-pmkid=yes eap-methods="" mode=dynamic-keys name=iot-sp supplicant-identity=""

/interface wireless
set [ find default-name=wlan1 ] band=5ghz-onlyac channel-width=20/40/80mhz-XXXX comment=5GHz country=netherlands default-authentication=no default-forwarding=no disabled=no distance=indoors frequency=5500 installation=indoor mode=ap-bridge \
    security-profile=2&5GHz-ap ssid=xxxx station-roaming=enabled vlan-id=84 wireless-protocol=802.11 wps-mode=disabled
set [ find default-name=wlan2 ] ampdu-priorities=0,1,2,3,4,5 band=2ghz-g/n channel-width=20/40mhz-XX comment=2GHz country=netherlands default-authentication=no default-forwarding=no disabled=no distance=indoors frequency=auto installation=indoor \
    mode=ap-bridge security-profile=iot-sp ssid=xxxx station-roaming=enabled wireless-protocol=802.11 wps-mode=disabled
add default-authentication=no default-forwarding=no disabled=no mac-address=76:4D:xx:xx:xx:xx master-interface=wlan2 name=wlan2.1 security-profile=2&5GHz-ap ssid=xxxx wps-mode=disabled
add default-authentication=no default-forwarding=no disabled=no mac-address=76:4D:xx:xx:xx:xx master-interface=wlan2 name=wlan2.2 security-profile=public-sp ssid=xxxx station-roaming=enabled wps-mode=disabled
```

Could you please post your wifi config for testing?


---
```

## Response 48
Author: Thu Sep 19, 2024 8:06 pm
Thank you ---

## Response 49
Author: Thu Sep 19, 2024 8:20 pm
So that person above is using EAP while the rest of seem to be using standard WPA 2/3. It absolutely does sound like an iOS 18 Wi-Fi authentication protocol issue which would make sense since the generic iOS error keeps claiming the password is incorrect. Or am I reading that wifi config incorrectly? ---

## Response 50
Author: Thu Sep 19, 2024 8:25 pm
Yes, thought the same. complex1 seems to use EAP while I've tested WPA2-PSK and WPA3-PSK ---

## Response 51
Author: Thu Sep 19, 2024 8:38 pm
Looks like MikroTik is not alone with Apple-breaking OS updates:https://techcrunch.com/2024/09/19/apple ... perts-say/This quote stood out:The engineer also said CrowdStrike sent out a “Tech Alert” to customers, adding that “there’s quite a lot going on with the changes in the network stack.” ---

## Response 52
Author: Thu Sep 19, 2024 8:41 pm
I've ordered a couple of eero Pro 6E units today just to see if updated Apple devices work with those. Should find out by tomorrow. ---

## Response 53
Author: Thu Sep 19, 2024 8:42 pm
As fa as I know, I don't use EAP ---

## Response 54
Author: Thu Sep 19, 2024 8:49 pm
As fa as I know, I don't use EAPAre you using "wireless" or the "wifi-qcom" packages? That looks like the original wireless package. ---

## Response 55
Author: Thu Sep 19, 2024 9:57 pm
That shows the legacy "wireless" security profile window indeed. ---

## Response 56
Author: Thu Sep 19, 2024 9:59 pm
I'm using the "wireless" package. ---

## Response 57
Author: Fri Sep 20, 2024 1:59 pm
I've fixed the problem, maybe this will help you.Additional information:I'm using new CAPSMANWhat I've done:1. deleted security profile from my configuration tab2. removed all encryption (= open Wifi)3. iPhone was able to connect4. ignored network on iPhone5. added security information only in configuration profile. security profile still NOT used6. added same PSK as before7. Connected iPhoneiPhone and MacBook working fine now.Maybe you can do a test. ---

## Response 58
Author: Fri Sep 20, 2024 9:25 pm
I have a similar problem.- Updated to macOS 15.0 and iOS 18.0.- iPhones, iPads, HomePods and Apple Watches are OK.- 2 x MacBook Air M1 and a Mac mini M1 unable to connect to wifi.- Above Macs are still connecting to neighbour's wifi. iinm a Dlink and a Skyworth (ISP provided wifi routers.)- Similar log messages as OP.- APs are hAP ax3 (5Ghz AX only) & hAP ax2 (dual band AX) managed by RB5009 (all on latest stable.)- Haven't had much time to look into it but temp solution is to disable FT. ---

## Response 59
Author: Sat Sep 21, 2024 1:56 am
``` 
```
[cesar@RB5009] > /interface/wifi/security/print detail                          
Flags: X - disabled 
 0   name="Example WPA3" authentication-types=wpa2-psk,wpa3-psk encryption=ccmp,gcmp,ccmp-256,gcmp-256 passphrase="xxxxxxxx" disable-pmkid=yes management-protection=required wps=disable dh-groups=19,20,21 ft=yes ft-over-ds=yes 

[cesar@RB5009] > /interface/wifi/security/unset numbers=0 value-name=encryption 

[cesar@RB5009] > /interface/wifi/security/print detail                          
Flags: X - disabled 
 0   name="Example WPA3" authentication-types=wpa2-psk,wpa3-psk passphrase="xxxxxxxx" disable-pmkid=yes management-protection=required wps=disable dh-groups=19,20,21 ft=yes ft-over-ds=yes 

[cesar@RB5009] >
```

I encountered the same problem with a MacBook Air M1 after updating it to macOS Sequoia and being unable to connect to my home Wi-Fi. The MacBook was connecting fine on macOS Sonoma.The issue appears to be related to theencryptionparameter in/interface/wifi/security.Now the MacBook connects fine after removing theencryptionparameter from my/interface/wifi/security profileand using the default value.After some more testing, it seems to work fine withencryption=ccmp,gcmpas well.


---
```

## Response 60
Author: Sat Sep 21, 2024 10:31 am
^^^Thank you, sir. Marvellous find. encryption=ccmp, gcmp, solved it for me too. Working again with FT enabled. ---

## Response 61
Author: Sat Sep 21, 2024 11:30 am
After some more testing, it seems to work fine withencryption=ccmp, gcmpas well.These two are basic encryption algorithms (ccmp is almost another name for AES, used in WPA2) which every device supports pretty bug-free. They use 128-bit keys. The other two (ccmp-256 and gcmp-256) are new ones (using longer keys), but it seems that only a few devices support them (or rather claim to support, but their support is flakey) and some don't support them but barf upon stumbling on an AP which mentions support for them.I did some testing a while ago (with ROS 7.1 and old wave2 driver running on Audience) and some of my older devices (which even don't support WPA3) didn't want to talk to such AP. So the result is that on my APs only basic encryption types are available for now.I'm surprised that this is s problem with such a modern OS as latest iOS (personally I'm not an iVictim, so what do I know). But then there might be a problem with implementation of Xcmp-256 codecs in ROS. ---

## Response 62
Author: Sat Sep 21, 2024 1:48 pm
We've been using both the preview and the latest releases of iOS 18 and macOS 15 (Sequoia) for a while now. I also checked with some colleagues who've spent a lot of time at different customer sites (including some Mikrotik setups) and none of them have had the issues described in this thread. My wife upgraded her iPhone to 18 a few days ago and hasn’t had any problems either at work or at home.I’m not ruling out bugs but I’m pretty sure if there was a bigger Wi-Fi issue we’d have noticed it by now. This makes me think there might be some misconfigurations in the Wi-Fi network causing these devices not to connect.Here are some useful resources:Apple Platform Security GuideConfiguration Profile ReferenceHow Apple devices join Wi-Fi networksAdd Wi-Fi settings for iOS and iPadOS devices in Microsoft IntuneIf you're still having issues and are convinced it's a bug I'd recommend reaching out to Apple Support:https://getsupport.apple.com/products ---

## Response 63
Author: Sun Sep 22, 2024 7:30 pm
I have this same problem - configs worked fine on iOS 17/mac14, not working anymore on iOS 18/mac15.Setup:* wifi devices: works after enablingencryption=ccmp, gcmp, doesn't work in default (ccmp only?) mode* wireless devices: I can't find the encryption setting, so I can't make these workWhat I suspect happens is that the new iOS/macOS versions enable ccmp256 by default, but either Mikrotik or iOS doesn't support that well, so the connection doesn't work. Forcing only ccmp/gcmp, it works. ---

## Response 64
Author: Sun Sep 22, 2024 8:43 pm
@iustin, The problem is not in ROS. Everything works for me on iOS18 regardless of whether encryption is enabled (ccmp/gcmp/ccmp256/gcmp256) or not ---

## Response 65
Author: Sun Sep 22, 2024 8:53 pm
Did OP ever tell us which ROS version his/her problem occurs on?? Or which Mikrotik AP? I would guess Audience but who knows. ---

## Response 66
Author: Sun Sep 22, 2024 9:49 pm
@iustin: I have this same problem...Link to Apple Support:https://getsupport.apple.com/products ---

## Response 67
Author: Mon Sep 23, 2024 6:34 am
Did OP ever tell us which ROS version his/her problem occurs on?? Or which Mikrotik AP? I would guess Audience but who knows.Latest v7 release. I've already swapped out the MikroTik Audience APs for a competing Wi-Fi AP product from another vendor and "like magic", everything works fine, even iOS 18 devices. I've switched on/off from MikroTik's Wi-Fi gear so many times over the years, I don't even see the point in continuing to use their Wi-Fi gear. There would need to be significant and compelling reasons for me to switch back at this point. The competition in the Wi-Fi space is so far ahead of MikroTik it's actually kind of sad. I'll continue to use the routers and switches but ugh, the wireless gear is like being in the stone age at this point. That doesn't even brush upon the shortcomings of the management solution for them (CAPsMAN) which is a wholly separate problem in itself.Hell, I haven't even had a response or acknowledgment yet on my open ticket with support about this. I'll leave the ticket open and hope maybe it helps everyone else but I think I'm done and moving on for a while. I need wireless gear that works without me having to touch it to fix something and it needs to be much easier to navigate, set up and manage. What we have now leaves much to be desired. There isn't even 6e or 7 wireless standard hardware available yet from them. ---

## Response 68
Author: Mon Sep 23, 2024 7:06 am
@k2dI5umrD9VO:Link to Apple Support:https://getsupport.apple.com/products ---

## Response 69
Author: Mon Sep 23, 2024 9:40 am
``` 
```
/interface wifi
set [ find default-name=wifi1 ] channel.frequency=2401-5835 \
    .skip-dfs-channels=all configuration.country="United States" .mode=ap \
    .ssid=MikroTik disabled=no security.authentication-types=\
    wpa2-psk,wpa3-psk .connect-priority=0/1 .encryption=\
    ccmp,gcmp,ccmp-256,gcmp-256 .ft=yes .ft-over-ds=yes .group-key-update=1d \
    .wps=disable
set [ find default-name=wifi2 ] channel.frequency=2401-5835 \
    .skip-dfs-channels=all configuration.country="United States" .mode=ap \
    .ssid=MikroTik disabled=no security.authentication-types=\
    wpa2-psk,wpa3-psk .connect-priority=0/1 .encryption=\
    ccmp,gcmp,ccmp-256,gcmp-256 .ft=yes .ft-over-ds=yes .group-key-update=1d \
    .wps=disable
set [ find default-name=wifi3 ] channel.frequency=2401-5835 \
    .skip-dfs-channels=all configuration.country="United States" .hide-ssid=\
    yes .mode=ap .ssid=MikroTik-Mesh disabled=no \
    security.authentication-types=wpa3-psk .connect-priority=0/1 .encryption=\
    ccmp,gcmp,ccmp-256,gcmp-256 .ft=yes .ft-over-ds=yes .group-key-update=1d \
    .wps=disable
```

Latest v7 release.That was a simple question about the ROS version number; the answer to that is not "latest". We don't know what you think "latest" is.My spouse recentlyupdated her iPhone SE to iOS 18. Since then, she can't connect to the Wi-Fi network. Whenever I try to connect, it prompts for the Wi-Fi password, I enter it correctly, but then it immediately says unable to connect.Nothing at the router or Wi-Fi AP level has changed.Yet, you come to the forum, create a topic, and want to place all the blame on ROS. That's a rather strange approach. The device you've updated has a problem after update. Is there a correlation?Sure, ask for help and for ways to solve the problem. Or for sharing your experience. There were also plenty of suggestions to direct the issue to Apple. Yet, Mikrotik gets all of your frustration. The hurdle for an Apple developer account is probably higher than venting your frustration in Mikrotik user forum.No one denies that there is also a problem in ROS. However, the issue specifically occurs after an update of the iOS device. It makes sense to first report to Apple.And because you didn't mention it, many people here believed your issue was was with an AX AP (wifi-qcom driver). That's why there are also responses saying it works perfectly on iOS 18. However, the Audience is an AC device with a wifi-qcom-ac driver. That's a completely different driver and hardware.Some remarks:- no reason to enable FT on mesh link (wifi3). Or are your Audiences moving around?- connect-priority=0/1. I see this in every second config pasted here. Are you all copy pasting from the same topic?- .encryption=ccmp,gcmp,ccmp-256,gcmp-256. Is this something WinBox sets? Or is this on purpose?


---
```

## Response 70
Author: Mon Sep 23, 2024 10:23 am
- .encryption=ccmp, gcmp, ccmp-256, gcmp-256. Is this something WinBox sets? Or is this on purpose?I found that @normis gave this as advice:2) in "configuration" tab add one config template, that is all you need. don't enter anything else except SSID name and wireless password (select WPA2 and all cyphers except TKIP)viewtopic.php?p=1090178&hilit=tkip#p1090178As this wasn't working form me, I set it back to default. But that is were it might have come from. ---

## Response 71
Author: Mon Sep 23, 2024 10:32 am
The default is "ccmp" - according to wifi docs. So there is no need to explicitly disable TKIP.https://help.mikrotik.com/docs/display/ ... to%20ccmp. ---

## Response 72
Author: Tue Oct 29, 2024 11:24 pm
Hi, We are also facing the same problem. Our case is:Corporate Mikrotik Network using RadiusDevices connection in other networks using WEP2The devices never had a problem before iOS 18/SonomaThere is a point. If you restart the device, it will work (either in your home or the organization).That is what I need to do, as well as others.Any clue? ---

## Response 73
Author: Mon Nov 04, 2024 9:36 am
I have the same issue with my iPhone 15 Pro Max and MacBook M1 Pro (2021) when connecting to the cAP Ax2 (ROS 7) as well as the hAP Ac2 (ROS 6) with CAPsMAN. Turning on the GCMP cipher resolves the issue with the cAP Ax2 (ROS 7). I’m going to try the same with the hAP Ac2 (ROS 6) CAPsMAN, where I couldn’t connect to my network until I rebooted the MacBook. However, after deep sleep or some time, the issue reappears, and I have to reboot the MacBook again to make it work. Meanwhile, my wife’s iPhone 16 Pro Max has no issues at all, regardless of whether the GCMP cipher is enabled.I also have a similar issue with my BMW X4 CarPlay function. BMW uses Bluetooth and WiFi for streaming audio, and after a fresh iPhone reboot, it works. However, after some time (maybe a few hours), it won’t connect until I reboot my iPhone.It seems like this is an Apple problem, and I can’t resolve it myself in the BMW like I did with the MikroTik. And it’s better described as a workaround rather than a solution.Update: solved in iOS 18.2 beta 2 ---

## Response 74
Author: Mon Nov 11, 2024 5:46 pm
Hi all. Just wanna contribute some info (with temporary workaround) that I have found during investigation of the issue.So, after updating my iPhone15 to 18.0.1 I got similar issues as described in this topic:1) I was using hAP AX3 (WPA2 PSK+WPA3 PSK / CCMP+GCMP) and hAP AH2 as temporary wireless bridge (it was connected as a station to AX3's 2.4 GHz network and was repeating the same SSID with it's own 5Ghz interface in a pseudo-bridge mode, but with WPA+WPA2/ aes + ccm).So after update I wasn't able to connect to the wireless bridge running on AH2 (I was getting the same logs as were posted above: connected/disconnected).2) I lost ability to connect to my action cameras: Insta X3, Insta X4 and GoPro 11 (they are using their own wifi to transfer filmed data).At the same time my old iPhone 12 (iOS 16.5.1) works perfectly with all my cameras and hAP AH2 )First issue was solved by migration to hAP AX2 + CAPSMAN.With second issue I went to Apple (I even came to their office and brought my cameras hehe ).I was sure that it's an issue with implementation of WPA2 + ccmp back-compatibility.But today after updating my iPhone15 to iOS 18.1 I found a way to reproduce an issue and even to find a workaround.It's very funny: if I connect iphone to some network with WPA3 and then try to switch to other wifi with WPA2 (this is exactly what was happening in both my cases) I get "incorrect password" errorSo...If I disable "auto-join" for WPA3 network, reboot the phone - my first connection to any WPA2 network will be successful. If I then join any WPA3 network I won't be able to connect to any other WPA2 network again until reboot )So looks like this bug in iOS "caches" somehow WPA3 auth. method and trying to use 192 bit key everywhere until reboot (otherwise I don't know how to explain "incorrect password" error for saved networks that were used before iOS update without any issues).HTH ---

## Response 75
Author: Mon Nov 11, 2024 8:01 pm
Usually, you just need 'Forget Network' to clear cached auths. ---

## Response 76
Author: Mon Nov 11, 2024 8:43 pm
Usually, you just need 'Forget Network' to clear cached auths.I wish that things would be so simple but nope ) this iOS update have brought a lot of surprises.It’s not some kind of intended “cache”. Before going to apple office I have tried “forgetting” network, changing the behavior of MAC address (this feature was implemented in this update), complete resetting network settings (this action actually deletes all known networks, all settings related to those networks and even VPNs).It’s some kind of glitch “cache” but I can reproduce it for 100% of my attempts: after connecting to any WPA3 powered network you will be no longer able to connect to any WPA2 network unless you reboot the phone. I think iPhone starts to use WPA3 for any WIFI connection since it tried it once )This actually explains most of the floating problems described in this thread…I went to Apple’s office to report the bug cause I am too lazy to install XCode ) their office is 20 minutes far away from my place ---

## Response 77
Author: Mon Nov 11, 2024 8:50 pm
Well, according to Apple Support 'Forget Network' should clear cached auths. Unless there’s a new flaw in iOS 18 I don’t know about.. ---

## Response 78
Author: Mon Nov 11, 2024 8:54 pm
I don't have such issue, at home using MT device (ac wifi) and WPA3; and at work is WPA2 (non MT device). Can connect to both with iPhone iOS 18.1 (different SSID/BSSID ofc) ---

## Response 79
Author: Mon Nov 11, 2024 9:38 pm
``` 
```
/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk disabled=no encryption=ccmp,gcmp ft=yes ft-over-ds=yes name=MyWiFi-VLAN10-SEC
/interface wifi configuration
add disabled=no mode=ap name=MyWiFi-VLAN10-CONF security=MyWiFi-VLAN10-SEC security.ft=yes .ft-over-ds=yes ssid=MyWiFi-VLAN10
/interface wifi
add channel.band=2ghz-ax .width=20mhz configuration=MyWiFi-VLAN10-CONF configuration.mode=ap disabled=no name=cap-wifi0-2Ghz radio-mac=XX:XX:XX:XX:XX:XX security=MyWiFi-VLAN10-SEC
add channel.band=5ghz-ax .width=20/40/80mhz configuration=MyWiFi-VLAN10-CONF configuration.mode=ap disabled=no name=cap-wifi0-5Ghz radio-mac=XX:XX:XX:XX:XX:XX security=MyWiFi-VLAN10-SEC
set [ find default-name=wifi2 ] channel.band=2ghz-ax .skip-dfs-channels=10min-cac .width=20mhz configuration=MyWiFi-VLAN10-CONF configuration.hide-ssid=no .mode=ap \
    datapath.bridge=CAPSMAN-BRIDGE disabled=no name=wifi0-2Ghz security=MyWiFi-VLAN10-SEC security.authentication-types=wpa2-psk,wpa3-psk .encryption=ccmp,gcmp,ccmp-256
set [ find default-name=wifi1 ] channel.band=5ghz-ax .skip-dfs-channels=10min-cac .width=20/40/80mhz configuration=MyWiFi-VLAN10-CONF configuration.mode=ap datapath.bridge=\
    CAPSMAN-BRIDGE disabled=no mtu=1500 name=wifi0-5Ghz security=MyWiFi-VLAN10-SEC
/interface wifi capsman
set enabled=yes interfaces=CAPSMAN-BRIDGE package-path="" require-peer-certificate=no upgrade-policy=none
```

Who knows - may be it's hardware dependent. But differently the need of rebooting device to connect to some wifi networks is something that I wouldn't expect from the gadget with $1500 price  )For me it's reproducible in 100% cases: connect to WPA3 powered WiFi (MT) leads to no connectivity to any WPA2 network (neither running on MT nor Action camera) unless device is rebooted.IMHO: I don't have anything special about my MT setupAnd I totally agree withLarsa: all those issues should be reported to apple support.


---
```

## Response 80
Author: Sat Nov 23, 2024 9:43 pm
I've been able to confirm the following conditions have to be met to replicate this issue (for me at least):iPhone SE (only this model, 2nd generation.)iOS 18.xRouterOS (latest v7.x iteration)I've personally encountered two iPhone SE 2nd generation phones, both on iOS 18.x, both cannot connect to MikroTik Wi-Fi.Users in this thread claim it's "fixed" in recent iOS 18.2.x betas but we'll see when it goes final. ---

## Response 81
Author: Sun Nov 24, 2024 9:58 am
running at least 2 iPhoneSE (2gen) on IOS18 on my wifi network without issues ...ROS 7.17rc on HAP AX3.all running fine ---

## Response 82
Author: Wed Dec 11, 2024 6:28 pm
iOS 18.2 is officially released- anyone have a chance to test their broken Wi-Fi with it? ---

## Response 83
Author: Wed Dec 11, 2024 6:38 pm
iOS 18.2 is officially released- anyone have a chance to test their broken Wi-Fi with it?I don’t have the update offered yet. It’s very easy to test if you have a GoPro or Nikon camera though, I’ll be able to test in a couple of days.On Mikrotik, just enable ccmp-256 and you should see the breakage. ---

## Response 84
Author: Wed Dec 11, 2024 7:57 pm
iOS 18.2 is officially released- anyone have a chance to test their broken Wi-Fi with it?I don’t have the update offered yet. It’s very easy to test if you have a GoPro or Nikon camera though, I’ll be able to test in a couple of days.On Mikrotik, just enable ccmp-256 and you should see the breakage.Enabling/disabling ccmp-256 yields the same result in my testing- iPhone SE (not on 18.2 yet) can't connect either way. ---

## Response 85
Author: Wed Dec 11, 2024 8:08 pm
I don’t have the update offered yet. It’s very easy to test if you have a GoPro or Nikon camera though, I’ll be able to test in a couple of days.On Mikrotik, just enable ccmp-256 and you should see the breakage.Enabling/disabling ccmp-256 yields the same result in my testing- iPhone SE (not on 18.2 yet) can't connect either way.More precisely, for me Mikrotiks started working with iOS 18 after setting the encryption parameters to “ccmp, gcmp”. I don’t know if it’s ccmp-256 or gcmp-256 that causes the problem, or maybe even something else, but setting “ccmp, gcmp” makes it work. ---

## Response 86
Author: Thu Dec 12, 2024 2:52 pm
For those still following this thread, I ran into the similar issue as you all, but my "fix" was much more involved. I was fine-tuning my wifi network settings, when suddenly I realized my iPhone, and only my iPhone, would not re-connect to my wifi network anymore. I can't remember if I was adjusting steering options, or FT, but whatever I was touching had nothing to do with the wifi security settings for my network. I ran into this issue when first setting up my new hAP ax2's using CAPsMAN running on a hEX refresh, and I figured it would figure itself out eventually again. I was wrong.Everything aforementioned in this thread did not work. Every device would connect to my HAP ax2's perfectly, but every time I would try to get my iPhone on iOS 18.1.1 (and also 18.2) to connect, my connection to my home network would just hang. And hang. And do nothing after that. No errors on my iPhone, not even a "could not connect to this network". This was after multiple reboots, many times forgetting the network, and also many times resetting my iPhone's network settings back to factory default. Still would not connect. Even if I used a wrong password, it would still hang and not error out and tell me the password was wrong. If I tried to manually connect to the network while also changing the security setting to something other than WPA2/WPA3 enterprise, I could get an error to present itself on my phone. If I disabled the security on my home network, it would connect fine. Around and around I went, resetting everything I could on my phone (and rebooting my hAP ax2's and hEX refresh), and trying different setting after different setting in ROS trying to get my iPhone to connect. This went on for around 4 hours of trial and error. Note: as far as other devices go, I have an Apple TV on tvOS 18 and also a MacBook Air running MacOS 15; both worked completely fine during this issue.For context, I was only using Winbox to make the config changes the entire time. I also did not take a look at theactualconfig to see if there was something that went wrong there while using Winbox. I wish I had really taken a look at the config before I fixed the issue. Regardless, my fix was to delete the wifi configs I had in CAPsMAN and set it all back up the exact same way it was when my iPhone was failing. Lo and behold, my phone connected to my home network instantly. With the same exact settings, at least according to Winbox.With all of this said, I do not deny that there is a problem with iOS 18. However, I do find it strange that, at least as far as my phoneshouldhave been concerned, it had never seen my home network before. Even still, it would not connect. It wasn't until I completely re-did my wifi config in CAPsMAN that my phone started connecting properly again. ---

## Response 87
Author: Thu Dec 12, 2024 3:04 pm
encryption (list of ccmp, ccmp-256, gcmp, gcmp-256, tkip)A list of ciphers to support for encrypting unicast traffic.Defaults to ccmp.Playing with this and mixing security profiles after overwriting them on the physical interface tab is the root of your problems.Every single iOS/ macOS device that was ever present in my network, never had a single problem. They're roaming between bands/ connecting via WPA3 etc. ---

## Response 88
Author: Thu Dec 12, 2024 6:29 pm
Enabling/disabling ccmp-256 yields the same result in my testing- iPhone SE (not on 18.2 yet) can't connect either way.More precisely, for me Mikrotiks started working with iOS 18 after setting the encryption parameters to “ccmp, gcmp”. I don’t know if it’s ccmp-256 or gcmp-256 that causes the problem, or maybe even something else, but setting “ccmp, gcmp” makes it work.Wow, interesting. This fixed it for me as well. Set both 2.4 and 5 GHz networks to only use CCMP and GCMP, everything else unchecked. Thank you. ---

## Response 89
Author: Thu Dec 12, 2024 9:46 pm
More precisely, for me Mikrotiks started working with iOS 18 after setting the encryption parameters to “ccmp, gcmp”. I don’t know if it’s ccmp-256 or gcmp-256 that causes the problem, or maybe even something else, but setting “ccmp, gcmp” makes it work.Wow, interesting. This fixed it for me as well. Set both 2.4 and 5 GHz networks to only use CCMP and GCMP, everything else unchecked. Thank you.Glad to hear it helped! The previous post said "but ccmp is the default", which I agree it is, but doesn't make sense. If ccmp would really be the default, then one needn't override it.Well, anyway, I'll test this weekend with 18.2.