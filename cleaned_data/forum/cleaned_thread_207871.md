# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 207871

# Discussion

## Initial Question
Author: Sat May 25, 2024 3:32 pm
``` :global$SaveNTP;$SaveNTPYourMonitorScriptName ``` ``` # SaveNTP function:globalSaveNTPdo={:localscriptName"SaveNTP";:localfileName"$scriptName.csv";:localfileMessage"";:localerrorMessage"";/log debug"$1 $scriptName started";# file adddo{:if([/file find name=$fileName]) do={} else={/fileaddname=$fileName};}on-error={:seterrorMessage"$1 $scriptName file add error";/log warning $errorMessage;:returnfalse;};# message:do{:localrouterName[/system identitygetname];:localuptime[/system resourcegetuptime];:localdate[/system clockgetdate];:localtime[/system clockgettime];:setfileMessage"$routerName;$uptime;$date;$time"}on-error={:seterrorMessage"$1 $scriptName message error";/log warning $errorMessage;:returnfalse;};# file set:do{:if([/file find name=$fileName])do={/fileset$fileName contents=$fileMessage;}else={:seterrorMessage"$scriptName file find error";/log warning $errorMessage;:returnfalse;};/log debug"$scriptName executed";:returntrue;}on-error={:seterrorMessage"$scriptName file set error";/log warning $errorMessage;:returnfalse;};}; ``` ``` :localfileName"$scriptName.txt";...:setfileMessage"routerName=$routerName\r\nuptime=$uptime\r\ndate=$date\r\ntime=$time" ``` Hi.You can run this on startup and then call it as a function after some NTP events.It is possible to use a log parser to analyze NTP messages.So, you need a script that will monitor NTP events and call this one
```
This creates a csv file "SaveNTP.csv" "YourMonitorScriptName" as argument.You will see an error messages "YourMonitorScriptName SaveNTP ...." in the system log if something wrong.
```

```
Another idea is to store the data not with a separator, but with the name of the variable for import:viewtopic.php?t=38191
```

```
PSSince you'll need a system log parser or other NTP event monitor, just don't do anything that requires accurate time. Until the time is synchronized. Why do you need an outdated file?


---
```

## Response 1
Author: Sun May 26, 2024 3:33 pm
``` # SaveNTP:localscriptName"SaveNTP";:localfileName"$scriptName.csv";:localfileMessage[/system clockget];:localerrorMessage"";/log debug"$scriptName started";# file adddo{:if([/file find name=$fileName]) do={} else={/fileaddname=$fileName};}on-error={:seterrorMessage"$scriptName file add error";/log warning $errorMessage;:returnfalse;};:delay1s;# file set:do{:if([/file find name=$fileName])do={/fileset$fileName contents=$fileMessage;}else={:seterrorMessage"$scriptName file find error";/log warning $errorMessage;:returnfalse;};/log debug"$scriptName executed";:returntrue;}on-error={:seterrorMessage"$scriptName file set error";/log warning $errorMessage;:returnfalse;}; ``` 
```
---
```

## Response 2
Author: Sun May 26, 2024 3:38 pm
``` # LoadNTP:localscriptName"LoadNTP";:localfileName"SaveNTP.csv";:localerrorMessage"";:localfileContents"";/log debug"$scriptName started";# LoadValue function:localLoadValuedo={:localstart[:find $1"$2="];:setstart($start+[:len $2]+1);:localend[:findfrom=$start $1";"];:return[:pick $1 $start $end];};# file contents:do{:if([/file find name=$fileName])do={:setfileContents[/fileget[/file find name=$fileName]contents];}else={:seterrorMessage"$scriptName file find error";/log warning $errorMessage;:returnfalse;};}on-error={:seterrorMessage"$scriptName file contents error";/log warning $errorMessage;:returnfalse;};# date time set:do{/system/clock/setdate=[$LoadValue $fileContents date];/system/clock/settime=[:totime[$LoadValue $fileContents";time"]];/log debug"$scriptName executed";:returntrue;}on-error={:seterrorMessage"$scriptName date time set error";/log warning $errorMessage;:returnfalse;}; ``` 
```
---
```

## Response 3
Author: Tue May 28, 2024 7:05 pm
``` /system/ntp/client/getstatusas-string ``` too many useless steps...as I already said, just create the file, and then re-read the time and date of the file, without wasting time writing and reading inside the file...It is better to run time-sensitive scripts after checking the NTP status:
```
---
```

## Response 4
Author: [SOLVED]Tue Sep 03, 2024 7:08 pm
thank you for your replyinghere is the easiest way to do thissave the time and date in text file time.txt and put it in the root directory interval 10m for example:/system scheduler add name=save-time start-time=startup interval=10m on-event=":delay 60s\r\\n:local currentTime [/system clock get time]\r\\n:local currentDate [/system clock get date]\r\\n/file print file=time.txt where name=\"time.txt\"\r\\n/file set time.txt contents=\"\$currentDate \$currentTime\""and restore it by using this:/system scheduler add name=restore-time start-time=startup on-event=":local savedTime [/file get time.txt contents]\r\\n:local savedDate [:pick \$savedTime 0 10]\r\\n:local savedClock [:pick \$savedTime 11 19]\r\\n/system clock set date=\$savedDate time=\$savedClock"note:if you use another time format like v6 (jul/02/2024) you need to change the pick value to 0 11 and 12 20