---
title: Upgrading and installation
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/328142/Upgrading+and+installation,
crawled_date: 2025-02-02T21:08:39.514305
section: mikrotik_docs
type: documentation
---

* 1Overview
* 2Upgrading2.1Version numbering2.2Standard upgrade2.4Manual upgrade2.4.1Manual upgrade process2.4.1.1Using WinBox2.4.1.2Using FTP2.5RouterOS local upgrade2.6RouterOS upgrade using Dude2.6.1The Dude auto-upgrade2.6.2The Dude hierarchical upgrade2.7License issues
* 3Netinstall
* 4CD Install
* 5RouterOS Package Types
* 2.1Version numbering
* 2.2Standard upgrade
* 2.4Manual upgrade2.4.1Manual upgrade process2.4.1.1Using WinBox2.4.1.2Using FTP
* 2.5RouterOS local upgrade
* 2.6RouterOS upgrade using Dude2.6.1The Dude auto-upgrade2.6.2The Dude hierarchical upgrade
* 2.7License issues
* 2.4.1Manual upgrade process2.4.1.1Using WinBox2.4.1.2Using FTP
* 2.4.1.1Using WinBox
* 2.4.1.2Using FTP
* 2.6.1The Dude auto-upgrade
* 2.6.2The Dude hierarchical upgrade
# Overview
MikroTik devices are preinstalled with RouterOS, so installation is usually not needed, except in the case where installing RouterOS on an x86 PC or virtual instance CHR. The upgrade procedure on already installed devices is straightforward.
# Upgrading
## Version numbering
RouterOS versions are numbered sequentially when a period is used to separate sequences, it doesnotrepresent a decimal point, and the sequences donothave positional significance. An identifier of 2.5, for instance, is not "two and a half" or "halfway to version three", it is the fifth second-level revision of the second first-level revision. Therefore v5.2 is older than v5.18, which is newer.
RouterOS versions are released in several "release chains": Long term, Stable, Testing, and Development. When upgrading RouterOS, you can choose a release chain from which to install the new packages.
* Long term: Released rarely, and includes only the most critical fixes, upgrades within one number branch do not contain new features. When aStablerelease has been out for a while and seems to be stable enough, it gets promoted into the long-term branch, replacing an older release, which is then moved to the archive. This consecutively adds new features.
* Stable: Released every few months, including all tested new features and fixes.
* Testing: Released every few weeks, only undergoes basic internal testing, and should not be used in production.
* Development: Released when necessary. Includes raw changes and is available for software enthusiasts for testing new features.
## Standard upgrade
The package upgrade feature connects to the MikroTik download servers and checks if there is another RouterOS version for your device under the selected release channel. Can also be used for downgrading, if you, for example, are using stable release at the moment, but changed the release channel to the long-term.
After clicking theCheck For Updatesbutton in QuickSet (or in the System → Packages menu) theCheck For Updateswindow will open with the current or the latest changelog (if a newer version exists). If newer version exists, buttonsDownloadandDownload&Installwill appear. By cicking theDownloadbutton a newest version will be downloaded (manual device reboot is required), by clickingDownload&Install, download will start, and after a successful download will reboot a device to install the downloaded packages.
The versions offered will depend on the selected release channel. Not all versions migh be available. It will not be possible to upgrade from an older version to the latest version in one go, when using check-for-updates approach. For example, if running RouterOS v6.x, even selecting the major release upgrade channel, called "Upgrade", you will only see v7.12.1 as the available version. You must first upgrade to that intermediate version and only then newer releases will be available in the channels. This intermediate step can be done using check for updates too, but you will simply have to repeat check for updates after the first update to the intermediate version.
If custom packages are installed, the downloader will take that into account and download all necessary packages.
You canautomatethe upgrade process by running a script in the system scheduler. This script queries the MikroTik upgrade servers for new versions, if the response received says "New version is available", the script then issues the upgrade command below. Important note, this will not work, if you are running it for the first time on a release that is older. It might not see latest versions as available, if you are running v6.x, you would first have to manually select the "Upgrade" channel to do a major release upgrade to v7.12.1 intermediate version, and only afterwards newer v7 releases will be visible in the upgrade channels.
```
[admin@MikroTik] >/system package update
check-for-updates once
:delay 3s;
:if ( [get status] = "New version is available") do={ install }
```
## Manual upgrade
You can upgrade RouterOS in the following ways:
* WinBox – drag and drop files to the Files menu
* WebFig - upload files from the Files menu
* FTP - upload files to the root directory
### Manual upgrade process
* First step - visitwww.mikrotik.comand head to the Software page, then choose the architecture of the system you have the RouterOS installed on (system architecture can be found in System → Resource section);
* Download therouteros(main)and extra packages that are installed on a device;
* Upload packages to a device using one of the previously mentioned methods:
Menu:/system/package/update installignore-missingcommand allows upgrading only the RouterOS main package, while omitting packages that are either missing or not uploaded during a manual upgrade process.
#### Using WinBox
Choose your system type, and download the upgrade package. Connect to your router with WinBox, Select the downloaded file with your mouse, and drag it to the Files menu. If some files are already present, make sure to put the package in the root menu, not inside the hotspot folder! The upload will start.
After it finishes - reboot the device. The New version number will be seen in the Winbox Title and in the Packages menu
#### Using FTP
* Open your favorite SFTP program (in this case it isFilezilla), select the package, and upload it to your router (demo2.mt.lvis the address of my router in this example). note that in the image I'm uploading many packages, but in your case - you will have one file that contains them all
* if you wish, you can check if the file is successfully transferred onto the router (optional):
```
[admin@MikroTik] >/file print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME                  TYPE       SIZE     CREATION-TIME       
0  routeros-7.9-arm.npk  package    13.0MiB  may/18/2023 16:16:18
1  pub                   directory           nov/04/2022 11:22:19
2  ramdisk               directory           jan/01/1970 03:00:24
```
* reboot your router for the upgrade process to begin:
```
[admin@MikroTik] >/system reboot
Reboot, yes? [y/N]: y
```
* after the reboot, your router will be up to date, you can check it in this menu:
```
[admin@MikroTik] >/system package print
```
* if your router did not upgrade correctly, make sure you check thelog
```
[admin@MikroTik] >/log print without-paging
```
## RouterOS local upgrade
Sub-menu:system/package/local-update/
```
system/package/local-update/
```
You can upgrade one or multiple MikroTik routers within your local network by using one device which have all needed packages. Feature is available from7.17beta3version in (system > packages local update) and will replace (system > auto update) feature. Here is a simple example with 3 routers (the same method works on networks with infinite numbers of routers):
Place needed packages under Files menu, on your main router:
Optional, you can set mirror device between main one, if not needed, skip this step:
* Choose Local Package Sources and enable Mirror device. Set Primary Server where the packages are located, 10.155.136.50. Check Intervalminimumsetting can be set to 00:07:12, at which device will connect using Winbox to a main device and check for packages.If new packages are available, it will begin to download, please note download process is slow and may require some time when large amount of files are used. In case some failures, download will resume on next Check.
* New "packs" folder is created, where mirror device will store packages:
* Add new package source on device which will be updated, in this example we use mirror device 10.155.136.71:
* Once you click Refresh in Local Update packages tab,  device using Winbox will try to connect to source and check if there are new packages.
* Choose packages and click download, after download completes device will be needed to reboot for update.
* Use system/package/local-update/refresh to automate this in your scripts and tools fetch url= can be used to download packages from our web page, for example: tool/fetch url=https://download.mikrotik.com/routeros/7.16.1/routeros-7.16.1-arm.npk
## RouterOS upgrade using Dude
#### The Dude auto-upgrade
The dude application can help you to upgrade the entire RouterOS network with one click per router.
* Set typeRouterOSand correct password for any device on your Dude map, that you want to upgrade automatically,
* Upload required RouterOS packages to Dude files
* Upgrade the RouterOS version on devices from the RouterOS list. The upgrade process is automatic, after a click on upgrade (or force upgrade), the package will be uploaded and the router will be rebooted by the Dude automatically.
#### The Dude hierarchical upgrade
For complicated networks, when routers are connected sequentially, the simplest example is "1router-2router-3router| connection. You might get an issue, 2router will go to reboot before packages are uploaded to the 3router. The solution is Dude Groups, the feature allows you to group routers and upgrade all of them with one click!
* Select the group and click Upgrade (or Force Upgrade),
## License issues
When upgrading from older versions, there could be issues with your license key. Possible scenarios:
* When upgrading from RouterOS v2.8 or older, the system might complain about an expired upgrade time. To override this, use Netinstall to upgrade. Netinstall will ignore old license restrictions and will upgrade
* When upgrading to RouterOS v4 or newer, the system will ask you to update the license to a new format. To do this, ensure your Winbox PC (not the router) has a working internet connection without any restrictions to reachwww.mikrotik.comand click "update license" in the license menu.
# Netinstall
NetInstallis a widely-used installation tool for RouterOS. It runs on Windows systems or via a command-line tool, netinstall-cli, on Linux, or through Wine (with superuser permissions required).
The NetInstall utilities can be downloaded from theMikroTikdownloadsection.
NetInstallis also used to re-install RouterOS in cases where a previous installation has failed, been damaged, or where access passwords have been lost.
To use NetInstall, your device must support booting from Ethernet, with a direct Ethernet connection between the NetInstall computer and the target device. All RouterBOARDs support PXE network booting, which can be enabled in the RouterOS "routerboard" menu (if RouterOS is accessible) or in the bootloader settings using a serial console cable.
Note:For RouterBOARD devices without a serial port or RouterOS access, you can activate PXE booting using theReset button.
NetInstallcan also directly install RouterOS onto a disk (USB/CF/IDE/SATA) connected to the NetInstall Windows machine. Once installed, simply transfer the disk to the Router machine and boot from it.
Attention!Do not try to install RouterOS on your system drive. Action will format your hard drive and wipe out your existing OS.
# CD Install
# RouterOS Package Types
Information about RouterOS packages can be foundhere