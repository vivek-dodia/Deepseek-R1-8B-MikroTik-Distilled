# Thread Information
Title: Thread-214169
Section: RouterOS
Thread ID: 214169

# Discussion

## Initial Question
Scenario :Bandwidth test server/client on both PCAll lan connections are @1GbpsTests (UDP) between two PC and between each PC and RB800 (both ways) run about 950 MbpsTest between any of three devices and RB3011 (eth1) runs @ 200 Mbps (3011 sending) or 350 Mbps (3011 receiving)Where to start checking from ? ---

## Response 1
Forget scenario diagram.A pc connected to RB3011 ETH1 gave me 200 to 350 Mbps test result.Pc to pc bandwidth test using 3011 as switch (eth1 and eth2) gave me 950 MbpsCpu usage while testing is about 50%Where's the issue ? ---

## Response 2
Where's the issue ?Sounds like the speedtest is handled by the RB's cpu. Can you share your config?
```
/exportfile=naynameyoulikeRemove serial and any other private info, post between code tags by using the </> button.

---
```

## Response 3
Well... config could be boring, however it manages :a 100Mb internet connection (on second switch chip)30 l2tp-ipsec tunnels (99% with no traffic)40 filter rules10 dstnat rulesnothing of so heavy, reallyCPU sits at 4%Anyway, CPU load is largely involved in Btest, just disabling on the fly all firewall rules, bandwidth jumps at 500/500 ---

## Response 4
How do you perform your speedtest, are you using (i.e.) iPerf:https://iperf.fr/iperf-download.phpI read BTest, that should be avoided at all time (except for some very specific use cases). ---