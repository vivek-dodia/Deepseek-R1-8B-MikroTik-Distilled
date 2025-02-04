# Document Information
Title: Services
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/103841820/Services,

# Content
# Summary
This page lists protocols and ports used by various MikroTik RouterOS services. It helps you to determine why your MikroTik router listens to certain ports, and what you need to block/allow in case you want to prevent or grant access to certain services. Please see the relevant sections of the Manual for more explanations.
The default services are:
Property | Description
----------------------
telnet | Telnet service
ftp | FTP service
www | Webfig HTTP service
ssh | SSH service
www-ssl | Webfig HTTPS service
api | API service
winbox | Responsible for Winbox tool access, as well as Tik-App smartphone app and Dude probe
api-ssl | API over SSL service
# Properties
Note that it is not possible to add new services, only existing service modifications are allowed.
Sub-menu:/ip service
```
/ip service
```
Property | Description
----------------------
address(IP address/netmask | IPv6/0..128; Default:) | List of IP/IPv6 prefixes from which the service is accessible
certificate(name; Default:none) | The name of the certificate used by a particular service. Applicable only for services that depend on certificates (www-ssl, api-ssl)
name(name; Default:none) | Service name
max-sessions(integer: 1..1000; Default:20) | Max simultaneous session count for service
port(integer: 1..65535; Default:) | The port particular service listens on
tls-version(any|only-1.2; Default:any) | Specifies which TLS versions to allow by a particular service
vrf(name; Default:main) | Specify which VRF instance to use by a particular service
# Example
For example, allow API only from a specific IP/IPv6 address range
```
[admin@dzeltenais_burkaans] /ip service> set api address=10.5.101.0/24,2001:db8:fade::/64
[admin@dzeltenais_burkaans] /ip service> print
Flags: X - disabled, I - invalid
# NAME     PORT  ADDRESS                                       CERTIFICATE
0   telnet   23
1   ftp      21
2   www      80
3   ssh      22
4 X www-ssl  443                                                 none
5   api      8728  10.5.101.0/24
2001:db8:fade::/64
6   winbox   8291
```
# Protocols and ports
The table below shows the list of protocols and ports used by RouterOS.
Proto/Port | Description
------------------------
20/tcp | FTP data connection
21/tcp | FTP control connection
22/tcp | Secure Shell (SSH) remote login protocol
23/tcp | Telnet protocol
53/tcp53/udp | DNS
67/udp | Bootstrap protocol orDHCP Server
68/udp | Bootstrap protocol orDHCP Client
80/tcp | World Wide Web HTTP
123/udp | Network Time Protocol (NTP)
161/udp | Simple Network Management Protocol (SNMP)
179/tcp | Border Gateway Protocol (BGP)
443/tcp | Secure Socket Layer (SSL) encrypted HTTP
500/udp | Internet Key Exchange (IKE) protocol
520/udp521/udp | RIProuting protocol
546/udp | DHCPv6 Clientmessage
547/udp | DHCPv6 Servermessage
646/tcp | LDPtransport session
646/udp | LDPhello protocol
1080/tcp | SOCKSproxy protocol
1698/udp 1699/udp | RSVP TE Tunnels
1701/udp | Layer 2 Tunnel Protocol (L2TP)
1723/tcp | Point-To-Point Tunneling Protocol (PPTP)
1900/udp2828/tcp | Universal Plug and Play (uPnP)
1966/udp | MME originator message traffic
1966/tcp | MME gateway protocol
2000/tcp | Bandwidth test server
5246,5247/udp | CAPsMAN
5350/udp | NAT-PMP client
5351/udp | NAT-PMP server
5678/udp | Mikrotik Neighbor Discovery Protocol
6343/tcp | Default OpenFlow port
8080/tcp | HTTP Web Proxy
8291/tcp | Winbox
8728/tcp | API
8729/tcp | API-SSL
20561/udp | MAC winbox
/1 | ICMP
/2 | Multicast | IGMP
/4 | IPIPencapsulation
/41 | IPv6 (encapsulation)
/46 | RSVP TE tunnels
/47 | General Routing Encapsulation (GRE) - used forPPTPandEoIPtunnels
/50 | Encapsulating Security Payload for IPv4 (ESP)
/51 | Authentication Header for IPv4 (AH)
/89 | OSPFrouting protocol
/103 | Multicast | PIM
/112 | VRRP