# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 180235

# Discussion

## Initial Question
Author: Wed Nov 10, 2021 4:06 pm
``` :forifrom=([:len $ipaddress]-1)to=0do={:if([:pick $ipaddress $i]="/")do={:put[:pick $ipaddress0$i]}} ``` ``` :put[:pick $ipaddress0[:find $ipaddress"/"]] ``` Hi!I'm using RB5009 and ROS 7.1rc6Works fine in terminal but won't work in a script. Can someone help me or is it a bug?Alt1
```
Alt 2
```

```
---
```

## Response 1
Author: [SOLVED]Fri Nov 12, 2021 9:22 am
``` :globalipaddress10.1.101.1/24;:setipaddress[:pick $ipaddress0[:find $ipaddress"/"]] ``` I had to change it to:
```
to make it work


---
```

## Response 2
Author: Fri Nov 12, 2021 2:35 pm
``` :put[:pick $ipaddress0[:find $ipaddress"/"]] ``` ``` :setipaddress[:pick $ipaddress0[:find $ipaddress"/"]] ``` No, that didn't work for me, I tried the wiki example.This line is being ignored:
```
The solution was to set the variable again
```

```
---
```

## Response 3
Author: Fri Nov 12, 2021 3:51 pm
``` :globalipaddress10.1.101.1/24:set$ipaddress[:pick $ipaddress0[:find $ipaddress"/"]] ``` Is like you do not know scripting,":put" simply write on terminal some text, if you must "put" the result inside a variable, is obvious than you must use set.And also on CORRECT way (the $ before ipaddress after set command):
```
---
```

## Response 4
Author: Sat Aug 24, 2024 5:50 pm
Can you help me, what am I doing wrong here?/tool netwatch set [find comment="isp4"] src-address=(([/ip dhcp-client get [find interface="ether1" %ipaddress [:pick $ipaddress 0 [find $ipaddress "/"I want to get the ip address only from the dhcp client but I can't do itthank you very much