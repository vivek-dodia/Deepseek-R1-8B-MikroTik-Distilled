# Thread Information
Title: Thread-1115074
Section: RouterOS
Thread ID: 1115074

# Discussion

## Initial Question
This is one of those questions that has perplexed me for a while now. My home lab network is relatively simple: hAP ax2, two Windows Server 2022 domain controllers, couple of dev servers and my workstation. The router is connecting upstream of a Virgin Media Superhub in modem mode. There are two subnets: 192.168.0/24 for private network and 10.0.0.1/24 for guest network.Importantly, the router is NOT acting as a DHCP server for the 192.168.0.1/24 network. That's handled by the Windows domain controllers which is required for an Active Directory setup linked to DNS servers also running on the DCs. Critically , the router/bridge has a static IP address of 192.168.0.1What's perplexing is that if I look at DHCP on the two domain controllers, I see an entry for ROUTER001. It's not a stale entry - it's been renewed every hour. DHCP lease is set to 2 hours.The question is WHY is the router asking for an DHCP address? AFAIK the router is defined with a static IP address.I'll post the config separately. I discovered this because I tried adding an A record of 192.168.0.1 to the DNS on the DCs and it kept changed to a random DHCP address. ---

## Response 1
I'll post the configuration later. When I did a cut down script, the router didn't register in DHCP so I'm going to do some most investigate myself. ---

## Response 2
... My home lab network is relatively simple: hAP ax2, two Windows Server 2022 domain controllers, couple of dev serversand my workstation.Simple ??Check for DHCP client on that device.Or sniff the network using wireshark to see which devices are sending out request for DHCP leases (and get a response).The MAC address corresponds ? Might already give you an idea too (each interface has a unique MAC (they should have) so that should tell you something). ---

## Response 3
In ROS there could be any number of static addresses assigned to an interface and at the same time DHCP Client could be active for the same interface grabbing dynamic address. Therefore as Halvoetn suggested check/disable DHCP client on hAP. ---

## Response 4
Simple ??Simple in terms of a SOHO running their own Windows Server AD environment. ---

## Response 5
Therefore as Halvoetn suggested check/disable DHCP client on hAP.The DHCP client has to be enabled for the WAN port otherwise no internet connection. I've not had chance to dig deeper into this but I will. ---

## Response 6
The question is WHY is the router asking for an DHCP address? AFAIK the router is defined with a static IP address.First, "you sayas far as I knowthe router is defined with a static IP address".That sounds like your assumption. Why don't you know for sure? Are you not the person that configured the router?Then you ask why is the router asking for a DHCP address? The obvious answer is that you have the DHCP client enabled for the router interface that is connected to the Windows Server.The DHCP client has to be enabled for the WAN port otherwise no internet connection. I've not had chance to dig deeper into this but I will.Now you also say that you will have to dig deeper into why you have no internet access if you disable DHCP client on the WAN port. This is basic network stuff. If your upstream ISP router is giving you a dhcp address, then of course you need dhcp client enabled. Or, if your upstream ISP router allows you to use a static address, you could use that instead.It's just very strange that you have a 2-node Windows Server cluster but yet you are getting confused on dhcp vs static ip addresses. ---

## Response 7
Therefore as Halvoetn suggested check/disable DHCP client on hAP.The DHCP client has to be enabled for the WAN port otherwise no internet connection. I've not had chance to dig deeper into this but I will.I never said to disable ALL DHCP client. Just the unneeded one(s).Look, it doesn't take 5 minutes to make an export. move it from your device and open it in a text editor to see where DHCP client is active.You know which (wrong) DHCP lease is being assigned. Then you know where to start looking.Either you look into it or you don't. Your choice.But posting here while saying you have no time, that's a bit strange ... to me it is. ---

## Response 8
I'm not going to waste everyone's time posting a configuration if I can first reduce it down to bare minimum and still recreate the quirk. As I also said, it's not a critical problem but is certainly unusual. My original reason for posting was if somebody went "Ahh, yes - I've seen something similar. It's because of XYZ". I share our internet with a neighbour so I have to arrange a time to take it down. ---

## Response 9
Please send tosupport@mikrotik.comthe supout.rif file from the router made right after it encounters the problem. ---