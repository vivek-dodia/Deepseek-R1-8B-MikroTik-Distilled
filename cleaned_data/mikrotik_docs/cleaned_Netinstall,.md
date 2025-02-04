# Document Information
Title: Netinstall
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/24805390/Netinstall,

# Content
# Introduction
Netinstall is a tool for installing and reinstalling MikroTik devices running RouterOS. Always try using Netinstall if you suspect that your device is not working properly. The tool is available for Windows (with a graphical interface) and for Linux (as a command line tool).
In short, the Netinstall procedure goes like this: Connect your PC directly to thebootport (Usually Ether1, the port labeled BOOT or as otherwise indicated in the product manual) of the device you will be reinstalling. Turn on the device while holding theresetbutton until it shows up in the Netinstall tool.
# Instructions for Windows
Download the RouterOSMain packagefrom thedownloadspage;
Disable all computer network interfaces (WiFi, Ethernet, LTE, or any other type of connection) except for the one to be used for installation. Netinstall will only function with one active interface on your computer. It's strongly recommended to deactivate any other network interfaces to ensure Netinstall selects the correct one.
Configure a static IP address for your Ethernet interface, openStart,and selectSettings:
Make sure that the Ethernet interface is running and launch Netinstall.exe. If you followed the guide precisely, then you should not have any Internet connection on your computer, Windows 10 wants to verify all apps that it runs, but will not be able to do it since lack of an Internet connection, for this reason, a warning might pop up, you should clickRun.
If the installation does not start (progress bar is not moving or no status is shown), then you can try closing the Netinstall application and opening it up again or try to put the device intoEtherbootmode again. If you are still unable to get Netinstall working, then you should try using it on a different computer since there might be an operating system's issue that is preventing Netinstall from working properly.
After using Netinstall the device will be reset to defaults (unless you specified not to apply default configuration). Some devices are not accessible throughether1port with the default configuration for security reasons. Read more aboutDefault configuration.
Option"Keep branding"allows you to retain the device's already installed branding package without reinstalling it using Netinstall.
# Instructions for Linux
The Linux version is a command line tool, which offers nearly the same parameters as the Windows counterpart.
Download the tool from our download page (links not literal):
```
wget https://download.mikrotik.com/routeros/[VERSION]/netinstall-[VERSION].tar.gz
```
Extract it:
```
tar -xzf netinstall-[VERSION].tar.gz
```
Run the tool:
```
sudo ./netinstall-cli [-parameters] [address/interface] routeros-arm64-[package VERSION].npk
```
The available parameters are as follows:
Parameter | Meaning
-------------------
-r | When the reinstallation process is performed, the current configuration will be reset, and for devices that have it, the default configuration will be applied (optional).
-e | Performing the reinstallation process will reset the device to an empty configuration.
-b | Option to discard the currently installed branding package from the device, otherwise it will be reinstalled together with RouterOS.
-o | When using the netinstall tool with the "-o" option, devices can only be installed once per netinstall run. This means that during the netinstall process, the tool will keep track of the MAC addresses of devices that were successfully installed. If a device with the same MAC address tries to reinstall during the same run, the tool will ignore it and not respond to its bootp requests.
-k keyfile | Provides the device with a license key in .KEY format (optional).
-s userscript | Pre-configures the device with the provided configuration (text file in .RSC format). This configuration also takes place of the default configuration. The script can access factory passwords with read-only variables $defconfPassword and $defconfWifiPassword (starting from RouterOS 7.10beta8)(optional).
-a IP | Uses a specific IP address that the Netinstall server will assign to the device. Mandatory, but can be auto-assigned if interface parameter used.
PACKAGE | Specify a list of RouterOS.NPK format packages that Netinstall will try to install on the device (mandatory).The system package must be listed first.
-i | Allows you to specify an interface (optional).
When the reinstallation process is performed, the current configuration will be reset, and for devices that have it, the default configuration will be applied (optional).
Performing the reinstallation process will reset the device to an empty configuration.
Option to discard the currently installed branding package from the device, otherwise it will be reinstalled together with RouterOS.
When using the netinstall tool with the "-o" option, devices can only be installed once per netinstall run. This means that during the netinstall process, the tool will keep track of the MAC addresses of devices that were successfully installed. If a device with the same MAC address tries to reinstall during the same run, the tool will ignore it and not respond to its bootp requests.
-a IP
Uses a specific IP address that the Netinstall server will assign to the device. Mandatory, but can be auto-assigned if interface parameter used.
Allows you to specify an interface (optional).
First make sure you have set the IP on your computer's interface:
```
admin@ubuntu:~$ sudo ifconfig <interface> 192.168.88.2/24
```
Then run theNetinstallversion 6 (an example thatresets the configuration upon reinstallation procedure):
```
admin@ubuntu:~$ sudo ./netinstall -r -a 192.168.88.3 routeros-mipsbe-6.48.1.npk
Using server IP: 192.168.88.2
Starting PXE server
Waiting for RouterBOARD...
PXE client: 01:23:45:67:89:10
Sending image: mips
Discovered RouterBOARD...
Formatting...
Sending package routeros-mipsbe-6.48.1.npk ...
Ready for reboot...
Sent reboot command
```
Or run theNetinstallversion 7 (an examplethat applies an empty configuration and discards the branding during the reinstallation procedure):
```
admin@ubuntu:~$ sudo ./netinstall-cli -e -b -i enx1234567ee890 -a 192.168.88.3 routeros-7.14.2-arm.npk wireless-7.14.2-arm.npk
Version: 7.15beta9(2024-03-27 20:41:15)
Will apply empty config
Will remove branding
Using Interface: enx1234567ee890
Wait for Link-UP on 'enx1234567ee890'. OK
Using Client IP: 192.168.88.3
Using Server IP: 192.168.88.10
Starting PXE server
Waiting for RouterBOARD...
client: 74:4D:28:8E:86:74
Detected client architecture: arm
Sending and starting Netinstall boot image ...
Installed branding package detected
Discovered RouterBOARD... 74:4D:28:8E:86:74
Formatting...
Sending package routeros-7.14.2-arm.npk ...
Sending package wireless-7.14.2-arm.npk ...
Sending empty config ...
Ready for reboot...
Sent reboot command
```
# Etherboot
Etherboot mode is a special state for a MikroTik device that allows you to reinstall your device usingNetinstall.There are two types of booters available for use: the regular booter and the backup booter. It's essential to verify both options.
# Reset button
TheResetcan be found on all MikroTik devices, this button can be used to put the device into Etherboot mode.An easy way to put a device into Etherboot mode using theResetbutton is by powering off the device, hold theResetbutton, power on the device while holding theResetbutton and keep holding it until the device shows up in yourNetinstalllwindow.
# RouterOS
```
/system routerboard settings set boot-device=try-ethernet-once-then-nand
```
After that either reboot the device or do a power cycle on the device. Next time the device will boot up, then it will first try going into Etherboot mode. Note that after the first boot up, the device will not try going into Etherboot mode and will boot directly from NAND or from the storage type the device is using.
# Serial console
Some devices come with a serial console that can be used to put the device into Etherboot mode. To do so, make sure you configure your computer's serial console. The required parameters for all MikroTik devices (except for RouterBOARD 230 series) are as following:
```
115200bit/s, 8 data bits, 1 stop bit, no parity, flow control=none by default.
```
For RouterBOARD 230 series devices the parameters are as following:
```
9600bit/s, 8 data bits, 1 stop bit, no parity, hardware (RTS/CTS) flow control by default.
```
Make sure you are using a proper null modem cable, you can find the proper pinouthere. When the device is booting up, keep pressingCTRL+Eon your keyboard until the device shows that it istrying bootp protocol:
```
RouterBOOT booter 7.14.2
CRS328-4C-20S-4S+
CPU frequency: 800 MHz
Memory size: 512 MiB
Storage size:  16 MiB
Press Ctrl+E to enter etherboot mode
Press any key within 2 seconds to enter setup
trying bootp protocol.... OK
Got IP address: 192.168.88.3
resolved mac address 84:69:93:9E:E6:49
transfer started ............................... transfer ok, time=2.00s
```
At this point your device is in Etherboot mode, now the device should show up in your Netinstall window.