# Document Information
Title: Basic VLAN switching
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/103841826/Basic+VLAN+switching,

# Content
# Introduction
Many MikroTik devices come with built-in switch chips that usually have an option to do VLAN switching on a hardware level, this means that you can achieve wire-speed performance using VLANs if a proper configuration method is used. The configuration method changes across different models, this guide will focus on setting up a basic trunk/access port with a management port from the trunk port using different devices with the right configuration to achieve the best performance and to fully utilize the available hardware components.
# CRS3xx, CRS5xx series switches, CCR2116, CCR2216 andRTL8367, 88E6393X, 88E6191X, 88E6190, MT7621 and MT7531 switch chips
```
/interface bridge
add name=bridge1 frame-types=admit-only-vlan-tagged
/interface bridge port
add bridge=bridge1 interface=ether1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether2 pvid=20 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether3 pvid=30 frame-types=admit-only-untagged-and-priority-tagged
/interface bridge vlan
add bridge=bridge1 tagged=ether1 vlan-ids=20
add bridge=bridge1 tagged=ether1 vlan-ids=30
add bridge=bridge1 tagged=ether1,bridge1 vlan-ids=99
/interface vlan
add interface=bridge1 vlan-id=99 name=MGMT
/ip address
add address=192.168.99.1/24 interface=MGMT
/interface bridge
set bridge1 vlan-filtering=yes
```
More detailed examples can be foundhere.
# CRS1xx/CRS2xx series switches
```
/interface bridge
add name=bridge1
/interface bridge port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
/interface ethernet switch ingress-vlan-translation
add ports=ether2 customer-vid=0 new-customer-vid=20
add ports=ether3 customer-vid=0 new-customer-vid=30
/interface ethernet switch egress-vlan-tag
add tagged-ports=ether1 vlan-id=20
add tagged-ports=ether1 vlan-id=30
add tagged-ports=ether1,switch1-cpu vlan-id=99
/interface ethernet switch vlan
add ports=ether1,ether2 vlan-id=20
add ports=ether1,ether3 vlan-id=30
add ports=ether1,switch1-cpu vlan-id=99
/interface vlan
add interface=bridge1 vlan-id=99 name=MGMT
/ip address
add address=192.168.99.1/24 interface=MGMT
/interface ethernet switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether1,ether2,ether3
```
More detailed examples can be foundhere.
# Other devices with a built-in switch chip
```
/interface bridge
add name=bridge1
/interface bridge port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
/interface ethernet switch vlan
add ports=ether1,ether2 switch=switch1 vlan-id=20
add ports=ether1,ether3 switch=switch1 vlan-id=30
add ports=ether1,switch1-cpu switch=switch1 vlan-id=99
/interface vlan
add interface=bridge1 vlan-id=99 name=MGMT
/ip address
add address=192.168.99.1/24 interface=MGMT
/interface ethernet switch port
set ether1 vlan-mode=secure vlan-header=add-if-missing
set ether2 vlan-mode=secure vlan-header=always-strip default-vlan-id=20
set ether3 vlan-mode=secure vlan-header=always-strip default-vlan-id=30
set switch1-cpu vlan-header=leave-as-is vlan-mode=secure
```
More detailed examples can be foundhere.
# Other devices without a built-in switch chip
It is possible to do VLAN filtering using the CPU, there are multiple ways to do it, but it is highly recommended to use bridge VLAN filtering.
```
/interface bridge
add name=bridge1 frame-types=admit-only-vlan-tagged
/interface bridge port
add bridge=bridge1 interface=ether1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether2 pvid=20 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether3 pvid=30 frame-types=admit-only-untagged-and-priority-tagged
/interface bridge vlan
add bridge=bridge1 tagged=ether1 vlan-ids=20
add bridge=bridge1 tagged=ether1 vlan-ids=30
add bridge=bridge1 tagged=ether1,bridge1 vlan-ids=99
/interface vlan
add interface=bridge1 vlan-id=99 name=MGMT
/ip address
add address=192.168.99.1/24 interface=MGMT
/interface bridge
set bridge1 vlan-filtering=yes
```
More detailed examples can be foundhere.