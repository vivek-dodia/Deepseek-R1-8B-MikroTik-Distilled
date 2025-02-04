# Thread Information
Title: Thread-1115319
Section: RouterOS
Thread ID: 1115319

# Discussion

## Initial Question
want to use the traffic accounting feature but in Winbox there is no traffic accounting menu and I use the Mikrotik V7 firmware. how to display the accounting traffic menu.Please help ---

## Response 1
It has been renamed to IP / Kid Control. ---

## Response 2
The Mikrotik V6 firmware still has a traffic accounting menu, meaning the Mikrotik V7 firmware has been renamed to Kid Control.Can kid control monitor client device IP address traffic ---

## Response 3
The Mikrotik V6 firmware still has a traffic accounting menu, meaning the Mikrotik V7 firmware has been renamed to Kid Control.That's what I said, didn't I ?Can kid control monitor client device IP address trafficYes. ---

## Response 4
If we enable traffic accounting, it can display graphics for each client's IP address and is supported by a sniffer application.Can kid control display graphics like in this attachment? ---

## Response 5
No, "Kid Control" will only provide nummeric values but Yes on a "client" (IP) basis.It is up to you to extract the data from RouterOS and do something with it. Through scripting you can transmit SYSLOG messages containing this "accounting" info and load them into something for further processing. ---

## Response 6
I have to search for it (again) but there was someone a couple of years ago who made a really nifty script which would do all the collecting and processing and send out info via mail per period you could specify yourself.Used it for SXT LTE6 setup in South of France to track data usage for vacation house tenants (limited monthly data volume, place is sold now).Ah, found it !viewtopic.php?t=185910 ---

## Response 7
Using syslog and send data to Splunk, you can make nice traffic graphs for how much each client uses. See some here:viewtopic.php?t=179960 ---