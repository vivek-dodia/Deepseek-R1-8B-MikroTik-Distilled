---
title: Step by step installation
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/50692141/Step+by+step+installation,
crawled_date: 2025-02-02T21:14:20.988740
section: mikrotik_docs
type: documentation
---

## LoRa card installation
LtAP LTE kit will be used as example in this section.
Open your routers case. Once you have removed all the screws carefully move the upper case to the left side, as the LTE antennas are attached to the inner side of it.
Insert R11e-LoRa card into the mini-PCIe slot and apply two screws to the threaded inserts.
Attach antenna to the card (UFL connector)
In this case UFL → SMA cable is also used, as the LtAP's case has a specific slot for it.
Once the previous steps are done, you can close the routers case and move on to configuration.
## Configuration
### GUI setup
Connect to your router via Winbox or WebFig.
Winbox can be downloaded in the link given below:
https://mikrotik.com/download
It is Highly recommended to upgrade your RouterOS version to the latest available. Installing the version will perform a reboot:
If your device does not haveIoT>LoRamenu, download "Extra packages" specifically for your routers architecture and rOS version. You can see the type of your routers architecture at the top of Winbox window or in System →  Resources → Architecture Name.
https://mikrotik.com/download
Once the package is downloaded and extracted, upload theIoTpackage to your router. It can be done via drag & drop as well. It should appear in the files folder after the upload is complete, reboot your router (System → Reboot) to install the package:
After the reboot, the package should be visible in the Package list:
Check if the LoRa gateway has initialized underIoT>LoRa>Devices. If it is LtAP model, make sure to set USB Type to Mini-PCIe:
Once the gateway has shown up (underIoT>LoRa>Devices) select it, choose Network Servers from the default ones or add your own (underIoT>LoRa>Servers) and enable it:
Navigate to Traffic tab to monitor the surrounding nodes sending requests:
This concludes basic installation and configuration of LoRa mini-PCIe cards. For additional settings check:General Properties