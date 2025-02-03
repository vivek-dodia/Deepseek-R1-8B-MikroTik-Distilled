---
title: Backup
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/40992852/Backup,
crawled_date: 2025-02-02T21:08:47.928046
section: mikrotik_docs
type: documentation
---

# Summary
The RouterOS backup feature allows cloning a router configuration in binary format, which can then be re-applied on the same device. The system's backup file also contains the device's MAC addresses, which are restored when the backup file is loaded.
We recommend restoring the backup on the same version of RouterOS.
# Saving a backup
Sub-menu:/system backup save
```
/system backup save
```
Property | Description
----------------------
dont-encrypt(yes | no; Default:no) | Disable backup file encryption. Note that since RouterOS v6.43 without a providedpassword,the backup file is unencrypted.
encryption(aes-sha256 | rc4; Default:aes-sha256) | The encryption algorithm to use for encrypting the backup file. Note that is not considered a secure encryption method and is only available for compatibility reasons with older RouterOS versions.
name(string; Default:[identity]-[date]-[time].backup) | The filename for the backup file.
password(string; Default: ) | Password for the encrypted backup file. Note that since RouterOS v6.43 without a providedpassword,the backup file is unencrypted.
The backup file will be available under/filemenu, which can be downloaded using FTP or using Winbox.
```
/file
```
# Loading a backup
Load units backup without password:
```
[admin@MikroTik] > system/backup/load name=auto-before-reset.backup password=""
```
Property | Description
----------------------
name(string; Default: ) | File name for the backup file.
password(string; Default: ) | Password for the encrypted backup file.
# Example
To save the router's configuration to file test and a password:
```
[admin@MikroTik] > /system backup save name=test password=<YOUR_PASSWORD> 
Configuration backup saved 
[admin@MikroTik] > /system backup
```
To see the files stored on the router:
```
[admin@MikroTik] > /file print 
# NAME TYPE SIZE CREATION-TIME 
0 test.backup backup 12567 sep/08/2018 21:07:50 
[admin@MikroTik] >
```
To load the saved backup file test:
```
[admin@MikroTik] > /system backup load name=test 
password: <YOUR_PASSWORD> 
Restore and reboot? [y/N]: y 
Restoring system configuration 
System configuration restored, rebooting now
```
# Cloud backup
Since RouterOS v6.44 it is possible to securely store your device's backup file on MikroTik's Cloud servers, read more about this feature on theIP/Cloudpage.