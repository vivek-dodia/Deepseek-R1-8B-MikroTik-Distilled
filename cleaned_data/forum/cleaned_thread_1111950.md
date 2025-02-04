# Thread Information
Title: Thread-1111950
Section: RouterOS
Thread ID: 1111950

# Discussion

## Initial Question
SwOS Lite version 2.18 releasedhttp://www.mikrotik.com/downloadWhat's new in v2.18:*) added option to set forced 2.5G for SFP+ ports;*) css610: added a distinct "Health" menu;*) css610pi: updated PoE firmware;*) fixed multicast forwarding after disabling IGMP snooping;*) fixed SNMP ifSpeed OID reporting in certain cases;*) ftc11xg: fixed DHCP packet forwarding;*) limit the number of displayed GUI "Hosts" entries up to 512;*) improved SwOS Lite web interface stability and responsiveness; ---

## Response 1
Glad to see there is still development for this version.*) added option to set forced 2.5G for SFP+ ports;How do you set this ?Never mind, found it. Disable autonegotiation and then you can select. ---

## Response 2
Follow up:On CSS610 I set an S+RJ10 to forced 2.5Gb, connected to ether1 of AX3 using VLAN trunk.Link becomes active. So far so good.On AX3 log files I see it determines speed as being 2.5Gb, which is ok however ...nothing passes (after the facts I can see in log files what happened).Only when I enable autonegotiation, I can get access via that link.Am I missing something ? ---

## Response 3
can we please please please get option 82 in swos lite! ---

## Response 4
Follow up:On CSS610 I set an S+RJ10 to forced 2.5Gb, connected to ether1 of AX3 using VLAN trunk.Link becomes active. So far so good.On AX3 log files I see it determines speed as being 2.5Gb, which is ok however ...nothing passes (after the facts I can see in log files what happened).Only when I enable autonegotiation, I can get access via that link.Am I missing something ?You should probably disable Auto Negotiation and fix it at 2.5Gbps on AX3 ether1 too... ---

## Response 5
You should probably disable Auto Negotiation and fix it at 2.5Gbps on AX3 ether1 too...When setting speed fixed on AX3 -> No Link on CSS610, both with auto and no autonegotiation.Also visible on AX3, ether lights go out for that port. ---

## Response 6
When auto negotiation is disabled you often need a crossover cable. Auto-crossover is often also disabled if auto negotiation is disabled ---

## Response 7
I understand what you say but I don't understand why that would be needed... doesn't make sense from a practical point of view.Auto MDX is something from the previous century !Anyhow, SUP-146041 created. Let's see what support says about it. ---

## Response 8
I understand what you say but I don't understand why that would be needed... doesn't make sense from a practical point of view.Auto MDX is something from the previous century !Anyhow, SUP-146041 created. Let's see what support says about it.Actually I believe onnoossendrijver is correct, modern ethernet controllers use standard IEEE 802.3ab auto negotiation protocol to automatically determine MDI, speed and duplex and for a practical standpoint it makes perfect sense, and once you disable auto negotiation you must use crossover cable... ---

## Response 9
Got response from support.Some info provided both from CSS610 and AX3.In parallel I ordered some CAT6 cross-convertor plugs.We'll see ... ---

## Response 10
Final ordeal:it's (again) S-RJ10 acting up. It can not be controlled to set lower speed. ---

## Response 11
[quote=holvoetn post_id=1061562 time=1709846844 user_id=185526]Final ordeal:it's (again) S-RJ10 acting up. It can not be controlled to set lower speed.[/quote]Which revision of S-RJ10 are you using? There is a Rev 2Read about it ---

## Response 12
It is Rev 2.That module will adjust on its own to lower speed when needed (e.g. when connected to 2.5G port of AX3) but it can not be configured to do so (e.g. when connecting 2 S-RJ10 to each other and not wanting full 10G because it will burn your fingers). ---

## Response 13
Yeah they get really hot.I've read that they need to be set at a fixed speed.Can you try this on RouterOS also if you have CRS somewhere? ---

## Response 14
Good to see more development, I'm running a few Netpower Lite 7R devices currently at 2.17.Please consider feature requests for new releases:- option to not save all config changes immediately, instead keep them only in RAM, and have a separate "Save" button (this way previous working config can be restored by reboot/power-cycle if you lost access due to wrong change)- option to reboot (optionally including power-cycling the PoE powered device) after some number of failures to get IP address by DHCP, to recover from wrong config change or hung uplink radio without power-cycle (tricky to do with reverse-PoE redundant power from multiple customers) ---

## Response 15
If I go to the hosts screen... after about 20 seconds I get this at the top of the screen.ERROR: SyntaxError: Unexpected token '{' ---

## Response 16
yup, same here on two css610 ---

## Response 17
I'm not seeing that.Edge as browser on Win11. ---

## Response 18
If I go to the hosts screen... after about 20 seconds I get this at the top of the screen.ERROR: SyntaxError: Unexpected token '{'Confirmed on CSS610: ---

## Response 19
I'm not seeing that.Edge as browser on Win11.O..K ...it took a LOT longer then 20 seconds (just left the window open while I was doing something else).Now I see it as well. ---

## Response 20
It is always a good practice to refresh the page to avoid these kind of errors... ---

## Response 21
Help, I can consult in this forum, I only get a reply and when I reply I get ---

## Response 22
I was about to update a CSS610-8P. When I go to update it doesn't show the 2.18 firmware.Did something change or get taken down?https://cdn.mikrotik.com/swoslite/css61 ... i-2.18.binGives me a 503 errorEDITWent back to the Switch and Hit Upgrade and it found the upgrade and installed it.For some reason Chrome won't load the page now... but I need to look into that some more. ---

## Response 23
I can confirm the syntax error in the Hosts tab after upgrade to 2.18. Fresh Netpower Lite 7R device (default config) upgraded from factory 2.13 firmware. Tried two different browsers (Firefox and Supermium), I've never seen this error in 2.17 or older. Refreshing the page doesn't change anything, and actually Supermium shows the error when freshly started accessing the upgraded device (it was upgraded using Firefox) for the first time.EDIT: Downgraded to 2.17 -https://cdn.mikrotik.com/swoslite/css61 ... 0-2.17.bin- link edited from 2.18 (fortunately it works, as I haven't seen a "download archive" web page for SwOS/Lite, only for RouterOS). Hosts table displayed just fine, no more syntax errors in both browsers. ---

## Response 24
I upgraded from 2.17 to 2.18 and I receive the error on the Hosts page: ERROR: SyntaxError: missing ) in parentheticalI have the CSS610-8P and CSS610-8G models. ---

## Response 25
Also... I have ICMP ping set up in netwatch to the CSS610-8P.Every once in a while it will miss more than 2 of the 5 pings. I get an error note on the router as that's where netwatch is running, which is directly connected to the switch.But since CSS has no logs... I can't track that.I have 4 CSS610-8P out there at this point. They all do this. ---

## Response 26
Are the missing pings new with 2.18, and fixed by downgrade to 2.17? (warning: can't downgrade lower than 2.17 without losing config because of changed config file format - sadly still not hashing the login password, so let's hope for another incompatible change soon).Over a month has passed and still no fix to that 2.18 syntax error bug? Makes hosts table useless. I'm running 2.17 and waiting for a fix. ---

## Response 27
A few months have passed - any news about a new bugfix release of SwOS Lite?I'm still running 2.17 everywhere because of the syntax errors in the hosts table on 2.18.Has the SwOS Lite development been outsourced, or has the last employee working on it already left?Put the source on github already :)Most of the value is in the hardware anyway, few companies make outdoor reverse-PoE switches.Some new features would be nice but I'm losing hope if even a simple bugfix takes so long.One that would have saved me a lot of trouble more than once - PoE watchdog (power-cycle the powered device if the switch can't get DHCP for too long, with configurable timeout - like 15 minutes or so, to avoid rebooting during OS upgrades).It's quite a challenge to ask a few customers to power-cycle their PoE adapters exactly at the same time (so there is a moment when all are off - only then will the switch reboot, because of redundancy - even though not the switch itself was hung, but the powered Cube radio). ---

## Response 28
#[SUP-161444] reported 2024-08-06 - still no response ---

## Response 29
Most of the value is in the hardware anyway, few companies make outdoor reverse-PoE switches.Your device is a dumb power consuming nothing without SwOS. So don't talk BS. And Mikrotik won't open source SwOS anyways. It wouldn't help you either way, as bugs are not fixed by just the action of publishing the source code.PS:Reply in your support ticket directly. Ask for acknowledgement at least. Publishing SUP numbers on the community forum has no effect. ---

## Response 30
Without SwOS it would probably be an unmanaged reverse-PoE switch (assuming the switch chip has some sane power-up defaults), limited (no VLANs etc.) but still somewhat useful. Before the netpower lite 7R there were chinese reverse-PoE switch boards but I coulnd't find them nicely packaged in an outdoor case which is what MT did and I appreciate it, so I don't have to roll my own ugly outdoor boxes anymore. If source was published with change history, it would be possible to find the specific commit that broke the Hosts table and revert just that, while keeping other changes that fix bugs or add new features. I'm also pretty sure the community would help with more bug fixes and new features. Hey, no password hashing in 2024 - even if using the old Unix V7 crypt() it would be better than nothing. I wouldn't be asking for the source if it was properly maintained, but it doesn't seem to be. New release is made that introduces an obvious easily reproducible bug (which shouldn't have passed the QA if there was any), and no fix in a few months. All I got from the report to support@ was the auto-ack with the SUP number, but no follow-up from any live person - not even the usual "we are working on it, but can't give any ETA". ---

## Response 31
Any news in support ticket ? ---

## Response 32
Still no news, running SwOS lite 2.17 on all my netpower lite 7r switches for now as it works for me, my theory (just a guess, pure speculation) is that SwOS Lite development is outsourced and MT has to pay for each new release, or have difficulty to find a contractor who wants to work on this code (perhaps it's so hairy that anyone resigns after shipping just one release), that could explain the "release late, release rarely" development philosophy.Prove me wrong and just fix the damn Host table syntax errors already, it's an obvious bug easily reproducible in default configuration. ---

## Response 33
Update:We have managed to reproduce the issue locally in our labs and look forward to fixing it on upcoming SwOS lite versions, unfortunately, I cannot provide a release date now.Fingers crossed...Still it would be very welcome to see a refresh of these switches - the switch chip is good, just add a better CPU and memory so the switch can be managed with RouterOS and have all CRS3xx-like features for like $10 extra BOM cost. ---

## Response 34
I was just about to buy a couple of CSS610-8G-2S+IN (plus SFP+ modules) and came here to see what this "Lite" version of SwitchOS is all about. I already wondered how well it's maintained, given that there are only2-3 productsrunning it. Unfortunately, my concern was justified - more than eight months and no fix yet? I really love my Mikrotik gear but this is apparently a failed strategy. I can't buy (current) products that are effectively abandoned software-wise. As the previous post said, drop SwitchOS Lite and bump the (very nice) hardware a little instead.Please Mikrotik, I know you're better than this! ---

## Response 35
I had the switch just stop passing traffic for 5 minutes.It suddenly started working again.I messaged Mikrotik about it... But can't send logs, as there are none.A month later I got a message that they had reproduced the lock up. I was sent a firmware that addresses the lock up. But not the hosts table. I installed it this week and am "waiting". ---