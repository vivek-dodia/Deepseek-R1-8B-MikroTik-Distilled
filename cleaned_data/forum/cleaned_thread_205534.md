# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 205534

# Discussion

## Initial Question
Author: Sat Mar 09, 2024 5:02 pm
``` /system script add dont-require-permissions=no name=test policy=read, write, policy, test source=":global test; :put \$test;" ``` ``` snmpwalk -v3 -l authPriv -u mkuser -a SHA -A xxxxxxxx -x DES -X xxxxxxxxxxx 10.20.30.40 1.3.6.1.4.1.14988.1.1.8.1.1.2 Result: iso.3.6.1.4.1.14988.1.1.8.1.1.2.11 = STRING: "test" ``` ``` snmpwalk -v3 -l authPriv -u mkuser -a SHA -A xxxxxxxx -x DES -X xxxxxxxxxxx 10.20.30.40 1.3.6.1.4.1.14988.1.1.18.1.1.2.11 Result: iso.3.6.1.4.1.14988.1.1.18.1.1.2.11 = STRING: " " ``` ``` snmpget -v3 -l authPriv -u mkuser -a SHA -A xxxxxxxx -x DES -X xxxxxxxxxxx 10.20.30.40 1.3.6.1.4.1.14988.1.1.18.1.1.2.11 Result: iso.3.6.1.4.1.14988.1.1.18.1.1.2.11 = STRING: " " ``` RouterOS ver 7.14Global environment declared before:test=123Script code:
```
Listing name from SNMP:
```

```
Trying to get value from snmpwalk:
```

```
Trying to get value from snmpget:
```

```
SNMP Scripts can't read global var?


---
```

## Response 1
Author: Sat Mar 09, 2024 6:54 pm
``` test=123 ``` ``` test="test" ``` ``` test=65 ``` 
```
Should that just declare some int, and when you reading it with snmp, you just get int like char value of 123.I think you should try to assign a string instead.
```

```
I am not any expert of RouterOS scripts, but like another programming lang and script lang.You can try to test my hypothesis with:
```

```
You should get "A"


---
```

## Response 2
Author: [SOLVED]Sat Mar 09, 2024 8:07 pm
I think problem is that SNMP service is executing script with different user (some internal system) than ROS login user which created global variable. Users cannot read global variables created by another. Same issue is for eg. with netwatch tool and getting/setting global variables that are used with other scripts.Try to set global variable intestscript before:putit should work, but that global var. value will not be readable by scripts which are not executed by SNMP, it will not even be listed with/system/script/environment/printfrom CLI or Winbox.You can try to set value to file and read from it instead as workaround.@patrikg - lol ---

## Response 3
Author: Sun Mar 10, 2024 10:14 pm
``` iso.3.6.1.4.1.14988.1.1.18.1.1.2.12 = STRING: "123" ``` @optio I think you are right.Tryed this and worked::global test;:set $test 123;:put $test;
```
---
```

## Response 4
Author: Sun Mar 10, 2024 11:17 pm
``` iso.3.6.1.4.1.14988.1.1.18.1.1.2.12 = "" ``` ``` iso.3.6.1.4.1.14988.1.1.18.1.1.2.12 = STRING: " SEQ HOST SIZE TTL TIME STATUS 0 8.8.8.8 56 58 36ms775us 1 8.8.8.8 56 58 34ms379us 2 8.8.8.8 56 58 34ms423us sent=3 received=3 packet-loss=0% min-rtt=34ms379us avg-rtt=35ms192us max-rtt=36ms775us " ``` This is very weird:Don't Work:ping address=8.8.8.8 interval=200ms count=3 as-value
```
Works:ping address=8.8.8.8 interval=200ms count=3
```

```
Worked, need to write :put:put [ping address=8.8.8.8 interval=200ms count=3 as-value]


---
```

## Response 5
Author: Sun Mar 10, 2024 11:36 pm
``` /system script add dont-require-permissions=no name=test policy=read, write, policy, test source=":global test; :put \$test;" ``` RouterOS ver 7.14[...]
```
[/code][...]SNMP Scripts can't read global var?It's permissions I think.  Perhaps dont-require-permissions=yes would allow it to be read via SNMP?But @optio is right: passing around global variable is problematic.


---
```

## Response 6
Author: Sun Mar 10, 2024 11:58 pm
``` :global savestate do={ :do { /file set "state$[:jobname].json" contents=[:serialize to=json $1] } on-error={ /file add name="state$[:jobname].json" contents=[:serialize to=json $1] } } :global getstate do={ :return [:deserialize from=json [/file get "state$[:jobname].json" contents]] } # examples: # an array to persist :global myvars {a="123";b="something"} # call \$savestate which write the RouterOS array as JSON to a file name state[:jobname].json $savestate $myvars :put [$getstate] # the state is override if saved state is called again. $savestate "mydata" :put [$getstate] # note: script depends on [:jobname] so the persisted variables should be scoped to each /system/script plus CLI has one state. ``` In this case personally I will rather use file in root path which is using tmpfs (assuming ROS is running on device with flash drive) than writing value into some config if presistance is not needed since such file will act as global variable, preserved only in RAM, no flash writes upon setting value and lost after reboot.Since we're talking about 7.14, there is the JSON serialization – which make reading/writing RouterOS vars to disk easy. Using a tmpfs be a good idea if there is a lot of writes to the data. But if it's mainly read, flash should be fine.Perhaps some script example help explain how to persist a variable. I wrapped the logic in two function $savestate and $getstate, but you can cut-and-paste/adapted as needed (including using a ramdisk via "/disk add type=tmpfs ...")
```
---
```

## Response 7
Author: Mon Mar 11, 2024 12:12 am
This is very weird:[...]Worked, need to write :put:put [ping address=8.8.8.8 interval=200ms count=3 as-value]SNMP is capturing stdout, as-value surpasses that. And /system/script don't "return" anything, like a function or [/cmd/get value] would – so :put is all ya got to SNMP. ---

## Response 8
Author: Mon Mar 11, 2024 12:55 am
``` /system script add dont-require-permissions=no name="Ping 8.8.8.8" policy=read source=":put [ping address=8.8.8.8 interval=200ms count=5]" ``` Well, work is done. This use Zabbix to get a value from ping and loss inside Mikrotik.Template for Zabbix 6.0OBS: Only run with SNMP read/write access. Please use SNMP version 3!You need to create the script into Mikrotik with a start name: PingExample: Ping - something else.Into Mikrotik, create your script.
```
If you liked, rate this!File is on topic:viewtopic.php?p=1062310


---
```

## Response 9
Author: Mon May 13, 2024 6:36 am
``` :global LinkAtivo :global PercentLossPrincipal :global MPLoss :global PercentLossBackup :global MBLoss system note set note="Link: $LinkAtivo Perda Prin: $PercentLossPrincipal Media Prin: $MPLoss Perda Back: $PercentLossBackup Media Back: $MBLoss" ``` ``` root@Syslog:~# snmpget -v1 -cpublic 10.100.203.1 1.3.6.1.4.1.14988.1.1.7.5.0 iso.3.6.1.4.1.14988.1.1.7.5.0 = STRING: "Link: PRINCIPAL Perda Prin: 0 Media Prin: 0 Perda Back: 0 Media Back: 0" ``` I spent a few years with this dilemma of how to query via SNMP some global variables generated by custom scripts with indicators that I would like to display in The Dude and in other monitoring systems like Zabbix.In fact, it is possible to do this using remote execution of scripts via snmp and returning their values, but this did not really please me, as the OID for the same script on different routers could be different, as the scripts are executed by their indexes and not by their names.This makes configuration in the monitoring system very difficult, but worse than that, a wrong configuration could simply cause another script to be executed in place of the one that only had the function of returning information, which is really very bad.Using a fake disabled bridge to look for its name that could be changed by the script to the content of the variable was one of the ways I saw other members suggested.This approach solves the problem of executing an inappropriate script, but does not solve the issue of the OID being different between different routers.The solution I found that solved my problem was to use the "system note" function, which is a space where you can create a complete text with several lines and you can consult it by OID ("1.3.6.1.4.1. 14988.1.1.7.5.0").So just create a script that brings together all the variables you want to use and writes them to the "system note", putting this script to run through the scheduler from time to time as needed.
```
It is possible to consult it with the read-only public community, the OID will always be the same regardless of the router, we do not run the risk of executing a script by mistake and it is possible to store a lot of information in this field.
```

```
On the monitoring side, simply create functions to filter with regular expressions and extract only the variable you want for that specific query.And "Voilá" we have it resolved.


---
```

## Response 10
Author: Mon May 13, 2024 7:13 am
``` array_element(oid_column("iso...mtxrScriptIndex"), array_find(oid_column("iso... mtxrScriptName"), "my_script_name")) ``` Yeah there is a lot of stuff you just cannot read from SNMP, so /system/note may not be a bad option. But just note since it updates config, it does increase flash writes since an update is stored in config. In terms of SNMP+scripts, it's a shame therestored/persistent variables, for a lot of reasons... but one be to expose some user variables to SNMP with its own OID exposed.In fact, it is possible to do this using remote execution of scripts via snmp and returning their values, but this did not really please me, as the OID for the same script on different routers could be different, as the scripts are executed by their indexes and not by their names.This makes configuration in the monitoring system very difficult, but worse than that, a wrong configuration could simply cause another script to be executed in place of the one that only had the function of returning information, which is really very bad.[...]This approach solves the problem of executing an inappropriate script, but does not solve the issue of the OID being different between different routers.FWIW, the OID is determined by the order added to config. So if use some netinstall/flashfig/defconf process to deploy routers, the initial can add a script (or placeholder one) with what you want to expose. And as long as it's not removed, the OID remains constant.Also, if need is only The Dude, you have more options since you can use ros_command() to run a RouterOS command directly. Or find the script's by name, using Dude's array functions
```
Neither approach helps with Zabbix/et'al...But you should be able to use the Zabbix HTTP agent against Mikrotik's REST API, and the use $ JSONPath syntax in Zabbix to read the specific data from JSON returned from RouterOS REST call.  See:https://www.zabbix.com/documentation/cu ... types/httphttps://help.mikrotik.com/docs/display/ROS/REST+API
```