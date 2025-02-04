# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213273

# Discussion

## Initial Question
Author: Sat Dec 14, 2024 2:18 am
Hey there, hopefully I am not to blind to see the most obvious.Recently I upgraded my two RBLHGG-5acD to ROS 7.16.1 and also installed the wifi-qcom-ac driver on them.But now I don't find - as the documentation for point-to-point connections is only on wireless not wifi interfaces - the needed mode (ap bridge) in the settings. If this setting does not exsist (yet) in the wifi-section, is it the recommended way to stick with the legacy wireless driver package or should I rather use:on the first RBLHGG-5acD- Wireless mode: AP- the "access list" in the wifi configuration section to allow only one client - the second RBLHGG-5acD - to connectand adding a VLAN trunk on both interfaces to span my network over this connection which is not really a transparent L2 bridge anymore?Thanks in advance for your help. ---

## Response 1
Author: [SOLVED]Sat Dec 14, 2024 12:02 pm
AFAIK the mode "ap-bridge" has been renamed to simply "ap", see:viewtopic.php?p=1052701#p1052701The other side should be set in station-bridge mode, as both devices are Mikrotik:https://help.mikrotik.com/docs/spaces/R ... tion+Modes ---

## Response 2
Author: Mon Dec 16, 2024 9:39 pm
Thanks for clarification / pointing to the right place.