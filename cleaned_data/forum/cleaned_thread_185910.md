# Thread Information
Title: Thread-185910
Section: RouterOS
Thread ID: 185910

# Discussion

## Initial Question
Recently I started to get close to reaching my ISP data cap, so I wanted to track monthly bandwidth usage per each device behind my home router hAP ac2. I searched the forum and saw several ideas, but they weren't quite what I was looking for. So I wrote my own script that I would like to share with the community.Key featuresEverything is local on the router. You don't need any external servers or software to collect the data. You only need a computer to view the report.The script uses kid-control functionality in RouterOS, which has a nice bonus - tracking per IP bandwidth.I'm using it with a USB flash drive where I don't worry about write cycles. If your device doesn't support external storage, you could schedule the script to run less frequently (at the expense of more collected data loss due to unexpected reboots).LimitationsTested with RouterOS 7 only.Kid-control counts all inter-VLAN traffic, not just WAN. Potentially you could re-write the script and use something likeviewtopic.php?t=168427instead of kid-control.The HTML report (placed in the root of flash drive) has .txt extension - this is RouterOS limitation. You need to download the report from WinBox Files window and then remove .txt so that only .html is left. You could set up SFTP or FTP and use the fetch tool to rename it or upload/rename to another location on your network. There are some discussions about using the branding package for serving custom static web pages directly from the router. I haven't looked into that.RouterOS supports only integers, so report accuracy is +/-1GB. If you need more precision, you can modify the script to report in megabytes. Note, all calculation and saving is done in bytes, so there are no repeated rounding losses. The rounding (or rather truncating) happens only at the last step when the report is generated.How to useEnable bandwidth tracking in kid-control. With configuration below kid-control doesn't limit anything but starts tracking traffic.
```
/ip kid-controladdname=Monitormon=0s-1dtue=0s-1dwed=0s-1dthu=0s-1dfri=0s-1dsat=0s-1dsun=0s-1dInstall and format USB drive.Create a directory called "bandwidth" on it (the easiest way is to create a folder on your PC and drag into Winbox Files window). You can change the paths as needed by changing the script variables.Schedule the script to run every hour (or however often you like) at x:59:59. On the last day of the month at 23:59:59 the script will generate the final report for the month and won't touch it again. The next scheduled run will use the new month name for data files and the report.Here is how the report looks like:report.pngEdit: uploaded the revised script to address the new scripting date format and USB path.

---
```

## Response 1
very interesting, thank you for sharing ---

## Response 2
5. How to read report?can you do?http://your.router.ip/xxxx ---

## Response 3
I have already seen that line on Splunk... ---

## Response 4
Should be built into the router as a selectable function!! ---

## Response 5
You read the report by downloading it to your computer and removing .txt, so that the resulting file is report-2022may.html (for May). Then you can open it in any browser. It's a basic HTML with JavaScript leveraging Google Charts.You are correct, the script doesn't do any magic and fully relies on kid-control to provide the data. The main point is storing the data persistently without anything external. And also presenting the data in a friendly format. It is especially useful for users who don't have any servers/Raspberry PI's/NAS/etc running somewhere to collect the data. It's very simple to set up, just copy and paste the script.can you do?http://your.router.ip/xxxxIdeally, if RouterOS had the ability to serve custom static web pages, then it would be possible. Like I mentioned above, the branding package might do this but I haven't looked into that. ---

## Response 6
@anserk, just a little shout out that I am using your script on an SXT device used for internet access in a vacation home setup.MUCH prettier then simply mailing output from kid-control devices print stats ---

## Response 7
VERY interesting feature of kid-control. Replacing "IP accounting" ?TXS for the script!HOW to get the authenticated user (RADIUS) into this Kid-Control device list ?(Wifi AP authenticated via WPA2/Enterprise, Username value can be copied into Radius "MT Comment" attribute with User Manager 5, and remains visible in the Registration table, as long as the device is connected. DUDE collects in "RouterOS Info" all registration tables, including the comment field)The username/password is stored in the client device, and is never entered again for the same SSID. So this should be acting as automated RSSO (Radius single signon).But how to make Kid-control or Hotspot pick up this signon ? ---

## Response 8
If you downloaded the script before July 23 2022, please update line 35 from:
```
:localip[get$device ip-address]# To:localip[:tostr[get$device ip-address]]I recently ran into issue with traffic counter overflow on the report, messing up all statistics. It turns out when a device has multiple IP addresses, the script was grabbing wrong fields for traffic counters. The issue is resolved by forcing the whole IP field to a string.@bpwl I've never used RADIUS - wouldn't that authenticated user device get an IP from DHCP server? I don't know exactly how kid-control works under the hood, it seems to simply pick up devices by MAC address. Presumably anything that goes through the firewall, which is why it also counts traffic from one local VLAN to another. So as long as that user sends some traffic, it should be on the list. The difficult part is identifying who is who. If the device doesn't register a name with DHCP server, then only MAC and IP are shown. And with many phones (like Apple) periodically changing their MAC address, it becomes impossible to identify all devices accurately. So kid-control is quite a limited feature, but works well in simple configurations with mostly fixed number of devices.

---
```

## Response 9
The difficult part is identifying who is who.That's why I use RADIUS with EAP/PEAP wifi authentication (= username/password).The data is stored once in the device (until you 'forget" the wifi network in the known wifi network list.)Limits are then per user. Hotspot login does the same but with many APP as primary use, the browser popup for logging in is sometimes missed. And Hotspot cookies are just a means for avoiding repeated login actions for the same MAC.Whatever they do with the private MAC addresses, the user identification with EAP/PEAP is dependent on the stored login credentials only.RADIUS accounting would collect the usage per user, but that is mostly all (wifi) traffic, and the interesting part is the WAN usage only.RADIUS could give a specific range of IP addresses to one user. But when you have multiple network segments (eg VLAN) then it becomes more difficult.RADIUS could also force a specific VLAN for a user.RADIUS can be used for VPN, DHCP, Hotspot, wifi, and other services. But afaik only the wifi is persistent. (The device connects with that userwithout any interaction of the user, even when not around for more than a year, and when it comes with a different private MAC address.) ---

## Response 10
I would think if the same sort of info can be retrieved from the Radius part (incl. user name), the concept of the script can still be used. ---

## Response 11
RADIUS itself is a bid special in this. Is some device authenticated to what user or IP address? Is not easy to tell.RADIUS authentication is an event, that in the best case gets logged, username and MAC address of the AP. (not the client), in my case.De-authentication in de most cases does not involve the RADIUS server. (There is CoA, but mostlly the wifi disconnects, "reason=3" by AP, "reason=8" by roaming client, extensive data loss (client is gone or out of range?)) So the RADIUS authenticator cannot tell if a user is still authenticated or not, and does not have the IP address of the client.The AP maintains the registration (on MAC address) but does not register the user used for the authentication.The way RADIUS knows about the disconnect is through the RADIUS accounting. (User name , IP address, MAC address, quota consumed). But RADIUS misses sometimes an accounting record.Actually I'm using the old MT User Manager for collecting RADIUS accounting, even with another RADIUS server doing the authentication.Reason is that MT limits the number of accounted sessions to 19, for a L4 license. Accounting updates is set to someting like every 10 minutes.RADIUS authentication is quite central, for multiple AP, so the number of active sessions is likely above 19. Even L5 only allows for 50 sessions.I have 10.000 RADIUS authentications per day, caused by 40 named users, 100 client devices on 34 MT AP. There is a lot of roaming in that large 1 km2 area, also between 2.4 and 5GHz on the same AP. (Playing kids, indoor/outdoor swap, ...)Roaming can be every few seconds, and takes a split second. But steady clients their connections remain active for multiple days.DHCP lease in this does not interfere (roaming does not renew the lease). Lease time is 24h, most client devices keep the same IP for the whole holiday stay period.All data is there, but not correlated. DUDE collects the logs from (non-MT) RADIUS server, (non-MT) DHCP server, and MT AP's.MT User manager only can follow 19 Active sessions with license level L4, via RADIUS accounting. ---

## Response 12
I encountered another bug with the script. One device that showed up in kid-control didn't have an IP address. That empty field was screwing up the report. I added the fix to the attached script above. It's just one new line.
```
:if([:len $name]=0)do={:set$name"unknown"}:localip[:tostr[get$device ip-address]]:if([:len $ip]=0)do={:set$ip"no-ip"}<==newline:localdown[get$device bytes-down]:localup[get$device bytes-up]

---
```

## Response 13
Hi, your script works great and i really appreciate this tool that you providedI seemed to have messed up some of the older reports by moving them before the last day of the monthIs there anyway to generate the report with all the older raw data? (in Txt format and also still viewable in Kid Control)i am not familiar with Google Charts ---

## Response 14
Is there anyway to generate the report with all the older raw data? (in Txt format and also still viewable in Kid Control)The script uses the current date to produce the txt filenames, which are then used for generating the report. You can make a copy of the script and edit the line:
```
:localsysdate[/system/clock/getdate]Change it to a static date for older month. The format is jan/04/2023.As far as Kid Control goes, that data gets reset every time the script runs. So what you see there is only new data since the last run.

---
```

## Response 15
Thank you, Appreciate your expertise and assistance! ---

## Response 16
MIKROTIK PLEASE PLEASE INTEGTRATE THIS!!!!!!!! OR GIVE AS BACK IP ACCOUNTING!!!!!!! PLEASE PLEASE ---

## Response 17
So this works for me out of 3 of 4 Mikrotik(2 x RB3011 and 2 x RB1100AHx4) devices that i currently run themThe 4th one(RB1100AHx4) keeps giving me this error for the last 3 monthsThe only result generated in the html is belowDoes anyone has any idea what is the error? All the boxes were running ROS 7.6 and now ROS 7.7
```
<html><head><scripttype='text/javascript'src='https://www.gstatic.com/charts/loader.js'></script><scripttype='text/javascript'>google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawMultSeries);

function drawMultSeries() {
var data = google.visualization.arrayToDataTable([
['Device', 'Download', 'Upload', 'Total'],
 
failure: new contents too long

---
```

## Response 18
That errorfailure: new contents too longseems to imply you are running out of space somewhere. ---

## Response 19
Pity RB4011 does not have USB... ---

## Response 20
Without USB you can send information to an external server using Syslog ---

## Response 21
i tried to run on SXTsq Lite5 AC [6.48.6 (long-term) ]. i tried but i failed to setup this. I don't where i am getting stuck. No report generated. Can you please provide a video tutorial how to set it up?1st i do turn on kid control through you give the code [ /ip kid-control add name=Monitor mon=0s-1d tue=0s-1d wed=0s-1d thu=0s-1d fri=0s-1d sat=0s-1d sun=0s-1d ]and then2nd i go to script and then paste the whole code and run interval of 00:59:59 .nothing getting output. i change the directory according to me. i don't have external storage so i create a folder on Mikrotik and then i choose the path.Troubleshoot by me:I tried to run in scheduler not in script nothing happeni tried to paste the whole code in script and then run it through schulder.i tried to change the interval runtime to 10 sec to 1 min and 5min nothing results.Please make a video tutorial and the installation. Please. I need this very badly to track my own internet ussage without any external thing. ---

## Response 22
You can follow the steps to setup monitoring here:viewtopic.php?t=179960 ---

## Response 23
Kid-control doesn't seem to give accurate bandwidth usage information. I'm using 7.10 on an hap ac2 as a test. When I run a speedtest on my computer, I get about 100Mbps down and about 45Mbps up. Kid control is showing about 30Mbps down and kbps up.Is anyone else having the same issue? Does it seem to work with applications other than speedtest? It might just be showing one of the speedtest streams which would be a little unlucky.I am currently using torch which gives accurate information but it would be nice to use kidcontrol instead so I don't need to add up all the connections for the same IPs. ---

## Response 24
Thank you for your work, it works perfect.When I try to save the report to a shared drive (runs on SMB raspberrypi) using:local reportpath ("smb://user:password@192.168.3.19/home/pi/MyNASA/BWbyIP/report-" . $yearmonth . ".html")either with or without the user/passwordfailure: cannot open output fileIs it my smb syntax or elsewhere ? Thanks. ---

## Response 25
i tried to run on SXTsq Lite5 AC [6.48.6 (long-term) ]. i tried but i failed to setup this. I don't where i am getting stuck. No report generated. Can you please provide a video tutorial how to set it up?The script was developed and tested only for RouterOS 7. ---

## Response 26
Kid-control doesn't seem to give accurate bandwidth usage information. I'm using 7.10 on an hap ac2 as a test. When I run a speedtest on my computer, I get about 100Mbps down and about 45Mbps up. Kid control is showing about 30Mbps down and kbps up.Is anyone else having the same issue? Does it seem to work with applications other than speedtest? It might just be showing one of the speedtest streams which would be a little unlucky.I am currently using torch which gives accurate information but it would be nice to use kidcontrol instead so I don't need to add up all the connections for the same IPs.I don't think kid control is a good tool for watching live traffic utilization, it's probably averaging out the numbers. However, the count is accurate to the best of my knowledge.If you want to watch live traffic, I suggest using interface graphs or just interfaces window. ---

## Response 27
Thank you for your work, it works perfect.When I try to save the report to a shared drive (runs on SMB raspberrypi) using:local reportpath ("smb://user:password@192.168.3.19/home/pi/MyNASA/BWbyIP/report-" . $yearmonth . ".html")either with or without the user/passwordfailure: cannot open output fileIs it my smb syntax or elsewhere ? Thanks.RouterOS cannot use SMB shares as a client, unfortunately. There is the fetch tool that you can use to upload via SFTP, but to work with files you still need to keep them locally either in RAM or on USB drive. ---

## Response 28
Thank you for your work, it works perfect.When I try to save the report to a shared drive (runs on SMB raspberrypi) using:local reportpath ("smb://user:password@192.168.3.19/home/pi/MyNASA/BWbyIP/report-" . $yearmonth . ".html")either with or without the user/passwordfailure: cannot open output fileIs it my smb syntax or elsewhere ? Thanks.RouterOS cannot use SMB shares as a client, unfortunately. There is the fetch tool that you can use to upload via SFTP, but to work with files you still need to keep them locally either in RAM or on USB drive.ROSE package ??You can mount a SMB-share from your NAS and write it on there. ---

## Response 29
Recently I started to get close to reaching my ISP data cap, so I wanted to track monthly bandwidth usage per each device behind my home router hAP ac2. I searched the forum and saw several ideas, but they weren't quite what I was looking for. So I wrote my own script that I would like to share with the community.I just wanted to thank you for the script! I tried using Splunk and Grafana to get a simple total bandwidth usage per interface, but neither could calculate it out of the box. One suggestion: it would be great if the script could calculate the total bandwidth usage per interface listed as WAN. This would be helpful in scenarios where a WAN link is configured for failover. ---

## Response 30
hello thank your for script but my report show noting !!report-2025-01.html.txt:
```
<html><head><scripttype='text/javascript'src='https://www.gstatic.com/charts/loader.js'></script><scripttype='text/javascript'>google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawMultSeries);

function drawMultSeries() {
var data = google.visualization.arrayToDataTable([
['Device', 'Download', 'Upload', 'Total'],export of my kid-control :
```

```
/ip kid-controladdfri=0s-1dmon=0s-1dname=Monitorsat=0s-1dsun=0s-1dthu=0s-1dtue=0s-1dwed=0s-1d/ip kid-control deviceaddmac-address=00:0C:29:E6:CE:C1 name=device1 user=Monitoraddmac-address=00:0C:29:88:6E:85name=device3 user=Monitori have dynamic and static of kid-control device2025-01-ECBD1DEE6001.txt

---
```

## Response 31
Do you see any data collected in Winbox under Kid Control - Devices? My script just takes the data generated by Kid Control.Looking at the file you provided, I think there is something wrong with how you run the script. It should look like this (dummy data):00:00:00:DB:00:00, XBOXONE, 10.1.2.63, 4967533, 3788218, 8755751, ---

## Response 32
Do you see any data collected in Winbox under Kid Control - Devices? My script just takes the data generated by Kid Control.Looking at the file you provided, I think there is something wrong with how you run the script. It should look like this (dummy data):00:00:00:DB:00:00, XBOXONE, 10.1.2.63, 4967533, 3788218, 8755751, yes i have dynamic and static device in kid-controlHave I made a mistake?image.png ---

## Response 33
I suggest you black out MAC addresses as that is usually considered a privacy concern.As a troubleshooting step, open a Terminal window in Winbox and paste this code:It's just an excerpt from the script without saving anything to disk.
```
{/ip/kid-control/device:foreachdevicein=[find]do={:localmac[get$device mac-address]# Remove colons from MAC.:localmac2([:pick $mac02].[:pick $mac35].[:pick $mac68].[:pick $mac911].[:pick $mac1214].[:pick $mac1518]):localname[get$device name]# Empty names or IPs will cause issues when reading into array, so replace them.:if([:len $name]=0)do={:set$name"unknown"}:localip[:tostr[get$device ip-address]]:if([:len $ip]=0)do={:set$ip"no-ip"}:localdown[get$device bytes-down]:localup[get$device bytes-up]:localtotal($down+$up)# Save data as array:            0     1    2    3    4    5:put"$mac,$name,$ip,$down,$up,$total,"# End of for loop.}}It should produce a list of devices in the format I posted earlier.I suspect the issue is with IPv6 addresses having colons. I remember I had to remove colons from MAC addresses but never used IPv6. I will see what can be done about it.

---
```

## Response 34
I suggest you black out MAC addresses as that is usually considered a privacy concern.As a troubleshooting step, open a Terminal window in Winbox and paste this code:It's just an excerpt from the script without saving anything to disk.
```
{/ip/kid-control/device:foreachdevicein=[find]do={:localmac[get$device mac-address]# Remove colons from MAC.:localmac2([:pick $mac02].[:pick $mac35].[:pick $mac68].[:pick $mac911].[:pick $mac1214].[:pick $mac1518]):localname[get$device name]# Empty names or IPs will cause issues when reading into array, so replace them.:if([:len $name]=0)do={:set$name"unknown"}:localip[:tostr[get$device ip-address]]:if([:len $ip]=0)do={:set$ip"no-ip"}:localdown[get$device bytes-down]:localup[get$device bytes-up]:localtotal($down+$up)# Save data as array:            0     1    2    3    4    5:put"$mac,$name,$ip,$down,$up,$total,"# End of for loop.}}It should produce a list of devices in the format I posted earlier.I suspect the issue is with IPv6 addresses having colons. I remember I had to remove colons from MAC addresses but never used IPv6. I will see what can be done about it.thanks but no need to black out the mac address they are virtual made by vmware and any time i cant delete the mac addressoutput:
```

```
00:0C:29:E6:CE:C1,fgde1,212.xx.xx.193,13567097295,13314776453,26881873748,00:0C:29:6A:0F:48,fgus1,212.xx.xx.194,6787106593,6758910538,13546017131,00:0C:29:37:0D:A4,ubuntu,fe80::20c:29ff:fe37:da4;212.xx.xx.206,26387020,11721983,38109003,00:0C:29:F0:8E:A8,windows-2025,fe80::e720:e828:8548:a53;212.xx.xx.207,146270,176998,323268,00:0C:29:1F:96:A1,DetaBase,212.xx.xx.192,98202582,50713849,148916431,00:0C:29:88:6E:85,fgtr1,212.xx.xx.195,693958,2672979,3366937,00:0C:29:19:0F:40,fgfi,212.xx.xx.196,16335611419,16145100134,32480711553,00:0C:29:5E:9F:0D,fgfr,212.xx.xx.197,488893,2168415,2657308,00:0C:29:B1:1A:0B,fguk,212.xx.xx.198,1139875,2759023,3898898,EC:BD:1D:EE:60:01,unknown,85.x.xx.129,0,0,0,00:0C:29:E6:DB:46,unknown,fe80::20c:29ff:fee6:db46,0,0,0,00:0C:29:92:F0:93,unknown,fe80::20c:29ff:fe92:f093,0,0,0,00:0C:29:66:28:3A,unknown,fe80::20c:29ff:fe66:283a,0,0,0,00:0C:29:A0:83:CB,unknown,fe80::20c:29ff:fea0:83cb,0,0,0,00:0C:29:01:93:F0,unknown,fe80::20c:29ff:fe01:93f0,0,0,0,00:0C:29:F9:ED:AE,unknown,fe80::20c:29ff:fef9:edae,0,0,0,00:0C:29:1D:3B:01,unknown,fe80::20c:29ff:fe1d:3b01,0,0,0,00:0C:29:30:91:D8,unknown,fe80::20c:29ff:fe30:91d8,0,0,0,00:0C:29:AE:F9:F5,unknown,fe80::20c:29ff:feae:f9f5,0,0,0,00:0C:29:BD:1C:35,unknown,fe80::20c:29ff:febd:1c35,0,0,0,00:0C:29:92:DE:29,unknown,fe80::20c:29ff:fe92:de29,0,0,0,00:50:56:BC:AE:57,unknown,fe80::250:56ff:febc:ae57,0,0,0,00:0C:29:D2:D2:3C,unknown,fe80::20c:29ff:fed2:d23c,0,0,0,00:50:56:BC:57:97,unknown,fe80::250:56ff:febc:5797,0,0,0,00:50:56:84:4A:2B,unknown,fe80::250:56ff:fe84:4a2b,0,0,0,00:50:56:BC:A6:03,unknown,fe80::250:56ff:febc:a603,0,0,0,00:50:56:BC:0A:CF,unknown,fe80::250:56ff:febc:acf,0,0,0,00:0C:29:30:93:EA,unknown,fe80::20c:29ff:fe30:93ea,0,0,0,00:0C:29:DA:67:16,unknown,fe80::20c:29ff:feda:6716,0,0,0,I also deleted all devices that had IPv6 and ran the script, but the html file was still the same as before.output after remove ipv6 devices :
```

```
00:0C:29:E6:CE:C1,fgde1,212.xx.xx.193,840899749,830698808,1671598557,00:0C:29:6A:0F:48,fgus1,212.xx.xx.194,7922273387,7887784538,15810057925,00:0C:29:1F:96:A1,DetaBase,212.xx.xx.192,114360091,61259459,175619550,00:0C:29:88:6E:85,fgtr1,212.xx.xx.195,780762,3004863,3785625,00:0C:29:19:0F:40,fgfi,212.xx.xx.196,17739021198,17542112225,35281133423,00:0C:29:5E:9F:0D,fgfr,212.xx.xx.197,544288,2437490,2981778,00:0C:29:B1:1A:0B,fguk,212.xx.xx.198,1280800,3105035,4385835,

---
```

## Response 35
OK, please do me a favor and paste the following into the Terminal:
```
{:localsysdate[/system/clock/getdate]:globalyearmonth[:pick $sysdate07]:localreportpath("usb1-part1/report-".$yearmonth.".html"):localsavedir"usb1-part1/bandwidth"/ip/kid-control/device:foreachdevicein=[find]do={:localmac[get$device mac-address]:localmac2([:pick $mac02].[:pick $mac35].[:pick $mac68].[:pick $mac911].[:pick $mac1214].[:pick $mac1518]):localfilename($savedir."/".$yearmonth."-".$mac2.".txt")# If the file does not exist, create it using a workaround.:if([:len[/file/find name=$filename]]=0)do={/system/identity/printfile=$filename### Wait for the write to finish, otherwise "set" will fail later.:while([:len[/file/find name=$filename]]=0)do={:delay2}}/file/set$filename contents="$mac,testname,testip,5,5,10,"}}After this, all 2025-01-mac.txt files should have: "MAC,testname,testip,5,5,10,". This is just to prove that the file writes are taking place.

---
```

## Response 36
OK, please do me a favor and paste the following into the Terminal:
```
{:localsysdate[/system/clock/getdate]:globalyearmonth[:pick $sysdate07]:localreportpath("usb1-part1/report-".$yearmonth.".html"):localsavedir"usb1-part1/bandwidth"/ip/kid-control/device:foreachdevicein=[find]do={:localmac[get$device mac-address]:localmac2([:pick $mac02].[:pick $mac35].[:pick $mac68].[:pick $mac911].[:pick $mac1214].[:pick $mac1518]):localfilename($savedir."/".$yearmonth."-".$mac2.".txt")# If the file does not exist, create it using a workaround.:if([:len[/file/find name=$filename]]=0)do={/system/identity/printfile=$filename### Wait for the write to finish, otherwise "set" will fail later.:while([:len[/file/find name=$filename]]=0)do={:delay2}}/file/set$filename contents="$mac,testname,testip,5,5,10,"}}After this, all 2025-01-mac.txt files should have: "MAC,testname,testip,5,5,10,". This is just to prove that the file writes are taking place.I thank you for your support regarding this script.Sorry but it seems to be a mistake on my part.I don't have much knowledge in Mikrotik scripts and since I couldn't connect usb in the virtual machine I decided to delete "usb1-part1" but I didn't know that I even had to delete "/".I had made these changes in order:your script:
```

```
:localsysdate[/system/clock/getdate]:globalyearmonth[:pick $sysdate07]:localreportpath("usb1-part1/report-".$yearmonth.".html"):execute{:localsavedir"usb1-part1/bandwidth":localdownmonthly0:localupmonthly0:localgig1073741824my first change (delete "usb1-part1"):
```

```
:localsysdate[/system/clock/getdate]:globalyearmonth[:pick $sysdate07]:localreportpath("/report-".$yearmonth.".html"):execute{:localsavedir"/bandwidth":localdownmonthly0:localupmonthly0:localgig1073741824my second change (delete "usb1-part1/"):
```

```
:localsysdate[/system/clock/getdate]:globalyearmonth[:pick $sysdate07]:localreportpath("report-".$yearmonth.".html"):execute{:localsavedir"bandwidth":localdownmonthly0:localupmonthly0:localgig1073741824Is everything okay now

---
```

## Response 37
Great to hear! Yes, the reportpath is the variable to the report file location. The savedir is where text files with bandwidth data are stored between script executions.Keep in mind that on some (most?) devices a path location that is just in the root directory "/" means RAM. So, if the device is rebooted, all data stored there is lost. If you want to save to internal flash storage (I would be careful with that), you need to use /flash. See more here:https://help.mikrotik.com/docs/spaces/R ... 5971/FilesRouterOS now also has the ability to mount a remote share like SMB that you could use to store this data.https://help.mikrotik.com/docs/spaces/R ... torage-SMB ---