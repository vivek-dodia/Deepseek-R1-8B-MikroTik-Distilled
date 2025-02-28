# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 178693

# Discussion

## Initial Question
Author: Mon Sep 20, 2021 10:04 am
Hi everyone, I've read several other topics about band steering and 5Ghz priority here on the forum. So I quite have the picture.Ever since I have my Chateau12 I wondered, why so many clients register with wlan1 (2.4Ghz) and hardly none at wlan2 (5Ghz). But I did not research, because there were other fields in ROS 7 that got my attention.So now I thought it is time to find out whats happening. So I opened the wireless network scanner on my macbook to find out, why it connects to 2.4Ghz instead of the faster 5Ghz.Please see it as an example:RSSI of 2.4Ghz: about -50RSSI of 5Ghz: about -70Where -70 is just a decent signal for 5Ghz, the client uses 2.4Ghz instead. After reconnecting Macbook-wifi, it first connects 5Ghz sometimes, but switched to 2.4Ghz after some 1 or 2minutes.I used Wifi-analyzer for Android, in most rooms/places where I use wifi-devices, I have round-about -70RSSI for 5Ghz.Mikrotik features no band steering.First approach:I added a wireless access lists to prevent clients to access wlan1 (2.4Ghz) in a signal better than -70RSSI. But that kind of sucks, as some of my clients are 2.4Ghz only (like Hap lite, map lite) and would not connect anymore. And I do not like to add some "whitelist" just for these devices. So I reverted the whitelist stuff again.Second approach:Lower tx-power of wlan1. I increased antenna-gain to 10. Now wlan1 transmits at 10dbm (was 17dbm) before. 2.4Ghz wireless signal got a little weaker, but still it has significant better RSSI than 5Ghz. But it seems, that some clients now already switch over to 5Ghz. But just a few. On the other hand I like to have wifi-signal when I am outside the house and/or at a far away room. So I'd like to keep TX-power at it's regulatory-maximum.Has anyone a better idea? Anyone has a script, that emulates some kind of "poor man's band steering"?It really annoys me, that sitting away like 5 meters from my Chateau12, that devices use 2.4Ghz. That's not nice and needs at least an improvement - when there is no real solution available.Thanks. ---

## Response 1
Author: Mon Sep 20, 2021 10:11 am
If you have already read all other topic, why open anoter one?Except what you already have read, there is not a solution (for now, until mikrotik does something) ---

## Response 2
Author: Mon Sep 20, 2021 10:21 am
Because I did not want to hi-jack other topics. Some OPs have other requirements like "my 2.4 is so crowded. I'd like to limit clients or force them to 5g". Some are about capsman. Some topics date back to 2017. I did not want to bring up my question in a topic with already 100 comments. ---

## Response 3
Author: Mon Sep 20, 2021 10:25 am
All what Mikrotik does is ©normis: "but when 5g and 2g signal is same, then apple chooses 5g"But that is academical. When there is a simple obstacle (NOT even a wall) in router direction - 2g has better RSSI. ---

## Response 4
Author: Mon Sep 20, 2021 10:27 am
I prefer to use your second approach and add more accesspoints. Especially outside! And both your devices but also your neighbors will prefer it. ---

## Response 5
Author: Mon Sep 20, 2021 2:21 pm
Use more APs. Shut of 2.4 on most of them. Turn down the 2.4 on the working ones. Bounce the 2.4 off and on for a few seconds at some interval.This is how I managed to steer devices onto 5Ghz if they have it.I started making this script that would add devices to and ACL once they connected to 5GHZ. Then I was going to use a rule that would check that ACL vs the signal on 2.4 and boot it...Then Apple/Google/Microsoft started adding the "private random Mac address" BY DEFAULT!!! That shot down my plans... ---

## Response 6
Author: Mon Sep 20, 2021 9:35 pm
2.4ghz down to 10dbm. 5gzh at 21dbm. But still only ONE device connects to 5ghz. The others all go to 2.4ghz. But Mikrotik does not see any problem.... ---

## Response 7
Author: Tue Sep 21, 2021 2:58 pm
``` 
```
/interface wireless
set [ find default-name=wlan1 ] default-authentication=no

/interface wireless access-list
add allow-signal-out-of-range=30s interface=wlan1 signal-range=-120..-70
add interface=wlan1 mac-address=08:55:31:E4:E4:C9 comment="haplite 2ghz only"
```

Given that reducing TX-power of wlan1 to 10dbm did not improve the situation. Now I am back at a simple access-list solution. Not that optimal - but it works for now. I refuse to connect to 2.4ghz if signal is better than -70. It maybe could work with -60 or -65 too - but I need to slowly go down and watch the behaviour.I have only 2 devices that only support 2.4ghz band. HAP-lite and MAP-lite. The map is quite far away and has a signal of -75 due to the distance itself. The HAPlite is whitelisted.


---
```

## Response 8
Author: Tue Sep 21, 2021 3:05 pm
``` 
```
IF device already connected to wlan2 AND want to connect to wlan1 AND wlan2-signal is better than -80: DENY connect to wlan1
```

One thing I noticed/observed:Some of my clients (Android, Macbook) first connect to 5ghz and switch over to 2.4ghz within approx a minute after connecting to 5ghz.For me this looks like, that these devices prefer 5ghz by default. They connect. Then they find 2.4ghz with "better" signal and switch over.--Has someone a script, that can handle following scenario?Pseudocode:


---
```

## Response 9
Author: Tue Sep 21, 2021 5:34 pm
First the client often has option to select "preferred band".Then what you need is Access rules per Wifi interface.Example: client A has at same location 70 RSSI in 5Ghz and 55 RSSI in 2.4--> Allow connection to 5Ghz -120..120 (it can always try to connect to 5G)--> Allow connection to 2.4Ghz -120..-65 (only if signal is getting below -65 (which then would be ~-90 in 5G)This means 2.4G will only be used when signal becomes pretty bad.Inconvenience is, you need to do this per client as signal levels are different per client...But for an environment with known clients and a bit of tuning, this can do quit well. ---

## Response 10
Author: Tue Sep 21, 2021 5:40 pm
Isn't that quite similar to my current access-list configuration I posted above? ---

## Response 11
Author: Tue Nov 30, 2021 9:52 am
This is how it looks like without access list rules. It is quite useless to have 5ghz enabled at all, as not a single client would connect to it. they all prefer wlan1 cause of slightly better RSSI.Screenshot_20211130-084629.pngt ---

## Response 12
Author: Tue Nov 30, 2021 12:28 pm
Do you have access to a spectrum analyser that covers both the 2.4GHz and 5GHz bands?In free space, 5GHz suffers from around 7dB more attenuation than 2.4GHz, so you'd need to have to reduce the 2.4GHz signal by 7dB minimum just to give them the same signal strength at the client device.Now, you've reduced the signal by 10dB by increasing the "gain" value on the antenna, but only a spectrum analyser will tell you whether that actually means the signal strength was down by enough at the client device, ignoring the effects of walls, bodies and everything else you find in the average home/office.If you don't have a spectrum analyser, you can still see what happens when you set the antenna gain back to default and reduce the TX power setting by 12 or even 15dB on the 2.4GHz radio. This is more likely to give a stronger signal strength on 5GHz at least in the room the AP is in and you should get devices preferring that band. ---

## Response 13
Author: Tue Nov 30, 2021 12:48 pm
This is a difficult one to solve in wifi. Because in wifi the CLIENT decides which band to use. This is different from mobile networks (3G, 4G, 5G ...) where the network devices decide who will serve a client at what band. "Band steering" in wifi will never be perfect. Client devices use different algoritmes for making the decision.KIcking a client off or refusing the 2.4GHz might help, if the client learns that some AP/band has a bad connection. Otherwise it is just statistics. Flapping between bands is also a common problem for some clients (Some smartphones tend to swap after each sleeping period. Sometimes you see 4 second connections.). The algoritmes are unknown and divers.The "station roaming" is more active with lower signal level. Adding more AP and giving better coverage reduces the roaming attempts. (MT station can switch this on or off. The default behaviour has changed from on to off in RouterOS. With "off" the station will not be scanning for a better AP in the background, as can be followed in the "wireless, debug" logging.One way to mitigate is adding a second SSID that is band specific. For stable and well behaving clients the common name can be used. But again be carefull as the client might swap to the other SSID name if it is a known network.How can we inform the client what we want? Maybe (maybe!) abusing the Hotspot 2.0 "Interworking profiles" might be a way to inform the clients what we want, as 802.11k 802.11v is missing.Some reading:https://www.networkcomputing.com/wirele ... ring-myths ---

## Response 14
Author: Tue Nov 30, 2021 12:51 pm
If you don't have a spectrum analyser... you might use just another MT AP in station mode to measureviewtopic.php?t=170014#p852871 ---

## Response 15
Author: Tue Nov 30, 2021 7:24 pm
bpwlIf only... I swear...Moving on...I think I recall a document I read a long time ago about "holding the 2.4 transmit beacon" to get the client to hear the 5 first.The trick I tried for a little bit was making an ACL that kicked off MAC address groups that I "figured" had 5 GHZ radios is the 2.4 signal range was above 75. I got the idea when I was trying to make URC remotes connect to the right room when you move around.Alas the 2.4 radios dropping or no longer passing traffic while still showing connected in caps man wasted a ton of my time.Since I gave up on caps-man for having 2014 ACv1 drivers in radios today... I stopped trying to pick a turd by the clean end. ---

## Response 16
Author: Tue Nov 30, 2021 8:43 pm
Since I gave up on caps-man for having 2014 ACv1 drivers in radios today... I stopped trying to pick a turd by the clean end.Yes it is not easy. The weapons we get are very limited. One can play with minimal RSSI, and with higher basic rates. Just kicking off clients from the wifi does not instruct the client on what else to do, only to try again. Higher basic rates to avoid clients with disturbed reception to keep trying to reconnect. (Just kicked out my friends airco unit from his AP with MAC address and access list, The espressive system in there now attempts reconnection 3 times per second.)Is RSSI the critrerion for the access list we want? Maybe not, I have BYOD clients connecting at 54Mbps @ -86dBm, and at 12 Mbps @ -72 dBm but poor CCQ. Saving AP beacon broadcast time? Kicking off sticky clients? Well maybe yes. What I want is preserve air-time, and use it with the best possible throughput. So that 12Mbps was even worse with its 3 fold average retransmit.2014 ACv1 drivers? Optimistic? I rather see "802.11n" drivers adapted for "ac" hardware, enough to make it work. A-MSDU and A-MPDU buffer sizes are too small for good AC performance, but the needed RAM may be missing. And newer "ac" developped aditional adaptive weapons are missing. So we have to fight with what we have, and use Dog Poo Bags to keep the hands clean. ---

## Response 17
Author: Wed Dec 01, 2021 7:17 am
And you still refuse to say GARBAGE!As to your comment about "going to battle"...Mikrotik gave me cotton candy, to throw at steel tanks.I swear... You are clearly better than I am at wireless... If you would just publiclly call Mikrotik wireless for how deeply flawed it is... And stop apologizing for it... Maybe Mikrotik might actually address things???I had to go back and forth with them for months (and had to call them out here when weeks would pass between emails) before they copped to the fact that it was their wireless causing all my customers problems.It cost my company thousands to replace all those radios. ---

## Response 18
Author: Wed Dec 01, 2021 7:57 am
It's all point of view.Majority of people using these devices do not have access to internet allowing to stress those devices enough.There are plenty of cases where this underperforming WiFi is more then sufficient.E.g I have two cap devices I use in a rental home. I don't care the speed never goes beyond 100mbps. Main line is at best 15 mpbs using SXT LTE !It's located in the middle of nowhere. Half of the time literally no cell reception, not even for phone calls.It does not matter to use more expensive and maybe less easy to handle equipment from another vendor.Not saying the performance problems do not need to be fixed, they certainly do, just giving some perspective. For the majority of customers, there is no problem. They just need a working wifi. Period. ---

## Response 19
Author: Wed Dec 01, 2021 9:32 am
I have to agree with holvoetn.I have 300Mb down service and I am using the cAP ac in my home, managed by capsman. None of my wireless use-cases require massive throughput, I use wireless on my family's phones and tablets, where the most stressing traffic is some video streaming and some Zoom usage. None of that needs huge WiFi throughput.For laptops, the same thing applies except when I need to work with larger video files. For this I use a wired GbE connection on my dock anyway.Even downloading large files like OS or software updates isn't a problem over a sub-150Mb WiFi connection as I'm never in a position where if something doesn't download in 37 seconds flat the earth will stop turning.Yes, Mikrotik should address the issues , but even then I believe they should focus on stability in crowded spectrum over pure speed. Other than for speed tests and pure bragging rights, on WiFi speed is rarely the most important part of a connection, stability and being able to support more clients is much more important for most people. ---

## Response 20
Author: Wed Dec 01, 2021 2:04 pm
Reading comprehension...My main problem with MIKROTIK WIRELESS is the "giving up in crowded environments".I gave in to the idea... "Well if you have S--t internet service... It's not gonna be as apparent." That's how I tried to justify the lousy throughput once you have more than like 5 devices.THE PROBLEM IS CONNECTIVITY!!! I had the same problem again and again. The 2.4 radio would show all sorts of disconnect messages. And of course things didn't work. But EVEN WORSE would be clients that "appeared fine". Caps-man would show the devices as connected with good numbers. But things don't actually pass.The cure... You have to restart the radio.How do you detect that device are no longer working??? You have to find something else connected to that radio to net watch. (Like a printer) When it drops... Cycle that radio. Then magically... That OTHER device, that "looked fine" starts passing traffic again.With more and more devices relying on wifi... Basing the network on Mikrotik wireless... Doesn't make any sense. ---

## Response 21
Author: Sat Jan 22, 2022 12:38 pm
2.4ghz down to 10dbm. 5gzh at 21dbm. But still only ONE device connects to 5ghz. The others all go to 2.4ghz. But Mikrotik does not see any problem....We have many devices not capable of using DFS channels. Try disabling them in your router and see if your devices come up in the 5ghgz band. ---

## Response 22
Author: Wed Feb 09, 2022 4:30 pm
Good afternoon, can please anybody advise why my 5Ghz interfaces always shows up 17dBm though I'm changing the Tx power value in Channels sections and I'm setting it to 20dBm or otherhttps://imgur.com/a/CjovlwZ ---

## Response 23
Author: Wed Feb 09, 2022 5:39 pm
You might want to read this:https://help.mikrotik.com/docs/display/ ... he802.11acIf you have 2 chains, 20dbm - 3dbm = 17dbm ---

## Response 24
Author: Wed Feb 09, 2022 8:57 pm
``` 
```
[admin@Omnitik] > interface wireless info country-info etsi
  ranges: 2402-2482/b,g,gn20,gn40(20dBm)
          5170-5250/a,an20,an40,ac20,ac40,ac80,ac160,ac80+80(23dBm)/passive,indoor
          5170-5330/a,an20,an40,ac20,ac40,ac80,ac160,ac80+80(20dBm)/dfs,passive,indoor
          5250-5330/a,an20,an40,ac20,ac40,ac80,ac160,ac80+80(20dBm)/dfs,passive,indoor
          5490-5710/a,an20,an40,ac20,ac40,ac80,ac160,ac80+80(27dBm)/dfs,passive
          5190-5310/a-turbo(20dBm)/dfs
          5180-5300/a-turbo(20dBm)/dfs
          5520-5680/a-turbo(27dBm)/dfs,passive
          5510-5670/a-turbo(27dBm)/dfs,passive
          902-927/b,g,g-turbo,gn20,gn40(30dBm)


[admin@MktwAPac] /interface wireless info> allowed-channels 
interface: wlan2
  channels: 5180/20-Ce/ac/P(21dBm),5185/20-Ce/ac/P(21dBm),5190/20-Ce/ac/P(21dBm),5195/20-Ce/ac/P(21dBm),
            5200/20-Ce/ac/P(21dBm),5205/20-Ce/ac/P(21dBm),5210/20-Ce/ac/P(21dBm),5215/20-Ce/ac/P(21dBm),
            5220/20-Ce/ac/P(21dBm),5180/20-Ce/ac/DP(18dBm),5185/20-Ce/ac/DP(18dBm),5190/20-Ce/ac/DP(18dBm),
            5195/20-Ce/ac/DP(18dBm),5200/20-Ce/ac/DP(18dBm),5205/20-Ce/ac/DP(18dBm),5210/20-Ce/ac/DP(18dBm),
            5215/20-Ce/ac/DP(18dBm),5220/20-Ce/ac/DP(18dBm),5225/20-Ce/ac/DP(18dBm),5230/20-Ce/ac/DP(18dBm),
            5235/20-Ce/ac/DP(18dBm),5240/20-Ce/ac/DP(18dBm),5245/20-Ce/ac/DP(18dBm),5250/20-Ce/ac/DP(18dBm),
            5255/20-Ce/ac/DP(18dBm),5260/20-Ce/ac/DP(18dBm),5265/20-Ce/ac/DP(18dBm),5270/20-Ce/ac/DP(18dBm),
            5275/20-Ce/ac/DP(18dBm),5280/20-Ce/ac/DP(18dBm),5285/20-Ce/ac/DP(18dBm),5290/20-Ce/ac/DP(18dBm),
            5295/20-Ce/ac/DP(18dBm),5300/20-Ce/ac/DP(18dBm),5260/20-Ce/ac/DP(18dBm),5265/20-Ce/ac/DP(18dBm),
            5270/20-Ce/ac/DP(18dBm),5275/20-Ce/ac/DP(18dBm),5280/20-Ce/ac/DP(18dBm),5285/20-Ce/ac/DP(18dBm),
            5290/20-Ce/ac/DP(18dBm),5295/20-Ce/ac/DP(18dBm),5300/20-Ce/ac/DP(18dBm),5500/20-Ce/ac/DP(25dBm),
            5505/20-Ce/ac/DP(25dBm),5510/20-Ce/ac/DP(25dBm),5515/20-Ce/ac/DP(25dBm),5520/20-Ce/ac/DP(25dBm),
            5525/20-Ce/ac/DP(25dBm),5530/20-Ce/ac/DP(25dBm),5535/20-Ce/ac/DP(25dBm),5540/20-Ce/ac/DP(25dBm),
            5545/20-Ce/ac/DP(25dBm),5550/20-Ce/ac/DP(25dBm),5555/20-Ce/ac/DP(25dBm),5560/20-Ce/ac/DP(25dBm),
            5565/20-Ce/ac/DP(25dBm),5570/20-Ce/ac/DP(25dBm),5575/20-Ce/ac/DP(25dBm),5580/20-Ce/ac/DP(25dBm),
            5585/20-Ce/ac/DP(25dBm),5590/20-Ce/ac/DP(25dBm),5595/20-Ce/ac/DP(25dBm),5600/20-Ce/ac/DP(25dBm),
            5605/20-Ce/ac/DP(25dBm),5610/20-Ce/ac/DP(25dBm),5615/20-Ce/ac/DP(25dBm),5620/20-Ce/ac/DP(25dBm),
            5625/20-Ce/ac/DP(25dBm),5630/20-Ce/ac/DP(25dBm),5635/20-Ce/ac/DP(25dBm),5640/20-Ce/ac/DP(25dBm),
            5645/20-Ce/ac/DP(25dBm),5650/20-Ce/ac/DP(25dBm),5655/20-Ce/ac/DP(25dBm),5660/20-Ce/ac/DP(25dBm),
            5665/20-Ce/ac/DP(25dBm),5670/20-Ce/ac/DP(25dBm),5675/20-Ce/ac/DP(25dBm),5680/20-Ce/ac/DP(25dBm)

[admin@MktwAPac] /interface wireless info> allowed-channels 
interface: wlan1
  channels: 2412/20/gn(18dBm),2417/20/gn(18dBm),2422/20/gn(18dBm),2427/20/gn(18dBm),2432/20/gn(18dBm),
            2437/20/gn(18dBm),2442/20/gn(18dBm),2447/20/gn(18dBm),2452/20/gn(18dBm),2457/20/gn(18dBm),
            2462/20/gn(18dBm),2467/20/gn(18dBm),2472/20/gn(18dBm)
```

Well the power settings on a MT are not simple with the later devices and higher RouterOS versions.What I assume as what it does ......- TX power, certainly in Europe, is limited by the regulatory domain max EIRP (20dBm for 2.4GHz, 23dBm and 20 dBm for 5GHz indoor only freq, 27 dBm for 5GHz also outdoor freq)See CLI: " interface wireless info country-info etsi" or replace etsi with your country- TX power is limited at the higher MCS encoding because of the needed signal quality (see data sheets)- TX power used to be given as information in "Current TX power", and power could be set per MCS. Now only "all rate fixed" can be used. Andno feedback is given.The only line of information visible in RouterOS GUI is in the "status". All possible values of this can be seen with: "/interface wireless info allowed-channels"It is the calculation of the EIRP limit, reduced with the antenna gain filled in or set by default. In text below wAP has "antenna gain=2" setAs far as I verified there is no reduction for the multiple antenna in the status info,  not even for 2.4GHz "n" where it is set "per antenna", versus "ac" where it is total (see wiki)The EIRP table values get sometimes updated with ROS releasesThe manual TX-power "all rates fixed" filled in value, does not change this status line. So there you can not see what the TX-power used actually is.The value in the status line will be the maximum used !But as the wiki says you should set the TX-power per antenna for all protocols except "ac" chipsets where you should give the total. "802.11n wireless chipsets represent power per chain and the 802.11ac wireless chipsets represent the total power". This does not fit with the above data, which is always the total power, or not? The multiple antenna must be compensated for, so with 2 it is 3dBm lower per antenna.And with no feedback, what are we doing when we set manual TX-power to 17 , on "n" chipsets and what on "ac" chipsets?The max is 'status_dBm - 3dBm' ??


---
```

## Response 25
Author: Fri Feb 11, 2022 7:26 am
Well the power settings on a MT are not simple with the later devices and higher RouterOS versions.What I assume as what it does ......- TX power, certainly in Europe, is limited by the regulatory domain max EIRP (20dBm for 2.4GHz, 23dBm and 20 dBm for 5GHz indoor only freq, 27 dBm for 5GHz also outdoor freq)See CLI: " interface wireless info country-info etsi" or replace etsi with your country- TX power is limited at the higher MCS encoding because of the needed signal quality (see data sheets)- TX power used to be given as information in "Current TX power", and power could be set per MCS. Now only "all rate fixed" can be used. And no feedback is given.The only line of information visible in RouterOS GUI is in the "status". All possible values of this can be seen with: "/interface wireless info allowed-channels"It is the calculation of the EIRP limit, reduced with the antenna gain filled in or set by default. In text below wAP has "antenna gain=2" setAs far as I verified there is no reduction for the multiple antenna in the status info, not even for 2.4GHz "n" where it is set "per antenna", versus "ac" where it is total (see wiki)The EIRP table values get sometimes updated with ROS releasesCode: Select all[admin@Omnitik] > interface wireless info country-info etsiranges: 2402-2482/b, g, gn20, gn40(20dBm)5170-5250/a, an20, an40, ac20, ac40, ac80, ac160, ac80+80(23dBm)/passive, indoor5170-5330/a, an20, an40, ac20, ac40, ac80, ac160, ac80+80(20dBm)/dfs, passive, indoor5250-5330/a, an20, an40, ac20, ac40, ac80, ac160, ac80+80(20dBm)/dfs, passive, indoor5490-5710/a, an20, an40, ac20, ac40, ac80, ac160, ac80+80(27dBm)/dfs, passive5190-5310/a-turbo(20dBm)/dfs5180-5300/a-turbo(20dBm)/dfs5520-5680/a-turbo(27dBm)/dfs, passive5510-5670/a-turbo(27dBm)/dfs, passive902-927/b, g, g-turbo, gn20, gn40(30dBm)[admin@MktwAPac] /interface wireless info> allowed-channelsinterface: wlan2channels: 5180/20-Ce/ac/P(21dBm),5185/20-Ce/ac/P(21dBm),5190/20-Ce/ac/P(21dBm),5195/20-Ce/ac/P(21dBm),5200/20-Ce/ac/P(21dBm),5205/20-Ce/ac/P(21dBm),5210/20-Ce/ac/P(21dBm),5215/20-Ce/ac/P(21dBm),5220/20-Ce/ac/P(21dBm),5180/20-Ce/ac/DP(18dBm),5185/20-Ce/ac/DP(18dBm),5190/20-Ce/ac/DP(18dBm),5195/20-Ce/ac/DP(18dBm),5200/20-Ce/ac/DP(18dBm),5205/20-Ce/ac/DP(18dBm),5210/20-Ce/ac/DP(18dBm),5215/20-Ce/ac/DP(18dBm),5220/20-Ce/ac/DP(18dBm),5225/20-Ce/ac/DP(18dBm),5230/20-Ce/ac/DP(18dBm),5235/20-Ce/ac/DP(18dBm),5240/20-Ce/ac/DP(18dBm),5245/20-Ce/ac/DP(18dBm),5250/20-Ce/ac/DP(18dBm),5255/20-Ce/ac/DP(18dBm),5260/20-Ce/ac/DP(18dBm),5265/20-Ce/ac/DP(18dBm),5270/20-Ce/ac/DP(18dBm),5275/20-Ce/ac/DP(18dBm),5280/20-Ce/ac/DP(18dBm),5285/20-Ce/ac/DP(18dBm),5290/20-Ce/ac/DP(18dBm),5295/20-Ce/ac/DP(18dBm),5300/20-Ce/ac/DP(18dBm),5260/20-Ce/ac/DP(18dBm),5265/20-Ce/ac/DP(18dBm),5270/20-Ce/ac/DP(18dBm),5275/20-Ce/ac/DP(18dBm),5280/20-Ce/ac/DP(18dBm),5285/20-Ce/ac/DP(18dBm),5290/20-Ce/ac/DP(18dBm),5295/20-Ce/ac/DP(18dBm),5300/20-Ce/ac/DP(18dBm),5500/20-Ce/ac/DP(25dBm),5505/20-Ce/ac/DP(25dBm),5510/20-Ce/ac/DP(25dBm),5515/20-Ce/ac/DP(25dBm),5520/20-Ce/ac/DP(25dBm),5525/20-Ce/ac/DP(25dBm),5530/20-Ce/ac/DP(25dBm),5535/20-Ce/ac/DP(25dBm),5540/20-Ce/ac/DP(25dBm),5545/20-Ce/ac/DP(25dBm),5550/20-Ce/ac/DP(25dBm),5555/20-Ce/ac/DP(25dBm),5560/20-Ce/ac/DP(25dBm),5565/20-Ce/ac/DP(25dBm),5570/20-Ce/ac/DP(25dBm),5575/20-Ce/ac/DP(25dBm),5580/20-Ce/ac/DP(25dBm),5585/20-Ce/ac/DP(25dBm),5590/20-Ce/ac/DP(25dBm),5595/20-Ce/ac/DP(25dBm),5600/20-Ce/ac/DP(25dBm),5605/20-Ce/ac/DP(25dBm),5610/20-Ce/ac/DP(25dBm),5615/20-Ce/ac/DP(25dBm),5620/20-Ce/ac/DP(25dBm),5625/20-Ce/ac/DP(25dBm),5630/20-Ce/ac/DP(25dBm),5635/20-Ce/ac/DP(25dBm),5640/20-Ce/ac/DP(25dBm),5645/20-Ce/ac/DP(25dBm),5650/20-Ce/ac/DP(25dBm),5655/20-Ce/ac/DP(25dBm),5660/20-Ce/ac/DP(25dBm),5665/20-Ce/ac/DP(25dBm),5670/20-Ce/ac/DP(25dBm),5675/20-Ce/ac/DP(25dBm),5680/20-Ce/ac/DP(25dBm)[admin@MktwAPac] /interface wireless info> allowed-channelsinterface: wlan1channels: 2412/20/gn(18dBm),2417/20/gn(18dBm),2422/20/gn(18dBm),2427/20/gn(18dBm),2432/20/gn(18dBm),2437/20/gn(18dBm),2442/20/gn(18dBm),2447/20/gn(18dBm),2452/20/gn(18dBm),2457/20/gn(18dBm),2462/20/gn(18dBm),2467/20/gn(18dBm),2472/20/gn(18dBm)The manual TX-power "all rates fixed" filled in value, does not change this status line. So there you can not see what the TX-power used actually is. The value in the status line will be the maximum used ! But as the wiki says you should set the TX-power per antenna for all protocols except "ac" chipsets where you should give the total. "802.11n wireless chipsets represent power per chain and the 802.11ac wireless chipsets represent the total power". This does not fit with the above data, which is always the total power, or not? The multiple antenna must be compensated for, so with 2 it is 3dBm lower per antenna. And with no feedback, what are we doing when we set manual TX-power to 17 , on "n" chipsets and what on "ac" chipsets? The max is 'status_dBm - 3dBm' ??Thank you for your detailed answer. Based on that I can conclude that I won't be able to increase the power. Then what are other ways to improve the situation that devices switch to 2.4GHz though 5GHz RSSI is quite acceptable?http://prntscr.com/26thu4f ---

## Response 26
Author: Fri Feb 11, 2022 8:35 am
``` 
```
[admin@Omnitik] > interface wireless info country-info etsi
  ranges: 2402-2482/b,g,gn20,gn40(20dBm)
          5170-5250/a,an20,an40,ac20,ac40,ac80,ac160,ac80+80(23dBm)/passive,indoor
          5170-5330/a,an20,an40,ac20,ac40,ac80,ac160,ac80+80(20dBm)/dfs,passive,indoor
          5250-5330/a,an20,an40,ac20,ac40,ac80,ac160,ac80+80(20dBm)/dfs,passive,indoor
          5490-5710/a,an20,an40,ac20,ac40,ac80,ac160,ac80+80(27dBm)/dfs,passive
          5190-5310/a-turbo(20dBm)/dfs
          5180-5300/a-turbo(20dBm)/dfs
          5520-5680/a-turbo(27dBm)/dfs,passive
          5510-5670/a-turbo(27dBm)/dfs,passive
          902-927/b,g,g-turbo,gn20,gn40(30dBm)


[admin@MktwAPac] /interface wireless info> allowed-channels 
interface: wlan2
  channels: 5180/20-Ce/ac/P(21dBm),5185/20-Ce/ac/P(21dBm),5190/20-Ce/ac/P(21dBm),5195/20-Ce/ac/P(21dBm),
            5200/20-Ce/ac/P(21dBm),5205/20-Ce/ac/P(21dBm),5210/20-Ce/ac/P(21dBm),5215/20-Ce/ac/P(21dBm),
            5220/20-Ce/ac/P(21dBm),5180/20-Ce/ac/DP(18dBm),5185/20-Ce/ac/DP(18dBm),5190/20-Ce/ac/DP(18dBm),
            5195/20-Ce/ac/DP(18dBm),5200/20-Ce/ac/DP(18dBm),5205/20-Ce/ac/DP(18dBm),5210/20-Ce/ac/DP(18dBm),
            5215/20-Ce/ac/DP(18dBm),5220/20-Ce/ac/DP(18dBm),5225/20-Ce/ac/DP(18dBm),5230/20-Ce/ac/DP(18dBm),
            5235/20-Ce/ac/DP(18dBm),5240/20-Ce/ac/DP(18dBm),5245/20-Ce/ac/DP(18dBm),5250/20-Ce/ac/DP(18dBm),
            5255/20-Ce/ac/DP(18dBm),5260/20-Ce/ac/DP(18dBm),5265/20-Ce/ac/DP(18dBm),5270/20-Ce/ac/DP(18dBm),
            5275/20-Ce/ac/DP(18dBm),5280/20-Ce/ac/DP(18dBm),5285/20-Ce/ac/DP(18dBm),5290/20-Ce/ac/DP(18dBm),
            5295/20-Ce/ac/DP(18dBm),5300/20-Ce/ac/DP(18dBm),5260/20-Ce/ac/DP(18dBm),5265/20-Ce/ac/DP(18dBm),
            5270/20-Ce/ac/DP(18dBm),5275/20-Ce/ac/DP(18dBm),5280/20-Ce/ac/DP(18dBm),5285/20-Ce/ac/DP(18dBm),
            5290/20-Ce/ac/DP(18dBm),5295/20-Ce/ac/DP(18dBm),5300/20-Ce/ac/DP(18dBm),5500/20-Ce/ac/DP(25dBm),
            5505/20-Ce/ac/DP(25dBm),5510/20-Ce/ac/DP(25dBm),5515/20-Ce/ac/DP(25dBm),5520/20-Ce/ac/DP(25dBm),
            5525/20-Ce/ac/DP(25dBm),5530/20-Ce/ac/DP(25dBm),5535/20-Ce/ac/DP(25dBm),5540/20-Ce/ac/DP(25dBm),
            5545/20-Ce/ac/DP(25dBm),5550/20-Ce/ac/DP(25dBm),5555/20-Ce/ac/DP(25dBm),5560/20-Ce/ac/DP(25dBm),
            5565/20-Ce/ac/DP(25dBm),5570/20-Ce/ac/DP(25dBm),5575/20-Ce/ac/DP(25dBm),5580/20-Ce/ac/DP(25dBm),
            5585/20-Ce/ac/DP(25dBm),5590/20-Ce/ac/DP(25dBm),5595/20-Ce/ac/DP(25dBm),5600/20-Ce/ac/DP(25dBm),
            5605/20-Ce/ac/DP(25dBm),5610/20-Ce/ac/DP(25dBm),5615/20-Ce/ac/DP(25dBm),5620/20-Ce/ac/DP(25dBm),
            5625/20-Ce/ac/DP(25dBm),5630/20-Ce/ac/DP(25dBm),5635/20-Ce/ac/DP(25dBm),5640/20-Ce/ac/DP(25dBm),
            5645/20-Ce/ac/DP(25dBm),5650/20-Ce/ac/DP(25dBm),5655/20-Ce/ac/DP(25dBm),5660/20-Ce/ac/DP(25dBm),
            5665/20-Ce/ac/DP(25dBm),5670/20-Ce/ac/DP(25dBm),5675/20-Ce/ac/DP(25dBm),5680/20-Ce/ac/DP(25dBm)

[admin@MktwAPac] /interface wireless info> allowed-channels 
interface: wlan1
  channels: 2412/20/gn(18dBm),2417/20/gn(18dBm),2422/20/gn(18dBm),2427/20/gn(18dBm),2432/20/gn(18dBm),
            2437/20/gn(18dBm),2442/20/gn(18dBm),2447/20/gn(18dBm),2452/20/gn(18dBm),2457/20/gn(18dBm),
            2462/20/gn(18dBm),2467/20/gn(18dBm),2472/20/gn(18dBm)
```

Well the power settings on a MT are not simple with the later devices and higher RouterOS versions.What I assume as what it does ......- TX power, certainly in Europe, is limited by the regulatory domain max EIRP (20dBm for 2.4GHz, 23dBm and 20 dBm for 5GHz indoor only freq, 27 dBm for 5GHz also outdoor freq)See CLI: " interface wireless info country-info etsi" or replace etsi with your country- TX power is limited at the higher MCS encoding because of the needed signal quality (see data sheets)- TX power used to be given as information in "Current TX power", and power could be set per MCS. Now only "all rate fixed" can be used. Andno feedback is given.The only line of information visible in RouterOS GUI is in the "status". All possible values of this can be seen with: "/interface wireless info allowed-channels"It is the calculation of the EIRP limit, reduced with the antenna gain filled in or set by default. In text below wAP has "antenna gain=2" setAs far as I verified there is no reduction for the multiple antenna in the status info,  not even for 2.4GHz "n" where it is set "per antenna", versus "ac" where it is total (see wiki)The EIRP table values get sometimes updated with ROS releasesThe manual TX-power "all rates fixed" filled in value, does not change this status line. So there you can not see what the TX-power used actually is.The value in the status line will be the maximum used !But as the wiki says you should set the TX-power per antenna for all protocols except "ac" chipsets where you should give the total. "802.11n wireless chipsets represent power per chain and the 802.11ac wireless chipsets represent the total power". This does not fit with the above data, which is always the total power, or not? The multiple antenna must be compensated for, so with 2 it is 3dBm lower per antenna.And with no feedback, what are we doing when we set manual TX-power to 17 , on "n" chipsets and what on "ac" chipsets?The max is 'status_dBm - 3dBm' ??Thank you for your detailed answer. Based on that I can conclude that I won't be able to increase the power. Then what are other ways to improve the situation that devices switch to 2.4GHz though 5GHz RSSI is quite acceptable?http://prntscr.com/26thu4f


---
```

## Response 27
Author: Sun Sep 10, 2023 10:25 am
It seems like this is somehow implemented, although the details are obscure, https://help.mikrotik.com/docs/display/ ... ropertiesthe effect seems dubious to me as i am still having issues with 2.4G being the selected band most of the time. ---

## Response 28
Author: Sun Sep 10, 2023 1:01 pm
My main problem with MIKROTIK WIRELESS is the "giving up in crowded environments".When Mikrotik (WLAN driver) is in competition with other brands ( or with MT on wifiwave2), then MT has a handicap of 3dB. That is if the EIRP level is the power limiting factor (EIRP is very low in Europe and is the limiting factor).MT WLAN driver (has to? why?) follow the non-TPC permitted EIRP levels, which are 3 dB lower than the TPC permitted EIRP levels.Other brand AP will be the preferred AP, because of the stronger signal. ---

## Response 29
Author: Sun Sep 10, 2023 4:44 pm
ROS 7.12 beta*) wifiwave2 - list APs with a higher maximum data rate as more preferable roaming candidates; ---

## Response 30
Author: Sun Sep 10, 2023 7:52 pm
But how ? Used in 802.11k ?Or will MT finally add QBSS fields in the beacons?"The QBSS (QOS enhanced basic service set) information element is an 802.11e construct that enables an access point to communicate its channel usage"Missing QBSS with MT. Yet another potential reason why the MT AP is/was not the preferred AP for wireless devices. ---

## Response 31
Author: Mon Sep 11, 2023 7:30 pm
AsI understand it, the 'preference' mostly works by delaying response frames for the 2.4GHz channel, so that the client receives the 5G channel frames first.I simple workaround that has worked well for me has been to set a longer beacon interval for 2G than 5G.Additionally an access policy blocking 5G for low RSSI would help insure 2G is selected for low signal strength. ---

## Response 32
Author: Mon Sep 11, 2023 9:24 pm
Band steering MT, yuck yuck........... Is this the comedy forum ???Just dont hand out passwords to 2.4 no connection. ---

## Response 33
Author: Wed Sep 13, 2023 12:50 am
Re:RSSI of 2.4Ghz: about -50RSSI of 5Ghz: about -70Move your wireless client device much closer to your dual-band AP. Then see what you default connect to.A -50 connection on 2.4 GHz might be a faster connection than a -70 connection on 5 GHz.Normally , connection rates will shift up to faster rates. Each time they shift to a faster rate , the TX power will normally decrease and the RX receive signal strength will also decrease ( for both the client and the AP ). These connection rates will try to achieve the fastest rate possible based on the client and AP signal quality. However , if/when a link has problems ( including problems at faster connection rates after it has already connected ), it may disconnect and auto-reconnect to a different AP. ---

## Response 34
Author: [SOLVED]Fri May 24, 2024 4:16 pm
MikroTik gave us vendor drivers (wifi-qcom-ac) starting with ROS 7.13. No issues with roaming anymore. Clients choose 5ghz when relatively near AP, smoothly roam over to 2ghz when moving away from AP, smoothly roam back to 5ghz when moving near AP again. Works like a charm.♥ Thank you Mikrotik for making it happen. ♥ ---

## Response 35
Author: Thu May 30, 2024 4:40 pm
MikroTik gave us vendor drivers (wifi-qcom-ac) starting with ROS 7.13. No issues with roaming anymore. Clients choose 5ghz when relatively near AP, smoothly roam over to 2ghz when moving away from AP, smoothly roam back to 5ghz when moving near AP again. Works like a charm.♥ Thank you Mikrotik for making it happen. ♥Yes.. but... if only is on Same SSID. I tried to roam to another SSID using fixed steering group, but with no success.I need to have 2 separates SSIDs ---

## Response 36
Author: Thu May 30, 2024 4:45 pm
Yes.. but... if only is on Same SSID. I tried to roam to another SSID using fixed steering group, but with no success.I need to have 2 separates SSIDsCan't do that.1 steering group per SSID. ---

## Response 37
Author: Thu May 30, 2024 5:29 pm
I tried to roam to another SSIDWifi roaming is only possible within the same SSID. ---

## Response 38
Author: Wed Jul 03, 2024 11:52 pm
Steering in MK is junk, I have 15 access points in AX mode and FT enabled. Steering makes devices to roam every second, most of them were losing internet access and falling back to cellular, some were stuck at 5 Ghz without roaming back to 2.4 and eventually losing connection due to low signal."Sa Query timeout" where flooding the log.It's a chaos. I had to disable it. ---

## Response 39
Author: Sat Jul 27, 2024 9:27 pm
In my case - Steering option fixed my problem, that devices would prefer sometimes 2.4ghz instead of 5ghz.I have observed that Mikrotik is pushing "too much" for 5ghz and devices sometimes simply just disconnect instead of connecting to 2.4ghz. However this might due to super crowded 2.4ghz band around me.In short - if 5ghz drops for some reason shortly or device preferred 2.4 instead of 5ghz, now it's working as supposed to and clients prefer 5ghz as soon as it's there.Mikrotik is overly complicated for non professionals. I think ubiquity, for instance is more plug and play and that's why if we are not professional enough assume that other manufacturers are better. They are not. IMHO. ---

## Response 40
Author: Sun Jul 28, 2024 12:25 am
Steering sucks on most cheap APs... I have networks with cAP ac, then I have networks with UniFi U6-Pro and then with Huawei AP361 (no money for anything better)...With the cheap devices it causes problems on MikroTik and UBNT... I had to turn it off everywhere, otherwise VoIP calls and such were dropping out. Unfortunately AP placement is not ideal, hence I have to help it by reducing Tx power and using nonDFS channels. It works pretty well on the Huawei, however I'm still worried about it. ---

## Response 41
Author: Thu Aug 22, 2024 3:48 pm
Steering in MK is junk, I have 15 access points in AX mode and FT enabled. Steering makes devices to roam every second, most of them were losing internet access and falling back to cellular, some were stuck at 5 Ghz without roaming back to 2.4 and eventually losing connection due to low signal."Sa Query timeout" where flooding the log.It's a chaos. I had to disable it.This is also my experience, devices kept hopping back and forth sometimes twice in a second. This is particularly noticeable in areas with low signal quality. I dropped steering for now but kept FT so devices can roam but are no longer kicked around. ---

## Response 42
Author: Sat Aug 24, 2024 5:09 pm
"Sa Query timeout" where flooding the log.Try setting connect-priority=0/1 to improve this.With default settings the new AP will only accept a roaming client after the old AP has confirmed it has disconnected. Making sure accept priority is always lower than hold priority can largely improve roaming speed at the cost of being more vulnerable to mac spoofing attacks. ---

## Response 43
Author: Sat Aug 24, 2024 5:30 pm
The ultimately get rid of SA query timeouts is to disable management-protection.security.managment-protection=disabledThis disables 802.11w. Bye Bye SA query timeout! You are limited to WPA2 though, because WPA3 requires it.More like a workaround. Other vendors allow to change the SA query timeout value and/or the retry attempts count. Mikrotik probably chose a very low timeout value not all clients can respond on time. ---

## Response 44
Author: Fri Dec 13, 2024 9:58 pm
MikroTik gave us vendor drivers (wifi-qcom-ac) starting with ROS 7.13. No issues with roaming anymore. Clients choose 5ghz when relatively near AP, smoothly roam over to 2ghz when moving away from AP, smoothly roam back to 5ghz when moving near AP again. Works like a charm.♥ Thank you Mikrotik for making it happen. ♥Mikrotik 7.17 - band steering does not work even neighborhood group is selected ---

## Response 45
Author: Sat Dec 14, 2024 12:10 am
``` 
```
/export file=anynameyoulike
```

Mikrotik 7.17 - band steering does not work even neighborhood group is selectedYou could show your config just to make sure that all settings are correct.Remove serial and any other private info.


---
```

## Response 46
Author: Sat Dec 14, 2024 12:08 pm
``` 
```
/interface wifi channel
add disabled=no frequency=2412,2437,2462 name=2.4Ghz reselect-interval=3h..4h \
    width=20mhz
add disabled=no name=5Ghz reselect-interval=4h..5h skip-dfs-channels=\
    10min-cac
/interface wifi configuration
add country=Sweden datapath.vlan-id=10 disabled=no mode=ap name=production \
    ssid=main
add country=Sweden datapath.vlan-id=20 disabled=no name=guest \
    security.authentication-types=wpa2-psk,wpa3-psk ssid=guest
/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk disabled=no name=production wps=\
    disable
add authentication-types=wpa2-psk,wpa3-psk disable-pmkid=yes disabled=no \
    name=guest wps=disable
/interface wifi
set [ find default-name=wifi2 ] channel=2.4Ghz channel.frequency=\
    2412,2437,2462 configuration=production configuration.mode=ap disabled=no \
    mac-address=78:9A:18:36:27:DC name=2Ghz security=production \
    steering.neighbor-group=dynamic-main-64b37b74
set [ find default-name=wifi1 ] channel=5Ghz channel.frequency=5170-5730 \
    configuration=production configuration.mode=ap disabled=no mtu=1500 name=\
    5Ghz security=production steering.neighbor-group=dynamic-main-64b37b74
add configuration=guest configuration.mode=ap disabled=no mac-address=\
    7A:9A:18:36:27:DE master-interface=5Ghz name="5Ghz Guest" security=guest \
    steering.neighbor-group=dynamic-guest-b9af47c9
add configuration=guest configuration.mode=ap disabled=no mac-address=\
    7A:9A:18:36:27:DB master-interface=2Ghz name="2.4Ghz Guest" security=\
    guest security.authentication-types=wpa2-psk,wpa3-psk \
    steering.neighbor-group=dynamic-guest-b9af47c9
add configuration.mode=ap .ssid=iot datapath.vlan-id=40 disabled=no \
    mac-address=7A:9A:18:36:27:DD master-interface=2Ghz name="2.4Ghz IoT" \
    security.authentication-types=wpa-psk,wpa2-psk .disable-pmkid=yes
```

You did not mean those whole config, right?At the moment i am doing a workaround with access list by blocking strong signal from 2.4Ghz


---
```

## Response 47
Author: Sat Dec 14, 2024 12:28 pm
It's not a good idea to actively block clients using access list.Some clients might avoid such an AP completely.Unless that's your aim, then I wonder why you keep using the same SSID for that frequency ? ---

## Response 48
Author: Sat Dec 14, 2024 12:55 pm
It's not a good idea to actively block clients using access list.Some clients might avoid such an AP completely.Unless that's your aim, then I wonder why you keep using the same SSID for that frequency ?I know it's not a good solution. Workaround works in a way, that only clients with strong signal are blocked from 2.4GhzIf steering have worked - workaround is not needed ---

## Response 49
Author: Sat Dec 14, 2024 10:55 pm
It's not a good idea to actively block clients using access list.Some clients might avoid such an AP completely.Unless that's your aim, then I wonder why you keep using the same SSID for that frequency ?Some clients might avoid that BSSID not the AP as such, AFAIK.I make all MAC addresses unique (BSSID). Maybe that's not the best setup. ? Other setups known for this?(If you change MAC/BSSID in your AP setup, sometimes clients must "Forget" those known networks, for association to succeed again)I used access list 'deny' to keep too (!) strong 2.4GHz clients away from using that interface.(travel routers these days are a plague with their 20dBm, laying besides the hAP ac2)Not sufficient, even if they switch to another AP then with different channel (@MKX explained, receiver saturation still happens if they use another channel in the same band)Too strong signal around ... all sorts of problems and disconnects.Just a sidenote: (With Fortigate/ForiAP all BSSID for the SSID are the same, the Fortigate decides which (Forti)AP will respond to client. It's their VAP (Virtual AP) concept)Flapping 2.4 and 5 GHz, frustrating indeed: like too many 2 sec sessions in Radius accounting. I also added extra SSID so one can use specific or common SSID.It's not fully solved that way. We want and fast wifi and long range, without user intervention. ---

## Response 50
Author: Sun Dec 15, 2024 1:14 am
It's not a good idea to actively block clients using access list.Some clients might avoid such an AP completely.Unless that's your aim, then I wonder why you keep using the same SSID for that frequency ?Just a sidenote: (With Fortigate/ForiAP all BSSID for the SSID are the same, the Fortigate decides which (Forti)AP will respond to client. It's their VAP (Virtual AP) concept)inheritance from Meru Networks which was bought by fortihttps://www.fortinet.com/lat/corporate/ ... u-networksMeru has a unique way of working, was very "controversial" at that moment for their Single Channel Architecture (SCA)very unique in other matters alsohttps://www.cwnp.com/making-sense-of-meru-decodes/ ---

## Response 51
Author: Sun Dec 15, 2024 10:23 pm
Seems that connect-priority 0/1 improved the situation. Devices now do switch to 5ghz when close to router and vice versa when far away. ---

## Response 52
Author: Mon Dec 16, 2024 8:39 am
``` 
```
07:17:30 wireless,info <station-MAC>@<old_WiFi_radio> roamed to <station-MAC>@<new_WiFi_radio>, signal strength -75
 07:17:30 wireless,debug <station-MAC>@<old_WiFi_radio> disassociated, connected to other interface, signal strength -88
```

```
```

```
15:53:58 wireless,info <station-MAC>@<old_WiFi_radio>: disconnected, extensive data loss, signal strength -75
```

Seems that connect-priority 0/1 improved the situation. Devices now do switch to 5ghz, but it does not seem due to actual steering, but because they eventually take that decision themselves.WiFi standards (802.11anything) don't standardize handovers (at decision of network entity), they standardize steering ... which helps device to decide if and when to switch to different BSSID inside same SSID. The difference between no steering and steering more or less boils down to duration of connectivity outage during switch over (with steering it's pretty short, without steering it can take seconds). But decision is always device's.The difference is also seen in logs. With steering logs will say something likeso "roamed to ... disassociated".And without steering, logs will say something likeso "disconnected".


---
```

## Response 53
Author: Mon Dec 16, 2024 3:38 pm
How do You enable this level of logging? ---

## Response 54
Author: Mon Dec 16, 2024 10:15 pm
``` 
```
/system logging set topics=debug,info,wireless action=memory
```

the debug output can be enabled within the logging section under system or as example for wireless:That's it. BTW: here you could set up as well sending emails per log event (such as user login for example)


---
```

## Response 55
Author: Wed Dec 18, 2024 12:08 am
``` 
```
/system logging set topics=debug,info,wireless action=memory
```

the debug output can be enabled within the logging section under system or as example for wireless:That's it. BTW: here you could set up as well sending emails per log event (such as user login for example)Appreceate, thank you.
```