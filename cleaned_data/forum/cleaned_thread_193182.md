# Thread Information
Title: Thread-193182
Section: RouterOS
Thread ID: 193182

# Discussion

## Initial Question
I just (finally) received RB5009, and I see no serial port? Am I missing something? ---

## Response 1
Yes, you missed reading the specs before buying it. ---

## Response 2
Yes, you missed reading the specs before buying it.Excellent. Is there a way to access the device over USB port via serial adapter or something?? ---

## Response 3
Sure, there is the WOOBM:https://www.youtube.com/watch?v=2yWrUQ_woKQ ---

## Response 4
Do not work on v7, see other topic about that. ---

## Response 5
Sure, there is the WOOBM:https://www.youtube.com/watch?v=2yWrUQ_woKQBut this doesn't connect to serial console? It is only for running routeros devices? ---

## Response 6
Do not work on v7, see other topic about that.Could you please provide me the with the thread link? I can't find it.This said, 5009 is a great device, but without serial I can't implement it anywhere as there is no backup access. ---

## Response 7
Could you please provide me the with the thread link? I can't find it.try to write WOOBM v7 on Search... and press ener....This said, 5009 is a great device, but without serial I can't implement it anywhere as there is no backup access.Backup for what? For have serial port onsite or use remotely the serial port? ---

## Response 8
This said, 5009 is a great device, but without serial I can't implement it anywhere as there is no backup access.Backup for what? For have serial port onsite or use remotely the serial port?[/quote]Backup for when routeros is broken so I can fix it tru console. ---

## Response 9
Do not work on v7, see other topic about that.Thanks, there might be issues, but on my HAPac2 it does work well with v7, just tested it, could connect via WOOBM:
```
[admin@ut-r1]/system/routerboard>printrouterboard:yes
        board-name:hAP ac^2model:RBD52G-5HacD2HnDserial-number:E5780F4848A2
     firmware-type:ipq4000L
  factory-firmware:6.45.9current-firmware:7.8beta2upgrade-firmware:7.8beta2

---
```

## Response 10
Must be 5009 then, as hAP ac3 ROS V7 is no problem.Klembord-2.jpgKlembord-3.jpg ---

## Response 11
What firmware have your WOOBM? (on bottom of the settings page) ---

## Response 12
I put my WOOBM already away, but I know I have installed the file: woobmfw_211105.binThat file is still on my laptop... ---

## Response 13
:/ I hope on more recent version that fix the issue.... ---

## Response 14
Is there a way to access the device over USB port via serial adapter or something??I get where your coming from – want to get in if the router is FUBAR...But winbox's MAC-address / layer2 access is a godsend to avoid needing a serial port to access the router if you're at the physical router. If you enable RoMON, Layer2 access get extended to other routers using an alternative switching plane.I don't have any handy, but I'd image a USB to serial adapter work if it showed up under /port... Then it could be assigned to console in /system/console – before you'd needed for an "emergency". Just plugging in the serial-to-USB is likely going to do nothing since RouterOS wants you to assign the port to some service, of which console is one possibility. ---

## Response 15
My version v1.1.Once had a problem on hAP ac2 , with the already defined system/console. Deleting console solved the problem.EDIT: with some luck and fail-safe RouterOS design.https://wiki.mikrotik.com/wiki/Serial_Port_Usage"as RouterOS will recreate the console after the next reboot when you really remove it.""When rebooting a RouterBoard the bootloader (RouterBOOT) will always use the serial console (serial0 on RouterBoards) to send out some startup messages and offer access to the RouterBOOT menu." ---

## Response 16
I got a reply re connectivity -> USB-serial-nullmodemcable-serial-usb contraption should work no problems.I just ordered another usb adapter I know works fine and I tested over USB connection.As for woobm I am still not sure if that is console connection or terminal connection. ---

## Response 17
What I do on "important" RB5009 is to sacrifice ether8 for mgmt port. I make it not part of the main bridge nor part of the LAN interface group and bind a static ip directly to ether8, allow winbox/webui/ssh on it. So if I mess up bridge settings or FW rules in a way not even MAC access is working, I can connect an Ethernet cable to ether 8.But as long as RB5009 is still booting, MAC access usually works also for worst config mishaps.And there is always safe mode which should be activated before changing bridge/IP/FW settings. ---

## Response 18
I got a reply re connectivity -> USB-serial-nullmodemcable-serial-usb contraption should work no problems.It can be made even easier from two USB to TTL boards (super cheap from China, <$1, just get FTDI chips as they are least problematic), connect RX->TX, TX->RX, GND->GND and it's done. Easiest OOB management from one Mikrotik to another.As for woobm I am still not sure if that is console connection or terminal connection.WOOBM contains ESP8266 MCU for dealing with wifi/serving web pages and USB to UART module so it appears as USB serial device/adapter on Mikrotik.So it's USB serial console terminal with WEB UI. ---

## Response 19
What I do on "important" RB5009 is to sacrifice ether8 for mgmt port. I make it not part of the main bridge nor part of the LAN interface group and bind a static ip directly to ether8, allow winbox/webui/ssh on it. So if I mess up bridge settings or FW rules in a way not even MAC access is working, I can connect an Ethernet cable to ether 8.But as long as RB5009 is still booting, MAC access usually works also for worst config mishaps.And there is always safe mode which should be activated before changing bridge/IP/FW settings.I usually just enable mac access and be done with it. Password is humongous, so if someone breaks it, well - they have my permisson to wreak havocwhat bothers me the most is not having ability to access the actual terminal console, because that thing saved my ass not once. A month ago I had dead 4011, as in completely dead. Corrupted ssd storage. And I fixed it thru boot sector force over serial. It worked! So no serial is a deal-breaker for me. But it is not a big deal, as if I understand correctly USB is just an implementation of serial port, but I will have to test that + there is an other option of using serial adapters. ---

## Response 20
I got a reply re connectivity -> USB-serial-nullmodemcable-serial-usb contraption should work no problems.It can be made even easier from two USB to TTL boards (super cheap from China, <$1, just get FTDI chips as they are least problematic), connect RX->TX, TX->RX, GND->GND and it's done. Easiest OOB management from one Mikrotik to another.As for woobm I am still not sure if that is console connection or terminal connection.WOOBM contains ESP8266 MCU for dealing with wifi/serving web pages and USB to UART module so it appears as USB serial device/adapter on Mikrotik.So it's USB serial console terminal with WEB UI.Not sure about TTL boards. What benefit do they bring? I need a robust solution that I will use once or never and that will always work.As for woobm I will have to test that thing. If it works, fine! But I need to have xmodem protocol working for it to transfer bootsector. ---

## Response 21
you can connect any USB-RS232 and use it as console in /system ports if you have USB-HUB also you can connect many USBs devices and configure it as you like we was use it for UPS and GSM devices etc.also there is Quad/Octa Serial ports you can connected it Router OS almost support all serial chips and in market FDS chip its available.like thishttps://www.usbgear.com/USB2-8COM-M.html ---

## Response 22
While all these adapters might work (because nobody guarantees the support in RouterOS), they are non-functional if RouterOS doesn't boot, the main reason you'd want a serial connection in the first place.So they are kinda useless. ---

## Response 23
I am confused now - does this mean I wouldn't be able to connect to serial console using an adapter? (in usb-serial = serial-usb config) ---

## Response 24
Probably there are some stuff lost in translation.1. You CAN use serial<>usb adapters to connect to your RouterOS, IF: that adapter is properly recognized and configured under RouterOS and if RouterOS is functional.2. You CAN'T use serial<>usb adapters as a debug port, if RouterOS crashed for some reason and it doesn't boot: RouterBOOT has disabled serial console output on the devices that have no serial port from the factory and it's not configured to output to some random USB device anyway.Better? ---

## Response 25
Probably there are some stuff lost in translation.1. You CAN use serial<>usb adapters to connect to your RouterOS, IF: that adapter is properly recognized and configured under RouterOS and if RouterOS is functional.2. You CAN'T use serial<>usb adapters as a debug port (if RouterOS crashed for some reason and it doesn't boot): RouterBOOT has disabled serial console output on the devices that have no serial port from the factory and it's not configured to output to some random USB device anyway.Better?Yes, it is better, but I am not happy.From what I understand, all this means that there is no way to connect to debug port on 5009? [And that I can use both adapters or Woobm to connect to to console thru USB if ROS is operational, but unaccessible (because I was stupid and blocked myself out)] ---

## Response 26
Exactly. ---

## Response 27
Crap.OK... So tell me this: I had a failed 4011 two months ago, as the storage got corrupted. That is the most plausible explanation of what happened to it. Netinstall did not work whatever I tried, it just got stuck on upload, so I had to reformat the storage, and reupload the routerboot that I got from MT. I did that thru serial port xmodem and the completely dead 4011 now works, here I am looking at it right now. It looks nice and happy.Say somehting like this happens to me on production 5009, I can literally throw it away because it is bricked?TBH I am pissed at MT now for committing serial on 5009. ---

## Response 28
That's my take on it, yes. Unless they have some secret recovery procedure, you'll have to send it back for repairs or get it replaced.Or, void the warranty, get your hands dirty to solder a header and flip a bit in the config partition to enable serial output. But probably not worth the risk(not an easy job anyway).Boo MikroTik, boo! :pBut, chances that you get a device in a state when Netinstall doesn't work are low anyway (except your lucky rb4011), so don't panic. ---

## Response 29
Like on the back of the The Hitchhiker's Guide to the Galaxy book. ---

## Response 30
I also got a reply from MikroTik support: both Woobm and USB-Serial adapters can work only if ROS is running, so no console for me. So I guess it better not break. LOL ---

## Response 31
No surprise ---

## Response 32
Soft-disabling UART console on most of the devices is one of the most stupid decisions Mikrotik made. Thanks to it devices that could be repaired are tossed into e-waste (or regular) bin for no reason. Also with no console you can't even see what's going on during netinstall. So many people are failing to do netinstall properly and it's mostly because there is ZERO debug or status output of what's happening.It's one thing to decide not to put serial port connector on device, be it for design or cost reasons. But why disable the internal UART pins, that are right there on PCB? That may be your last way to recover the device.There is no official reason why they do this. Never got any good answer from anyone, be it here on forum or support. Only usual "if product is not working you can RMA it" reply. Yeah, great.. and when warranty is over, then it's just supposed to be doorstop brick?! Just plain stupid. While Mikrotik is relatively friendly when it comes to repairing out of warranty devices and even doing things like NAND chip swaps, having proper console would help many devices to not need such expensive repair in a first place. In the end it's waste of everyone's time (be it support answering questions, sellers having to do extra RMAs or people who then have to repair these broken devices).It's good idea to netboot OpenWRT and flip that config byte to enable the console as soon as warranty is over, it seems to work on all ARM devices.. that way if you happen to need it in the future, you can have bootloader console access. ---

## Response 33
Do you happen to have OpenWRT manual on how to do this? 5009 is ARM 64 bit which is plenty and a reason why I bought it. ---

## Response 34
Looks like on RB5009 situation is more complex. If you want to go down the rabbit hole:https://openwrt.org/toh/mikrotik/rb5009ug_s_inhttps://github.com/adron-s/aux-loader2 ---

## Response 35
Probably not a good idea. It seems it would be very easy to brick the router this way...I just won't use this thing in production and that's about it.RB1100 is plenty. ---

## Response 36
Let's make a request for MikroTik to make that setting an option? Something that can be flipped the same way other RouterBOOT settings can? ---

## Response 37
Let's make a request for MikroTik to make that setting an option? Something that can be flipped the same way other RouterBOOT settings can?I support that. Even if going to the board directly if there are headers there, that would be a viable option to recover router that died. Or make header ourselves. The current way is kind of no go. ---

## Response 38
+1Enabling internal UART to be actually usable would be great. Especially for boards with no USB, where UART is only way to connect anything... ---

## Response 39
Any router that might be designed for use as a test bed or lab environment should be designed with a serial port.The fact that the RB5009 wasn't baffles me. Initially, it looked attractive till I saw the serial port wasn't there..Just get a RB4011 instead..-tp ---

## Response 40
Any router that might be designed for use as a test bed or lab environment should be designed with a serial port.The fact that the RB5009 wasn't baffles me. Initially, it looked attractive till I saw the serial port wasn't there..Just get a RB4011 instead..-tpExactly what I did. I decided to put 5009 as a core router in my LAN, and 4011 I salvaged last month exactly thru serial console connection will be used for testing.Having a serial port on 5009 was such a normal idea to me that I didn't even pay attention does it have it or not. I think MikroTik did this on purpose, so the people will buy more expensive (and similarly performant) RB1100AHx4. Can't really blame them tho, as 5009 is really powerful. ---

## Response 41
Sorry for the necro.....What I don't get is that they added the serial port to the L009.... but not the 5009. Odd decision. (Just saw this today on a L009 I was installing in a rack.) ---

## Response 42
What I don't get is that they added the serial port to the L009.... but not the 5009. Odd decision. (Just saw this today on a L009 I was installing in a rack.)The RB5009 came out before the L009, so I'd like to think MT learned a serial port is still useful. Also the L009 is a replacement for the RB2011 - which did have a serial port - while RB5009 was a new design/model/series. Now in all these "upgrades", stuff like the RB2011's LCD was lost, so who knows... But we're down reading tea leaves.Just for clarity, USB serial does work on RB5009 – once booted – although that often not when you need a serial port... ---

## Response 43
Just for clarity, USB serial does work on RB5009 – once booted – although that often not when you need a serial port...[/quote]Correct. I tested it, and it is so, but if a TB fails, it would be very hard to fix it. ---