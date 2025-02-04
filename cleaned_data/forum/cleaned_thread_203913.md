# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 203913

# Discussion

## Initial Question
Author: [SOLVED]Sat Feb 03, 2024 8:43 am
``` /system logging action add disk-file-count=10 disk-file-name=disk1/dudeLog/dudeLogNew disk-lines-per-file=4000 name=dudeLog target=\ disk # for testing (later) add name=dudeSyslog remote=127.0.0.1 target=remote /system logging add action=dudeLog topics=dude add action=dudeLog topics=script # testing # Should get 2 entries, one sent to memory, second to dudeLog. /log info message="testing" ``` ``` /log info message="testing" ``` What I have works, but it was setup quite a while ago, so there maybe something I have missed here.
```
Now In dude:In Notifications sectionAdd a NotificationCall it "log to syslog"It is of type loglog prefix=syslogSchedule should be active all the timeAdvanced, sorry not sure, doesn't really seem relevant.In Settings (Server Configuration) /Syslog TabEnabledPort 514Add an entryAction=accept Notification="log to syslog"# testingIn winbox, system loggingchange rule with script topic (created above) to action=dudeSyslogthen
```

```
With luck you should get 2 messages in log again,but now one message should be dude, event, and have syslog: prefix in front of it.Change script rule action back to dudeLog (or disable it)Edit: Also need to firewall rule to allow udp port 514 input.
```