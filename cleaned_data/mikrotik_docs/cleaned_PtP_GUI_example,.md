# Document Information
Title: PtP GUI example
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/39682067/PtP+GUI+example,

# Content
# Summary
This example shows how to configure transparent wireless bridge in GUI from one W60G device to another.
Example is done from empty configuration state with [WinBox] utility
# Connect to the device
After configuration reset - only mac-telnet is possible. In main WinBox screen press on Neighbours, choose your devices MAC address and press Connect:
# Configure bridge
Add new bridge and assign bridge members to it. This will allow to pass traffic from from Ethernet to W60G interface without routing.
Add interface members (ether1 and wlan60-1) to newly created bridge.
# Set up wireless connection
All previously explained steps are identical tobridgeandstationdevices. Different modes needs to be used when configuring wireless interfaces.
Configurebridgedevice as follows:
Configurestationdevice as follows:
# Additional configuration
Interfaces when enabled from greyed out will become active.
Link should be established after all previously explained steps are done. It's recommended to set up administrator password on both devices.
To create point to multi-point setup: On bridge device ap-bridge must be set and station-bridge for stations.