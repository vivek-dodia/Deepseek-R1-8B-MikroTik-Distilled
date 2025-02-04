# Document Information
Title: Fail-over PtP GUI example
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/43843592/Fail-over+PtP+GUI+example,

# Content
# Summary
This example shows how to configure automatic fail-over (bonding) 5Ghz link in combination with 60Ghz devices in GUI.When a connection between 60Ghz wireless is lost, it will automatically use the bonded interface.Example is done from empty configuration state with [WinBox] utility
# Connect to the device
After configuration reset - only mac-telnet is possible. In main WinBox screen press on Neighbours, choose your devices MAC address and press Connect:
# Configure bridge
Add new bridge.
Later in the instructions it requires to assign bridge members to it. This will allow to pass traffic from Ethernet to W60G interface without routing.
# Set up 60Ghz wireless connection
All previously explained steps are identical tobridgeandstationdevices. Different modes needs to be used when configuring wireless interfaces.
Configurebridgedevice as follows:
Configurestationdevice as follows:
# Set up 5Ghz wireless connection
Choose Security Profile for your devices -
For bridge device -
For station device -
If everything is done correctly - running (R) flags should appear as shown in the screenshot -
# Configure bonding
Configure bonding and assign slave interfaces in this setup it is selected as built in wlan1 interface, but it can be also ether interface in other kind of setups.
For bridge device -
For station device -
# Configure bridge
Configuring bridge settings including the bonding interface is mandatory for the active-backup to work on used devices ( In this case bridge and station devices settings are the same ).
# Additional configuration
Interfaces when enabled from greyed out will become active.
Link should be established after all previously explained steps are done. It's recommended to set up administrator password on both devices.