# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 208782

# Discussion

## Initial Question
Author: Thu Jun 27, 2024 5:56 am
``` local user "26031970"; :local iValidUntil [/system scheduler get $user next-run]; put "$iValidUntil" sample output: 2024-06-28 01:30:11 ``` Hello Everyone, Anyone can give me a script on how to separate date and time on the scheduler for the next run.
```
---
```

## Response 1
Author: [SOLVED]Thu Jun 27, 2024 10:46 am
``` { :local test "2024-06-28 01:30:11" :local findfrom -1 ; # -1 mean "from the start" :local spaceposition [:find $test " " $findfrom] ; # find inside the string the character [SPACE] from the start :local dstartposition 0 ; # the date start at the begin of the string :local dendposition $spaceposition ; # the date end before the [SPACE] position :local tstartposition ($spaceposition + 1) ; # the time start after [SPACE] position :local tendposition [:len $test] ; # the time end at the last character of the string :local d [:pick $test $dstartposition $dendposition] ; # pick the date :local t [:pick $test $tstartposition $tendposition] ; # pick the time :put "Date is >$d< and Time is >$t<" } ``` ``` { :local test "2024-06-28 01:30:11" :local d [:pick $test 0 10] :local t [:pick $test 11 19] :put ">$d<" :put ">$t<" } ``` Do not use useless ; and put everytime the : on :local and :putNo matter if is only one examle. Bad habit stay on all little things.
```
Since the format have everytime the same lenght and position, can be simplified with static lenght and position:
```