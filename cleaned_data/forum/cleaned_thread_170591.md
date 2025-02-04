# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 170591

# Discussion

## Initial Question
Author: Sat Jan 30, 2021 11:09 am
by baidu translate ：I have a method to define a schedule to read environment variables to the array every minute. In the definition of the second boot from the start of the schedule. Use the acquired array to write to the second schedule at any time. Maybe the idea is to make it by yourselfThere is only one command to demonstrate ：:put [/system script environment print as-value ] ---

## Response 1
Author: [SOLVED]Sat Oct 02, 2021 1:30 pm
``` /system script environment :foreach item in=[find] do={ :local vname [get $item name] :local vvalue [get $item value] :if ($vvalue~"^\\*") do={:set vvalue "ID$vvalue"} :if ($vvalue~"^(\\(code\\)|;\?\\(eva\?l )") do={:set vvalue "(code)"} /ip firewall layer7 remove [find where name=$vname] add name=$vname comment="$vvalue" :delay 10ms :execute "/ip firewall layer7 set [find where name=$vname] regexp=[:typeof \$$vname]" :if ($vvalue="(code)") do={:delay 10ms ; set [find where name=$vname] regexp="code"} } ``` ``` /ip firewall layer7 :foreach item in=[find where regexp~"^(array|bool|code|id|ip|ip-prefix|ip6|ip6-prefix|lookup|nil|nothing|num|str|time)\$"] do={ :local vname [get $item name] :local vvalue [get $item comment] :local vtype [get $item regexp] /system script environment remove [find where name=$vname] :if ($vtype~"^(array|ip|ip6|num|str|time)\$") do={ :execute ":global $vname [:to$vtype [/ip firewall layer7 get [find where name=$vname] comment]]" } else={ :if ($vtype~"^(bool|id|ip-prefix|ip6-prefix|lookup|nil|nothing)\$") do={ :if ($vtype="bool") do={:execute ":global $vname [:tobool $vvalue]"} :if ($vtype="id") do={:execute ":global $vname [:toid $[:pick $vvalue [:find $vvalue "*" -1] [:len $vvalue]]]"} :if (($vtype="ip-prefix") or \ ($vtype="ip6-prefix")) do={:execute ":global $vname [[:parse \":return $vvalue\"]]"} :if ($vtype="lookup") do={:execute ":global $vname \"\$$vname\""} :if ($vtype="nil") do={:execute ":global $vname"} :if ($vtype="nothing") do={:execute ":global $vname [:nothing]"} } else={ # vtype="code" :log error "Unknow variable >$vname< of type >$vtype<" :execute ":global $vname [/ip firewall layer7 get [find where name=$vname] comment]" } } :delay 10ms } ``` search tag # rextended save and restore global variables on rebootThis is for save and restore variables withkeeping the right data type on restore:Scheduled script do that every x minutes, on purpose store only variables, butdo not store codes or functionsbecause till now I do not have find one way to do that.code= from ":parse" function, like :global c [:parse "/interface print"]function= created like :global f do={ /interface print }, but is reported as array from :typeofOnly simple arrays are exported, do not work for array of array and more complex data structure.
```
Store variable name... on name, variable type on regexp, variable contents on comment.On reboot this script is scheduled at startup, this restore also variables that do not contain readable data, like binary data, lower numbers and special characters:
```

```
True Level 7 rules for Firewall are not "touched" unless they regexp is exactly a single word as the names of reserved variable types.Someone know the full list of variable types???standard:arrayboolidipip6numstrtimebroken, but restored with an hack:ip-prefixip6-prefixnot recoverable:codefunction (reported as array)"undefined" types:nilnothinglookup ($0 on functions)The script is not fixed for unknow data types discovered from me on 2023:viewtopic.php?p=1014223#p1014223apireq (api request)exclamationcmditeratorbackreferenceEDIT: added fix for new discovered "op" on RouterOS, thanks to@tabrahamreport2025 EDIT: added missing types discovered on 2023


---
```

## Response 2
Author: Tue May 31, 2022 10:46 am
``` :if ($vtype = "bool") do={ [[:parse ":global $vname [:to$vtype $[/ip firewall layer7 get [find where name=$vname] regexp]]"]]} ``` ``` :if ($vvalue = "(function)") do={:set vtype "function" } ``` Thanks to the author for the very beautifully written scripts for saving and restoring global variables.There are comments:In the save script, you need to remove the save "(function)", since it will not be possible to restore the function code.Only variables should be saved and restored.When restoring, restoring boolean variables via :execute does not work for me, all boolean variables are restored as nil (have no values).I had to insert such a check and restore via :parse
```
In this form, everything works.You also need to remove the line from the recovery script
```

```
since the functions are not saved and they do not need to be restored, they will have to be redefined again.


---
```

## Response 3
Author: Tue May 31, 2022 3:22 pm
``` :if ($vtype = "bool") do={ [[:parse ":global $vname [:to$vtype $[/ip firewall layer7 get [find where name=$vname] regexp]]"]]} ``` ``` :if ($vtype="bool") do={:execute ":global $vname [:tobool $vvalue]"} ``` When restoring, restoring boolean variables via :execute does not work for me, all boolean variables are restored as nil (have no values).I had to insert such a check and restore via :parse
```
Yes, a bug, but simply solved with
```

```
Thanks for the info, I do some restyling and also fix boolean.About "(function)" (and CODE!)it was put there for some reasons:1) manage all the types as possible,2) in the future maybe they can be managed directly, and it is already ready3) is ready for add on script the search for file in (flash/)functions/vname.rsc or (flash/)codes/vname.rsc and load it at startup, if the file exist...On this way also codes and functions are restored...But is not intended to store inside the file the code "(eval /interface print)" because also if restored, can be restored only as string,actually there is no way to convert directly "(eval /interface print)" to code or function.


---
```

## Response 4
Author: Wed Jun 01, 2022 12:29 pm
``` # # The function of saving/restoring global environment variables v 01/06/2022 # $1 parameter can take values: # "save" - saving global variables in /ip firewall layer7 # "recover" - restoring global variables from layer7 # "erase" - cleaning layer7 only ! from global variables # "print" - printing to the log and terminal of the list of variables located at the time of printing in Layer7 # :global FuncGlobal do={ :if ([:typeof $0]="lookup") do={ :local count 0 :if (($1="save") or ($1="recover") or ($1="erase") or ($1="print")) do={ :if ($1="save") do={ /system script environment :foreach item in=[find] do={ :local vname [get $item name] :local vvalue [get $item value] /ip firewall layer7 remove [find where name=$vname] :if (([:typeof [:find [:tostr $vvalue] "(eval " -1]] = "nil") and ([:typeof [:find [:tostr $vvalue] "(evl " -1]] = "nil")) do={ :if ([:find $vvalue "*" -1] = 0) do={:set vvalue "ID$vvalue"} add name=$vname regex="$vvalue" :set count ($count+1) } :delay 10ms :execute "/ip firewall layer7 set [find where name=$vname] comment=[:typeof \$$vname]" } :log warning ("Function $0 has saved $count variables") :return $count} :if ($1="recover") do={ /ip firewall layer7 :foreach item in=[find where comment~"^(array|bool|id|ip|ip-prefix|ip6|ip6-prefix|num|str|time|code|nothing|nil)\$"] do={ :set count ($count+1) :local vname [get $item name] :local vvalue [get $item regexp] :local vtype [get $item comment] # :if ($vvalue = "(function)") do={:set vtype "function" } /system script environment remove [find where name=$vname] :if ($vtype~"^(array|bool|id|ip|ip6|num|str|time)\$") do={ :if ($vtype = "id") do={ :set vvalue [:pick $vvalue [:find $vvalue "*" -1] [:len $vvalue]] :execute ":global $vname [:to$vtype $vvalue]"} :if ($vtype = "bool") do={ [[:parse ":global $vname [:to$vtype $[/ip firewall layer7 get [find where name=$vname] regexp]]"]] # :if ($vtype="bool") do={:execute ":global $vname [:tobool $vvalue]"} } else={ :execute ":global $vname [:to$vtype [/ip firewall layer7 get [find where name=$vname] regexp]]" } } else={ :if ($vtype~"^(ip-prefix|ip6-prefix|nothing|nil)\$") do={ :if ($vtype~"^(ip-prefix|ip6-prefix)\$") do={:execute ":global $vname [[:parse \":return $vvalue\"]]"} :if ($vtype="nothing") do={:execute ":global $vname [:nothing]"} :if ($vtype="nil") do={:execute ":global $vname"} } else={ :log error "Unknow variable type >$vtype<" :execute ":global $vname [/ip firewall layer7 get [find where name=$vname] regexp]" } } :delay 10ms; } :log warning ("Function $0 restored $count variables") :return $count} :if ($1="erase") do={ /ip firewall layer7 :foreach item in=[find where comment~"^(array|bool|id|ip|ip-prefix|ip6|ip6-prefix|num|str|time|code|nothing|nil)\$"] do={remove $item; :set count ($count+1) } :log warning ("The repository has been cleared of $count global variables") :return $count} :if ($1="print") do={ /ip firewall layer7 :foreach item in=[find where comment~"^(array|bool|id|ip|ip-prefix|ip6|ip6-prefix|num|str|time|code|nothing|nil)\$"] do={ :set count ($count+1) :local vname [get $item name]; :local vvalue [get $item regexp]; :local vtype [get $item comment]; :put ("$vname "."$vtype "."$vvalue"); :log info ("$vname "."[ $vtype ] "."$vvalue"); } :log warning ("In Layer7 repository has $count global variables") :put ("In Layer7 repository has $count global variables") :return $count} } else={ :if ([:typeof $1]="nothing") do={:log error ("The function $0 parameter is not set"); :return ("Error $0")}} :log error ("The function $0 parameter is not valid"); :return ("Error $0"); } } # usage examples: # :log info [$FuncGlobal save] # :log info [$FuncGlobal recover] # :log info [$FuncGlobal erase] # :log info [$FuncGlobal print] # examples of erroneous usage: # :log info [$FuncGlobal] # :log info [$FuncGlobal anovertext] ``` Here's what it looks like:
```
The function can be called to save variables with the command [$FuncGlobal save] with the desired frequency. Recovery from layer7 is possible at any time, including at the start of the router. To clear leyer7 of global variables, use [$FuncGlobal erase]. It is planned to finalize with the introduction of restoring only part of the variables (for example, with a certain prefix of names)


---
```

## Response 5
Author: Wed May 24, 2023 12:09 pm
Check twice.... after reboot....If the function is:global f do={ /interface print }It's normal this::put [$f](function)Is just a text "(function)" or another script set again the function correctly... ---

## Response 6
Author: Wed May 24, 2023 12:20 pm
Check twice.... after reboot....If the function is:global f do={ /interface print }It's normal this::put [$f](function)Is just a text "(function)" or another script set again the function correctly...look at the screenshots.. ---

## Response 7
Author: Sat Jun 17, 2023 1:46 am
``` :put [:typeof (>[])] ``` I found another lost data type:
```
Return:opthis data type behaves likecode


---
```

## Response 8
Author: Sat Jun 17, 2023 2:22 am
``` :put [:typeof (>[])] ``` I found another lost data type:
```
Return:opthis data type behaves likecode????????????????????????????????????????????????????????????Thanks........


---
```

## Response 9
Author: Sat Jun 17, 2023 2:44 am
``` :global optype (>[:global z "blah"]) $optype :put $z # "blah" ``` ``` :global optype (>[:do {:put "$1"}]) :put [:typeof $optype] # op $optype "hmm" # hmm :put $optype # (evl (evl /docommand=;(evl (evl /putmessage=$1)))) ``` ``` :global shortThanToArray (>{}) :put "$shortThanToArray $[:typeof $shortThanToArray] $[:len $shortThanToArray]" # array 0 ``` I found another lost data type:Fascinating...
```
Even can be a function with params using :do...
```

```
Or with (>{}) it's an empty array...
```

```
And according /console/inspect, it valid syntax like "(>"... e.g./console/inspect input="(" request=completionColumns: TYPE, COMPLETION, STYLE, OFFSET, PREFERENCE, SHOWTYPE        COMPLETION  STYLE        OFFSET  PREFERENCE  SHOWcompletion              none              2  80          nocompletion  (           syntax-meta       2  75          nocompletion  $           syntax-meta       2  75          nocompletion  [           syntax-meta       2  75          nocompletion  {           syntax-meta       2  75          nocompletion  "           syntax-meta       2  75          nocompletion  !           syntax-meta       2  75          nocompletion  -           syntax-meta       2  75          nocompletion  ~           syntax-meta       2  75          nocompletion  >           syntax-meta       2  75          nocompletion              syntax-meta       2  75          nocompletion  <value>     none              2  -1          no


---
```

## Response 10
Author: Fri Jun 23, 2023 1:39 am
``` :put $varWithCodeDataType or :put [ :parse "local var" ] or :put ( $function->1 ) ``` ``` :put [ /system script environment get [ find name="globalFunction" ] value ] ``` ``` /environment print ``` ``` (evl /localname=$var) ``` ``` {(evl [/local{name=$var}])} ``` Also i found that the 2 this variants to print "code":1 - directly printing by "put":
```
2 - print global function parsed code value from /system script environment
```

```
both this variants printing text of parsed code is not completely.For comparison use 3-rd method:
```

```
this printing ALL global variables, but if find the needed text of the code in the printout - will see difference with 1st and 2nd methods:For example, let source:local varthen parse them to code-data-type and printing with all methods.1st and 2nd methods are returned:
```

```
but 3rd method (store code to global variable and print) are returned:
```

```
It seems 3rd method are more preferred to analyse parsed code.Unfortunately, the "/environment print" command are not have any arguments. But it possible redirect console output with :execute to file (or directly in variable with ros 7.8+ by "as-string" argument), and extract needed part.I wrote a usefull function that does all this work automatically


---
```

## Response 11
Author: Mon Jun 26, 2023 12:59 am
``` :global arraytest {"a";"b";"c";{"q";"z"}} :put $arraytest :global pointer (>($arraytest->1)) :put $pointer :put [$pointer] :set ($arraytest->1) "x" :put $arraytest :put $pointer :put [$pointer] :set [$pointer] "W" :set pointer "J" :put $arraytest :put $pointer :put [$pointer] :global pointer (>($arraytest->3)) :put $pointer :put [$pointer] :put ([$pointer]->1) :set ([$pointer]->1) "RR" :put $pointer :put [$pointer] :put $arraytest ``` op..."only pointer" ?Probably is only for point data inside complex array without everytime specify full path...Experimental code ---

## Response 12
Author: Mon Jul 31, 2023 6:55 pm
``` :put [:typeof (>[])] ``` I found another lost data type:
```
Return:opthis data type behaves likecodeAnyway to use this data type to write a script that uses mac-telnet to log into another device by MAC address and execute a command?Something I've been struggling with since there seems to be no way to pass credentials into the mac-telnet command once you launch it.  (and since someone will suggest it, no I cannot SSH into the device, this need exists in situations where there is no IP address defined on a device, it is ONLY accessible via mac-telnet)


---
```

## Response 13
Author: Fri Jan 03, 2025 2:26 pm
@rextended this is a great script!It will probably help-me to solve the problem I'm trying to solve.Thanks!But... (There is always a but, ha-ha.)To be sincere, I do not like very much the idea of subverting the use of a field of a specific resource like was done with layer7 firewall rules.I Understand that it was what the best that could be done whit the resources that were available at that time...But I feel that Layer7 Firewall Rules could be removed sometime, and then this script would be orphaned.Last interaction on this thread wasWed Aug 30, 2023 4:37 amBut 4 months later the Json serialize and deserialized resources were added:What's new in 7.13 (2023-Dec-14 09:24):*) console - added ":serialize" and ":deserialize" commands for converting values to/from JSON;with the first documentation of for those resources being published inScripting - RouterOS - MikroTik Documentation - v. 54 dez. 07, 2023 13:21I tend to believe that Json support will not be removed... Several "new" features have resources based on it like REST-API, MQTT/IOT/GPIO.Considering that, I was wondering to use that Json structure to persist the environment variables.The second part of my ideia was to use /system/script as the persistence method for a json file.Why /system/script?In my opinion saving it on a script is the easiest way to persist a text-based file on an editable way and contained in the backup.rsc and not on another extra file.I will start to think of a way to do that.Please alert me if I'm trying to reinvent the wheel...Any help is welcome. ---

## Response 14
Author: Sat Jan 04, 2025 5:45 pm
I also thought about using json, but......but hopefully by the time it is removed, it will be possible to use serialize and deserialize using the text field of a script...Yep... I guess you are right.I don't like the idea of using layer 7 as a DB, but it is what is available for now.Maybe in the future MikroTik Guys Accept better the idea of dealing with persisten variables.Just adding on what already exists on /system/script/environment/ the possibilities:"D"ynamic entries (what we already know)Persistent entriesTo me, sounds "not-that-hard" for MT-Guys inserting that on RouterOS/CLI/Winbox.Follows the same concept of all the RouterOS. ---

## Response 15
Author: Sun Jan 12, 2025 11:22 am
``` :global persist do={ :local varName $1 :local varValue $2 :local varID [/ip firewall layer7-protocol find name="$varName"] :if ([:typeof $varValue] = "nothing") do={ :if ($varID != "") do={ :set $varValue [/ip firewall layer7-protocol get $varID value-name=regexp] } } else={ :if ($varID = "") do={ /ip firewall layer7-protocol add name="$varName" regexp="$varValue" } else={ /ip firewall layer7-protocol set $varID regexp="$varValue" } } return $varValue } ``` Great job with the variable type handling!Since I don't use many persistent variables, I was never a fan of using scheduled scripts for them. A couple years ago, I wrote a light and easy function that reads/writes to layer7 protocols directly. It only uses strings by default, but can be adapted.
```
Usage examples: (name = variable name, value = variable value)$persist name=Read persistent variable$persist name value=Write persistent variable:global name [$persist name]=Read persistent variable and write it to a global variable:global name [$persist name value]=Write data into a global variable and into a persistent variable at the same timeNotes:The function uses layer7-protocols to store persistent variables.Read/write directly to layer7-protocols without scheduled scripts.All values will be strings.The function always returns a value.


---
```

## Response 16
Author: Tue Jan 28, 2025 1:15 pm
``` :global l7var do={ /ip firewall layer7-protocol :local varName [:tostr $1] :local varNewValue [:tostr $2] :local valuePresent ([:typeof $2] != "nothing") :if ($varName = "") do={ :return [:nothing] } :local varID [find where name=$varName] :if ($delete = "yes") do={ remove $varID ; :return [:nothing] } :if ($valuePresent) do={ :if ([:len $varID] = 0) do={ add name=$varName regexp=$varNewValue :set varID [find where name=$varName] } else={ set $varID regexp=$varNewValue } } :if ([:len $varID] != 0) do={ :return [get $varID regexp] } :return [:nothing] } ``` The function still haveproblemsafter 6 years...Refitted to avoid errors.Also added the ability to delete the "variable" ifdelete=yesis specified as parameter.reworked code ---

## Response 17
Author: Tue Jan 28, 2025 5:15 pm
``` { # an array with most types, including a JSON "float" :local arr { "num"=0; "str"="mystr"; "emptystr"=""; "ip4"=1.1; "ip6"=1::1; "prefix4"=1.0.0.1/31; "prefix6"=1::1/69; "float"="1.1"; "time"=1s; "now"=[:timestamp]; "null"=[:nothing]; "list"=(1, 2,"three"); "listlist"={(1, 2, 3);("a","b","c")} "dict"={"a"=1;"b"="z"}; "dictlist"={{"m"="M"};{"z"="Z"}}; "dictdict"={"b"={"one"=1;"two"=2};"w"={"1"="one";"2"="two"}}; "optype"=(>[:put "echo"]); "bignum"=[:tonsec [:timestamp]]; "bigneg"=(0-[:tonsec [:timestamp]]); } # helpers for test :local prettyprint do={:put [:serialize to=json options=json.pretty $1]} :local addtypes do={:local rv $1; :foreach n, a in=$1 do={ :set ($rv->"$n-type") [:typeof $a] }; :return $rv } :put "\r\narray BEFORE serialization" $prettyprint [$addtypes $arr] :put "\r\nconvert to JSON" :local json [:serialize to=json $arr] :put "\r\nconvert to base64 for storage as RouterOS string" :local base64out [:convert to=base64 $json] $prettyprint $base64out :put "\r\nsave to base64 JSON as unused L7 FW rule" :local storename "example-base64-json-to-save-vars" :local storeid [/ip/firewall/layer7-protocol/find name=$storename] :if ([:len $storeid]=1) do={ /ip/firewall/layer7-protocol set $storeid regexp=$base64out } else={ /ip/firewall/layer7-protocol add name=$storename regexp=$base64out } :put "\r\nPRETEND you reboot and come back...so wait 3 seconds" :delay 3s :put "\r\nsave to base64 JSON as unused L7 FW rule" :local base64in [/ip/firewall/layer7-protocol get [find name=$storename] regexp] :put "\r\nif base64, restore it to JSON" :local newjson [:convert from=base64 $base64in] :put "\r\nfinally get the array back, with types perserved by :deserialize JSON" :local arr2 [:deserialize from=json $newjson] :put "\r\narray AFTER deserialization" $prettyprint [$addtypes $arr2] :put "\r\nBONUS: simulate using RESTORED array variables using 'activate-in-context' and 'op' types" ((>[:put "now: $now listlen: $[:len $list] bignum: $bignum prefix6: $prefix6"]) <%% $arr2) :put "... even though its array, you can use them as normal variables without the -> if you use the <%% to unwrap them" } ``` ``` (>[:put [:typeof [:deserialize from=json [:serialize to=json $1]]]]) <%% "1.1.1.1/0" # ip-prefix ``` I also thought about using json, but...[...]So, in conclusion, layer7 is certainly not going away anytime soon, but hopefully by the time it is removed, it will be possible to use serialize and deserialize using the text field of a script...A possible solution is to convert everything into a base64 array[...]FWIW, I adapted a test script for serialize/deserialize, to test using JSON to base64 to L7 FW regex storage (and back). I wasn't trying to replace anything here, more just trying the above approach to see if it even works, since I had a complex array already. And, critically, this will only work in 7.16+ (or maybe even needs 7.17).You can see below how JSON serialization largely preserves types. The only oddity is "0.0" become 0.000000 in JSON, but plus side is "1.1" becomes 1.100000 in JSON (a float). And there is an option in :serialize to prevent that if desired.
```
array BEFORE serialization{"bigneg": -1738076593889845466,"bigneg-type": "num","bignum": 1738076593889955906,"bignum-type": "num","dict": {"a": 1,"b": "z"},"dict-type": "array","dictdict": {"b": {"one": 1,"two": 2},"w": {"1": "one","2": "two"}},"dictdict-type": "array","dictlist": [{"m": "M"},{"z": "Z"}],"dictlist-type": "array","emptystr": "","emptystr-type": "str","float": 1.100000,"float-type": "str","ip4": "1.0.0.1","ip4-type": "ip","ip6": "1::1","ip6-type": "ip6","list": [1,2,"three"],"list-type": "array","listlist": [[1,2,3],["a","b","c"]],"listlist-type": "array","now": "2025-01-28 15:03:13","now-type": "time","null": null,"null-type": "nil","num": 0,"num-type": "num","optype": "(op)","optype-type": "op","prefix4": "1.0.0.1/31","prefix4-type": "ip-prefix","prefix6": "1::/69","prefix6-type": "ip6-prefix","str": "mystr","str-type": "str","time": "1970-01-01 00:00:01","time-type": "time"}convert to JSONconvert to base64 for storage as RouterOS string"eyJiaWduZWciOi0xNzM4MDc2NTkzODg5ODQ1NDY2LCJiaWdudW0iOjE3MzgwNzY1OTM4ODk5NTU5MDYsImRpY3QiOnsiYSI6MSwiYiI6InoifSwiZGljdGRpY3QiOnsiYiI6eyJvbmUiOjEsInR3byI6Mn0sInciOnsiMSI6Im9uZSIsIjIiOiJ0d28ifX0sImRpY3RsaXN0IjpbeyJtIjoiTSJ9LHsieiI6IloifV0sImVtcHR5c3RyIjoiIiwiZmxvYXQiOjEuMTAwMDAwLCJpcDQiOiIxLjAuMC4xIiwiaXA2IjoiMTo6MSIsImxpc3QiOlsxLDIsInRocmVlIl0sImxpc3RsaXN0IjpbWzEsMiwzXSxbImEiLCJiIiwiYyJdXSwibm93IjoiMjAyNS0wMS0yOCAxNTowMzoxMyIsIm51bGwiOm51bGwsIm51bSI6MCwib3B0eXBlIjoiKG9wKSIsInByZWZpeDQiOiIxLjAuMC4xLzMxIiwicHJlZml4NiI6IjE6Oi82OSIsInN0ciI6Im15c3RyIiwidGltZSI6IjE5NzAtMDEtMDEgMDA6MDA6MDEifQ=="save to base64 JSON as unused L7 FW rulePRETEND you reboot and come back...so wait 5 secondssave to base64 JSON as unused L7 FW ruleif base64, restore it to JSONfinally get the array back, with types perserved by :deserialize JSONarray AFTER deserialization{"bigneg": -1738076593889845466,"bigneg-type": "num","bignum": 1738076593889955906,"bignum-type": "num","dict": {"a": 1,"b": "z"},"dict-type": "array","dictdict": {"b": {"one": 1,"two": 2},"w": {"1": "one","2": "two"}},"dictdict-type": "array","dictlist": [{"m": "M"},{"z": "Z"}],"dictlist-type": "array","emptystr": "","emptystr-type": "str","float": 1.100000,"float-type": "str","ip4": "1.0.0.1","ip4-type": "ip","ip6": "1::1","ip6-type": "ip6","list": [1,2,"three"],"list-type": "array","listlist": [[1,2,3],["a","b","c"]],"listlist-type": "array","now": "2025-01-28 15:03:13","now-type": "time","null": null,"null-type": "nil","num": 0,"num-type": "num","optype": "(op)","optype-type": "str","prefix4": "1.0.0.1/31","prefix4-type": "ip-prefix","prefix6": "1::/69","prefix6-type": "ip6-prefix","str": "mystr","str-type": "str","time": "1970-01-01 00:00:01","time-type": "time"}BONUS: simulate using array variables in function using the 'activate-in-context'with 'op' typenow: 2873w5d15:03:13  listlen: 3 bignum: 1738076593889955906  prefix6: 1::/69... even though its array, you can use them as normal variables without the -> ifyou use the <%% to unwrap themAlso, the combo of [:deserialize [:serialize]] works on any type -so input does NOT have to be array– you use that to do something like get an ip-prefix from a string, without an array:
```

```
---
```

## Response 18
Author: Tue Jan 28, 2025 7:49 pm
``` { :global globalVars [:toarray ""] :put $globalVars :set ($globalVars->"testArray") [:toarray ""] :set ($globalVars->"testArray"->"value") [:toarray "a, b"] :set ($globalVars->"testArray"->"type") [:typeof ($globalVars->"testArray"->"value")] :set ($globalVars->"testBool") [:toarray ""] :set ($globalVars->"testBool"->"value") true :set ($globalVars->"testBool"->"type") [:typeof ($globalVars->"testBool"->"value")] :set ($globalVars->"testCode") [:toarray ""] :set ($globalVars->"testCode"->"value") [:parse ";"] :set ($globalVars->"testCode"->"type") [:typeof ($globalVars->"testCode"->"value")] :set ($globalVars->"testID") [:toarray ""] :set ($globalVars->"testID"->"value") [:toid *BEEF6] :set ($globalVars->"testID"->"type") [:typeof ($globalVars->"testID"->"value")] :set ($globalVars->"testIP4") [:toarray ""] :set ($globalVars->"testIP4"->"value") 127.0.0.1 :set ($globalVars->"testIP4"->"type") [:typeof ($globalVars->"testIP4"->"value")] :set ($globalVars->"testIP4px") [:toarray ""] :set ($globalVars->"testIP4px"->"value") 192.168.0.0/24 :set ($globalVars->"testIP4px"->"type") [:typeof ($globalVars->"testIP4px"->"value")] :set ($globalVars->"testIP6") [:toarray ""] :set ($globalVars->"testIP6"->"value") 127:0:0::1 :set ($globalVars->"testIP6"->"type") [:typeof ($globalVars->"testIP6"->"value")] :set ($globalVars->"testIP6px") [:toarray ""] :set ($globalVars->"testIP6px"->"value") 192:168:0::0/64 :set ($globalVars->"testIP6px"->"type") [:typeof ($globalVars->"testIP6px"->"value")] :global lookupGen do={:return $0} :set ($globalVars->"testLook") [:toarray ""] :set ($globalVars->"testLook"->"value") [$lookupGen] :set ($globalVars->"testLook"->"type") [:typeof ($globalVars->"testLook"->"value")] :set ($globalVars->"testNil") [:toarray ""] :set ($globalVars->"testNil"->"value") [] :set ($globalVars->"testNil"->"type") [:typeof ($globalVars->"testNil"->"value")] :set ($globalVars->"testNth") [:toarray ""] :set ($globalVars->"testNth"->"value") ; # undefined on purpose for nothing :set ($globalVars->"testNth"->"type") [:typeof ($globalVars->"testNth"->"value")] :set ($globalVars->"testNum") [:toarray ""] :set ($globalVars->"testNum"->"value") -256 :set ($globalVars->"testNum"->"type") [:typeof ($globalVars->"testNum"->"value")] :set ($globalVars->"testOP") [:toarray ""] :set ($globalVars->"testOP"->"value") (>[]) :set ($globalVars->"testOP"->"type") [:typeof ($globalVars->"testOP"->"value")] :set ($globalVars->"testStr") [:toarray ""] :set ($globalVars->"testStr"->"value") [:convert to=base64 "1.1"] :set ($globalVars->"testStr"->"base64") true :set ($globalVars->"testStr"->"type") [:typeof ($globalVars->"testStr"->"value")] :set ($globalVars->"testTime") [:toarray ""] :set ($globalVars->"testTime"->"value") 1w1d1h1m1s :set ($globalVars->"testTime"->"type") [:typeof ($globalVars->"testTime"->"value")] :foreach name, content in=$globalVars do={ :if (($content->"type") = "array") do={ :put ">$name< = >$($content->"type")< >$[:tostr ($content->"value")]< " } else={ :if (($content->"base64") = true) do={ :put ">$name< = >$($content->"type")< >$[:convert from=base64 ($content->"value")]< " } else={ :put ">$name< = >$($content->"type")< >$($content->"value")< " } } } :local json [:serialize to=json options=json.pretty $globalVars] # debug # :put $json :put "\r\nAfter array -> json -> array conversion:\r\n" :global newArr [:deserialize from=json options=json.no-string-conversion $json] :foreach name, content in=$newArr do={ :if (($content->"type") = "array") do={ :put ">$name< = >$($content->"type")< >$[:tostr ($content->"value")]< IMPORTED TYPE: >$[:typeof ($content->"value")]<" } else={ :if (($content->"base64") = true) do={ :put ">$name< = >$($content->"type")< >$[:convert from=base64 ($content->"value")]< IMPORTED TYPE: >$[:typeof ($content->"value")]<" } else={ :put ">$name< = >$($content->"type")< >$($content->"value")< IMPORTED TYPE: >$[:typeof ($content->"value")]<" } } } :put "\r\nNOTES\r\ncode, function, lookup and op are not exportable. Function is also reported as array." :put "Strings are exported and imported on base64 for prevent 7.16.2 and less errors with implicit conversions to json," :put "on importing strings already exist options=json.no-string-conversion that prevents implicit conversions from json" :put "MISSING: apireq, backreference, cmd, exclamation, iterator\r\n" } ``` Some tests on vars that do not have sub-arrays...test variable types code