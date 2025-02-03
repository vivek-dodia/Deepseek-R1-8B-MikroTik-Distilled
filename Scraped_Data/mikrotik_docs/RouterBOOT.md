---
title: RouterBOOT
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/136839241/RouterBOOT
crawled_date: 2025-02-02T20:25:26.563452
section: mikrotik_docs
type: documentation
---

* 1Main and Backup loaders
* 2RouterBOARD reset button
* 3Configuration Reset For Wireless Wire kits
* 4Configuration
* 5Simple Upgrade
* 6Checking RouterBOOT version
RouterBOOT is responsible for starting RouterOS in RouterBOARD devices.
## Main and Backup loaders
By default, the main (regular) loader is used, but RouterBOARD devices also have a secondary (backup) bootloader, which can be used in case the main doesn't work. It is possible to call the backup loader with a configuration setting in RouterOS:
```
system/routerboard/settings/set force-backup-booter=yes
```
It is also possible to use the backup booter by turning on the device, with the RESET button pushed. It is only possible to upgrade the main RouterBOOT, so in case of failure, you can use the backup booter to start the device and downgrade the main loader. For upgrade instructions, follow the separate instructions inRouterBOARD#UpgradingRouterBOOT
## RouterBOARD reset button
RouterBOOT reset button has three functions:
* Hold this button during boot time until the LED light starts flashing, and release the button to reset the RouterOS configuration (total 5 seconds)
* Keep holding for 5 more seconds, LED turns solid, release now to turn on CAPs mode (total 10 seconds)
* Or Keep holding the button for 5 more seconds until the LED turns off, then release it to make the RouterBOARD look for Netinstall servers
Reset the password
https://www.youtube.com/watch?v=6Unz92rABs8
## Configuration Reset ForWireless Wirekits
The reset button has the same functionality as on other devices, explained in detailhttps://help.mikrotik.com/docs/display/ROS/Reset+Button
5-second button hold on startup (USR LED light starts flashing) - resets to password-protected state.
10-second button hold on startup (USR LED turns solid after flashing) - completely removes configuration.
## Configuration
For RouterBOARD devices that feature a serial console connector, it is possible to access the RouterBOOT loader configuration menu. The required cable is described in theSerial Consolemanual. RouterBOARD serial port is configured to115200bit/s,8 data bits,1 stop bit, andno parity. We suggest disabling the hardware flow control.
This example shows the menu which is available in RouterBOOT 7.4beta4:
```
RouterBOOT booter 7.4beta4
CRS328-24P-4S+
built by build at Jun/15/2022 11:34:09 from revision 73B4521C
CPU frequency: 800 MHz
  Memory size: 512 MiB
 Storage size:  16 MiB
Press Ctrl+E to enter etherboot mode
Press any key within 2 seconds to enter setup
RouterBOOT-7.4beta4
What do you want to configure?
   d - boot delay
   k - boot key
   s - serial console
   n - silent boot
   o - boot device
   z - extra kernel parameters
   r - reset booter configuration
   e - format storage
   w - repartition nand
   g - upgrade firmware
   i - board info
   p - boot protocol
   b - booter options
   j - boot os
   t - hardware tests
   l - erase license
   x - exit setup
your choice:
```
The options are self-explanatory.
letter | description | explanation
----------------------------------
d | boot delay | Delays starting of RouterOS to allow an interface to initialize
k | boot key | The button that will open the configuration menu
s | serial console | Sets the baud rate of the serial port
n | silent boot | Suppresses all output on the serial port, in case some device is connected to it (like a GPS device or a temperature monitor)
o | boot device | Allows to enable Netinstall booting
z | extra kernel parameters | 
r | reset booter configuration | Resets the settings in this menu.Warning, no confirmation!
e | format storage | Destroys all data on the NAND, including RouterOS configuration and license
w | repartition nand | Refer to thePartitionsdocument for more info
y | active partition | Choose an active partition from which to try to load RouterOS
g | upgrade firmware | Allows upgrading RouterBOOT version through the network, or the XModem protocol
i | board info | 
p | boot protocol | 
b | booter options | Select which bootloader to use by default
t | do memory testing | booter options
j | boot os | do memory testing
t | hardware tests | 
l | erase license | 
x | exit setup | 
exit setup
Hitting the appropriate keyboard letter will give you a list of further options, they are shown below:
```
# d - boot delay:
Select boot delay:
   1 - 1s
 * 2 - 2s
   3 - 3s
   4 - 4s
   5 - 5s
   6 - 6s
   7 - 7s
   8 - 8s
   9 - 9s
# k - boot key:
Select key which will enter setup on boot:
 * 1 - any key
   2 - <Delete> key only
# s - serial console:
Select baud rate for serial console:
 * 1 - 115200
   2 - 57600
   3 - 38400
   4 - 19200
   5 - 9600
   6 - 4800
   7 - 2400
   8 - 1200
   9 - off
# n - silent boot:
Silent boot:
   0 - off
 * 1 - on
# o - boot device:
Select boot device:
   e - boot over Ethernet
 * n - boot from NAND, if fail then Ethernet
   1 - boot Ethernet once, then NAND
   o - boot from NAND only
   b - boot chosen device
   f - boot Flash Configure Mode
   3 - boot Flash Configure Mode once, then NAND
# f - cpu frequency:
Select CPU frequency:
   a -  200MHz
   b -  400MHz
   c -  600MHz
   d -  800MHz
   e - 1000MHz
 * f - 1200MHz
# r - reset booter configuration:
# e - format nand:
Do you realy want to format your storage device?
that would result in losing all your data
type "yes" to confirm: 
# w - repartition nand:
Select parititon count:
   1 - partition
 * 2 - partitions
   3 - partitions
   4 - partitions
# y - active partition:
Select active partiton:
 * 0 - partition
   1 - partition
# g - upgrade firmware:
Upgrade firmware options:
   e - upgrade firmware over ethernet
   s - upgrade firmware over serial port
# i - board info:
Board Info:
        Board type: CCR1009-8G-1S-1S+
     Serial number: 48FF01DDE6FD
  Firmware version: 3.19
     CPU frequency: 1200 MHz
       Memory size: 2048 MiB
         NAND size: 128 MiB
        Build time: 2014-09-23 15:02:34
  eth1 MAC address: 00:0C:42:00:BE:4A
  eth2 MAC address: 00:0C:42:00:BE:4B
  eth3 MAC address: 00:0C:42:00:BE:4C
  eth4 MAC address: 00:0C:42:00:BE:4D
  eth5 MAC address: 00:0C:42:00:BE:4E
  eth6 MAC address: 00:0C:42:00:BE:4F
  eth7 MAC address: 00:0C:42:00:BE:50
  eth8 MAC address: 00:0C:42:00:BE:51
  eth9 MAC address: 00:0C:42:00:BE:52
 eth10 MAC address: 00:0C:42:00:BE:53
# p - boot protocol:
Choose which boot protocol to use:
 * 1 - bootp protocol
   2 - dhcp protocol
# b - booter options:
Select which booter you want to load:
 * 1 - load regular booter
   2 - force backup-booter loading
#t - do memory testing:
launches built in memory test!
# x - exit setup:
Exit bios configuration menu and continues with system startup.
```
## Simple Upgrade
RouterBOOT can be upgraded from RouterOS by:
* Run command/system routerboard upgrade
* Reboot your router to apply the upgrade (/system reboot)]
```
[admin@admin] > system/routerboard/upgrade 
Do you really want to upgrade firmware? [y/n]
```
## Checking RouterBOOT version
This command shows the current RouterBOOT version of your device and the available upgrade which isincluded inrouteros-x.yy.npkpackage, or if you uploaded a*.FWFfilecorresponding to the device model:
```
[admin@admin] >  system/routerboard/print 
                ;;; Firmware upgraded successfully, please reboot for changes 
                    to take effect!
       routerboard: yes
        board-name: hAP ac
             model: RouterBOARD 962UiGS-5HacT2HnT
     serial-number: 6737057562DD
     firmware-type: qca9550L
  factory-firmware: 3.29
  current-firmware: 6.49.5
  upgrade-firmware: 7.4beta5
```
In this case, you see, there isa newer versionof the Bootloader firmware available already inside your current RouterOS version and it has been updated and requires a reboot.