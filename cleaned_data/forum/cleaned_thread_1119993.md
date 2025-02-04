# Thread Information
Title: Thread-1119993
Section: RouterOS
Thread ID: 1119993

# Discussion

## Initial Question
HiHow Can Using a Mikrotik router to PXE Boot?Thank you ---

## Response 1
- setup DHCP server with the required options for your client- add storage to your router for the required bootfiles (USB stick, SD card, M.2 card, whatever fits your router)- put required bootfiles on the storage- configure TFTP service with these files ---

## Response 2
- setup DHCP server with the required options for your client- add storage to your router for the required bootfiles (USB stick, SD card, M.2 card, whatever fits your router)- put required bootfiles on the storage- configure TFTP service with these filesI did itBut Error Number 0 is displayed in the Mikrotik log! ---

## Response 3
Hello, Really interested in a solution. Trying to setup a PXE boot server. For initial testing I've setup a standalone network on a CCR1009. OS 6.40.8.4 ports in a bridge to a DHCP server for a single LAN 192.168.0.0/24. DHCP lease scope 192.168.0.10-50. Options set for PXE boot, but this doesn't really matter yet since I'm first just trying to get the tftp to work.... There's no firewall or routing.Used the CCR to format an SD card fat32. Used the FTP protocol to copy the files from another working PXE server. The files are located in disk1/tftpboot . (again need to focus on tftp first)I've used several dozen versions of the syntax to setup the tftp server. (Also MS Windows native tftp client, and a third party download)./ip tftp add allow-rollover=yes real-filename=disk1/tftpboot/ req-filename=.*Just to try and get some success I tried/ip tftp add allow-rollover=yes real-filename=disk1/tftpboot/pxelinux.0 req-filename=pxelinux.0Sometimes I specify the 192.168.0.0/24 for allowed. Sometimes I specify 0.0.0.0 Most of the time I leave this blank.There are three result...ERROR code;0 string:permission denied!orERROR code:1 string: file no found (typically when I deliberately GET something invalid like a file I know isn't there)ERROR code: 8 (no other text after this. (This occurs when I boot a NUC on this LAN, which indicates DHCP is working.).When I specify a req-filename (specific or wildcard) the tftp GET fails immediately (usually with permission denied)If I don't specify any req-filename the GET command has to time out or exhaust all retries.Ultimately I would like a blank (or wildcard) req-filename parameter, and a real-filename parameter that sets disk1/tftpboot folder as the TFTP root....This shouldn't be hard.Anyone out there have any success with this.ThanksKevin ---

## Response 4
Well, I consider it brave to try that. Good luck!I have some experience with making a PXE server work, to install Windows from the network starting with a PXEboot (and then starting a dialog with pxelinux, user selects and enters some options, finally setup is loaded and started).This all without using Microsoft's tools that work only on Windows Server (which we don't have).I got it all working (on a Linux server) but there so many small details and tricks that I would not even think of implementingthis on RouterOS....When you want to use it to install Windows I also wonder how you implement the Boot Information Negotiation Layer?(I use a Python program called binlsrv2.py for that, but I would not know how to do that on RouterOS)Easy solution: do it on a Raspberry Pi. ---

## Response 5
Hello, Really interested in a solution. Trying to setup a PXE boot server. For initial testing I've setup a standalone network on a CCR1009. OS 6.40.8.4 ports in a bridge to a DHCP server for a single LAN 192.168.0.0/24. DHCP lease scope 192.168.0.10-50. Options set for PXE boot, but this doesn't really matter yet since I'm first just trying to get the tftp to work.... There's no firewall or routing.Used the CCR to format an SD card fat32. Used the FTP protocol to copy the files from another working PXE server. The files are located in disk1/tftpboot . (again need to focus on tftp first)I've used several dozen versions of the syntax to setup the tftp server. (Also MS Windows native tftp client, and a third party download)./ip tftp add allow-rollover=yes real-filename=disk1/tftpboot/ req-filename=.*Just to try and get some success I tried/ip tftp add allow-rollover=yes real-filename=disk1/tftpboot/pxelinux.0 req-filename=pxelinux.0Sometimes I specify the 192.168.0.0/24 for allowed. Sometimes I specify 0.0.0.0 Most of the time I leave this blank.There are three result...ERROR code;0 string:permission denied!orERROR code:1 string: file no found (typically when I deliberately GET something invalid like a file I know isn't there)ERROR code: 8 (no other text after this. (This occurs when I boot a NUC on this LAN, which indicates DHCP is working.).When I specify a req-filename (specific or wildcard) the tftp GET fails immediately (usually with permission denied)If I don't specify any req-filename the GET command has to time out or exhaust all retries.Ultimately I would like a blank (or wildcard) req-filename parameter, and a real-filename parameter that sets disk1/tftpboot folder as the TFTP root....This shouldn't be hard.Anyone out there have any success with this.ThanksKevinStill not working in ROS 7.10. The error is still the same "permission denied!", in the log it appears as:ERROR code:0 string:permission denied!If i increase the logging to DEBUG, an additional line appears before:requested file(binary): pxeboot access: deniedthis is strange as there is no permission setting in the router.I i use a different external tftp server there is no problem to get the boot file, but this SHOULD work on ROS. ---

## Response 6
Hello, Really interested in a solution. Trying to setup a PXE boot server. For initial testing I've setup a standalone network on a CCR1009. OS 6.40.8.4 ports in a bridge to a DHCP server for a single LAN 192.168.0.0/24. DHCP lease scope 192.168.0.10-50. Options set for PXE boot, but this doesn't really matter yet since I'm first just trying to get the tftp to work.... There's no firewall or routing.Used the CCR to format an SD card fat32. Used the FTP protocol to copy the files from another working PXE server. The files are located in disk1/tftpboot . (again need to focus on tftp first)I've used several dozen versions of the syntax to setup the tftp server. (Also MS Windows native tftp client, and a third party download)./ip tftp add allow-rollover=yes real-filename=disk1/tftpboot/ req-filename=.*Just to try and get some success I tried/ip tftp add allow-rollover=yes real-filename=disk1/tftpboot/pxelinux.0 req-filename=pxelinux.0Sometimes I specify the 192.168.0.0/24 for allowed. Sometimes I specify 0.0.0.0 Most of the time I leave this blank.There are three result...ERROR code;0 string:permission denied!orERROR code:1 string: file no found (typically when I deliberately GET something invalid like a file I know isn't there)ERROR code: 8 (no other text after this. (This occurs when I boot a NUC on this LAN, which indicates DHCP is working.).When I specify a req-filename (specific or wildcard) the tftp GET fails immediately (usually with permission denied)If I don't specify any req-filename the GET command has to time out or exhaust all retries.Ultimately I would like a blank (or wildcard) req-filename parameter, and a real-filename parameter that sets disk1/tftpboot folder as the TFTP root....This shouldn't be hard.Anyone out there have any success with this.ThanksKevinStill not working in ROS 7.10. The error is still the same "permission denied!", in the log it appears as:ERROR code:0 string:permission denied!If i increase the logging to DEBUG, an additional line appears before:requested file(binary): pxeboot access: deniedthis is strange as there is no permission setting in the router.I i use a different external tftp server there is no problem to get the boot file, but this SHOULD work on ROS.I tried removing the IP address parameter as this is like an ACL, but now the error is: Error 8 (no more info) ---

## Response 7
tftp error code explained:https://docs.ruckuswireless.com/fastiro ... 014D2.htmlhope this helps. ---

## Response 8
```
/ip dhcp-server optionaddcode=66name=boot-servervalue="IP_of_PXE_Server"addcode=67name=boot-filevalue="pxelinux.0"

---
```

## Response 9
Hello all, I would like to contribute to this discussion what it is I found necessary to get TFTP network boot to work for those struggling. I hope this helps out.BestAs a foundation, I am using a server w/ Proxmox 8.0.4. I've set up a LXC container running Docker and the netboot.xyz image to serve as my TFTP Server. Then I can configure a VM to network boot. It works just as well for bare metal hardware client.For reference to the netboot.xyz:Linuxserver.ioRouterOS Config:As @jonnes86 pointed out, you need to set some DHCP Options. Notice, though, you have to be specific in the value formats or RouterOS will complain it's not a valid entry with
```
"... Unknown data type"Notice the double quote around a single quoted string.  You then configure anOption Setto include both of the Options defined.  Then, you need to update one, any or all of your Networks to include aNext Server, which points to your PXE server IP and select theDHCP Option Setyou configured.  Alternatively, you can skip the Option Set and select theDHCP Optionsthemselves.  I don't understand why it's necessary to select a Next Server when it's already been defined in an Option Set and by virtue of the fact that you've set the DHCP Open Set (or DHCP Options) it should already know you're configuring the Network to point to a TFTP Server, but oh well.CLI method:
```

```
/ip dhcp-server optionaddcode=66name=pxe-boot-servervalue="'10.13.37.113'"addcode=67name=boot-filevalue="'netboot.xyz.kpxe'"/ip dhcp-server option setsaddname=NetworkBootoptions=pxe-boot-server,boot-fileSet the needed changes to the network(s) entry to include next-server and dhcp-option-set (or dhcp-option alternatively)
```

```
/ip dhcp-server networkaddaddress=10.13.37.0/24dhcp-option-set=NetworkBootdns-server=10.0.2.11,10.0.2.12,1.1.1.1gateway=10.13.37.1\next-server=10.13.37.113GUI Method:

---
```

## Response 10
I seem to be having a similar issue. My router is set up the way it's described here and yet, I get:>>Start PXE over IPv4.Station IO address is 172.16.0.9Server IP address is 172.16.0.13NBP filename is netboot.xyz.kpxe <-- here it adds an 'y' with umlauts that I am unable to retype here (see screenshot)... why???NBP filesize is 0 BytesPXE-E23: Client received TFTP error from serverWhat am I doing wrong?Any ideas are more than welcome!!Annotation 2025-01-18 190719.jpgyet no y with umlauts in the config:Annotation 2025-01-18 190938.jpg ---

## Response 11
Did you try from the CLI to set the DHCP Option? I suppose it's possible winbox/webfig used ߵsmartquoteߴ or some unknown Windows locale/code-page/keyboard thing in winbox...This will explicitly update any existing entry, if any unicode was present the CLI will strip it.
```
/ip dhcp-server optionset[find code=67name=boot-file]value="'netboot.xyz.kpxe'"

---
```

## Response 12
' (apostrophe) in AltCODE is entered as 0255 (4 digits) but German ÿ is Unicode 00FF so IMHO if there is an apostrophe in the filename then it becomes y umlat in Unicode as 255 = 0xFF and 0 is just 0. Seems that it could be an error but maybe the "consumer" side misunderstands the received data. ---

## Response 13
I've set up everything from the CLI originally, I just did the screenshots from the GUI.I thought about that as the y with umlaut is Alt-0255 as I've learnedStill, it seems as it's not finding the appropriate file (length = 0). What could be wrong?Not to mention that based on the matchers, the selected file should be the efi file, not the kpxe...I'm redoing the whole config based on a working example... we'll see. ---

## Response 14
Ok, well the error is still the same with the brand new config. The only thing that is seemingly working now is that the matcher finally selects the right file so the error is now:Annotation 2025-01-18 231646.jpgI'm really lost.Client is a DELL PowerEdge R720... maybe that is the culprit? ---

## Response 15
Looks like if I create a new VM on my Proxmox server and set it to netboot with SeaBIOS (not uefi), that works.So the question I guess becomes why the DELL is refusing to netboot?Sorry for being this problematic ---

## Response 16
Semi-random thought, but do you really need a "multidot" filename?I know that the (good ol') '90's are long gone, but (still good ol') 8.3 filename can some times help.Only for the record, in the (again good ol') days of BartPe, XP USB booting, etc. it was a common saying "oh noes, it's a Dell!" as Dell PC's had their own non- standard behaviours both at BIOS and Windows drivers levels.The strange y can Indeed be a parsing error of some kind of the single quote/apostroph, but I have no idea if there Is a way to workaround It. ---

## Response 17
I actually didn't touch the filename, that's literally the default in netboot.xyzIt works in UEFI mode with the Proxmox VM. PfffI first got an error, but that was a setting on the Proxmox side ("Pre-Enroll Keys" had to be disabled in System/Advanced when creating the VM).I'm also starting to suspect it's a DELL thang ---