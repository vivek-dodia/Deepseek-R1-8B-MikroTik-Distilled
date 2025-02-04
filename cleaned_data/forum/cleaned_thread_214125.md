# Thread Information
Title: Thread-214125
Section: RouterOS
Thread ID: 214125

# Discussion

## Initial Question
Hello, I have the following two open tickets at help.mikrotik.com:SUP-176047 (problem with OSPF over ZeroTier)SUP-168963 (Routing process lockup that persists reboots)Both of them had been replied initially by support, then I replied back and now both are in the "waiting for support" status. The first one for one week and the second one since Nov 14(!). Both of them are important: the older one reported an occasional routing process lockup that persisted after reboots, while the newer ticket refers to multicast traffic (by OSPF but could also be relevant to other cases) not getting through a router-hosted ZeroTier network.I have been using Mikrotiks for over 15 years and i can safely say that I don't spam support. I actually revert to it after researching each problem. In the case of OSPF, I attampted to find an answer via the forum before opening the ticket. Why are these two questions neglected? How often do you guys at Mikrotik check for and reply to tickets? ---

## Response 1
Just so you know ...This is a user forum with users helping other users.Sometime MT staff pops in but certainly not all the time nor everywhere.So while I do understand your problem and your need to ventilate, you may get a lot of sympathy here but maybe not much resolution.Unless Normis or EdPa step in ... ---

## Response 2
Just so you know ...This is a user forum with users helping other users.Sometime MT staff pops in but certainly not all the time nor everywhere.So while I do understand your problem and your need to ventilate, you may get a lot of sympathy here but maybe not much resolution.Unless Normis or EdPa step in ...I know, but I also know that MT staff reads the forum. And so I hope that someone will see my post (and also any sympathy replies) and do something about this, since I cannot believe that this is an isolated issue. ---

## Response 3
If you login to Jira at help.mikrotik.com, you should be able to find your ticket. You can add a comment to ask for an update and/or add another supout.rif with the problem.Although, sometimes they don't say anything, if they think it's a problem and don't have an answer (and they escalated).Normally they respond in a few days if they think it NOT a valid issue. ---

## Response 4
If you login to Jira at help.mikrotik.com, you should be able to find your ticket. You can add a comment to ask for an update and/or add another supout.rif with the problem.Although, sometimes they don't say anything, if they think it's a problem and don't have an answer (and they escalated).Normally they respond in a few days if they think it NOT a valid issue.I see... So they may (or may not) be working on both issues I reported.Thanks. ---

## Response 5
LOL. They are bad about "progress"... it's either fixed, your problem, or in limbo. I'm just offering hope - it being "open" rather than closed is in keeping with Mikrotik's minimalist communications. And by adding a comment, you go back to top of someone's queue I think.On your OSPF+ZeroTier issue, it may not hurt to try 7.18beta2. Sometimes these problems get fixed by some unrelated bug fix. And/or that a good reason to update your case (i.e. it's still not fixed in 7.18...) ---

## Response 6
@nkourtzis - Just curious, why are you using OSPF on top of ZeroTier? ---

## Response 7
Just to link the threads, this is kinda a continuation of this one:viewtopic.php?t=213760And @Larsa as usual has a good point... I got a bit distracted by RoMON in your other thread...But if everything is connected by ZeroTier, you can use its route distribution system, instead OSPF to edges. The routes do NOT have be ZT IPs - it really does "inject" any routes defined on the controller as-is into the client/peer/member's route table. This might avoid all the complexity of OSPF and ZT's handling of multicast. ---

## Response 8
@nkourtzis - Just curious, why are you using OSPF on top of ZeroTier?I have chosen ZeroTier as the easiest way to create a WAN with 70+ nodes that will be reasonably secure and work over different types of upstream connections, NATted/not-NATted, ISP firewalls, etc.I want these nodes to be able to route to each other via the ZT network. Since the network will be large, I am trying to avoid the recurring costs of a ZT subscription and thus I am using the built-in controller of RouterOS instead of the cloud-based one by ZT. Unfortunately, it looks like this part of RouterOS has not got the attention and care it needs, especially in the controller part, which looks quite neglected. For example, there is no option to create or edit any rules, unlike the online dashboard provided by ZT. Also, although it should be able to act as a switch and pass multicast/broadcast traffic, it obviously does not, or at least not in all cases.I thought of using OSPF because it can detect neighbors automatically, even in large numbers. My goal, as said above, is to exchange routes between them. But any type of OSPF network that uses broadcast (or multicast) to detect neighbors, fails to detect anything on ZT. If the neighbors are set up manually (and the network type set to nbma or ptmp), it works. But setting up so many clients by hand is something I would like to avoid, if possible. ---