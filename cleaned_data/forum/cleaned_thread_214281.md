# Thread Information
Title: Thread-214281
Section: RouterOS
Thread ID: 214281

# Discussion

## Initial Question
strange behaviorthere is a hap ac3 router routeros 7.16.2 with ether1 on it vlan on which macvlan and then ppoe-client to the providermtu 1508 is installed on the ether vlan and macvlan so that on the ppoe interface it turns out 1500, main connection connects and works, then there is an ip-tunnel with ipsec on ppoe interface also connects and work ok with mtu 1438ping with packets of size 2000 and 5000 works fine inside the ip-tunnelbut the following problem occurs, sites do not open via ip-tunnel, but when I launch the sniffer to see what’s happening it starts working, when I turn off the sniffer it stops working againwhat to do? ---

## Response 1
From the information provided, I can only guess that you have a FastTrack rule on your IPv4 firewall filter table that is incompatible with your IP tunnel.I say that because the Packet Sniffer disables FastPath while running (thus, disables FastTrack too) and that could be the reason your IP tunnel works fine while the Packet Sniffer is running.So, in case you have a FastTrack rule enabled, check if the problem is "solved" by disabling it. ---

## Response 2
[solved] yes I had a fasttrack rule with hw. offloadand when I turned it off, the traffic started flowingthank you very much ---