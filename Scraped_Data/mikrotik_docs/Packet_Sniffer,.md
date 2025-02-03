---
title: Packet Sniffer
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/8323088/Packet+Sniffer,
crawled_date: 2025-02-02T21:15:02.348212
section: mikrotik_docs
type: documentation
---

* 1Introduction
* 2Packet Sniffer configuration2.1Packet Sniffer Quick Mode2.2Packet Sniffer Protocols2.3Packet Sniffer Host2.4Packet Sniffer Connections
* 2.1Packet Sniffer Quick Mode
* 2.2Packet Sniffer Protocols
* 2.3Packet Sniffer Host
* 2.4Packet Sniffer Connections
# Introduction
A packet sniffer is a tool that can capture and analyze packets that are going to, leaving, or going through the router. Packet sniffing is very useful when you diagnose networks or protect against security attacks over networks.
# Packet Sniffer configuration
RouterOS embedded sniffer allows you to capture packets based on various protocols.
In the following example, we will configure the sniffer to match packets going through the ether1 interface:
```
[admin@MikroTik] > /tool/sniffer/start interface=ether1           
[admin@MikroTik] > /tool/sniffer/stop                             
[admin@MikroTik] > /tool/sniffer/save file-name=/flash/test.pcap            
MikroTik] > file print where name~"test" 
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME        TYPE  SIZE  CREATION-TIME       
9  flash/test.pcap  file  3696  dec/04/2019 10:48:16
```
You can download captured packets from a file section. Then you can use apacket analyzer such asWiresharkto analyze a file:
If you are using packet streaming to PC and are using Wireshark, to ensure you are only viewing the streamed data, you will need to apply a filter that matches the port the sniffer is using, by default 37008 is used. In addition, we recommend usingfilter-stream=yes.
```
filter-stream=yes
```
Sub-menu:/tool sniffer
```
/tool sniffer
```
Property | Description
----------------------
file-limit(integer 10..4294967295[KiB]; Default:1000KiB) | File size limit. Sniffer will stop when a limit is reached.
file-name(string; Default:) | Name of the file where sniffed packets will be saved.
filter-cpu(integer; Default:) | CPU core used as a filter.
filter-ip-address(ip/mask[,ip/mask] (max 16 items); Default:) | Up to 16 IP addresses used as a filter.
filter-dst-ip-address(ip/mask[,ip/mask] (max 16 items); Default:) | Up to 16 IP destination addresses used as a filter.
filter-src-ip-address(ip/mask[,ip/mask] (max 16 items); Default:) | Up to 16 IP source addresses used as a filter.
filter-ipv6-address(ipv6/mask[,ipv6/mask] (max 16 items); Default:) | Up to 16 IPv6 addresses used as a filter.
filter-dst-ipv6-address(ipv6/mask[,ipv6/mask] (max 16 items); Default:) | Up to 16 IPv6 destination addresses used as a filter.
filter-src-ipv6-address(ipv6/mask[,ipv6/mask] (max 16 items); Default:) | Up to 16 IPv6 source addresses used as a filter.
filter-mac-address(mac/mask[,mac/mask] (max 16 items); Default:) | Up to 16 MAC addresses and MAC address masks used as a filter.
filter-dst-mac-address(mac/mask[,mac/mask] (max 16 items); Default:) | Up to 16 MAC destination addresses and MAC address masks used as a filter.
filter-src-mac-address(mac/mask[,mac/mask] (max 16 items); Default:) | Up to 16 MAC source addresses and MAC address masks used as a filter.
filter-port([!]port[,port] (max 16 items); Default:) | Up to 16 comma-separated ports used as a filter. A list of predefined port names is also available, like ssh and telnet.
filter-dst-port([!]port[,port] (max 16 items); Default:) | Up to 16 comma-separated destination ports used as a filter. A list of predefined port names is also available, like ssh and telnet.
filter-src-port([!]port[,port] (max 16 items); Default:) | Up to 16 comma-separated source ports used as a filter. A list of predefined port names is also available, like ssh and telnet.
filter-ip-protocol([!]protocol[,protocol] (max 16 items); Default:) | Up to 16 comma-separated IP/IPv6 protocols used as a filter. IP protocols (instead of protocol names, protocol numbers can be used):ipsec-ah- IPsec AH protocolipsec-esp- IPsec ESP protocolddp- datagram delivery protocolegp- exterior gateway protocolggp- gateway-gateway protocolgre- general routing encapsulationhmp- host monitoring protocolidpr-cmtp- idpr control message transporticmp- internet control message protocolicmpv6- internet control message protocol v6igmp- internet group management protocolipencap- ip encapsulated in ipipip- ip encapsulationencap- ip encapsulationiso-tp4- iso transport protocol class 4ospf- open shortest path firstpup- parc universal packet protocolpim- protocol independent multicastrspf- radio shortest path firstrdp- reliable datagram protocolst- st datagram modetcp- transmission control protocoludp- user datagram protocolvmtp- versatile message transportvrrp- virtual router redundancy protocolxns-idp- xerox xns idpxtp- xpress transfer protocol
filter-mac-protocol([!]protocol[,protocol] (max 16 items); Default:) | Up to 16 comma separated entries used as a filter. Mac protocols (instead of protocol names, protocol number can be used):802.2- 802.2 Frames (0x0004)arp- Address Resolution Protocol (0x0806)capsman- CAPsMAN to CAP MAC layer connection (0x88BB)dot1x- EAPoL IEEE 802.1X (0x888E)homeplug-av- HomePlug AV MME (0x88E1)ip- Internet Protocol version 4 (0x0800)ipv6- Internet Protocol Version 6 (0x86DD)ipx- Internetwork Packet Exchange (0x8137)lacp- Link Aggregation Control Protocol (0x8809)lldp- Link Layer Discovery Protocol (0x88CC)loop-protect- Loop Protect Protocol (0x9003)macsec- MAC security IEEE 802.1AE (0x88E5)mpls-multicast- MPLS multicast (0x8848)mpls-unicast- MPLS unicast (0x8847)packing-compr- Encapsulated packets with compressedIP packing(0x9001)packing-simple- Encapsulated packets with simpleIP packing(0x9000)pppoe- PPPoE Session Stage (0x8864)pppoe-discovery- PPPoE Discovery Stage (0x8863)rarp- Reverse Address Resolution Protocol (0x8035)romon- Router Management Overlay Network RoMON (0x88BF)service-vlan- Provider Bridging (IEEE 802.1ad) & Shortest Path Bridging IEEE 802.1aq (0x88A8)vlan- VLAN-tagged frame (IEEE 802.1Q) and Shortest Path Bridging IEEE 802.1aq with NNI compatibility (0x8100)
filter-stream(yes | no; Default:yes) | Sniffed packets that are devised for the sniffer server are ignored.
filter-size(integer[-integer]:0..65535; Default: ) | Filters packets of specified size or size range in bytes.
filter-direction(any | rx | tx; Default:) | Specifies which direction filtering will be applied.
filter-interface(all | name; Default:all) | Interface name on which sniffer will be running.allindicates that the sniffer will sniff packets on all interfaces.
filter-operator-between-entries(and | or; Default:or) | Changes the logic for filters with multiple entries.
filter-vlan(integer[,integer]:0..4095; Default:) | Up to 16 VLAN IDs used as a filter.
memory-limit(integer 10..4294967295[KiB]; Default:100KiB) | Memory amount used to store sniffed data.
memory-scroll(yes | no; Default:yes) | Whether to rewrite older sniffed data when the memory limit is reached.
only-headers(yes | no; Default:no) | Save in the memory only the packet's headers, not the whole packet.
show-frame (yes | no; Default:no) | Whether to see the content of the frame when running quick sniffer in command line.
streaming-enabled(yes | no; Default:no) | Defines whether to send sniffed packets to the streaming server.
streaming-server(IP; Default:0.0.0.0) | Tazmen Sniffer Protocol (TZSP) stream receiver.
Up to 16 IP destination addresses used as a filter.
Up to 16 IP source addresses used as a filter.
* ipsec-ah- IPsec AH protocol
* ipsec-esp- IPsec ESP protocol
* ddp- datagram delivery protocol
* egp- exterior gateway protocol
* ggp- gateway-gateway protocol
* gre- general routing encapsulation
* hmp- host monitoring protocol
* idpr-cmtp- idpr control message transport
* icmp- internet control message protocol
* icmpv6- internet control message protocol v6
* igmp- internet group management protocol
* ipencap- ip encapsulated in ip
* ipip- ip encapsulation
* encap- ip encapsulation
* iso-tp4- iso transport protocol class 4
* ospf- open shortest path first
* pup- parc universal packet protocol
* pim- protocol independent multicast
* rspf- radio shortest path first
* rdp- reliable datagram protocol
* st- st datagram mode
* tcp- transmission control protocol
* udp- user datagram protocol
* vmtp- versatile message transport
* vrrp- virtual router redundancy protocol
* xns-idp- xerox xns idp
* xtp- xpress transfer protocol
* 802.2- 802.2 Frames (0x0004)
* arp- Address Resolution Protocol (0x0806)
* capsman- CAPsMAN to CAP MAC layer connection (0x88BB)
* dot1x- EAPoL IEEE 802.1X (0x888E)
* homeplug-av- HomePlug AV MME (0x88E1)
* ip- Internet Protocol version 4 (0x0800)
* ipv6- Internet Protocol Version 6 (0x86DD)
* ipx- Internetwork Packet Exchange (0x8137)
* lacp- Link Aggregation Control Protocol (0x8809)
* lldp- Link Layer Discovery Protocol (0x88CC)
* loop-protect- Loop Protect Protocol (0x9003)
* macsec- MAC security IEEE 802.1AE (0x88E5)
* mpls-multicast- MPLS multicast (0x8848)
* mpls-unicast- MPLS unicast (0x8847)
* packing-compr- Encapsulated packets with compressedIP packing(0x9001)
* packing-simple- Encapsulated packets with simpleIP packing(0x9000)
* pppoe- PPPoE Session Stage (0x8864)
* pppoe-discovery- PPPoE Discovery Stage (0x8863)
* rarp- Reverse Address Resolution Protocol (0x8035)
* romon- Router Management Overlay Network RoMON (0x88BF)
* service-vlan- Provider Bridging (IEEE 802.1ad) & Shortest Path Bridging IEEE 802.1aq (0x88A8)
* vlan- VLAN-tagged frame (IEEE 802.1Q) and Shortest Path Bridging IEEE 802.1aq with NNI compatibility (0x8100)
## Packet Sniffer Quick Mode
The quick mode will display results as they are filtered out with a limited-size buffer for packets. There are several attributes that can be set up for filtering. If no attributes are set current configuration will be used.
```
[admin@MikroTik] > /tool/sniffer/quick ip-protocol=icmp
Columns: INTERFace, TIME, NUm, DIr, SRC-MAC, DST-MAC, SRC-ADDRESS, DST-ADDRESS, PROTOCOl, SIze, Cpu, FP
INTERF  TIME    NU  DI  SRC-MAC            DST-MAC            SRC-ADDRESS     DST-ADDRESS     PROTOCO  SI  C  FP
ether7  35.472  79  <-  6C:3B:6B:ED:83:69  6C:3B:6B:ED:81:83  10.155.126.252  10.155.126.253  ip:icmp  70  7  no
ether7  35.472  80  ->  6C:3B:6B:ED:81:83  6C:3B:6B:ED:83:69  10.155.126.253  10.155.126.252  ip:icmp  70  7  no
ether1  35.595  81  <-  6C:3B:6B:ED:83:63  6C:3B:6B:ED:81:7D  172.24.24.2     172.24.24.1     ip:icmp  70  4  no
ether1  35.595  82  ->  6C:3B:6B:ED:81:7D  6C:3B:6B:ED:83:63  172.24.24.1     172.24.24.2     ip:icmp  70  4  no
ether7  36.457  83  <-  6C:3B:6B:ED:83:69  6C:3B:6B:ED:81:83  10.155.126.252  10.155.126.253  ip:icmp  70  7  no
ether7  36.457  84  ->  6C:3B:6B:ED:81:83  6C:3B:6B:ED:83:69  10.155.126.253  10.155.126.252  ip:icmp  70  7  no
ether1  36.6    85  <-  6C:3B:6B:ED:83:63  6C:3B:6B:ED:81:7D  172.24.24.2     172.24.24.1     ip:icmp  70  4  no
ether1  36.6    86  ->  6C:3B:6B:ED:81:7D  6C:3B:6B:ED:83:63  172.24.24.1     172.24.24.2     ip:icmp  70  4  no
```
## Packet Sniffer Protocols
In this submenu, you can see all sniffed protocols and their share of the whole sniffed amount.
```
[admin@MikroTik] /tool sniffer protocol> print 
 # PROTOCOL IP-PROTOCOL PORT                                     PACKETS      BYTES        SHARE
 0 802.2                                                              1         60        0.05%
 1 ip                                                               215     100377       99.04%
 2 arp                                                                2        120        0.11%
 3 ipv6                                                               6        788        0.77%
 4 ip       tcp                                                     210      99981       98.65%
 5 ip       udp                                                       3        228        0.22%
 6 ip       ospf                                                      2        168        0.16%
 7 ip       tcp         8291 (winbox)                               210      99981       98.65%
 8 ip       tcp         36771                                       210      99981       98.65%
 9 ip       udp         646                                           3        228        0.22%
```
## Packet Sniffer Host
The submenu shows the list of hosts that were participating in the data exchange you've sniffed.
```
[admin@MikroTik] /tool sniffer host> print 
 # ADDRESS         RATE                PEEK-RATE           TOTAL            
 0 10.5.101.3      0bps/0bps           0bps/720bps         0/90             
 1 10.5.101.10     0bps/0bps           175.0kbps/19.7kbps  61231/7011       
 2 10.5.101.13     0bps/0bps           0bps/608bps         0/76             
 3 10.5.101.14     0bps/0bps           0bps/976bps         0/212            
 4 10.5.101.15     0bps/0bps           19.7kbps/175.0kbps  7011/61231       
 5 224.0.0.2       0bps/0bps           608bps/0bps         76/0             
 6 224.0.0.5       0bps/0bps           1440bps/0bps        302/0
```
## Packet Sniffer Connections
Here you can get a list of the connections that have been watched during the sniffing time.
```
[admin@MikroTik] tool sniffer connection> print
Flags: A - active
  #   SRC-ADDRESS       DST-ADDRESS             BYTES     RESENDS   MSS
  0 A 10.0.0.241:1839   10.0.0.181:23 (telnet)  6/42      60/0      0/0
  1 A 10.0.0.144:2265   10.0.0.181:22 (ssh)     504/252   504/0     0/0
```