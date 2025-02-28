# Thread Information
Title: Thread-213835
Section: RouterOS
Thread ID: 213835

# Discussion

## Initial Question
Picked up a "new old stock" hAP AX2. Doesn't seem to be used, but also without any warranty.My issue is that Winbox won't stay connected. Either 3.41 or 4_beta16. LOG says user connected/disconnected, Winbox4 will say "Decrypt failed". Legacy mode in Winbox3 doesn't help. Sometimes it disconnects immediately, sometimes after clicking around, almost always when typing "print" into Terminal.Tried to downgrade from 7.16.2 to 7.15.3 (where my other hAP AX2 is, in case it was a 7.16 issue) and nothing.WebFig works without problems but I just prefer RouterOS.SSH sometimes disconnects with "message authentication code incorrect"Right now I'm using at as a WiFi AP only and that is stable, no issues there, it's just Winbox.Any ideas?
```
[tomsikr@KTAP1]/system/routerboard>printrouterboard:yes
        board-name:hAP ax^2model:C52iG-5HaxD2HaxDserial-number:HEH0[redacted]firmware-type:ipq6000
  factory-firmware:7.8current-firmware:7.16.2upgrade-firmware:7.15.3
```

```
[tomsikr@KTAP1]>exporthide-sensitive# 2025-01-10 17:20:50 by RouterOS 7.15.3# software id = MJ5Y-ZF9S## model = C52iG-5HaxD2HaxD# serial number = HEH0[redacted]/interfacebridgeaddname=br0/interfacewifi# DFS channel availability check (1 min)set[finddefault-name=wifi1]configuration.country=Czech.mode=ap.ssid=Tomsik_5Gdisabled=nosecurity.authentication-types=wpa2-pskset[finddefault-name=wifi2]configuration.country=Czech.mode=ap.ssid=Tomsik_2Gdisabled=nosecurity.authentication-types=wpa2-psk/interfacelistaddname=WANaddname=LAN/interfacebridge portaddbridge=br0interface=wifi1addbridge=br0interface=wifi2addbridge=br0 disabled=yesinterface=ether1addbridge=br0interface=ether2addbridge=br0interface=ether3addbridge=br0interface=ether4addbridge=br0interface=ether5/interfacelist memberaddinterface=ether1 list=WANaddinterface=br0 list=LAN/ip addressaddaddress=10.0.1.2/24interface=br0 network=10.0.1.0/ip dhcp-clientadddisabled=yesinterface=ether1/ip dnssetservers=10.0.1.1/ip ipsec profileset[finddefault=yes]dpd-interval=8sdpd-maximum-failures=4/ip routeadddisabled=nodst-address=0.0.0.0/0gateway=10.0.1.1routing-table=main suppress-hw-offload=no/ip servicesettelnet disabled=yessetftp disabled=yessetapi disabled=yessetapi-ssl disabled=yes/system identitysetname=KTAP1/system notesetshow-at-login=no

---
```

## Response 1
Is there nobody who could help me? I just tried Netboot reinstall of 7.17 and it didn't change anything. ---

## Response 2
Winbox BOTH by MAC and IP?I would try assigning manually a MAC to the bridge, maybe it is unrelated, still it won't make any harm:viewtopic.php?t=190747Another thing to try is to put a (dumb) switch between your PC and the AX2, it is one of those mysterious things that sometimes help in connection.And if you don't need it, taking a port out of the bridge and reserve it to Winbox management is a common practice, in your simple configuration it is not needed, but if you start fiddling with bridge settings it is easy to get locked out. ---

## Response 3
Hi, yes, over both. The AX2 is connected through my AC2, for now only acting as an access point.I do have an update though: I managed to netinstall 7.8 and that seems to be stable. I upgraded to 7.13.5 (just the OS, not the routerboard firmware) and it also seems to be fine. I would like to find out why it happens on 7.15 and higher (what I tested in the past). My other AX2 doesn't have any issues, currently on 7.16.2.Let me find my dumb Mercusys switch and I will test that theory. ---

## Response 4
Maybe going again through the factory version did reset *something* that was mis-ported during one of the past updates. ---

## Response 5
Or maybe I have a revision that changed something in the config. I wonder if verbose export would have any differences. I mean, it shouldn't, right? ---

## Response 6
Maybe going again through the factory version did reset *something* that was mis-ported during one of the past updates.Okay, so 7.14.3 is also fine. But 7.15.2 is busted. I went through the verbose export (with every setting on default except IP on eth1 so I can access webfig) and I can see nothing that would cause this. Only minor settings with like SMB, OpenVPN default config and that sort of thing.Well, for now I will have to stay at 7.14.3. Thanks! ---

## Response 7
It remains "strange", even if it happens only on some particular versions the Ax2 is a common device and 7.15.2 is old enough that should have already been some reports.The good news are that 7.14.3 seems like a very stable version for wi-fi issues. ---

## Response 8
I have a third AX2 coming in next week. Also used, but under warranty this time. I hope it doesn't happen on that one. But yeah, at least a stable build works just fine now. I just wonder what the "decryption failed" means in Winbox4. I mean it's clearly related to the encrypted Winbox traffic, but I have not seen that error code anywhere, no documentation for it etc. Winbox3 just logs out. ---