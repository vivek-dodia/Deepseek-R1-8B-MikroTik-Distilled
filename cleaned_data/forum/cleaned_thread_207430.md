# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 207430

# Discussion

## Initial Question
Author: [SOLVED]Wed May 08, 2024 7:11 pm
``` :global lastLog :if ([:typeof $lastLog] != "num") do={:set lastLog 0} { :local id2num do={:return [:tonum "0x$[:pick $1 1 [:len $1]]"]} /log :foreach item in=[find where (([$id2num $".id"] > $lastLog) and (message="FCC: Attemtped to send a frame with no bonded connections established"))] do={ :set lastLog [$id2num $item] # do something here.................. } } ``` search better on forum, some of my script do not catch twice the same log, only new added log.....viewtopic.php?p=1051243#p1051243example code