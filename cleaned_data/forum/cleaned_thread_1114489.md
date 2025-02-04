# Thread Information
Title: Thread-1114489
Section: RouterOS
Thread ID: 1114489

# Discussion

## Initial Question
I have two sites connected by two Mikrotiks through an IP tunnel over IPsec.In Site1, I have several LANs that can successfully communicate with LAN1 in Site2.Now I need the LANs in Site1 to connect to the remote IPsec sites of Site2 (Azure, GCP, Branch1, Branch2).How can I achieve this?Could I use some kind of NAT?the red line indicates the remote network I want to reach.I am attaching an image with the network design. ---

## Response 1
on site 1 router you nead add ipsec policy witch dst net of azure and the reverse to site 2nat it is not necessary if you set correct routing in azure ---

## Response 2
Thank you very much for your response.That is the logical solution, but I cannot implement it because I don't control Azure, GCP, or the other offices, so I have to use the output already established by Site2.Could I use a NAT at Site2 so that when something destined for Azure comes in, it changes the address to the LAN used to connect to Azure? ---

## Response 3
ensures 1<-->2 site connection via ipsec witch azure networks policies, and then use NAT on router site2 like:EXAMPLE-1/ip routeadd dst-address=10.10.10.0/24 (network azure) gateway=1.1.1.1 (ISP GW) pref-src=192.168.1.1 (LAN mikrotik ip/site2) routing-table=main/ip firewall natadd action=masquerade chain=srcnat dst-address=10.10.10.0/24 (network azure) out-interface=e1_WAN (ISP GW lnk) src-address=192.168.2.0/24 (LAN net site1)EXAMPLE-2 / do +/- the same/ip firewall natadd action=src-nat chain=srcnat dst-address=10.10.10.0/24 (network azure) out-interface=e1_WAN (ISP GW lnk) src-address=192.168.2.0/24 (LAN net site1) to-addresses=192.168.1.1 (LAN mikrotik ip/site2) ---