# Thread Information
Title: Thread-1116482
Section: RouterOS
Thread ID: 1116482

# Discussion

## Initial Question
I currently use a MikroTik hEX Refresh router and have run out of Ethernet ports for managing my network. My setup includes three WAN connections on Ether1-Ether3, and I need to expand to support five separate LAN subnets.I’m exploring options for expanding my Ethernet ports while maintaining control over the following functionalities:The ability to assign a specific Ethernet port to a particular LAN subnet and route its gateway through one of the available WAN connections.The flexibility to bridge Ethernet ports as needed to adapt to configuration changes.Given these requirements, would a switch or a router be more suitable for my needs?I’m considering the RB260GS and CRS106-1C-5S as potential options. My goal is to implement a budget-friendly solution for my homelab, allowing me to isolate devices to their own WAN connections and subnets.Any guidance on the best approach or recommendations for suitable devices would be greatly appreciated. ---

## Response 1
Sounds like you need a switch. Your thought to use a RB260GS (also known as a CSS106-5G-1S) is a fine suggestion - I have several of them. They will give you five Gig-E ports plus an SFP if you need one more port. SwitchOS is quite different from RouterOS, but once you get the hang of it, it's fairly easy - including VLANs. For what you are trying to do, I would assign one port on your router as a VLAN trunk to the switch and then let the switch break out the VLANs. Note that with what you said your needs are, you would completely fill the available ports on both the router and switch - unless you use the SFP on the switch. I am doing that on one of mine with a 1G copper SFP that I had laying around. ---

## Response 2
I would get another hex as I dont really like the 260GS, the other option seems very cagey....... ---

## Response 3
To the CRS106-1C-5S you would need to add the SFP modules, and besides budget considerations (5 modules at 25-30 US$ each are 125-150$), copper modules on a passively cooled device are not a good idea for the heat management.For that kind of money you could get a "real" 24 port switch:https://mikrotik.com/product/crs326_24g_2s_inThe RB260GS is SwOS only, so it is less flexible than Ros, but it is so cheap that I don't think you can find any other managed switch for that kind of money.Still it isn't a router.At the end of the day for your use case another hex refresh might be the best solution, though 3WAN+5LAN should mean 8 ports, and 5-1+5-1=8 so you will be using all ports.So maybe you could consider a L009, which should be on par to the hex refresh for both routing and bridging but has 3 ports more (but it costs double the hex refresh). ---

## Response 4
I would go with L009 in stead of hex refresh.A bit more future safe.But every time you add a device, you loose 2 ports on the complete setup for trunk. So better get a bit more ports from the beginning.So why not CSS318 ? A bit more expensive then L009, 16 ether ports, 2 SFP+ for future expansion. SWOS only ( but for a switch that's no problem). ---

## Response 5
So why not CSS318?I thought of that one too. I wish it had come out a month earlier. would have been perfect for a task I have. Ended up with a CSS326 - which I have several of already. ---

## Response 6
I was sticking as close as possible to the budget margin of the OP! ---