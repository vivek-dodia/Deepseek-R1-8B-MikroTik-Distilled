# Thread Information
Title: Thread-141633
Section: RouterOS
Thread ID: 141633

# Discussion

## Initial Question
HiI am running 17 CRS328-24P-4S+ connected to 2 CRS317-1G-16S+ using this SFP S+32LC10D. The 328 boxes are running RouterOS 6.43.2 and the CRS317 boxes are running 6.43.4. I am experiencing that all the ports on the CRS317 are going up and down with anything between minutes to hours apart. It is almost no traffic on the network. I am totally in the dark here, do any of you have any idea what this could be?Example from log:17:02:12 interface, info sfp-sfpplus2 link down17:04:07 interface, info sfp-sfpplus2 link up (speed 10G, full duplex)17:09:04 interface, info sfp-sfpplus8 link down17:09:05 interface, info sfp-sfpplus8 link up (speed 10G, full duplex)17:18:00 interface, info sfp-sfpplus3 link down17:18:01 interface, info sfp-sfpplus3 link up (speed 10G, full duplex)17:24:13 interface, info sfp-sfpplus4 link down17:24:15 interface, info sfp-sfpplus4 link up (speed 10G, full duplex)17:25:04 interface, info sfp-sfpplus16 link down17:25:05 interface, info sfp-sfpplus16 link up (speed 10G, full duplex)17:34:00 interface, info sfp-sfpplus4 link down17:34:01 interface, info sfp-sfpplus4 link up (speed 10G, full duplex)Interface stats from one of the CRS328:/interface ethernet print stats from=sfp-sfpplus2name: sfp-sfpplus2driver-rx-byte: 4 096 343 318driver-rx-packet: 44 864 695driver-tx-byte: 1 460 265 180driver-tx-packet: 9 040 331rx-bytes: 4 277 853 088rx-too-short: 0rx-too-long: 0rx-unicast: 9 695 367rx-broadcast: 31 908 257rx-pause: 0rx-multicast: 3 273 516rx-error-events: 239rx-fcs-error: 0rx-fragment: 0rx-overflow: 0rx-jabber: 0tx-bytes: 1 498 564 543tx-unicast: 9 049 910tx-broadcast: 231tx-pause: 0tx-multicast: 4 463tx-underrun: 0tx-collision: 0tx-late-collision: 0tx-rx-64: 31 287 843tx-rx-65-127: 4 828 178tx-rx-128-255: 17 182 394tx-rx-256-511: 179 280tx-rx-512-1023: 436 533tx-rx-1024-1518: 17 622tx-queue0-packet: 9 037 205tx-queue1-packet: 0tx-queue2-packet: 0tx-queue3-packet: 0tx-queue4-packet: 0tx-queue5-packet: 0tx-queue6-packet: 0tx-queue7-packet: 0 ---

## Response 1
Try 6.43.7 and make sure routerboot is also updated. ---

## Response 2
Sure, i dont see anything about the 317s in the changelog, but i'll try. Will give a new status in about 24h, will see if anything has changed. ---

## Response 3
Try 6.43.7 and make sure routerboot is also updated.Sad to say, but this made no difference. ---

## Response 4
I am also seeing some link downs on CRS328 switches but the firmware update made them significantly less for me. ---

## Response 5
Did you find a fix yet? ---

## Response 6
Unfortunately not. I sendt them the support files at 22. Nov and did a follow up on 4. Des. Still no reply. Would be great if MT would have a look at this. ---

## Response 7
From the MikroTik site it looks to me like the S+32LC10D is specifically meant to have the S+23LC10D module on the other end. Are you using the same module on both ends? ---

## Response 8
I have the SAME EXACT problem. Mikrotik needs to fix this. No problem with 1Gbps SFP but with OWM SFP+ it's hell. I think this could be combination of software and hardware problem with SFP+ modules. ---

## Response 9
I have the SAME EXACT problem. Mikrotik needs to fix this. No problem with 1Gbps SFP but with OWM SFP+ it's hell. I think this could be combination of software and hardware problem with SFP+ modules.I agree with you assumtion that this is an edge case between the SFP units and the switch. But strangely it only occurs on one of our two CRS317 in the installation. ---

## Response 10
From the MikroTik site it looks to me like the S+32LC10D is specifically meant to have the S+23LC10D module on the other end. Are you using the same module on both ends?I am using the paired SFP+ from Mikrotik S+2332LC10D. So yes. ---

## Response 11
What's the fix Mikrotik? ---

## Response 12
Push - she problem on CRS328 here.... waiting for a fix ---

## Response 13
We had this same problem appear on one of our 317s. I am not 100% sure when it started, but it was observed on 6.43.4. The upgrade to 6.43.7 fixed it, but ONLY after I did a full factory reset and reloaded the configuration by hand (it wasn't complex).We also observed it for a brief time on several of the 328s. Switching from using SFP+1 to SFP+2 for the uplink fixed it. ---

## Response 14
We are experiencing the same thing. Running 6.42.7 with DAC Cable from CRS317 to CRS328-4C-20S-4S+RM.I had to go to a SFP 1G on both units for the flapping to stop. I had tried SFP+ DAC and SFP+ single mode fiber with the same issue.We have 8 CRS212 plugged into the CRS317 via DAC Cable with no issue. Only the 328 SFP+ ports appear to have the issue. ---

## Response 15
Exactly the same problem here. Links between CRS317 and CRS328-4C-20S-4S+ are flapping. I have 3 pairs of 317 <-> 328 and all have the same problem. I tried different SFP/DAC. The latest firmware (6.43.does not help. No problem with 1GbE links....... ---

## Response 16
I sendt MT a service dump in november - still no answer. Could i bother you guys that are experiencing the same problem with sending MT an email urging them to have a look at the issue - or at least give some feedback. I am experiencing total radio silence. ---

## Response 17
Are any of you using port ether1 or just sfp-plus ports? If you are, remember that "The new Cloud Router Switch 317-1G-16S+RM is a rack-mountable manageable switch with Layer3 features, it has 16 SFP+ ports for high performance 10GbE connectivity and a1GbE copper port for management." ---

## Response 18
Are any of you using port ether1 or just sfp-plus ports? If you are, remember that "The new Cloud Router Switch 317-1G-16S+RM is a rack-mountable manageable switch with Layer3 features, it has 16 SFP+ ports for high performance 10GbE connectivity and a1GbE copper port for management."I can only speak for myself - and i am only using the SFP+ ports. ---

## Response 19
I think the problem is the CRS328. We use the CRS317 as Core with downlinks to different CA devices, some with 1GbE and some with 10GbE. The only affected links are those between CRS317 and CRS328 with 10GbE. ---

## Response 20
exact same issue here, same symptoms, same workaround (force 1G link), it would be great if Mikrotik took this issue seriously... ---

## Response 21
I ever had bad experiences with CRSs port flapping and I don't use them anymore, both ethernets and SFPs.Sometimes on CCRs ports go totally down, disabling and enabling them solves the problem. ---

## Response 22
Sometimes on CCRs ports go totally down, disabling and enabling them solves the problem.In production context ? ---

## Response 23
I've wrote to Mikrotik Support ~2 weeks ago and also our Distributor said he would contact Mikrotik but till now no reaction. ---

## Response 24
Hi, I got an answer from support. They could reproduce the flapping issue and are working on a solution. ---

## Response 25
Same problem over here with CRS328-4C-20S-4S+RM on Sfp+ ports. I'm connected to a Dell X1052 with S+DA0003.Let's wait for the correction. ---

## Response 26
I will add my agreement to this thread. I have a CRS317-1G-16S+ with 4 CRS328-24P-4S+ and 3 CSS326-24G-2S+RM All are using the Maxxwave MW-SX+MM-US Modules. I have the same port flaping on all the CRS328 ports and the CRS317 reboots on a regular basis. The links to the CSS326's seem to be stable. I too am interested in this fix.Steve CearleySteve@cearley.usWellshire Presbyterian Church. ---

## Response 27
hi, same for us. We fighting with the same problem on our CRS317-1G-16S+ (viewtopic.php?f=2&t=146044). We thougth, it might be a configuration issue. I replaced cable, SFP+ modules (Allnet / Ubiquitiy) but nothing helped. Now I replaced the both ports (core-03 and core-04) with the 10G copper SFP ports and its seems now stable.We replaced in the first time also one switched, which helped (core-lan-01). But now we have the same issue between core-lan-03 and core-lan-04. ---

## Response 28
i mean the same problemport flapping on CRS328-24P-4S+ and CRS317-1G-16S+software version 6.44I tried different SFP modules.Are there any solutions to this problem? ---

## Response 29
Me too..317 - Ccr 10Gb mk Dac ok317 - 326 10Gb mk S+85DLC03D ok317 - 328 10Gb mk Dac flappingThe strange thing is that for over one month all worked fine, after that, without any change, the flapping began.Forcing the Dac to 1Gbps stop the flapping immediatly, now we are monitoring it, but we need 10Gb connections. ---

## Response 30
hello folks, we have multiple CRS317-1G-16S+ and CRS328-24P+4S+ with the same problem.All running RouterOS and firmware 6.44.They all connected togehter with Mikrotik DAC S+DA0001.After switching to RouterOS and firmware to 6.45beta6 (Testing) don't solve the flapping port problem.Last try....Finally we switched on the CRS317-1G-16S+ to SwitchOS 2.9.So the CRS328-24P+4S+ with RouterOS works with the CRS317-1G-16S+ with SwitchOS for 24h without problems...So i think it's a problem on the CRS317-1G-16S+ with RouterOS.regards ---

## Response 31
hi, Me too..317 - Ccr 10Gb mk Dac ok317 - 326 10Gb mk S+85DLC03D ok317 - 328 10Gb mk Dac flappingThe strange thing is that for over one month all worked fine, after that, without any change, the flapping began.Forcing the Dac to 1Gbps stop the flapping immediatly, now we are monitoring it, but we need 10Gb connections.since, not all ports flapping, just one or two, I assume that there is a hardware failure. But we have to wait, until MikroTik have something so say. ---

## Response 32
hmm, same problemCRS317-1G-16S+ vs CRS326-24G-2S+ - DACtoday CRS317 stop traffic and in same time CRS326 stop working port connecting to CRS317.MKv6.44 ---

## Response 33
hello folks, update:After we switched on the CRS317-1G-16S+ to SwitchOS 2.95 days without port flapping.regards ---

## Response 34
hello folks, update:After we switched on the CRS317-1G-16S+ to SwitchOS 2.95 days without port flapping.regardsThis is good news and indicative of software issues. Raising the probability of a fix. I have however met nothing but radio silence from MT lately, have any of you guys gotten any info from them? ---

## Response 35
What's the stats of the fix? ---

## Response 36
After we switched on the CRS317-1G-16S+ to SwitchOS 2.95 days without port flapping.Hi roggles, still stable with SwitchOs? ---

## Response 37
yes, since there are no log entries ---

## Response 38
CRS317 replaced with UBNT EdgeSwitch 16XG. Problem solved. I will not wait for the device to stop 1Gbit traffic.I won't wait for it to ever be fixed. Similar to flapping on RB3011 and the like.MIkrotik -1000. ---

## Response 39
Have the same problem with UF-SM-10G & CRS317-1G-16S+ with 6.42.12.Any RoOS version with fix? ---

## Response 40
Have the same problem with UF-SM-10G & CRS317-1G-16S+ with 6.42.12.Any RoOS version with fix?Could you please send us email, about your setup and problem, tosupport@mikrotik.com? ---

## Response 41
Have the same problem with UF-SM-10G & CRS317-1G-16S+ with 6.42.12.Any RoOS version with fix?Could you please send us email, about your setup and problem, tosupport@mikrotik.com?Hi! How Is the fix coming along? ---

## Response 42
Could you please send us email, about your setup and problem, tosupport@mikrotik.com?Ticket#2019040322003846 ---

## Response 43
Could you please send us email, about your setup and problem, tosupport@mikrotik.com?Ticket#2019040322003846Where do i get additional information about tickets? I see no links in the emails i have gotten. ---

## Response 44
Severe port flapping on 10G links, works with auto-negotiation turned off and set to 1g.CRS317-1G-16S+ <<>> CCR1009-8G-1S-1S+, Flapping at 10G, Works stable at 1GCRS317-1G-16S+ <<>> CRS328-4C-20S-4S+, Flapping at 10G, Works stable at 1GCRS317-1G-16S+ <<>> CRS212-1G-10S-1S+, Works Stable at 10G.CRS328-4C-20S-4S+<<>> CRS328-4C-20S-4S+, Works Stable at 10G.So, it all boils down to ROS BUG in CRS317. ---

## Response 45
Does anyone have port flapping problem with 10G link between CRS317-1G-16S+ <<>> CRS317-1G-16S+ ?In our case it starts to happen after about a week after reboot and it happens on 2 of 3 ports. We tried to interchange modules used on stable link - but on other link it also flaps.We have flapping on 1 & 5 ports, but no flapping on 9 port. Coincidence?In SwitchOS you dont have log entries and the link is stable also? May be in SwOS it just does not log the short term failures? ---

## Response 46
Mikrotik support tell us that the problem is well known and that they don't have ETA for the resolution.Their official workarround is to downgrade links to 1Gb or use switchos on 317I hope that someone take care about this terrible bug!!Alessandro ---

## Response 47
file bug ---

## Response 48
Hello, SwitchOS is one big pile of shit with no real featues, as it was intended for the general audience.When i add SFP media converters or non-mikrotik or unmanaged switches on the other end it does not pick the link up.But ROS does, hence we cannot use SWOS at all (As a last resort even if it a very crap OS .). ---

## Response 49
Hello, SwitchOS is one big pile of shit with no real featues, as it was intended for the general audience.When i add SFP media converters or non-mikrotik or unmanaged switches on the other end it does not pick the link up.But ROS does, hence we cannot use SWOS at all (As a last resort even if it a very crap OS .).You are absolutely right about SwOS, but what can do with many introduced MiktoTik devices with only SwOS ?It's not normal to produce a lot of hardware with no software capable to handle it...I still believe, that MiktoTik will get attention on this and will produce real working OS.btw I keep all my with SwOS 2.7 ---

## Response 50
BTW, how do u guys can confirm that there no port flapping under SwOS? I didnt find any log section in SwOS web interface... ---

## Response 51
You have to check it on 328 side, looking for disconnections or rstp recalculation ---

## Response 52
So seems like the problem is with CRS317-1G-16S+We have one CRS317-1G-16S+ in center and three CRS317-1G-16S+ at remote ends, after 6 days from reboot we got port flapping - but not on all ports, we tried to change SFP+ modules, cables but no sense. After we changed from RoOS to SwOS on central CRS317-1G-16S+ log files of the remote CRS317-1G-16S+ (that are still running RoOS) are showing no port flapping after more than 8 days! ---

## Response 53
I have issues on the CRS328 connecting to a Siklu. ---

## Response 54
I can confirm that the problem appear also with 2 CRS317 connected trought mk DAC.PLEASE MIKROTIK, GIVE US SUPPORT!!!!!!!!! ---

## Response 55
I confirm the problem with the CRS328 and CRS317 connection.The problem is partially solved by the change of the CRS317 system to SwOS. But still Rx FCS Errors occur on the 10G interfaces.[Ticket#2019051422003403] ---

## Response 56
Mikrotik, this issue has almost 6 months !!It seems that Mikrotik acknowledges the problem, my reseller confirmed this point, you should be able to prioritize this issue as it affects core features : we're unable to deliver 10G connectivity !! ---

## Response 57
The problem is partially solved by the change of the CRS317 system to SwOS. But still Rx FCS Errors occur on the 10G interfaces.We can confirm the same, but not on all interfaces, those that were stable on RoOS have only 2 Errors. ---

## Response 58
Mikrotik support, please WAKE UP!!Customers are angry and whants different brand hardware! ---

## Response 59
*) crs3xx - improved switch-chip resource allocation on CRS326, CRS328, CRS305;..but still problem not fixed.1.PNG2.PNG ---

## Response 60
Can anybody try to add attenuators on problematic links? Would it change anything? ---

## Response 61
Can anybody try to add attenuators on problematic links? Would it change anything?That seems unlikely as I have the same link flapping on my DAC links btween the CRS328 and CRS317 on 10G links. Something seems to be wrong (software or hardware??), but Mikrotik does not seem to be interested... ---

## Response 62
Does the DAC link have Rx FCS Errors also? ---

## Response 63
Does the DAC link have Rx FCS Errors also?YesThis is the setup on my desk. It does nothing, only connections between switches.3.PNG ---

## Response 64
We are having this issue as well between two CRS317-1G-16S+ in our datacenter. We wrote an E-Mail to MikroTik Support on the 18th of May.There has not been any reaction since*.EDIT: *except for the automated reply message. ---

## Response 65
Our client has 200+ units installed in different locations, now even in 1G is not stable.We have been pushed for months, mikrotik nothing to say.Very bad service, client try to use Ubq to replace all CRS328.I am thinking about it too, maybe we should close the distribution with Mikrotik. ---

## Response 66
Very bad service, client try to use Ubq to replace all CRS328.Hi gentrice, we are angry too, but the problem we are talking here is on crs317.. what kind of problem do you have on crs328? ---

## Response 67
There has not been any reaction since*.We received an answer that MikroTik is aware of this issue and is working on a solution. ---

## Response 68
Have anyone gotten any time estimates on when flapgate is beeing fixed? ---

## Response 69
new reply by mk support:We are working on this problem, it could take up to a couple of weeks, to find a proper solution and test it.we hope it... ---

## Response 70
Hi gentrice, we are angry too, but the problem we are talking here is on crs317.. what kind of problem do you have on crs328?We were able to reproduce this issue on CRS328-24P-4S+ connected via SFP+ DAC to a CRS317-1G-16S+. We tested the following scenarios:.) change SFP+ port on CRS328 -> port keeps flapping.) change SFP+ port on CRS317 -> port keeps flapping.) take a freshly delivered CRS317 connect it to the CRS328 -> port keeps flapping.) take different DAC -> port keeps flappingTurning off Auto Negotiation and pinning it on 10Gbps (tick the radiobutton under Interfaces->Ethernet) on both CRS results in a stable 1Gbps link.The setup firmwares and Package Versions:CRS328-24P-4S+: 6.43.12 (stable), Firmware: 6.42.5 (Factory)CRS317-1G-16S+: 6.44.3 (stable), Firmware: 6.44.3, Factory Firmware: 6.42.11We added this information to the ticket we have opened.EDIT: We updated the CRS328-24P-4S+ to 6.44.3 (Firmware & Packages) -> port keeps flapping ---

## Response 71
In our scenario we needed to connect CCR1036-8G-2S+ (ROS 6.44.1) to CRS328-4C-20S-4S+ (SwitchOS 2.9) using Mikrotik SFP+ DAC 1m. We got 10G FDX connection, but it was always unstable. We had the following troubles:10G link flapping, sometimes, when it wants)After a few hours of good working tagged traffic between CCR1036-8G-2S+ and CRS328-4C-20S-4S+ begun to drop. Connections begun to close one by one, until we reboot CRS. Than it works good again, but for a few hours only. After that we seen packet loss again.If we tried to change any SFP+ settings like auto negotiation or set manual 1G speed, link goes down after applying and not became up. Link became up only if we reboot CRS or physically replug SFP+ DAC. And many other port settings in SwitchOS has the same bug - not working without reboot. DHCP client starts to work only after reboot too.I think that's enough. Now we definitely completely refuse to work with mikrotik switch. It has too many unsolvable problems.Bcause if we tell our customers that they need to wait a few weeks/months/years without Internet connection, until Mikrotik fix it, they will simply connect to another provider, and our business will go bankrupt. ---

## Response 72
What's the status on this Mikrotik? ---

## Response 73
Any progress on this Mikrotik? It has been 6 months with no fix. Could we have an update and a plan to a fix? ---

## Response 74
do not use DAC. ---

## Response 75
do not use DAC.this issue also happens with mikrotik SFP+ and fibers ---

## Response 76
I can confirm thatthereisthe same problem on :CSS326-24G-2S+ with SwOS 2.9Any SFP+ device connected to port EXCEPT connection toCRS317-1G-16S+ with SwOS 2.7(with any SFP+ optic module and DAC working as required)there innotproblem at all on:CRS317-1G-16S+ with SwOS 2.7 (we are unable to upgrade to 2.8 or 2.9 because switch stops to work after 10-15 mins, but you can find this on forum as well)many switches with many different modules and vendors SFP+s, DACs, S+RJ10 ---

## Response 77
Today we started to request the replacement of flapping CRS328, where we were able to systematically reproduce it, at our distributor. ---

## Response 78
Hello. I need to buy two 24 port switches and I have to choose between CRS326 and second hand Cisco 2960G, the price is the same. If I take CRS326 it will be used with RouterOS for access switch. From what I read in forum, SwOS is not ready for "in production" setups and this is the reason to choose CRS326 instead of CSS326.My question is - if I use only 100Mbps and 1000Mbps (random mix of ports, PCs, VoIP phones etc.) connections and not 10G connections, the problem with port flapping will be present or not? ---

## Response 79
Hello. I need to buy two 24 port switches and I have to choose between CRS326 and second hand Cisco 2960G, the price is the same. If I take CRS326 it will be used with RouterOS for access switch. From what I read in forum, SwOS is not ready for "in production" setups and this is the reason to choose CRS326 instead of CSS326.My question is - if I use only 100Mbps and 1000Mbps (random mix of ports, PCs, VoIP phones etc.) connections and not 10G connections, the problem with port flapping will be present or not?According to all posters here, the problem presents itself only in connection with CRS317 and 10G SFP+. So it will not happen to your setup. ---

## Response 80
According to all posters here, the problem presents itself only in connection with CRS317 and 10G SFP+. So it will not happen to your setup.I think the same GuJack20. Do you have CRS326 in production? If you have, what is your opinion for the switch? Somebody else do you have CRS326 in production running RouterOS? ---

## Response 81
I think the same GuJack20. Do you have CRS326 in production? If you have, what is your opinion for the switch? Somebody else do you have CRS326 in production running RouterOS?Hi, please open or write in a thread/section where your question is addressed. This thread is about a severe port flapping issue on CRS328 and CRS317 as the title reflects.Thanks, nhEDIT: corrected a typo of product names. ---

## Response 82
Hi, please open or write in a thread/section where your question is addressed. This thread is about a severe port flapping issue on CRS328 and CRS317 as the title reflects.Thanks, nhEDIT: corrected a typo of product names.I'm sorry if this is mistake. I posted here because CRS328 is the same as CRS326 but with PoE. If moderators want they can delete my posts. ---

## Response 83
CRS328 to HP DL380 10gbit direct connection, port flapping exists.so this it not mikrotik-to-core or mikrotik-to-mikrotik connection issue, something wrong in hardware design, I guess. ---

## Response 84
Same problem appeared suddenly after months of uptime. Two links between CRS326 and CRS317 (two of both devices) - one works perfectly and other link is flooding logs and causing packet loss. All troubleshooting attempts lead to conclusion, that CRS317 is the source of the problem - when we cross-connected the uplinks (leading to CRS326s), then port flapping stayed on same CRS317. Changing patches and GBIC's did nothing at all. Changing the uplink to other unused port on CRS317 did not help either. Links to other devices were fine on that same switch.Upgrades or downgrades from 6.43.16 (same version on all devices) had no effect either.One other detail could not be unnoticed - link downs had made their way up to tomorrow alreadyScreenshot (602).png ---

## Response 85
Now we did one test with the problematic link - we converted it to 10GbE with CAT7 and pair of RJ-10 modules. For more than hour of heavy load there was absolutely no link downs or any packet loss - so this is not likely related to topology issues etc. When we connected ports with fiber as before, all problems were back.P. S. RJ-10 modules behaved differently on different hardware - everything was OK on CRS317, but module on CRS326 got quickly very hot (almost 90°C)... ---

## Response 86
Good Morning, has anyone check this behaivour with the new version 6.45.1?Regards ---

## Response 87
It is bad, when things get broken, but it is not better, when they suddenly get "cured" by itself.My problem just suddenly disappeared by itself. Link has been up from friday afternoon and all packet loss has also disappeared. Nobody has done anything to this link or the devices, nobody has even been in the server room, but port flapping just ended and now everything is fine for fourth day in the row. I have not been able to find any outside factors that could have caused this change...It is possible to understand, why this kind of bugs can be hard to chase down - these kind of problems can take a very long time to reproduce... ---

## Response 88
On the latest version 6.45.1, the problem is still exist.The bundle ( CRS328-24P-4S+ and CRS317-1G-16S+ ) constantly (~ 5-7 minutes) flapping occursMikrotik, you can finally pay attention to the problem !!!Several tickets were created in the support, and not one received an answer on this issue.Many people suffer from this problem for many months.And there is still no official response.If necessary, I can provide access to the equipment.But start doing something already! ---

## Response 89
I have the same combination: CRS328-24P-4S+ and CRS317-1G-16S+. Yesterday I installed 6.45.1. Since that time the number of port flaps increased dramatically (from once every few days to 70 during the last 24 hours!)The CRS328 reports:Rx Error Events 2335The CRS317 reports:Rx FCS Error 2389Rx Error Events 2650What is happening here? Was something changed in 6.45.1 that affects this? ---

## Response 90
First, I love MikroTik products and RouterOS.It was a big mistake to buy the combination (1x CRS317-1G-16S+ and 2x CRS328-4C-20S-4S+).The expectation was that it should work fine, because it goes from the same manufacturer to the same manufacturer10G to 10G Fiber SFP+ Tests with RouterOS 6.45.1from CRS317-1G-16S+ to CRS328-4C-20S-4S+ flapping all day, about every 5min flappingfrom CRS317-1G-16S+ to CCR1072-1G-8S+, works fine - no flappingfrom CRS317-1G-16S+ to C4500X-32, works fine - no flappingfrom CRS328-4C-20S-4S+ to CRS328-4C-20S-4S+, works fine - no flappingfrom CRS328-4C-20S-4S+ to CCR1072-1G-8S+, works fine - no flappingfrom CRS328-4C-20S-4S+ to C4500X-32, works fine -no flappingHas anyone already found a solution that works with RouterOS. ---

## Response 91
It is funny to see that in your case it is the combination CRS317-1G-16S+ to CRS328-4C-20S-4S+ that is flapping too. I have some links from the CRS317 to server that work great. The same applies to other links on the CRS328. One would guess that Mikrotik would be able to track the problem easily as it occurs between these specific Mikrotik products? ---

## Response 92
It's might not be always like that. My problem lasted for weeks, then it suddenly disappeared and now emerged again after 10 days. Now it has been flapping again for a second day in the row. This kind of problems can take a lot of time if there's no ways to "accelerate" the process... ---

## Response 93
Our investigation has revealed that there might be a SFP+ compatibility issue with specific CRS317-1G-16S+ units when connected to other CRS3xx devices resulting in random link downs. Please, contact MikroTik support if you experience similar issue, we will verify it and arrange a repair if necessary. ---

## Response 94
Could you be more precise? Is there a way to identify the cause and what would be done during repair?Think about the folks which are running these switches now without flapping ports, but might run into problems as soon as CRS3xx are installed.We would like to know about the issue before the installation if possible. ---

## Response 95
Hello, i can't belive that anyone else have a working connection between the CRS317-1G-16S+ and the CRS3xx devices.We have three CRS317-1G-16S+ and over 10 CRS328-24P-4S+RM and no combination works without flapping.All of them are updated to 6.45.1. ( firmware also! ) and we used original Mikrotik DAC Cables.For Mikrotik it would be so easy to test and confirm this behaviour. Especially because it runs better with Switch OS!I hoped for so long that Mikrotik fix this, i won't send this devices back, but slowly i have no more option.Many people contact already the support and became no help since months...so your (becs) answer is no help at all ---

## Response 96
Our investigation has revealed that there might be a SFP+ compatibility issue with specific CRS317-1G-16S+ units when connected to other CRS3xx devices resulting in random link downs. Please, contact MikroTik support if you experience similar issue, we will verify it and arrange a repair if necessary.Is there something hardware specific related to that - in a way that some devices might not be affected at all? I have one 317 with problem while other has been without problems... ---

## Response 97
HahahaNot well done MikroTik - hardware related problem?And why when you switch to SwOS there is no such problem, only CRS3017 with RouterOS?Same hardware - different behavior = simply software bug! ---

## Response 98
Our investigation has revealed that there might be a SFP+ compatibility issue with specific CRS317-1G-16S+ units when connected to other CRS3xx devices resulting in random link downs. Please, contact MikroTik support if you experience similar issue, we will verify it and arrange a repair if necessary.The worst problems with port flapping (more that 70 per day) after the upgrade to 6.45.1 have been resolved after another reboot of the CRS317, but I still see port flaps (1 per day??). I guess that the issues I noticed where my UNMS monitoring the network often reports nodes not responding and returning after 1 -3 minutes and frequent drops of the internet radio streams are related too (no proof of that though).I reported my case to support (Ticket#2019071022007154). Let's see what comes out of this ---

## Response 99
CRS317 and CRS328 would be a great hardware combination and ideal for FTTX deployments.I hope that the error can be corrected with a software update.Both devices work great (in my case), if they are not connected to each other. ---

## Response 100
Yesterday connected the new one CRS317-1G-16S+On it, not one flap happened.On old one also connected to same CRS328-24P-4S+ for this time 88 times.And also noticed a strange thing.Interface status, last link up / down shows a strange time.The system time is correct, and in the status is wrong/strange time. ---

## Response 101
Yesterday connected the new one CRS317-1G-16S+On it, not one flap happened.So it could really be a hardware problemAnd also noticed a strange thing.Interface status, last link up / down shows a strange time.time is not right for me either. strange bug... ---

## Response 102
I thinkCRS326-24G-2S+RMandCRS125-24G-1Scontains same problem.SFP+ port in 1G mode - no problems.SFP+ port in 10G mode - problematic case even with Mikrotik DAC's.Update:problems raised when connecting two identical CRS326-24G-2S+RM devices with 10G DAC cable on SFP+ port.Not all of devices was affected in my case. Totally installed 4 devices, two of them are problematic (from more early batch). ---

## Response 103
Our investigation has revealed that there might be a SFP+ compatibility issue with specific CRS317-1G-16S+ units when connected to other CRS3xx devices resulting in random link downs. Please, contact MikroTik support if you experience similar issue, we will verify it and arrange a repair if necessary.@BECS: is there a way to identify if a CRS is affected? Does the serial numer tell if the device is affected? ---

## Response 104
Is there any update on this?can we buy mt hardware again or does this issue still persist?BR ---

## Response 105
as MK support said: "if possible, please, consider using CRS309-1G-8S+ as replacement in similar applications todecrease probabilityof encountering this issue." ---

## Response 106
as MK support said: "if possible, please, consider using CRS309-1G-8S+ as replacement in similar applications todecrease probabilityof encountering this issue."If this is the case - it is simply not good enough. I have 30 of these devices in an installation, and -all- of them are experiencing this issue. It has almost been a year since i reported this to mikrotik support, and all i have got - despite several attempts at getting updated answers - is "we have recreated the issue". ---

## Response 107
To all posters here, i'm afraid that this is a combination of HW and SW problem when there's a SFP+ connection between CRS 317 and CRS 328 and simply put, don't expect that anything's gonna change anytime soon.We've replaced CRS 328 with much more expensive Cisco devices and it works like a charm.So my advice would be:If you can replace one of the devices, DO IT!If your network won't fully utilize 10G just go 1G and figure replacement later.If you can't or don't want to replace a lot devices for an non-Mikrotik equivalent sell CRS 317 and buy CRS 309 instead. ---

## Response 108
I have to say that it seems that there are eithera) just a few CRS317 affectedor/andb) most buyers not aware of this issueor/andc) the amount of CRS317 <- 10G SFP+ -> CRS328 combinations are lowIt seems that MikroTik accepts the risk to repair/replace a few CRS317 and continues selling a device which does not provide 10G connections to CRS328. I would go with a) or b) when comparing the stock levels over time of online shops to the amount of posts and active people in this thread.Telling customers not to buy a product in order to reduce the probability of failure is another way to tell them to look for alternatives as Elliot did. ---

## Response 109
To all posters here, i'm afraid that this is a combination of HW and SW problem when there's a SFP+ connection between CRS 317 and CRS 328 and simply put, don't expect that anything's gonna change anytime soon.We've replaced CRS 328 with much more expensive Cisco devices and it works like a charm.So my advice would be:If you can replace one of the devices, DO IT!If your network won't fully utilize 10G just go 1G and figure replacement later.If you can't or don't want to replace a lot devices for an non-Mikrotik equivalent sell CRS 317 and buy CRS 309 instead.I can live with GE a while longer, and i'm sure there will be a replacement program at some point. I just wish MT would communicate a little more. What switches did you go for? Changing the poe switches would be a nightmare for us, but changing the crs328 would be less painful. You say you chose cisco, did you consider other options? If so, what were they? ---

## Response 110
Let's add some advice:use CRS317 with SwOS (no other ver than 3.7) instead of RouterOS ---

## Response 111
I think we have a similar problem.I'm testing the two just arrived Microtik CRS 317-1G-16+ switches.I have my computer connected on ETH 10/100/1000 management/data port and a 100mbs ethernet link connected throught a S-RJ01 SFP (listed in MicroTik compatibility listhttps://wiki.mikrotik.com/wiki/MikroTik ... lity_table).The connection is not stable and the ports seems to flap.The problem occours with SwitchOS but not with RouterOS.I've also tried the connection using two S-RJ01 SFP, one for my computer and one for the 100mbs link, but the problem is the same.No problem if I use a 1000mbs ethernet link, either using S-RJ01 SFP or directly attached to ETH 10/100/1000 management/data port.I have also done a third test:I've connected the 100mbs ethernet link to the eth 10/100/1000 management/data port of the first switch, than I connected the two CRS317 with a Cisco 10Gbs DAC SFP+, and I connected my computer to the eth 10/100/1000 management/data port of the second switch (avoiding the use of S-RJ01 SFP). The problem is the same.Also in this case, no problem if I use a 1000mbs ethernet link.It seems a problem with MicroTik Switch OS software.I'm using 2.9 SwitchOS version and 6.45.2 RouterOS. ---

## Response 112
Just use (mention above) SwOS 2.7 - 2.9 has a lot of bugs (see topicviewtopic.php?f=21&t=144031)p.s. never use management port for traffic on switch ---

## Response 113
To all posters here, i'm afraid that this is a combination of HW and SW problem when there's a SFP+ connection between CRS 317 and CRS 328 and simply put, don't expect that anything's gonna change anytime soon.We've replaced CRS 328 with much more expensive Cisco devices and it works like a charm.So my advice would be:If you can replace one of the devices, DO IT!If your network won't fully utilize 10G just go 1G and figure replacement later.If you can't or don't want to replace a lot devices for an non-Mikrotik equivalent sell CRS 317 and buy CRS 309 instead.I can live with GE a while longer, and i'm sure there will be a replacement program at some point. I just wish MT would communicate a little more. What switches did you go for? Changing the poe switches would be a nightmare for us, but changing the crs328 would be less painful. You say you chose cisco, did you consider other options? If so, what were they?We have our Mikrotik CRS 317 connected to couple of Cisco SF350-48P (48 port POE switch) via 10G SFP+. And another couple of NETGEAR GS752TXP connected via SPF+ too. In both cases no port flapping.I might add that we haven't thrown out CRS328 but we run only 1G on uplink due to port flapping when running port in 10G. It's pretty sad because otherwise it would be great value solution when you have one or two core CRS 317 switches connected to multiple site with CRS328. ---

## Response 114
I have to say that it seems that there are eithera) just a few CRS317 affectedor/andb) most buyers not aware of this issueor/andc) the amount of CRS317 <- 10G SFP+ -> CRS328 combinations are lowIt seems that MikroTik accepts the risk to repair/replace a few CRS317 and continues selling a device which does not provide 10G connections to CRS328. I would go with a) or b) when comparing the stock levels over time of online shops to the amount of posts and active people in this thread.Telling customers not to buy a product in order to reduce the probability of failure is another way to tell them to look for alternatives as Elliot did.Well I reported my issues to support and now will have to return the CRS317 for RMA. I can only hope that that will solve my issues. It remains a mystery that this apparently happens only between the CRS317 and CRS328. It still sounds as if the issue is partly caused by the CRS328 as well, otherwise it should occur between the CRS317 and other switches and/or 10G network cards.... ---

## Response 115
We are having massive issues with this. We have replaced the switch reset the config and its still shocking. Its 100% the CRS328's not the CRS317'sWe have also changed the optics i dont know how many times tried DAC's its still awful.see the picture this is less than 24hours up-time! ---

## Response 116
Its 100% the CRS328's not the CRS317'sMy experience tells otherwise - links between 317 and 326 are flapping, but when link from one 317 is connected to other 326, then flapping travels along with "sick" 317.I don't know about 328-24P-4S+, but 326 seems to have similar hardware (counting out PoE and amount of sfp+ ports) hence problems might be of similar nature. ---

## Response 117
Its 100% the CRS328's not the CRS317'sMy experience tells otherwise - links between 317 and 326 are flapping, but when link from one 317 is connected to other 326, then flapping travels along with "sick" 317.I don't know about 328-24P-4S+, but 326 seems to have similar hardware (counting out PoE and amount of sfp+ ports) hence problems might be of similar nature.I raised a case with support and they told me to RMA the CRS317. We will see what will happen when I get the CRS317 (or a replacement) back.... ---

## Response 118
Some can see the post, no port flapping, but other problems, viewtopic.php?f=2&t=150971Thanks! ---

## Response 119
Its 100% the CRS328's not the CRS317'sMy experience tells otherwise - links between 317 and 326 are flapping, but when link from one 317 is connected to other 326, then flapping travels along with "sick" 317.I don't know about 328-24P-4S+, but 326 seems to have similar hardware (counting out PoE and amount of sfp+ ports) hence problems might be of similar nature.I raised a case with support and they told me to RMA the CRS317. We will see what will happen when I get the CRS317 (or a replacement) back....I RMAd the device and the problem got acknowledged. The switch now has to be sent to Mikrotik for repair, which will take 6-8 weeks. That is a loooong time.I was told that replacing it will not solve the issue as even new models have the problem.Does this mean that Mikrotik knowingly continues to sell a faulty product? ---

## Response 120
Does this mean that Mikrotik knowingly continues to sell a faulty product?According to the findings within this thread and the information I received from our distributor: Yes. ---

## Response 121
Does this mean that Mikrotik knowingly continues to sell a faulty product?According to the findings within this thread and the information I received from our distributor: Yes.So almost one year after, we're at the same place....We've bought high-end devices from Mikrotik, hoping for full 10G support : Mikrotik Support ignores the sheer volume of testing done in this thread, reaching the conclusion that crs317 are the core issueThey should at least acknowledge the issue, recall crs317 from customers wishing to upgrade to CRS326-24S+2Q+RM for instance, and offer competitive pricing to compensate for the inconvenience of months without basic core fonctionality (10G support) ---

## Response 122
So, we just bought a faulty device too, I see! We got a second piece of CRS317-1G-16S+ and the interconnection between the two of them has exactly the problems discussed here - port flapping and packet loss. It seems to be much better when connecting the two devices on higher ports rather than on the lower ports, but still there is some small packet loss at 10Gb. Fortunately, we do not really need to have the two devices interconnected at a high speed at the moment (just for management), but this is a disappointment and if there was an alternative at the same price level, I would immediately return the device and buy something else. I do not like to work with unreliable hardware at all. Good to know we should be more careful when buying MikroTik next time.Fortunately, everything seems to work well on connections to the servers and even on the connection to the CCR1036-8G-2S+, which is the important factor at the moment. ---

## Response 123
Exact same problem here, but it is between any CRS317-1G-16S+. Have confirmed its present on ALL links between CRS317's, but not any link to any other device or switch.Initially I thought it was a cable fault, but we've changed cables, SFPs, etc. Same result. Once I found this thread we've come to realise its yet another example of a product flaw with no real information from the vendor and no solution in sight.Unfortunately for us, this was the final straw. We've just placed a order for a whole batch of Cisco kit and all of our Mikrotik gear will be coming out once it arrives. Now officially a dissapointed ex-Mikrotik user but looking forward to dealing with reliable products and actual engagement from the vendor when things aren't right with their product. ---

## Response 124
Hi!I just found this topic.Did you use the Mikrotik switch through an UPS(uninterruptible power supply - pure sinus-wave type) hardware ?If not, then this maybe a main problem - the power supply might have receiving some OVP/UVP/NOISE effects - causing the port flapping. ---

## Response 125
Hi!I just found this topic.Did you use the Mikrotik switch through an UPS(uninterruptible power supply - sinus wave type) hardware ?If not, then this maybe a main problem - the power supply might have receiving some OVP/OCP/SCP effects - causing the port flapping.In my case - yes, they were on a UPS. ---

## Response 126
Hi people! Looks like MT is finally stepping up. I got this email from them today.We got the Supout.rif from CRS317 that you just sent, looks like we didn't receive couple of emails that you sent previously(sic). But yeah, from Supout.rif we can see that CRS317 - 846C083E29E4 is indeed faulty and needs an hardware repair.We have become aware of a small number of CRS317-1G-16S+RM devices that may exhibit sporadic port flapping issues in certain usage scenarios. Since we are unable to pinpoint exact devices which could potentially exhibit this issue, we do not recommend replacing the device with an identical model, instead, we recommend using CRS309-1G-8S+IN ( 8x SFP+ ports) and CRS312-4C+8XG-RM ( 4x SFP+/10G Ethernet combo ports and 8x 10G Ethernet ports) as temporary replacements, until you receive repaired units through our RMA procedure. Please contact the seller to submit the device for warranty repair.You can submit Supout.rif's from any other affected CRS317's that you have and we will take a look at them and check if they need to be sent to RMA as well.Any of you guys gotten the same? ---

## Response 127
Hi!I just found this topic.Did you use the Mikrotik switch through an UPS(uninterruptible power supply - sinus wave type) hardware ?If not, then this maybe a main problem - the power supply might have receiving some OVP/OCP/SCP effects - causing the port flapping.In my case - yes, they were on a UPS.Hi!I read in other topics/people, the power supply comes with the mikrotik switch - has not the best "quality".I dont have any other idea what causing the port flapping. ---

## Response 128
If the problem is on power supply there will be port flapping always, no matter what OS is running.I have always port flapping when winning RouterOS (every single version on it) and never when running SwOS 2.7. We have a lot of 317 some connected to 326, 328 - different versions, all with SFP+ 10G running without single flap - all 317 running SwOS 2.7, other switches RouterOS or SwOS 2.9.This is SOFTWARE problem, but I'm sure that MikroTik don't know how to resolve it - just see how many they need to produce new version on SwOS, because 2.9 is hell of the bugs. ---

## Response 129
Hi!I just found this topic.Did you use the Mikrotik switch through an UPS(uninterruptible power supply - sinus wave type) hardware ?If not, then this maybe a main problem - the power supply might have receiving some OVP/OCP/SCP effects - causing the port flapping.In my case - yes, they were on a UPS.Hi!I read in other topics/people, the power supply comes with the mikrotik switch - has not the best "quality".I dont have any other idea what causing the port flapping.Can you elaberate on what quality parameters are not up to scratch? Also, the CRS317 has internal PSUs. Furthermore - as per my last post, they have admitted hardware faults in some CRS317. ---

## Response 130
If the problem is on power supply there will be port flapping always, no matter what OS is running.I have always port flapping when winning RouterOS (every single version on it) and never when running SwOS 2.7. We have a lot of 317 some connected to 326, 328 - different versions, all with SFP+ 10G running without single flap - all 317 running SwOS 2.7, other switches RouterOS or SwOS 2.9.This is SOFTWARE problem, but I'm sure that MikroTik don't know how to resolve it - just see how many they need to produce new version on SwOS, because 2.9 is hell of the bugs.I heard a story, RouterBoard copper RJ45 ports had the same strange port flapping issue - they could not solve/trace the problem: software upgrade/config changes.They tried as a last resort: After replacing the PSU the port flapping is gone.I am not sure about that. ---

## Response 131
It's very normal to have issues on copper port, because of potential difference generated by two sides of the cable. On twisted pair technology this must be no problem at all, but very often it is indeed.On the other hand optic ports have no such problem at all and power related problems are just fiction. ---

## Response 132
Hi!I just found this topic.Did you use the Mikrotik switch through an UPS(uninterruptible power supply - sinus wave type) hardware ?If not, then this maybe a main problem - the power supply might have receiving some OVP/OCP/SCP effects - causing the port flapping.In my case - yes, they were on a UPS.Hi!I read in other topics/people, the power supply comes with the mikrotik switch - has not the best "quality".I dont have any other idea what causing the port flapping.Can you elaberate on what quality parameters are not up to scratch? Also, the CRS317 has internal PSUs. Furthermore - as per my last post, they have admitted hardware faults in some CRS317.I'm not an expert about that.But you can compare:https://viva-telecom.org/13121/mikrotik ... rm/review/https://viva-telecom.org/13024/mikrotik ... rm/review/https://www.youtube.com/watch?v=KNDZZ5bD-wMCSR317 have some "custom build" PSU: 2x "OF-WT2402500" in one cage. ---

## Response 133
Since it sounds like its not an isolated issue (lol), I wont bother posting all my topology. However, We just deployed close to 10 317s, and are experiencing flapping on ONE of them. If that's useful to anyone. All 317 to 317 connections. ---

## Response 134
Hi I have a CRS317-1G-16S+ and have had or trouble ticket open with Mikrotik support for months. I am wondering if anyone has had success getting their unit repaired or replaced and if so was the problem resolved with the new/repaired unit. In my case it works with 1Gb links. 10 GB links flap attached to any CRS switch. I have on 10GB link that is stable to a security video server. ---

## Response 135
I am wondering if anyone has had success getting their unit repaired or replaced and if so was the problem resolved with the new/repaired unit.I have one RMA'd with my supplier. On week 2 of the 4-6 week turn around... ---

## Response 136
Has anyone tried the new CRS326-24S+2Q+RM Cloud Router Switch? I am wondering if it has the same port issues when connection at 10GB to other CRS3xx switches as the CRS317. ---

## Response 137
I am wondering if anyone has had success getting their unit repaired or replaced and if so was the problem resolved with the new/repaired unit.I have one RMA'd with my supplier. On week 2 of the 4-6 week turn around...My RMA (6 - 8 weeks) is only in the third week. I was told that a replacement would not make sense as new switches willhave the same problem.... So I am waiting for the repair while Mikrotik continues to selll defective equipment. ---

## Response 138
Hello, we have the new CRS326-24S-2Q+RM here and they worked 2 days without problems now.I have connected this device to an CRS328-24P-4S through Mikrotik DAC Cables and multiple Mikrotik S+R10 r2.We have also sent three of our CRS317-1G-16S+ back for RMA.regards ---

## Response 139
Has anyone tried the new CRS326-24S+2Q+RM Cloud Router Switch? I am wondering if it has the same port issues when connection at 10GB to other CRS3xx switches as the CRS317.All the sources indicate that is only that specific combination that this topic is affected, and maybe even then only some part of CRS317 affected.I have several CRS3xx connected to CRS317 no issues (with exception of some doggy DAC, that got replaced). ---

## Response 140
we got 4 new crs317 as replacement (they have been tested at our supplier) but they show the same behaviour....the recommended crs309 and 312 do not work as a replacement for us since we need the port density in that specific usecase. Has anyone given the new MikroTik CRS326-24S+2Q+RM a try?in an other place I would consider the MikroTik CRS312-4C+8XG-RM but I got cautious with MT in general after those issues. Has anybody seen this issue occur on any other of the mentioned devices or only on 317?BRAlex ---

## Response 141
Has anyone given the new MikroTik CRS326-24S+2Q+RM a try?Yes, got a CRS326-24S+2Q+RM yesterday (great device, many switch chip features).Works great in conjunction with CRS328-4C-20S-4S+RM.No more SFP+ 10G Port flapping (we have one CRS317-1G-16S+RM in RMA). ---

## Response 142
Hi.I also see problems with port flapping when using CRS317-1G-16S+RM <-> S+DA0001 <-> CRS326-24G-2S+RM.CRS317-1G-16S+RM <-> SNR-SFP+LR-2 <-> CRS326-24G-2S+RM the problem is present.All ports are switched to 1G now. But, on one port after turning on the RX / TX Flow Control option to auto, we observed RX Errors at first time. Yesterday i reset the error counter and so far no errors on this port with 10G. Keep watchingWith CRS317-1G-16S+RM <-> S+DA0001 <-> RB4011iGS+RM everything is ok on 10G: no link downs, no rx errors. ---

## Response 143
Hi, we can confirm that CRS328-24P-4S+ in combination with CRS312-4C+8XG show the exact same problematic port flapping behavior (RouterOS & FW v6.45.6) as the CRS317-1G-16S+. The exact testing scenario is:- 2x CRS312-4C+8XG (both new)- 2x CRS328-24P-4S+ (1 new, 1 used but "working as expected" from our supplier)- The CRS328s are connected with SFP+ DACs to the CRS312 SFP+ combi ports- The test scenario ran 9 days in an air-conditioned environmentThe outcome is attached to this post. Some observations:- Both CRS328 show just a few link downs (<20 Link Downs), there is no behavioral difference between the new and the used CRS328- The CRS312s show different results 50 vs. 1129 Link Downs to the same CRS328- The screenshot was taken on the Oct. 10th, the Last Link Down Time information do contain wrong information.We also had two new CRS326 connected (via SFP+) to the CRS328 and CRS312 in question whichdid notshow any port flappings during the testing period. This test is a consequence of the recommendations done by MikroTik to use the CRS312 and CRS326 as replacement for the flapping CRS317. In our tests we see that at least the CRS312 have the exact same issue as the CRS317s. There is still no evidence that the CRS328 is not part of the problem.Conclusion:- CRS312-4C+8XG combined with CRS328-24P-4S+ do have flapping SFP+ connections- We did not receive any feedback from Mikrotik regarding this issue. Therefore, we will stop our tests of Mikrotiks problematic network devices.br, nicoh ---

## Response 144
I can confirm this as well.Hi, we can confirm that CRS328-24P-4S+ in combination with CRS312-4C+8XG show the exact same problematic port flapping behavior (RouterOS & FW v6.45.6) as the CRS317-1G-16S+. The exact testing scenario is:- 2x CRS312-4C+8XG (both new)- 2x CRS328-24P-4S+ (1 new, 1 used but "working as expected" from our supplier)- The CRS328s are connected with SFP+ DACs to the CRS312 SFP+ combi ports- The test scenario ran 9 days in an air-conditioned environmentThe outcome is attached to this post. Some observations:- Both CRS328 show just a few link downs (<20 Link Downs), there is no behavioral difference between the new and the used CRS328- The CRS312s show different results 50 vs. 1129 Link Downs to the same CRS328- The screenshot was taken on the Oct. 10th, the Last Link Down Time information do contain wrong information.We also had two new CRS326 connected (via SFP+) to the CRS328 and CRS312 in question whichdid notshow any port flappings during the testing period. This test is a consequence of the recommendations done by MikroTik to use the CRS312 and CRS326 as replacement for the flapping CRS317. In our tests we see that at least the CRS312 have the exact same issue as the CRS317s. There is still no evidence that the CRS328 is not part of the problem.Conclusion:- CRS312-4C+8XG combined with CRS328-24P-4S+ do have flapping SFP+ connections- We did not receive any feedback from Mikrotik regarding this issue. Therefore, we will stop our tests of Mikrotiks problematic network devices.br, nicoh ---

## Response 145
Anyone tested the CRS326-24S+2Q+RM yet? ---

## Response 146
I changed 2 317 with 2 326-24+The link with all 328 and between 326-24+ are now fine @10GbpsOne link with 326-24G still flap and needed to be set @1GpbsBetter then before, but seems to be not fully resolved.Alessandro ---

## Response 147
Received my CRS-317 back from RMA. The problem was NOT fixed, still produces FCS Errors immediately when configuring the link at 10G with a CRS-328. ---

## Response 148
I am having the same problem with the CSS326-24G-2S+ on the SFP+ ports.I am connecting a workstation with an Intel X520 10Gb card and Fiberstore Cisco SFP-10G-SR SFP+ modules.My Linux dmesg is full of this:ixgbe 0000:42:00.1 enp66s0f1: NIC Link is Downixgbe 0000:42:00.1 enp66s0f1: NIC Link is Up 10 Gbps, Flow Control: RX/TX ---

## Response 149
Hello, we have received our CRS317-1G-16S+ back from rma on Oct, 10th since then no port flapping.We have also running the new CRS326-24S+2Q+ since Aug, 23 and there are no port flapping.regards ---

## Response 150
After issuing RMA and receiving new unit it seems like this issue has been resolved - there has been no link downs or any sort of data errors for over a month of uptime... ---

## Response 151
I am still waiting for the RMA of my CRS317: after 8 weeks I asked the shop and they checked with MT: it is waiting for parts and no idea when they will arrive. I am quite disappointed by this whole story. What a mess!!The shop sent me a new CRS317 that I installed today. No flaps yet but in only 2 hours I see 15 FCS errrors and 2 RX error events, so I am not hopefull. ---

## Response 152
I am still waiting for the RMA of my CRS317: after 8 weeks I asked the shop and they checked with MT: it is waiting for parts and no idea when they will arrive. I am quite disappointed by this whole story. What a mess!!The shop sent me a new CRS317 that I installed today. No flaps yet but in only 2 hours I see 15 FCS errrors and 2 RX error events, so I am not hopefull.The new CRS317 I received to test has port flapping too: 5 - 10 times a day in addition to the FCS and RX errors.My original CRS317 is apparently still waiting for parts. I am now waiting for the repair for over 3 months and counting.Does anybody know of a workaround that makes the link stable (the switches are connected by means of a short (50cm) dac.My conclusion: don't buy a CRS317 when you want to connect to a CRS328 ---

## Response 153
Just installed CRS317-1G-16S+ and connect them with Mikrotik 10G modules to 5x CRS328-24P-4S+ (RouterOS 6.45.7). Port flapping on all links every 3-8 minutes.I found this theme and now I don't know what to do. ---

## Response 154
Hi allI recently got a reply from MT after sending them the support files from affected switches. The said that I should start an RMA process with my vendor. I did and got the new qsfp switch instead. Has worked flawlessly so far. ---

## Response 155
I have a network connected via switches as follows:1 unit CRS317-1G-16S+ as core5 unit CRS328-24P-4S+, 1 at the same cabinet as core, while the other 4 at each satellite buildings in one campusThe satellite buildings are all connected via singlemode fiber, and I installed 10G LR SFP+ on each.All running RouterOS v6.45.7, Firmware updated to the latest.I have been noticing port flapping on all the SFP+ ports connected to the campus switches, intermittently, sometimes every minute, sometimes every several minutes. I would get link downs to the hundreds each day. I tried changing fiber patch cords, but still the same.A post here suggested I switched the CRS317 to run SwOS. Updated it to 2.10 (from 2.7), been running flawless without any port flapping (checked on each of the satellite switches) for 3hrs already.All CRS328 switches are still on RouterOS at the moment. ---

## Response 156
I posted several times above:This problem persists only on CRS317 running RouterOS (any version).If you don’t want port flapping at all, use SwOS 2.7 or 2.10 (don’t even try 2.8, 2.9).We have many 317 in different configurations with heavy traffic, hundreds of vlans, many of them connected with 10G links to CSS326, CRS326, CRS328 (and many more 4011, 1009, other vendor switches and routers), WITH NO ANY PORT FLAPPING! ---

## Response 157
I posted several times above:This problem persists only on CRS317 running RouterOS (any version).If you don’t want port flapping at all, use SwOS 2.7 or 2.10 (don’t even try 2.8, 2.9).We have many 317 in different configurations with heavy traffic, hundreds of vlans, many of them connected with 10G links to CSS326, CRS326, CRS328 (and many more 4011, 1009, other vendor switches and routers), WITH NO ANY PORT FLAPPING!maybe some of us are not interested in SwOS ?adding unnecessary complexity to existing network setups to circumvent hardware/software bugs is your choice, not mine.CRS317 are sold as 10G switches, they have to work 10G without kludges ---

## Response 158
Follow-up:Up till now all are running without flapping, except for one, once at 3am. Will continue to monitor this.Since after changing to SwOS, the flapping mostly stopped, very good indication that this is a software bug. Should be able to fix. ---

## Response 159
I posted several times above:This problem persists only on CRS317 running RouterOS (any version).If you don’t want port flapping at all, use SwOS 2.7 or 2.10 (don’t even try 2.8, 2.9).We have many 317 in different configurations with heavy traffic, hundreds of vlans, many of them connected with 10G links to CSS326, CRS326, CRS328 (and many more 4011, 1009, other vendor switches and routers), WITH NO ANY PORT FLAPPING!As SwitchOS has very limited management capabilities (web only) and not even HTTPS it is a too limited platform to be taken serious. I do not want any plaintext management traffic in my network. Once they support HTTPS I could consider SwitchOS. I only need very basic functionality anyway but this silly HTTP(S) limitation stops me from even considering SwitchOS.I still don't understand why SwitchOS could work correctly where RouterOS does not: Mikrotik admits that there is a hardware problem on the CRS317, so why can SwitchOS work correctly when there is a hardware problem? If they could fix it in SW in SwitchOS why do they not fix it in RouterOS? ---

## Response 160
I just answered on those that ask "did you manage to resolve this problem".Everybody, of course, has own needs and requirements on same hardware - MikroTik must work hard to fix this.p.s. forums like this one is the place to be, before buy some equipment.cheers ---

## Response 161
RouterOS 6.46 released. In the changelog:*) crs3xx - improved switch-chip resource allocation on CRS317-1G-16S+, CRS309-1G-8S+, CRS312-4C+8XG, CRS326-24S+2Q+ devices;Would this solve the port flapping issue? Has anybody tested it? ---

## Response 162
RouterOS 6.46 released. In the changelog:*) crs3xx - improved switch-chip resource allocation on CRS317-1G-16S+, CRS309-1G-8S+, CRS312-4C+8XG, CRS326-24S+2Q+ devices;Would this solve the port flapping issue? Has anybody tested it?I noticed this comment too. I therefore upgraded my temporary CRS317 half an hour ago. Should know more tomorrow, but I am not optimistic.I had to return my own CRS317 as it required repair according to Mikrotik. So I would assume that this firmware upgrade does not solve the issue.... The changelog is not very informative so I cannot judge what is fixed. But resource allocation does not seem to be related to RX and FCS errors which seemed to be related to the flaps.B.t.w. I am seeing 6 RX and 4 FCS errors within 40 minutes after the upgrade.... ---

## Response 163
I have CRS328-24P-4S+ and CRS317-1G-16S+ on the shelf. In the next 1-3 days, I will test RouterOS 6.46 on them in 10G. ---

## Response 164
I have CRS328-24P-4S+ and CRS317-1G-16S+ on the shelf. In the next 1-3 days, I will test RouterOS 6.46 on them in 10G.Don't bother testing: it took 1.5 hours after the upgrade (on both CRS328 and CRS317) for the first flap to occur on my lightly loaded network ---

## Response 165
I have CRS328-24P-4S+ and CRS317-1G-16S+ on the shelf. In the next 1-3 days, I will test RouterOS 6.46 on them in 10G.Don't bother testing: it took 1.5 hours after the upgrade (on both CRS328 and CRS317) for the first flap to occur on my lightly loaded networkLess than a full day ater: 29 flaps... routerOS 6.46 does not solve the issues with port flapping ---

## Response 166
The only way to fix this problem is to send your devices back to your distributor! This is not a software bug!!!We have serveral CRS317, CRS328 and the new CRS326 and they worked now without port flappings or other problems.Now they running with RouterOS 6.46 since last friday.regards ---

## Response 167
The only way to fix this problem is to send your devices back to your distributor! This is not a software bug!!!We have serveral CRS317, CRS328 and the new CRS326 and they worked now without port flappings or other problems.Now they running with RouterOS 6.46 since last friday.regardsLast Friday I received my CRS317 back from repair (took "only" 4 months) and now I have not seen any port flaps (0 link downs) nor any receive error counters increase (FCS errors not RX error events) that I used to see. So the repair was successful.It is ridiculous to see that it took Mikrotik 4 months for a repair but it at least worked out well. I can now listen for a full day to streaming radio without disconnects, Would I recommend Mikrotik to friends? Don't think so.... ---

## Response 168
Hi, want to share small storyI have two CRS326, both devices powered from APC UPS, both CRS's are out of warranty.My problem was:- port flapping on both devices- Both CRS's with DAC cable on SFP+ interfaces won't work at all.- High CPU temperature, 76-78 degrees in celsius.I bought two 24V PSU from Mikrotik, those PSU's are for CCR, not for CRS!After few hours of DIY I have installed PSU and 24V fan to both devices.Results:- Link via SFP+ with DAC cable between both Mikrotiks, no issues at all!- Regarding flapping: I see link down/up only at the morning and at the evening, only when computer is turnted to on/off. Before modification - up/down happens lot of times during a day.- CPU temperature dropped to 43-45 degrees in celsius due to installed fan.Notes:- CCR PSU is too long to fit to CRS, 7mm of pcb have to be cut. There is enough space to do that.- PSU C14 inlet socket is also to big to fit to hole in CRS.- Soldering is needed: PSU cable is too short, routerboard PCB contains no internal connector for power.Strictly do not reccomend to do that, you can damage CRS. ---

## Response 169
This is interesting. So the port flapping might be just because of noisy PSU? Should be quite easy to verify, put CRS on external clean linear lab powersupply and see if it fixes the problem, or maybe try adding a few ferrites on the wires from original PSU if that would make a difference.... that is as long as yours is out of warranty. I RMA'd my CRS and got replacement that's not flapping ports anymore, so can't test it. ---

## Response 170
I have soldered fan wires directly to PSU 24V outlet. Fan could also produce noise.Unfortunately both CRS are far enough from me, can't do testing with lab PSU.linkdowns.txt - events for few last days, 10/100M speed - should be PC NIC in low power mode, I think.During transition between power modes the network adapter might lose connectivity for a short time.Situation with new PSU is definitely better! ---

## Response 171
An update from my side:We bought CRS326-24S+2Q to replace the CRS317 devices. Mikrotik support told us the flapping problem between CRS317 and CRS328-20S-4C-4S+ is caused by the CRS317. That was over 1 year ago. They also told us to buy other devices but no CRS317. That means over one year later they still sell the faulty devices!! Back then I told MT support that I don't think the problem is the CRS317 but the CRS328....Now I testet the CRS328 <-> CRS326-24S+2Q and of course I have flapping again. 696 link downs in 3 days. Well done Mikrotik!!We decided to switch to another vendor. That was too much. Not only the problem itself but also the handling. ---

## Response 172
An update from my side:We bought CRS326-24S+2Q to replace the CRS317 devices. Mikrotik support told us the flapping problem between CRS317 and CRS328-20S-4C-4S+ is caused by the CRS317. That was over 1 year ago. They also told us to buy other devices but no CRS317. That means over one year later they still sell the faulty devices!! Back then I told MT support that I don't think the problem is the CRS317 but the CRS328....Now I testet the CRS328 <-> CRS326-24S+2Q and of course I have flapping again. 696 link downs in 3 days. Well done Mikrotik!!We decided to switch to another vendor. That was too much. Not only the problem itself but also the handling.I had the flapping problem on the Crs317/CRS328 combo too. I had my CRS317 repaired (took them 4 months, unbelievable) but the link between the 2 is now absolutely stable: I just checked and the link is has now been up since Dec 18 (when I rebooted both switches for a SW u[date). So it shows that the CRS317 was at least part of the problem. It might quite well be that the CRS326-24S+2Q has the same problems as the CRS317... But you can not rule out the CRS328 either.I don't know what was done to my CRS317 but it now definitely works ok.Handling of problems is indeed not good at Mikrotik. No information, terrible repair time. ---

## Response 173
Has anybody introduced the new 48port CRS354-48G-4S+2Q+RM switch into the loop?Are there any flapping issues with that one? ---

## Response 174
HelloOne of my partner gave me the link to that thread when I was looking for a 10G Mikrotik switch.I'm still interested in CRS317 switch. What I need is just the following things:* no crash* RouterOS as I need kind of integration with other things (at least via CLI)* no port flapping* VLAN mapping/translation on each port. Hardware based* dual power source* most links will be fiber connections at 10G, but I predict mixture of 1G/10G fiber connections with none or few copper 1G connectionsI have no other Mikrotik devices. But, If everything works well, I may add more CRS317 or CRS326.If problem really related to combination of CRS317 and CRS326 I might avoid it. But, there were people saying it is same issue even with recommended CRS309.Could you please give me (other readers) what is the status with this issue?Thank you in advance for your information!PS CSR312 doesn't fit as it has only 4SFP+ cages. CSR309 doesn't fit as it has only one power source (maybe, there is a possibility to use POE-IN + power supply to achieve redundant power configuration?) ---

## Response 175
HelloOne of my partner gave me the link to that thread when I was looking for a 10G Mikrotik switch.I'm still interested in CRS317 switch. What I need is just the following things:* no crash* RouterOS as I need kind of integration with other things (at least via CLI)* no port flapping* VLAN mapping/translation on each port. Hardware based* dual power source* most links will be fiber connections at 10G, but I predict mixture of 1G/10G fiber connections with none or few copper 1G connectionsI have no other Mikrotik devices. But, If everything works well, I may add more CRS317 or CRS326.If problem really related to combination of CRS317 and CRS326 I might avoid it. But, there were people saying it is same issue even with recommended CRS309.Could you please give me (other readers) what is the status with this issue?Thank you in advance for your information!PS CSR312 doesn't fit as it has only 4SFP+ cages. CSR309 doesn't fit as it has only one power source (maybe, there is a possibility to use POE-IN + power supply to achieve redundant power configuration?)If you only need 10G go for the CRS317: it works well connected to anything but the CRS328 (and possibly the CRS326).Since the repair my CRS317 - CRS328 link has been rock solid too. That connection was the only one with flapping. It is now up since Dec 18 without any issues whatsoever. I am happy.I don't know what was done to fix the switch, but new switches may still have the same problem: at least the temporary replacement for my own CRS317 had the same flapping problem. New CRS 317 switches may still have the problem connected to other Mikrotik switches like the CRS328. It would be nice if Mikrotik could comment on this. It is a shame that the repair took 4 months! ---

## Response 176
...If you only need 10G go for the CRS317: it works well connected to anything but the CRS328 (and possibly the CRS326).Since the repair my CRS317 - CRS328 link has been rock solid too. That connection was the only one with flapping. It is now up since Dec 18 without any issues whatsoever. I am happy....Sounds good.Do you have mixture of 1G/10G connections or 10G connections only? Via SFP+ modules or DAC? ---

## Response 177
...If you only need 10G go for the CRS317: it works well connected to anything but the CRS328 (and possibly the CRS326).Since the repair my CRS317 - CRS328 link has been rock solid too. That connection was the only one with flapping. It is now up since Dec 18 without any issues whatsoever. I am happy....Sounds good.Do you have mixture of 1G/10G connections or 10G connections only? Via SFP+ modules or DAC?Right now I only have some 10Gb DACs (FS.com) and an S+RJ10 in the switch, but I used to have some 1Gb Fiber modules to an older (now removed) 1Gb switch. Worked perfectly fine. I never tried 10Gb fiber as I had no use for it. ---

## Response 178
CRS326-24S+2Q+RM @10gbps have the same problem of crs317.. port flapping, link down.. you have 24 ports but you have to do a lottery moving your link, hoping to found a working solution.. (yesterday: 10Gbps Dac to hpe server nic, on port 5 NO LINK, on port 7 flapping link, on port 9 OK).. very disappointed! ---

## Response 179
We have the same issues CRS328 to servers with 10Gtek X520 cards. 1G is fine, but 10G is unstable. We have 4 brand new CRS328 that do the same thing. Its very disappointing as we bought them so we could switch 10G traffic. Not sure what to do now as we need reliable 10G switching. Any recommendations? ---

## Response 180
Upgrade to RouterOS to last versionUpdate firmware to last version System->Routerboard->UpgradeRebootSwitch to SwOSUpgrade to last versionUse it with no flapping ---

## Response 181
Switch to SwOSUse it with no flappingok, you can also buy another vendor switch, but I don't think that it was the question...Hey Mikrotik guys, where are you? ---

## Response 182
Hey Mikrotik guys, where are you?This is user forum. Support replies in some topics occasionally, but there's not guarantee they reply to your particular message. If you are looking for an official reply you should contact support@ and/or you supplier/distributor directly. ---

## Response 183
This is user forum. Support replies in some topics occasionally, but there's not guarantee they reply to your particular message. If you are looking for an official reply you should contact support@ and/or you supplier/distributor directly.I think that after one year and an half, many support request, some device repair, some device went in the bin, and a lot of devices with the same problem, mikrotik guys could pubblicaly response and give us an idea if they want to continue seriusly making routerOs switches or not. ---

## Response 184
Switch to SwOSUse it with no flappingok, you can also buy another vendor switch, but I don't think that it was the question...Hey Mikrotik guys, where are you?Very funny - for you MikroTik = RouterOS ??!?Guy ask for solution, I gave to him one - it's not universal, but if he need basic switch capabilities it work. ---

## Response 185
for you MikroTik = RouterOS ??!?onestly, yes. ---

## Response 186
Using Switch OS is not a solution. Its possibly a bandaid, I don't want to be pushing 10G of data hoping that works. Need a reliable fix. ---

## Response 187
I'm also having some severe port flapping issues with a bonded 20G (2 DAC SFP Plus cables) between a CRS328 and a CRS317 switch.Need to use RouterOS on both because I would really like to have OSPF running on both switches. (i am aware of the routing performance of these switches, no need to comment on this).So, switching to SWOS is not an option for me.Need a reliable fix for this as well. ---

## Response 188
I'm also having some severe port flapping issues with a bonded 20G (2 DAC SFP Plus cables) between a CRS328 and a CRS317 switch.Need to use RouterOS on both because I would really like to have OSPF running on both switches. (i am aware of the routing performance of these switches, no need to comment on this).So, switching to SWOS is not an option for me.Need a reliable fix for this as well.Mail support at Mikrotik with the support files for both switches. They will probably tell you that the CRS317 needs a repair. In that case prepare for a long wait: it took them 4 months in my case if I remember correctly..... My switches now link perfectly fine: the link has been up since Dec 18: more than 5 months ---

## Response 189
I'm observing the same flapping issueI hae noted that temperature is quite high and FAN are at 0 RPM. Checking with snmp the fan are switched some time.but not enough to cool down the CRS317 with 5 SFP+ installed. the SFP module temperature are between 55 and 60 °C and they start to flap when reach 55 .... and they are mikrotik too ....question I noted from command line I can set fan trhreshould but noted that nothing change.Mikoritk manual does not explain the commands so I'm quite trying to set some valut but would be good to get some advice.thank you ---

## Response 190
I have the port flapping problem with my recently purchased CRS328-24P-4S+. The switch has 3 10Gig links plugged in to it. Two of them are 1m dac connections and work fine.The 3rd connection is a lc multimode fiber connection that is 21.5m in length (1.5m patch, 5m patch, and 15m mm fiber between locations). This fiber connection drops every few minutes and immediately reconnects. Also, I can make it drop the connection just by asking SWoS 3.11 to do a backup. The other two connections don't drop periodically, or exhibit this behavior when asking for a backup... they're reliable. It's only the mutimode fiber that has the problems.For the connection that doesn't work, I've proved that the switch is the problem by using the fiber link to directly connect two computers. I'm even using the same transceivers. When I do that, everything works perfectly (and in fact that was how the customer had originally setup their network... just a single 10gig fiber connection between the two computers).....very frustrated..... ---

## Response 191
Same problem on config:- CRS317- CRS328- DAC SFP+viewtopic.php?f=3&t=165650&p=815054Mikrotik why you provide BROKEN hardware? ---

## Response 192
You have to change switch port until you find the correct sequence that not flap.. good luck!Mk switch @10gbps are not reliable at the moment ---

## Response 193
Hello. I read this post and checked my fiber pop.CCR1009CRS317 where are connected (all via 10G SFP cables), CRS328.on ten switch, one has sfpplus1 flapping as described.I will try changing the DAC then I will RMA the switch.lastest long-term on it. ---

## Response 194
I have made further investigations.I have 10 CRS328 connected to a CRS317.the only CRS328 that have issues are:5 CRS with 5mt MT DAC, with 5mt MM fibers.a lot of CRS errorstwo of them flaps, the other 4 dont flap.I tried to fix everyone of them at 1G to see if it flaps again or give me errors.I see a lot of FCS errors, it seems that the cable is bad... it is possibile 5 5mt MT cables are all faulty?The other CRS are connected via a mix of 1MT / 3MT DAC from MT with 0 flaps and 0 errors. ---

## Response 195
Quick Question : If I try to switch to SWOs to reduce port flapping, How will I know if it's solved? Is there a log event for port down as in RouterOS? ---

## Response 196
Quick Question : If I try to switch to SWOs to reduce port flapping, How will I know if it's solved? Is there a log event for port down as in RouterOS?You can check the logs on the CRS328 side.I'm also having port flapping problems on my CRS317 and 4 units of CRS328 pairs. Right now I have the CRS328 connected to a CRS354, no flap yet, almost 12hrs.Seems the problem is at CRS317. ---

## Response 197
CRS326-24G-2S+ 85 degrees steady temperatureSFP+ 10G optical 60 degrees steadyRack temperature 24 degrees steadyCpu usage 1-3%Can´t begin to imagine where temperature will go if cpu usage gets higher ---

## Response 198
I upgraded the switch with the latest long-term and it no longer flaps!Finger crossed... 12h without a single flap :D ---

## Response 199
Update, just 1 switch in 4, resumed port flapthe other went flawlessy ---

## Response 200
Subscribing, I have a CRS326-24G-2S+RM that port flaps on the SFP+ port constantly. I've updated to beta 7 and tried blowing a fan across the SFP+ ports to resolve. I've also swapped ports between the DACs. ---

## Response 201
I had high hopes for this switch, but looks like I may have to switch to UniFi. I can't have the SFP+ port randomly dropping several times a day. ---

## Response 202
I solved most of the flaps with latest long-term and latest firmware on it. ---

## Response 203
I have a CRS328-24P-4S+RM that flaps on two of the four SFP+ ports. My CRS317-1G-16S+RM has no flapping issues. Both switches running SwOs 2.13. ---

## Response 204
try upgrading the routerboot inside routeros, install the latest bugfix, upgrade routerboot, then reboot with switchos. ---

## Response 205
try upgrading the routerboot inside routeros, install the latest bugfix, upgrade routerboot, then reboot with switchos.The documentation says:RouterBOOT is responsible for starting RouterOS in RouterBOARD devices.Does it also play a role in booting SwOs? ---

## Response 206
Yes, because in another changelog, I dont remember where, told to start routerOS, upgrade routerboot, then restart in sw os.I have a 326 that had tx drop, and the suggestion was to upgrade routerboot to the latest, then restart sw0s. now it is working perfectly with 0 tx drops. ---

## Response 207
Yes, because in another changelog, I dont remember where, told to start routerOS, upgrade routerboot, then restart in sw os.I have a 326 that had tx drop, and the suggestion was to upgrade routerboot to the latest, then restart sw0s. now it is working perfectly with 0 tx drops.Nice, I'm going to try that. Thanks :) ---

## Response 208
try then let me know.on a CRS326 with 2.12 I had a lot of tx drops.upgraded routerboot from 6.48.3, then put the sw os 2.13problems resolved. ---

## Response 209
Same issue here, flapping since v6, updated to latest v7, no dice. Still flapping. Solution is to switch to 1gb instead.Screenshot 2022-06-03 131526.png[Router] CCR2004-16G-2S+ RouterOS v7.2.3 Generic SFP-10G-T (fs.com) <---> CAT6 LAN cabling <---> [Switch] CRS309-1G-8S+ RouterOS v7.2.3 Generic SFP-10G-T (fs.com) ---

## Response 210
Hi guysi know this is an old threadbut we have the same problem with switch CRS328 on the 4 ports sfp+ ports flapping all the time.. if we plug the same gbic for 10gbps on our switch CRS305 it link 10gbps normal with no issue at all and they work normally, but we need to expand and we bought 2 CRS328 switches.. and soon as we remove the gbics from the crs305 and plug them on the CRS328 it keeps flapping.. we tried upgrading latest long-term version RouterOS .. stable version, older versions and none work.. it seems to be a problem on the CRS328..btw we also have.. other CRS317 RUNNING flawless without erros on other networks connected runnins switchOS mode.. with mikrotik CCRs all connected on 10gbps and also Dell Servers with SFP+ nic.. and no errors at all.. some CCRs connected 20miles distance linked 10g normally. soon as we try to put CRS328 up.. it keeps flapping ports..Hello. I need to buy two 24 port switches and I have to choose between CRS326 and second hand Cisco 2960G, the price is the same. If I take CRS326 it will be used with RouterOS for access switch. From what I read in forum, SwOS is not ready for "in production" setups and this is the reason to choose CRS326 instead of CSS326.My question is - if I use only 100Mbps and 1000Mbps (random mix of ports, PCs, VoIP phones etc.) connections and not 10G connections, the problem with port flapping will be present or not?According to all posters here, the problem presents itself only in connection with CRS317 and 10G SFP+. So it will not happen to your setup. ---

## Response 211
latest long-term version RouterOSIt was fixed in 7.4, which is “stable,” not LTS. ---

## Response 212
CRS328-24P <-> CRS312 with 1m Mikrotik DAC, port flapping every 2 hours. both switch running Stable 7.6, herebelow are the sfp+ 3 and sfp+ 4 link down ( sfp3+ and sfp+4 connected to CRS328 with LAG)
```
[brg3466@CRS312] > log print where message~"combo"
 dec/28 02:56:00 bridge,info hardware offloading activated on bridge "bridge1" po
rts: combo1,combo2
 dec/28 02:56:01 interface,info combo1 link up
 dec/28 02:56:01 interface,info combo3 link up (speed 10G, full duplex)
 dec/28 02:56:01 interface,info combo1 link down
 dec/28 02:56:01 interface,info combo4 link up (speed 10G, full duplex)
 dec/28 02:56:01 interface,info combo1 link up (speed 10G, full duplex)
 dec/28 02:56:02 interface,info combo3 link down
 dec/28 02:56:02 interface,info combo3 link up (speed 10G, full duplex)
 dec/28 02:56:02 interface,info combo1 link down
 dec/28 02:56:03 interface,info combo1 link up (speed 10G, full duplex)
 dec/27 20:10:42 interface,info combo3 link down
 dec/27 20:10:42 interface,info combo4 link down
 dec/27 20:11:38 interface,info combo4 link up (speed 10G, full duplex)
 dec/27 20:11:39 interface,info combo3 link up (speed 10G, full duplex)
 dec/27 21:11:22 interface,info combo4 link down
 dec/27 21:11:22 interface,info combo4 link up (speed 10G, full duplex)
 dec/28 08:12:09 interface,info combo3 link down
 dec/28 08:12:09 interface,info combo3 link up (speed 10G, full duplex)
 dec/28 08:46:29 interface,info combo3 link down
 dec/28 08:46:29 interface,info combo3 link up (speed 10G, full duplex)
 dec/28 10:59:42 interface,info combo3 link down
 dec/28 10:59:42 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 00:32:18 interface,info combo4 link down
 dec/29 00:32:18 interface,info combo4 link up (speed 10G, full duplex)
 dec/29 00:57:25 interface,info combo3 link down
 dec/29 00:57:26 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 05:35:05 interface,info combo3 link down
 dec/29 05:35:05 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 06:11:54 interface,info combo3 link down
 dec/29 06:11:54 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 07:29:38 interface,info combo3 link down
 dec/29 07:29:38 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 12:03:06 interface,info combo4 link down
 dec/29 12:03:07 interface,info combo4 link up (speed 10G, full duplex)
 dec/29 12:03:07 interface,info combo3 link down
 dec/29 12:03:07 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 12:05:52 interface,info combo3 link down
 dec/29 12:05:52 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 12:06:13 interface,info combo3 link down
 dec/29 12:06:13 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 12:06:19 interface,info combo3 link down
 dec/29 12:06:19 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 12:17:12 interface,info combo3 link down
 dec/29 12:17:12 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 16:19:47 interface,info combo4 link down
 dec/29 16:19:47 interface,info combo4 link up (speed 10G, full duplex)
 dec/29 16:19:48 interface,info combo3 link down
 dec/29 16:19:48 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 16:30:16 interface,info combo3 link down
 dec/29 16:30:16 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 16:30:54 interface,info combo3 link down
 dec/29 16:30:55 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 16:40:35 interface,info combo4 link down
 dec/29 16:40:36 interface,info combo4 link up (speed 10G, full duplex)
 dec/29 16:43:24 interface,info combo3 link down
 dec/29 16:43:24 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 16:44:10 interface,info combo3 link down
 dec/29 16:44:10 interface,info combo3 link up (speed 10G, full duplex)
 dec/29 17:04:24 interface,info combo3 link down
 dec/29 17:04:25 interface,info combo3 link up (speed 10G, full duplex)

---
```

## Response 213
CRS328-24P <-> CRS312 with 1m Mikrotik DAC, port flapping every 2 hours. both switch running Stable 7.6Please don't hijack unrelated threads. We are clearly not talking about cases like yours here. That should be obvious even to a newbie: nowhere in the world does "every 2 hours" qualify as "severe."(If you saw this condition happen in the pre-7.4 builds, you'd know what "severe" was!)Post a new thread, and include any details that might help. Logs, switch configs, etc. Remember: if you knew all the details that were relevant, you'd have the problem solved already, so it's better to post more information than less.Most especially, I'd want to see STP configurations and a network diagram if there's an RJ45 path between these switches as well. ---

## Response 214
Hi, I've run to the same problem with link going up and down on a port sfp-sfpplus4 of my CRS328-24P-4S+. Enabling and disabling the port helps for some time but that's not the right solution I suppose. I have now stable 6.49.14 version. Do I need to install a development 7.12.1 version, will it help?Thanks. ---

## Response 215
Guys, I just recently noticed the same port flapping in the logs every few minutes on the RJ45 PC clients sitting on my CRS 328 24p 4s+ with routerOS 7.14.2. (Router board also upgraded with same firmware version). This thread started in 2019. Is there really no fix ever since?For me nothing seems to help. I disabled autoneg, put fix 1G port speed, also on the client side, flapping just continues. I don't recall I've seen this with 6.x RouterOS but I may not remember well.Oddly, POE cameras, TV, media player, etc, sitting also there on the CRS do not flap. Only the PC computers connected to it do flap.Thanks for advices. ---

## Response 216
…the same port flapping…What makes you believe our flapping is your flapping?I'm serious. The "severe" in this thread's title was correct, at the time, and it is now fixed. It wasbadin the early 7.x days.Now it seems any time someone sees more than one flap, it's suddenly "severe" and aaaaaaaa MT sucks!Only the PC computers connected to it do flap.And what do PCs have in common that things like PoE cameras do not? They sleep.Your NICs are going into a low-power mode, dropping the conn as long as they can consistent with being available on demand.Want proof? Keep one of your PCs forcibly awake somehow, then monitor its port. Does it stay up? Yes? Then it's not a "flap" you're seeing, it's power savings. ---

## Response 217
I'm having what I believe to be severe flapping on a CRS305-1G-4S+To my desktop. I've tried swapping out the SFP and the cable.
```
192.168.40.62	Apr 23 19:55:06	interface,info				sfp-sfpplus4-tiny link down
192.168.40.62	Apr 23 19:55:08	interface,info				sfp-sfpplus4-tiny link up (speed 10G, full duplex)
192.168.40.62	Apr 23 19:55:08	interface,info				sfp-sfpplus4-tiny detect LAN
192.168.40.62	Apr 23 19:55:51	interface,info				sfp-sfpplus4-tiny link down
192.168.40.62	Apr 23 19:55:53	interface,info				sfp-sfpplus4-tiny link up (speed 10G, full duplex)
192.168.40.62	Apr 23 19:55:53	interface,info				sfp-sfpplus4-tiny detect LAN
192.168.40.62	Apr 23 19:55:54	interface,info				sfp-sfpplus4-tiny link down
192.168.40.62	Apr 23 19:55:55	interface,info				sfp-sfpplus4-tiny link up (speed 10G, full duplex)
192.168.40.62	Apr 23 19:55:55	interface,info				sfp-sfpplus4-tiny detect LAN
192.168.40.62	Apr 23 19:55:57	interface,info				sfp-sfpplus4-tiny link down
192.168.40.62	Apr 23 19:56:02	interface,info				sfp-sfpplus4-tiny link up (speed 10G, full duplex)
192.168.40.62	Apr 23 19:56:02	interface,info				sfp-sfpplus4-tiny detect LAN
192.168.40.62	Apr 23 20:21:25	interface,info				sfp-sfpplus4-tiny link down
192.168.40.62	Apr 23 20:21:28	interface,info				sfp-sfpplus4-tiny link up (speed 10G, full duplex)
192.168.40.62	Apr 23 20:21:28	interface,info				sfp-sfpplus4-tiny detect LAN
192.168.40.62	Apr 23 20:22:11	interface,info				sfp-sfpplus4-tiny link down
192.168.40.62	Apr 23 20:22:16	interface,info				sfp-sfpplus4-tiny link up (speed 10G, full duplex)
192.168.40.62	Apr 23 20:22:16	interface,info				sfp-sfpplus4-tiny detect LAN
192.168.40.62	Apr 23 20:22:18	interface,info				sfp-sfpplus4-tiny link down
192.168.40.62	Apr 23 20:22:21	interface,info				sfp-sfpplus4-tiny link up (speed 10G, full duplex)
192.168.40.62	Apr 23 20:22:21	interface,info				sfp-sfpplus4-tiny detect LAN
192.168.40.62	Apr 23 20:33:59	interface,info				sfp-sfpplus4-tiny link down
192.168.40.62	Apr 23 20:34:01	interface,info				sfp-sfpplus4-tiny link up (speed 10G, full duplex)
192.168.40.62	Apr 23 20:34:01	interface,info				sfp-sfpplus4-tiny detect LAN
192.168.40.62	Apr 23 20:38:38	interface,info				sfp-sfpplus4-tiny link down
192.168.40.62	Apr 23 20:38:51	interface,info				sfp-sfpplus4-tiny link up (speed 10G, full duplex)
192.168.40.62	Apr 23 20:38:51	interface,info				sfp-sfpplus4-tiny detect LAN
192.168.40.62	Apr 23 20:38:55	interface,info				sfp-sfpplus4-tiny link down
192.168.40.62	Apr 23 20:38:57	interface,info				sfp-sfpplus4-tiny link up (speed 10G, full duplex)
192.168.40.62	Apr 23 20:38:57	interface,info				sfp-sfpplus4-tiny detect LAN
192.168.40.62	Apr 23 20:38:58	interface,info				sfp-sfpplus4-tiny link down
192.168.40.62	Apr 23 20:38:59	interface,info				sfp-sfpplus4-tiny link up (speed 10G, full duplex)
192.168.40.62	Apr 23 20:38:59	interface,info				sfp-sfpplus4-tiny detect LAN

---
```

## Response 218
Hello, i have encountered this problem between my LHG XL 52 AC and CRS309-1G-8S+IN hardware revision 2.This devices are connected only through 1G SFP modules. There is about 150 meters of fiber optic cable. Ethernet port on LHG XL is used only for PoE, there is no traffic, no routing to internet.....Log from LHG XLIssue is present with these version of routeros 7.10.2 and later upgraded to 7.14.3What i have changed: SFP modules and LHG XL (also PoE adapter). The link was tested with OTDR, which showed 0 physical problems with link.The only think what help is reboot of devices, After reboot there is usually one hour or hour and half without problems.The only think what could change it, is change of CRS309, which costs some money....Few days ago tried autonegation tips, but still got this problem ---

## Response 219
found same problem between netPower 16P PoE CRS318-16P-2S+OUT and LHG XL 52 AC with 10 meters long single mode fiber optic cable.NetPower has 7.13.2 (Second SFP 1G)LHG XL has 7.14.3 (SFP internet, Eth only PoE from different device)Devices tried with multiple SFPs. Currently we also have same problem with original Mikrotik S-3553LC20D modules ---

## Response 220
For a workaround I swapped the SFP module for RJ-45 module S+RJ10. It's hot but works fine. For a month now I have not had that flapping problem. ---

## Response 221
It was fixed in 7.4, which is “stable,” not LTS.7.4 changelog says:switch - disabled second CPU core for CRS328-24P-4S+ device in order to improve SFP+ link stability;What about the CRS317? Was the same lobotomy performed on it as well?Could someone compare the PSU before and after an RMA? Maybe the issue could be resolved simply by replacing the capacitors with ones of higher capacitance? It makes sense, since in SwOS there were no SFP+ port flapping issues, possibly because the CPU's power consumption was lower compared to RouterOS.P.S. What is the maximum number of active SFP+ links that the CRS317 can handle with the factory PSU? ---

## Response 222
What about the CRS317? Was the same lobotomy performed on it as well?Could someone compare the PSU before and after an RMA? Maybe the issue could be resolved simply by replacing the capacitors with ones of higher capacitance? It makes sense, since in SwOS there were no SFP+ port flapping issues, possibly because the CPU's power consumption was lower compared to RouterOS.P.S. What is the maximum number of active SFP+ links that the CRS317 can handle with the factory PSU?CRS317 always have had 2 CPU cores no change on that AFAIKwith "normal" sfp+ modules no limitationCSS/CRS317-1G-16S+ - power controller supports up to 10 simultaneous S+RJ10 modules.https://help.mikrotik.com/docs/display/ ... patibilityFollowing S+RJ10 Positioning in devices Guide only 8 S+RJ10 must be used con CRS317https://help.mikrotik.com/docs/display/ ... l+guidance ---

## Response 223
Hi, CRS326-24G-2S+ still have port flapping, even HW revision r2I have mentioned about this problem in 2019, fife years passed and still the same.CRS326 is unusable at all. ---

## Response 224
There are no known issues with port flapping in switches that are made for the last ~4-5 years. There were some issues that were addressed around that time. If you see port flapping now - you might have to investigate the other end of the link, powering etc.P.S: please do not crosspost the same message in all topics ---