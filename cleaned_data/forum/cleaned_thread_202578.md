# Thread Information
Title: Thread-202578
Section: RouterOS
Thread ID: 202578

# Discussion

## Initial Question
We made a table with some clarifications, can you guys let me know if this clears up some confusion? I see thatDocumentationandYouTube videostill leaves some questions unanswered. So let's try it like this:split2.jpg ---

## Response 1
at least for me this is fair enough ---

## Response 2
If any edge cases are missing in the table, let us know, and we will make the ULTIMATE guide for packages ---

## Response 3
i think Youtube video does a good job clarifying most of the situation.What happens is that it is a complicated turning point, not achievable on a videois not only the wireless matter, the reduced storage memory on some generation of devices, new generation of wireless devices, new operating system, 802.11ax etcwe can expect some friction, but is a necesary step to get back on track the wireless development ---

## Response 4
If any edge cases are missing in the table, let us know, and we will make the ULTIMATE guide for packagesThe unfortunate position of the RB4011iGS+5HacQ2HnD w.r.t. WiFi support could be clarified better. ---

## Response 5
Shame. From YT and press notes I was under impression that it will be possible to have wifiwave, legacy CAPsMAN and use onboard wifi interface ---

## Response 6
Shame. From YT and press notes I was under impression that it will be possible to have wifiwave, legacy CAPsMAN and use onboard wifi interfaceShame? On contrary, a respect for MikroTik. They did exactly the opposite of planned obsolescence.MikroTik brought new software to old 802.11ac ARM devices. Now you can have 802.11r/k/v seamless fast roaming, with one WiFi/WifiWave2 CAPsMAN, without a need to replace wAP ac or else devices. ---

## Response 7
If any edge cases are missing in the table, let us know, and we will make the ULTIMATE guide for packagesThe unfortunate position of the RB4011iGS+5HacQ2HnD w.r.t. WiFi support could be clarified better.Same here ... the Situation for the RB4011iGS+5HacQ2HnD is not 100% clear for mebr, Richard ---

## Response 8
Easy, like manual says RB4011iGS+5HacQ2HnD-IN (no support for the 2.4GHz interface). Installing the new driver will remove 2GHz, only 5GHz will work ---

## Response 9
plz dont forget the mipsbe with AC gear.... also need some tunning in drivers!!!! ---

## Response 10
plz dont forget the mipsbe with AC gear.... also need some tunning in drivers!!!!mipsbe devices' CPU is underpowered and hardly manages decent throughputs even with legacy wireless. New wave2/wifi is even more demanding on CPU (specially for memory). ---

## Response 11
Easy, like manual says RB4011iGS+5HacQ2HnD-IN (no support for the 2.4GHz interface). Installing the new driver will remove 2GHz, only 5GHz will workBut it is not in that table. It should be in that table, and also there should be a clear warning on the website.Remember this is not some old obsolete product. This is a product you are selling today, with this promotional sales pitch:RB4011 series - amazingly powerful routers with ten Gigabit ports, SFP+ 10Gbps interface and IPsec hardware acceleration for a great price!The RB4011 uses a quad core Cortex A15 CPU, same as in our carrier grade RB1100AHx4 unit. The unit is equipped with 1GB of RAM, can provide PoE output on port #10 and comes with a compact and professional looking solid metal enclosure in matte black.RB4011iGS+5HacQ2HnD-IN (WiFi model) is dual band, four chain unit with a supported data rate of up to 1733 Mbps in 5GHz. For legacy devices, the unit also has a dual chain 2GHz wireless card installed in miniPCI-e slot.Nowhere it is mentioned that it in reality is a dead-end product where you have to select between the old WiFi drivers or not having the 2GHz support. That only surfaces once you have bought it and dive into the details of the manual.But I have seen that before. I bought a CCR2004-16G-2S+ after reading on that same website that it has USB3, only to discover later that it comes without USB3. That false information has remained on the websites for months thereafter, and still is in the block diagram. Apparently correct information on the product website is not a very high priority.(just as there still are no separate performance figures for v6 and v7, or even specification under which version tests were done) ---

## Response 12
Table is about specific products, it is said above each table. Products not in the table - not supported. Think about it that way. I don't see RB133c either. What could it mean? ---

## Response 13
Perhaps the RB4011 deserves a footnote in the @normis table, given you lose 2.4Ghz with qcom-ac?Similar with Audience, it needs a footnote too. e.g. it's pitched as "meshable", but that requires manual configuration with qcom-ac to wireless "mesh". ---

## Response 14
According to the compatibility table RB4011 with wireless package in dual-capsman configuration internal WiFi interfaces with legacy drivers must work. But both internal wifi interfaces in cap mode can't connect to legacy CAPsMAN. Have tried with shared network interface and with dedicated pseudo-lo bridge:/caps-man manager interfaceset [ find default=yes ] forbid=yesadd disabled=no interface=vlan9 - Shared to both CAPsMANadd disabled=no interface=br-lo - Dedicated to "internal" 4011 CAPs/interface wireless capset bridge=bridge caps-man-addresses=192.168.255.1 discovery-interfaces=br-lo enabled=yes interfaces=wlan1, wlan2Logs show in any cases like that:13:44:30 caps, debug CAP Connect->Select13:44:30 caps, debug CAP did not find suitable CAPsMAN13:44:30 caps, debug CAP Select->Sulking13:44:34 ipsec, error payload missing: SA13:44:35 caps, debug CAP Sulking->Discover13:44:35 caps, debug CAP discovery target list:13:44:35 caps, debug ::ffff:192.168.255.1:524613:44:38 caps, debug CAP discovery over, results:13:44:38 caps, debug rt-core (::ffff:192.168.255.1:5246)13:44:38 caps, debug CAP Discover->Select13:44:38 caps, info CAP selected CAPsMAN rt-core (::ffff:192.168.255.1:5246)13:44:38 caps, debug CAP Select->Connect13:44:46 caps, info 44:AF:28:2D:A5:32@ap-3 reassociating13:44:46 caps, debug 44:AF:28:2D:A5:32@ap-3 connected, signal strength -6613:44:58 caps, info CAP connect to rt-core (::ffff:192.168.255.1:5246) failed: timeout13:44:58 caps, info CAP failed to join rt-core (::ffff:192.168.255.1:5246)Any "external" devices work with both CAPsMAN successfully. ---

## Response 15
One suggestionPost what driver is needed on device page.It will be easier ---

## Response 16
Suggestion: we the MikroTik user base, need an abstraction. You know the hardware. Let us learn the software. By mixing everything it is really getting confusing. I think a better approach is needed. A single abstraction layer that figures it all out for us. As users we just implement generic WiFi concepts.So, one wifi menu for all hardware. One Capsman menu for all hardware. The software does the right thing. ---

## Response 17
Legacy wireless config is so much different in some places. So it would take an extra effort for MT developers to get an abstraction right. They would need to expose different config options depending on hardware and installed wireless/wifi package. Look at all these nv2/ and all the other massive wireless options (base rates, ampdu, etc ) in legacy driver and the much less, different and non-compatible QCOM driver options. Kind of silly in my eyes to move that in one config section. I am sure MT thought about it, but decided against. ---

## Response 18
plz dont forget the mipsbe with AC gear.... also need some tunning in drivers!!!!mipsbe devices' CPU is underpowered and hardly manages decent throughputs even with legacy wireless. New wave2/wifi is even more demanding on CPU (specially for memory).Actually, I would love to have my "wAP ac/hAP ac" devices managed by the same CAPsMAN and have roaming support even at the price of the lower throughput and higher CPU/RAM utilization, if possible in any way. Most times, wifi is not used to the max, but it is important just to have a connection - messengers, e-mail, reading (yes, some of us don't care about videos).So, if possible in any way, please make mipsbe devices compatible with new CAPsMAN. It would be fine if you have to remove all the other unnecessary stuff from them, like VPNs (all of them), everything from Tools menu, just make them simple CAPs...I know this won't happen, but if you don't ask.... ---

## Response 19
I think the issue is that CAPsMAN is not really a management layer for an abstracted WiFi device, but just a tool to copy a block of configuration data from the local device to the managed devices. That is why you also need to install the WiFi drivers on the CAPsMAN management device, even when it is not running WiFi at all.With the new drivers, the configuration block structure is completely different, and everything had to be replaced with a new version.So there is no chance of the new version managing old devices. When that would have been practical, they could have done it already.I am running a managed WiFi system from a similar company (the one named U*) and there it has been done differently. The management software manages devices of different generations and chip manufacturers. The configuration data is distributed as JSON files with generic parameters and their values. Each device receives its properly prepared JSON file (from the settings you made on the controller) and configures accordingly.But the whole thing is much "heavier" than the MikroTik solution! The controller is a Java application that becomes larger all the time, I run it on a virtual machine with several GB of disk and main memory. That manufacturer originally supplied a small Raspberry Pi 1 like device that could run the controller, but over time it became more overburdened with it and it now no longer works, you need a new more powerful device (more memory, faster CPU).The wireless APs also are much beefier than typical MikroTik units, with the associated price. MikroTik has clung to their 16MB flash while these APs had 256MB or 512MB flash for a long time. So lots more space for nifty data-conversion agents on both sides.So no, I don't think this is going to happen. Unless MikroTik makes that proposed "controller application" (which would be running on a powerful device) working at some time. Seeviewtopic.php?t=186352But I would not hold my breath... ---

## Response 20
...So there is no chance of the new version managing old devices. When that would have been practical, they could have done it already....But I would not hold my breath...They said that hap ac2 won't ever get WifiWave2, and there we have it, and it is working great. So maybe, just maybe, Mikrotik could give us another surprise and enable new Capsman on mipsbe devices, at least ones with enough memory (like mipsbe based wAP ac?).Not holding my breath either ---

## Response 21
Easy, like manual says RB4011iGS+5HacQ2HnD-IN (no support for the 2.4GHz interface). Installing the new driver will remove 2GHz, only 5GHz will workI checked the product page:https://mikrotik.com/product/rb4011igs_5hacq2hnd_inand the manuals there have no mention of this limitation. It would be fair to at least mention this on the product page.It's a pity for all of us who bought this model as "powerful enough to be future-proof for at least a few years" and now it's declared obsolete ---

## Response 22
It's not obsolete at all.It's your choice to use the wave2 package with its limitations or not.The fact 2GHz radio is not usable anymore when you use wave2 drivers on RB4011 is already known for almost 2 years since 7.1 came out. ---

## Response 23
It would be great if you can help to splitwifi-qcom-acin 2 packages, only one IPQ4019 or QCA9984 driver ?Due to hap ac2 has space limit while upgrade to this version with zerotier package space need another 117 kB more, log are said like thatThis split may help to fixed this issue, as we can reduce size of package.If it can solve space problem this must be great support.Thank you very much ---

## Response 24
The fact 2GHz radio is not usable anymore when you use wave2 drivers on RB4011 is already known for almost 2 years since 7.1 came out.It has been a problem for two years, yes. But there is no explanation why this problem even exists. In any other Linux system you can separately install drivers for each device without having such conflicts. When you have more than one driver that would support a certain chip, there would be a way to work around that by having the drivers detect their hardware in a certain sequence.(so wifi-qcom would pickup the 5 GHz device and wireless would pickup the 2 GHz device, and find the 5 GHz device already supported by wifi-qcom so it would not bother with that)I would have expected that now that you can have BOTH management menus available at the same time, you would be able to do this on a RB4011. ---

## Response 25
Let's not forget, ROS is, while based on it, not as flexible as Linux.I think the base problem on RB4011 is effectively that there are 2 different chipsets used, one for each of the radio bands and somehow ROS is only able to use 1 driver: either legacy, either wave2. But not both.However, that's pure speculation from my side. ---

## Response 26
It's a pity for all of us who bought this model as "powerful enough to be future-proof for at least a few years" and now it's declared obsoleteThe device isn't obsolete, 2.4GHz Wifi is obsolete. ---

## Response 27
Certainly not !2.4GHz spectrum is crowded (definitely !) but far from obsolete.There are still appliances being brought to market today only having 2.4GHz capability.Floppy disks are obsolete although I HAVE seen a setup some months ago where they still used 3.5" floppies ...nostalgic feelings ! ---

## Response 28
I would have expected that now that you can have BOTH management menus available at the same time, you would be able to do this on a RB4011.I assume their legacy wireless is not just a driver alone. possibly the legacy wireless has interaction with several system modules (routing/firewall) and makes it impossible to have new/legacy running same time. ---

## Response 29
The page shows that "New Capsman only controller" needs "routeros" only, while the video "https://www.youtube.com/watch?v=AkBIQxi-VKs" shows that "Package since 7.13" for "CAPsMAN for up to WiFi5 APs" is "routeos+wireless". Which one is correct? ---

## Response 30
Because you are quoting "new capsman ONLY", but video talks about old WiFi5 devices, which in the table is "running two capsmans at the same time" (old + new) ---

## Response 31
The page shows that "New Capsman only controller" needs "routeros" only, while the video "https://www.youtube.com/watch?v=AkBIQxi-VKs" shows that "Package since 7.13" for "CAPsMAN for up to WiFi5 APs" is "routeos+wireless". Which one is correct?For using the old CAPsMAN, the (additional) wireless package is required.The new CAPsMAN is part of the routeros package, this new CAPsMAN version can be used for managing the wifi-qcom (all ax devices) and wifi-qcom-ac (supported ac devices) packages. ---

## Response 32
Because you are quoting "new capsman ONLY", but video talks about old WiFi5 devices, which in the table is "running two capsmans at the same time" (old + new)In other words, a switch like CRS326-24G-2S+IN that acts as new capsman only just needs routeos 7.13 without package "wifi". On the other hand, an AP like RBwAPG-5HacD2HnD that supports new wifi just needs routeos 7.13 with package "wifi-qcom-ac". Is it correct? ---

## Response 33
Correct. ---

## Response 34
Correct.There seems something wrong. I set AP managed by CAPs but CAPs can't find AP's wifi interface. Any advice? Thanks. ---

## Response 35
Read the table again ---

## Response 36
Read the table againYes, I read it again. My AP runs with routreos + wifi-qcom-ac and is waiting for capsman's control. My switch acts as new capsman with routeros but cannot find AP's wifi interface. Because the table does not mention the switch device but wifi device only, I am not sure whether my switch needs wifi-qcom-ac or I neglect something else.Any hint would be appreciated. ---

## Response 37
If they are on the same network, the CAP's should be able to find the CAPsMAN.Have you seen this part:https://help.mikrotik.com/docs/display/ ... ionexample:It requires an edit on the default CAPs mode.Or as an alternative, share the config of both CAPsMAN and CAP:
```
/export file=anynameyoulikeRemove serial and any other private information en post the output in between code tags by using the </> button.

---
```

## Response 38
If they are on the same network, the CAP's should be able to find the CAPsMAN.Have you seen this part:https://help.mikrotik.com/docs/display/ ... ionexample:It requires an edit on the default CAPs mode.Or as an alternative, share the config of both CAPsMAN and CAP:
```
/export file=anynameyoulikeRemove serial and any other private information en post the output in between code tags by using the </> button.Eventually new caps works. Now the way  to putting AP under new CAPMAN's control is the following 3 steps on AP. No1. WiFi--WiFi--CAP-Enable; No2. Configuration--create New WiFi Configuration--Configuration--Manager--capsman; No3. Apply configuration to WiFi interface.

---
```

## Response 39
According to the table RB4011iGS+5HacQ2HnD should run dual capsman using `routeros+wireless` package. Hereviewtopic.php?t=202640people are struggling to have it running. Looks like CAPsMANs are conflicting each-other. Can we get a clear statement if it stable and possible at all for the particular product?Any hint for a proper setup? it should not come to a hint game. ---

## Response 40
It's not obsolete at all.It's your choice to use the wave2 package with its limitations or not.If all other currently sold top-tier devices support it and one model support is dropped for "new" drivers and if you want the feature that all others have, you have to use "legacy" drivers that will lack new functionality, then it is fully qualified for this label.The fact 2GHz radio is not usable anymore when you use wave2 drivers on RB4011 is already known for almost 2 years since 7.1 came out.Then why it is not stated in the product specifications? There might be rational reasons for this decision, no doubt, but I would think twice about buying this model under such circumstances."It is already known" means "if you dig long and deep enough into this forum, you'll eventually find it". I kinda relied on the fact, that old RB devices did not lose that much functionality when you want to use new features. Until now, I supposeNever mind, there is no point in complaining here. It's just a highly disappointing experience. ---

## Response 41
RB4011 comes with wireless functionality enabled out of the box. You can simply use it as it is. But Changing package to another one is optional and at your own risk. It is in the documentation that RB4011 is not compatiblehttps://help.mikrotik.com/docs/display/ ... patibility ---

## Response 42
It is mentioned deep down in the documentation, but NOT on the product specification sheet, where this of course belongs.Just like there is:Note: Passive DAC (MikroTik S+DA0001/S+DA0003) are not supported.on the product page, there should also be:Note: the new WiFi drivers are not supported.Even when you decide to keep using it as-is, updating past 7.12.1 causes issues.Because you added another WiFi menu and moved menus around, winbox does not correctly save/restore window information anymore.Please give us the option to upgrade software on RB4011 and keep everything as it is, including not introducing code for wireless devices that is not supported on this model.(i.e. move WiFi menu into the qcom-ac packages, where it belongs) ---

## Response 43
Like I said, the product comes preinstalled with a working wireless package and there is no reason to change it to anotherone. If YOU decided to do this, it's in the manual, but it is not an advertised feature for this model. Does a BMW come with a specification note that engine from diesel to gasoline can't be changed? ---

## Response 44
Do you even READ what is written?Again: when an RB4011 (or any device) is upgraded from 7.12.1 to 7.13, an unusable WiFi menu is added.This takes up space on the device (a real problem on e.g. the hAP ac2!!!) and also it causes winbox to fail saving sessions.Reported before.So to be clear again: this happens when NOT opting to install the new driver. ---

## Response 45
when an RB4011 (or any device) is upgraded from 7.12.1 to 7.13, an unusable WiFi menu is added.It's not unusable, it is required for managing ax devices via capsman. ---

## Response 46
Normis wrote that the new driver is not supported on the RB4011. So it is unusable.When there is some specific use for it, move it into an optional package so those that need it can install that.While those that do not need it can continue to use their device as it was sold. ---

## Response 47
Normis wrote that the new driver is not supported on the RB4011. So it is unusable.Capsman for managing qcom-ac/qcom devices is possible even without installing any qcom-* package at all. So basically any ROS-device 7.13+ can be capsman for devices that are using new drivers.So not unusable - but bloat for many users. ---

## Response 48
Do you even READ what is written?Again: when an RB4011 (or any device) is upgraded from 7.12.1 to 7.13, an unusable WiFi menu is added.This takes up space on the device (a real problem on e.g. the hAP ac2!!!) and also it causes winbox to fail saving sessions.Reported before.So to be clear again: this happens when NOT opting to install the new driver.Agree, maybe it's not so extra space but as useless WiFi section appearing, there is no need to display section for package that is not installed. Also in iOS mobile app wireless section is missing even when wireless package is installed (WiFi is there as useless section). ---

## Response 49
Well, on the hAP ac2 the extra space is a real issue, because despite being advertised as "16MB flash" in reality it has only 15.3MB flash, and the code for ARM is also bigger than for MIPSBE. So a hAP ac2 with 7.13 (with wireless package) is filled to the brim and fails once you configure a lot of features or maybe had it originally running v6 (so the v6 config is still on the device).My hAP ac2 running 7.12.1 and configured only as a WiFi AP in bridge mode already has only 1MB of space left.I don't understand why the base config code for WiFi is in the routeros package, while the wireless package again has its own base config code for the classic driver... the config code for the new drivers should be in qcom-ac* or in a wifi package, so that you will not install it when using the classic drivers. ---

## Response 50
the config code for the new drivers should be in qcom-ac* or in a wifi package, so that you will not install it when using the classic drivers.The configuration and common parts should belong to a separate package called something like "qcom-common" or alike. So one can still install/have the capsman for qcom-ac/qcom on e.g. RB5009 - but without the wifi device drivers that would be completely useless on a RB5009. Would be even worse, when the config-code would be part of qcom-ac/qcom packages. ---

## Response 51
Again: when an RB4011 (or any device) is upgraded from 7.12.1 to 7.13, an unusable WiFi menu is added.This takes up space on the device (a real problem on e.g. the hAP ac2!!!)WiFi menu is usable to manage CAPsMAN. You can ignore it, just like you can ignore BGP menu, SNMP menu and others.And so the RB4011 issus is most problematic on hAP ac2 ? ---

## Response 52
Again: when an RB4011 (or any device) is upgraded from 7.12.1 to 7.13, an unusable WiFi menu is added.This takes up space on the device (a real problem on e.g. the hAP ac2!!!)WiFi menu is usable to manage CAPsMAN. You can ignore it, just like you can ignore BGP menu, SNMP menu and others.Unfortunately, no. I have a winbox session open to my devices all the time and I have saved the windows/tabs/columns I want to be open as a session.With the new situation there are 2 different wireless windows and winbox confuses them (just like the user).When I close winbox with the old-style wireless window open on the RB4011 or hAP ac2, and then re-open it again, it does open the new WIFi window instead of the old one, it opens the wrong tab as well (I normally have it on "registration").Then when I close that window and re-open the original wireless window, all my saved column selections and widths are gone.I do not consider that "you can just ignore it". It is a loss of function.And so the RB4011 issus is most problematic on hAP ac2 ?The hAP ac2 (which I also have) is most affected by the lack of storage, the RB4011 of course is not.But the problem mentioned above occurs on both models! ---

## Response 53
Again: when an RB4011 (or any device) is upgraded from 7.12.1 to 7.13, an unusable WiFi menu is added.This takes up space on the device (a real problem on e.g. the hAP ac2!!!)WiFi menu is usable to manage CAPsMAN. You can ignore it, just like you can ignore BGP menu, SNMP menu and others.And so the RB4011 issus is most problematic on hAP ac2 ?The whole idea behind, is that a number of customers want NOT to ignore it, but rather USE it managing both old CAPs and internal wifi and AX CAPs.TLDR: it does not work. Please pay more attention in testing the solution i.e. "Dual capsman" or do not announce it, if it is not stable.The "feature" is really nice for transition but please educate either publishing the HOW-TO or any documentation for proper setup since it is problematic. ---

## Response 54
What about 60GHZ product like Wap 60G?If i upgrade to 7.13+ i see both Wifi and wireless, i takes more space on the device and it doesnt let me install our branding packages anymore due to spaceas far as i can see, i cant uninstall the Wifi part, and if i uninstall the wireless part, it frees up space but i lose the W60 interfaces...What is the sollution here?for now the only thing i could do is downgrade with a lot of hassle to 7.12.1 and install the brandingafter that, i cant upgrade to 7.13+ because space is an issueFYI, my branding package is 893kB ---

## Response 55
What is the sollution here?The solution is to stay at 7.12.1 and pray that MT will manage to get space problems under control. ---

## Response 56
Yes, I hope that MikroTik consider to promote 7.12.1 to "long-term" and apply possible security fixes in the future.The 7.13+ versions have those issues and it looks like it is going to take time to iron them out, in the meantime "we" want to have a version we can keep running in production situations. ---

## Response 57
What is the sollution here?The solution is to stay at 7.12.1 and pray that MT will manage to get space problems under control.Jip, that is what im going to do as for now.To bad they implement things not designed for the device it will run on. like wifiwave2 wifi menu on 60GHz devices..... i dont see the point in hat oneFYI, i have the same issue on hap ac2 devices. ---

## Response 58
The solution is to stay at 7.12.1 and pray that MT will manage to get space problems under control.Jip, that is what im going to do as for now.To bad they implement things not designed for the device it will run on. like wifiwave2 wifi menu on 60GHz devices..... i dont see the point in hat oneRight or wrong. Their logic is any device can an be a Wi-Ficontroller, even if it does not have 802.11 hardware.One option is you can use webfig to create a skin to remove the Wi-Fi menu and assign the skin to your user account. Skins also apply to winbox too, even though you have to create/edit them in webfig. ---

## Response 59
+1For a long term stable Vers 7.12.1 variant! ---

## Response 60
+1 For a long term stable Vers 7.12.1 variant!+1 ---

## Response 61
Mentioned long term in release topicviewtopic.php?t=202423#p1042578but no response... Maybe it should be replied to thisviewtopic.php?t=201378#p1035120 ---

## Response 62
Do you even READ what is written?Again: when an RB4011 (or any device) is upgraded from 7.12.1 to 7.13, an unusable WiFi menu is added.This takes up space on the device (a real problem on e.g. the hAP ac2!!!) and also it causes winbox to fail saving sessions.Reported before.So to be clear again: this happens when NOT opting to install the new driver.Agree, maybe it's not so extra space but as useless WiFi section appearing, there is no need to display section for package that is not installed. Also in iOS mobile app wireless section is missing even when wireless package is installed (WiFi is there as useless section).Same here with missing wireless tab in the mobile app, I have both CAPsMAN versions running on the RB750Gr3, but only wifi is visible in the mobile app, also old CAPsMAN devices are missing from the interfaces. Any clue? ---

## Response 63
only wifi is visible in the mobile app, also old CAPsMAN devices are missing from the interfaces. Any clue?There have been complaints about the iOS mobile app in another thread, see...viewtopic.php?t=203149On top of top wlanX not showing up in the Advanced menus. Even without CAPsMAN running, it does NOT let you set the wireless SSID or password from the Home Screen, which is the end-user way of changing them using the app. ---

## Response 64
In the end I don't understand this package-approach at all.Just build a main-package for each ARM device!So we don't have to mess around with wifi packages and confuse users.Device: D53G-5HacD2HnD- Main package with Legacy Wireless- Main package with Qcom driversNo package manager overhead. No other overhead. No confusion. Easy to switch between "editions". Just drop the according NPK and reboot. done. No need to mess around with wireless package and - do I need wifi-wcom-ac or do I need wifi-qcom? And where is all my free space gone???? ---

## Response 65
Yes, a bit more RAM usage for larger npk (Qcom ax+ac), but it I think all devices should be able to handle that, it will be more cleaner process for upgrade. Upgrade process should be able to detect which drivers you need for device and install them. ---

## Response 66
So we don't have to mess around with wifi packages and confuse users.If you just follow /system/package/upgrade...theoretically, all should work fine & if not, it's a bug IMO. It's only when you want to use the "new drivers" on an old device that take messing with packages. But foisting the wifi-qcom-ac drivers would be a bad idea in same cases since not all features map perfectly... so could break an upgrade in some case (beyond just disk space).But packages are avoidable. And the issue is disk space. Most folks don't need TR069, calea, etc... but some do. And monolithic package with all features possible won't fit in 16MB flash devices... So issue comes up say you TR069 to setup a zerotier-enabled IoT gateway but don't need BGP/OSPF & other wacky combo since Mikrotik are used in a lot application outside someone home. ---

## Response 67
Suggestion is to have 2 packages, Legacy and Qcom, not forcing new Qcom drivers. Qcom bundle can contain ax+ac drivers and upgrade process can install drivers only needed for device, device will not have both ax and ac drivers on flash storage if upgrade process is a bit "smarter". ---

## Response 68
Personally, all care about is the packages I used before still fit.The "how" is kinda less important – but moving to "more monolithic" doesn't seem like the right direction, but maybe.One benefit with the wireless/qcom being seperate in 7.13+, is it allows wi-fi to be remove if it's not needed in an install...Now... still think it's just lousy UX using files to manage packages... when the extra-package are well-known & there are multiple GUIs to configure RouterOS for some "checkbox" for features(/packages).The recent MT newsletter suggests there still releasing 16MB flash units – which is "good news" IMO since there committing to managing in 16MB. ---

## Response 69
Problem is that npk install script is dumb copy all files process from package to ROS fs location, when having all Qcom drivers in single package it will need to first check device peripherals and copy only needed driver files (it will be the same at the end like installing ac or ax separately), in this case user will not be bothered to check if he needs ax or ac drivers, even it is not so complicated but for some it seems it is. ---

## Response 70
is dumbIf I worked at MikroTik as a programmer the problem would have already been solved, in fact, it probably would never have been created, because I would have done everything in a more logical way:you only download the drivers (and optional features) you need based on the model, without downloading and installing too many things.If I had been the hardware manager then I would have put 1GiB chips everywhere, rather than continuing to use chips from paleolithic.I'm sorry to all of you, but I am neither one of their programmers, nor their hardware manager. ---

## Response 71
The problem is that MT (especially Normis position on that) declines "more granular" package splits so we can reduce flash-usage as much as possible.Every few days a new forum topic is created where a confused user is puzzled by 7.13. It is very unclear for the regular user to understand this "split" and the difference between "wireless" and "wifi". Not mentioning the topics recently about the free flash space and users cant fit zerotier package anymore and so on.So what I proposed:Keep running systems untouched. The default "MAIN PACKAGE" should have remained the same as it was until 7.12. A MAIN PACKAGE with LEGACY WIRELESS. Continuing to work as before. Same flash size usage. Same ALL.Then introduce a "per device" built "MAIN PACKAGE". So everyone who wants wave2 is now able to OPT-IN and use the "device specific" MAIN PACKAGE instead. It would contain the new QCOM drives for the specific device and necessary other stuff. Not more, not less. I am pretty sure this approach would result in a very tight/optimized MAIN PACKAGE and we could regain a notable amount of space on all the ARM 16MB platforms. ---

## Response 72
@infaboWe have no guarantee that the staff who PROGRAM RouterOS will ignore our comments.Probably our reports and proposals on the forum are not even passed on to the programmers, just because those of the staff who read the forum do not consider them worthy of note.Like this:viewtopic.php?t=198641#p1022672On 7.13.3 still exist that line... ---

## Response 73
---

## Response 74
Update 9 inviewtopic.php?p=1054314#p1054314This raises questions of business continuity.Moving from /interface/wireless ("wireless") to /interface/wifi ("wifi-qcom" and "wifi-qcom-ac") may cause service interrruption.If you have a mixed bag of devices, some 802.11ac other 802.11ax, then you need wifi-qcom on the CAPsMAN, wifi-qcom on the 802.11ax CAPs and wifi-qcom-ac on the 802.11ac CAPs. Since CAPsMAN does not manage packages in CAPs, you have to do it yourself.Assuming your devices have "wireless" installed, what happens if you install "wifi-qcom"?We already know that "wireless" will be automatically disabled.Are the /interface/wireless settings automatically ported to /interface/wifi to prevent service interruption?Users would have preferred to have everything in "wireless". ---

## Response 75
We made a table with some clarifications, can you guys let me know if this clears up some confusion? I see thatDocumentationandYouTube videostill leaves some questions unanswered. So let's try it like this:split2.jpgCan you split base package even more? Please make VPN functionality as separate optional package. Media/DLNA separated package. Possibly even more so we can install it without problem on hAP ac2 without problem with disk size. Thank you. ---

## Response 76
Well, on the hAP ac2 the extra space is a real issue, because despite being advertised as "16MB flash" in reality it has only 15.3MB flash, and the code for ARM is also bigger than for MIPSBE. So a hAP ac2 with 7.13 (with wireless package) is filled to the brim and fails once you configure a lot of features or maybe had it originally running v6 (so the v6 config is still on the device).Yup, same "space" issue here.I was running 7.13 (routeros+wireless package) and barely had enough room to create a backup (running config) file to the flash drive.RouterOS + wireless package and 1 backup-ed config file left me with 1% free space (14.9MB of 15.3MB used).I was hoping 7.14 would have a little more space left, but it turns out that upgrading to 7.14 bricked my hAP ac2's altogether.After many failed tries with Netinstall (confirmed bug), I finally managed to get 7.13 back on both devices.See:viewtopic.php?t=205614Mikrotik support suggests upgrading to 7.14.1, but those packages are exactly the same size as 7.14. So I don't think this will solve the space issue.So basically, installing thewifi-qcom-acpackage on the hAP ac2 isn't even an option, because it's even bigger than the older wireless package.wireless: 2.64 MBwifi-qcom-ac: 2.85 MBWhich leaves no room for a config backup file. ---

## Response 77
I was running 7.13 (routeros+wireless package) and barely had enough room to create a backup (running config) file to the flash drive.Well, you are not supposed to create a backup to the flash drive!In those 16MB devices the Files section points to a RAM disk and flash is a subdirectory of that (where space on flash is mounted).You should make your backup in the root directory and then download the file to another device.That is required anyway to be able to recover it when the device crashes.(make both a /system/backup/save and a /export show-sensitive) ---

## Response 78
Well, you are not supposed to create a backup to the flash drive!In those 16MB devices the Files section points to a RAM disk and flash is a subdirectory of that (where space on flash is mounted).You should make your backup in the root directory and then download the file to another device.Not sure what you mean by this.I always log into my routers with Winbox, then go toFilesand hit the "Backup" option.I enter the filename and voila... the config backup file is created.I then download the file to my local machine from within the sameFilesmenuSo if this is not the way to create a backup, why is this option there?And regardless of where I store this file, it will take up space from the 16MB.Whether it's on the RAM disk, or in a sub-directory (flash) on the same disk.Or am I missing something here? ---

## Response 79
We made a table with some clarifications, can you guys let me know if this clears up some confusion? I see thatDocumentationandYouTube videostill leaves some questions unanswered. So let's try it like this:Sorry I'm very new forgive me if this chart explains it, but if i go to the suppot & downloads page under the model to me which seems very generalized to mikrotik software and not the device i'm using. How do I know that my device can use the latest software? Do i need to download both the routeros-7.15.1-mipsbe.npk and the wireless-7.15.1-mipsbe.npk, and then also i seen certain device have a boot that needs to be updated too..does that need to be updated everytime a new software is released? Also what are the steps i need to take to backup everything to prepare for the software upgrade, seem that the backup option is just for the configuration and nothing eles? Im surprised that someone hasn't made a sticky about the backup process for beginers already! ---

## Response 80
As an end user you only need to do this:- upgrade the router to 7.12.1 via system->packages->upgrade when it has lower than that version- (reboot, that installs the upgrade)- upgrade the router to 7.15.1 via system->packages->upgradeThe router itself will automatically download the required packages and there is no need to download anything manually.The logic to select the correct packages is not present in versions before 7.12 so that is why you have to upgrade with that version as an intermediate step. ---

## Response 81
well thats great when it works.... but that only answers if i want to auto update... it doesn't answer my other questions! ---

## Response 82
You did not tell us what device you have, and the answer depends on that.When you have a minimal device, there is little more that you can do than take a backup (both a .backup and a .rsc), and make sure you have the netinstall and image of the existing version available offline in case you need it.With a higher-end device, with sufficient flash memory, you can partition it and save your entire install on the router in the second partition and switch to it when the upgrade is not a success.I do that all the time, on devices like RB4011, RB5900, CCRxxxx, etc."a boot that needs to be updated", well the opinions on that differ.Some people (including MikroTik personnel) claim it isn't necessary to update boot, but unfortunately they have tied the boot version number to the RouterOS version number some time ago, so you really cannot know if there are changes between the boot you have on the device and the one in the RouterOS image, other than the version number.(before, the boot would have a version like 3.41 and when you upgraded RouterOS to like 6.11 it still showed the same boot version and no need to upgrade. however, they were apparently annoyed that people answered "3.41" when asked for the RouterOS version, which was in the 6.xx range then, so they thought it was a good idea to change that. I would have changed it to like boot3.41) ---

## Response 83
So there is no chart that details the mikrotik devices model numbers and the current software compatible with or which version you should use for the device? It was a good thing you mention about upgrading to 7.12.1, the device that im working with is a RB2011UiAS-2HnD-IN using not by my choice 6.37.3. Im just not sure if there is something wrong with the setup of the device but it wouldn't check for upgrades complaining about dns and the wireless wasn't working. so I was going to update to the lates software but then I got confused if I need to backup the config and packages/files, then if I need the routeros-7.15.1-mipsbe.npk and/or the wireless-7.15.1-mipsbe.npk. When you click the RouterOS current release download from the products discontinued page both of those versions appear, then with the product being discontinued if it even supported the latest version or if I needed to update boot?. ---

## Response 84
With that particular router it is possible to partition it.First check that you have less than about 40MB of flash in use, then go to partition menu, "repartition" to 2 partitions, router will reboot, then you can again go to "partition", select part0, do "copy to" part1, and you have saved everything on your router.Now when you do upgrades you can always go back to "partition", select part1, click "make active" and reboot, it will reboot the old situation (routeros and config).Anyway, to upgrade that router all the way from 6.37.3 to 7.15.1 is very likely going to fail.At minimum, you first need to upgrade to 6.49.15, then to 7.12.1, and finally to 7.15.1.But as there apparently already are configuration issues, I would recommend to just netinstall 7.15.1 and start configuring completely from scratch.(depending on what the config is now. when it is "just a home NAT router" that is easy, when it has special config on it there could be more involved)The first thing to do would be open a terminal, do "/export file=config", go to files and download "config.rsc" to your computer, and open it in a text editor, print it, whatever, to see what is in there. ---

## Response 85
I did the do command but it isnt showing in files, how do i list the files and directories and move within them? ---

## Response 86
You will see the file when you used the export command correctly. ---

## Response 87
yeah I did that do "/export file=config", with and without the quotes but nothing shows up! For some reason i dont think its going to the right directory! Im using winbox terminal! ---

## Response 88
Well, of course it should be without the quotes and you should hit ENTER after it.And there should not be an error message.Anyway, do you have any special requirements and configuration or is it just your home router for an ISP?If so, check if you have a PPPoE interface or are using DHCP, note down how that is configured, and just ditch everything.(install a fresh new version and re-configure it)And lets terminate the off-topic discussion here. ---

## Response 89
ill create a thread in the beginer basics. thank you! ---

## Response 90
And now you goto Files menu on the left side in winbox and you may have a file to click <Download> to download. ---

## Response 91
With temporary deleting DNS DoH certificates from my wAP R ac i can install the new wireless package without the need to netinstall (but i still probably should do that) ---