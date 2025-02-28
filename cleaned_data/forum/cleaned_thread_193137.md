# Thread Information
Title: Thread-193137
Section: RouterOS
Thread ID: 193137

# Discussion

## Initial Question
Hello, I have a few of these UACC-CM-RJ45-MG new "multi-gig" NBASE-T RJ45 transceivers and they do not appear to be working in any of my SFP+-supported Mikrotik gear.I get no link activity with both autonegotiation and manual speed negotiation. This device seems similar to the S+RJ10, just using a newer revision BCM chip internally.Any plans to support it? ---

## Response 1
I doubt its a priority unless they have customer, (talking in the $100, 000+ range) that requests that functionality............. ---

## Response 2
I doubt its a priority unless they have customer, (talking in the $100, 000+ range) that requests that functionality.............If that were the stipulation, IPv6 would have been supported in RouterOS 5 lol.This doesn't seem like a huge deal to implement. Like I mentioned, it's based on a newer revision of similar hardware in the S+RJ10. If they're working on an /r3 of it they may be working on it already, just would be nice to hear from them directly. ---

## Response 3
What version of RouterOS are you running? What version of firmware is on the switch/router? There were some SFP+ updates in 7.4.1 and later I believe.I have a couple of the EA versions of those and they seem to work fine. The switch (or router, in my case a CCR2004) seems to negotiate 10G to the SFP+, which in turn negotiates 2.5G to the other device (in my most recent test, the latest revision of the Wave AP with a 2.5G copper port). ---

## Response 4
What version of RouterOS are you running? What version of firmware is on the switch/router? There were some SFP+ updates in 7.4.1 and later I believe.I have a couple of the EA versions of those and they seem to work fine. The switch (or router, in my case a CCR2004) seems to negotiate 10G to the SFP+, which in turn negotiates 2.5G to the other device (in my most recent test, the latest revision of the Wave AP with a 2.5G copper port).I'm on the 7.7 on all devices. CRS309 is firmware 7.6 (which I'm trying). I don't believe they worked in my CCR2004 either. Mine are EA as well. I don't get any links to any devices when they're in, with autonegotiation or manual setting. ---

## Response 5
And under System Routerboard the firmware also 7.7?7.8b2 has a warning that it's not for CRS300 devices. ---

## Response 6
And under System Routerboard the firmware also 7.7?7.8b2 has a warning that it's not for CRS300 devices.7.6 firmware. I'm not on 7.8b on any device. Didn't think 7.6 firmware mattered since you mentioned the fixes were 7.4.1 ---

## Response 7
Oh, I was reading on my phone on a rooftop, and I thought I saw 7.8 on the CRS309 instead of 7.6. (Guess it's time to get glasses.)Have you tried setting it to 2.5Gbps or 10Gbps without auto-negotiation? When I'm done with my outside work today, I'll have to take one of those and try it on a 309 in the lab. ---

## Response 8
Oh, I was reading on my phone on a rooftop, and I thought I saw 7.8 on the CRS309 instead of 7.6. (Guess it's time to get glasses.)Have you tried setting it to 2.5Gbps or 10Gbps without auto-negotiation? When I'm done with my outside work today, I'll have to take one of those and try it on a 309 in the lab.I tried 2.5Gbps without autonegotiation, but I haven't tried 10. I can try that and come back. ---

## Response 9
Oh, I was reading on my phone on a rooftop, and I thought I saw 7.8 on the CRS309 instead of 7.6. (Guess it's time to get glasses.)Have you tried setting it to 2.5Gbps or 10Gbps without auto-negotiation? When I'm done with my outside work today, I'll have to take one of those and try it on a 309 in the lab.So I just went down and tried it again, it seems to actually work on my CCR2004. However, on both my CRS309 and CRS328 I'm unable to get a link on any of the SFP+ ports. I even brought out an unopened one and that didn't work either. ---

## Response 10
Bumping this to see if anyone has any other experience/ideas/suggestions.Thanks! ---

## Response 11
Another bump, any feedback from 'Tik? ---

## Response 12
If you want to see any official feedback, contact Mikrotik support directly.But don't expect any quick fix, unless it's something really trivial. Then it might be fixed in one or two next ROS versions...If you need this working ASAP for a job, get a supported transceiver instead. ---

## Response 13
I'm interested as well. Did anyone manage to get these working? They worked out-of-the-box in a Intel X520-DA2, I thought they'll just work on Mikrotiks, but CRS309/310 seem to see them (I can see the model, vendor, etc.) but no link, in either autoneg or forced 10G. Running 7.8. ---

## Response 14
I'm interested as well. Did anyone manage to get these working? They worked out-of-the-box in a Intel X520-DA2, I thought they'll just work on Mikrotiks, but CRS309/310 seem to see them (I can see the model, vendor, etc.) but no link, in either autoneg or forced 10G. Running 7.8.I have a ticket open with Mikrotik in which they said they wanted to fix this and I provided them some logs and audit info for them to look into it. I haven't heard anything from them though, but I imagine it's on the table for the next update(s).OT: You said yours worked in an X520-DA2, what OS were you using them on, and did you have to do any mods for it to work? ---

## Response 15
I have a ticket open with Mikrotik in which they said they wanted to fix this and I provided them some logs and audit info for them to look into it. I haven't heard anything from them though, but I imagine it's on the table for the next update(s).OT: You said yours worked in an X520-DA2, what OS were you using them on, and did you have to do any mods for it to work?Thanks, I raised a ticket too, will see.As to the X520: stable Debian, custom kernel (5.10) but no mods, just took out S+RJ10, put this in, instant link. They don't support temp nor voltage monitoring (under Linux, at least), but I can actually hold my finger onto it, whereas with the S+RJ10 I couldn't. ---

## Response 16
That's good to know it works in X520 without any problems. I was looking for alternative to S+RJ10 because that runs as hot as fusion reactor... and X520 under full load is already plenty hot even with fan. So might give this one a try.. at least for X520 for now. Having it supported by ROS would be even better, running multiple S+RJ10s in a switch is horrible... you can feel the heat radiating from the SFP modules! ---

## Response 17
Did anyone retest with newer routeros, 7.10? ---

## Response 18
Did anyone retest with newer routeros, 7.10?Go, and test yourself. ---

## Response 19
I was looking for alternative to S+RJ10 because that runs as hot as fusion reactor.IMHO, having on the market, a 30$/€ SFP or SFP+ module supporting 1Gb/s or 2.5Gb/s would be very interesting if it can avoid such heat issues.If my memory serves me right, reducing speed from 10Gb/s to 2.5 Gb/s is not so easy "in an autoneg world" so if you ever meet some issue on a remote site, replacing a S+RJ10 with one such 2.5 Gb/s SFP/SFP+ module can help. ---

## Response 20
Did anyone retest with newer routeros, 7.10?Did a quick test - one CRS310 with S+RJ10, another one with the Ubiquity, both in autoneg - doesn't work. "RX loss" is shown all the time. ---

## Response 21
Thank you! I'm about to upgrade my home network to 10gbit, but have to use a few copper links. I started with a netpower 16p and S+RJ10, but this is running way to hot. I won't buy more S+RJ10 but wait until mikrotik releases a better sfp+ RJ45 adapter or supports the ubiquity one. This is a home network, I can wait ---

## Response 22
If you can pull cat6e (or cat7) UTP cables, then you could pull FO cables as well. And optical SFP modules generally don't suffer from the excessive heat generation problem. Plus the range is much longer. ---

## Response 23
If you can pull cat6e (or cat7) UTP cables, then you could pull FO cables as well. And optical SFP modules generally don't suffer from the excessive heat generation problem. Plus the range is much longer.+1 for fiber. If you need new cable anyway, pull multimode fiber. The SFP+ modules are a lot cheaper and far less hot, and the cabling costs roughly the same and is easier to handle to boot. ---

## Response 24
I have to use 2 Cat7 cables which should carry 10gbit, one is buried in the ground for 20m, the other goes through concrete (unfortunately without conduit so I can't replace it). Those were the first cables I installed, now I found fs.com and I really like their FTTA fiber optic cables, supplied ready with plugs. Cheaper than Cat7, strong and perfect for indoor and outdoor unprotected installation. Singlemode cables seems to be cheaper than multimode and can easily transmit 100gbit and more. Transceivers cost about the same, so I went with singlemode.I started with S-31DLC20D transceivers for 1Gbit, but for 10gbit the S+31DLC10D 10gbit is unfortunately discontinued (why??). So I tried the transceivers from fs.com, #29901 for Dual Speed 1gbit and 10gbit, working great here at 1gbit (need to replace the rb2011 to update to 10gbit). Combined with the heat of the S+RJ10, I should have gone with their "industrial" transceivers that work at higher temperatures (#153818). They even have transceiver which work with single mode and multimode (#158596). Maybe mikrotik should source their transceivers from fs.com ---

## Response 25
Yeah, it really sucks SFP+ and fiber in general is not more widespread as it's clearly superior. But good luck finding non-server motherboard with SFP+ instead of metallic 10GbE, even in $500+ range. Fiber is still seen as premium and server only by manufacturers, but in reality 2nd hand SFPs are dirt cheap, same for patch cables etc. ... but I guess everybody on this forum knows all this. It's just annoying in general, especially when you don't have a choice...</rant> ---

## Response 26
If you can pull cat6e (or cat7) UTP cables, then you could pull FO cables as well.I thought FO is harder to deploy than copper as:you can't easily pull a FO along its connector end within small conduits (20mm diameter or so)FO required minimum bend radiusyou can't pull the FO cable with the same strengthWhich FO cable would work around the above limitations ? ---

## Response 27
I always use the small LC connectors, they are slightly smaller than RJ45 connectors. The fiber cable is thinner than CAT7 cables, so you can put several cables in a 20mm conduit. You can even split the LC connector and put one piece a little behind the other, then the connector will have a minimal size. (but don't bend the second fiber too much, wrap it around the other strand). It is also possible to use special transceivers which only need one fiber for rx+tx on different wavelengths, then you save even more space. Or you can use 0.9mm cable and a field assembly connector....I usually push a pull wire through the empty conduit, then I attach the fiber cable to it with thin tape and protect the connectors with it. Then I pull it through the conduit, sometimes it helps if a second person pushes the fiber into the conduit on the other side. This is the same for CAT7 and fiber optic cables, but fiber optic cables are easier to pull in my opinion.There are many different types of fiber optic cable with different strengths and bend radii. I think the minimum bend radius of thin fiber optic cable is about the same as CAT7, but CAT7 is more robust, it doesn't break completely if you bend it a lot. But 10GBe probably won't work if you bend it too much. I bent a knot in a fiber optic patch cable, from a diameter of 2cm the signal at the receiver got worse, but the value got better after loosening the knot (but not as good as before). CAT7 also loses performance if you bend it a lot, but you can only measure that with professional equipment. With fiber cables, I don't need professional equipment to test the cables, I can just check the tx/rx power on the connected transceivers.In my house, I use standard and very cheap fiber patch cables when it is easy to run the cable. For complicated cases and outdoor I use FTTA cables from fs.com, they are strong and robust enough for me (400N). You can even buy stronger industrial or military cable if you want.One big argument against fiber: POE is impossible. But in case of a lightning strike it's a big advantage, because the overvoltage won't destroy all other connected devices. ---

## Response 28
I always use the small LC connectors,...Thank you very much for this very informative reply. ---

## Response 29
Yeah, tried it my CRS328-24P-4S+ and they are not working. Running latest RouterOS v7.11beta4. Really disappointing as these are only 1.9W and run much cooler than the usual 3W parts.I'll make a support ticket as well. ---

## Response 30
Well.I've been in contact with support on this and can now happily report as of latest version v7.11, for me this is now working!!!No more RX Loss.I did not see any mentioning of it in the changlog, but it's working now.Great work Mikrotik. ---

## Response 31
Latest 7.11 release? And what switch are you using?I just tested this with 7.11 release version and mine are still not working. I suspect this may have to do with mine being EA models at this point, but not sure.Edit: well it does actually work in my CRS328, but not in my CRS309. Not sure what's going on there. ---

## Response 32
I tried it right now, in Netpower 16p it doesn't work. I tried 7.11 and 7.12-beta1, It always signals RX loss. Do you have a ticket number? Then I‌ can reference it when contacting support.
```
/interfaceethernet monitor sfp-sfpplus2# 2023-08-22 12:20:10 by RouterOS 7.11# software id = 3VVI-W6C1#name:sfp-sfpplus2
                             status:no-linkauto-negotiation:failed
                        advertising:link-partner-advertising:sfp-module-present:yes
                        sfp-rx-loss:yes
                       sfp-tx-fault:nosfp-type:SFP/SFP+/SFP28
                 sfp-connector-type:RJ45
  sfp-link-length-copper-active-om4:100msfp-vendor-name:UbiquitiInc.sfp-vendor-part-number:UACC-CM-RJ45-MG
                sfp-vendor-revision:U07
                  sfp-vendor-serial:AK23017502216
             sfp-manufacturing-date:23-01-28eeprom-checksum:good
                             eeprom:0000:03042210000000204004800667000000.."....  @...g...
                                     0010: 00 00 64 00 55 62 69 71  75 69 74 69 20 49 6e 63  ..d.Ubiq uiti Inc
                                     0020: 2e 20 20 20 00 24 5a 4c  55 41 43 43 2d 43 4d 2d  .   .$ZL UACC-CM-
                                     0030: 52 4a 34 35 2d 4d 47 20  55 30 37 20 03 52 00 e9  RJ45-MG  U07 .R..
                                     0040: 00 00 00 00 41 4b 32 33  30 31 37 35 30 32 32 31  ....AK23 01750221
                                     0050: 36 20 20 20 32 33 30 31  32 38 20 20 00 00 08 91  6   2301 28  ....
                                     0060: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ........ ........
                                     *

---
```

## Response 33
Hi.Support ticket is SUP-121423. I had some initial back and forth communication with them, but then they went silent. This was on a CRS328-POE switch.In the meantime it seems they fixed the problems (either by actually looking into it, or I just got lucky that fixing something else also fixed this issue. Who knows...).I reported back to them that my issues are now fixed, but still no reply.Hopefully they can solve your issues as well as I think these run quite a bit cooler than my other versions. ---

## Response 34
They did fix it on the 328, but it's still not working on my 309. My ticket is also silent with replies. Hopefully they'll address it in the next couple versions. ---

## Response 35
I've been in contact with support on this and can now happily report as of latest version v7.11, for me this is now working!!!No more RX Loss.I was trying RB5009 + this UACC-CM-RJ45-MG on 7.11.2 and nope. It can see it, but nothing can be negotiated (1000Mbit/s on the other side), even if I put manual speed, also doesn't work. ---

## Response 36
Just checked with 7.12 beta 9 and still the same. Why why did they fix it only on some models… ---

## Response 37
7.12rc5 has changes to 98DX226S switch chip. I tried it on Netpower 16p, UACC-CM-RJ45-MG still does not work, always RX Loss detected. ---

## Response 38
For what is worth: after waiting and waiting, I gave up and searched for a different, low-power RJ45 transceiver. I bought one from fs.com (SFP-10G-T100, part number #154925, chipset Broadcom, and marked as Power: ≤1.8W) and that just worked when plugged into a CRS309. On the other end is a S+RJ10 for now (I immediately ordered a few more from fs.com).This is clearly more efficient than the S+RJ10:it doesn't burn my finger when I touch itthe "cpu temperature" has decreased by 1-2 celsius since thenThe transceiver itself doesn't have a temperature sensor, but as the S+RJ10 was reporting ~85 celsius before I took it off, and this not burning me, I'm sure there's a large difference.Now I'm stuck with a few Ubiquity ones that don't seem to get any traction, sigh. ---

## Response 39
For what is worth: after waiting and waiting, I gave up and searched for a different, low-power RJ45 transceiver. I bought one from fs.com (SFP-10G-T100, part number #154925, chipset Broadcom, and marked as Power: ≤1.8W) and that just worked when plugged into a CRS309. On the other end is a S+RJ10 for now (I immediately ordered a few more from fs.com).This is clearly more efficient than the S+RJ10:it doesn't burn my finger when I touch itthe "cpu temperature" has decreased by 1-2 celsius since thenThe transceiver itself doesn't have a temperature sensor, but as the S+RJ10 was reporting ~85 celsius before I took it off, and this not burning me, I'm sure there's a large difference.Now I'm stuck with a few Ubiquity ones that don't seem to get any traction, sigh.fs.com from my expirience is by far better than UBNT ...their fiber cables and (Q)SFPs are a price/performance no-brainer and you can even rebrand them if needed (got them introduced at work and running a bunch of 100G QSFPs in cisco n9k 9364C and a bunch of sfp+ with FC on SM and MM and some copper sfp and sfp+ from fs.com .... running really smooth) ---

## Response 40
I bought one from fs.com (SFP-10G-T100, part number #154925, chipset Broadcom, and marked as Power: ≤1.8W)This looks great, but I have to ask, did you really pay $139 per adapter? That's what it's listed for at fs.com right now (the 100m version, which seems to be the only one with the low 1.8W rating) ---

## Response 41
Hi everyone.Any change for UACC-CM-RJ45-MG on ROS 7.13?Thanks! ---

## Response 42
I bought one from fs.com (SFP-10G-T100, part number #154925, chipset Broadcom, and marked as Power: ≤1.8W)This looks great, but I have to ask, did you really pay $139 per adapter? That's what it's listed for at fs.com right now (the 100m version, which seems to be the only one with the low 1.8W rating)I didYes, it's expensive, but also it was the easiest (and possibly the cheapest) way to solve the one link I need at 10G over copper. ---

## Response 43
I didYes, it's expensive, but also it was the easiest (and possibly the cheapest) way to solve the one link I need at 10G over copper.OK, thanks for confirming, and thanks for the hint about the product in the first place! ---

## Response 44
For what is worth: after waiting and waiting, I gave up and searched for a different, low-power RJ45 transceiver. I bought one from fs.com (SFP-10G-T100, part number #154925, chipset Broadcom, and marked as Power: ≤1.8W) and that just worked when plugged into a CRS309.Another question, if I may. I ordered this adapter as well but when I plugged it into the SFP+ slot on the CRS309, it does not link up. I also have an S+RJ10 on the other side. I can see the vendor/serial info etc. in the SFP tab, but it won't connect.Did you do anything else when you started using it in the CRS309? ---

## Response 45
For what is worth: after waiting and waiting, I gave up and searched for a different, low-power RJ45 transceiver. I bought one from fs.com (SFP-10G-T100, part number #154925, chipset Broadcom, and marked as Power: ≤1.8W) and that just worked when plugged into a CRS309.Another question, if I may. I ordered this adapter as well but when I plugged it into the SFP+ slot on the CRS309, it does not link up. I also have an S+RJ10 on the other side. I can see the vendor/serial info etc. in the SFP tab, but it won't connect.Did you do anything else when you started using it in the CRS309?Initially no, but after the most recent version (7.13), I need to force link speed to fixed. I haven’t tried mixed, only same transceiver on both ends, both with fixed ---

## Response 46
Initially no, but after the most recent version (7.13), I need to force link speed to fixed. I haven’t tried mixed, only same transceiver on both ends, both with fixedI am on 7.13 and I can confirm that it does indeed start to work for me when I turn off auto-negotiation and configure the speed manually. It did not work with different adapters on both ends, I had to use two of the FS ones. Now I'll see how much cooler they run.I wonder if disabling auto-negotiation would also make it work for the Ubiquiti ones.Thanks again for the tips! ---

## Response 47
Initially no, but after the most recent version (7.13), I need to force link speed to fixed. I haven’t tried mixed, only same transceiver on both ends, both with fixedI am on 7.13 and I can confirm that it does indeed start to work for me when I turn off auto-negotiation and configure the speed manually. It did not work with different adapters on both ends, I had to use two of the FS ones. Now I'll see how much cooler they run.I wonder if disabling auto-negotiation would also make it work for the Ubiquiti ones.Thanks again for the tips!I filed a support ticket with MikroTik requesting that they fix that issue and fully support this FS.com module. The support case number is SUP-142140. ---

## Response 48
Anyone able to test UACC-CM-RJ45-MG with ROS 7.14? Thanks! ---

## Response 49
Tested CRS326-24G-2S+ ROS 7.14.3 and CSS610-8P-2S+ SwOS 2.18 with UACC-CM-RJ45-MG. Both not working ---

## Response 50
Just tested a UACC-CM-RJ45-MG on 7.15.3 on a CCR2004-16G-2S+ and still not working. ---

## Response 51
anyone tried this with 7.16? this is pretty much holding me back from making a purchase ---

## Response 52
A lot of generic platitudes and non-answers as usual.It's SFP.It is an industry standard.I plug the thing in: it should work.We're not talking about a 1 petabyte gigahyper quantum-link subspace transformer module. It's a friggin' RJ45 jack! I'm asking for 1Gbps, not even the 2.5Gbps the SFP input takes. ---

## Response 53
It's SFP. It is an industry standard.You'd think.And you'd think wrong.Why else would FS.com ship agiven modulematching the rough specs of this thread's topic in 20 different versions plus "Generic," each with a different product ordering attribute? Why would their staff follow up after the order to make sure you selected the right one for your specific application? Why would they offer afirmware reprogrammerfor moving existing modules from one vendor to another?There do exist generic modules, but in my experience, they lack features, suggesting a lowest-common-denominator approach. ---

## Response 54
In my experience coding the SFP(+) for different vendors is only done to get around vendor lock-in. I even have a few original Cisco FET-10G modules that won't even work in non-Nexus Cisco boxes, which work just fine in my CRS-309 and get recognized for what they are, 100m reach 10GBASE-SR. ---

## Response 55
It's SFP. It is an industry standard.You'd think.And you'd think wrong.Why else would FS.com ship agiven modulematching the rough specs of this thread's topic in 20 different versions plus "Generic," each with a different product ordering attribute? Why would their staff follow up after the order to make sure you selected the right one for your specific application? Why would they offer afirmware reprogrammerfor moving existing modules from one vendor to another?There do exist generic modules, but in my experience, they lack features, suggesting a lowest-common-denominator approach.Thanks for the guidance and my apologies for the heated attitude I brought in as my first post. I’ve absolutely enjoyed using Mikrotik products. I first familiarized myself with it almost a decade ago whilst living in Rīga, Latvia when it was still relatively unknown in the wider world, where it was used in the apartment complex I lived. Just recently though I purchased my first own home for the family here in Finland and based on a Canadian friend’s recommendation chose a mix of Mikrotik routers and Ubiquiti APs for building a home network. They have worked together surprisingly well. Just somehow I got hit in the face when I hoped to gain an extra Ethernet port by buying an RJ45 SFP module. I had indeed reviewed the official manual listing SFP compatibility for each RouterOS device, and had assumed the lowest tier of 1Gbps copper modules would all work. The only immediately available SFP RJ45 module I had nearby was one by Ubiquiti. I have little experience with enterprise level network equipment so I naturally assumed SFP was a standard and much like CAT6 as long as it has the designation it would work. I have now ordered a Mikrotik RJ45 module as a replacement and will report back. ---

## Response 56
In my experience coding the SFP(+) for different vendors is only done to get around vendor lock-in.The experience behind the post above is from accidentally ordering a Huawei-coded version ofFS.com's SFP-10G-T-30Iafter being advised that this unit runs far cooler thanMikroTik's S+RJ10, the closest first-party equivalent.(The heat difference is allegedly due to it supporting only 1G and 10G instead of the six speeds of the MT module, not because it's "industrial," though thatdoesmean it can deal with the heat better regardless.)Problem is, the temperature readout on the FS module doesn't work! (Just re-checked on 7.17rc2.) I have reason tobelievethat it's running cooler, but this is only by inference from the surrounding modules' temperature readouts. For this price, I did expect to get temp readout on-module.I could have returned it for a MikroTik-coded one, whichissupposed to give temp readouts, but I needed it in-service right immediately then. ---

## Response 57
I can additionally confirm that another SFP product by Ubiquiti is incompatible with the latest stable RouterOS. Product is theUACC-CM-RF45-1G, running RoS on 7.16.1Connecting it and a standard CAT6 RJ45 plug yields no lights and no established link. Curiously, RoS is able to detect the module and decipher it partially:
```
interfaceethernet monitor sfp-sfpplus2
                               name:sfp-sfpplus2
                             status:no-linkauto-negotiation:donesupported:10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full,1G-baseX,2.5G-baseT,2.5G-baseX,5G-baseT,10G-baseT,10G-baseSR-LR,10G-baseCR
                      sfp-supported:10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
                               name:sfp-sfpplus2
                             status:no-linkauto-negotiation:donesupported:10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full,1G-baseX,2.5G-baseT,2.5G-baseX,5G-baseT,10G-baseT,10G-baseSR-LR,10G-baseCR
                      sfp-supported:10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
                        advertising:10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
           link-partner-advertising:sfp-module-present:yes
                        sfp-rx-loss:nosfp-tx-fault:nosfp-type:SFP/SFP+/SFP28/SFP56
                 sfp-connector-type:RJ45
  sfp-link-length-copper-active-om4:100msfp-vendor-name:UbiquitiInc.sfp-vendor-part-number:CM-RJ45-1Gsfp-vendor-revision:A1
                  sfp-vendor-serial:AX23082802353
             sfp-manufacturing-date:23-08-07eeprom-checksum:good
                             eeprom:0000:0304220000000800000000010d000000.."..... ........
                                     0010: 00 00 64 00 55 62 69 71  75 69 74 69 20 49 6e 63  ..d.Ubiq uiti Inc
                                     0020: 2e 20 20 20 00 24 5a 4c  43 4d 2d 52 4a 34 35 2d  .   .$ZL CM-RJ45-
                                     0030: 31 47 20 20 20 20 20 20  41 31 20 20 00 00 00 5a  1G       A1  ...Z
                                     0040: 00 00 00 00 41 58 32 33  30 38 32 38 30 32 33 35  ....AX23 08280235
                                     0050: 33 20 20 20 32 33 30 38  30 37 20 20 00 00 00 a1  3   2308 07  ....
                                     0060: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ........ ........
                                     *Do we have any information on a possible patch of some sort to fix compatibility?

---
```

## Response 58
I can additionally confirm that another SFP product by Ubiquiti is incompatible with the latest stable RouterOS. Product is theUACC-CM-RF45-1G, running RoS on 7.16.1Connecting it and a standard CAT6 RJ45 plug yields no lights and no established link. Curiously, RoS is able to detect the module and decipher it partially:
```
interfaceethernet monitor sfp-sfpplus2
                               name:sfp-sfpplus2
                             status:no-linkauto-negotiation:donesupported:10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full,1G-baseX,2.5G-baseT,2.5G-baseX,5G-baseT,10G-baseT,10G-baseSR-LR,10G-baseCR
                      sfp-supported:10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
                               name:sfp-sfpplus2
                             status:no-linkauto-negotiation:donesupported:10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full,1G-baseX,2.5G-baseT,2.5G-baseX,5G-baseT,10G-baseT,10G-baseSR-LR,10G-baseCR
                      sfp-supported:10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
                        advertising:10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
           link-partner-advertising:sfp-module-present:yes
                        sfp-rx-loss:nosfp-tx-fault:nosfp-type:SFP/SFP+/SFP28/SFP56
                 sfp-connector-type:RJ45
  sfp-link-length-copper-active-om4:100msfp-vendor-name:UbiquitiInc.sfp-vendor-part-number:CM-RJ45-1Gsfp-vendor-revision:A1
                  sfp-vendor-serial:AX23082802353
             sfp-manufacturing-date:23-08-07eeprom-checksum:good
                             eeprom:0000:0304220000000800000000010d000000.."..... ........
                                     0010: 00 00 64 00 55 62 69 71  75 69 74 69 20 49 6e 63  ..d.Ubiq uiti Inc
                                     0020: 2e 20 20 20 00 24 5a 4c  43 4d 2d 52 4a 34 35 2d  .   .$ZL CM-RJ45-
                                     0030: 31 47 20 20 20 20 20 20  41 31 20 20 00 00 00 5a  1G       A1  ...Z
                                     0040: 00 00 00 00 41 58 32 33  30 38 32 38 30 32 33 35  ....AX23 08280235
                                     0050: 33 20 20 20 32 33 30 38  30 37 20 20 00 00 00 a1  3   2308 07  ....
                                     0060: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ........ ........
                                     *Do we have any information on a possible patch of some sort to fix compatibility?Upgrading to 7.17beta2 yielded similar results, SFP is detected but no link is established. Manually configuring negotiation to any of the standard 1G/100M/10M both full and half duplex also doesn't help as it did some users. I'm going to on a limb and assume there's no compatibility. I'll try notifying Mikrotik support for further assistance.

---
```

## Response 59
By chance I found out today that the transceiver works with 2.5g, 5g and 10g! Only 1g and slower doesn't work. I always tested against one of the 1g ports on the switch and failed. It runs now on a Netpower 16p with 7.17rc3, negotiated stable to 5g. 2.5g, 5g and 10g are always shown as 10g in winbox, you can't influence the speed. ---

## Response 60
I was also not able to get UACC-CM-RJ45-MG to work in a CRS309. The module is recognised in the CRS309 but I can't get it to link with an identical module in a Unifi switch on the other end.I also wanted to find a BCM84891-based SFP+ module as the S+RJ10 runs at 95C+ at 10G and hits thermal cutoff.I can report that the 10Gtek ASF-10G-T80 SFP+ modules work well in the CRS309. They autonegotiate at 10G and report temperature, voltage, tx/rx power to RouterOS.The module reports itself as SFP-10G-T to RouterOS.https://www.amazon.co.uk/10Gtek-10GBase ... B09GY2MVLFThere are a few similar modules, the 80m variant is the correct one. ---