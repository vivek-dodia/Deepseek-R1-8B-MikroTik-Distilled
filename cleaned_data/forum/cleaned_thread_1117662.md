# Thread Information
Title: Thread-1117662
Section: RouterOS
Thread ID: 1117662

# Discussion

## Initial Question
Hi guys, i have an RB493AH as my core router in my home, and from time to time, the switch chip ports seem to just cut the data stream away from the rest of the router with a port not on the switch chip, while still bridging betwen themselves, as they should. (local network works, but the router becomes inaccessible thru Winbox and ping. Only accessible thru the port not on the switch chip.) The problem is usually solved after restarting the router, sometimes requiring 2. I've noticed that the problem is less likely to happen with lower CPU frequency. Also, there is a slightly swollen capacitor, that hasn't been changed, unlike all of the other ones. Here's the config, and thanks for any replies.
```
# jan/05/2025 13:28:40 by RouterOS 6.49.15# software id = ZKR9-Y3HI## model = 493AH# serial number = XXXXXXXXXXXXX/interfacebridgeaddadmin-mac=00:0C:42:50:FA:09auto-mac=nofast-forward=noname=bridge1 protocol-mode=none/interfaceethernetset[finddefault-name=ether1]comment=WANset[finddefault-name=ether2]comment=Volnyset[finddefault-name=ether3]comment=Volnyset[finddefault-name=ether4]comment=Kotelnaset[finddefault-name=ether5]comment="AP Chodba"set[finddefault-name=ether6]comment="Ob\FDv\E1k"set[finddefault-name=ether7]comment=Pracovnaset[finddefault-name=ether8]comment="M\ED\9Aa"set[finddefault-name=ether9]comment=NVR/interfacevlanaddinterface=ether1 name=vlan848 vlan-id=848/interfacepppoe-clientaddadd-default-route=yes disabled=nointerface=vlan848 max-mru=1480max-mtu=1480name=\
    pppoe-out1use-peer-dns=yes user=cetin/interfacelistaddname=WANaddname=LAN/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTik/ip pooladdname=dhcp ranges=192.168.1.100-192.168.1.199/ip dhcp-serveraddaddress-pool=dhcp disabled=nointerface=bridge1 lease-time=12hname=dhcp1/ppp profileaddname=Isekremote-address=192.168.30.1/interfacepptp-clientaddconnect-to=85.163.230.102name="PPTP Isek"profile=Isekuser=admina/interfacebridge portaddbridge=bridge1interface=ether2addbridge=bridge1interface=ether3addbridge=bridge1interface=ether4addbridge=bridge1interface=ether5addbridge=bridge1interface=ether6addbridge=bridge1interface=ether7addbridge=bridge1interface=ether8addbridge=bridge1interface=ether9/ip firewall connection trackingsetenabled=yes/ip settingssettcp-syncookies=yes/interfacedetect-internetsetdetect-interface-list=all/interfacelist memberaddinterface=pppoe-out1 list=WANaddinterface=bridge1 list=LAN/ip addressaddaddress=192.168.1.1/24interface=bridge1 network=192.168.1.0/ip dhcp-server leaseaddaddress=192.168.1.23client-id=1:10:e7:c6:cd:a9:e9 mac-address=10:E7:C6:CD:A9:E9 \
    server=dhcp1addaddress=192.168.1.83client-id=1:88:c2:55:15:7:d mac-address=88:C2:55:15:07:0Dserver=\
    dhcp1addaddress=192.168.1.2client-id=1:0:c:42:a6:bf:4fmac-address=00:0C:42:A6:BF:4Fserver=\
    dhcp1addaddress=192.168.1.11client-id=1:d8:7:b6:a4:f4:a5 mac-address=D8:07:B6:A4:F4:A5 server=\
    dhcp1addaddress=192.168.1.32mac-address=58:BF:25:4D:28:D9 server=dhcp1addaddress=192.168.1.42client-id=1:e0:98:6:10:6a:58mac-address=E0:98:06:10:6A:58server=\
    dhcp1addaddress=192.168.1.51client-id=1:ec:5c:84:44:81:54mac-address=EC:5C:84:44:81:54\
    server=dhcp1addaddress=192.168.1.85client-id=1:bc:df:58:51:f7:6mac-address=BC:DF:58:51:F7:06server=\
    dhcp1addaddress=192.168.1.21client-id=1:2c:f0:5d:80:f2:25mac-address=2C:F0:5D:80:F2:25\
    server=dhcp1addaddress=192.168.1.55client-id=1:f2:68:3c:9b:c:47mac-address=F2:68:3C:9B:0C:47server=\
    dhcp1addaddress=192.168.1.22client-id=1:f8:b1:56:d4:90:af mac-address=F8:B1:56:D4:90:AF \
    server=dhcp1addaddress=192.168.1.31mac-address=00:A2:FF:01:80:D3 server=dhcp1addaddress=192.168.1.7client-id=1:0:c:42:58:a2:2amac-address=00:0C:42:58:A2:2Aserver=\
    dhcp1addaddress=192.168.1.12mac-address=3C:E3:6B:E1:24:B5 server=dhcp1addaddress=192.168.1.13mac-address=3C:E3:6B:E1:24:66server=dhcp1addaddress=192.168.1.5client-id=1:0:c:42:32:cd:86mac-address=00:0C:42:32:CD:86server=\
    dhcp1addaddress=192.168.1.6client-id=1:0:c:42:ae:be:f2 mac-address=00:0C:42:AE:BE:F2 server=\
    dhcp1addaddress=192.168.1.4client-id=1:0:c:42:ae:bf:4mac-address=00:0C:42:AE:BF:04server=\
    dhcp1addaddress=192.168.1.82client-id=1:18:c8:e7:35:1e:14mac-address=18:C8:E7:35:1E:14\
    server=dhcp1addaddress=192.168.1.53client-id=1:8:c5:e1:8f:ef:fb mac-address=08:C5:E1:8F:EF:FB server=\
    dhcp1addaddress=192.168.1.52client-id=1:1c:b7:96:69:62:ac mac-address=1C:B7:96:69:62:AC \
    server=dhcp1addaddress=192.168.1.24client-id=1:74:70:fd:a2:e3:e7 mac-address=74:70:FD:A2:E3:E7 \
    server=dhcp1addaddress=192.168.1.86mac-address=34:00:8A:E3:2E:FA server=dhcp1addaddress=192.168.1.84client-id=1:1c:5a:6b:80:8a:5mac-address=1C:5A:6B:80:8A:05server=\
    dhcp1addaddress=192.168.1.14client-id=1:a8:31:62:28:e:5cmac-address=A8:31:62:28:0E:5Cserver=\
    dhcp1addaddress=192.168.1.56client-id=1:78:d6:dc:1b:86:47mac-address=78:D6:DC:1B:86:47\
    server=dhcp1addaddress=192.168.1.43client-id=1:48:3f:da:4e:6:41mac-address=48:3F:DA:4E:06:41server=\
    dhcp1addaddress=192.168.1.57client-id=1:80:f3:ef:92:5:6bmac-address=80:F3:EF:92:05:6Bserver=\
    dhcp1/ip dhcp-server networkaddaddress=192.168.1.0/24dns-server=192.168.1.1gateway=192.168.1.1netmask=24/ip dnssetallow-remote-requests=yes servers=160.218.161.54,195.113.144.194,1.1.1.1/ip firewall nataddaction=masquerade chain=srcnatout-interface=pppoe-out1 src-address=192.168.1.0/24/ip servicesetwww address=192.168.1.0/24setwinbox address=192.168.1.0/24/ip upnpsetallow-disable-external-interface=yes enabled=yes/ip upnp interfacesaddinterface=pppoe-out1 type=externaladdinterface=bridge1 type=internal/system clocksettime-zone-name=Europe/Prague/system identitysetname="The Matrix"/system routerboard settingssetcpu-frequency=400MHz/system watchdogsetping-timeout=10swatch-address=192.168.1.2/tool bandwidth-serversetenabled=no

---
```

## Response 1
I've noticed that the problem is less likely to happen with lower CPU frequency. Also, there is a slightly swollen capacitor, that hasn't been changed, unlike all of the other ones.If this wasn't happening before, the chance that the "swollen" capacitor is related are quite high, especially since you mention relationship to CPU frequency - the higher the CPU frequency the higher the current consumption. I suppose that since you've replaced the onboard capacitors, you have also replaced the original power source (or retrofitted the capacitors inside it)?If it's not the capacitor(s), I'm afraid some silicon part has reached its end of life (I figure the board has been making you a company for more than ten years?), and you'll have to retire the board and use L009 (or 5009 if you don't like the red case). ---