# Thread Information
Title: Thread-213456
Section: RouterOS
Thread ID: 213456

# Discussion

## Initial Question
Could you please support 802.11ah, wifi ha-low in your line of products as well?Would this wifi halow module work on any MikroTik RouterOS board?It says it is OpenWRT supported so i think it is doable in RouterOS as well.https://www.alfa.com.tw/products/ahm272 ... 7185781832or thishttps://www.alfa.com.tw/products/ahmc72 ... 0231772232Their tube-ah allegedly has two separate openwrts so i think it might see the modules as an ethernet adapter, but that's just a speculation...https://www.alfa.com.tw/products/tube-a ... 9371985992source:https://github.com/manikmakki/Alfa-Tube-AH-Info
```
The Tube-AH is an odd device.
Out of the box, it has two installs of OpenWRT running. One is exposed over 192.168.1.1, the other is 192.168.1.254.
The .1 interface has the following:

OpenWrt SNAPSHOT, r17031+232-e6b3e77e6e
root@OpenWrt:~# uname -ar
Linux OpenWrt 5.10.54 #0 SMP Sat Jul 31 18:41:15 2021 armv7l GNU/Linux

The .254 interfaces shows:

OpenWrt 22.03-SNAPSHOT, r19522-5c7aed8b1e
root@OpenWrt:~# uname -ar
Linux OpenWrt 5.10.127 #0 Mon Jul 4 21:40:43 2022 mips GNU/Linux

This leads me to believe that the base board (Tube E4G) is running the MIPS install, and the AHM27292U module is running the ARM7L install. It may be obvious to others, but this is the first time I've seen this type of device before.

---
```

## Response 1
+1I've nearly bought a couple of HaLow kits but MT branded I'd buy tomorrow. ---