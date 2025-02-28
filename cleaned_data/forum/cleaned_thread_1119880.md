# Thread Information
Title: Thread-1119880
Section: RouterOS
Thread ID: 1119880

# Discussion

## Initial Question
Hey guys, need some help over here.We're running multiple Mikrotik switches in the network and I cannot find a way to log stp changes. I need to log them because I'm trying to troubleshoot a strange issue with one of our switches that I suspect is related to (R)STP. Problem is that the issue might not occur at all for weeks at a time or it might not occur while I'm physically next to the switch so I cannot log into using a serial cable and check things out (logging in remotely is not an option as the switch is inaccessible while the problem is ongoing). I want to check for STP related events, but I cannot find a way to do it.WHAT I HAVE TRIEDI have tried using the bridge filter function using the rstp multicast dst mac address 01:80:C2:00:00:00/FF:FF:FF:FF:FF:FF but it does not capture anything. I have tried setting different stp flags like tcn, or tried to match timers (e.g., Hello time 2s) to get a hit. I ended up just making the following rules to log all traffic going through the interface
```
/interface bridge filter
add action=log chain=input disabled=no in-interface=ether2 log=yes log-prefix=\
    testinpu
add action=log chain=output disabled=no log=yes log-prefix=testoutp \
    out-interface=ether2
add action=log chain=forward disabled=no in-interface=ether2 log=yes \
    log-prefix=testfor out-interface=ether2For a bit of context I'm not testing on the affected switch. I'm using an RB4011 with RSTP-enabled bridge which I have connected to a bridge port of a hap ax2 that is using RSTP. The above filters do work as I can see lldp and cdp traffic being logged (e.g., 01:80:C2:00:00:0E) but no traffic for RSTP is being reported. I have sniffed packets on the link and bpdus are being properly sent and received, obviously until the topology has converged and the hap ax2 root port stops sending bpdus to the uplink 4011. Notice that the bpdu filters were already configured and running before I connected the devices so it's not that hap ax2 had already stopped sending bpdus by the time the filters were configured.I have come across some other similar forum posts but none has apparently reached any conclusion regarding this matter (e.g.,viewtopic.php?t=73621). Appreciate your time!

---
```

## Response 1
Hey friend. Did you figure out anything?I don't think the filter rule will work as it only filters packets that cross the CPU.I had some luck by turning on the STP topic in Logging. ---

## Response 2
I havent actually found the solution to that yet. I stopped searching for a while because I found out that rstp was the problem and I solved it. Actually it might even be a bug but I'm not sure and have not bothered to check any further.What have you found out exactly? I might not have found a way to log stp topology changes but if there is a way I would like to know it. What is stp topic at logging? You mean the log menu or what exactly? ---

## Response 3
```
/system logging action add memory-lines=36 name=mempage target=memory
/system logging add action=mempage topics=stp

---
```

## Response 4
Conrad thank you so much! I have never actually noticed that I there is a dedicated option for configuring what is logged. ---

## Response 5
You're welcome. Besides limiting the topics, the distinct action is an isolated view. ---