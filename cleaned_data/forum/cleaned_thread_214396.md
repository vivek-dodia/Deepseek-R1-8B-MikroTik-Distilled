# Thread Information
Title: Thread-214396
Section: RouterOS
Thread ID: 214396

# Discussion

## Initial Question
Hi everyone just joined here as I'm in desperate need of some help. I've spent last 8 hours straight trying to figure this out before giving into coming here to ask for some help as I just cannot figure out the issue.I recently got 2.5gbps direct fiber installed to my propertyThe basic router that came with the install was a tp link with a 2.5gbps port I plugged it all in and I got 2.5gps speed on all speed tests.The router interface was just useless and I couldn't do some custom port forwarding I needed.So I went for this mikrotikI have set it all up, the ONT is plugged into the sfp plus port with a sfp - rj45 10gb adapterI have set up the pppoe connection and it all worksI have setup my lan on ether 1 port (labeled 2.5g)The connection works but I am constantly throttled at 950 mbps speeds it never goes higher.Currently the interfaces are set to auto discover the speed as if I change it manually I get disconnected and it won't let let me connect again until I change it back to auto discoverAny ideas what I am missing about this? ---

## Response 1
Attached two speed testsFastest one is with isp provided router connected to ontIf I unplug the cables wan in and lan out and switch out the tplink for the mikrotik I get the slower speedsSo the issue has to be with mikrotik somewhere ---

## Response 2
I seem to remember a previous thread on this issue and believe you need to disable flow control on the 2.5 g port. Also I'm unsure if the 5009 can do 2.5 g with PPPoE ---

## Response 3
I'll try and find flow control option and disable that now.Would be crazy if it can't handle 2.5g and a 80 gbp tplink isp provided freebie can ---

## Response 4
Ah flow control is already disabled by default ---

## Response 5
Try turning it on? I found a post on the forum with someone saying that worked for him. Have you searched the forum at all? This has been a recurring thread. ---

## Response 6
Yeah I've been searching for answers all day on multiple forumsI tried turning it on too and no changeAccording to chatgpt mikrotik rb5009 cannot handle 2.5gb speeds using pppoe which is frustratingMay have to order a tp link er8411 instead ---

## Response 7
I've no personal experience but PPPoE in general is the devil. I thought some of the other users suggested they had it working but can't remember if they were using ether1 or SFP+ ---

## Response 8
Have you tried setting the interface rate manually? See the commands here:https://help.mikrotik.com/docs/spaces/R ... ansceiversIt could also be an issue with the SFP interface. Not all SFP+ 10Gbps modules can use multigig rates (2.5 & 5). What model SFP module are you using? ---

## Response 9
This onehttps://amzn.eu/d/iOCAi5b ---

## Response 10
It could also be an issue with the SFP interface. Not all SFP+ 10Gbps modules can use multigig rates (2.5 & 5). What model SFP module are you using?But the RB5009 can do 10Gbps on the SFP+...I never tested one with PPPoE and 2, 5Gbps - but I can say that mine does 500Mbps with PPPoE and barely reaches 10% with PPPoE and fast track. I don't have IPv6, so can't test there.Without fast track it did the same 500Mbps using a little less than 20% CPU - with load evenly spread. Usually the CPU clock was about 250 - 700Mhz. I saw it jumping here and there to 1400, but got back to 700 soon enough.Looks reasonable to me: the product page says we should get about 3Gbps, without fast track, with 25 firewall rules and with a packet size of 512 bytes. Using fast track it gets up to 9 Gbps with the same conditions.https://mikrotik.com/product/rb5009ug_s ... estresults ---

## Response 11
How do I enable fast track? ---

## Response 12
Also about setting interface speed manuallyIf I do this it seems to disconnect me from that connection ---

## Response 13
How do I enable fast track?It comes enabled by default, with the default firewall. Just look for this line, after doing one "/ip/firewall/export" on the router shell.
```
filteraddchain=forward action=fasttrack-connection connection-state=established,related comment="defconf: fasttrack"But this is not Your problem: even without fast track one RB5009 should easily do more than 1Gbps. Your speed looks like the SFP+ (You are using one SFP+ module from Your provider, correct?) speed is set to 1Gbps.Take a look. Go to interfaces, and open the SFP+ tab. Open the "status" part, and look at the "Rate". If it is at 1Gbps, that's the problem. I set mine to 2,5Gbps (that's the speed my module supports) by hand - if left to "auto" it negotiated 1Gbps.

---
```

## Response 14
Also about setting interface speed manuallyIf I do this it seems to disconnect me from that connectionI had some "gotchas" with this.1) My SFP+ takes its sweet time to change the speed. Sometimes more than 45 seconds.2) One thing that doesn't hurt (just to make sure) is to make the change and cut the power. Just to force a cold reboot. Should not be necessary, but...3) If setting by hand, You must KNOW the speed your moduls supports - and the type of connection. It's no use (say) to set 2, 5Gbps baseT if Your module is 2, 5Gbps baseX. ---

## Response 15
For me the status on the sfp interface shows 10gbpsBut the lan status is 1gbps so the issue is with lan side ---

## Response 16
If I set the 2.5gb port manually instead of auto negotiationI get disconnected and cannot connect to that port even via Mac address.Even after reboot and waiting several mins too ---

## Response 17
If I set the 2.5gb port manually instead of auto negotiationWait, are we talking about ethernet 1 here? The only cooper port that is 2, 5 Gbps is eth1. SFP+ is 10 Gbps and all the rest of eths are 1 Gbps. If eth1 can't sync at 2, 5 Gbps then You have some problem either with the cable or one of the ports (either RB5009 or the other device). ---