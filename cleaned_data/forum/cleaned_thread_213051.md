# Thread Information
Title: Thread-213051
Section: RouterOS
Thread ID: 213051

# Discussion

## Initial Question
Hello, I tried searching the forums for someone with similar problem but couldn't find anyone that came up with a solution.So we have Mikrotik RB1100AHx4 that is on v6.49.2 and we have OVPN set up on it. We also have IPsec tunnel to one of our clients locations set up.So everything worked fine until month and a half ago. It would randomly stop accepting connections from OpenVPN Connect (tried both older and newer than v3.0 for the client).I have logging enabled for ipsec and ovpn with debug going to disk and ovpn logs show nothing. No new connection attempt, no connection blocked, literally nothing related with ovpn when this happens. Like no traffic is comming to the router related to ovpn, but also no reject entries from firewall. IPsec logs on the other hand show the connection between us and clients location and that works fine. Only when I restart our router does the ovpn start to work again and 9/10 it accepts connections just fine. But last time it happened it refused to work for about 4h even with restart.This happened on the mains power so first I switched it to UPS just to eliminate some power fluctuations but alas it did not help.We do have IP providers router in front of ours but that works just as a bridge and I'm waiting to hear from them if their logs show anything.The mind boggling thing is that this config worked just fine for 3+ years and only started acting up at the end of October. I also bought a new router, matched the firmware to the old one, copied the config manually and nothing, same problem after a week. So it's not a hardware fault of the router.At this point I exhausted my options and am hitting a wall. Any help with this and what direction I should go to look for next would be greatly appreciated. The fact that new router didn't fix the problem only tells me that it's either some bug in firmware that manifested now (hard to believe that it would work flawless for years) or that maybe it's a fault with my providers equipment. It's just such a specific problem that's hard to pinpoint to something without any help from logs.Edit:So when this happens, active connections remain active, just new ones can't be established.Here is the redacted config related to ovpn:
```
/ppp profileadddns-server=1.1.0.1,8.8.8.8local-address=OpenVPN-SerengetiPoolname=\OpenVPNremote-address=OpenVPN-SerengetiPooluse-encryption=requiredadddns-server=1.1.0.1local-address=OpenVPN-BackupPoolname=OpenVPN-Backup\
    remote-address=OpenVPN-BackupPooluse-encryption=required wins-server=\8.8.8.8/interfaceovpn-server serversetauth=sha1 certificate=CA-Servercipher=aes256default-profile=OpenVPN\
    enabled=yes netmask=16/interfacepptp-server serversetauthentication=chap,mschap1,mschap2default-profile=defaultclient config:
```

```
client
dev tun
proto tcp-client
remote(ouraddress)port1194nobind
persist-key
persist-tun
tls-client
remote-cert-tls server
ca CA-Certificate_new.crt
certUser-Cetificate_new.crt
keyUser-Cetificate_new.key
verb4mute10cipher AES-256-CBC
auth SHA1
auth-user-passsecret
auth-nocache
redirect-gateway def1I know there is a type-o in certificate name but this config is set up like that and stopped working randomly so all was entered correctly.I did get a new error in logs today
```

```
Dec/04/202412:21:50ovpn,info:usingencoding-AES-256-CBC/SHA1Dec/04/202412:22:27ovpn,debug<xxx.xxx.xxx.xxx>:disconnected<peer disconnected>Dec/04/202412:22:27ovpn,debug listening againforincoming connectionsDec/04/202412:22:27ovpn,info TCP connection establishedfromxxx.xxx.xxx.xxxDec/04/202412:22:27ovpn,debugnomore listeningforincoming connections:too busyDec/04/202412:22:27ovpn,debug,packet sent P_CONTROL_HARD_RESET_SERVER_V2 kid=0sid=9eaab3acb63e7cfcpid=0DATA len=0Dec/04/202412:22:27ovpn,debug<xxx.xxx.xxx.xxx>:disconnected<peer disconnected>Dec/04/202412:22:27ovpn,debug listening againforincoming connectionsDec/04/202412:22:27ovpn,info TCP connection establishedfromxxx.xxx.xxx.xxxDec/04/202412:22:27ovpn,debugnomore listeningforincoming connections:too busyDec/04/202412:22:27ovpn,debug,packet sent P_CONTROL_HARD_RESET_SERVER_V2 kid=0sid=92cfaa6a3e253feepid=0DATA len=0Dec/04/202412:22:27ovpn,debug<xxx.xxx.xxx.xxx>:disconnected<peer disconnected>Dec/04/202412:22:27ovpn,debug listening againforincoming connectionsDec/04/202412:22:27ovpn,info TCP connection establishedfromxxx.xxx.xxx.xxxDec/04/202412:22:27ovpn,debugnomore listeningforincoming connections:too busy

---
```

## Response 1
hi, i'm experiencing this problem too, anyone have the solution?i'm using CCR2004 and Router OS version 7.12.2 ---