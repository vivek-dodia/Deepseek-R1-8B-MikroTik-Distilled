# Thread Information
Title: Thread-213132
Section: RouterOS
Thread ID: 213132

# Discussion

## Initial Question
Hello dear Friends !Ac2 had ros 7.16.1 only.No other packages !Free space was approx 1.8 mb.Due to global power on\off cycles it s been reset somehow.I have a 1 week old bin backup, size approx 1 mb, which seems to be a salvation.But its not ...Many times I tried to restore bin backup - no luck.It boots up with empty config.I did netinstall 7.16.2 with no problems.Then did upgrade and many times tried to restore bin backup from internal flash - no luck.From ext usb flash - no luck.Ac2 just boots up with no config.Only address lists are loaded (12k records).Used space 13.6 of 16 mbMy guess is that something happens during restore, may be not enough space ?For config of for logs?Unfortunately I dont have rsc.Any advise?Thank you beforehand. ---

## Response 1
I've just loaded (restored) a backup saved on a hAP ac² running 7.16.1 on a CHR running 7.16.2 that I have cloned for the purpose and equipped it with 5 Ethernet interfaces. To my surprise,/exportshows even the configuration of the wifi interfaces that do not exist on the CHR. For even better results than I've got, before starting the CHR for the first time, you have to set the MAC addresses of the virtual Ethernet interfaces to those the real hAP ac² uses, because the machine will expect these to be present after the restore and if it cannot see them, it will create ether6 to ether10 instead and the configuration items that refer to ether1 to ether5 will end up hanging in the air, i.e. refer to*3and alike that cannot be easily mapped to the original interface names.That said - if you give the CHR 512 MByte of RAM, there will definitely be no memory issue, and I have just confirmed that this kind of unhinged restore is possible. So if it fails on you, the reason why the backup load on the hAP ac² itself fails in your case is that the contents of the backup file is corrupt. ---

## Response 2
I'm having the same problem with my AC2 ---

## Response 3
"The same" including the fact that your enchanted configuration contained a huge amount of address list items and that's the only part that got restored? ---

## Response 4
So if it fails on you, the reason why the backup load on the hAP ac² itself fails in your case is that the contents of the backup file is corrupt.Thank you.You are right.I found a bit older binary backup (even larger size), and succesfully managed to recover with no problems to 7.16.2 ---

## Response 5
HI, For this main reason about the ridiculous 16MB flash, i avoid theses.And for backup config, i always theses two commands and after, trough scp, i get theses files :[*] /system/backup/save dont-encrypt=yes name=xxx.backup[*] /export show-sensitive file=xxx.rscThis allow with the .backup to restore easily to the same dev ; and with the rsc to have a human readable cfg.For example, i've a damaged CRS326 and just ordered for a CRS328.... i'm happy to have the .rsc for easier rewrite and custom for the new dev/model. ---