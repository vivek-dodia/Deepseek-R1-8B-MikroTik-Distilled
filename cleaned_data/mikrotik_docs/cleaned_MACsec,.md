# Document Information
Title: MACsec
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/201523202/MACsec,

# Content
# Overview
The MACsec (Media Access Control Security) protocol is a standard security technology employed in Ethernet networks to ensure the confidentiality, integrity, and authenticity of data transmitted over the physical medium. MACsec is defined by IEEE standard 802.1AE.
MACsec utilizes GCM-AES-128 encryption over Ethernet and secures all LAN traffic, including DHCP, ARP, LLDP, and higher-layer protocols.
# Basic Configuration Example
Imagine Host1 ether1 is connected to Switch ether1 and Host2 ether1 is connected to Switch ether2. In this example, we will create two MACsec interface pairs and use a bridge to create a secure Layer2 connection between both end devices.
First, configure MACsec interfaces on Host1 and Host2. We can specify only the Ethernet interface and RouterOS will automatically generate the Connectivity Association Key (CAK) and connectivity association name (CKN). Use theprintcommand to see the values:
```
print
```
```
# Host1
/interface macsec
add interface=ether1 name=macsec1
[admin@Host2] /interface/macsec print
Flags: I - inactive, X - disabled, R - running
0   name="macsec1" mtu=1468 interface=ether1 status="negotiating" cak=71a7c363794da400dbde595d3926b0e9
ckn=f2c4660060169391d29d8db8a1f06e5d4b84a128bad06ad43ea2bd4f7d21968f profile=default
# Host2
/interface macsec
add interface=ether1 name=macsec1
[admin@Host2] /interface/macsec print
Flags: I - inactive, X - disabled, R - running
0   name="macsec1" mtu=1468 interface=ether1 status="negotiating" cak=dc47d94291d19a6bb26a0c393a1af9a4
ckn=e9bd0811dad1e56f06876aa7715de1855f1aee0baf5982ac8b508d4fc0f162d9 profile=default
```
On the Switch device, to enable MACsec we need to configure the matching CAK and CKN values for the appropriate Ethernet interface:
```
# Switch
/interface macsec
add comment=Host1 cak=71a7c363794da400dbde595d3926b0e9 ckn=f2c4660060169391d29d8db8a1f06e5d4b84a128bad06ad43ea2bd4f7d21968f interface=ether1 name=macsec1
add comment=Host2 cak=dc47d94291d19a6bb26a0c393a1af9a4 ckn=e9bd0811dad1e56f06876aa7715de1855f1aee0baf5982ac8b508d4fc0f162d9 interface=ether2 name=macsec2
```
Once the pre-shared keys are successfully exchanged, the MACsec Key Agreement (MKA) protocol is activated. MKA is responsible for ensuring the continuity of MACsec on the link and determines which side becomes the key server in a point-to-point connection. The key server generates a Secure Association Key (SAK) that is shared exclusively with the device on the other end of the link. This SAK is used to secure all data traffic passing through the link. Periodically, the key server generates a new randomly-created SAK and shares it over the point-to-point link to maintain MACsec functionality.
In RouterOS, the MACsec interface can be configured like any Ethernet interface. It can be used as a routable interface with an IP address, or placed inside a bridge. On Host1 and Host2 we will add an IP address from the same network. On Switch, we will use a bridge.
```
# Host1
/ip address
add address=192.168.10.10/24 interface=macsec1
# Host2
/ip address
add address=192.168.10.20/24 interface=macsec1
# Switch
/interface bridge
add name=bridge1
/interface bridge port
add bridge=bridge1 interface=macsec1
add bridge=bridge1 interface=macsec2
```
Last, confirm that Host1 can reach Host2 using a ping.
```
[admin@Host1] > ping 192.168.10.20
SEQ HOST                                     SIZE TTL TIME       STATUS
0 192.168.10.20                              56  64 1ms438us
1 192.168.10.20                              56  64 818us
2 192.168.10.20                              56  64 791us
3 192.168.10.20                              56  64 817us
4 192.168.10.20                              56  64 783us
sent=5 received=5 packet-loss=0% min-rtt=783us avg-rtt=929us max-rtt=1ms438us
```
# Property Reference
# Interface settings
Sub-menu:/interface/macsec
```
/interface/macsec
```
Configuration settings for the MACsec interface.
Property | Description
----------------------
cak(string; Default: ) | A 16-byte pre-shared connectivity association key (CAK). To enable MACsec, configure the matching CAK and CKN on both ends of the link. When not specified, RouterOS will automatically generate a random value.
ckn(string; Default: ) | A 32-byte connectivity association name (CKN). To enable MACsec, configure the matching CAK and CKN on both ends of the link. When not specified, RouterOS will automatically generate a random value.
comment(string; Default: ) | Short description of the interface.
disabled(yes | no; Default:no) | Changes whether the interface is disabled.
interface(name; Default:) | Ethernet interface name where MACsec is created on, limited to one MACsec interface per Ethernet.
mtu(integer; Default:1468) | Sets the maximum transmission unit. Thel2mtuwill be set automatically according to the associatedinterface(subtracting 32 bytes corresponding to the MACsec encapsulation). Thel2mtucannot be changed.
name(string; Default:macsec1) | Name of the interface.
profile(name; Default:default) | Sets MACsec profile, used for determining the key server in a point-to-point connection.
status(read-only: disabled |initializing|invalid| negotiating | open-encrypted) | Shows the current MACsec interface status.
Property
Description
Sets the maximum transmission unit. Thel2mtuwill be set automatically according to the associatedinterface(subtracting 32 bytes corresponding to the MACsec encapsulation). Thel2mtucannot be changed.
```
l2mtu
```
```
interface
```
```
l2mtu
```
Sets MACsec profile, used for determining the key server in a point-to-point connection.
Shows the current MACsec interface status.
# Profile settings
Sub-menu:/interface/macsec/profile
```
/interface/macsec/profile
```
Configuration settings for the MACsec profile.
Property | Description
----------------------
name(string; Default: ) | Name of the profile.
server-priority(integer: 0..255; Default:10) | Sets the priority for determining the key server in a point-to-point connection, a lower value means higher priority. In case of a priority match, the interface with the lowest MAC address will be acting as a key server.
Property
Description