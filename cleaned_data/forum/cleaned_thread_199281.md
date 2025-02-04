# Thread Information
Title: Thread-199281
Section: RouterOS
Thread ID: 199281

# Discussion

## Initial Question
Hello friends.Please, could you help me with this problem? Thank you so much.I am facing a problem that is constantly happening to me on many routerOS with different versions (current and new).LTE interface disappears:For example:RouterOS RBwAPR-2nDversion: 6.44.5CPU: MIPS 24Kc V7.4architecture-name: mipsbeboard-name: wAP Rplatform: MikroTik/interface lte> prFlags: X - disabled, R - running/interface lte> info 0no such itemIt is not solved even by updating the firmware version. In these cases what I do is change the router.On my other routers, when I search for the interface it should come out like this./interface lte> prFlags: X - disabled, R - running0 R name="lte1" mtu=1480 mac-address= apn-profiles= network-mode=/interface lte> info 0pin-status: no password requiredfunctionality: fullregistration-status: registeredmanufacturer: "MikroTik"model: "R11e-LTE"I don't understand why on other routers I have this problem of not detecting the LTE interface. Do you think it could be a hardware failure?From the directory: /interface> pr the lte interface does not appear either/system resource usb> pr# DEVICE VENDOR NAME SPEED0 1-0 Linux 3.3.5 ehci_hcd RB400 EHCI 4801 1-1 MARVELL WUKONG 480Any troubleshooting for this problem? It is a problem that is happening to me on many of my computers. They usually use the same configuration template.Thank you very much again.All the best. ---

## Response 1
I think that it's a hardware problem. It's not normal that LTE interface dissapears.Regards. ---

## Response 2
RouterOS RBwAPR-2nDversion: 6.44.5It's possible after modem firmware upgrade needs a newer RouterOS.Maybe upgrade to at least the latest version of RouterOS V6. Also make sure you upgrade RouterBOOTfirmware the /system/routerboard/upgrade after you upgrade to "stable" V6.You can also try V7, but the wAP and R11e-LTE should be fine at V6. ---

## Response 3
Hello friends.Thanks for answering.This happens on any firmware.I think it is a hardware problem.Is there any way to try to get the router to recognize that LTE interface again? Like passing a component recognition or something like that.Thank you. ---

## Response 4
You can try to manually add lte1 ?Had it happen once on a SXT LTE device (my own mistake, accidentally deleted LTE instead of disabling).Manually adding it again fixed it.You may have to perform a reboot at first. ---

## Response 5
You can try to manually add lte1 ?Had it happen once on a SXT LTE device (my own mistake, accidentally deleted LTE instead of disabling).Manually adding it again fixed it.You may have to perform a reboot at first.Hello.I am a basic user with mikrotik.What would be the command to add it again?Thank you ---

## Response 6
When I try to add it here:/interface list member> prFlags: X - disabled, D - dynamic# LIST INTERFACE0 ;;; defconfLAN bridge1 ;;; defconfWAN *1/interface list member> add interface=lte1input does not match any value of interface/interface list member> set interface=lte1input does not match any value of interfaceHow could I do it?Thank you ---

## Response 7
WinboxInterfacesLteAdd ---

## Response 8
WinboxInterfacesLteAddHello.It is not a computer managed from my home, so I cannot access it through winbox. I can only access via ssh by jumping from another router.That's why I'm asking you about the commands.This resource appears and disappears/system resource usb> pr# DEVICE VENDOR NAME SPEED0 1-0 Linux 3.3.5 ehci_hcd RB400 EHCI 4801 1-1 MARVELL WUKONG 480/system resource usb> pr# DEVICE VENDOR NAME SPEED0 1-0 Linux 3.3.5 ehci_hcd RB400 EHCI 480/system resource usb> pr# DEVICE VENDOR NAME SPEED0 1-0 Linux 3.3.5 ehci_hcd RB400 EHCI 480Can you think of anything else?Thank you. ---

## Response 9
Hmmm ... out of the top of my head/interface lte addshould at least bring back the lte interface and then you can change config. ---

## Response 10
Interesting read here (but not something to become happy with...)viewtopic.php?t=126683 ---

## Response 11
Yeah I doubt it's a hardware problem – other than the software is not "finding" the right USB PIDs in hardware to match the modem.Adding "lte1" manual is very unlikely to do anything, if it's not added automatically, it's not found as an LTE modem.When you say "tried all the firmware", that's a little vague....I just want to be clear you copied the 6.49.10 RouterOS to root of "Files" from left menu, then reboot (System > Reboot), and after it's running V6 "stable" (6.49.10). The RouterOS files are on their websitehttps://download.mikrotik.com/routeros/ ... .49.10.npkAfter confirming 6.49.10, you also go the System > RouterBoard and hit the "Update" button, and the do another System > Reboot.If you're at 6.49.10 with matching boot loading in /system/routerboard & LTE still isn't showing up. You should file a ticket at help.mikrotik.com, and include a "supout.rif" (which you can generate using "Make supout.rif" from left menu, and then drag-and-drop to desktop/laptop from files). ---

## Response 12
The power supply adaptor is the problem! If using OEM supplied my Mikrotik (12V 0.8A), it doesn't work12V 2A works like charm ---

## Response 13
Wow ! That definitely is something you should contact support about !Because that IS a HW problem. ---

## Response 14
Glad that fixed it.Wow ! That definitely is something you should contact support about !Because that IS a HW problem.But they come should come with24V800mA AC/DC adapter... So yeah 800mA at12Vis half the power of 24V that should have come with... ---

## Response 15
Just had this issue with a RB912R-2nD.No matter what, the LTE interface did not show up.Might be a fluke, but after going to System/Resources and clicking on USB, initially it only showed one device named RB400 EHCI.After a couple of seconds, the 2nd device named R11e-LTE appeared and the LTE interface was now online.1.jpg2.jpgTry this before going nuclear and reset or RMA.later edit:Seems that selecting the modem as MBIM instead of Auto fixed this issue on another RB912R-2nD.5 reboots with modem Auto = no modem even after 5 minutes of waiting5 reboots with modem MBIM = always modem right after reboot.Set the modem to Auto and did a couple of more reboots = no modem again.Something is messed up with this setting, at least on this model. ---

## Response 16
same problem with my LTE : RB912R-2nDreboot does not solved the problem.any idea? ---

## Response 17
same problem with my LTE : RB912R-2nDreboot does not solved the problem.any idea?Tried selecting the modem as MBIM instead of Auto? ---

## Response 18
same problem with my LTE : RB912R-2nDreboot does not solved the problem.any idea?Tried selecting the modem as MBIM instead of Auto?How to do that? Which menu? ---

## Response 19
Tried selecting the modem as MBIM instead of Auto?How to do that? Which menu?In Winbox, Interfaces/LTE/Modem ---

## Response 20
How to do that? Which menu?In Winbox, Interfaces/LTE/ModemInterface LTE dissapear. Can we still change that mode? ---

## Response 21
In Winbox, Interfaces/LTE/ModemInterface LTE dissapear. Can we still change that mode?Change it from Auto to MBIM. Reboot. Check ---

## Response 22
Interface LTE dissapear. Can we still change that mode?Change it from Auto to MBIM. Reboot. Checksorry can u show me from winbox.. which menu that need to be pressed? Auto to MBIM.. i dont find that settings. ---

## Response 23
Change it from Auto to MBIM. Reboot. Checksorry can u show me from winbox.. which menu that need to be pressed? Auto to MBIM.. i dont find that settings.Click on Modem after 2modem.png ---

## Response 24
sorry can u show me from winbox.. which menu that need to be pressed? Auto to MBIM.. i dont find that settings.Click on Modem after 2modem.pngit seems only work in ros7 right?i am still using ros6. ---

## Response 25
Click on Modem after 2modem.pngit seems only work in ros7 right?i am still using ros6.Well, upgrade then. ---

## Response 26
This is very frustrating, because I have the same issue. I tried plugging a SIM into it. I tried removing the SIM. The LTE interface will just not appear.I changed the setting to MBIM, and it still does not show the USB interface.I also tried both the 24V .8A adapter that came with it, as well as a 12V 2A adapter I had. Both of them also failed to have the LTE interface show up.I am wondering if the new 7.17 firmware that was just released might be an issue.LTEMissing.pngJust had this issue with a RB912R-2nD.No matter what, the LTE interface did not show up.Might be a fluke, but after going to System/Resources and clicking on USB, initially it only showed one device named RB400 EHCI.After a couple of seconds, the 2nd device named R11e-LTE appeared and the LTE interface was now online.1.jpg2.jpgTry this before going nuclear and reset or RMA.later edit:Seems that selecting the modem as MBIM instead of Auto fixed this issue on another RB912R-2nD.5 reboots with modem Auto = no modem even after 5 minutes of waiting5 reboots with modem MBIM = always modem right after reboot.Set the modem to Auto and did a couple of more reboots = no modem again.Something is messed up with this setting, at least on this model. ---

## Response 27
Well, I figured out my problem. The RB912R I purchased did not come with the R11e-LTE card.This brings up a good question. Is the RB912R supposed to have the R11e-LTE card included? The words on the following page indicate that it is installed at the factory, but there are places selling it where it clearly was never there in the first place, as the LTE antenna is wrapped in plastic ends and has never been used.The device is equipped with a miniPCIe slot and a factory-installed LTE modem. Two SIM slots are provided for use together with a miniPCIe modem.https://help.mikrotik.com/docs/spaces/U ... kit-seriesBut this URL hints that it only has the antennas:https://mikrotik.com/product/ltap_mini ---

## Response 28
This brings up a good question. Is the RB912R supposed to have the R11e-LTE card included?Nope. While it is a bit confusing with all the LTE talk (and I do believe GPS is still built in) but it does say:The LtAP mini ... with integrated LTE antennas (with two u.fl pigtails) and miniPCI-e slot, so you can use your own LTE modem of your choice.While the "R" in model means it has the miniPCIe slot, it does not mean it has a modem - that's typically encoded in the end of model number like RB912R...&R11e-LTE6 which clarify what modem it had too. ---