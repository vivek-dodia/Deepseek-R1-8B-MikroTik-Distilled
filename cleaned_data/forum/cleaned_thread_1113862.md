# Thread Information
Title: Thread-1113862
Section: RouterOS
Thread ID: 1113862

# Discussion

## Initial Question
(Posts split from Is there a SwOS version compatible with CRS304-4XG-IN? -viewtopic.php?t=212335)Hi alli have this exact same problem! Its my first time buying a Mikrotik device and i start regretting it (please prove me wrong!!)I just received this CRS304 10GB SWITCH (and i bought this exactly for that reason, using it as a SWITCH and needs it to be 10 GBE) and i spent all day yesterday trying to make this work as a dumb 10 GBE switch ( i dont need all routing features!). I tried also setting it to boot on SwOS but had the same issues as described here (booting loop). had to reset it about 12 times, and still can't make this work! Why advertising this as a 10 GBE switch if it doesn't work as a switch right out of the box? Please let me know what i am missing.thanksMT ---

## Response 1
I'm pretty sure that if you reset your CRS to defaults, it'll come out configured as "dumb switch" even when running ROS. The only item to be done after that is to adjust IP address if you don't like the one used by default. Shouldn't be too hard when using Webfig (just try to avoid Quickset - switch over to Webfig ... Quickset is very limited and has tendency to screw config if anything is done outside Quickset). ---

## Response 2
unfortunately, no, the out of the box config isnt working of rme.. ---

## Response 3
Post config and specify what you want to do.1 bridgeAll interfaces to bridgePossibly dhcp client to bridge or fixed ip.There is not much more to it.For configopen terminalexport file=anynameyouwishmove file to PCredact serial numberpost contents back here in between [code] [/code] quotes.PS splitting this thread ... ---