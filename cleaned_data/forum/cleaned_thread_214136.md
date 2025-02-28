# Thread Information
Title: Thread-214136
Section: RouterOS
Thread ID: 214136

# Discussion

## Initial Question
Hi friendsHere's my topology:topology.pngIt's mostly good. I've had zero links down. However, I'm getting high Tx Drops on CORE -SW01 on the 3xSFP28 interfaces in the 802.3ad link. I think that's why everything seems OK on the network, but we get random disconnects from things like out ERP system very occasionally. It's a CRS518-16XS-2XQ (as are the other CORE-SWs). I've seen other forum posts suggest that this is a problem with LACP links. Something about too much data being sent to the bond interface and the interface dropping packets when it's overloaded. It makes sense that there could be a lot of traffic going across those links - CORE-SW01 and CORE-SW02 look after one server stack and CORE-SW03 and CORE-SW04 look after another server stack and both stacks are supposed to replicate to each other. Each server has a few 25Gbps links to the core switches, plus that 100Gbps between the two core switches. I think that's why I get RSTP topology changes at the same time every day - servers doing big workloads over the link.Do you think that could be the issue? All the SFP28 adapters are the same and its only CORE -SW01 having issues?Can you give any recommendations on helping find the underlying cause or give me suggestions on how we could improve things?My transmit hash policy for the LACP link is currently layer 2. I saw after implementation that I should have moved this to layer 3 + layer 4. Is that fine to do live? Others have suggested that the switch chips I have will do layer 2 + layer 3 + layer 4 anyway, regardless of what setting I use.I've also seen suggestions that I could limit bandwidths in places that might help.Any thoughts or suggestions you might have would be appreciated. ---

## Response 1
if you can try RouterOS 7.16.2, then enable QoS hardware offloadingin Winbox switch QoS menu you will have detailed info about buffer and drops on each interfacejust in case: be sure you have all interfaces using hardware offload within a properly configured bridge ---

## Response 2
if you can try RouterOS 7.16.2, then enable QoS hardware offloadingin Winbox switch QoS menu you will have detailed info about buffer and drops on each interfacejust in case: be sure you have all interfaces using hardware offload within a properly configured bridgeThanks chechito. I'm a bit of a noob to QoS sorry. Would that just allow me to prioritise traffic, or does it add some additional buffers that might help stop TX Drops? Would you be able to share some configuration you'd apply for this situation?Also, would you recommend 7.17 instead, since it's considered stable now? ---

## Response 3
I did find these cool transceivers:https://www.fs.com/au/products/135560.htmlI think I'll give them a go and create a true 100Gbps link between the two stacks and see how I go from there.Any other suggestions would be welcomed. I'm interested in the hardware QoS option still, but I'm not sure how to implement and how it would help. ---