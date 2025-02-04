# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 214173

# Discussion

## Initial Question
Author: Fri Jan 24, 2025 6:31 pm
Hi, I have been browsing the documentation, this forum and the web in general looking for a way to say: "I want all 2.4GHz networks, on all CAPs, to be available only for the following 3 clients identified by MAC address".A lot of guides suggest going inside the `/caps-man` menu, which I simply do not have. I know CAPSMAN was merged inside Wifiwave2, or whatever it's called, and that whole space is in a state of flux to put it mildly, but I can't really find any clue on how to achieve what I want.Can you help? Thanks. ---

## Response 1
Author: [SOLVED]Fri Jan 24, 2025 9:26 pm
I didn't try ... but how about /interface/wifi/access-list on CAPsMAN device? ---

## Response 2
Author: Fri Jan 24, 2025 9:36 pm
on CAPsMAN on hAP AX3 that is possible ... ---

## Response 3
Author: Sat Jan 25, 2025 1:58 pm
I didn't try ... but how about /interface/wifi/access-list on CAPsMAN device?Thanks, you pointed me in the right direction. The problem then was that my 2.4GHz interfaces, both local and remote, are created dynamically and there is no way for the access list entries to be relevant to, say, all interfaces whose name matches a regex pattern. So I had to come up with an interface list populated automatically via a datapath. The whole experience has been as frustrating and painful as it gets, truly a horrible user journey.Thanks again for your help!