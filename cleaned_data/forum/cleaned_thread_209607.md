# Thread Information
Title: Thread-209607
Section: RouterOS
Thread ID: 209607

# Discussion

## Initial Question
Hey guys, I am back with a different issue I need more intelligent people than myself for.Hardware:Router: Mikrotik CCR2004-16G-12S+ with ROS 7.15GPON: Zyxel PMG3000-D20BSince I have switched to the Zyxel GPON I am having spontaneous link down and ups on the SFP interface. The GPON stays up (uptime is more than 3 days during which I had ~40 disconnects).I have used the following way to get access to the GPON directly:https://github.com/xvzf/zyxel-gpon-sfpWith the ISP-provided modem, the connection was rock solid, as such it seems highly likely that it is indeed the GPON that is at fault.The only thing that sticks out here is the following which can be found in the dmesg of the GPON:
```
...[321234.652000]ERO[321249.656000]ERO[321281.656000]ETU[321281.656000]ERO[321481.660000]ERO[322132.656000]ERO[322224.656000]ETU[322224.656000]ERO[322345.648000]ERO[322346.656000]ETU[322790.656000]ETU[322790.656000]ERO[323055.652000]ETU[323055.652000]ERO[323056.656000]ETU[323288.656000]ERO[323486.652000]ERO[323793.652000]ETU[323793.652000]ERO[324011.656000]ERO[324178.652000]ERO[324200.660000]ERO[324304.660000]ERO[324388.652000]ERO[324450.648000]ETU[324450.648000]EROAny steps except to help my ISP to debug the issue? I already switched the fibre cable from the house delivery point (passive) to the GPON. I have found another occurrence about this but I don't speak Italian (viewtopic.php?t=204929). Another topic about this is also unsolved at the moment (viewtopic.php?t=197293).Regards,Enno aka matrixfueller

---
```

## Response 1
I can only help for the Italian language issue, but it is - I believe - about a different problem, a certain Italian ISP provides a Zyxel router that is *somehow* mis-configured and doesn't reach the expected upload speed.It is a peculiar case where the contract is about up to 2.5 Gb in download (but the actual infrastructure - exception made for a few rare cases/locations - tops anyway at 1 Gb in download) and 0.5 Gb in upload, but the upload is capped (by a bug in the firmware/software) to 0.2 Gb or less.The thread is about downgrading (with the risk of bricking the router) to an earlier release that is capped to 1.0 Gb in download, but allows 0.5 Gb in upload.Nothing to do with frequent disconnections.This said, it is rather common that various manufacturers SFP's have compatibility issues with Mikrotiks, but the particular model you have (PMG3000-D20B) seems to be working fine for other members, at least on other Mikrotik hardware:viewtopic.php?p=1074021 ---

## Response 2
Thank you for the translation. Then this thread is indeed unrelated.My issue is a different one to the thread you linked because I don't have a slow link but instead my link goes down randomly for a short while.My research so far seems to suggest that also UniFi Devices don't work reliably with the GPON.I would expect that a GPON that is running openWRT has some kind of possibility to fix the issue as it is software related. ---

## Response 3
My issue is a different one to the thread you linked because I don't have a slow link but instead my link goes down randomly for a short while.Yes, but on that thread, once the MTU/fasttrack issue was solved, the OP was happy with the device connected to his Hex S, this should mean that there is not a "generic" incompatibility issue between Mikrotik and that Zyxel SFP, which leaves us with:1) a specific incompatibility between your CCR2004-16G-12S+ and the Zyxel PMG3000-D20B (possible but IMHO improbable)2) *something* in the firmware or settings of the Zyxel PMG3000-D20B (what you are suspecting, most probable)3) *something* in your Router OS settings (less probable, still possible)For #2, I don't think you will find many people with Zyxel experience here.For #3, if you post your configuration, following these instructions:viewtopic.php?t=203686#p1051720some of the more experienced members may be able to review it and possibly spot something that might be involved, or however give you some instructions on how/what to log on the Mikrotik side. ---

## Response 4
I'll check out if I find reason for the case that the MTU is the issue. Thanks for the additional pointers. After work I will invest some mote time into this topic. ---

## Response 5
So I don't know if I am wrong but my research says that my ISP doesn't support an MTU/MRU of 1500 for PPPoE and still wants to have 1492 as an MTU set. If I understood you right the MTU of 1500 should be set on my physical interface. You can see both the physical interface and the tagged VLAN is at an MTU of 1500. So I should be good? Or are you referring to the actual PPPoE interface which is at 1492 but my understanding is that I can't change that myself?Source:https://telekomhilft.telekom.de/t5/Fest ... -p/6361250Edit: I did an impulse buy of a FS GPON-ONU-34-20BI. Maybe that works better. I will see once it has arrived. ---

## Response 6
I face the same issue with the zyxel module and a rb5009 (provider is deutsche telekom). Did the FS GPON-ONU-34-20BI work without port flapping? Would you recommend it? ---

## Response 7
I face the same issue with the zyxel module and a rb5009 (provider is deutsche telekom). Did the FS GPON-ONU-34-20BI work without port flapping? Would you recommend it?Yes I can fully recommend it. The only issue was getting the device ID which is only visible after logging into the GPON. This however was straightforward after checking the manual. Sorry for not confirming this earlier. ---

## Response 8
I made a support ticket at Mikrotik for the issues I had with my Telekom PMG3000. They let me know that the Zyxel SFP is not built to the SFP-MSA, and that pin 6 is not properly grounded like it is supposed tho.https://web.archive.org/web/20241129013 ... Issue.htmlThis is a very similair issue on a Nokia branded GPON SFP.The Zyxel also works fine in my Mikrotik RB260Gs switch, but i have random disconnects in my L009. Same module!Am now also looking at a replacement module, and I want to contact telekom if they are aware that this SFP is not MSA-compliant. I hope they are willing on working to resolve this issue...Possibly also getting the FS SFP. Did you just change the GPON S/N to the one of your Zyxel and it is now working? or did you contact telekom to have the FS ONT registered in their system/olt? ---