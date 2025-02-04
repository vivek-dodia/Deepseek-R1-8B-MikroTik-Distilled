# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213161

# Discussion

## Initial Question
Author: Tue Dec 10, 2024 2:18 am
You'd normally use a script on the /ip/dhcp-server to do this, in which case "print" is not involved, only "/ip/firewall/address-list add ...", see "lease-script=" underhttps://help.mikrotik.com/docs/spaces/R ... PropertiesIs there some reason this approach does not work? ---

## Response 1
Author: Tue Dec 10, 2024 2:31 am
You'd normally use a script on the /ip/dhcp-server to do this, in which case "print" is not involved, only "/ip/firewall/address-list add ...", see "lease-script=" underhttps://help.mikrotik.com/docs/spaces/R ... PropertiesIs there some reason this approach does not work?i am monitoring the network and restrict their IP by adding their ip to ip/firewall/address lists when see trafic to certain webpagesand together with a firewall Rule limit their freedom.When and IP visiting forbidden sites like youtube, facebook to give some example my plane is to add the ip will to address list upon detecting with this command/ip/kid-control/device/ print proplist=ip-address where activity ~"youtube"will expand this activity field to include more sites but dont know how guessing it will be by using an array ... ---

## Response 2
Author: Tue Dec 10, 2024 2:40 am
Well, now you have me more confused. Kid control does not do blocking of sites, only controls access by time. RouterOS is poorly suited to do content filtering.So, even in terms of scripting, I'm not sure what your what your trying to gleam from /ip/kid-control/devices since it just what "kids" are connected, not anything about traffic/sites.But you'd likely need to a :foreach and "print as-value" to loop "line-by-line" as RouterOS uses arrays variables to pass data, not text. But again what you're looking for isn't it kid-control AFAIK. ---

## Response 3
Author: Tue Dec 10, 2024 2:45 am
Well, now you have me more confused. Kid control does not do blocking of sites, only controls access by time. RouterOS is poorly suited to do content filtering.So, even in terms of scripting, I'm not sure what your what your trying to gleam from /ip/kid-control/devices since it just what "kids" are connected, not anything about traffic/sites.But you'd likely need to a :foreach and "print as-value" to loop "line-by-line" as RouterOS uses arrays variables to pass data, not text. But again what you're looking for isn't it kid-control AFAIK.from command prompt i can get what kind of activity any given IP have at any given time at ip/kid-control/devices and field ip address and activity among other data on ROS 7.16.2 at least and seems usefull to use to monitor, my apology if i can not make my idea clearar but like to limit users activity "only if they do not avoid site that is not permited" without addding rules to deny unless needed, it is a project of mine. .. ---

## Response 4
Author: Tue Dec 10, 2024 2:56 am
I guess I don't understand, since it just bytes per "kid" AFAIK. So if you want to add the IP address of some kid to the address-list based on traffic volume, not site. I've never heard of kid control doing anything with content filtering, so really not sure what you're after.Do you have some print command output that shows what you trying to add, and describe what should happen in a script? Otherwise, what I cannot connect the dots in what you're trying to do.This is printout of an abuser based on kid control, not just to control kids but as a tools to monitor the usage here is the output of my command but need to save each ip in addresslist as abusers:/ip/kid-control/device/print proplist=ip-address where activity ~"youtube"Flags: D - DYNAMICColumns: IP-ADDRESS# IP-ADDRESS0 D 192.168.200.18Hope this is possible ---

## Response 5
Author: Wed Dec 11, 2024 7:28 pm
``` :foreachipaddrin=[/ip/kid-control/device/find activity~"YouTube"]do={/ip/firewall/address-list name=ytkids timeout=1haddress=[/ip/kid-control/device/get$ipaddr ip-address]} ``` I guess it should be something like this, but I don't use kid-control so cannot test
```
---
```

## Response 6
Author: Thu Dec 12, 2024 1:39 am
HiThank you for your response, apology for my ignorace butthe script fails using your suggestions.what do i expect to get from each "/ip/kid-control/device/get line ?The variable $ipaddress contains*18*22*25that is what to expect ? but second lines fails since /ip/kid-control/device get option is "number" or "value-name".if i tabb thru the options i find ip address, mac address and so on after value-name optionkid-control exist in ROS7 for anyone i guess ... ---

## Response 7
Author: [SOLVED]Thu Dec 12, 2024 5:04 am
Couple of things:1. the "find" gets returns the ".id" attributes for any matched results to activity~"youtube" - so $ipaddrs should be a list of *xx values - so that right2. but... using "get <id> <attribute>" is valid form, but it's just a shortened version of "get numbers=<id> value-name=<attribute>" - so that right3. "get" will NOT output anything to console - so if testing use ":put [/ip/kid-control/device/get *18 ip-address]" (replace *18 with a valid value from find).4. "kid-control" is also used for "accounting" and simple client throttling too – so it's right to say it's not just for kids5. in my example, YouTube is camel-cased (auto-corrected I guess) - but from your example it should be ~"youtube"I just tried this, and while the script logic is appears right... I don't get anything in activity for any users, even from winbox or CLI with "print". And docs (https://help.mikrotik.com/docs/spaces/R ... id+Control) actually do not describe the "activity" attribute so I have no idea what it's doing to poplulate (or not populate it)...But I do see your output does find something for activity~"youtube" but I cannot repo that. Activity for the "kid" associated with a MAC is always empty in my tests. ---

## Response 8
Author: Thu Dec 12, 2024 6:48 pm
Couple of things:1. the "find" gets returns the ".id" attributes for any matched results to activity~"youtube" - so $ipaddrs should be a list of *xx values - so that right2. but... using "get <id> <attribute>" is valid form, but it's just a shortened version of "get numbers=<id> value-name=<attribute>" - so that right3. "get" will NOT output anything to console - so if testing use ":put [/ip/kid-control/device/get *18 ip-address]" (replace *18 with a valid value from find).4. "kid-control" is also used for "accounting" and simple client throttling too – so it's right to say it's not just for kids5. in my example, YouTube is camel-cased (auto-corrected I guess) - but from your example it should be ~"youtube"I just tried this, and while the script logic is appears right... I don't get anything in activity for any users, even from winbox or CLI with "print". And docs (https://help.mikrotik.com/docs/spaces/R ... id+Control) actually do not describe the "activity" attribute so I have no idea what it's doing to poplulate (or not populate it)...But I do see your output does find something for activity~"youtube" but I cannot repo that. Activity for the "kid" associated with a MAC is always empty in my tests.Hi, Got it working as i want it, the error i got was becasue same ip already entered in firewall address list but it works, THANK YOU a bunch