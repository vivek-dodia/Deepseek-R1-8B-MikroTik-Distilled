# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211612

# Discussion

## Initial Question
Author: Wed Oct 09, 2024 8:42 pm
Hi All, Just looking for a santiy check here before I go back to EE!I have a LtAP Mini (the new 2024 version) with an external antenna.EE as the network obviously.RSSI -77 dBmRSRP -92dBmSINR 2dBRSRW -13dBScreenshot 2024-10-09 131002.pngI've configured the APN for EE as "everywhere" with "eesecure" and "secure" as the username/password. Doesn't seem to matter if I use PAP or CHAP.Screenshot 2024-10-09 131033.pngI keep getting an internet IP of 254.128.0.0 and can't ping 8.8.8.8 for example on the lte1 interface.LTE interface is configured for bands 3 and 20. (I have tried specifying no bands, and it picks up Band1 (-86,-100, 3,-13 respectively on that band)Screenshot 2024-10-09 131148.pngCell monitor sees plenty of Cell ID's on Band 3.Screenshot 2024-10-09 131336.pngSeems like things are up, but not getting an IP. Can anyone suggest some troubleshooting please? ---

## Response 1
Author: Wed Oct 09, 2024 11:20 pm
If you put an APN manually, It Is ignored if the "use network APN" is ticked.Not to be overly critic of the good Mikrotik guys, but I think that GUI designer apprentices learn on the first or maybe second day that when a check box disables a field, the field must be grayed out and made not editabile.Still ... ---

## Response 2
Author: Thu Oct 10, 2024 1:05 am
If you put an APN manually, It Is ignored if the "use network APN" is ticked.Not to be overly critic of the good Mikrotik guys, but I think that GUI designer apprentices learn on the first or maybe second day that when a check box disables a field, the field must be grayed out and made not editabile.Still ...Good spot - I will try and toggle this when I return to site tomorrow! ---

## Response 3
Author: Fri Oct 18, 2024 2:20 pm
Ok, this doesn't seem to have affected anything sadly. Still getting that 254.128.0.0 IP.Put a known working SIM in also, and it registers OK, but doesn't seem to change no matter if I try CHAP or PAP or leave the Use Network APN enabled or not! ---

## Response 4
Author: [SOLVED]Fri Oct 18, 2024 2:44 pm
Cracked it - had the IP set to "Auto" not "IPv4".FFS!!! ---

## Response 5
Author: Fri Oct 18, 2024 7:08 pm
``` 
```
[admin@MikroTik]>/interface/lte/apn/printdetailFlags:*-default0*name="default"apn="data.uk"use-peer-dns=nouse-network-apn=noadd-default-route=yesdefault-route-distance=2ip-type=autoauthentication=none
```

With 1pMobile (an MVNO on EE), the following works:It might be that they run their own PGW and so the allocation process is different, but I get an EE IP address (not locally, it's a CGNAT NAT44 external address) so I'm tending to think they don't.
```