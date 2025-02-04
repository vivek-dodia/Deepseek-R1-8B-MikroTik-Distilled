# Thread Information
Title: Thread-213235
Section: RouterOS
Thread ID: 213235

# Discussion

## Initial Question
I try to repair mikrotik via netinstall, but i'am seeing this error:sudo ./netinstall-cli -v -r -a 192.168.88.3 routeros-smips-6.49.13.npkVersion: 7.16.2(2024-11-26 13:15:20)Will reset to default configUsing interface enp0s20u2Using interface enp0s20u2Waiting for Link-UP on enp0s20u2Waiting for RouterBOARD...Can't Netinstall 6C:3B:6B:04:F4:93, please supply the mips system package ---

## Response 1
This is VERY odd indeed ?!And did you try simply using the mips package as it indicates ?Because what strikes me as equally odd, is that same QCA9533 CPU is used in mAP Lite and cAP Lite and those ARE mips devices. Not SMIPS. ---

## Response 2
This is VERY odd indeed ?!And did you try simply using the mips package as it indicates ?Because what strikes me as equally odd, is that same QCA9533 CPU is used in mAP Lite and cAP Lite and those ARE mips devices. Not SMIPS.Sorry, do you mean MIPSBE? But in specification an architectury of hap lite is SMIPS. Also i have two same devices. And on another one i uploaded SMIPS and all works fine. ---

## Response 3
/system resource printon a hap lite tc I have gives:cpu: MIPS 24Kc v7.4architecture name: smips ---