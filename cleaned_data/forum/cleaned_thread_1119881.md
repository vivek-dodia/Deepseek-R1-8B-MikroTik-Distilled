# Thread Information
Title: Thread-1119881
Section: RouterOS
Thread ID: 1119881

# Discussion

## Initial Question
I am looking through NetInstall documentation for Chateau Pro AX and by default it uses ether1 port, which is also default WAN port. Of course I can change WAN port to anything else, but is it not a bad idea to let NetInstall port = WAN port by default? Doesn't that make router vulnerible to attacks over WAN?I think NetInstall disabled if booting is set to "nand-only" instead of default "nand-if-fail-then-ethernet", but when trying to change to "nand-only", I get "not allowed by device mode ()" error. ---

## Response 1
Wait a minute ...when you netinstall, what other device is connected to that WAN port in order to perform that netinstall ?Tip: not the Big Bad Web ... most likely your PC.Non-issue.Second part is most likely a result from new device mode settings since 7.17rc(whatever).Check that part to enable it. ---

## Response 2
Ether1 is default WAN port and is also default NetInstall port. Using such defaults allows us of NetInstall through WAN port. That means use of NetInstall of WAN. That's an issue for sure. ---

## Response 3
You can not have AND ISP device AND your PC for netinstall connected at the same time to one single port.Not without a switch or hub in between.The fact you need to use ether1 for netinstall, forces you to disconnect whatever WAN device is connected to it.Again: non-issue. ---

## Response 4
Again: non-issue.It would actually be an issue if netisntall would have to be performed through any other port then WAN.What I do agree on is that any device connected to any port on the Routerboard is a potential thread. ---

## Response 5
It would actually be an issue if netisntall would have to be performed through any other port then WAN.What I do agree on is that any device connected to any port on the Routerboard is a potential thread.1- indeed and that's why with the current process, it remains a non-issue.2- True but that's the responsibility of the admin handling that device. And for most home/soho device, port labeled as WAN is default protected by firewall. All other ports are considered to be LAN (as in: trusted).E, g, CCR do not have a firewall by default but those devices do have notifications in manuals they first need to be setup properly before being used.Nobody can help it if a WAN connection is put on another port then where it should be without proper config.Nobody can help it if you do not read the manual.Are you also going to blame car manufacturers if the owner puts in water in the tank ?Let's remain a bit logical and practical, shall we ? ---

## Response 6
Are you also going to blame car manufacturers if the owner puts in water in the tank ?Depends on where you life I think, Europe isn't that bad.Let's remain a bit logical and practical, shall we ? ---

## Response 7
It can only be an issue when:- your WAN is actually a plain L2 link to the ISP network and there could be someone on the other side who can connect a machine with netinstall to that- they already know your credentials so they can log in to your router and set "boot ethernet once" and then do a reboot.- alternatively: they have a person on site that can boot the router with the button pressed.Not a very likely scenario... but you can always put WAN on another port and leave that port open or put some "lock" in it? ---

## Response 8
It can only be an issue when:IMO none of ifs help with OP's considerations ... because they're out of device admin's hands. But there's an up side: netinstall is not triggered without doing a few things and all involve physical access to device at some point:button presswhilecold booting device which ultimately puts device in netinstall modethis is not easily done, at many SOHO devices the button is pretty close to power jack so it takes some effort to do it properlychanging routerboard setting toboot-device=try-ethernet-once-then-nandwhich, since ROS 7.17, requires device mode setting routerboot enabled. By default it's disabled and to enable it one has to "power fail" device while setting change is pending (max 5 minutes)But if device does enter netinstall mode, it can be a problem with certain ISPs ... specially those with "flat networks" ... where customers might not be as separated as we'd like to think ... ---

## Response 9
Ok but even with a flat L2 network the "hacker" must be in the same L2 space (which means at the ISP or maybe in the same street in some cases) and it cannot be "a Russian hacker" (over here the media think that all hackers are Russian) working from home. ---

## Response 10
When on ROS 7.17 and presuming the routerboot has the default boot mode "nand-if-fail-then-ethernet" then you need to do a physical button press to either change the bootmode( to something different) or power cycle while holding the reset button until the device boots into netinstall mode.So unless the evil person has physical access to your device: no way to netinstall. Regardless of eth1 is WAN or whatever. ---

## Response 11
Yes, but who has installed 7.17? I probably never will...Before that, an admin user could set the "try ethernet once" mode and reboot, but even then it would not work on a typical internet connection (at least here, it is all PPPoE) ---

## Response 12
OP has Chateau Pro AX. I would advise to upgrade to latest ROS for this pretty recent device. ---

## Response 13
I have all the updates and RouterBOARD upgrade and this is the best router money can buy. For $200 it beats anything out there. I wish I was a professional reviewer with credibility to write a review of this beautiful device, but my posts show I don't know enough about networking.Back to topic - yes, my concern is MITM between router and ISP. I'm behind CGNAT with shared IP's and there is some crazy neighbourhood traffic. ISP doesn't even isolate routers and forces UPnP and DIAL protocols over WAN on their own routers, which I, of course, do not use. That, and STP's are everywhere on this WAN, but fiber connection is super-fast with ultra-low latency.I think remapping the port is the safest bet. Its just too simple. ---

## Response 14
Back to topicAgain... there is no known way to force a netinstall from the outside without the router asking for it. The probability that such a way exists is similar to a probability that a way exists to access the router management with proper firewall rules in place and without knowing the credentials, so exposing the netinstall interface to your ISP network does not increase the attack surface significantly.But for your device model in particular, repurposing any other Ethernet interface for the WAN role won't have any negative impact - ether1 is not a 2.5 gigabit one, nor can your ISP power your device via PoE, so moving away WAN from ether1 would only become an issue if they asked you to power their gear using PoE. So although there is a consensus here that you don't need to care, it will be helpful to move the WAN elsewhere, because peace of mind is important. ---