# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213647

# Discussion

## Initial Question
Author: Thu Jan 02, 2025 9:48 pm
I have a switch (CRS312-4C+8xg) and 2 AP's (cAP ax). They are all running RouterOS 7.16.2.I'm trying to configure Capsman on the switch, but it appears it's running the "old" capsman version. It doesn't show configs for 80mhz channels, WPA 3 etc.How do I upgrade Capsman? I've seen tons of posts and references to the new version, but zero pages telling me how to install it. ---

## Response 1
Author: [SOLVED]Thu Jan 02, 2025 9:56 pm
You don't, CAPsMAN is automatically installed with version 7.13.x and up.It has moved, can be configured on /interface wifi (or the wifi menu item).Here is a link to the official documentation:https://help.mikrotik.com/docs/spaces/R ... iFiCAPsMANAnd...if you don't use the old CAPsMAN, you could consider removing the wireless package (which is of no use). ---

## Response 2
Author: Wed Jan 08, 2025 9:12 pm
Thanks! I got it all configured. ---

## Response 3
Author: Wed Jan 08, 2025 9:25 pm
Glad it worked out, you can mark this topic as solved.