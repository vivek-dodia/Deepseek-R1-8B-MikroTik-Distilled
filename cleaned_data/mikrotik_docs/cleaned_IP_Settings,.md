# Document Information
Title: IP Settings
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/103841817/IP+Settings,

# Content
# Summary
Several IPv4 and IPv6 related kernel and system-wide parameters are configurable.
# IPv4 Settings
Sub-menu:/ip settings
```
/ip settings
```
Property | Description
----------------------
accept-redirects(yes | no; Default:no) | Whether to accept ICMP redirect messages. Typically should be enabled on a host and disabled on routers.
accept-source-route(yes | no; Default:no) | Whether to accept packets with the SRR option. Typically should be enabled on the router.
allow-fast-path(yes | no; Default:yes) | AllowsFast Path.
arp-timeout(time interval; Default:30s) | Sets Linuxbase_reachable_time(base_reachable_time_ms) on all interfaces that use ARP. The initial validity of the ARP entry is picked from the interval [timeout/2 - 3*timeout/2] (default from 15s to 45s) after the neighbor was found. Can use postfix ms, s, m, h, d for milliseconds, seconds, minutes, hours, or days. if no postfix is set then seconds (s) are used. The parameter means how long a valid ARP record will be considered complete if no one communicates with the specific MAC/IP during this time. The parameterdoes not represent a time when an ARP entry is removed from the ARP cache (seemax-neighbor-entriessetting).
icmp-errors-use-inbound-interface-address(yes | no; Default: no) | If enabled,the ICMP error message reply will be sent with the source address equal to primary address of the receiving interface that caused the error . This feature can be useful for complex network debugging.
icmp-rate-limit(integer [0..4294967295]; Default:10) | Limit the maximum rates for sending ICMP packets whose type matchesicmp-rate-maskto specific targets.0disables any limiting, other values indicate the minimum space between responses in milliseconds.
icmp-rate-mask([0..FFFFFFFF]; Default:0x1818) | Mask made of ICMP types for which rates are being limited.More info in Linux man pages
ip-forward(yes | no; Default:yes) | Enable/disable packet forwarding between interfaces. Resets all configuration parameters to defaults according to RFC1812 for routers.
ipv4-multipath-hash-policy(l3 | l4 | l3-inner; Default:l3) | IPv4 Hash policy used for ECMP routing in/ip/settingsmenul3 -- layer-3 hashing of src IP, dst IPl3-inner -- layer-3 hashing or inner layer-3 hashing if availablel4 -- layer-4 hashing of src IP, dst IP, IP protocol, src port, dst port
rp-filter(loose | no | strict; Default:no) | Disables or enables source validation.no - No source validation.strict - Strict mode as defined in RFC3704 Strict Reverse Path. Each incoming packet is tested against the FIB and if the interface is not the best reverse path the packet check will fail. By default failed packets are discarded.loose - Loose mode as defined in RFC3704 Loose Reverse Path. Each incoming packet's source address is also tested against the FIB and if the source address is not reachable via any interface the packet check will fail.The current recommended practice in RFC3704 is to enable strict mode to prevent IP spoofing from DDoS attacks. If using asymmetric routing or other complicated routing or VRRP, then the loose mode is recommended.Warning:strict mode does not work with routing tables
secure-redirects(yes | no; Default:yes) | Accept ICMP redirect messages only for gateways, listed in the default gateway list.
send-redirects(yes | no; Default:yes) | Whether to send ICMP redirects. Recommended to be enabled on routers.
tcp-timestamps(disabled | enabled | random-offset; Default: random-offset) | Parameter allows to enable/disable TCP timestamps or add random offset to TCP timestamp (default behavior). Disabling timestamps completely may help to reduce spikes of performance drops.
tcp-syncookies(yes | no; Default:no) | Send out syncookies when the syn backlog queue of a socket overflows. This is to prevent the common 'SYN flood attack'. syncookies seriously violate TCP protocol, and disallow the use of TCP extensions, which can result in serious degradation of some services (f.e. SMTP relaying), visible not by you, but to your clients and relays, contacting you.
max-neighbor-entries(integer [0..4294967295]; Default:) | Sets Linuxgc_thresh3.A maximum number of allowed neighbors in the ARP table. Since RouterOS version 7.1,the default value depends on the installed amount of RAM. It is possible to set a higher value than the default, but it increases the risk of out-of-memory condition.The default values for certain RAM sizes:2048 for 64 MB,4096 for 128 MB,8192 for 256 MB,16384 for 512 MB or higher.The ARP cache stores ARP entries, and if some of these entries are incomplete, they can stay in the cache for an indefinite period of time. This will only happen if the number of entries in the cache is less than one-fourth of the maximum number allowed. The reason for this is to prevent the unnecessary running of the garbage-collector when the ARP table is not close to being full.
route-cache(yes | no; Default:yes) | Disable or enable the Linux route cache. Note that disabling the route cache, will also disable the fast path.
IPv4 Hash policy used for ECMP routing in/ip/settingsmenu
```
/ip/settings
```
Warning:strict mode does not work with routing tables
tcp-timestamps(disabled | enabled | random-offset; Default: random-offset)
Sets Linuxgc_thresh3.A maximum number of allowed neighbors in the ARP table. Since RouterOS version 7.1,the default value depends on the installed amount of RAM. It is possible to set a higher value than the default, but it increases the risk of out-of-memory condition.
The default values for certain RAM sizes:
The ARP cache stores ARP entries, and if some of these entries are incomplete, they can stay in the cache for an indefinite period of time. This will only happen if the number of entries in the cache is less than one-fourth of the maximum number allowed. The reason for this is to prevent the unnecessary running of the garbage-collector when the ARP table is not close to being full.
Read-Only Properties
Property | Description
----------------------
ipv4-fast-path-active(yes | no) | Indicates whether fast-path is active
ipv4-fast-path-bytes(integer) | Amount of fast-pathed bytes
ipv4-fast-path-packets(integer) | Amount of fast-pathed packets
ipv4-fasttrack-active(yes | no) | Indicates whether fasttrack is active
ipv4-fasttrack-bytes(integer) | Amount of fasttracked bytes
ipv4-fasttrack-packets(integer) | Amount of fasttracked packet.
# IPv6 Settings
Sub-menu:/ipv6 settings
```
/ipv6 settings
```
Property | Description
----------------------
accept-redirects(no | yes-if-forwarding-disabled; Default:yes-if-forwarding-disabled) | Whether to accept ICMP redirect messages. Typically should be enabled on the host and disabled on routers
accept-router-advertisements(no | yes | yes-if-forwarding-disabled; Default:yes-if-forwarding-disabled) | Accept router advertisement (RA) messages. If enabled, the router will be able to get the address usingstateless address configuration
disable-ipv6(yes | no; Default:no) | Enable/disable system wide IPv6 settings (prevents LL address generation)
forward(yes | no; Default:yes) | Enable/disable packet forwarding between interfaces
max-neighbor-entries(integer [0..4294967295]; Default:) | A maximum number or IPv6 neighbors. Since RouterOS version 7.1,the default value depends on the installed amount of RAM. It is possible to set a higher value than the default, but it increases the risk of out-of-memory condition.The default values for certain RAM sizes:1024 for 64 MB,2048 for 128 MB,4096 for 256 MB,8192 for 512 MB,16384 for 1024 MB or higher.
multipath-hash-policy(l3 | l4 | l3-inner; Default:l3) | IPv6 Hash policy used for ECMP routing in/ipv6/settingsmenul3 -- layer-3 hashing of src IP, dst IP, flow label, IP protocoll3-inner -- layer-3 hashing or inner layer-3 hashing if availablel4 -- layer-4 hashing of src IP, dst IP, IP protocol, src port, dst port
disabled-lonk-local-address(no | yes; Default:no) | Disable automatic link-local address generation for non-VPN interfaces. This can be used when manually configured link-local addresses are being used.
stale-neighbor-timeout(time; Default:60) | Timeout after which stale IPv6/Neighbor entries should be purged.
min-neighbor-entries(integer; Default:4096) | Minimal number of IPv6/Neighbor entries, for which device must allocate memory.
soft-max-neighbor-entries(integer; Default:8192) | Expected maximum number of IPv6/Neighbor entries which system should handle.
max-neighbor-entries(integer; Default:16384) | Maximum number of entries for IPv7/Neighbor list.
allow-fast-path(yes | no; Default:yes) | AllowsFast Path.
The default values for certain RAM sizes:
IPv6 Hash policy used for ECMP routing in/ipv6/settingsmenu
```
/ipv6/settings
```
Disable automatic link-local address generation for non-VPN interfaces. This can be used when manually configured link-local addresses are being used.
Timeout after which stale IPv6/Neighbor entries should be purged.
Minimal number of IPv6/Neighbor entries, for which device must allocate memory.
Expected maximum number of IPv6/Neighbor entries which system should handle.
Maximum number of entries for IPv7/Neighbor list.
AllowsFast Path.
Read-Only Properties
Property | Description
----------------------
ipv6-fast-path-active(yes | no) | Indicates whether fast-path is active
ipv6-fast-path-bytes(integer) | Amount of fast-pathed bytes
ipv6-fast-path-packets(integer) | Amount of fast-pathed packets
ipv6-fasttrack-active(yes | no) | Indicates whether fasttrack is active
ipv6-fasttrack-bytes(integer) | Amount of fasttracked bytes
ipv6-fasttrack-packets(integer) | Amount of fasttracked packet.