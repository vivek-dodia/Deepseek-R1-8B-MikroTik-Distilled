# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213148

# Discussion

## Initial Question
Author: Mon Dec 09, 2024 11:25 am
``` ./netinstall-cli -r -a 192.168.88.1 routeros-7.16.1-arm.npk all_packages-arm-7.16.1/wifi-qcom-ac-7.16.1-arm.npk ``` ``` [admin@MikroTik]/system/script>addname=test[admin@MikroTik]/system/script>edit0comment dont-require-permissions name owner policy sourcevalue-name ``` After using netinstall to reset and update the firmware of a mikrotik hap ac2, I wish to create a script to test the Mikrotik using bandwith-test.However after the reset with netinstall, I don't seem to be able to use script.NetInstall :
```
Trying to create a script :
```

```
Is there a package to add to the install by netinstall ? If yes witch is it ? Do I do something wrong ?


---
```

## Response 1
Author: [SOLVED]Mon Dec 09, 2024 12:21 pm
``` edit test source ``` You press <TAB> after edit 0.So?What mean edit 0? what is 0?