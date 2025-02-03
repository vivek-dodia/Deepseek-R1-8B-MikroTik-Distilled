---
title: RouterBOARD
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/40992878/RouterBOARD,
crawled_date: 2025-02-02T21:14:45.410818
section: mikrotik_docs
type: documentation
---

* 1Introduction
* 2Properties
* 3Upgrading RouterBOOT
* 4Settings4.1Preboot etherboot4.2Protected bootloader4.3Mode and Reset buttons
* 4.1Preboot etherboot
* 4.2Protected bootloader
* 4.3Mode and Reset buttons
# Introduction
On RouterBOARD devices, the following menu exists which gives you some basic information about your device:
```
[admin@demo.mt.lv] /system routerboard> print 
       routerboard: yes
             model: 1200
     serial-number: 3B5E02741BF0
     firmware-type: amcc460
  factory-firmware: 2.38
  current-firmware: 7.1beta3
  upgrade-firmware: 7.2
```
# Properties
Read-only properties:
Property | Description
----------------------
current-firmware(string) | The version of the RouterBOOT loader is currently in use. Not to be confused with RouterOS operating system version.
factory-firmware(string) | The version of the RouterBOOT loader the particular device was manufactured with.
firmware-type(string) | Firmware type that is used on the particular device.
model(string) | Describes the model name.
routerboard(yes | no) | Whether this is a MikroTik RouterBOARD device.
serial-number(string) | The serial number of this particular device.
upgrade-firmware(string) | RouterOS upgrades also include new RouterBOOT version files, but they have to be applied manually. This line shows if a new RouterBOOT file has been found in the device. The file can either be included via a recent RouterOS upgrade or an FWF file that has been manually uploaded to the router. In either case, the newest found version will be shown here.
# Upgrading RouterBOOT
RouterBOOT upgrades usually include minor improvements to overall RouterBOARD operation. It is recommended to keep this version upgraded. If you see that theupgrade-firmwarevalue is bigger thancurrent firmware, you simply need to perform theupgradecommand, accept it withyand then reboot with/system reboot
```
[admin@mikrotik] /system routerboard> upgrade 
Do you really want to upgrade firmware? [y/n] 
y
echo: system,info,critical Firmware upgraded successfully, please reboot for changes to take effect!
```
After rebooting, thecurrent-firmwarevalue should become identical withupgrade-firmware
# Settings
Sub-menu level:/system routerboard settings
```
/system routerboard settings
```
```
[admin@MikroTik] /system/routerboard/settings> print 
              auto-upgrade: no
                 baud-rate: 115200
                boot-delay: 2s
            enter-setup-on: any-key
               boot-device: nand-if-fail-then-ethernet
         preboot-etherboot: disabled
             cpu-frequency: 1200MHz
          memory-frequency: 1066DDR
             boot-protocol: bootp
       enable-jumper-reset: yes
       force-backup-booter: no
               silent-boot: yes
      protected-routerboot: disabled
      reformat-hold-button: 20s
  reformat-hold-button-max: 10m
```
Property | Description
----------------------
auto-upgrade(yes | no; Default:no) | Whether to upgrade firmware automatically after RouterOS upgrade. The latest firmware will be applied after an additional reboot
baud-rate(integer; Default:115200) | Choose the onboard RS232 speed in bits per second (if installed)
boot-delay(time; Default:2s) | How much time does to wait for a keystroke while booting
boot-device(nand-if-fail-then-ethernet ...; Default:nand-if-fail-then-ethernet) | Choose the way RouterBOOT loads the operating system:ethernet - boot the device inEtherbootmode;flash-boot-Flashfig mode on startup is enabled. This setting will revert to NAND after a successful configuration change OR once any user logs into the board.flash-boot-once-then-nand- Flashfig mode on startup is enabled for a single boot only, resets to nand-if-fail-then-ethernet after that.nand-if-fail-then-ethernet - boot RouterOS from the NAND, if RouterOS is not booting -it goes to Etherboot automatically. This is the default mode for devices straight out of the box;nand-only - boot RouterOS from the NAND;try-ethernet-once-then-nand- boot device in Etherboot mode once and if no server is available - it will boot directly from the NAND or of the storage type the device is using.
boot-os(router-os |swos; Default:router-os) | Changes the bootingoperating systemfor CRS3xx series switches
boot-protocol(bootp |dhcp ...; Default:bootp) | Boot protocol to use:bootp- the default option for booting RouterOSdhcp- used for OpenWRT and possibly other OS
cpu-frequency(depends on model; Default:depends on model) | This option allows for changing the CPU frequency of the device. Values depend on the model, to see available options, hit the [?] button in RouterOS version 6 or the [F1] button inRouterOSversion 7on the keyboard at this prompt
cpu-mode(power-save | regular; Default:power-save) | Whether to enter CPU suspend mode in HTL instruction. Most OSs use HLT instruction during the CPU idle cycle. When the CPU is in suspend mode, it consumes less power, but in low-temperature conditions, it is recommended to choose a regular mode, so that the overall system temperature would be higher
enable-jumper-reset(yes | no; Default:yes) | Disable this to avoid accidental setting reset via the onboard jumper
enter-setup-on(any-key | delete-key; Default:delete-key) | Which key will cause the BIOS to enter configuration mode during boot delay. Useful when the serial console prints out symbols during the boot process and goes into RouterBOOT menu by itself. Note that in some serial terminal programs, it is impossible to use the Delete key to enter the setup - in this case, it might be possible to do this with the Backspace key
force-backup-booter(yes | no; Default:no) | If to use the backup RouterBOOT. This is only useful if the main loader has become corrupted somehow and cannot be fixed. So that you don't have to boot the device with a pushed reset button (which loads the backup loader), you can use this setting to load it every timeyes- backup loader will be used alwaysno- main booter will be used
init-delay(timeout interval 0s..9s; Default:) | Used for mPCIe modems with RB9xx series devices onlyIn case your modem is not being recognized after a soft reboot, then you might need to add a delay before the USB port is initialized
memory-frequency(depends on model; Default:depends on model) | This option allows changing the memory frequency of the device. Values depend on the model, to see available options, hit the [?] button in RouterOS version 6 or the [F1] button inRouterOSversion 7button on the keyboard at this prompt
memory-data-rate(depends on the model; Default:depends on model) | This option allows changing the memory data rate of the device. Values depend on the model, to see available options, hit the [?] button in RouterOS version 6 or the [F1] button inRouterOSversion 7button on the keyboard at this prompt
preboot-etherboot(timeout interval 1s..30s; Default:disabled) | Enablespreboot etherboot, which runs before the regular boot device. It works the same asboot-device=etherboot, but has an additional timeout value. If an IP address is not received from the Netinstall server before the timeout expires, the regular booting process will start.
preboot-etherboot-server(IP address, any: Default:any) | Setspreboot-etherbootto accept IP address only from the specified Netinstall server IP address. By enabling this feature, unintentional etherboot from other BOOTP/DHCP servers can be prevented.
regulatory-domain-ce(yes | no; Default:no) | Enables extra-low TX power for high antenna gain devices (requires a reboot)
silent-boot(yes | no; Default:no) | This option disables output on the serial console and beeping sounds during booting, to avoid the text output interrupting a connected device. Useful if you have some temperature monitor or modem connected to the serial portyes- no output on the serial console and no booting beeps (does not disable the RouterOS: beep command)no- regular info and options menu on a serial console
* ethernet - boot the device inEtherbootmode;
* flash-boot-Flashfig mode on startup is enabled. This setting will revert to NAND after a successful configuration change OR once any user logs into the board.
* flash-boot-once-then-nand- Flashfig mode on startup is enabled for a single boot only, resets to nand-if-fail-then-ethernet after that.
* nand-if-fail-then-ethernet - boot RouterOS from the NAND, if RouterOS is not booting -it goes to Etherboot automatically. This is the default mode for devices straight out of the box;
* nand-only - boot RouterOS from the NAND;
* try-ethernet-once-then-nand- boot device in Etherboot mode once and if no server is available - it will boot directly from the NAND or of the storage type the device is using.
* bootp- the default option for booting RouterOS
* dhcp- used for OpenWRT and possibly other OS
Which key will cause the BIOS to enter configuration mode during boot delay. Useful when the serial console prints out symbols during the boot process and goes into RouterBOOT menu by itself. Note that in some serial terminal programs, it is impossible to use the Delete key to enter the setup - in this case, it might be possible to do this with the Backspace key
* yes- backup loader will be used always
* no- main booter will be used
Used for mPCIe modems with RB9xx series devices only
In case your modem is not being recognized after a soft reboot, then you might need to add a delay before the USB port is initialized
Enablespreboot etherboot, which runs before the regular boot device. It works the same asboot-device=etherboot, but has an additional timeout value. If an IP address is not received from the Netinstall server before the timeout expires, the regular booting process will start.
* yes- no output on the serial console and no booting beeps (does not disable the RouterOS: beep command)
* no- regular info and options menu on a serial console
## Preboot etherboot
preboot-etherbootis a feature that instructs RouterOS device to search for a Netinstall server on every boot for specified amount of time, before starting the regular booting process (e.g., RouterOS). This feature is particularly useful for remote reinstall, as it allows the device to attempt etherboot on every startup.
preboot-etherboot-serverspecifies that thepreboot-etherbootbooter should look only for a Netinstall server with a specific IP address. Since by default, etherboot accepts address from any BOOTP/DHCP server,  with this feature, you can specify to accept the address only from a particular Netinstall server, meaning that the device can be reinstalled without removing it from the network.
With both features enabled, any device can be reinstalled remotely without accessing RouterOS or holding the reset button. One example of starting a remote reinstall process would be to simply power cycle RouterOS device from a PoE switch or another power controller. After installation, disable your Netinstall server and simply power cycle the installed device.
To enablepreboot-etherbootandpreboot-etherboot-server:
1) Install RouterOS version 7.9+2) Upgrade RouterBOOT with "/system routerboard upgrade"3) Reboot
The feature can be set with command:
```
system/routerboard/settings/set preboot-etherboot=9s preboot-etherboot-server=10.155.115.199
```
On every next reboot/power cycle, this device will try to receive IP address from Netinstall server with IP 10.155.115.199, for 9 seconds. If there will be no such server, regular boot process will start.
## Protected bootloader
The feature allows the protection of RouterOS configuration and files from a physical attacker by disabling etherboot. It is called "Protected RouterBOOT". This feature can be enabled and disabled only from within RouterOS after login, i.e., there is no RouterBOOT setting to enable/disable this feature. These extra options appear only under certain conditions. When this setting is enabled - both the reset button and the reset pin-hole are disabled. RouterBOOT menu is also disabled. The only ability to change boot mode or enable the RouterBOOT settings menu is through RouterOS. If you do not know the RouterOS password - only a complete format is possible.
A special package is provided to upgrade the backup RouterBOOT (DANGEROUS). Newer devices will have this new backup loader already installed at the factory. If your RouterOS isv7, yourfactory-firmwareversion is lower than7.6and your device displays the message →The "protected routerboot" feature requires a backup-routerboot upgrade← when trying to enable the feature, do the following:a) upgrade or downgrade the device specifically to the7.6release (from ourdownload pageorarchive).b) upgrade your current RouterBOOT version with "/system routerboard upgrade" then reboot the device, so that the RouterBOOT version (current-firmwareversion when checking "/system routerboard print") is the same as the firmware version ("/system resource print") installed, which should be 7.6.c) drag and drop thev7 universal package for all architecturesinto the device's file system then reboot the device again. This will make yourfactory-firmwareversion 7.6, where you are allowed to enable the feature. After this step, you can upgrade the device to a newer release.If your RouterOS version isv6and you get the same prompt, follow the same steps mentioned above, but only update/downgrade/compare your device version to specifically6.49.7instead and usev6 universal package for all architectures.
For example, when setting protected-routeboard enabled, you will be given 60 seconds to confirm by pressing the reset button, otherwise, this setting won't be enabled.
```
[admin@450] > system/routerboard/settings/set protected-routerboot=enabled 
[admin@450] > system/routerboard/settings/print 
                        ;;; press button within 60 seconds to confirm 
                            protected routerboot enable
              auto-upgrade: no
                 baud-rate: 115200
                boot-delay: 2s
            enter-setup-on: any-key
               boot-device: nand-if-fail-then-ethernet
             cpu-frequency: auto
             boot-protocol: bootp
       enable-jumper-reset: yes
       force-backup-booter: no
               silent-boot: yes
      protected-routerboot: enabled
      reformat-hold-button: 20s
  reformat-hold-button-max: 10m
```
Property | Description
----------------------
protected-routerboot(enabled | disabled; Default:disabled) | This setting disables any access to the RouterBOOT configuration settings over a console cable and disables the operation of the reset button to change the boot mode (Netinstall will be disabled). Access to RouterOS will only be possible with a known RouterOS admin password. Unsetting of this option is only possible from RouterOS. If you forget the RouterOS password, the only option is to perform a complete reformat of both NAND and RAM with the following method, but youhaveto know the reset button hold time in seconds.enabled- secure mode, only RouterOS can be accessed with a RouterOS admin password. Any user input from the serial port is ignored. Etherboot is not available, RouterBOOT setting change is not possible.disabled- regular operation, RouterBOOT settings available with serial console and reset button can be used to launch Netinstall
reformat-hold-button(5s .. 300s; Default:20s) | As an emergency recovery option, it is possible to reset everything by pressing the button at power-on for longer than reformat-hold-button time, but less than reformat-hold-button-max (new in RouterBOOT 3.38.3).When you use the button for a complete reset, the following actions are taken:EXTREMELY DANGEROUS. Use this only if you have lost all access to the device.RouterOS, all of its files and configuration is completely and irreversibly erased by nand re-format;All RouterBOOT settings are reset to defaults;Board is rebooted;As boot from NAND fails, it goes to etherboot automatically;Netinstall is required to reinstall RouterOS.Please note!Reformat on some RouterBOARDS can take more than 5 minutes. After formatting the board will be ready for Netinstall.
reformat-hold-button-max(15s .. 600s; Default:10m) | Increase the security even further by setting the max hold time, this means that you must release the reset button within a specified time interval. If you set the "reformat-hold-button" to 60s and "reformat-hold-button-max" to 65s, it will mean that you must hold the button 60 to 65 seconds, not less and not more, making guesses impossible. Introduced in RouterBOOT 3.38.3
* enabled- secure mode, only RouterOS can be accessed with a RouterOS admin password. Any user input from the serial port is ignored. Etherboot is not available, RouterBOOT setting change is not possible.
* disabled- regular operation, RouterBOOT settings available with serial console and reset button can be used to launch Netinstall
When you use the button for a complete reset, the following actions are taken:
```
EXTREMELY DANGEROUS. Use this only if you have lost all access to the device.
```
* RouterOS, all of its files and configuration is completely and irreversibly erased by nand re-format;
* All RouterBOOT settings are reset to defaults;
* Board is rebooted;
* As boot from NAND fails, it goes to etherboot automatically;
* Netinstall is required to reinstall RouterOS.
## Mode and Reset buttons
Reset button additional functionality is supported by all MikroTik devices running RouterOS
Some RouterBOARD devices have a mode button that allows you to run any script when the button it pushed.
The list of supported devices:
* RBcAP-2nD (cAP)
* RBcAPGi-5acD2nD (cAP ac)
* RBwsAP5Hac2nD (wsAP ac lite)
* RB750Gr3 (hEX)
* RB760iGS (hEX S)
* RB912R-2nD (LtAP mini, LtAP mini LTE/4G kit)
* RBD52G-5HacD2HnD (hAP ac^2)
* RBLHGR (LHG LTE/4G kit)
* RBSXTR (SXT LTE/4G kit)
* CRS328-4C-20S-4S+RM
* CRS328-24P-4S+RM
* CCR1016-12G r2
* CCR1016-12S-1S+ r2
* CCR1036-12G-4S r2
* CCR1036-8G-2S+ r2
* RBD53G-5HacD2HnD (Chateau)
* RBD53GR-5HacD2HnD (hAP ac^3)
Property | Description
----------------------
enabled(no | yes; Default:no) | Disable or enable the operation of the button
hold-time(time interval Min..Max; Default: ) | HoldTime:= Button functionality can be called if a button is pressed for a certain period of time:Min..Max: Min -- 0s..1m (time interval), Max -- 0s..1m (time interval) (available only starting from RouterOS 6.47beta60)
on-event(string; Default: ) | Name of the script that will be run upon pressing the button. The script must be defined and named in the "/system scripts" menu
Example for mode button:
```
/system script add name=test-mode-button source={:log info message=("mode button pressed");}
/system routerboard mode-button set on-event=test-mode-button enabled=yes
```
Upon pressing the button, the message"mode button pressed"will be logged in the system log.
Examples for RouterOS version newer than 6.47:
```
/system script add name=test-mode-button source={:log info message=("mode button pressed");} 
/system routerboard mode-button set on-event=test-mode-button hold-time=3..5 enabled=yes
```
The reset button works in the same way, but the menu is moved underthe :/system routerboard reset-button:
```
/system routerboard reset-button
```
```
/system script add name=test-reset-button source={:log info message=("reset button pressed");} 
/system routerboard reset-button set on-event=test-reset-button hold-time=0..10 enabled=yes
```
LED dark modecontrol with the mode button:
```
/system script add name=dark-mode source={
   :if ([system leds settings get all-leds-off] = "never") do={
      /system leds settings set all-leds-off=immediate 
   } else={
        /system leds settings set all-leds-off=never
   }
 }
/system routerboard mode-button set enabled=yes on-event=dark-mode
```
The C53, S53 and cAP ax series RouterBoards have configurable WPS button. It also works in the same way as reset button and mode button and executes a script.
```
/system script add name=test-wps-button source={:log info message=("wps button pressed");}
/system routerboard wps-button set on-event=test-wps-button hold-time=0..10 enabled=yes
```
WPS accept control with the WPS button:
```
/system script add name=wps-accept source={
    :foreach iface in=[/interface/wifiwave2 find where configuration.mode="ap"] do={
        /interface/wifiwave2 wps-push-button $iface
    }
}
/system routerboard wps-button set enabled=yes on-event=wps-accept
```