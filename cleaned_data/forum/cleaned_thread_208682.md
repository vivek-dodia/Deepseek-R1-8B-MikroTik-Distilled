# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 208682

# Discussion

## Initial Question
Author: Sun Jun 23, 2024 8:21 pm
hello everybody!well... v7.15 have this changelog:*) console - added log for script execution failures;and I have this function on dude, that keep showing logs errors on rb that havent the temperature data.if(ros_command(":put [/system health get temperature]")>0,"have","havent")The question is: There is any workaround to "test" without print error?obs: the function is placed on setting/apperance of map, 20rb) ---

## Response 1
Author: [SOLVED]Sun Jun 23, 2024 10:50 pm
``` :do { :put [/system/health/get [find name=temperature] value] } on-error={:put "0"} ``` /system/health is kinda weird in how it works, since the values like temp are just plain list items... So the simple "get temperature" isn't going to work....You can just use a :do {} on-error={} to prevent errors (like temperature not being found):
```
The key part to understand is "/system/health get temperature" does not work, as all the health values are not indexed by name=.... so the specific entry must be found using [find] to get the .id for temperature item (or a [print as-value] anditerating over thelist-typearrayto locate the temperature item could also work, but that more code if it's just temp)


---
```

## Response 2
Author: Mon Jun 24, 2024 3:30 pm
``` concatenate( if(ros_command(":do { :put [/system health get [find name=board-temperature1] value] } on-error={:put \"0\"}")>0, concatenate("RB Temp: ",round(ros_command(":do { :put [/system health get [find name=board-temperature1] value] } on-error={:put \"\"}")),"°C "), "" ), if(ros_command(":do { :put [/system health get value-name=temperature] } on-error={:put \"0\"}")>0, concatenate("RB Temp: ",round(ros_command(":do { :put [/system health get value-name=temperature] } on-error={:put \"0\"}")),"°C "), "" ) ) ``` ``` :do { :put [/system/health/get [find name=temperature] value] } on-error={:put "0"} ``` very thanks!final result:
```
I accept adjustements, for now, working perfectly!/system/health is kinda weird in how it works, since the values like temp are just plain list items... So the simple "get temperature" isn't going to work....You can just use a :do {} on-error={} to prevent errors (like temperature not being found):
```

```
The key part to understand is "/system/health get temperature" does not work, as all the health values are not indexed by name=.... so the specific entry must be found using [find] to get the .id for temperature item (or a [print as-value] anditerating over thelist-typearrayto locate the temperature item could also work, but that more code if it's just temp)
```