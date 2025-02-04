# Document Information
Title: RADIUS
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328097/RADIUS,

# Content
# Summary
RADIUS, short for Remote Authentication Dial-In User Service, is a remote server that provides authentication and accounting facilities to various network appliances. RADIUS authentication and accounting allows the ISP or network administrator to manage PPP user access and accounting from one server throughout a large network. The MikroTik RouterOS has a RADIUS client that can authenticaterouter's localusers,HotSpot,PPP,PPPoE,PPTP,L2TP,OVPN,SSTP,IPsecand ISDN connections. The attributes received from the RADIUS server override the ones set in the default profile, but if some parameters are not received they are taken from the respective default profile.
The RADIUS server database is consulted only if no matching user access record is found in the router's local database.
If RADIUS accounting is enabled, accounting information is also sent to the RADIUS server default for that service.
# RADIUS Client
Sub-menu:/radius
----------------
```
/radius
```
This sub-menu allows adding and removing RADIUS clients.
# Properties
Property | Description
----------------------
accounting-backup(yes | no; Default:no) | Whether the configuration is for the backup RADIUS server
accounting-port(integer [1..65535]; Default:1813) | RADIUS server port used for accounting
address(IPv4/IPv6 address; Default:0.0.0.0) | IPv4 or IPv6 address of RADIUS server.The following formats are accepted:-ipv4-ipv4@vrf-ipv6-ipv6@vrf
authentication-port(integer [1..65535]; Default:1812) | RADIUS server port used for authentication.
called-id(string; Default: ) | Value depends on Point-to-Point protocol: PPPoE - service name, PPTP - server's IP address, L2TP - server's IP address.
certificate(string; Default: ) | Certificate file to use for communicating with RADIUS Server with RadSec enabled.
comment(string; Default: ) |
disabled(yes | no; Default:no) |
domain(string; Default: ) | Microsoft Windows domain of client passed to RADIUS servers that require domain validation.
protocol(radsec | udp; Default:udp) | Specifies the protocol to use when communicating with the RADIUS Server.
require-message-auth(no | yes-for-request-respDefault:yes-for-request-resp) | Specifies if Message-Authenticator attributes are required.
realm(string; Default: ) | Explicitly stated realm (user domain), so the users do not have to provide proper ISP domain name in the user name.
secret(string; Default: ) | The shared secret used to access the RADIUS server.
service(ppp|login|hotspot|wireless|dhcp|ipsec|dot1x; Default: ) | Router services that will use this RADIUS server:hotspot - HotSpot authentication servicelogin - router's local user authenticationppp - Point-to-Point clients authenticationwireless - wireless client authenticationdhcp - DHCP protocol client authentication (client's MAC address is sent as User-Name)ipsec - ipsec client authentificationdot1x - dot1x authentification
src-address(ipv4/ipv6 address; Default:0.0.0.0) | Source IP/IPv6 address of the packets sent to the RADIUS server
timeout(time; Default:100ms) | Timeout after which the request should be resent, for example, "/radius set timeout=300ms numbers=0"
IPv4 or IPv6 address of RADIUS server.
The following formats are accepted:
-ipv4-ipv4@vrf-ipv6-ipv6@vrf
```
@
```
```
@
```
# Example
To set up a RADIUS Client for HotSpot and PPP services that will authenticate against a RADIUS Server (10.0.0.3), you need to do the following:
```
[admin@MikroTik] > /radius add service=hotspot,ppp address=10.0.0.3 secret=ex
[admin@MikroTik] > /radius print
Flags: X - disabled
# SERVICE CALLED-ID DOMAIN ADDRESS SECRET
0 ppp,hotspot
```
To set up a RADIUS Client with RadSec, you need to do the following:
```
[admin@MikroTik] > /radius add service=hotspot,ppp address=10.0.0.3 secret=radsec protocol=radsec certificate=client.crt
[admin@MikroTik] > /radius print
Flags: X - disabled
# SERVICE CALLED-ID DOMAIN ADDRESS SECRET
0 ppp,hotspot 10.0.0.3 radsec
```
To view RADIUS Client statistics, you need to do the following:
```
[admin@MikroTik] > /radius monitor 0
pending: 0
requests: 10
accepts: 4
rejects: 1
resends: 15
timeouts: 5
bad-replies: 0
last-request-rtt: 0s
```
Make sure you enable RADIUS authentication for the desired services:
```
/ppp aaa set use-radius=yes
/ip hotspot profile set default use-radius=yes
```
# Connection Terminating from RADIUS
Sub-menu:/radius incoming
-------------------------
Sub-menu:/radius incoming
```
/radius incoming
```
This facility supports unsolicited messages sent from the RADIUS server. Unsolicited messages extend RADIUS protocol commands, that allow terminating a session that has already been connected from the RADIUS server. For this purpose, DM (Disconnect-Messages) is used. Disconnect messages cause a user session to be terminated immediately.
# Properties
Property | Description
----------------------
accept(yes | no; Default:no) | Whether to accept unsolicited messages
port(integer; Default:1700) | The port number to listen for the requests on
vrf(VRF name; default value:main) | Set VRF on which service is listening for incoming connections
vrf(VRF name; default value:main)