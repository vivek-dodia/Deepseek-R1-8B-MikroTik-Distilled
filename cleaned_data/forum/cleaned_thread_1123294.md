# Thread Information
Title: Thread-1123294
Section: RouterOS
Thread ID: 1123294

# Discussion

## Initial Question
Has someone else's router webfig login screen broken like this? Or is it just me?Upgraded from 7.14 to 7.17. ---

## Response 1
I have just found a device mode bug. I was able to set routerboard "cpu-frequency" from "auto" to "768MHz". Then I wanted to undo it by "/undo". It did not undo unfortunately (even though it shows "R" as like it has undone the action - but has not). So I wanted to manually set it back to "auto" -> but it was disallowed by device mode. Details reported via support ticket. ---

## Response 2
@zajDee Please clear your Browser's cache. This is the old login design. 7.17 webfig got a design overhaul. ---

## Response 3
@infabo: this is not about browser cache, it's doing this in incognito mode on all browsers and devices I have, even in Chrome when developer tools are enabled and "disable cache" toggle checked. I've run a RouterOS "Check installation" process too, it did not find anything to be repaired. ---

## Response 4
When you are familiar with developer tools: check network tab for failing requests (4x or 5x status). I am curious. But it seems more likely that the login html document is already the source of issue. So you have a modified/customized login HTML markup somehow? Branding package or the like? ---

## Response 5
In all devices in network I see this in logsystem, info ovpn server added by (/interface ovpn-server server set)I look and see OpenVPN server add to list, not see any one logged in time of creation on device.Anyone else ?Yes...Have same message. ---

## Response 6
Hello, I recently updated to version 7.17 from 7.16.2 and encountered a major issue with bridges. Their MAC addresses keep changing continuously.I’ve stripped down the configuration as much as possible, and the problem persists even with just the following minimal setup (tested on CCR, HEX, HAP, etc.):
```
# 1970-01-02 00:46:38 by RouterOS 7.17
# software id = XXXX-XXXX
#
# model = RB750Gr3
# serial number = XXXXXXXXXXXX
/interface bridge add name=VLAN10
/interface bridge add name=VLAN20
/interface bridge add name=bridge1
/interface vlan add interface=bridge1 name=vlan10 vlan-id=10
/interface bridge port add bridge=VLAN10 interface=vlan10
/system note set show-at-login=no
/system routerboard settings set auto-upgrade=yesHere’s a screenshot showing the issue:2025-01-26 17_49_51-Window.pngAfter rolling back to version 7.16.2, the problem disappears entirely.Thank you for your help.

---
```

## Response 7
You need to set the admin-mac= parameter to the MAC of the bridge.The default config does that automatically but apparently you have tinkered with it. ---

## Response 8
You need to set the admin-mac= parameter to the MAC of the bridge.The default config does that automatically but apparently you have tinkered with it.Hello pe1chl, That’s what I initially thought as well. However, in the example above, this is a full export of my HEX after a factory reset.I created the bridges and VLANs using Winbox without making any additional modifications.I’ve noticed that the issue seems to occur as soon as you add a VLAN to a bridge and then decide to bridge that VLAN to another bridge. ---

## Response 9
The default config creates a bridge and it has the admin-mac set correctly.You should normally not create any additional bridges! The VLANs can (now) be added on the single bridge.Open a new topic with your specific requirements and/or look in the existing topics about bridge and VLAN! ---

## Response 10
Bridging and switching is well documented and has a section dedicated to many possible misconfiguration examples.https://help.mikrotik.com/docs/spaces/R ... figuration ---

## Response 11
Is MT DNS buggy? I have setup Wireguard tunnels for some of our admins. Wanted to watch the DNS cache, se setup the tunnels to go via Mikrotik, which, as a first item, has internal Windows server IP address set. It works for a while, but then internal named domains / servers stop to resolve and I can see DNS cache items marked with "N", as a negative, and 0.0.0.0 IP address. Turning WG clients against the same Windows server directly, it resolves all internal domains / servers just flawlessly ..... ---

## Response 12
I was finally able to update RB450Gx4 7.16.2 -> 7.17 by going "babysteps":At start 7.17. stable gave error message "free up 9 kB of kernel disk space"I tried then with 7.17 beta6 -> "free up 5 kB of kernel disk space". Looks like we are moving to right direction...Then I took 7.17 beta2 and that succeeded - CAP's became unbound thoughThen I tried 7.17 stable again and failed.I tried again with 7.17 beta6 and that succeeded - CAP's were operational again - good news.Then I went to /system package update download to get 7.17 stable - and now that succeeded as well and all seems to be working OK for now.So your path can be 7.16.2 -> 7.17beta2 -> 7.17beta6 -> 7.17 stableThat all meant that I had to manually dig out these old betas from download.mikrotik.com - if they would not be available then all this would not have been possible.It works, thanks for the method ---

## Response 13
After reading this thread... I'm wondering... does Mikrotik actually TEST these updates on *actual* devices?By the looks of it, the situation is "we fixed 1 bug and added 3 new ones".I won't be updating to 7.17 until at least 2 minor releases. ---

## Response 14
After the update, all folder and file names in share via SMB in Cyrillic are displayed as hieroglyphs. ---

## Response 15
After reading this thread... I'm wondering... does Mikrotik actually TEST these updates on *actual* devices?As always: some tens of users, who have problems after upgrade, did come here and report problems. Hundreds (thousands), who upgraded and didn't have any problems, didn't write any praise.Myself included. ---

## Response 16
It's like evaluating a restaurant in the center of Rome where in the last few years 10 people have complained that the food was bad...In comparison to 199990 people who haven't written anything... ---

## Response 17
After upgrading to 7.17 the dhcp+radius bundle stopped working. We switched back to 7.16.2 and everything works as it should. DHPC clients receive ip after authorization via radius.We're experiencing the same issue when using DHCPv4 + RADIUS. DHCPv6 seems to work fine.Just opened a support ticket (SUP-177570), will keep you updated ---

## Response 18
IKEv2 tunnels fail to establish after upgrading to 7.17 (between 7.17<->7.17 and 7.17<->7.16.2). However, 7.17 does establish IKEv2 with Huawei AR (same settings).Rolling back to 7.16.2 does fix the issue.Auth method is PSK, 7.17 peer sends "Delete" right after successful IKE_AUTH. Tested on both live RBs and GNS3 lab.Am I the only one with this issue?UPD /ip/ipsec/proposal enc-algorithms=chacha20poly1305doesn't work.omg! You are right! That's what's not working... ---

## Response 19
on the CCR2116-12G-4S+ router, the Webfig skin designer is not working with v7.17. File is present on the correct place (skins/skinname.json) but is not selectable via System/User/Groups menu. ---

## Response 20
Maybe I'm missing something here... but this "device-mode" thing seems REALLY problematic... am I the only one using various features, across device types for scheduling and scripting and management and updates and all kinds of other things??? There is no "mode" which has everything enabled any more? So...we just break thousands of devices on the next upgrade because some of the features are on some of the routers, but nothing has everything? This seems like the death of MirkoTik in our network at this point... or, never upgrading past 7.16.2 ... I'm kind of in shock. Am I reading this wrong? ---

## Response 21
Maybe I'm missing something here... but this "device-mode" thing seems REALLY problematic... am I the only one using various features, across device types for scheduling and scripting and management and updates and all kinds of other things??? There is no "mode" which has everything enabled any more? So...we just break thousands of devices on the next upgrade because some of the features are on some of the routers, but nothing has everything? This seems like the death of MirkoTik in our network at this point... or, never upgrading past 7.16.2 ... I'm kind of in shock. Am I reading this wrong?You can always enable features you needLike the docs state:
```
system/device-mode/update mode=advanced zerotier=nohttps://help.mikrotik.com/docs/spaces/R ... evice-mode

---
```

## Response 22
The problem with device-mode is not that "no router has all features". You can simply enable all features on all your routers.The problem is that it requires physical access to enable a feature, and there is no possibility to enable a feature before you upgrade (and lose access to the feature because it is now protected by device-mode and it is not yet enabled).So you need a physical visit to your devices, and cause at least one reboot (with downtime) to make things work as before.And even then, you run the risk that MikroTik discovers another abuse scenario and puts another feature behind device-mode.Which will require another visit to solve, because there is no device-mode that says "don't bother me with device-mode"... ---

## Response 23
Maybe I'm missing something here... but this "device-mode" thing seems REALLY problematic... [...] This seems like the death of MirkoTik in our network at this point... or, never upgrading past 7.16.2 ... I'm kind of in shock. Am I reading this wrong?That was the theme from the 7.17beta thread... And, by now, Mikrotik is well aware folks use their routers on top of mountains and in war zones or other cases where a physical reboot is NOT easy...or, that they could apply to NEW routers from factory. Yet Mikrotik seemed set on adding device-mode upon upgrade, and retroactive removing features.I also don't like device-mode, at all (i.e. all of my "real" routers are remote)... but in fairness, the device-mode blocked items are pretty targeted in the 7.17 stable. So it has not had a practical effects yet. Still the concept of some "!) new device-mode restrictions..." release note in a future release still has me worried too...And I still don't get why they don't add all possible features to device-mode (with =yes) — so at least it's be wholistic one-time change that can be managed atinstall time& not some piecemeal approach of adding existing features to device-mode release-by-release in upgradesafterdeploying a router... ---

## Response 24
I see disabling the scheduler as worst problem of these "improvements". I remember the bug in hap ax lite LTE6 which caused SIM to be locked after every reboot and all Mikrotik was able to do was to provide a scheduled script as a workaround because problem was in modem firmware if my memory serves me right.Now these devices might be in use as remote devices - what happens if somebody is relying on that Mikrotik-provided "fix" and decides to apply currently available update which kills scheduler functionality? At first he would be scratching his head about why device would not come back online. Then he might start to go through the details of configuration backup and might find that scheduled script - and then even find release notes on 7.17 with these "improvements" - and what if device is not in different town but in other country or on another continent?Diving farther into this rabbit hole - can we be sure that next updates would not bring other "improvements" by disabling features through this same mechanism and everybody ends up doing this circus all over again?There might be a point where one decides to switch equipment vendor... ---

## Response 25
This is expected, if you see that ovpn server is added by system:https://help.mikrotik.com/docs/spaces/R ... OVPNServerAfter upgrade to 7.17 version ovpn server will receive its configuration, due to multiple server support.An disabled ovpn server with added mac will appear in configuration:/interface ovpn-server server add mac-address=99:99:99:99:99:99 name=ovpn-server1 ---

## Response 26
CCR2004-1G-12S-2XS -------DEAD ---

## Response 27
CCR2004-1G-12S-2XS -------DEADYou try the upgrade on lab on another CCR2004-1G-12S-2XS with same software and same backup before update? ---

## Response 28
If you can netinstall, it's not dead.Already tried that ? ---

## Response 29
The problem with device-mode is not that "no router has all features". You can simply enable all features on all your routers.The problem is that it requires physical access to enable a feature, and there is no possibility to enable a feature before you upgrade (and lose access to the feature because it is now protected by device-mode and it is not yet enabled).So you need a physical visit to your devices, and cause at least one reboot (with downtime) to make things work as before.And even then, you run the risk that MikroTik discovers another abuse scenario and puts another feature behind device-mode.Which will require another visit to solve, because there is no device-mode that says "don't bother me with device-mode"...Really annoying but perhaps the market reactions forces MTik managers to think through it once again. ---

## Response 30
You need to set the admin-mac= parameter to the MAC of the bridge.The default config does that automatically but apparently you have tinkered with it.Hello pe1chl, That’s what I initially thought as well. However, in the example above, this is a full export of my HEX after a factory reset.I created the bridges and VLANs using Winbox without making any additional modifications.I’ve noticed that the issue seems to occur as soon as you add a VLAN to a bridge and then decide to bridge that VLAN to another bridge.If it is full export of your configuration it wouldn't work regardless of Routeros version since it doesn't have any Ethernet interfaces attached to any bridge... as you would if you have chosen to activate default configuration in which case you would also have admin-mac of bridge1 set to the ether1 mac address... so either you made some additional modifications or you choose empty configuration and made this dysfunctional configuration from scratch all by your self... ---

## Response 31
I just upgraded my CCR1009 (border router) to 7.17 AND downgraded to 7.16.2 within 10minutesthere IS a problem with static DNS entries.certain hostnames where "invalid" while they always worked7.16.2 and earlierhost1.home.lan. <--- with trailing dot is acceptedin 7.17host1.home.lan. gives "failure: bad name"host1.home.lan <-- wihout dot is accepted
```
[eddie@rb1100] /ip/dns/static> add address=192.168.0.10 name=host1.home.lan. type=A                                          
failure: bad name
[eddie@rb1100] /ip/dns/static> add address=192.168.0.10 name=host1.home.lan type=A 
[eddie@rb1100] /ip/dns/static>ticket raised ...

---
```

## Response 32
If you can netinstall, it's not dead.Already tried that ?I installed 7.16.2 with NetinstallThe version with 7.17 does not restart ---

## Response 33
The problem with device-mode is not that "no router has all features". You can simply enable all features on all your routers.The problem is that it requires physical access to enable a feature, and there is no possibility to enable a feature before you upgrade (and lose access to the feature because it is now protected by device-mode and it is not yet enabled).So you need a physical visit to your devices, and cause at least one reboot (with downtime) to make things work as before.And even then, you run the risk that MikroTik discovers another abuse scenario and puts another feature behind device-mode.Which will require another visit to solve, because there is no device-mode that says "don't bother me with device-mode"...Thank you for the clarification... Yes, this is going to be an ongoing huge challenge if new features or old ones are added to device mode. I'm still just kind of in shock.. I get the need for security, but ultimately that's up to the end users.It's too bad the device mode features cant be enabled by using some known codes or info from the device (the original admin password), or requiring registration online, with a secret code provided there... or, some cloud enabled checkin to enable or disable features (which, I realize doesn't work in all cases either with air-gapped devices). ---

## Response 34
Maybe I'm missing something here... but this "device-mode" thing seems REALLY problematic... [...] This seems like the death of MirkoTik in our network at this point... or, never upgrading past 7.16.2 ... I'm kind of in shock. Am I reading this wrong?That was the theme from the 7.17beta thread... And, by now, Mikrotik is well aware folks use their routers on top of mountains and in war zones or other cases where a physical reboot is NOT easy...or, that they could apply to NEW routers from factory. Yet Mikrotik seemed set on adding device-mode upon upgrade, and retroactive removing features.I also don't like device-mode, at all (i.e. all of my "real" routers are remote)... but in fairness, the device-mode blocked items are pretty targeted in the 7.17 stable. So it has not had a practical effects yet. Still the concept of some "!) new device-mode restrictions..." release note in a future release still has me worried too...And I still don't get why they don't add all possible features to device-mode (with =yes) — so at least it's be wholistic one-time change that can be managed atinstall time& not some piecemeal approach of adding existing features to device-mode release-by-release in upgradesafterdeploying a router...Same situation here, and it will be impossible to get to all of the devices physically... it would literally take years and thousands of man hours to track down every device. This is just nuts.I posted some thoughts above about alternatives to device-mode... but another could be enabling device mode requires physical access the first time, where a key/password is set and further changes to device mode could be done remotely but need this key. This would only work for us though on NEW devices... we literally can't have features blocked on routers just because of an upgrade!In fact, I've just paused all firmware updates for everything... and I've been notifying friends and partners and others about this as well so we all don't end up with accidentally bricked networks. ---

## Response 35
I see disabling the scheduler as worst problem of these "improvements". I remember the bug in hap ax lite LTE6 which caused SIM to be locked after every reboot and all Mikrotik was able to do was to provide a scheduled script as a workaround because problem was in modem firmware if my memory serves me right.Now these devices might be in use as remote devices - what happens if somebody is relying on that Mikrotik-provided "fix" and decides to apply currently available update which kills scheduler functionality? At first he would be scratching his head about why device would not come back online. Then he might start to go through the details of configuration backup and might find that scheduled script - and then even find release notes on 7.17 with these "improvements" - and what if device is not in different town but in other country or on another continent?Diving farther into this rabbit hole - can we be sure that next updates would not bring other "improvements" by disabling features through this same mechanism and everybody ends up doing this circus all over again?There might be a point where one decides to switch equipment vendor...I agree 100%... The scheduler is one of the first things I think of when I freak out. We use the scheduler for scripts to do pretty much everything... we use use these together in groups and separately to provide "logic" to behaviors and automation, control traffic, enable and disable ports, etc etc. ---

## Response 36
Just saw the "Flagged Status" thing also... based on some arbitrary rules (which we do not know), our configuration could be flagged and we could be locked out of certain configuration items and have to PHYSICALLY visit a site to clear this flag.This is the biggest joke on the planet.Definitely wont be upgrading to 7.17...and I guess it's time to start checking into Juniper and paying a lot more. Sad day for MikroTik users, I think... I couldn't begin to trust a product with these restrictions in my networks, unless there is always a way to recover from an issue/error state remotely. Happy to always support security initiatives, but there's a point where too much security makes the device untrusted/unusable. I can have the most secure and completely guaranteed un-hackable MikroTik in the world by leaving it in the box...but that's not very useful. There needs to be a balance. ---

## Response 37
It would be just as simple as giving 24h (or maybe a bit more) of "grace time" to set the new desired mode, if you don't -> restrictions get enforcedAfter all:- if you don't upgrade -> you're "vulnerable" (in the future)- if you upgrade -> set (or not) the desired mode during the "grace time" -> ok- if a hacker enter your device and they upgrade the device (why would they do that?!?) -> they can change mode/everything during grace time ..BUT they could do almost anything already, so what's the point!Is my thinking so wrong? sure I'm missing some scenario otherwise it would be already in place ;-) ---

## Response 38
Is MT DNS buggy? ... "N", as a negative, and 0.0.0.0 IP address. Turning WG clients against the same Windows server directly, it resolves all internal domains / servers just flawlessly .....Do you see something similar to "syn flood detected on port" in your logs? Other have reported if there is "too much" DNS requests, it falsely detects syn flood and DNS starts to returns NXDOMAIN, i saw the same once on a RB5009 running 7.17, did not happen again since.Not sure how DNS UDP is related to TCP syn flood detection. ---

## Response 39
Do you see something similar to "syn flood detected on port" in your logs?Yes, for me also, and had to go back to 7.16.2 which is for me the last in the mikrotik line. I am already looking for other vendors unfortunately, after 16 years of Mikrotik use. ---

## Response 40
Hello Mikrotik, Playing around with a firmware analysis tool called BugProve shows several critical vulnerabilities and possible buffer overflows in ARM64 RouterOS firmware version 7.17. Attached is a screenshot of the analysis. Is this an oversight or is the BugProve application providing some false-positives?Thanks for your time.Screenshot 2025-01-28 204158.png ---

## Response 41
... I am already looking for other vendors unfortunately, after 16 years of Mikrotik use.@normis this is what the start of MikroTik business failure looks like.Bug fix RouterOS before everything else is the best hope.Alternative is allow third party software on MT hardware. ---

## Response 42
Download from ... FAILED: Idle timeout - receiving contentexecuting script ... from scheduler failed, please check it manually ---

## Response 43
Download from ... FAILED: Idle timeout - receiving contentexecuting script ... from scheduler failed, please check it manuallyWhat a meaningful trouble report. No context, no nothing. Damn, my crystal ball failed again. ---

## Response 44
Just saw the "Flagged Status" thing also... based on some arbitrary rules (which we do not know), our configuration could be flagged and we could be locked out of certain configuration items and have to PHYSICALLY visit a site to clear this flag.Flagging is actually covered in documentation... ---

## Response 45
... I am already looking for other vendors unfortunately, after 16 years of Mikrotik use.@normis this is what the start of MikroTik business failure looks like.Bug fix RouterOS before everything else is the best hope.Alternative is allow third party software on MT hardware.What would make Mikrotik "special" in any use-worthy way if you would run other software on it? ---

## Response 46
The problem with device-mode is not that "no router has all features". You can simply enable all features on all your routers.The problem is that it requires physical access to enable a feature, and there is no possibility to enable a feature before you upgrade (and lose access to the feature because it is now protected by device-mode and it is not yet enabled).So you need a physical visit to your devices, and cause at least one reboot (with downtime) to make things work as before.And even then, you run the risk that MikroTik discovers another abuse scenario and puts another feature behind device-mode.Which will require another visit to solve, because there is no device-mode that says "don't bother me with device-mode"...Thank you for the clarification... Yes, this is going to be an ongoing huge challenge if new features or old ones are added to device mode. I'm still just kind of in shock.. I get the need for security, but ultimately that's up to the end users.It's too bad the device mode features cant be enabled by using some known codes or info from the device (the original admin password), or requiring registration online, with a secret code provided there... or, some cloud enabled checkin to enable or disable features (which, I realize doesn't work in all cases either with air-gapped devices).If that "cloud-enabled checkin" would work as this forum does then it would be significantly less than completely useless. It woud be one more thing for Mikrotik to maintain, develop and "bugfix" ---

## Response 47
After updating my hAP ax2 to 7.17, I can't connect my Galaxy Watch 6 with latest Wear OS to 5GHz anymore, only to 2GHz. Nothing special in settings, just basic setup via "Quick Set". I see these messages in the logs: ---

## Response 48
What would make Mikrotik "special" in any use-worthy way if you would run other software on it?IMO MikroTik has market share by undercutting both enterprise and consumer devices.There is a forever market as the hardware performance value provider.RouterOS v7 changed development model used upto v6 and prior.RouterOS v7 kept "stable" release name but it is not so anymore.IMO network devices should reliably upgrade firmware without requiring users to become expert MikroTik forum readers to decide if release fails on their device.Even though I'd rather do something else with my time, I'm here because I want this scrappy Latvian business story to continue indefinitely.IMO MikroTik is making poor software development choices right now but they are all fixable issues which is the real frustration.More voices pointing toward to an in demand future should become persuasive for keeping MikroTik ongoing and well. ---

## Response 49
RouterOS v7 changed development model used upto v6 and prior.Are you referring to the update channels (aka release trees: bug-fix (later long-term), stable and testing) here? Those were introduced circa 6.29 or 6.30 in the middle of 2015. At that point there were no missing features compared to v5, and this split allowed for field testing of new features in stable without exposing the accompanying bugs to those who don't need these new features. Apparently, it's too early to follow the same model in v7 yet, at least that's how explain it to myself. ---

## Response 50
The problem with device-mode is not that "no router has all features". You can simply enable all features on all your routers.The problem is that it requires physical access to enable a feature, and there is no possibility to enable a feature before you upgrade (and lose access to the feature because it is now protected by device-mode and it is not yet enabled).Do you know what is funny? If you use CHR on cloud and want to enable features you gonna open case and beg admins toshut offVM within limited time if you are lucky enough. It's like wishing all planets to line up. What a joke. ---

## Response 51
Do you know what is funny? If you use CHR on cloud and want to enable features you gonna open case and beg admins toshut offVM within limited time if you are lucky enough. It's like wishing all planets to line up. What a joke.Wouldn't it be more logical if you could do that power-cycle yourself ? ---

## Response 52
That would be possible if you have management access to your externally hosted VM. If not then you're in trouble. Other thing is that normal VM reboot is not enough - it must be executed as powerdown or reset action. ---

## Response 53
Does device-mode get reset during factory rest to defaults?? or once they are enabled on hardware, they persist? ---

## Response 54
Documentation doesn't say. One probably needs to test to find out... ---

## Response 55
Does device-mode get reset during factory rest to defaults?? or once they are enabled on hardware, they persist?Documentation doesn't say. One probably needs to test to find out...Seehttps://help.mikrotik.com/docs/spaces/R ... evice-modeI'm not a fan of device-mode" but the docs do explain, although in a long paragraph that Mikrotik should format betterThere are three available modes:advanced, home and basic.[...]if the router is manufactured andshipped withMikroTik RouterOS v7.17 or later.[*] Advanced (previously called enterprise) mode is assigned to CCR and 1100 series devices,[*] home mode is assigned to home routers and basic mode to any other type of device.For devices running versionsprior to RouterOS version 7.17,[*]all devicesuse theadvanced/enterprisemode.and so if you upgrade to 7.17, you'll get "advanced" (or should per docs). There is NO reset to default mentioned in and the upgrade only changes the /system/device-mode setting, NOT your config.So and "advanced" mode, which you'd have after upgrade, only restricts four things (from docs and test router):By default, advanced mode allows optionsexcept traffic-gen, container, partitions, install-any-version, routerboard. So to use these features, you will need to turn it on by performing a device-mode update.And resolving those device-mode restrictions from docs:traffic-gen- /tool traffic-generator /tool flood-ping /tool ping-speedpartitions**- /partitions -does not allow to change count of partitions. If your router is unable to boot, it will still be able to boot into your other partitions. No restriction for crash recovery.install-any-version- RouterOS will no longer allow for you to install RouterOS version below versions listed under "allowed-versions" attribute.container*- all container featuresrouterboard- /system routerboard settings (except auto-upgrade option)* device-mode container=no has always been disabled by device-mode for many versions. In my test, I had container=yes already enabledbeforeupgrade and the upgrade left that alone - but on this one the docs are NOT clear....And the "allowed-version", on RB1100 at least, is shown as:
```
:put [/system/device-mode/get allowed-versions]
7.13+,6.49.8+So, yes, after update you will no longer be able"remotely"downgrade to below versions.  So theinstall-any-version=nomay be biggest restriction someone may face IMO - i.e. You're running 7.12.1 on router w/16MB flash - e.g. version one before the wifi changes that you have to stop at if below 7.12 – you would NOT be able to go back 7.12 without physical access to enable the install-any-version=yes via device-mode.  I presume if an upgrade fails due to disk space, it will still rollback from 7.12 since hopefully device-mode wouldn't have applied — but I'm not sure nor confident – why I worry about this feature.Now on new factory units, device-mode is going to have to added to folks provisioning processes — sincenew units may have "home" which is FAR more restricted (see docs for NEW routers).

---
```

## Response 56
Yea, I've read the docs but I agree they're not very clear on certain things.I asked about the device mode settings sticking around after a factory reset, because I've set at my desk thousands of miles away from a router before and factory reset them, and then set them up completely from scratch again. Hopefully we can still do this.Maybe device mode reboot/power restriction could be removed for console connections and/or ROMON? (since you'd need layer 2 access) ??*shrugs* Trying to be ok with all of this, and just not hahaha. Maybe I can send MikroTik the bill every time we need to hire a helicopter to fly to remote sites to push a button? hahaha ---

## Response 57
Since im thrilled with the new interface list option for the switches and the bridge.. I was trying to get all of my switches flash figged to my set up with this configuration. But at first I was having an error that said "device-mode" wasn't allowing it. So I then made some changes and it let me change the boot mode to flash-boot. But now it just doesnt work and im connecting to the switch on port 1this is the CRS318-16-2S+OUT.
```
system/device-mode> print 
                 mode: advanced     
     allowed-versions: 7.13+,6.49.8+
              flagged: no           
     flagging-enabled: yes          
            scheduler: yes          
                socks: yes          
                fetch: yes          
                 pptp: yes          
                 l2tp: yes          
       bandwidth-test: yes          
          traffic-gen: no           
              sniffer: yes          
                ipsec: yes          
                romon: yes          
                proxy: yes          
              hotspot: yes          
                  smb: yes          
                email: yes          
             zerotier: yes          
            container: no           
  install-any-version: no           
           partitions: no           
          routerboard: yes          
        attempt-count: 0and config is like this for my ether1 port
```

```
/interface bridge port
add bridge=bridge comment=defconf frame-types=admit-only-untagged-and-priority-tagged interface=ether1 internal-path-cost=10 \
    path-cost=10 pvid=200 trusted=yesAnd I can reach and configure my switch on that port. I download the latest version of flash fig. and for whatever reason after the reboot.. it just doesnt take.. Im lost.And router board config I like this every time I reboot and im plugged into port 1..
```

```
/system routerboard settings
set boot-device=flash-boot-once-then-nandAny help would be greatly appreciated.. ive been doing this for my event switches for a few years now with no issues.. not sure whats going on now..Firmware is up to date btw
```

```
/system/routerboard> print 
       routerboard: yes           
        board-name: netPower 16P  
             model: CRS318-16P-2S+
     serial-number:   
     firmware-type: dx3230L       
  factory-firmware: 6.48.6        
  current-firmware: 7.17          
  upgrade-firmware: 7.17

---
```

## Response 58
Hello Mikrotik, long long (1996) time user here, congratulations on your great product, and good technology roadmap. BUT.I have two CHR used in my family residences, beautiful product, reliable as hell. I upgrade them sparingly as they work: one of them has 14+ Wireless Access Points, other is local to me, at my new home, and I am just running x1 Wireless Access Point, with CapsMan. At least I was, until I decided to upgrade to 7.17. GUESS WHAT HAPPENED ?1. I hadn't upgraded in a long while, older version was I believe 7.13/7.14 I forget. (Getting old, me). I thought - the upgrade process is always smooth, so I will download and install and all will be fine before sleep.AND THEN.2. Nothing. No activity. None whatsover. "It's dead, Jim". "He's dead, Jim".3. Ok, I have a LAN cable, and a laptop with ethernet dongle, and I am the only engineer in this city who has umpteen years of experience with branded Mikrotik, and I can fix it. SO.4. I power cycle the CHR, and see the Winbox come up (GREAT) and then notice the RouterOS was upgraded, and installed. But WIRELESS package 7.17 was showing "X". I tried rebooting etc., but it stayed stubbornly "X". So, no CapsMan, no wireless access points, no wireless service.5. I got worried that I had bricked the system, or that my old CapsMan config was lost, or something. I looked at the Forum, and didn't see anyone else complain about the missing WIRELESS packages, and didn't have anything else to try - BUT I could DELETE IT. So I did.6. I downloaded the RouterOS support packages for ARM and extracted the WIRELESS 7.17 package and uploaded via WinBox to FILES. (FANTASTIC).7. I then rebooted to install, and CapsMAN showed up. GREAT.8. AND MY CONFIG WAS STILL THERE !I have since (a) upgraded boot image (b) restarted DDNS service (c) done cloud backup and rediscovered the EXPORT command (CLI) that gives me full text only configuration file (.rsc) for the entire routerOS.Please highlight this for newbies, or non-professional admins.Thank you Mikrotik developers. ---

## Response 59
... I am already looking for other vendors unfortunately, after 16 years of Mikrotik use.@normis this is what the start of MikroTik business failure looks like.Bug fix RouterOS before everything else is the best hope.Alternative is allow third party software on MT hardware.Big fall of a great story, I'm sad. They don't seem to care until they realize they've shot themselves in the foot. Maybe they want to close the store, who knows, but I also stops every MTik device acquisition at my company as long as they cling rigidly to this nightmare. This is very not professional.Most of the MT HW is 3rd party capable I think. Netboot a Linux on them and you can testing. I did it on my RB450G and RB433AH 15 years ago. Maybe it works on new ones too. ---

## Response 60
Most of the MT HW is 3rd party capable I think. Netboot a Linux on them and you can testing. I did it on my RB450G and RB433AH 15 years ago. Maybe it works on new ones too.Mikrotik locked out 3rd party OS with RouterBOARD firmware version 7...https://openwrt.org/toh/mikrotik/commonFor older devices you can downgrade, but on newer devices that are shipped with ROS7 you cannot install anything but RouterOS, at least for now...But frankly I never used any 3rd party software because great part of why I use Mikrotik is RouterOS, and although there are some hiccups with new version they are usually fixed soon enough. That being said maybe it is time to stabilize ROS 7 and release something like Long-Term version... ---

## Response 61
It seems 7.17 has a problem with VRRP and connection tracking.I have a setup where two CHRs are connected with a VXLAN (due to corporate BS that does not allow VRRP native)Connection tracking was turned on in 7.16.X and to my knowledge seems to have worked, - we switched the routers multiple times and never got a complaint that switching routers caused a connection to drop.Today we upgraded to 7.17 and immediately got a red warning in winbox that connection tracking is not working.Additional info: I can see traffic on the underlying VXLAN back and forth but VRRP does not seem to be to pass connection information or much of anything else.what can I do to get connection tracking back online or is that a bug and I will have to downgrade?UPDATE: Since this is in a PROD environment I could not wait and had to downgrade to 7.16.2 and the problems went away. Same Firewall, same everything, so somewhere there is a bug in the 7.17 VRRP over VXLAN ---

## Response 62
Mikrotik locked out 3rd party OS with RouterBOARD firmware version 7...Writing that mikrotiklocked out3rd party OSes is quite a heavy statement. Judging on MT's track record I'd rather say that with v7 MT introduced changes in routerboot (OS loader) which are in a way incompatible and nobody reverse-engineered those changes to make their OS compatible with routerboot v7. MT is definitely not interested in supporting 3rd party OSes on their hardware but and I guess it's only expected (MT started as OS shop and added proprietary hardware, not the other way around). But I never got impression that MT would actively work against 3rd party OSes. ---

## Response 63
Mikrotik locked out 3rd party OS with RouterBOARD firmware version 7...Writing that mikrotiklocked out3rd party OSes is quite a heavy statement.Not publishing bootloader specs is effectively the same thing as locking out, for as long as somebody from 3rd parties hacks and reverse engineer it at least... ---

## Response 64
Writing that mikrotiklocked out3rd party OSes is quite a heavy statement.Not publishing bootloader specs is effectively the same thing as locking outIMO "locking out" is deliberate and active act, "not publishing" can only be called "negligence" towards 3rd parties and is completely normal in normal (i.e. not "free as speach") corporate environments.But I guess this is now discussion about last year's snow, not important for MT and ROS future (at least not until MT changes their business goals).I guess that there are large number of users who like ROS and some users who like MT hardware (and I guess their number is much lower than number of ROS fans ... after all, I don't find MT hardware particularly attractive compared to other vendors' offerings in same price range). And there are (majority?) users who don't have strong feelings about the matter (because low price point matters to them). So IMO ROS is MT's strength and they should focus on it ... nice proprietary hardware might be a cherry on the top of a cake (and I prefer this cake over this cherry). ---

## Response 65
Not publishing bootloader specs is effectively the same thing as locking out, for as long as somebody from 3rd parties hacks and reverse engineer it at least...MikroTik has the choice to make it 3rd party software easy with full hardware disclosure or hard by doing nothing. ---

## Response 66
Not publishing bootloader specs is effectively the same thing as locking outYou could go to the EU Parliament and propose a law requiring all manufacturers to make their devices fully accessible for open-source operating systems, including the publication of specifications and all relevant documentation. ---

## Response 67
We only make changes that improve security of the users, none of those changes are to actively deny 3rd party OSes ---

## Response 68
IMO "locking out" is deliberate and active act, "not publishing" can only be called "negligence" towards 3rd parties and is completely normal in normal (i.e. not "free as speach") corporate environments.... So IMO ROS is MT's strength and they should focus on it ... nice proprietary hardware might be a cherry on the top of a cake (and I prefer this cake over this cherry).Agreed, MikroTik rights on hardware disclose is their choice. I'm pleasantly surprised by last said which suggests as a late comer viewing MikroTik as hardware company first is a historical misconception; thank you for sharing that history and a different perception. This suggests MikroTik has customers with competing interests that it must straddle to maximize market share and secure it's future.As customers, what can we do the help MikroTik chart such a path? ---

## Response 69
We only make changes that improve security of the users, none of those changes are to actively deny 3rd party OSes@normis! So good to see you out and about. I find your reassurances both credible and compelling. Thank you, ---

## Response 70
Flash fig 🥹 ---

## Response 71
You could go to the EU Parliament and propose a law requiring all manufacturers to make their devices fully accessible for open-source operating systems, including the publication of specifications and all relevant documentation.I respect everyone's right to petition their governing authority for relief they may deem compelling.My personal preference in this case is leaving MikroTik the choice to determine their future. ---

## Response 72
Voluntarism works very well in a market economy. However, as Normis already mentioned, MikroTik does not take active countermeasures.Can you name another manufacturer that has voluntarily published both its bootloader code and comprehensive documentation for its devices? Just one example will suffice. ---

## Response 73
I have an CRS326 with L3HW here, that gets a prefix via DHCP6. The prefix is announced, as well as the default route registered, but traffic is not forwarded. For traffic to be correctly forwarded, i need to disable and re-enable L3HW manually. Looks a lot like a bug to me.Anyone else seen something similar?Best! ---

## Response 74
After upgrading to 7.17 the dhcp+radius bundle stopped working. We switched back to 7.16.2 and everything works as it should. DHPC clients receive ip after authorization via radius.We're experiencing the same issue when using DHCPv4 + RADIUS. DHCPv6 seems to work fine.Just opened a support ticket (SUP-177570), will keep you updatedReply from Mikrotik support:Hello, Thank you for contacting MikroTik Support.The issue is identified and will be addressed in further RouterOS releases.We are sorry for the inconvenience causedBest regards, Thanks!!! ---

## Response 75
But I guess this is now discussion about last year's snow, not important for MT and ROS future (at least not until MT changes their business goals).I guess that there are large number of users who like ROS and some users who like MT hardware (and I guess their number is much lower than number of ROS fans ... after all, I don't find MT hardware particularly attractive compared to other vendors' offerings in same price range). And there are (majority?) users who don't have strong feelings about the matter (because low price point matters to them). So IMO ROS is MT's strength and they should focus on it ... nice proprietary hardware might be a cherry on the top of a cake (and I prefer this cake over this cherry).Honestly... it's hard to see much worth of "writing home about" in Mikrotik hardware without RouterOS. It is mostly a combination of generic off-the-shelf components - and these combinations are often put together in a questionable way when it comes to performance. And I don't even want to start about these 24 V "power bricks" which cause most of equipment outages by their own death... ---

## Response 76
We only make changes that improve security of the users, none of those changes are to actively deny 3rd party OSes@normis! So good to see you out and about. I find your reassurances both credible and compelling. Thank you, Well, "improving security of the users" by making changes and then not documenting them is effectively the same as denying 3rd parties.Remember how the authentication of winbox and MAC access was changed, to improve security, but the new method remains undocumented.Now the 3rd pary "mac-telnet" tool no longer works and cannot easily be made working again. ---

## Response 77
About "improving security" - one "sensitive data handling" bug was fixed in latest Winbox 4 and who knows if there's more if they're not discovered. Dedicated app can be handy and useful but is another can of worms in addition to device itself. ---

## Response 78
Remember how the authentication of winbox and MAC access was changed, to improve security, but the new method remains undocumented.The question is: was the method before the "new method" documented? ---

## Response 79
The question is: was the method before the "new method" documented?Probably it was a "known" method, apparently someone was able to write an independent mac-telnet program that worked.And now that no longer works.Still, "security by obscurity" is not a method that is generally valued well in the security world. ---

## Response 80
Well, "improving security of the users" by making changes and then not documenting them is effectively the same as denying 3rd parties.While, I don't doubt Mikrotik's efforts or good intent. It's the communications and attitude about security is downright lousy.Security topics deserve some docs/blog/help/KB/etc, not just two-way trolling messages in the forum. Look atcloudflare/others, their security blogs are full of real discussion of problem/solution/effected things/workaround. I'm not that expecting much, but for example device-mode should have been mentioned/explained onhttps://mikrotik.com/supportsec– instead last update was in 2023.Like I'd really like to know where the "allowed-version" /system/device-mode comes from?
```
allowed-versions: 7.13+,6.49.8+That implies less than 7.13 has some vulnerability or otherwise flawed.  So should everyone upgrade to at least 7.13?Now for all we know they could have from @normis' cat too.  Thus the complaints.

---
```

## Response 81
Well, "improving security of the users" by making changes and then not documenting them is effectively the same as denying 3rd parties.While, I don't doubt Mikrotik's efforts or good intent. It's the communications and attitude about security is downright lousy.Security topics deserve some docs/blog/help/KB/etc, not just two-way trolling messages in the forum. Look atcloudflare/others, their security blogs are full of real discussion of problem/solution/effected things/workaround. I'm not that expecting much, but for example device-mode should have been mentioned/explained onhttps://mikrotik.com/supportsec– instead last update was in 2023.Like I'd really like to know where the "allowed-version" /system/device-mode comes from?
```
allowed-versions: 7.13+,6.49.8+That implies less than 7.13 has some vulnerability or otherwise flawed.  So should everyone upgrade to at least 7.13?Now for all we know they could have from @normis' cat too.  Thus the complaints.That is as problematic as "release notes" stuff i.e. inability to have count on known issues. Maybe these are missing because they themselves do not know (about them)? This is lingering into "unknown known" field of things - which makes this issue itself one of "known unknowns"...It might be good to pound the chest by not having any known CVE level security issues after 2023, but that might not mean that there's no actual issues of this level in existence.Depending on forum posts instead of proper release notes and other related documentation is not sustainable either - especially while forum has not been proven to be reliable lately (500 Internal Server Error messages are not exactly rare...)

---
```

## Response 82
Security topics deserve some docs/blog/help/KB/etc, not just two-way trolling messages in the forum. Look atcloudflare/others, their security blogs are full of real discussion of problem/solution/effected things/workaround. I'm not that expecting much, but for example device-mode should have been mentioned/explained onhttps://mikrotik.com/supportsec– instead last update was in 2023.And it doesn't look promising when topics like this quickly gets deletedviewtopic.php?t=214285Still indexed by Googlehttps://www.google.com/search?q=%22Rout ... ilities%22 ---

## Response 83
https://mikrotik.com/supportsecAnd it doesn't look promising when topics like this quickly gets deletedviewtopic.php?t=214285Still indexed by Googlehttps://www.google.com/search?q=%22Rout ... ilities%22Well, in fairness, they do publish a "responsible disclosure policy" on their security web site. So publishing potential vulnerabilities on the forum is pretty clearly against those rules, and thus forum rules. But it does strain credibility that there is nothing of note on the security front since 2023-07-27.On the practical side, I'd rather not upgrade otherwise working router to every release, so I run a mix a versions. Now if there is documented security issue, I'd want to upgrade ASAP. But the 16MB flash stuff is still a risk in my world, so unless there is a security issue, I want to leave them alone as much as possible until replaced. But why I persist in the topic. ---

## Response 84
I saw that topic, maybe there is a way to handle this more transparent and trustworthy, for example eather MT staff respond that reported vulnerabilities are false positive or edit OP post, remove sensitive info, respond that they are investigating it and lock topic.This looks like they are ignoring such issues or are unable to fix, such investigation like in that topic can do some security enthusiast IMO, which means some serous hackers are aware of it for sure if vulnerabilities are valid. ---

## Response 85
Hi guys ! Do you have please any feedback how hap ac2 "cooperates" with 7.17+wifiwave2 ? I have some spare devices which i need to deploy, thinking about this config+capsman for one AP. Im just wondering how does it perform (registered in this topic some reboot issues during beta phase). Thank you ! ---

## Response 86
Do you see something similar to "syn flood detected on port" in your logs?Yes, for me also, and had to go back to 7.16.2 which is for me the last in the mikrotik line. I am already looking for other vendors unfortunately, after 16 years of Mikrotik use.I'm seeing this as well:possible SYN flooding on tcp port 53 ---

## Response 87
Regarding the latest ROS updates, there is a popular saying in Brazil that says "Before it gets better, it gets worse" ---

## Response 88
A have a CHRs only lab which was runs on 7.17beta2 fine. It has configured OSPFv2+v3, MPLS LDP dual-stack, BGP IPv4, IPv6, VPNv4, VPNv6, VPLS (both)Upgraded to 7.18beta2 and the IPv4 RIB issue (SUP-176975) happens. On 7.17beta4 the same. Something happens between 7.17beta2 and 7.17beta4 and a lot of another bad things happened between 7.16 and 7.17.7.17 is far from stable and from RC too in BGP aspect. ---

## Response 89
It is time for 7.17.1. ---

## Response 90
What's new in 7.17.1 (2025-Jan-30 12:29):*) bgp - improved system stability when printing BGP advertisements;*) bridge - fixed endless MAC update loop (introduced in v7.17);*) dhcpv4-server - fixed lease assigning when server address is not bind to server interface (introduced in v7.17);*) igmp-proxy - fixed multicast routing after upstream interface flaps (introduced in v7.17);*) ipsec - fixed chacha20 poly1305 proposal;*) ipsec - fixed installed SAs update process when SAs are removed;*) ipv6 - fixed an issue where bridge, IP, IPv6 and discovery settings were lost after upgrade due to conflicting IPv6 properties (introduced in v7.17);*) ovpn - added requirement for server name when exporting configuration;*) ppc - fixed HW encryption (introduced in v7.17);*) queue - improved system stability when many simple queues are added (introduced in v7.17);*) resolver - fixed static FQDN resolving (introduced in v7.17);*) system, arm - automatically increase boot part size on upgrade or netinstall (fixed upgrade failed due to a lack of space on kernel disk/partition);*) winbox - show warning messages for static DNS entries; ---

## Response 91
And it doesn't look promising when topics like this quickly gets deletedviewtopic.php?t=214285Still indexed by Googlehttps://www.google.com/search?q=%22Rout ... ilities%22Well, in fairness, they do publish a "responsible disclosure policy" on their security web site. So publishing potential vulnerabilities on the forum is pretty clearly against those rules, and thus forum rules. But it does strain credibility that there is nothing of note on the security front since 2023-07-27.There may be sufficient reason to hide an exploit technique but IMO hiding an exploit exists in specific version or the OP was just false warrants disclosure. ---

## Response 92
Since I saw the OP's screenshot of the deleted post and checked every line, it was all bullshit.The only way to exploit those vulnerabilities in libraries used by RouterOS was to hack RouterOS first, to execute arbitrary commands as super-admin.So, who cares about those problems, if to exploit them the device as had to be compromised already???All bullshit.WARNING: New RouterOS vulnerability: If RouterBOARD is immersed in water, it stops working. ---

## Response 93
I'm not sure, but since the upgrade to 7.17.1, neither my L2TP (IPsec) VPN nor my WireGuard tunnel to ProtonVPN are connecting. I hope this isn't directly related. ---

## Response 94
I'm not sure, but since the upgrade to 7.17.1, neither my L2TP (IPsec) VPN nor my WireGuard tunnel to ProtonVPN are connecting. I hope this isn't directly related.Do you see a "TCP syn flood warning" in the log?I have a similar problem since end of last year. The MT detects a possible syn flood and shuts down all responses to tcp syn packets. The support have not responded to the ticket for a month... ---

## Response 95
No syn flood warning. I only saw a handshake timeout for WireGuard and a "VPN terminating" message for the L2TP connection in the log. I enabled debug logging for the IPsec and L2TP topics, but nothing appeared—there were no changes or additional debug output (watched the situation for at least 10min). After rebooting the device, the log was suddenly full of debug messages, and both WireGuard and L2TP were working again. I'm not sure what happened, especially since enabling debug logging initially had no effect. It was quite strange, aside from the actual issue itself. ---

## Response 96
Well, in fairness, they do publish a "responsible disclosure policy" on their security web site. So publishing potential vulnerabilities on the forum is pretty clearly against those rules, and thus forum rules. But it does strain credibility that there is nothing of note on the security front since 2023-07-27.There may be sufficient reason to hide an exploit technique but IMO hiding an exploit exists in specific version or the OP was just false warrants disclosure.MikroTik did not delete that topic, it was one of the volunteer moderators, because it was a duplicate post. It still exists in the other post. ---

## Response 97
@infaboI haven’t noticed any issues with WireGuard after the update. ---

## Response 98
It is time for 7.17.1.You got it in less than 1 hour :) ---

## Response 99
*) bgp - improved stability;What does it mean exactly? What is the scenario that has been fixed? ---

## Response 100
MikroTik did not delete that topic, it was one of the volunteer moderators, because it was a duplicate post. It still exists in the other post.Didn't noticed that other duplicate/similar topics are such quickly deleted, mostly there is a post in it like "see -> <url_to_other_similar_topic>".Regarding my transparency and handling such topics, @rextended could be right that these vulnerabilities can be exploited only on already compromised ROS (no remote exploits), but by looking from perspective of users who are not following this forum and searching on Google security/vulnerabilities terms for MT devices which may lead to such deleted topics it may rise their concerns. This can lead to bad reputation and reduced sale. I still think there are better ways to handle this, like @Amm0 proposed with sec. blogs/KB/etc where is explained that some audits can lead to false positive results - and which and why; or at least leave such forum topics with some official response and lock them. ---

## Response 101
Like I said, I (or MikroTik) would not have deleted it. It was a volunteer mod. ---

## Response 102
OK, still you can advise them how to handle it. ---

## Response 103
Not sure what all the fuss is about ...Look for post in this thread with "RouterOS 7.17 BugProve Testing" as title.It's still there for everyone to see.Like I said, I (or MikroTik) would not have deleted it. It was a volunteer mod.To be correct, it was merged into this thread, not deleted.(it wasn't me)Maybe you can respond to it ? ---

## Response 104
Hmmm, since the update from 7.17 to 7.17.1 my routing rules are not working anymore.I´ve two ISP-lines (TK is main, VF is backup) and SIP numbers from both.To prevent the connectivity to the VF SIP numbers over the TK line I´ve created coresponding routing rules.That worked fine until the update. After it all 3 VF numbers were offline.A trace shows me that the connection went over the TK-line instead over the VF-line, so the rules were ignored.The reactivation of dedicated routing entries in the MAIN table fixed it.@MT: could you please check this behaviour? ---

## Response 105
Uh, bad... I have public hotspots that route the traffic via VPN (Mullvad). That is does with routing rules, and fails to do so with RouterOS 7.17.1 - so all traffic goes via regular WAN. ---

## Response 106
Not sure what all the fuss is about ...Look for post in this thread with "RouterOS 7.17 BugProve Testing" as title.It's still there for everyone to see.Like I said, I (or MikroTik) would not have deleted it. It was a volunteer mod.To be correct, it was merged into this thread, not deleted.(it wasn't me :lol: )There was one topic on "BugProve" where I responded/replied to. Then suddenly this particular topic vanished and my reply appeared in this topic - without any context. So I requested to delete my post because it made no sense without the original-post I had replied to. ---

## Response 107
Do you have please any feedback how hap ac2 "cooperates" with 7.17+wifiwave2 ? I have some spare devices which i need to deploy, thinking about this config+capsman for one AP. Im just wondering how does it perform (registered in this topic some reboot issues during beta phase).The big problem of hAP ac2 and wifi-qcom-driver is lack of flash storage. I think that consensus would be that it works OK if number of functions of device is kept at minimum. So if you only use it as AP (no routing, no DNS adlists, no any other crap), it should work great ... wifi-qcom-ac drivers offer greatly improved throughputs and stability of wireless service. However htere are functions, which are not available with wifi-qcom-ac driver (e.g. VLAN handling by driver itself, any other wireless protocol apart from 802.11, etc.) and if you require them, then ... get used to the new reality because some lacking features are there also in wifi-qcom (which is the only option supported on AX hardware).Another issue might be low RAM amount (initially wave2 drivers required 256MB, officially hAP ac2 has 128MB RAM) and some users noticed nasty memory leaks leading to device crashes. However these seem to be tied to certain device configuration (or configuration history) and it doesn't seem to happen to everybody.Personally, I did test it when 7.13 came out and was quite satisfied with performance ... until it (quite quickly) ran out of flash space (my device is also used as router and it had some extensive address lists). RAM was not a problem (my unit is one of the eraly ones which had 256MB RAM). ---

## Response 108
Uh, bad... I have public hotspots that route the traffic via VPN (Mullvad). That is does with routing rules, and fails to do so with RouterOS 7.17.1 - so all traffic goes via regular WAN.Currently I can not reproduce... Wondering if I tricked myself when I was connected a way I did not expect - will keep an eye on this. ---

## Response 109
But I am suffering another issue I think: The hotspot profile keeps adding "flash" to thehtml-directoryproperty, that causes my custom login page not being available. ---

## Response 110
*) bgp - improved stability;What does it mean exactly? What is the scenario that has been fixed?This ambiguity is extremely inadequate!It is a de-facto standard that every correction and improvement bring a reference to detailed case of issue and diagnostic. And I'm not talking about Opensource transparency.On telco routing/switching Juniper, Cisco, even Huawei and ZTE do that. On SOHO networking even D-Link and TP-Link have been doing it recently.Hey @normis and @EdPa, I bet no customer of MikroTik would be upset if you assume some compromise in bringing minimal references of what is being done on release notes. ---

## Response 111
Successfully upgrade main part of 2 RB5009 in prod to 7.17.1. ---

## Response 112
Thanks for feedback.There was a chance that route process crashed during "/routing/bgp/advertisements/print". Updated the changelog:*) bgp - improved system stability when printing BGP advertisements; ---

## Response 113
If I might suggest something: "fixed potential route process crash when printing BGP advertisements" would be much more useful to those reading changelog as well as those that experienced such behavior before. "System stability" is such a huge term that it basically means nothing, can be a crash but can also be reducing CPU or memory during printing that leads to overall better stability on lower end devices. ---

## Response 114
A have a CHRs only lab which was runs on 7.17beta2 fine. It has configured OSPFv2+v3, MPLS LDP dual-stack, BGP IPv4, IPv6, VPNv4, VPNv6, VPLS (both)Upgraded to 7.18beta2 and the IPv4 RIB issue (SUP-176975) happens. On 7.17beta4 the same. Something happens between 7.17beta2 and 7.17beta4 and a lot of another bad things happened between 7.16 and 7.17.7.17 is far from stable and from RC too in BGP aspect.I tested the lab after upgrade to 7.17.1, and it seems 7.17beta2 is moooore stable than 7.17.1. Till 7.17beta2, all of the above features works.On 7.17.1, if I enable any of L3VPN under BGP, autosupout.rif generated in that instant and IPv4 RIB vanished (except connected and static routes).
```
/routing bgp vpn
add disabled=yes export.redistribute=connected .route-targets=65530:1 import.route-targets=65530:1 .router-id=VRF_A label-allocation-policy=per-vrf name=bgp-mpls-vpn-1 \
    route-distinguisher=65530:1 vrf=VRF_A
add disabled=yes export.redistribute=connected .route-targets=65530:2 import.route-targets=65530:2 .router-id=VRF_B label-allocation-policy=per-prefix name=bgp-mpls-vpn-2 \
    route-distinguisher=65530:2 vrf=VRF_BAnother function which doesn't work is LDP signaled VPLS, if I understand MT documentation right. BGP signaled VPLS works.
```

```
/routing bgp vpls
add bridge=VPLS_A bridge-horizon=3 cisco-id=33.33.33.16 disabled=no export-route-targets=65530:3 import-route-targets=65530:3 name=VPLS_A pw-type=vpls rd=65530:3
add bridge=VPLS_B bridge-horizon=4 disabled=no export-route-targets=65530:4 import-route-targets=65530:4 name=VPLS_B pw-type=vpls rd=65530:4 site-id=16

[admin@rtr6.CPE] > /interface/vpls/print detail 
Flags: X - disabled, R - running; D - dynamic; B - bgp-signaled, C - cisco-bgp-signaled 
 0  D  name="vpls1" mtu=1500 mac-address=02:BA:62:00:0B:4B arp-timeout=auto peer=10.0.10.11 vpls-id="" pw-type=vpls bridge=VPLS_A bridge-horizon=3 bgp-vpls=VPLS_A 
       bgp-vpls-prfx="33.33.33.11&65530:3" 

 1  D  name="vpls2" mtu=1500 mac-address=02:5D:34:8F:DD:05 arp-timeout=auto peer=10.0.10.11 vpls-id="" pw-type=vpls bridge=VPLS_A bridge-horizon=3 bgp-vpls=VPLS_A 
       bgp-vpls-prfx="33.33.33.12&65530:3" 

 2  D  name="vpls3" mtu=1500 mac-address=02:F9:1A:DB:B4:F5 arp-timeout=auto peer=10.0.10.11 vpls-id="" pw-type=vpls bridge=VPLS_A bridge-horizon=3 bgp-vpls=VPLS_A 
       bgp-vpls-prfx="33.33.33.14&65530:3" 

 3  D  name="vpls4" mtu=1500 mac-address=02:E1:15:A7:BE:8E arp-timeout=auto peer=10.0.10.11 vpls-id="" pw-type=vpls bridge=VPLS_A bridge-horizon=3 bgp-vpls=VPLS_A 
       bgp-vpls-prfx="33.33.33.15&65530:3" 

 4  D  name="vpls5" mtu=1500 mac-address=02:B9:23:E7:E5:68 arp-timeout=auto peer=10.0.10.11 vpls-id="" pw-type=vpls bridge=VPLS_A bridge-horizon=3 bgp-vpls=VPLS_A 
       bgp-vpls-prfx="33.33.33.13&65530:3" 

 5 RD  name="vpls6" mtu=1500 mac-address=02:98:EA:AD:2C:87 arp-timeout=auto peer=10.0.10.11 pw-type=vpls pw-l2mtu=1500 pw-control-word=enabled bridge=VPLS_B bridge-horizon=4 bgp-vpls=VPLS_>
       bgp-vpls-prfx="veId=11,veBlockOffset=16&65530:4" 

 6 RD  name="vpls7" mtu=1500 mac-address=02:65:2B:31:40:F7 arp-timeout=auto peer=10.0.10.11 pw-type=vpls pw-l2mtu=1500 pw-control-word=enabled bridge=VPLS_B bridge-horizon=4 bgp-vpls=VPLS_>
       bgp-vpls-prfx="veId=12,veBlockOffset=16&65530:4" 

 7 RD  name="vpls8" mtu=1500 mac-address=02:29:76:7B:48:91 arp-timeout=auto peer=10.0.10.11 pw-type=vpls pw-l2mtu=1500 pw-control-word=enabled bridge=VPLS_B bridge-horizon=4 bgp-vpls=VPLS_>
       bgp-vpls-prfx="veId=14,veBlockOffset=16&65530:4" 

 8 RD  name="vpls9" mtu=1500 mac-address=02:4F:4A:8F:B7:23 arp-timeout=auto peer=10.0.10.11 pw-type=vpls pw-l2mtu=1500 pw-control-word=enabled bridge=VPLS_B bridge-horizon=4 bgp-vpls=VPLS_>
       bgp-vpls-prfx="veId=15,veBlockOffset=16&65530:4" 

 9 RD  name="vpls10" mtu=1500 mac-address=02:18:1A:D9:6B:CD arp-timeout=auto peer=10.0.10.11 pw-type=vpls pw-l2mtu=1500 pw-control-word=enabled bridge=VPLS_B bridge-horizon=4 
       bgp-vpls=VPLS_B bgp-vpls-prfx="veId=13,veBlockOffset=16&65530:4" 

[admin@rtr6.CPE] > /interface/vpls/monitor vpls1
  local-label: 5293                                              
     nexthops: { label=29; nh=10.0.6.1%ether1; interface=ether1 }

[admin@rtr6.CPE] > /interface/vpls/monitor vpls6
  remote-label: 32                                                
   local-label: 5288                                              
      nexthops: { label=29; nh=10.0.6.1%ether1; interface=ether1 }

[admin@rtr6.CPE] > /ip/address/print 
Columns: ADDRESS, NETWORK, INTERFACE
# ADDRESS        NETWORK     INTERFACE     
0 10.0.6.2/30    10.0.6.0    ether1        
1 10.0.10.16/32  10.0.10.16  Loopback0     
2 10.0.11.41/29  10.0.11.40  Loopback_VRF_A
3 10.0.12.41/29  10.0.12.40  Loopback_VRF_B
4 10.0.13.16/24  10.0.13.0   VPLS_A        
5 10.0.14.16/24  10.0.14.0   VPLS_B        
[admin@rtr6.CPE] > ping 10.0.13.11   
  SEQ HOST                                     SIZE TTL TIME       STATUS                                                                                                                    
    0 10.0.13.11                                                   timeout                                                                                                                   
    sent=1 received=0 packet-loss=100% 

[admin@rtr6.CPE] > ping 10.0.14.11 
  SEQ HOST                                     SIZE TTL TIME       STATUS                                                                                                                    
    0 10.0.14.11                                 56  64 4ms450us  
    1 10.0.14.11                                 56  64 1ms911us  
    sent=2 received=2 packet-loss=0% min-rtt=1ms911us avg-rtt=3ms180us max-rtt=4ms450us 

[admin@rtr6.CPE] >

---
```

## Response 115
Thanks for feedback.There was a chance that route process crashed during "/routing/bgp/advertisements/print". Updated the changelog:*) bgp - improved system stability when printing BGP advertisements;Ok that is nice, but I hope that the other BGP instabilities will also be fixed. At least now I know I do not have to try 7.17.1 for that.What I mean is:- sessions go to idle state and have to be re-established when ANOTHER session closes e.g. due to hold time exceeded or BFD reachability failed.- after some time, BGP prefixes are not accepted on sessions, received messages increases but prefixes count remains 0 and routes not in table.- and of course: prefixes are only sent by the receiving end of a session after one keepalive-time has elapsed. ---

## Response 116
I hope that the other BGP instabilities will also be fixed.- sessions go to idle state and have to be re-established when ANOTHER session closes e.g. due to hold time exceeded or BFD reachability failed.- after some time, BGP prefixes are not accepted on sessions, received messages increases but prefixes count remains 0 and routes not in table.- and of course: prefixes are only sent by the receiving end of a session after one keepalive-time has elapsed.Are there MikroTik jira support ticket numbers for those?Links to other references of that in forum?Could you share with us? ---

## Response 117
Yes, there is an open ticket. Useless to share it here because you cannot access that anyway.The ticket was made 23/Jul/24 but unfortunately after the usual "please send supout files when the problem occurs" (and doing that) there was no further progress. ---

## Response 118
...Like I'd really like to know where the "allowed-version" /system/device-mode comes from?
```
allowed-versions: 7.13+,6.49.8+That implies less than 7.13 has some vulnerability or otherwise flawed.  So should everyone upgrade to at least 7.13?Now for all we know they could have from @normis' cat too.  Thus the complaints.7.12 to 7.13 was the big wireless change, so might just be to prevent loosing wireless support on downgrade. Only MikroTik knows.

---
```

## Response 119
But I am suffering another issue I think: The hotspot profile keeps adding "flash" to thehtml-directoryproperty, that causes my custom login page not being available.Looks like this is already known.*) hotspot - fixed an issue where extra "flash/" is added to html-directory for devices with flash folders (introduced in v7.17);Time for 7.17.2... 😁 ---

## Response 120
The big problem of hAP ac2 and wifi-qcom-driver is lack of flash storage....wifi-qcom-ac drivers offer greatly improved throughputs and stability of wireless service...until it (quite quickly) ran out of flash space@mkx, would you mind creating a dedicated topic to discuss the points above outside this 7.17.x related one? ---

## Response 121
The big problem of hAP ac2 and wifi-qcom-driver is lack of flash storage.@mkx, would you mind creating a dedicated topic to discuss the points above outside this 7.17.x related one?Actually I do. My use case for my hAP ac2 doesn't require any wireless driver and it's not available for experimenting. Hence I'm not very interested in discussing this further. If somebody else starts new topic about this, I'll certainly follow discussion though. ---

## Response 122
Same disk space issue is with similar specs device Chateau LTE12#152.Discussions regarding disk space was already made in several topics when ROS 7.13 was introduced with new wifi drivers, disk space usage was reduced with 7.15 whenwifi-qcom-acpackage size was optimized and it was possible to use ROS with new wifi drivers on such devices, but from 7.17 ROS base package is increased and we are at beginning. ---

## Response 123
@optioSeems like you already had reduced free disk space on 7.16 already. I too have container+wifi-qcom-ac installed and about 200kb free on 7.17.1 (was 270kb on 7.17.0).seeviewtopic.php?t=213941#p1119443Unless you have stored some files/graphs on your flash, you can reclaim disk space by a netinstall with keep-configuration flag. Last time I did that at 7.15 IIRC and regained quite some space.But there is again a trend of shrinking free-space. ---

## Response 124
I know about netinstall disk space reclaim, doing that occasionally, but not sure how much it will help, I'm sure less than 100KB will be free. I did netinstall after reverting to 7.16 version, backup file was reduced about 40KB with same config for same ROS version. How large is you config file when is exported when performing/export show-sensitive file=export.rsc? My is 141.6KB (having lots of rules and scripts) and also having 3 certificates with keys added, no manually added files on flash, so even if I will have 40-50KB space left after netinstall 7.17 I'm worried about small amount of disk space growth per config chnage or even worse if is needed by VM swap file, if ROS uses it, which can lead to out of space eventually, see some discussion about it ->viewtopic.php?t=214312. ---

## Response 125
Does a netinstall with keep-configuration flag effectively to the same as an export to file, then reset-configuration with import from that file?Or is it more like the restore of a backup? ---

## Response 126
Reset config does not completely clean house.Netinstall does.Import from backup is a binary restore with all leftovers with it. ---

## Response 127
I always perform netinstall without config and restoring it from export to be sure that ROS is completely clean with my config. ---

## Response 128
Like I said, I (or MikroTik) would not have deleted it. It was a volunteer mod.IMO @normis is on the best path.What matters most is confidence and trust in the forum process. Forum moderation suggestions:do not delete bad posts; quote bad information in new post with correct informationleave bad topics open long enough for other concerned perspectives to emergeonce bad topics go quiet, make final locking topic post and lock the topicThe goal is a transparent audit trail doesn't leave much room for speculation or conspiracy theories. ---

## Response 129
Just downgraded to 7.17, lot of problem... need to identify and play on lab to understand what happen and be sure it .1 release and not any other stuff. ---

## Response 130
Like I said, I (or MikroTik) would not have deleted it. It was a volunteer mod.IMO @normis is on the best path.What matters most is confidence and trust in the forum process. Forum moderation suggestions:The goal is a transparent audit trail doesn't leave much room for speculation or conspiracy theories.For me the mistake was made by themoderatorwhoaccepted as the first postof this person yet another warning from the little green men with a clickbait title.If the user wants to report vulnerabilities, write to support, instead of publishing them in plain sight for anyone, so thatMikroTik can take action first.So dear moderators, STOP accepting certain first posts, as has happened several times in these weeks...What's the point of a moderator who accepts posts without eventhinkingabout the consequences?You might as well enable all new users to post anything right away.Since the "attacker authenticated as admin" problem will always exist on all operating systems that exist now and in the future, there should be a permanent CVE-UNIVERSAL grade 10 at this point, since the latest reported vulnerabilities are all "if you shoot yourself in the foot" type... ---

## Response 131
Another function which doesn't work is LDP signaled VPLS, if I understand MT documentation right. BGP signaled VPLS works.After testing it a little bit more, IPv4 and IPv6 do not works at all on LDP signaled VPLS. Over BGP signaled, IPv4 works, IPv6 doesn't.I replicated this CHR lab with some real MTik HW, both works the same, so support can't tell us its because of virtualization. ---

## Response 132
Anyone else having difficulty with Winbox connections to routers using internal ip addresses? The issue eemed to start this morning before updating to 7.17.1 but updating didn’t help. Mac os Winbox version 4 latest beta. thanks. ---

## Response 133
Possible bug?viewtopic.php?t=214376 ---

## Response 134
I was not able to upgrade an MLAG setup on two CRS312-4C+8XG switches successfully. Right after an upgrade it immediately caused a broadcast storm on MLAG bonding-interfaces which were connected to another Mikrotik appliances like CCR2116-12G-4S+ where bonding-interfaces were a slave ports in a switch-chip bridge. CCR2116 was already upgraded to the 7.17 version.Simpler two interface loops connected via a few same MSTP region Mikrotik switches also started to cause a broadcast storm and printed a multiple errors like these below:
```
combo2 excessive broadcasts/multicasts, probably a loop
combo2: bridge RX looped packet - MAC 48:a9:8a:be:de:b5 -> 33:33:00:00:00:01 VID 500 ETHERTYPE 0x86dd
combo2: bridge RX looped packet - MAC 48:a9:8a:be:de:b5 -> 33:33:00:00:00:01 VID 500 ETHERTYPE 0x86dd
combo2: bridge RX looped packet - MAC 48:a9:8a:be:de:b5 -> ff:ff:ff:ff:ff:ff VID 500 ETHERTYPE 0x0806
combo2: bridge RX looped packet - MAC 48:a9:8a:be:de:b5 -> ff:ff:ff:ff:ff:ff VID 500 ETHERTYPE 0x0806
combo2: bridge RX looped packet - MAC 48:a9:8a:be:de:b5 -> 33:33:00:00:00:01 VID 500 ETHERTYPE 0x86ddThankfully rolling back to the previous 7.16.2 version restored functionality of MLAG setup.Today I've checked versions 7.17.1 and 7.18beta4 and it didn't solved the issue with MLAG -SUP-177393.Problem with the CTSYNC on VRRP interfaces still exist. Everytime after the reboot you have to switch conntrack settings to make it work again -SUP-177488.
```

```
/ip firewall connection tracking
set enabled=auto
set enabled=yes

---
```

## Response 135
Have strange issue with Rose Storage on hap ax3.On version 7.17.1 have attached usb flash 8Gb with files. But after downgrade to 7.16.2 files are not seeing in Winbox - Files, usb1 folder is emplty and via FTP protocol is nothing. Before was using only FTP access with no problems.Tried Samba on win machine via explorer and files are recognised, dispaying and manageable.Do not want upgrade to latest stable again for now.What is could it be?
```
system/package/print 
Columns: NAME, VERSION, BUILD-TIME, SIZE
# NAME          VERSION  BUILD-TIME           SIZE     
0 wifi-qcom     7.16.2   2024-11-26 12:09:40  10.2MiB  
1 rose-storage  7.16.2   2024-11-26 12:09:40  3016.1KiB
2 routeros      7.16.2   2024-11-26 12:09:40  11.7MiB
```

```
disk/ print 
Flags: B - BLOCK-DEVICE; M - MOUNTED; m - MEDIA-SHARING
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS, RAID-MASTER
#     SLOT  MODEL                         SERIAL    INTERFACE                  SIZE           FREE  FS    RAID-MASTER
0 BMm usb2  JetFlash Mass Storage Device  1KRK9J0D  USB 2.00 480Mbps  8 032 092 160  4 585 451 520  ext4  none

---
```

## Response 136
I'm having an issue after upgrading. I'm getting a message under bridge vlan:
```
# duplicate vlan ids are not allowed due to interface list support, please merge vlan entries into oneI have eyeballed the config and don't see any duplicates.  Things seem to be working, but the message is concerning and it also smacks my hands any time I want to make any changes.
```

```
[admin@crs309] /interface/bridge/vlan> export compact 
# 2025-02-03 10:55:19 by RouterOS 7.17.1
# software id = ZBSD-VLT6
#
# model = CRS309-1G-8S+
# serial number = HG509ZJGZGZ
/interface bridge vlan
add bridge=bridge comment="public internet" tagged=sfp-sfpplus1,bridge,sfp-sfpplus7 vlan-ids=1000
add bridge=bridge tagged=bridge,sfp-sfpplus1,sfp-sfpplus7,sfp-sfpplus3 vlan-ids=911
# duplicate vlan ids are not allowed due to interface list support, please merge vlan entries into one
add bridge=bridge comment="trunk ports" tagged=sfp-sfpplus7,bridge,sfp-sfpplus1 vlan-ids=5-8,15,44,59,666
# duplicate vlan ids are not allowed due to interface list support, please merge vlan entries into one
add bridge=bridge comment="att wan" tagged=bridge,sfp-sfpplus1,sfp-sfpplus7,sfp-sfpplus5 vlan-ids=1001
add bridge=bridge comment="management vlan 2" tagged=bridge,sfp-sfpplus1,sfp-sfpplus7 untagged=sfp-sfpplus5 vlan-ids=2
add bridge=bridge comment="wifi vlan" tagged=sfp-sfpplus3 vlan-ids=5
[admin@crs309] /interface/bridge/vlan>

---
```

## Response 137
I'm having an issue after upgrading. I'm getting a message under bridge vlan:
```
# duplicate vlan ids are not allowed due to interface list support, please merge vlan entries into oneI have eyeballed the config and don't see any duplicates.  Things seem to be working, but the message is concerning and it also smacks my hands any time I want to make any changes.Any /interface/vlan interface that has its interface= set to a vlan-filtering=yes /interface/bridge, will "dynamically" get added to /interface/bridge/vlans with the bridge marked as a tagged= interface.  So a "/interface/bridge/vlan/print" would show the "D" mark ones with vlan-ids from the L3 VLAN interface.  Andlikelywhy your "static" config in ":export" it shows the comment since any vlan-id to VLAN that has a L3 interface is redundant config.  But it should be harmless AFAIK, as it's just ignoring the duplicate.Now the underlying issue is that automatic VLAN tagged=bridge behavior is NOT expressed in config, other than by that new comment to tell you about the situation - which does make folks now aware of the new 7.16 logic for bridged VLANs (which I think 7.17 add comment about it).   But dynamic config is never express in :export, so it is tricky problem if you're used to auditing VLANs via config....Anyway, I suspect a "/interface/bridge/vlan/print detail" would give you a fuller picture.

---
```

## Response 138
I'm having an issue after upgrading. I'm getting a message under bridge vlan:
```
# duplicate vlan ids are not allowed due to interface list support, please merge vlan entries into oneI have eyeballed the config and don't see any duplicates.  Things seem to be working, but the message is concerning and it also smacks my hands any time I want to make any changes.Any /interface/vlan interface that has its interface= set to a vlan-filtering=yes /interface/bridge, will "dynamically" get added to /interface/bridge/vlans with the bridge marked as a tagged= interface.  So a "/interface/bridge/vlan/print" would show the "D" mark ones with vlan-ids from the L3 VLAN interface.  Andlikelywhy your "static" config in ":export" it shows the comment since any vlan-id to VLAN that has a L3 interface is redundant config.  But it should be harmless AFAIK, as it's just ignoring the duplicate.Now the underlying issue is that automatic VLAN tagged=bridge behavior is NOT expressed in config, other than by that new comment to tell you about the situation - which does make folks now aware of the new 7.16 logic for bridged VLANs (which I think 7.17 add comment about it).   But dynamic config is never express in :export, so it is tricky problem if you're used to auditing VLANs via config....Anyway, I suspect a "/interface/bridge/vlan/print detail" would give you a fuller picture.I've been following the changes around automatically / dynamically tagging bridges, and dynamically adding untagged for bridge port pvid has been a thing for a while now, but in the past there was no issue being explicit with the config.
```

```
[admin@crs309] /interface/bridge/vlan> print                                         
Flags: D - DYNAMIC
Columns: BRIDGE, VLAN-IDS, CURRENT-TAGGED, CURRENT-UNTAGGED
#   BRIDGE  VLAN-IDS  CURRENT-TAGGED  CURRENT-UNTAGGED
;;; public internet
0   bridge  1000      bridge                          
                      sfp-sfpplus7                    
                      sfp-sfpplus1                    
1   bridge  911       bridge                          
                      sfp-sfpplus7                    
                      sfp-sfpplus3                    
                      sfp-sfpplus1                    
;;; duplicate vlan ids are not allowed due to interface list support, please merge vlan entries into one
;;; trunk ports
2   bridge  5-8       bridge                          
            15        sfp-sfpplus7                    
            44        sfp-sfpplus1                    
            59                                        
            666                                       
;;; duplicate vlan ids are not allowed due to interface list support, please merge vlan entries into one
;;; att wan
3   bridge  1001      bridge                          
                      sfp-sfpplus7                    
                      sfp-sfpplus5                    
                      sfp-sfpplus1                    
;;; management vlan 2
4   bridge  2         bridge          sfp-sfpplus5    
                      sfp-sfpplus7                    
                      sfp-sfpplus1                    
;;; wifi vlan
5   bridge  5         sfp-sfpplus3                    
;;; added by pvid
6 D bridge  1                         bridge          
                                      sfp-sfpplus7    
                                      sfp-sfpplus1    
;;; added by pvid
7 D bridge  6                         sfp-sfpplus3    
[admin@crs309] /interface/bridge/vlan>For instance, if I attempt to remove the bridge as a tagged interface from #2 above:
```

```
[admin@crs309] /interface/bridge/vlan> set tagged=sfp-sfpplus7,sfp-sfpplus1 numbers=2
failure: vlan already added
[admin@crs309] /interface/bridge/vlan>I can imagine no scenario where this isn't a RouterOS bug, and I'm pretty sure it was introduced with 7.17.1

---
```