# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 208113

# Discussion

## Initial Question
Author: [SOLVED]Sun Jun 02, 2024 12:18 pm
``` {:localCurrentDate[/system clockgetdate]:localCurrentDay"10"#[:pick $CurrentDate 8 10]:localCurrentMonth"12"#[:pick $CurrentDate 5 7]:localCurrentYear"2027"#[:pick $CurrentDate 0 4]:localLastYear($CurrentYear-1):localdayX:localmonthX:localyearX:localdateX:locallastday:globalLifeDay:localleapyear:localyeardiv:localyearmult:setyeardiv($CurrentYear/4):setyearmult($yeardiv*4):if([$yearmult]=$CurrentYear)do={:setleapyeartrue}else={:setleapyearfalse}:if([$CurrentMonth]="01")do={:setlastday"31"}:if([$CurrentMonth]="02")do={:if($leapyear=true)do={:setlastday"29"}:if($leapyear=false)do={:setlastday"28"}}:if($CurrentMonth="03")do={:setlastday"31"}:if($CurrentMonth="04")do={:setlastday"30"}:if($CurrentMonth="05")do={:setlastday"31"}:if($CurrentMonth="06")do={:setlastday"30"}:if($CurrentMonth="07")do={:setlastday"31"}:if($CurrentMonth="08")do={:setlastday"31"}:if($CurrentMonth="09")do={:setlastday"30"}:if($CurrentMonth="10")do={:setlastday"31"}:if($CurrentMonth="11")do={:setlastday"30"}:if($CurrentMonth="12")do={:setlastday"31"}:put $CurrentMonth:put $lastday:localdayX($CurrentDay+$LifeDay);:if($dayX<=$lastday)do={:setmonthX($CurrentMonth):setyearX($CurrentYear)}:if($dayX>$lastday)do={:if($CurrentMonth="12")do={:setdayX($dayX-$lastday):setmonthX($CurrentMonth-"11"):setyearX($CurrentYear+"1")}:if($CurrentMonth<"12")do={:setdayX($dayX-$lastday):setmonthX($CurrentMonth+"1"):setyearX($CurrentYear)}}:localmonthY[:len $monthX]:localdayY[:len $dayX]:if($monthY=1)do={:set$monthX("0".$monthX)}:if($dayY=1)do={:set$dayX("0".$dayX)}:localdateX($yearX."-".$monthX."-".$dayX):put $dateX} ``` Good morning everyone, I created this script to allow the user via the LifeDay variable to decide after how many days to schedule the deletion of a hotspot user. the script works perfectly. writes the date in YYYY-MM-DD format in the user's comment. another script reads how long the user has been active and if he has exceeded the days set in LifeDay it has been shown to delete him. In your opinion, is the part of the screenplay that I post below well done? From the tests I've done it seems reliable, but maybe it can be simplified with fewer lines
```
---
```

## Response 1
Author: Sun Jun 02, 2024 12:38 pm
``` :setlastday"31":if([$CurrentMonth]="02")do={:if($leapyear=true)do={:setlastday"29"}:if($leapyear=false)do={:setlastday"28"}}:if($CurrentMonth="04")do={:setlastday"30"}:if($CurrentMonth="06")do={:setlastday"30"}:if($CurrentMonth="09")do={:setlastday"30"}:if($CurrentMonth="11")do={:setlastday"30"} ``` Six lines less (not much):
```
Italian:30 dì conta novembre, con april, giugno e settembre, di 28 ce n'è uno,tutti gli altri ne han 31.https://it.wikipedia.org/wiki/Trenta_giorni_ha_novembreEnglish:https://en.wikipedia.org/wiki/Thirty_Da ... _SeptemberThirty days has September,April, June, and November,All the rest have thirty-one,Save February at twenty-eight,But leap year, coming once in four,February then has one day more.


---
```

## Response 2
Author: Tue Jun 04, 2024 2:52 am
``` :local daysOnMnt [:toarray "31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31"] :if ((($yyyy - 1968) % 4) = 0) do={:set ($daysOnMnt->1) 29} ``` extract code