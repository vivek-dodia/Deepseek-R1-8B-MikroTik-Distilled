# Thread Information
Title: Thread-213269
Section: RouterOS
Thread ID: 213269

# Discussion

## Initial Question
Hello everyone, I'm currently facing an issue with my CCR2216 when using a full BGP routing table. The device starts to lose packets, and the CPU usage spikes to 95%. I need a solution capable of handling approximately 100 Gbps of traffic.Here are the options I've considered so far:1. Install Mikrotik CHR on a PROXMOX server with an Intel Xeon CPU E5-2699C v4 (88 cores) that I already own.2. Install Mikrotik ISO on an Ampere Altra Q80-30 server (which I would need to purchase).I'm open to exploring other solutions as well. Your advice and recommendations would be greatly appreciated.Thanks in advance! ---

## Response 1
Probably your setup, the router is spec'd at handling up to approx 180Gbps of traffic with filter rules. ---

## Response 2
1. Install Mikrotik CHR on a PROXMOX server with an Intel Xeon CPU E5-2699C v4 (88 cores) that I already own.I'm open to exploring other solutions as well. Your advice and recommendations would be greatly appreciated.Thanks in advance!That CPU is 22 core, dont confuse cores with threads.I suggest you for your kind of setup, a Juniper MX204 (that I have for sale brand new boxed)Unfortunately your post doesnt have any conf so we cannot see where issues are on the conf... we are not wizards!the 2216 should do that traffic in the right scenario. ---

## Response 3
That CPU is 22 ore, dont confuse cores with thread.I suggest you for your kind of setup, a Juniper MX204 (that I have for sale brand new boxed)Unfortunately your post doesnt have any conf so we cannot see where issues are on the conf... we are not wizards!the 2216 should do that traffic in the right scenario.Thank you, please PM to discuss about Juniper MX204. ---

## Response 4
HelloMy mail is admin at spadhausen dot comI dont know how PM here works. ---

## Response 5
I dont know how PM here works.It doesn't. ---

## Response 6
Any other sugestion? ---

## Response 7
Any other sugestion?Your question is missing important detail:How many upstream peers?How many downstream peers (if any)?Do youneedfull BGP tables?Are you using L3HW offload, and if so, is the router configured properly to support hardware offload?What does the profiler say is pegging your CPU? ---

## Response 8
hi, Three upstream and downstream peers, I need full BGP tables, I have enabled L3HW offload.Currently without full BGP tables the CPU is at 60% at peak tiemes, of course I have no firewall rules, no nat, just BGP. A couple of bonding and some VLANs ---

## Response 9
Are you using the single-bridge configuration to benefit from l3-hw?can you post your config? ---

## Response 10
I have no bridge.Should I create a bridge with all physical ports or bonds that I am using and set up properly in VLAN tab of the bridge? ---

## Response 11
Absolutely yes! You should do a single bridge and put VLAN there, otherwhise they are via CPU!Attaching the VLAN to the phisical port is an old-way procedure that has been replaced by the single bridge!https://help.mikrotik.com/docs/spaces/R ... p+features ---

## Response 12
I have no bridge.Should I create a bridge with all physical ports or bonds that I am using and set up properly in VLAN tab of the bridge?Double yes. ---

## Response 13
Absolutely yes! You should do a single bridge and put VLAN there, otherwhise they are via CPU!Attaching the VLAN to the phisical port is an old-way procedure that has been replaced by the single bridge!https://help.mikrotik.com/docs/spaces/R ... p+featuresEither I'm reading help page incorrectly but It didn't occur to me that all interface that you want to use L3HW offloading has to be done via bridge... I'm not sure it's clear enough in documentation. The L3HW offloading is under the bridge and switching section though.So we can't just have 2 or more ports that are part of any bridge to be routed and take advantage of L3HW? Why do I still see the H on my routes then... ---

## Response 14
the main objective using single bridge is to use bridge vlan filteringhttps://help.mikrotik.com/docs/spaces/R ... NFiltering ---

## Response 15
the main objective using single bridge is to use bridge vlan filteringhttps://help.mikrotik.com/docs/spaces/R ... NFilteringYes agreed but in my case particularly I don't need vlansExample:Ether1 is isp with public ip and bgpEther2...10 is internal network with public ip from own as number....No vlans, no bridge, no dhcp, no firewall, no nat, no connection tracking, just routing packets from ether1 to ether2 and back as example. ---

## Response 16
No vlans, no bridgethen you won't have L3 hardware offload acceleration, which is the key feature of ccr2216even if you dont use vlans (or tag vlans), you can implement/convert your scheme to using bridge vlan filtering ---

## Response 17
Then why use RouterOS / CCR-box ? do this on native Linux ?Get yourself some 25/40/100Gbps NIC's and perform some tuning.https://fasterdata.es.net/host-tuning/l ... 0g-tuning/ ---

## Response 18
No vlans, no bridgethen you won't have L3 hardware offload acceleration, which is the key feature of ccr2216even if you dont use vlans (or tag vlans), you can implement/convert your scheme to using bridge vlan filteringYes I understand that now but It wasn't perfectly clear to me that L3HW is directly linked to working off bridge.I can convert the configuration very easy to use the bridge setup but I didn't know was full requirement.Thank you for clearing this up for me. ---

## Response 19
Then why use RouterOS / CCR-box ? do this on native Linux ?Get yourself some 25/40/100Gbps NIC's and perform some tuning.https://fasterdata.es.net/host-tuning/l ... 0g-tuning/The setup I gave was an example, not specifically my setup. ---

## Response 20
This doc specifically explains many key concepts about L3HW:https://help.mikrotik.com/docs/spaces/ ... OffloadingThe dependency on L2HW (https://help.mikrotik.com/docs/spaces/ ... Dependency), some basic config and typical errors. ---

## Response 21
L3HW should work if you don't have any VLANs, and simply assign IP's to each port.It is "best practices" to put everything in the bridge, build VLANs on the bridge, tag those VLANs to the bridge ports, create VLAN interfaces on the bridge, and assign IP's to the bridge VLAN interfaces instead of directly on physical interfaces. This gives you flexibility down the road.Any time you create new VLAN interfaces, you have to synchronize those changes with the ASIC by disabling/enabling L3HW offload on the Switch. ---

## Response 22
L3HW should work if you don't have any VLANs, and simply assign IP's to each port.It is "best practices" to put everything in the bridge, build VLANs on the bridge, tag those VLANs to the bridge ports, create VLAN interfaces on the bridge, and assign IP's to the bridge VLAN interfaces instead of directly on physical interfaces. This gives you flexibility down the road.Any time you create new VLAN interfaces, you have to synchronize those changes with the ASIC by disabling/enabling L3HW offload on the Switch.Ok this is a much better answer and explains why I still have L3HW working (on some of my devices) so yes it will work but advised to use bridge for best practices and flexability.Right now "most" of other devices I cant use L3HW due to VRF's I'm waiting for L3HW with VRF support. ---