# Thread Information
Title: Thread-1113600
Section: RouterOS
Thread ID: 1113600

# Discussion

## Initial Question
Hello.Is there any way to set the DUID of the IPv6 dhcp-client for requesting a prefix. Online.net predefines a DUID, which has to be used by the client...Thanks, Peter ---

## Response 1
Hi Peter, Same problem here.I found this post regarding your question :viewtopic.php?f=2&t=120801&p=593966&hilit=duid#p607902I was running vmware so I could change the interface mac-address and check that the DUID also changed.It didn't solve the problem : I still don't get an IPv6 address.Did you make some progress on this issue ?Thanks, Arnaud ---

## Response 2
Ah - this makes sense (my guess about Comcast in the other thread appears to have been wrong).It's interesting to see how so many different ISPs do so many different things with their IPv6 rollouts. It's going to be nice a few years down the road once the industry settles into standards like it has with IPv4.Hopefully by then Mikrotik will decide which "advanced" features to implement in IPv6 to accommodate the standard, since they don't want to spend any time developing features that don't gain traction in the industry.... like stateful host assignment capabilities in DHCPv6 server or prefix-translation NAT - sure THOSE features will get abandoned the day after Mikrotik decides to implement them. ---

## Response 3
Yeah, and it's quite discouraging to see how long changes like this (which seem to be really minor adjustments) can take to reach the RC…I'm still waiting for what seems to be a simple switch change :viewtopic.php?f=14&t=122446&p=620492#p606682 ---

## Response 4
I know this is an old thread, but i really need to set the DUID of the dhcp client of mikrotik.The use case is when you change the router, the provider changes the prefix it gives you. ---

## Response 5
DUID's were same for two different internet uplinks and cannot be changed. I had two internet connection and as the DUID same, I was not getting address or prefix from the ISP. But now there's an entry "Use Interface DUID" so when I click that, I got two different ipv6 prefixes from verizon. ---