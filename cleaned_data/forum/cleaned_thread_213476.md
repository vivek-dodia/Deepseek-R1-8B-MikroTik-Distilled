# Thread Information
Title: Thread-213476
Section: RouterOS
Thread ID: 213476

# Discussion

## Initial Question
So, is there some possibility if I have a 1000 routers in my vpn network to somehow access it to troubleshoot if there is no internet connection.I never used rommon, but dont sure if thats some possibility through vpn ---

## Response 1
If there's a chain of accessibility (i.e. you can access R1 but cant access R2 directly, while R1 can access R2), then you can use CLI (ssh, MAC telnet, normal telnet) if any of these is allowed on R2. ROS includes clients for all mentioned protocols. The only issue is with MAC telnet, ancient versions (something like 6.42 and older) are incompatible with recent ones. ---

## Response 2
Just wondering ... how does that VPN work then without internet connectivity ? ---

## Response 3
Just wondering ... how does that VPN work then without internet connectivity ?Maybe VPN as in Various People Near the routers? ---

## Response 4
I didnt say that vpn works. I only said that i have 1000 routers on VPN and f something broke and need to fix maybe with routes, etc, and try to find a way to solve it. ---

## Response 5
Again, and do you plan to do that when there is no internet connection ?A backup connection is the only solution then.But I think I get what you mean... you are referring to "simple" config issues which break the connection ?What I do for the client sites I control ("only" 40 or soabout 90 MT devices in total):- most are connected via MPLS from ISP, up til now rather stable. That MPLS is also connected to Azure (client application)- for those sites which are not connected via MPLS, I use wireguard to a central RB5009 (and parallel IPSEC to Azure, for client applications)- on top of that MPLS/Wireguard I put an EOIP tunnel, not connected to bridge, all to that central point where I have RB5009 in a rack with UPS etc.- that RB5009 is reachable via Wireguard, Zerotier and (when connected to client Azure environment) via Azure.- because of that EOIP, it allows me to use ROMON (from wherever I am when connecting to the RB5009) for ALL MT devices (and where a stupid switch blocked me, I applied another EOIP for that specific segment towards central point)Also, especially for remote sites, SAFE MODE in Winbox is your friend.Use safe mode, make the change, when things still work after some minutes, disable safe mode which will apply config for real.Don't rush your changes. Safe mode, change, wait, verify it works, disable safe mode.Repeat when needed.If things break, safe mode will make sure to revert to situation right before the changes you made. ---

## Response 6
I didnt say that vpn works. I only said that i have 1000 routers on VPN and f something broke and need to fix maybe with routes, etc, and try to find a way to solve it.The usual approach for this is to have a kind of a "first aid kit" consisting of a LTE router or a combination of a WiFi router and mobile phone that you can "mail" to the site and let the local coworkers, even non-IT ones, connect it to the router that needs help. The first aid kit router then connects to your VPN using the mobile network and you can find out what is wrong with the main one. mac-telnet and romon are of great help if the IP configuration got broken really severely, provided that at least one of these two has been set up properly in advance. ---