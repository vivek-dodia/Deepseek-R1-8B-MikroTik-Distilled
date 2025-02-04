# Thread Information
Title: Thread-1122807
Section: RouterOS
Thread ID: 1122807

# Discussion

## Initial Question
Updated hAP ac2 (RBD52G-5HacD2HnD) from version 7.12.1 to 7.16.2There are a lot of unnecessary entries in the Log. I can't turn off the excess. ---

## Response 1
The "!dns !package" log rule will mean "debug" (or anything NOT dns and NOT package - which is a log. In general, the "double negative" rules really make it difficult to predict what will happen since it's essentially "everything else"... So may be more OTHER entries beyond "!dns !package" that's including a lot of extra entries. ---

## Response 2
Yeah that rule makes no sense. You have turned on ALL POSSIBLE LOGS from all functions, except DNS and package installs ---

## Response 3
Yeah that rule makes no sense. You have turned on ALL POSSIBLE LOGS from all functions, except DNS and package installsWhat is correct then? ---

## Response 4
What is correct then?Depends: what is "correct"? What kind of logging are you expecting? ---

## Response 5
!dns ---

## Response 6
Don't use !! means "everything except DNS" ---

## Response 7
Please change the title like "I do not understand correctly how set the logs", is not a RouterOS problem.Now I'm writing you what the others who answered did NOT deduce from your screenshot...@K0NCTANT1NYou completely got it all wrong.!ntp also logs literally everything, except ntp... so it logs ALSO dns, packet ...It's not a firewall that as you add rules to block something, so it doesn't appear... each ruleADDSsomething to the logs.First of all delete all the mess you made by pasting this in the terminal (reset all logs to defaults, but not the actions submenu):
```
/system loggingset0action=memory disabled=noprefix=""topics=infoset1action=memory disabled=noprefix=""topics=errorset2action=memory disabled=noprefix=""topics=warningset3action=echo disabled=noprefix=""topics=criticalremove[findwheredefault=no]After that, what you exactly want log that is not already logged by defaults rules?Add a rule for that, for eample for log NTP(*) addntp,!debug(remember toavoid everytime debugon new rules, if is not relally needed)(is not needed to add !debug on default rules. Debug is never used with critical/error/warning/info)What you exactly want NOT log that is already logged by defaults rules?MODIFY default rule for that. For example for avoid useless DHCP warning, add !dhcp on defaultwarningrule.And so on...(*) NTP not already logged by critical/error/warning/info, for avoid duplicates, add on newntp,!debugrule also!critical !error !warning !infothat are already logged by default rules.

---
```

## Response 8
Don't use !! means "everything except DNS"How can I remove unnecessary (garbage) from the log? ---

## Response 9
Don't check the boxes in each of those logs in System>Logging for "dns", "wireguard", "ntp", "dhcp". You DO want the checkbox enabled for "!debug", "!packet", "!raw" things, under the "Topics".Liketopics=wireguard,!debug(while from your screenshot you have something liketopics=!wireguard,!debugIf that does not make sense, can you do a "/system/logging export" cut-and-paste from Terminal, and post that here? ---

## Response 10
How can I remove unnecessary (garbage) from the log?You have done what I wrote on post #8?viewtopic.php?t=214019#p1121110 ---

## Response 11
How can I remove unnecessary (garbage) from the log?You have done what I wrote on post #8?viewtopic.php?t=214019#p1121110Yes ---

## Response 12
what yo do not want log anymore?(screenshot is better to not omit details) ---