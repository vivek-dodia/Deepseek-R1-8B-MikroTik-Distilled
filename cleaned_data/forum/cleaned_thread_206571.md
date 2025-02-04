# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 206571

# Discussion

## Initial Question
Author: Tue Apr 09, 2024 7:01 am
``` /interface bridge add name=LOOPBACK /interface ethernet set [ find default-name=ether2 ] mtu=1530 /port set 0 name=serial0 /ip address add address=10.0.0.1 interface=LOOPBACK network=10.0.0.1 add address=192.168.1.1/30 interface=ether2 network=192.168.1.0 /ip dhcp-client add interface=ether1 /mpls interface add disabled=no input=yes interface=dynamic /mpls ldp add disabled=no lsr-id=10.0.0.1 /mpls ldp interface add disabled=no interface=ether2 transport-addresses=10.0.0.1 /system identity set name=R1 /system note set show-at-login=no /tool romon set enabled=yes ``` ``` /interface bridge add name=LOOPBACK /interface ethernet set [ find default-name=ether1 ] mtu=1530 /port set 0 name=serial0 /ip address add address=10.0.0.2 interface=LOOPBACK network=10.0.0.2 add address=192.168.1.2/30 interface=ether1 network=192.168.1.0 /ip dhcp-client add interface=ether1 /ip route add disabled=no dst-address=0.0.0.0/0 gateway=10.0.0.1 routing-table=main \ suppress-hw-offload=no /mpls interface add disabled=no input=yes interface=dynamic /mpls ldp add disabled=no lsr-id=10.0.0.2 transport-addresses=10.0.0.2 /mpls ldp interface add disabled=no interface=ether1 transport-addresses=10.0.0.2 /system identity set name=R2 /system note set show-at-login=no /tool romon set enabled=yes ``` I configured MPLS and I got those Flags and MPLS dont work at all.I tried everything but I don't get the issue.imagen_2024-04-08_235640084.pngR1 - CONFIG
```
R2 - CONFIG
```

```
imagen_2024-04-09_000023779.pngNote: I try to do the same config on physical router and I get the same flags.
```