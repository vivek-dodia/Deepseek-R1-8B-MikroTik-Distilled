# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210827

# Discussion

## Initial Question
Author: Tue Sep 10, 2024 10:11 pm
Hello, how are youI hope everyone is wellI have a scriptWorking on issuingv6I updated to the latest version v7It no longer worksglobal input [/system clock get date]:global mon 0:if ([:len $input] > 0) do={:local input1 [ [:pick $input 0 3]]#/log info " $input1 ":local months [:toarray "jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec"]:for x from=0 to=([:len $months] -1 ) do={:if ([:tostr [:pick $months $x]] = [:tostr [:pick $input1 0 3]]) do={:if ($x <= 9) do={ :set mon (($x + 1))} else={ :set mon ($x + 1) } } }# /log info [ [:pick $input 4 6]]#/log info "$mon"}:global xxx ($mon."/".[:pick $input 4 6]."/".[:pick $input 7 11])/log info "$xxx"/ppp secret:foreach i in=[find] do={:local name1 [get $i name]:local name [get $i routes]:if ($xxx=$name) do={/ppp secret disable [/ppp secret find name=$name1]/ppp active remove [find name=$name1] }}Can you modify it to make it work?New version v7 ---

## Response 1
Author: Wed Sep 11, 2024 11:15 pm
``` :globalinput[/system clockgetdate]:globalxxx([:pick $input57]."/".[:pick $input810]."/".[:pick $input-14])/log info"$xxx"/ppp secret:foreachiin=[find]do={:localname1[get$i name]:localname[get$i routes]:if($xxx=$name)do={/ppp secret disable[/ppp secret find name=$name1]/ppp activeremove[find name=$name1]}} ``` The date format was updated in ROS7.10, and your code needs to be updated accordingly.Check e.g. this thread for more info:https://forum.mikrotik.com/viewtopic.php?t=196072I think this will do it for you:
```
No guarantees…


---
```

## Response 2
Author: Thu Sep 12, 2024 10:51 pm
``` :globalinput[/system clockgetdate]:globalxxx([:pick $input57]."/".[:pick $input810]."/".[:pick $input-14])/log info"$xxx"/ppp secret:foreachiin=[find]do={:localname1[get$i name]:localname[get$i routes]:if($xxx=$name)do={/ppp secret disable[/ppp secret find name=$name1]/ppp activeremove[find name=$name1]}} ``` Didn't work for meIs it possible for me to write?Date formatinroutes. routesThe date format was updated in ROS7.10, and your code needs to be updated accordingly.Check e.g. this thread for more info:https://forum.mikrotik.com/viewtopic.php?t=196072I think this will do it for you:
```
No guarantees…


---
```

## Response 3
Author: [SOLVED]Fri Sep 13, 2024 2:20 pm
``` :if($xxx=$name)do={ ``` ``` :globalinput[/system clockgetdate]:globalxxx([:pick $input57]."/".[:pick $input810]."/".[:pick $input-14]):put $xxx/log info"$xxx"/ppp secret:foreachiin=[find]do={:localname1[get$i name]:localname[get$i routes]:if($xxx=$name1)do={/ppp secret disable[/ppp secret find name=$name1]/ppp activeremove[find name=$name1]}} ``` You are not exactly clear on the purpose of the script, but in this line:
```
It seems that you are comparing a date to a route. I cant imagine that will ever be true.Maybe you should be comparing to name1 instead, if the name of the secret is a date?In this case it would be:
```