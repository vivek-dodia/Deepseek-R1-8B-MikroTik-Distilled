# Document Information
Title: Profiler
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/8323153/Profiler,

# Content
# Summary
The profiler tool shows CPU usage for each process running in RouterOS. It helps to identify which process is using most of the CPU resources.Watch ourvideo about this feature.
```
[admin@MikroTik] > /tool/profile
```
On multi-core systems, the tool allows specifying per core CPU usage.
"CPU" parameter allows specifying integer number which represents a core or two of predefined valuesallandtotal:
In the following example we will take a look at both predefined values:
```
[admin@MikroTik] > /tool/profile cpu=all
NAME             CPU        USAGE
ethernet         1          0%
kvm              0          0%
kvm              1          4.5%
management       0          0%
management       1          0.5%
idle             0          100%
idle             1          93%
profiling        0          0%
profiling        1          2%
[admin@MikroTik] > /tool profile cpu=total
NAME             CPU        USAGE
ethernet         all        0%
console          all        0%
kvm              all        2.7%
management       all        0%
idle             all        97.2%
profiling        all        0%
bridging         all        0%
```
# Classifiers
RouterOS processes are classified by type and the CPU usage for each type is displayed separately for ease of debugging.
Property | Description
----------------------
backup | Backup service
bfd | BFD service
bgp | BGP service
bridging | Bridging service
btest | Bandwidth test.
certificate | Certificate service
console | Console
container | combined container usage
dhcp | DHCP-Server and DHCP-Client services
disk | storage-related services
dns | DNS-related services
dude | The Dude package services
e-mail | e-mail tool
encrypting | encrypting processes
eoip | EoIP
ethernet | Ethernet-related properties like link speed, auto-negotiation, duplex mode, monitor a transceiver diagnostic information, etc.
fetcher | Fetch tool
firewall | Firewall-related processes
firewall-mgmt | Firewall Management: Filtering, NAT, Mangle
flash | storage-related services
ftp | FTP Service
gps | GPS Service
graphing | Graphing tool
gre | GRE
health | system monitoring, workd health
hotspot | Hotspot service
idle | Free CPU resources
igmp-proxy | IGMP Proxy service
internet-detect | Detect Internet tool
ip-pool | IP Pool service
ipsec | IPsec service:xfrm -  set of statistics showing numbers of packets dropped by the transformation code and why.drivers/crypto - drivers that provide access to the hardware cryptographic accelerators.ipsec - processes that relate to the Internet Key Exchange (IKE) protocols, Authentication Header (AH), Encapsulating Security Payload (ESP).
kvm | KVM virtual machine functionality
l7-matcher | L7 matcher
lcd | LCD Interfaces system
ldp | Label Distribution Protocol (LDP)
logging | Logging system
management | different subsystems: scheduler, networking, file management, etc.
mpls | MPLS-related features
neighbour-discovery | Neighbour discovery service
networking | common set of services included in the networking
ntp | NTP service
ospf | OSPF service
ovpn | OVPN service
pim | Protocol Independent Multicast
profiling | Profiler service
queue-mgmt | Queues: Simple queues, Queue tree, Queue types
queuing | Intermediate Queuing
radius | RADIUS service
radv | IPv6 radv daemon log messages service
remote-access | accessing the device directly without logging into RouterOS
rip | Routing Information Protocol
routing | Routing-related services
serial | serial console and terminal tool
sniffing | packet Sniffer tool
snmp | SNMP
socks | Socket Secure
spi | storage-related services
ssh | SSH Server
ssl | SSL
supout.rif | supout.rif file generation
telnet | Telnet service
tftp | TFTP service
traffic-accounting | Traffic-Flow log system
traffic-flow | Traffic-Flow system
unclassified | processes or services that are not defined by this classifier
upnp | UPnP protocol
usb | USB features
user-manager | User Manager service
vrrp | VRRP
web-proxy | Web Proxy
winbox | Winbox
wireguard | Wireguard
wireless | common set of services using Wireless systems
www | Webfig HTTP service
zerotier | ZeroTier
IPsec service:xfrm -  set of statistics showing numbers of packets dropped by the transformation code and why.drivers/crypto - drivers that provide access to the hardware cryptographic accelerators.ipsec - processes that relate to the Internet Key Exchange (IKE) protocols, Authentication Header (AH), Encapsulating Security Payload (ESP).