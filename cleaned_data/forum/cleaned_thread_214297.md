# Thread Information
Title: Thread-214297
Section: RouterOS
Thread ID: 214297

# Discussion

## Initial Question
Hello everyone!At the end of September 2024, we built an x86 server in the configuration:Motherboard - SuperMicro X10SRi-FCPU - Xeon E5-2697A v4RAM - Kingston 8Gb 2133MHzNIC - Intel X520-DA2All this time, 3-4 days after the reboot, which has to be done once a week because of this, there is a gradual loading of 1 core, with an increase to a peak close to 100% threshold. This problem persists starting with version 7.15 during the initial installation, and ending with the current 7.17Below is the CPU load graph (few month)graph (2).pngfew daysgraph (3).png ---

## Response 1
What doesProfilershow? ---

## Response 2
Can you as well share your config?
```
/exportfile=anynameyoulikeRemove serial and any other private info.

---
```

## Response 3
What doesProfilershow?The load goes through the firewall3_firewall.png2_firewall.png1_firewall.pngI found a possible reason, but I didn't understand why it was happening gradually, as an accumulation effect. It seems to be related to the connection tracker. I have used the script to clean up old connections several times, for which there was no activity for more than 60 seconds. And it showed a sharp drop in load. But what is more interesting is that the load is initially distributed across all cores, but then it seems to fall on one core and stops parallelizing. Perhaps this is a failure of the internal load balancing logic. The strangest thing is that this happens only ater 3-4 days and is increasing. ---

## Response 4
Can you as well share your config?
```
/exportfile=anynameyoulikeRemove serial and any other private info.Maybe you want to see something specific, some sections like Firewall, etc.? the file is very large to clean it from excess or post the whole thing.

---
```

## Response 5
I would like to see both /interface and /ip/firewall (and perhaps complete /ip). ---

## Response 6
look at: rx/tx p/s in interface menu
```
/ipfifipr co

---
```

## Response 7
look at: rx/tx p/s in interface menutx-rx.png
```
/ipfifipr co21

---
```

## Response 8
What doesProfilershow?The load goes through the firewall3_firewall.png2_firewall.png1_firewall.pngI found a possible reason, but I didn't understand why it was happening gradually, as an accumulation effect. It seems to be related to the connection tracker. I have used the script to clean up old connections several times, for which there was no activity for more than 60 seconds. And it showed a sharp drop in load. But what is more interesting is that the load is initially distributed across all cores, but then it seems to fall on one core and stops parallelizing. Perhaps this is a failure of the internal load balancing logic. The strangest thing is that this happens only ater 3-4 days and is increasing.check actual connections with
```
ip/firewall/connection/tracking/print

---
```

## Response 9
```
/ipfico tr pr

---
```

## Response 10
```
/ipfico tr prIMO your post would be much better if you used full commands and properties instead of these obfuscated code snippets. If not for other thing, these snipets might stop working if some future ROS would add new configuration branch/command with name beginning with same two characters as existing branch/command.

---
```

## Response 11
```
/ipfico tr prI'll take the data at peak load later in the evening.mikrotik.png

---
```

## Response 12
```
/ipfico tr prPeek timemikrotik.png

---
```