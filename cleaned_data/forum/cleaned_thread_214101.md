# Thread Information
Title: Thread-214101
Section: RouterOS
Thread ID: 214101

# Discussion

## Initial Question
I have upgraded one RBwAPG-5HacD2HnD from version 7.13.5 to 7.17 by uploading the required files (os + wifi-com-ac) and rebooting the device. After the update, the device stopped working because it couldn't start the OS (it boots with Etherboot mode). I have applied Netinstall with the same NPKs and now is working as expected.Fortunately, the equipment was physically accessible and it was used as a backup router. If the problem had occurred with a more critical device, it could have been a very big issue. This is something that has happened to us in previous versions and we have been unable to locate the cause of the error. As far as I understand, if the router does not have enough memory the update gets canceled, but it does not get bricked like in this case...Could any of you provide some insight about what could be the cause? Storage space, power supply...Thanks! ---

## Response 1
Mikrotik Devices with 16MB Storage are prone to running out of DISK spacewhen updating to the latest version of RouterOS. Resulting in failed Updates or in some casesin the Device not booting anymore.This is especially true, if you have Data on the Device and/or optional Packages installed (e.g. wifi-qcom-ac) ---

## Response 2
Well, I think there should be a stable update process to this kind of devices. It is unacceptable that the update process can randomly fail, with the consequence of leaving the router completely unusable.Could Mikrotik support team give us some info about how to proceed? ---

## Response 3
Just to be clear, the Device doesn`t "randomly" fail, it runs out of storage spaceBut yeah... it shouldn`t happen :DP.S: Mikrotik do have some Warnings....Before an upgrade:1) Remember to make backup/export files before an upgrade and save them on another storage device;2) Make sure the device will not lose power during upgrade process;3) Device has enough free storage space for all RouterOS packages to be downloaded.viewtopic.php?t=213941 ---

## Response 4
Allow me to disagree.What would be the problem in having the update process actually checking that there is enough space (+ a reasonable amount of "slack") and simply plain refusing to go on?With a message *like*:The pre-update check determined that this device has x.xx Kbytes free, a minimum of y.yy Kbytes are needed.Continuing is likely to fail or even brick the device.Aborting in 60 seconds time.If you want to continue type in CAPITAL LETTERS:YESIWANTTORISKABRICKand press [Enter] within this time. ---

## Response 5
Yeah, something like that would be enough to avoid possible disastersDo any of you have any information about how many free space is required to avoid a potential brick? These devices have around 400-500KB of free flash memory and if the stored configuration is large enough, you can get out of space pretty easily...In our case, we also have some scripts to handle LTE recovery and other maintenance tasks so we are afraid that we won't be able to update any of our routers without risking a major outage.Thanks! ---