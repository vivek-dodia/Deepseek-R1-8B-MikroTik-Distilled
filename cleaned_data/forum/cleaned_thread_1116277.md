# Thread Information
Title: Thread-1116277
Section: RouterOS
Thread ID: 1116277

# Discussion

## Initial Question
Hi!I have a starlink kit gen 2 with network adapter. The starlink router is not configured in bridge (bypass).I configured a dhcp-client in interface that's connected with starlink's network adapter. The internet works ok.But, about a day later, the internet in mikrotik stops working. In dhcp-client option i see status "searching", and doesn't change.I try reboot mikrotik, disabling and enabling the dhcp-client in interface, change the ethernet cable between network adapter and mikrotik.The only thing that works is power-off the starlink system and power on again. But in next day, the problem occurs again?The starlink supports just asks me to change the ethernet cable, but doesn't work.Has anyone ever experienced this?Thanks a lot! ---

## Response 1
I have the same setup without issues.Here is the Starlink WAN port config: ---

## Response 2
I seem to be encountering this same issue.It appears the Mikrotik nAP router is not accepting a DHCP address from the starlink. Occasionally it will work, but in the cases where it fails - such as during a bootup of the starlink and the mikrotik router it never resolves an IP address.When I direct attach a laptop via ethernet to starlink I receive a IP via DHCP every time. The DHCP includes both IPv6 and IPv4 information. But for some reason when I move the Ethernet connection back to the mikrotik, same problem - it never resolves an IP address.The setup is a basic as you could guess on the Mikrotik. Default config. Running the lastest firmware. I turned off the firewall feature just to ensure it was not somehow affecting the dhcp process, but it didn't correct the problem. Perhaps I'll try a 3rd party router in place of the Mikrotik just to confirm it appears the problems stays with the Mikrotik installation.But if there is a way to troubleshoot the dhcp client, I'd like to resolve this fundamental issue....thanks ---

## Response 3
Did either post author find a resolution? I have an old RB2011 that has this issue. It never receives a DHCP address from the Starlink router (not in bypass). ---

## Response 4
Did either post author find a resolution? I have an old RB2011 that has this issue. It never receives a DHCP address from the Starlink router (not in bypass).From my novice experience with this issue, check your configuration and make sure the WAN eth port connected to starlink adapter isn't in a bridge... If it is, remove it. You can make searches about getting a proper router config ---

## Response 5
This problem seems to happen often, I am having this problem too! ---