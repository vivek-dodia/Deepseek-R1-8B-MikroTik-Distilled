# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 205980

# Discussion

## Initial Question
Author: Tue Mar 19, 2024 7:15 am
``` put "Uptime: $[:if ([:len [:find [/system resource get uptime] "w"]] != 0) do={([:pick [/system resource get uptime] 0 ([:find [/system resource get uptime] "w"])] *7 + [:pick [/system resource get uptime] ([:find [/system resource get uptime] "d"] -1) ([:find [/system resource get uptime] "d"])])} else={[:pick [/system resource get uptime] ([:find [/system resource get uptime] "d"]-1) ([:find [/system resource get uptime] "d"])]}] days" ``` Hello, RouterOS get uptime days code is:
```
The output result is:Uptime:  days;Uptime: 18 daysI have a problem.The output has more "Uptime:  days;"I don't want the output to have the "Uptime:  days;" symbol.Or is there a better way for people to do this?


---
```

## Response 1
Author: Tue Mar 19, 2024 8:19 am
``` :put [/system/resource/get uptime 11w2d15:59:17 ] ``` 
```
---
```

## Response 2
Author: Tue Mar 19, 2024 9:26 am
``` :put [/system/resource/get uptime] 11w2d15:59:17 ``` 
```
Hello,Thank you reply.I need the unit to be days.


---
```

## Response 3
Author: Tue Mar 19, 2024 11:35 am
``` # rextended's function (thanks Master) # Convert uptime to seconds :global timetoseconds do={ :local inTime $1 :local wPos [:find $inTime "w" -1] :local dPos [:find $inTime "d" -1] :local itLen [:find $inTime "." -1] ; :if ([:typeof $itLen] = "nil") do={:set itLen [:len $inTime]} :local itSec [:pick $inTime ($itLen - 2) $itLen] :local itMin [:pick $inTime ($itLen - 5) ($itLen - 3)] :local itHou [:pick $inTime ($itLen - 8) ($itLen - 6)] :local itDay 0 :local itWee 0 :if (([:typeof $wPos] = "nil") and ([:typeof $dPos] = "num")) do={:set itDay [:pick $inTime 0 $dPos] } :if (([:typeof $wPos] = "num") and ([:typeof $dPos] = "num")) do={:set itDay [:pick $inTime ($wPos + 1) $dPos] } :if ([:typeof $wPos] = "num") do={:set itWee [:pick $inTime 0 $wPos] } :local totitSec ($itSec + (60 * $itMin) + (3600 * $itHou) + (86400 * $itDay) + (604800 * $itWee)) :return $totitSec } :local upd ([$timetoseconds [/system resource get uptime]] / 86400) :put "Uptime: $upd days" ``` I need the unit to be days.Try:
```
---
```

## Response 4
Author: [SOLVED]Tue Mar 19, 2024 12:20 pm
``` :put "Uptime: $([:tonum [/system resource get uptime]] / 86400) days" ``` My functiontimetosecondsis correct...viewtopic.php?p=930465#p930465but if already is v7.12.1 (and up) just simply...
```
---
```

## Response 5
Author: Tue Mar 19, 2024 12:58 pm
``` :put "Uptime: $([:tonum [/system resource get uptime]] / 86400) days" ``` My functiontimetosecondsis correct...viewtopic.php?p=930465#p930465but if already is v7.12.1 (and up) just simply...
```
That's great.Effective and simple code.Thank you.
```