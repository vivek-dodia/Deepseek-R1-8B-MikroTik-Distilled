# Thread Information
Title: Thread-1113412
Section: RouterOS
Thread ID: 1113412

# Discussion

## Initial Question
Hi, When selecting "interface activity" for say ether1, if you have a VLAN interface it doesn't show activity for the VLAN interface.Is there a way around this ? ---

## Response 1
Actually it does show ... it shows all traffic, passing a physical port (tagged or untagged).If you are not seeing the same way, then explain actual topology and setup so we can see if there's misunderstanding or a possible bug. And what exactly you're observing, it could be I'm referring to something completely different. ---

## Response 2
Actually it does show ... it shows all traffic, passing a physical port (tagged or untagged).If you are not seeing the same way, then explain actual topology and setup so we can see if there's misunderstanding or a possible bug. And what exactly you're observing, it could be I'm referring to something completely different.I am talking about the front LEDs yeah ?Sure - I have ether1 connected to the Fibre ONT. I need to tag my internet traffic with VLAN10 so I created a VLAN interface on and "bound" it to ether1. On top of that VLAN10 interface I have created a PPPoE interface that auth's me to my ISP. If I leave it as led1 to ether1 I see broadcasts and the likes - a flash ever now and then. Changing this to the VLAN10 interface, I see a very fast blinking LED, same if I set it to the PPPoE interface.I also have a bond running down to a HP switch, same thing...I just did a compare where I have a server, connected to ether4 on an "access" port, aka nothing else, no VLAN etc and it only shows broadcast type traffic. I did an update on my Ubuntu and it flashed like 20 times during the whole process - including the SSH session....Happy to upload a video somewhere if you want ---

## Response 3
I am talking about the front LEDs yeah ?Ah, right.It could be that leds functionality refers to L3 interface (when configured so). And that excludes tagged traffic. You may want to open a ticket withsupport@mikrotik.comand have them clarify (and update/ammend help page as well). ---

## Response 4
I am talking about the front LEDs yeah ?Ah, right.It could be that leds functionality refers to L3 interface (when configured so). And that excludes tagged traffic. You may want to open a ticket withsupport@mikrotik.comand have them clarify (and update/ammend help page as well).Will do ---

## Response 5
Any update on this? I noticed that the LEDs on my CRS326-24G-2S+ do not blink when there is traffic but just jointly every couple of seconds. I use vlans as well. They also do not blink on
```
/interface/ethernet/blink ether01. They are all set to "interface-activity".

---
```

## Response 6
Any update on this? I noticed that the LEDs on my CRS326-24G-2S+ do not blink when there is traffic but just jointly every couple of seconds. I use vlans as well. They also do not blink on
```
/interface/ethernet/blink ether01. They are all set to "interface-activity".So I opened the ticket and yes, the lights will respond to L3 "events" only with NO parent/child relationships - from memory, let's say you create a vlan on ether1, the lights will "work" better with "vlan" as the activity, rather than ether1.They do have plans to fix this, but given that ROS v7 doesn't have a stable version yet, I would suspect this is very low priority.

---
```

## Response 7
Thank you for the quick reply. Showing vlan activity of course will show the same pattern on all ports of the vlan, but to me it is more useful than before. ---