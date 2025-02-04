# Thread Information
Title: Thread-214126
Section: RouterOS
Thread ID: 214126

# Discussion

## Initial Question
Hi Folks, We have two redundant Mikrotik RB5009 routers setup to act as our OVPN servers. We are using TCP port 443 to receive OVPN connections from the staff OVPN client apps.The symptoms on client side during the issue is that they will see server timeout while they cycle through trying our two OVPN server IPs on the two RB5009. On RB5009 side, we observed with packet sniffer that the TCP SYN for the OVPN connection is arriving at the Mikrotik, but not being responded to. This suggests to me that the transit network between client and server is not our issue, and that whatever is happening is on the RB5009, since I do not see it replying with SYN ACK to get through the 3 way handshake.Without any change on either side, maybe after 5-20 minutes, things will start working again, and we will see the TCP 3 way handshake complete and everything works as normal. The packet sniffer is able to see the TCP SYN and TCP SYN ACK and TCP ACK at this point too, without any changes to the filter.My first concern is that I'm dropping the SYN ACK for some reason on my firewall rules. I'm not sure where else to look for my intermittently absent SYN ACKs.
```
/ip firewall filter
add action=fasttrack-connection chain=forward comment=fasttrack \
    connection-state=established,related hw-offload=yes
add action=accept chain=forward comment="Accept established,related" \
    connection-state=established,related
add action=accept chain=forward comment="VPN IPs to rt1" out-interface=\
    ether2.224 src-address=192.168.208.0/20
add action=accept chain=forward comment=\
    "Accept RDP return traffic (Should not be needed)" dst-address=\
    192.168.208.0/20 dst-port=49152-65535 in-interface=ether2.224 protocol=\
    tcp src-port=3389
add action=accept chain=forward comment=\
    "management network devices to the world" in-interface=mgmt \
    out-interface=ether2.224
add action=drop chain=forward comment="deny the rest"
add action=accept chain=input comment="Accept established,related" \
    connection-state=established,related
add action=drop chain=input comment="Drop invalid" connection-state=invalid
add action=accept chain=input comment="Accept ICMP" protocol=icmp
add action=accept chain=input comment="OpenVPN UDP" dst-port=1194 \
    in-interface=ether2.224 protocol=udp
add action=accept chain=input comment="OpenVPN TCP" dst-port=1194 \
    in-interface=ether2.224 protocol=tcp
add action=accept chain=input comment="OpenVPN TCP 443" dst-port=443 \
    in-interface=ether2.224 protocol=tcp
add action=accept chain=input comment=Mgmt src-address-list=RemoteAccess
add action=accept chain=input comment="Accept OSPF" in-interface=ether2.224 \
    protocol=ospf
add action=accept chain=input comment="Accept BGP" dst-port=179 in-interface=\
    ether2.224 protocol=tcp
add action=drop chain=input comment="Default drop"I did enable the OVPN debug in logging as well, but am finding it very difficult to correlate what the output is saying versus my missing TCP SYN ACK. There does not seem to be IP addresses nor usernames shown in the OVPN debug, so I'm not sure what each entry correlates to in terms of my incoming client connections.I'd also assert that authentication and such don't happen until the TCP 3-way handshake completes, right?Could I be reaching a throughput limit on my RB5009 routers? I notice that at the moment my OVPN connections are lopsided, such that vpn1 has 50 connections up, and vpn2 has 80 connections up. Over several disconnects and reconnects, it seems that we time out often on vpn2, and usually wind up on vpn1 - suggesting that maybe vpn2 has reached a threshold limit perhaps and is rejecting the new connections due to capacity?For the time being, I am sidestepping my TCP handshake issue. Thankfully in the 7.17 firmware update Mikrotik added multiple instances of OVPN server to be active, where previously we had been restricted to only one choice of UDP or TCP and port. I'm updating my RB5009 to accept both UDP and TCP now, and so my clients are trying UDP first and not falling prey to this strange TCP handshake trouble I'm observing.

---
```

## Response 1
Are there log messages like "possible SYN flooding on tcp port ...” at the time the connection breaks or before?I have a similar issue, as you know, and figured out, that something is wrong, if there are to "many" (5-10 per second) tcp syn packets from one sourceviewtopic.php?p=1116612#p1116612 ---