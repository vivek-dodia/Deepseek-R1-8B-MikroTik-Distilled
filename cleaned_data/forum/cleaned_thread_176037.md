# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 176037

# Discussion

## Initial Question
Author: Sun Jun 13, 2021 5:21 pm
This can be set to NONE, known to cause issues......../interface detect-internetset detect-interface-list=WANStill dont see your DNS server settings........../ip dhcp-server networkadd address=100.100.11.0/24 gateway=100.100.11.1dns-server=100.100.11.1add address=100.100.12.0/24 gateway=100.100.12.1 etcadd address=100.100.13.0/24 gateway=100.100.13.1 etcadd address=100.100.14.0/24 gateway=100.100.14.1 etcadd address=100.100.15.0/24 gateway=100.100.15.1 etcadd address=192.168.100.0/24 gateway=192.168.100.1 etcThis should be set to NONE/tool mac-serverset allowed-interface-list=LANLeft over from default settings, can be removed./ip dns staticadd address=192.168.88.1 comment=defconf name=router.lanMaybe add some decent DNS servers from the net/ip dnsset allow-remote-requests=yes servers=1.1.1.1, 9, 9, 9 ---

## Response 1
Author: Sun Jun 13, 2021 6:23 pm
This can be set to NONE, known to cause issues......../interface detect-internetset detect-interface-list=WANStill dont see your DNS server settings........../ip dhcp-server networkadd address=100.100.11.0/24 gateway=100.100.11.1dns-server=100.100.11.1add address=100.100.12.0/24 gateway=100.100.12.1 etcadd address=100.100.13.0/24 gateway=100.100.13.1 etcadd address=100.100.14.0/24 gateway=100.100.14.1 etcadd address=100.100.15.0/24 gateway=100.100.15.1 etcadd address=192.168.100.0/24 gateway=192.168.100.1 etcThis should be set to NONE/tool mac-serverset allowed-interface-list=LANLeft over from default settings, can be removed./ip dns staticadd address=192.168.88.1 comment=defconf name=router.lanMaybe add some decent DNS servers from the net/ip dnsset allow-remote-requests=yes servers=1.1.1.1, 9, 9, 9I am going to start over with no configuration in the 3011. Maybe I can understand my error by doing that from scratch. ---

## Response 2
Author: Sun Jun 13, 2021 6:25 pm
This can be set to NONE, known to cause issues......../interface detect-internetset detect-interface-list=WANStill dont see your DNS server settings........../ip dhcp-server networkadd address=100.100.11.0/24 gateway=100.100.11.1dns-server=100.100.11.1add address=100.100.12.0/24 gateway=100.100.12.1 etcadd address=100.100.13.0/24 gateway=100.100.13.1 etcadd address=100.100.14.0/24 gateway=100.100.14.1 etcadd address=100.100.15.0/24 gateway=100.100.15.1 etcadd address=192.168.100.0/24 gateway=192.168.100.1 etcThis should be set to NONE/tool mac-serverset allowed-interface-list=LANLeft over from default settings, can be removed./ip dns staticadd address=192.168.88.1 comment=defconf name=router.lanMaybe add some decent DNS servers from the net/ip dnsset allow-remote-requests=yes servers=1.1.1.1, 9, 9, 9I am going to start over with no configuration in the 3011. Maybe I can understand my error by doing that from scratch.Learning from my mistakes is a wonderful thing. Thanks for all the pointers and help. ---

## Response 3
Author: Mon Jun 14, 2021 5:59 pm
On your config some changes requiredAdd DNS server on the DHCP network settings AND REMOVE WHAT YOU HAVE DONE FOR adding DNS servers under IP DNS./ip dhcp-server networkadd address=10.2.2.0/24 gateway=10.2.2.1dns-server=10.2.2.1do this for all of them - should match the gateway!!add address=10.10.10.0/24 gateway=10.10.10.1add address=10.10.11.0/24 gateway=10.10.11.1add address=10.10.12.0/24 gateway=10.10.12.1add address=10.10.13.0/24 gateway=10.10.13.1add address=10.10.14.0/24 gateway=10.10.14.1add address=10.10.15.0/24 gateway=10.10.15.1add address=10.10.16.0/24 gateway=10.10.16.1add address=100.100.25.0/27 gateway=100.100.25.1add address=100.100.25.0/24 gateway=100.100.25.1For DNS servers just add a few good DNS servers that the router can use .../ip dnsset allow-remote-requests=yes servers=9.9.9.9, 1.1.1.1 etc.........Sourcenat rules need fixing.Remove the first one as it does nothing helpful.The rest as well.Alll you need isadd action=masquerade chain=srcnat out-interface-list=WAN