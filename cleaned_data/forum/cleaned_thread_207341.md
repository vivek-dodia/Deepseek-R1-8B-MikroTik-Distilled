# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 207341

# Discussion

## Initial Question
Author: Mon May 06, 2024 10:03 pm
``` ping -f -l 1472 google.com ping -6 -l 1452 google.com ``` ``` ping -4 -M do -s 1472 -c 4 google.com ping -6 -M do -s 1452 -c 4 google.com ``` I just wanted to check the following:1. If I need to set my vlan101 MTU to 1508, does that mean that I need to set my ether1 MTU to 1512? (1508+4 for VLAN) or keep it at 1508?2. Do I need to adjust my L2 MTU values for ether1 (1514 -> 1526) and vlan101 (1522) to account for these MTU changes? It concerns me that these values are different to every other port on the bridge etc.3. Should the MTU on my VDSL modem be set to 1500 or 1508?You don't need to change the MTU of ether1 from the default of 1500. A few weeks ago, there were a bug with VLAN and MTU where back then you would need to set the MTU of ether1 to 1508 too, otherwise the MTU of vlan101 might be reset back to 1500 after a reboot, mentioned here:viewtopic.php?p=1059444#p1058995That bug seems to have been fixed now if you use the latest stable version 7.14.3. Now the MTU of ether1 can stay at 1500. You just need to make sure that the MTU value of 1508 for vlan101 is less than or equal to the L2MTU value on the column next to it (which should be the case). You also don't need to make the change on your modem. Like I wrote above the change needed on the ethernet interface directly underneath pppoe-outX (in this case vlan101 and MTU 1508) is only needed due to the bug(?) with the automatic MSS handling of the PPP profile. For the MTU value of the pppoe interface, the only requirement is that your ISP support RFC 4638.You don't need to change L2MTU if its value is already above 1508. You can watch this video for explanationshttps://www.youtube.com/watch?reload=9&v=7a_z1jAdIME. And here is an illustration with the interfaces on my router. pppoe-out1 (MTU 1500) uses vlan1000 (MTU 1508). vlan1000 sits over the main bridge (MTU 1500) and sfp-sfpplus1 is the access port for it (also MTU 1500). L2MTU of the VLAN interfaces are 1510, which is 4 bytes less than 1514 of the ethernet interfaces (see video for explanations) but is still greater than 1508, so no adjustments are needed.interfaces-mtu.pngIf the screenshot with the green text above is from your machine, then I think MTU 1500 is supported by your ISP and working. To test if you use Windows run:
```
if both commands succeed (no timeout or error message) then MTU 1500 works for both IPv4 (first command) as well as IPv6 (2nd command). For Linux, use
```

```
---
```

## Response 1
Author: Mon Aug 12, 2024 10:37 pm
``` # ":for" loop for ipv4 :for LoopCount4 from=40 to=1460 do={ :log info "Current loop4 count = $LoopCount4"; :local "target-mss4" ($LoopCount4 + 1) :set "target-mss4" ($"target-mss4" . "-65535") :log info $"target-mss4" /ip firewall mangle add action=add-src-to-address-list address-list=$LoopCount4 address-list-timeout=2h chain=forward comment=$LoopCount4 protocol=tcp tcp-flags=syn tcp-mss="$LoopCount4-$LoopCount4" add action=change-mss chain=forward comment=$LoopCount4 dst-address-list=$LoopCount4 new-mss=$LoopCount4 passthrough=yes protocol=tcp tcp-flags=syn tcp-mss=$"target-mss4" } # ":for" loop for ipv6 :for LoopCount6 from=40 to=1440 do={ :log info "Current loop6 count = $LoopCount6"; :local "target-mss6" ($LoopCount6 + 1) :set "target-mss6" ($"target-mss6" . "-65535") :log info $"target-mss6" /ipv6 firewall mangle add action=add-src-to-address-list address-list=$LoopCount6 address-list-timeout=2h chain=forward comment=$LoopCount6 protocol=tcp tcp-flags=syn tcp-mss="$LoopCount6-$LoopCount6" add action=change-mss chain=forward comment=$LoopCount6 dst-address-list=$LoopCount6 new-mss=$LoopCount6 passthrough=yes protocol=tcp tcp-flags=syn tcp-mss=$"target-mss6" } ``` here is script for proper and faster CCR internet. but YMMV.
```
your router now remembers TCP MSS for 2 hours for each connected server. Use with clamping enabled.
```