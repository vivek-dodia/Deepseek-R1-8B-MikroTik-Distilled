---
title: Container - ThingsBoard MQTT/HTTP server
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/166920348/Container+-+ThingsBoard+MQTT+HTTP+server,
crawled_date: 2025-02-02T21:15:28.102015
section: mikrotik_docs
type: documentation
---

* 1Introduction
* 2Summary
* 3Configuration3.1Container mode3.2Networking3.3Environment variables and mounts3.4Getting image3.5Starting the container
* 4Verification4.1Management access4.2MQTT test
* 5Enabling HTTPS and SSL MQTT5.1Create certificates5.2Download the ThingsBoard's configuration file5.3Alter the ThingsBoard's settings5.4Upload altered ThingsBoard configuration file5.5Confirm HTTPS access5.6Confirm SSL MQTT connection5.6.1Testing with the device that is running the container5.6.2Testing with another device
* 3.1Container mode
* 3.2Networking
* 3.3Environment variables and mounts
* 3.4Getting image
* 3.5Starting the container
* 4.1Management access
* 4.2MQTT test
* 5.1Create certificates
* 5.2Download the ThingsBoard's configuration file
* 5.3Alter the ThingsBoard's settings
* 5.4Upload altered ThingsBoard configuration file
* 5.5Confirm HTTPS access
* 5.6Confirm SSL MQTT connection5.6.1Testing with the device that is running the container5.6.2Testing with another device
* 5.6.1Testing with the device that is running the container
* 5.6.2Testing with another device
# Introduction
The introduction of the container feature into the RouterOS made it possible to run all kinds of servers for all sorts of tasks inside the router. This is especially relevant for people, who want to reduce the number of devices in their network. Instead of running a server on a separate device/machine, why not run it inside the router?
A lot of users need a server that is able to gather the data, store it and display it in a way it is easy to understand. This is where a platform likeThingsBoardcan come into play.
It is primarily positioned as an IoT platform and you can find all sorts of use cases for it that they demonstrate in thelink.
The most appealing part, from the RouterOS user standpoint, is that it can be used as an MQTT server (MQTT broker) or an HTTP server. Meaning, you can useMQTT publishorHTTP postto post the data. You can find ThingsBoard MQTT API guide by using the linkhereand HTTP API by using the linkhere.
In short, you can utilizescriptingto collect RouterOS statistics (like uptime, GPS coordinates, packet statistics, and almost anything else that you print into the terminal), then store this information into variables and structure a JSON message out of those. You can, then send this message using MQTT or HTTP post to the ThingsBoard via ascheduler(that will run this script whenever you need it). You can find an example of a basic script that does it inthis guide.
ThingsBoard will store and display the data with the help ofwidgets, which can be used to help you set up dashboards that visualize the data in graphs, tables, maps, and other ways.
There are 3 versions of the ThingsBoard instances available and each of them uses a different database:
* thingsboard/tb-postgres
* thingsboard/tb-cassandra
* thingsboard/tb
You can find more information in the ThingsBoard/docker documentation.
In our example, we will showcasetb-postgres- a single instance of ThingsBoard with PostgreSQL database.
# Summary
Sub-menu:/container
```
/container
```
note:containerpackage is required.
RouterOS versions that are older than v7.8 will not be able to run this scenario.
Make sure to study ourcontainerguide before proceeding with the configuration. Make sure to check thedisclaimerandrequirementssections to understand all the risks and necessary steps you might be required to do.
In this example, we will run it on aCloud Hosted Router, CHRdevice. To help you set it up in aVirtual Box, please check ouryoutube tutorial.
At the time, when the guide was published,thingsboard/tb-postgresimage was available for linux/arm64and linux/amd64OS/architecturesonly. Meaning, you are not able to run this scenario on our arm32-bit architecture RouterOS devices.
There are a couple of parameters to keep in mind:
* You need to understand that it is aserverand that you will need to have additional space for the data that is stored there and the image itself. In our tests, 8 GB of disk space was plenty enough but! you might want to consider adding more for real-life applications, especially if you are planning on running more containers. Just remember → it might be better to have a reserve.
* Same as with disk space, RAM memory is also important. Per the ThingsBoard documentation, when using a single instance of ThingsBoard with a PostgreSQL database, it is recommended to allocate at least 1GB of RAM and use a minimum load (a few messages per second). 2-4GB RAM is recommended. In other words, if you want to run it on a RouterBoard device, please understand, that you might not be able to achieve it on devices that have less than 1 GB RAM. That is why → consider having a device with more RAM memory to spare.
Go to thetips and trickssection to understand how to limit RAM.
# Configuration
## Container mode
Enable container mode:
```
/system/device-mode/update container=yes
```
You will need to confirm the device-mode with a press of the reset button, or a cold reboot, if using container on X86.
## Networking
Add veth interface for the container:
```
/interface/veth/add name=veth1 address=172.18.0.2/24 gateway=172.18.0.1
```
Create a bridge for the container, assign an IP network to it, and add veth to the bridge:
```
/interface/bridge/add name=dockertb
/ip/address/add address=172.18.0.1/24 interface=dockertb
/interface/bridge/port add bridge=dockertb interface=veth1
```
Setup NAT for outgoing traffic:
```
/ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.18.0.0/24
```
Forward TCP 9090 for HTTP management (the default HTTP port per ThingsBoard documentation):
```
/ip firewall nat add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=9090 protocol=tcp to-addresses=172.18.0.2 to-ports=9090
```
In thedst-addressfield shown in DNAT (dst-nat) rule above, we use the device's local IP address. First,use local IPs(local access)toset everything upandconfirm that everything is working.
```
dst-address
```
Forward TCP 1883 for non-SSL MQTT (the default MQTT port used per ThingsBoard documentation):
```
/ip firewall nat add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=1883 protocol=tcp to-addresses=172.18.0.2 to-ports=1883
```
Same as with HTTP access, in thedst-addressfield shown in DNAT (dst-nat) rule above, we use the device's local IP address. First,use local IPs(local access)toset everything upandconfirm that everything is working.
```
dst-address
```
## Environment variables and mounts
Checkdocker-thingsboarddocumentation for exact mounts and variables that need to be added.
Environment variables:
```
/container/envs/add name=tb_envs key=TB_QUEUE_TYPE value="in-memory"
```
Mounts:
```
/container/mounts/add name=mytb-data src=tb/mytb-data dst=/data
/container/mounts/add name=mytb-logs src=tb/mytb-logs dst=/var/log/thingsboard
```
## Getting image
To simplify the configuration, we will get the image from an external library but you can also import it via the.tarfile.
Make sure that you have "Registry URL" set accordingly, limit RAM usage (if necessary), and set up a directory for the image.
```
/container/config/set registry-url=https://registry-1.docker.io tmpdir=pull ram-high=2048.0MiB
```
Pull image:
```
/container/add remote-image=thingsboard/tb-postgres:latest interface=veth1 root-dir=ThingsBoard mounts=mytb-data,mytb-logs envlist=tb_envs logging=yes
```
After running the command, RouterOS should start "extracting" the package. Check "File System" for newly created folders and monitor container status with the command/container/print.
```
/container/print
```
## Starting the container
After you make sure that the container has been added and the status changed tostatus=stoppedafter using/container/print→ you can initiate it:
```
status=stopped
```
```
/container/print
```
```
/container/start 0
```
Wait for a couple of minutes for the container to fully load.
# Verification
## Management access
After the container is started and installed, access it using any browser, by going to →http://192.168.88.1:9090(where the IP address is the address used in the DNAT rule):
By default, credentials are (Username/Password):
* Systen Administrator: sysadmin@thingsboard.org / sysadmin
* Tenant Administrator: tenant@thingsboard.org / tenant
The login prompt should confirm that the server is running.
## MQTT test
Name it, however, you like, and click on "Add":
Check your device access token by clicking on the device you've just created and selecting the "Manage credentials" setting (copy the access token generated or type in your own →  "YOUR_TOKEN"):
After these steps, go to the RouterOS settings (back to CHR settings) and create a newMQTT broker(make sure that you have IoT package installedbecause otherwise, you will not have this menu):
```
/iot/mqtt/brokers/add name=tb address=172.18.0.2 port=1883 username=YOUR_TOKEN
```
Publish a static test MQTT message in the JSON format:
```
/iot/mqtt/publish broker="tb" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```
Confirm that the message was posted:
# Enabling HTTPS and SSL MQTT
By default, HTTP and MQTT protocols are used. As mentioned previously in the "Networking" section, working with non-SSL HTTP and non-SSL MQTT is not very safe (unless they are used within heavily protected networks with a well-configured firewall/restricted access) andwe advise enabling HTTPSandSSL MQTT.
Please check ThingsBoard documentation for more information →HTTP over SSLandMQTT over SSLguides.
First of all, there is no SSL without a certificate and one needs to be made (or purchased).
In short, this section will demonstrate how to generate self-signed certificates for HTTPS and SSL MQTT. Then, you will need to upload them to the correct folder within the ThingsBoard installation and alter the ThingsBoard configuration file accordingly.
In our guide, we will use RouterOS to generate bothcertificates(but you can also use OpenSSL or other tools you want).
## Create certificates
Create a certificate for HTTPS:
```
/certificate add name=TBhttps common-name=172.18.0.2
/certificate sign TBhttps
```
Create a certificate for MQTT:
```
/certificate add name=TBmqtt common-name=172.18.0.2
/certificate sign TBmqtt
```
Confirm that they were added with the help of/certificate/printcommand:
```
/certificate/print
```
```
[admin@MikroTik] > /certificate/print
Flags: K - PRIVATE-KEY; A - AUTHORITY; T - TRUSTED
Columns: NAME, COMMON-NAME, FINGERPRINT
#     NAME     COMMON-NAME  FINGERPRINT                                                     
0 KAT TBhttps  172.18.0.2   863f4547c74ce3ec70c3e82172502711517b52bbc055d18c24ba4aafec46152c
1 KAT TBmqtt   172.18.0.2   ebf3ff5d03ed4cc73546e058da9bc414cdaf24ce45da29b203348045fbbd21ae
```
Export the certificates using PKCS12 format and set up a password/passphrase for them:
```
/certificate/export-certificate file-name=keystore export-passphrase=thingsboard_cert_password type=pkcs12 numbers=0
/certificate/export-certificate file-name=mqttserver export-passphrase=thingsboard_mqttcert_password type=pkcs12 numbers=1
```
Use your ownexport-passphraseand remember them.
```
export-passphrase
```
The output from the command above will create certificatekeystore.p12andmqttserver.p12files that you can download from the "File List" menu:
```
[admin@MikroTik] > /file/print 
Columns: NAME, TYPE, SIZE, CREATION-TIME
 #  NAME                 TYPE             SIZE       CREATION-TIME       
 0  tb/mytb-data         container store             jan/19/2023 13:43:16
 1  container-log.0.txt  .txt file        2240.5KiB  jan/27/2023 15:37:41
 2  skins                directory                   jan/18/2023 15:12:22
 3  tb/mytb-logs         container store             jan/27/2023 12:24:30
 4  pull                 directory                   jan/19/2023 13:41:01
 5  pub                  directory                   jan/18/2023 16:15:29
 6  tb                   directory                   jan/23/2023 15:46:39
 7  tb/data              container store             jan/18/2023 16:50:08
 8  tb/logs              container store             jan/18/2023 16:50:08
 9  mqttserver.p12       .p12 file        2438       jan/27/2023 15:36:26
10  keystore.p12         .p12 file        2448       jan/27/2023 15:08:07
11  ThingsBoard          container store             jan/19/2023 13:40:50
```
Download both files from the router into any directory on your PC. For example, we've downloaded it intoC:\Users\Admin\Desktop\ThingsBoardfolder.
```
C:\Users\Admin\Desktop\ThingsBoard
```
## Download the ThingsBoard's configuration file
Open your command terminal ("CMD", as Administrator, for Windows users, or "Linux Shell or Command Terminal" for Linux users) and navigate it to the directory where the certificates are:
```
C:\Windows\System32>cd c:\Users\Admin\Desktop\ThingsBoard
C:\Users\Admin\Desktop\ThingsBoard>dir
Directory of C:\Users\Admin\Desktop\ThingsBoard
27.01.2023  15:36    <DIR>          .
27.01.2023  15:36    <DIR>          ..
27.01.2023  15:09             2 448 keystore.p12
27.01.2023  15:36             2 434 mqttserver.p12
               2 File(s)          4 882 bytes
               2 Dir(s)  51 380 154 368 bytes free
```
From this directory, you will need to connect to the router's IP via the SFTP (which allows you to file transfer using SSH protocol, so you need to make sure thatSSH serviceis enabled beforehand):
```
c:\Users\Admin\Desktop\ThingsBoard>sftp admin@192.168.88.1
The authenticity of host '192.168.88.1 (192.168.88.1)' can't be established.
RSA key fingerprint is SHA256:/WmmZErqWL51SOlS4EaGvSQ0i4HPnSIHCEjnc8AmP2c.
Are you sure you want to continue connecting (yes/no/[fingerprint])?yes
admin@192.168.88.1's password:
Connected to 192.168.88.1.
sftp>
```
While the container is running, go to the ThingsBoard configuration file folder (usedirorlscommand to see the content of the folder you are in andcdcommand to go to the folder of our choice). By default, it should be the folder with the "thingsboard.yml" configuration file in it. In our example, we could locate it under:
```
dir
```
```
ls
```
```
cd
```
```
sftp> cd ThingsBoard\usr\share\thingsboard\conf
sftp> dir
banner.txt          i18n                logback.xml         templates           thingsboard.conf    thingsboard.yml
```
Download the "thingsboard.yml" configuration usinggetcommand. This will download the default ThingsBoard configuration file to your machine (to the directory from where you initiated SFTP):
```
get
```
```
sftp> get thingsboard.yml
Fetching /ThingsBoard/usr/share/thingsboard/conf/thingsboard.yml to thingsboard.yml
/ThingsBoard/usr/share/thingsboard/conf/thingsboard.yml                               100%   67KB   2.0MB/s   00:00
sftp> quit
c:\Users\Admin\Desktop\ThingsBoard>dir
 Directory of c:\Users\Admin\Desktop\ThingsBoard
30.01.2023  10:59    <DIR>          .
30.01.2023  10:59    <DIR>          ..
27.01.2023  15:09             2 448 keystore.p12
27.01.2023  15:36             2 434 mqttserver.p12
30.01.2023  10:59            68 846 thingsboard.yml
               3 File(s)         73 728 bytes
               2 Dir(s)  50 901 626 880 bytes free
```
## Alter the ThingsBoard's settings
Open "thingsboard.yml" via your preferred text editor (notepad or any other), and alter a few lines. You can backup this file and save it with a different name to have a copy of the default settings, in case, of misconfiguration.
HTTPS-related settings:
* Enable SSL →  Change "SSL_ENABLED:false" to "SSL_ENABLED:true";
* Change credentials type → from "SSL_CREDENTIALS_TYPE:PEM" to "SSL_CREDENTIALS_TYPE:KEYSTORE";
* Change the path → from "SSL_KEY_STORE:classpath:keystore/keystore.p12" to "SSL_KEY_STORE:keystore.p12" (optional);
* Disable key alias setting → comment it → just put the "#" symbol in front of thekey_alias: "${SSL_KEY_ALIAS:tomcat}"line;
* Input your own certificate password that was used in RouterOS → from "SSL_KEY_STORE_PASSWORD:thingsboard" to "SSL_KEY_STORE_PASSWORD:thingsboard_cert_password" and from "SSL_KEY_PASSWORD:thingsboard" to "SSL_KEY_PASSWORD:thingsboard_cert_password".
```
ssl:
    # Enable/disable SSL support
    enabled: "${SSL_ENABLED:true}"
    # Server SSL credentials
    credentials:
      # Server credentials type (PEM - pem certificate file; KEYSTORE - java keystore)
      type: "${SSL_CREDENTIALS_TYPE:KEYSTORE}"
      # Keystore server credentials
      keystore:
        # Type of the key store (JKS or PKCS12)
        type: "${SSL_KEY_STORE_TYPE:PKCS12}"
        # Path to the key store that holds the SSL certificate
        store_file: "${SSL_KEY_STORE:keystore.p12}"
        # Password used to access the key store
        store_password: "${SSL_KEY_STORE_PASSWORD:thingsboard_cert_password}"
        # Key alias
        #key_alias: "${SSL_KEY_ALIAS:tomcat}"
        # Password used to access the key
        key_password: "${SSL_KEY_PASSWORD:thingsboard_cert_password}"
```
MQTT-related settings:
* Enable SSL →  Change "MQTT_SSL_ENABLED:false" to "MQTT_SSL_ENABLED:true";
* Change credentials type → from "MQTT_SSL_CREDENTIALS_TYPE:PEM" to "MQTT_SSL_CREDENTIALS_TYPE:KEYSTORE";
* Change type of key → from "MQTT_SSL_KEY_STORE_TYPE:JKS" to "MQTT_SSL_KEY_STORE_TYPE:PKCS12";
* Change the path (extension) → from "MQTT_SSL_KEY_STORE:mqttserver.jks" to "MQTT_SSL_KEY_STORE:mqttserver.p12";
* Disable key alias setting → comment it → just put the "#" symbol in front of thekey_alias: "${MQTT_SSL_KEY_ALIAS:}"line;
* Input your own certificate password that was used in RouterOS → from "MQTT_SSL_KEY_STORE_PASSWORD:server_ks_password" to "MQTT_SSL_KEY_STORE_PASSWORD:thingsboard_mqttcert_password" and from "MQTT_SSL_KEY_PASSWORD:server_key_password" to "MQTT_SSL_KEY_PASSWORD:thingsboard_mqttcert_password".
```
ssl:
      # Enable/disable SSL support
      enabled: "${MQTT_SSL_ENABLED:true}"
      # Server SSL credentials
      credentials:
        # Server credentials type (PEM - pem certificate file; KEYSTORE - java keystore)
        type: "${MQTT_SSL_CREDENTIALS_TYPE:KEYSTORE}"
        # Keystore server credentials
        keystore:
          # Type of the key store (JKS or PKCS12)
          type: "${MQTT_SSL_KEY_STORE_TYPE:PKCS12}"
          # Path to the key store that holds the SSL certificate
          store_file: "${MQTT_SSL_KEY_STORE:mqttserver.p12}"
          # Password used to access the key store
          store_password: "${MQTT_SSL_KEY_STORE_PASSWORD:thingsboard_mqttcert_password}"
          # Optional alias of the private key; If not set, the platform will load the first private key from the keystore;
          #key_alias: "${MQTT_SSL_KEY_ALIAS:}"
          # Optional password to access the private key. If not set, the platform will attempt to load the private keys that are not protected with the password;
          key_password: "${MQTT_SSL_KEY_PASSWORD:thingsboard_mqttcert_password}"
```
Apply the changes to the "thingsboard.yml" file (re-save it after editing).
## Upload altered ThingsBoard configuration file
All that is left is to overwrite the current configuration file with an altered file and upload both certificates.
Once again, make sure your terminal is pointing to the right folder (where 3 files are located → both certificates and an altered "thingsboard.yml" file), and, from there, SFTP into the container's configuration file directory:
```
c:\Users\Admin\Desktop\ThingsBoard>dir
 Directory of c:\Users\Admin\Desktop\ThingsBoard
30.01.2023  10:59    <DIR>          .
30.01.2023  10:59    <DIR>          ..
27.01.2023  15:09             2 448 keystore.p12
27.01.2023  15:36             2 434 mqttserver.p12
30.01.2023  10:59            68 846 thingsboard.yml
               3 File(s)         73 728 bytes
               2 Dir(s)  50 901 626 880 bytes free
c:\Users\Admin\Desktop\ThingsBoard>sftp admin@192.168.88.1
admin@192.168.88.1's password:
Connected to 192.168.88.1.
sftp> cd ThingsBoard\usr\share\thingsboard\conf
sftp> dir
banner.txt          i18n                logback.xml         templates           thingsboard.conf    thingsboard.yml
```
Upload these files with the help ofputcommand:
```
put
```
```
sftp> put thingsboard.yml
Uploading thingsboard.yml to /ThingsBoard/usr/share/thingsboard/conf/thingsboard.yml
thingsboard.yml                                                                       100%   67KB   2.2MB/s   00:00
sftp> put keystore.p12
Uploading keystore.p12 to /ThingsBoard/usr/share/thingsboard/conf/keystore.p12
keystore.p12                                                                          100% 2448     1.2MB/s   00:00
sftp> put mqttserver.p12
Uploading mqttserver.p12 to /ThingsBoard/usr/share/thingsboard/conf/mqttserver.p12
mqttserver.p12                                                                        100% 2434   608.5KB/s   00:00
sftp> dir
banner.txt          i18n                keystore.p12        logback.xml         mqttserver.p12      templates           
thingsboard.conf    thingsboard.yml
```
Restart the container:
```
[admin@MikroTik] > /container/stop 0
[admin@MikroTik] > /container/start 0
```
Make sure to wait for the container to stop (status=stoppedshould be shown after using/container/printcommand) before initiating it again.
```
status=stopped
```
```
/container/print
```
## Confirm HTTPS access
Now, you should be able to accesshttps://your_IP:9090(where the IP address is the address used in the DNAT rule):
## Confirm SSL MQTT connection
In this example, we will test aone-way SSL communication access token scenario.
### Testing with the device that is running the container
Add MQTT broker:
```
/iot/mqtt/brokers/add name=tbssl address=172.18.0.2 port=8883 username=YOUR_TOKEN ssl=yes
```
Publish a static test MQTT message in the JSON format:
```
/iot/mqtt/publish broker="tbssl" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```
Confirm that it was received by the MQTT broker:
### Testing with another device
When you have two RouterOS devices, one that is running the container (and, in our example, is the same device that generated the certificate) and the other one that you wish to test the MQTT connection from (let's say, anLTAPor any other RouterOS device with IoT package installed) → you will need to import the certificate to the second device.
Drag and drop the exported certificate (mqttserver.p12) into the device's "File List":
```
[admin@LTAP] > /file/print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME            TYPE       SIZE  CREATION-TIME       
0  mqttserver.p12  .p12 file  2438  jan/30/2023 13:28:11
1  flash           disk             jul/06/2021 14:51:53
2  flash/pub       directory        jul/06/2021 14:51:53
3  flash/skins     directory        jan/01/1970 02:00:07
[admin@LTAP] >
```
Import the certificate:
```
[admin@LTAP] > /certificate/import file-name=mqttserver.p12 passphrase=thingsboard_mqttcert_password
```
Add MQTT broker, where the address is the IP address "dst-address" that is used in the TCP 8883 port-forwarding rule on the ThingsBoard-container router:
```
dst-address
```
```
/iot/mqtt/brokers/add name=tbssl address=192.168.88.1 port=8883 username=YOUR_TOKEN ssl=yes
```
Publish a static test MQTT message in the JSON format:
```
/iot/mqtt/publish broker="tbssl" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```
And confirm that the broker received it → under the "Latest Telemetry" section on the ThingsBoard.