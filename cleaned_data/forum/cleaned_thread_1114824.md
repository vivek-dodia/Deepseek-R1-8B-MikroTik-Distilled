# Thread Information
Title: Thread-1114824
Section: RouterOS
Thread ID: 1114824

# Discussion

## Initial Question
I'm shortening really hard here now:Imagine you have 2 brand new CRS520-4XS-16XQ-RM.Imagine you take multiple DAC Breakout cable.Imagine some of them go straigt into "running" on all ports of this particular QSFP port.Imagine most of them dont do that, instead going "Link up - link down, and so on".Imagine you turn of auto negotionation, and behaviour wont change.Imagine you take the cable of the NOT working port, and realize: The same cable with the same devices hooked up, which didnt work in QSFP: 1, 2, 3, 4, 6, 7, 8, 9 suddenly go up and running stable in QSFP 11.You realize: Oh, why is it working in 11, but not in the other ones?You swap the cables, an repeat the process, with the same result.Am I wrong, when I say: 80% of my QSFP ports of both switches are broken? ---

## Response 1
Hi we have the same problem:https://youtu.be/4jiZP0HSBXEWe didnt found the resolv yet. We think that it is a software/hardware bug for this model. ---

## Response 2
Already contacted support about it ?They don't read all posts here since this is a user forum. ---

## Response 3
Yes, the ticekd is open and being processed. Mikrotik support recommended an upgrade to version 7.17rc3.After upgrade the newer version, the stability of the DAC cable connections has minimally improved, while problems still occur, here the video after the update:https://youtu.be/oBZ4NMrXVqkIt is very weak that you buy a new device, DAC cables from Mikrotik and have such problems.Last time we bought several switches from Mikrotik, including the fastest and best models in Mikrotik's range, and not only are there problems with connection stability, one of the switches after plugging to powerr in a short circuit and burned one of the power supplies.In our opinion, the quality of these devices lately is definitely worse than before, it is definitely better to buy used Dell, CISCO, HP, etc. switches than new Mikrotiks - at least you will not spend several hours troubleshooting problems that do not arise through no fault of your own. ---