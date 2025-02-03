---
title: Packages
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/40992872/Packages ,
crawled_date: 2025-02-02T20:25:09.476885
section: mikrotik_docs
type: documentation
---

* 1Summary
* 2Acquiring packages
* 3RouterOS packages3.1System packages3.2Extra packages
* 4Working with packages
* 5Examples
* 3.1System packages
* 3.2Extra packages
## Summary
In RouterOS v7, most of the features are combined in onerouteros(system) package.
Installing the corresponding package can enable specific features (like container, dude).
Packages are provided only by MikroTik, and no 3rd parties are allowed to make them.
## Acquiring packages
Packages can be downloaded fromtheMikroTik downloadpage.
## RouterOS packages
Starting from RouterOS 7.13, therouteros(system) package and one of the wireless packages are needed for the basic operation of a simple home router.
802.11ax WiFi APs require radio drivers, which are provided by thewifi-qcompackage or (for RouterOS version before 7.13) thewifiwave2package.
Previous generation WiFi APs require awirelesspackage.
Other packages are optional and not required for a home router. Install them only if you are sure of their purpose.
For an example,E50UG - hEX refresh uses ARM packages.
### System packages
Package | Description
---------------------
routeros-arm(arm) | system package for arm devices
routeros-arm(arm64) | system package for arm64 devices
routeros-mipsbe(mipsbe) | system package for mipsbe devices
routeros-mmips(mmips) | system package for mmips devices
routeros-smips(smips) | system package for smips devices
routeros-tile(tile) | system package for tile devices
routeros-ppc(ppc) | system package for ppc devices
routeros(x86, CHR) | system package for x86 installations and CHR environment
### Extra packages
To install extra packages, download the necessary package from theMikroTik downloadpage, selecting the RouterOS v6 section based on your device's architecture found in the System/Resources menu. Extract the archive and upload the required package to your routerusing any convenient method,and proceed to reboot the router.
Package (supported architecture) | Description
----------------------------------------------
calea(arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR) | Data gathering tool for specific use due to "Communications Assistance for Law Enforcement Act" in the USA
container(arm, arm64, x86, CHR) | Containerimplementation of Linux containers,allows users to run containerized environments within RouterOS
dude(arm, arm64, mmips, tile, x86, CHR) | Dudetool that allows monitoring of networkenvironment
extra-nic(arm64) | arm64 CPU architecture, Network Interface Card(NIC) support, recommended for UEFI installation on non MikroTik boards
gps(arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR) | Global Positioning Systemdevices support
iot(arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR) | Enables:MQTTLoRa(for devices with LR8/9/2 miniPCie cards)Bluetooth(for devices with Bluetooth chip)GPIO(for devices with GPIO pins)Modbus(for devices with RS485 port)
iot-bt-extra(arm, arm64) | A package for ARM, ARM64 devices which enables the use of USB Bluetooth adapters (must support LE 4.0+).note:Not all adapters were tested. We can not guarantee beforehand that a specific adapter will work.
lora(arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR) | Dummy package forLorasupport.LoRa package is not obligatory anymore and is left only for compatibility reasons. LoRa functionality is moved into iot package.
lte(mipsbe) | Required package only for SXT LTE (RBSXTLTE3-7), which contains drivers for the built-in LTE interface.
rose-storage(arm, arm64, tile, x86, CHR) | Additionalenterprise data center functionalityin RouterOS, support disk monitoring, improved formatting, RAIDs, rsync, iSCSI , NVMe over TCP, NFS, and improved SMB
tr069-client(arm, arm64, mipsbe, mmips, smips, tile, ppc, x86, CHR) | TR069 Clientpackage
ups(arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR) | APC ups managementinterface
user-manager(arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR) | MikroTik User Managerserver for controlling Hotspot and other service users.
wifi-qcom(arm, arm64) | Mandatory driver package for 802.11ax interfaces. Introduced in 7.13.Wifi CAPsMANsupport comes with the system package.
wifi-qcom-ac(arm) | OptionalWifidriver package for compatible 802.11ac interfaces. Introduced in 7.13.
wireless(arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR) | Utilities and drivers for managing WiFi (up to 802.11ac) and 60GHz wireless interfaces.This package is bundled into RouterOS for versions up to 7.12. Starting with 7.13, it is a separate package.Thewirelesspackage conflicts withwifi-qcomandwifi-qcom-acpackages - they cannot be active at the same time.
zerotier(arm, arm64) | EnablesZeroTierfunctionality
Enables:
* MQTT
* LoRa(for devices with LR8/9/2 miniPCie cards)
* Bluetooth(for devices with Bluetooth chip)
* GPIO(for devices with GPIO pins)
* Modbus(for devices with RS485 port)
A package for ARM, ARM64 devices which enables the use of USB Bluetooth adapters (must support LE 4.0+).
note:Not all adapters were tested. We can not guarantee beforehand that a specific adapter will work.
Utilities and drivers for managing WiFi (up to 802.11ac) and 60GHz wireless interfaces.This package is bundled into RouterOS for versions up to 7.12. Starting with 7.13, it is a separate package.
Thewirelesspackage conflicts withwifi-qcomandwifi-qcom-acpackages - they cannot be active at the same time.
## Working with packages
Menu:/system package
Commands executed in this menu will take place only on restart of the router. Until then, the user can freely schedule or revert set actions.
Command | Description
---------------------
disable | schedule the package to be disabled after the next reboot. No features provided by the package will be accessible
downgrade | will prompt for the reboot. During the reboot process will try to downgrade the RouterOS to the oldest version possible by checking the packages that are uploaded to the router.
enable | schedule package to be enabled after the next reboot
uninstall | schedule package to be removed from the router. That will take place during the reboot.
unschedule | remove scheduled task for the package.
print | outputs information about the packages, like: version, package state, planned state changes, etc.
update | manages the"check-for-updates"channel and performs RouterOS upgrades
Menu:/system/check-installation
The "Check installation" function ensures the integrity of the RouterOS system by verifying the readability and correct placement of files. Its primary purpose is to confirm the health and status of your NAND/Flash storage.
Menu:/system/package/update install ignore-missingcommand allows upgrading only the RouterOS main package, while omitting packages that are either missing or not uploaded during a manual upgrade process.
## Examples
The upgrade process is describedhere.
List of available packages.
zerotier package is disabled and dude package is scheduled for uninstall.
```
/system package print 
Flags: X - DISABLED
Columns: NAME, VERSION, SCHEDULED
#   NAME      VERSION  SCHEDULED              
0   dude      7.9      scheduled for uninstall
1 X zerotier  7.9                             
2   routeros  7.9
```
Uninstall package
```
/system package uninstall dude; /system reboot; 
Reboot, yes? [y/N]:
```
Disable package
```
/system package disable zerotier; /system reboot;
Reboot, yes? [y/N]:
```
Downgrade
```
/system package downgrade; /system reboot;
Reboot, yes? [y/N]:
```
Cancel uninstall or disable action
```
/system package unschedule zerotier;
/system package unschedule dude;
```