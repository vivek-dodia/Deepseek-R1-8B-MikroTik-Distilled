# Document Information
Title: Wake on LAN
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/120782862/Wake+on+LAN,

# Content
# Introduction
Sub-menu:/tool wol
```
/tool wol
```
The Wake on LAN tool can send aUDP Magic Packet to the Broadcast address with a selected MAC address embedded in it.
If the target device supports Wake on LAN (a target computer has specific hardware and software requirements for the Wake on LAN feature to work), it should wake up from sleep or shutdown state.
Currently, secure WoL is not supported.
# Property Description
Property | Description
----------------------
interface(string; Default:) | Interface through which the Magic Packet will be sent
mac(MAC; Default: ) | MAC address of a target computer
Interface through which the Magic Packet will be sent
# Application Example
The command requires a MAC address parameter and interface.
```
/tool wol mac=FE:4B:71:05:EA:8B interface=ether1
```