# Document Information
Title: NTP
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/40992869/NTP,

# Content
RouterOS v6 implements the SNTP protocol defined in RFC4330, manycast mode is not supported. SNTP client is included in thesystempackage. To use an NTP server,ntppackage must beinstalled and enabled.
RouterOS v7 main package includes NTP client and server functionality, which is based on RFC5905.
The client configuration is located in the/system ntp clientconsole path, and the"System > SNTP Client"(RouterOS version 6),"System > NTP Client"(RouterOS version 7) WinBox window.This configuration is shared by the SNTP client implementation in thesystempackage and the NTP client implementation in thentppackage. Whenntppackage is installed and enabled, the SNTP client is disabled automatically.
# RouterOS version 6
# SNTP Clientproperties:
Property | Description
----------------------
enabled(yes, no default:no) | Enable SNTP client for time synchronization
mode(broadcast, unicast, filed is read-only) | Mode that the SNTP client will operate in. If no NTP servers are configuredbroadcastmode will be used. If there is a dynamic or static NTP server IP address or FQDN used it will automatically switch to unicast mode.
primary-ntp(IP address default:0.0.0.0) | IP address of the NTP server that has to be used for time synchronization. If both values are non-zero, then the SNTP client will alternate between the two server addresses, switching to the other when the request to the current server times out or when the "KoD" packet is received, indicating that the server is not willing to respond to requests from this client.The following formats are accepted:- ipv4- ipv6
secondary-ntp(IP address default:0.0.0.0) | seeprimary-ntp
server-dns-names(Comma separated domain name list default:) | To set the NTP server using its domain name. The domain name will be resolved each time an NTP request is sent. Router has to have/ip dnsconfigured.
IP address of the NTP server that has to be used for time synchronization. If both values are non-zero, then the SNTP client will alternate between the two server addresses, switching to the other when the request to the current server times out or when the "KoD" packet is received, indicating that the server is not willing to respond to requests from this client.
The following formats are accepted:
- ipv4- ipv6
Status
Last received packet information
Values of the following properties are reset when the SNTP client is stopped or restarted, either because of a configuration change, or because of a network error.
# Client settings example:
To check the status of the NTP client in CLI, use the "print" command
```
[admin@ntp-example_v6] > /system ntp client print
enabled: no
primary-ntp: 0.0.0.0
secondary-ntp: 0.0.0.0
server-dns-names:
mode: unicast
```
To enable the NTP client and set IP addresses or FQDN of the NTP servers:
```
[admin@ntp-example_v6] > /system ntp client set enabled=yes
[admin@ntp-example_v6] > /system ntp client print
enabled: yes
primary-ntp: 0.0.0.0
secondary-ntp: 0.0.0.0
server-dns-names:
mode: unicast
dynamic-servers: x.x.x.x, x.x.x.x
poll-interval: 15s
active-server: x.x.x.x
last-update-from: x.x.x.x
last-update-before: 6s570ms
last-adjustment: -1ms786us
[admin@ntp-example_v6] > /system ntp client set primary-ntp=162.159.200.123
[admin@ntp-example_v6] > /system ntp client print
enabled: yes
primary-ntp: 162.159.200.123
secondary-ntp: 0.0.0.0
server-dns-names:
mode: unicast
dynamic-servers: x.x.x.x, x.x.x.x
poll-interval: 16s
active-server: x.x.x.x
```
# NTP Server settings:
Server configuration is located in/system ntp server
Property | Description
----------------------
enabled(yesorno; default value:no) | Enable  NTP server
broadcast(yesorno; default value:no) | Enable certain NTP server mode, for this mode to work you have to set up broadcast-addresses field
multicast(yesorno; default value:no) | Enable certain NTP server mode
manycast(yesorno; default value:no) | Enable certain NTP server mode
broadcast-addresses(IP address; default value: ) | Set broadcast address to use for NTP server broadcast mode
enabled(yesorno; default value:no)
broadcast(yesorno; default value:no)
multicast(yesorno; default value:no)
manycast(yesorno; default value:no)
broadcast-addresses(IP address; default value: )
Example:
Set up an NTP server for the local network that is 192.168.88.0/24
```
/system ntp server set broadcast=yes broadcast-addresses=192.168.88.255 enabled=yes manycast=no
```
# RouterOS version 7
# NTP Client properties:
Property | Description
----------------------
enabled(yes, no default:no) | Enable NTP client for time synchronization
mode(broadcast, manycast, multicast, unicast) | Mode that the NTP client will operate in
NTP servers | The list of NTP servers. It is possible to add static entries.The following formats are accepted:-FQDN ("Resolved Address" will appear in the "Servers"- window in an appropriate column if the address is resolved) or IP address can be used. If DHCP-Client propertyuse-peer-ntp=yes- the dynamic entries advertised byDHCP-ipv4-ipv4@vrf-ipv6-ipv6@vrf-ipv6-linklocal%interface
vrf(default: main) | Virtual Routing and Forwarding
Servers(Button/Section) | A detailed table of dynamically and statically added NTP servers (Address, Resolved address, Min Poll, Max Poll, iBurst, Auth. Key)To set the NTP server using its FQDN. The domain name will be resolved each time an NTP request is sent. Router has to have/ip/dnsconfigured.
Peers | Current parameter values[admin@ntp-example_v7] > /system/ntp/monitor-peers
type="ucast-client" address=x.x.x.x refid="y.y.y.y" stratum=3 hpoll=10 ppoll=10 root-delay=28.869 ms root-disp=50.994 ms
offset=-0.973 ms delay=0.522 ms disp=15.032 ms jitter=0.521 ms
-- [Q quit|D dump|C-z pause]
Keys | NTP symmetric keys, used for authentication between the NTP client and server. Key Identifier (Key ID) - an integer identifying the cryptographic key used to generate the message-authentication code.
NTP servers
The list of NTP servers. It is possible to add static entries.
The following formats are accepted:
-FQDN ("Resolved Address" will appear in the "Servers"- window in an appropriate column if the address is resolved) or IP address can be used. If DHCP-Client propertyuse-peer-ntp=yes- the dynamic entries advertised byDHCP-ipv4-ipv4@vrf-ipv6-ipv6@vrf-ipv6-linklocal%interface
```
@
```
```
@
```
```
%
```
A detailed table of dynamically and statically added NTP servers (Address, Resolved address, Min Poll, Max Poll, iBurst, Auth. Key)
To set the NTP server using its FQDN. The domain name will be resolved each time an NTP request is sent. Router has to have/ip/dnsconfigured.
Peers
Current parameter values
```
[admin@ntp-example_v7] > /system/ntp/monitor-peers
type="ucast-client" address=x.x.x.x refid="y.y.y.y" stratum=3 hpoll=10 ppoll=10 root-delay=28.869 ms root-disp=50.994 ms
offset=-0.973 ms delay=0.522 ms disp=15.032 ms jitter=0.521 ms
-- [Q quit|D dump|C-z pause]
```
Keys
NTP symmetric keys, used for authentication between the NTP client and server. Key Identifier (Key ID) - an integer identifying the cryptographic key used to generate the message-authentication code.
Status
# NTP Server settings:
Server configuration is located in/system ntp server
Property | Description
----------------------
enabled(yesorno; default value:no) | Enable NTP server
broadcast(yesorno; default value:no) | Enable certain NTP server mode, for this mode to work you have to set up broadcast-addresses field
multicast(yesorno; default value:no) | Enable certain NTP server mode
manycast(yesorno; default value:no) | Enable certain NTP server mode
broadcast-addresses(IP address; default value: ) | Set broadcast address to use for NTP server broadcast mode
vrf(default: main) | Virtual Routing and Forwarding
use-local-clock(yesorno; default value:no) | The server will supply its local system time as valid if others are not available.
local-clock-stratum | Manually set stratum ifuse-local-clock=yes
auth-key(default value:none) | NTP symmetric key, used for authentication between the NTP client and server. Key Identifier (Key ID) - an integer identifying the cryptographic key used to generate the message-authentication code.
broadcast(yesorno; default value:no)
multicast(yesorno; default value:no)
manycast(yesorno; default value:no)
broadcast-addresses(IP address; default value: )
vrf(default: main)
use-local-clock(yesorno; default value:no)
local-clock-stratum
auth-key(default value:none)
# Log messages
SNTP client can produce the following log messages. See the article "log" on how to set up logging and how to inspect logs.
Explanation of log message fields
NOTE: the above logging rules work only with the built-in SNTP client, the separate NTP package doesn't have any logging facilities.