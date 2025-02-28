# Document Information
Title: 6to4
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/135004174/6to4,

# Content
# Summary
Sub-menu:/interface 6to4
```
/interface 6to4
```
6to4 is a special mechanism that allows IPv6 packets to be transmitted over IPv4 networks without the need of explicitly configured tunnel interfaces. It is especially useful for connecting two or more IPv6 networks over a network that does not have IPv6 support. There are two different ways of 6to4 mechanism. Ifremote-addressis not configured, the router will encapsulate and send an IPv6 packet directly over IPv4 if the first 16 bits are2002, using the next 32 bits as the destination (IPv4 address converted to hex). In other case, the IPv6 packet will be sent directly to the IPv4remote-address.
# Property Description
Property | Description
----------------------
clamp-tcp-mss(yes | no; Default:yes) | Controls whether to change MSS size for received TCP SYN packets. When enabled, a router will change the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet will still contain the original MSS, and only after decapsulation the MSS is changed.
comment(string; Default: ) | Short description of the interface.
disabled(yes | no; Default:no) | Whether an item is disabled.
dont-fragment(inherit | no; Default:no) | Whether to include DF bit in related packets:no- fragment if needed,inherit- use Dont Fragment flag of original packet.(Without Dont Fragment: inherit - packet may be fragmented).
dscp(integer: 0-63; Default:inherited) | DSCP value of packet. Inherited option means that DSCP value will be inherited from packet which is going to be encapsulated.
ipsec-secret(string; Default: ) | When secret is specified, router adds dynamic IPsec peer to remote-address with pre-shared key and policy (by default phase2 uses sha1/aes128cbc).
keepalive(integer[/time],integer 0..4294967295; Default:0,0) | Tunnel keepalive parameter sets the time interval in which the tunnel running flag will remain even if the remote end of tunnel goes down. If configured time,retries fail, interface running flag is removed. Parameters are written in following format:KeepaliveInterval,KeepaliveRetrieswhereKeepaliveIntervalis time interval andKeepaliveRetries- number of retry attempts. By default keepalive is set to 10 seconds and 10 retries.
local-address(IP; Default: ) | Source address of the packets, local on the router.
mtu(integer; Default:auto) | Layer3 maximum transmission unit.
name(string; Default: ) | Interface name.
remote-address(IP; Default: ) | IP address of remote end of 6to4 tunnel. If left unspecified, IPv4 address from 2002::/16 gateway address will bederived.
Whether to include DF bit in related packets:
no- fragment if needed,inherit- use Dont Fragment flag of original packet.
(Without Dont Fragment: inherit - packet may be fragmented).
```
KeepaliveInterval,KeepaliveRetries
```
```
KeepaliveInterval
```
```
KeepaliveRetries
```
# Configuration Examples
# Simple 6to4 tunnel encapsulation (Currently not working)
It is possible to simply route IPv6 packets over IPv4 network by utilizing the 2002::/16 allocated address space. All 6to4 nodes has to have reachable IPv4 addresses - if you are running this setup over the Internet, all IPv4's must be public addresses.
R1 configuration:
Create the 6to4 tunnel interface:
```
/interface 6to4
add name=6to4-tunnel1
```
Assign an IPv6 address with '2002' as the first 16 bits and IPv4 in hex format as the next 32 bits. For example, if the router's IP address is 10.0.1.1, the IPv6 address is 2002:A00:101::
```
/ipv6 address
add address=2002:a00:101::/128 advertise=no interface=6to4-tunnel1
```
Add a route to specially allocated 6to4 tunnel range over the 6to4-tunnel interface.
```
/ipv6 route
add dst-address=2002::/16 gateway=6to4-tunnel1
```
R2 configuration:
Create the 6to4 tunnel interface:
```
/interface 6to4
add name=6to4-tunnel1
```
Assign an IPv6 address that is generated by the same principles as R1. In this case, 10.0.2.1 translates to 2002:A00:201::
```
/ipv6 address
add address=2002:a00:201::/128 advertise=no interface=6to4-tunnel1
```
The 6to4 route is necessary on this side as well.
```
/ipv6 route
add dst-address=2002::/16 gateway=6to4-tunnel1
```
Testing:
After configuring both devices, it should be possible to ping the IPv6 addresses if they were generated correctly.
From R1:
```
/ping 2002:a00:201::
```
# Hurricane Electric Tunnel Broker Example
Following example will show how to get IPv6 connectivity on a RouterOS device through IPv4 network using 6to4 tunnel.
To be able to create the tunnel, you have to have a public IPv4 address and enable ping from Tunnel Broker IPv4 server.
When you create a tunnel usingHurricane Electric Tunnel Broker, you will be given a routed /64 IPv6 prefix and additional information necessary for setting up the tunnel.
This example presumes that your public IPv4 address is 194.105.56.170
Hurricane Electric provides ready to use commands for RouterOS in the 'Example Configurations' section:
```
/interface 6to4
add comment="Hurricane Electric IPv6 Tunnel Broker" disabled=no local-address=194.105.56.170 mtu=1280 name=sit1 remote-address=216.66.80.90
/ipv6 route
add comment="" disabled=no distance=1 dst-address=2000::/3 gateway=2001:470:27:37e::1 scope=30 target-scope=10
/ipv6 address
add address=2001:470:27:37e::2/64 advertise=no disabled=no eui-64=no interface=sit1
```
These commands will setup the tunnel itself - the router will be able to connect to IPv6 hosts, but end-user devices (computers, tablets, phones) will not yet have IPv6 connectivity.
To be able to assign IPv6 addresses to your clients you have to add the Routed IPv6 Prefix to your internal interface (by default bridge-local).
```
/ipv6 address add address=2001:470:28:37e:: interface=bridge-local advertise=yes
```
Enable DNS server advertising through network discovery
```
/ipv6 nd set [ find default=yes ] advertise-dns=yes
```
And finally add IPv6 DNS servers (these are Google public DNS servers, you can also use the one which is provided by Hurricane Electric - 2001:470:20::2).
```
/ip dns set allow-remote-requests=yes servers=2001:4860:4860::8888,2001:4860:4860::8844
```
Afterwards enable IPv6 on your device and you should have IPv6 connectivity.http://ipv6-test.comcan be used to test IPv6 connectivity.