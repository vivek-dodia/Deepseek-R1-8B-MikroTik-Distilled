# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210982

# Discussion

## Initial Question
Author: Tue Sep 17, 2024 4:31 pm
Hello, Is it possible to create a rule on CAPsMAN (access list, firewall... wherever) that the wireless uses a password at a specific time and to be open beyond that time?For example, who knows the password can use wifi all the time and who doesn't know the password can use from 10 - 11h and 13 - 14h. ---

## Response 1
Author: [SOLVED]Tue Sep 17, 2024 4:42 pm
IMHO this is impossible with single SSID. but you can use one SSID protected and one open SSID and use access list rules for the open SSID. ---

## Response 2
Author: Tue Sep 17, 2024 6:31 pm
No problem:Use /system scheduler for the scheduling part and /sysstem/script for enabling/disabling the wifi interface. ---

## Response 3
Author: Tue Sep 17, 2024 10:15 pm
Access list have time filter. no need for scheduler Scripting ---

## Response 4
Author: Wed Sep 18, 2024 4:13 pm
Thank you for answers. I will probably create slave interface on CAPsMAN for second configuration, leave it open and use access list for time interval. ---

## Response 5
Author: Wed Sep 18, 2024 4:16 pm
PS: Don't forget the "default reject" rule for this secondary SSID. Allow by specific time and final rule is a reject.