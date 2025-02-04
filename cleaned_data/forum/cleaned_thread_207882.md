# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 207882

# Discussion

## Initial Question
Author: [SOLVED]Fri May 24, 2024 10:14 am
https://help.mikrotik.com/docs/display/ROS/WirelessWhen using /system/package/update you should not run into the described issues. I guess you uploaded NPK of ROS main package manually without the appropriate wireless package.Reading the changelog, instead of YOLO upgrading a device would have been a good idea as well:https://mikrotik.com/download/changelogs#c-stable-v7_137.13 2023-12-14Notice - Starting from RouterOS version 7.13, significant changes have been made to the RouterOS wireless packages. This is done due to a new product development which will require more disk space for hardware drivers so we had to split it in order to maintain old products alongside the new ones. More wireless packages are yet to come.1. When upgrading by using "check-for-updates", all versions earlier than 7.12 will display 7.12 as the latest available version. Upgrade from v7.12 to v7.13 or later versions must be done through 7.12 in order to convert wireless packages automatically. Fresh installation with Netinstall or manual package installation works in the same manner as always.2. Drivers for older wireless and 60GHz interfaces, as well as the wireless management system CAPsMAN, are now part of a separate "wireless" package instead of being a part of the bundle package. This package can be uninstalled if not needed.3. The existing "wifiwave2" package has been divided into distinct packages: "wifi-qcom" and "wifi-qcom-ac", and the necessary utilities for WiFi management are now included in the RouterOS bundle. RouterOS and "wifi-qcom-ac" packages alongside each other now fit into 16MB flash memory.