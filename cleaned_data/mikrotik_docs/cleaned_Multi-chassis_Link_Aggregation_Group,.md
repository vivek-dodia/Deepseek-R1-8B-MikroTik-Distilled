# Document Information
Title: Multi-chassis Link Aggregation Group
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/67633179/Multi-chassis+Link+Aggregation+Group,

# Content
# Introduction
MLAG (Multi-chassis Link Aggregation Group) implementation in RouterOS allows configuring LACP bonds on two separate devices, while the client device believes to be connected to the same machine. This provides a physical redundancy in case of switch failure. All CRS3xx, CRS5xx series switches, and CCR2116, CCR2216 devices can be configured with MLAG using RouterOS version 7.
Both peers establish the MLAG interfaces and update the bridge host table overpeer-portusing ICCP (Inter Chassis Control Protocol). RouterOS ICCP does not require an IP configuration, but it should be isolated from the rest of the network using a dedicated untagged VLAN. This untagged VLAN can be configured withvlan-filteringandpvid. Peer ports can also be configured as LACP bonding interfaces.
```
peer-port
```
```
vlan-filtering
```
```
pvid
```
Whenpeer-portis running and ICCP is established, the primary device election happens andsystem-idwill be selected. The peer with the lowestprioritywill act as the primary device. If the priorities are the same, the peer with the lowest bridge MAC address will become the primary. Thissystem-idis used for STP BPDU bridge identifier andLACP system ID. The MLAG requires enabled STP, RSTP or MSTP protocol. Use the same STP priority and the same STP configuration on dual-connected bridge ports on both nodes. When MLAG bridges are elected as STP root, then both devices will show as root bridges under the bridge monitor.
```
peer-port
```
```
system-id
```
```
priority
```
```
system-id
```
# Quick setup
in this example, CRS317 and CRS309 devices are used as MLAG peers and any device with two SFP+ interfaces can be used as an LACP client. The SFP+1 interface is used on both peer nodes to createpeer-port, and it is used for ICCP,  see a network scheme below.
```
peer-port
```
Below are configuration commands to create a regularLACP bondingin RouterOS for the Client device:
```
/interface bonding
add mode=802.3ad name=bond1 slaves=sfp-sfpplus1,sfp-sfpplus2
```
Next, configure bonding interfaces for MLAG on Peer1 and Peer2 devices, use a matchingmlag-idsetting on both peer devices:
```
mlag-id
```
```
# Peer1
/interface bonding
add mlag-id=10 mode=802.3ad name=client-bond slaves=sfp-sfpplus2
# Peer2
/interface bonding
add mlag-id=10 mode=802.3ad name=client-bond slaves=sfp-sfpplus2
```
Configure bridge with enabledvlan-filtering, and add needed interfaces as bridge ports. A dedicated untagged VLAN should be applied for the inter-chassis communication on a peer port, thus a differentpvidsetting is used. Below are configuration commands for Peer1 and Peer2 devices:
```
vlan-filtering
```
```
pvid
```
```
# Peer1
/interface bridge
add name=bridge1 vlan-filtering=yes
/interface bridge port
add bridge=bridge1 interface=sfp-sfpplus1 pvid=99
add bridge=bridge1 interface=client-bond
# Peer2
/interface bridge
add name=bridge1 vlan-filtering=yes
/interface bridge port
add bridge=bridge1 interface=sfp-sfpplus1 pvid=99
add bridge=bridge1 interface=client-bond
```
In this example, client-bond interfaces are using the default untagged VLAN 1 (the defaultpvid=1is set). In order to send these packets over peer ports, we need to add them as tagged VLAN 1 members. Notice that the defaultpvidvalue for the peer ports was changed in the previous step, it is important to include the peer ports in all the VLANs that are used on other bridge ports, this includes the untagged and tagged VLANs. Below are configuration commands for both peer devices:
```
pvid=1
```
```
pvid
```
```
# Peer1
/interface bridge vlan
add bridge=bridge1 tagged=sfp-sfpplus1 vlan-ids=1
# Peer2
/interface bridge vlan
add bridge=bridge1 tagged=sfp-sfpplus1 vlan-ids=1
```
Last, specifybridgeandpeer-portto enable MLAG. Below are configuration commands for both peer devices:
```
bridge
```
```
peer-port
```
```
# Peer1
/interface bridge mlag
set bridge=bridge1 peer-port=sfp-sfpplus1
# Peer2
/interface bridge mlag
set bridge=bridge1 peer-port=sfp-sfpplus1
```
Additionally, check MLAG status on peer devices and make sure that Client LACP has both interfaces active.
```
# Peer1
[admin@Peer1] > /interface/bridge/mlag/monitor
status: connected
system-id: 74:4D:28:11:70:6B
active-role: primary
# Peer2
[admin@Peer2] > /interface/bridge/mlag/monitor
status: connected
system-id: 74:4D:28:11:70:6B
active-role: secondary
# Client
[admin@Client] > /interface bonding monitor bond1
mode: 802.3ad
active-ports: sfp-sfpplus1,sfp-sfpplus2
inactive-ports:
lacp-system-id: 74:4D:28:7B:7F:96
lacp-system-priority: 65535
lacp-partner-system-id: 74:4D:28:11:70:6C
```
# MLAG settings and monitoring
This section describes the available MLAG settings and monitoring options.
Sub-menu:/interface bridge mlag
```
/interface bridge mlag
```
Property | Description
----------------------
bridge(interface;Default:none) | The bridge interface where MLAG is being created.
heartbeat(time: 1s..10s | none; Default:00:00:05) | This setting controls how often heartbeat messages are sent to check the connection between peers. If no heartbeat message is received for three intervals in a row, the peer logs a warning about potential communication problems. If set tonone, heartbeat messages are not sent at all.
peer-port(interface;Default:none) | An interface that will be used as a peer port. Both peer devices are using inter-chassis communication over these peer ports to establish MLAG and update the host table. Peer port should be isolated on a different untagged VLAN using apvidsetting. Peer port can be configured as a bonding interface.
priority(integer: 0..128;Default:128) | This setting changes the priority for selecting the primary MLAG node. A lower number means higher priority. If both MLAG nodes have the same priority, the one with the lowest bridge MAC address will become the primary device.
Property
Description
```
none
```
peer-port(interface;Default:none)
An interface that will be used as a peer port. Both peer devices are using inter-chassis communication over these peer ports to establish MLAG and update the host table. Peer port should be isolated on a different untagged VLAN using apvidsetting. Peer port can be configured as a bonding interface.
```
pvid
```
Use themonitorcommands to see the current MLAG status.
```
monitor
```
```
[admin@Peer1] > /interface/bridge/mlag/monitor
status: connected
system-id: 74:4D:28:11:70:6B
active-role: primary
```
Property | Description
----------------------
status(connected | connecting | disabled) | The MLAG status.
system-id(MAC address) | The lowest MAC address between both peer bridges will be used as thesystem-id. Thissystem-idis used for (R)STP BPDU bridge identifier andLACP system ID.
active-role(primary | secondary) | The peer with the lowestprioritywill act as the primary device. If the priorities are the same, the peer with the lowest bridge MAC address will become the primary. Thesystem-idof the primary device is used for sending the (R/M)STP BPDU bridge identifier and LACP system ID.
Property
Description
system-id(MAC address)
```
system-id
```
```
system-id
```
active-role(primary | secondary)
The peer with the lowestprioritywill act as the primary device. If the priorities are the same, the peer with the lowest bridge MAC address will become the primary. Thesystem-idof the primary device is used for sending the (R/M)STP BPDU bridge identifier and LACP system ID.
```
priority
```
```
system-id
```
Sub-menu:/interface bonding
```
/interface bonding
```
Property | Description
----------------------
mlag-id(integer: 0..4294967295;Default:) | Changes MLAG ID for bonding interface. The same MLAG ID should be used on both peer devices to successfully create a single LAG for the client device. Thepeer-portshould not be configured with the MLAG ID.
Property
Description
```
peer-port
```
LACP bonding interface and bonding slave ports can be monitored withmonitorandmonitor-slavescommands. See more details onBonding monitoring.
```
monitor
```
```
monitor-slaves
```