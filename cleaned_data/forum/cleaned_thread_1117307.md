# Thread Information
Title: Thread-1117307
Section: RouterOS
Thread ID: 1117307

# Discussion

## Initial Question
Hello, good afternoon, Does anyone know why when I enable in /system /Ntp Client and enter some time server for example 0.es.pool.ntp.org the router does not synchronize the time ? it stays in started and does not appear as synchronized ?Thank you. ---

## Response 1
export your config ...maybe output fw 4/6 rule, maybe dns resolv ---

## Response 2
can you ping that address from the CLI? are you sure that traffic originated from router leaves the router? Not the one originated from LAN. ---

## Response 3
Add firewall rule to accept port 123 ---

## Response 4
There are dumb ISPs (there is one in my country) that prevent packets with destination port UDP 123 from reaching their customers. If that's the case, you'll might try this solution:viewtopic.php?f=13&t=208791&p=1082590#p1082590 ---