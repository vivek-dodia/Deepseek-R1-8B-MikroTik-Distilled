# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212738

# Discussion

## Initial Question
Author: Thu Nov 21, 2024 11:33 pm
Hi, I am looking for a simple script to add 30 days to current date.with below code i can get current date.{:local cdate [ /system clock get date ]:put $cdate}How can i get the date 30 days later from today.if today is2024-11-22, i want to get2024-12-22I have seen other implementation by very long methods using timestamp, unixdate, etc.Any simple 2 line code is highly appreciated ---

## Response 1
Author: Fri Nov 22, 2024 11:55 am
``` [rex@test-v7] > :put ([:totime [/system clock get date]]) 2864w1d00:00:00 = 20049 days after 01/01/1970 [rex@test-v7] > :put ([:totime [/system clock get date]] + 30d) 2868w3d00:00:00 = 20079 days after 01/01/1970 [rex@test-v7] > :put (2868w3d00:00:00 - 2864w1d00:00:00) 4w2d00:00:00 = 30 days [rex@test-v7] > :put ([:tonum (2868w3d00:00:00 - 2864w1d00:00:00)] / 86400) 30 ``` What do you think everyone is stupid to do such complicated things?If you don't need to print the date in a human way, just:(Example of 2024-11-22)terminal example code ---

## Response 2
Author: Sun Nov 24, 2024 1:30 pm
``` [rex@test-v7] > :put ([:totime [/system clock get date]]) 2864w1d00:00:00 = 20049 days after 01/01/1970 [rex@test-v7] > :put ([:totime [/system clock get date]] + 30d) 2868w3d00:00:00 = 20079 days after 01/01/1970 [rex@test-v7] > :put (2868w3d00:00:00 - 2864w1d00:00:00) 4w2d00:00:00 = 30 days [rex@test-v7] > :put ([:tonum (2868w3d00:00:00 - 2864w1d00:00:00)] / 86400) 30 ``` What do you think everyone is stupid to do such complicated things?If you don't need to print the date in a human way, just:(Example of 2024-11-22)terminal example codeThank you for your reply.I tried your code, some of them gives output and some dont. Please see the attached sreenshot.If you can be kind enough to give me code to get the "date" (without time) after 30 days from current date.I want just want the output as date. ---

## Response 3
Author: Mon Nov 25, 2024 10:02 am
``` <<PASTE GLOBAL FUNCTION HERE>> [rex@test-v7] > :put [$unixtodatetime [:tonum 2868w3d00:00:00]] 2024/12/22 00:00:00 ``` some of them gives output and some dontYou don't specify that you use old 7.10, actually the "stable" is 7.16.1 and have more functions than the 7.10You can use this:viewtopic.php?p=977170#p977170example codeIf you do not want " 00:00:00" just remove " $timeStart" from the function, at the end.