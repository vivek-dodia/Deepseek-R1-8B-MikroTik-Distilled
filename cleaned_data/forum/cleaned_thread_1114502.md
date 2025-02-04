# Thread Information
Title: Thread-1114502
Section: RouterOS
Thread ID: 1114502

# Discussion

## Initial Question
Hi Everyone, I'm running an L2TP/IPSec VPN, and see different IP's try to connect in my log.respond new phase 1 (Identity Protection): Mikrotik_IP[500]<=>x.x.x.x[12345]x.x.x.x failed to get valid proposal.x.x.x.x failed to pre-process ph1 packet (side: 1, status 1).x.x.x.x phase1 negotiation failed.I do have a filter rule that add's all IP's to a list connecting to poort 500 and 4500, but the above connection attempt is not added to the list.
```
chain=input action=add-src-to-address-list protocol=udp src-address=!192.168.0.0/24 address-list=test address-list-timeout=0s src-port=500,1701,4500 log=nothe only thing I could think of was to parse the log and search for the error message, but this seems like unnecessary load on the router.How do I add the failed connection attempt IP address to a blocklist without parsing the log every minute?

---
```

## Response 1
Should you not be using dst-port rather than src-port? ---

## Response 2
Also, as IPsec uses UDP, won't the addresslist be filled constantly regardless if the tunnel establishes or not? ---

## Response 3
Also, as IPsec uses UDP, won't the addresslist be filled constantly regardless if the tunnel establishes or not?True, but the tries come from a specific range 1.2.3.x so I can identify it that way.I'm still thinking of another way, without port knocking or parsing... will be continued ---

## Response 4
The source address is not authenticated with UDP. If you add IPs to a block list based solely on a UDP packet, then you risk your network breaking horribly when someone spoofs a bunch of popular IPs such as DNS servers, Google, Facebook, etc. ---

## Response 5
KitMikro, were you able to improve your firewall filter to stop this kind of attacks? I'm also getting them.Thanks and Best Regards, Ricardo ---

## Response 6
KitMikro, were you able to improve your firewall filter to stop this kind of attacks? I'm also getting them.Thanks and Best Regards, RicardoIt seems they connect from a range of Ipaddresses like 1.2.3.X so I've added a rule to drop all connections on UDP ports 500 and 4500 from 1.2.3.0/24Also added a Knock on door rule. It works like this; When you connect on the publicIP on a specific port e.g. 12345. Your IP is added to an address list for 10 seconds. If you connect again on port 54321 within does 10 seconds and your ip is on list 1, you'll be added to list 2. Only list 2 is allowed to connect to ports 500 and 4500. ---

## Response 7
KitMikro, were you able to improve your firewall filter to stop this kind of attacks? I'm also getting them.Thanks and Best Regards, RicardoIt seems they connect from a range of Ipaddresses like 1.2.3.X so I've added a rule to drop all connections on UDP ports 500 and 4500 from 1.2.3.0/24Also added a Knock on door rule. It works like this; When you connect on the publicIP on a specific port e.g. 12345. Your IP is added to an address list for 10 seconds. If you connect again on port 54321 within does 10 seconds and your ip is on list 1, you'll be added to list 2. Only list 2 is allowed to connect to ports 500 and 4500.Many thanks for your answer KitMikro, I will try to apply this type of rule in my Router.Saludos, Ricardo ! ---

## Response 8
KitMikro, were you able to improve your firewall filter to stop this kind of attacks? I'm also getting them.Thanks and Best Regards, RicardoIt seems they connect from a range of Ipaddresses like 1.2.3.X so I've added a rule to drop all connections on UDP ports 500 and 4500 from 1.2.3.0/24Also added a Knock on door rule. It works like this; When you connect on the publicIP on a specific port e.g. 12345. Your IP is added to an address list for 10 seconds. If you connect again on port 54321 within does 10 seconds and your ip is on list 1, you'll be added to list 2. Only list 2 is allowed to connect to ports 500 and 4500.Many thanks for your answer KitMikro, I will try to apply this type of rule in my Router.Saludos, Ricardo !Hey Ricardo, your welcome! If you want to, you can use layer 7 to include some sort of password. If your on a Mac or other Linux based OS you can send a "Knock on door", with the following command
```
echo -n "SOME_TEXT_FOR_LAYER_7" >/dev/udp/YOUR_VPN_IP/YOUR_PORT_NUMBERnotice, I'm sending the request to an UDP port, not TCP.also have a look here;https://wiki.mikrotik.com/wiki/Port_Knocking

---
```

## Response 9
Thank you very much KitMikro, we will try this method that you recommend us! ---

## Response 10
Thanks for the info KitMikro; this works for me too. Below is what I used; handy for those people who don't use ipsec at all:
```
/ip firewall filter add chain=input protocol=udp dst-port=500,4500 in-interface=WAN action=dropPretty blunt code just to drop anything trying to come in on those ports. I can see 9 blocked packets in the last few minutes and no more nasty red ipsec logs

---
```

## Response 11
Here is solution of our problemhttps://github.com/Onoro/Mikrotik ---

## Response 12
I've been annoyed by this very issue for quite a while.Recently I decided to make/ip firewall filter add action=passthrough chain=input protocol=udp dst-port=500 log=yesrule (next to accept established ofc) to investigate.Apparently, those pesky IKE requests come in low packet size, usually below 400 bytes, while valid are 600-1000 bytes.Based on this observation I now take benefit of the following rule:/ip firewall filter add action=drop chain=input protocol=udp dst-port=500 packet-size=0-400 place-before=1Off course, this matching policy isn't 100% efficient, and moreover, may also block valid connections, but it is what it is. ---