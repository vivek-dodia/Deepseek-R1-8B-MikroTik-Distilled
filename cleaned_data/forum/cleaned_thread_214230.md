# Thread Information
Title: Thread-214230
Section: RouterOS
Thread ID: 214230

# Discussion

## Initial Question
Hey guy, I used to mess with openwrt but mikrotik always been a mysterious routeros to me i finally decided to use it and im excited. My only last challenge is im confuse what model should be good for a beginner like me?Thanks ---

## Response 1
For what purpose? ---

## Response 2
What @normis is saying (but in more words): in principle every device, running ROS, offers same functionality (apart from models with 16MB flash which is tight and doesn't allow to install all the optional ROS packages). But devices differ wildly when it comes to capacity when running those functions. So if your main goal is learning how to ROS, then you can go with some low-end device (with consideration about storage/flash space). If you have in your mind some particular task for the device, then we might be able to give you an advice (or two), but you have to describe that task (in detail). ---

## Response 3
For what purpose?Mmm suppose im gonna using it for small business. Been looking through options there are alot of cool fancy stuff but i cant afford it. I believe my budget is like 200-260$ ---

## Response 4
What @normis is saying (but in more words): in principle every device, running ROS, offers same functionality (apart from models with 16MB flash which is tight and doesn't allow to install all the optional ROS packages). But devices differ wildly when it comes to capacity when running those functions. So if your main goal is learning how to ROS, then you can go with some low-end device (with consideration about storage/flash space). If you have in your mind some particular task for the device, then we might be able to give you an advice (or two), but you have to describe that task (in detail).Yes theres actually a task in my mind. Because im planning to run small business offering wifi to neighbors through litebeam or powerbeam. Everything is planned and prepared exept the device that can manage and allow me to have control over users.Any advice and tips highly appreciated and will be noted.Ty ---

## Response 5
https://mikrotik.com/product/rb5009ug_s_in ---

## Response 6
https://mikrotik.com/product/rb5009ug_s_inWow, based on its features its amazingly insane!All mik routerboards run same RouterOS no? ---

## Response 7
Yes, the same OS is on all devices. There are some small differrences in License level, but this one already has a good license level with not many limits.https://help.mikrotik.com/docs/spaces/R ... ekeylevels ---

## Response 8
Same ROS but depending on the model they have different levels of licence that limits some functions eg. max number of connections:https://wiki.mikrotik.com/Manual:LicenseOf course the efficiency for small & cheap device is different than the big & insanepriced oneAlthough the "insane priced" is quite cheap if you get fully flagged fast and supported for a long long time device in comparision to other vendors. ---

## Response 9
Yes, the same OS is on all devices. There are some small differrences in License level, but this one already has a good license level with not many limits.https://help.mikrotik.com/docs/spaces/R ... ekeylevelsWith the mentioned router i will be able to build a good workplace?These are the tasks, 2 isp bonding (optional and not interested currently)A full control over users(blocking, limiting, enabling, QOS) ---

## Response 10
Same ROS but depending on the model they have different levels of licence that limits some functions eg. max number of connections:https://wiki.mikrotik.com/Manual:LicenseOf course the efficiency for small & cheap device is different than the big & insanepriced oneAlthough the "insane priced" is quite cheap if you get fully flagged fast and supported for a long long time device in comparision to other vendors.So cool, do you have other suggestions with the mentioned price tag? ---

## Response 11
Do not buy switch for use it as router. ---

## Response 12
The "key" is IMHO your ISP connection speed more than anything else.If it is below 1 Gb speed, you can get a hex refresh (or even a hap ax lite) as a first device on the cheap (with 5 or 4 ports) around 60$.If it is 1 Gb the "right" device is the hap Ax3 (5 ports) 140$.If it is more than 1 Gb - as BartoszP advised - go for the RB5009 (8 ports+the SFP socket) 220$.Of course the latter is the more future-proof choice at the moment, and surely it is the "entry level" for a business offering like the one you plan, then the amount of customers/clients may make you shift towards a more powerful device, such as one of the CCR series, but the good thing about these Mikrotik devices is that - within limits - they can be re-used in other roles, as managed or "dumb" switch, just as an example, so you can start with *any* device and when you get a new, more powerful one, the old one can be re-used in other projects/setups. ---

## Response 13
Do not buy switch for use it as router.Ooooo, no one mentioned this actually!Im in need for router! ---

## Response 14
The "key" is IMHO your ISP connection speed more than anything else.If it is below 1 Gb speed, you can get a hex refresh (or even a hap ax lite) as a first device on the cheap (with 5 or 4 ports) around 60$.If it is 1 Gb the "right" device is the hap Ax3 (5 ports) 140$.If it is more than 1 Gb - as BartoszP advised - go for the RB5009 (8 ports+the SFP socket) 220$.Of course the latter is the more future-proof choice at the moment, and surely it is the "entry level" for a business offering like the one you plan, then the amount of customers/clients may make you shift towards a more powerful device, such as one of the CCR series, but the good thing about these Mikrotik devices is that - within limits - they can be re-used in other roles, as managed or "dumb" switch, just as an example, so you can start with *any* device and when you get a new, more powerful one, the old one can be re-used in other projects/setups.My brain farted im sorry, can we speak in terms of noob level? *_*First as i mentioned i need a router with decent cores, ghz speed and ran. I believe RB5009UG fulfill the requirements of bein mid range routerAnd yes clients aint gonna be many. I believe maximum is 30 clients, the RB5009UG gonna do its job in this situation? ---

## Response 15
Do not buy switch for use it as router.Ooooo, no one mentioned this actually!Im in need for router!All (not really all, but let's ignore this) MikroTik devices, RouterBOARD, have RouterOS inside, even the switches.All RouterOS features are available in all devices (except things that require specific hardware),so even a superfast switch, perfect as a switch, could act as a router, but with trivial performance.So avoid any CRSxxx or CSSxxx ---

## Response 16
I believe maximum is 30 clients, the RB5009UG gonna do its job in this situation?Yes but, 30 clients, at what speed each? ---

## Response 17
IMO @rextended gives good advice; I recently bought RB5009 for router on a stick deployment.CRS305-1G-4S+IN $149.00CRS326-24G-2S+IN $199.00RB5009UG+S+IN $219.00CRS309-1G-8S+IN $269.00CRS3xx devices supportL3 Hardware Offloadingwhich can route and firewall at wire speed for some cases; thelearning curve is steep. See forum topichow does L3HW actually works?If you have tight budgetANDfirewall rules are simpleANDclient count is small then CRS3xx may work for youbut don't go this route without verifying your requirements fit within L3HW limits. ---

## Response 18
My brain farted im sorry, can we speak in terms of noob level? *_*You want a plumber comparison?Imagine that in your house there are 9 bathrooms, a kitchen, an outdoor tap in the garden and one in the garage.That makes roughly 30 taps, each 1/2".If you want to have all of them open at the same time you need to deliver to your home enough water.Roughly, a 1" pipe will provide enough water for 4 such taps. So you need 6 or 7 of these 1" pipes. But a 2" pipe Is enough, still roughly, for 4 x 1" pipes, and a 2 1/2" Is enough for 6 of them.In reality you can have reasonably at the most 10 to 20 of the 30 taps open at the same time and in a same bathroom you are not going to have more than two taps open fully a the same time so you can have distribution lines 3/4" and a 2" pipe from the main line in the road to your house is enough.Along this water line you will have fitted at least a gate valve, a water meter and a second (gate or ball) valve.Of course these will be as well 2" diameter, to avoid bottlenecks. If you fit smaller ones the amount of water available will be reduced.Same goes for the main distribution lines, if you use 3/4" pipes, section valves will also need to be 3/4".Internet and networks are not that much different in principle, the router needs to be able to let pass through all the speed and bandwidth the ISP can deliver, then the switch(es) and the network connections behind the router need to be able to distribute It.But It makes little sense to have a router capable of (say) 5 Gb if the ISP cannot provide more than 1 Gb, or viceversa have a 1 Gb network if the ISP and router can deliver 5 Gb.All elements in the chain need to be dimensioned in such a way to not create bottlenecks.The easy way Is to get the most powerful devices available, if budget Is not an issue.Since usually there are limits to what you can spend, you need to carefully estimate the needs/requirements first and then choose the hardware that can deliver what is planned at the lower possible cost, allowing some reasonably slack.Forum members may be able to give you advice on the hardware that is more suitable to fulfill the requirements and possibly also help you in calculating these requirements, the more details you can provide, the more accurate/appropriate the advice can be. ---

## Response 19
I believe maximum is 30 clients, the RB5009UG gonna do its job in this situation?Yes but, 30 clients, at what speed each?I believe maximum speed will be 250mbps, RB5009 will be capable of that? ---

## Response 20
My brain farted im sorry, can we speak in terms of noob level? *_*Forum members may be able to give you advice on the hardware that is more suitable to fulfill the requirements and possibly also help you in calculating these requirements, the more details you can provide, the more accurate/appropriate the advice can be.Im so happy that everyone is helping actually, for now i noted every possible advice here ---

## Response 21
Also, dont think just about today. Plan ahead, what will likely occur in the next five years.An investment in a router should cover at least that time span. In other words, is your ISP throughput likely to be the same or increase? ---

## Response 22
Also, dont think just about today. Plan ahead, what will likely occur in the next five years.An investment in a router should cover at least that time span. In other words, is your ISP throughput likely to be the same or increase?After 5 years i believe in my country we may reach 1.5gig speed. But as for a start till i build and start the first step do you think the RB5009U will do its purpose? ---

## Response 23
Yes but, 30 clients, at what speed each?I believe maximum speed will be 250mbps, RB5009 will be capable of that?Math? 30 * 250 = 7500Mbps...Yu have a link at 10Gbps?Official Ethernet test results:Routing 25 simple queues 512 byte4612MbpsSince I do not think all clients download 250Mbps continuosly, can suffice.https://cdn.mikrotik.com/web-assets/pro ... 220852.png ---

## Response 24
Once, 10+ years ago, I had a chance to collect data for multibranch company that used centralized system in 24/7 mode and all employees were connected all working day to central system + circa 70 people in main office used same line for everyday mail, browsing, music etc.The average throughput was at 4Mb for a whole year. Day+night+holidays .... insane when you compare it to peak traffic when you can "eat as much as you want". ---

## Response 25
I believe maximum speed will be 250mbps, RB5009 will be capable of that?Math? 30 * 250 = 7500Mbps...Yu have a link at 10Gbps?Official Ethernet test results:Routing 25 simple queues 512 byte4612MbpsSince I do not think all clients download 250Mbps continuosly, can suffice.https://cdn.mikrotik.com/web-assets/pro ... 220852.pngWell thats a con. I guess i will reconsider my decision abt rb5009*_* soooo now im convinced to invest in better router thoughts on rb1100x4? ---

## Response 26
Also, dont think just about today. Plan ahead, what will likely occur in the next five years.An investment in a router should cover at least that time span. In other words, is your ISP throughput likely to be the same or increase?Hi, thoughts on rb1100x4? Im reconsidering my decision about rb5009 ---

## Response 27
Once, 10+ years ago, I had a chance to collect data for multibranch company that used centralized system in 24/7 mode and all employees were connected all working day to central system + circa 70 people in main office used same line for everyday mail, browsing, music etc.The average throughput was at 4Mb for a whole year. Day+night+holidays .... insane when you compare it to peak traffic when you can "eat as much as you want".This is really insane, im really convinced now to invest in better mikrotik routerboard, whats your opinion on rb1100x4? ---

## Response 28
RB1100AHx4 do not have SFP and all ports are only gigabit. ---

## Response 29
Since you say possibly 1.5gbps will come for your ISP in 5 years what's the problem ?Rb5009 will be more then enough. ---

## Response 30
Find clients, make money, buy newer "toys". That is the roadmap. ---

## Response 31
very old product: rb1100 - arm32 cpu 1.4Mhz ram1gig storage 128Mb, 13x 1gig ports, ---throughput -->2.3Gbpsrelatively new product: rb5009 - arm64 3.5-1.4Mhz ram1gig storage 1gig, 7x 1gig ports 1x 2.5gig port 1x sfp+1 port --- throughput --> 3.1Gbps++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Yup, your plan of spending $100 more to get a less capable older product makes much sense...........You would be better by spending $100 more than the RB1100 and get the CCR2004CCR2004 - arm64 cpu 1.7Mhz ramg4ig storage 128Mb, 16x 1gig ports, 2x spf+ ports -- throughput -- 4.6Gbps ( 2x power supplies ) ---