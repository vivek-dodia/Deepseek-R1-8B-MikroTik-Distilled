# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 160180

# Discussion

## Initial Question
Author: Tue Apr 21, 2020 1:48 am
Hi guysI'm very new to Mikrotik (bought my first one yesterday) and intend to use is as Wireless Bridge to the main router to provide connectivity to a few clients which don't have wifi capabilities.Main Router ))))~~~((((( Mikrotik Router ------->PCMikrotik is connected to the main router WIFI via pseudo bridgeWlan and all ethernet ports are moved to the bridge.I do see an IP lease (issued by the main router) in the client section of the RouterOS there is Internet available for the Mikrotik router - I can ping google dns from there just fine.However that IP lease is not passed over to the ethernet ports, so clients connected to the Mikrotik router via cable don't have access to the Internet an LAN (ipconfing shows windows 169.x.x.x. IP)I have tried a few things:Removing RSTPmake interfaces trustedNothing workedIs it a fault or work as designed?Thank you very much ---

## Response 1
Author: Tue Apr 21, 2020 2:35 am
I've used station-pseudobridge mode in the past and its worked fine, havn't needed to do anything special just put in a bridge with an ethernet portThe wiki does say thisThis mode is limited to complete L2 bridging of data to single device connected to station (by means of single MAC address translation) and some support for IPv4 frame bridging - bridging of non-IP protocols to more than one device will not work. Also MAC address translation limits access to station device from AP side to IPv4 based access - the rest of protocols will be translated by single MAC address translation and will not be received by station itself.Implying it should only work with 1 device on the ethernet side, however I swear i've used it with multiple clients before without an issue.....I'd like to hear a MikroTik rep confirm or deny that for sure. But that could be your problem, test with just 1 device, then try and add another oneIf it doesn't, I wonder if you could use regular station mode and local-proxy-arp with the same subnet on both interfaces (not bridged) to make your own pseudo-bridge anyway (mikrotik responds with its own MAC address) ---

## Response 2
Author: Tue Apr 21, 2020 7:47 am
Hi, At this moment the only device that is connected to mikrotik is a PC.I can manually assign an IP to the connected pc and it will work. However what about the devices that don't support that.This is so strange that such a simple thing that a $20 dollar extender can do is so difficult to implement with mikrotik.Can somebody please adviseThank you ---

## Response 3
Author: [SOLVED]Tue Apr 21, 2020 12:30 pm
It does work, there will be an explanation for whats going on, why it isn't working for you and a way to fix it. It may be something like your AP is blocking multiple DHCP requests (unlikely but you never know). The mikrotik does not need a lease, so disable that to start with, heck just do a system->reset configuration and tick no defaults, then just bridge ethernet and wlan and set it up as station-pseudobridge and connect. No DHCP or anything, mikrotik doesn't need it for access via winbox anyway. That's as simple as the configuration can get, if it's still not working then unfortunately i don't know ---

## Response 4
Author: Tue Apr 21, 2020 4:03 pm
Hi millenium7, thank you so much for your advice, it was indeed the access point which doesn't allow multiple DHCP request to be assigned to clients.I tested with the other 2 access points and got no issues at all.It is an Aruba instant On, sort of semi-enterprise one, not sure what I can do about it ---

## Response 5
Author: Tue Dec 29, 2020 4:46 pm
EDIT: This worked for me perfectly....until I rebooted the device, and now it wont work. Even after restoring a backup taken while it was working. I will update again if I find a cause.EDIT 2: Looks like the issue was my ISP router. After restoring backups and starting again from scratch nothing worked. Until I rebooted my ISP router, then it worked perfectly again.I just spent a week trying to get this to work (delayed mostly due to me being an idiot and locking myself out repeatedly, plus Christmas slowed me down a little). Wanted to share how I got it working somewhere for other people to find, and it seems to be related to your situation too.I finally got it to work by turning on DHCP Relay from my Wireless interface. This points to the main routers IP address, and passes DHCP requests directly to the main router. No NATing involved.Full setup I have:Hardware:hAP ACSoftware:6.48Initial SetupReset configuration with no default configBridge:Bridged ALL ports that I might use (In my instance, I kept wlan1 disabled, as I don't want 2.4GHz, so all other ports, but you could set up a separate AP here)Security ProfileSet up a newSecurity Profileto match the main routers details. I selected all authentication types and entered my main routers Wifi Password and saved.Wirelesswlan2set up as a "station-pseudobridge" set to 5GHz-only-AC (I did this to ensure I get the maximum throughput between the two routers)Set the view forwlan2configuration toAdvanced Modeand set theSecurity Profileto the profile you set above.SelectApplyand thenScan...ClickStartand select the main routers SSID, then clickConnect.DHCPSelectIP>DHCP RelayAdd a new relay, putting in wireless interface (wlan2) and your main routers IP Address.OPTIONAL: DHCP ClientYou can set up to have the Bridge get an IP address from DHCP too, so you can connect to the unit without being directly connected. Just add a new DHCP Client, select the bridge name, and enable it. You will see it get an IP quite quickly.Done. This was all I needed to do. No NAT, no special VLANs, etc. Each device plugged in is getting a unique IP within the same range as the rest of the network.Note on setting it to AC Only :- When I had this as the broad 5GHz option, I found I was limited to 450Mbps, whereas when I switched to AC-only, I was topping out just over 1, 000Mbps. I don't know if RouterBoardOS or the main router was selecting the lower options, but forcing it to AC worked perfectly. ---

## Response 6
Author: Sat Feb 06, 2021 12:21 pm
``` 
```
/interface bridge nat add chain=dstnat mac-protocol=ip ip-protocol=udp src-port=67 dst-port=68 action=dst-nat to-dst-mac-address=FF:FF:FF:FF:FF:FF
```

UPDATED:tested this more, and figured out that the hack is only needed when DHCP server and AP are a single MikroTik device in 802.11 or nstreme mode (in nv2 mode pseudobridge works as a proper bridge)Posting here because this thread is a top google result for "mikrotik pseudobridge dhcp".Hope it helps me and everyone else in the future.If you try to use MikroTik in this scenario:DHCP server⮁Wi-FiAccess Point⮁(standard 802.11Wi-Fi)MikroTik in "station pseudobridge" mode, with Wi-Fi and Ethernet bridged⮁(wiredEthernet)1 or morewireddevices asDHCP clientsThis scheme works works well, except when DHCP server and AP are both in a single MikroTik device, then wired devices fail to get their IP addresses.This happens because MikroTik AP's DHCP server replies using broadcast destination address (FF:FF:FF:FF:FF:FF), and MikroTik in pseudobridge mode replaces this to its own MAC, therefore the DHCP client doesn't receive the DHCP reply.This can be solved by using a simple Bridge NAT rule, which replaces DHCP reply DST MAC back to broadcast:You will need to replacebridgethere with your bridge name, which bounds Ethernet and Wi-Fi together.Be warned, that some protocols that rely on broadcasting or use MAC addresses will not work (for example DLNA), but for most cases this allows to connect a wired LAN segment wirelessly to an existing Wi-Fi.


---
```

## Response 7
Author: Sat Feb 06, 2021 3:02 pm
``` 
```
/interface bridge nat add chain=dstnat mac-protocol=ip ip-protocol=udp src-port=67 dst-port=68 action=dst-nat to-dst-mac-address=FF:FF:FF:FF:FF:FF
```

This happens because DHCP server replies using broadcast destination address (FF:FF:FF:FF:FF:FF), and MikroTik in pseudobridge mode replaces this to its own MAC, therefore the DHCP client doesn't receive the DHCP reply.This can be solved by using a simple Bridge NAT rule, which replaces DHCP reply DST MAC back to broadcast:You will need to replacebridgethere with your bridge name, which bounds Ethernet and Wi-Fi together.Be warned, that some protocols that rely on broadcasting or use MAC addresses will not work (for example DLNA), but for most cases this allows to connect a wired LAN segment wirelessly to an existing Wi-Fi.Interesting !!I thought it was the DHCPserver that made the mistake. But I don't remember where I did the sniffing (but non-Mikrotik DHCP-servers DO work with the same pseudo-bridges)... . Fact is indeed the DHCP offer never arrives(DHCP server now also has a parameter with the number of IP addresses per MAC address. But still it would not arrive.)viewtopic.php?f=2&t=116963#p734225


---
```

## Response 8
Author: Thu Oct 21, 2021 9:23 pm
Same Issue here.... ---

## Response 9
Author: Thu Oct 21, 2021 11:13 pm
Just related ....viewtopic.php?t=179493#p886773Remember that MT-MT will work perfectly as "AP-bridge" - "station bridge" . Experiences with nv2 are always MT-MT , and may work just because of the AP-bridgefunction.Other brands don't have a compatible "bridge" function in the AP. (But their DHCP server mostly does work with "station-pseudobridge") ---

## Response 10
Author: Tue Apr 09, 2024 1:43 pm
``` 
```
/interface bridge nat add chain=dstnat mac-protocol=ip ip-protocol=udp src-port=67 dst-port=68 action=dst-nat to-dst-mac-address=FF:FF:FF:FF:FF:FF
```

```
```

```
/interface bridge nat add chain=dstnat mac-protocol=ip ip-protocol=udp src-port=67 dst-port=68 action=dst-nat to-dst-mac-address=FF:FF:FF:FF:FF:FF
```

UPDATED:tested this more, and figured out that the hack is only needed when DHCP server and AP are a single MikroTik device in 802.11 or nstreme mode (in nv2 mode pseudobridge works as a proper bridge)Posting here because this thread is a top google result for "mikrotik pseudobridge dhcp".Hope it helps me and everyone else in the future.If you try to use MikroTik in this scenario:DHCP server⮁Wi-FiAccess Point⮁(standard 802.11Wi-Fi)MikroTik in "station pseudobridge" mode, with Wi-Fi and Ethernet bridged⮁(wiredEthernet)1 or morewireddevices asDHCP clientsThis scheme works works well, except when DHCP server and AP are both in a single MikroTik device, then wired devices fail to get their IP addresses.This happens because MikroTik AP's DHCP server replies using broadcast destination address (FF:FF:FF:FF:FF:FF), and MikroTik in pseudobridge mode replaces this to its own MAC, therefore the DHCP client doesn't receive the DHCP reply.This can be solved by using a simple Bridge NAT rule, which replaces DHCP reply DST MAC back to broadcast:You will need to replacebridgethere with your bridge name, which bounds Ethernet and Wi-Fi together.Be warned, that some protocols that rely on broadcasting or use MAC addresses will not work (for example DLNA), but for most cases this allows to connect a wired LAN segment wirelessly to an existing Wi-Fi.Same issue here, works after


---
```

## Response 11
Author: Thu Oct 10, 2024 4:50 pm
``` 
```
/interface bridge nat add chain=dstnat mac-protocol=ip ip-protocol=udp src-port=67 dst-port=68 action=dst-nat to-dst-mac-address=FF:FF:FF:FF:FF:FF
```

This can be solved by using a simple Bridge NAT rule, which replaces DHCP reply DST MAC back to broadcast:Thank you, this really helped!BTW I found out, that some DHCP servers can have problem, when src MAC and Client MAC address (in DHCP data, not Option 61) are different. The server doesn't response at all...Unfortunately it looks like there is no way to manipulate DHCP packet in the Mikrotik.But some DHCP helper which wouldn't change the src MAC only for these DHCP packets could help. Also what could (generaly) help is changing in the DHCP request the unicast flag to broadcast (so the offer from DHCP server is able to return, if the client doesn't have already IP isn't reachable).As a proof of concept I tried to make bridge src-nat on the AP side and it worked. Unfortunately making src-nat in bridge on station side is not working, the station-pseudobridge still makes it's own src-nat always...P.S. I tested also some TP-Link repeater/bridge and DHCP works without problem with it.
```