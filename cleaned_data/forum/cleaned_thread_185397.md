# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 185397

# Discussion

## Initial Question
Author: Sat Apr 23, 2022 11:03 pm
``` $ sudo ../netinstall -a 192.168.88.20 routeros-mmips-6.48.6.npk Using server IP: 192.168.88.10 Starting PXE server Waiting for RouterBOARD... PXE client: 08:55:31:4C:B7:5C PXE client: 08:55:31:4C:B7:5C PXE client: 08:55:31:4C:B7:5C ``` Well, I'm not sure if the device is bricked.Actually, I don't think so because I can dothis, means I can load OpemWRT's initramfs.Using netinstall I get this:
```
This means, the client is identified, but netinstall fails to load the the *.npk package.


---
```

## Response 1
Author: Sun Apr 24, 2022 2:48 pm
``` $ sudo dnsmasq -dd -C /etc/dnsmasq.conf dnsmasq: gestartet, Version 2.86, DNS abgeschaltet dnsmasq: Optionen bei Übersetzung: IPv6 GNU-getopt DBus no-UBus i18n IDN2 DHCP DHCPv6 no-Lua TFTP conntrack ipset auth cryptohash DNSSEC loop-detect inotify dumpfile dnsmasq-dhcp: DHCP, IP-Bereich 192.168.88.20 -- 192.168.88.100, Leasezeit 1d dnsmasq-dhcp: 245898967 verfügbarer DHCP-Bereich: 192.168.88.20 - 192.168.88.100 dnsmasq-dhcp: 245898967 "Vendor class": MMipsBoot dnsmasq-dhcp: 245898967 Marken: bootp, known, enp5s0 dnsmasq-dhcp: 245898967 BOOTP(enp5s0) 192.168.88.20 08:55:31:4c:b7:5c dnsmasq-dhcp: 245898967 nächster Server: 192.168.88.10 dnsmasq-dhcp: 245898967 sent size: 4 option: 1 netmask 255.255.255.0 dnsmasq-dhcp: 245898967 sent size: 4 option: 28 broadcast 192.168.88.255 dnsmasq-dhcp: 245898967 sent size: 4 option: 3 router 192.168.88.10 dnsmasq-dhcp: 245898967 sent size: 6 option: 12 hostname iptime ``` ``` $ sudo ./netinstall -a 192.168.88.20 routeros-mmips-6.48.6.npk Using server IP: 192.168.88.10 Starting PXE server Waiting for RouterBOARD... bind bootp failed: Address already in use ``` I guess the issue is that router expects DHCP.There's a similar issuehere.So, I configured a DHCP server on my ethernet port connected to router's ethernet port 1.The log of DHCP server shows:
```
Starting netinstall fails with error:
```

```
Any idea how to fix this?
```