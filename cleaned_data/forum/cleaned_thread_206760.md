# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 206760

# Discussion

## Initial Question
Author: Mon Apr 15, 2024 10:36 am
``` :local test [/system routerboard get routerboard]; :put $test ``` The company I work for uses alot of scripts across both CHRs and routerboards. To validate if the script is currently running on a CHR or a routerboard we have always used the "/system routerboard get routerboard" command.It seems like that this has been removed in CHRs on ROS7. In ROS6 it would always generate false/true based on if it was a CHR or a routerboard.Does anyone know if this will be brought back in ROS7 or if there is a better way to accomplish it?I have not been able to find any information why this was removed from ROS7 CHRs.If you want to test it on your own device you can run:
```
---
```

## Response 1
Author: [SOLVED]Mon Apr 15, 2024 4:58 pm
``` /system/resource get board-name ``` 
```
---
```

## Response 2
Author: Mon Apr 15, 2024 10:08 pm
``` /system/resource get board-name ``` 
```
Works good enough, thank you!Sad that the menu was removed, even though it was completely empty. It was nice to have a simple bool to check.


---
```

## Response 3
Author: Mon Apr 15, 2024 10:11 pm
``` :put ([/system resource get board-name] != "CHR") ``` No logic on check what do not exist.true when is a routerboard
```
---
```

## Response 4
Author: Mon Jun 10, 2024 5:51 pm
``` :put ([/system resource get board-name] != "CHR") ``` ``` :put ("ABC" . [:find [/system resource get board-name] "CHR"] . "DEF"="ABCDEF") ``` No logic on check what do not exist.true when is a routerboard
```
From RouterOS 7.15system resource get board-nameincludes also the virtualization platform like "CHR VMware, Inc. VMware Virtual Platform", so I've update the check in this way.truewhen is a routerboard
```

```
---
```

## Response 5
Author: Tue Jun 11, 2024 9:45 am
``` :put ([/system resource get board-name] != "CHR") ``` ``` :put ("ABC" . [:find [/system resource get board-name] "CHR"] . "DEF"="ABCDEF") ``` ``` :put ([/system resource get board-name] ~ "CHR") ``` No logic on check what do not exist.true when is a routerboard
```
From RouterOS 7.15system resource get board-nameincludes also the virtualization platform like "CHR VMware, Inc. VMware Virtual Platform", so I've update the check in this way.truewhen is a routerboard
```

```
No logic to add something instead of just check...true when is a routerboard
```

```
(on my case is "CHR VMware, Inc. VMware Virtual Platform")
```