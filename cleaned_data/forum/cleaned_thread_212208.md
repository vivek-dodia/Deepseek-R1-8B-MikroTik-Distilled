# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212208

# Discussion

## Initial Question
Author: Fri Nov 01, 2024 3:02 pm
Hello, I am curios about the redirect-to-cpu ACL rule action.Hardware offload is enabled on the bridge. All ports show Hardware Offload as being active.I have the following test configuration:/interface bridgeadd admin-mac=00:11:22:33:44:55 auto-mac=no comment=defconf name=bridgeLocal/interface bridge portadd bridge=bridgeLocal comment=defconf interface=ether1 hw=yesadd bridge=bridgeLocal comment=defconf interface=ether2 hw=yesadd bridge=bridgeLocal comment=defconf interface=ether3 hw=yesadd bridge=bridgeLocal comment=defconf interface=ether4 hw=yesadd bridge=bridgeLocal comment=defconf interface=ether5 hw=yes/interface bridge settings/interface bridge settings set allow-fast-path=yes use-ip-firewall=yes/interface ethernet switch ruleadd dst-address=192.168.88.88/32 dst-port=22 ports=ether4 protocol=tcp \redirect-to-cpu=yes switch=switch1I have no IP firewall rules, so the packet should go back to the switch after reaching the IP firewall.The switch ACL rule checks whether the packet is destined to 192.168.88.88 on tcp port 22 and it will redirect this packet to the switch-CPU. All well and good, I can se the packet on the prerouting chain but I don't know how to forward the packet back to the switch, whenever the rule is active, the redirected traffic acts as if it's being dropped.I've read the packet flow and whether the packet receives additional processing or not, it should go back to the switch-cpu as it's destination is outside the router.Am I missing something?Thank you. ---

## Response 1
Author: [SOLVED]Tue Dec 17, 2024 8:23 am
You possibly also need a bridge nat rule to kick the packet into the routing section of the device.Something like:/interface bridge natadd action=redirect chain=dstnat disabled=no dst-address=192.168.88.88 ip-protocol=tcp dst-port=22 log=yes mac-protocol=ip