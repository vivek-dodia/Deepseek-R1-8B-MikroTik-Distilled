---
title: PPP AAA
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/132350049/PPP+AAA,
crawled_date: 2025-02-02T21:09:43.283795
section: mikrotik_docs
type: documentation
---

* 1Summary
* 2User Profiles
* 3User Database
* 4Active Users
* 5Remote AAA
* 6Examples6.1Add new profile6.2Add new user
* 6.1Add new profile
* 6.2Add new user
# Summary
Sub-menu:/ppp
```
/ppp
```
The MikroTik RouterOS provides scalable Authentication, Authorization, and Accounting (AAA) functionality.
Local authentication is performed using the User Database and the Profile Database. The actual configuration for the given user is composed using the respective user record from the User Database, the associated item from the Profile Database, and the item in the Profile database which is set as default for a given service the user is authenticating to. Default profile settings from the Profile database have the lowest priority while the user access record settings from the User Database have the highest priority with the only exception being particular IP addresses take precedence over IP pools in the local-address and remote-address settings, which are described later on.
Support for RADIUS authentication gives the ISP or network administrator the ability to manage PPP user access and accounting from one server throughout a large network. The MikroTik RouterOS has aRADIUS clientthat can authenticate for PPP,PPPoE,PPTP,L2TP,OPVN,and ISDN connections. The attributes received from the RADIUS server override the ones set in the default profile, but if some parameters are not received they are taken from the respective default profile.
# User Profiles
Sub-menu:/ppp profile
```
/ppp profile
```
PPP profiles are used to define default values for user access records stored under/ppp secretsubmenu. Settings in/ppp secretUser Database overrides corresponding/ppp profilesettings except that single IP addresses always take precedence over IP pools when specified as local-address or remote-address parameters.
```
/ppp secret
```
```
/ppp secret
```
```
/ppp profile
```
Properties
Property | Description
----------------------
address-list(string; Default: ) | Address listname to which ppp assigned (on server) or received (on client) address will be added.
bridge(string; Default: ) | Name of thebridgeinterface to which ppp interface will be added as a slave port. Both tunnel endpoints (server and client) must be in the bridge to make this work, see more details in theBCP bridgingmanual.
bridge-horizon(integer 0..429496729; Default: ) | Used split-horizon value for the dynamically created bridge port. Can be used to prevent bridging loops and isolate traffic. Set the same value for a group of ports, to prevent them from sending data to ports with the same horizon value.
bridge-learning(default | no | yes; Default:default) | Changes MAC learning behavior on the dynamically created bridge port:yes - enables MAC learningno - disables MAC learningdefault - derive this value from the interface default profile; same as yes if this is the interface default profile
bridge-path-cost(integer 1..200000000; Default: ) | Used path cost for the dynamically created bridge port, used by STP/RSTP to determine the best path, used by MSTP to determine the best path between regions. This property has no effect when a bridge protocol-mode is set to none.
bridge-port-priority(integer 0..240; Default: ) | Used priority for the dynamically created bridge port, used by STP/RSTP to determine the root port, used by MSTP to determine the root port between regions. This property has no effect when a bridge protocol-mode is set to none.
bridge-port-vid(integer 1..4094; Default:1) | Used to assign PVID parameter for dynamically created interface. This property only has an effect when bridge vlan-filtering is set to yes.
bridge-port-trusted(no | yes;Default:no) | Used to set dynamically created interface as DHCP trusted.
change-tcp-mss(yes | no | default; Default:no) | Modifies connection MSS settings (applies only for IPv4):yes - adjust connection MSS valueno - do not adjust connection MSS valuedefault - derive this value from the interface default profile; same as no if this is the interface default profile
comment(string; Default: ) | Profile comment
dhcpv6-pd-pool(string; Default: ) | Name of theIPv6 poolwhich will be used by dynamically createdDHCPv6 serverwhen client connects.Read more >>
dns-server(IP; Default: ) | IP address of the DNS server that is supplied to PPP clients
idle-timeout(time; Default: ) | Specifies the amount of time after which the link will be terminated if there is no activity present. Timeout is not set by default
incoming-filter(string; Default: ) | Firewall chain name for incoming packets. The specified chain gets control of each packet coming from the client. The ppp chain should be manually added and rules with action=jump jump-target=ppp should be added to other relevant chains for this feature to work. For more information look at theexamplessection
insert-queue-before(bottom | first | queue name; Default: ) | Inserts new queue as the last, first, or before a specified queue
interface-list(interface list name; Default: ) | Specifies interface list to which profile interfaces will be added
local-address(IP address | pool; Default: ) | Tunnel address or name of thepoolfrom which the address is assigned to ppp interface locally
name(string; Default: ) | PPP profile name
on-up(script; Default: ) | Execute script on user login-event. These are available variables that are accessible for the event script:userlocal-addressremote-addresscaller-idcalled-idinterface
on-down(script; Default: ) | Execute script on the user logging off. Seeon-upfor more details
only-one(yes | no | default; Default:default) | Defines whether a user is allowed to have more than one ppp session at a timeyes - a user is not allowed to have more than one ppp session at a timeno - the user is allowed to have more than one ppp session at a timedefault - derive this value from the interface default profile; same as no if this is the interface default profile
outgoing-filter(string; Default: ) | Firewall chain name for outgoing packets. The specified chain gets control for each packet going to the client. The PPP chain should be manually added and rules with action=jump jump-target=ppp should be added to other relevant chains for this feature to work. For more information look at the Examples section.
parent-queue(none|queue name; Default: ) | Specifies parent queue
queue-type(default | ethernet-default | wireless-default | synchronous-default |hotspot-default | pcq-upload-default | pcq-download-default | only-hardware-queue | multi-queue-ethernet-default | default-small | custom queue type name; Default: ) | Specifies queue type
rate-limit(string; Default: ) | Rate limitation in form ofrx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]from the point of view of the router (so "rx" is client upload, and "tx" is client download). All rates are measured in bits per second, unless followed by an optional 'k' suffix (kilobits per second) or 'M' suffix (megabits per second). If tx-rate is not specified, rx-rate serves as tx-rate too. The same applies to tx-burst-rate, tx-burst-threshold and tx-burst-time. If both rx-burst-threshold and tx-burst-threshold are not specified (but burst-rate is specified), rx-rate and tx-rate are used as burst thresholds. If both rx-burst-time and tx-burst-time are not specified, 1s is used as default. Priority takes values 1..8, where 1 implies the highest priority, but 8 - the lowest. If rx-rate-min and tx-rate-min are not specified rx-rate and tx-rate values are used. The rx-rate-min and tx-rate-min values can not exceed rx-rate and tx-rate values.
remote-address(IP; Default: ) | Tunnel address or name of thepoolfrom which address is assigned to remote ppp interface.
remote-ipv6-prefix-pool(string | none; Default:none) | Assign a prefix from the IPv6 pool to the client and install the corresponding IPv6 route.
session-timeout(time; Default: ) | Maximum time the connection can stay up. By default, no time limit is set.
use-compression(yes | no | default; Default:default) | Specifies whether to use data compression or not.yes - enable data compressionno - disable data compressiondefault - derive this value from the interface default profile; same as no if this is the interface default profileThis setting does not affect OVPN tunnels.
use-encryption(yes | no | default | require; Default:default) | Specifies whether to use data encryption or not.yes - enable data encryptionno - disable data encryptiondefault - derive this value from the interface default profile; same as no if this is the interface default profilerequire - explicitly requires encryptionThis setting does not work on OVPN and SSTP tunnels.
use-ipv6(yes | no | default | require; Default:default) | Specifies whether to allow IPv6. By default is enabled if IPv6 package is installed.yes - enable IPv6 supportno - disable IPv6 supportdefault - derive this value from the interface default profile; same as no if this is the interface default profilerequire - explicitly requires IPv6 support
use-mpls(yes | no | default | require; Default:default) | Specifies whether to allow MPLS over PPP.yes - enable MPLS supportno - disable MPLS supportdefault - derive this value from the interface default profile; same as no if this is the interface default profilerequire - explicitly requires MPLS support
use-upnp(yes | no | default; Default:default) | Specifies whether to allowUPnPyes - enableUPnPno - disableUPnPdefault - derive this value from the interface default profile; same as no if this is the interface default profile
wins-server(IP address; Default: ) | IP address of the WINS server to supply to Windows clients
* yes - enables MAC learning
* no - disables MAC learning
* default - derive this value from the interface default profile; same as yes if this is the interface default profile
* yes - adjust connection MSS value
* no - do not adjust connection MSS value
* default - derive this value from the interface default profile; same as no if this is the interface default profile
```
Read more >>
```
* user
* local-address
* remote-address
* caller-id
* called-id
* interface
* yes - a user is not allowed to have more than one ppp session at a time
* no - the user is allowed to have more than one ppp session at a time
* default - derive this value from the interface default profile; same as no if this is the interface default profile
queue-type(default | ethernet-default | wireless-default | synchronous-default |hotspot-default | pcq-upload-default | pcq-download-default | only-hardware-queue | multi-queue-ethernet-default | default-small | custom queue type name; Default: )
* yes - enable data compression
* no - disable data compression
* default - derive this value from the interface default profile; same as no if this is the interface default profile
* yes - enable data encryption
* no - disable data encryption
* default - derive this value from the interface default profile; same as no if this is the interface default profile
* require - explicitly requires encryption
* yes - enable IPv6 support
* no - disable IPv6 support
* default - derive this value from the interface default profile; same as no if this is the interface default profile
* require - explicitly requires IPv6 support
* yes - enable MPLS support
* no - disable MPLS support
* default - derive this value from the interface default profile; same as no if this is the interface default profile
* require - explicitly requires MPLS support
Specifies whether to allowUPnP
* yes - enableUPnP
* no - disableUPnP
* default - derive this value from the interface default profile; same as no if this is the interface default profile
Notes
The two default profiles cannot be removed:
```
[admin@rb13] ppp profile> print
Flags: * - default
 0 * name="default" use-compression=no use-encryption=no only-one=no
     change-tcp-mss=yes
 1 * name="default-encryption" use-compression=default use-encryption=yes
     only-one=default change-tcp-mss=default
[admin@rb13] ppp profile>
```
incoming-filterandoutgoing-filterarguments add dynamic jump rules to chainppp, where the jump-target argument will be equal toincoming-filteroroutgoing-filterargument in the profile. Therefore, chainpppshould be manually added before changing these arguments.
only-one parameter is ignored if RADIUS authentication is used.
# User Database
Sub-menu:/ppp secret
```
/ppp secret
```
PPP User Database stores PPP user access records with PPP user profile assigned to each user.
Properties
Property | Description
----------------------
caller-id(string; Default: ) | ForPPTPandL2TPit is the IP address a client must connect from. ForPPPoEit is the MAC address (written in CAPITAL letters) a client must connect from. For ISDN it is the caller's number (that may or may not be provided by the operator) the client may dial-in from
comment(string; Default: ) | Short description of the user.
disabled(yes | no; Default:no) | Whether secret will be used.
limit-bytes-in(integer; Default:0) | The maximum amount of bytes for a session that the client can upload.
limit-bytes-out(integer; Default:0) | The maximum amount of bytes for a session that the client can download.
local-address(IP address; Default: ) | IP address that will be set locally on ppp interface.
name(string; Default: ) | Name used for authentication
password(string; Default: ) | Password used for authentication
profile(string; Default:default) | Whichuser profileto use
remote-address(IP; Default: ) | IP address that will be assigned to the remote ppp interface.
remote-ipv6-prefix(IPv6 prefix; Default: ) | IPv6 prefix assigned to ppp client. Prefix is added toND prefix listenablingstatelessaddress auto-configuration on ppp interface.
routes(string; Default: ) | Routes that appear on the server when the client is connected. The route format is: dst-address gateway metric (for example, 10.1.0.0/ 24 10.0.0.1 1). Other syntax is not acceptable since it can be represented incorrectly. Several routes may be specified and separated with commas. This parameter will be ignored forOpenVPN.
service(any | async | isdn | l2tp | pppoe | pptp | ovpn | sstp; Default:any) | Specifies the services that a particular user will be able to use.
# Active Users
Sub-menu:/ppp active
```
/ppp active
```
This submenu allows monitoring active (connected) users.
/ppp active printcommand will show all currently connected users.
```
/ppp active print
```
/ppp active print statscommand will show received/sent bytes and packets
```
/ppp active print stats
```
Properties
Property | Description
----------------------
address(IP address) | The IP address the client got from the server
bytes(integer) | Amount of bytes transferred through this connection. The first figure represents the amount of transmitted traffic from the router's point of view, while the second one shows the amount of received traffic.
caller-id(string) | ForPPTPandL2TPit is the IP address the client connected from. ForPPPoE, it is the MAC address the client connected from.
encoding(string) | Shows encryption and encoding (separated with '/' if asymmetric) being used in this connection
limit-bytes-in(integer) | The maximum amount of bytes the user is allowed to send to the router.
limit-bytes-out(integer) | The maximum amount of bytes the user is allowed to send to the client.
name(string) | User name supplied at authentication stage
packets(integer/integer) | Amount of packets transferred through this connection. The first figure represents the amount of transmitted traffic from the router's point of view, while the second one shows the amount of received traffic
service(async | isdn | l2tp | pppoe | pptp | ovpn | sstp) | Type of service the user is using.
session-id(string) | Shows unique client identifier.
uptime(time) | User's uptime
# Remote AAA
Sub-menu:/ppp aaa
```
/ppp aaa
```
Settings in this submenu allows to set RADIUS accounting and authentication. Note that the RADIUS user database is consulted only if the required username is not found in the local user database.
Properties
Property | Description
----------------------
accounting(yes | no; Default:yes) | Enable RADIUS accounting
interim-update(time; Default:0s) | Interim-Update time interval
use-radius(yes | no; Default:no) | Enable user authentication via RADIUS. If an entry in the local secret database is not found, then the client will be authenticated via RADIUS.
enable-ipv6-accounting(yes | no; Default:no) | Enable IPv6 separate accounting. PPP service counts Layer2, IPv4 and IPv6 data all together when reporting network usage statistics to the RADIUS server by default. If it is required to differ IPv4 and IPv6 traffic, then this option can be enabled. Prerequisites for it to work are that the prefix must be assigned to the client through PPP service and also rate-limit must be provided. Dynamically created queue statistics will be used as counters for IPv6 data, which then will be included in accounting packets as separate IPv6 statistics attributes. This will not work for prefixes assigned by dynamically created DHCPv6 server due to provided prefix pool or PPP/Profile configuration. Then prefix assignment is handled by DHCP service, not PPP, thus accounting can not be managed by PPP service.
# Examples
### Add new profile
To add the profile ex that assigns the router itself the 10.0.0.1 address, and the addresses from the ex pool to the clients, filtering traffic coming from clients through mypppclients chain:
```
[admin@rb13] ppp profile> add name=ex local-address=10.0.0.1 remote-address=ex incoming-filter=mypppclients
[admin@rb13] ppp profile> print
Flags: * - default
 0 * name="default" use-compression=no use-vj-compression=no use-encryption=no only-one=no
     change-tcp-mss=yes
 1   name="ex" local-address=10.0.0.1 remote-address=ex use-compression=default
     use-vj-compression=default use-encryption=default only-one=default change-tcp-mss=default
     incoming-filter=mypppclients
 2 * name="default-encryption" use-compression=default use-vj-compression=default use-encryption=yes
     only-one=default change-tcp-mss=default
[admin@rb13] ppp profile>
```
### Add new user
To add the user ex with password lkjrht and profile ex available for PPTP service only, enter the following command:
```
[admin@rb13] ppp secret> add name=ex password=lkjrht service=pptp profile=ex
[admin@rb13] ppp secret> print
Flags: X - disabled
 #   NAME                SERVICE CALLER-ID         PASSWORD          PROFILE            REMOTE-ADDRESS
 0   ex                  pptp                      lkjrht            ex                 0.0.0.0
[admin@rb13] ppp secret>
```