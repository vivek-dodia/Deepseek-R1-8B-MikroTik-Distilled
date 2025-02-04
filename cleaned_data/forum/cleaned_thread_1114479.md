# Thread Information
Title: Thread-1114479
Section: RouterOS
Thread ID: 1114479

# Discussion

## Initial Question
Daer all, I have tried so many times. but port forwarding is not working on DigitalOcean.I want to forward port8295, 8296, 8297, 8298.But on the port checker against my public IP, it shows 8295, 8296 is blocked and 8297, 8298 is opened.but when I changed the CHR 8295 port to my Winbox then it worked for Winbox access.but port forward is not working on open ports too.here is my nat configuration./ip firewall natadd action=masquerade chain=srcnat src-address=172.16.7.0/24add action=masquerade chain=srcnat src-address=172.16.8.0/24add action=dst-nat chain=dstnat dst-port=8295 in-interface-list=\WAN-Interface-List protocol=tcp to-addresses=172.16.7.19 to-ports=8297add action=dst-nat chain=dstnat dst-port=8297 in-interface-list=\WAN-Interface-List protocol=tcp to-addresses=172.16.7.19 to-ports=8298 ---

## Response 1
No idea what digital ocean is, so your first statement is meaningless.Is this a server on your LAN, is it a server in the cloud that you control, etc etc..Technically:Why are you port forwarding winbox ports?? Do you not know that winbox is a router service and not a LAn service??Security: Why are you port forwarding winbox ports?? They should only be used from internal users and those who have entered the router through VPN. ---

## Response 2
Accessing winbox is done byFIRSTconnecting VIA wireguard to the CHR on digital ocean.Then use winbox on pc, or winbox app on smartphoneFrom there you can reacha. the MT router behind NAT to config the routerb. the subnets behind NAT to access servers.CHR DEVICE:add chain=forward action=accept comment="relay remote peers in-interface=wireguard-interface out-interface=wireguard-interface/ip routeadd dst-address=mt-lan-subnet gateway=wireguard-interface table=main++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++If you want to give access to the server to other peopleand wireguard is not an option( too many users ) then yes you can port forward to your router via the Tunnel.CHRa. forward chain rule to allow port forwardingadd chain=forward action=accept comment="port forwarding" connection-nat-state=dstnatb. DSTNAT rule to push the incoming users to the server via wireguard tunneladd chain=dstnat action=dst-nat dst-address=CHR-static-public-ip dst-port=serverport protocol=??? to-address=MT-Server-IPd. add route so the router knows where to send such traffic.add dst-address=MT-Server-Subnet gateway=wireguard-interface table=maine. add a sourcenat rule on CHR, so that the config at both ends of the tunnel is simplifiedadd chain=srcnat action=masquerade out-interface=wireguard-interfaceMT behind NAT:f. ensure forward chain rule allows wireguard traffic to serveradd chain=forward action=accept comment="PF thru WG" in-interface=wireguard-interface dst-address=server-IP ---

## Response 3
No idea what digital ocean is, so your first statement is meaningless.Is this a server on your LAN, is it a server in the cloud that you control, etc etc..Technically:Why are you port forwarding winbox ports?? Do you not know that winbox is a router service and not a LAn service??Security: Why are you port forwarding winbox ports?? They should only be used from internal users and those who have entered the router through VPN.I have setup a wireguard VPN on CHR and connected my Mikrotik RB over the VPN. (which is behind the NAT)172.16.7.19 is the remote Mikrotik IP (which is behind the NAT)so I want to port forward 172.16.7.19 with 8295 or 8297 port so I can access Mikrotik behind the NAT directly with CHR public IP just by changing the port number.But I also tried it on AWS and Digital Ocean but it is not working.I also open all ports in AWS and Digital Ocean firewall but not working ---

## Response 4
I dont care about AWS or digital ocean, the CHR as you stated on a cloud server simply works. Stick with that. ---