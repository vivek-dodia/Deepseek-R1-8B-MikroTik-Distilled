---
title: Container - freeradius server
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/172294200/Container+-+freeradius+server,
crawled_date: 2025-02-02T21:15:25.077998
section: mikrotik_docs
type: documentation
---

* 1Introduction
* 2Summary
* 3Configuration3.1Container mode3.2Networking3.3Getting image3.4Starting the container3.5Altering the server's configuration files
* 4Result verification
* 3.1Container mode
* 3.2Networking
* 3.3Getting image
* 3.4Starting the container
* 3.5Altering the server's configuration files
# Introduction
The introduction of the container feature into the RouterOS made it possible to run all kinds of servers for all sorts of tasks inside the router. This is especially relevant for people, who want to reduce the number of devices in their network. Instead of running a server on a separate device/machine, why not run it inside the router?
Radiusis short for Remote Authentication Dial-In User Service. RouterOS has a RADIUS client feature supported that can authenticate for HotSpot,PPP,PPPoE,PPTP,L2TP, and ISDN connections. Basically, this feature allows you to connect RouterOS to a Radius Server, and then, utilize the user database from the server for client authentication.
In our example, we will showcasefreeradius/freeradius-serverimage installation.
# Summary
Sub-menu:/container
```
/container
```
note:containerpackage is required.
Make sure to study ourcontainerguide before proceeding with the configuration. Make sure to check thedisclaimerandrequirementssections to understand all the risks and necessary steps you might be required to do.
At the time, when the guide was published, the image was available for linux/amd64OS/architectureonly. Meaning, you are not able to run this scenario on our arm32-bit and arm64-bit architecture RouterOS devices. For arm64, arm you will need to make your own container fromFreeRADIUS source.
You can only run it onCloud Hosted Router, CHR, or x86 installation.
To help you set up a CHR in aVirtual Box, please check ouryoutube tutorial, orMake your own x86 router.
# Configuration
## Container mode
Enable container mode:
```
/system/device-mode/update container=yes
```
You will need to confirm the device-mode with a cold reboot if using the container on X86.
## Networking
Add veth interface for the container:
```
/interface/veth/add name=veth3 address=172.17.0.2/24 gateway=172.17.0.1
```
Create a bridge for the container, assign an IP network to it, and add veth to the bridge:
```
/interface/bridge/add name=dockerfreeradius
/ip/address/add address=172.17.0.1/24 interface=dockerfreeradius
/interface/bridge/port add bridge=dockerfreeradius interface=veth3
```
Setup NAT for outgoing traffic if required:
```
/ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.17.0.0/24
```
## Getting image
To simplify the configuration, we will get the image from an external library but you can also import it via the.tarfile.
Make sure that you have "Registry URL" set accordingly, limit RAM usage (if necessary), and set up a directory for the image:
```
/container/config/set registry-url=https://registry-1.docker.io tmpdir=pull
```
Pull image with the help of the command:
```
/container/add remote-image=freeradius/freeradius-server:latest interface=veth3 root-dir=freeradius logging=yes cmd="-X"
```
wherecmd="-X"enables debug logging (per the "freeradius" documentation).
```
cmd="-X"
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
## Altering the server's configuration files
To access the server's configuration files (clients.confandauthorize), we will need to use SFTP (file transfer over SSH) protocol, so make sure that SSHserviceis enabled.
Open your command terminal ("CMD", as Administrator, for Windows users, or "Linux Shell or Command Terminal" for Linux users) and navigate it to the directory where you want to download the configuration files. For example, to "radius" folder on your "Desktop":
```
C:\WINDOWS\system32>cd C:\Users\Administrator\Desktop\radius
C:\Users\Administrator\Desktop\radius>
```
Initiate SFTP to the device's IP address:
```
C:\Users\DenissPC\Desktop\radius>sftp admin@10.55.8.53
admin@10.55.8.53's password:
Connected to 10.55.8.53.
sftp>
```
Go to the server's configuration file folder (usedirorlscommand to see the content of the folder you are in andcdcommand to go to the folder of our choice).
```
dir
```
```
ls
```
```
cd
```
The first file, "clients.conf" allows you to define RADIUS clients. Per the "freeradius" documentation, it should be under the "/etc/freeradius" directory...so, navigate there and usegetcommand to download it:
```
get
```
```
sftp> dir
freeradius          pub                     pull                    skins                   
sftp> cd freeradius/etc/freeradius
sftp> dir
README.rst          certs               clients.conf        dictionary          experimental.conf   hints               
huntgroups          mods-available      mods-config         mods-enabled        panic.gdb           policy.d            
proxy.conf          radiusd.conf        sites-available     sites-enabled       templates.conf      trigger.conf        
users
sftp> get clients.conf
Fetching /freeradius/etc/freeradius/clients.conf to clients.conf
/freeradius/etc/freeradius/clients.conf                                               100% 8323     1.2MB/s   00:00
```
Open "clients.conf" via your preferred text editor (notepad or any other). You can study the file to see all the options that you have (additionally, checkfreeradius.org). This example shows a basic setup, so, we will just overwrite the whole file with the lines shown below:
```
client new {
    ipaddr = 0.0.0.0/0
    secret = client_password
}
```
where we indicate, that our radius client can connect using any possible IP address (ipaddr=0.0.0.0/0ensures that, but you also can change it to the actual ip address/mask of your radius client if you require to do so) and that our secret is "client_password" (you can change it to any other secret).
Save the file/overwrite it.
The second file, "authorize" allows you to set up users. Per the "freeradius" documentation, it should be under "/etc/freeradius/mods-config/files". Go there andgetthe file:
```
get
```
```
sftp> dir
freeradius          pub                     pull                    skins                    
sftp> cd freeradius/etc/freeradius/mods-config/files
sftp> dir
accounting  authorize   dhcp        pre-proxy
sftp> get authorize
Fetching /freeradius/etc/freeradius/mods-config/files/authorize to authorize
/freeradius/etc/freeradius/mods-config/files/authorize                                100% 6594     1.1MB/s   00:00
```
Open "authorize" via your preferred text editor (notepad or any other). This example shows a basic setup, so, we will just uncomment (remove the "#" symbol from) the line shown below (leave the rest of the configuration/lines as they are):
```
bob	Cleartext-Password := "hello"
```
which creates a username "bob" and sets the password to "hello" (you can change the username and password).
Save the file/overwrite it.
Upload both files back/overwrite the default files with the help of theputcommand:
```
put
```
```
sftp> dir
freeradius          pub                     pull                    skins      
sftp> cd freeradius/etc/freeradius
sftp> dir
README.rst          certs               clients.conf        dictionary          experimental.conf   hints               
huntgroups          mods-available      mods-config         mods-enabled        panic.gdb           policy.d            
proxy.conf          radiusd.conf        sites-available     sites-enabled       templates.conf      trigger.conf        
users
sftp> put clients.conf
Uploading clients.conf to /freeradius/etc/freeradius/clients.conf
clients.conf                                                                          100%   67    22.3KB/s   00:00
sftp> cd mods-config/files
sftp> dir
accounting  authorize   dhcp        pre-proxy
sftp> put authorize
Uploading authorize to /freeradius/etc/freeradius/mods-config/files/authorize
authorize                                                                             100% 6626     1.6MB/s   00:00
```
Restart the container:
```
/container/stop 0
/container/start 0
```
Make sure to wait for the container to stop (status=stoppedshould be shown after using/container/printcommand) before initiating it again.
```
status=stopped
```
```
/container/print
```
# Result verification
In RouterOS, add a new RADIUS client configuration:
```
/radius/add service=login address=172.17.0.2 secret="client_password"
```
,where theaddressis the IP address of the veth3 interface,secretis the secret that we configured in theclients.conffile andserviceis the allowed service that you wish to use.
```
address
```
```
secret
```
```
service
```
Allow "login" with RADIUS users via the command:
```
/user/aaa/set use-radius=yes
```
We have allowed the "login" service for the RADIUS and we can test it using ssh/winbox/webfig connection. For SSH test, issue the command (where you need to indicate the device's management IP and input bob's password "hello" after):
```
/system/ssh 10.55.8.53 user=bob
```
You should be able to verify, that the terminal user changed from "admin@MikroTik" to "bob@MikroTik":
```
[admin@MikroTik] > /system/ssh 10.55.8.53 user=bob
password:hello                                                                                                                                                                 
  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK
  MikroTik RouterOS 7.8alpha173 (c) 1999-2023       https://www.mikrotik.com/
Press F1 for help
[bob@MikroTik] >
```
If you issue the command/user/active/print:
```
/user/active/print
```
```
/user/active/print
Flags: R - RADIUS
Columns: WHEN, NAME, ADDRESS, VIA
#   WHEN                  NAME   ADDRESS     VIA    
0   feb/16/2023 16:31:21  admin  xx.xx.xx.xx  winbox 
1   feb/16/2023 16:38:46  admin  xx.xx.xx.xx  console
2 R feb/16/2023 16:38:53  bob    10.55.8.53  ssh
```
you will be able to verify, that a new user "bob" is "active" and has a flag "R" assigned, which indicates it is a RADIUS user.