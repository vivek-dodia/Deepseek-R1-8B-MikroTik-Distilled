# Thread Information
Title: Thread-1120818
Section: RouterOS
Thread ID: 1120818

# Discussion

## Initial Question
good morning, I have the configuration as below on a 5009, two zyxel nwa50ax aps are connected to it. the two aps have a fixed ip of the same class as the 5009. All the devices connect and receive the ip except two iphones that cannot receive the ip. if I set the fixed ip on the 5009 they connect otherwise nothing. I can't find the problem. the 5009 has firmware 7.17# 2025-01-16 16:53:56 by RouterOS 7.16.2# software id = MHM4-RZ9P## model = RB5009UG+S+# serial number = ***/interface bridgeadd name=lan port-cost-mode=short/interface ethernetset [ find default-name=ether1 ] name=WAN/ip dhcp-serveradd interface=lan lease-time=12h name=dhcp1/ip kid-controladd name=Andrewadd name=Vivi/ip pooladd name=dhcp_pool ranges=192.168.1.2-192.168.1.254/zerotierset zt1 comment="ZeroTier Central controller -https://my.zerotier.com/" name=zt1 port=9993/zerotier interfaceadd allow-default=no allow-global=no allow-managed=yes disabled=no instance=zt1 name=zerotier1 network=--/interface bridge portadd bridge=lan interface=ether2 internal-path-cost=10 path-cost=10add bridge=lan interface=ether3 internal-path-cost=10 path-cost=10add bridge=lan interface=ether4 internal-path-cost=10 path-cost=10add bridge=lan interface=ether5 internal-path-cost=10 path-cost=10add bridge=lan interface=ether6 internal-path-cost=10 path-cost=10add bridge=lan interface=ether7 internal-path-cost=10 path-cost=10add bridge=lan interface=ether8 internal-path-cost=10 path-cost=10/ip firewall connection trackingset udp-timeout=10s/ip addressadd address=192.168.1.1/24 interface=lan network=192.168.1.0add address=192.168.0.200/24 interface=WAN network=192.168.0.0/ip dhcp-clientadd interface=WAN/ip dhcp-server leaseadd address=192.168.1.18 mac-address=56:46:4F:A0:2B:32 server=dhcp1add address=192.168.1.22 mac-address=1A:0B:D3:9D:47:FB server=dhcp1add address=192.168.1.23 mac-address=D8:A0:11:D6:35:B3 server=dhcp1/ip dhcp-server networkadd address=192.168.1.0/24 dns-server=8.8.8.8 domain=Workgroup gateway=192.168.1.1 netmask=24/ip dnsset servers=8.8.8.8/ip firewall filteradd action=accept chain=forward in-interface=zerotier1add action=accept chain=input in-interface=zerotier1add action=accept chain=input connection-state=established, related, untrackedadd action=drop chain=forward connection-state=invalidadd action=drop chain=input connection-state=invalid/ip firewall natadd action=masquerade chain=srcnat out-interface=WAN src-address=192.168.1.0/24/ip ipsec profileset [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5/ip kid-control deviceadd mac-address=0C:2C:54:C6:EB:11 name=HUAWEI_P20_lite-6bea8d290 user=Vivi/ip routeadd disabled=no dst-address=0.0.0.0/0 gateway=192.168.0.1 routing-table=main suppress-hw-offload=no/system note ---

## Response 1
I think you forgot to "attach" your IP pool to the DHCP server:
```
/ip dhcp-serveraddinterface=lan lease-time=12hname=dhcp1/ip pooladdname=dhcp_pool ranges=192.168.1.2-192.168.1.254Should be:
```

```
/ip dhcp-serveraddaddress-pool=dhcp_poolinterface=lan lease-time=12hname=dhcp1/ip pooladdname=dhcp_pool ranges=192.168.1.2-192.168.1.254Be aware that there are no IP addresses available within this scope that can be used staticly (by which I mean, set on the client).Instead of staic IP address, please use static leases (as you already did according to /ip dhcp-server lease).

---
```

## Response 2
so I have to leave the AP in DHCP and give and assign the static IP for the AP on the 5009? ---

## Response 3
What it means (after correcting that DHCP pool problem):your pool is completely using the subnet.But it should not be a problem.DHCP server is smart enough to first check if an IP address is already in use before handing it out. But you will not see it right away then.So, couple of options:Either you make the IP pool smaller and then you can use the excluded part to assign IP addresses manually on device *but it will not show in DHCP leases)Or leave pool as is and assign IP leases statically in DHCP server (benefit: you will see in the lease table which addresses are in use, dynamic and static)Or: Set static DHCP lease but configure it anyhow on the device itself too (I do this for printers, servers, NAS, things like that).If for some reason that device gets confused and asks for a DHCP lease, it will get the one you are expecting it to get so you don't need to go hunting around where it is. Also, if your router breaks down or whatever, you can still access some of your network devices via their IP address. ---

## Response 4
Be aware that there are no IP addresses available within this scope that can be used staticly (by which I mean, set on the client).Instead of staic IP address, please use static leases (as you already did according to /ip dhcp-server lease).I misunderstood what was written here. I solved it by selecting dhcp_pool in Address Pool. Thanks for the replies. ---

## Response 5
Just to be sure, better not use static IP addresses, instead work with staic leases (where clients use DHCP client).If the topic is answered, please feel free to mark it as solved. ---

## Response 6
One problem is duplication of WAN, either use IP address OR ip dhcp client, NOT both!!!/ip addressadd address=192.168.1.1/24 interface=lan network=192.168.1.0add address=192.168.0.200/24 interface=WAN network=192.168.0.0/ip dhcp-clientadd interface=WANIs this device your router? No firewall rules?? ---

## Response 7
One problem is duplication of WAN, either use IP address OR ip dhcp client, NOT both!!!/ip addressadd address=192.168.1.1/24 interface=lan network=192.168.1.0add address=192.168.0.200/24 interface=WAN network=192.168.0.0/ip dhcp-clientadd interface=WANIs this device your router? No firewall rules??yes this acts as a router, I have a natted 5g modem upstream. do I need to add firewall rules? ---

## Response 8
If you are assigned an internal IP address from your 5G provider's modem, then you do not need additional firewall rules. Your internal LAN address must be different from the modem's IP. ---

## Response 9
I would never rely on NAT and an ISPs modem to provide security. So yes, I think you should add the standard set of firewall rules. ---

## Response 10
If you are assigned an internal IP address from your 5G provider's modem, then you do not need additional firewall rules. Your internal LAN address must be different from the modem's IP.ok. I assigned 192.168.0.1 to the external modem, 192.168.0.200 to the wan-ether1 port and 192.168.1.1/24 to the LAN ---

## Response 11
I would never rely on NAT and an ISPs modem to provide security. So yes, I think you should add the standard set of firewall rules.could you tell me which rules to add? ---

## Response 12
/ip firewall address-list(using static dhcp leases)add address=192.168.1.X list=Authorized comment="admin desktop"add address=192.168.1.Y list=Authorized comment="admin laptop"add address=192.168.1.Z list=Authorized comment="admin smartphone"/ip firewall filteradd action=accept chain=input connection-state=established, related, untrackedadd action=drop chain=input connection-state=invalidadd action=accept chain=input protocol=icmpadd action=accept chain=input dst-address=127.0.0.1add action=accept chain=input comment="admin to router" in-interface-list=LAN src-address-list=Authorizedadd action=accept chain=input comment="allow zerotier users to router" in-interface=zerotier1add action=accept chain=input comment="users to services" in-interface-list=LAN dst-port=53 protocol=udpadd action=accept chain=input comment="users to services" in-interface-list=LAN dst-port=53 protocol=tcpadd action=drop chain=input comment="Drop all else"{ add this last }++++++++++++++++++++++++++++++++++++++add action=fasttrack-connection chain=forward connection-state=established, relatedadd action=accept chain=forward connection-state=established, related, untrackedadd action=drop chain=forward connection-state=invalidadd action=accept chain=forward comment="internet traffic" in-interface-list=LAN out-interface-list=WANadd action=accept chain=forward comment="allow zerotier users to LAN" in-interface=zerotier1 dst-address=192.168.1.0/24add action=drop chain=forward comment="drop all else" ---

## Response 13
Hi, I applied the rules you recommended. Thank you for your time. Is there a guide for novice users to study? ---

## Response 14
/ip firewall address-list(using static dhcp leases)add address=192.168.1.X list=Authorized comment="admin desktop"add address=192.168.1.Y list=Authorized comment="admin laptop"add address=192.168.1.Y list=Authorized comment="admin smartphone"/ip firewall filteradd action=accept chain=input connection-state=established, related, untrackedadd action=drop chain=input connection-state=invalidadd action=accept chain=input protocol=icmpadd action=accept chain=input dst-address=127.0.0.1add action=accept chain=input comment="admin to router" in-interface-list=LAN src-address-list=Authorizedadd action=accept chain=input comment="allow zerotier users to router" in-interface=zerotier1add action=accept chain=input comment="users to services" in-interface-list=LAN dst-port=53 protocol=udpadd action=accept chain=input comment="users to services" in-interface-list=LAN dst-port=53 protocol=tcpadd action=drop chain=input comment="Drop all else"{ add this last }++++++++++++++++++++++++++++++++++++++add action=fasttrack-connection chain=forward connection-state=established, relatedadd action=accept chain=forward connection-state=established, related, untrackedadd action=drop chain=forward connection-state=invalidadd action=accept chain=forward comment="internet traffic" in-interface-list=LAN out-interface-list=WANadd action=accept chain=forward comment="allow zerotier users to LAN" in-interface=zerotier1 dst-address=192.168.1.0/24add action=drop chain=forward comment="drop all else"Hi, since I applied these rules I can't access the router remotely through zerotier while I can access the APs and the printer. ---

## Response 15
I am not a zerotier expert, but assuming stating the zerotier interface on the input chain rule was not enough or accurate, perhaps you need to add actual IP address??? ---

## Response 16
I am not a zerotier expert, but assuming stating the zerotier interface on the input chain rule was not enough or accurate, perhaps you need to add actual IP address???ok. which rule should i copy inserting the exact zerotier ip?fix: I can reach Mikrotik from winbox but not from web page.I can't with iphone. ---