---
title: Fail-over PtP GUI example
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/43843592/Fail-over+PtP+GUI+example,
crawled_date: 2025-02-02T21:13:40.105309
section: mikrotik_docs
type: documentation
---

## Summary
This example shows how to configure automatic fail-over (bonding) 5Ghz link in combination with 60Ghz devices in GUI.When a connection between 60Ghz wireless is lost, it will automatically use the bonded interface.Example is done from empty configuration state with [WinBox] utility
## Connect to the device
After configuration reset - only mac-telnet is possible. In main WinBox screen press on Neighbours, choose your devices MAC address and press Connect:
* Select correct deviceMAC Address;
* Login by default is "admin" and no password is set;
* PressConnect.
## Configure bridge
Add new bridge.
* Open Bridge sub-menu;
* Press on "+" to add new bridge;
* Apply your changes.
Later in the instructions it requires to assign bridge members to it. This will allow to pass traffic from Ethernet to W60G interface without routing.
## Set up 60Ghz wireless connection
All previously explained steps are identical tobridgeandstationdevices. Different modes needs to be used when configuring wireless interfaces.
Configurebridgedevice as follows:
* Open Interface menu;
* Double click on wlan60-1 interface;
* Press on Wireless sub-menu and set mode tobridge (orap-bridgefor PtmP);
* Set SSID and password and region;
* Select previously created bridge under "Put Stations In Bridge";
* Apply your changes;
* Press enable to start transmitting.
Configurestationdevice as follows:
* Open Interface menu;
* Double click on wlan60-1 interface;
* Press on Wireless sub-menu and set mode tostation bridge;
* Set SSID and password;
* Apply your changes;
* Press enable to start transmitting.
## Set up 5Ghz wireless connection
Choose Security Profile for your devices -
* ChooseWirelessmenu
* ChooseSecurity Profilessub-menu
* Add new profile with "+" sign
* Choosename,mode,authentication typeand a secure password.
* Applythe configuration.
For bridge device -
* OpenInterfacesmenu;
* Double click onwlan1interface;
* Press onWirelesssub-menu and set mode tobridge(orap-bridgefor PtmP);
* SetSSID,passwordandcountry.
* Press onAdvanced Mode.
* Choose yourSecurity Profile;
* Applyyour changes;
* Pressenableto start transmitting.
For station device -
* OpenInterfacesmenu;
* Double click onwlan1interface;
* Press onWirelesssub-menu and set mode tostation-bridge;
* SetSSID,passwordandcountry;
* Press onadvancedmode ( similar to bridge device* );
* ChooseSecurity Profile;
* Applyyour changes;
* Pressenableto start transmitting.
If everything is done correctly - running (R) flags should appear as shown in the screenshot -
## Configure bonding
Configure bonding and assign slave interfaces in this setup it is selected as built in wlan1 interface, but it can be also ether interface in other kind of setups.
For bridge device -
* Press onBondingsub-menu;
* Add new member with "+";
* Add interface members (wlan1andwlan60-station-1) tobondinginterface asSlaves;
* Add interface memberwlan60-station-1asPrimaryinterface;
* Choose Mode asactive backup;
* Applyconfiguration.
For station device -
* Press onBondingsub-menu;
* Add new member with "+";
* Add interface members (wlan1andwlan60-1) tobondinginterface asSlaves;
* Add interface memberwlan60-1asPrimaryinterface;
* Choose Mode asactive backup;
* Applyconfiguration.
## Configure bridge
Configuring bridge settings including the bonding interface is mandatory for the active-backup to work on used devices ( In this case bridge and station devices settings are the same ).
* Press onBridgesub-menu;
* Add new member with "+";
* Add interface member asether1and Bridge member asbridge1;
* Applyconfiguration.
* Press onBridgesub-menu;
* Add new member with "+";
* Add interface member asbonding1and Bridge member asbridge1;
* Applyconfiguration.
## Additional configuration
Interfaces when enabled from greyed out will become active.
Link should be established after all previously explained steps are done. It's recommended to set up administrator password on both devices.