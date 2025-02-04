# Document Information
Title: IPIP
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/47579173/IPIP,

# Content
# Summary
Sub-menu:/interface ipipStandards:RFC2003
```
/interface ipipStandards:RFC2003
```
The IPIP tunneling implementation on the MikroTik RouterOS is RFC 2003 compliant. IPIP tunnel is a simple protocol that encapsulates IP packets in IP to make a tunnel between two routers. The IPIP tunnel interface appears as an interface under the interface list. Many routers, including Cisco and Linux, support this protocol. This protocol makes multiple network schemes possible.IP tunneling protocol adds the following possibilities to a network setup:
# Properties
Property | Description
----------------------
clamp-tcp-mss(yes | no; Default:yes) | Controls whether to change MSS size for received TCP SYN packets. When enabled, a router will change the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead).The received encapsulated packet will still contain the original MSS, and only after decapsulation the MSS is changed.
dont-fragment(inherit | no; Default:no) | Whether to include DF bit in related packets:no- fragment if needed,inherit- use Dont Fragment flag of original packet.(Without Dont Fragment: inherit - packet may be fragmented).
dscp(inherit | integer [0-63]; Default: ) | Set dscp value in IPIP header to a fixed value or inherit from dscp value taken from tunnelled traffic
ipsec-secret(string; Default: ) | When secret is specified, router adds dynamic ipsec peer to remote-address with pre-shared key and policy with default values (by default phase2 uses sha1/aes128cbc).
local-address(IP; Default: ) | IP address on a router that will be used by IPIP tunnel
mtu(integer; Default:1500) | Layer3 Maximum transmission unit
keepalive(integer[/time],integer 0..4294967295; Default:10s,10) | Tunnel keepalive parameter sets the time interval in which the tunnel running flag will remain even if the remote end of tunnel goes down. If configured time,retries fail, interface running flag is removed. Parameters are written in following format:KeepaliveInterval,KeepaliveRetrieswhere KeepaliveInterval is time interval and KeepaliveRetries - number of retry attempts. By default keepalive is set to 10 seconds and 10 retries.
name(string; Default: ) | Interface name
remote-address(IP; Default: ) | IP address of remote end of IPIP tunnel
Whether to include DF bit in related packets:
no- fragment if needed,inherit- use Dont Fragment flag of original packet.
(Without Dont Fragment: inherit - packet may be fragmented).
```
KeepaliveInterval,KeepaliveRetries
```
# Example
Suppose we want to add an IPIP tunnel between routers R1 and R2:
At first, we need to configure IPIP interfaces and then add IP addresses to them.The configuration for routerR1is as follows:
```
[admin@MikroTik] interface ipip> add
local-address: 10.0.0.1
remote-address: 22.63.11.6
[admin@MikroTik] interface ipip> print
Flags: X - disabled, R - running
# NAME MTU LOCAL-ADDRESS REMOTE-ADDRESS
0 X ipip1 1480 10.0.0.1 22.63.11.6
[admin@MikroTik] interface ipip> en 0
[admin@MikroTik] interface ipip> /ip address add address=1.1.1.1/24 interface=ipip1
```
The configuration of theR2is shown below:
```
[admin@MikroTik] interface ipip> add local-address=22.63.11.6 remote-address=10.
0.0.1
[admin@MikroTik] interface ipip> print
Flags: X - disabled, R - running
# NAME MTU LOCAL-ADDRESS REMOTE-ADDRESS
0 X ipip1 1480 22.63.11.6 10.0.0.1
[admin@MikroTik] interface ipip> enable 0
[admin@MikroTik] interface ipip> /ip address add address=1.1.1.2/24 interface=ipip1
```
Now both routers can ping each other:
```
[admin@MikroTik] interface ipip> /ping 1.1.1.2
1.1.1.2 64 byte ping: ttl=64 time=24 ms
1.1.1.2 64 byte ping: ttl=64 time=19 ms
1.1.1.2 64 byte ping: ttl=64 time=20 ms
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 19/21.0/24 ms
[admin@MikroTik] interface ipip>
```