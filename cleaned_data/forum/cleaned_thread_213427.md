# Thread Information
Title: Thread-213427
Section: RouterOS
Thread ID: 213427

# Discussion

## Initial Question
HiI have a RB911-5HPnD, an old Mikrotik Wi-Fi antenna which gets a WAN IP on its Wi-Fi interface set to station mode.Now, I'd like to put an OPNsense device behind it (plugged to the only one RB91's Ethernet LAN-port), and I would like to avoid double NAT.In a few words, I want to pass the antenna WAN IP to the OPNsense WAN interface. Is it possible?Thanks ---

## Response 1
It should be enough to bridge the wireless interface on the 911 with ether1, remove any IP configuration from it, and change the wireless interfacemodefromstationtostation-pseudobridge-clone. But if your ISP reserves the DHCP lease of the public IP for you based on your MAC address, you may have to set the MAC address of the OPNsense WAN interface to the one of the wireless interface of the 911, and set the own MAC address of the wireless interface to something else.After such a change, you have to manage the 911 via the MAC address of ether1, or you can set up a VLAN on the bridge and on the WAN of the OPNsense to host a management subnet so that you could reach the 911 via an IP address. ---

## Response 2
It should be enough to bridge the wireless interface on the 911 with ether1, remove any IP configuration from it, and change the wireless interfacemodefromstationtostation-pseudobridge-clone. But if your ISP reserves the DHCP lease of the public IP for you based on your MAC address, you may have to set the MAC address of the OPNsense WAN interface to the one of the wireless interface of the 911, and set the own MAC address of the wireless interface to something else.No public IP. The wan is on another private subnetWhy Do I need to change the wireless interface mode from station to station-pseudobridge-clone? Just to learn something new.After such a change, you have to manage the 911 via the MAC address of ether1, or you can set up a VLAN on the bridge and on the WAN of the OPNsense to host a management subnet so that you could reach the 911 via an IP address.Interesting solution indeed. Could you please give more details and even a rough setup?Thanks ---

## Response 3
By the way, any issue with the DHCP client on the WAN once I set it up in the bridge? ---

## Response 4
No public IP. The wan is on another private subnetWhy Do I need to change the wireless interface mode from station to station-pseudobridge-clone? Just to learn something new.The design of 802.11 did not expect any L2 networks to exist behind STAtions (clients), hence whilst there are separate fields for transmitter MAC address and sender MAC address in the wireless frames the AP sends to the STA, the receiver MAC address and destination MAC address share the same header field; in the frames from the STA to the AP, there is only one MAC address header field for transmitter and sender and two separate ones for recipient and destination. Frame formats with 4 MAC addresses are proprietary per vendor (station-bridge mode on Mikrotik switches to this type of frames and Mikrotik APs adjust to the capabilities of the individual STAs.Interesting solution indeed. Could you please give more details and even a rough setup?Assuming you already have a bridge namedbridgeon the 911, withwlan1andether1as ports, do the following:/interface vlan add interface=bridge vlan-id=123 name=bridge.mgmt.123/ip address add address=10.123.123.123/24 interface=bridge.mgmt.123Then do whatever needs to be done to attach a VLAN "subinterface" to the WAN interface of the OPNSense and attach an IP address from 10.123.123.0/24 to it, and you'll be able to connect to the 911 using 10.123.123.123. ---

## Response 5
By the way, any issue with the DHCP client on the WAN once I set it up in the bridge?Well - multiple ones. A client should not be attached to a member port of a bridge, that's first, so if it wasn't for the rest, you would have to move the DHCP client from wlan1 to the bridge. I don't think it is a good idea to combine a locally originated traffic withmodeof the wireless interface set tostation-pseudobridge-clone, that's second, so better disable the DHCP client completely. And third, even if the address you get from the remote AP is not public, you may still be entitled to just one IP address in total, so asking for two might cause issues as well. ---

## Response 6
Assuming you already have a bridge namedbridgeon the 911, withwlan1andether1as ports, do the following:/interface vlan add interface=bridge vlan-id=123 name=bridge.mgmt.123/ip address add address=10.123.123.123/24 interface=bridge.mgmt.123Then do whatever needs to be done to attach a VLAN "subinterface" to the WAN interface of the OPNSense and attach an IP address from 10.123.123.0/24 to it, and you'll be able to connect to the 911 using 10.123.123.123.Please bear with me, there is still something here I don't understand.An IP in the subnet 10.123.123.0/24, let's say 10.123.123.124, is going to be the OPNsense WAN IP or is it just for management purpose, so that I can enter in the mikrotik device via Winbox from an OPNsense LAN client? ---

## Response 7
The second, the "main" IP will be obtained using the DHCP client attached to the OPNsense WAN IP itself, via untagged frames. VLAN-tagged frames use the same cable but provide logical separation. ---

## Response 8
The second, the "main" IP will be obtained using the DHCP client attached to the OPNsense WAN IP itself, via untagged frames. VLAN-tagged frames use the same cable but provide logical separation.Got it!I am going to give it a try ASAPThank you very much ---