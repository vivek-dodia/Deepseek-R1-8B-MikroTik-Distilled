# Thread Information
Title: Thread-1121345
Section: RouterOS
Thread ID: 1121345

# Discussion

## Initial Question
Hi, I'm stuck with finding why my router RB750Gr3 (7.16.1) is sending DHCPDISCOVER all the time.I noticed that there is a constant flow on DHCPDISCOVER with source address of ether2 interface on that interfaceI have bridge with vlan filtering and multiple vlans on this interface.There is no dhcp-client set on that interface, and this is inded router sending those packages since hostname in that packet matches my router hostname.What is going on ?It looks like this:
```
3time=1.025num=4direction=tx src-mac=CC:2D:E0:07:84:E1 dst-mac=FF:FF:FF:FF:FF:FF vlan=73interface=ether2 src-address=0.0.0.0:68(bootpc)dst-address=255.255.255.255:67(bootps)protocol=ip ip-protocol=udp size=346cpu=3ip-packet-size=328ip-header-size=20dscp=0identification=0fragment-offset=0ttl=164time=1.046num=5direction=tx src-mac=CC:2D:E0:07:84:E1 dst-mac=FF:FF:FF:FF:FF:FF vlan=74interface=ether2 src-address=0.0.0.0:68(bootpc)dst-address=255.255.255.255:67(bootps)protocol=ip ip-protocol=udp size=346cpu=3ip-packet-size=328ip-header-size=20dscp=0identification=0fragment-offset=0ttl=165time=1.056num=6direction=tx src-mac=CC:2D:E0:07:84:E1 dst-mac=FF:FF:FF:FF:FF:FF vlan=302interface=ether2 src-address=0.0.0.0:68(bootpc)dst-address=255.255.255.255:67(bootps)protocol=ip ip-protocol=udp size=346cpu=3ip-packet-size=328ip-header-size=20dscp=0identification=0fragment-offset=0ttl=166time=1.077num=7direction=tx src-mac=CC:2D:E0:07:84:E1 dst-mac=FF:FF:FF:FF:FF:FF vlan=71interface=ether2 src-address=0.0.0.0:68(bootpc)dst-address=255.255.255.255:67(bootps)protocol=ip ip-protocol=udp size=346cpu=3ip-packet-size=328ip-header-size=20dscp=0identification=0fragment-offset=0ttl=167time=1.077num=8direction=tx src-mac=CC:2D:E0:07:84:E1 dst-mac=FF:FF:FF:FF:FF:FF vlan=70interface=ether2 src-address=0.0.0.0:68(bootpc)dst-address=255.255.255.255:67(bootps)protocol=ip ip-protocol=udp size=346cpu=3ip-packet-size=328ip-header-size=20dscp=0identification=0fragment-offset=0ttl=16

---
```

## Response 1
There's service "detect internet" which in theory helps to set router correctly for people who don't fiddle with manual settings (too much), but has potential to screw things up ... One of mechanizms is using DHCP client procedures even on interfaces where DHCP client is not configured.So check settings under/interface/detect-internet. My recommendation is to disable the functionality altogether if you configured LAN and WAN manually because detect internet can still interfere. You can do it by setting all interface lists tonone. ---

## Response 2
Spot on !That was it. I never heard about that feature.Thanks! ---