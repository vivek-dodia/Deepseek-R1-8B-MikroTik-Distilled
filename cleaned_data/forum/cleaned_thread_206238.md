# Thread Information
Title: Thread-206238
Section: RouterOS
Thread ID: 206238

# Discussion

## Initial Question
I've seen this now a couple of times, both with 7.14 and 7.14.1:Screenshot 2024-03-27 at 18.52.51.pngBasically reboot the cap AC, and watch its memory slowly but inexorably go down. Once it's above ~87% usage, the cap AC becomes unresponsive (time out waiting for process 85/24/etc), and I have to hard power cycle.The interesting thing is that I have two of these, connected to same capsMAN, and only one does this for a while, then the problem moves to the other, etc.Did anyone else see this? Is it a known issue? (Should I just move to cap AX with its 1GB of RAM?) ---

## Response 1
7.13.5, cap ac, wifi-qcom-ac, uptime 1week. free memory: 32.6mb ---

## Response 2
7.13.5, cap ac, wifi-qcom-ac, uptime 1week. free memory: 32.6mbThe actual free memory is less concerning than the fact that it continuously decreases between reboots. This is the same graph but over 6 months: you can clearly see that until 7.13 and the new wifi-qcom-ac drivers it was stable, since then it's not really stable - and seems to have gotten worse recently:Screenshot 2024-03-27 at 22.00.35.pngI don't know if it's capsman, the number of connected devices, or something else. But it doesn't seem stable at all. ---

## Response 3
What happened on 12/27? ---

## Response 4
What happened on 12/27?That's when I upgraded to 7.13, but still using old drivers, if I remember correctly. My upgrade timeline:- migrated host from hAP ac to cAP ac: 2023.11.22- 7.12 → 7.13: 2023.12.24- 7.13 → 7.13.4: 2024.02.08- 7.13.4 → 7.14.1: 2024.03.24So it was stable on 7.8 and 7.12, up until 7.13. Since 7.13, it's more or less leaking memory. Either 7.13 itself, or the wifi-qcom-ac drivers. ---

## Response 5
So basically you say, leaking memory since 7.13 and qcom drivers? What's odd, you already had only like 60mb free memory on 7.12 with capac. ---

## Response 6
Only 60MB free (out of 128MB) is not bad (for me). I'd be happy if I could stay there.I've now disabled connection tracking entirely, and there was a reduction in memory usage, but the leak is still present. I'll probably file a support ticket, since it doesn't seem to be a widely known issue. ---

## Response 7
I can confirm this behavior, with one hap ac3 and wifi-qcom-ac drivers. Two other hap ac3, with legacy drivers don't show this behavior. ---

## Response 8
I can confirm this behavior, with one hap ac3 and wifi-qcom-ac drivers. Two other hap ac3, with legacy drivers don't show this behavior.Oh, thanks, this is a good datapoint! ---

## Response 9
I know this is ove a year old, but as I think I'm also affected I wanted to ask - were you able to resolve this using the support ticket?I have two cAP acs currently running 7.17 (stable) and for some reason, two days ago, the same problems started for me at one of them.It reboots, and afterwards I see in my monitoring that the memory usage was going towards 100%.The other cAP ac is not (yet?) affected by this, and running smoothly.I'm not aware of any configuration changes I did, but I did introduce a couple of new VMs around that time which I'm thinking might have to do with it - pending investigation from my side. ---

## Response 10
It's complicated ...I have 1 cap AC using 7.16.1 which I reboot every night using script because it will crash every 2 to 3 days because of this problem. A daily reboot makes sure I never get to the point where it crashes. I do have SNMP monitoring on that device and I can see memory is being consumed over time.I also have a support ticket for it but so far no conclusive answer yet.However, I also have AC2 and wAP AC (wap AC = exact same HW as cAP AC !) NOT showing this behavior. They already run stable for months.I haven't tested yet myself (that one cAP AC is high on the wall on a site I don't frequent that much) but I suspect if you would netinstall that device clean to 7.16.1 (or .2 or 7.17) it will not show the problem anymore. ---

## Response 11
As a first measure or attempt, I would Netinstall the affected cap ac (with "keep-configuration" flag). ---