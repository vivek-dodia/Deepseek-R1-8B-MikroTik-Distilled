# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 214284

# Discussion

## Initial Question
Author: [SOLVED]Wed Jan 29, 2025 2:24 am
``` /system logging disable[find topics=fetch]/system logging reset4/system logging disable[find topics=raw]/system logging disable[find topics=write] ``` ``` /system loggingprintFlags:*-DEFAULTColumns:TOPICS, ACTION# TOPICS ACTION0*info memory1*error memory2*warning memory3*critical echo4fetch memory/system logging actionprintFlags:*-default0*name="memory"target=memory memory-lines=1000memory-stop-on-full=no1*name="disk"target=disk disk-file-name="log"disk-lines-per-file=1000disk-file-count=2disk-stop-on-full=no2*name="echo"target=echo remember=yes3*name="remote"target=remote remote=0.0.0.0remote-port=514src-address=0.0.0.0bsd-syslog=nosyslog-time-format=bsd-syslog syslog-facility=daemon syslog-severity=auto ``` While debugging a problem with/tool/fetchI entered the command/system logging add topics=fetch. Now lots of unwanted messages are logged (attached).How can I reset logging to default settings? I tried:
```
without success.  Here are the current settings:
```

```
---
```

## Response 1
Author: Wed Jan 29, 2025 4:19 am
``` /system loggingprint/system loggingremove4 ``` 
```
---
```

## Response 2
Author: Wed Jan 29, 2025 9:03 pm
``` /system loggingprint/system loggingremove4 ``` 
```
Worked!  Many thanks!
```