# Thread Information
Title: Thread-1121414
Section: RouterOS
Thread ID: 1121414

# Discussion

## Initial Question
Hi, today I updated to the latest firmware version v7.15.3 and received a warning that requires upgrading the backup RouterBOOT for optimal NAND stability. I have an RB2011UiAS with the factory firmware v3.41 (F.T.: AR9344). Can someone tell me how to do it? Thanks. ---

## Response 1
Can someone help me with this? thanks ---

## Response 2
Isn't that documented here?https://help.mikrotik.com/docs/display/ ... RouterBOOT ---

## Response 3
look at the protected bootloader section of the above document ---

## Response 4
In the Protected Bootloader section, it shows v7 and v6, but I have version v3.41. What version should I add to the device? What is the procedure? Thanks. ---

## Response 5
I am not sure to understand, the v3.41 is likely your factory-firmware, that is "carved in stone" and cannot be changed.Post the output of/system routerboard printand of/system resource print(remove serial)Anyway, you need to be careful, and do the procedure in the given page:A special package is provided to upgrade the backup RouterBOOT (DANGEROUS). Newer devices will have this new backup loader already installed at the factory. If your RouterOS is v7, your factory-firmware version is lower than 7.6 and your device displays the message → The "protected routerboot" feature requires a backup-routerboot upgrade ← when trying to enable the feature, do the following:a) upgrade or downgrade the device specifically to the 7.6 release (from our download page or archive).b) upgrade your current RouterBOOT version with "/system routerboard upgrade" then reboot the device, so that the RouterBOOT version (current-firmware version when checking "/system routerboard print") is the same as the firmware version ("/system resource print") installed, which should be 7.6.c) drag and drop the v7 universal package for all architectures into the device's file system then reboot the device again. This will make your factory-firmware version 7.6, where you are allowed to enable the feature. After this step, you can upgrade the device to a newer release.If your RouterOS version is v6 and you get the same prompt, follow the same steps mentioned above, but only update/downgrade/compare your device version to specifically 6.49.7 instead and use v6 universal package for all architectures. ---

## Response 6
In the Protected Bootloader section, it shows v7 and v6, but I have version v3.41. What version should I add to the device?It doesn't matter which version your device currently shows, what matters is which version you want to have. If you plan to run ROS v7, then start with 7.6 ... first ROS (under packages), then Routerboot (under Routerboard) and then the backup routerboot (the special package). After that you should upgrade ROS to some recent version, e.g. 7.15.2 (again followed by Routerboot, but don't touch backup Routerboot any more)Similarly with 6.49.7 if you plan to stay with v6. ---

## Response 7
In the wiki version it notesThe backup RouterBOOT version can not be older than v3.24 version.So presumably given yours is newer than this, you don't need an upgraded backup routerboot. (so it won't let you upgrade it perhaps) ---

## Response 8
I'm going to try it and let you know how it goes. ---

## Response 9
check it herhttps://help.mikrotik.com/docs/display/ ... RouterBOOT ---

## Response 10
Strange - hEX was able to update backup-routerboot and factory software version was changed to 7.6, but RB450Gx4 had just message "installed package bb-upgrade-7.6" but message about updating factory software version was not in the log and factory software version was not actually updated while all procedure was done in same way for both devices... ---

## Response 11
This isn't directly related to the original topic. A search of the forum indicates that the only supported architectures for upgrade are MIPSBE, SMIPS, MMIPS, TILE and some PPC but NO ARMviewtopic.php?t=94303#p580430 ---

## Response 12
It makes sense then that mmips device succeeded but arm device did not... ---