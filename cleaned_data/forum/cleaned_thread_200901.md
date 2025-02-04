# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 200901

# Discussion

## Initial Question
Author: Wed Oct 25, 2023 2:53 am
The built-in firewall in Linux (iptables / nftables(nft)) has counters for each rule (--> see "iptables -L -n -v").By this, one sees how many times each filter rule did match, which is also very useful when debugging the filter rules.In RouterOS (/ip firewall filter) this feature seems to be missing, isn't it?But since ROS under the hood is using Linux, then it should be easily possible to make these counters avail also in ROS.Ie. a task for the MikroTik SW developers. ---

## Response 1
Author: [SOLVED]Wed Oct 25, 2023 3:12 am
``` /ip firewall filter print value-list stats /ipv6 firewall filter print value-list stats ``` Is this what you're looking for?
```
Edit: I guess this doesn't help, right? I think proper solution would be for the count to be a property of the rule, so that we could have a way of obtaining only the count value (not an entire descriptive line which needs to be parsed to extract the count)


---
```

## Response 2
Author: Wed Oct 25, 2023 3:15 am
``` /ip firewall filter print value-list stats /ipv6 firewall filter print value-list stats ``` Is this what you're looking for?
```
That's indeed what I mean!Already built-in, that's cool!Thx


---
```

## Response 3
Author: Wed Oct 25, 2023 11:36 am
I guess this doesn't help, right? I think proper solution would be for the count to be a property of the rule, so that we could have a way of obtaining only the count value (not an entire descriptive line which needs to be parsed to extract the count)I just now noticed how weird it shows thousands and millions, with a whitespace where there should be a comma. Be careful with that.Maybe this is already possible. Maybe a script guru can answer this --> s.a. Scripting forumviewforum.php?f=9.But there is a related issue, IMO even more important :A similar counter (numPackets and sumBytes) for each address (/ip firewall address-list) seems to be missing in ROS.In Linux one can use theipsetutility for defininig such IP address lists, each such list can have adefault timeout, user can define also anindividual timeoutfor each address(after which the item autom. gets removed from the list).Each address can have also suchcounters. One can use this then iniptablesfirewall rules.For example if the packet counter of a blocked IP becomes > 10 then do a user defined action...It's a very powerful feature, IMO. Would be nice if such counters were possible also in ROS under/ip firewall address-list, and of course making use of it in the/ip firewall filterrules. ---

## Response 4
Author: Mon Oct 14, 2024 7:21 pm
I guess this doesn't help, right? I think proper solution would be for the count to be a property of the rule, so that we could have a way of obtaining only the count value (not an entire descriptive line which needs to be parsed to extract the count)I just now noticed how weird it shows thousands and millions, with a whitespace where there should be a comma. Be careful with that.Maybe this is already possible. Maybe a script guru can answer this --> s.a. Scripting forumviewforum.php?f=9.But there is a related issue, IMO even more important :A similar counter (numPackets and sumBytes) for each address (/ip firewall address-list) seems to be missing in ROS.In Linux one can use theipsetutility for defininig such IP address lists, each such list can have adefault timeout, user can define also anindividual timeoutfor each address(after which the item autom. gets removed from the list).Each address can have also suchcounters. One can use this then iniptablesfirewall rules.For example if the packet counter of a blocked IP becomes > 10 then do a user defined action...It's a very powerful feature, IMO. Would be nice if such counters were possible also in ROS under/ip firewall address-list, and of course making use of it in the/ip firewall filterrules.I've not followed the changelog of RouterOS since the above posting of mine, but I need such atimeoutfeature for list items (ie. like the iptables/nftables toolipsetin Linux;cf.https://ipset.netfilter.org/ipset.man.html#lbAJ).The nice thing abouttimeoutis that the added item autom. gets removed after the elapsing of the timeout seconds.This hugely simplifies firewall code for blocking of attackers, and also for other use-cases like portknocking.My main firewall strategy on Linux boxes is based on this smart feature.So, in my RouterOS firewalls I would like to use the same feature.Is such atimeoutfeature now possible in the RouterOS firewall lists? Is it on the TODO list?