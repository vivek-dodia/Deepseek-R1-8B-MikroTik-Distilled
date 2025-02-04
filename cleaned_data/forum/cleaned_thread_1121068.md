# Thread Information
Title: Thread-1121068
Section: RouterOS
Thread ID: 1121068

# Discussion

## Initial Question
Does anybody have any insight on what Mikrotik is doing with MLAG? It appears that MLAG has been broken since 7.7 and looking at the changelog in 7.7 I see a few bridge changes:*) bridge - added support for static MDB entries;*) bridge - disallow port-controller while the bridge has MSTP enabled;*) bridge - fixed "edge=yes" setting for MSTP;*) bridge - fixed MSTP compatibility with STP;*) bridge - fixed R/M/STP bridge identifier on protocol-mode change;*) bridge - fixed RSTP BCP with bridged PPP interfaces;*) bridge - fixed STP blocking state on port-controller;*) bridge - fixed host moving with fast-path;*) bridge - fixed incorrect root port blocking for MSTP;*) bridge - fixed master port conversion;*) bridge - fixed mst-override port priority for MSTP;*) bridge - fixed port priority for STP and RSTP;*) bridge - improved port-controller system stability;*) bridge - improved system stability when using MSTP and many VLAN mappings;*) bridge - removed "age" monitoring property from the host table;Not saying that those changes are specifically what broke MLAG, but it's probably related. MLAG was perhaps a little pre-maturely released, but it's now completely broken.I understand that sometimes things get broken while moving forward, but anything that gets messed up along the way really should be fixed pretty quickly. We're coming up on 6 months that this has been broken. I need to expand some networks and those networks need some sort of redundant access-layer solution, and right now, Mikrotik is apparently broken with no fix in sight. ---

## Response 1
Hi, what configuration do you have?We also found that MLAG on ROS versions higher than 7.6 (so 7.7, 7.8 and 7.9) does NOT work, especially if you have two pairs of switches in MLAG (4 devices)We also have 2 device setups with ROS 7.9 and MLAG works fine...viewtopic.php?p=1002218&hilit=mlag#p1002218 ---

## Response 2
Interesting....I hadn't seen your thread otherwise I would have piled on in there.In my case I have a pair of CRS326-24S+ switches as a "core" with a pair of CRS328-24p switches below.When everything is on 7.6, the MLAG on the "core" layer works great. Trying to enable MLAG on the CRS328 "access" pair just creates a big spanning tree loop. Similar MLAG config as with the CRS326's above, but the 328's fail and create a loop.Upgrading the CRS326 pair beyond 7.6 causes instability. Spannihg-tree blocking, MAC shifting, it's a mess.I have another pair of CRS326-24G switches on an additional site for that customer and they experience the same issue moving past 7.6.It's unusable. I'll take a look at your thread more in depth when I get some time tomorrow.Thanks!!! ---

## Response 3
Hi, Mikrotik Support has reproduced and confirmed the bug:Hello, Thank you for the report!We have managed to reproduce the issue locally in our labs and look forward to fixing it on upcoming RouterOS versions, unfortunately, I cannot provide a release date now.Unfortunately, I cannot suggest any known workarounds.Best regards, Edgars P. ---

## Response 4
Good news, everyone! ---

## Response 5
Is MLAG working on 7.10 for you now? ---

## Response 6
Please, tell me - is the MLAG working on 7.10?I have issues with configuring the Mlag, not appear in active port in the following command:Interface/bonding/monitor “name of the bonding” ---

## Response 7
Mikrotik MLAG has never worked properly. Anyone who says otherwise has never used a REAL working MLAG setup. The entire Mikrotik approach to MLAG is half-baked. Ive been waiting over a year for a fix and they could care less.. I have a pair of nice paper weights sitting here.. Completely worthless equipment.viewtopic.php?p=986537#p986537 ---

## Response 8
Mikrotik MLAG has never worked properly. Anyone who says otherwise has never used a REAL working MLAG setup. The entire Mikrotik approach to MLAG is half-baked. Ive been waiting over a year for a fix and they could care less.. I have a pair of nice paper weights sitting here.. Completely worthless equipment.viewtopic.php?p=986537#p986537Hi! Are you refering to the issue that the interfaces after a switch reboot starts sending traffic through only one switch? I'm trying to make 2 CRS326 24S+ 2Q working at the same time balancing the traffic of my network but is impossible. I have to change the mode of the bondings in the switches after a reboot and revert the changes. There's no way to keep that working fine unless you use balance-rr but the interface performance is so much poor. ---

## Response 9
Hello, Thank you for the report!We have managed to reproduce the issue locally in our labs and look forward to fixing it on upcoming RouterOS versions, unfortunately, I cannot provide a release date now.Unfortunately, I cannot suggest any known workarounds.Best regards, Edgars P.Has this fix made it into RouterOS yet ? ---

## Response 10
Mikrotik MLAG has never worked properly. Anyone who says otherwise has never used a REAL working MLAG setup. The entire Mikrotik approach to MLAG is half-baked. Ive been waiting over a year for a fix and they could care less.. I have a pair of nice paper weights sitting here.. Completely worthless equipment.viewtopic.php?p=986537#p986537Hi! Are you refering to the issue that the interfaces after a switch reboot starts sending traffic through only one switch? I'm trying to make 2 CRS326 24S+ 2Q working at the same time balancing the traffic of my network but is impossible. I have to change the mode of the bondings in the switches after a reboot and revert the changes. There's no way to keep that working fine unless you use balance-rr but the interface performance is so much poor.I'm referring to the fact that they (mikrotik) have no idea what they are doing. Thr lacp system id changes when devices are rebooted. Causing disruption. The spanning tree bridge id changes when devices are rebooted. Causing disruption. It doest work with igmp snooping. It's a poor attempt. ---

## Response 11
if you need reliable MLAG hardware go for cisco, extreme or if you need to be on budget ... fs.comspeaking of fs...MLAG featuring switches:N5860-48SC (mlag or stack)S5860-48SC (stack)S5850-48S6Q (mlag)routing ... mikrotikswitching ... cisco, fs, aruba, extreme ---

## Response 12
Interesting....I hadn't seen your thread otherwise I would have piled on in there.In my case I have a pair of CRS326-24S+ switches as a "core" with a pair of CRS328-24p switches below.When everything is on 7.6, the MLAG on the "core" layer works great. Trying to enable MLAG on the CRS328 "access" pair just creates a big spanning tree loop. Similar MLAG config as with the CRS326's above, but the 328's fail and create a loop.Upgrading the CRS326 pair beyond 7.6 causes instability. Spannihg-tree blocking, MAC shifting, it's a mess.I have another pair of CRS326-24G switches on an additional site for that customer and they experience the same issue moving past 7.6.It's unusable. I'll take a look at your thread more in depth when I get some time tomorrow.Thanks!!!Since MLAG doesn't work properly, how would you rather setup a redundant network, using 2x CRS326-24+2Q switches, connected to a RB301?I have 5x Proxmox servers, setup with LACP (802.3ad) over 2x SFP+ ports. And each SFP+ port is connected to a CRS3262-24+2Q switch.Currently I am using ROS 7.13.4 ---

## Response 13
Easy. Don't use mikrotik! ---

## Response 14
Easy. Don't use mikrotik!What else then? ---

## Response 15
Easy. Don't use mikrotik!What else then?EDIT:i just gave you alternativesRIGHT aboveyour postif you are on a budget ... fs.com S5850 or N5860. i would recommend the Ndefinitely heavier on the price tag than mikrotik but quite solid switchesif budget is no concern you could go with juniper or extreme.if you REALLY do not care about money - cisco nexus 9k, but licensing is an utter shitshow over there ---

## Response 16
What else then?EDIT:i just gave you alternativesRIGHT aboveyour postif you are on a budget ... fs.com S5850 or N5860. i would recommend the Ndefinitely heavier on the price tag than mikrotik but quite solid switchesThose switches are 7x more expensive than the MikroTiks ---

## Response 17
EDIT:i just gave you alternativesRIGHT aboveyour postif you are on a budget ... fs.com S5850 or N5860. i would recommend the Ndefinitely heavier on the price tag than mikrotik but quite solid switchesbut they work quite well.Those switches are 7x more expensive than the MikroTiksyep. i know. but way cheaper than cisco, extreme or juniper ---

## Response 18
EDIT:i just gave you alternativesRIGHT aboveyour postif you are on a budget ... fs.com S5850 or N5860. i would recommend the Ndefinitely heavier on the price tag than mikrotik but quite solid switchesThose switches are 7x more expensive than the MikroTiksYou are throwing your money away on mikrotik if you intend to mlag. Plain and simple. 7x more and working is a better deal than 1/7 cheaper and doesn't work at all.Anyone living with a mikrotik mlag setup had never used a real good mlag setup from a number of other vendors. ---

## Response 19
You are throwing your money away on mikrotik if you intend to mlag. Plain and simple. 7x more and working is a better deal than 1/7 cheaper and doesn't work at all.Anyone living with a mikrotik mlag setup had never used a real good mlag setup from a number of other vendors.As one of the people who _heavily_ pushed Mikrotik to add MLAG and tested it from Day 1, I completely agree. They really missed the mark on this feature.I wish they had brought a couple of cheap Extreme Summits from eBay and set them up in a MLAG to see how to do it properly before they implemented it. ---

## Response 20
The only version that works decently with MLAG is 7.6All the others bring serious problems ---

## Response 21
Registered here and following this topic because I'm in the same struggle as others here, having MLAG not working under 7.14.2. Nothing in the changelog of the future 7.15 brings me hope, and I cannot downgrade to 7.6 some of my devices since they were originally shipped with newer versions. ---

## Response 22
as mlag mostly is populated in data centre environments, try to invest in decent switches for mlag setupsif not for extreme, juniper or even ci$co give fs a try ---

## Response 23
as mlag mostly is populated in data centre environments, try to invest in decent switches for mlag setupsif not for extreme, juniper or even ci$co give fs a tryOf course. There are many other things out there that I could replace with way more expensive substitutions to finally enjoy the advertised features...But we're here on a Mikrotik forum, discussing about a RouterOS feature that should just... work (and used to, apparently, in previous firmware versions).So apart from your patronizing answer, I would loooove to buy a Juniper QFX just to have MLAG finally working. You're welcome to finance me.There are wide gaps between, say, a home installation with just a switch and a SOHO router, a homelab with somewhat advanced features, and finally a Tier 4 datacenter. Obviously people discussing on this board are eager to achieve better reliability in their setups with a usable MLAG function, but I'm pretty sure they're all quite aware that they won't build a datacenter-like setup with non-expensive hardware.So I might be wrong, but despite being very well aware that expensive hardware is more prone to deliver high-end features (having worked with Cisco and Juniper in the past, we can all say that they also have their bugs and software regressions, sometimes even for simple features), I'm really not sure that advising us to chose other expensive equipment on this Mikrotik forum is going to help much. ---

## Response 24
OP here....One year later....Still broken.This one feature was the whole reason that I specified Mikrotik for a few specific deployments.Since this has been broken, Mikrotik has built-in lots of new features...Created lots of new problems...And yet this KNOWN and reproducible issue has gone seemingly without attention for over a year.7.7 was released on January 12th 2023.At this point, they should just completely remove the feature from the product and stop advertising that they can do it. ---

## Response 25
as mlag mostly is populated in data centre environments, try to invest in decent switches for mlag setupsif not for extreme, juniper or even ci$co give fs a tryOf course. There are many other things out there that I could replace with way more expensive substitutions to finally enjoy the advertised features...But we're here on a Mikrotik forum, discussing about a RouterOS feature that should just... work (and used to, apparently, in previous firmware versions).So apart from your patronizing answer, I would loooove to buy a Juniper QFX just to have MLAG finally working. You're welcome to finance me.There are wide gaps between, say, a home installation with just a switch and a SOHO router, a homelab with somewhat advanced features, and finally a Tier 4 datacenter. Obviously people discussing on this board are eager to achieve better reliability in their setups with a usable MLAG function, but I'm pretty sure they're all quite aware that they won't build a datacenter-like setup with non-expensive hardware.So I might be wrong, but despite being very well aware that expensive hardware is more prone to deliver high-end features (having worked with Cisco and Juniper in the past, we can all say that they also have their bugs and software regressions, sometimes even for simple features), I'm really not sure that advising us to chose other expensive equipment on this Mikrotik forum is going to help much.i agree with most of your statements. i also wished MT could deliver a working MLAG solution, but it seems they don'tof course more expensive hardware will deliver features differently but as i "advertized" switches from FS i was just trying to give options to working MLAG hardware other than juniper, cisco, extreme, etc. which most of the time are starting at a 4-digit price tag. a pity.so FS might be a reasonable option for some people and those people trying to achieve MLAG setups are even willing to spend "a little more" for that MLAG reliability/benefit and have never heard of e.g. FShaven't known that brand 3 years before and per today managing about 45 of those devices with little to no hurdles.that's why i mentioned them. not to blindly point away from MT (been with MT for >10 years) ---

## Response 26
@spippan: Regarding FS, what do you think of their own FSOS compared to Mikrotik ROS or any kind of ONIE? Is there a big difference in cold boot time between them? ---

## Response 27
@spippan: Regarding FS, what do you think of their own FSOS compared to Mikrotik ROS or any kind of ONIE? Is there a big difference in cold boot time between them?on e.g. N8560 or S5850 the CLI syntax is very cisco-likeboot time on a S5850 concludes about 3-5minsboot time on a N8560 concludes about 5-8minsnever exactly measured them, but far from a reboot of, let's say, a CCR2004-1G-12S+2XS (which is out of context, because there is no switch chip in it, sry, but just for reboot times) ---

## Response 28
Thanks for pointing me in the right direction guys. I got a pair of CRS326's for the express purpose of running MLAG and even with 7.14.3 it completely breaks STP and then downs the entire network. If you disable MLAG, STP still doesn't work until you reboot the switches. After that it correctly puts ports in alternate or backup mode as it should. These were going to be a top-of-rack pair in a co-lo rack....but even I'm not that masochistic! ---

## Response 29
Hi, Same here, have four 2116 running MLAG on 7.11Ran the upgrade to 7.12.1. First pair went okay, but with the second pair I got burnt.They made a loop in the network, lost contact with the local unit on the secondary link until after power down/up.Eventually I managed downgrade all back to 7.11 but lost contact with the remote on the second link until after power down/up.Ran a config compare between the one on 7.11 and 7.12.1 and did not find config changes.Not sure MT broke MLAG beyond repair, but given the road to deployment and now the 1st upgrade (minor upgrade i dare say), it feels far from stable/reliable to us. ---

## Response 30
Does anyone know if it works on 7.15.1? ---

## Response 31
Not really I dare say. I have a pair of 326 as distribution switches on 7.15.1 running MLAG to the edge switches and also to the core. Recently I rebooted the primary and completely lost both. No more traffic to the core. Could not even access either one via MAC address, despite links were up. Had to go onsite. First I did a power reset on thesecondary(the one that has not been rebooted before). And guess what, both units are running fine since then.Conclusion: Once it works, don't touch it anymore. That's far from reliable and I will have to go back to Spanning Tree redundancy. Very sad. ---

## Response 32
Has support responded to anyone about these MLAG? Is there a bug tracker somewhere?The reason I went down the road with Mikrotik was because of MLAG support on the CRS326's. I now like MT for many other reasons but having flaky MLAG is going to cause me the re-think what I want to do. This is just for home setup but I'm trying to build HA everywhere as an exercise and MLAG is a key part of the puzzle. I even bought extra network cards for all my servers with this in mind. I guess I should have tried it first ---

## Response 33
7.15.2 same problems... ---

## Response 34
7.15.2 same problems...Which is? ---

## Response 35
if you need reliable MLAG hardware go for cisco, extreme or if you need to be on budget ... fs.comspeaking of fs...MLAG featuring switches:N5860-48SC (mlag or stack)S5860-48SC (stack)S5850-48S6Q (mlag)routing ... mikrotikswitching ... cisco, fs, aruba, extremeEven if the same name FSOS , different by platform ( rebranded ).The S series uses the CENTEC ASIC with the original OS ( they just renamed it, the versioning is the same as the manufacturer's ), matured platform. ---

## Response 36
if you need reliable MLAG hardware go for cisco, extreme or if you need to be on budget ... fs.comspeaking of fs...MLAG featuring switches:N5860-48SC (mlag or stack)S5860-48SC (stack)S5850-48S6Q (mlag)routing ... mikrotikswitching ... cisco, fs, aruba, extremeEven if the same name FSOS , different by platform ( rebranded ).The S series uses the CENTEC ASIC with the original OS ( they just renamed it, the versioning is the same as the manufacturer's ), matured platform.ok, did not know it all originated from centec (maybe...), but what do want to say with that? ---

## Response 37
if you need reliable MLAG hardware go for cisco, extreme or if you need to be on budget ... fs.comspeaking of fs...MLAG featuring switches:N5860-48SC (mlag or stack)S5860-48SC (stack)S5850-48S6Q (mlag)routing ... mikrotikswitching ... cisco, fs, aruba, extremeEven if the same name FSOS , different by platform ( rebranded ).The S series uses the CENTEC ASIC with the original OS ( they just renamed it, the versioning is the same as the manufacturer's ), matured platform.Depends on the model, most of the S-series are using Broadcom nowadays (which you will see already on the product page which model uses which switchchip vendor). Some use Realtek and I think they might have some even older left in production which is using a chinese ASIC.It seems likehttps://www.ruijienetworks.com/are the ones who have OEMed the FSOS which FS.com is using as their NOS.Except for their own gear with FSOS they also resell devices from Nvidia with Cumulus Linux as NOS and regular whiteboxes that comes preloaded and with a license from PicOS as NOS. ---

## Response 38
Yea...the only reason I bought Mikrotik was because of MLAG on the CRS518-16XS-2XQ.I've had my share of issues during reboots, but most of the time my setup has recovered without manual intervention - but nevertheless I would never have bought those switches if they had not been advertised supporting MLAG :/But except for those fun MLAG outages I've been happy with the rest of the features (bought two CRS518 switches and two CCR2004 routers for a small DC setup) for the money. ---

## Response 39
Has support responded to anyone about these MLAG? Is there a bug tracker somewhere?The reason I went down the road with Mikrotik was because of MLAG support on the CRS326's. I now like MT for many other reasons but having flaky MLAG is going to cause me the re-think what I want to do. This is just for home setup but I'm trying to build HA everywhere as an exercise and MLAG is a key part of the puzzle. I even bought extra network cards for all my servers with this in mind. I guess I should have tried it firstThey acknowledged it is broken and even asked me how things should work, then said they don't have time to fix it. ---

## Response 40
They might be fixed in "RouterOS 8.0"( ~ 10 years ) ---

## Response 41
They acknowledged it is broken and even asked me how things should work, then said they don't have time to fix it.Well isn't that awesome? The whole reason I bought a pair of CRS326 was to MLAG some critical ports. Is anyone from Mikrotik going to chime in here? ---

## Response 42
We using mlag 2x 326 24s+ on ros 7.13.5. it works, but it's unstable in places.for example: if you have a lacp host connected to two switches, then everything works fine, but as soon as I delete the lacp group from the host side, everything stops working. the switches continue to operate in lacp mode, despite the lack of lacp (partner id) negotiation. in the bonding settings, you can select only ARP and Mii, and neither is suitable. We reported this to technical support (SUP-114652) back in May 2023, but there are still no fixes.on version 7.13.5, it seems to have been working for a year, but I will not update the version until this error is fixed.in general, I think you really need to choose other switches to create mlag conf: we successfully use used arista and it works more stable and more predictable ---

## Response 43
Yea...the only reason I bought Mikrotik was because of MLAG on the CRS518-16XS-2XQ.I've had my share of issues during reboots, but most of the time my setup has recovered without manual intervention - but nevertheless I would never have bought those switches if they had not been advertised supporting MLAG :/But except for those fun MLAG outages I've been happy with the rest of the features (bought two CRS518 switches and two CCR2004 routers for a small DC setup) for the money.Agreed. This is the only reason I brought a pair of CRS326-24S-2Q+RM switches. to use MLAG. And now it's broken. ---

## Response 44
The only version that works decently with MLAG is 7.6All the others bring serious problemsYes, exactly! The last stable version with MLAG support is ROS 7.6. But how can we use the new CRS520 and CRS510 switches, which actually cannot be downgraded to version 7.6 of ROS? ---

## Response 45
Seems to be a hard nut to crack for Mikrotik developers...Perhaps my Expectations about MLAG is wrong.I would expect after initial Setup of two Switches for ICCP - now connected via MLAG for redundancy - that under Interfaces->Bond I could choose either two local interfaces as "normal" LACP like in the last years or - MLAG! - one interface of the local and another interface from the second switch, choose 802.3ad, plug the Network device as LACP-Device into both configured ports and could see the Link on either a master switch (like in stacking) or even both.Where the slaves could be monitored is - for me - completely irrelevant.But this doesn't even work in 7.6, Link-flapping, no data transmission overall or - despite trying everything regarding vlan - not for all VLANs. And if one switch fails, everything goes down, not exactly what I had in mind in terms of redundancy. I grant the RTSP/MSTP mechanism the one second for failover, but since the bridge even changes the MAC adress as ist seems, the whole process is completely out of control. (tested with the two 504)Due to our rather small setup with 9x CRS354-48P, 2x CRS504, 2x CRS510, 2x CRS317 and 1x CRS326 next to one CCR2116-12G+4S+ on the biggest office it is no problem at the moment to have not that level of redundancy via MLAG which I wished to have. But perhaps there is some working MLAG planned by Mikrotik in the next releases. ---

## Response 46
as in the latest 7.17beta5 changelog, mikrotik is obviously working on bridge and mlag performanceso hopefully on 7.17 final or 7.18 MLAG is finally USABLEviewtopic.php?p=1108704#p1109249 ---

## Response 47
after all, it's was broken on 7.13.5in the simplest configuration, disabling a port in a bridge that is not in the mlag group stops forwarding all traffic for 3 seconds on all bridge interfaceseven the metrics on the interfaces in winbox stop updatingat first it seemed to me that I was doing something wrong, and then I realized that I was just disabling the interface with the disable commanddoes it make sense for me to update this to 7.16.1 or is it better to wait for 7.17? it's impossible to work like thisSUP-172251 ---

## Response 48
4xCRS520-in-MLAG-to-MLAG-r.2.PNGI created a lab where I connected four CRS520-4XS-16XQ switches in a High Availability MLAG configuration. All switches are accessed through a configured VLAN interface with a VLAN ID and IP address added to each bridge, and the corresponding VLAN is tagged on the ICCP ports of the four CRS520-4XS-16XQ. Switches SW2 and SW3 are in MLAG with each other, as are SW4 and SW5. (L3 hardware offloading is disabled on all switches). For the purpose of the lab, two CRS326-24S-2Q+ switches are bonded in LACP 802.3ad via their 40G interfaces to the respective MLAG groups, with VLAN interfaces and IP addresses for management.In my test, when one of the MLAG primary peers (SW2 or SW4) is restarted, connectivity between SW1 and SW6 is restored in about 13 seconds. Conversely, when one of the MLAG secondary peers (SW3 or SW5) is restarted, connectivity between SW1 and SW6 is almost unaffected (around one echo request loss).However, what happens to the management VLAN interfaces of the switches configured in MLAG (SW2/SW3 and SW4/SW5)? In 90% of cases, when a primary peer (e.g., SW2) is restarted, access between SW2 and SW3 (and vice versa) to the VLAN management interface is lost. A random number of restarts of SW2 and SW3 can restore access, but not consistently. I noticed that in the ARP table of the secondary peer (SW3), the MAC address of the primary peer (SW2) appears in the incomplete state and then fails, suggesting that SW2 either does not respond to the ARP request from SW3 or there is another issue, such as with M/R/STP. However, I cannot pinpoint the exact cause.When I manually change the MAC addresses of SW2 and SW3, everything is restored, and I can ping SW2 from SW3 and vice versa, but only until the next restart of the primary peer. I should note that during the test, there is access to SW2 and SW3 from/to SW1 and SW6, except during the MLAG and LACP convergence period.I described the situation for one MLAG group (SW2 and SW3), but it also applies to the other MLAG group (SW4 and SW5).The test was conducted with ROS 7.17rc1, 7.17beta5, and 7.17beta4.I strongly hope and sincerely wish the MikroTik team will stabilize the MLAG functionality in version 7.17.Congratulations to the MikroTik team for the work done so far! ---

## Response 49
Thanks for your effort with this Lab setup. Mikrotik does seemingly work on this topic, let's hope that it will work flawlessly at least in 7.18.1 or so.13 seconds outage is too much because if you do a "rolling firmware upgrade" it will be inevitably that the primarys will be down for the update. Together with the Capsman-managed APs loosing all their configuration and rebuilding the WLAN from the scratch even if they just have 1 second connection outage from the capsman, this is not ideal.But Mikrotik has fixed so many issues in the past, I think they will eventually get MLAG into working condition. ---

## Response 50
@satbox, wonderful labIn my test, when one of the MLAG primary peers (SW2 or SW4) is restarted, connectivity between SW1 and SW6 is restored in about 13 seconds.this 13 second could be caused by what stp (or port - if any) mode you are using.Conversely, when one of the MLAG secondary peers (SW3 or SW5) is restarted, connectivity between SW1 and SW6 is almost unaffected (around one echo request loss).hmm... how about to take notes on every mac address involved in this switching lab? so that we know where the traffic direction goes in reality? (which switch holds the brain, the forwarding port etc...)super ---

## Response 51
Hi!on ROS 7.17 apparently MLAG Works fine. I have work on lab with two CRS309 and 3 clients, 2 mk hex and 1 linux server. Probes works sucessfully, both in the case of turning off one switch like in the case of cable disconnect.Time or recover is about 1-3 secs and both switch appears stable for two hours, ping, cpu, etc.Disclaimer: my probes have consisted on ping tests and nothing more. I haven't made high traffic probes.I wait for other users test for launch fireworks ---