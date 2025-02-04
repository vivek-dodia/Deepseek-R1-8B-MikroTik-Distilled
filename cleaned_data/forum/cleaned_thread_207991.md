# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 207991

# Discussion

## Initial Question
Author: Tue Dec 24, 2024 2:32 am
``` [admin@rb450gx4-hkjm]/routing/ospf/interface>printFlags:D-dynamic0D address=192.168.9.254%vlan9 area=10.8.0.0state=passive network-type=broadcast cost=1priority=128use-bfd=noretransmit-interval=5stransmit-delay=1shello-interval=10sdead-interval=40s1D address=192.168.10.254%vlan10 area=10.8.0.0state=passive network-type=broadcast cost=1priority=128use-bfd=noretransmit-interval=5stransmit-delay=1shello-interval=10sdead-interval=40s2D address=192.168.11.254%vlan11 area=10.8.0.0state=passive network-type=broadcast cost=1priority=128use-bfd=noretransmit-interval=5stransmit-delay=1shello-interval=10sdead-interval=40s3D address=192.168.8.254%vlan8 area=10.8.0.0state=passive network-type=broadcast cost=1priority=128use-bfd=noretransmit-interval=5stransmit-delay=1shello-interval=10sdead-interval=40s4D address=172.29.100.9%wg109 area=0.0.0.0state=ptp network-type=ptp cost=106use-bfd=noretransmit-interval=5stransmit-delay=1shello-interval=10sdead-interval=40s5D address=172.29.100.1%wg101 area=0.0.0.0state=ptp network-type=ptp cost=101use-bfd=noretransmit-interval=5stransmit-delay=1shello-interval=10sdead-interval=40s6D address=172.29.100.5%wg105 area=0.0.0.0state=ptp network-type=ptp cost=105use-bfd=noretransmit-interval=5stransmit-delay=1shello-interval=10sdead-interval=40s[admin@rb450gx4-hkjm]/routing/ospf/area/range>printFlags:A-ADVERTISEColumns:AREA, PREFIX# AREA PREFIX0A10.8.0.0192.168.8.0/22[admin@rb450gx4-hkjm]/routing/ospf/lsa>printwhereid=192.168.8.0Flags:S-self-originated, F-flushing, W-wraparound;D-dynamic0SD instance=ospf-instance-1area=0.0.0.0type="inter-area-prefix"originator=10.8.0.100id=192.168.8.0sequence=0x80002963age=225checksum=0x27C4body=netmask=255.255.255.0metric=1 ``` I might encounter the same problem.The ABR(rb450gx4 , fw: 7.16.2) has 192.168.8.0/24, 192.168.9.0/24, 192.168.10.0/24 and 192.168.11.0/24. I create an area range item: 192.168.8.0/22 adv=yes, but ospf propagate the wrong lsa:
```
I have been reboot the routerboard, no suprised.any suggestion？


---
```

## Response 1
Author: Tue Dec 24, 2024 8:53 am
``` Flags:A-ADVERTISEColumns:AREA, PREFIX, COST# AREA PREFIX COST0A dt.home10.21.0.0/1610 ``` Set value for COST, for example as bellow:
```
---
```

## Response 2
Author: Tue Dec 24, 2024 10:36 am
``` Flags:A-ADVERTISEColumns:AREA, PREFIX, COST# AREA PREFIX COST0A dt.home10.21.0.0/1610 ``` ``` [admin@rb4011-2w]/routing/ospf/lsa>printwhereid=192.168.8.0Flags:S-self-originated, F-flushing, W-wraparound;D-dynamic1SD instance=ospf-instance-1area=10.12.0.0type="inter-area-prefix"originator=10.12.0.12id=192.168.8.0sequence=0x80000009age=4checksum=0xF856body=netmask=255.255.255.0metric=1162D instance=ospf-instance-1area=10.12.0.0type="inter-area-prefix"originator=10.12.0.13id=192.168.8.0sequence=0x80000009age=6checksum=0x1B2Fbody=netmask=255.255.255.0metric=1203D instance=ospf-instance-1area=0.0.0.0type="inter-area-prefix"originator=10.8.0.100id=192.168.8.0sequence=0x80000009age=6checksum=0xC0A2body=netmask=255.255.255.0metric=10 ``` Set value for COST, for example as bellow:
```
Thanks, but no suprise.After setup the ABR area range cost. The intra-router's received lsa indeed change the cost of id=192.168.8.0, but the netmask is still 255.255.255.0, no expected 255.255.252.0
```