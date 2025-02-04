# Document Information
Title: FlashFig
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/139526145/FlashFig,

# Content
# Description
FlashFig is an application for mass router configuration. It can be used by MikroTik distributors, ISPs, or any other companies who need to apply RouterOS configuration to many routers in the shortest possible time.
FlashFig applies MikroTik RouterOSconfigurationto any RouterBOARD within3 seconds. You can perform FlashFig on a batch of routers, the only thing you need is toconnectRouterBOARD to a Layer 2 network running FlashFig and topowera FlashFig-enabled RouterBOARD up.
FlashFig only runs on a Windows computer and is available from thedownloadspage.
All RouterBOARDs support FlashFig mode. It works between a Windows computer runningFlashFig and a RouterBOARD in the same broadcast domain (direct Layer 2 Ethernet network connection is required).
FlashFig support is enabled on every new RouterBOARD manufactured since March 2010 by default from the factory. For older models, FlashFig can be enabled via RouterBOOT or from MikroTik RouterOS console -/system routerboard settings set boot-device=flash-boot-once-then-nandor/system routerboard settings set boot-device=flash-boot.
FlashFig mode on a brand new RouterBOARD is disabled on further boots only after the first successful user login or successful FlashFig attempt to avoid unwanted reconfiguration at a later time. To use FlashFig a second time on the same router, you need to enableflash-bootinBootloadersettings (this setting will revert to NAND after a successful configuration change OR once any user logs into the board).
If RouterOSreset-configurationcommand is used later (or configuration reset using the Reset button), FlashFig configuration is loaded. To permanently overwrite, use the Netinstall process and checkApply default configurationor use-rflag in Linux-based command line.
You view FlashFigvideo tutorialon MikroTik YouTube channel.
# FlashFig Example
This is a step-by-step example of how to use the FlashFig process to apply a chosen MikroTik RouterOS configuration to a 'factory fresh' RouterBOARD.
# Requirements
The Windows computer must be equipped with the following ports and contain the following files:
# Pre-Configuration
# Windows Computer
# RouterBOARD
```
system/routerboard/settings/set boot-device=flash-boot
```
Or use a more preferable option, for a single boot flash-boot:
```
system/routerboard/settings/set boot-device=flash-boot-once-then-nand
```
Your router is now ready for FlashFig.
# Connect
Connect theBootport of RouterBOARD and FlashFig computer to the same Local Area Network.
# Run FlashFig
Messages log shows "FlashFigged" and RouterBOARD should repeatedly make the morse code sound for the character "/" ("_.._." and flash the LED - it is now safe to unplug / power down the router.
# Troubleshoot
# FlashFig can not find a router
If between a PC and a router there is another device (a router/switch), ensure that for this device:
# FlashFigfinds a router, flashing is not done (no TFTP request)
Ensure that the computer on which FlashFig is running has only one network interface active.
# FlashFig is done, but a configuration is not applied
If all procedures went successfully, but RouterOS configuration from .rsc file is not applied, addstartup delayto *.rsc configuration file. The reason might be, that the configuration script is executed before all interfaces boots up.
# Not enough flash space, ignoring
FlashFig configuration maximum file size is up to 4000 bytes, otherwise program will return an error as above.