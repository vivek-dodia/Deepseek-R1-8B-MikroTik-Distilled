# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210387

# Discussion

## Initial Question
Author: Mon Aug 26, 2024 10:43 pm
It would be nice to have a full export of the config to have a general overview of the situation:export file=anynameyouwish (minus any sensitive info)As for your question, you would need to configure a VLAN interface if you will be handling L3 traffic (addresses, DHCP, routing, etc.), and change the PVIDs of ether9-ether16 from/interface/bridge/portafter adding them to the VLAN enbled bridge from the same menu. If you handle L3 traffic, you would also need firewall rules to block traffic between the subnets.Here you can find some very useful info on how to generally set up VLANs:viewtopic.php?t=143620