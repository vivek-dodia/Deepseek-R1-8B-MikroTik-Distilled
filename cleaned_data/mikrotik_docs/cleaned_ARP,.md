# Document Information
Title: ARP
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/100892687/ARP,

# Content
# Summary
Sub-menu:/ip arp
```
/ip arp
```
Even though IP packets are addressed usingIP addresses, hardware addresses must be used to transport data from one host to another. Address Resolution Protocol is used to map OSI level 3 IP addresses to OSI level 2 MAC addresses. A router has a table of currently used ARP entries. Normally the table is built dynamically, but to increase network security, it can be partially or completely built statically by adding static entries.
# Properties
This section describes the ARP table configuration options.
Property | Description
----------------------
address(IP; Default:) | IP address to be mapped
interface(string; Default:) | Interface name the IP address is assigned to
mac-address(MAC; Default:00:00:00:00:00:00) | MAC address to be mapped to
published(yes | no; Default:no) | Static proxy-arp entry for individual IP addresses. When an ARP query is received for the specific IP address, the device will respond with its own MAC address. No need to set proxy-arp on the interface itself for all the MAC addresses to be proxied. The interface will respond to an ARP request only when the device has an active route towards the destination
Read-only properties:
Property | Description
----------------------
complete(yes | no) | Complete flag is included in ARP entries when the ARPstatusis permanent, reachable, stale, probe, or delay
dhcp(yes | no) | Whether the ARP entry is added by DHCP server
disabled(yes | no) | Whether the ARP entry is disabled
dynamic(yes | no) | Whether the entry is dynamically created
invalid(yes | no) | Whether the entry is not valid
status(delay | failed | incomplete | permanent | probe | reachable | stale) | Shows the ARP entry state:delay- neighbor entry validation is currently delayedfailed- ARP resolution has failed, the system was not able to obtain the MAC address for the given IP addressincomplete- system does not have the MAC address information for the IP address, it has not yet been resolvedpermanent- ARP entry is considered permanent and will not be removed from the table, even if it is not actively being used. This is set for manually configured ARP entriesprobe- neighbor is being probedreachable- ARP resolution is successful, and the MAC address associated with the IP address is know, the entry is valid until the reachability timeout expiresstale- entry is still valid, but it is aged. This means that the system has not recently communicated with the device associated with the IP address.
```
status
```
Shows the ARP entry state:
```
delay
```
```
failed
```
```
incomplete
```
```
permanent
```
```
probe
```
```
reachable
```
```
stale
```
# ARP Modes
It is possible to set several ARP modes on the interface configuration.
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
# Disabled
If the ARP feature is turned off on theinterface, i.e.,arp=disabledis used, ARP requests from clients are not answered by the router. Therefore, a static ARP entry should be added to the clients as well. For example, the router's IP and MAC addresses should be added to the Windows workstations using the arp command:
```
arp=disabled
```
```
C:\> arp -s 10.5.8.254  00-aa-00-62-c6-09
```
# Enabled
This mode is enabled by default on all interfaces. ARPs will be discovered automatically and new dynamic entries will be added to the ARP table.
# Proxy ARP
A router with a properly configured proxy ARP feature acts as a transparent ARP proxy between different networks.
This behavior can be useful, for example, if you want to assign dial-in (ppp, pppoe, pptp) clients' IP addresses from the same address space as used on the connected LAN.
Proxy ARP can be enabled on each interface individually with the commandarp=proxy-arp:
```
arp=proxy-arp
```
Setup proxy ARP:
```
[admin@MikroTik] /interface ethernet> set 1 arp=proxy-arp
[admin@MikroTik] /interface ethernet> print
Flags: X - disabled, R - running
# NAME                 MTU   MAC-ADDRESS         ARP
0  R ether1              1500  00:30:4F:0B:7B:C1 enabled
1  R ether2              1500  00:30:4F:06:62:12 proxy-arp
```
# Reply Only
If ARP property is set toreply-onlyon the interface, then the router only replies to ARP requests. Neighbor MAC addresses will be resolved only using statically configured entries from the "/ip arp" menu, but there will be no need to add the router's MAC address to other hosts' ARP tables like in case if ARP isdisabled.
```
reply-only
```
```
/ip arp
```
# Local Proxy Arp
If the ARP property is set tolocal-proxy-arpon an interface, then the router performs proxy ARP to/from this interface only. i.e. for traffic that comes in and goes out of the same interface. In a normal LAN, the default behavior is for two network hosts to communicate directly with each other, without involving the router.
```
local-proxy-arp
```
Withlocal-proxy-arpenabled, the router will respond to all client hosts with the router's own interface MAC address instead of the other host's MAC address.
```
local-proxy-arp
```
E.g. If Host A (192.168.88.2/24) queries for the MAC address of Host B (192.168.88.3/24), the router would respond with its own MAC address. In other words, iflocal-proxy-arpis enabled, the router would assume responsibility for forwarding traffic between Host A 192.168.88.2 and Host B 192.168.88.3. All the ARP cache entries on Hosts A and B will reference the router's MAC address. In this case, the router is performinglocal-proxy-arpfor the entire subnet 192.168.88.0/24.
```
local-proxy-arp
```
```
local-proxy-arp
```
An example for RouterOSlocal-proxy-arpcould be a bridge setup with a DHCP server and isolated bridge ports where hosts from the same subnet can reach each other only at Layer3 through bridge IP.
```
local-proxy-arp
```
```
/interface bridge
add arp=local-proxy-arp name=bridge1
/interface bridge port
add bridge=bridge1 horizon=1 interface=ether2
add bridge=bridge1 horizon=1 interface=ether3
add bridge=bridge1 horizon=1 interface=ether4
```
# Gratuitous ARP
It is possible to create Gratuitous ARP requests in RouterOS. To do so you must use the Traffic-Generator tool, below is an example of how to generate a Gratuitous ARP request to update the ARP table on a remote device:
```
/tool traffic-generator inject interface=ether2 \
data="ffffffffffff4c5e0c14ef78080600010800060400014c5e0c14ef780a057a01ffffffffffff0a057a01000000000000000000000000000000000000"
```
You must change the MAC address (4c5e0c14ef78) and the IP address (0a057a01) to your router's address. The IP address and the MAC address must be from the device that requests an ARP table update. You also need to specify through which interface (ether2) you want to send the Gratuitous ARP request. Make sure that the receiving device supports Gratuitous ARP requests.