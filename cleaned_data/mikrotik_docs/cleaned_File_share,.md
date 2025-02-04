# Document Information
Title: File share
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/295239888/File+share,

# Content
File share function allows you to use your routers external storage to share files with anyone on the internet. Simply attach a USB, nVME or any supported drive to your device, and then add whole directory paths to the fileshare menu. The router will use the MikroTik cloud service to issue a HTTPS certificate and a domain name for your router. The URL which you can then distribute to anyone will be shown in the file-share menu. You can also enable ability for anyone to upload files into your router. The URL is randomly generated, so while it is available to anyone who knows the link, if you keep it safe, only people with the link will be able to use it.
# Adding shares
First, attach your USB drive and determine the file path of the directory you want to share:
```
[user@RouterOS] > file/print
# NAME                                                                           TYPE             SIZE LAST-MODIFIED
0 web                                                                            directory             2025-01-23 09:29:42
1 usb1                                                                           disk                  2025-01-22 09:45:57
2 pub                                                                            directory             2025-01-23 09:24:41
3 skins                                                                          directory             2024-12-10 08:19:27
4 pub/index.html                                                                 .html file        670 2025-01-23 09:24:41
5 skins/default.json                                                             .json file        151 2024-07-15 10:20:11
6 usb1/Secret Files                                                        	  directory             2024-03-18 09:01:41
7 usb1/forum                                                                     directory             2025-01-22 10:58:20
8 usb1/Secret Files/Home Video.srt                 							  .srt file         267 2020-06-01 11:29:14
9 usb1/Secret Files/Home Video.mp4                 							  .mp4 file   1584.4MiB 2020-06-01 11:34:33
10 usb1/forum/cat.jpeg                                                            .jpeg file  4307.7KiB 2025-01-22 09:38:55
11 usb1/forum/cat1.jpeg                                                           .jpeg file   231.8KiB 2025-01-22 10:58:20
12 usb1/forum/cat2.jpeg                                                           .jpeg file   129.6KiB 2025-01-22 10:58:20
13 usb1/forum/cat3.jpeg                                                           .jpeg file   263.8KiB 2025-01-22 10:58:20
14 usb1/forum/cat4.jpeg                                                           .jpeg file   438.4KiB 2025-01-22 10:58:20
15 web/index.html                                                                 .html file       1473 2025-01-23 09:29:42
```
Now in the ip/cloud menu go to file share, and add a new share, specifying theexpiration dateand whether the other user will have permission toupload filesto your router:
```
[user@RouterOS] /ip/cloud/file-share> add allow-uploads=no expires=never path="usb1/Secret Files/"
```
Now you can issue the print command to see if the share link has been made and what the URL is to copy for sharing:
```
[user@RouterOS] /ip/cloud/file-share> print
Columns: PATH, URL, DIRECT-URL, EXPIRES, DOWNLOADS
# PATH                      URL                                                        DIRECT-URL                                                    EXPIRES  DOWNLOADS
0 /usb1/Secret Files  https://acf017skgys.routingthecloud.net/s/4MPgHbEZCZYGVtp  https://acf017skgys.routingthecloud.net/s/4MPgHbEZCZYGVtp?dl  never            5
1 /usb1/Secrets      https://acf017skgys.routingthecloud.net/s/K8zkh1UjKuqtEQ0  https://acf017skgys.routingthecloud.net/s/K8zkh1UjKuqtEQ0?dl  never            2
[user@RouterOS] /ip/cloud/file-share>
```
Now, if you copy the "URL", you can share it with other people, regardless of where they are located, and regardless of whether your router has a public IP or not.
When you send the URL to a friend, they can then see all the files in the shared directory and can download them. If you enabled uploads in the share creation process, they can also upload files into your router. Keep this URL safe, or specify "expires" date to avoid other people accessing these files.
Property | Description
----------------------
enable(Default) | Enables the File Share function. The File Share service will be activated when the first share is added. If no shares are present, the File Share service remains disabled.
disable | Disables the File share function.
allow-uploads(yes | no;Default:no) | Enables the option for anyone to upload files to your router.
expires | Share expires date. Format: ISO 8601 (2025-01-25 00:00:00)Example: /ip/cloud/file-share set 0 expires="2025-01-25 07:15:00"
path | Sets the path for the file to be shared.Example: "/ip/cloud/file-share/add path=mypath/myfile"
Enables the File Share function. The File Share service will be activated when the first share is added. If no shares are present, the File Share service remains disabled.
Enables the option for anyone to upload files to your router.
Share expires date. Format: ISO 8601 (2025-01-25 00:00:00)Example: /ip/cloud/file-share set 0 expires="2025-01-25 07:15:00"
Sets the path for the file to be shared.
Example: "/ip/cloud/file-share/add path=mypath/myfile"
# WinBox GUI
To share the file, access the "File Shares" menu located under the IP → Cloud "Configuration" section.
To create a new share, set the "Path", "Expires" and "Auto uploads" options.
```
[admin@MikroTik] > ip/cloud/file-share/print detail
Flags: X - disabled; I - invalid
0    path=/mypath/myfile allow-uploads=no expires=2025-01-25 07:15:00 key="*********"
url="https://*********.routingthecloud.net/s/*********" direct-url="https://*********.routingthecloud.net/s/*********"
downloads=0
```
File share uses HTTPS (TCP port 443), but if you have manually configured WebFig to also use HTTPS, File Share will then automatically work only though our cloud relay service, since there can not be two things using the same port in one device. By default www-ssl is not enabled, so File Share works directly by default, without using the relay for downloads. Enabling file share will not in any way affect your WebFig confguration and will not open it to the world.
In the case of the File Share feature, when a user wants to share a file with somebody, this is the order of operation, if your router is directly accessible from the internet (checked by the Relay server):
# Relay service
If device is not directly accessible from the internet, it will choose to use the MikroTik hosted Relay service.
* Relay has no way of decrypting your data, because certificate with private key is on the router only