# Thread Information
Title: Thread-1115582
Section: RouterOS
Thread ID: 1115582

# Discussion

## Initial Question
I have an interface (just a simple interface, not part of a bridge) and I would like to throw away incoming packets from a specific MAC address, can I do that on a RB960PGS (hEX PoE)? ---

## Response 1
Most likely switch ACL rules.Check this thread for more background info.viewtopic.php?t=203589 ---

## Response 2
On that particular device model, the followingshouldwork but you have to try:/interface ethernet switch ruleadd ports=ether5 src-mac-address=10:20:30:40:50:60/FF:FF:FF:FF:FF:FF switch=switch1 new-dst-ports=""On devices without switch chip rules support, you would have to create a dedicated bridge whose only port would be the interface in question. ---