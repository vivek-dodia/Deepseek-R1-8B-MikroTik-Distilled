# Thread Information
Title: Thread-1123477
Section: RouterOS
Thread ID: 1123477

# Discussion

## Initial Question
I would like to have a possibility to create a crc hash for local file. This way I can make a backup file every day. If the file today is has a different hash than yesterday, I know some has changed and then send the file to external server. ---

## Response 1
It would have to be more intelligent than a simple hash, because the backup includes a stamp of the date/time it was made, so each time the hash would be different.(unless the hash function would be smart enough to skip that timestamp) ---

## Response 2
Weird, they look the same here.
```
PS D:\Temp> Get-FileHash .\GW-R4-20220927-1916.backup
Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
SHA256          9732B4DD495D13E49B875D3C2862F5AC606DAE6349C1A1AE6A0128542F1D99D0       D:\Temp\GW-R4-20220927-1916.backup
```

```
PS D:\Temp> Get-FileHash .\GW-R4-20220927-1917.backup
Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
SHA256          9732B4DD495D13E49B875D3C2862F5AC606DAE6349C1A1AE6A0128542F1D99D0       D:\Temp\GW-R4-20220927-1917.backup

---
```

## Response 3
Ok you mean a .backup file... I never use that because it is impossible to restore it on a new device when the old one breaks.I use .rsc files and they do include a timestamp. ---

## Response 4
@Znevna You are 100% that some config has changed, not just the file name? ---

## Response 5
I was just proving that backup files don't contain a timestamp inside.But pe1chl was referring to rsc files, and not to the backup files that you were talking about.Try to keep up. ---

## Response 6
I would like to see the functionality to create checksums as well. But please do not limit this to file, but support it via parameter:
```
:put [ :sha256 input="foo bar" ];
:put [ :sha256 input=[ /file/get content your-file name ] ];That way you can also strip the timestamp from export files to check for differences.

---
```

## Response 7
There is a separate topic about suggesting new features for the scripting language:viewtopic.php?p=913066Maybe this fits better in there...However, it was started in 2018 by mrz but it does not look like any of the useful suggestions made in there has ever been implemented...One problem with the scripting language is the fixed 4096 byte limit on string values, even within expressions, which means that a file larger than 4K cannot be processed this way. It would have to be processed in a "open/read records in a loop/close" fashion, but the scripting language does not support that. ---

## Response 8
Create dynamic vlan entry with added tagged bridge to it in "interface/bridge/vlan/" when i set interface vlan on bridge with vlan filtering enabled, like you alredy doing it with pvid. ---

## Response 9
A very simple element will help make it easier to put things in order in the winbox window. Attached design example.Screenshot 2022-09-30 122747.png ---

## Response 10
Would love to see some of the CAKE functions offloaded to the packet filtering engines on various low/medium range devices. ---

## Response 11
Dear Mikrotik, Is it possible to fix the vlan priority tagging issue concerning firewall or bridge rules ?Pls see this forum topic :viewtopic.php?t=189628Regards. ---

## Response 12
Add Support for "Virtual Interfaces"-MACVLAN-IPVLANMore infohttps://developers.redhat.com/blog/2018 ... networking+1 ---

## Response 13
Please implement PPPoE hardware offloading on devices with chip that supports it.PPPoE data packet processing should not load a CPU core. ---

## Response 14
HiCan add comment on view list of columns ? its easy to view/edit/sort by comment some time need it specially in ip firewall address listaccess.png ---

## Response 15
HiCan add comment on view list of columns ? its easy to view/edit/sort by comment some time need it specially in ip firewall address listIt already existsDon't you read what appears in front of you?Instead of clicking "Show Columns..." it's just the top row option... "Inline comments"May the peace be upon you. ---

## Response 16
ah done I think I need to renew my mikrotik certificate very oldacc2.png ---

## Response 17
Not sure if this is supported or I am being an idiot.Handing out /32 dhcp leases using radius and unnumbered interfaces.currently using dhcp lease script to add the correct address and network in the address table of the dhcp server ---

## Response 18
Would love the ability to specify a DoH server but also FWD entries to specific DNS servers. Currently, enabling DoH disables all FWD entries. ---

## Response 19
Would love the ability to specify a DoH server but also FWD entries to specific DNS servers. Currently, enabling DoH disables all FWD entries.Me too... But all comments here in forum are ignored by Mikrotik. ---

## Response 20
The DNS resolver is a joke... just see how many new bugs there are in every v7 beta/rc release.The fact that a DoH server should just have been another server in addition to the plain servers (keeping the same functionality for the static entries) is just the most obvious problem. ---

## Response 21
There is a separate topic about suggesting new features for the scripting language:viewtopic.php?p=913066I just wish there was some clarity when folks should use the "Feature Request" in the new-ish help.mikrotik.com. I'd like to think some the items here and above link are at least being tracked by them – but hard to know.Just for example, should everyone who needs JSON support, file a feature request in Jira / help.mikrotik.com? That seems a bit silly. At the same time, it be good to know an item is "on the list" with some ACK in forum to some of the reoccuring themes. ---

## Response 22
Create dynamic vlan entry with added tagged bridge to it in "interface/bridge/vlan/" when i set interface vlan on bridge with vlan filtering enabled, like you alredy doing it with pvid.+1 ---

## Response 23
Are there plans to add support for additional LACP hashing algos? encap2+3 and encap3+4 would be greatly appreciated ---

## Response 24
Hi, Happy new year everyone and great Mikrotik Tip shared today:https://www.youtube.com/watch?v=BbDnBxlBTdYFeature Request:Possibility to disable the anti-replay protectionDescription:This feature request is probably very specific, however don't think it would be hard to implement, at the moment the replay value seems to be always ON and hard-coded to 128B:/ip ipsec installed-sa> printFlags: H - hw-aead, A - AH, E - ESP0 HE spi=0x70426F0 src-address=162.159.65.18:4500 dst-address=192.168.1.100:4500 state=mature auth-algorithm=sha256 enc-algorithm=aes-cbc enc-key-size=256 auth-key="<REDACTED>" enc-key="<REDACTED>"add-lifetime=24m19s/30m24sreplay=128This anti-replay protection it's actually a problem when trying to use the Mikrotik IPsec with anycast networks like Cloudflare:https://developers.cloudflare.com/magic ... rotection/Many devices allow disabling the anti-replay protection but i wasn't able to find a way to do it on Mikrotik, which is why i mentioned above it's hard-coded, if there is one way to do this please let me know.While i'm not able to make the IPsec work, the alternative will be to set up GRE tunnels, which due to the lack of encryption not everyone is willing to use. ---

## Response 25
Feature request is to move the "Disable" button away from other common actions such as "Comment" or to add a "Confirm" dialogue. Too easy to disable an interface accidentally by being a few pixels off target when you are trying to click on "Apply" or "Comment".disable-button.jpg ---

## Response 26
[feature request]pppoe-relayand broadcast-relaycould be extra package possibly bundled with other relay daemons[feature request]ipsec alg (helper)[feature request]dhcpv6 server - address (/128) distribution[feature request]dhcpv6 client: ability to change DUID manuallywould be useful if you have lots of links from same provider.[feature request]configurable looking glass package for ROSv7[feature request]Please add routing-table support for ping and traceroute[feature request]Please add clear-DF and strip-IPV6-options actions for IPv6 firewall (mangle)[bug report]4 uplink with 4 VRFeach had add default route feature with distance:10VRF confuses and one pppoe interface has TX drops and shows RX bytes/bps: 0thanks for reading hope it can be fixed.changing default route distances fixes the problem temporarily. i guess VRF conflicts with ECMP. fyi.[feature request]please add wireless DTIM and beacon interval setting.[feature request]please add TCP_RTO_MIN, TCP_RTO_MAX and the tcp_retries2 settings[feature request]Please add target and destination to queue tree rulesPlease add 'any' packet mark matcher to queue tree.[feature request]Please add;expired DNS cache sizeandexpired DNS cache TTLand fallback to expired storage when resolver is unable to resolve something.something like recycle bin[feature request]regarding wireless ANI feature; add one another choice line below: REQUIRED or just ENABLED.thanks for reading and considering, regards ---

## Response 27
[feature request]WinBox Keyboard hotkey navigationto be activated for example pressing [ALT] twicethen the menu items could, for example, be iterated through a-z and on submenus (like MPLS, etc.) the iterations could move over to the submenuso navigation could be much faster, hence one can navigate with the keyboard anyways for adding entries ( [INS] key) or de/activating items ( [STRG]+[D] / + [E] )MT-featReq_winbox_keyboardShortcutNav.png ---

## Response 28
Add to Winbox a menu section with commands for automatic arranging multiple windows (cascade, side by side, in a stack) ! ---

## Response 29
I suggest in Winbox program implement the ability to display two additional columns in the window of the "IP - Firewall - Connection" section: the first should display the number # of the rule line from the "Filter Rules" section, which allowed packets to pass, and the second column should display that " comment" which is recorded for the corresponding rule with line number # from the "Filter Rules" section. This functionality will make it possible to significantly simplify the process of debugging firewall rules, i.e. it will become similar to modern Next-generation firewalls. ---

## Response 30
WinBox Keyboard hotkey navigationto be activated for example pressing [ALT] twiceWow. That's a good one!+1 for #HotLockWinbox ---

## Response 31
This functionality will make it possible to significantly simplify the process of debugging firewall rules, i.e. it will become similar to modern Next-generation firewalls.You can already do some of that yourself! In the firewall you can apply connection marks and you can see them in the connections window.Also, in the firewall you can enable "log" (+ optional tag) and see the matching packets in your log window. ---

## Response 32
[feature request]Hi all, On my Tik I am using few VLAN's, multi Wireless networks and about 10 DHCP servers due to a need of splitting the connection to different sectors that should not communicate one to the others.I also need a way of seeing inone place all the connected devices for all the network's, and the best way of seeing this closer to my need is similar to Quick Set - WISP AP - Local Clients (but the Quick set is intended for other purposes, and not for "viewing things, or so).I would like to see something similar on the main menu, maybe on the Interface menu would be a good place for this; to create a tab about "Connected devices", or maybe a dedicated place on the main menu for this would do the trick.I would like to see over here:- All the local clients listed (IPv4 and IPv6)- The type of the client connection (wifi / ethernet)- The total number of clients connected via Wifi / Ethernet - if possible listed also by each network (VLAN / VPN / each Wifi network), e.g 2 clients VLAN 22, 3 clients Wireguard, 22 clients VLAN 33, 1 client IPSec- The MAC of the device- The IP of the device- The VLAN, VPN (Wireguard, IPSec or whatever) and the DHCP server used- The comment of the DHCP Lease for the static IP's (i am using this for naming the clients in case of the client does not have a defined name - some IoT and not only IoT devices does not have a device name on the network provided by the device itself for the identification)- For the Wifi devices - the signal straight and the 2.4 / 5 GHz, whatever connection it uses- The up-time- The current up/download speed, the average rate, the Bytes and the packages, the top up/download speed on the last hour / day / week / month- The Brigde used for the client- The Interface used for the clientIt would be also nice to be able on this screen to enable/disable the view of the entire DHCP leases that uses a static IP that are not connected at the current moment and to see the last connection time.. ---

## Response 33
I would like to see something similar on the main menu, maybe on the Interface menu would be a good place for this; to create a tab about "Connected devices", or maybe a dedicated place on the main menu for this would do the trick.You do some of this in webfig with the Status page. Any of the controls in webfig, from any page, can be add as an element on a Status page. Seehttps://wiki.mikrotik.com/wiki/Manual:W ... tatus_page ---

## Response 34
When you start the phrase like "You do some of this into other whatever" you troll me.My request was:1. for Winbox2. more complex than what the Webfig offer's on that cripy interface for your own puzzle that puzzled you from the startIf you cannot add value, or, if you do not understand the request, please keep your words for yourself. ---

## Response 35
You did not mention that your request was for Winbox! How can anyone know that?Of course it is possible to do what you want using an external program and scripting and/or API calls.Maybe a useful feature request for Winbox would be to have some capability for user-defined menu entry that opens a form (or even a generic terminal window) that can be populated using a script.I have seen uses for that as well. And it would be more generic than to have them implement exactly what you need in that much detail. ---

## Response 36
Sorry, my bad, i had lost some text and missed that; the request was for Winbox indeed, even if it is not mentioned.It would be a huge effort to make the Winbox able to be manage a sort of lego screen composed with whatever you like as columns from the entire RouterOS available screen's, i do not think that this is a bad idea; but the first thing to do is a "Status page" that may be used to see all the connected devices from all the network's in one page. I have just made a list of what i consider, but the software architect and the Mikrotik team will be the ones that will decide if this is manageable, if this is required and what should contain. My feature request and my list is just a start for whatever may be, if it may be anything on this side.The first step is to have something like this build in into Winbox from the start; API's, script's, lego and puzzle's may be developed afterwards.Not to have something so basic into Winbox is worse than having something that does not satisfy all the client's. Scrip't and API's are not for the basic users of Tik's (e.g. soho users)but i agree that are a good ideea; but, let's nail them one by one.In fact, they got all they need to do this, is that screen from the Quick Set that may be improved a little bit and placed as independend window or a tab, is not so difficult i assume. ---

## Response 37
Well, I hope that (but I have never researched that) winbox, webfig and command operate using some form of table that defines how a dialog is presented (layout) and what data it shows.I.e. that this is not in code, but it is data-driven. The capability should already be there, it just isn't exposed to the user.Similarly I would like to have the possibility to add an extra field in a form, especially on the Status tab of some items, where it can show the output of a user script.I have worked with a Windows application that has that capability, and it is very convenient to have that. It also reduces the number of feature requests a supplier has to implement, because users can resolve some of them on their own without bothering the supplier. ---

## Response 38
You do some of this in webfig with the Status page. Any of the controls in webfig, from any page, can be add as an element on a Status page. Seehttps://wiki.mikrotik.com/wiki/Manual:W ... tatus_pageNot any controls, and by the way, the Design is extremely buggy, slow, crashes with Firefox and even with Chrome, log's you out random sometimes. I never manage to add more than few things (basic). You were never able to add the mentioned list and status of the Local client's (the one that i was referring to). To be honest...could that feature be ever used by the users that want a Status of the clients, interfaces, VPN connections, signal and other real time data; or is it only for static fields data meant to be usable ? No, to honest, not even if I try (i have just tried now to do my setup on Webfig), I could not get what I need from that functionality, because you simply cannot. ---

## Response 39
I'm not the target. Especially as someone who design configs so they don't break "QuickSet as a status page" & too familiar with limitations of the webfig. All I was saying it's not like they are starting 0% on a "status page" & more trying to be helpful to readers here who may not even know the webfig status page part existed – it is useful, but could be better for sure.<rant>But I'll be honest it's the talk of "Multiplatform Client" I fear (in "WinBox for MacOS" from@Normis (in 2021)):We do have plans for true multi platform Winbox. Finally. Let this be a teaser for 2022No ETA and no promises though.I even use a Mac, and I want winbox fixed up rather than some new client... Maybe with 60+% of internet traffic mobile users (and growing), fixup the existing, languishing mobile apps? So this Mac user wants the same incremental progress onwinboxas the "Desktop solution".Anyway, this forum is littered with reasonable and somewhat smallish feature-ettes and/or "bugs" – some more trivial than others no doubt. But progress on some of the small items here (and other threads too), but especially on the tools like Winbox, Dude, etc. is extreme slow or non-existent. Obviously I'd like them working innovative new things. But so many good features...that are missing a few minor things that really make them shine. Instead I get the impression they get lumped into future/mythical "new multiplatform winbox". For what? to solve theoretical concerns about wine...</rant> ---

## Response 40
It is still my opinion that effort spent on a MAC-specific Winbox (and then a Linux-specific one? What about *BSD?) is better spent on making a modern web-based config tool that has the same functionality as Winbox but runs in a browser like Webfig.It would have been difficult in the days when Webfig was first created, but nowadays other companies show what is possible and it is way more than what Webfig does.The advantage is that there is no more need for specific client OS support, there would be only some simple "agent" that can perform tasks like MAC-level connect, RoMON, and Netinstall, and that you can run only when you want to do that (and which you manage via your browser to a port at localhost). ---

## Response 41
The advantage is that there is no more need for specific client OS support, there would be only some simple "agent" that can perform tasks like MAC-level connect, RoMON, and Netinstall, and that you can run only when you want to do that (and which you manage via your browser to a port at localhost).But wait, there will be no more Mikrotik way of being in that case. There will be no more pain all over the place and obscure tools and settings that only the Mikrotik guy knows and then Mikrotik will be more and more like all the others and there will be nothing special about them, they probably will just work without bug's and so and you will forget them at all.It is so fun to discover the wheel all and all and all. I must agree that they are doing a lot of things in a very particular way (very advanced and a high modularity) and they are so good of creating their own ecosystem that they go sometimes to such complicated things that lead them to discover the AX standard or the WPA 3 after such a long time after low end companies and the entire planet; and lead them to create an ecosystem (v7) that still does not have a long term version after few years of development and another one year and (almost half) of releases (not to count that there was 17 !!! official releases from the v7.1.1 launch until now).No, "simple" is not a good word to place in connection of your Mikrotik. ---

## Response 42
The advantage is that there is no more need for specific client OS support, there would be only some simple "agent" that can perform tasks like MAC-level connect, RoMON, and Netinstall, and that you can run only when you want to do that (and which you manage via your browser to a port at localhost).But wait, there will be no more Mikrotik way of being in that case. There will be no more pain all over the place and obscure tools and settings that only the Mikrotik guy knows and then Mikrotik will be more and more like all the others and there will be nothing special about them, they probably will just work without bug's and so and you will forget them at all.To make my point clear: in that proposal I do NOT intend to indicate that the entire management interface of RouterOS should change towards what a home router is!What I propose is that Webfig is upgraded to supply what Winbox now does (interface with child windows, selectable columns, dialogs with tabs, etc). But the function of the dialogs in that revamped Webfig would be exactly what it is now in Winbox. So the same "knowledge about obscure config" would be required, only it could be applied from any device with a modern internet browser, with no software to be installed or run except in cases where low-level access is required. (e.g. to rescue a device where one has been locked out, or that has been bricked) ---

## Response 43
I guess I'm saying fix up theexistingtooling for advanced users. A few small things would go a long way... AND, give some breathing room for MT to create some great new tools, even if that meant whatever "multiplatform client" came in years (like V7 ended up taking)...For home users, fix up the mobile apps. They already do setup (for a single WAN), status, and port forwarding, so starting in a reasonable place. But things like adding device notifications, would avoid needing scripts for what is obvious need. Or use the mobile OS to store passwords, etc. Or having some "multi WAN" or "VLAN" wizard that do the [cleaver+ridiculous] recursive routes for the user. Sure there are others that make it easier for a neophyte to setup/use Mikrotik. Put those in the mobile apps.Bundling up everyones needs into some great new thing is why there isn't a more keyboard shortcut, status page in Winbox, or important things like BFD. ---

## Response 44
Bundling up everyones needs into some great new thing is why there isn't a more keyboard shortcut, status page in Winbox, or important things like BFD.^^^ Best way of saying where Mikrotik lose themselves. Totally agree with you previous post as entity, not only the quote. ---

## Response 45
Bundling up everyones needs into some great new thing is why there isn't a more keyboard shortcut, status page in Winbox, or important things like BFD.To be clear: I don't propose a great new thing, I propose reworking of an existing tool and after that is finished, end the maintance of another existing tool.(including ongoing requests to port that tool to another OS, incurring more and more development work on what is essentially a dead end)I agree that "feature parity of v7 relative to v6" (including support for BFD at least with the features it had in v6) should be the #1 priority, but all recent release notes show that MikroTik (unfortunately) does not see it that way. ---

## Response 46
Who decided that everything in web browser is the right way? I for one say it's not. Don't touch my toys! ---

## Response 47
Add Support for "Virtual Interfaces"-MACVLAN-IPVLANMore infohttps://developers.redhat.com/blog/2018 ... networking+2, a little rediculous that RouterOS doesn't already have this. ---

## Response 48
Multiple Connection Marks and/or Packet MarksWould help a ton for people who want to use policy routingandQoS. As it is now, the number of connection marks you need is a cartesian product of (# of interfaces) X (# of things you want to QoS). For example, wan1-voip, wan2-voip, wan1-data, wan2-data, wan1-game, wan2-game, ...Maybe rename it from "marks" to "tags"?Or even just let me have 2 connection marks per connection.Or allow me to have one connection-mark and one... conn-queueing-mark or something.Or let me match by wildcard? connection-mark=wan1-* or connection-mark=*-data?Port ListsSimilar to/ip firewall address-listbut for ranges of TCP/UDP ports.It would be very handy to specify a list called "http" for instance, and make it contain 80, 443, and "ssh" containing 22, and "winbox" containing 8291, and then create a firewall raw rule that had something likeport-lists=http, ssh, winboxto target all the ports in those lists. I think it makes it more readable with friendly names, and hopefully would be just as performant as the current way of specifyingport=22, 80, 443, 8291.Fixthe initial normis postfor this threadHere normis says to email Mikrotik with your feature requests. Maybe that can be expressed in the original post? or the dead link removed? Just for folks who aren't aware that the page was taken down in 2014 and don't waste time looking for it? ---

## Response 49
Multiple Connection Marks and/or Packet MarksI agree with that! And I proposed it before, too.At some point it seemed that in RouterOS v7, things were going to change. Suddenly there was a max of like 256 different marks, suggesting that they had now split the 32-bit field that is used for this in Linux into 4 bytes for 4 separate marks.But the UI to put the marks in them has not appeared yet.In theory, with a max of 32 different marks, you could have each possible combination of them, and with 4 classes of 256 different marks, for purposes like you describe it would work well too.I guess they are busy with other things at the moment, but one time it could appear. ---

## Response 50
I'd like to suggest a dedicated "Feature requests" sub-forum. A sub-forum would allow one feature request per topic and discussion on this specific topic alone.Having all feature requests thrown into one thread is not helpful on discussion or working out details on a solution which would work for most peopl. It's also very cumbersome to follow up on a specific feature request.I would love to have a way address shortcomings / missing features though, but, and I apologize beforehand as I surely don't want to offend anybody, right now this thread looks a bit like a convolute of ideas where they let people play with ideas so that they don't bother support... ---

## Response 51
Feature request for Winbox(this is NOT a feature request for ROS)I suggest an updated version of Winbox that includes the Mikrotik btest.exe functions.Currently without this new feature:Winbox can only btest ( speedtest ) between any two Mikrotik devices.Currently , the btest results indicate nothing about how fast the Windows PC computer running Winbox is performng.With an updated Winbox with a built-in btest.exe ( btest speedtest ) function - you gain these new features & abilities:A Windows computer running Winbox can now btest ( speedtest ) from the Windows computer to a Mikrotik.These btest ( speedtest ) results would now indicate the users Windows computer network speed to the remote test Mikrotik device.*** Some background information to support this new feature request in Winbox:Most of the text below is from a posting I previously made in the forum section --> Public-Mikrotik-Bandwidth-Test-Server(s)When , you are using a Windows computer that is running a Windows Winbox program. Your Winbox is then controlling a Mikrotik ROS device ( router or switch ) - and your winbox has opened the btest functions on the Mikrotik ROS device.If/when you run a btest , you are speed testing ( btest ) the TCP and/or UDP throughput of your Mikrotik ( to another Mikrotik ROS device ). When the btest is running , the Mikrotik is performing the btest ( speedtest ) and the CPU on the Mikrotik is doing all of the work. Your Windows computer itself is not speed-testing anything.Here is an enviornment where a btest function in Winbox that is running on a Windows PC computer can provide much more useful information :- 1) You have a nice/new/very-fast Windows computer- 2 ) Your computer has a 10-Meg Ethernet connection ( or a wireless connection ) to your Mikrotik ROS router device- 3 ) Your Mikrotik ROS router device has a 10-Gig fiber link to another 2'nd Mikrotik ROS device* When your Windows PC computer running Winbox sends commands to btest between both of your Mikrotik devices , you should get very close to 10-Gig ( if both Mikrotik devices have a fast enough CPU ). This does not imply that your Windows computer can talk at 10-Gig.* If Winbox had a built-in btest function -- then you could btest ( using Winbox ) on your computer to either Mikrotik ROS device and you would get 10-Meg ( nothing faster ). So why only 10-Meg instead of 10-Gig ? --- Because you only have a 10-Meg Ethernet connection ( or wireless connection ) to the Mikrotik ROS device your PC computer is connected to.*** If you have multiple Windows PC computers/servers ( all running a Winbox with built-in btest functions ) , then you can btest ( speedtest ) from any of your Windows computers through your network(s) to another Windows PC computers/servers ( or Mikrotik ) and then get a better picture of how fast your network really is ( not just Mikrotik to Mikrotik ).***** If somebody can run 1 mile in 10 minutes ( Mikrotik btest to another Mikrotik ) , the speed that somebody can run has nothing to do with how fast you or I can run.(AKA - the current btest speedtest results do not indicate anything about how fast the Windows computer is performing)Currently , there is a Mikrotik btest.exe ( x86 based ) btest ( speedtest ) program that runs on a Windows computer. Few end-uses know anything or use this Mikrotik program and have never used it.I would think it would be somewhat easy to append the btest.exe x86 program/code to the end of the Winbox.exe x86 program/code ( combine both programs into one program ) , and then add some new/additional GUI buttons in Winbox which can then allow Winbox itself on the Windows computer to perform a btest ( speedtest )* It might also be desirable to hard-code limit the maximum time best can run ( 10 to 60 seconds ) , to prevent users from creating a sustained I/O saturation of their network(s)..Also - add a new GUI button in Winbox ( Check for Winbox updates ). The current method to update Winbox is semi-hidden and you have to know where to look to update Winbox.Does this sound like a good feature idea to everybody else ?North Idaho Tom Jones ---

## Response 52
Feature request for Winbox(this is NOT a feature request for ROS)I suggest an updated version of Winbox that includes the Mikrotik btest.exe functions.So if I understand this, you're suggesting winbox.exe "embed" btest.exe so it can be used without having to download it? And some UI to winbox that launch it as a window within (or outside) Winbox...It been long recommend to run btest's NOT from the router your testing & you're right, this would make that easier to do.That be useful since there isn't a btest.exe for Mac.... ---

## Response 53
Also - add a new GUI button in Winbox ( Check for Winbox updates ). The current method to update Winbox is semi-hidden and you have to know where to look to update Winbox.I used RouterOS/winbox for YEARS before I noticed winbox could update itself (e.g. it's ONLY in the initial "Discovery"/"Login" windows menus, NOT the main "session" window).I'd like this more automatic to check on launch if there is a new version and prompts to update. Dude essentially already does this today. With some "Enable/Disable Update Check" hidden in the menu. ---

## Response 54
North Idaho Tom JonesYou really care about your name, it's always the most prominent thing in each of your posts and it's repeated in a completely useless way, since it's also the nickname and on the avtar... ---

## Response 55
North Idaho Tom JonesYou really care about your name, it's always the most prominent thing in each of your posts and it's repeated in a completely useless way, since it's also the nickname and on the avtar...North Idaho Tom Jonesis that better ? ---

## Response 56
You couldn't wait to do it.What a narcissist… ---

## Response 57
North Idaho Tom JonesYou really care about your name, it's always the most prominent thing in each of your posts and it's repeated in a completely useless way, since it's also the nickname and on the avtar...I see that you as a moderator are attackingNorth Idaho Tom Jonesbecause he like to see his name prominently …I 41 like his sig … an attack of this nature is not becoming of a fine Italian person like yourself… ---

## Response 58
Thanks, but I didn't delete or edit his message...I got bored like all those who let appear "Sent from my device using Tapatalk" and similar repetitive message, but in his case he also gave him more emphasis than the whole topic...... ---

## Response 59
why this wiki pade have been removed ?Because exist this topic.... ---

## Response 60
One of the reasons I use "North Idaho Tom Jones" is that in the past when I simply use "Tom Jones" I will always get the following?"Do you sing ? ""Any relation ? ""I bet you wish you had his money ? ""Theeee Tom Jones ? ""Do you know him ? "... and about a million other repeating comments ...No , No, Yes, No, NoBest I can say is that I have actually had my checking account mixed up with his ( my paychecks going into his account. Also, I've had Las Vegas hotel reservations totally botched up and given keys to a luxury hotel room he would be using ( way way way way above my pay grade ).In this industry, you got to have a slightly sick twisted sense of humor and be able to survive light humorous criticism .North Idaho Tom Jones ---

## Response 61
All junk, your nick and your picture does not say Jones, only you are obsessed with adding it at the bottom, otherwise people would not even know. ---

## Response 62
SSTP AES hardware acceleration please!SSTP is the only standard protocol for Windows road warriors (but also can be used on other platforms with additional software) which works nearly anywhere. All other options like l2tp, ikev2, wireguard etc. are sometimes blocked in public or hotel networks.Now we have pretty poor speeds and high cpu load with sstp on Mikrotik. ---

## Response 63
All junk, your nick and your picture does not say Jones, only you are obsessed with adding it at the bottom, otherwise people would not even know.what does it bother you?does it hurt someone?way less offensive than many of your posts anyways. just leave it be, fgs ---

## Response 64
I already wrote it a little while ago, just re-read.I feel it is useless to continue the discussion. ---

## Response 65
I feel it is useless...Like so many of your posts. No wonder your mod powers were revoked. You've contributed nothing to this thread today other than to attack someone. Now I've contributed negatively as well but after watching your interactions with forum users over the past year or so I finally cracked. If you are going to just take pot shots at others please STFU. ---

## Response 66
Re: Feature requests (AP log connection nv2 signal strength)Years ago , Mikrotik added the ability for an AP to log " connected, signal strength " when a client connects to an AP.Below is a log example of Mikrotik AP logs AP using thewireless Protocol: 802.11 :mar/02 09:04:31 wireless, info A6:CE:45:00:11:93@wlan1: disconnected, registered to other interface, signal strength -62mar/02 09:25:37 wireless, info A6:CE:45:00:11:93@wlan2: disconnected, extensive data loss, signal strength -62mar/02 11:33:54 wireless, info A6:CE:45:00:11:93@wlan2: connected, signal strength -73mar/02 11:34:15 wireless, info A6:CE:45:00:11:93@wlan2: disconnected, received disassoc: sending station leaving (8), signal strength -73mar/02 11:34:16 wireless, info A6:CE:45:00:11:93@wlan2: connected, signal strength -63However , a Mikrotik AP using thewireless Protocol: nv2does not have this AP logging feature.Example below:mar/01 10:21:27 wireless, info B8:69:F4:E5:30:49@wlan1: connectedmar/01 12:54:30 wireless, info 6C:3B:6B:DF:16:04@wlan1: connectedmar/01 12:54:31 wireless, info 6C:3B:6B:0E:5E:61@wlan1: connectedmar/01 12:54:32 wireless, info B8:69:F4:E5:30:B8@wlan1: connectedI would like to suggest that Mikrotik add this logging feature into APs using nv2.Background supporting information for this feature request:- The current AP Registration table that shows the current Tx/Rx Signal Strength has little relation to the original connection Tx/Rx Signal Strength when the client first connected.- A wireless Client device will normally connect to an AP using a lower/slower connection rate. At slower connection rates , wireless cards almost always have a higher transmit power and a better more sensitive receive capability. At the initial wireless connection, both the AP and the Client will have better stronger signal strength for both tx and rx and a slower connection rate.- After a Client is connected to an AP , both the Client and the AP connection rates will begin to up-shift to the fastest stable connection rates the wireless link can communicate at. Almost all wireless cards have a lower transmit power at faster connection rates -and- also have lesser receive sensivity at faster connection rates. Thus , the original signal connection strength can easily be 15-dB to 27-dB stronger or more than the current Registration table shows.Here is a partial example of the wireless specifications for a 5-GHz DISC Lite5 :Connect rate Transmit (dBm) Receive Sensitivity6MBit/s 25 -96MCS7 19 -75After the initial wireless connection at 6MBit/s and after the connection has rate upshifted to MCS7 , the transmit power on the AP and client have both gone down by 6 dBm and the receive sensitivity on the AP and the client have both gone down by 21 dB.Thus , an original connection strength may of actually been +27 dB stronger in both directions than what the Registration shows.This information should be logged when an AP is configured to use Access-List Signal-Strength-Range setting ( strength required to connected and signal strength to force a disconnect ). If/when these settings are incorrectly configured , you can easily have your wireless clients connecting and disconnecting over and over again and repeating this loop forever. Hense - the reason a logging of wireless nv2 connection strengths is needed.NorthIdahoTom Joneslol ---

## Response 67
It would be great to implement a ``routing table lookup'' . it is described in the WIKI, but there is no way to use it.https://help.mikrotik.com/docs/display/ROS/IP+RoutingIN Extreme XOS thehe is this feature.Screenshot_1.pngScreenshot_3.png ---

## Response 68
It would be great to implement a ``routing table lookup'' . it is described in the WIKI, but there is no way to use it.https://help.mikrotik.com/docs/display/ROS/IP+RoutingIn V6 there was /ip/route/check that gave a definitive routing result, but V7 removed it. Seeviewtopic.php?t=164150&hilit=route+checkI too like to see that back (or similar), it was a quick way to know your routing tabling was doing what you'd expect. ---

## Response 69
It would be great to implement a ``routing table lookup'' . it is described in the WIKI, but there is no way to use it.https://help.mikrotik.com/docs/display/ROS/IP+RoutingIn V6 there was /ip/route/check that gave a definitive routing result, but V7 removed it. Seeviewtopic.php?t=164150&hilit=route+checkI too like to see that back (or similar), it was a quick way to know your routing tabling was doing what you'd expect.yes, it can be used in version 6, but I want a better implementation, and to see which route is active. ---

## Response 70
NorthIdahoTom JoneslolFinally someone with just spirit....@gabacho4 calm down, it was already over there, it's normal to disagree or send yourself to hell, I'm not the hypocrite of the moment who gets along with everyone just to please.Continuing to continue to continue is useless. ---

## Response 71
IPv6 Fasttrack support, please ---

## Response 72
hello, i would like to request dynamic queues like dhcp for dot1x.so every devices connected will create dynamic queues according to the parameter given on radius.do not forget others parameter like insert before, parent queues, etccheersP ---

## Response 73
hello, i would like to request dynamic queues like dhcp for dot1x.so every devices connected will create dynamic queues according to the parameter given on radius.do not forget others parameter like insert before, parent queues, etccheersP+1 for this one. ---

## Response 74
consoleIt would be useful if "add" command (in all menus) return to script id of created entry.Sorry, my mistake, add already returned )) ---

## Response 75
OOB interface:> IPMI/Redfish - management (no more "Netinstall")https://www.dmtf.org/standards/redfish ---

## Response 76
Hello, Feature request:Add button to log entry so one can create firewall rule to remote address.Log is seen by admin to reveal some undesired activity. Copypasting is time consuming.Consider adding a button which will call New Firewall rule, with pre-filled IP from Log entry. This is supposed to improve usability.Thanks. ---

## Response 77
Hello, Feature request:Add button to log entry so one can create firewall rule to remote address.Log is seen by admin to reveal some undesired activity. Copypasting is time consuming.Consider adding a button which will call New Firewall rule, with pre-filled IP from Log entry. This is supposed to improve usability.Thanks.FYI - PfSense has this feature, and it works well - The feature you are asking for might be very useful in Mikrotik ROSNorth Idaho Tom Jones ---

## Response 78
1) Why leave SSH open to the world (these are the consequences, if notalso attract DDoS attacks),2) Why don't you already have a script that blacklists the IP after the second failed attempt in not even 4 seconds? ---

## Response 79
Log is seen by admin to reveal some undesired activity. Copypasting is time consuming.Consider adding a button which will call New Firewall rule, with pre-filled IP from Log entry. This is supposed to improve usability.Of course you would not want to make a "new firewall rule" for that!First learn a bit more about firewall rules. To block random IP addresses, make a SINGLE rule that blocks some traffic referencing an "address list".Then put the address you want to block in the address list. You can add many addresses in the address list and they will all be blocked by a single rule. Better for CPU usage!Also, you can have a timeout on an address list entry, so it automatically gets removed after some time.And of course, what you want is already possible! You can write a script that reads the log, finds messages like the above, extracts the address from it and adds it to the address list.No new feature required for that. ---

## Response 80
Thanksrextended&pe1chl, the script idea looks reasonable. Will consider this. ---

## Response 81
Request scripting feature.Modify commands:local <name> <value>:global <name> <value>to make it possible set <name> from other variable.also add $$ construction for access to such dynamically-named vars.Example::local varname "newVar";:local $varname "test";:put $newVar;test:put $$varname;test ---

## Response 82
I don't think it's a matter of implementing useless things or not, but a question ofknowing how to use what already exists...Example::local varname "newVar";:local $varname "test";:put $newVar;<<== this do not have any logic, if you already know the varname inside the script, no need to create it dinamicallytest:put $$varname;testworking example code{ :local localvars [:toarray ""] :local varname "newVar" :set ($localvars->$varname) "test" :put ($localvars->"newVar") ; # the same as on previous comment, is illogic, but for example... # previous :put wire "test" on terminal :put ($localvars->$varname) # previous :put write "test" on terminal :local testip "newipvar" :set ($localvars->$testip) 127.0.0.1 :put "Local variable $testip value is $($localvars->$testip) and the type is $[:typeof ($localvars->$testip)]" # previous :put write "Local variable newipvar value is 127.0.0.1 and the type is ip" on terminal }And if the variable must be global, just create
```
:global globalvars [:toarray ""]etc.Or use another method:viewtopic.php?f=9&t=178435&p=879152#p879152

---
```

## Response 83
knowing how to use what already existsAll this examples i understand and i know how to use it.Feature request desire to simplify a lot of work. ---

## Response 84
Simplifya lot of work?I would say it is just a niche case that is mainly a trick, and associative arrays (as in the example by rextended) are the proper way to do what you want.Sure there are some things that can be improved in the scripting language, and especially in its parser, but I don't consider this one of them. ---

## Response 85
[…] there are some things that can be improved in the scripting language […]For example, decimal division...RouterOS: 3 / 2 = 1 must be done (3 * 1000) / 2 = 1500, then split the string "1" + "," + "500" and remove last zeros at the end... ---

## Response 86
For me, the most important is to add a BNF definition of the language and make the parser adhere to it.I have found many times that when combining various constructs that each are supported into a complicated expression, it does not work.You need to break up complicated expressions into various steps. In a decent language that is not required, anything derived from the simple examples goes when combined in a complicated expression. ---

## Response 87
For me, the most important is to add a BNF definition of the language and make the parser adhere to it.Not BNF, but there is a "table" of the syntax in /console/inspect
```
/console/inspect input=":put \$" request=completion 

Columns: TYPE, COMPLETION, STYLE, OFFSET, PREFERENCE, SHOW, TEXT
TYPE        C  STYLE        O  PR  SH  TEXT                         
completion  [  syntax-meta  6  75  no  start of command substitution
completion  (  syntax-meta  6  75  no  start of expression          
completion  $  syntax-meta  6  75  no  substitution                 
completion  "  syntax-meta  6  75  no  start of quoted string
```

```
/console/inspect request=syntax 

Columns: TYPE, SYMBOL, SYMBOL-TYPE, NESTED, NONORM, TEXT
TYPE    SYMBOL         SYMBOL-TYPE  N  NONORM  TEXT                                                                    
syntax                 collection   0  yes                                                                             
syntax  beep           explanation  1  no                                                                              
syntax  blink          explanation  1  no                                                                              
syntax  certificate    explanation  1  no      Certificate managementIt'sturtlestables all the way down.

---
```

## Response 88
The problem is that there is no BNF definition of the language that corresponds with the behavior of the parser.So you cannot make arbitrarily complex nested expressions that would be valid in almost any language. At some point it just issues an error.And of course, the indication and handling of errors also leaves a lot to be desired... ---

## Response 89
Please add syntax error / bad command messages into log file (same messages when commands are executed from terminal likebad command name egdfg (line 2 column 1)) for uploaded autorun script (<something>.auto.rsc), into"<something>.auto.log"or"<something>.auto.err"if.logfile is meant to be only for successful execution.I'm trying to create IDE (VSCode) task configuration which uploads working script over SFTP and reads output from log file or error over SSH, but I'm unable to catch error for exact executed script, it is not possible to exactly match script error log with that uploaded script execution (ex. if other script is executed with error in that time) but it will possible if is error logged into file with same basename. ---

## Response 90
Please add sstp - authentication process using EC digital signature ---

## Response 91
Greetings. The feature request I recommend is that the host used to detect the Internet in interface/detect-internet can be customized to any other host (domain or IP). ---

## Response 92
[FEATURE REQUEST]- Firewall History Logcould it be possible to implement a firewall connections log (a seperate TAB for example directly in the ip>firewall window/section)?with maybe some settings like "max-conn-count", "max-lines" and/or "max-history-timeframe" (which could define for how long it is possible to look back)something like CHECKPOINT or BARRACUDA NG Firewalls do have.cheers ---

## Response 93
You can create that yourself by adding the proper /system logging definition... ---

## Response 94
When adding a bridge filter to a vlan-filtering bridge, it would be nice when you could specify the VLAN id AND the MAC protocol.As it is now, when you filter on a VLAN id you cannot filter on any other MAC protocol.I would like to filter "ARP on VLAN 2", for example. So I want to specify MAC protocol ARP and at the same time VLAN id 2.(of course the filter would match on the string of MAC protocol 8100, VLAN 2, MAC protocol ARP) ---

## Response 95
Bridge filter rules have limited matching options for L3, L4 headers when a packet is VLAN-tagged (contrary to switch ACL rules). But there is a special "vlan-encap" matcher that will look for MAC protocol.
```
/interface bridge filter
add chain=forward mac-protocol=vlan vlan-encap=arp vlan-id=2

---
```

## Response 96
Now the 4096 byte limit on variables is lifted and variables are now limited by the amount of available memory.https://help.mikrotik.com/docs/pages/di ... ersions=28:too fetch is still limited to 64512 bytes when using user->data and it then depends to the target server supporting chunked transfers. My request is to able to also read download larger than 64512 bytes directly into a variable.To avoid stuff more data into a variable/internal memory a check could be done in advance with: [/tool fetch url=$url keep-result=no as-value] or have an extra parameter indicating the expected amount of data to be stored. So that a unintended big download does not bring the router in any problems.This could be automatic like ((available memory / 3) * 2) limiting to 2/3 of available memory to be used by one variable.Preferred or even enforced is using :local for big variables over/instead of :global. ---

## Response 97
Second request on bigger variables.Using fetch I can write a bigger file to disk in one go. But then I can't read those back when the file is bigger than 4KB, despite the variable in not a limiting factor anymore in ROS.This could be first one, so the request above for direct download in variable can be done on a later moment. Then a work around situation is created by first saving to disk and then read the file back to a variable.https://help.mikrotik.com/docs/display/ ... remotehostThere is stated that the limit for variables is still 4KB and that is limiting reading the file. ---

## Response 98
Bridge filter rules have limited matching options for L3, L4 headers when a packet is VLAN-tagged (contrary to switch ACL rules). But there is a special "vlan-encap" matcher that will look for MAC protocol.
```
/interface bridge filter
add chain=forward mac-protocol=vlan vlan-encap=arp vlan-id=2Ok thanks!  I saw that vlan-encap parameter but I mistakenly assumed that it would select the type of vlan encapsulation...Unfortunately, when configuring it like that, it does not allow filtering on the ARP parameters as it does when mac-protocol=arpIs that a bug or is it just impossible to implement?

---
```

## Response 99
Right, the arp-* matchers require mac-protocol=arp/rarp to be set. I believe it is a bridge filter (ebtables) limitation. ---

## Response 100
Pity... now I still need to have a dummy bridge on the VLAN CPU port on the main bridge. Then I might as well drop the entire VLAN filtering bridge on this config (it is the one where I tried to hw offload the bonding interface)...On to the next (unrelated) feature request:I would like to see an option in /routing/table to have connected routes automatically added to a user-created routing table.Ideally it would be a pulldown selector similar to what is in the firewall for "interface list", where you can select "none" (default), "all", or a user-defined interface list. But when that is impossible, just a checkmark to enable this (for all interfaces) would be nice as well.This function will put "C" routes (as seen in table "main") into the user-created table as well.I think it is already available in VRF, but VRF is often too restrictive for what I want to do (overlay networks, balance/failover between ISPs, etc). ---

## Response 101
The "Input accept NLRI" filtering in BGP would be more usable when there is an extra "accept default route" option.As it is now, you can accept prefixes in certain subnets (as present in the address-list parameter of "Input accept NLRI"), but once you want to accept the 0.0.0.0/0 route, everything is accepted. It would be great when you could accept some networks in the address-list, and not the networks outside that, but still accept the default route. ---

## Response 102
The "Input accept NLRI" filtering in BGP would be more usable when there is an extra "accept default route" option.As it is now, you can accept prefixes in certain subnets (as present in the address-list parameter of "Input accept NLRI"), but once you want to accept the 0.0.0.0/0 route, everything is accepted. It would be great when you could accept some networks in the address-list, and not the networks outside that, but still accept the default route.+1 for that.would be really useful ---

## Response 103
bump for RFC 2439 / route dampening ---

## Response 104
I understand the need to restart interfaces/processes/policies/etc. on change, but it is possible to exclude Comments field from this rule? They does not affect the actual configuration of the item in any way.It's a bit annoying if I want to change a comment for IPsec Policy or Netwatch Host and the item turns off and on again, causing connection reset / execution of Up/Down scripts etc... ---

## Response 105
Please add sstp - authentication process using EC digital signatureAlso updating ciphers available for MT SSTP server would be a good idea, because the only ones offered now are TLS_RSA_WITH_RC4_128_SHA and TLS_RSA_WITH_AES_256_CBC_SHA ---

## Response 106
Some Winbox related requests from me:#1 I often use Winbox to support IOT devices behind a firewall. Access is based on Telnet or SSH using Tools->Telnet menu access. If this menu option could be accessed from the DHCP Server->Leases screen, possibly using Right click with the device highlighted it would save a LOT of time.#2 Certain operations such as a firmware upgrade cause the device to reboot and the connection to be Disconnected. If a "Reconnect" option (or better keyboard shortcut) can be added to automatically reconnect using same protocol and credentials it would be wonderful.#3 Ability to hide/remove certain columns from some of the screens would be wonderful. This will allow support staff to reduce the clutter by having fewer but relevant columns displayed on some mobile devices such as small laptops.#4 If the above custom configuration can be saved as part of a user profile this will be wonderful and save time having to remove the same columns again. ---

## Response 107
#3 Ability to hide/remove certain columns from some of the screens would be wonderful. This will allow support staff to reduce the clutter by having fewer but relevant columns displayed on some mobile devices such as small laptops.#4 If the above custom configuration can be saved as part of a user profile this will be wonderful and save time having to remove the same columns again.This has been available for ages! You need to click the small triangle at the rightmost edge of the column titles and use "show columns".This is also saved to the profile for that router when you click "session->save" or have "session->autosave on close" enabled and neatly close the session.(does not save when you lose the network connection e.g. because the router reboots) ---

## Response 108
Ability to choose specific archive version in packages to downgrade/upgrade to.RouterOS stable versions have proved to be unstable regularly. Having the option to just choose a version to install will be very helpful on devices with small flash storage where you can't just drop the file in and reboot. ---

## Response 109
Sure the System->Packages menu could have some very simple improvements! Not only selection of a version, but also selection of packages to install.The packages are available from the update server, so why do we have to download them on a computer, finding the correct architecture, unzip the file, upload the npk to the router? There could be an Install button that shows the packages available for the installed version, and download and add one. ---

## Response 110
#3 Ability to hide/remove certain columns from some of the screens would be wonderful. This will allow support staff to reduce the clutter by having fewer but relevant columns displayed on some mobile devices such as small laptops.#4 If the above custom configuration can be saved as part of a user profile this will be wonderful and save time having to remove the same columns again.This has been available for ages! You need to click the small triangle at the rightmost edge of the column titles and use "show columns".This is also saved to the profile for that router when you click "session->save" or have "session->autosave on close" enabled and neatly close the session.(does not save when you lose the network connection e.g. because the router reboots)Thanks, havent seen the right most side because we have always reduced the size of windows to fit in.... ---

## Response 111
And another (much repeated request) for a NATIVE MacOS Winbox version. Currently have to start VMWare Fusion just to start Winbox.... ---

## Response 112
Sure the System->Packages menu could have some very simple improvements! Not only selection of a version, but also selection of packages to install.100% agree. It comes up when a "stable" release isn't actually "stable" for a particular configuration/router/hardware/whatever. "Rollback" to another version is quite tedious/manual & requires a good how understanding of package management. e.g. you have to align the specific packages previously installed to manually copy the same set of "extra-packages" & knowledge of the "file copy" method of upgrade in first place. ---

## Response 113
And another (much repeated request) for a NATIVE MacOS Winbox version. Currently have to start VMWare Fusion just to start Winbox....I use a Mac, just use wine, it works "natively enough". Now they should release a 64-bit Dude, because there you do need Fusion (or similar VM), which is annoying.IMO Mikrotik should focus on fixing these little things, not worrying about multi-platform clients. And if they made their iOS app more functional, it work on newer Macs. ---

## Response 114
And another (much repeated request) for a NATIVE MacOS Winbox version. Currently have to start VMWare Fusion just to start Winbox....WinBox works perfectly under CrossOver for ages, you do not need virtualisation software to run it. ---

## Response 115
Pity... now I still need to have a dummy bridge on the VLAN CPU port on the main bridge. Then I might as well drop the entire VLAN filtering bridge on this config (it is the one where I tried to hw offload the bonding interface)...On to the next (unrelated) feature request:I would like to see an option in /routing/table to have connected routes automatically added to a user-created routing table.Ideally it would be a pulldown selector similar to what is in the firewall for "interface list", where you can select "none" (default), "all", or a user-defined interface list. But when that is impossible, just a checkmark to enable this (for all interfaces) would be nice as well.This function will put "C" routes (as seen in table "main") into the user-created table as well.I think it is already available in VRF, but VRF is often too restrictive for what I want to do (overlay networks, balance/failover between ISPs, etc).+1 to this!!automatically add local routes to additional route tables ---

## Response 116
I need either shadow socks or some kind of obfuscated vpn protocol (v2ray, vless, xtls reality, etc...).Shadow socks seems to me more preferable, as it operates separately tcp-tcp , udp-udp, plus socks5 already in ROS.UNFORTUNATELY nowdays most if restictions cannot be resolved with wireguard/ipsec, as these protocols are blocked easily and effectively. ---

## Response 117
It would be really nice if MikroTik would add the ability to graph health information such as voltage and temperature and no I'm not referring about SNMP and API, I am referring to tools->graphing, the same way as resources, queues and interfaces are graphed.Yes please. With RouterOS 6 this could be managed with scripts and email, but I've yet to find a way to get a report of a router's voltage health for the duration of a day on RouterOS 7. ---

## Response 118
IMO - if you want to graph your network , consider using something like Cacti, or Zabbix , or LibreNMS ( or any other Network Monitoring software ).I prefer a fast non-bloated switch/router that is not also using disk space or cpu processes or memory processes to capture and store graph into.Then you can also keep your graphs much longer ( years or more ) on everything ( cpu, mem, I/O throughput , voltages , temperature , connected users ... and/or anything your switch/router will allow your NMS system to SNMP read.Normally , on a Mikrotik , I disable/turn-off all graphing to avoid tasking the CPU , consuming flash disk space to get the maximum throughput performance possible.North Idaho Tom Jones ---

## Response 119
What is the current correct way to submit feature requests to Mikrotik? ---

## Response 120
Make a ticket on the customer support portal athttps://help.mikrotik.com/servicedesk ---

## Response 121
I stumbled upon "cannot run, not enough permissions." error while trying to run script from scheduler (MT 6.48.6). For years is worked fine and it seems with some upgrade it stopped working as something with permissions was changed.While searching for a solution, I found out numerous issues reporting with NetWatch. People were unaware WHAT permissions are needed for script to be executable by NetWatch.I resolved an issue. In my case I had to allow all permissions but romon and dude to both schedule and script to make it work. with less permission, although it was the same for schedule and script, it still reported permission error, but not what permission is required and missing.I have a feature suggestion: When permission error is reported, post what exact permissions are not fulfilled. It would really help finding issue in quicker and easier manner, and with less frustration. ---

## Response 122
When creating a GRE tunnel using IPsecret - the dynamically created IPsec peer uses exchange mode MAIN. It would be great if there was a way for the dynamic peer to use IKEv2 (without having to manually create the peer and identity under IPsec) ---

## Response 123
+1! It would be great to be able to select a profile other than default (but I see exchange mode is not part of the profile)It would be great when these settings would be moved into the profile, e.g. also "passive". ---

## Response 124
+1! It would be great to be able to select a profile other than default (but I see exchange mode is not part of the profile)It would be great when these settings would be moved into the profile, e.g. also "passive".how would you like to move phase1 settings to phase2 around or vice-versa? ---

## Response 125
We needwildcard searching(*) in address-list searches:[xxxxx@yyyyy] /ip firewall address-list> add list=TEST address=192.168.128.3[xxxxx@yyyyy] /ip firewall address-list> add list=TEST address=192.168.128.0/24[xxxxx@yyyyy] /ip firewall address-list> print where address=192.168.128.*Flags: X - disabled, D - dynamic# LIST ADDRESS CREATION-TIME TIMEOUT ---

## Response 126
+1! It would be great to be able to select a profile other than default (but I see exchange mode is not part of the profile)It would be great when these settings would be moved into the profile, e.g. also "passive".how would you like to move phase1 settings to phase2 around or vice-versa?No need for that. I would (like the other request) just want to specify an initial phase1 profile. ---

## Response 127
We needwildcard searching(*) in address-list searches:[xxxxx@yyyyy] /ip firewall address-list> add list=TEST address=192.168.128.3[xxxxx@yyyyy] /ip firewall address-list> add list=TEST address=192.168.128.0/24[xxxxx@yyyyy] /ip firewall address-list> print where address=192.168.128.*Flags: X - disabled, D - dynamic# LIST ADDRESS CREATION-TIME TIMEOUTThis has been asked several times before by people who do not realize that it already exists.print where address in 192.168.128.0/24 ---

## Response 128
We needwildcard searching(*) in address-list searches:[xxxxx@yyyyy] /ip firewall address-list> add list=TEST address=192.168.128.3[xxxxx@yyyyy] /ip firewall address-list> add list=TEST address=192.168.128.0/24[xxxxx@yyyyy] /ip firewall address-list> print where address=192.168.128.*Flags: X - disabled, D - dynamic# LIST ADDRESS CREATION-TIME TIMEOUTThis has been asked several times before by people who do not realize that it already exists.print where address in 192.168.128.0/24Ah, cool!Should be added into the documentation.BUT: what about wildcard searching after domain names in such address lists, for example searching all related to "google", ie. "*google*" ? ---

## Response 129
This has been asked several times before by people who do not realize that it already exists.print where address in 192.168.128.0/24Ah, cool!Should be added into the documentation.You should read the documentation. Is already present, on both old and new.https://wiki.mikrotik.com/wiki/Manual:S ... _Operatorshttps://help.mikrotik.com/docs/display/ ... lOperatorsThe documentation cannot provide all the examples of what can be done with scripting.Simply (of what) it says1+1=2, then(4 * 6 + 2 - 7 / 22) = 26you have to do it yourself... ---

## Response 130
Added during previous reply:BUT: what about wildcard searching after domain names in such address lists, for example searching all related to "google", ie. "*google*" ?literallywhere address have inside "google" on any point(literally is not one script instruction)/ip firewall address-list print where address~"google"Still you do not read the already available documentation....https://wiki.mikrotik.com/wiki/Manual:S ... _Operatorshttps://help.mikrotik.com/docs/display/ ... rOperatorsSo your "Feature requests" would be: "Someone read the documentation for me"... ---

## Response 131
In conclusion, for this:[xxxxx@yyyyy] /ip firewall address-list> print where address=192.168.128.*The correct way is to use "in" but forparagonable/regex syntax is:/ip firewall address-list print where address~"^192\\.168\\.128\\.*" ---

## Response 132
The GRE IPSec profile suggestion is good one. Never thought about this approach:When creating a GRE tunnel using IPsecret - the dynamically created IPsec peer uses exchange mode MAIN. It would be great if there was a way for the dynamic peer to use IKEv2 (without having to manually create the peer and identity under IPsec)+1! It would be great to be able to select a profile other than default (but I see exchange mode is not part of the profile)It would be great when these settings would be moved into the profile, e.g. also "passive".+1 too. The "Use IPSec" checkbox is so handy, just limited today – a profile selector be useful .I just add equally or more useful on EoIP too. ---

## Response 133
Why is this then not working?
```
[xxxxx@yyyyy] /ip firewall address-list> print where list=TEST
Flags: X - disabled, D - dynamic 
 #   LIST                                                         ADDRESS                                                                           CREATION-TIME        TIMEOUT             
 0   TEST                                                         play.google.com                                                                   nov/03/2023 15:43:46
 1 D ;;; play.google.com
     TEST                                                         172.217.16.78                                                                     nov/03/2023 16:28:30
 2   TEST                                                         www.google.com                                                                    nov/03/2023 16:52:02
 3 D ;;; www.google.com
     TEST                                                         142.250.181.196                                                                   nov/03/2023 16:52:02

[xxxxx@yyyyy] /ip firewall address-list> print where address~"*google*"                  
Flags: X - disabled, D - dynamic 
 #   LIST                                                         ADDRESS                                                                           CREATION-TIME        TIMEOUT             
[xxxxx@yyyyy] /ip firewall address-list>because you did not read the documentation and the examples above.  *google* is not a valid regexp.

---
```

## Response 134
+1 too. The "Use IPSec" checkbox is so handy, just limited today – a profile selector be useful .I just add equally or more useful on EoIP too.Yes, of course when that is implemented for GRE/IPsec it should be added for *all* cases where automatic IPsec config is possible.(IPIP/IPsec, EoIP/IPsec, L2TP server, L2TP client) ---

## Response 135
how would you like to move phase1 settings to phase2 around or vice-versa?No need for that. I would (like the other request) just want to specify an initial phase1 profile.oh sorry, misunderstoodgot it. indeed would be favourable ---

## Response 136
Add Support for "Virtual Interfaces"-MACVLAN-IPVLANMore infohttps://developers.redhat.com/blog/2018 ... networking+2, a little rediculous that RouterOS doesn't already have this.FinallyWhat's new in 7.12rc1 (2023-Oct-05 08:46):*) interface - added "macvlan" interface support; ---

## Response 137
Feature request:- SOC/ASIC Hardware accelerated multi-bridge/interface support(example: Microchip SparX-5 / Marvell OCTEON TX2 CN9670 + RouterOS) ---

## Response 138
I've ask support to modify ssh public keys (/user/ssh-keys) to expose a read-only property with the key's fingerprint (SUP-132909). Actually public key authentication works quite well, but there is no way to verify that a key is the one you expect it to be.Imagine you import a certificate "ISRG Root X1" to verify websites, but there is no way to verify its fingerprint, which should be "96bcec06264976f37460779acf28c5a7cfe8a3c0aae11a8ffcee05c0bddf08c6". Pretty bad, no?Support answered:If there will be more requests, we will consider implementing this feature.So if you think this is useful (or even mandatory) please open your own request! ---

## Response 139
Winbox Feature RequestInContainerwhen using copy put the "tag" value into the "remote-image" field. so you can effectively duplicate the entry when required.allow to use a log prefix to easily identify which container is actually reporting the thing to the longInIP / FirewallAdd the "log_prefix" as the "comment" to the "add ___ to address list" action. This would help tracking which firewall rule added the address to the list and could potentionally reduce the number of lists. For instance there would be no need for an ssh_stage# list and a winbox_stage# list if I could just use stage# and now where each address got added from.InFilesCollapsible folders ---

## Response 140
Add select kernel congestion to bbrafter container is stable, router os has can take more service function in network. It's worth to support BBR congestion control for internal service such as VPN, storage, although it has no effect as a switch or router. ---

## Response 141
Winbox Feature RequestInContainerwhen using copy put the "tag" value into the "remote-image" field. so you can effectively duplicate the entry when required.allow to use a log prefix to easily identify which container is actually reporting the thing to the long+10InFilesCollapsible folders+1 ---

## Response 142
InContainerwhen using copy put the "tag" value into the "remote-image" field. so you can effectively duplicate the entry when required.+10I filled a feature request bug a couple months ago (SUP-128652) on copy problemand that it :export doesn't actually create a usable "/container add" with remote-image= set. ---

## Response 143
SSTP AES hardware acceleration please!SSTP is the only standard protocol for Windows road warriors (but also can be used on other platforms with additional software) which works nearly anywhere. All other options like l2tp, ikev2, wireguard etc. are sometimes blocked in public or hotel networks.Now we have pretty poor speeds and high cpu load with sstp on Mikrotik.Totally agree!Hardware acceleration for sstp is very much needed. ---

## Response 144
SSTP AES hardware acceleration please!SSTP is the only standard protocol for Windows road warriors (but also can be used on other platforms with additional software) which works nearly anywhere. All other options like l2tp, ikev2, wireguard etc. are sometimes blocked in public or hotel networks.Now we have pretty poor speeds and high cpu load with sstp on Mikrotik.would help implementing standard windows clients by a LOT ---

## Response 145
Wouldn't it be cool to have signal strength graph in the Wi-Fi Registration table like in Quick Set?Having that column one can easily identify problem clients at a glance.Signal Strength Graph - Quick Set.pngSignal Strength Graph - Registration.png ---

## Response 146
Please implement non persistent (no flash write) change configuration possibility. This could be implemented through some global command like
```
:nonpersistent do={ ... }any command that is performed inside that command context block should not persist change in configuration.Some practical usages:disabling/enabling interfaces or VPN servers to force reconnect used by netwatch or schedulersany short interval configuration change in loop where persistence is not needed, like LED light show script that turns on/off different leds in short intervals (it is possible on some routers), I know router is not Christmas tree, but it could be used for presentation, eg. on stores shelfBenefits:reduced flash writesavoiding possible edge case scenario when netwatch script disables WAN (internet connection) interface to force reconnect (eg. lte) and while it's disabled power loss occurred, on next boot, because of persistence, internet connection is no longer available and can be an issue if user is not at home and wants to use for eg. BTH VPN - this is solvable with additional startup script that checks enabled states of interfaces, VPN servers, etc., but it just complicates things where it could be simpler with non persistent commands

---
```

## Response 147
Export with "show-sensitive" to include users and their hashed passwords. Also the ability to import users and include pre-hashed passwords. ---

## Response 148
Export with "show-sensitive" to include users and their hashed passwords. Also the ability to import users and include pre-hashed passwords.YES! The export should be expanded to (at least optionally) include all of the configuration, including users, certificates etc. ---

## Response 149
Please make IKEv2 roadwarrior split-include functionality actually interwork with other people's software.As it is now, it only works with other MikroTik devices. Standard IKEv2 client software only gets the first split-include entry, not further entries (i.e. you can route only a single local network using this mechanism). ---

## Response 150
Ability to color the winbox header differently per device type. Or somehow allow the changing of the color and keep it persistant once changed..This would allow me to make sure I don't "grab" the wrong window when I have 20 of them open and make a change in the wrong one. ie, green for cpe's, red for core devices, etc... ---

## Response 151
extended logging for scripts etc, with ability to specify the topiclike this
```
/log/write topic=script,info message="Doing fine!"and to create a user defined topic
```

```
/system/logging/add topics=my-scripts action=memory

---
```

## Response 152
script errors (syntax, runtime) must be notified somehowwith a log message I suppose ---

## Response 153
Winbox: I am requesting automatic window tiling like done in linux tiling window managers. Not as feature blown but at least some control over the window-sizes and the split mode (horizontal/vertical).I am disgusted by the floating alignment of the windows as it is now. I am aligning and resizing windows so I am fine with it. But want to add another window? Hell no. Resizing again. It is a real pita. ---

## Response 154
Use session / windows layout:viewtopic.php?t=203402 ---

## Response 155
Busy cat this morning, check emails ;-PWhen you do perhaps give me a hint on how to use sessions windows or why it would be good for me. ---

## Response 156
(done)give me a hint on how to use sessions windows or why it would be good for me.Just for memorize windows positions, colum size, colum order, filed present on colums and tab open... ---

## Response 157
@normis please checkviewtopic.php?p=1049302 ---

## Response 158
Use session / windows layout:viewtopic.php?t=203402Yes, but I still have to fiddle around with sizing the windows inside winbox. "Right-click -> auto-layout windows" I am aiming for. ---

## Response 159
Well, I would not know how it could meaningfully auto-layout different windows with a so much varying content and optimal size...For a window with "IP addresses" or many other similar windows you can use a tiny window. For something like routes or firewall you need a much larger window.And, I always put "log" as a full-size window as a backdrop of all other windows, so that I can keep an eye on what is being logged. ---

## Response 160
It would be great if this is implemented.viewtopic.php?p=1050972 ---

## Response 161
Feature requests - CHR on Bare Metal for faster Network throughputNote:This topic is about achieving very fast network/Ethernet throughput( as in 10-Gig and faster network routing throughput)I would like to see a CHR that can be installed on a Bare Metal server.Here is my reasoning and justification why I would like to see a CHR that can be installed on a Bare Metal server.Mikrotik's CHR ROS runs on a Hypervisor ( such as VmWare or ... ). This is a 64-Bit operating system and also does not have the ability to be directly installed on a Bare Metal computer/serverthus:- CHR , does not run on Bare Metal- CHR , no install ISO ( or any procedure ) to install CHR on a Bare Metal computer- CHR , can be installed as a 64-bit operating system in many Hypervisor environmentsMikrotik's x86 ROS can be installed on most Bare Metal computers and under most Hypervisor environments. However, x86 ROS is a 32-Bit operating system.-When a virtual CHR sends an Ethernet packet out through the virtual Ethernet interface, the packet is first delivered to the Hypervisor virtual vSwitch , which will always require at least one ( 1 ) physical CPU clock-cycle - thus so far , the packet has not actually been sent to anything yet.Now that the hypervisor's vSwitch has the packet , the hypervisor will always require at least one ( 1 ) physical CPU clock cycle to send the packet out through the physical network interface card.* So far , we have consumed at least two ( 2 ) CPU clock cycles or more to get the packet from the CHR out on the physical network switches.if the packet is destined for another CHR on another different hypervisor , then there is at least one ( 1 ) CPU clock cycle to get the paket from the physical Ethernet interface and place the inbound packet on the vSwitch , and one ( 1 ) more CPU clock cycle to move the packet from the vSwitch to the CHR.The effective throughput result is that when a CHR is sending or receiving packets out or in through physical network interfaces, we are running at half CPU speed. Thus , it is almost impossible for a CHR to achieve sustained network speeds of 6-Gig or faster ... because of the hypervisor CPU clock cycle overhead to transfer packets.Depending on the physical CPU processor GHz clock speeds that the hypervisor is running on , it is easily possible to have a wall of 6-Gig or 8-Gig that the CHR is limited to in throughput. This wall is there because of hypervisor CPU clock cycle overhead when moving packets. Even if you have 100-Gig physical network cards on the hypervisor , the packet transfer throughput wall is still there. ((( And - there is also the CPU consuming clock cycle resources of the hypervisor which may also be slowing down the CHR throughput - because the hypervisor is also doing other things at the same time)))ROS x86 32-Bit does not have this hypervisor CPU overhead when installed on a bare metal box. However, this is a 32-Bit ROS router and may not have enough RAM memory for large RAM needs such as multiple BGP tables and multiple OSPF tables and/or other RAM consuming things such as firewall rules and large address-list tables.I think CHR might support SR-IOV interfaces ( which should eliminate the hypervisor CPU clock cycle overhead) , but I do not know if a SR-IOV driver is in the CHR ROS software. Also , not all hypervisors and network cards and BIOS configurations have SR-IOV support.If Mikrotik were to support a CHR install on a bare metal install, the packet throughput should be possibly double the speed or more.To backup my claim of packet speeds and hypervisor CPU clock speed overhead, there is a VyOS open-source router that can be installed on bare metal and also has SR-IOv support. There are many reports of VyOS router installs sustaining 40-Gig and much faster (nearly up to 100-Gig) network transfer speeds.My ISP network CHRs are hitting that wall. I am currently upgrading my physical servers and switches to 100-Gig. I am also upgrading my four BGP Internet feeds to 100-Gig. My current CHRs can sustain 6-Gig but it's impossible to layer-3 route faster than 10-Gig.So , I ask ... Would Mikrotik please consider creating a CHR platform that can be installed on bare metal - and have drivers for 40-Gig, 100-Gig, 200-Gig and 400-Gig network cards -and- also include support for SR-IOV network interfaces?If the future of CHR will not include bare metal install features, then I will be forced to migrate my layer-3 CHR routers to something else.North Idaho Tom Jones ---

## Response 162
The problem with that idea is that for every network card some user has, and for every new network card on the market, the whining about "can you please include the driver for my card??" will begin. And not only for network cards, but also for all other hardware in the system (disk devices etc).We have already seen that in the x86 release...Running CHR on a Hypervisor neatly separates the RouterOS from the hardware at hand.And SR-IOV is indeed supported. ---

## Response 163
As I mentioned in another comment, in terms of CHR performance using today's modern drivers supporting DirectIO/DirectPath/SR-IOV, it's as fast as bare metal and the overhead of the supervisor is barely measurable. A properly configured virtual system can easly push many hundreds of gigabits without significant CPU load.IMO, one of the major advantages of CHR is that the platform becomes hardware-agnostic and enables live migration including network sessions to new hardware without any downtime (aka Hyper-V/vSphere live migration). It's a perfect fit for data center solutions likevirtual BNG'setc I might add.Thus from a purely operational and production perspective, CHR has almost nothing but advantages.EDIT:Forgot to mention that CHR is in no way dependent on or related to DirectIO/DirectPath/SR-IOV.Instead, these features are managed by the host virtual machine and implemented through the network card's drivers, and they are available from most manufacturers for mid-end to high-performance solutions (though I've seen support for cheaper NICs nowadays). ---

## Response 164
I am still waiting for RouterOS logging in RFC 5424 standard. Requested this for more than 5 years???viewtopic.php?t=124291 ---

## Response 165
So , I ask ... Would Mikrotik please consider creating a CHR platform that can be installed on bare metal - and have drivers for 40-Gig, 100-Gig, 200-Gig and 400-Gig network cards -and- also include support for SR-IOV network interfaces?Let me explain, you start digging by hand you hit a rock, you get "new shovel", but you stuck again, cant pass through - you asking what improvements needed on the "new-shovel" to break the rocks - the answer is simpe: You can't - you need heavy-duty equipment for that jobCPU PCI-E lanes can't handle/sustain that speed - other factors will be problem too ( example: LATENCY ).The ASR9K/NCS series can do that kind of job. ---

## Response 166
It could be handy to have a VLAN setup script just like the DHCP server setup script...Was reviewing the different ways of doing common VLAN setups on mikrotik router+switch hardware. It seems to differ based on the switch chips, etc..e.g../int/vlan/setupwhat is the VLAN ID you'd like to use? (1-4095)5what interface(s) should be tagged with vlan 5? /* tab completion would be welcome */spfplus1what interfaces(s) should be vlan5 without tags?ether2, ether3, ether4/* perhaps display a humanreadable summary and press enter to complete or control-c to cancel */ ---

## Response 167
RouterOS is not for the users that require wizards for everything... ---

## Response 168
Could be added to QuickSet ---

## Response 169
You can forget about that... Quickset is not good for simple things, let alone VLANs that are whole different story on Mikrotik. ---

## Response 170
CPU PCI-E lanes can't handle/sustain that speed - other factors will be problem too ( example: LATENCY ). The ASR9K/NCS series can do that kind of job.ASR9xand similar models nowadays act more like "regular" linux blade servers with Cisco Linux (IOS XR). Blade cards mainly utilize standard buses including PCIe as interconnects. FPGA/ASICswitch fabric cardsused for backplane intercomms currently yield approximately 230 Gbps per fabric with up to seven per backplane, totaling 1.6 Tbit/s.CurrentPCIe 6has a latency of a few nanoseconds and a transfer rate of approx 60 Gbit/s per lane. An internal fabric interface card using standard 16 lines provides about 960 Gbit/s and a blade card using 4 buses 3.8 Tbit/s. Even an old server from 2010 using PCIe 3 and a Xeon CPU can achieve over 200 Gbit/s line speed using a single bus.CXL(explained) enhances the standardization with faster and broader utilization of interconnects based on PCIe for example within and between interfaces, backplanes, and servers.Modern drivers with no-copy support operate solely with pointers to network data through DMA, meaning that the CPU only initiates the communication.For standard systems, network cards generally constitute the main bottleneck. ---

## Response 171
RouterOS is not for the users that require wizards for everything...That may be true. But request is not far off from /ip/dhcp-server/setup which does prompting (and supports <tab>). So doing a /interface/vlan/add, /ip/address/add then /ip/dhcp-server/setup gets you a working VLAN in three steps (outside port assignment, and firewall which may solved with a another step by adding it to the LAN interface-list).Bigger issue WRT VLANs is the port assignment – that's wouldn't be helped by a wizard. Better UI is what's needed there.You can forget about that... Quickset is not good for simple things, let alone VLANs that are whole different story on Mikrotik.QuickSet could be improved. But the default configuration could just include "vlan-filtering=yes" as a default, so a router be "VLAN Ready™". It doesn't break normal case & safe to set if done as part of initial boot. ---

## Response 172
Probably instead of adding even more of these "QuickSet" and "setup" hacks it would be better to develop a newbie-friendly GUI tool that allows configuration of the router in the same way as modern consumer routers are configured (wizards, task-oriented screens) and configures the router accordingly via API/WINBOX. With the express warning that once you configure the router directly, that tool can no longer be used.(preferably also with some real guard against that, which should also be added to QuickSet itself) ---

## Response 173
If the router does not have a public IP address (4G connection), all traffic is routed through MikroTik servers, right? ---

## Response 174
Great idea, especially for routers that targets home users. I mean you have Mikrotik Home app and BTH app and those are nicely designed and user friendly.Mikrotik should make RouterOS lite, just for home lineup of routers IMHO. And if you want you can netinstall full version. It's just the matter of licensing in that case. ---

## Response 175
It would not require a different RouterOS do do that, just an application that has many wizards and knowledge of the hardware (how many ports, what are they called, what kind of WiFi, etc). The application asks the users what he wants to have, and sends the correct configuration commands to the router.Once you make changes outside that application, you are on your own.This is basically how Cisco did it on their IOS routers. ---

## Response 176
I never really saw Cisco GUI, last time i had interaction with Cisco was in high school 11 years ago and that was through CLI.What I meant when I said that Mikrotik should consider RouterOS lite is that they should maybe create stripped down version without for e.g all that routing protocols that home user will never use. So leave functions that home user will use (VLANs, VPN and so on) and create nice GUI and maybe cloud management app like ubiquiti and TP - Link for eg.Also I would like to see PPSK. ---

## Response 177
I never really saw Cisco GUI, last time i had interaction with Cisco was in high school 11 years ago and that was through CLI.I don't know how it works today, but in the past we had Cisco routers and at some point a new router came with a packagethat could be used to configure it. Written in Java to be executed inside your browser. It presented a web page with someuse cases and parameter fields similar to QuickSet, but if I remember well there also was a little more advanced configuration.It resembled the UI of a consumer NAT router.As I did not require this I de-installed it and used CLI, which is what all our other routers had and for which I already had aconfiguration file (where only IP addresses had to be changed).MikroTik (or an independent developer!) could write such a thing and cover the most frequent use cases in it.The unfortunate thing is that once you require one single feature that is not covered by that program, and you start changingthings on the router itself, it then becomes unreliable to change other things via the GUI program. Same as with QuickSet.So it better be very advanced and cover almost everything. A lot of work to make. ---

## Response 178
I never really saw Cisco GUI, last time i had interaction with Cisco was in high school 11 years ago and that was through CLI.I don't know how it works today, but in the past we had Cisco routers and at some point a new router came with a packagethat could be used to configure it. Written in Java to be executed inside your browser. It presented a web page with someuse cases and parameter fields similar to QuickSet, but if I remember well there also was a little more advanced configuration.It resembled the UI of a consumer NAT router.Omg not this one. Cisco Configuration Professional.That .hta file that would start a tomcat via an ActiveX component then show a Flash/Flex applet that will itself also embed a Java Applet. WHY would you do that. ---

## Response 179
Yeah, the implementation was sort of sub-optimal, and it would no longer work today.But the idea in itself is apparently what a lot of people want: manage the router at "application" or "task" level, not at "VLAN config" or "firewall rule" level.When there is demand for that, someone could write it and maybe make some money.(although it is doubtful that people would want to pay money to overcome their lack of RouterOS knowledge, so probably that would have to work via in-app advertisement) ---

## Response 180
Omg not this one. Cisco Configuration Professional. That .hta file that would start a tomcat via an ActiveX component then show a Flash/Flex applet that will itself also embed a Java Applet. WHY would you do that.And I must be old... because I recall cisco IOS's "ip http server" being a rather limited, style-less UI in times roman font that let you get a config or type a command using old-school HTML forms.The original feature request that prompt this discussion was a "wizard for VLANs". Given VLANs are both pretty "popular" & non-trivial to setup – seem reasonablerequest. IMO, "wizards" belong in the smartphone apps.But do think somevisual"VLAN configurator" be handy to both newbies and pros. e.g. It's a lot of config-reading to know if VLAN are configured as expected. ---

## Response 181
VLAN configuration is tricky in many different products. Often there is no good overview of what you are doing.It can be done VLAN-centric (you define VLANs and specify which ports are tagged members and which are untagged members) or it can be done port-centric (for each port you can set which VLANs it has tagged and which VLAN it has untagged).And then you can do it MikroTik-way, which is a mix of these two, and very confusing. That PVID setting has to go, and should be put in the VLAN untagged member list only.But MikroTik is not the only supplier that does that... in my Netgear switch at home (GS108T2) it is done the same way and even worse: you need to set BOTH the PVID and the untagged VLAN. At least in RouterOS setting the PVID automatically sets the untagged VLAN (which I discovered only much later).This mixed config allows the "flexibility" of having different config in upstream and downstream direction, but I would not know a valid use-case for that. ---

## Response 182
VLAN configuration is tricky in many different products. Often there is no good overview of what you are doing.It can be done VLAN-centric (you define VLANs and specify which ports are tagged members and which are untagged members) or it can be done port-centric (for each port you can set which VLANs it has tagged and which VLAN it has untagged).And then you can do it MikroTik-way, which is a mix of these two, and very confusing. That PVID setting has to go, and should be put in the VLAN untagged member list only.But MikroTik is not the only supplier that does that... in my Netgear switch at home (GS108T2) it is done the same way and even worse: you need to set BOTH the PVID and the untagged VLAN. At least in RouterOS setting the PVID automatically sets the untagged VLAN (which I discovered only much later).This mixed config allows the "flexibility" of having different config in upstream and downstream direction, but I would not know a valid use-case for that.Re: ...and very confusing...IMO - I agree , extremely confusing - - - and not the same configuration procedures across all Mikrotik past and present products.IMO - I would like to see all Vlan and switching features and functions completely removed from ROS - and replaced with a SwOS package that is part of ROS. Then instead of a Mikrotik ROS software product and also a Mikrotik SwOS product , to just have one ROS software system with built-in SwOS. Then , if you have any Mikrotik product with a newer ROS release ( with built-in SwOS ), all routing functions and all Vlan configurations and all switching functions could then be all configured one common procedure. AKA - make it KISS ( Keep It Simple Stupid -- and the same across all Mikrotik products ).well - that's my opinion. ---

## Response 183
If the router does not have a public IP address (4G connection), all traffic is routed through MikroTik servers, right?no. why would you think that? ---

## Response 184
But do think somevisual"VLAN configurator" be handy to both newbies and pros. e.g. It's a lot of config-reading to know if VLAN are configured as expected.More than I suggested, but that would be agame changerway to go!I might be showing my age.... The Cisco 2501 CLI had an awful little wizard to set things up if you did not choose "conf t"The very easiest hardware to do VLANs with is the old HP Procurve managed switches... 4000m, 2524, 2848, 5300 series...Rows were ports. Columns were VLANs. play battleship. Every switch worked the same. You could use their text interface like this, or use the CLI which was formatted in the way the text configuration is written.Every switch's web interface since has not matched the HP text interface.We eventually moved more to Mikrotik for power savings, as battery run time at tower sites is very important. And noisy hot switches run down battery backups quick. Now, how vlans work in mikrotik depends on which mikrotiks because they differ in cpu/switch chips. e.g.. things ideally program different for vlans between a crs124 and crs326 I think. ---

## Response 185
imagine a world/dimension where there is routeros feature richness and customizability and a GUI like from that "UB.." company ---

## Response 186
imagine a world/dimension where there is routeros feature richness and customizability and a GUI like from that "UB.." companyIt is already more feature rich and customizable. I think the other company's GUI is good for central monitor and easy admin tasks (like updates and wireless settings), but difficult for things I might consider advanced. ---

## Response 187
Please make dynamic vlan assignment possible for wifi-qcom-ac wireless driver ---

## Response 188
Please make dynamic vlan assignment possible for wifi-qcom-ac wireless driverdo you mean via RADIUS? ---

## Response 189
Bridge-To-Bridge joiner.To be assumed it will not be high performance.Uses:- Legacy PPPoE pass through (My ISP uses PPPoE...)- Natting Mac addresses from devices to the CPU. (Multiple devices with the same Mac Address)- mDNS and SSDP pass through in a single router.viewtopic.php?t=194842&sid=9823878ca8fa ... 9452b2a5de- Bridging items with different MTU'sNotes:- An item that has 2 interfaces.- Can (only) use the interfaces as a bridge port.- Transparently transfers ethernet frames between interface 1 and interface 2 (bidirectional)including any vlan tags, low level bpdu's, etc.- Allows both ends to connect to same bridge (eg. for mDNS between 2 vlans)- Maybe loop detect option (for when accidently join both ends to same bridge and same vlan)- All filtering done using existing bridge filtering functionality- Each interface gets the MTU of the bridge it is attached too.(Don't have to be the same on each end) ---

## Response 190
Please make dynamic vlan assignment possible for wifi-qcom-ac wireless driverdo you mean via RADIUS?Via RADIUS or via access list. I also want to have that, I use it in the old wireless driver. ---

## Response 191
Bridge-To-Bridge joiner.You can do that with two local EoIP interfaces. ---

## Response 192
Wouldn't it be cool to have signal strength graph in the Wi-Fi Registration table like in Quick Set?Having that column one can easily identify problem clients at a glance.It would be even cooler to have the "hostname" in the wifi registration table (like it was available in the wireless registration table). But unfortunately Mikrotik seems not to be interested to add it anytime soon. ---

## Response 193
Bridge-To-Bridge joiner.You can do that with two local EoIP interfaces.Whenever I have tried this it never allows me to have 2 with the same tunnel ID.Also quite a lot of overhead. ---

## Response 194
Please make dynamic vlan assignment possible for wifi-qcom-ac wireless driverThis, a trillion times, this.Also, make the vAPs for secondary SSIDs auto-populate and map on local bridges correctly.There really should be "configuration parity" between wifi-qcom-ac and wifi-qcom.Configuring and managing wifi-qcom-ac CAPs is a process that's entirely too manual right now in a way that the AX-generation driver doesn't seem as bad.CAPSMAN is supposed to mitigate the challenge of managing a growing and/or complex infrastructure, not simply "dampen" the the linear increase of time/labor a bit. ---

## Response 195
Bridge-To-Bridge joiner.You can do that with two local EoIP interfaces.You can't as the tunnel number can't be the same for 2 interfaces.It's the same story for VLAN interfaces - it's the networking equivalent of the Pauli exclusion principle - you aren't allowed to have more than one VLAN interface with the same bridge and VLAN ID.Mikrotik: Request - allow more than one VLAN interface to share the same bridge and VLAN ID. It will allow for some interesting modes mixing bridge filtering and routing.<edit> Holy crap MACVLANs solves this problem! Cancel request! ---

## Response 196
Hi!I try access to link in fisrt post but it's broken.Perhaps this has been requested before, sorry.A printer server for share a printer connected to a USB port of devices i think it would be very useful for many users.Regards. ---

## Response 197
A printer server for share a printer connected to a USB port of devices i think it would be very useful for many users.Regards.The Mikrotik would be an excellent place for a print server!I used to have to use a SSL vpn on my PC for work, and it broke local lan access which included printing I needed to do for work breaking network printing. It did allow access to my gateway IP, so that would have been ideal place for a printserver that's not affected by the PC VPN that routes everything except default gateway. Because I had a Mikrotik router, I setup a port forward to my network printer, internal accesible only, so that I could print.A print server should be configurable to be blocked from the outside by default. ---

## Response 198
The Mikrotik would be an excellent place for a print server!I don't know about that. I'd think some mDNS support be more useful, than a print server, in 2024? ---

## Response 199
The Mikrotik would be an excellent place for a print server!I don't know about that. I'd think some mDNS support be more useful, than a print server, in 2024?Indeed! This is just a general "VPN setup in the wrong way" issue. Put your VPN range in a different IP range and it all works fine.Maybe the "automatic discovery of the printer" would be more difficult but mDNS support would improve that. ---

## Response 200
One other request...Make adin rail mounting option for the 5-port sized Mikrotiks.(hex, hex-s, hap-ac2, etc...)I used to be in the ISP/WISP world, and Mikrotiks went on a rack shelf or zip tied to a cabinet.Now, I work on boat ethernet systems and it would be real handy to snap a mikrotik and a few other items like data converters and power supplies to the wall with a din rail system. Mikrotik is a good fit for this market because of it's low power and wide input voltage. I mostly use them as a glorified switch for their logging/management features. ---

## Response 201
I don't know about that. I'd think some mDNS support be more useful, than a print server, in 2024?Indeed! This is just a general "VPN setup in the wrong way" issue. Put your VPN range in a different IP range and it all works fine.Maybe the "automatic discovery of the printer" would be more difficult but mDNS support would improve that.some VPN clients do tunnel all traffic and block local access (e.g. Checkpoint client vpn)and there is not much you can do against it on your gateway (e.g. mikrotik router) ---

## Response 202
Please make dynamic vlan assignment possible for wifi-qcom-ac wireless driver+1, this is a must-have feature. You can't reasonably manage APs without it. Currently I have to have a static VAP in bridge and set the VLAN ID there... ---

## Response 203
Please make dynamic vlan assignment possible for wifi-qcom-ac wireless driver+1, this is a must-have feature. You can't reasonably manage APs without it. Currently I have to have a static VAP in bridge and set the VLAN ID there...I agree. I have done some testing in this regard. With VLAN-Filtering turned on on a qcom-ac device it does indeed dynamically add the wireless interface, but to the wrong VLAN! Why!? It feels like it's a solved problem but for this unless there are other technical issues as yet unrevealed.I think the issue though is that the method of setting up an AP client differs for AX devices and AC devices. The former doesn't need VLAN-Filtering and the latter does. Also there is the issue of how VLANs are tagged and how frames are promoted based on DSCP markings. The former it seems the AX devices have a hardware feature that adds and strips VLAN tags and also sets WMM priority based on DSCP. The older AC devices don't and you get a warning if you try use those options.If the AC and AX devices all just used VLAN-Filtering and allow dynamic Wifi interfaces that'd be swell. ---

## Response 204
- the old wiki page is missing, please update the first post!+1 mac address listviewtopic.php?p=1057990#p1057990 ---

## Response 205
+1 mac address list ! ---

## Response 206
[FEATURE REQUEST]Please consider adding support for the MAP-E (RFC7597) transitional protocol(preferably accelerated for the socs that support so).Recently my isp (Cosmote, the major ISP in Greece),began implementing MAP-E on its latest cpes for residential/soho (xdsl/FTTH) connections, and some users find themselves having an ipv6-only connection.I suppose the plan is for the ISP to move away from dual-stack.For now, its deployment is rather limited, and if the customer call support and ask for dual-stack they revert the change, but this is bound to change sooner than later.Now, cosmote usually is the testbed for DT (it's a member of the group),and as far as I know DT also begun transitioning to MAP-E, so, the change can possibly affect large part of EU, and can render the use of mikrotiks/ros problematic. ---

## Response 207
wifi wave 2 qcom-ac:Is there any chance you will add dynamic client VLAN assignment again?It would also be nice to see the EAP identity in the registration table like before. ---

## Response 208
Hello Mikrotik.please allow the Mac-Telnet from WAN ether1 on default configuration we have very big problem when we reseting factory or installing new router all any access to router from ether1 disabled.we tired from using ether2 or any other interface to first time login.and some routers installed in places can not reach it.Mac-Telenet required physical access to neighbor router and which its done locallysome one with me ? or I'm wrong. ---

## Response 209
The allowed interfaces for MAC-level access can depend on the model of the router, and possibly on the software it first came with.However, usually it is enabled on all ports and when it is not, it is because you changed that yourself before. ---

## Response 210
The allowed interfaces for MAC-level access can depend on the model of the router, and possibly on the software it first came with.However, usually it is enabled on all ports and when it is not, it is because you changed that yourself before.Yes but firewalls drop every thinks from WAN which its ether1 even the MAC discovery in almost router types, if we have client or any new router need to install two cables one for POE ether1 and 2nd for login to remove the default configuration , normally we do reset without default configuration but when do reset from Reset bottom its big problem , all our customer we use hAPacˆ3 with Power over POE ether1 and PowerBox Pro as POE switch all APs are on celling or in Higher place.including new router need also two cable one for POE and 2nd connected to ether2MAC-telnet its my lovely option in world of IT since 2005.I think its easy to make the WAN from last interface such as ether5 or4 or make default WAN bridge and all interfaces in LAN bridge after first login user he can assign the WAN from interface list.this was option and also its easy to except the MAC-Protocols from firewallsRegards. ---

## Response 211
The allowed interfaces for MAC-level access can depend on the model of the router, and possibly on the software it first came with.However, usually it is enabled on all ports and when it is not, it is because you changed that yourself before.Yes but firewalls drop every thinks from WAN which its ether1 even the MAC discovery in almost router typesNo, the firewall does not affect MAC level access.I recommend you to do a full reset to defaults on the type of device that you have, and examine the configuration of MAC level access. ---

## Response 212
Feature request: let us save graphs on USB/SD card finally! ---

## Response 213
+1 HA clustering with configuration preferably on the main node and config sync (like CARP from opnsense) ---

## Response 214
Double click on an entry in Winbox to connect. ---

## Response 215
Double click on an entry in Winbox to connect.Already works! ---

## Response 216
Never has here. Double click on that line and all it does is populate the top box. ---

## Response 217
Please Mikrotik, implement PPSK already... ---

## Response 218
Feature request: let us save graphs on USB/SD card finally!RouterOS do support syslog so you can send any logs externally and graph everything. Look at my Mikrotik for Splunk. ---

## Response 219
Feature request:IKEv2 Mobility (MOBIKE) ---

## Response 220
Never has here. Double click on that line and all it does is populate the top box.On the "managed" tab it works. I do not know about the "neighbors" tab, rarely use that. ---

## Response 221
On the "managed" tab it works. I do not know about the "neighbors" tab, rarely use that.I always wondered what managed tab was all about! Yes, double-click does work there. Same in Neighbors tab then ---

## Response 222
RouterOS do support syslog so you can send any logs externally and graph everything. Look at my Mikrotik for Splunk.Yes, we can. But I agree with him: why not allow this? It must be a one liner change: In pseudo code, something like "write logs in /logs or /usb/logs?" ---

## Response 223
Likely the reason for not allowing such things is that users would configure it to use USB storage and then pull the USB key at an inappropriate moment, then complain about things crashing or otherwise failing. ---

## Response 224
I always wondered what managed tab was all about! Yes, double-click does work there. Same in Neighbors tab thenOkay, added a few entries to "Managed" tab. Version, board and uptime are missing columns. Prefer Neighbours. ---

## Response 225
Did you enable "advanced mode"? It does not provide those fields, but it provides some other useful features. ---

## Response 226
Unless I've missed it somewhere...Please for the love of God add a command or hotkey toggle to show all 'sensitive' fields in the console and not have them blocked outWhen typing or pasting in a command that contains a password, it will blank that entire line out as soon as the enter key is pressed. Was there a typo in there? Were all commands on that line present? What exactly was typed? Who knows it's a total mystery BECAUSE THE DAMN LINE DISAPPEARSIt's made significantly worse when its part of a larger block or code, the entire block gets turned invisible. It's an absolute nightmare to work with ---

## Response 227
Yes, I think you've missed it - settings show/hide passwords? Unless I'm missing something ---

## Response 228
Likely the reason for not allowing such things is that users would configure it to use USB storage and then pull the USB key at an inappropriate moment, then complain about things crashing or otherwise failing.You can't fix stupid. Let it using the onboard storage by default, but allow the user to change this. The Linux kernel already fails gracefully, when some block device goes away - there's even an mount option to control this. They only have to make sure the logger used fails gracefully too. ---

## Response 229
As it is now, RouterOS does not even properly close some files after using them (or forgets to "chdir").I have an open bug where I have an NFS-mounted directory (the router mounts a directory on a server) where I put backups so they end up in the backup made from that server.When I do a/user-manager/database/save name=nfs/umbackup overwrite=yesit correctly makes the backup but then the directory can no longer be unmounted (file in use).So when I have done that I cannot even reboot the router anymore (e.g. as part of an upgrade), it hangs in the reboot.It was claimed to be fixed, but it isn't. ---

## Response 230
Feature request for "ups" package: allow to set a script to be executed when UPS state changes between on line / on battery.(to enable sending an e-mail or other alert when power fails) ---

## Response 231
Winbox - better way of configuring the columns in all the dialogs. Certainly be able to right-click on a column and remove it. ---

## Response 232
Hi, I think, it will be usefull to have context option "Wake On Lan" in ip / dhcp-server / leases.I'm using this mostly to connect home with my home computer off (energy saving).I have to lookup MAC address, start terminal and type (or lookup from history) command to start computer.(too lazy to setup a script and I prefer typing before clicking)Interface selection:I recommend to select interface from related server section.Other option is to offer interface (combobox) - anyhow not all interfaces are for internal/dhcp use.Interface identification:get Server column from leases list (Wake On Lan option can be located bellow Make Static)wbx-dhcp-srv-leases.PNGlookup interface in corrensponding DHCP serverwbx-dhcp-srv-interfaces.PNGI also wrote several scripts to wake computers with parameter to lookup in /ip dhcp-server lease (IP or Comment lookup or hostname).According to limited functionality to use parameters in scripts, it must be in eval form in global variable and global variables are not consistent across router reboots. ---

## Response 233
I'm using this mostly to connect home with my home computer off (energy saving).I tackle this another way - I've got a couple of cheap IoT plug sockets. PC is configured in BIOS to power-up if the power fails. So I go in the app on my mobile, turn the socket off, wait a minute and turn it back on. I gave up on WOL years ago when it never seemed to work! ---

## Response 234
More context options for DHCP leases would be nice. Especially right clicking and choosing mac-telnet, winbox, SSH, HTTPS etcI'm almost exclusively looking in DHCP leases for a particular device that I need to do something with by connecting to it. Cutting out those extra steps of them opening putty/browser/winbox and typing in the address would be very welcome ---

## Response 235
Currently UPnP and Hairpin NAT does not work together. It is because the dynamic dst-nat rules created by UPnP has the in-interface=<external> filter. It would be nice to remove this filter from dynamic rules created UPnP, either by default or via a configurable option. See this discussion thread for more details:viewtopic.php?p=1062302 ---

## Response 236
I tackle this another way - I've got a couple of cheap IoT plug sockets. PC is configured in BIOS to power-up if the power fails. So I go in the app on my mobile, turn the socket off, wait a minute and turn it back on. I gave up on WOL years ago when it never seemed to work!There are some mainboards that don't work with WOL. Just a BIOS bug, I guess. I had one of those: an Asus, M5A97 LE. WOL just didn't work. As soon as I used another one (Intel or AMD, didn't matter), it worked alright. ---

## Response 237
A version of routeros 7 that has reduced footprint (and reduced functionality) but works comfortably on 16mb flash devices. I started a separate threadviewtopic.php?t=205735if anybody wants to comment and discuss what functionality the small flash devices can go without ---

## Response 238
Feature request: Register DHCP leases in the DNS Resolver, providing local name lookups for any DHCP client, static or dynamic.I know it can be worked around with scripts, adding static entries on each lease but its bad solution that wears out flash memory. ---

## Response 239
Please make dynamic vlan assignment possible for wifi-qcom-ac wireless driverdo you mean via RADIUS?nope, I want just the existing feature in wifi-qcom driver, like this: ---

## Response 240
do you mean via RADIUS?nope, I want just the existing feature in wifi-qcom driverThat is not a required feature, you can assign the VLAN in the bridge.What is missing is the dynamic assignment via RADIUS or bridge filters. ---

## Response 241
Request:- New "CCR2004" rackmount hardware ( 24x1G, 4x10G port) with external 2x USB ports, internal 2x M.2 Storage portThe current CCR2004 lack of USB and Storage connection ports ( no LTE modem connection), this is ridiculous.Mikrotik loves "cheap" SOC so use the "RTL9301-CG" chip with the ARM64 CPU with external USB and internal Storage ports. ---

## Response 242
Request: some function to "compact databases" so that the size of the databases again corresponds to what you would have after a"reset configuration" and an "import" of the current configuration (plus things like certificates etc).As it is now, the databases size tends to increase over time, resulting in large backup files and problems with storage on 16MB flash. ---

## Response 243
Not sure if this is already asked, please put configuration change log into separate topic, for eg.system, info, configurationto have ability to filter it out without filtering other logs fromsystem, infotopic. When configuration change logging was introduced intosystem, infotopic, log can get bloated with these records for eg. in case when some shceduler is changing configuration multiple times during the day and it would be nice to have ability to filter this out. ---

## Response 244
Or more general: add an extra topic to each and every unique log message, which is some numeric code that uniquely identifies that particular message.That allows us to easily log or exclude particular messages. ---

## Response 245
[feature request]WinBox Keyboard hotkey navigationto be activated for example pressing [ALT] twicethen the menu items could, for example, be iterated through a-z and on submenus (like MPLS, etc.) the iterations could move over to the submenuso navigation could be much faster, hence one can navigate with the keyboard anyways for adding entries ( [INS] key) or de/activating items ( [STRG]+[D] / + [E] )MT-featReq_winbox_keyboardShortcutNav.pngstill waiting ---

## Response 246
Feauture requestPlease addaddress-list on ros 7Policy Routing RuleThank you ---

## Response 247
The underlying OS does not provide that feature! ---

## Response 248
In the WinBox script editor WHY there is not the line number and the column number of the cursor?When you run a script you get errors referring to a line/column! ---

## Response 249
On devices capable of it, for PoE besides the auto-on setting that attempts passive PoE, also provide a 802.3af/at setting that only attempts standards-compliant PoE negotiation. ---

## Response 250
On the Products page of the website, improve the "filter" section to serve as a product selector.Ideally, all features available across all models would have a section or checkmark there.Like:- number of ethernet ports and their speed- RAM size- Flash size- CPU architecture- CPU performance- supply methods- USB- RS232- Mini-PCIe- M.2- etc(of course best if the selections are automatically populated based on the info about products, so new features appear here without risk of being forgotten) ---

## Response 251
On the Products page ....what also would be a convenience on the "Specifications" Page -> Link the Row "License Level" direktly to theLicense Levels Help Pages ---

## Response 252
Ive been using Mikrotik for a few years now and there are a few things I'd love to see to make things a bit slicker. I have a background in networking earlier in my career, and I've worked a lot with Cisco ASA/Enterprise Switches/Routers & ASR and Palo Alto, plus HP/3Com so my requests are somewhat influenced by this. I only use Mikrotik at home.My main asks are around config changes1) Take a safe mode approach by default. or at least have a configuration setting that allows this to be turned on by default, needing manual exit of safe mode each time to be fully commited. Eg on Cisco I have to write mem/commit, as with many other vendors. Better to be able to reboot to back out changes Vs being locked out because you forgot to enable safe mode and really screwed something up by accident2) Be able to see a clear difference of what was changed before committing. The current audit log is not very helpful as it just says things like "firewall rule moved" but without further detail - I want to know exactly what changed; a 'rollback commit' feature would be amazing.3) Logs - Show the action taken on a firewall rule. The current format is esoteric and needs you to rely on giving meaningful log prefixes so that you know if it was dropped, accepted, whatever4) I find that I can't really trust exports & backups. Just today I noticed user accounts missing which are critical for access, and certs can be a pain aswell. It would be nice to know that I have a full, complete backup that I can load on a fresh device and be fully back as it was in a couple of clicks5) Lower the barrier to entry and adoption. These are amazing devices with a challenging learning curve and an extremely unforgiving UI and CLI if not used with care. Improve quick start type features to make it easier to segment your network. Why let Ubiquiti and TP-Link take market share through a reputation of being too tricky? I am a power user in most sense but still feel like a rookie on Mikrotik (some incredibly helpful people around here help there, though). ---

## Response 253
Adlist whitelist function would be great!More Fans.viewtopic.php?t=209369 ---

## Response 254
3) Logs - Show the action taken on a firewall rule. The current format is esoteric and needs you to rely on giving meaningful log prefixes so that you know if it was dropped, accepted, whatever4) I find that I can't really trust exports & backups. Just today I noticed user accounts missing which are critical for access, and certs can be a pain aswell. It would be nice to know that I have a full, com+1 on 3 and 4note to MT on "4":optionally make the binary ".backup" files not bound to the device it has been created on. e.g., maybe give a option to save a .backup for other devices so for example MAC addresses do not get overwritten but stuff like certificates and user/user group information is saved and restored on another mikrotik device ---

## Response 255
Re: ...optionally make the binary ".backup" files not bound to the device...It would be a useful feature to be able to make a backup that is portable to a different replacement Mikrotik device.-or- even betterIt would be very useful to have a new restore/import feature which would allow a replacement Mikrotik router to import a foreign (a backup from a different Mikrotik router).Where the new imported/restored configuration has two options when restoring.- Restore foreign backup andreplace the current running configuration(does not restore stuff like MAC addresses)- Restore foreign backup andadd to the current running configuration(Does not auto reboot- does not restore stuff like MAC addresses)North Idaho Tom Jones ---

## Response 256
It would be a useful feature to be able to make a backup that is portable to a different replacement Mikrotik device.that's what i meant ---

## Response 257
So does that mean that if my MT dies and I get another unit exactly the same, I cannot restore from the backup? I'd have to use commands from an export? yikes, i didn't know that. Then +1 to the above! ---

## Response 258
4) I find that I can't really trust exports & backups. Just today I noticed user accounts missing which are critical for access, and certs can be a painYou are right, it is a real pain that users and certificates are not included in /exports, not even with show-sensitive or other options!That certainly should be fixed. ---

## Response 259
3) Logs - Show the action taken on a firewall rule. The current format is esoteric and needs you to rely on giving meaningful log prefixes so that you know if it was dropped, accepted, whateverTrue. I don't mind that much that you need to put the action taken in a log prefix, but I do want to have the option to specify that the log message includes either what it is now (default) or an extended dump of the packet.As I understand that a full packet dissector would cost valuable space in the code, it would be acceptable when one can log the header or the full packet in HEX so it can be decoded elsewhere.For example, I am now studying the use of bad MSS values in TCP SYN, and while one can filter packets based on MSS, the log message issued when it matches a packet does not include the actual MSS value.To get the affected packet it would have to be sent using a "sniff" action but that can only be done in "mangle", making the whole setup overly complex. ---

## Response 260
3) Logs - Show the action taken on a firewall rule. The current format is esoteric and needs you to rely on giving meaningful log prefixes so that you know if it was dropped, accepted, whateverTrue. I don't mind that much that you need to put the action taken in a log prefix, but I do want to have the option to specify that the log message includes either what it is now (default) or an extended dump of the packet.As I understand that a full packet dissector would cost valuable space in the code, it would be acceptable when one can log the header or the full packet in HEX so it can be decoded elsewhere.For example, I am now studying the use of bad MSS values in TCP SYN, and while one can filter packets based on MSS, the log message issued when it matches a packet does not include the actual MSS value.To get the affected packet it would have to be sent using a "sniff" action but that can only be done in "mangle", making the whole setup overly complex.and additionally the #number of the matching rule ---

## Response 261
and additionally the #number of the matching ruleYes! I forgot to note that, but definitely, it would make things way easier to analyse and troubleshoot ---

## Response 262
1) Take a safe mode approach by default. or at least have a configuration setting that allows this to be turned on by default, needing manual exit of safe mode each time to be fully commited. Eg on Cisco I have to write mem/commit, as with many other vendors. Better to be able to reboot to back out changes Vs being locked out because you forgot to enable safe mode and really screwed something up by accident2) Be able to see a clear difference of what was changed before committing. The current audit log is not very helpful as it just says things like "firewall rule moved" but without further detail - I want to know exactly what changed; a 'rollback commit' feature would be amazing.3) Logs - Show the action taken on a firewall rule. The current format is esoteric and needs you to rely on giving meaningful log prefixes so that you know if it was dropped, accepted, whatever4) I find that I can't really trust exports & backups. Just today I noticed user accounts missing which are critical for access, and certs can be a pain aswell. It would be nice to know that I have a full, complete backup that I can load on a fresh device and be fully back as it was in a couple of clicks5) Lower the barrier to entry and adoption. These are amazing devices with a challenging learning curve and an extremely unforgiving UI and CLI if not used with care. Improve quick start type features to make it easier to segment your network. Why let Ubiquiti and TP-Link take market share through a reputation of being too tricky? I am a power user in most sense but still feel like a rookie on Mikrotik (some incredibly helpful people around here help there, though).These are all great points. Items 1 and 2 in particular were surprising to me when I first started using Mikrotik. I had previously used Ubiquiti EdgeRouters, which do this. It seemed like a basic, common sense approach. For those unfamiliar, any config changes in EdgeOS don't take effect until you issue the
```
commitcommand. You can issue
```

```
commit-confirmto commit changes and auto-reboot the router if you don't issue a
```

```
confirmcommand within ten minutes by default. This is handy if you have a remote router that you discover you've locked yourself out of.If you want to preview the changes you're about to make before committing, you can issue the
```

```
comparecommand. Once you've committed changes and you decide you want them to persist past a reboot, you issue the
```

```
savecommand.Also the config file includes all configuration and can be easily imported to another router of the same model. You just need to modify if it you want to import to a different model that, say, might have a different number of ports.

---
```

## Response 263
Karl Denninger, who was one of the pioneers in bringing Internet to personal use, justposted a recommendationfor users to randomize their IPv6 addresses on Wi-fi (via OS settings) since the standard SLACC protocol for assigning IP addresses results in a globally-unique identifier for each machine, regardless of which location it travels to or network it is connected to.Fair Use Excerpt:Unfortunately in the IPv6 world this [MAC addresses being readable only on the local network] is no longer true. SLACC, which is what most IPv6 networks use for local devices, results in a globally-unique address that is specifically tied to your hardware and is visible anywhere on the Internet you connect to!So now when you connect to any site on the Internet and are using IPv6 the other end has a globally-unique identifier for your specific device, and unless you can randomize the MAC address it uses you now have dropped a "breadcrumb" that identifies your specific machine. You did not have to sign on, your browser didn't have to send a cookie or do anything else for this to occur. The mere connection attempt is enough as that address always winds up in the other end's log data.Karl goes on to note that "Unfortunately for most systems there is no similar setting for hardware connections (e.g. cabled.)..." My suggestion is that MikroTik add the option to randomize IPv6 addresses via a local DHCPv6 and separate the address assignment from the devices' MAC addresses. So if a laptop, for example, is taken from its home network and used on the road, it will not be trivially identified with the user.Just a suggestion. By The Way, Karl rotates posts off his site regularly, usually after 90 days. Come November or after you probably can't access the original article any more. ---

## Response 264
It seems Karl has gotten a bit behind the times...Not only does he not know how to spell SLAAC, he also does not know about "Privacy Extensions for IPv6 SLAAC".It is a problem that has been solved long ago, even without his input. ---

## Response 265
Linux (systemd-networkd): just use "IPv6PrivacyExtensions=true" and done. ---

## Response 266
Linux (systemd-networkd): just use "IPv6PrivacyExtensions=true" and done.It is on by default in systems like Windows, Android, iOS, etc. ---

## Response 267
If I do not remember bad, Windows use 2 IPs, overlapped for 12h ---

## Response 268
I have a feature request.Where --> Using Winbox , In the wireless interfaces , in the [ Frequency-usage ] screen.I would like to see two new usage items added to the screen.- Average-Usage ; shows the total average during the scan.- Maximum-Usage ; shows the maximum peak detected when the scan was performed.These two new features would be very useful - especially when looking for potential most-quiet frequency ( best frequency ) for an AP.Let the scan run for about 10 minutes , then pick the frequency with the lowest average and/or lowest peak usage for the AP.Feature-Request-Frequency-Usage.png ---

## Response 269
Please add the source IP to the message "ipsec, error payload missing: SA".(the address where the packet was sent from that triggers the message) ---

## Response 270
Hello everyone, I have suggestion for: ip firewall address-listfor selected IP address entry it would be usefull to have quick access to telnet, ssh, pingright now there is enable and disable, it would be also good to have other options to test, monitor or login to selected address.Thanks ---

## Response 271
Please add support for the AmneziaWG protocol using standard tools without using Docker. Bypassing Internet censorship is very important and using it directly inside the router is a big advantage. ---

## Response 272
Please add support for the AmneziaWG protocol using standard tools without using Docker. Bypassing Internet censorship is very important and using it directly inside the router is a big advantage.The problem with adding features like AmneziaWG is its effectiveness is subject to change over time, and built-in things are generally based on some durable RFC/etc standards. i.e. while DPI may be used today... no doubt AmneziaWG still might have other identifiable patterns over time.IMO, this kinda need is why Mikrotik added /containers (generically "Docker™"). But I totally get the reluctance – /container is not so easily setup. And since RouterOS /container !== Docker™ often something like Anastasia or really most things on DockerHub require more tweaks/adaptation to actually work on RouterOS.My feature request be a little broader.... I wish had some Mikrotik "container store" with some curated images... so well-known container is more like adding an extra-package. Or even some "higher-level" CLI/API or "compose-like" metadata be useful.While I get you can just "pull" from DockerHub... the issue some containers have a fair amount of configuration and/or assume some orchestration platform. Basically it often takes reverse-engineering "docker commands" into what be needed on RouterOS. RouterOS specific registry and/or metadata be useful to fill in that gap.i.e."just use a container" is actually a bit daunting for most users... since someone need to be familiar with firewall, routing, "Docker", on top of the software package inside the image... to actually use /container for something like AmneziaWG. ---

## Response 273
I agree, it would certainly be useful when there was some location (MikroTik or not) where one could pull ready-made containers for RouterOS for often requested additions!Especially when Docker containers are often only available for amd64 architecture, and may not be tailored to RouterOS use.There is an example for "freeradius" in the help page, but that would not work on a CCR or RB, only on CHR.Such a repository could contain several often-requested features for RouterOS as easy to use (and update) containers.Examples of useful ready-made containers could be:- Unusual or newly developed VPN protocols (as above)- DNS server/resolver- RADIUS server (freeradius)- Web serverand other similar network services. ---

## Response 274
Hi all -- this is my first time posting...I'm long-time *nix user. I would *really* appreciate `Ctrl-w` (delete word) support on the CLI. Should be easy to implement right? ---

## Response 275
Please, allow several /ip socks entries on different ports with different VRFs. ---

## Response 276
Feature request: Register DHCP leases in the DNS Resolver, providing local name lookups for any DHCP client, static or dynamic.I know it can be worked around with scripts, adding static entries on each lease but its bad solution that wears out flash memory.+1 for this, I think the development of mikrotik features and capabilities went through a lot of changes through the years, however such a simple feature like registering DHCP leases in DNS natively was never one of them.It would be much easier if we could have this feature as an option rather then scripting it... I hope we will see this soon. ---

## Response 277
I support this request. DNS gained a lot of attention recently (adlist, dns forwarders, etc.). And such a feature, registering hostnames in internal DNS resolver, would be a killer. I could remove that wonky dhcp lease script that just bloats my configuration export. And save on disk writes I would welcome as well. ---

## Response 278
Don't know if this has been discussed already, but I do find it baffling that I can't see, let along control any of my additional switch interfaces from my router. Instead I have to log into and configure the switch independently. I should imagine most people sooner or later need more than the five, or eight ethernet ports that come with most routers and want to add more. Why can't they simply be 'added' some way to the configuration page of the controlling router? ---

## Response 279
Add info in winbox toolIt would be very functional to be able to add a description for each connection that you save and thus identify more quickly to which mikrotik equipment I want to connect, until today whenever you save an access you only have as reference the IP address and the user name after that there is a big blank space that is not used. This will be the perfect space to add that description.It is difficult when you have more than 50 mikrotik devices installed and they are not in your network to see their description like when you use the NEIGHBORS tab. ---

## Response 280
Don't know if this has been discussed already ...There's such a feature already:port extender. Not many devices are compatible ... and it comes with some serious gotchas. But it's here. ---

## Response 281
It would be very functional to be able to add a description for each connection that you save and thus identify more quickly to which mikrotik equipment I want to connectI am assuming you a speaking of the managed tab in winbox.In tools at the top, there is and advanced mode you can select, and a bunch of additional information becomes available. ---

## Response 282
IPv6 Fastrack please.viewtopic.php?t=175513 ---

## Response 283
...I think, it will be usefull to have context option "Wake On Lan" in ip / dhcp-server / leases....i just thought this option would come in handy!something like an entry in the context menuScreenshot from 2024-12-02 12-15-23.png ---

## Response 284
something like an entry in the context menuOf which menu? You are surely aware that when device is in sleep mode, it doesn't transmit anything and all caches (e.g. ARP cache, list of DHCP leases, etc.) will forget about it probably long before you'd want to send WoL packet to it, aren't you? Which means that swtich/router, implementing this kind of feature, would have to remember every single ethernet MAC address it sees (indefinitely), together with any other metadata (IP address, DHCP host name, colour of its admin's underware, breed of neighbour's dog, etc.). ---

## Response 285
Static DHCP leases have the MAC Address saved, so on that context menu (which seems to be the screenshot from) makes perfect sense. ---

## Response 286
Static DHCP leases have the MAC Address saved, so on that context menu (which seems to be the screenshot from) makes perfect sense.exactly. thank you sir! ---

## Response 287
something like an entry in the context menuOf which menu? You are surely aware that when device is in sleep mode, it doesn't transmit anything and all caches (e.g. ARP cache, list of DHCP leases, etc.) will forget about it probably long before you'd want to send WoL packet to it, aren't you? Which means that swtich/router, implementing this kind of feature, would have to remember every single ethernet MAC address it sees (indefinitely), together with any other metadata (IP address, DHCP host name, colour of its admin's underware, breed of neighbour's dog, etc.).don't overcomplicate things. as seen in the screenshot (ip > dhcp-server > leases) it would be handy for static leases ---

## Response 288
SNMP OIDs dedicated to common and important metrics like:- Total IPv4 firewall session states- Total IPv4 L3HW offloaded firewall session states- Total IPv6 firewall session states- Total IPV6 L3HW offloaded firewall session statesYou may as well have MAX amount reached since last snmp get so we can know to what extent the device went between snmp polls.This with CPU monitoring (already available) speaks a lot to a network admin in a NMS. ---

## Response 289
DHCP matchers. I'd love to be able to match the agent-id, circuit-id, or agent+circuit-id for a lease. Would make for easy handling of option 82 data. ---

## Response 290
I suggested that too. In fact I think it would be very nice when a DISCOVER-phase script was added that gets all parameters from the DHCP packet and can decide which lease time, which address pool and which option set are to be used (or "none" to ignore the request).It would cover many special cases. E.g. I would like to handle requests on a local network differently depending on whether the MAC address is IEEE-registered or locally-assigned (random). But instead of having "MAC address / mask" as another matching criterium, it could be handled using a script. ---

## Response 291
I suggested that too. In fact I think it would be very nice when a DISCOVER-phase script was added that gets all parameters from the DHCP packet and can decide which lease time, which address pool and which option set are to be used (or "none" to ignore the request).It would cover many special cases. E.g. I would like to handle requests on a local network differently depending on whether the MAC address is IEEE-registered or locally-assigned (random). But instead of having "MAC address / mask" as another matching criterium, it could be handled using a script.absolutely. that script would need to have the lease variables exposed. The current DHCP scripts dont, you have to let the lease be created then match against it.The ability to re-write the 'match' via script would get me where I need to be.For instance, have a variable that defaults to 'match=$macaddress' and all we need to do is 'match=($agent-id . $circuit-id)' for example. When using option 82, I basically never want to match on MAC unless there is no agent-id or circuit-id , I expect the MAC to change when they swap a router or even just change their router's port or bridge configuration.I would love for this to just be a 'match= combobox-selection' thing in the DHCP server but I'll happily settle for it in scripting. ---

## Response 292
absolutely. that script would need to have the lease variables exposed. The current DHCP scripts dont, you have to let the lease be created then match against it.The current DHCP lease script is called after an address has been assigned, which is fine when you want to use it to create a DNS entry, for example, or to send an alert when new clients are detected, but it cannot be used for the use cases we have.In ISC DHCPD there was a scripting language that could be used for these cases. It could be used to assign a class to a requesting system in DISCOVER phase and that could then be used to determine all other parameters in the network definitions.(I write in past tense because this product is no longer supported)I have used this a lot, e.g. to use a different pool for systems that present a hostname that matches a certain pattern. ---

## Response 293
I would like to have logging of state changes of routes with "check-gateway".I.e. when the state of these routes changes (up to down or down to up) a message is logged with at least the dst-address, gateway, and routing-table. ---

## Response 294
Add comment field in Firewall action add-src-to-address-listWould be nice to have ability to set at comment when it is added to an address list to see for example what fw rule added the address to the list. ---

## Response 295
I would like a refresh version of the hap ac2. Pretty much exactly thesame as current. Exactly the same Case, pcb and components, except the RAM isreplaced with a 256M unit, and the Flash is replaced with a 32M Unit.(Possibly by now cheaper than the current smaller devices)I would also like a (cheap) retrofit kit, consisting of the 2 new parts, and appropriate software and instructions to transfer calibration, licensing, etc from existing to new.I would imagine the Gaming Mod people, maybe phone fixing people could do the hardware change for me.(Sadly If I attempt it, I would just wind up with a broken mess)May need an efficient mechanism for the software transfer for the person with thousands of these units.Perhaps finally a retrofit plus kit, which also includes some of themore common failing components found in these devices(As found over the years by Mikrotik and their distributors)Thanks ---

## Response 296
That is not possible because those parts are not user-serviceable (they are not socketed and not easy to solder).Furthermore, hAP ac2 is just a "throwaway device" which users would replace with something like hAP ax2 or hAP ax3 once they find the limits. ---

## Response 297
Chateau 5G R16was introduced last year, also 16MB disk device. Now you can just throw it away? A $485.00+ device still available on sale ---