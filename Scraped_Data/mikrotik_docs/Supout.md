---
title: Supout.rif
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/328106/Supout.rif ,
crawled_date: 2025-02-02T20:25:17.943576
section: mikrotik_docs
type: documentation
---

# What is supout.rif file?
The support file is used for debugging MikroTik RouterOS and to solve the support questions faster. All MikroTik Router information is saved in a binary file, which is stored in the router and can be downloaded from the router using FTP or WinBox. If required, then you can generate the file on the "/flash" folder on devices with FLASH type memory or external storage drive, by specifying the full path to the file "name=flash/supout.rif". You can view the contents of this file in yourMikrotik account, simply click on "Supout.rif viewer" located in the left column and upload the file.
This file contains all your router's configuration, logs, and some other details that will help MikroTik Support to solve your issue. The file does not contain sensitive information or router passwords.
# Creating a Support Output file
## Winbox
To generate this file in Winbox, click on "Make Supout.rif".
To save the file to your computer, right mouse click on the file and select "Download" to get support output file or simply drag the file to your desktop.
## Webfig
To generate this file in Webfig, click on "Make Supout.rif" and then "Download" to get it on your computer.
## Console
To generate this file, please type in the command line:
```
/system sup-output name=supout.rif
```
If you open the file on supout viewer and output is too narrow, then you can re-generate supout file and specify output width manually with output-width option:
```
/system sup-output name=supout.rif output-width=300
```