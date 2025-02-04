# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 172385

# Discussion

## Initial Question
Author: Sun Feb 07, 2021 10:17 pm
``` /system package update check-for-updates; /system package update install; ``` ``` /system routerboard print; /system routerboard upgrade; /system reboot; ``` Is there a 1 liner to upgrade RouterOS and firmware at the same time?At the moment I have to update RouterOS:
```
And then firmware
```

```
So need to reboot 2 times .... is it possible to do it in one command with one reboot?


---
```

## Response 1
Author: Mon Feb 08, 2021 12:44 am
``` /system routerboard settings set auto-upgrade=yes ``` ``` /system routerboard upgrade ``` It is not possible to upgrade routerboot before device reboots to upgraded ROS version. The only corner that can be cut is to set
```
which saves administrator from executing
```

```
after ROS upgrade. Another reboot is still necessary.


---
```

## Response 2
Author: Mon Feb 08, 2021 12:57 pm
``` /system routerboard settings set auto-upgrade=yes ``` ``` /system routerboard upgrade ``` It is not possible to upgrade routerboot before device reboots to upgraded ROS version. The only corner that can be cut is to set
```
which saves administrator from executing
```

```
after ROS upgrade. Another reboot is still necessary.So if I understand that correctly, when I set routerboard to Auto-Upgrade it will reboot 2x as well when it upgrades ROS/firmware?
```