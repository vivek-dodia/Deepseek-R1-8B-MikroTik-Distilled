# Thread Information
Title: Thread-211441
Section: RouterOS
Thread ID: 211441

# Discussion

## Initial Question
Been using an ATL LTE 18 while I wait for a fiber connection, and it works great aside from a non-trivial issue: in the past few days, every couple of days it slows down to a crawl.Symptoms are like a system being bogged down by CPU/disk usage: very unresponsive on all fronts, but I'm still able to log in (with a lot of patience) and issue a reboot command. Rebooting fixes everything for another couple of days.Problem is, I'm not seeing a CPU spike when this happens. I set up mktxp to track counters, and I am attaching the view from this morning when the slowdown happened again. Around 7AM I restarted the router, and now all is fine.It's a pity that this is happening as it's a great device otherwise. Any ideas on how to investigate further?Edit: I'm on 7.16, modem firmware EG18EAPAR01A13M4G_01.002.01.002ATL LTE18 stats.png ---

## Response 1
one question not related to your problem, what program do you use to analyze the device?txkorg ---

## Response 2
one question not related to your problem, what program do you use to analyze the device?mktxp, which leverages Prometheus and Grafana to store metrics and visualize them in a dashboard. ---

## Response 3
Hi!Did you figure this out? Im having exactlysame problem. When it slows down I can log it, but it pretty slow and unresposive. Ping might go thru to 8.8.8.8 but its 4000-6000ms. Im using ATL18 only as an LTE modem. Passthrough mode and I have firewall which does all the LAN traffic. ---

## Response 4
Did you figure this out? Im having exactlysame problem. When it slows down I can log it, but it pretty slow and unresposive. Ping might go thru to 8.8.8.8 but its 4000-6000ms. Im using ATL18 only as an LTE modem. Passthrough mode and I have firewall which does all the LAN traffic.I didn't, and luckily I finally got fiber installed so put the ATL away. Which is a pity as I would like to use it in a remote location where I have an old Huwaei CPE, but won't until this issue is resolved as I need a super reliable connection there. ---

## Response 5
The part of the story missing is the LTE metrics. If you're doing monitoring, adding RSRP, RSRQ, and SINR likely be useful since it could be on the LTE carrier side (i.e. time-of-day, changing bands, etc.) which some data either confirm or rule-out.Now the dramatic drop in traffic might indicate some device-side issue... But the first thing to check is the ATL is fully updated including RouterOS, RouterBOOT (in /system/routerboard), and the LTE firmware (/interface/lte). Often the factory installed version is pretty old and Mikrotik does routinely update LTE support. If these versions get mismatched, that where you often seeing more random problem IMO.Maybe already fully updated... but that's always the first thing to try. ---

## Response 6
I did add LTE metrics at the time right after posting, and LTE is rock stable. And yes, everything was up to date: os, modem and routerboard firmware. ---

## Response 7
The part of the story missing is the LTE metrics. If you're doing monitoring, adding RSRP, RSRQ, and SINR likely be useful since it could be on the LTE carrier side (i.e. time-of-day, changing bands, etc.) which some data either confirm or rule-out.Now the dramatic drop in traffic might indicate some device-side issue... But the first thing to check is the ATL is fully updated including RouterOS, RouterBOOT (in /system/routerboard), and the LTE firmware (/interface/lte). Often the factory installed version is pretty old and Mikrotik does routinely update LTE support. If these versions get mismatched, that where you often seeing more random problem IMO.Maybe already fully updated... but that's always the first thing to try.I updated RouterOS and RouterBOOT earlier and they are up to date. I have excellent value on all RSSI, RSRP, RSRQ, and SINR. And we also have two mobile phones with 4G. Same operator. There is no problems with singal. This happened two times today. Everything was excellent 10 hours and then suddenly it slows down to unusable.I pinged 8.8.8.8 30 minutes and it was 2000-6000ms. CPU and Memory are fine everytime this happends. Tried to disable LTE interface but couldnt enable it anymore. RouterOS crashes everytime and it remains disabled when i log in again (which is slow to do). Then rebooted and everything works again... ---

## Response 8
Same exact symptoms I was having... ---

## Response 9
If you can't disable the interface without a crash, that seems like bug somewhere. I'd file a ticket atsupport@mikrotik.com, and make sure to include a supout.rif when you have the problem.If it keeps happening, you can also try running 7.17rc (+upgrading the boot and LTE firmware too for 7.17), which may a quicker to try than waiting for support to get back. ---

## Response 10
If you can't disable the interface without a crash, that seems like bug somewhere. I'd file a ticket atsupport@mikrotik.com, and make sure to include a supout.rif when you have the problem.If it keeps happening, you can also try running 7.17rc (+upgrading the boot and LTE firmware too for 7.17), which may a quicker to try than waiting for support to get back.The main issue is not being unable to disable the interface, it's not having the slowdown in the first place. I've been using a (bulky, inflexible) Huawei CPE for the past 4 years in my other (offgrid) house, and I never had to reboot it once. LTE is often used in remote locations, where you cannot go to the other room and pull the plug when something starts misbehaving. Especially if it happens twice a day.My ATL is now an expensive doorstop, and it will be a long time before I buy another Mikrotik LTE product. Which is a pity, as I love RouterOS (my fiber is terminated on a RB450Gx4 and I have several other RouterOS devices scattered around). ---

## Response 11
We have many similarly configure LTE routers, so it's easier for me to test that a version works before dealing with anything remote... But if you got just one and it's remote, that makes it harder... Especially if it's stable for hours and then dies, that's sounds really annoying...Their support is pretty good at fixing things, albeit not quick. But it's why I keep focusing on the version... since there are totally bugs for some combo of device/modem/carrier over the releases... & what seem to happen sometimes is they fix something for one modem/carrier, that may break something else that was working. But why trying both "stable" and "testing" is worthwhile when facing LTE issues, since they do make fixes often to LTE. ---