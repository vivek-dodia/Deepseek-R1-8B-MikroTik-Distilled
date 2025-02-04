# Thread Information
Title: Thread-206646
Section: RouterOS
Thread ID: 206646

# Discussion

## Initial Question
Hello everyone! Is there a chance of addingAmneziaWG-protocolin future releases RouterOS? For example Keenetic already added this in beta-release. ---

## Response 1
+1Necessary thing ---

## Response 2
It uses Docker and takes a lot of space, it will not fit into most MikroTik routers ---

## Response 3
It uses Docker and takes a lot of space, it will not fit into most MikroTik routersIf keenetic who made routers for housewives can do this i can't believe Mikrotik can't.Maybe at least someone can create a wiki article of how to do this docker and how to configure it in simply words. I foundthis on githubbut didn't understand everything...My RB450Gx4 can handle dockers but it seems i have not enough brains to make it work so i'll be glad to every help to resist censorship.Also sorry for my english, it's not native language to me. ---

## Response 4
Also it says 2GB of RAM is needed for the server ---

## Response 5
I foundthis on githubbut didn't understand everything...Looks like it has everything needed. So all you need is a powerful ARM device with enough RAM ---

## Response 6
Also it says 2GB of RAM is needed for the serverMy server with 2 dockers (as far as i know new docker is created for every protocol and i have AWG and OpenVPN over Cloak installed) uses 500 Mbi.pngI foundthis on githubbut didn't understand everything...Looks like it has everything needed. So all you need is a powerful ARM device with enough RAMInstall Docker buildx subsystemI made it but how to use i can't understandBut that's not the theme of this forum i guess. Probably i have to find someone who can show this to me on fingers. ---

## Response 7
Their privacy policy starts withThe company Amnezia (hereinafter – the "company", "we", "us"), but nowhere do they seem to give more information about that company, like where are they located (ie under which jurisdiction to they fall)? They say that data can be transferred outside of the EU, but not to which countries. They do say they use Yandex, so I assume they mean that data can be send to Russia?Unless somebody has already shown that their apps adhere tohttps://reproducible-builds.org/I wouldn't put too much trust in themThat said, it would be nice if VPN configurations could be exported through a QR code in ROS. ---

## Response 8
t uses Docker and takes a lot of space, it will not fit into most MikroTik routersSorry guys, I hijack this thread.Hello, normis. Just do a bit deeper investigate to Amnezia, and found that you already implemented this. At least, about 95%.How it can be possible. Well, Amnezia just a little fork of Wireguard. It allow some tuning to prevent, or, at least, make it difficult to chinese great firewall, russian and iraq censorship to shutdown this. And, most important, have a full backward compatibility with standart wireguard. If you don't touch any values and leave itself by default, it works like standart wireguard.https://github.com/amnezia-vpn/amneziawg-goAmneziaWG is a fork of the WireGuard protocol. We have taken WireGuard as a basis and made some of its parameters (by which it is usually recognized by DPI systems) configurable, i.e. if we leave these parameters as default (equal to 0), AmneziaWG will work as a normal WireGuard.AmneziaWG has changed the headers of all packages:handshake packet (Initiator to Responder),response packet (Responder to Initiator),data packet, as well as special packet "Under Load" - by default they are random values, but you can change them in the settings.Random bytes are added to each auth packet to change its size.Thus "init and response packets" of the handshake additionally have "garbage" at the beginning of the data, the size of which is determined by the values S1 and S2. By default, the initiating handshake packet has a fixed size (148 bytes), and after adding garbage, its size will be 148 bytes +S1. The values for each packet are different for different users, so it is impossible to write a universal rule for tracking. In order to completely confuse DPI systems, Amnezia sends a certain number of "garbage" packets before starting a session. The number of such packets and their minimum and maximum size in bytes is also set in the settings, by the parameters Jc, Jmin and Jmax. ---

## Response 9
At least, about 95%.Well, if MikroTik uses native kernel module instead of user-space implementation of WireGuard - then probably less than 95% ---

## Response 10
Interesting concept. If some routers can be set to recognize vlan traffic and this rendition of WG, avoids that detection, would seem to have some value. ---

## Response 11
AmneziaWG also have a fork of wireguard linux kernel module.https://github.com/amnezia-vpn/amneziaw ... nel-moduleDifferences are very small.The link in first post is not for AmneziaWG, the correct link ishttps://docs.amnezia.org/documentation/amnezia-wg/ ---

## Response 12
MY AV does not like your link!! ---

## Response 13
This linkhttps://docs.amnezia.org/documentation/amnezia-wg/?There is a short description of AmneziaWG on the page.It is basically the same as avacha wrote a couple posts ago.The main link ishttps://github.com/amnezia-vpn/amneziaw ... nel-moduleThis is the source of kernel module based on original wireguard kernel module.Keenetic add the AmneziaWG support (The WireGuard advanced security configuration (ASC) parameters) to KeeneticOS in 4.2 Alpha 2.https://docs.keenetic.com/eaeu/ultra/kn ... lease.htmlIt is be great when Mikrotik do it too. ---

## Response 14
I'm with everyone who wants to see this feature added to RouterOS. What's more, if amneziawg already has a native kernel module, then porting it shouldn't take much time or resources. Honestly, I can't even begin to imagine how useful this would be in countries with authoritarian regimes. ---

## Response 15
There is a also a way to tunnelWireguardtrough other protocol obfuscation methods, for eg.Xray, it is possible to run it in ROS container if device has enough powerful CPU. I have setup in container similar to this setup for Linux -https://computerscot.github.io/wireguard-over-xray.html.Xrayrunning in container and it is forwarding port to Wireguard running in ROS which port is not even exposed to WAN, only dstnat forXrayin container - TCP 443. But also it can be used in combination, Wireguard exposed on input for direct connection and forwarding from Xray. This only works for Wireguard clients running on desktop OS'es, since on mobile OS'es doesn't allow multiple VPN's running at same time. Also ti should be possible to connect 2 ROS devices like that, one running Xray server in container, other Xray client... ---

## Response 16
+1 for this feature, really interested in it. It would be really cool if this protocol was supported natively ---

## Response 17
+1I want to support the initiative. The improvement doesn't look very complicated, but it will make it possible to bypass blocking ---

## Response 18
+1I'm also looking forward to native support. ---

## Response 19
+1Very need it ---

## Response 20
It uses Docker and takes a lot of space, it will not fit into most MikroTik routersIt haslinux-kernel-modulefyiAnd awg tun interface can be linked to vanilla wireguard:Jc = 1 ≤ Jc ≤ 128; recommended range is from 3 to 10 inclusiveJmin = Jmin < Jmax; recommended value is 50Jmax = Jmin < Jmax ≤ 1280; recommended value is 1000S1 = 0S2 = 0H1 = 1H2 = 2H3 = 3H4 = 4 ---

## Response 21
Really needed, will help with remote employees to provide continuous stable communication ---

## Response 22
+1This feature very useful in non free country and help to bypass VPN blocking. ---

## Response 23
Hi guys, I'm trying to run the container with amnezia wg. Why do I get error: could not find image manifest in archive. What am I doing wrong? ---

## Response 24
+1Perhaps the developers will be able to compile the awg kernel for RoS. It will be very cool, because all VPN protocols that Mikrotik supports already can be blocked by DPI. So if you want to have a VPN tunnel with which the router can work, you need a separate server with this VPN. ---

## Response 25
Last I checked, there's plenty of vpn or equivalent sneaky ways to get a MT to bypass a state based vpn block, that doesnt require some 'magic' plugin for MT that "would work", but other existing mechanisms already onboard dont... ---

## Response 26
+1I'm also looking forward to native support. ---

## Response 27
Last I checked, there's plenty of vpn or equivalent sneaky ways to get a MT to bypass a state based vpn block, that doesnt require some 'magic' plugin for MT that "would work", but other existing mechanisms already onboard dont...Please enlighten us as most States have ways of detecting VPN patterns regardless of tricks. This solution seems unique in its ability to appear random. ---

## Response 28
https://hub.docker.com/r/wiktorbgu/amneziawg-mikrotikI compiled the images and wrote instructions for launching.Works both in client and server mode.If Mikrotik had also implemented thedriver into the kernel, it would have been much better. ---

## Response 29
+1 you just need to allow overriding the standard values of some wg fields in order for amneziawg to work. It's not difficult! We are really waiting ---

## Response 30
+ 1 ---

## Response 31
You know people who join just to PLUS1 this thread are either bots, trolls, or the original poster LOL.............. no one is fooled by this stupidity.EDIT: the stupidity continues see below. ---

## Response 32
+ 1 ---

## Response 33
https://hub.docker.com/r/wiktorbgu/amneziawg-mikrotikI compiled the images and wrote instructions for launching.Works both in client and server mode.If Mikrotik had also implemented thedriver into the kernel, it would have been much better.Is there any firewall rule needed to send incoming port 51820 to the VETH IP of the AmneziaWG container? Nothing about that in the manual.I created VETH 172.17.0.6 with gateway 172.17.0.1 and also added NAT rule, to send incoming packets on 51820 to 51820 on 172.17.0.6 and configured everything as in manual.I'm trying to get this to work, but no luck for now. I can see incoming packets on 51820 if i add rule in Firewall NAT, but nothing afterwards.Trying to help a friend who want's to watch home television (SLO) when he works all over the world and also in Russia, but no luck for now. All other protocols are practicaly cripled and unusable there. ---

## Response 34
yet another properitary shortlived VPN solution - no thanks. ---

## Response 35
yet another properitary shortlived VPN solution - no thanks.sounds like a shortsighted opinion............. the concept has validity whether or not we will ever see a viable rendition is anyones guess. ---

## Response 36
I added this in awg0.conf
```
[Interface]Address=10.0.0.1/24ListenPort=51820PrivateKey=2ONX7xNsinRtVLG5STJwGkA1T57sX1SJ8Sy898rB6Us=Jc=4Jmin=50Jmax=1000S1=146S2=42H1=532916466H2=2096090865H3=406337014H4=57583056# Add IP masqueradingPostUp=iptables-t nat-A POSTROUTING-o eth0-j MASQUERADE# Del IP masqueradingPostDown=iptables-t nat-D POSTROUTING-o eth0-j MASQUERADE[Peer]PublicKey=kY6T9/56TWyaWg2uKIZynED7uOdJWR5ygOyG60OEZHA=AllowedIPs=10.0.0.2/32And this in awg.conf
```

```
[Interface]PrivateKey=sFMkMpJqU+8fzsKFiUvmZs64GzpafAPDJgSlil9HslE=Address=10.0.0.2/24DNS=8.8.8.8,1.1.1.1MTU=1440Jc=6Jmin=50Jmax=1000S1=0S2=0H1=1H2=2H3=3H4=4# Add IP masqueradingPostUp=iptables-t nat-A POSTROUTING-o%i-j MASQUERADE# Del IP masqueradingPostDown=iptables-t nat-D POSTROUTING-o%i-j MASQUERADE# Replace 192.168.254.1 with your router IP address in the bridge where the container is located# exclude local networksPreUp=ip routeadd10.0.0.0/8via192.168.254.1dev eth0# Here is the IP of the EndpointPreUp=ip routeaddIP via192.168.254.1dev eth0[Peer]PublicKey=z7tnHzJqSqwtkt4MiqfoQAZW4f5YM0JUR3elbOr8bh0=AllowedIPs=0.0.0.0/1,128.0.0.0/1# don't use 0.0.0.0/0PersistentKeepalive=25Endpoint=IP:51820also i added firewall rule, that sends all packets comming in on 51820 to VETH IP of AmneziaWGadd action=dst-nat chain=dstnat comment=AmneziaTEST dst-port=51820 in-interface=ether1 protocol=udp to-addresses=172.17.0.6 to-ports=51820Test client is a HapAX Lite LTE6 on mobile network.Trying to ping server from client... nothing
```

```
[admin@MikroTik]>/container shell0MikroTik:/#ping10.0.0.1PING10.0.0.1(10.0.0.1):56data bytes^CAlso i tried with this on my phone with Amnezia app and found Handshake did not complete after 5 seconds somewhere in logs.
```

```
[Interface]PrivateKey=sFMkMpJqU+8fzsKFiUvmZs64GzpafAPDJgSlil9HslE=Address=10.0.0.2/24ListenPort=51820DNS=10.0.0.1MTU=1440Jc=6Jmin=50Jmax=1000S1=0S2=0H1=1H2=2H3=3H4=4[Peer]PublicKey=z7tnHzJqSqwtkt4MiqfoQAZW4f5YM0JUR3elbOr8bh0=AllowedIPs=0.0.0.0/1,128.0.0.0/1Endpoint=X.sn.mynetname.net:51820ifconfig on server:
```

```
[admin@MikroTik]>/container shell4MikroTik:/#ifconfig
awg0Linkencap:UNSPECHWaddr00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00inet addr:10.0.0.1P-t-P:10.0.0.1Mask:255.255.255.0UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1420Metric:1RX packets:0errors:0dropped:0overruns:0frame:0TX packets:7errors:0dropped:0overruns:0carrier:0collisions:0txqueuelen:500RX bytes:0(0.0B)TX bytes:588(588.0B)eth0Linkencap:EthernetHWaddr7E:52:ED:6D:79:4Finet addr:172.17.0.6Bcast:0.0.0.0Mask:255.255.255.0inet6 addr:fe80::7c52:edff:fe6d:794f/64Scope:LinkUP BROADCAST RUNNING MULTICAST  MTU:1500Metric:1RX packets:160861errors:0dropped:0overruns:0frame:0TX packets:1612errors:0dropped:0overruns:0carrier:0collisions:0txqueuelen:1000RX bytes:39345228(37.5MiB)TX bytes:71888(70.2KiB)loLinkencap:LocalLoopbackinet addr:127.0.0.1Mask:255.0.0.0inet6 addr:::1/128Scope:HostUP LOOPBACK RUNNING  MTU:65536Metric:1RX packets:25errors:0dropped:0overruns:0frame:0TX packets:25errors:0dropped:0overruns:0carrier:0collisions:0txqueuelen:1000RX bytes:2658(2.5KiB)TX bytes:2658(2.5KiB)ifconfig on client:
```

```
[admin@MikroTik]>/container shell0MikroTik:/#ifconfig
awgLinkencap:UNSPECHWaddr00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00inet addr:10.0.0.2P-t-P:10.0.0.2Mask:255.255.255.0UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1440Metric:1RX packets:0errors:0dropped:0overruns:0frame:0TX packets:0errors:0dropped:0overruns:0carrier:0collisions:0txqueuelen:500RX bytes:0(0.0B)TX bytes:0(0.0B)eth0Linkencap:EthernetHWaddrA6:63:14:35:17:B7  
          inet addr:192.168.254.4Bcast:0.0.0.0Mask:255.255.255.0inet6 addr:fe80::a463:14ff:fe35:17b7/64Scope:LinkUP BROADCAST RUNNING MULTICAST  MTU:1500Metric:1RX packets:56128errors:0dropped:0overruns:0frame:0TX packets:69314errors:0dropped:0overruns:0carrier:0collisions:0txqueuelen:1000RX bytes:2742689(2.6MiB)TX bytes:34784346(33.1MiB)loLinkencap:LocalLoopbackinet addr:127.0.0.1Mask:255.0.0.0inet6 addr:::1/128Scope:HostUP LOOPBACK RUNNING  MTU:65536Metric:1RX packets:0errors:0dropped:0overruns:0frame:0TX packets:0errors:0dropped:0overruns:0carrier:0collisions:0txqueuelen:1000RX bytes:0(0.0B)TX bytes:0(0.0B)Any idea what i am doing wrong, wiktorbgu or anyone else?

---
```

## Response 37
I have the same problem, it's necessary feature to add on routeros ---

## Response 38
I confirm that Amnesia WG is running on Keenetic and DPI does not detect packets. I would really like to implement it on Mikrotik. ---

## Response 39
It's a big mystery to me why the company hasn't added this protocol AmneziaWG to its products yet. to implement this protocol you need a minimum of effort, and the benefit will be colossal. I think marketers should be fired because they do not understand the market requirements and are poorly oriented in the needs of users. If you have the opportunity, write to the company atsupport@mikrotik.comand say that you need to have this protocol, they do not read this forum and it will not help us what we write here. ---

## Response 40
I wrote in support and even gave a link to this topic in the text of the letter here. ---

## Response 41
So, after some help from wiktorbgu we managed to get this docker instance working using following options:awg.conf
```
[Interface]PrivateKey=sFMkMpJqU+8fzsKFiUvmZs64GzpafAPDJgSlil9HslE=Address=10.0.0.2/24MTU=1440Jc=4Jmin=50Jmax=1000S1=146S2=42H1=532916466H2=2096090865H3=406337014H4=57583056# Add IP masqueradingPostUp=iptables-t nat-A POSTROUTING-o%i-j MASQUERADE# Del IP masqueradingPostDown=iptables-t nat-D POSTROUTING-o%i-j MASQUERADETable=awgPostUp=ip ruleaddpriority300fromall iif eth0 lookup awg||truePostDown=ip ruledelfromall iif eth0 lookup awg||true[Peer]PublicKey=z7tnHzJqSqwtkt4MiqfoQAZW4f5YM0JUR3elbOr8bh0=AllowedIPs=0.0.0.0/1,128.0.0.0/1# don't use 0.0.0.0/0PersistentKeepalive=25Endpoint=*.sn.mynetname.net:51820Replace * with your DNS name.This is for server, awg0.conf
```

```
[Interface]Address=10.0.0.1/24ListenPort=51820PrivateKey=2ONX7xNsinRtVLG5STJwGkA1T57sX1SJ8Sy898rB6Us=Jc=4Jmin=50Jmax=1000S1=146S2=42H1=532916466H2=2096090865H3=406337014H4=57583056# Add IP masqueradingPostUp=iptables-t nat-A POSTROUTING-o eth0-j MASQUERADE# Del IP masqueradingPostDown=iptables-t nat-D POSTROUTING-o eth0-j MASQUERADETable=awgPostUp=ip ruleaddpriority300fromall iif eth0 lookup awg||truePostDown=ip ruledelfromall iif eth0 lookup awg||true[Peer]PublicKey=kY6T9/56TWyaWg2uKIZynED7uOdJWR5ygOyG60OEZHA=AllowedIPs=0.0.0.0/0

---
```

## Response 42
Hello! I wrote to technical support and received the following response:Hello, Thank you for contacting MikroTik Support.We do not have any plans to add such a feature at the moment, but if more users will request it, we will see how this can be implemented.Best regards, Therefore, if you are interested in adding the protocol, also write to technical support with a request to add amneziawg ---

## Response 43
https://hub.docker.com/r/wiktorbgu/amneziawg-mikrotikI compiled the images and wrote instructions for launching.Works both in client and server mode.If Mikrotik had also implemented thedriver into the kernel, it would have been much better.On my Mikrotik RB5009, your container started without problems, but on the Mikrotik CHR it doesn't start. Start and immediately stop occurs without recording in the logs. I think it's because i need an amd64 docker image. Please add an amd64 image. ---

## Response 44
Please add an amd64 image.Initially, everything is done and tested for all Mikrotik arm, arm64 and amd64.https://hub.docker.com/r/wiktorbgu/amne ... rotik/tags ---

## Response 45
Yes, you're right, I didn't see this tag.sorryYour container starts only if there is a 'usb1' root folder in the files didectory.For example if dir is '/usb1/docker/pull' - all is ok, if dir is '/docker/pull' - image not starting.I think there is no need to set the 'usb1' root directory in Mikrotik CHR....but for this image it is necessary. ---