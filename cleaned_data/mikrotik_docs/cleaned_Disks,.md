# Document Information
Title: Disks
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/91193346/Disks,

# Content
# Summary
Sub-menu:/disk
```
/disk
```
This menu will list all attached storage devices, presuming that they are supported and in working condition. This is especially useful for RouterBOARD devices with SD/CF/USB/SATA/NVMe slots and x86 systems with additional dedicated storage drives - as the built-in storage is quite small, an external drive comes in very handy when you want a big User Manager database, proxy cache or possibly SMB shares on your router.
You can add as many external or secondary drives as you want, and select any number of them for each of the mentioned feature usages. For example, User Manager could be used on 3 disks, one of them would be the active database, and the rest would be backups. You can then add a fourth disk, copy the active data to it - unmount - unplug it - and move to another server, to keep using the actual database. This means migration and backup are made easy!
Disks carry names where they are physically connected.
# Properties
Property | Description
----------------------
eject-drive() | Safely unmounts (ejects) drive of your selection by using "slot" that is assigned to it. After issuing this command it can be removed from host device.
format-drive() | Command to initiate disk formatting process. Contains additional properties of its own. Such as "file-system" and "label".select disk (slot) that should be formattedfile-system('exfat', 'ext4', 'fat32' or 'wipe') - Format disk with type ExFAT, FAT32 or EXT4 or securely wipe all datalabelmbr-partition-table - make mbr partition table
reset-counters | Resets disk (slot) statistics
monitor-traffic | Check real time disk performance and health stats
test | allows performing performance tests of selected device (Available from RouterOS 7.16)disk -device or devices for testdirection- ('read','write')duration - (int)pattern - ('random', 'sequential')thread-count - (int)block-size - size of block to be used for testingtype - ('device', 'filesystem')
allows performing performance tests of selected device (Available from RouterOS 7.16)
# Flags
Property | Description
----------------------
X - disabled | Disabled device
E - empty | Empty slot
B - BLOCK-DEVICE | The "B - BLOCK-DEVICE"- Flag means that this device works using blocks for input/output operations. In the context of RouterOS, its distinction is crucial, as it helps determine whether a device is functioning as a data carrier or simply providing information about the disk layout structure. This difference becomes important when considering the extender with the device behind it. If a device is marked with the letter "B", this indicates its ability to be used as storage or memory. In contrast, devices that do not have a "B" mark are designed primarily to understand the structure of the disk.This allows to quickly recognize the presence of a PCIe or SAS expander, as well as detect the presence of drives in the first expander. In addition, it allows you to estimate the speed of the connection to which each device is connected.However, the most notable benefit of the "B" flag is its ability to instantly indicate whether a device can be formatted or used for RAID purposes.
M - mounted | Mounted partition
F - formatting | The device is currently in the formatting process
p - partition | The device has a partition
f - raid-member-failed | These options are used with theROSEpackage.
r - raid-member
c - encrypted
g - guid-partition-table
t - nvme-tcp-export
i - iscsi-export
s - smb-export
n - nfs-export
O - tcg-opal-self-encryption-enabled
o - tcg-opal-self-encryption-supported
Disabled device
Empty slot
The "B - BLOCK-DEVICE"- Flag means that this device works using blocks for input/output operations. In the context of RouterOS, its distinction is crucial, as it helps determine whether a device is functioning as a data carrier or simply providing information about the disk layout structure. This difference becomes important when considering the extender with the device behind it. If a device is marked with the letter "B", this indicates its ability to be used as storage or memory. In contrast, devices that do not have a "B" mark are designed primarily to understand the structure of the disk.
This allows to quickly recognize the presence of a PCIe or SAS expander, as well as detect the presence of drives in the first expander. In addition, it allows you to estimate the speed of the connection to which each device is connected.
However, the most notable benefit of the "B" flag is its ability to instantly indicate whether a device can be formatted or used for RAID purposes.
# Settings
Property | Description
----------------------
auto-smb-sharing(yes | no; Default: no) | Enables dynamic SMB shareswhen new disk/partition item is added in "/disk"
auto-smb-user(list of strings; Default: ) | Default value for smb-sharing/smb-user setting, when new disk/partition item is added in "/disk"
auto-media-share(yes | no; Default: no) | Enables media dynamically when new disk/partition item is added in "/disk"
auto-media-interface(list of strings; Default: ) | Interface that will be used in dynamic instance for ip/media when new disk/partition item is added in "/disk"
# Examples
# Formatting attached storage unit - Simple
1. Disk is attached, and already mounted automatically by the system.
```
[admin@MikroTik] > disk print
Flags: B - BLOCK-DEVICE; M, F - FORMATTING
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS
# SLOT  MODEL           SERIAL            INTERFACE                  SIZE           FREE  FS
0 BM usb1  USB Flash Disk  FBA0911260071572  USB 2.00 480Mbps  2 004 877 312  1 921 835 008  ext4
```
```
[admin@MikroTik] > /file print
# NAME                        TYPE          SIZE CREATION-TIME
0 skins                       directory          jan/01/1970 03:00:01
1 pub                         directory          feb/04/1970 21:31:40
2 usb1                        disk               mar/07/2022 14:05:16
```
1. Formatting the disk, in either of two supported file-systems (ext4 or fat32).
```
[admin@MikroTik] > /disk format-drive usb1 file-system=ext4 mbr-partition-table=no
formatted: 100%
```
1. It's done! Drive is formatted and should be automatically mounted after formatting process is finished.
# Formatting attached storage unit - Detailed
Let us presume that you have added a storage device to your device that is running RouterOS. System will try to automatically mount it and in such case if storage is formatted in a supported file-system and partition record, it will be found in "/files" menu moments after you plugged it in to the host device.
If not, here is what you have to do.
1. Do a quick print of disk menu, to make sure that router sees the attached storage.
```
[admin@MikroTik] > disk print
Flags: B - BLOCK-DEVICE; M, F - FORMATTING
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS
# SLOT  MODEL           SERIAL            INTERFACE                  SIZE           FREE  FS
0 BM usb1  USB Flash Disk  FBA0911260071572  USB 2.00 480Mbps  2 004 877 312  1 921 835 008  ext4
```
We can here see that system sees one storage drive and also that it is formatted with a known file-system type.
When running file menu print-out we also see that is mounted.
```
[admin@MikroTik] > file print
# NAME     TYPE    SIZE CREATION-TIME
0 usb1     disk         mar/07/2022 14:05:16
1 skins    directory    jan/01/1970 03:00:01
2 pub      directory    feb/04/1970 21:31:40
```
1. To formatting drive - we issue command with previously know id or name(slot) and with desired file-system (ext4 or fat32), we can also assign label to device as I did in this example and make mbr partition table
```
[admin@MikroTik] > /disk format-drive usb1 file-system=ext4 label=usb-flash mbr-partition-table=yes
formatted: 100%
```
If multiple GPT partitions are needed format drive without partition table and add them manually:
```
[admin@MikroTik] > /disk format-drive usb1 file-system=ext4 label=usb-flash mbr-partition-table=no
formatted: 100%
```
```
[admin@MikroTik] > /disk add type=partition parent=usb1 partition-size=200M
[admin@MikroTik] > /disk add type=partition parent=usb1 partition-size=500M
[admin@MikroTik] > /disk add type=partition parent=usb1 slot=usb1-last-partition
```
# Web-Proxy cache configuration example
Enter proxy cache path under IP -> Proxy menu and web proxy store is automatically created in files menu. If a non-existent directory path is used, an additional sub-directory is also created automatically.
```
[admin@MikroTik] >  /ip proxy set cache-path=usb1/cache-n-db/proxy/
...
[admin@MikroTik] >  /file print
# NAME                                              TYPE                             SIZE CREATION-TIME
0 skins                                             directory                             mar/02/2015 18:56:23
1 sys-note.txt                                      .txt file                        23   jul/03/2015 11:40:48
2 usb1                                             disk                                  jul/03/2015 11:35:05
3 usb1/lost+found                                  directory                             jul/03/2015 11:34:56
4 usb1/cache-n-db                                  directory                             jul/03/2015 11:41:54
4 usb1/cache-n-db/proxy                            web-proxy store                       jul/03/2015 11:42:09
```
# Log on disk configuration example
When configuring logging on disk make sure that you create directories in which you want to store the log files manually, as non-existent directories will NOT be automatically created in this case.
```
[admin@MikroTik] >  /system logging action set disk disk-file-name=/disk1/log
...
[admin@MikroTik] >  /file print where name~"disk1/log"
# NAME                                              TYPE                             SIZE CREATION-TIME
0 disk1/log                                        directory                             jul/03/2015 12:44:09
1 disk1/log/syslog.0.txt                           .txt file                         160 jul/03/2015 12:44:11
```
# Allocate RAM to folder
It is possible to add folders linked to RAM. Folders will be emptied on reboot or power loss.RAM will be filled up to tmpfs-max-size and if this variable in not provided - up to 1/2 from available RAM.
```
[admin@MikroTik] >  /disk add type=tmpfs tmpfs-max-size=100M
[admin@MikroTik] > file print
Columns: NAME, TYPE, SIZE, CREATION-TIME
# NAME            TYPE       SIZE             CREATION-TIME
0  tmp1             disk     100 003 840        dec/12/2022 11:01:48
```
# Test disk performance
Starting from 7.16 to run disk performance tests. Disks has to be disabled or without mountable file system (unformatted).Check available disks, if disk is already mounted - disable it.
```
[admin@MikroTik] > disk print
Flags: B - BLOCK-DEVICE; M - MOUNTED
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS
# SLOT  MODEL             SERIAL         INTERFACE                    SIZE            FREE  FS
0 BM usb1  JMicron External  DD56419883891  USB 3.10 5000Mbps  64 023 257 088  62 692 188 160  ext4
[admin@MikroTik] > disk disable usb1
[admin@MikroTik] > disk test disk=usb2 pattern=sequential  type=device thread-count=4 block-size=4K direction=write
Columns: SEQ, RATE, IOPS, DISK, TYPE, PATTERN, DIR, BSIZE, THREADS
SEQ  RATE          IOPS  DISK  TYPE    PATTERN     DIR    BSIZE  THREADS
0    1622.5Mbps  49 516  usb2  device  sequential  write   4096        4
1    26.2Mbps       800  usb2  device  sequential  write   4096        4
2    33.0Mbps     1 008  usb2  device  sequential  write   4096        4
3    11.7Mbps       360  usb2  device  sequential  write   4096        4
4    28.5Mbps       872  usb2  device  sequential  write   4096        4
5    34.6Mbps     1 056  usb2  device  sequential  write   4096        4
6    33.8Mbps     1 032  usb2  device  sequential  write   4096        4
TOT  255.7Mbps    7 806  usb2  device  sequential  write   4096        4
```