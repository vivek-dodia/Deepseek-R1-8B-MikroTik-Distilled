# Thread Information
Title: Thread-1120529
Section: RouterOS
Thread ID: 1120529

# Discussion

## Initial Question
i have upgraded a few days ago some switches to RouterOS v7.16 and now the system log and the bridge hosts / FDB table is filling up and overflowing…. i have seen one of the switches crashing when it went above 60000 (60 THOUSAND) Hosts in the Bridge->Hosts table as displayed by WinBox… even if in the log it keeps saying "bridge1: maximum host entry limit reached (8192)"it seems v7.16 is dumping random MACs (multicast?) in the same hosts table as regular ones - i even turned IGMP Snooping off and it keeps doing this.affected on the network:CRS354-48G-4S+2Q+ switches - upgraded 2 of them to 7.16 … when i turned off IGMP snooping, one of them keeps showing the host entry limit message in the log. The one upstream of it has mostly stopped showing the warning when i turned off IGMP snooping.. but it still shows it now and then (a few times every hour)CRS112-8P-4S - shows the hosts entry limit message (every few minutes) - currently has about 28300 (28 thousand!) entries in the Bridge Hosts list and about 1000 in the Switch → FDBs listRBSXTsq5nD (in wireless bridge mode) - shows about 5000 (5 thousand) entries in the Bridge Host listOur arpwatch server has only recorded a total of 576 different pairs of ip to MAC addresses, collected since yesterday around noon when i reset its statistics.(also please note that some hosts have multiple ip addresses on the same MAC address)it is impossible to have so many (tens of thousands) different MAC addresses on our network… this is definitely a bug in RouterOS - our network is heavily used for IPTV / CCTV cameras (a few hundred of them), some (quite a few) of the cameras and/or recording servers themselves even have multicast enabled.... and i think ROS v7.16 is messed up by the multiple IPTV video streamsAlso, before the upgrade there was no message about "excessive or late collision, link duplex mismatch?"... but now with v7.16 it pops random messages about this in the log of CRS354-48G-4S+2Q+ switches.(forum note: i have tried to post this as a reply on the big v7.16 thread in the announcements but since i did not have a forum account before i had to create one - and new users are not allowed to post replies / bug reports to release announcements)Note: i have also opened a support ticket with relevant supout / autosuport files - SUP-166998while i was preparing the forum post here i watched it crash again… the hosts table grew to more than 66.000 items (i.e. it blew past 65535)… i looked away to another monitor… and saw in the corner of my eye the WinBox window return to the connect screen… when it came back i had a red crash message in the log. and an autosupout.rif waiting in the list of files - i have attached that to the support ticket also. (kernel failure in previous boot, out of memory condition was detected) ---

## Response 1
update:i have downgraded the affected CRS354-48G-4S+2Q+ switches back to 7.15.3 .. they work OK again now.Also downgraded the two CRS112-8P-4S switches from 7.16 to 7.15.3 - they work OK now tooi also have upgraded a few CRS326-24G-2S+ switches to RouterOS v7.16 - these do not seem affected by the random MAC junk... probably because they have ARM chips. (and use the ARM build of RouterOS).Our affected devices seem to be all MIPSBE based. ---

## Response 2
it seems v7.16 is dumping random MACs (multicast?) in the same hosts table as regular ones - i even turned IGMP Snooping off and it keeps doing this.Multicast MACs should start with01:xx ... would be interesting if you sorted host list in ascending MAC address order... ---

## Response 3
tested on 26 pcs of crs354 and I cannot reproduce this error ---

## Response 4
Multicast MACs should start with01:xx ... would be interesting if you sorted host list in ascending MAC address order...i have looked through the supout.rif files that contain snapshots of the mac address tables from that day ... there are barely a handfull of them that start with 01:xx, the majority seems random data... even the 00:00:00:00:00:00 one (in the screenshot below) seems random junk.here is another screenshot that i made that day with them sorted in ascending order...notes:- the screenshot was made before i reconfigured the backup link port, thinking that maybe that secondary/backup link bridge was the cause (but that was not the cause)- the 00:07:5F mac addresses are legit, we have many BOSCH IPTV cameras too..crs354-almost-30k-MACs-and-increasing - REDACTED.png....tested on 26 pcs of crs354 and I cannot reproduce this errorwe have a pair of XS+27LC15D / XS+33LC15D SFP+ modules between these CRS354-48G-4S+2Q+ switches but instead of the nominal 10G link speed we run them at just 1G link speed so probably that is also a factor in this random data...?We keep the link at just 1G until we can re-arrange the fiber layout - the fiber distance is about 6-7 kilometers, there is an intermediate fiber patch panel located in a building very close to a busy intersection where heavy tonnage road vehicles cross over rails.. the random vibrations from the intersection affect a bit the link stability at 10G but are not noticeable at 1G.. our best guess so far is that the SC fiber connector(s) in that patch panel are the cause of the tiny link dropouts at 10G... but for any changes in that panel we need a ton of paperwork and approvals) ---

## Response 5
HelloI'm seeing this same behavior on ours 4x CRS354-48G-4S+2Q+Bridge > Hosts is weird. We see like 1000 hosts a second later is 6000, several times reaching 8000, then go back to 1000, this in just a few seconds.In logs I also see the same "maximum host entry limit reached".Not sure if this is related with fiber modules. I'm using the native qsfpplus ports to connect between switchs with the mikrotik qsfpplus cables.Thank you ---

## Response 6
HelloJust to add more information.I also had to downgrade to v7.16 to keep things working.Even without seeing the Bridge > Hosts weird behavior there was a huge performance impact. I have 4x CRS354-48G-4S+2Q+ and seeing 50mbps bandwidth transferring a file from a port to another on the same switch.Thank you ---

## Response 7
Hello, same problem here: CRS518-16XS-2XQ 7.16.1 (maximum host entry limit reached)Any statement of Mikrotik? Any other solution than downgrading?kr Josef ---

## Response 8
I also had the issue of maximum host entry limit reached. There was however one switch in my network that wasn't giving the maximum host entry error but was giving excessive or late collision, link duplex mismatch error messeges. After rebooting this switch the issue went away (for now). ---

## Response 9
Hi all, I have the same problem. After upgrade to 7.16.2 whole network was affected by slowdown and VLANs started drops.I see in the log the same issues as described.Mainly:bridge: maximum host entry limit reached (8192)sfp-sfpplus1 excessive or late collision, link duplex mismatch?hardware offloading activated on bridge "bridge" ports: ether38, ether40, ether39, ether42, ether41, ether46, ether43, ether44, ether45, ether47, ether48I did downgrade to 7.15.3 version and all is working again flawlessly.Does any have the solution for this problem?My network is 3x CRS326-24G-2S+, 2x CRS354-48G-4S+2Q+, 2x CRS354-48P-4S+2Q+. Connected using fiber optic or metallic 10G SFP modules from Mikrotik.Thank youJosef ---

## Response 10
Just to check:did anyone create a ticket to support about this ?Otherwise chances are high they do not know about it ... ---

## Response 11
Hi, I opened the ticket for this bug. I let know when there will be some news from MTK support. ---

## Response 12
There is the reply from support team.The problem should be fixed in the RouterOS 7.17 or newer:*) switch - fixed a potential issue with packet corruption caused by incorrect switch initialization on CRS3xx/5xx devices;Let us know if the issue still configured, and provide supout.rif files in case it does. ---