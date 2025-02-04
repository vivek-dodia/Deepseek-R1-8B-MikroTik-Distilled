# Thread Information
Title: Thread-1122412
Section: RouterOS
Thread ID: 1122412

# Discussion

## Initial Question
Please help me!I'm a beginner, a few days ago I accidentally checked the deletion of the default configuration.And when I put it back to default, the mikrotik (mANTBox ax 15s) no longer displays the wifi configuration in 2GHz and 5GHz.I restored a backup (by a .backup configuration that I did), but nothing works.Currently, I can't see the configurations of the Channel, bands, etc. Which in my opinion causes me not to be able to see my wifi network on phone or others.Please help me!In PC, a screenshot in /interface/wifi.Please!Sincerely, Gaëtan ---

## Response 1
I sadly don`t have access to a mANTBox ax 15sSo I can not attempt and reproduce the Issue...Nevertheless, I would do another attempt to RESET the Device
```
/system/reset-configurationno-defaults=yes skip-backup=yesIf the Issue persist, i would attempt a reinstall via NETInstall

---
```

## Response 2
Could this device been compromised?Was it a backup of the identical (or same) device?I would netinstall the device (don't forget both packages):https://help.mikrotik.com/docs/spaces/R ... Netinstall ---

## Response 3
Thank you for your answers!Erilnde > Yes, the backup comes from this mikrotik.After reinstallation by Netinstall the mantbox (os version: 7.16) works a bit because sometimes and when I change the SSID of the wifi, the problem comes back, and I still have to launch my backup. It's going round in circles! ---

## Response 4
Export config tot txt file, move away from deviceCheck export for completenessNetinstall (yes, again)DON'T restore binary backup, it clearly has some errors in it and you are simply re-importing those.Apply config again block by block via terminal and copy-paste.In case of doubt, post the config here for review (remove private info, serial, passwds ... and please use code quotes when posting).[code] [/code] ---

## Response 5
Thank you for this good idea! I'll see about it ---

## Response 6
I followed the instruction fromHolvoet(that is, to reconfigure Mantbox and not to restore the backups); after checking Mantbox over several days, everything is normal so far. ---