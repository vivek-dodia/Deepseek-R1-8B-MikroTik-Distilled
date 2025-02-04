# Document Information
Title: Cloud
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/97779929/Cloud,

# Content
# Summary
MikroTik offers multiple services for your RouterBOARD devices that are connected to the Internet. These services are meant to ease the inconveniences when configuring, setting up, controlling, maintaining, or monitoring your device. A more detailed list of available services that IP/Cloud can provide can be found below.
# Services
# DDNS
DDNS or Dynamic DNS is a service that updates the IPv4 address for A records and the IPv6 address for AAAA records periodically. Such a service is very useful when your ISP has provided a dynamic IP address that changes periodically, but you always need an address that you can use to connect to your device remotely. Below you can find operation details that are relevant to the IP/Cloud's DDNS service:
Since RouterOS v6.43 if your device is able to reachcloud2.mikrotik.comusing IPv6, then a DNSAAAArecord is going to be created for your public IPv6 address. If your device is only able to reachcloud2.mikrotik.comusing IPv4, then only a DNSArecord is going to be created for your public IPv4 address. cloud.mikrotik.com is used for older RouterOS versions prior 6.44
To enable the DDNS service:
```
[admin@MikroTik] /ip cloud set ddns-enabled=yes
[admin@MikroTik] /ip cloud print
ddns-enabled: yes
ddns-update-interval: none
update-time: yes
public-address: 159.148.147.196
public-address-ipv6: 2a02:610:7501:1000::2
dns-name: 529c0491d41c.sn.mynetname.net
status: updated
```
To disable the DDNS service:
```
/ip cloud set ddns-enabled=auto
```
To manually trigger a DNS update:
```
[admin@MikroTik] > /ip cloud force-update
```
# Update time
Correct time on a device is important, it causes issues with the system's logs, breaks HTTPS connectivity to the device, tunnel connectivity, and other issues. To have your system's clock updated, you can useNTPorSNTP, though it requires you to specify an IP address for the NTP Server. In most cases, NTP/SNTP is not required in order to simply have a correct time set on the device, for simplicity you can use the IP Cloud's update time service. Below you can find operation details that are relevant to the IP/Cloud's update time service:
To enable the time update service:
```
[admin@MikroTik] > /ip cloud set update-time=yes
```
To enable automatic time zone detection:
```
[admin@MikroTik] > /system clock set time-zone-autodetect=yes
```
# Backup
It is possible to store your device'sbackupon MikroTik's Cloud server. The backup service allows you to upload an encrypted backup file, download it and apply the backup file to your device as long as your device is able to reach MikroTik's Cloud server. Below you can find operation details that are relevant to the IP/Cloud's backup service:
To create a new backup and upload it the MikroTik's Cloud server:
```
[admin@MikroTik] > /system backup cloud upload-file action=create-and-upload password=test123!!!
[admin@MikroTik] > /system backup cloud print
0 name="cloud-20180921-162649" size=13.2KiB ros-version="6.44beta9" date=sep/21/2018 16:26:49 status="ok" secret-download-key="AbCdEfGhIjKlM1234567890"
```
To download the uploaded backup file and save it to the device's memory:
```
[admin@MikroTik] > /system backup cloud download-file action=download number=0
# OR
[admin@MikroTik] > /system backup cloud download-file action=download secret-download-key=AbCdEfGhIjKlM1234567890
```
To remove the uploaded backup:
```
/system backup cloud remove-file number=0
```
To replace an existing file with a new backup file, use the following command:
```
/system/backup/cloud/upload-file action=create-and-upload replace=_your_previously_created_backup_file_ password=test123!!!
```
To upload an existing backup file (created previously):
```
[admin@MikroTik] > /system backup save encryption=aes-sha256 name=old_backup password=test123!!!
[admin@MikroTik] > /system backup cloud upload-file action=upload src-file=old_backup.backup
[admin@MikroTik] > /system backup cloud print
0 name="cloud-20180921-164044" size=13.2KiB ros-version="6.44beta9" date=sep/21/2018 16:40:44 status="ok" secret-download-key="AbCdEfGhIjKlM1234567890"
```
# Back to Home
For more info about Back to Home (BTH) service, see the separatedocumentation page.
# File share
For more info about File Share service, see the separatedocumentation page.
# Relay service
Back to home and File Share both partially rely on the MikroTik cloud relay service. All transmissions through the relay service are end-to-end encrypted, relay is purely to faclilitate connection and is designed to never require decryption of user data or metadata. See respective manuals for details on how each service uses the relay.
# Properties
Sub-menu:/ip cloud
```
/ip cloud
```
Property | Description
----------------------
ddns-enabled(yes | auto; Default:auto) | If set toyes, then the device will send an encrypted message to MikroTik's Cloud server. The server will then decrypt the message and verify that the sender is an authentic MikroTik device. If all is OK, then MikroTik's Cloud server will create a DDNS record for this device and send a response to the device. Every minute the IP/Cloud service on the router will check if the WAN IP address matches the one sent to MikroTik's Cloud server and will send an encrypted update to the cloud server if the IP address changes.If set to auto, ddns will only be enabled ifBack To Homeis enabled.
ddns-update-interval(time, minimum 60 seconds; Default:none) | If set DDNS will attempt to connect IP Cloud servers at the set interval. If set tononeit will continue to internally check IP address update and connect to IP Cloud servers as needed. Useful if the IP address used is not on the router itself and thus, cannot be checked as a value internal to the router.
update-time(yes | no; Default:yes) | If set toyesthen router clock will be set to time, provided by the cloud serverIFthere is noNTPorSNTPclient enabled. If set tono, then IP/Cloud service will never update the device's clock. If update-time is set toyes, Clock will be updated even when ddns-enabled is set tono.
public-address(read-only: address) | Shows the device's IPv4 address that was sent to the cloud server. This field is visible only after at least one IP Cloud request was successfully completed.
public-address-ivp6(read-only: address) | Shows the device's IPv6 address that was sent to the cloud server. This field is visible only after at least one IP Cloud request was successfully completed.
warning(read-only: string) | Shows a warning message if the IP address sent by the device differs from the IP address in the UDP packet header as visible by MikroTik's Cloud server. Typically this happens if the device is behind NAT. Example: "DDNS server received a request from IP 123.123.123.123 but your local IP was 192.168.88.23; DDNS service might not work"
dns-name(read-only: name) | Shows the DNS name assigned to the device. Name consists of 12 characters serial number appended by.sn.mynetname.net. This field is visible only after at least one ddns-request is successfully completed.
status(read-only: string) | Contains text string that describes the current dns-service state. The messages are self explanatoryupdating...updatedError: no Internet connectionError: request timed outError: REJECTED. Contact MikroTik supportError: internal error- should not happen. One possible cause is if the router runs out of memory
If set toyes, then the device will send an encrypted message to MikroTik's Cloud server. The server will then decrypt the message and verify that the sender is an authentic MikroTik device. If all is OK, then MikroTik's Cloud server will create a DDNS record for this device and send a response to the device. Every minute the IP/Cloud service on the router will check if the WAN IP address matches the one sent to MikroTik's Cloud server and will send an encrypted update to the cloud server if the IP address changes.
```
yes
```
If set to auto, ddns will only be enabled ifBack To Homeis enabled.
```
yes
```
```
no
```
```
yes
```
```
no
```
# Advanced
Sub-menu:/ip cloud advanced
```
/ip cloud advanced
```
Property | Description
----------------------
use-local-address(yes | no; Default:no) | By default, the DNS name will be assigned to the detected public address (from the UDP packet header). If you wish to send your "local" or "internal" IP address, then set this toyes
```
yes
```
# Cloud backup
Sub-menu:/system backup cloud
```
/system backup cloud
```
Below you can find commands and properties that are relevant to the specific command, other properties will not have any effect.
Property | Description
----------------------
action(download) | Downloads an uploaded backup file from MikroTik's Cloud server.
number(integer) | Specifies the backup slot on MikroTik's Cloud server, the free backup slot is always going to be in the0thslot.
secret-download-key(string) | Unique identifier that can be used to download your uploaded backup file. When downloading the uploaded backup file you do not have to be using the same device, from which the backup was uploaded from. Useful when deploying a backup on a new device.
```
0th
```
Property | Description
----------------------
number(integer) | Deletes the backup file in the specified backup slot, the free backup slot is always going to be in the0thslot.
```
0th
```
Property | Description
----------------------
action(create-and-upload) | Uploads a backup file to MikroTik's Cloud server.create-and-upload- creates a new backup file with the specified password and uploads itupload- uploads a created system's backup file.
name(string) | Specifies the backup's name that will show up in the uploaded backups list. This isNOTthe source backup's name, this name is only used for visual representation.
src-file(file) | Backup's file name to upload that was created using/system backup. This property only has an effect when the action is set toupload.
password(string) | Create, encrypt and upload a backup file with the specified password. This property only has an effect when the action is set tocreate-and-upload.
```
create-and-upload
```
```
upload
```
```
/system backup
```
```
upload
```
```
create-and-upload
```