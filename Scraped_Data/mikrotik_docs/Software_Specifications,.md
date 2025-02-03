---
title: Software Specifications
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/19136707/Software+Specifications,
crawled_date: 2025-02-02T21:08:32.284173
section: mikrotik_docs
type: documentation
---

* 1Hardware Support
* 2Installation
* 3Configuration
* 4Backup/Restore
* 5Firewall
* 6Routing
* 7MPLS
* 8VPN
* 9Wireless
* 10DHCP
* 11Hotspot
* 12QoS
* 13Proxy
* 14Tools
* 15Other features
* 16Kernel version
* 17Supported Encryptions
### Hardware Support
MikroTik made devices:RouterOS is  compatible with MikroTik hardware it comes preinstalled on. Even MikroTik devices that are no longer manufactured, can run the latest RouterOS versions and will receive software updates. There are a few exceptions to this for the very oldest product lines.The latest RouterOS v7 is not compatible with all MIPS-LE family of devices (such as RB100, series, some RB700 series devices etc. please check the architecture of the device in question). It is also not compatible with MikroTik devices that have 32MB of RAM or less, but a minimum of 64MB is suggested. In short, there is no set limit on software compatibility or upgrades. Even devices that are no longer manufactured for 20 years, will still receive software updates, as long as they have enough RAM and are not based on a MIPS-LE CPU.
3rd party devices:RouterOS can also be run on 3rd party devices if they meet the following requirements:
* x86 or AMPERE powered ARM CPU
* Minimum 64MB of RAM
* IDE, SATA, USB, and flash storage medium with a minimum of 64MB of space
* Network cards supported by Linux kernel
### Installation
* Netinstall: Full network-based installation from PXE or EtherBoot enabled network card
* CHR: RouterOS version intended for running as a virtual machine
* CD-based installation
### Configuration
* MAC-based access for initial configuration
* WinBox – standalone Windows GUI configuration tool
* Webfig - advanced web-based configuration interface
* MikroTik - Android and iOS-based configuration tool
* Powerful command-line configuration interface with integrated scripting capabilities, accessible via local terminal, serial console, telnet and ssh
* API - the way to create your own configuration and monitoring applications
### Backup/Restore
* Binary configuration backup saving and loading
* Configuration export and import in human-readable text format
### Firewall
* Stateful filtering
* Source and destination NAT
* NAT helpers (h323, pptp, quake3, sip, ftp, irc, tftp)
* Internal connection, routing and packet marks
* Filtering by IP address and address range, port and port range, IP protocol, DSCP and many more
* Address lists
* Custom Layer7 matcher
* IPv6 support
* PCC - per connection classifier, used in load balancing configurations
* RAW filtering to bypass connection tracking.
### Routing
* Static routing
* Virtual Routing and Forwarding (VRF)
* Policy based routing
* Interface routing
* ECMP routing
* IPv4 dynamic routing protocols: RIP v1/v2, OSPFv2, BGP v4
* IPv6 dynamic routing protocols: RIPng, OSPFv3, BGP
* Bidirectional Forwarding Detection (BFD)
### MPLS
* Static Label bindings for IPv4
* Label Distribution protocol for IPv4
* RSVP Traffic Engineering tunnels
* VPLS MP-BGP based autodiscovery and signaling
* MP-BGP based MPLS IP VPN
### VPN
* IPSec – tunnel and transport mode, certificate or PSK, AH and ESP security protocols.
* IKEv2 support
* AES-NI hardware acceleration support for IPSec
* Point to point tunneling ( OpenVPN, PPTP, PPPoE, L2TP, SSTP)
* Advanced PPP features (MLPPP, BCP)
* BCP supported on sstp, ppp, pptp, l2tp and pppoe
* Simple tunnels ( IPIP, EoIP) IPv4 andIPv6 support
* 6to4 tunnel support (IPv6 over IPv4 network)
* VLAN – IEEE802.1q Virtual LAN support, Q-in-Q support
* MPLS based VPNs
* WireGuard
* ZeroTier
### Wireless
* IEEE802.11a/b/g wireless client and access point
* Full IEEE802.11n support
* Nstreme and Nstreme2 proprietary protocols
* NV2 protocol
* Wireless Distribution System (WDS)
* Virtual AP
* WEP, WPA, WPA2
* Access control list
* Wireless client roaming
* WMM
* HWMP+ Wireless MESH protocol
* MME wireless routing protocol
### DHCP
* Per interface DHCP server
* DHCP client and relay
* Static and dynamic DHCP leases
* RADIUS support
* Custom DHCP options
* DHCPv6 Prefix Delegation (DHCPv6-PD)
* DHCPv6 Client
### Hotspot
* Plug-n-Play access to the Network
* Authentication of local Network Clients
* Users Accounting
* RADIUS support for Authentication and Accounting
### QoS
* Hierarchical Token Bucket ( HTB) QoS system with CIR, MIR, burst and priority support
* Simple and fast solution for basic QoS implementation - Simple queues
* Dynamic client rate equalization ( PCQ)
### Proxy
* HTTP caching proxy server
* Transparent HTTP proxy
* SOCKS protocol support
* DNS static entries
* Support for caching on a separate drive
* Parent proxy support
* Access control list
* Caching list
### Tools
* Ping, traceroute
* Bandwidth test, ping flood
* Packet sniffer, torch
* Telnet, ssh
* E-mail and SMS send tools
* Automated script execution tools
* CALEA
* File Fetch tool
* Advanced traffic generator
* WoL (Wake on LAN) sending
### Other features
* Samba support
* OpenFlow support
* Bridging – spanning tree protocol (STP, RSTP), bridge firewall and MAC natting.
* Dynamic DNS update tool
* NTP client/server and synchronization with GPS system
* VRRP v2 and v3 support
* SNMP
* M3P - MikroTik Packet packer protocol for wireless links and ethernet
* MNDP - MikroTik neighbor discovery protocol, supports CDP (Cisco discovery protocol)
* RADIUS authentication and accounting
* TFTP server
* Synchronous interface support (Farsync cards only) (Removed in v5.x)
* Asynchronous – serial PPP dial-in/dial-out, dial on demand
* ISDN – dial-in/dial-out, 128K bundle support, Cisco HDLC, x75i, x75ui, x75bui line protocols, dial on demand
### Kernel version
* RouterOS version 6.x uses 3.3.5
* RouterOS version 7.x uses 5.6.3
### Supported Encryptions
RouterOS 7 is used for the management of network (telecommunication) devices.
* RouterOS 7 includes encryption features (components), intended for data (information) security, passed through telecommunication channels and device control channels.
* All encryption features (components) are an integral part of RouterOS 7 and can not be changed by the end-users.
* RouterOS 7 is intended for installation by end-users without significant support from the vendor.
* RouterOS 7 uses the following security protocols:
RouterOS 7 includes encryption features (components), intended for data (information) security, passed through telecommunication channels and device control channels.
All encryption features (components) are an integral part of RouterOS 7 and can not be changed by the end-users.
RouterOS 7 is intended for installation by end-users without significant support from the vendor.
RouterOS 7 uses the following security protocols:
Supported security protocol | Encryption algorithm | Maximum key length
-----------------------------------------------------------------------
IPSec | DES | 56 bit
3DES | 168 bit
AES | 128, 192, 256 bit
Blowfish | 448 bit
Twofish | 256 bit
Camelia | 128, 192, 256 bit
PPTP (with MPPE) | RC4 | 128 bit
L2TP (with MPPE) | RC4 | 128 bit
SNMP | DES | 56 bit
AES | 128 bit
SSH | Blowfish | 128 bit
3DES | 192 bit
AES | 128, 192, 256 bit
SSTP | AES | 256 bit
RC4 | 128 bit
Used in WinBox connection (nameless) | AES | 128 bit
WEP | RC4 | 104 bit
WPA-TKIP | RC4 | 128 bit
WPA2-TKIP | RC4 | 128 bit
WPA-AES | AES | 128 bit
WPA2-AES | AES | 128 bit
HTTPS | NULL, RC4, DES, DES40, 3DES, AES | 128, 192, 256 bit
IPSec
SSH
SSTP