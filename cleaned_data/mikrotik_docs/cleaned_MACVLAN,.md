# Document Information
Title: MACVLAN
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/217874440/MACVLAN,

# Content
# Overview
The MACVLAN provides a means to create multiple virtual network interfaces, each with its own unique Media Access Control (MAC) address, attached to a physical network interface. This technology is utilized to address specific network requirements, such as obtaining multiple IP addresses or establishing distinct PPPoE client connections from a single physical Ethernet interface while using different MAC addresses. Unlike traditionalVLAN(Virtual LAN) interfaces, which rely on Ethernet frames tagged with VLAN identifiers, MACVLAN operates at the MAC address level, making it a versatile and efficient solution for specific networking scenarios.
# Basic Configuration Example
Picture a scenario where the ether1 interface connects to your ISP, and your router needs to lease two IP addresses, each with a distinct MAC address. Traditionally, this would require the use of two physical Ethernet interfaces and an additional switch. However, a more efficient solution is to create a virtual MACVLAN interface.
To create a MACVLAN interface, select the needed Ethernet interface. A MAC address will be automatically assigned if not manually specified:
```
/interface macvlan
add interface=ether1 name=macvlan1
/interface macvlan print
Flags: R - RUNNING
Columns: NAME, MTU, INTERFACE, MAC-ADDRESS, MODE
# NAME       MTU  INTERFACE  MAC-ADDRESS        MODE
0 R macvlan1  1500  ether1     76:81:BF:68:69:83  bridge
```
Now, a DHCP client can be created on ether1 and macvlan1 interfaces:
```
/ip dhcp-client
add interface=ether1
add interface=macvlan1
```
# Property Reference
Sub-menu:/interface/macvlan
```
/interface/macvlan
```
Configuration settings for the MACVLAN interface.
Property | Description
----------------------
arp(disabled | enabled | local-proxy-arp | proxy-arp | reply-only; Default:enabled) | Address Resolution Protocol settingdisabled- the interface will not use ARPenabled- the interface will use ARPlocal-proxy-arp-the router performs proxy ARP on the interface and sends replies to the same interfaceproxy-arp-the router performs proxy ARP on the interface and sends replies to other interfacesreply-only- the interface will only reply to requests originating from matching IP address/MAC address combinations, which are entered as static entries in theIP/ARPtable. No dynamic entries will be automatically stored in theIP/ARPtable. Therefore, for communications to be successful, a valid static entry must already exist.
arp-timeout(auto | integer; Default:auto) | Sets for how long the ARP record is kept in the ARP table after no packets are received from IP. Valueautoequals to the value ofarp-timeoutin/ip/settings/, default is 30s.
comment(string; Default: ) | Short description of the interface.
disabled(yes | no; Default:no) | Changes whether the interface is disabled.
interface(name; Default:) | Name of the interface on top of which MACVLAN will work. MACVLAN interfaces can be created on Ethernet or VLAN interfaces, adding VLAN on MACVLAN is not supported.
loop-protect(on | off | default; Default:default) | Enables or disables loop protect on the interface, thedefaultworks as turned off.
loop-protect-disable-time(time interval | 0; Default:5m) | Sets how long the selected interface is disabled when a loop is detected.0- forever.
loop-protect-send-interval(time interval; Default:5s) | Sets how often loop protect packets are sent on the selected interface.
mac-address(MAC; Default: ) | Static MAC address of the interface. Arandomly generated MAC address will be assigned when not specified.
mode(private | bridge; Default:bridge) | Sets MACVLAN interface mode:private- does not allow communication between MACVLAN instances on the same parentinterface.bridge- allows communication between MACVLAN instances on the same parentinterface.
mtu(integer; Default:1500) | Sets Layer 3 Maximum Transmission Unit. For the MACVLAN interface, it cannot be higher than the parentinterface.
name(string; Default:) | Interface name.
```
disabled
```
```
enabled
```
```
local-proxy-arp
```
```
proxy-arp
```
```
reply-only
```
```
auto
```
```
arp-timeout
```
```
/
```
```
ip/settings/
```
Sets MACVLAN interface mode:
```
private
```
```
bridge
```
Sets Layer 3 Maximum Transmission Unit. For the MACVLAN interface, it cannot be higher than the parentinterface.