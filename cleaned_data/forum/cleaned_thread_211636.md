# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211636

# Discussion

## Initial Question
Author: Thu Oct 10, 2024 2:14 pm
I need to configure aMikroTik hAP ax lite LTE6to provide Internet at home via mobile network (LTE).The documentation athttps://help.mikrotik.com/docs/display/ ... +lite+LTE6says:- In the (QuickSet) menu, set up the following: Choose your country, to apply country regulation settings;- Set up your wireless network password in the left field;- Set up your router password in the bottom field.I don't see any LTE-settings in the QuickSet window, so there is no country setting.The device is default as Router/Firewall.There it has Internet as static with IP 192.168.88.1, as well Local network IP is the same 192.168.88.1.Is that not buggy? Do I need to set it to automatic instead of static?Wireless and wired LAN are ok, but Internet access via the SIM card from my provider (Congstar HomeSpot, Germany) in the router isn't working yet.Also DNS resolving isn't working, as there is no DNS defined. I was thinking this will be set automatically from the mobile provider, not?Could a kind soul please help me to get this working? Thx. ---

## Response 1
Author: Thu Oct 10, 2024 2:27 pm
I don't know but can you set the sim card wrong, backwards?So the LTE interface will not appear if there is not any working sim card detected.And with Mikrotik devices you need to upgrade two things.But with LTE you have to upgrade also the LTE modem.So you have the latest and greatest ---

## Response 2
Author: Thu Oct 10, 2024 2:34 pm
I don't know but can you set the sim card wrong, backwards?So the LTE interface will not appear if there is not any working sim card detected.And with Mikrotik devices you need to upgrade two things. But with LTE you have to upgrade also the LTE modem.So you have the latest and greatestLTE on the QuickSet window I was meaning.I think the SIM card is already inserted correctly.An LTE interface under interfaces is present. But is there any country setting? Maybe I missed it. Will check again. ---

## Response 3
Author: Thu Oct 10, 2024 2:40 pm
In APN settings you need to make sure to use the correct settings for your provider.Other then that, there is little to be done.That device is pretty much working out of the box.If you already changed some settings, best to reset to default and then start again.Use Quickset ONCE, then never again.It can really mess with your settings if you changed things using webfig/winbox. ---

## Response 4
Author: Thu Oct 10, 2024 3:04 pm
In APN settings you need to make sure to use the correct settings for your provider.Other then that, there is little to be done.That device is pretty much working out of the box.If you already changed some settings, best to reset to default and then start again.Use Quickset ONCE, then never again.It can really mess with your settings if you changed things using webfig/winbox.Where are the APN seetings?Under the LTE interface it seems to have recognized the provider as "Telekom.de".But where can I find the WAN IP that gets assigned from the provider? ---

## Response 5
Author: Thu Oct 10, 2024 3:08 pm
Webfig or WinboxAPN settingsOpen Interfaces and then LTE tab.There you have a button with LTE APNsAt least one should be defined and on lte interface itself you specify which one is to be used (I usually keep default as-is and make a new one for my purpose).WAN IPIP AddressesShould be linked to lte1 interface ---

## Response 6
Author: Thu Oct 10, 2024 3:48 pm
Now I finally have found the country setting on the QuickSet window, unexpectly under the wireless settings, as I was thinking wireless means local wireless stuff, not mobile stuff.It was by default set to the first in the country list: AfghanistanBut now I have unfortunately to reset the device again b/c I also had fiddled with the IPs there, can no longer access the IP... ---

## Response 7
Author: Thu Oct 10, 2024 4:03 pm
Now I finally have found the country setting on the QuickSet window, unexpectly under the wireless settings, as I was thinking wireless means local wireless stuff, not mobile stuff.And you were right, the country is related to local wireless (the wifi radio) as different countries allow different frequencies and transmitting power on them, nothing related to LTE, AFAICT. ---

## Response 8
Author: Thu Oct 10, 2024 4:14 pm
Webfig or WinboxAPN settingsOpen Interfaces and then LTE tab.There you have a button with LTE APNsAt least one should be defined and on lte interface itself you specify which one is to be used (I usually keep default as-is and make a new one for my purpose).WAN IPIP AddressesShould be linked to lte1 interfaceThx. I now have found all of them and it seems ok.Under IP addresses I see the local IP (192.168.88.1) as well an IP (10.16.105.xx) for thelte1interface.So, as next step I tried to ping a public IP address from the MikroTik CLI, but it gives timeoutHmm. what to do now?Btw, where can I find thecountrysetting in the CLI or the WebFig, as the QuickSet is a dangerous location? ---

## Response 9
Author: Thu Oct 10, 2024 4:19 pm
Country for wifi ?On Wifi interfaces ---

## Response 10
Author: Thu Oct 10, 2024 4:20 pm
Now I finally have found the country setting on the QuickSet window, unexpectly under the wireless settings, as I was thinking wireless means local wireless stuff, not mobile stuff.And you were right, the country is related to local wireless (the wifi radio) as different countries allow different frequencies and transmitting power on them, nothing related to LTE, AFAICT.Oh, thx, that's good to know, I really was wrongly thinking it's LTE related... ---

## Response 11
Author: Thu Oct 10, 2024 4:22 pm
So, as next step I tried to ping a public IP address from the MikroTik CLI, but it gives timeoutHmm. what to do now?IP doesn't work ?And you are sure about the IP address ? I always use as test 8.8.8.8 (= Google DNS)What do you have as route ?Should be something like 0.0.0.0/0 and gateway lte1 ---

## Response 12
Author: Thu Oct 10, 2024 4:23 pm
Country for wifi ?On Wifi interfacesIt's really confusing: wireless, wifi, wlan, cellular, mobile. ---

## Response 13
Author: Thu Oct 10, 2024 4:27 pm
And LAN and WAN and ...And don't get started on all the possible routing protocols and their accronymsOnce you get used to the terms, it's pretty clear. ---

## Response 14
Author: Thu Oct 10, 2024 4:34 pm
``` 
```
0.0.0.0/0lte1210.16.105.73/32lte10192.168.88.1/24bridge0
```

So, as next step I tried to ping a public IP address from the MikroTik CLI, but it gives timeoutHmm. what to do now?IP doesn't work ?And you are sure about the IP address ? I always use as test 8.8.8.8 (= Google DNS)What do you have as route ?Should be something like 0.0.0.0/0 and gateway lte1Yes, pinging a public IP like 8.8.8.8 gives error "timeout"./ip route print shows something like this (I cannot do copy-paste, rather have to read from the screen):


---
```

## Response 15
Author: Thu Oct 10, 2024 4:39 pm
Yes, pinging a public IP like 8.8.8.8 gives error "timeout".So it is not a missing route the issue (otherwise you would have "no route to host").Have you configured (properly) the APN?It depends on the ISP that issued the SIM, some work just nicely with the automatic APN (that the SIM provides) some need to have it set manually, AND, if you need to set it manually, you MUST disable the "use network APN" otherwise the one you typed in will be ignored. ---

## Response 16
Author: Thu Oct 10, 2024 5:05 pm
``` 
```
InWebFig:Interfaces/LTE/LTEAPNs:EnabledyesCommentGeneraL:Namelte1TypeLTE
  MTU1500ActualMTU1500L2 MTUNetworkmode:3glte
  LTEBands1PIN(nothing)Operator(nothing)ModemInit(nothing)APN profiledefaultAllowroaming(nothing)Cellular:Currentoperator:Telekom.deCurrentCellID:......
```

Yes, pinging a public IP like 8.8.8.8 gives error "timeout".So it is not a missing route the issue (otherwise you would have "no route to host").Have you configured (properly) the APN?It depends on the ISP that issued the SIM, some work just nicely with the automatic APN (that the SIM provides) some need to have it set manually,AND, if you need to set it manually, you MUST disable the "use network APN" otherwise the one you typed in will be ignored.The ISP says the SIM can be used with any LTE router, it has even the PIN deactivated by default.I would of course prefer an auto-setup over a manual one.So, when I call the SIM provider, what should I ask them?


---
```

## Response 17
Author: Thu Oct 10, 2024 5:14 pm
These things:APN name to be usedAuthentication typeIP-typeuser name to be usedand if needed, passwd to be usedThose values need to be filled in in APN settings.And that APN record needs to be applied to your lte interface. Remember the above remark about "Use network APN settings" !Usually you should be able to find that info on their website. ---

## Response 18
Author: Thu Oct 10, 2024 5:15 pm
The APN, then if needed username, password, etc.It depends on the SIM, it could be "internet" or "internet.telekom" or "internet.v6.telekom":https://www.telekom.de/hilfe/mobilfunk/ ... ndards/apnSee also this:viewtopic.php?t=183528Check:/interface lte print/interface lte apn print ---

## Response 19
Author: Thu Oct 10, 2024 6:17 pm
I now got all the APN data from the provider.Will now try to apply them... ---

## Response 20
Author: Thu Oct 10, 2024 7:44 pm
Webfig or WinboxAPN settingsOpen Interfaces and then LTE tab.There you have a button with LTE APNsAt least one should be defined and on lte interface itself you specify which one is to be used (I usually keep default as-is and make a new one for my purpose).Ok, I created a new entry named "my" (now there is "default" and "my"),but where do I need to specify that this new one shall be used? ---

## Response 21
Author: [SOLVED]Thu Oct 10, 2024 8:23 pm
Success! I now can ping 8.8.8.8Got it finally working by using an "alternate" (ie. old) APN=telekom.t-d1.de using proto=CHAP and user=internet pw=t-d1The difference is this: the LTE device now gets a public IPv4 address (37.84.96.xx/32) assigned, whereas in previous attempts it got just a private IPv4 address (10.16.105.xx/32).Found the said alternate APN in this old public support posting of the provider:https://forum.congstar.de/thread/64622- ... post429090Thanks everybody, without your useful hints this would have taken much longer. ---

## Response 22
Author: Thu Oct 10, 2024 9:21 pm
From inside this AP router I can ping internet addresses (both IP and domainnames),but from the attached PC pinging internet IP addesses does not work yet.On the PC the gateway and DNS server is this AP (ie. 192.168.88.1),and the PC itself has IP 192.168.88.3.So, it seems to be a firewall issue on this AP router.The firewall so far is untouched by me, ie. everything is default setting.Any idea how to fix? ---

## Response 23
Author: Thu Oct 10, 2024 9:53 pm
Forum veteran with 800+ posts can not figure this out? How is that even possible?Anyway.. you have to decide if you want your router to handle DNS requests or if clients should connect directly to public DNS servers.If you want your router to be midleman, you have to enableallow-remote-requestsin DNSif you want to skip that, you can change settings of your DHCP server and use public DNS servers directly ---

## Response 24
Author: Thu Oct 10, 2024 10:11 pm
Forum veteran with 800+ posts can not figure this out? How is that even possible?Just setting up the device and then doing something else in the next 3 or 5 years...Anyway.. you have to decide if you want your router to handle DNS requests or if clients should connect directly to public DNS servers.If you want your router to be midleman, you have to enableallow-remote-requestsin DNSif you want to skip that, you can change settings of your DHCP server and use public DNS servers directlyFound the reason: I forgot to change the resolver settings (/etc/resolv.conf on the Linux PC).Had nothing to do in the router firewall setup (though I better should do something in the firewall, but atm q&d functionally has higher prio).Ok, now everything finally okThx. ---

## Response 25
Author: Thu Oct 10, 2024 10:26 pm
Now I'm going to test whether streaming (ie. netflix-like providers) is working satisfactorily via LTE.If yes, then I'll say good-bye to my cable internet, which has become also very expensive here.Update:Right now watching some Youtube cat videos over this connection.The quality is satisfactory for my needs.So, then this was a useful investment ---

## Response 26
Author: Thu Oct 10, 2024 10:57 pm
I've used such a device for teleworking from South of France during some weeks.A couple of days with 8 hours straight, not a single disconnect (and Azure remote desktop is quite sensitive to it !). ---

## Response 27
Author: Thu Oct 10, 2024 11:02 pm
Right now watching some Youtube cat videos over this connection.Be very aware of cupboard cat attacks:https://youtu.be/QefxGauB3_cYou'll never know what hit you. ---

## Response 28
Author: Fri Oct 11, 2024 1:46 am
Encountered a problem:I wanted to hide the wifi SSID, but it gives a cryptic error message"Invalid value in undefined".I did not change anything in these settings, ie. just using the defaults.On my other (older) MT router (hAP ac^2) using ROSv6 hiding an SSID works just fine. ---

## Response 29
Author: Fri Oct 11, 2024 9:40 am
Export of wifi part please.terminal/interface wifiexport file=anynameyouwishMove that file to your computerRemove serial, passwds, ...Post contents back here between [code] [/code] quotes ---

## Response 30
Author: Fri Oct 11, 2024 2:13 pm
``` 
```
# 2024-10-11 12:27:17 by RouterOS 7.15.2# software id = Y028-72I4## model = L41G-2axD&FG621-EA# serial number = XXXXX/interfacewifiset[finddefault-name=wifi1]channel.band=2ghz-ax.skip-dfs-channels=\10min-cac.width=20/40mhzconfiguration.mode=ap.ssid=XXXXX \
    disabled=nosecurity.authentication-types=wpa2-psk,wpa3-psk.ft=yes \.ft-over-ds=yes
```

Export of wifi part please.terminal/interface wifiexport file=anynameyouwishMove that file to your computerRemove serial, passwds, ...Post contents back here between [code] [/code] quotesOk, thx, here's it:


---
```

## Response 31
Author: Fri Oct 11, 2024 2:23 pm
And where is the offending setting ?Should be something like/interface wifiset [ find default-name=wifi1 ] channel.band=2ghz-ax .frequency=2412 .width=\20mhz configuration.country=Belgium .hide-ssid=yes.mode=ap .ssid=XYZ \disabled=no security.authentication-types=wpa2-psk, wpa3-pskPS: you do not need this, not on a single radio AP not being under capsman controlft=yesft-over-ds=yes ---

## Response 32
Author: Fri Oct 11, 2024 4:28 pm
And where is the offending setting ?Should be something like/interface wifiset [ find default-name=wifi1 ] channel.band=2ghz-ax .frequency=2412 .width=\20mhz configuration.country=Belgium .hide-ssid=yes.mode=ap .ssid=XYZ \disabled=no security.authentication-types=wpa2-psk, wpa3-pskPS: you do not need this, not on a single radio AP not being under capsman controlft=yesft-over-ds=yesAfter updating RouterOS to the latest version (7.16.1) the said error disappeared! ---

## Response 33
Author: Fri Oct 11, 2024 6:19 pm
Anyone know: does RouterOS keep traffic stats for each interface?Ie. how many bytes transferred in and out on daily/weekly/monthly basis? ---

## Response 34
Author: Fri Oct 11, 2024 6:56 pm
Yes and no.It does keep stats for as long as the device is connected, aggregated.You can use Tools / Graphing but it can be a load on local resources.If you want more detailed info, you need to look at other options:Splunk:viewtopic.php?t=179960Kid control (someone here made a script to use Kid Control to collect stats etc. Maybe you can find it if you search a bit, I couldn't find it right away)... ---

## Response 35
Author: Fri Oct 11, 2024 7:50 pm
``` 
```
OnlineTimeDataVolume(MB)Connections(hh:mm)TotalSentReceivedToday18:44224857416732Yesterday24:00644578456610Currentweek114:44431553867392882Currentmonth258:44825328743737882Previousmonth713:56211193234161877776
```

My other router has such a useful traffic statistics page for the WAN interface (ie. Internet).Need a similar one for my MikroTik LTE interface b/c need to monitor (control) the traffic amount as it's not flat rate.


---
```

## Response 36
Author: Fri Oct 11, 2024 8:07 pm
Ah, found it.See hereviewtopic.php?t=198794 ---

## Response 37
Author: Fri Oct 11, 2024 8:21 pm
Ah, found it.See hereviewtopic.php?t=198794This indeed looks very interesting.I'll try to use it.Thank you very much for your help.