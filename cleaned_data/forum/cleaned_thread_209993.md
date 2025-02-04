# Thread Information
Title: Thread-209993
Section: RouterOS
Thread ID: 209993

# Discussion

## Initial Question
RouterOS version 6.49.17 has been released in the "v6 stable" channel!Before an upgrade:1) Remember to make backup/export files before an upgrade and save them on another storage device;2) Make sure the device will not lose power during upgrade process;3) Device has enough free storage space for all RouterOS packages to be downloaded.What's new in 6.49.17 (2024-Aug-07 14:47):*) defconf - increased LTE interface wait time;*) system - fixed an issue with duplicated package list when upgrading from separated to bundled package;*) system - improved system stability for RBLDF-5nD;What's new in 6.49.16 (2024-Jun-07 10:02):(factory only release)To upgrade, click "Check for updates" at /system package in your RouterOS configuration interface, or head to our download page:http://www.mikrotik.com/downloadIf you experience version related issues, then please send supout file from your router tosupport@mikrotik.com. File must be generated while a router is not working as suspected or after some problem has appeared on the devicePlease keep this forum topic strictly related to this particular RouterOS release. ---

## Response 1
Took a couple old 6.49.15 systems to 6.49.17 with no apparent issues after 30 minutes, FWIW. ---

## Response 2
hello, how about #[SUP-92244]: The Dude limited to 5 concurrent clients ? has it solved ?P ---

## Response 3
As it was already replied, please use v7 ---

## Response 4
hi normis, it intended for mikrotik training class (espesially mtcna) where we put the dude server on main router (rb4011) but not all of students can open it from their pc / notebook as it's limited to max 5 users on the same time. ---

## Response 5
Is the training material still on 6.49.x ? ---

## Response 6
Is the training material still on 6.49.x ?I hope so, v7 is still far away from a production-ready replacement. ---

## Response 7
I hope so, v7 is still far away from a production-ready replacement.Can you give a list of why its not production-ready? ---

## Response 8
Please make 6.49.17 Long-Term.And please, create the Long-Term chain on v7 also.This will help to avoid mimimis around "v7 is not production ready". ---

## Response 9
You can't please mimimis. ---

## Response 10
And please, create the Long-Term chain on v7 also.I had to use PIM in a v7-device, it is so stable as a house of cards.Every few days a "autosupout.rif" is generated, because something crashed internally.The Multi-WAN Wireguard-route-selection was fixed only in last 7.15.3.For easy setups, maybe, v7 is stabel enough. But the moment you use it for cases ROS is designed for. Heaven forbid! Is's years away from a long-term in my eyes... Look here:https://help.mikrotik.com/docs/display/ ... l+Overviewso much red and yellow and you dream of a "long-term" :D ---

## Response 11
Is the training material still on 6.49.x ?I hope so, v7 is still far away from a production-ready replacement.Da, da, da ---

## Response 12
hello, if possible, please add the following features (security reasons) for users who log-in into router :+ max active session on the same time for each apps; winbox, telnet, ssh, etc+ automatic logged out if inactive during certain durationthank you ---

## Response 13
You still forgot my #[SUP-126246]: Winbox IPv6 ND reachable time units. Cosmetic bug (works correctly and the value is specified in seconds, only Winbox and Webfig show wrong units label "ms" instead of "s"), but introduced in 6.47.10 which itself was a long-term release.Reported exactly one year ago, and the response was: "This has been fixed in RouterOS V7, in RouterOS V6 branches this won't be fixed as V6 updates will only include security fixes." (yeah, so the long-term 6.47.10 showing the wrong units was a security fix?)I plan to stick with v6 for a long time on RB931/RB941-2nD (the cheap basic routers which I give to customers for free with the service, tired of supporting cheap crappy chinese routers), simply because of limited hardware resources. ---

## Response 14
What's new in 6.49.16 (2024-Jun-07 10:02):(factory only release)Out of sheer curiosity - what device was released to the market with 6.49.16 factory installed?I plan to stick with v6 for a long time on RB931/RB941-2nD (the cheap basic routers which I give to customers for free with the service, tired of supporting cheap crappy chinese routers), simply because of limited hardware resources.I wonder how long v6 is going to get updates, most of my switches are on v6 long-term and I don't really see any reason to update them to v7 unless I have no other option (somewhat old hardware). ---

## Response 15
I think most of the MIPS hardware gets v6 in factory still - given they are manufactured still.But what makes me wonder more than that:why was it necessary to release 6.49.16 without a single actual change? This maybe only makes sense for the purpose of raising the "factory-software version" property in routerboard. But why was this necessary? ---

## Response 16
Perhaps some of those v6-only hardware got R2 (with some slight HW changes, requiring minor changes in some device driver?) Since such change doesn't apply to already shipped hardware, ROS change can be factory-only (and it doesn't have to be publicly available since new devices can not be downgraded to older ROS to be upgraded to such factory-only version). The only problem is if owner of such R2 device wants to netinstall the device (in which case he'd probably get necessary files from MT support). ---

## Response 17
Well, why not just mention that in changelog?"*) add support for model xzy rev4"all way too mysterious ---

## Response 18
Well, why not just mention that in changelog?When did MT make changelogs easily understandable? ---