# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 183631

# Discussion

## Initial Question
Author: [SOLVED]Fri Feb 25, 2022 9:03 pm
``` # # Created Jotne 2024 v1.7 # # 1.7 Fixed new CHR naming (Credit bp0 & baragoon) # 1.6 Fixed script for x86 devicews (Credit rextended) # 1.5 Fixed for router missing serial # 1.4 Added Router OS version # 1.3r Revised by rextended # 1.3 / 1.2 try to fix v6/v7 compability # 1.1 added "show-sensitive" # 1.0 initial release # # Takes two different backup and send then to email # # backup.rsc readable backup # Certificates, the Dude and Usermanager are also NOT exported or backed up fully and should be backed up separately # Can be used to restore config to different routers # # backup.bin binary backup # Binary backup that can only be used to fully restored the same router. # :local email "<your mail>@gmail.com" :local rscfn "backup" :local bakfn "bin" /system :local date [clock get date] :local time [clock get time] :local info [identity get name] :local board [resource get board-name] :local files "$rscfn.rsc,$bakfn.backup" :local Version [resource get version] /system :local serial "undefined" :if (!($board~"(x86|CHR)")) do={ :global testrbsn "NO RouterBOARD" :execute ":global testrbsn; :set testrbsn [/system routerboard get serial-number]" :delay 1s :set serial $testrbsn :set testrbsn } else={ :if ($board="x86") do={:set serial [license get software-id]} :if ($board~"CHR") do={:set serial [license get system-id]} } :if ($Version~"^7") do={ [:parse "/export show-sensitive file=$rscfn.rsc"] } else={ /export file="$rscfn.rsc" } :delay 2s /system backup save name="$bakfn" :delay 2s /tool e-mail send to="$email" subject="Mikrotik: Backup $info $Version $serial" file="$files" body="Automatic Backup of $info $serial at $date $time" :delay 20s :execute "/file remove $files" :log info "Backup router=$info serial=$serial ok" ``` Backup script to send config to Gmail account.
```
PS Since gmail are free, I suggest you make a new email for your backup files.----------------------------------------------------------------------------------------UseSplunk>to log/monitor yourMikroTikRouter(s). See link below.MikroTik->Splunk


---
```

## Response 1
Author: Fri Feb 25, 2022 11:11 pm
``` { :local vermajor [:tonum [:pick [/system resource get version] 0 1]] :if ($vermajor > 6) do={ [:parse "export show-sensitive file=backup.rsc"] } else={ :export file=backup.rsc } } ``` Their syntax checker kicks in... But you could still cheat with [:parse ":export ..."].
```
I always thought it strange they didn't just add "show-sensitive" as option in the V6 codeline, even if it's implied in V6.  That wouldn't break annoying thing in V6, but avoid needing a stupid [:parse ""] thing for a common task.  (and yes, I'm sure they need to deal with BOTH show-sensitive and hide-sensitive in V6, but scripts would then be portable between V6/V7)


---
```

## Response 2
Author: Sat Feb 26, 2022 12:29 am
``` # # Created Jotne 2022 v1.3 # # 1.1 Added "show-sensitive" # 1.3 Fixed v6/v7 compability # # Takes two different backup and send then to email # # backup.rsc readable backup # Certificates, the Dude and Usermanager are also NOT exported or backed up fully and should be backed up separately. Can be used to restore config to different routers # # backup.bin binary backup # Binary backup that can only be used to fully restored the same router. # :local email "<your mail>@gmail.com" :if ([:tonum [:pick [/system resource get version] 0 1]] > 6) do={ [:parse "export show-sensitive file=backup.rsc"] } else={ :export file=backup.rsc } :delay 2s /system backup save name=bin :delay 2s :local date [/system clock get date] :local time [/system clock get time] :local info [/system identity get name] :local serial [/system routerboard get serial-number] :local files "backup.rsc, bin.backup" /tool e-mail send to="$email" subject="Mikrotik: Backup $info $serial" file=$files body="Automatic Backup of $info $serial at $date $time." :delay 20s /file remove backup.rsc /file remove bin.backup :log info message="Backup router=$info serial=$serial ok" ``` Perfect. Did learn some new today, so thank you for the helpWas just what I needed and have tested the script on various version and works fine.
```
---
```

## Response 3
Author: Sat Feb 26, 2022 11:09 am
``` # # Created Jotne 2022 v1.3r # # 1.3r Revised by REX # 1.3 / 1.2 try to fix v6/v7 compability # 1.1 added "show-sensitive" # 1.0 initial release # # Takes two different backup and send then to email # # backup.rsc readable backup # Certificates, the Dude and Usermanager are also NOT exported or backed up fully and should be backed up separately # Can be used to restore config to different routers # # backup.bin binary backup # Binary backup that can only be used to fully restored the same router. # { :local email "<your mail>@gmail.com" :local rscfn "backup" :local bakfn "bin" /system :local date [clock get date] :local time [clock get time] :local info [identity get name] :local serial [routerboard get serial-number] :local files "$rscfn.rsc,$bakfn.backup" /system resource :if ([get version]~"^7") do={ [:parse "/export show-sensitive file=$rscfn.rsc"] } else={ /export file="$rscfn.rsc" } :delay 2s /system backup save name="$bakfn" :delay 2s /tool e-mail send to="$email" subject="Mikrotik: Backup $info $serial" file="$files" body="Automatic Backup of $info $serial at $date $time" :delay 20s :execute "/file remove $files" :log info "Backup router=$info serial=$serial ok" } ``` Revised by REX codeEdit: put back the [ ] on :parse for v7 (invalid syntax but, thank to "if", never executed on v6) ---

## Response 4
Author: Sat Feb 26, 2022 12:01 pm
``` :parse "/export show-sensitive file=test.rsc" ``` ``` [:parse "/export show-sensitive file=test.rsc"] ``` Does not work. Tested in 7.1.2Pasting this to terminal, does not give anything.
```
But this works:
```

```
---
```

## Response 5
Author: Sat Feb 26, 2022 5:00 pm
``` :parse "/export show-sensitive file=test.rsc" ``` ``` [:parse "/export show-sensitive file=test.rsc"] ``` ``` :put [:parse "/ip address print"] #(eval /ip address print) :put [:typeof [:parse "/ip address print"]] # code ``` We wouldn't be here if either V7 or V6 just ignored a meaningless "hide-sensitive" or "show-sensitive" – that seem like something MT should fix somehow...Does not work. Tested in 7.1.2Pasting this to terminal, does not give anything.
```
But this works:
```

```
":parse"alonecreates a :typeof "code", at "runtime".  But the context that :parse used matters, since it acts more like a script do={} function – so it's more confusing than it appears.  You can see the "code" type here:
```

```
Before my time in RouterOS, but believe ":parse" was a way to create functions before the ":global fn do={}" way.  So if you view that ":parse <string_script>" is same as do={<actual_script>}, then " :parse" is a definition of something runnable, why :parse at CLI doesn't run anything.


---
```

## Response 6
Author: Sat Feb 26, 2022 9:54 pm
``` :global x do={:put "blah"} # Version 7 it's ";evl(" that need to be :find /system script environment print detail where name=x # 3 name="x" value=";(evl (evl /putmessage=blah))" # But in Version 6, it's ";eval" that's @rextended uses /system script environment print detail where name=x # 1 name="x" value=";(eval (eval /putmessage=blah))" ``` ``` # did not work in V7 $bymail $dsubj="Certificate $certname $date $time" $dfile="auto_$certname.p12" # works in V7 ($bymail $dsubj="Certificate $certname $date $time" $dfile="auto_$certname.p12") # NOTE: I'm not sure the $ in $dsubj= needed ``` My version do work at both 6 and 7. What do I need to make rextendeds script to work on 7.x?@Jonte, which one, and what problem you having? I can offer what see in @rextended's examples below, but can't vouch that's all the V7 issues.save and restore global variables on rebootviewtopic.php?f=9&t=170591&p=883422#p883422I didn't try this one, but I DO know it won't detect functions right in V7. "eval" is now "evl", here no :parse be needed, just different string to look for in V7 vs V6 to fix that one.
```
Basically those are :typeof str, but represent the "compiled script" which why @rextended excludes them.  Only issue how he's identifying them similar ":if ($majorversion>6) do={} else={}" thing.Save RouterBOARD full backup of everything [configuration, certificates, host key, router users (no passwords), user-manager, dude, other files]viewtopic.php?f=1&t=175360&p=858564#p858564This one has a different problem.  I don't know exactly why but the "$byemail ..." lines need be wrapped in a parenthesis.  Only did a quick test, but changing the ALL the $byemail lines like this:
```

```
I've found being using a "command subdirectory" to then "short form" find/get/set's sometimes causes odd issues in V7.  Do something like "/certificate", then your code does make the script more human readable – but RouterOS "script compiler" seems to needs more help to figure stuff out when you do that.   So putting commands or functions with parameters in parenthesis and/or brackets often helps MT's hidden script compiler.  In theory, I wouldn't say you should need them, but the ($bymail ...) fixed @rextended's backup script on v7.2rc4 in my quick test.


---
```

## Response 7
Author: Sun Feb 27, 2022 12:24 am
``` if ([:tonum [:pick [/system resource get version] 0 1]] > 6) do={ # translated: pick one character from the start of the version string, convert it to a number, if the resulting number is greater than 6 do ... ``` ``` /system resource :if ([get version]~"^7") do={ # translated: if the version string contains "7" at the beginning do ... ``` My version do work at both 6 and 7. What do I need to make rextendeds script to work on 7.x?(I have edited previous post)The "related" link are not fully tested on v7 (see the dates of the posts...)Ok, I understand why you do not understand:The code itself is formally valid until not executed,(for be more precise, is invalid the "show-sensitive" inside, not the use of the [ ])the condition is never meet and never executed on v6Put back [ ] on my "revision" work again on v7My revision is only a hint for explain some "shortcut" or better style of coding...For example: put / in front of export, because "export" export only current section.:parse and :execute both consider / as start point, but if on future thath change, script is already ready...Another exampleall this
```
can be replaced with simpler and fastly readable
```

```
it work until version 70.x do not come out on year 2345 (for fixit on year 2345, simply add \. at the end, if someone of us is stil alive...)If sometime on the future 8.x come out, probably the syntax change again, but if on 8, 9, 10 etc, is identical, use something like "^(7|8|9|10)"For precision (tested on 6.47.10)::parse "export file=backup.rsc" on v6 do not work like on v7[:parse "export file=backup.rsc"] this work on both (but on v7 the new default do not export the sensitive data)[:parse "export show-sensitive file=backup.rsc"] work only on v7 and NOT on v6, because have show-sensitive inside, not recognized on v6


---
```

## Response 8
Author: Sun Feb 27, 2022 1:16 am
``` :global x do={:put "blah"} # Version 7 it's ";evl(" that need to be :find /system script environment print detail where name=x # 3 name="x" value=";(evl (evl /putmessage=blah))" # But in Version 6, it's ";eval" that's @rextended uses /system script environment print detail where name=x # 1 name="x" value=";(eval (eval /putmessage=blah))" ``` ``` :if ([:typeof [:find $vvalue "(eval " -1]] = "nil") do={ ``` ``` :if (([:typeof [:find $vvalue "(eval " -1]] = "nil") and ([:typeof [:find $vvalue "(evl " -1]] = "nil")) do={ ``` I didn't try this one, but I DO know it won't detect functions right in V7. "eval" is now "evl", here no :parse be needed, just different string to look for in V7 vs V6 to fix that one.
```
probably the fix for work on both v6 and v7 is to replacev6 only codewithv6 and v7 code


---
```

## Response 9
Author: Sun Feb 27, 2022 1:42 am
``` # did not work in V7 $bymail $dsubj="Certificate $certname $date $time" $dfile="auto_$certname.p12" # works in V7 ($bymail $dsubj="Certificate $certname $date $time" $dfile="auto_$certname.p12") # NOTE: I'm not sure the $ in $dsubj= needed ``` ``` $bymail dsubj=("Certificate $certname $date $time") dfile=("auto_$certname.p12") $bymail dsubj=("Host Key $date $time") dfile="auto_host-key_dsa, auto_host-key_dsa.pub, auto_host-key_rsa, auto_host-key_rsa.pub" $bymail dsubj=("User Export $date $time") dfile="auto_user_export.rsc" $bymail dsubj=("Backup $date $time") dfile="auto_backup.backup" $bymail dsubj=("Database User-Manager $date $time") dfile="auto_user-manager.umb" $bymail dsubj=("Database The Dude $date $time") dfile="auto_thedude.db" ``` This one has a different problem. I don't know exactly why but the "$byemail ..." lines need be wrapped in a parenthesis. Only did a quick test, but changing the ALL the $byemail lines like this:
```
[...]the ($bymail ...) fixed @rextended's backup script on v7.2rc4 in my quick test.Thanks.The correct syntax iswithout $in front of dsubj and dfile,(caused for make consistant name of variables using replace $oldvarname with $newvarname, without removing $ when is not to be placed)AND if used $var inside the strings, parenthesys ( ) must be used.no need to use ( ) when the string not contain $varnameThanks to you I just discover this strange behaviour.Correct lines are (I have corrected the original script)
```

```
---
```

## Response 10
Author: Sun Feb 27, 2022 2:08 am
``` :if ($vtype~"^(ip-prefix|ip6-prefix)\$") do={:execute ":global $vname [[:parse \":return $vvalue\"]]"} ``` ``` [rex@MATRIX] > :global test 1.1.1.0/24 [rex@MATRIX] > :put [:typeof $test] ip-prefix [rex@MATRIX] > :global test "1.1.1.0/24" [rex@MATRIX] > :put [:typeof $test] str [rex@MATRIX] > :global test [:toip "1.1.1.0/24"] [rex@MATRIX] > :put [:typeof $test] nil [rex@MATRIX] > :global test [[:parse ":return 1.1.1.0/24"]] [rex@MATRIX] > :put [:typeof $test] ip-prefix ``` [...] in V7. "eval" is now "evl", here no :parse be neededI need to use this on v6
```
because someone on the past broken the ":toip" function and for convert 1.1.1.0/27 to ip-prefix variable type I need to use this hack...v6 ip-prefix example code


---
```

## Response 11
Author: Mon Feb 28, 2022 6:00 pm
``` :global rosmajorver [:tonum [:pick [/system resource get version] 0 1]] :global rtlookup :set $rtlookup do={ :if ($rosmajorver>6) do={ :return [[:parse "/routing table find where name=$1"]] } else={ :return $1 } } # >> :put [$rtlookup main] # *0 ``` ``` /ip firewall nat find where routing-mark=[$rtlookup "main"] ``` Sound familiar:viewtopic.php?p=881126&hilit=v7#p881126It was a long time age...even before the Russian war.Yeah it not only ":export XXXX-sensitive" attributes that differ subtle ways. I've been using V7 as excuse to re-writing my V6 scripts as functions, which has worked out well so far: basically everything is aparameterized function. So if you combine [:parse] WITH a function to apply @rextended's route table fix in above post...
```
With that above your firewall script, like so:
```

```
The function will hide the "ugly" :parse, and in theory you can use extend the above function to validate the route table for V6 etc.  But using functions is how I've generically solve any some of oddities without a lot of ":if () do={}"'s everywhere.Note: I know the code works for "main", but didn't test too much – more example of an approach to the next "show-sensitive".


---
```

## Response 12
Author: Mon Feb 28, 2022 6:25 pm
``` :if ($vtype~"^(ip-prefix|ip6-prefix)\$") do={:execute ":global $vname [[:parse \":return $vvalue\"]]"} ``` [...] in V7. "eval" is now "evl", here no :parse be neededI need to use this on v6
```
because someone on the past broken the ":toip" function and for convert 1.1.1.0/27 to ip-prefix variable type I need to use this hack...Oh that's a fun one!  In the: "very cleaver solution, but annoying it's needed" category – but be a long wait for some ":toip-prefix" (or fixing/paramerizing :toip and other :toX) built-in....   Quite the path:a :execute "background script", that's generated dynamically via :parse, to update a global variable used in the current – all because only a ":global" type definition will actually do a convert from string to a "ip[6]-prefix" type, BUT where you can define a global is limited.  Somehow @rextended approach here does works, pretty nifty.


---
```

## Response 13
Author: Mon May 09, 2022 10:35 am
``` # # Created Jotne 2022 v1.4 # # 1.4 Added Router OS version # 1.3r Revised by REX # 1.3 / 1.2 try to fix v6/v7 compability # 1.1 added "show-sensitive" # 1.0 initial release # # Takes two different backup and send then to email # # backup.rsc readable backup # Certificates, the Dude and Usermanager are also NOT exported or backed up fully and should be backed up separately # Can be used to restore config to different routers # # backup.bin binary backup # Binary backup that can only be used to fully restored the same router. # :local email "<your mail>@gmail.com" :local rscfn "backup" :local bakfn "bin" /system :local date [clock get date] :local time [clock get time] :local info [identity get name] :local serial [routerboard get serial-number] :local files "$rscfn.rsc,$bakfn.backup" :local Version [resource get version] :if ($Version~"^7") do={ [:parse "/export show-sensitive file=$rscfn.rsc"] } else={ /export file="$rscfn.rsc" } :delay 2s /system backup save name="$bakfn" :delay 2s /tool e-mail send to="$email" subject="Mikrotik: Backup $info $Version $serial" file="$files" body="Automatic Backup of $info $serial at $date $time" :delay 20s :execute "/file remove $files" :log info "Backup router=$info serial=$serial ok" ``` Script updated to v1.4Now also sends router version information in the subject. Faster to see when router was upgraded.
```
---
```

## Response 14
Author: Mon May 09, 2022 11:28 am
``` :local Version [/system/resource get version] -> :local Version [resource get version] ``` @JotneScript updated to v1.4When something needs to be run on both versions, don't use syntax compatible only with v7
```
---
```

## Response 15
Author: Mon May 09, 2022 12:28 pm
``` :local Version [/system/resource get version] -> :local Version [resource get version] ``` When something needs to be run on both versions, don't use syntax compatible only with v7
```
Good catch, updated.


---
```

## Response 16
Author: Mon Aug 08, 2022 10:54 pm
``` :local email "my@email.com" :local rscfn "$info. "-" .$date. "-" .$time" :local bakfn "$info. "-" .$date. "-" .$time" ``` Hi, thank you for this script. Works fine. Just note, how can I change name of files?now I have backup.rsc , bin.backupwant to have for example $info.backup, so it will be ie RB4011.backupTried to add it, script stopped work for me.Thank you
```
---
```

## Response 17
Author: Mon Aug 08, 2022 11:57 pm
``` :local email "my@email.com" :local rscfn "$info-$date-$time" :local bakfn "$info-$date-$time" # or :local email "my@email.com" :local rscfn ($info . "-" . $date . "-" . $time) :local bakfn ($info . "-" . $date . "-" . $time) ``` date contain special character /time contain special character :and the routerboard name alsocancontain special charactersbut ignoring that, your syntax is wrong (and why use two variables to store same things inside...)
```
---
```

## Response 18
Author: Tue Aug 09, 2022 6:41 pm
``` :local email "my@email.com" :local rscfn "$info-$date-$time" :local bakfn "$info-$date-$time" # or :local email "my@email.com" :local rscfn ($info . "-" . $date . "-" . $time) :local bakfn ($info . "-" . $date . "-" . $time) ``` 
```
tried both, doesn't work fine.Attachments are now:--.rsc--.backup


---
```

## Response 19
Author: Thu Oct 27, 2022 7:57 am
``` # # Created Jotne 2022 v1.4 # # 1.4 Added Router OS version # 1.3r Revised by REX # 1.3 / 1.2 try to fix v6/v7 compability # 1.1 added "show-sensitive" # 1.0 initial release # # Takes two different backup and send then to email # # backup.rsc readable backup # Certificates, the Dude and Usermanager are also NOT exported or backed up fully and should be backed up separately # Can be used to restore config to different routers # # backup.bin binary backup # Binary backup that can only be used to fully restored the same router. # :local email "<your mail>@gmail.com" :local rscfn "backup" :local bakfn "bin" /system :local date [clock get date] :local time [clock get time] :local info [identity get name] :local serial [routerboard get serial-number] :local files "$rscfn.rsc,$bakfn.backup" :local Version [resource get version] :if ($Version~"^7") do={ [:parse "/export show-sensitive file=$rscfn.rsc"] } else={ /export file="$rscfn.rsc" } :delay 2s /system backup save name="$bakfn" :delay 2s /tool e-mail send to="$email" subject="Mikrotik: Backup $info $Version $serial" file="$files" body="Automatic Backup of $info $serial at $date $time" :delay 20s :execute "/file remove $files" :log info "Backup router=$info serial=$serial ok" ``` Script updated to v1.4Now also sends router version information in the subject. Faster to see when router was upgraded.
```
The script does not work. I put in script with "don't require permission". Where did it goes wrong?


---
```

## Response 20
Author: Thu Oct 27, 2022 6:34 pm
``` :local serial na :if ($board!="CHR") do={ /system routerboard :set serial [get serial-number] } else={ /system license :set serial [get system-id] } ``` must be tested
```
---
```

## Response 21
Author: Fri Jan 20, 2023 12:52 pm
``` /system license :set serial [get system-id] ``` ``` /system license :set serial [get software-id] ``` Hi Jotne, I have tested your script with RouterOS version 7.7 and this part does not work:
```
Now it is:
```

```
Greetings.


---
```

## Response 22
Author: Fri Jan 20, 2023 8:47 pm
``` [admin@MikroTik] /system/license> pr software-id: XXXX-XXXX nlevel: 5 features: ``` I'm sorry, but I don't understand Jotne's answer.I mean this: (non system-id)
```
That's all.BR.


---
```

## Response 23
Author: Sat Jan 21, 2023 2:01 am
``` { /system :local board ([/system resource get board-name]) :local serial na :if ($board!="x86") do={ /system routerboard :set serial [get serial-number] } else={ /system license :set serial [get system-id] } :put "$serial" } ``` ``` :put ([/system resource get board-name]) x86 ``` ``` :local serial na :if ($board!="CHR") do={ :set serial [routerboard get serial-number] } else={ /system license :set serial [get system-id] } ``` ``` :local serial <your id> ``` This part does not work on x86 routers, it seems to not like the routerboard command.After testing adding the correct x86 name like this:
```
I get this output on 7.7 routerOS on x86.gmail.png.Just to show the version:
```

```
To get it to work temporarily, just replace this:
```

```
with this
```

```
---
```

## Response 24
Author: Sat Jan 21, 2023 2:10 am
``` :global thisvar "no routerboard" :execute ":global thisvar; :set thisvar [/system routerboard get serial-number]" :delay 1s :put $thisvar ``` when you do not know if something exist...
```
---
```

## Response 25
Author: Sat Jan 21, 2023 2:38 am
``` { /system :local board [resource get board-name] :local serial "undefined" :if (!($board~"(x86|CHR)")) do={ :global testrbsn "NO RouterBOARD" :execute ":global testrbsn; :set testrbsn [/system routerboard get serial-number]" :delay 1s :set serial $testrbsn :set testrbsn } else={ :if ($board="x86") do={:set serial [license get software-id]} :if ($board="CHR") do={:set serial [license get system-id]} } :put "$serial" } ``` run code ---

## Response 26
Author: Sat Apr 01, 2023 9:20 pm
``` # # Created Jotne 2023 v1.6 # # 1.6 Fixed script for x86 devicews (Credit rextended) # 1.5 Fixed for router missing serial # 1.4 Added Router OS version # 1.3r Revised by rextended # 1.3 / 1.2 try to fix v6/v7 compability # 1.1 added "show-sensitive" # 1.0 initial release # # Takes two different backup and send then to email # # backup.rsc readable backup # Certificates, the Dude and Usermanager are also NOT exported or backed up fully and should be backed up separately # Can be used to restore config to different routers # # backup.bin binary backup # Binary backup that can only be used to fully restored the same router. # :local email "<your mail>@gmail.com" :local rscfn "backup" :local bakfn "bin" /system :local date [clock get date] :local time [clock get time] :local info [identity get name] :local board ([resource get board-name]) :local files "$rscfn.rsc,$bakfn.backup" :local Version [resource get version] /system :local serial "undefined" :if (!($board~"(x86|CHR)")) do={ :global testrbsn "NO RouterBOARD" :execute ":global testrbsn; :set testrbsn [/system routerboard get serial-number]" :delay 1s :set serial $testrbsn :set testrbsn } else={ :if ($board="x86") do={:set serial [license get software-id]} :if ($board="CHR") do={:set serial [license get system-id]} } :if ($Version~"^7") do={ [:parse "/export show-sensitive file=$rscfn.rsc"] } else={ /export file="$rscfn.rsc" } :delay 2s /system backup save name="$bakfn" :delay 2s /tool e-mail send to="$email" subject="Mikrotik: Backup $info $Version $serial" file="$files" body="Automatic Backup of $info $serial at $date $time" :delay 20s :execute "/file remove $files" :log info "Backup router=$info serial=$serial ok" ``` Backup script to send config to Gmail account.
```
----------------------------------------------------------------------------------------UseSplunk>to log/monitor yourMikroTikRouter(s). See link below.  :mrgreen:MikroTik->SplunkThanks a lot for your script, sir!


---
```

## Response 27
Author: Thu Feb 01, 2024 12:37 am
``` # # Created Jotne 2023 v1.6 # # 1.6 Fixed script for x86 devicews (Credit rextended) # 1.5 Fixed for router missing serial # 1.4 Added Router OS version # 1.3r Revised by rextended # 1.3 / 1.2 try to fix v6/v7 compability # 1.1 added "show-sensitive" # 1.0 initial release # # Takes two different backup and send then to email # # backup.rsc readable backup # Certificates, the Dude and Usermanager are also NOT exported or backed up fully and should be backed up separately # Can be used to restore config to different routers # # backup.bin binary backup # Binary backup that can only be used to fully restored the same router. # :local email "<your mail>@gmail.com" :local rscfn "backup" :local bakfn "bin" /system :local date [clock get date] :local time [clock get time] :local info [identity get name] :local board ([resource get board-name]) :local files "$rscfn.rsc,$bakfn.backup" :local Version [resource get version] /system :local serial "undefined" :if (!($board~"(x86|CHR)")) do={ :global testrbsn "NO RouterBOARD" :execute ":global testrbsn; :set testrbsn [/system routerboard get serial-number]" :delay 1s :set serial $testrbsn :set testrbsn } else={ :if ($board="x86") do={:set serial [license get software-id]} :if ($board="CHR") do={:set serial [license get system-id]} } :if ($Version~"^7") do={ [:parse "/export show-sensitive file=$rscfn.rsc"] } else={ /export file="$rscfn.rsc" } :delay 2s /system backup save name="$bakfn" :delay 2s /tool e-mail send to="$email" subject="Mikrotik: Backup $info $Version $serial" file="$files" body="Automatic Backup of $info $serial at $date $time" :delay 20s :execute "/file remove $files" :log info "Backup router=$info serial=$serial ok" ``` Backup script to send config to Gmail account.
```
----------------------------------------------------------------------------------------UseSplunk>to log/monitor yourMikroTikRouter(s). See link below.MikroTik->SplunkThanks a lot for your script, sir!Love this! Many thanks to you guys !


---
```

## Response 28
Author: Mon Apr 22, 2024 9:22 pm
There is a change not included in change list. /system resource board-name for CHR now has extra information about the host/platform it is running on.For example, it might now be "CHR x86 Xen HVM domU"So, testing if board-name is "CHR" no longer works; you'd need to use something like /^CHR/.