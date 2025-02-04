# Thread Information
Title: Thread-213934
Section: RouterOS
Thread ID: 213934

# Discussion

## Initial Question
Hi there, We are providing Wi-Fi solution to a hospitality client where there are 2 levels Level 1 function Banquet space and Level 2 where we have rooms.Here both the levels we have same SSID broadcasting but for level 1 we have vlan 10 and for level 2 we have vlan 20 as we have different login pages for both the levels.Vlans 10 and 20 DHCP pools are different.When a guest moves from Level 1 to Level 2 he faces internet disconnection issue and he has to switch off and switch on his wi-fi in order to get internet connectivity(this is an intermittent issue which happens with few guests)We tried to make the DHCP pools common for both the vlans 10 and 20 but the login pages are not directing properly.Can anyone help me on this one ---

## Response 1
I was able to reproduce your Issues in my LABIn some Cases, the Device will switch from one AP to anotherand if both have the same SSID/Password but are connected todifferent networks, the Device will experience the Issues you described.Requesting a new IP-Address from the DHCPor restarting the Wireless-Interface will solve the Issuebut it is not a Solution... ---