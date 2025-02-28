# Thread Information
Title: Thread-1122694
Section: RouterOS
Thread ID: 1122694

# Discussion

## Initial Question
Hello. I figured I would post something about how I fixed this problem after wracking my brain for half of a day and to save others the same fate.I have FIOS, and I pay for 300/300. When I replaced my old setup (Orbi RBR50) with the hEX refresh connected directly to my Verizon ONT, I noticed that my download speed was ~300Mbps, but my upload speed was anywhere from 1-6Mbps, depending on the particular speedtest.net attempt. Plug my Orbi back in, back to 300/300. Odd. I messed with every known setting you should try to get it to work, but nothing made a difference (flow control, fasttrack, firewall rules, queues, ethernet settings, the works).While going through the WAN link’s auto-negotiation settings and trying to force 1Gbps full duplex (even though the link was coming up as that anyway), I decided to set my link speed to 100Mbps full duplex and give that a shot. Surprise, surprise, my upload speed increased dramatically…To make a very long story short, there seems to be a problem with the hEX refresh and Verizon’s ONT (I-211M-L in my case) where they do not, in fact, auto-negotiate the link completely/correctly, even though the hEX says the link is at 1Gbps full duplex. After doing some googling, I found a lot of other people that had this type of issue, not with the hEX refresh in particular, but with routers from other vendors like Netgear, Ubiquiti, and others.Their collective fix? Put a small unmanaged switch between the ONT and hEX refresh to force both links to come up as 1Gbps full on their own (with the help of the switch, of course, since the ONT link only works in an auto-negotiate state). In my case, I had an old T-Mobile router from 10 years ago that I booted up, disabled WiFi/DHCP on, and just used the switchports in the back as my simple, unmanaged switch. Lo and behold, I was back to getting 300/300, but this time, it was on the hEX refresh and not just my Orbi.Hopefully this post will help someone out in the future from pulling all of their hair out. A $15 unmanaged Netgear switch is now on order, and I’ll report back with the particular model if it works as intended for this particular issue. ---

## Response 1
So the problem is clearly with Verizon ONT ...Just wondering:What port did you use for uplink to ISP device ? I suppose ether1 ?You are aware ether1 is handled completely different from the 4 other ether ports on that particular version of Hex ? (see block diagram)When you do speedtests maxing out that connection, what CPU usage do you see on your Hex ?I have Hex Refresh here in my home lab (to use as virtual ISP router when I need to prepare setup stuff before deploying) and I use ether2 as uplink to my main router. ---

## Response 2
If I did not make it clear enough that it wasn’tjusta hEX refresh issue when I mentioned others having the same (or similar) issues with other routers, I don’t know what to say there…That aside, yes, I am using ETH1. No, I was not aware that ETH1 is treated completely different, but I’m definitely going to look into it now and give another port a shot. I’m brand new to the world of MikroTik and these hEX routers. I come from the land of enterprise Cisco/Aruba/Palo Alto devices. In 20 years of that landscape, I’ve never run into an auto-negotiation issue with these hallmarks before, which is why this particular issue was so frustrating.Later on in the day, when my better half doesn’t require home internet for her business, I’ll tinker around and see what else I can find out. ---

## Response 3
If I did not make it clear enough that it wasn’tjusta hEX refresh issue when I mentioned others having the same (or similar) issues with other routers, I don’t know what to say there…No, no, you made that very clear ---

## Response 4
If I did not make it clear enough that it wasn’tjusta hEX refresh issue when I mentioned others having the same (or similar) issues with other routers, I don’t know what to say there…No, no, you made that very clear ---

## Response 5
Ok, so I was able to play with all of this before the household woke up…Results: ETH2 does in fact work considerably better when acting as the WAN port versus ETH1. Instead of 300/~3, I’m getting 300/150~. It’s still not as good as having a switch between ETH1 and the ONT though. I would assume ETH2 would improve in much of the same way with a switch in the middle of it and the ONT, however, I did not test that out this round.Despite my best efforts, I was unable to get ETH2 to do more than 150~ upload. Swapped back to ETH1 while using my T-mobile router as a middle-man between itself and the ONT, and I’m immediately back to 300/300. As a side note, I am using the same CAT6 cabling for all of these different setups; I’m just moving the same cables around.Thanks for the tip on swapping out the ports. Even though the manual explicitly states to use ETH1 with one’s router, I’m sure your tip will help someone else out that doesn’t have another network device to use as a middle-man. ---

## Response 6
So the problem is clearly with Verizon ONT ...Just wondering:What port did you use for uplink to ISP device ? I suppose ether1 ?You are aware ether1 is handled completely different from the 4 other ether ports on that particular version of Hex ? (see block diagram)When you do speedtests maxing out that connection, what CPU usage do you see on your Hex ?I have Hex Refresh here in my home lab (to use as virtual ISP router when I need to prepare setup stuff before deploying) and I use ether2 as uplink to my main router.I just realized I hadn’t answered the CPU usage question. Pulling down 300Mbps, CPU is at ~20% during the download phase of the speedtest. While uploading, CPU drops down to around 2-3% (when ETH1 is directly connected to the ONT). ---

## Response 7
Thanks so much for posting this solution! I fortunately had a 1GB switch laying around to try this out. I was about to return the hEX Refresh! ---

## Response 8
Thanks so much for posting this solution! I fortunately had a 1GB switch laying around to try this out. I was about to return the hEX Refresh!You’re welcome! I figured only one aneurism was enough as far as this matter was concerned. I’m glad to at least help someone else with the same issue. Thankfully this is the only “major” quirk I’ve run into with the Refresh specifically, so hopefully you’re also now in the clear! ---

## Response 9
One month later and still in the clear! Thanks again! Now I have to decide if I should replace perfectly working CAPs with hAP ax ones in order to upgrade to Wifi6. ---

## Response 10
One month later and still in the clear! Thanks again! Now I have to decide if I should replace perfectly working CAPs with hAP ax ones in order to upgrade to Wifi6.No problem! I’m glad it’s working for you. For the others out there, I winded up going with a simple 5-port TPLink switch, and it has worked perfectly so far.I purchased two hAP AX2’s alongside the hEX refresh and have them configured using CAPsMAN on my hEX. After muddling through that learning curve, everything works great. I was using an Orbi RBR50 with one satellite before, and performance is definitely better all-around. Range isn’t as great, but I also don’t need my wifi network to reach past my house as much as the Orbi system did. I’m currently on RouterOS 7.17 all-around and I have no complaints! Definitely recommended if you’re not using WIFI6 yet and have devices that support it. ---

## Response 11
One month later and still in the clear! Thanks again! Now I have to decide if I should replace perfectly working CAPs with hAP ax ones in order to upgrade to Wifi6.If you have cap AC devices, you can use wifi-qcom-ac driver. No need to replace them yet (unless you really want to). ---