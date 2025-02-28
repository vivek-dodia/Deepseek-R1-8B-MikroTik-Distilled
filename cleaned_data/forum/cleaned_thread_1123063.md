# Thread Information
Title: Thread-1123063
Section: RouterOS
Thread ID: 1123063

# Discussion

## Initial Question
Just a nice to have...With WiFi 6 / ax having barely been introduced into Mikrotik harware lineup as of this general message. I read Wi-Fi 7 is not far off.Further reading I see Mikrotik's favorite supplier Qualcomm is now producing chips with Wi-Fi 7 onboard. ( IPQ9574 / PQ9554 / etc etc)Would it not be great to see MT get on the front foot and start implementing some of these chips into upcoming products( even if RoS is not ready just yet ). And I would think ideally into MT's ceiling mounted gear 1st up(CaP AC/ Cap XL etc)..wifi 7.pngCPU – Quad-core Arm Cortex-A73 @ 2.2 GHzSystem Memory – DDR3L, DDR4 16/32-bitStorage – eMMC, NAND, Serial NOR, SD/eMMCNetworkingWired – 6 Port Integrated Ethernet Switch 4 x 2.5 GbE + 5 GbE + 10 GbEWirelessWi-Fi StandardsWi-Fi 7 (802.11be), Wi-Fi 6E, Wi-Fi 6 (802.11ax),Wi-Fi 5 (802.11ac), Wi-Fi 4 (802.11n), 802.11a/b/gWi-Fi Spectral Bands – 6GHz, 5GHz, 2.4GHzSpatial Streams – 16 streamsChannel Support – 320MHz, 249MHz, 160MHz, 80MHz, 40MHz, 20MHzPeak Speed – 33 Gbps PHY rate, up to 10+ Gbps PHY rate per channelWi-Fi FeaturesSimultaneous & Alternating Multi Link Puncturing for wideband operation in presence of 5G/DFS & 6G/AFC interferers4K QAMUL/DL OFDMA up to 37 users per channelUL/DL MU-MIMO, up to 8 users per channelSustained throughput for up to 2000 usersTxBF, 802.11be QoSWi-Fi Security SuiteWPA3 Personal, WPA3 Enterprise, WPA3 Enhanced Open, WPA3 Easy Connect, WPA2, WPS, 802.11i securityAES-CCMP, AES-GCMP, PRNG, TKIP, WAPI2, WAPI1, WEPPlatform Extensions – Bluetooth, 802.15.4 (Zigbee/Thread), 4G/5G FWAPacket Processing – WAN tunnel offload engine, integrated Ethernet switch, enhanced security processor, high-performance QoS/TMPeripheralsAudio – I2SUSB – USB 3.0I2C, SDIO, SPI, UART4x PCIe 3.0 controllers2x USXGMII (Universal Serial 10GE Media Independent Interface), 1x USXGMII-MProcess Technology – 14nmhttps://www.qualcomm.com/products/appli ... oduct-list"Qualcomm says the new WiFi 7 Networking Pro SoCs can run Openwrt with Linux Kernel 5.4. With up to 2000 clients, the Networking Pro 1620 is designed for highly-congested venues (e.g. stadiums), enterprise, small-to-medium business, and prosumer home environments. The Networking Pro 1220 and 820 both target enterprise, SMB, prosumer, and premium home mesh systems, while the Networking Pro 620 is better suited for enterprise, SMB, gaming, and home mesh systems." ---

## Response 1
For me in that tabel the 6GHz is the most interesting improvement, as there is more interfering 5GHz around us already. Wifi 6E , but probably need Wifi 7 to implement 6GHz properly.The other things are more incremental gains, that will need undisturbed signal for those high MCS encoding, IMHO. ---

## Response 2
I seriously doubt that Mikrotik will come out with a "WiFi 7" product in less than 2 or 3 years from now.It also looks like Mikrotik totally missed the "Wi-Fi 6e" market.Some (non-Mikrotik)WiFi 7 , Wi-Fi 7 products are shipping right now.IMO , Mikrotik has great reliable wireless products for Wi-Fi 5 products but hardly anything for Wi-Fi 6. I've been waiting for years for Mikrotik to make a product that operates in the 6 GHz to low 7-GHz bands. ---

## Response 3
Well to be fair TPLINK just live streamed its wifi7 product release this past week or so, and none of the business class APs are showing up on their websites yet. ---

## Response 4
Well to be fair TPLINK just live streamed its wifi7 product release this past week or so, and none of the business class APs are showing up on their websites yet.Dont forget TP-LINK mention 2024 as the year expected for wi-fi 7 ---

## Response 5
Will we ever get a decent MU-MIMO and OFDMA?New standards are just broader channels and more chains to show more numbers on the paper. 4-8-16 chains give a lot of throughput but have anyone seen a wireless client with more than 2*2 MIMO?I hardly believe that one can't find a free 5GHz channel indoors. Is it so important to have 6-7GHz?MU-MIMO is not working so what is the different?Just a broader channel and higher potential MCS (u hardly get) ---

## Response 6
Of all the new bells and whistles coming with WiF7, I'm most optimistic about MU-MIMO because it mostly relies on AP's capabilities and it isn't impossible to build AP with large array of antennae (which will make AP huge or ugly or both). But that doesn't increase speed for clients when there's only very few active at a time (i.e. in typical SOHO case). So the benefit of it will only be there for large commercial installations.The rest of features are, as already written, harder to achieve and it's quite likely that we'll see even larger discrepancy between theoretical capacity and reality. ---

## Response 7
Noting the expected 2024 timeframe for most manufacturers to have product(s) ready.It would be now where the R&D teams should be getting there sample/test boards ready for a ~1year turn-around to market.Of all the new bells and whistles coming with WiF7, I'm most optimistic about MU-MIMO because it mostly relies on AP's capabilities and it isn't impossible to build AP with large array of antennae (which will make AP huge or ugly or both). But that doesn't increase speed for clients when there's only very few active at a time (i.e. in typical SOHO case). So the benefit of it will only be there for large commercial installations.As I stated earlier, probably a good initial product would be the Cap XL(RBcAPGi-5acD2nD-XL) type of product to get this gear into.I currently run a campus with about 60 roof mounted MT AP's at the moment, and could easily see the new WiFi-7 boards being utilized in 2 years time.. ---

## Response 8
yeah... 320mhz @ 4096qam with an 16x16 array....the baseband/DSP alone will burn a lot of power...the only "good" thing about "wifi7" is the "MU" part, and maybe some improvements to how OFDMA works.the laws of physics will keep us closer to 40mhz@2x2 streams for most applications.i would rather have working wave2+capsman for the existing AX line and CapAC.That will have some real impact in real scenarios, with real phones that real people have from the last 5+ yearswould make a lot more people happy that way (let the half a dozen wifi{next} enthusiasts suffer with tplink for a while) ---

## Response 9
Why no one is talking about MLO.... That for me is the biggest improvement on Wifi7, at least on performance even without a huge Channel width.. ---

## Response 10
320Mb channel width? ... say goodbye to 16 channels at once ... a few devices will "kill" whole block of flats especially if default configuratin set the max power "just to be safe not to be weekest one".BTW ... what channel combintaion in 5GHz spectrum will let using 320MHz mode? ---

## Response 11
The cAP AC XL that was released in 2022 is Wifi ACv1 with no upgrade path.So 2014 radio standard... 8 years later.The audience wifi wave2 driver would bring it to ACv2. A 2016 standard. Which they are just getting into caps-man in 2023... 7 years late.Outside of the 60Ghz PtP line... It's pretty hard to take Mikrotik WiFi seriously anymore. ---

## Response 12
So wifi7 is now here. What does it look like?Is there already hardware with 6 GHz?I've had your hardware with 60 GHz in the house for many years and would love to have everything from a single source. ---

## Response 13
wifi 6 started in 2019 and MT has new products now. Wifi 7 started now so wait 4-5 yers.... ---

## Response 14
Not that long. AX took longer, since we had to move from our own drivers to chipset manufacturer drivers. From now on with wifi.npk package, it will be much easier. ---

## Response 15
Ahh so you are at work Normands, still waiting for the detailed response to this post ( you can use email if you prefer )viewtopic.php?p=1046445#p1046445 ---

## Response 16
Looking at some of the MT YT videos, and the consumer products line upI come to conclusion that MT is targeting products that "wider public/consumers"will buy, rather then creating "latest" products .......Or, as it's evident from the YT videos, operators or large ISP's in bulkat least for "consumer grade products (SOHO)".I could be wrong .... ---

## Response 17
Ahh so you are at work Normands, still waiting for the detailed response to this post ( you can use email if you prefer )viewtopic.php?p=1046445#p1046445I am waiting for some sort of "blanket refund" for the CRS354. ---

## Response 18
Just put it down as a business loss, sending you postage to send to my location. ---

## Response 19
Just put it down as a business loss, sending you postage to send to my location.Its not something I would consider funny.viewtopic.php?t=160561&start=300 ---

## Response 20
Just put it down as a business loss, sending you postage to send to my location.Its not something I would consider funny.viewtopic.php?t=160561&start=300I read the thread, couldnt find one single mention of supout report let alone the 100s I expected to see.Also some folks not reporting issues is weird and sounds like production quality more than anything else. ---

## Response 21
Maybe it's time for cAP be...https://eu.store.ui.com/eu/en/products/u7-pro ---

## Response 22
Only when I get my wifi7 smartphone which is what vendors should be aiming for in the home market. ---

## Response 23
Maybe it's time for cAP be...https://eu.store.ui.com/eu/en/products/u7-proThe U7 Pro will have even more issues than its predecessor since on the 6 GHz bandclient devices' maximum allowed EIRP will be lower than access points'therefore APs need higher gain antenna for the 6 GHz band than for the 2.4 GHz and 5 GHz in order to maintain their RCPI advantage over mobile client devices. ---

## Response 24
... client devices' maximum allowed EIRP will be lower than access points' therefore APs need higher gain antenna for the 6 GHz band ...Tx power asymmetry can not be "rectified" by antenna gain (because it works for both Tx and Rx), this kind of asymmetry can only be "rectified" by asymmetry of Rx sensitivity ... which means that APs will need Rx higher sensitivity than stations. And the difference in Tx power between AP and station is only 6dB. This is way less than difference in Tx power between base station and terminal in mobile networks, in LTE difference is usually somewhere around 20dB (terminals are limited to 23dBm and base stations usually operate at around 40dBm to 46dBm, at least on low and medium frequency bands, i.e. lower than 2.5GHz).Alas, higher Rx sensitivity means that prices of AP chipsets will go up considerably ... perhaps by around 6dB as well. ---

## Response 25
The cAP AC XL that was released in 2022 is Wifi ACv1 with no upgrade path.So 2014 radio standard... 8 years later.The audience wifi wave2 driver would bring it to ACv2. A 2016 standard. Which they are just getting into caps-man in 2023... 7 years late.Outside of the 60Ghz PtP line... It's pretty hard to take Mikrotik WiFi seriously anymore.Credit where it's due.Out of nowhere... The AC units did get an upgrade path to ACv2 at the end of 2023. No longer requiring legacy customers to trash the units to move on.I rescind my earlier statement about "2014 wireless in 2023."We now have 2016 wireless in 2024! ---

## Response 26
Not that long. AX took longer, since we had to move from our own drivers to chipset manufacturer drivers. From now on with wifi.npk package, it will be much easier.Can you give us a hint here, we've been waiting for over 3 years at this point for 6ghz capable wifi gear from Mikrotik. Skip 6e at this point, missed the boat on that, lets get 7 so we can start buying your WiFi gear again. Ready to purchase man!By any chance do you have a router with an M.2 slot inside that I can put a WiFi 7 Intel BE200 card in and update the wifi.npk on yet until you start packaging one with it built in? ---

## Response 27
I seriously doubt that Mikrotik will come out with a "WiFi 7" product in less than 2 or 3 years from now.It also looks like Mikrotik totally missed the "Wi-Fi 6e" market.Some (non-Mikrotik)WiFi 7 , Wi-Fi 7 products are shipping right now.IMO , Mikrotik has great reliable wireless products for Wi-Fi 5 products but hardly anything for Wi-Fi 6. I've been waiting for years for Mikrotik to make a product that operates in the 6 GHz to low 7-GHz bands.Mikrotik never been good with wi-fi/wireless.If you want something good and reliable you getUbiquiti U6-LRfor example as meExample: Friend of mine gothAP ax³and he's not happy with it at least with Wi-Fi range and speeds. ---

## Response 28
Snímek obrazovky 2024-03-05 123734.pngI was also not satisfied with Wi-Fi on cAP ac and hAP ac2, however, since the migration to wifi-qcom-ac drivers, the throughput and stability of the network have improved many times (even with 25-30 clients on one interface).I have hAP ax2 at home for testing and I am getting this over Wi-Fi (one room): (it was download from Steam over WISPs 60 GHz connection on village).The coverage is slightly better than with the Turris Omnia. ---

## Response 29
I seriously doubt that Mikrotik will come out with a "WiFi 7" product in less than 2 or 3 years from now.It also looks like Mikrotik totally missed the "Wi-Fi 6e" market.Some (non-Mikrotik)WiFi 7 , Wi-Fi 7 products are shipping right now.IMO , Mikrotik has great reliable wireless products for Wi-Fi 5 products but hardly anything for Wi-Fi 6. I've been waiting for years for Mikrotik to make a product that operates in the 6 GHz to low 7-GHz bands.Mikrotik never been good with wi-fi/wireless.If you want something good and reliable you getUbiquiti U6-LRfor example as meExample: Friend of mine gothAP ax³and he's not happy with it at least with Wi-Fi range and speeds.I bought hAP ax3 for my parents and for the past 10 months, no issues(there was one Wifi interface freezing issue at the beginning, which Mikrotik fixed). I also installed PiHole on it which my parents seem happy about(blocking ads).The range is also quite good(~90-100m) but I tested it in a very low interference environment. ---

## Response 30
I was also not satisfied with Wi-Fi on cAP ac and hAP ac2, however, since the migration to wifi-qcom-ac drivers, the throughput and stability of the network have improved many times (even with 25-30 clients on one interface).since the migration to wifi-qcom-ac drivers, the throughput and stability of the network have improved many times ---

## Response 31
Any updates coming? ---

## Response 32
I will be surprised if Mikrotik releases their be devices this year... ---

## Response 33
The bet is on. ---

## Response 34
Yea... It took them quite long to release WiFi6 devices. (Not saying that this was bad thing.) ---

## Response 35
Sat through Qualcomm led training today.MLO is awesome in concept!!! ---

## Response 36
I've seen in Normis post since they are not using their in-house Wi-Fi driver anymore they can jump on the wifi7 band wagon with ease, I guess the demand will only be the limiting factor here time will tell of course ---

## Response 37
I think it would be nice to have some kind of roadmap, including Wi-Fi 7. With the proliferation of low-cost Intel BE cards for end-user devices on the market and equipment already available from major competitors - the EAP770 line, UniFi U7 Pro, with the U7 Pro retailing for $189 - it might make it more transparent for many people whether to wait for Mikrotik or buy what is already on the market.Also, https://www.androidpolice.com/wifi-7-phones-list/ ---

## Response 38
Agreed, some kind of announcement is long overdue. ---

## Response 39
I think it would be nice to have some kind of roadmap, including Wi-Fi 7. With the proliferation of low-cost Intel BE cards for end-user devices on the market and equipment already available from major competitors - the EAP770 line, UniFi U7 Pro, with the U7 Pro retailing for $189 - it might make it more transparent for many people whether to wait for Mikrotik or buy what is already on the market.Also, https://www.androidpolice.com/wifi-7-phones-list/You do realize Mikrotik was 8 years late getting wifi ACv2 out the door??? ---

## Response 40
WiFi 7 from Mikrotik will happen, and it will probably happen soon.There are already packages with WiFi 7 drivers in them... ---

## Response 41
If they don't have to wrie their owns drivers now, I guess everything will be smoother ? ---

## Response 42
If they don't have to wrie their owns drivers now, I guess everything will be smoother ?Remind me how the wifi 6 release went. ---

## Response 43
1/4 of all new topics seem to topic "bad wifi on ... AX". As a user visiting frequently this forum I would get the impression that AX devices suffer of some problems. ---

## Response 44
Well a bit of time has passed since I put up this thread....Wi-Fi 8 ..802.11bnThe goal of 802.11bn is to reach 100 Gbps speeds. This is faster than copper Ethernet which tops out at 40 Gbps. This will require retrofitting ceiling mounted access points with single mode fiber.https://en.wikipedia.org/wiki/IEEE_802.11bn ---

## Response 45
wifi 8 is old news. I want wifi 10 aka "wifi X" ---

## Response 46
Wifi 8 will be released the same year Mikrotik release their WiFi 7 AP ---

## Response 47
Wifi 7 was officially released 01/24. Mikrotik will have their wifi7 devices this year. ---

## Response 48
Would like to see something like hap ax2, but wifi 7 and with USB port. ---

## Response 49
Would like to see something like hap ax2, but wifi 7 and with USB port.This would be awesome. ---

## Response 50
Would like to see something like hap ax2, but wifi 7 and with USB port.+1 !! ---

## Response 51
I want a WiFi 7 Chateau with a 5G Modem, 1 SFP+ Port and the rest 10Gbps Ethernet ports ---

## Response 52
And 350-500$ price tag I presume ?And no USB3 port ??Also don't forget more than 16MB of flash for ROS ---

## Response 53
you must choose: 16mb or SFP+. Can't have bothBut joke aside: Chateau line is ISP equipment. Why would one need SFP+ on a consumer device. ---

## Response 54
you must choose: 16mb or SFP+. Can't have bothBut joke aside: Chateau line is ISP equipment. Why would one need SFP+ on a consumer device.Because companies like Google are offering 2.5Gbps and 5Gbps service. Even if nobody needs it, an SFP+ port allows the customer (or ISP providing customer equipment) to put in a 1G, 2.5G, 5G, or 10G optic for connection to the WAN. ---

## Response 55
you must choose: 16mb or SFP+. Can't have bothBut joke aside: Chateau line is ISP equipment. Why would one need SFP+ on a consumer device.Because companies like Google are offering 2.5Gbps and 5Gbps service. Even if nobody needs it, an SFP+ port allows the customer (or ISP providing customer equipment) to put in a 1G, 2.5G, 5G, or 10G optic for connection to the WAN.^- This. ---

## Response 56
While idea is good, all 10G ports and SFP+ in that form factor ? I don't think it's possible. Maybe if they put SFP+ on the side. Also with all 10G ports there is a issue with cooling. I don't think it's possible without active cooling. ---

## Response 57
you must choose: 16mb or SFP+. Can't have bothBut joke aside: Chateau line is ISP equipment. Why would one need SFP+ on a consumer device.Because companies like Google are offering 2.5Gbps and 5Gbps service. Even if nobody needs it, an SFP+ port allows the customer (or ISP providing customer equipment) to put in a 1G, 2.5G, 5G, or 10G optic for connection to the WAN.Chateau is deployed for LTE or 5G areas. This is what these Chateaus makes expensive: their modems. You can expect which speeds on LTE/5G in real world? And with these tremendous speeds 5G/LTE offer it makes no sense to have an SFP port. It makes even no sense to have more than 2.5g ports. And again: Mikrotik develops these Chateau for ISP like the Latvian LMT as I recall. Consumers put it on a desk beside a power socket and it works. It is about needs and costs. They sell the hardware individually as well.When there is need for fiber, then ISP gives you another device. Or you just don't buy Chateau. ---

## Response 58
Chateau is deployed for LTE or 5G areas. This is what these Chateaus makes expensive: their modems. You can expect which speeds on LTE/5G in real world? And with these tremendous speeds 5G/LTE offer it makes no sense to have an SFP port. It makes even no sense to have more than 2.5g ports. And again: Mikrotik develops these Chateau for ISP like the Latvian LMT as I recall. Consumers put it on a desk beside a power socket and it works. It is about needs and costs. They sell the hardware individually as well.When there is need for fiber, then ISP gives you another device. Or you just don't buy Chateau.I jumped in with a "me too," more aboutanyCPE having one or more SFP+, not so much specifically about Chateau. But even then, Chateau with a 2.5G or SFP+ port would be great for businesses who get multigig (>1Gbps) from fiber or wireless (Wave, Tachyon, future vendor) but also need/want an LTE/5G backup. ---

## Response 59
Why is Mikrotik being so dead silent on this? ---

## Response 60
Because they want to surprise us! ---

## Response 61
They dont have a road map, they make it up as they go............... NOT.Its really none of your business, aka what their business plans are. They provide cheaper products with great flexiblity, buy it or not......... ---

## Response 62
They dont have a road map, they make it up as they go............... NOT.Its really none of your business, aka what their business plans are. They provide cheaper products with great flexiblity, buy it or not.........LoL, Yes and no. Depends on how much sales you want to generate/market share you want to tap into etc. Manufacturer and Partner integrator relationships are important but the value maybe oblivious to some. ---

## Response 63
The problem with roadmaps is that after you publish dates, you damn well stick to them. My impression is that MT has hard time when negotiating with manufacturers of MT's designs (because, let's face it, MT is a small vendor compared to some other well known low-end brands). And it might be that MT's development teams can't stick to some deadlines as well. So MT as a company have to act in a flexible way when it comes to production and product launches. Hence their habit of surprising us.Sometimes a close look at beta packages gives some hints about what they are working on (or perhaps they are more wary not to reveal such things to us lately), but the information is mostly vague (e.g. we might see new SoC type mentioned, but it doesn't tell us what kind of device that will be ... or we see some commercial device names but we can only guess their functionality and/or performance levels).So ... relax, seat back and let them surprise youAnd don't hold your breathe while waiting for a new product to appear, it may take longer than you can live without breathing ---

## Response 64
And don't hold your breathe while waiting for a new product to appear, it may take longer than you can live without breathingCorollary:Do you think that's air you're breathing now? /size] ---

## Response 65
The problem with roadmaps is that after you publish dates, you damn well stick to them. My impression is that MT has hard time when negotiating with manufacturers of MT's designs (because, let's face it, MT is a small vendor compared to some other well known low-end brands). And it might be that MT's development teams can't stick to some deadlines as well.Well, we can always look at the big corporations. For example, in the software (as well as gaming) industry, you can simply announce something with a estimated year of release. If Mikrotik agreed to at least that... Customers would be able to plan the lifecycle of their LAN or WAN equipment.The way it is happening now - looks like complete crap and disrespect for their customers.To give you an example, we're thinking about migrating from 802.11ac to new access points right now. Last year was a good year, we were given a good budget, and most of our work equipment, including employee laptops at the branch offices, have already been upgraded to support at least Wi-Fi 6. In our country (where the head office is located) 6Ghz spectrum is allowed, so we are considering migration either to 6E or straight to Wi-Fi 7, which is still under discussion. Accordingly, I have to solve the issue of planning - either we move the entire corporation to mikrotik access points, or we change the infrastructure and migrate to another vendor with a more adequate attitude to the customer. We are not big as Coca-Cola or Google, but we have about 12.000 employees in 11 countries...And yes, we use a Mikrotik. No, we don't use Mikrotik as core routers (I want to sleep well at nightand we still use DMVPN...)P.S. If they hadn't fixed the wireless drivers, migration wouldn't have been an issue - we would have definitely migrated to another vendor's hardware. ---

## Response 66
I agree that there should be a bit of a road-map from Mikrotik, at least in terms of "a product that will.... and has a form factor of ....", because honestly they need to start concentrating on larger customers who as stated by avacha do have large budgets and do lifecycle planning. I also fall a bit into that category of getting a budget to work against, and honestly its getting real hard to justify Mikrotik in core/edge switch gear & wireless to some extent( especially busted drivers in new qcom-ac not working in capsman doing vlans), MT routers thou are generally ok(CCR). I do get a lot of pushback to just put in Cisco gear and be done with it. Its a tough life !It probably wont hurt the bottom line of MT to increase ram/flash storage of future products too so they can jam in a larger OS's( RoS v8+ ), so they don't have to compromise on deliverable features.Anyhow its a wait and see thing as per usual with MT's wireless side of the house. I only hope they have 1 capsman to rule them all in future products, not this broken wifi/wireless 'crap' that has been thrust onto us poor souls who have to manage a large mix of AX + legacy ac2 gear. ---

## Response 67
Poor souls is the right wording.It is quite sure that Mikrotik is working on some Mediathek based devices. We don't know what kind these devices will be. I would guess wifi7 APs. But who knows.I don't even know why is so top secret.there are only 2 options: wifi7 devices come or not come.a) "we are in development and may release 2025"b) "we focus on AX gear and currently no wifi7 in the making"For b) this would make things clear. People could spend their wifi7 budgets on other vendors and done.On the other hand: every new Mikrotik product or development even when public, needs at least some time for stabilization. Look how it went with ROS7, wifi wave2, Winbox 4. Even when it landed, it will most probably be far from production ready. my 2 cents ---

## Response 68
Maybe its time MT splits their product lines, and does a 'budget' version of their gear( which I understand reasons for ), and a PRO line of gear ( happy to pay more to have all the bells and whistles.) ---

## Response 69
Would make sense. Especially for the European market. Labour is very expensive. An European company can make a simple equation: "pay some more $$$ for hardware but get all the bells and whistles or save some bucks on hardware but spend $$$$$ IT admins for hours of hours for troubleshooting capsman" ---

## Response 70
I wonder if RoS v8, or a Kernel update( e.g v6.4+ ) will help assist with Wi-Fi 7.E.g :https://www.phoronix.com/search/WiFi+7 ---

## Response 71
I don't think so. Support in kernel is IMHO mostly relevant for consumer PCs. Embedded devices and even Android smartphones often use very "old" Kernel versions with many patches applied. And SOC vendors like Qualcomm provide their own driver SDK as well. ---

## Response 72
Its been another month, still eager to see some news here.I see they announced a refresh of the model I'd love to have WiFi 7 (6ghz support) in for shop floor industrial machines with ethernet ports that get moved around when the floor is reconfigured for new product runs. They refreshed the wAP ac LTE kit, yes, rounding out the end of 2024 and they released a hardware refresh with an 802.11AC WiFi chipset ---

## Response 73
Yea... @infabo... Year is almost over and still no be devices from mikrotik ---

## Response 74
It's over when it's over ---

## Response 75
Would like to see something like hap ax2, but wifi 7 and with USB port.Yes, I would also like an SFP+ cage for my PON ONT, 2.5G Ethernet interfaces and get this Homeplug AV2 1300 standard back for CPL meshing over powerline option in a USB-C power supply option!Rock. ---

## Response 76
Mikrotik has a serious problem with its product development timelines. This has been happening since the WiFi 5 lines, but especially since WiFi 6. For years, all manufacturers released complete WiFi 6 product lines while Mikrotik had nothing. When they finally started to release something, they didn’t introduce a complete line (indoor and outdoor APs, desktop devices, etc.). Instead, they started releasing products little by little: first desktop devices, then a month later an indoor AP... years later, an outdoor one. By the time they completed their WiFi 6 line, practically all manufacturers were already releasing their WiFi 7 product lines. Knowing Mikrotik, I don’t expect to see the first WiFi 7 products until at least late 2025 or 2026... not to mention when they will complete the line. This makes it impossible to think of Mikrotik as a serious provider of WiFi solutions. As of today, you cannot offer a reasonably serious client a solution that is not at least WiFi 6-based. Until recently, there were no outdoor WiFi 6 antenna options from Mikrotik, which forced us to look for solutions from other manufacturers... inevitably leading to a loss of customers to other platforms out of sheer necessity. It's clear that Mikrotik has very solid solutions when it comes to routing, but we cannot deny that other platforms have them too, and they offer the possibility of implementing an integrated network with all their equipment from the same manufacturer, something that with Mikrotik becomes, at the very least, complicated, especially during periods of technological change. ---

## Response 77
MikroTik has definitely fallen behind, that much is clear. The real question is whether they can catch up. But without a solid roadmap, not even a letter to Santa is going to help them here. ---

## Response 78
I'll bring it up to him, but this wish might be hard to fulfill. ---

## Response 79
The world is moving fast, and companies are making significant investments. It's not just about a handful of devices; we're talking about hundreds of APs being purchased and deployed, sometimes some more to have spare parts. These are investments planned for years ahead. If another vendor is chosen, MikroTik could be waiting years before they even become a theoretical option in the next purchasing cycle. But by then, Wi-Fi 9 could be the standard, and MikroTik might only have a Wi-Fi 7 lineup. Falling behind like this is not a sustainable business strategy for them in the long run. ---

## Response 80
We ask for WiFi 7, and in the October newsletter we get another Wi-Fi 6 product in the wAP ax. Insert facepalm emoji here. ---

## Response 81
the same hype of every year around wi-fi latest and greatest... ---

## Response 82
Before to see a Wifi 7 AP on the market I could accept a Wifi6 with 4x4 MIMO and 2.5gb ethernet uplink . ---

## Response 83
Before to see a Wifi 7 AP on the market I could accept a Wifi6 with 4x4 MIMO and 2.5gb ethernet uplink .Already has - Chateau PRO ax + 2.5G ethernet usb adapter, or two or more ethernet ports in bonding ---

## Response 84
Although with wan throughput effectively capped at about 1.1 gigs, the 2.5 has limited utility. ---

## Response 85
Before to see a Wifi 7 AP on the market I could accept a Wifi6 with 4x4 MIMO and 2.5gb ethernet uplink .Already has - Chateau PRO ax + 2.5G ethernet usb adapterit is not exactly an AP . I mean a device like cAp Ax ---

## Response 86
Although with wan throughput effectively capped at about 1.1 gigs, the 2.5 has limited utility.I don't understand your thought ---

## Response 87
Not applicable to the AP scenario, was speaking to its router suitability. ---

## Response 88
For 802.1be a.k.a wifi7 we need ROS v.8 with linux kernel 6+ ---

## Response 89
Not applicable to the AP scenario, was speaking to its router suitability.ok, sure. in any way I don't see it as AP ---

## Response 90
For 802.1be a.k.a wifi7 we need ROS v.8 with linux kernel 6+does it there a release date forecast ? ---

## Response 91
For 802.1be a.k.a wifi7 we need ROS v.8 with linux kernel 6+does it there a release date forecast ?It's a secret or a surprise for now ---

## Response 92
bad thing ---

## Response 93
Not applicable to the AP scenario, was speaking to its router suitability.ok, sure. in any way I don't see it as APMaybe soon super cAPaxPRO/wAPaxPRO - cAP2G+5SHPaxQ2SHPaxQ/wAP2G+5SHPaxQ2SHPaxQ ---

## Response 94
Spouse is getting iphone 16, it can handle wifi7. Guess who will be buying a tplink the first sale I see on their wifi7 products....... ---

## Response 95
Guess who will be buying a tplink the first sale I see on their wifi7 products.......No idea. Can you give us a hint? ---

## Response 96
You may not see me anymore on the forums. With my wifi7 I will just be a blur if noticed at all. ---

## Response 97
No news isn't good news... Are we going to have to wait for ROS 8.X with Linux kernel 6.5+ to get good 802.11be support? ---

## Response 98
For 802.1be a.k.a wifi7 we need ROS v.8 with linux kernel 6+Well according to a previous poster Qualcomm driver supports Kernel 5.4+ and according to the banana pi docs the corresponding MediaTek one does too. (there are rumors about MediaTek Wi-Fi drivers being tested)https://docs.banana-pi.org/en/BPI-R4/BananaPi_BPI-R4Since ROS7 is using Kernel 5.6.3 that should work out alright.https://help.mikrotik.com/docs/spaces/R ... nelversion ---