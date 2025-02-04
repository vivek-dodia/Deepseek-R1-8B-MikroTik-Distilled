# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 209489

# Discussion

## Initial Question
Author: Tue Jul 23, 2024 12:51 pm
``` :localuptimeuser[/ip hotspot userget[findwherename=$user]uptime]; ``` ``` :localuptimeuser[/ip hotspot usergetname=$user uptime]; ``` Hey everyone, I'm new to Mikrotik and I'm trying to get a better understanding of it. I'm wondering why this script has different syntax but the same output. Is there anyone who can explain it to me? thank you
```
---
```

## Response 1
Author: Tue Jul 23, 2024 6:00 pm
``` :localaUsrNote[/ip hotspot usergetname=$user comment]; ``` ``` :localaUsrNote[/ip hotspot usergetname="$user"comment]; ``` ``` :localaUsrNote[/ip hotspot usergetname="$username"comment]; ``` the first iswrong, because find results is one array, andgetdo not accept arrays as parameters.Coincidentally if exist only one possible results from find, it work, because pass only one array with one single itemThank you very much sir rex. what about this.
```
a little confuse with" ",$userand$username
```