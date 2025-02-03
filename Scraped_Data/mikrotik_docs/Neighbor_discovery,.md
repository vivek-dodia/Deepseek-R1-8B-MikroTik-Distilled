---
title: Neighbor discovery
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/24805517/Neighbor+discovery,
crawled_date: 2025-02-02T21:12:44.349361
section: mikrotik_docs
type: documentation
---

* 1Summary
* 2Neighbor list
* 3Discovery configuration
* 4LLDP
# Summary
Neighbor Discovery protocols allow us to find devices compatible with MNDP (MikroTik Neighbor Discovery Protocol), CDP (Cisco Discovery Protocol), or LLDP (Link Layer Discovery Protocol) in the Layer2 broadcast domain. It can be used to map out your network.
# Neighbor list
The neighbor list shows all discovered neighbors in the Layer2 broadcast domain. It shows to which interface neighbor is connected, its IP/MAC addresses, and other related parameters. The list is read-only, an example of a neighbor list is provided below:
```
[admin@MikroTik] /ip neighbor print 
 # INTERFACE ADDRESS         MAC-ADDRESS       IDENTITY   VERSION    BOARD      
 0 ether13   192.168.33.2    00:0C:42:00:38:9F MikroTik   5.99       RB1100AHx2
 1 ether11   1.1.1.4         00:0C:42:40:94:25 test-host  5.8        RB1000   
 2 Local     10.0.11.203     00:02:B9:3E:AD:E0 c2611-r1   Cisco I...                    
 3 Local     10.0.11.47      00:0C:42:84:25:BA 11.47-750  5.7        RB750  
 4 Local     10.0.11.254     00:0C:42:70:04:83 tsys-sw1   5.8        RB750G    
 5 Local     10.0.11.202     00:17:5A:90:66:08 c7200      Cisco I...
```
Sub-menu:/ip neighbor
```
/ip neighbor
```
Property | Description
----------------------
address(IP) | The highest IP address configured on a discovered device
address6(IPv6) | IPv6 address configured on a discovered device
age(time) | Time interval since last discovery packet
discovered-by(cdp|lldp|mndp) | Shows the list of protocols the neighbor has been discovered by. The property is available since RouterOS version 7.7.
board(string) | RouterBoard model. Displayed only to devices with installed RouterOS
identity(string) | Configured system identity
interface(string) | Interface name to which discovered device is connected
interface-name(string) | Interface name on the neighbor device connected to the L2 broadcast domain. Applies to CDP.
ipv6(yes | no) | Shows whether the device has IPv6 enabled.
mac-address(MAC) | Mac address of the remote device. Can be used to connect with mac-telnet.
platform(string) | Name of the platform. For example "MikroTik", "cisco", etc.
software-id(string) | RouterOS software ID on a remote device. Applies only to devices installed with RouterOS.
system-caps(string) | System capabilities reported by the Link-Layer Discovery Protocol (LLDP).
system-caps-enabled(string) | Enabled system capabilities reported by the Link-Layer Discovery Protocol (LLDP).
unpack(none|simple|uncompressed-headers|uncompressed-all) | Shows the discovery packet compression type.
uptime(time) | Uptime of remote device. Shown only to devices installed with RouterOS.
version(string) | Version number of installed software on a remote device
# Discovery configuration
It is possible to change whether an interface participates in neighbor discovery or not using an Interface list. If the interface is included in the discovery interface list, it will send out basic information about the system and process received discovery packets broadcasted in the Layer2 network. Removing an interface from the interface list will disable both the discovery of neighbors on this interface and also the possibility of discovering this device itself on that interface.
```
/ip neighbor discovery-settings
```
Property | Description
----------------------
discover-interface-list(string; Default:static) | Interface list on which members the discovery protocol will run on.
discover-interval(time: 5s..9h6m8s; Default:30s) | Adjusts the frequency at which neighbor discovery packets are transmitted. It also adjusts the Time-to-Live (TTL) TLV value for CDP and LLDP packets using the formula: (discover-interval* 4) + 1. The setting is available since RouterOS version 7.16.
lldp-dcbx(yes | no; Default:no) | Whether to send Data Center Bridging Capabilities Exchange Protocol (DCBX) TLVs, which allows to communicate switchQoS settingsand capabilities with other neighboring devices using LLDP. Only applies to CRS3xx, CRS5xx, CCR2116 and CCR2216 devices.Enabled DCBX includes the following TLVs:ETS (Enhanced Transmission Selection) Configuration TLV. This TLV is used to share the switch's ETS configuration. It includes:The willingness bit, which indicates whether the device is willing to accept QoS configuration from neighboring devices. In RouterOS, the willing bit is set to disabled, meaning the switch will not accept remote configurations and instead uses its own settings.The priority assignment table, which maps priorities to specific traffic-class.The bandwidth allocation table, where RouterOS calculates the percentage of bandwidth allocated to each queue based on theweightproperty. This applies to queues using thehigh-priority-groupin the/interface/ethernet/switch/qos/tx-manager/queuesettings.The Transmission Selection Algorithm (TSA) table, wherehigh-priority-groupqueues are assigned to ETS,strict-priorityqueues to Strict Priority, andlow-priority-groupor non-hardware offloaded queues to the Vendor Specific Algorithm.ETS Recommendation TLV. This provides a recommendation on how neighboring devices should configure ETS. RouterOS uses the same data as in the ETS Configuration TLV to give its recommendation.Priority-based Flow Control Configuration TLV. This TLV is used to share PFC configuration. Similar to the ETS TLV, the willingness bit is set to disabled, meaning the switch does not accept remote PFC configurations. PFC is enabled for specific priorities based on settings configured under/interface/ethernet/switch/qos/priority-flow-control, and/interface/ethernet/switch/qos/port.Application Priority TLV. This TLV is used to communicate how different applications are prioritized in the network.Application VLAN TLV. This TLV is used to share VLAN configurations for applications. RouterOS currently does not support sending values in this TLV and will send an empty VLAN table instead.
lldp-mac-phy-config(yes | no; Default:no) | Whether to send MAC/PHY Configuration/Status TLV in LLDP, which indicates the interface capabilities, current setting of the duplex status, bit rate, and auto-negotiation. Only applies to the Ethernet interfaces. While TLV is optional in LLDP, it is mandatory when sending LLDP-MED, meaning this TLV will be included when necessary even though the property is configured as disabled.
lldp-max-frame-size(yes | no; Default:no) | Whether to send Maximum Frame Size TLV in LLDP, which indicates the maximum frame size capability of the interface in bytes (l2mtu+ 18). Only applies to the Ethernet interfaces.
lldp-poe-power(yes | no; Default:yes) | Two specific TLVs facilitate Power over Ethernet (PoE) management between Power Sourcing Equipment (PSE) and Powered Devices (PD):IEEE 802.3 Organizationally SpecificPower Via MDITLVTIA-1057 (LLDP-MED) Organizationally SpecificExtended Power via MDITLVThelldp-poe-powerattribute determines whether to transmit the IEEE 802.3 Organizationally Specific Power Via MDI TLV in LLDP messages.The transmission of LLDP-MED Organizationally Specific Extended Power via MDI TLV is not configurable. It is automatically included in outgoing LLDP-MED packets when the remote device has transmitted LLDP-MED capability of receiving power.These TLVs are relevant only for Ethernet interfaces that supportPoE-Out.The setting is available since RouterOS version 7.15, and it replaces PoE-out portpoe-lldp-enabledsetting.
lldp-med-net-policy-vlan(integer 0..4094; Default:disabled) | Advertised VLAN ID for LLDP-MED Network Policy TLV. This allows assigning a VLAN ID for LLDP-MED capable devices, such as VoIP phones. The TLV will only be added to interfaces where LLDP-MED capable devices are discovered. Other TLV values are predefined and cannot be changed:Application Type - VoiceVLAN Type - TaggedL2 Priority - 0DSCP Priority - 0When used together with the bridge interface, the (R/M)STP protocol should be enabled withprotocol-modesetting.Additionally, other neighbor discovery protocols (e.g. CDP) should be excluded usingprotocolsetting to avoid LLDP-MED misconfiguration.
lldp-vlan-info(yes | no;Default:no) | Whether to send IEEE 802.1 Organizationally Specific TLVs in LLDP related to VLANs.When this setting is enabled, three TLVs are advertised:Port VLAN ID. This applies to the bridge port'spvidproperty.Port And Protocol VLAN ID. This TLV is not used and always indicates "not supported" and "not enabled".VLAN Name. This includes up to 10 active VLANs from the "/interface/bridge/vlan" table.These TLVs are relevant to interfaces that are added to avlan-filteringbridge, and the setting is available since RouterOS version 7.16.
mode(rx-only | tx-only | tx-and-rx; Default:tx-and-rx) | Selects the neighbor discovery packet sending and receiving mode. The setting is available since RouterOS version 7.7.
protocol(cdp | lldp | mndp; Default:cdp,lldp,mndp) | List of used discovery protocols.
```
discover-interval
```
Whether to send Data Center Bridging Capabilities Exchange Protocol (DCBX) TLVs, which allows to communicate switchQoS settingsand capabilities with other neighboring devices using LLDP. Only applies to CRS3xx, CRS5xx, CCR2116 and CCR2216 devices.
Enabled DCBX includes the following TLVs:
* ETS (Enhanced Transmission Selection) Configuration TLV. This TLV is used to share the switch's ETS configuration. It includes:The willingness bit, which indicates whether the device is willing to accept QoS configuration from neighboring devices. In RouterOS, the willing bit is set to disabled, meaning the switch will not accept remote configurations and instead uses its own settings.The priority assignment table, which maps priorities to specific traffic-class.The bandwidth allocation table, where RouterOS calculates the percentage of bandwidth allocated to each queue based on theweightproperty. This applies to queues using thehigh-priority-groupin the/interface/ethernet/switch/qos/tx-manager/queuesettings.The Transmission Selection Algorithm (TSA) table, wherehigh-priority-groupqueues are assigned to ETS,strict-priorityqueues to Strict Priority, andlow-priority-groupor non-hardware offloaded queues to the Vendor Specific Algorithm.
* ETS Recommendation TLV. This provides a recommendation on how neighboring devices should configure ETS. RouterOS uses the same data as in the ETS Configuration TLV to give its recommendation.
* Priority-based Flow Control Configuration TLV. This TLV is used to share PFC configuration. Similar to the ETS TLV, the willingness bit is set to disabled, meaning the switch does not accept remote PFC configurations. PFC is enabled for specific priorities based on settings configured under/interface/ethernet/switch/qos/priority-flow-control, and/interface/ethernet/switch/qos/port.
* Application Priority TLV. This TLV is used to communicate how different applications are prioritized in the network.
* Application VLAN TLV. This TLV is used to share VLAN configurations for applications. RouterOS currently does not support sending values in this TLV and will send an empty VLAN table instead.
* The willingness bit, which indicates whether the device is willing to accept QoS configuration from neighboring devices. In RouterOS, the willing bit is set to disabled, meaning the switch will not accept remote configurations and instead uses its own settings.
* The priority assignment table, which maps priorities to specific traffic-class.
* The bandwidth allocation table, where RouterOS calculates the percentage of bandwidth allocated to each queue based on theweightproperty. This applies to queues using thehigh-priority-groupin the/interface/ethernet/switch/qos/tx-manager/queuesettings.
* The Transmission Selection Algorithm (TSA) table, wherehigh-priority-groupqueues are assigned to ETS,strict-priorityqueues to Strict Priority, andlow-priority-groupor non-hardware offloaded queues to the Vendor Specific Algorithm.
```
weight
```
```
high-priority-group
```
```
/interface/ethernet/switch/qos/tx-manager/queue
```
```
high-priority-group
```
```
strict-priority
```
```
low-priority-group
```
```
/interface/ethernet/switch/qos/priority-flow-control
```
```
/interface/ethernet/switch/qos/port
```
Whether to send MAC/PHY Configuration/Status TLV in LLDP, which indicates the interface capabilities, current setting of the duplex status, bit rate, and auto-negotiation. Only applies to the Ethernet interfaces. While TLV is optional in LLDP, it is mandatory when sending LLDP-MED, meaning this TLV will be included when necessary even though the property is configured as disabled.
Whether to send Maximum Frame Size TLV in LLDP, which indicates the maximum frame size capability of the interface in bytes (l2mtu+ 18). Only applies to the Ethernet interfaces.
```
l2mtu
```
Two specific TLVs facilitate Power over Ethernet (PoE) management between Power Sourcing Equipment (PSE) and Powered Devices (PD):
* IEEE 802.3 Organizationally SpecificPower Via MDITLV
* TIA-1057 (LLDP-MED) Organizationally SpecificExtended Power via MDITLV
Thelldp-poe-powerattribute determines whether to transmit the IEEE 802.3 Organizationally Specific Power Via MDI TLV in LLDP messages.
```
lldp-poe-power
```
The transmission of LLDP-MED Organizationally Specific Extended Power via MDI TLV is not configurable. It is automatically included in outgoing LLDP-MED packets when the remote device has transmitted LLDP-MED capability of receiving power.
These TLVs are relevant only for Ethernet interfaces that supportPoE-Out.The setting is available since RouterOS version 7.15, and it replaces PoE-out portpoe-lldp-enabledsetting.
```
poe-lldp-enabled
```
Advertised VLAN ID for LLDP-MED Network Policy TLV. This allows assigning a VLAN ID for LLDP-MED capable devices, such as VoIP phones. The TLV will only be added to interfaces where LLDP-MED capable devices are discovered. Other TLV values are predefined and cannot be changed:
* Application Type - Voice
* VLAN Type - Tagged
* L2 Priority - 0
* DSCP Priority - 0
When used together with the bridge interface, the (R/M)STP protocol should be enabled withprotocol-modesetting.
```
protocol-mode
```
Additionally, other neighbor discovery protocols (e.g. CDP) should be excluded usingprotocolsetting to avoid LLDP-MED misconfiguration.
```
protocol
```
Whether to send IEEE 802.1 Organizationally Specific TLVs in LLDP related to VLANs.
When this setting is enabled, three TLVs are advertised:
* Port VLAN ID. This applies to the bridge port'spvidproperty.
* Port And Protocol VLAN ID. This TLV is not used and always indicates "not supported" and "not enabled".
* VLAN Name. This includes up to 10 active VLANs from the "/interface/bridge/vlan" table.
```
pvid
```
```
/interface/bridge/vlan
```
These TLVs are relevant to interfaces that are added to avlan-filteringbridge, and the setting is available since RouterOS version 7.16.
Selects the neighbor discovery packet sending and receiving mode. The setting is available since RouterOS version 7.7.
Since RouterOS v6.44, neighbor discovery is working on individual slave interfaces. Whenever a master interface (e.g. bonding or bridge) is included in the discovery interface list, all its slave interfaces will automatically participate in neighbor discovery. It is possible to allow neighbor discovery only to some slave interfaces. To do that, include the particular slave interface in the list and make sure that the master interface is not included.
```
/interface bonding
add name=bond1 slaves=ether5,ether6
/interface list
add name=only-ether5
/interface list member
add interface=ether5 list=only-ether5
/ip neighbor discovery-settings
set discover-interface-list=only-ether5
```
Now the neighbor list shows a master interface and actual slave interface on which a discovery message was received.
```
[admin@R2] > ip neighbor print
 # INTERFACE ADDRESS                                           MAC-ADDRESS       IDENTITY   VERSION    BOARD         
 0 ether5    192.168.88.1                                      CC:2D:E0:11:22:33 R1         6.45.4 ... CCR1036-8G-2S+
   bond1
```
# LLDP
Depending on RouterOS configuration, different type-length-value (TLV) can be sent in the LLDP message, this includes:
* Chassis ID (MAC address)
* Port ID (interface name)
* Time To Live
* System Name (system identity)
* System Description (platform - MikroTik, software version - RouterOS version,  hardware name - RouterBoard name)
* Management Address (all IP addresses configured on the port)
* System Capabilities (enabled system capabilities, e.g. bridge or router)
* Port Description (combined interface name like "bridge/ether1" if the sending interface is part of bridge or bond, or interface name same as Port ID)
* IEEE 802.1Port VLAN ID
* IEEE 802.1Port And Protocol VLAN ID
* IEEE 802.1VLAN Name
* IEEE 802.3 MAC/PHY Configuration/Status
* IEEE 802.3 Power Via MDI
* IEEE 802.3 Maximum Frame Size
* LLDP-MED Media Capabilities (list of MED capabilities)
* LLDP-MED Network Policy (assigned VLAN ID for voice traffic)
* LLDP-MED Extended Power via MDI
* Port Extension (Port Extender and Controller Bridge advertisement)
* End of LLDPDU