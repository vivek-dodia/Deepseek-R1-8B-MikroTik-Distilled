# Document Information
Title: Container - mosquitto MQTT server
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/169246787/Container+-+mosquitto+MQTT+server,

# Content
# Introduction
The introduction of the container feature into the RouterOS made it possible to run all kinds of servers for all sorts of tasks inside the router. This is especially relevant for people, who want to reduce the number of devices in their network. Instead of running a server on a separate device/machine, why not run it inside the router?
In this guide, we will showcase how to install a basic MQTT broker (or in other words, server) calledeclipse-mosquitto. MQTT protocol is a very popular choice, especially in IoT topologies. It is an open OASIS and ISO standard lightweight, publish-subscribe network protocol that transports messages between devices. A typical topology consists of an MQTT publisher (a device that sends information), an MQTT broker (a server where the data is stored), and an MQTT subscriber (a device that listens to the data published on the server).
RouterOS supportsMQTT publish, subscribefeature, and, now, we can also run the MQTT broker as well.
The image that we are going to use, can be found by following the hub.dockerlink.
# Summary
Make sure to study ourcontainerguide before proceeding with the configuration. Make sure to check thedisclaimerandrequirementssections to understand all the risks and necessary steps you might be required to do.
You can find supported architectures by following thelink.
At the time, when the guide was published,eclipse-mosquittoimage was available for ARM32, ARM64, and AMD64 (CHR and x86) devices. In this example, we will run it on an ARM32 architecture device →RB1100AHx4.
# Container configuration
Sub-menu:/container
```
/container
```
note:containerpackage is required.
# Container mode
Enable container mode:
```
/system/device-mode/update container=yes
```
You will need to confirm the device-mode with a press of the reset button, or a cold reboot, if using container on X86.
# Networking
Add veth interface for the container:
```
/interface/veth/add name=veth2 address=172.19.0.2/24 gateway=172.19.0.1
```
Create a bridge for containers and add veth to it:
```
/interface/bridge/add name=msqt
/ip/address/add address=172.19.0.1/24 interface=msqt
/interface/bridge/port add bridge=msqt interface=veth2
```
Forward TCP 1883 for non-SSL MQTT (where 192.168.88.1 is the device's LAN IP address) for testing purposes if NAT is required (optional):
```
/ip firewall nat add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=1883 protocol=tcp to-addresses=172.19.0.2 to-ports=1883
```
# Environment variables and mounts
Per the eclipse-mosquitto docker hub, define a mount for the configuration file. We will mount not just the configuration file, but the whole folder, because, for SSL MQTT, we will need to upload certificates into the folder as well:
```
/container mounts add src=/mosquitto_mounted dst=/mosquitto/config name=msqt_config
```
# Getting image
To simplify the configuration, we will get the image from an external library but you can also import it via the.tarfile.
In this example, we will use the device's own storage. RB1100AHx4 has 128 MB disk space and a basic mosquitto installation should not take up more than ~15 MB.
Make sure that you have "Registry URL" set accordingly, limit RAM usage (if necessary), and set up a directory for the image:
```
/container/config/set registry-url=https://registry-1.docker.io tmpdir=pull
```
Pull image:
```
/container/add remote-image=eclipse-mosquitto:latest interface=veth2 root-dir=mosquitto mounts=msqt_config logging=yes
```
After running the command, RouterOS should start "extracting" the package. Check "File System" for newly created folders and monitor container status with the command/container/print.
```
/container/print
```
# Setting up mosquitto configuration file
To get themosquttio.conffile, we will need to use SFTP (file transfer over SSH) protocol, so make sure that SSHserviceis enabled. You can also use FTP.
Open your command terminal ("CMD", as Administrator, for Windows users, or "Linux Shell or Command Terminal" for Linux users) and navigate it to the directory where you want to download the configuration file. For example, to the "Container" folder on your "Desktop":
```
C:\WINDOWS\system32>cd C:\Users\Administrator\Desktop\Container
C:\Users\Administrator\Desktop\Container>
```
Initiate SFTP to the device's IP address:
```
C:\Users\Administrator\Desktop\Container>sftp admin@192.168.88.1
The authenticity of host '192.168.88.1 (192.168.88.1)' can't be established.
RSA key fingerprint is SHA256:lfxxs+xMrXlvP7hiHi9ZAEZlPi6/c5US+r6J7ljhkaA.
Are you sure you want to continue connecting (yes/no/[fingerprint])?yes
Warning: Permanently added '192.168.88.1' (RSA) to the list of known hosts.
Connected to 192.168.88.1.
sftp>
```
Go to the mosquitto configuration file folder (usedirorlscommand to see the content of the folder you are in andcdcommand to go to the folder of our choice). By default, the configuration is loaded from the "/mosquitto/config/mosquitto.conf", so, navigate there and usegetcommand to download it:
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
get
```
```
sftp> cd mosquitto/mosquitto/config
sftp> dir
mosquitto.conf
sftp> get mosquitto.conf
Fetching /mosquitto/mosquitto/config/mosquitto.conf to mosquitto.conf
/mosquitto/mosquitto/config/mosquitto.conf
```
Open "mosquitto.conf" via your preferred text editor (notepad or any other), and just overwrite it with two lines shown below:
```
listener 1883
allow_anonymous true
```
Overwrite the file using the samemosquitto.confname.
After you have created your own custom configuration file, upload it into the mounted directory/folder "mosquitto_mounted". If you have not run the container yet, you will not have the "mosquitto_mounted" folder and you can create it manually. If you did run it (/container start 0), it should have been created automatically:
```
/container start 0
```
```
sftp> dir
mosquitto           mosquitto_mounted   pub                 pull                skins
```
Use SFTP from the directory where the edited mosquitto.conf file is located andputit into the mounted directory:
```
put
```
```
C:\Users\Administrator\Desktop\Container>dir
Directory of C:\Users\Administrator\Desktop\Container
02/03/2023  12:09 PM    <DIR>          .
02/03/2023  12:09 PM    <DIR>          ..
02/03/2023  12:09 PM            40,449 mosquitto.conf
1 File(s)         40,449 bytes
2 Dir(s)  76,166,430,720 bytes free
C:\Users\Administrator\Desktop\Container>sftp admin@192.168.88.1
Connected to 192.168.88.1.
sftp> dir
mosquitto           mosquitto_mounted   pub                 pull                skins
sftp> cd mosquitto_mounted
sftp> put mosquitto.conf
Uploading mosquitto.conf to /mosquitto_mounted/mosquitto.conf
mosquitto.conf                                                                        100%  162    40.5KB/s   00:00
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
# Starting the container
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
If you have enabled container logging, you would see something like this in theLogssection:
```
12:12:46 container,info,debug 1707214366: mosquitto version 2.0.18 starting
12:12:46 container,info,debug 1707214366: Config loaded from /mosquitto/config/mosquitto.conf.
12:12:46 container,info,debug 1707214366: Opening ipv4 listen socket on port 1883.
12:12:46 container,info,debug 1707214366: Opening ipv6 listen socket on port 1883.
12:12:46 container,info,debug 1707214366: mosquitto version 2.0.18 running
```
# MQTT publish and subscribe
Sub-menu:/iot mqtt
```
/iot mqtt
```
note:iotpackage is required.
Add an MQTT broker:
```
/iot/mqtt/brokers/add name=mosquitto username=test address=172.19.0.2
```
Subscribe to the MQTT broker and the required topic:
```
/iot/mqtt/subscribe broker=mosquitto topic=test/topic
```
Publish a static MQTT message:
```
/iot/mqtt/publish broker="mosquitto" topic="test/topic" message="{\"test\":\"123\"}"
```
Check subscriptions for received messages:
```
/iot/mqtt/subscriptions/recv/print
0 broker=mosquitto topic="test/topic" data="{"test":"123"}"
time=2023-07-12 10:01:40
```
You can also check the container logs (if enabled), to confirm the mosquitto is operational:
```
12:47:28 container,info,debug 1675421248: New connection from 172.19.0.1:42240 on port 1883.
12:47:28 container,info,debug 1675421248: New client connected from 172.19.0.1:42240 as MTD8580EC793C4 (p2, c1, k60, u'test').
12:47:38 container,info,debug 1675421258: Client MTD8580EC793C4 disconnected.
```
# SSL MQTT
Usingnon-SSL MQTTfor a production environmentis not secure. One can easilycapture/sniffthe packet exchange between the broker and the publisher and, as a result, will be able to obtain user credentials and other sensitive information.
To increase security, use SSL MQTT.
The first step is to generate the certificates. In this example, we will use a simple Root CA scenario (with no device/client certificate requirement).
Use the officialmosquitto-tls user guidefor the step-by-step.
# Server configuration
You should have generated ca.crt (Certificate Authority file), server.crt (server certificate) and server.key (server's key):
```
C:\Users\Administrator\Desktop\Container>dir
Directory of C:\Users\Administrator\Desktop\Container
07/12/2023  10:58 AM    <DIR>          .
07/12/2023  10:58 AM    <DIR>          ..
07/12/2023  10:56 AM             1,322 ca.crt
07/12/2023  10:56 AM             1,854 ca.key
07/12/2023  09:57 AM                35 mosquitto.conf
07/12/2023  10:58 AM             1,164 server.crt
07/12/2023  10:57 AM               960 server.csr
07/12/2023  10:56 AM             1,704 server.key
6 File(s)          7,039 bytes
2 Dir(s)  52,401,184,768 bytes free
```
Open mounted "mosquitto.conf" via your preferred text editor (notepad or any other), and just overwrite it with the lines shown below:
```
tls_version tlsv1.2
port 8883
allow_anonymous true
cafile /mosquitto/config/ca.crt
keyfile /mosquitto/config/server.key
certfile /mosquitto/config/server.crt
```
Upload the certificate files, and updated SSL-ready mosquitto.conf file into the mounted folder "mosquitto_mounted":
```
C:\Users\Administrator\Desktop\Container>sftp admin@192.168.88.1
Connected to 192.168.88.1.
sftp> cd mosquitto_mounted
sftp> dir
mosquitto.conf
sftp> put ca.crt
Uploading ca.crt to /mosquitto_mounted/ca.crt
ca.crt                                                                                100% 1322   323.0KB/s   00:00
sftp> put server.crt
Uploading server.crt to /mosquitto_mounted/server.crt
server.crt                                                                            100% 1164   227.3KB/s   00:00
sftp> put server.key
Uploading server.key to /mosquitto_mounted/server.key
server.key                                                                            100% 1704   415.7KB/s   00:00
sftp> dir
ca.crt           mosquitto.conf   server.crt       server.key
sftp> put mosquitto.conf
Uploading mosquitto.conf to /mosquitto_mounted/mosquitto.conf
mosquitto.conf                                                                        100%  162    32.2KB/s   00:00
```
Restart the container:
```
[admin@MikroTik] > /container/stop 0
[admin@MikroTik] > /container/start 0
```
Confirm that the broker listens on port 8883 using the logs:
```
11:20:41 container,info,debug 1689160841: mosquitto version 2.0.15 starting
11:20:41 container,info,debug 1689160841: Config loaded from /mosquitto/config/mosquitto.conf.
11:20:41 container,info,debug 1689160841: Opening ipv4 listen socket on port 8883.
11:20:41 container,info,debug 1689160841: Opening ipv6 listen socket on port 8883.
11:20:41 container,info,debug 1689160841: mosquitto version 2.0.15 running
11:22:24 system,info,account user admin logged in from 10.5.217.34 via local
```
# Testing the connection
Upload CA certificate (ca.crt) into RouterOS, into the device's "File List":
```
/file print
Columns: NAME, TYPE, SIZE, CREATION-TIME
# NAME                TYPE             SIZE  CREATION-TIME
0  skins               directory              1970-01-01 03:00:02
1  pub                 directory              2023-01-04 11:05:04
2  disk7               disk                   2023-07-12 09:52:07
3  mosquitto           container store        2023-07-12 09:52:09
4  mosquitto_mounted   container store        2023-07-25 16:38:37
5  pull                directory              2023-07-12 09:52:09
6  ca.crt              .crt file        1322  2023-07-12 11:28:23
```
Import the certificate:
```
/certificate/import file-name=ca.crt passphrase=""
```
Add MQTT broker for SSL connection:
```
/iot/mqtt/brokers/add name=mosquittoSSL username=test address=172.19.0.2 port=8883 ssl=yes
```
Subscribe to the MQTT broker and the required topic:
```
/iot/mqtt/subscribe broker=mosquittoSSL topic=test/topic
```
Publish a static MQTT message:
```
/iot/mqtt/publish broker="mosquittoSSL" topic="test/topic" message="{\"test\":\"123\"}"
```
Check subscriptions for received messages:
```
/iot/mqtt/subscriptions/recv/print
0 broker=mosquittoSSL topic="test/topic" data="{"test":"123"}"
time=2023-07-12 10:20:40
```