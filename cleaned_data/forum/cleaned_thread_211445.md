# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211445

# Discussion

## Initial Question
Author: Thu Oct 03, 2024 11:42 am
``` # define variables:locallist:localcomment:localnewip:localoldip# Loop through each entry in the address list.:foreachiin=[/ip firewall address-list find]do={# Get the first five characters of the list name:setlist[:pick[/ip firewall address-listget$i list]05]# If they're 'host_', then we've got a match - process it:if($list="host_")do={# Get the comment for this address list item (this is the host name to use):setcomment[/ip firewall address-listget$i comment]:setoldip[/ip firewall address-listget$i address]:setnewip[:resolve $comment server9.9.9.9]# Resolve it and set the address list entry accordingly.:if($newip!=$oldip)do={/ip firewall address-listset$i address=$newip}}} ``` Hallo, After upgrade ROS 4011 to 7.15.3 have a error in log with the script running in sheduler:executing script from scheduler failed, please check it manuallyPlease help to find howto update script to bypass error. Thank you.
```
---
```

## Response 1
Author: Thu Oct 03, 2024 3:33 pm
``` importdns-update.rscScriptfile loadedandexecuted successfully ``` saving the script as .rsc and then dry-run importing it might show something.Thank you, sad but no success:
```
Checked policies, code for errors. Also no success%( No idea..
```