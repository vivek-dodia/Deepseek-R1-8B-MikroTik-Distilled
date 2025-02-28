# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 209192

# Discussion

## Initial Question
Author: Thu Jul 11, 2024 9:59 am
Hi everyone, I'm quite new to the mikrotik devices and trying to configure a ptp link using w60g devices. I have to deploy the devices on a live network and I have failed once with my config and cannot afford to have any issue with my config.I want my AP bridge to receive an IP from vlan 2003 and station bridge to receive an IP from vlan 2004 via a dhcp client. The switch to which AP bridge w60g is connected is configured with both the vlans. Below is my config which I think will work according to my requirements. I would be grateful if anyone from the experts could confirm this config.AP Bridge Proposed config:1- Wireless mode (AP Bridge, configured SSID and Pass, isolate stations checked, put stations in the bridge enabled)2- Created a bridge and added ether1, wlan3- Created vlan 2003 and put on the bridge4- In the bridge vlan section, created data vlan 12, 13 and tagged on ether1, bridge, wlan, wlan-station5- In the bridge vlan section, created vlan 2004 and tagged on ether1, bridge, wlan, wlan-station6- In the bridge vlan section, created vlan 2003 and tagged on ether1, bridge7- Enabled vlan filtering8- Configured dhcp-client for vlan 2003Station Bridge Proposed config:1- Wireless mode (Station Bridge, configured SSID and Pass)2- Created a bridge and added ether1, wlan3- In the bridge vlan section, created data vlan 12, 13 and tagged on ether1, bridge, wlan4- In the bridge vlan section, created vlan 2004 and tagged on ether1, bridge, wlan5- Enabled vlan filtering6- Configured dhcp-client for vlan 2004 ---

## Response 1
Author: Sat Jul 13, 2024 3:50 pm
The wAP 60Gs... don't need to know about your VLAN tags. ---

## Response 2
Author: Tue Jul 23, 2024 3:37 pm
Sorry for the late reply, and can you please tell me if there's anything that I need to change in the mentioned configuration to achieve the desired results ?This config is an updated one and not the one with which I had issues at first. ---

## Response 3
Author: Thu Jul 25, 2024 7:07 am
The WAP 60 doesn't need to know about your VLAN Tags. ---

## Response 4
Author: Thu Jul 25, 2024 12:17 pm
I don't understand the reasons why you need to fiddle with VLANs on the PTP link devices, it seems to me like you are using the PtP as a "wireless wire" connection (as Mikrotik would call it) between two networks that already have devices capable of managing the VLANs (and surely much more computing power than a WAP60).To hopefully clarify the basic concepts of the wireless wire, you have to imagine the couple of devices as if they were a (unmanaged) switch (actually two).Simplified example, skip it if it is too basic:Let's say that you have two devices/networks, A and B, with ethernet ports physically separated by 9 meters distance and connected by a 10 m ethernet cable.The cable is accidentally cut, and you have to re-establish connection.But you only have handy 2 x 5m ethernet cables.You get a spare, el-cheapo 8 port switch and put it in the middle, it will know nothing of VLANs or IP addresses, it will simply (like a longer ethernet cable) pass data from A to B and viceversa.Now imagine that you have instead 2 x 0.50 m and 1 x 8 m cable, but - luckily enough - you have two spare el-cheapo 5 port switches, you can connect them to the existing networks with the two short cables and connect between them with the 8 m cable, again the switches will know nothing about VLANs or anything.And now imagine that you have only the 2 x 0.50 m cables but happen to have handy two WAP60G's (and clear line of sight).The W60G's - just like the unmanaged switches - will simply connect A with B.In theory, they don't even need - just like the unmanaged switches - an own IP over the one or the other network (you can still connect to them via Winbox by their MAC for management). ---

## Response 5
Author: Tue Jul 30, 2024 12:43 pm
Thank you for such a detailed reply. Actually the only reason why I'm persisting with the vlans is to manage the ptp devices remotely. We have a dhcp server configured for our vlans on the network. We're a WISP company so we want to manage both of our devices remotely via an IP which it will receive through a dhcp server. ---

## Response 6
Author: [SOLVED]Tue Jul 30, 2024 5:49 pm
Unless you want to keep specific VLANs from going through the link, don't mess with bridge VLAN filtering and don't add them to the bridge VLAN table.For just two radios in a PTP config, it's simply enough to create a VLAN interface (attached to the radio's bridge) with the VLAN tag (2003 or 2004) you want that radio to use. Set up a DHCP client on that VLAN interface and it will pull an IP from the upstream DHCP server. I also make a backup VLAN interface tagged to ether1 so I can get into it on a known IP on that "hidden" VLAN.I have roughly 100 wAP 60's, Cubes, LHG60's doing this. Most of the AP's are simply bridging everything, and the CPE do the VLAN tagging on the customer-facing ethernet port.(In some cases, I do want the radios to block some VLANs from traversing them, so I enable bridge VLAN filtering and add only the VLANs I want to allow through that portion of the network. But it gets complicated to have to keep doing that down the line, especially if I need to add a new VLAN.) ---

## Response 7
Author: Wed Jul 31, 2024 9:02 am
Thank you, got your point. What I have done is that although I have enabled bridge vlan filtering but I have tagged all the vlans that would be used by CPE in that region and also few management vlans.What I have understood from your point is that I should create vlan 2003, 2004 on bridge interface on the "Master" and "Slave" end and make the wireless interfaces part of the bridge on both the devices and create dhcp client for the respective vlans. This would also let the traffic of other vlans pass through them such as customers vlans traffic to pass through the PtP link. Correct ? ---

## Response 8
Author: Thu Aug 15, 2024 6:05 am
Thank you, got your point. What I have done is that although I have enabled bridge vlan filtering but I have tagged all the vlans that would be used by CPE in that region and also few management vlans.What I have understood from your point is that I should create vlan 2003, 2004 on bridge interface on the "Master" and "Slave" end and make the wireless interfaces part of the bridge on both the devices and create dhcp client for the respective vlans. This would also let the traffic of other vlans pass through them such as customers vlans traffic to pass through the PtP link. Correct ?That sounds about right. Did you give it a try and did it work for you? ---

## Response 9
Author: Thu Aug 15, 2024 8:40 am
Yes, Thank you so much. It did work and you helped me cleared my concepts as well. ---

## Response 10
Author: Thu Aug 15, 2024 9:23 am
Sorry for diverting the topic and raising another query in the current thread. But I would be grateful if anyone from the experts could help me resolve my issue.I am facing very strange loop message in one of mikrotik devices although I have checked STP config thoroughly and there should be no loops since config is correct also no chance on physical layer as well.Device: Mikrotik v6.48.1 CRS 112-8P-4S (mipsbe)Logs:ether5: bridge port received packet with own address as source address (cc:2dx:1c:x), probably loopether1: bridge port received packet with own address as source address (cc:2dx:1c:x), probably loopAirfiber 5X and Cambium antennas are connected to these interfaces and I am not sure why I am facing this error. The MAC it is showing is of the bridge interface. I have tried checking on forum but didn't get the answer which could resolve my query.