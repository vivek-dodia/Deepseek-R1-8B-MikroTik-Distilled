# Document Information
Title: GRE
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/24805531/GRE,

# Content
# Introduction
Sub-menu:/interface greStandards:RFC1701
```
/interface gre
```
GRE (Generic Routing Encapsulation) is a tunneling protocol that was originally developed by Cisco. It can encapsulate a wide variety of protocols creating a virtual point-to-point link.
GRE is the same asIPIPandEoIPwhich were originally developed as stateless tunnels. This means that if the remote end of the tunnel goes down, all traffic that was routed over the tunnels will get blackholed. To solve this problem, RouterOS has added a 'keepalive' feature for GRE tunnels.
# Properties
Property | Description
----------------------
allow-fast-path(yes | no; Default:yes) | Whether to allow FastPath processing. Must be disabled if IPsec tunneling is used.
clamp-tcp-mss(yes | no; Default:yes) | Controls whether to change MSS size for received TCP SYN packets. When enabled, a router will change the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet will still contain the original MSS, and only after decapsulation the MSS is changed.
comment(string; Default: ) | Short description of the tunnel.
disabled(yes | no; Default:no) | Enables/disables tunnel.
dont-fragment(inherit | no; Default:no) | Whether to include DF bit in related packets:no- fragment if needed,inherit- use Dont Fragment flag of original packet.(Without Dont Fragment: inherit - packet may be fragmented).
dscp(inherit | integer [0-63]; Default: ) | Set dscp value in Gre header to a fixed value or inherit from dscp value taken from tunnelled traffic
ipsec-secret(string; Default: ) | When secret is specified, router adds dynamic IPsec peer to remote-address with pre-shared key and policy (by default phase2 uses sha1/aes128cbc).
keepalive(integer[/time],integer 0..4294967295; Default:10s,10) | Tunnel keepalive parameter sets the time interval in which the tunnel running flag will remain even if the remote end of tunnel goes down. If configured time,retries fail, interface running flag is removed. Parameters are written in following format:KeepaliveInterval,KeepaliveRetrieswhere KeepaliveInterval is time interval and KeepaliveRetries - number of retry attempts. By default keepalive is set to 10 seconds and 10 retries.
l2mtu(integer [0..65536]; Default:65535) | Layer2 Maximum transmission unit.
local-address(IP; Default:0.0.0.0) | IP address that will be used for local tunnel end. If set to 0.0.0.0 then IP address of outgoing interface will be used.
mtu(integer [0..65536]; Default:1476) | Layer3 Maximum transmission unit.
name(string; Default: ) | Name of the tunnel.
remote-address(IP; Default: ) | IP address of remote tunnel end.
Whether to include DF bit in related packets:
no- fragment if needed,inherit- use Dont Fragment flag of original packet.
(Without Dont Fragment: inherit - packet may be fragmented).
```
KeepaliveInterval,KeepaliveRetries
```
# Setup example
The goal of this example is to get Layer 3 connectivity between two remote sites over the internet
We have two sites,Site1with local network range 10.1.101.0/24 andSite2with local network range 10.1.202.0/24.
The first step is to create GRE tunnels. A router on site 1:
```
/interface gre add name=myGre remote-address=192.168.90.1 local-address=192.168.80.1
```
A router on site 2:
```
/interface gre add name=myGre remote-address=192.168.80.1 local-address=192.168.90.1
```
As you can see tunnel configuration is quite simple.
Now we just need to set up tunnel addresses and proper routing. A router on site 1:
```
/ip address add address=172.16.1.1/30 interface=myGre
/ip route add dst-address=10.1.202.0/24 gateway=172.16.1.2
```
A router on site 2:
```
/ip address add address=172.16.1.2/30 interface=myGre
/ip route add dst-address=10.1.101.0/24 gateway=172.16.1.1
```
At this point, both sites have Layer 3 connectivity over the GRE tunnel.