# Thread Information
Title: Thread-189584
Section: RouterOS
Thread ID: 189584

# Discussion

## Initial Question
Hi, I am quite new with Mikrotik products. I've setup a L2TP server to provide remote access to iphone, laptop ... Everything works fine except in one specific situation.I am able to use my remote device without any issue, but if I launched a speedtest on the iPhone, after several seconds the connection is frozen : througput is down, browsing is broken.During the speedtest, I am able to ping remote host, but after several seconds there is a timeout, and active connection in PPP->Active Connections disappears.Any idea ?Thanks a lot. ---

## Response 1
HiI'm faceing the same issue. VPN-Tunnel from iPhone to MT works fine over L2TP. "Normal" traffic flow's as well into both directions (e.g. browsing, email, fileshare).By doing a speedtest on the iphone it comes to this issue. The download works fine. But as soon as the upload (from iPhone to MT) starts and works for 1-2 seconds, then it crushes.No traffic anymore. Only solution then is to stop the VPN-connection on the iPhone and start it new. It looks like the VPN-Tunnel stucks somwhere itselfs.Does anybody has an idea where to search for the root cause?BR ---

## Response 2
Iphones are embarrassed by speed tests??Just don't do speed tests and be happy.I tried it on my iphone, cellular connection to my Home router via WIREGUARD and it worked fine, no cutout at all.77 down 15 up were my speeds..............Sounds like you are using the wrong VPN type. ---

## Response 3
After update Router OS from 7.8 to 7.9, as well the site-to-site VPN iKE stops working well. The tunnel was up, but almost no speed trough the tunnel was possible. An invastigation by support was not succesfully.The solution was found on the following thread, thx a lot!https://saputra.org/threads/mikrotik-fa ... -ipsec.34/(Copy from original thread:)Fasttrack is a new feature introduced in RouterOS v6.29 that allows you to forward packages in a way that they are not handled by the Linux Kernel which greatly improves the throughput of your router as well as lowering the CPU load.Fasttrack allows all packages that have the state Established or Related to bypass the Kernel and be directly forwarded to the target. So, once a connection is marked as established or related, it won’t go through any firewalling or processing and will directly forwarded to the target. Of course – a connection gains the state of established or related once it went through the firewall so it will still be secure.But there’s a known issue that Fasttrack will not work with IPsec connections, it will result in a rather wonky experience or very unstable IPsec connection. So if you have IPsec connections in your MikroTik but want to take the advantages of Fasttrack, here’s the resolution for you! ---

## Response 4
Swiss MT, that is already covered by the default rules in the forward chain.We accept ipsec traffic prior to the fastrack rule!! Done!add action=accept chain=forward comment="defconf: accept in ipsec policy" \ipsec-policy=in, ipsecadd action=accept chain=forward comment="defconf: accept out ipsec policy" \ipsec-policy=out, ipsecadd action=fasttrack-connectionchain=forward comment="defconf: fasttrack" \connection-mark=no-mark connection-state=established, related hw-offload=\yes ---

## Response 5
I've integrated the fasttrack bypass into my configuration, but I’m encountering some issues (not sure if they’re related). Occasionally, the IPsec peers' PH2 state gets stuck at 'ready to send', which seems to cause upload problems for VPN clients. This doesn't happen all the time, but I’ve been able to (inconsistently) replicate the issue using the vpn_public and vpn_mgmt profiles.I see that Sebgva reported issues with high-bandwidth uploads during speed tests over VPN connections, which led to throughput dropping to zero and eventually the connection disconnecting.I strongly believe there’s a connection between the PH2 status being ‘established’ and successfully completing a speed test. When the PH2 state remains 'ready to send', that's when the upload issue occurs.Config.txt ---

## Response 6
Hi, I'm experiencing the same thing but my RouterOs is CHR version so no Fast track.Every time I try to do a Speedtest from remote client the VPN tunnel goes down. ---

## Response 7
You are choking the tunnel, that's why.There is nothing left for anything else.Do speedtest with limit on bandwidth, leave at least 5% over for management connection ( too much but to be safe).Then test again. ---

## Response 8
I've used other tunneling software and never I suffered of that issue ---

## Response 9
I've integrated the fasttrack bypass into my configuration, but I’m encountering some issues (not sure if they’re related).Config.txtFor traffic to work properly, it is good practice to first specify Input traffic in firewall rules and only then Forward, rather than mixing everything. The order of firewall rules is important because they are executed from top to bottom.INPUT CHAIN ​​--> To the Router or to Router Services. Directional flow is WAN to Router, and LAN to Router.FORWARD CHAIN ​​--> Through the Router. Directional flow is LAN to LAN, LAN to WAN, WAN to LAN.OUTPUT CHAIN ​​--> From the Router. Directional flow is Router to WAN.Allowing the dns53 port to the outside world in the firewall is a very bad idea. We only grant permission to local LAN.I will copy an example for you that you can safely use and add the entries you need.
```
/ip firewall filteraddaction=accept chain=input connection-state=established,related,untrackedaddaction=drop chain=input connection-state=invalidaddaction=accept chain=input protocol=icmpaddaction=accept chain=input dst-address=127.0.0.1addaction=accept chain=input comment="WG handshake"dst-port=13232protocol=udpaddaction=accept chain=input comment="admin access"in-interface-list=LAN src-address-list=Authorizedaddaction=accept chain=input comment="users services"in-interface-list=LAN dst-port=53protocol=udpaddaction=accept chain=input comment="users services"in-interface-list=LAN dst-port=53protocol=tcpaddaction=accept chain=input comment=L2TP dst-port=500,1701,4500\in-interface-list=WAN protocol=udpaddaction=accept chain=input comment="IKE IPSec"in-interface-list=WAN \
    protocol=ipsec-espaddaction=drop chain=input comment="drop all else"addaction=accept chain=forward comment="defconf: accept in ipsec policy"\
ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward connection-state=established,related disabled=nohw-offload=yes connection-mark=no-markaddaction=accept chain=forward connection-state=established,related,untrackedaddaction=drop chain=forward connection-state=invalidaddaction=accept chain=forward comment="internet traffic"in-interface-list=LANout-interface-list=WANaddaction=accept chain=forward comment="Wg to LAN"in-interface=wireguard1 dst-address=192.168.88.0/24addaction=accept chain=forward comment="port forwarding"connection-nat-state=dstnat disabled=yes{enableorremoveasrequired}addaction=drop chain=forward comment="drop all else"

---
```

## Response 10
The download works fine. But as soon as the upload (from iPhone to MT) starts and works for 1-2 seconds, then it crushes.After two years it is strange to hear the same issue ... is it possible Mikrotik people give us an official reply on this issue ? ---