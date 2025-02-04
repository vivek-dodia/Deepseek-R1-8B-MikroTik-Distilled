# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 153641

# Discussion

## Initial Question
Author: Tue Nov 05, 2019 10:33 am
``` :tool e-mail send to=email@example.com subject="Violation alert!!! New DHCP client in the network"body="MAC: $leaseActMAC, ``` I've added the flowing script in dhcp server alerts but not working
```
please guide me


---
```

## Response 1
Author: Tue Nov 05, 2019 1:41 pm
``` /tool e-mailsetaddress=mail.provider.comfrom=dhcpalerts@provider.com password=youremailpassword port=465start-tls=tls-only user=dhcpalerts@provider.com ``` Did you configure /tool e-mail before?Like:
```
-Chris


---
```

## Response 2
Author: Tue Nov 05, 2019 2:54 pm
``` :localrecipient"someemail@soemserver.com"/ip dhcp-server lease:if($leaseBound=1)do={:do{:tool e-mail send to=$recipient subject="DHCP Address Alert [MAC: $leaseActMAC]"body="The following MAC address [$leaseActMAC] received an IP address [$leaseActIP] from the DHCP Server [$leaseServerName]":log info"Sent DHCP alert for MAC $leaseActMAC"}on-error={:log error"Failed to send alert email to $recipient"}} ``` I've got this script from a search but also no email sent when a new device connected to networkI put it in dhcp server alert with default settings of new alert
```
there is no log entryI think the event didn't fire and the code never executed


---
```

## Response 3
Author: [SOLVED]Thu Dec 05, 2019 3:58 am
``` :localrecipient"someemail@soemserver.com"/ip dhcp-server lease:if($leaseBound=1)do={:do{:tool e-mail send to=$recipient subject="DHCP Address Alert [MAC: $leaseActMAC]"body="The following MAC address [$leaseActMAC] received an IP address [$leaseActIP] from the DHCP Server [$leaseServerName]":log info"Sent DHCP alert for MAC $leaseActMAC"}on-error={:log error"Failed to send alert email to $recipient"}} ``` I've got this script from a search but also no email sent when a new device connected to networkI put it in dhcp server alert with default settings of new alert
```
there is no log entryI think the event didn't fire and the code never executedThis should go in the script box of the dhcp-server you want it to run on - not in the alerts tab.


---
```

## Response 4
Author: Thu Dec 05, 2019 10:16 am
``` :localrecipient"someemail@soemserver.com"/ip dhcp-server lease:if($leaseBound=1)do={:do{:tool e-mail send to=$recipient subject="DHCP Address Alert [MAC: $leaseActMAC]"body="The following MAC address [$leaseActMAC] received an IP address [$leaseActIP] from the DHCP Server [$leaseServerName]":log info"Sent DHCP alert for MAC $leaseActMAC"}on-error={:log error"Failed to send alert email to $recipient"}} ``` I've got this script from a search but also no email sent when a new device connected to networkI put it in dhcp server alert with default settings of new alert
```
there is no log entryI think the event didn't fire and the code never executedThis should go in the script box of the dhcp-server you want it to run on - not in the alerts tab.thank you I think it is my mistake I'll try that and reply


---
```

## Response 5
Author: Thu Dec 05, 2019 11:36 am
``` :localrecipient"someemail@server.com"/ip dhcp-server lease:if(($leaseBound=1)&&([/ip dhcp-server lease findwheredynamicmac-address=$leaseActMAC]!=""))do{:do{:tool e-mail send to=$recipient subject="DHCP Address Alert [MAC: $leaseActMAC]"body="The following MAC address [$leaseActMAC] received an IP address [$leaseActIP] from the DHCP Server [$leaseServerName]":log info"Sent DHCP alert for MAC $leaseActMAC"}on-error={:log error"Failed to send alert email to $recipient"}} ``` a simple alteration to the scriptthe previous script sends an email when ever a new devices connected to router static or dynamicin my situation I need to know only dynamic ones because the static ones in known to methis modification sends only dynamic ip addresses
```
---
```

## Response 6
Author: Wed Dec 25, 2019 11:47 am
``` :localrecipient"someemail@server.com"/ip dhcp-server lease:if(($leaseBound=1)&&([/ip dhcp-server lease findwheredynamicmac-address=$leaseActMAC]!=""))do{:do{:tool e-mail send to=$recipient subject="DHCP Address Alert [MAC: $leaseActMAC]"body="The following MAC address [$leaseActMAC] received an IP address [$leaseActIP] from the DHCP Server [$leaseServerName]":log info"Sent DHCP alert for MAC $leaseActMAC"/ip firewall filteraddchain=forward src-mac-address=$leaseActMAC action=drop}on-error={:log error"Failed to send alert email to $recipient"}} ``` Nice Addition to the scriptadd filter rule to block mac address from using internet
```
---
```

## Response 7
Author: Thu Dec 26, 2019 5:46 pm
``` :localrecipient"someemail@server.com"/ip dhcp-server lease:if(($leaseBound=1)&&([/ip dhcp-server lease findwheredynamicmac-address=$leaseActMAC]!=""))do{:do{:tool e-mail send to=$recipient subject="DHCP Address Alert [MAC: $leaseActMAC]"body="The following MAC address [$leaseActMAC] received an IP address [$leaseActIP] from the DHCP Server [$leaseServerName]":log info"Sent DHCP alert for MAC $leaseActMAC"/ip firewall filteraddchain=forward src-mac-address=$leaseActMAC action=drop}on-error={:log error"Failed to send alert email to $recipient"}} ``` Very nice - thank you.Nice Addition to the scriptadd filter rule to block mac address from using internet
```
---
```

## Response 8
Author: Mon Dec 30, 2019 4:40 pm
``` :localrecipient"someemail@server.com"/ip dhcp-server lease:if(($leaseBound=1)&&([/ip dhcp-server lease findwheredynamicmac-address=$leaseActMAC]!=""))do{:do{:tool e-mail send to=$recipient subject="DHCP Address Alert [MAC: $leaseActMAC]"body="The following MAC address [$leaseActMAC] received an IP address [$leaseActIP] from the DHCP Server [$leaseServerName]":log info"Sent DHCP alert for MAC $leaseActMAC"}on-error={:log error"Failed to send alert email to $recipient"}} ``` a simple alteration to the scriptthe previous script sends an email when ever a new devices connected to router static or dynamicin my situation I need to know only dynamic ones because the static ones in known to methis modification sends only dynamic ip addresses
```
Very nice modification .... just to let you know that on my system this generates a syntax error in the following:&& ([/ip dhcp-server lease find where dynamic mac-address=$leaseActMAC]!=""))do {To correct the following change works:&& ([/ip dhcp-server lease find where dynamic mac-address=$leaseActMAC]!="")) do={


---
```

## Response 9
Author: Thu Feb 03, 2022 1:20 am
``` :globalreportedMacs;:if(:typeof[$reportedMacs]="nil")do={:globalreportedMacs[:toarray""]}:localrecipient"someemail@server.com"/ip dhcp-server lease:if(($leaseBound=1)&&([:type[:find $reportedMacs $leaseActMAC]]="nil")&&([/ip dhcp-server lease findwheredynamicmac-address=$leaseActMAC]!=""))do={:do{:localleaseHostname $"lease-hostname":tool e-mail send to=$recipient subject="[MikroTik] DHCP Address Alert [MAC: $leaseActMAC]"body="MAC: $leaseActMAC\nIP: $leaseActIP\nHost: $leaseHostname\nDHCP: $leaseServerName\n\n-- \nRouterOS":log info"Sent DHCP alert for MAC $leaseActMAC":setreportedMacs($reportedMacs,$leaseActMAC);}on-error={:log error"Failed to send alert email to $recipient"}} ``` Anyone knows how to send email only if a new device connected.I mean, if the "lease time" is not over yet, then don't send emailI use this modification to "remember" already sent MAC addresses (globally). The downside is that it sends again all addresses after restart.- Also, it would be nice to implement TTL for each record, but this is good enough for me right now.- Note that my version also sends the hostname of the connected device.
```
---
```

## Response 10
Author: Sun Aug 18, 2024 2:46 am
Thank you.It working. Super very good.My modification.I added the hostname::local recipient "email@gmail.com"/ip dhcp-server lease:if (($leaseBound=1) && ([/ip dhcp-server lease find where dynamic mac-address=$leaseActMAC]!="")) do= {:do {:tool e-mail send to=$recipient subject="DHCP Alert [$leaseActIP] [$"lease-hostname"]" body="The following MAC address [$leaseActMAC] received an IP address [$leaseActIP] [$"lease-hostname"] from the DHCP Server [$leaseServerName]":log info "Sent DHCP alert for MAC $leaseActMAC"} on-error={:log error "Failed to send alert email to $recipient"}}