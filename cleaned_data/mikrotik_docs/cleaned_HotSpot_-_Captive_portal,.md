# Document Information
Title: HotSpot - Captive portal
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/56459266/HotSpot+-+Captive+portal,

# Content
# Introduction
The MikroTik HotSpot Gateway provides authentication for clients before access to public networks.
# HotSpot Gateway features:
A hotspot can work reliably only when IPv4 is used. Hotspot relies on Firewall NAT rules which currently are not supported for IPv6.
# Example
```
[admin@MikroTik] /ip hotspot> setup
Select interface to run HotSpot on
hotspot interface: ether3
Set HotSpot address for interface
local address of network: 10.5.50.1/24
masquerade network: yes
Set pool for HotSpot addresses
address pool of network: 10.5.50.2-10.5.50.254
Select hotspot SSL certificate
select certificate: none
Select SMTP server
ip address of smtp server: 0.0.0.0
Setup DNS configuration
dns servers: 10.1.101.1
DNS name of local hotspot server
dns name: myhotspot
Create local hotspot user
name of local hotspot user: admin
password for the user:
[admin@MikroTik] /ip hotspot>
```
Verify HotSpot configuration:
```
[admin@MikroTik] /ip hotspot> print
Flags: X - disabled, I - invalid, S - HTTPS
# NAME INTERFACE ADDRESS-POOL PROFILE IDLE-TIMEOUT
0 hotspot1 ether3 hs-pool-3 hsprof1 5m
[admin@MikroTik] /ip hotspot>
[admin@MikroTik] /ip pool> print
# NAME RANGES
0 hs-pool-3 10.5.50.2-10.5.50.254
[admin@MikroTik] /ip pool> /ip dhcp-server
[admin@MikroTik] /ip dhcp-server> print
Flags: X - disabled, I - invalid
# NAME INTERFACE RELAY ADDRESS-POOL LEASE-TIME ADD-ARP
0 dhcp1 ether3 hs-pool-3 1h
[admin@MikroTik] /ip dhcp-server> /ip firewall nat
[admin@MikroTik] /ip firewall nat> print
Flags: X - disabled, I - invalid, D - dynamic
0 X ;;; place hotspot rules here
chain=unused-hs-chain action=passthrough
1 ;;; masquerade hotspot network
chain=srcnat action=masquerade src-address=10.5.50.0/24
[admin@MikroTik] /ip firewall nat>
```
# Parameters asked during the setup process
Parameter | Description
-----------------------
hotspot interface(string; Default:allow) | Interface name on which to run HotSpot. To run HotSpot on a bridge interface, make sure public interfaces are not included in the bridge ports.
local address of network(IP; Default:10.5.50.1/24) | HotSpot gateway address
masquerade network(yes | no; Default:yes) | Whether to masquerade HotSpot network, whenyesrule is added to/ip firewall natwithaction=masquerade
address pool of network(string; Default:yes) | Address pool for HotSpot network, which is used to change user IP address to a valid address. Useful if providing network access to mobile clients that are not willing to change their networking settings.
select certificate(none | import-other-certificate; Default: ) | Choose SSL certificate, when HTTPS authorization method is required.
ip address of smtp server(IP; Default:0.0.0.0) | The IP address of the SMTP server, where to redirect HotSpot's network SMTP requests (25 TCP port)
dns servers(IP; Default:0.0.0.0) | DNS server addresses used for HotSpot clients, configuration taken from/ip dnsmenu of the HotSpot gateway
dns name(string; Default:"") | the domain name of the HotSpot server, a full qualified domain name is required, for example,www.example.com
name of local hotspot user(string; Default:"admin") | username of one automatically created HotSpot user, added to/ip hotspot user
password for the user'(string; Default: ) | Password for automatically created HotSpot user
# IP HotSpot
```
/ip/hotspot
```
The menu is designed to manage the HotSpot servers of the router. It is possible to run HotSpot on Ethernet, wireless, VLAN, and bridge interfaces. One HotSpot server is allowed per interface. When HotSpot is configured on the bridge interface, set HotSpot interface as bridge interface, not as bridge port, do not add public interfaces to bridge ports. You can add HotSpot servers manually to the/ip/hotspotmenu, but it is advised to run/ip/hotspot/setup, which adds all necessary settings.
Parameters | Description
------------------------
name(text) | HotSpot server's name or identifier
address-pool(name/none; default:none) | address space used to change HotSpot clientanyIP address to a valid address. Useful for providing public network access to mobile clients that are not willing to change their networking settings
idle-timeout(time/none; default:5m) | period of inactivity for unauthorized clients. When there is no traffic from this client (literally client computer should be switched off), once the timeout is reached, a user is dropped from the HotSpot host list, its used address becomes available
keepalive-timeout(time/none; default:none) | Value of how long host can stay out of reach to be removed from the HotSpot
login-timeout(time/none; default:none) | Period of time after which if a host hasn't been authorized itself with a system the host entry gets deleted from host table. Loop repeats until the host logs in the system. Enable if there are situations where a host cannot log in after being too long in the host table unauthorized.
interface(name of an interface) | Interface to run HotSpot on
addresses-per-mac(integer/unlimited; default: 2) | Number of IP addresses allowed to be bind with the MAC address, when multiple HotSpot clients connected with one MAC-address
profile(name; default:default) | HotSpot server default HotSpot profile, which is located in/ip/hotspot/profile
Read-only
Parameters | Description
------------------------
keepalive-timeout (read-only; time) | The exact value of the keepalive-timeout, that is applied to the user. Value shows how long the host can stay out of reach to be removed from the HotSpot
# IP HotSpot Active
```
/ip/hotspot/active
```
HotSpot active menu shows all clients authenticated in HotSpot, the menu is informational (read-only) it is not possible to change anything here.
Parameters | Description
------------------------
server(read-only; name) | HotSpot server name client is logged in
user(read-only; name) | name of the HotSpot user
domain(read-only; text) | the domain of the user (if split from the username), a parameter is used only with RADIUS authentication
address(read-only; IP address) | The IP address of the HotSpot user
mac-address(read-only; MAC-address) | MAC-address of the HotSpot user
login-by(read-only; multiple-choice: cookie/http-chap/http-pap/https/mac/mac-cookie/trial) | the authentication method used by the HotSpot client
uptime(read-only; time) | current session time of the user, it is showing how long the user has been logged in
idle-time(read-only; time) | the amount of time the user has been idle
session-time-left(read-only; time) | the exact value of session-time, that is applied for the user. Value shows how long user is allowed to be online to be logged off automatically byuptimereached
idle-timeout(read-only; time) | the exact value of the user's idle-timeout
keepalive-timeout(read-only; time) | the exact value of the keepalive-timeout, that is applied for the user. Value shows how long the host can stay out of reach to be removed from the HotSpot
limit-bytes-in(read-only; integer) | value shows how many bytes received from the client, an option is active when the appropriate parameter is configured for HotSpot user
limit-bytes-out(read-only; integer) | value shows how many bytes send to the client, an option is active when the appropriate parameter is configured for HotSpot user
limit-bytes-total(read-only; integer) | value shows how many bytes total were send/received from the client, an option is active when the appropriate parameter is configured for HotSpot user
# IP HotSpot Host
```
/ip/hotspot/host
```
The host table lists all computers connected to the HotSpot server. The host table is informational and it is not possible to change any value there:
Parameters | Description
------------------------
mac-address(read-only; MAC-address) | HotSpot user MAC-address
address(read-only; IP address) | HotSpot client original IP address
to-address(read-only; IP address) | The new client address assigned by HotSpot might be the same as the originaladdress
server(read-only; name) | HotSpot server name client is connected to
bridge-port(read-only; name) | "/interface bridge port"the client is connected to, value is unknown when HotSpot is not configured on the bridge
uptime(read-only; time) | value shows how long the user is online (connected to the HotSpot)
idle-time(read-only; time) | time user has been idle
idle-timeout(read-only; time) | value of the client idle-timeout (unauthorized client)
keepalive-timeout(read-only; time) | keepalive-timeout value of the unauthorized client
bytes-in(read-only; integer) | amount of bytes received from an unauthorized client
packet-in(read-only; integer) | amount of packets received from an unauthorized client
bytes-out(read-only; integer) | amount of bytes sent to an unauthorized client
packet-out(read-only; integer) | amount of packets sent to an unauthorized client
idle-timeout(read-only; time)
# IP Binding
```
/ip/hotspot/ip-binding
```
IP-Binding HotSpot menu allows to the setup of static One-to-One NAT translations, allows to bypass specific HotSpot clients without any authentication, and also allows to block specific hosts and subnets from the HotSpot network
Property | Description
----------------------
address(IP Range; Default:"") | The original IP address of the client
mac-address(MAC; Default:"") | MAC address of the client
server(string | all; Default:"all") | Name of the HotSpot server.all- will be applied to all hotspot servers
to-address(IP; Default:"") | New IP address of the client, translation occurs on the router (client does not know anything about the translation)
type(blocked | bypassed | regular; Default:"") | Type of the IP-binding actionregular- performs One-to-One NAT according to the rule, translatestheaddresstoto-addressbypassed- performs the translation, but excludes client from login to the HotSpotblocked- translation is not performed and packets from a host are dropped
# Cookies
The menu contains all cookies sent to the HotSpot clients, which are authorized by cookie method, all the entries are read-only.
```
/ip/hotspot/cookie
```
Property | Description
----------------------
domain(string) | The domain name (if split from the username)
expires-in(time) | How long the cookie is valid
mac-address(MAC) | Client's MAC-address
user(string) | HotSpot username
# Using DHCP option to advertise HotSpot URL
Most devices, such as modern smartphones, do some kind of background checking to see if they are behind a captive portal. They do this by requesting a known webpage and comparing the contents of that page, to what they should be. If contents are different, the device assumes there is a login page and creates a popup with this login page.
This does not always happen, as this "known webpage" could be blocked, whitelisted, or not accessible in internal networks. To improve on this mechanism, RFC 7710 was created, allowing the HotSpot to inform all DHCP clients that they are behind a captive-portal device and that they will need to authenticate to get Internet access, regardless of what webpages they do or do not request.
This DHCP option field is enabled automatically, but only if the router has a DNS name configured and has a valid SSL certificate (so that the login page can be accessed over HTTPS). When these requirements are met, a special DHCP option will be sent, containing a link tohttps://<dns-name-of-hotspot>/api. This link contains information in JSON format, instructing the client device of the captive portal status, and the location of the login page.
```
https://<dns-name-of-hotspot>/api
```
Contents ofhttps://<dns-name-of-hotspot>/apiare as follows:
```
https://<dns-name-of-hotspot>/api
```
```
{
"captive": $(if logged-in == 'yes')false$(else)true$(endif),
"user-portal-url": "$(link-login-only)",
$(if session-timeout-secs != 0)
"seconds-remaining": $(session-timeout-secs),
$(endif)
$(if remain-bytes-total)
"bytes-remaining": $(remain-bytes-total),
$(endif)
"can-extend-session": true
}
```
Some devices require venue-info URLas well, so you are free to modify the api.json file to your liking, just like any other hotspot files. It is located in the router files menu.