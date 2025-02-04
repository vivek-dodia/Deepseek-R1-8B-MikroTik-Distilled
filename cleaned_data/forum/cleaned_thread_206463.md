# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 206463

# Discussion

## Initial Question
Author: Thu Apr 04, 2024 9:31 pm
``` /interface bridge add name=aBridge port-cost-mode=short protocol-mode=none pvid=11 vlan-filtering=yes /interface vlan add interface=aBridge name=VLAN10 vlan-id=10 add interface=aBridge name=VLAN11 vlan-id=11 /interface list add name=WAN add name=LAN [...] /ip pool add name=VLAN10_POOL ranges=192.168.10.100-192.168.10.200 add name=VLAN11_POOL ranges=192.168.11.100-192.168.11.200 /ip dhcp-server add address-pool=VLAN10_POOL interface=VLAN10 lease-time=10m name=VLAN10_DHCP add address-pool=VLAN11_POOL interface=VLAN11 lease-time=10m name=VLAN11_DHCP [..] /interface bridge port add bridge=aBridge frame-types=admit-only-untagged-and-priority-tagged interface=ether2 internal-path-cost=10 path-cost=10 pvid=10 add bridge=aBridge frame-types=admit-only-untagged-and-priority-tagged interface=ether3 internal-path-cost=10 path-cost=10 pvid=10 add bridge=aBridge frame-types=admit-only-untagged-and-priority-tagged interface=wlan1 internal-path-cost=10 path-cost=10 pvid=10 add bridge=aBridge frame-types=admit-only-untagged-and-priority-tagged interface=wlan2 internal-path-cost=10 path-cost=10 pvid=11 add bridge=aBridge frame-types=admit-only-untagged-and-priority-tagged interface=ether4 internal-path-cost=10 path-cost=10 pvid=11 add bridge=aBridge frame-types=admit-only-untagged-and-priority-tagged interface=ether5 internal-path-cost=10 path-cost=10 pvid=11 [..] /interface bridge vlan add bridge=3TSBridge tagged=3TSBridge vlan-ids=101 add bridge=3TSBridge tagged=3TSBridge vlan-ids=100 /interface list member add interface=ether1 list=WAN add interface=VLAN10 list=LAN add interface=VLAN11 list=LAN /ip address add address=192.168.10.1/24 interface=VLAN10 network=192.168.10.0 add address=192.168.11.1/24 interface=VLAN11 network=192.168.11.0 [..] /ip dhcp-server network add address=192.168.10.0/24 dns-server=192.168.10.1 gateway=192.168.10.1 add address=192.168.11.0/24 dns-server=192.168.11.1 gateway=192.168.11.1 /ip dns set allow-remote-requests=yes /ip firewall address-list add address=192.168.10.0/24 list=LAN add address=192.168.11.0/24 list=LAN /ip firewall filter add action=accept chain=input comment="Accept established/related/untracked" connection-state=established, related, untracked add action=drop chain=input comment="Drop invalid" connection-state=invalid add action=accept chain=input comment="Accept ICMP" protocol=icmp add action=accept chain=input comment="Accept local loopback (for CAPsMAN)" dst-address=127.0.0.1 add action=drop chain=input comment="Drop all not comming from LAN" in-interface-list=!LAN add action=accept chain=forward comment="Accept in ipsec policy" ipsec-policy=in, ipsec add action=accept chain=forward comment="Accept out ipsec policy" ipsec-policy=out, ipsec add action=fasttrack-connection chain=forward comment="Fastrack for established/related" connection-state=established, related hw-offload=yes add action=accept chain=forward comment="Accept forwardig of established/related/untracked" connection-state=established, related, untracked add action=drop chain=forward comment="Drop all WAN not NATed" connection-nat-state=!dstnat connection-state=new in-interface-list=WAN /ip firewall nat add action=masquerade chain=srcnat comment="NAT out" ipsec-policy=out, none out-interface-list=WAN [..] ``` Hi everyone, after resolving this issueviewtopic.php?t=206359just wanted to know how to setup RouterOS 7 (without external switch) in order to have the following setup:VLAN10, 192.168.10.0/24, for router and proxmox managementVLAN11, 192, 168, 11.0/24, for virtualized machines inside Proxmox nodes on VLAN10I want to have a virtualized LAN in order to isolate "operative" infraestructure/LAN (VLAN11) inside the IT LAN (VLAN10).Besides Proxmox and virtualized machines setup, what would be the correct configuration of tagget/untagged in the router. Now I have the following conf (only what I believe is important for VLAN conf) but only VLAN10 is working (internet, LAN connection), VLAN11 outside proxmox working ok, VLAN11 inside proxmox seems not to have network connectivity (inside and outside):
```
Thanks in advance!Juan Ignacio.


---
```

## Response 1
Author: Fri Apr 05, 2024 12:22 am
The configuration doesn't make sense - you havename=aBridgein/interface bridgebut references tobridge=3TSBridgein/interface bridge vlan.Also, do not set the bridge-to-CPU PVID in/interface bridgeto have the same ID as an/interface vlanattached to the bridge. ---

## Response 2
Author: [SOLVED]Fri Apr 05, 2024 1:09 am
``` [admin@RT] > export # 2024-04-04 22:01:36 by RouterOS 7.15beta9 # software id = # /interface bridge add frame-types=admit-only-vlan-tagged name=bridge vlan-filtering=yes /interface vlan add interface=bridge name=VLAN10 vlan-id=10 add interface=bridge name=VLAN11 vlan-id=11 /ip pool add name=dhcp_pool0 ranges=192.168.10.2-192.168.10.254 add name=dhcp_pool1 ranges=192.168.11.2-192.168.11.254 /port set 0 name=serial0 /interface bridge port add bridge=bridge frame-types=admit-only-vlan-tagged interface=ether1 pvid=4094 /interface bridge vlan add bridge=bridge tagged=bridge, ether1 vlan-ids=10 add bridge=bridge tagged=bridge, ether1 vlan-ids=11 /ip address add address=192.168.10.1/24 interface=VLAN10 network=192.168.10.0 add address=192.168.11.1/24 interface=VLAN11 network=192.168.11.0 /ip dhcp-server add address-pool=dhcp_pool0 interface=VLAN10 name=dhcp1 add address-pool=dhcp_pool1 interface=VLAN11 name=dhcp2 /ip dhcp-server network add address=192.168.10.0/24 gateway=192.168.10.1 add address=192.168.11.0/24 gateway=192.168.11.1 /system identity set name=RT /system note set show-at-login=no /tool romon set enabled=yes ``` You need a trunk port on both router and proxmox, this is how you are going to do it if your equipment is aCRS 3xx switchthis is device specific , this is just a bare minimum and assume that your tagged port is ether1
```
---
```

## Response 3
Author: Fri Apr 05, 2024 1:40 am
``` [admin@RT] > export # 2024-04-04 22:01:36 by RouterOS 7.15beta9 # software id = # /interface bridge add frame-types=admit-only-vlan-tagged name=bridge vlan-filtering=yes /interface vlan add interface=bridge name=VLAN10 vlan-id=10 add interface=bridge name=VLAN11 vlan-id=11 /ip pool add name=dhcp_pool0 ranges=192.168.10.2-192.168.10.254 add name=dhcp_pool1 ranges=192.168.11.2-192.168.11.254 /port set 0 name=serial0 /interface bridge port add bridge=bridge frame-types=admit-only-vlan-tagged interface=ether1 pvid=4094 /interface bridge vlan add bridge=bridge tagged=bridge, ether1 vlan-ids=10 add bridge=bridge tagged=bridge, ether1 vlan-ids=11 /ip address add address=192.168.10.1/24 interface=VLAN10 network=192.168.10.0 add address=192.168.11.1/24 interface=VLAN11 network=192.168.11.0 /ip dhcp-server add address-pool=dhcp_pool0 interface=VLAN10 name=dhcp1 add address-pool=dhcp_pool1 interface=VLAN11 name=dhcp2 /ip dhcp-server network add address=192.168.10.0/24 gateway=192.168.10.1 add address=192.168.11.0/24 gateway=192.168.11.1 /system identity set name=RT /system note set show-at-login=no /tool romon set enabled=yes ``` Thanks @loloski, I believed the solution was about trunk port, but did not know how to apply the the specific mikrotic implementation (tried randomly some changes related to tagged/untagged without success) I will try you solution in my scenario and then tell the about results!Juan Ignacio.You need a trunk port on both router and proxmox, this is how you are going to do it if your equipment is aCRS 3xx switchthis is device specific , this is just a bare minimum and assume that your tagged port is ether1
```
---
```

## Response 4
Author: Thu Apr 11, 2024 6:05 am
``` admit-only-vlan-tagged ``` Thank you @loloski, just played a little more with
```
onaBridgeand the specific port to use Proxmox and its virtual machines.Have a nice week! Juan Ignacio.


---
```

## Response 5
Author: Wed Oct 30, 2024 7:29 pm
#Bridge/interface bridgeadd frame-types=admit-only-vlan-taggedname=bridge1 vlan-filtering=yes...#Bridge Port: Facing to Proxmox/interface bridge portadd bridge=bridge frame-types=admit-only-vlan-taggedinterface=ether2pvid=4094 ---

## Response 6
Author: Sat Nov 02, 2024 11:46 am
``` auto lo iface lo inet loopback iface enp0s25 inet manual auto vmbr0 iface vmbr0 inet static address 192.168.99.100/24 gateway 192.168.99.1 bridge-ports enp0s25 bridge-stp off bridge-fd 0 bridge-vlan-aware yes bridge-vids 2-4094 source /etc/network/interfaces.d/* ``` ``` auto lo iface lo inet loopback auto enp0s25 iface enp0s25 inet manual auto vmbr0 iface vmbr0 inet manual bridge-ports enp0s25 bridge-stp off bridge-fd 0 bridge-vlan-aware yes bridge-vids 2-4000 #vlans: 99, 210, 220; auto vmbr0.99 iface vmbr0.99 inet static address 192.168.99.100/24 gateway 192.168.99.1 #vlan-mgmt auto vmbr0.210 iface vmbr0.210 inet static address 192.168.210.100/24 #vlan-210 source /etc/network/interfaces.d/* ``` Settingpvid=is irrelevant withframe-types=admit-only-vlan-taggedas untagged packets are discarded.Yes, it's what is expected.The default Proxmox network interface withbridge-vlan-awarelook like this:
```
If we want to utilize all available vlans on single NIC, nothing works except with the configuration above, i.e. adding non-existent pvid. With this specific configuration, we can use any available vlans inside Proxmox or it's VMs.
```

```
It should be noted that the value of iface'sbridge-vids2-4094(default) must be changed into something likebridge-vids2-4090, then we use the value outside that range forpvidin the Mikrotik bridge/port. I'm not a linux expert. So I don't know if this behavior applies to all linux bridges or only on Proxmox.On VM inside Proxmox, simply tag the intended vlan:Proxmox.JPG


---
```

## Response 7
Author: Sat Nov 02, 2024 1:50 pm
``` /interface/bridge/port add bridge=bridge interface=etherX ingress-filtering=yes frame-types=allow-only-vlan-tagged /interface/bridge/vlan add bridge=bridge vlan-ids=2-4094 tagged=etherX ``` ``` /interface/bridge/vlan add bridge=bridge vlan-ids=2-299, 301-4094 tagged=etherX add bridge=bridge vlan-ids=300 tagged=bridge, etherX ``` If we want to utilize all available vlans on single NIC, nothing works except with the configuration above, i.e. adding non-existent pvid.Not entirely true. When setting VLAN-related thing on bridge and sub-items, things are pretty much divided:items underbridge/portare about ingress behavioursetting bridge port withframe-types=admit-only-vlan-taggedmakes pirt to reject any untagged frame on i gress. Also makes settingpvidcompletely irrellevantitems underbridge/vlanare about egress behaviouronly frames, belonging to one of VLANs of which port is member, can egress that port. If port is set as untagged member of port, then VLAN header will be stripped upon leaving the portitems on bridge definition (under bridge) are either about bridgeswitch-like entity(very few of them) or about CPU-facing bridge port (most of items) ... frame-types is one of CPU-facing port propertiesAnd then there are a few interactions between first two items above, some are automatic and some have to be enabled explicitly:when port is set with PVID (and it allways is even if with default value of 1) and frame-types setting allows untagged on ingress, then port isautomaticallyadded as untagged member of corresponding VLANThis doesn't happen in your case as frame-types setting doesn't allow untagged frames on ingresswheningress-filteringis enabled (bymanualconfiguration) on bridge/port, then port VLAN membership (from bridge/vlan) is consulted when determinimg if a frame can be allowed to ingress or not.I.e. if port is member of VLANs with IDs 100 and 200 and there's frame with VID 300 "trying to enter", it'll be dropped with ingress-filtering ebabled ... but would be alowed to ingress with ingress-filtering disabled (which is default setting).The proxmox config woukd be mirrored on proxmox-facing MT port lije this:
```
The problem with config in the bridge/vlan section is that there can be only line targeting any given VLAN ID. So if there was a line likeadd bridge=bridge vlan-ids=300 tagged=bridge,etherX, configuration attempt would fail. It woukd have to be rewritten like this:
```

```
The config libe order doesn't matter, what matters is "puncturing holes" in VID range of the upper line (and I'm not entirely sure if the syntax shown for merging two intervals is actually valid). And this need for "puncturing tge interval" is the biggest PITA when it comes to the way VLANs are configured in ROS (but it's actually the same way as in linux bridge).
```