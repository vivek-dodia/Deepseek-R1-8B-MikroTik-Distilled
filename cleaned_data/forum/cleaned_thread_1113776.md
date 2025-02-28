# Thread Information
Title: Thread-1113776
Section: RouterOS
Thread ID: 1113776

# Discussion

## Initial Question
UPDATEAfter further reading, it seems to me that what I have found is an issue with certain PXE clients and not Mikrotik's DHCP server implementation. Marking an end code with "FF" is done according to spec as perRFC 2132 section 3.2and my proposed workaround might cause problems, as every option is properly formatted with its length preceeding the option (RFC 2132 section 2) which, after implementing my workaround, is incorrect.UPDATE ENDHello, I would like to post a bugreport as well as workaround for an issue I found in Mikrotik RouterOS. It seems that DHCP server injects additional characters when using "DHCP Options" making certain systems unable to boot using PXE. I will forward this post to Mikrotik support, but I want to make it public for everyone, so if someone is facing similar issue, they will be able to apply my workaround.EnvironmentI created a setup for PXE boot using my Mikrotik RB5009UPr+S+ running latest RouterOS 7.16.2. I want to boot legacy BIOS and UEFI machines and I do want to host boot assets on my home NAS running Ubuntu Server 24.04.1 with tftpd-hpa. I used this blog post as a reference:https://dimitrije.website/posts/2024-03 ... tboot.htmlHere is my config:
```
/ip dhcp-serveraddaddress-pool=<snap>_POOLinterface=<snap>_VLAN lease-time=4w2dname=<snap>_DHCP/ip dhcp-server optionaddcode=67name=boot-file-pxe-biosvalue=s'pxelinux.0'addcode=67name=boot-file-pxe-uefivalue=s'grubnetx64.efi'/ip dhcp-server option setsaddname=boot-pxe-uefi options=boot-file-pxe-uefiaddname=boot-pxe-bios options=boot-file-pxe-bios/ip dhcp-server matcheraddaddress-pool=<snap>_POOL code=60matching-type=substring name=if-client-arch-is-legacy-then-boot-bios option-set=boot-pxe-bios server=<snap>_DHCPvalue=\PXEClient:Arch:00000/ip dhcp-server networkaddaddress=<snap>.0/24comment=defconf dhcp-option=boot-file-pxe-uefi dns-server=<snap>.2domain=pmrlan gateway=<snap>.128next-server=\<snap>.69Some options were cut due to privacy concerns. Careful reader might also notice, that I am using a little different method for detecting BIOS/UEFI boot than described in the blog post, as solution described there didn't work for me.TestingNow, the config above seems to work on most devices, but not all, as there are certain systems that refuse to boot. Here are the results of my testing (all of this is using integrated NICs unless stated otherwise):* Asus P4C800-E Deluxe - ok* Asus P8Z77-V legacy - ok* Dell Precision 3571 UEFI - ok* VirtualBox BIOS - ok* VirtualBox UEFI - ok* Gigabyte H97N-WiFi UEFI - fail (the same result on both integrated NICs)h97n_wifi_fail.jpg* Asus B650E-E legacy with chinese Fenvi AQC113 NIC - failb650e_e_fail.jpgProblemAfter some investigation using Wireshark, it turns out that RouterOS adds "ff" to every payload when using DHCP Options. When using Boot File Name to define boot filename, the same behavior is not observed and it makes B650E-E boot properly, but also doesn't allow for flexibility of booting both UEFI and legacy BIOS devices.dhcp_options.pngBoot_file_name.pngWorkaroundAs for the workaround. According toMikrotik's documentation, it's possible to use pure hex values in DHCP Options. By using hex values and appending "00" to hex representing the filename in DHCP, it pushes the "ff" by one octet and makes affected system boot with DHCP Options used and, as such, allows to keep possibility to boot UEFI and legacy BIOS devices.
```

```
addcode=67name=boot-file-pxe-biosvalue=0x7078656c696e75782e3000addcode=67name=boot-file-pxe-uefivalue=0x677275626E65747836342E65666900Resulting boot packet:workaround.pngAs you can see, "ff" is still there despite using hex values, so without "00" appended, I've seen the same behavior as when using strings.The good thing is, that this workaround should be permanent. Whenever Mikrotik fixes this bug, I assume the config with workaround applied should keep working just fine, but obviously I have no way of verifying that.Additional note: it's not required to use Option Matcher which I am using to boot both UEFI and BIOS devices. It's enough to just switch from "Boot File Name" to "DHCP Options" or "DHCP Options Set" to trigger this bug.I hope that someone will find this post useful.

---
```

## Response 1
As this is a user forum, you should post this tosupport@mikrotik.com ---

## Response 2
Referring to my first post:I will forward this post to Mikrotik support, but I want to make it public for everyone, so if someone is facing similar issue, they will be able to apply my workaround.Also, I provided an update at the top of my post. If someone more experienced than myself has proposal for a workaround that will not break the spec, I am all earsMy understanding of thespecis that whole DHCP Options definition should be terminated with "FF". It's just so happens that option "67" is the last one and that's why it's followed by "FF". Next thing that came to my mind was to define another option with number higher than 67. I browsedavailable optionsand '72 HTTP server' seemed pretty harmless. But after adding it to Option Set, there is no change in packet structure - option 67 containing bootfile name is the last one and option 72 is not passed.Does anyone have any ideas for these problematic clients? ---

## Response 3
FF = DHCP Option 255 (End). You don't need null-termination because the DHCP options are prefixed with their length.
```
Option:(67)BootfilenameLength:14Bootfilename:grubnetx64.efiOption:(255)EndOptionEnd:255Padding:00000000If you do want to null-terminate the string - the workaround can be simplified to this:
```

```
/ip dhcp-server optionaddcode=67name=boot-file-pxe-uefivalue="'grubnetx64.efi'0x00"addcode=67name=boot-file-pxe-biosvalue="'pxelinux.0'0x00"

---
```

## Response 4
I browsedavailable optionsand '72 HTTP server' seemed pretty harmless. But after adding it to Option Set, there is no change in packet structure - option 67 containing bootfile name is the last one and option 72 is not passed.According to the standard, a DHCP server only provides the options the client has requested. So if the client did ask for 67 but did not ask for 72, there's no wonder that the server did not send it despite being defined. ---

## Response 5
According to the standard, a DHCP server only provides the options the client has requested. So if the client did ask for 67 but did not ask for 72, there's no wonder that the server did not send it despite being defined.Right, thank you for clarification. Now that you mention it, it is quite obvious.FF = DHCP Option 255 (End). You don't need null-termination because the DHCP options are prefixed with their length.
```
Option:(67)BootfilenameLength:14Bootfilename:grubnetx64.efiOption:(255)EndOptionEnd:255Padding:00000000If you do want to null-terminate the string - the workaround can be simplified to this:
```

```
/ip dhcp-server optionaddcode=67name=boot-file-pxe-uefivalue="'grubnetx64.efi'0x00"addcode=67name=boot-file-pxe-biosvalue="'pxelinux.0'0x00"My concern with this workaround is that when you append this null character to the filename, it's going to change the length and might confuse some PXE clients ("pxelinux.0" has lenght "10", but with null added it's going to be 11 (hex 1A) and I assume some clients might not like it).The whole problem seems to be caused by certain clients handling the length the wrong way. I can tell that length is correct, but some PXE clients take "FF" as part of the filename. This is especially obvious on screenshot from H97N-WiFi mainboard which clearly displays and in turn, requests from TFTP server wrong filename.

---
```

## Response 6
You could try force=yes on dhcp option 72?https://help.mikrotik.com/docs/spaces/R ... POptions.1According to the DHCP protocol, a parameter is returned to the DHCP client only if it requests this parameter, specifying the respective code in the DHCP request Parameter-List (code 55) attribute. If the code is not included in the Parameter-List attribute, the DHCP server will not send it to the DHCP client, but since RouterOS v7.1rc5 it is possible to force the DHCP option from the server-side even if the DHCP-client does not request such parameter:
```
ip/dhcp-server/option/setforce=yes

---
```

## Response 7
My concern with this workaround is that when you append this null character to the filename, it's going to change the length and might confuse some PXE clients ("pxelinux.0" has lenght "10", but with null added it's going to be 11 (hex 1A) and I assume some clients might not like it).It seems that MT DHCP server currently operates according to standards. Which means that some DHCP clients are broken. If this is so, then changing the way MT DHCP server works is a no-go. However, if you know that some DHCP clients are broken and you know the work-around. you can set up DHCP server to do whatever is appropriate for any given client.BTW, if you'll manage to push another DHCP option (e.g. option 72), it'll be appended to existing option set ... and if DHCP client is severely brain-dead, it'll append option number ... if you'll use option 72, then it'll append 'H' (character with ASCII number 72 or 0x48). Options start with option number, next is length and then value of option follows. ---

## Response 8
Yup, I think I will call it a day. According to my testing:* When null-byte is appended to the string, every system mentioned in first post boots properly.* When option 72 is added/forced, mkx assumption was almost spot on. I performed the testing on H97N-WiFi since it displays the filename it attempts to load. Seems like it parses the packet until it finds null-byte, so it seems to disregard option length altogether. When I forced option 72, it passed... whole option as the filename, lol. So not only it added "H" character, but also whole IP server I put as an option "72" and "ÿ" character.What a mess, I am going to hold on to first workaround I tried, and if I find any system that will complain about it, I hope I will still remember what I did, haha. Sorry for implying that there might be something wrong with RouterOS, as I made assumptions without proper homework. If anything, now I think I know a little bit more, and maybe someone facing similar issue will find this thread useful. ---