# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 205965

# Discussion

## Initial Question
Author: Tue Mar 19, 2024 12:21 am
``` # NTPdo{/system clocksettime-zone-name=Greenwichntp clientsetenabled=yes ntp clientsetprimary-ntp=0.0.0.0ntp clientsetsecondary-ntp=0.0.0.0}on-error={:put"Ignoring - RouterOS v7"}do{/system clocksettime-zone-name=Greenwichntp clientsetenabled=yes ntp client serversaddaddress=0.0.0.0ntp client serversaddaddress=0.0.0.0}on-error={:put"Ignoring - RouterOSv6"} ``` Hi guys!I have a standard script that I use to configure Mikrotiks in my work.I'm trying to adapt the script so that would work in ROS6 and ROS7, but i'm not having lucky when testing this part on latest version of ROS7.The code is supposed to result in error in one of the versions, that's why I'm using "on-error".The problem is that the error is not being handled as I programmed in code, instead it only shows that that is having an error.Am I making this wrong? Appreciate the help.expected end of command (line 6 column 20)
```
---
```

## Response 1
Author: Wed Mar 20, 2024 11:36 am
``` {:localver[:tonum[:pick[/system resourcegetversion]01]]:put $ver} ``` Instead of using on-error, find out what version of RouterOS the router is running and the run the correct part with if:Sample code to see main version:
```
---
```

## Response 2
Author: Wed Mar 20, 2024 4:03 pm
``` :localrOSversion[:tonum[:pick[system resourcegetversion]]]:if(num($rOSversion)<7)do={/system clocksettime-zone-name=Greenwichntp clientsetenabled=yes ntp clientsetprimary-ntp=0.0.0.0ntp clientsetsecondary-ntp=0.0.0.0}else={/system clocksettime-zone-name=Greenwichntp clientsetenabled=yes ntp client serversaddaddress=0.0.0.0ntp client serversaddaddress=0.0.0.0} ``` Thanks @Jotne !I change my approach on how to solve the problem just like you said and it's working now!
```
---
```

## Response 3
Author: [SOLVED]Wed Mar 20, 2024 5:41 pm
``` :if ([/system resource get version]~"^7") do={ # call script for v7 /system script run v7script } else={ # call script for v6 /system script run v6script } ``` ``` :execute "/system clock set time-zone-name=Greenwich" :execute "/system ntp client set enabled=yes" :execute "/system ntp client set primary-ntp=1.1.1.1 secondary-ntp=2.2.2.2" :execute "/system ntp client add address=1.1.1.1" :execute "/system ntp client add address=2.2.2.2" ``` Of course there is a way.Even more than one.For example make two scripts, and call from a third script only the correct script for that version.untested example codeOr you can ignore the syntax difference altogether....untested example codeIn the latter way, each version applies its own commands and ignores errors. ---

## Response 4
Author: Wed Mar 20, 2024 8:03 pm
``` # ROSv6:execute"/system clock set time-zone-name=Greenwich":execute"/system ntp client set enabled=yes":execute"/system ntp client set primary-ntp=0.0.0.0":execute"/system ntp client set secondary-ntp=0.0.0.0"# ROSv7:execute"/system clock set time-zone-name=Greenwich":execute"/system ntp client set enabled=yes":execute"/system ntp client servers add address=0.0.0.0":execute"/system ntp client servers add address=0.0.0.0" ``` Thanks for the answer, rextended!By the way, your posts here in the forum already helped me a lot since I started working with Mikrotik, thanks!I tested both ways you mentioned in ROSv7 and ROSv6 and it work flawless.Decided to go with the second method for simplicity.So the result was:
```
Thanks rextended and Jotne!
```