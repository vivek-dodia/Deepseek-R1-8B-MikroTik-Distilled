# Thread Information
Title: Thread-1116138
Section: RouterOS
Thread ID: 1116138

# Discussion

## Initial Question
Could you please support 802.11ah, wifi ha-low in your line of products as well?Would this wifi halow module work on any MikroTik RouterOS board?It says it is OpenWRT supported so i think it is doable in RouterOS as well.https://www.alfa.com.tw/products/ahm272 ... 7185781832or thishttps://www.alfa.com.tw/products/ahmc72 ... 0231772232Their tube-ah allegedly has two separate openwrts so i think it might see the modules as an ethernet adapter, but that's just a speculation...https://www.alfa.com.tw/products/tube-a ... 9371985992source:https://github.com/manikmakki/Alfa-Tube-AH-Info
```
TheTube-AHisan odd device.Outofthe box,it has two installsofOpenWRTrunning.Oneisexposed over192.168.1.1,the otheris192.168.1.254.The.1interfacehas the following:OpenWrtSNAPSHOT,r17031+232-e6b3e77e6e
root@OpenWrt:~#uname-arLinuxOpenWrt5.10.54#0 SMP Sat Jul 31 18:41:15 2021 armv7l GNU/LinuxThe.254interfaces shows:OpenWrt22.03-SNAPSHOT,r19522-5c7aed8b1eroot@OpenWrt:~#uname-arLinuxOpenWrt5.10.127#0 Mon Jul 4 21:40:43 2022 mips GNU/LinuxThisleads me to believe that thebaseboard(TubeE4G)isrunning the MIPS install,andthe AHM27292Umoduleisrunning the ARM7L install.Itmay be obvious to others,butthisisthe first time I've seen this type of device before.

---
```

## Response 1
+1I've nearly bought a couple of HaLow kits but MT branded I'd buy tomorrow. ---