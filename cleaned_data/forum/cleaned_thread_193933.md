# Thread Information
Title: Thread-193933
Section: RouterOS
Thread ID: 193933

# Discussion

## Initial Question
I went to update a RB3011 this morning running 7.5 to 7.7 so I created a backup and completed the upgrade. I don't think I changed anything else. Prior to the upgrade my Wireguard connections were working great. The setup is 4 offices that are all interconnected with Wireguard and by that I mean each office has a connection back to each office. This office and one other have an RB3011 and the other 2 are Ubiquiti. I also have a config for my PC to allow remoting in to each of the offices. The other 3 offices are still connected and working as expected however the upgraded router stopped passing any Wireguard traffic. I can still see packets in the Firewall view on the accept input rule for the Wireguard port so traffic is getting to the router however the Wireguard interface is showing no activity. I tried some other allow rules from other threads even though these are not present in the other office with the RB3011 (RouterOS v7.1).For troubleshooting I have downgraded back to 7.5, restored backup I created, restored another backup from 12/2022 when everything was working, and still no luck. I created an export of the current config and redacted public IPs and keys. Any help or suggestions would be appreciated. This has also been posted to the Mikrotik Reddit.https://pastebin.com/6twbhkpG ---

## Response 1
Hello, a similar thing just happened to me.I have two 7.7 CHR on ESXI as site-to-site VPN. Going great for at least a month. Suddenly one end stopped sending packets to the other (I found out using nmap, vps on the internet, and counting rule in the firewall on both routers). Other direction worked fine (at least fw was counting). I tried cycling both WG interfaces and peers.In WG counters (using keepalive) there were just tx packets. There were no configuration changes on both side for at least 12 hours. The tunnel is in constant usage.I did upgrade to 7.8 on both sides and running fine now. I couldn't tell whether restarting could fix that since colleagues were getting ...intensiveWe are using WG company-wide since Christmas and there was not a single issue yet. ---

## Response 2
I have the same problem, using mikrotik v7.7 suddenly wireguard doesnt work anymore, i tried also upgrade to the latest v7.12.1 it works but then stop working also. it was working when it was 7.1 - 7.5. i even tried re-create wireguard settings and configuration but client cant still connect. ---

## Response 3
Without seeing your config, its merely an opinion based on no evidence!!/export file=anynameyouwish ( minus router serial number, public WANIP information, keys etc.... ) ---

## Response 4
I have just upgraded my router OS version from 7.6 to 7.12.1. My wireguard had stopped working, just like yours. I have found out, that even though the wireguard interface was set to LAN, it did behave as if it was set to WAN. i had to set it to WAN, the set it back to LAN again to make it work. Is this intended behavior? Is this a Bug? Where could i report this? ---

## Response 5
Upgrade to 7.17 and see if the behaviour repeats itself. Im pretty sure they are interested in working on bugs based on the latest firmware, as any previous bugs may have been taken care of already. ---

## Response 6
okay, i did the upgrade to 7.17, and now it's completely broken. The same trick wont fix it. My router is hap ax³ , i have a wireguard on a port said port is open to accept udp inputs in the firewall, and the wireguard is set to LAN in the interface list. I can connect to the wireguard interface from the outside, the connection is established, and i see the endpoint address from the router. I have both rx and tx data on the router in the size of 2kb. on the client side, i see2 kb rx and 60kb of tx data. So i suspect it is a routing problem again. this have worked just fine yesterday, and with no problem for 2 months before the upgrade. Internal address space is set up to 10.3.3.0 and 10.3.3.1/24 for the router, and 10.3.3.10/24 is configured for the client on both sides. Allowed address is 10.3.3.10/24 on the server side and 0.0.0.0/0 on the client side. What else can i try besides the interface being in LAN? how could i create a diagnostic file to upload here? i'm sorry i'm only using mikrotik for a few months at home so i'm not really well versed in all the features. ---

## Response 7
Like this:/export file=anynameyouwish ( minus router serial number, public WANIP information, keys etc.... )Move file to PC and then post back here between code quotes. ---

## Response 8
Interesting, disabling the peer in the peer-list and then re-enabling it fixed the problem and now everything is working again. weird behavior. should i still export everything and upload for the sake of debugging?maybe this is related to me being connected to wireguard and updating from the client connected to wireguard trough the web interface? ---

## Response 9
Or just a matter of not waiting long enough ? ---

## Response 10
it could be. altough i have waited 14+ hours. anyway, now it's solved, i hope if someone runs into the same thing later this trhead will be useful for them. thanks for the assistance. ---