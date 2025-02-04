# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 188088

# Discussion

## Initial Question
Author: Mon Aug 01, 2022 3:27 pm
Hi just a simple question how can i remove a value or delete it.I my case i will edit the value /interface wireless cap caps-man-names=server1i am able to edit or to set this but i wont to remove it just like i click on the "arrow up" in the GUILG David ---

## Response 1
Author: [SOLVED]Mon Aug 01, 2022 4:04 pm
/interface wireless capsetcaps-man-names=""""are two", not 4' ---

## Response 2
Author: Tue Oct 29, 2024 4:52 pm
This solution does not work for /ip firewall nat>set in-interface="" produces error "ambiguous value of interface, more than one possible value matches input"6.49.13 long-term ---

## Response 3
Author: Tue Oct 29, 2024 5:07 pm
You can use:"/ip firewall nat unset value-name=in-interface"or"/ip firewal nat set !in-interface"