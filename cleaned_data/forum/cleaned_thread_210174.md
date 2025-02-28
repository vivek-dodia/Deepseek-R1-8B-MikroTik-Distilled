# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210174

# Discussion

## Initial Question
Author: Thu Aug 15, 2024 11:05 am
I have a MikroTik RB951 router running RouterOS version 6.49, which I want to manage using CAPsMAN on my CRS326-24G-2S+ switch that is running RouterOS version 7.15 with the new CAPsMAN setup under the WiFi package. However, I am unable to see the RB951 in the CAPsMAN interface, even though other CAP devices running version 7.15 are visible and working fine.I have ensured that CAP is enabled on the RB951 and that the manager IP is set to the IP address of the CRS326. Both devices are on the same network, and there are no apparent firewall or routing issues preventing communication between them. I've also checked the logs on both devices, but I can't seem to pinpoint the problem.Has anyone encountered a similar issue or can provide guidance on what might be causing the RB951 to not appear in CAPsMAN? Any advice would be greatly appreciated. ---

## Response 1
Author: Thu Aug 15, 2024 12:08 pm
The new CAPsMAN does only support wifi-qcom and wifi-qcom-ac devices. The latter is supported on ac devices, using the ARM processor. Unfortunately, the RB951 is a MIPSBE device, hence you can't find it. If you want it to be managed by your switch, you have to add the wireless package and run two instances of CAPsMAN. ---

## Response 2
Author: Thu Aug 15, 2024 12:10 pm
Basically it's not compatible.. There isn't CAPsMAN v6 and v7. Two different versions areWireless CAPsMANandWiFi CAPsMAN.WiFi CAPsMAN is for newer devices, mainly 802.11axand also for 802.11ac.Anything older has to use Wireless CAPsMAN. But it can run on ROSv7, you just have to install wireless package.. ---

## Response 3
Author: [SOLVED]Thu Aug 15, 2024 1:29 pm
To continue where @neki stopped: even if both capsmans run on same device, they don't share config. And since support for better mobility (as in 802.11 r/k/v) is tied to wifi capsman, legacy cap devices don't benefit from that either.Which means that running legacy capsman for sake of single legacy cap device on an ARM switch with only 16MB of storage is very questionable IMO.