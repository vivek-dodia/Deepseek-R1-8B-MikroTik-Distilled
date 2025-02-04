# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210297

# Discussion

## Initial Question
Author: Tue Aug 20, 2024 4:03 pm
``` UP /ip route set [find comment=ISP-1] disabled=no /ip firewall connection {remove [find]} :log warning "ISP-1 UP" /tool fetch url="https://api.telegram.org .... Down /ip route set [find comment=ISP-1] disabled=yes /ip firewall connection {remove [find]} :log error "ISP1-DOWN!" /tool fetch url="https://api.telegram.org .... ``` This problem is observed after updating to 7.15.3.What can be the problem, this script is used in several projects and had no problems except for one case. Here the main channel ISP-1 wifi bridge, backup ISP-2 starlink. The script in netwatch switching can once work completely the second time causes an error message in the log.The script disables/enables the default route through ISP-1, then clears all connections, and displays a message in the log and sends a message to telegram. According to the logs it turns out that the error is caused by line 2 connection clearing. Help me where to look
```
---
```

## Response 1
Author: Tue Aug 20, 2024 7:01 pm
``` :onerror err in={ <script_code> } do={:return [:log error "Up/Down script error: $err"]} ``` Try to catch error message from scripts to see what is actual error:
```
@rextended in first screenshotfetchlogs successful execution which is strange if is not permitted, also if is fetch error, it will be logged "ISP-1 UP" or "ISP1-DOWN!"  before script error message because:log warning  "ISP-1 UP"or:log error  "ISP1-DOWN!"commands are executed beforefetch.In myNetwatchevent script there is also IP update script on DDNS provider withfetchand there is no issue, butfetchcommand is not directly executed in event script, event script runs other script with/system/script run ....


---
```

## Response 2
Author: Fri Aug 30, 2024 7:51 pm
``` /ip route set [find comment=ISP-1] disabled=yes /ip firewall connection {remove [find]} :log error "ISP1-DOWN!" ``` ``` /ip route set [find comment=ISP-1] disabled=yes # /ip firewall connection {remove [find]} :log error "ISP1-DOWN!" ``` Anyway, I haven't unequivocally found the problem yet.what features I have found1.The log outputs messages in a different order than the order of lines in the script.2. I suspect that the problem lies in copy-paste through a remote session. Because I had to copy the line of sending to telegram again and the error disappeared, visually the lines are exactly the same.3. I inserted an empty line with a comment and the error disappearedthere is an error in the log
```
no error in the log
```

```
---
```

## Response 3
Author: Wed Sep 04, 2024 1:02 am
``` /system/script add name=error-script source=":log info \"test\"\81" ``` It could happen that invisible characters are in script and when is edited in Winbox it looks fine, like this for eg.:
```
When backspace is pressed at EOL and saved, it will work without error.But you are right it will always fail until is edited.Then it could be that in some cases/ip firewall connection {remove [find]}produces error by some reason, you can find which error is produced if you put script in:onerrorblock as I written in#3, it will log actual error produced by command in script and you can post it here for examination.


---
```

## Response 4
Author: [SOLVED]Mon Sep 09, 2024 2:41 pm
/ip firewall connection{remove [find]}First of all it is already wrong to write it this way.I've already explained exactly on 2021 why it's bu11sh1t to write something like that in other posts.viewtopic.php?p=853800#p853800