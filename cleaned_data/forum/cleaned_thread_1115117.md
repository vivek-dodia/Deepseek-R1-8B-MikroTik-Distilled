# Thread Information
Title: Thread-1115117
Section: RouterOS
Thread ID: 1115117

# Discussion

## Initial Question
hi guysabout this topic :viewtopic.php?t=189729unfortunately, all tunnel (IPIP, EoIP, GRE, WireGuard, and etc) and all vpn protocols (pptp, l2tp, sstp, open-vpn and etc) dropped and blocked in iran.all port sniffed, analyzed and captured by iran regime.for example :you can visit website and transfer data on port 443 and it work well, but if you run SSTP or Open-VPN or Socks5 and etc on 443 port it dosnt work !!! but when you running port scan by wireshark, you will see port 433 is open ! but you cant run tunnel on this port !!! becuse port check by dpiiran regime run this method by DPI filternig and there is one of the most powerfull DPI device that bought from chiness and russia and runed in IRAN.now in iran v2ray protocol work well.dear mikrotik please help us by adding v2ray protocol on next ros version or please write an article to help install and configuration v2ray on mikrotik container to bypass filtering device.by the way do you have creative idea to bypass DPI ? can you deploy and run obfuscation traffic on MikroTik?I can provid one mikrotik in IRAN to check and analyze.please help iranian#opIran#to_help_iran ---

## Response 1
have you tried a ssh socks proxy? ---

## Response 2
How do you use ssh socks proxy on Mikrotik? Those guys have mostly Tik hardware for various reasons, and OpenWRT is not available for each Tik model... Plus with DPI, the next step will be to ban SSH to foreign IPs. ---

## Response 3
have you tried a ssh socks proxy?Socks and Socks5 is block ---

## Response 4
Plus with DPI, the next step will be to ban SSH to foreign IPs.yes, thats right ---

## Response 5
That's right. The current situation in Iran’s network is such thatall VPN and tunneling protocols are either blocked or barely functional. It would be beneficial if Mikrotik OS could support theV2RAY client protocol. This protocol, with adjustable masquerade settings, could make the traffic resemble that of regular browser traffic. As a result, we couldresumeusing Mikrotik routers without the need for OpenWRT or any additional Linux server.The V2RAY protocol is currently the most effective method for transmitting data. It is specifically designed to withstand severe internet censorship, not just for sending traffic over a private network that can be easily blocked. Therefore, its implementation would allow us to once again benefit from internet access through Mikrotik routers.We would greatly appreciate it if Mikrotik could consider this protocol and think about incorporating V2RAY into the VPN clients in ROS. ---

## Response 6
ssh tunnel and Amnezia VPN could also help here. But, unfortunately, Mikrotik does not support this at the moment ---

## Response 7
Can amnezia vpn be run on a server/pc behind the router ?? ---

## Response 8
I also have this exact problem and I was only able to connect with nekoray software. This software also creates a virtual interface. So that I can connect Mikrotik to another Ethernet, in this way, by writing a rule, I can pass all the traffic of filtered sites through it.This makes the network very complex and unstable ---

## Response 9
Dear friends, thank you for your support.Thank you, if such a feature is added in the new Mikrotik update, please let me know here----------------------------------------------------------------------------------------------hi guysabout this topic :viewtopic.php?t=189729unfortunately, all tunnel (IPIP, EoIP, GRE, WireGuard, and etc) and all vpn protocols (pptp, l2tp, sstp, open-vpn and etc) dropped and blocked in iran.all port sniffed, analyzed and captured by iran regime.for example :you can visit website and transfer data on port 443 and it work well, but if you run SSTP or Open-VPN or Socks5 and etc on 443 port it dosnt work !!! but when you running port scan by wireshark, you will see port 433 is open ! but you cant run tunnel on this port !!! becuse port check by dpiiran regime run this method by DPI filternig and there is one of the most powerfull DPI device that bought from chiness and russia and runed in IRAN.now in iran v2ray protocol work well.dear mikrotik please help us by adding v2ray protocol on next ros version or please write an article to help install and configuration v2ray on mikrotik container to bypass filtering device.by the way do you have creative idea to bypass DPI ? can you deploy and run obfuscation traffic on MikroTik?I can provid one mikrotik in IRAN to check and analyze.please help iranian#opIran#to_help_iran ---

## Response 10
People wants to penetrate DPI firewalls in few clicks while using containers it is already possible, but requires more clicks and keyboard presses... ---