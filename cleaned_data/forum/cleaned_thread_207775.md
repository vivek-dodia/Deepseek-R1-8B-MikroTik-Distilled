# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 207775

# Discussion

## Initial Question
Author: Mon May 20, 2024 6:11 pm
I am observing frequent yet not 100% repeatable cases where a console command aimed at removing all items from a given list (remove [find]to be exact) gets stuck while executing. The following is true:Happens to different collections of items, e.g. /ip/dhcp-server remove [find], /interface/bridge remove [find] and so on.Happens both when the target collection of items is non-empty and empty.Happens both in the script as well as a standalone call in the terminal window, but seems like it happens more often when running from a script.Happens in about 20% of calls.Sometimes never completes, sometimes takes very long time to complete, but still finishes, sometimes takes long time and then exits with a timeout message.RouterOS 7.14.3 (most current stable version)Hence the questions:Why such a trivial call would get stuck, especially in non-deterministic manner? Is there a way to prevent it from getting stuck by performing some preparatory actions?Is there another, more reliable way to remove all items from a given collection that would not cause the execution to get stuck?Update 1:Upgraded to recently released 7.15.1, same problem, same place.Happens on multiple CRS354-48P-4S+2Q+ switches (MIPSBE-based, I own 11 of them)Never happens on CCR2004-1G-12S+2XS and CCR2216-1G-12XS-12XQ routers (both ARM64-based)Can be reproduced even without remove command, it is [find] that gets stuck (for example, :put [find])print gets stuck too when called from the script, similarly to :put [find]If the script gets stuck and then interrupted, running it again always results in getting stuck againHappens specifically to /interface/bridge and /ip/dhcp-server collectionsThis is gotta be some kind of race-condition-based bug in MIPSBE version of RouterOS. Can anybody from MikroTik debug this?Update 2 (solution):I solved the problem, here is TLDR (full solution in the thread below)Only happens on MIPS-based switchesHappens when you are trying to delete a bridge configuration that uses interface lists to specify portsRemoving interface list containing a lot of ports (like 48 for example) from the bridge port list just prior to attempting to remove the bridge itself causes an unexplained spike in CPU load to 100% that lasts for several minutes after apparent completion of the operation (which will effectively hang subsequent attempt to remove the bridge itself)The way to avoid this problem is to remove the bridge from the bridge list first, and only then dismantle that bridge's ports by removing interface list from the bridge port listBasically shut down the bridge first, and then take care of its ports, do not manipulate ports on active bridge ---

## Response 1
Author: Mon May 20, 2024 7:56 pm
``` :localretryCmdOnErrordo={:if(retryCnt=null)do={:set$retryCnt1}:onerror errin={$cmd}do={:if($retryCnt<$maxRetry)do={:return[$retryCmdOnError retryCmdOnError=$retryCmdOnError cmd=$cmd retryCnt=($retryCnt+1)maxRetry=$maxRetry]}else={:error $err}}}# edit cmd function with command(s) for error handling:localcmddo={<some_cmd>}# adjust maxRetry argument if needed to max amount of retries on error$retryCmdOnError retryCmdOnError=$retryCmdOnError cmd=$cmd maxRetry=5 ``` I doubt it is because of error while removing dynamic objects because it will stop on error, not stuck or go in timeout. Could be device performance issue or storage corruption.Regarding removing dynamic objects and error handling with retry (but it doubt that's the case here), it can be solved with simple script function:
```
---
```

## Response 2
Author: Mon May 20, 2024 9:04 pm
``` /interface/bridge/portremove[findwhere!dynamic]/interface/listremove[findwhere!builtin] ``` ``` /ip/dhcp-serverremove[find]/interface/bridgeremove[find] ``` Does that happen on "static" or "dynamic" lists?I.e. is this the case?viewtopic.php?f=9&t=154606&p=853803#p853800I am only trying to clear simple static lists, so no, it is not related to lists where items can disappear on their own in the middle of command execution like described in the post you are referring to.Furthermore, in cases where the list can contain dynamic or built-in items, I am taking additional precautions like:
```
However, where it does gets stuck are simple lists where only static, previously manually added items can be present:
```

```
Of note, it can happen both when the list is not empty and when the list is empty. And it only happens from time to time, not every time.


---
```

## Response 3
Author: Mon May 20, 2024 9:25 pm
``` :put[:time{/interface/bridge/port find}]] ``` ``` :put[/interface/bridge/port find]# *1;*2;...:put[:time{/interface/bridge/portremove*1;*2;...}] ``` Hmm. Does doing just the [find] work, or is it in the "remove" part.There is the :time command to see how things take. Be curious what if it's the "find" part or the "remove" works.
```
And/or try if you using the list as a string to "remove":
```

```
---
```

## Response 4
Author: Sat Jun 22, 2024 8:06 pm
``` :put[:time{/interface/bridge/port find}]] ``` ``` :put[/interface/bridge/port find]# *1;*2;...:put[:time{/interface/bridge/portremove*1;*2;...}] ``` ``` :put"1":localids[find]:put"2"remove$ids:put"3" ``` Hmm. Does doing just the [find] work, or is it in the "remove" part.There is the :time command to see how things take. Be curious what if it's the "find" part or the "remove" works.
```
And/or try if you using the list as a string to "remove":
```

```
OK, I followed your advise. It always gets stuck in [find] part, never even proceeds to the remove part. Here is even simpler code to test this:
```

```
When it gets stuck, it shows 1, then never shows 2.Other observations:If I interrupt (Ctrl-C) stuck script, then run it again, it still gets stuck in the same place every time.If I interrupt stuck script, then execute :put [find] as a standalone command, then run the script again, it does not get stuck.


---
```

## Response 5
Author: Sat Jun 22, 2024 9:45 pm
Could be device performance issue or storage corruption.I own 11 identical switches and it gets stuck on all of them in the same place (/interface/bridge and /ip/dhcp-server), so no, it is not a hardware problem of a specific switch. ---

## Response 6
Author: Sat Jun 22, 2024 10:07 pm
Updates after more experimenting:Upgraded to recently released 7.15.1, same problem, same place.Happens on multiple CRS354-48P-4S+2Q+ switches (MIPSBE-based, I own 11 of them)Never happens on CCR2004-1G-12S+2XS and CCR2216-1G-12XS-12XQ routers (both ARM64-based, I own two and one of each correspondingly)Can be reproduced even without remove command, it is [find] that gets stuck (for example, :put [find])print gets stuck too when called from the script, similarly to :put [find], again, NOT every time, there is some randomness to itIf the script gets stuck and then interrupted, running it again always results in getting stuck againHappens specifically to /interface/bridge and /ip/dhcp-server collectionsThis is gotta be some kind of race-condition-based bug in MIPSBE version of RouterOS. Can anybody from MikroTik debug this? ---

## Response 7
Author: Sat Jun 22, 2024 10:24 pm
Is this happening in /system/script or via the CLI.If it's the CLI, a local is gone upon the next prompt - so it's nil [:nothing]. You'd need some curly braces at CLI:/interface/bridge/vlans { :local x [find]; remove $x }You may also want to qualify the "find" as things can be weird in scripting sometimes. So if you mean /interface/bridge/port/find ... use the full form to see if it works then. ---

## Response 8
Author: Sat Jun 22, 2024 11:18 pm
``` /interface/bridge:put" 1":localids[/interface/bridge/find]:put" 2"remove$ids:put" 3" ``` Is this happening in /system/script or via the CLI.If it's the CLI, a local is gone upon the next prompt - so it's nil [:nothing]. You'd need some curly braces at CLI:/interface/bridge/vlans { :local x [find]; remove $x }This is what I am doing:Upload a script file to /file using WinBox GUIRun it from CLI using the following command: import file-name=my_script.rscSo local persists while the script is running, I even confirmed it with debug output (:put $ids)You may also want to qualify the "find" as things can be weird in scripting sometimes. So if you mean /interface/bridge/port/find ... use the full form to see if it works then.I have just tried it, same result - [/interface/bridge/find] gets stuck
```
I also tried to run the same script by first creating a script entry in /system/script (both from terminal and GUI) and it gets stuck equally well.


---
```

## Response 9
Author: Sun Jun 23, 2024 4:23 am
``` :put[/interface/bridge/find] ``` Is this happening in /system/script or via the CLI.I also tried to run the same script by first creating a script entry in /system/script (both from terminal and GUI) and it gets stuck equally well.The hang is just weird. If same script works on ARM, does sound like a bug.Using a :local in a :import script without it being inside {} might be allowed/okay, but still not my recommendation. Does doing just a plain:
```
at CLI also hang?The only thing to try is add some condition to the find, like adding as [find name~"*"] which match all names.  Perhaps it needs some filter - it shouldn't, but that might avoid the hang (or at least be another data point for a bug report).


---
```

## Response 10
Author: Sun Jun 23, 2024 4:50 pm
``` :put[/interface/bridge/find] ``` ``` :put"Resetting device configuration"# Clear all the lists:put" Clearing bridge port list"/interface/bridge/port:localids[findwhere!dynamic]remove$ids:put" Clearing bridge list"/interface/bridge:put" 1":localids[/interface/bridge/findwherename~"*"]:put" 2"remove$ids:put" 3" ``` ``` Resettingdevice configurationClearingbridge port listClearingbridge list1interrupted ``` Using a :local in a :import script without it being inside {} might be allowed/okay, but still not my recommendation. Does doing just a plain:
```
at CLI also hang?Yes, it does occasionally, but in my observation it happens much less frequently. Roughly speaking, the script hangs in about 20-40% of runs any day of the week, but a plain CLI single-liner hung at most twice in the last month that I was trying to debug this problem.The only thing to try is add some condition to the find, like adding as [find name~"*"] which match all names.  Perhaps it needs some filter - it shouldn't, but that might avoid the hang (or at least be another data point for a bug report).Yes, gets stuck too:
```

```
Results in:
```

```
(here "interrupted" line is a result of me pressing Ctrl-C after waiting for a long time)


---
```

## Response 11
Author: Sun Jun 23, 2024 6:53 pm
``` :put"Resetting device configuration"# Clear all the lists:put" Clearing bridge port list"/interface/bridge/port:localids[findwhere!dynamic]remove$ids:put" Clearing bridge list"/interface/bridge:put" 1":localids[find]:put" 2"remove$ids:put" 3" ``` ``` # [ Configuration ]:localConfigDoClean1;:localConfigDoLAN1;# [ Lookup data ]:localPortListLAN{"ether1";"ether2";"ether3";"ether4";"ether5";"ether6";"ether7";"ether8";"ether9";"ether10";"ether11";"ether12";"ether13";"ether14";"ether15";"ether16";"ether17";"ether18";"ether19";"ether20";"ether21";"ether22";"ether23";"ether24";"ether25";"ether26";"ether27";"ether28";"ether29";"ether30";"ether31";"ether32";"ether33";"ether34";"ether35";"ether36";"ether37";"ether38";"ether39";"ether40";"ether41";"ether42";"ether43";"ether44";"ether45";"ether46";"ether47";"ether48";};# [ Reset ]:if($ConfigDoClean)do={:put"Resetting device configuration"# Clear all the lists:put" Clearing bridge port list"/interface/bridge/port:localids[findwhere!dynamic]remove$ids:put" Clearing bridge list"/interface/bridge:put" 1":localids[find]:put" 2"remove$ids:put" 3":put" Clearing interface list"/interface/list:localids[findwhere!builtin]remove$ids:put" Clearing interface member list"/interface/list/member:localids[find]remove$ids};# [ Configure LAN ]:if($ConfigDoLAN)do={:put"Configuring LAN"# Port/interface settings:put" Configuring LAN interface list"/interface/listaddname=InterfaceList.LAN/interface/list/member:foreachPortin=($PortListLAN)do={addinterface=$Port list=InterfaceList.LAN}:put" Configuring LAN bridge"/interface/bridgeaddname=Interface.LAN/interface/bridge/portaddbridge=Interface.LANinterface=InterfaceList.LAN}; ``` OK, I think I am getting somewhere. At least I am now able to reproduce the problem deterministically.Steps to reproduce (for your convenience I have automated most of these steps in the script at the end of the message):Need to use MIPS-based CRS354-48P-4S+2Q+ switch (you won't reproduce the problem on ARM64-based routers)Connect to the device via MGMT Ethernet port (ether49) using WinBoxCreate custom interface list and add all 48 Ethernet ports to that list as list members (this can be automated in a script). Do not include ether49 to this list unless you want to suffer from your WinBox connection being reset in the next step.Create a bridge and add previously created interface list to its ports list (this can be automated in a script)Open /System/Resources GUI dialog to monitor CPU load(no, WinBox dashboard CPU load gadget does not faithfully report true CPU load, so do use /System/Resource GUI dialog!)Ensure that CPU load in GUI dialog isnot100%. If it is, do not proceed until it settles down.Run a script that does the following in one shot: first removes all non-dynamic items from /interface/bridge/port and then removes all items from /interface/bridge:
```
The script will get stuck in its second part (removing all items from /interface/bridge). To be more exact, it will get stuck just finding all such items.Observe CPU load - it will now be 100%Interrupt the script by pressing Ctrl-CObserve CPU load - it will still be 100% for a few minutes.Without waiting for CPU load to drop down, run the script again - it will get stuck again in exact same place - attempting to read a list of /interface/bridge/. It will be getting stuck every time you keep running it while the CPU load is still 100%. Interrupt the script by pressing Ctrl-C.Go get some tea/coffee and wait for the CPU load to drop down from 100% back to normal values. It will take several minutes.Run the script again - this time it won't get stuck. The difference this time - it has nothing to delete in /interface/bridge/port anymore in the first portion of the script, so the CPU remains unloaded and proceeds to the second step where it does not get stuck anymore.Conclusion:It takes a combination of the following for the script to get stuck:Loading the CPU with removing one non-dynamic list-type item from /interface/bridge/port, which in turn causes an automatic removal of 48 dynamic items.And then immediately proceeding to an /interface/bridge [find] call which gets stuck.Important caveats:Notice that if /interface/bridge/port is already empty, there will be no spike in CPU load and the script will not get stuckNotice also that when /interface/bridge/port isnotempty, control returns immediately and successfully from removal of the /interface/bridge/port and corresponding GUI window shows immediate and successful disappearance of all items from this list (both static and dynamic), yet the CPU remains overloaded for a while after this operation and can't correctly handle subsequent operations.As a matter of fact, you don't even need a script to reproduce a CPU overload - you can simply remove one non-dynamic list-type item from /interface/bridge/port in GUI and watch the CPU go into 100% overload for the next two minutes for no particular reason (while all items, both dynamic and static are immediately gone from the list).Here is a unified script that will reproduce both setup and the problem (it won't get stuck first time you are running it because it first cleans up and then sets up, so run it twice).
```

```
At this point I have done everything I could to deterministically reproduce the problem, I think now it is time for someone from MikroTik to fix it as soon as Līgo is over.


---
```

## Response 12
Author: [SOLVED]Sun Jun 23, 2024 9:40 pm
``` # [ Configuration ]:localConfigDoClean1;:localConfigDoLAN1;# [ Lookup data ]:localPortListLAN{"ether1";"ether2";"ether3";"ether4";"ether5";"ether6";"ether7";"ether8";"ether9";"ether10";"ether11";"ether12";"ether13";"ether14";"ether15";"ether16";"ether17";"ether18";"ether19";"ether20";"ether21";"ether22";"ether23";"ether24";"ether25";"ether26";"ether27";"ether28";"ether29";"ether30";"ether31";"ether32";"ether33";"ether34";"ether35";"ether36";"ether37";"ether38";"ether39";"ether40";"ether41";"ether42";"ether43";"ether44";"ether45";"ether46";"ether47";"ether48";};# [ Reset ]:if($ConfigDoClean)do={:put"Resetting device configuration"# Clear all the lists# Reverse, counterintuitive removal order - bridge first, then bridge ports - ensures that CPU does not go into 100% load for several minutes:put" Clearing bridge list"/interface/bridge:put" 1":localids[find]:put" 2"remove$ids:put" 3":put" Clearing bridge port list"/interface/bridge/port:localids[findwhere!dynamic]remove$ids:put" Clearing interface list"/interface/list:localids[findwhere!builtin]remove$ids:put" Clearing interface member list"/interface/list/member:localids[find]remove$ids};# [ Configure LAN ]:if($ConfigDoLAN)do={:put"Configuring LAN"# Port/interface settings:put" Configuring LAN interface list"/interface/listaddname=InterfaceList.LAN/interface/list/member:foreachPortin=($PortListLAN)do={addinterface=$Port list=InterfaceList.LAN}:put" Configuring LAN bridge"/interface/bridgeaddname=Interface.LAN/interface/bridge/portaddbridge=Interface.LANinterface=InterfaceList.LAN}; ``` Wow, I might have just found a workaround to this problem:Turns out if you do removal inopposite, counterintuitive order (bridge first, then bridge ports), nothing gets stuck and the CPU does not go into two minutes of overload.So this is how a modified script looks like:
```
Even if you do not do any scripting and merely using WinBox GUI, this equally applies to you as well. So the rule is:When removing the bridge configuration made with interface list, first remove the bridge itself, and only then clean up the bridge ports assignment.If you remove bridge port assignment first while the bridge is still active, this will cause about two minutes of CPU doing who knows what at 100% load factor after seemingly successfully completing the operation.Huge thanks to @Amm0 and @pe1chl for pointing me in several productive directions!
```