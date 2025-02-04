# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 207689

# Discussion

## Initial Question
Author: Fri May 17, 2024 7:59 am
Helloi want script to delete all hotspot disabled users and their scripts with same hotspot nameex:i have disabled user with name 23456 and it has script with same name 23456i want to delete themi used below script but it delete all scripts# Fetch all disabled hotspot users:foreach user in=[/ip hotspot user find disabled=yes] do={:local username [/ip hotspot user get $user name]# Remove the user/ip hotspot user remove $user:log info ("Removed disabled hotspot user: " . $username)# Remove associated scripts:foreach script in=[/system script find] do={:local scriptName [/system script get $script name]:if ([:find $scriptName $username] != 0) do={/system script remove $script:log info ("Removed associated script: " . $scriptName)}}}thanks ---

## Response 1
Author: [SOLVED]Sat Jun 15, 2024 7:59 pm
SOLVEDusing this script/ip hotspot user remove [find disabled]delay 120s:local hotspotUsers [/ip hotspot user find]:local scripts [/system script find name!=scheduler_helpers]:foreach script in=$scripts do={:local scriptName [/system script get $script name]:local userExists false:foreach user in=$hotspotUsers do={:local userName [/ip hotspot user get $user name]:if ($scriptName = $userName) do={:set userExists true}}:if ($userExists = false) do={/system script remove $script}}