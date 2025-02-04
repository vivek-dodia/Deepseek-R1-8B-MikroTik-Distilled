# Thread Information
Title: Thread-1122883
Section: RouterOS
Thread ID: 1122883

# Discussion

## Initial Question
Hi Guys, I have new router RB952Ui-5ac2nD with default config and current wirmware 6.49.17.Im trying to connect some USB device but I still dont see on port list this devices.Im trying connecte some USB flash or some LTE/3G modem and same result.USB flash its model: ‎DTMAXA/256GBUSB modems I tryied to use:HUAWEI E3372h-153HUAWEI E3372h-320HUAWEI E352S-5ALCATEL IK41VE1D-LINK DWM-222[admin@MikroTik] > /port print detailFlags: I - inactivePlease can you help me why I cant see and configure any USB device on this router?Thank you ---

## Response 1
You can verify that USB port works and that USB device attached does present to RouterOS kernel by running command
```
/system/resource/usb/printIt should shown your attached device along with a few devices with namexHCI Host Controller.Yet another thing is to get USB device working ... and with ROS it's not as straight forward as with most desktop computer. Reason is that ROS includes only a very limited number of peripherials' drivers so generally you can't expect that a random USB device will just work. Storage USB sticks normally work, modems not so much.

---
```

## Response 2
Compare with the list here:https://help.mikrotik.com/docs/spaces/R ... eripheralssome of them are only supported if they have a certain firmware revision or USB vid/pid or will only work on v7 and not v6.HUAWEI E3372h-153 -> should work?HUAWEI E3372h-320 -> v7 onlyHUAWEI E352S-5 -> not on listALCATEL IK41VE1 -> should work?D-LINK DWM-222 -> should work? (may depend on firmware revision) ---

## Response 3
I can confirm that the Huawei E3372h-320 works on both the hAP ac and CCR1036-8G-2S+ with ROS7. ---

## Response 4
Power problem maybe ??Tried another power source ??You could try to add active usb hub. ---

## Response 5
Hi Guys, thank you for your help.I tried also other power adapter but no change.I tried also use USB HUB with external power delivery but no change.I crated ticket to mikrotik support and they send me reply:Device does not see any devices connected to the USB port. As a last resort, you can try to re-install the device using netinstall utility, but if that does not help, and RMA will be required.Device was sent to RMA. ---

## Response 6
You can verify that USB port works and that USB device attached does present to RouterOS kernel by running command
```
/system/resource/usb/printI checked it via winbox but i didnt saw there any device.I think there was some issue on mainbord.

---
```