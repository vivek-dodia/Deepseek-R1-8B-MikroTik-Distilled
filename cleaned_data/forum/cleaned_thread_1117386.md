# Thread Information
Title: Thread-1117386
Section: RouterOS
Thread ID: 1117386

# Discussion

## Initial Question
Any updates to this issue, is it better with SWOS ?It is really quiet here !?This week i installed on my 3 CRS354 the SWOS 2.13 in the office I had no problems at all, so I will begin on Monday to replace one of my 3 HP Procurve at production site with a CRS354.If there will be no problem after 2 weeks I will replace another one and so on.My configuration will have no VLAN, I bouht this Switches because of the 2 Power-Supplies and the SFP+ 10Gbit.I will report here, how it works with SWOS.CU ---

## Response 1
Just an update.. I used RouterOS 6.47.10 (latest long-term) on CRS354-48G-4S+2Q+ and after 28days port 41-48 stop forwarding packets.. ---

## Response 2
This thread was a disappointing find as I just purchased 2x of these.I just put them in a rack and started configuring last friday, then found this thread.I usually only run Long-term release so how long is it going to take before Testing-release changes show up?If they even fix the issues anyways?Here are some highlights from the latest Testing-release (6.49beta54 - July 5th, 2021):https://mikrotik.com/download/changelog ... lease-tree*) crs3xx - fixed jumbo frame forwarding for CRS354 devices (introduced in v6.49beta36);*) crs3xx - correctly filter packets by L2MTU on 1Gbps Ethernet interfaces for CRS354 devices;*) crs3xx - fixed packet forwarding on 1Gbps Ethernet interfaces for CRS354 devices (introduced in v6.49beta44);*) crs3xx - improved QSFP+ linking and mode changing for CRS326-24S+2Q+ and CRS354 devices;*) crs3xx - improved switch resource allocation for CRS317, CRS309, CRS312, CRS326-24S+2Q+ and CRS354 devices;*) poe - fixed PoE out functionality on CRS354 (introduced in v6.49beta22);*) sfp - improved link stability for 10G, 25G and 40G modules on CRS309, CRS312, CRS326-24S+2Q+ CRS354 and CCR2004 devices;It seems like we're not even past the re-introduce new problems phase :/Why would anyone expect issues to be improved or fixed if big ticket items are still being fixed or were re-introduced anyways?I <3 router OS and I've been waiting to get these for as long as i can remember, but now i'm wondering to what extent i'll use them at all. I can't physically babysit 48p switches. ---

## Response 3
Deleted ---

## Response 4
Update:I have 2 Devices with SWOS 2.13 running since last Friday 30th of July without Problems.Configuration is without VLANs.CUTenos ---

## Response 5
Got this issue at ports 41-48 on 49beta54 firmware and 48G (non PoE switch). Outdoor security cameras on these ports went down. I thought the issue happened to 12V line or something like that but nothing helped until switch been rebooted few hours later. I guess it might be somehow related to big rain with thunder that night. Joints are sealed but nothing perfect in this world. Anyway whole block of ports went down and back after reboot. Sad story. ---

## Response 6
If you don’t need Router functionality you could switch to SWOS, I have now 3 devices running since 30th of July without problems. ---

## Response 7
If you don’t need Router functionality you could switch to SWOS, I have now 3 devices running since 30th of July without problems.It been running for months without reboots and issues. Rare thing. ---

## Response 8
Issue still persists in 6.48.4, ports 17-23 got stuck.I noticed that there is something that may be related to this in latest rc2 of 6.49:*) crs3xx - fixed bridge controller and extender packet forwarding for CRS312, CRS326-24S+2Q+ and CRS354 devicesDoes anyone have any information if this really fixes the issue? ---

## Response 9
Issue still persists in 6.48.4, ports 17-23 got stuck.I noticed that there is something that may be related to this in latest rc2 of 6.49:*) crs3xx - fixed bridge controller and extender packet forwarding for CRS312, CRS326-24S+2Q+ and CRS354 devicesDoes anyone have any information if this really fixes the issue?Watching this thread for months to see someone from Mikrotik appear to give more information about that. No one word. A little strange. ---

## Response 10
Strange ?Yeah.... but not a singe unit have this problems since 6.48 ROS series ---

## Response 11
Running 6.49 and it been having issues like crazy for the past week ! Port group stop working several time a day, to every few days now... I just can't take it anymore ! Removing that switch this week as soon as we can ! ---

## Response 12
Well shit, I was about to build my new network with these switches at the core. The lack of response and root cause from Mikrotik sounds like they aren't able to fix this, I guess the Marvel chip is broken and they are trying software workarounds to no avail.Is there anyone at Mikrotik willing to confirm that hardware revision 2 and RouterOS 6.48+ makes this switch usable? ---

## Response 13
Deleted ---

## Response 14
Well, it is now removed !!! 6.49.1 and port group traffic was still blocking !I'm really not happy in how Mikrotik dealing all this ! Not just for his product, but represent how they will deal with their other product and future product...This is not their small entry level 15$ home router... I like having a single vendor for my equipment so there is no excuse that it because of someone else... But if they can't take care of their own gears...I'm really disappointed since I've been rooting for them for a while and I didn't want to spend the time to find replacement gear ! ---

## Response 15
Just got this on ROS 7.1 and revision 2 device. After reboot block of ports stuck. No traffic. Another reboot helped. ---

## Response 16
CRS354-48P-4S+2Q+uptime 13d 16:39:196.48.2 (stable)so far so goodHello, still running without issue with 6.48.2 stable ?We are considering to use the ones we have for non critical stuff (like BMC / IPMI).Also can anyone confirm that there is no issue when using SwOS ?Mikrotik staff maybe some official feedback ? ---

## Response 17
Mikrotik has been irresponsibly mum on this issue. The issue continues to impact the CRS354 POE switches in production especially on ports 9-16 for us. ---

## Response 18
To anyone reading who desperately wants this to be fixed because the price is so attractive - it isn't fixed, if you put this device on your network, prepare for the worst.Why this is switch still for sale? The issues have ongoing for years and MT are either unable or willing to fix them.My setup was reasonably straight forward - just default switching with a single VLAN on the bridge. Connections to SFP+ ports were fine, the 1Gb ports were just downtime waiting to happen on a fairly regular basis. Always had the most recent stable FW (was up to 6.48.4 before I pulled the plug on it). Functions In SwOS just fine, but you can get that level of functionality for better prices elsewhere. ---

## Response 19
CRS354-48P-4S+2Q+uptime 13d 16:39:196.48.2 (stable)so far so goodHello, still running without issue with 6.48.2 stable ?We are considering to use the ones we have for non critical stuff (like BMC / IPMI).Also can anyone confirm that there is no issue when using SwOS ?Mikrotik staff maybe some official feedback ?Hello, I'm runnig 7 of them with Switch OS without Problems (the Version without PoE) ---

## Response 20
Is this good now ?Any news? ---

## Response 21
Is this good now ?Any news?No. Mikrotik continues to irresponsibly ignore this problem. No information or any eta from them on the fix. ---

## Response 22
Found the reason of "High CPU load" hereviewtopic.php?t=179064#p936933Still have the problem with ethernet ports:I still see the random Ethernet ports turn off. One thing I noticed, it can happen when power went down and the switch did reboot. After that I see unstable work until I turn off the switch, wait 10 minutes and start again. Then it seems to be stable. ---

## Response 23
A job I have next week could really use a 48 Port.EdgeSwitch ES-48-500 is still out of stock.Distro got a bunch of CRS354-48P in.Came back and checked this thread...Back to looking for something else. ---

## Response 24
Have we really made it 2 years without a fix? ---

## Response 25
Is this problem still current? I wonder if I dare to buy the CRS354. ---

## Response 26
I ve installed a CRS354 recently, not fully loaded yet, just a couple of ethernet ports and an SFP+ port.I ve not seen any port flapping...Versions 6.49.6VLANs are used on the CRS... ---

## Response 27
I ve installed a CRS354 recently, not fully loaded yet, just a couple of ethernet ports and an SFP+ port.I ve not seen any port flapping...Versions 6.49.6VLANs are used on the CRS...It's not port flapping.You will see groups of ports stop forwarding traffic AT ALL until reboot. ---

## Response 28
You will see groups of ports stop forwarding traffic AT ALL until reboot.ok.The device has an uptime of approximately 2 weeks without any problems... ---

## Response 29
This is terrible. Why is there no response from Mikrotik or acknowledgement to this problem and the switch is still for sale?I am researching switch choices for a large network and thought I had better search the forums here before deciding. ---

## Response 30
Is it certain that there is a problem indeed ? That is not fixed on recent ROS releases ?Anyone made a support ticket ? ---

## Response 31
Is it certain that there is a problem indeed ? That is not fixed on recent ROS releases ?Anyone made a support ticket ?I read every post in this thread, and it looks like the only working solution is to use SwOS. ---

## Response 32
You can use the "smaller brother 24Gig+4TenGig " ( CRS328-24P-4S+RM ) - it doesn't have this port/CPU problem.The price is skyrocketed :O ---

## Response 33
I was hired for an existing job that has "problems".During discovery... I found out they have 3 of these switches.Ohh boy... ---

## Response 34
Called back on Friday...Customer, "That VPN hub spoke thing you did is working great. But we are having a lot of problems with local devices staying connected. We pulled the Mikrotik switches and put in some Merakis. The wired stuff stays connected now..."I explained about this thread and my past experience.Customer, "Well I guess that explains it."He was pretty cool with having to swap out the switches. Must have had a return period with his distributor. Or must have actually made some money buy putting in the Meraki switches for a FLAT network. ---

## Response 35
But we are having a lot of problems with local devices staying connectedThat is a general description.Did you actually observe this problem yourself ?Any log check on the devices?The previous posts mention that the switch stops forwarding traffic until reboot, but in your case there is no such description...e.g. the client was rebooting the switches ? otherwise how was the problem resolved ? So are we talking about the same problem ?ROS version on the switches ? ---

## Response 36
Zacharias, I worked for them on Friday.When I called on the NEXT FRIDAY, to ask about adding more users on Zerotier... That's when they told me they wanted me to look at the WIRELESS to explain why they were having problems.They had already replaced one switch BEFORE they called.They moved the Wireless to the Meraki switch and they could maintain connections.I didn't wanna touch the switches when they were in. They had "just been installed" and I didn't want to blamed if this happened. I am pretty sure I saw 6.48 in winbox when I was working on the router. ---

## Response 37
I just wanted to post some positive feedback which is much needed during these times.We have 10 units of CRS354-48P-4S+2Q+ running flawlessly.Running stable 6.49.6Features used: multiple VLANS, Dot1x, PoE, DHCP snooping, STP etc.Purchased in multiple batches, running for various time - from years to couple of months.Factory firmware varies from 6.46.1 to 6.48.3Only complain is the "weird" Q+ ports which acts as 4 separate ones, but that is by design. ---

## Response 38
Hello, Is that problem solved completly ?Can we use old CRS 354 ?I have 4 unit. ---

## Response 39
Anyone tried RouterOS V7 on CRS354?Wonder how it affects this traffic problem... ---

## Response 40
Any official, or not, news on this behavior ?Problem solved with ros7 ??Can anyone confirm they are absolutely reliable when used in SWOS ??I have to buy some PoE units, as Mikrotik fan, I wouldn't switch to Unifi or some other brand because of this , it's NOT just a price matter....Thank you ---

## Response 41
Any official, or not, news on this behavior ?Problem solved with ros7 ??Can anyone confirm they are absolutely reliable when used in SWOS ??I have to buy some PoE units, as Mikrotik fan, I wouldn't switch to Unifi or some other brand because of this , it's NOT just a price matter....Thank youEtcoplasmosis: I dealt with an install last month, that was unfortunate enough to have 3 354... They require daily reboots to work as basic layer 2 switches.The 354 was flawed at release. 2+ years later it's still not fixed.Much like the RB1200 or their client serving wifi... There is stuff Mikrotik can not fix. Move on. ---

## Response 42
@gotsprings what is the revision version under /system routerboard ? ---

## Response 43
@gotsprings what is the revision version under /system routerboard ?I did update the switches to whatever was current that day. Ergo routerOS and board firmware.As for watching it...I had seen it at home years ago. You will see a bunch of ports that just seem to be at idle. I could send a ping through those ports... So it would appear as if it was working. But nothing bigger than a ping seemed to go.Power cycling the switch would return normal operation for a few hours or days.Now if you look in another recent thread... A guy took over a hotel and the switches are doing this exactly.I followed up with the guys I worked for and they had already pulled the switches. "If we had asked you first we never would have put them in."Problems vanished when the switches did. ---

## Response 44
What about SWos behavior ? Same issue ? ---

## Response 45
I did update the switches to whatever was current that day. Ergo routerOS and board firmware.Revision is not the same as firmware version.The revision i think changes when there is a hardware change on the device.For example, my CRS354 indicates asRevision : r2. ---

## Response 46
I did update the switches to whatever was current that day. Ergo routerOS and board firmware.Revision is not the same as firmware version.The revision i think changes when there is a hardware change on the device.For example, my CRS354 indicates asRevision : r2.My mistake.I didn't notice if Mikrotik changed the actual hardware without admitting the fault or RMAing ALL THE BAD ONES THEY PUT OUT THERE FOR YEARS.I thought you meant did I update the board firmware. ---

## Response 47
So, yours is r2 ? Or the revision is not mentioned? ---

## Response 48
So, yours is r2 ? Or the revision is not mentioned?I didn't notice if there was a revision at the time.The switches were decommissioned, (ripped out of rack and maybe thrown away) so I can't check now. ---

## Response 49
I am having a similar problem. I don't know if it is certain ports.The ports are switched and the moment the device boots traffic goes through. After a while, I think if I also transfer something like 100mbit data for a few seconds it stops working. No data is going through some ports.I tried it several times and all of the times it was doing it.At first I thought I was doing something wrong at my gateway (ccr2116-12g-4s+) breaking my b@!!S but it seems that it was because of the CRS354.I had 7.5 and 7.6beta8 on the switch.Btw all the devices are brand new and I am still preparing the setup for the customer before the installation takes place.For now it looks solved by moving to SwOS but I would rather have RouterOS running.Any help would be appreciated since the installation date is in 2 weeks ---

## Response 50
Being a pragmatist... It's a pretty simple answer. ---

## Response 51
Pfff the problem exists also on SwOS finally. Can something be done soon enough? ---

## Response 52
Pfff the problem exists also on Swiss finally. Can something be done soon enough?I have an install with a 328 and 326 linked with the SFP+ DAC.Gives me 24 POE Gigabit Copper ports. 24 non POE Gigabit Copper ports and 4SFP+ ports.I had not seen the problem in the ARM based switches after running it on my bench for a few months. ---

## Response 53
Pfff the problem exists also on SwOS finally. Can something be done soon enough?So no OS issue (swos or ros) ??Definitely an hardware issue ? ---

## Response 54
I think the problem on mine is on ports eth9-eth16. The moment it boots they work and after a while possible when some data pass through they stop communicating. POE is working on those ports, the data are not passing ---

## Response 55
I think the problem on mine is on ports eth9-eth16. The moment it boots they work and after a while possible when some data pass through they stop communicating. POE is working on those ports, the data are not passingIf it broke right away... Wouldn't have been a problem for so long. ---

## Response 56
It is brand new not delivered to the customer yet. At first I was breaking my head spending hours trying to spot what I was doing wrong in my config. Then I looked it up and found that post with pretty similar problem. I also turned it to SwOS and nothing changed. You only see traffic going out and nothing coming back. If you disable and enable the port it is not coming back. The moment I reboot the switch it starts working again communicating for a while and then the problem returns. If I had read that post before I buy it I would still buy it and I wouldn't believe that it wouldn't be fixed by now. ---

## Response 57
After some (LONG) time one of my CRS354 unit fail on this again. I can't believe this is still a thing.... ---

## Response 58
Same issue here ... allmost 3 years later, not fixed ... ---

## Response 59
Same issue here ... allmost 3 years later, not fixed ...Still on my..."Do not order" sheet.Sales keeps asking... I keep saying NO. ---

## Response 60
[/quote]Still on my..."Do not order" sheet.Sales keeps asking... I keep saying NO.[/quote]That sounds wise indeed...The Switch in question is brand new, 3 months in production. ---

## Response 61
Very glad I found this topic 1 year ago, I almost purchased a bunch of these and the issue is still not fixed after a year! It must be broken hardware, very irresponsible to continue shipping it. ---

## Response 62
Coming up on 3 years now?Maybe we need one of those posts at the top of the forum that gets put at the top every day."Today is January 15, 2023 (Day #1085) and the CRS354s are still defective." ---

## Response 63
Still no update? The situation with these switches is incredible...I have one that worked without issues for 9 months. After it stopped passing traffic twice in the same day I replaced it... and I don't trust using it anymore.And now I'm looking for 48 port switches at other suppliers. ---

## Response 64
Hello, has mikrotik already found a solution to the failure to switch individual blocks? I'm having trouble with ports 9-16. ---

## Response 65
Hello, has mikrotik already found a solution to the failure to switch individual blocks? I'm having trouble with ports 9-16.Replace it with 2 24 port units. ---

## Response 66
It's been 3 years...Still can't use them? ---

## Response 67
Same trouble with 9-16 ports. New CRS354-48PMikroTik team, what happen with 354 switches? ---

## Response 68
Is this problem still existent, even with SwitchOS?We are on the process of buying 02 48-port PoE switches with 10GB uplinks and CRS354-48P-4S+2Q+RM is one of the candidates but this bug is a showstopper.RegardsMauricio ---

## Response 69
Is this problem still existent, even with SwitchOS?We are on the process of buying 02 48-port PoE switches with 10GB uplinks and CRS354-48P-4S+2Q+RM is one of the candidates but this bug is a showstopper.RegardsMauricioBuy 4 of the CRS328-24PSeems to be the only way to make sure it's gonna work. ---

## Response 70
Is there a way to identify the problem when ports stop working? To create a script that would reboot the switchin that case. MikroTik has become completely unprofessional in their business, and I don't understand why the EU doesn't do something and ban them from selling faulty products in the EU territory. They know about this issue and know that the devices they sell are technically faulty, yet they continue to be sold. This is against all laws and regulations.I bought 5 of these switches and all 5 are faulty. I filed a complaint and received 5 new ones that are also defective. ---

## Response 71
Sadly... Pings still pass when the port is "locked up". This makes it harder to figure out.But the new netwatch can query for a webpage. Maybe that would be enough to let netwatch know it's down. Then you could REBOOT THE WHOLE SWITCH.(That's right... That's what has to be done when ports stop passing traffic.) ---

## Response 72
bump bump ---

## Response 73
MIKROTIK SHAME ON YOU!!! IT'S BEEN 3 YEARS AND YET STILL SILENCE ON YOUR END? ---

## Response 74
Was talking with another company's tech. He needed a EdgeSwitch to complete an install that required passive 24Volt and standard AF/AT power at the same switch.Since he had been waiting for the EdgeSwitch for over a year at this point... I pointed him to the CRS328-24P I have settled on. I specifically stated that I use a DAC cable between multiple switches to increase port count.I also specifically pointed him to this thread.What did he do? Ordered a CRS354-48P. (From a US distributor who doesn't take returns...)"I couldn't find that post you were talking about." ---

## Response 75
MIKROTIK SHAME ON YOU!!! IT'S BEEN 3 YEARS AND YET STILL SILENCE ON YOUR END?What is your support ticket number? ---

## Response 76
I have had 2 of these switches running live with no issues for over 6 months running RouterOS v6.49.6. The load on these is not large and only 4 or 5 ports are really being used on them at a time. I recently started swapping out some rack switches with these switches before I ran across this thread and what a mistake that has been so far. The first one I swapped in lasted for 33 days before port flapping for a few hours and then halting all traffic altogether when no was in the office. The other one did the same thing within 4 hours of going live, all ports just stopped passing traffic except for the management port. These new ones I swapped in were both running RouterOS v7.8 (stable) These are very basic setups with no VLAN's. Hard to believe they have not recalled this product at this point. ---

## Response 77
Been having this issue across our stores. We have 100+ of these switches installed and ports 9-16 are basically unusable. We have put it on our "do not use" list and are using 2 of the CRS328-24P-4S+RM in place of 1 of the 48P switches.Sad. But in our last order of these switches I noticed that it now says "r3" for revision 3. All our previous switches were either r1 or r2 (mostly r2) so I wonder what is new with this r3 version?Screenshot 2023-06-15 at 2.03.26 PM.png ---

## Response 78
Regarding revision 3 of this switch, this is what support said:"Revision 3 comes with larger flash storage - 32MB."So I'm sure it's not fixed if that's the only thing that has changed on it. ---

## Response 79
They are still selling that switch as if it's perfectly fine, without any shame. This needs to be reported to regulators, other companies have paid large fines, in millions and billions for such behavior in the EU market. What they are doing is a criminal offense. ---

## Response 80
They are still selling that switch as if it's perfectly fine, without any shame. This needs to be reported to regulators, other companies have paid large fines, in millions and billions for such behavior in the EU market. What they are doing is a criminal offense.In the US... its an Undocumented Feature."Daily Power Reboot Reminder." ---

## Response 81
Need a new switch for an upcoming job.Thought "maybe its time to look at the CRS354s again."Out of stock.But this thread doesn't have a bunch of "ITS FINALLY WORKING!"So whats the story this month? ---

## Response 82
Today is July 26 2023...I am about to order a switch elsewhere... again?This thread is 1183 days old. ---

## Response 83
I would buy immediately 354 (poe or not) but this issue made me buy Aruba or Ubiquiti units without take the risk of try one.It's still not clear how many 354 have been sold and how many have the issue , how many get issue running ros and how many swos.I can't believe Mikrotik doesn't know about.They offer great products @ great cost and almost 100% support and issues-solving.CRS354 is the black sheep of the family... ---

## Response 84
Regarding revision 3 of this switch, this is what support said:"Revision 3 comes with larger flash storage - 32MB."So I'm sure it's not fixed if that's the only thing that has changed on it.It would be interesting to know if issue is still present on REV.3 ---

## Response 85
I have my CRS354-48P-4S+2Q+ r2 for two years now, without any issue. Maybe I am doing something wrong? ---

## Response 86
I was reading another thread...viewtopic.php?t=189614Where Normis is actively going back and forth with someone over a design vs defect issue.Yet nothing on this thread. ---

## Response 87
Today is Oct 3 2023...And the 3 CRS354s are still locking up.Updated the firmware last week and that buys a day or two between reboots.This thread is 1252 day old. ---

## Response 88
And now the switch is not in stock at the suppliers in Denmark...I'm thinking of buying 2 pcs. I don't think I will have any problems returning a switch if it shows that some of the ports will have the issue. ---

## Response 89
And now the switch is not in stock at the suppliers in Denmark...I'm thinking of buying 2 pcs. I don't think I will have any problems returning a switch if it shows that some of the ports will have the issue.So what happened with your switch purchase?The only site I have with 354s in it are asking for a replacement. ---

## Response 90
I've ordered 2 pcs 2 weeks ago, I still haven't received confirmation on delivery date.Are you going to replace them because of port problems? ---

## Response 91
I've ordered 2 pcs 2 weeks ago, I still haven't received confirmation on delivery date.Are you going to replace them because of port problems?But why do you ask here?Contact your distributor, instead of asking these useless questions on the user forum. ---

## Response 92
I've ordered 2 pcs 2 weeks ago, I still haven't received confirmation on delivery date.Are you going to replace them because of port problems?But why do you ask here?Contact your distributor, instead of asking these useless questions on the user forum.I mean... I did ask.And yes they want the switches replaced due to the reboots required to make the switches pass packets again. ---

## Response 93
But why do you ask here?Contact your distributor, instead of asking these useless questions on the user forum.I mean... I did ask.And yes they want the switches replaced due to the reboots required to make the switches pass packets again.They are still not in stock. I've tried searching at all major suppliers in Denmark, strange... Our main supplier can't tell anything about delivery date, because the import company don't have a date... I wonder if it's related with the issues, or it's just shortages. ---

## Response 94
Since the ES48-500 is available again from UBNT. Might be going back to EdgSwitch. ---

## Response 95
Mikrotik EU Store has 5pcs on stock:https://www.mikrotik-store.eu/en/mikrot ... 48p-4s2qrmNo need to by from a distributor having them from an importer, both putting their own margin on top of the price for doing nothing else then forwarding your order. ---

## Response 96
Mikrotik EU Store has 5pcs on stock:https://www.mikrotik-store.eu/en/mikrot ... 48p-4s2qrmNo need to by from a distributor having them from an importer, both putting their own margin on top of the price for doing nothing else then forwarding your order.Yes, the POE version is also available in Denmark, but for Edge switching / AP's we are into the Unifi ecosystem at the moment, so we don't need POE. CRS354's QSFP+ and SFP+ ports combined with the RJ45 ports, matches exactly what we need for our 2x "Server / Distribution" switches in our setup.Is anybody familiar with the HPE FlexFabric 5900AF 48G 4XG 2QSFP+ ? The specs looks very much the same but I've not worked with HP switches before...Edit: Ok, that HPE 5900AF is rather old... Is anybody aware of an alternative with minimum 2x QSF+, 2x SFP+ and 24x RJ45 ports, alternative minimum 6x SFP+ and 24x RJ45 ports ? ---

## Response 97
Since there are 2 threads out there about people having just bought this switch and are having issues...Time to bump this thread to the top again. ---

## Response 98
Since there are 2 threads out there about people having just bought this switch and are having issues...Time to bump this thread to the top again.Can you paste a link to the other thread ---

## Response 99
Since there are 2 threads out there about people having just bought this switch and are having issues...Time to bump this thread to the top again.Can you paste a link to the other threadviewtopic.php?t=202646 ---

## Response 100
This thread is 1341 days old. ---

## Response 101
This thread is 1341 days old.Maybe they will release a new model instead of fixing the old oneThanks for the link, and I cancelled the order on the CRS354 I had ordered. Then I hope the old switches they should replace, will hold a little longer... ---

## Response 102
We unfurtuantely have the same issue, but our CRS354-48P-4S+2Q+ ran fine for many month until about christmas 2023. Probably because we use it with SwOS from the beginning it took longer for the problem to occure. Now as we received strange network issues with failing ports 1-8, I found this thread and took about two hours to read through the previous years. Problem is that there is not a newer SwOS version than 2.13.The problem seems to be not fixed yet, after nearly four years and I doubt it will get fixed in the future. ---

## Response 103
Hard to have sympathy reading this thread as Rextended alluded to ........ where are the 1000s supout reports..........??? ---

## Response 104
Hard to have sympathy reading this thread as Rextended alluded to ........ where are the 1000s supout reports..........???Other threads and Facebook posts come up from time to time.The unlucky sob is pointed here.... Return occurs. Some just trash them. ---

## Response 105
Have you guys tried 7.13.1? Those switch changes should fix the CRS354 issues described in the topic ---

## Response 106
I wil try. Thx for some hope. ---

## Response 107
@normis - Even if it does. What is with those people using SwOS? The problem occures there, as well. ---

## Response 108
@normis.Welcome to the thread.(3 years 8 months and 13 days)Hopefully we can finally get these units working, and we can take them off the "do not quote list". ---

## Response 109
Have you guys tried 7.13.1? Those switch changes should fix the CRS354 issues described in the topicnot fixed, today (couple days after update to 7.13.1) strikes this problem again ---

## Response 110
rushlifecould I please see your configuration on these switches? does this happen to all of them or just specif ones? and what is usually your uptime without the failure? Thank you. ---

## Response 111
The ones I saw./IP dhcp-client add interface=bridge/IP dhcp-client enable 0/IP address disable 0 ---

## Response 112
rushlifecould I please see your configuration on these switches? does this happen to all of them or just specif ones? and what is usually your uptime without the failure? Thank you.hi, here is my export/interface bridge add admin-mac=macFROMether1 auto-mac=no name=bridge1/interface ethernet set [ find default-name=ether1 ] loop-protect=on/interface ethernet set [ find default-name=ether2 ] loop-protect=on/interface ethernet set [ find default-name=ether3 ] loop-protect=on/interface ethernet set [ find default-name=ether4 ] loop-protect=on/interface ethernet set [ find default-name=ether5 ] loop-protect=on/interface ethernet set [ find default-name=ether6 ] loop-protect=on/interface ethernet set [ find default-name=ether7 ] loop-protect=on/interface ethernet set [ find default-name=ether8 ] loop-protect=on/interface ethernet set [ find default-name=ether9 ] loop-protect=on/interface ethernet set [ find default-name=ether10 ] loop-protect=on/interface ethernet set [ find default-name=ether11 ] loop-protect=on/interface ethernet set [ find default-name=ether12 ] loop-protect=on/interface ethernet set [ find default-name=ether13 ] loop-protect=on/interface ethernet set [ find default-name=ether14 ] loop-protect=on/interface ethernet set [ find default-name=ether15 ] loop-protect=on/interface ethernet set [ find default-name=ether16 ] loop-protect=on/interface ethernet set [ find default-name=ether17 ] loop-protect=on/interface ethernet set [ find default-name=ether18 ] loop-protect=on/interface ethernet set [ find default-name=ether19 ] loop-protect=on/interface ethernet set [ find default-name=ether20 ] loop-protect=on/interface ethernet set [ find default-name=ether21 ] loop-protect=on/interface ethernet set [ find default-name=ether22 ] loop-protect=on/interface ethernet set [ find default-name=ether23 ] loop-protect=on/interface ethernet set [ find default-name=ether24 ] loop-protect=on/interface ethernet set [ find default-name=ether25 ] loop-protect=on/interface ethernet set [ find default-name=ether26 ] loop-protect=on/interface ethernet set [ find default-name=ether27 ] loop-protect=on/interface ethernet set [ find default-name=ether28 ] loop-protect=on/interface ethernet set [ find default-name=ether29 ] loop-protect=on/interface ethernet set [ find default-name=ether30 ] loop-protect=on/interface ethernet set [ find default-name=ether31 ] loop-protect=on/interface ethernet set [ find default-name=ether32 ] loop-protect=on/interface ethernet set [ find default-name=ether33 ] loop-protect=on/interface ethernet set [ find default-name=ether34 ] loop-protect=on/interface ethernet set [ find default-name=ether35 ] loop-protect=on/interface ethernet set [ find default-name=ether36 ] loop-protect=on/interface ethernet set [ find default-name=ether37 ] loop-protect=on/interface ethernet set [ find default-name=ether38 ] loop-protect=on/interface ethernet set [ find default-name=ether39 ] loop-protect=on/interface ethernet set [ find default-name=ether40 ] loop-protect=on/interface ethernet set [ find default-name=ether41 ] loop-protect=on/interface ethernet set [ find default-name=ether42 ] loop-protect=on/interface ethernet set [ find default-name=ether43 ] loop-protect=on/interface ethernet set [ find default-name=ether44 ] loop-protect=on/interface ethernet set [ find default-name=ether45 ] loop-protect=on/interface ethernet set [ find default-name=ether46 ] loop-protect=on/interface ethernet set [ find default-name=ether47 ] loop-protect=on/interface ethernet set [ find default-name=ether48 ] loop-protect=on/interface ethernet set [ find default-name=ether49 ] loop-protect=on/interface ethernet set [ find default-name=qsfpplus1-1 ] loop-protect=on/interface ethernet set [ find default-name=qsfpplus1-2 ] loop-protect=on/interface ethernet set [ find default-name=qsfpplus1-3 ] loop-protect=on/interface ethernet set [ find default-name=qsfpplus1-4 ] loop-protect=on/interface ethernet set [ find default-name=qsfpplus2-1 ] loop-protect=on/interface ethernet set [ find default-name=qsfpplus2-2 ] loop-protect=on/interface ethernet set [ find default-name=qsfpplus2-3 ] loop-protect=on/interface ethernet set [ find default-name=qsfpplus2-4 ] loop-protect=on/interface ethernet set [ find default-name=sfp-sfpplus1 ] loop-protect=on/interface ethernet set [ find default-name=sfp-sfpplus2 ] loop-protect=on/interface ethernet set [ find default-name=sfp-sfpplus3 ] loop-protect=on/interface ethernet set [ find default-name=sfp-sfpplus4 ] loop-protect=on/interface ethernet switch set 0 l3-hw-offloading=yes/interface list add name=mgmtPORT/interface list add exclude=mgmtPORT include=all name=withoutMGMTport/interface bridge port add bridge=bridge1 interface=withoutMGMTport/ip neighbor discovery-settings set discover-interface-list=all/interface list member add interface=ether49 list=mgmtPORT/ip address add address=192.168.xx.xxx/24 interface=bridge1 network=192.168.xx.0/ip dns set servers=192.168.xx.xxx/ip route add disabled=no dst-address=0.0.0.0/0 gateway=192.168.xx.xxx routing-table=main suppress-hw-offload=no/ip service set telnet disabled=yes/ip service set ftp disabled=yes/ip service set www disabled=yes/ip service set api disabled=yes/ip service set api-ssl disabled=yes/snmp set enabled=yes/system clock set time-zone-name=Europe/Prague/system identity set name=crs354-xxx/system note set show-at-login=no/system ntp client set enabled=yes ---

## Response 113
I cannot reproduce this, It is happening randomly really.Sometime this unit work for couple of months, sometime 2 days.Unit is always reachable with ping, winbox or even ssh. No problem. Just clients connected to eth ports become offline. Still have LINK but no data are transfered.Yesterday I bought new crs354 r3 unit and replace it. So now I am curious if will help or will this new revision on new unit will do the same sh*t.BTW. for testing purposes I was not using first 8 port for couple months, it did not help, problem was still the same ---

## Response 114
For my part I have 4x48P units at a customer site that have not exhibited this problem that we know which have been up well over 1y at this point, but also 3 of the 4 are really sparsely populated, so if there was a block of 8 stopped ports on a switch it is not impossible it is simply a block of 8 which are not in use and so it's not been noticed. They're pretty minimal config, no LAGs, at most 4 vlans, and all just uplink to a RB4011, so they're about as basic as it gets.The only reason I am here is because I was about to buy 2x48G that would see much more use than those existing 48P switches and I have now seen this thread....Has anyone else tried the 7.14 betas with these switches like the last poster here to see if it cures their issues? Seems a bit early for them to declare success given some people in here have said they'd had as much as a month or so with no issues on other firmware;viewtopic.php?t=202646#p1049369 ---

## Response 115
After reading this topic, I was expecting similar problems, but I've been waiting for 3 years for something to stop working...Probably users who have problems have caused the device to overheat because it is in a place with little replacement or covered by other peripherals...​ ---

## Response 116
It's a rack mount switch, if it can't handle being installed in a rack "covered by other peripherals" then it is defective. So glad I didn't take the gamble on this hardware, it's ridiculous that these are still being sold with so many problems. ---

## Response 117
it's ridiculous that these are still being sold with so many problems.You have no concrete method of comparison, Only those who complain write here on the forum, not all those satisfied who had no problems... ---

## Response 118
it's ridiculous that these are still being sold with so many problems.You have no concrete method of comparison, Only those who complain write here on the forum, not all those satisfied who had no problems...as I posted in the thread... I was brought in on a job where they already had the switches. And they were having to reboot the switches DAILY!. As soon as they told me the model of the Switch I described exactly what was going wrong.Client, "Is there a fix?"Me, "You found the workaround. Reboot it and it works 'for a while'. Since pings still pass when its locked up... you could maybe set the DLI to check a webport. When that stops working reboot???"All switches were tossed. ---

## Response 119
rushlifethanks for the export. May I also see your supout.rif file? ---

## Response 120
two of my units (I have around 15pcs totally) are affected with this issue and both are failing on ether1-8, I can confirm that, no any other port show problem...Also may I know your topology and what kind of traffic is mostly going through your switches(unicast, multicast, broadcast etc.)? ---

## Response 121
3 years 9 months 7 days... and counting. ---

## Response 122
Hello, any progress with version 7.13.4 or are there still problems?We are thinking of buying 2 switches for the company and after reading this thread I have no confidence in CRS354. ---

## Response 123
Hello, any progress with version 7.13.4 or are there still problems?We are thinking of buying 2 switches for the company and after reading this thread I have no confidence in CRS354.I have been connecting CRS328-24P+4S-RMs together with DAC cables. ---

## Response 124
Is it the fact that the 24 ports are arm, and this one is not? ---

## Response 125
Is it the fact that the 24 ports are arm, and this one is not?It's a sick joke from Mikrotik guys:
```
https://mikrotik.com/product/crs354_48p_4s_2q_rmCPU:QCA9531(MIPSBE)Switchchip model:98DX3257SizeofRAM:64MBStoragesize:16MB 

https://mikrotik.com/product/crs328_24p_4s_rmCPU:98DX3236(ARM32bit)Switchchip model:98DX3236SizeofRAM:512MBStoragesize:16MBThe CRS328 is far superior hardware.

---
```

## Response 126
I saw a mention that 7.14 fixed the issue, can someone confirm ? ---

## Response 127
I saw a mention that 7.14 fixed the issue, can someone confirm ?We have heard prior firmwares corrected this. ---

## Response 128
Well, I can't speak for others, but since I upgraded to version 7.13, I haven't encountered any issues (it's been almost three months now). I have multiple of these devices running continuously at almost wired speeds. ---

## Response 129
Bump...Got asked this morning if the CRS354s are orderable yet?"as far as I know... Mikrotik has never addressed the issue. I will go check the thread."As of today... this tread is3 years, 11 months and 24 days old. ---

## Response 130
I just found this topic and read everything that was written before me and realized that I’m not alone)At my work I have 2xCRS354-48P-4S+2Q+ installed running on SwOS, one with firmware 2.13 and the other with 2.16. For half a year there were no problems, and then a month ago problems similar to what was written here began, sometimes a block of ports and sometimes all ports freeze at the same time. Only a reboot helps, and not always right away, sometimes after a reboot the traffic is up for a few seconds and then down again. Sometimes the switch does not freeze for weeks, sometimes it freezes several times a day. When the problem started, I installed a new switch of the same type, same problem(The problem is specifically on the switch with SwOS 2.16 firmware where 17x Poe access points and 1x Poe camera are connected, and in the switch with firmware 2.13 there are no problems yet, but maybe this is due to the fact that this one is less loaded - 13x Poe access points and 1x Poe camera. ---

## Response 131
4 More Years! ---

## Response 132
Jokes aside... this thread is 4 years old now.I need a 48 Port switch for the job I am spec'ing. Do I still have to go EdgeSwitch at this point? ---

## Response 133
Have you guys tried 7.13.1? Those switch changes should fix the CRS354 issues described in the topicLooking for "Does" not interested in "should". ---

## Response 134
Have you guys tried 7.13.1? Those switch changes should fix the CRS354 issues described in the topicLooking for "Does" not interested in "should".Everybody looked something else already, even used equipment from ebay (other vendors equipment "works" as it should be). ---

## Response 135
I just found this topic and read everything that was written before me and realized that I’m not alone)At my work I have 2xCRS354-48P-4S+2Q+ installed running on SwOS, one with firmware 2.13 and the other with 2.16. For half a year there were no problems, and then a month ago problems similar to what was written here began, sometimes a block of ports and sometimes all ports freeze at the same time. Only a reboot helps, and not always right away, sometimes after a reboot the traffic is up for a few seconds and then down again. Sometimes the switch does not freeze for weeks, sometimes it freezes several times a day. When the problem started, I installed a new switch of the same type, same problem(The problem is specifically on the switch with SwOS 2.16 firmware where 17x Poe access points and 1x Poe camera are connected, and in the switch with firmware 2.13 there are no problems yet, but maybe this is due to the fact that this one is less loaded - 13x Poe access points and 1x Poe camera.I experienced the exact same problem you're describing. This issue has been resolved in RouterOS, but not yet in SwOS. Mikrotik support informed me that they are currently working on implementing the same fix in SwOS as well.There are two main issues with this switch that often get mixed together:1. All ports occasionally freeze [FIXED in RouterOS].2. Specific port groups stop passing traffic [NOT yet fixed].The second issue is particularly challenging because Mikrotik cannot reproduce it when the switches are returned for RMA. It seems to be triggered by specific network applications. ---

## Response 136
We bought 8 of these switches and had the same issue on one of them. We RMA it and the replacement did not have this problem with identical config. I'd contact support in the first instance. ---

## Response 137
We bought 8 of these switches and had the same issue on one of them. We RMA it and the replacement did not have this problem with identical config. I'd contact support in the first instance.When is this going to be fixed? ---

## Response 138
Anyone tried latest version ?*) switch - fixed limited Tx traffic on Ethernet ports for CRS354 devices (introduced in v7.15); ---

## Response 139
We bought 8 of these switches and had the same issue on one of them. We RMA it and the replacement did not have this problem with identical config. I'd contact support in the first instance.Why nobody wants to tell us if it is SW or HW problem ?A replacement with no issue with identical configuration means it's only an hardware problem.I would have bought several 354 units, but I still go for Aruba ones unless the risk to get into a faulty unit (this fault) is eliminated. ---

## Response 140
As I stated before...I connect 2 CRS328-24P+4S-RM with a DAC cable. ---

## Response 141
After reading this topic, I was expecting similar problems, but I've been waiting for 3 years for something to stop working...Probably users who have problems have caused the device to overheat because it is in a place with little replacement or covered by other peripherals...​Still waiting for problems: No problems yet... ---

## Response 142
What's new in 7.16beta3 (2024-Jun-27 08:33):*) switch - fixed an issue with Ethernet port group hang for CRS354 devices; ---

## Response 143
I encountered the same problem and tried all methods. This year we purchased 4 of these CRS354-48P-4S+2Q+, I want to report that the flight is normal on ROS 7.16beta4.The ports no longer turn off spontaneously, and the speed has not yet dropped. testing day 4 on two CRS354s at once with full load (without qsfp+). ---

## Response 144
I can confirm that the issue has been fully resolved. It took some time, though.. ---

## Response 145
I can confirm that the issue has been fully resolved. It took some time, though..So we are sure THIS TIME?4.5 years after release. ---

## Response 146
Yes... but... I never have problem on that hardware... Probably one failed batch???Inefficent cooling???After reading this topic, I was expecting similar problems, but I've been waiting for 3 years for something to stop working...Probably users who have problems have caused the device to overheat because it is in a place with little replacement or covered by other peripherals...​ ---

## Response 147
We have a CRS354-48G-4S+2Q+ r2 running 6.49.1 that has gone for years without showing issues, suddenly porta 9-16 suddenly are not passing data to the connected devices in either direction, nothing else of note is strange. Will review the advice in this thread, thank you. ---

## Response 148
I have been facing issues with this model for almost a year. For the issue of hanging ports, Mikrotik support suggested a temporary solution using a scheduled script:
```
if([/ping gateways_IP count=10]=0)\do={/interfaceethernet disable[findwhereswitch=switch1];:delay3s;/interfaceethernet enable[findwhereswitch=switch1];log warning"Resetting switch1 !!!"}At some point, I received a pre-release version of RouterOS, which seemed to resolve the port hanging issue. Later, an official stable firmware update was released on July 16, 2024, and I received a notification from Mikrotik confirming that the solution for the port hang issue was included in this update. I updated to the latest stable release and have been keeping it up to date since then.However, on RouterOS 7.15.3, the port hanging problem reappeared, so I re-enabled the scheduled script. Since then, I have observed the script resetting all ports only once. I am uncertain whether this was due to the port hanging issue or simply a lack of ping response during other network activities at the time. I am continuing to monitor the situation closely.However, another problem occurs periodically: sometimes the network slows down almost to a complete stop. After extensive testing and debugging, I discovered that the switch occasionally sends random data to all network ports as packets. For example, I found a packet made from a fragment of JSON data, and the source (SRC) and destination (DST) MAC addresses were random (not present in the network). These packets are transmitted across the entire network as the switches attempts to locate the DST MAC address (receiver) but are ultimately dropped at the endpoints.Because the SRC MAC address is also random, it gets registered in the MAC tables of all network devices. Due to the high volume of random packets, the MAC tables on all devices grow rapidly, clearly indicating that the CRS354-48P-4S+2Q+ switch has started malfunctioning.Throughout this time, I performed various reconfigurations and tests. Today, the switch malfunctioned again. My test setup consisted of only a router and the switch, with all other ports disabled except one connected to the router. The router was configured with only a WAN interface and one port connected to the switch. The switch was transmitting random packets to the router, but the traffic from the router was clean. After rebooting the switch, the random traffic stopped in both directions. The CPU usage of the switch also dropped from ~30% to 6–9%. RouterOS v7.16.2, firmware updated.It seems like there is some kind of buffer overflow in the OS or a memory issue.I have provided all this information to Mikrotik support and am currently waiting for their response. In the meantime, I am preparing the device for return, either to replace it with another model or switch to a different brand, as I no longer have the time or energy to deal with these issues in a production network.

---
```

## Response 149
nezmogusThis unit has been a problem for 4.5 years.I think its time that Mikrotik just pull the thing.Looking into FS at this point myself. ---