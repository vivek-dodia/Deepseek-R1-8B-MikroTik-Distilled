# Thread Information
Title: Thread-1114322
Section: RouterOS
Thread ID: 1114322

# Discussion

## Initial Question
Is there any other way to use a VPN even if my ISP is blocked Wireguard?I have tried to change port 443, 8295 for wireguard but it's not connectingWireGuard is not connectingfound this error in logs:wireguard1: [test] KQf3CazJ+nfylMl+Nnajsfnjsd TUT6yoyX/xbxPNzEE=: Handshake for peer did not complete after 5 seconds, retrying (try 2).It may look like:WG peer Client Listen port 51820 is blocked by ISP ---

## Response 1
Try BTH.https://help.mikrotik.com/docs/spaces/R ... ck+To+Home ---

## Response 2
If the ISP is blocking wireguard, the fact that you have tried numerous ports tells me that they are checking DPI, into the weeds to see the type of traffic.Therefore suggesting BTH is fruitless.However, if the lack of connection is eithera. operator config errorb. no access to public IPThen BTH may help alleviate both. :-0So question to OP, is your config correct and do you have a public IP. ---

## Response 3
I have a public IP on my Router.Wireguard was working fine before ISP changed its policies.but now the Wireguaurd is not connecting. Sometimes it connected but suddenly disconnected.I also tried "bth" but it is also blocked.Please help me if there is any other wayThanks ---

## Response 4
ikev2 (ipsec) is well supported, and there are fairly good examples around.https://help.mikrotik.com/docs/spaces/R ... enticationThis is more industrial, so perhaps less likely to be dropped.But if your ISP doesn't want you running VPN's. You will struggle. ---

## Response 5
Or change ISP ?A party blocking VPN is not worth to receive your money. ---

## Response 6
Or change ISP ?A party blocking VPN is not worth to receive your money.actually all ISPs and organizations blocking vpn ---

## Response 7
Yup, it's not a matter of switching the ISP, it's a matter of switching the country. AmneziaWG seems to be successful in addressing this type of issue, but you need a Mikrotik that supports containers or a completely different hardware. Depending on the country, it may or may not be enough. ---

## Response 8
Yup, it's not a matter of switching the ISP, it's a matter of switching the country. AmneziaWG seems to be successful in addressing this type of issue, but you need a Mikrotik that supports containers or a completely different hardware. Depending on the country, it may or may not be enough.any advice on what I need to do how I can use a VPN or which port I can use?I think they are not blocking ports they are blocking the VPN protocol. ---

## Response 9
SSTP looks almost like a normal HTTPS connection but it is relatively slow. The initial packets of all other VPN protocols are quite distinctive so easy to spot using DPI and therefore easy to block. AmneziaWG targets exactly this. ---

## Response 10
SSTP looks almost like a normal HTTPS connection but it is relatively slow. The initial packets of all other VPN protocols are quite distinctive so easy to spot using DPI and therefore easy to block. AmneziaWG targets exactly this.Scenario is thatI have Mikrotik CHR on Digital Ocean. We are using CHR as a WireGuard Server.We have installed the WG application on Android and iPhone, ISP blocks this and we can't establish a connection with CHR-WireGuard Server.In this case How I can deploy AmneziaWG?orI need to deploy any other machine for AmneziaWG on Cloud? ---

## Response 11
I do know people who run containers on CHRs running in the cloud, because it is simpler than to set up a separate virtual machine there. But keeping a CHR only as a host for a single container would make little sense so maybe spawning a dedicated Debian machine may be a better choice for you - I don't have enough information to recommend you any of these variants. ---

## Response 12
We have installed the WG application on Android and iPhone, ISP blocks this and we can't establish a connection with CHR-WireGuard Server.In this case How I can deploy AmneziaWG?orI need to deploy any other machine for AmneziaWG on Cloud?1. Leave server as is, and try Amnezia client for smartphone. Amnezia client needs exactly same config as usual wg (qr scan almost dead, import client config works fine). Don't forget to switch on obfuscation checkbox.2. If there is no luck with #1, try clean vps (without router os, just clean any kind of os like Ubuntu) with libreswan.Here is ready script for most OS:https://github.com/hwdsl2/setup-ipsec-vpnUse strongSwan smartPhone app , import file xxx.sswan which will be generated as a result of #2.I have couple of cases with pretty same problems, both #1 and #2 work fine. ---

## Response 13
We have installed the WG application on Android and iPhone, ISP blocks this and we can't establish a connection with CHR-WireGuard Server.In this case How I can deploy AmneziaWG?orI need to deploy any other machine for AmneziaWG on Cloud?1. Leave server as is, and try Amnezia client for smartphone. Amnezia client needs exactly same config as usual wg (qr scan almost dead, import client config works fine). Don't forget to switch on obfuscation checkbox.2. If there is no luck with #1, try clean vps (without router os, just clean any kind of os like Ubuntu) with libreswan.Here is ready script for most OS:https://github.com/hwdsl2/setup-ipsec-vpnUse strongSwan smartPhone app , import file xxx.sswan which will be generated as a result of #2.I have couple of cases with pretty same problems, both #1 and #2 work fine.hello, I have test AmneziaWG on my android it is working but Instagram isn't working I can't able to test all the apps.AmneziaWG is slower then Wireguard.but some time Wireguard is working. and working perfectly fine.one moe thing Wireguard is much faster then AmneziaWG. ---

## Response 14
What speeds do you achieve? Are you sure, you have full tunnel and not maybe some split tunnelig? Because AmneziaWG isn't realy much different then ordinary WG, so anything, that worked there, should also work with AmneziaWG.¸It could also be MTU issue. Many times, when some sites don't load it's a MTU issue. ---

## Response 15
What speeds do you achieve? Are you sure, you have full tunnel and not maybe some split tunnelig? Because AmneziaWG isn't realy much different then ordinary WG, so anything, that worked there, should also work with AmneziaWG.¸It could also be MTU issue. Many times, when some sites don't load it's a MTU issue.There is a bit of difference between when scrolling up on YouTube, Insta etc also on speed test a bit differenceon ROS I have default MTU. ---

## Response 16
Well, i was asking for something like speedtest.net results.Try with this in firewall mangle rule. See if it fixes anything.
```
addaction=change-mss chain=forward comment="Clamp MTU to PMTU"disabled=yesnew-mss=clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=syn

---
```

## Response 17
...without thedisabled=yesof course. ---

## Response 18
MISSING!!Besides the disabled=yes error, where is the interface?designated on that rule.Try/ip firewall mangleadd action=change-mss chain=forward comment="Clamp MSS to PMTU for Outgoing packets" new-mss=clamp-to-pmtuout-interface=wireguard1passthrough=yes protocol=tcp tcp-flags=synIf you dont see any difference with that mangle rule you an also try this mangle rule./ip firewall mangleadd action=change-mss chain=forward new-mss=1380out-interface=wireguard1protocol=tcp tcp-flags=syn tcp-mss=1381-65535 ---

## Response 19
I only copied it from my 5009. I'm not using that rule right now and that is why it's disabled. I found it in such form (without interface) somewhere on the internet or even maybe on this forum.Thanks for fixing it. ---

## Response 20
MISSING!!Besides the disabled=yes error, where is the interface?designated on that rule.Try/ip firewall mangleadd action=change-mss chain=forward comment="Clamp MSS to PMTU for Outgoing packets" new-mss=clamp-to-pmtuout-interface=wireguard1passthrough=yes protocol=tcp tcp-flags=synIf you dont see any difference with that mangle rule you an also try this mangle rule./ip firewall mangleadd action=change-mss chain=forward new-mss=1380out-interface=wireguard1protocol=tcp tcp-flags=syn tcp-mss=1381-65535Thank you ---