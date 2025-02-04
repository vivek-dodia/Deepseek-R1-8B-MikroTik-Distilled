# Thread Information
Title: Thread-1120760
Section: RouterOS
Thread ID: 1120760

# Discussion

## Initial Question
Hey, maybe I was too fast with upgrading to 7.14 (recently released).I saw the changelog regarding SMB and a few posts about in the release thread but I'm unsure if I need to change the settings now.SMB was working before, now it's not accessible from Windows-Clients.I do not need to add the "rose-storage" package, since they moved SMB out of this package to the "standard" /IP/SMB-Package in order to update it, am I right?Anyway it's stuck here - is it for everyone or just my dumbness or is it lacking documentation at the moment?Thanks for any input and have a great weekend, Martin ---

## Response 1
Hi, try to removeold smb credentials from windowsalso if they are the same and use \\routerIP\shareforder URL format ---

## Response 2
Did this - sadly no joy. There were stored credentials and mapped drives, removed both and tried to map new.Behaves like SMB is not active at all on the routerboard ("Network share not found" - in German "Der Netzwerkpfad wurde nicht gefunden"). ---

## Response 3
SMB sharing worked for me on 7.13. Formatting too. On 7.14, if I try to connect to the SMB share, there is a kernel failure. Formatting does not work on 7.14, there is a kernel error when formatting FAT32. ---

## Response 4
my RB5009 just crashes on 7.14 when I try to access SMB share from my MacBook ---

## Response 5
Same error on AC3 and AX3. There is no error on RB3011.... ---

## Response 6
Same error on RB750. ---

## Response 7
Same problems using L009: SMB worked OK with 7.13.5; migrated to 7.14 I get the error "The remote device doesn't accept the connection" from Windows.The USB unit is there and is recognized by L009: the MINIDLNA server (container) that uses it is still working (fortunately).Update March 127.14.1 does not solve the problem. ---

## Response 8
Same error on RB750Gr3 and RBD52G-5HacD2HnD ---

## Response 9
I updated to 7.14.1. The error is gone. ---

## Response 10
I raised a ticket to support. its working after disabling encryption on the share (require-encryption=no).When it's (officially) fixed and confirmed, I'll update. ---

## Response 11
SMB not working, i have the same error: "The remote device doesn't accept the connection" from Windows /it is also not working from linux/.EDIT: i simply tried to add DOMAIN and COMMENT in SMB settings..and now is working. Weird... ---

## Response 12
Had to turn SMB off, otherwise my rb4011 was rebooting every few hours. ---

## Response 13
This is so weird. Running 14.1 - had add comment in SMB settings - then it started to work. Mikrotik AX3. ---

## Response 14
This is so weird. Running 14.1 - had add comment in SMB settings - then it started to work. Mikrotik AX3.Yup, same thing did fix my problem. RBD52GBut listen to this, if you remove the comment, it stops working, and if you type the same comment again it still does not work. You need to type a new comment (different that the previews one) and it works again. ---

## Response 15
Is there any news on this problem? I experienced this today.I am on 7.15.3 and tried for the first time an SMB share. (encryption enabled and share is on an SSD/USB)After accessing the share from my client the switch completely crashes.Still necessary workaround with comment or no encryption?Edit:Last test, after disabling encryption and setting an comment, it does work! ---

## Response 16
my RB5009 just crashes on 7.14 when I try to access SMB share from my MacBookI've tried sharing USB drive contents (a 32GB ext4 formatted one) on 7.15.3 and accessing the share from Windows 10 resulted with router rebooting itself, we might have experienced the same issue.Had to turn SMB off, otherwise my rb4011 was rebooting every few hours.With SMB turned off it's perfectly stable for me. I wonder what SMB implementation does RouterOS use, I've had weirdly similar issues with devices using older ksmbd version before. ---

## Response 17
Posting "same here" does not help anyone.We are using SMB ourselves here and there have been no issues at all, so we need a lot of detailed info. Every step, every command that you use to configure SMB in the router. And then every detail about when you connect to it. Also, try the latest version, which is 7.16rc2 ---

## Response 18
my RB5009UG+S+ just crashes on 7.15.3 when I try to access SMB share from my Windows, the usb drive Kingston DataTraveler 3.0 even self disconnects after while, I am running adguard and homeassistent as containers on the usb drive ---

## Response 19
Posting "same here" does not help anyone.We are using SMB ourselves here and there have been no issues at all, so we need a lot of detailed info. Every step, every command that you use to configure SMB in the router. And then every detail about when you connect to it. Also, try the latest version, which is 7.16rc2Hi, here is my very simple config:
```
# 2024-11-08 21:37:53 by RouterOS 7.16.1
# model = RB5009UPr+S+
/ip smb shares
add directory=backup name=backup read-only=yes require-encryption=yes valid-users=guestWhen connecting from Windows with the username "guest", the router restarts, no matter if a password is set.When I set "require encryption" to no, the problem does not occur.

---
```

## Response 20
We are using SMB ourselves here and there have been no issues at all, so we need a lot of detailed info.Out of sheer curiosity: what SMB solution does MikroTik use, is it ksmbd (solution basically built in Linux kernel) or something custom?I will test SMB again on different device (L009UiGS-RM) and the same RB5009UG+S+IN I've tried before very soon, then report back my findings about its stability. ---

## Response 21
Hi, I think I have the exact same issue here, both on my RB5009 and on the hap-ax3.I'm using 7.16.2 firmware on all my devices, on the RB5009 I have an usb-stick connected to usb port and I share that one via smb (with domain set, comment set, user with password and no encryption). I can connect to the share, but as soon as I start putting files on the share the RB5009 crashes after few seconds. When I have winbox open, I see the cpu load slowly increases until it comes close to 100%, also the memory used slowly increases to just few MiB left as free, and then it crashes.I've also tried the same on my hap-ax3, same firmware, same settings, only using and external harddrive instead of usb-stick, also here I can connect but the hap-ax3 crashes as soon as I start putting files on the share.I'm trying to set these devices as a backup for my home-server (proxmox with several vm's) but sadly can't get this to work reliably, the mikrotiks keep crashing when a backup starts from proxmox.Any idea if this can be fixed somehow ?Thanks, Herman ---

## Response 22
When I set "require encryption" to no, the problem does not occur.Problem seems to be fixed in v7.17
```
*) smb - stability improvements for client/server;

---
```

## Response 23
In the meantime I circumvented the issue and installed the rose-storage package, disabled smb and enabled nfs file share.That doesn't crash the mikrotik devices and is also usable as a remote backup for proxmox.But thanks anyway for pointing out, I will give it a try with the new version, btw: releasenotes for this new version is rather impressive.... ---

## Response 24
Yesterday I have upgraded from 7.16.2 -> 7.17. So far so good I thought. Until I found out that I cannot access my SMB shares through Android, iPhone, iPad, Google TV. When I open it with my WIndows 11 PC or Kali Linux there is no problem.Once I input my username and password from the not working OS's -> I can see the shared folders, but I cannot access their content. Going to downgrade back to 7.16.2 to see if it helped. ---