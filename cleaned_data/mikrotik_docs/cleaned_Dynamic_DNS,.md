# Document Information
Title: Dynamic DNS
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/139067407/Dynamic+DNS,

# Content
# Introduction
```
/tool dns-update
```
Standards:RFC 2136, RFC 3007
```
RFC 2136, RFC 3007
```
Dynamic DNS Update Tool gives a way to keep the domain name pointing to a dynamic IP address. It works by sending a domain name system update requests to the name server, which has a zone to be updated. Secure DNS updates are also supported.
The DNS update tool supports only one algorithm -hmac-md5. It's the only proposed algorithm for signing DNS messages.
# Properties
Property | Description
----------------------
address(IP; Default:) | Defines the IP address associated with the domain name.
dns-server(IP; Default:) | DNS server to send updates to.
key(string; Default:) | Authorization key to access the server.
key-name(string; Default:) | Authorization key name (like a username) to access the server.
name(string; Default:) | Name to attach with the IP address.
ttl(integer; Default:) | Time to live for the item (in seconds).
zone(string; Default:) | DNS zone where to update the domain name in.
# Example
To tell 23.34.45.56 DNS server to (re)associate mydomain name in the myzone.com zone with 68.42.14.4 IP address specifying that the name of the key is dns-update-key and the actual key updates:
```
[admin@MikroTik] tool> dns-update dns-server=23.34.45.56 name=mydomain \
\... zone=myzone.com address=68.42.14.4 key-name=dns-update-key key=update
```