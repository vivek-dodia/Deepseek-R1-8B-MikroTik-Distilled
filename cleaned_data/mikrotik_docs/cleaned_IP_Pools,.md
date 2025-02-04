# Document Information
Title: IP Pools
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/129531938/IP+Pools,

# Content
# Summary
IP pools are used to define range of IP addresses that can be used by various RouterOS utilities, for example, DHCP server, Point-to-Point servers and more. Separate lists for IPv4 and IPv6 are available. Whenever possible, the same IP address is given out to each client (OWNER/INFO pair).
# IPv4 Pool
Sub-menu:/ip pool
```
/ip pool
```
Property | Description
----------------------
comment(string; Default: ) | Short description of the pool
name(string; Default: ) | Unique identifier of the pool
next-pool(string; Default:) | When IP address acquisition is performed a pool that has no free addresses, and the next-pool property is set, then IP address will be acquired from next-pool
ranges(IP; Default:) | IP address list of non-overlapping IP address ranges in the form of: from1-to1,from2-to2,...,fromN-toN. For example, 10.0.0.1-10.0.0.27,10.0.0.32-10.0.0.47
name(string; Default: )
# Example
To define a pool named "my-pool" with the 10.0.0.1-10.0.0.126 address range excluding gateway's address 10.0.0.1 and server's address 10.0.0.100, and the other pool dhcp-pool, with the 10.0.0.200-10.0.0.250 address range:
```
[admin@MikroTik] ip pool> add name=my-pool ranges=10.0.0.2-10.0.0.99,10.0.0.101-10.0.0.126
[admin@MikroTik] ip pool> add name=dhcp-pool ranges=10.0.0.200-10.0.0.250
[admin@MikroTik] ip pool> print
# NAME                                        RANGES
0 ip-pool                                     10.0.0.2-10.0.0.99
10.0.0.101-10.0.0.126
1 dhcp-pool                                   10.0.0.200-10.0.0.250
```
# Used addresses
Sub-menu:/ip pool used
```
/ip pool used
```
Here you can see all used IP addresses from IP pools.
Read-only properties
Property | Description
----------------------
address(IP) | IP address that is assigned to client from the pool
info(string) | For DHCP MAC address from leases menu and for PPP connections username of PPP type client
owner(string) | Service which is using this IP address
pool(string) | Name of the IP pool
info(string)
Name of the IP pool
# IPv6 Pool
Sub-menu:/ipv6 pool
```
/ipv6 pool
```
Property | Description
----------------------
name(string; Default: ) | Descriptive name of the pool.
prefix(IPv6/0..128; Default: ) | Ipv6 address prefix
prefix-length(integer [1..128]; Default: ) | The option represents the prefix size that will be given out to the client.
Read-only properties
Property | Description
----------------------
dynamic(yes | no) | Whether the pool is dynamic.
expire-time(time) | Expire time is set to dynamic pools added byDHCPv6 client.
# Example
The example will create a pool of "2001::/60" to give out /62 prefixes:
```
[admin@test-host] /ipv6 pool> add
name: test prefix: 2001::/60
prefix-length: 62
[admin@test-host] /ipv6 pool> print
# NAME PREFIX PREFIX-LENGTH
0 test 2001::/60 62bits
```
# Used addresses
Sub-menu:/ipv6 pool used
```
/ipv6 pool used
```
Read-only properties
Property | Description
----------------------
info(string) | Shows DUID related information received from the client (value in hex). Can contain also a raw timestamp in hex.
owner(string) | What reserved the prefix ("DHCP", etc.)
pool(string) | Name of the pool.
prefix(IPv6/0..128) | IPv6 prefix that is assigned to the client from the pool.