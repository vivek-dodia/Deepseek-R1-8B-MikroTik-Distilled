---
title: FlashFig
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/139526145/FlashFig,
crawled_date: 2025-02-02T21:09:34.410637
section: mikrotik_docs
type: documentation
---

* 1Description
* 2FlashFig Example2.1Requirements2.2Pre-Configuration2.2.1Windows Computer2.2.3RouterBOARD2.3Connect2.4Run FlashFig
* 3Troubleshoot3.1FlashFig can not find a router3.2FlashFig finds a router, flashing is not done (no TFTP request)3.3FlashFig is done, but a configuration is not applied3.4Not enough flash space, ignoring
* 2.1Requirements
* 2.2Pre-Configuration2.2.1Windows Computer2.2.3RouterBOARD
* 2.3Connect
* 2.4Run FlashFig
* 2.2.1Windows Computer
* 2.2.3RouterBOARD
* 3.1FlashFig can not find a router
* 3.2FlashFig finds a router, flashing is not done (no TFTP request)
* 3.3FlashFig is done, but a configuration is not applied
* 3.4Not enough flash space, ignoring
## Description
FlashFig is an application for mass router configuration. It can be used by MikroTik distributors, ISPs, or any other companies who need to apply RouterOS configuration to many routers in the shortest possible time.
FlashFig applies MikroTik RouterOSconfigurationto any RouterBOARD within3 seconds. You can perform FlashFig on a batch of routers, the only thing you need is toconnectRouterBOARD to a Layer 2 network running FlashFig and topowera FlashFig-enabled RouterBOARD up.
FlashFig only runs on a Windows computer and is available from thedownloadspage.
All RouterBOARDs support FlashFig mode. It works between a Windows computer runningFlashFig and a RouterBOARD in the same broadcast domain (direct Layer 2 Ethernet network connection is required).
FlashFig support is enabled on every new RouterBOARD manufactured since March 2010 by default from the factory. For older models, FlashFig can be enabled via RouterBOOT or from MikroTik RouterOS console -/system routerboard settings set boot-device=flash-boot-once-then-nandor/system routerboard settings set boot-device=flash-boot.
FlashFig mode on a brand new RouterBOARD is disabled on further boots only after the first successful user login or successful FlashFig attempt to avoid unwanted reconfiguration at a later time. To use FlashFig a second time on the same router, you need to enableflash-bootinBootloadersettings (this setting will revert to NAND after a successful configuration change OR once any user logs into the board).
If RouterOSreset-configurationcommand is used later (or configuration reset using the Reset button), FlashFig configuration is loaded. To permanently overwrite, use the Netinstall process and checkApply default configurationor use-rflag in Linux-based command line.
You view FlashFigvideo tutorialon MikroTik YouTube channel.
## FlashFig Example
This is a step-by-step example of how to use the FlashFig process to apply a chosen MikroTik RouterOS configuration to a 'factory fresh' RouterBOARD.
#### Requirements
The Windows computer must be equipped with the following ports and contain the following files:
* A working Ethernet port;
* Valid .rsc file(s) with MikroTik RouterOS configuration similar to an export/import file. In addition to regular configuration commands, it is also possible to re-apply the factory passwords by using the read-only variables$defconfPasswordand$defconfWifiPassword(starting from RouterOS 7.10beta8);
* Always use the latest FlashFig program available from thedownloadspage;
* The RouterBOARD has to be in flash-boot mode, if this is the very first boot, nothing needs to be done
#### Pre-Configuration
##### Windows Computer
* Run FlashFig;
* Prepare.rscfile,.rscfile is regular/import file, it accepts valid MikroTik RouterOS CLI commands. You can create .rsc file with any text editor program (Notepad, Notepad++, Texteditor, TextEdit, Microsoft Word, OpenOffice Writer)
* AssignBoot Client Address, which should be an address withinthe same subnet as that configured on the computer's Ethernet interface,
* Browsefor.rscMikroTik RouterOS configuration file to apply to the RouterBOARD, highlight the file andSelectto approve it,
* Activate FlashFig server, now it is ready to FlashFig. Note, any RouterBOARD will be FlashFig'ed within the network when they are powered on with boot-device configured toflash-bootorflash-boot-once-then-nand,
##### RouterBOARD
* FlashFig mode is enabled on every RouterBOARD from the factory by default, which meansno configurationis required on RouterBOARD.
* If FlashFig is not enabled on your router, access the RouterBOARD with WinBox/Console and change theboot-devicetoflash-bootorflash-boot-once-then-nand:
```
system/routerboard/settings/set boot-device=flash-boot
```
Or use a more preferable option, for a single boot flash-boot:
```
system/routerboard/settings/set boot-device=flash-boot-once-then-nand
```
Your router is now ready for FlashFig.
#### Connect
Connect theBootport of RouterBOARD and FlashFig computer to the same Local Area Network.
#### Run FlashFig
* Plug-in power for RouterBOARD
* Check the status on FlashFig program,
Messages log shows "FlashFigged" and RouterBOARD should repeatedly make the morse code sound for the character "/" ("_.._." and flash the LED - it is now safe to unplug / power down the router.
* FlashFigconfigurationwas applied to the RouterBOARD and it isreadyto be used in production with this new config.
## Troubleshoot
### FlashFig can not find a router
If between a PC and a router there is another device (a router/switch), ensure that for this device:
* DHCP server is disabled;
* if used ports are in a bridge, set bridgeprotocol-modetonone;
* HW-offload for used ports is disabled.
### FlashFigfinds a router, flashing is not done (no TFTP request)
Ensure that the computer on which FlashFig is running has only one network interface active.
### FlashFig is done, but a configuration is not applied
If all procedures went successfully, but RouterOS configuration from .rsc file is not applied, addstartup delayto *.rsc configuration file. The reason might be, that the configuration script is executed before all interfaces boots up.
### Not enough flash space, ignoring
FlashFig configuration maximum file size is up to 4000 bytes, otherwise program will return an error as above.