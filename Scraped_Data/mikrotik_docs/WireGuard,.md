---
title: WireGuard
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/69664792/WireGuard,
crawled_date: 2025-02-02T21:13:19.496469
section: mikrotik_docs
type: documentation
---

# Introduction
* 1Introduction
* 2Properties2.1Read-only properties
* 3Peers3.1Read-only properties
* 4Application examples4.1Site to Site WireGuard tunnel4.1.1WireGuard interface configuration4.1.2Peer configuration4.1.3IP and routing configuration4.1.4Firewall considerations
* 5RoadWarrior WireGuard tunnel5.1RouterOS configuration5.2iOS configuration5.3Windows 10 configuration
* 2.1Read-only properties
* 3.1Read-only properties
* 4.1Site to Site WireGuard tunnel4.1.1WireGuard interface configuration4.1.2Peer configuration4.1.3IP and routing configuration4.1.4Firewall considerations
* 4.1.1WireGuard interface configuration
* 4.1.2Peer configuration
* 4.1.3IP and routing configuration
* 4.1.4Firewall considerations
* 5.1RouterOS configuration
* 5.2iOS configuration
* 5.3Windows 10 configuration
WireGuard®is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec while avoiding massive headaches. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general-purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable.
# Properties
Property | Description
----------------------
comment(string; Default: ) | Short description of the tunnel.
disabled(yes | no; Default:no) | Enables/disables the tunnel.
listen-port(integer; Default: 13231) | Port for WireGuard service to listen on for incoming sessions.
mtu(integer [0..65536]; Default:1420) | Layer3 Maximum transmission unit.
name(string; Default: ) | Name of the tunnel.
private-key(string; Default: ) | A base64 private key. If not specified, it will be automatically generated upon interface creation.Each network interface has a private key and a list of peers.
## Read-only properties
Property | Description
----------------------
public-key(string) | A base64 public key is calculated from the private key.Each peer has a public key. Public keys are used by peers to authenticate each other. They can be passed around for use in configuration files.
running(yes | no) | Whether the interface is running.
Whether the interface is running.
# Peers
Property | Description
----------------------
allowed-address(IP/IPv6 prefix;Default: ) | List of IP (v4 or v6) addresses with CIDR masks from which incoming traffic for this peer is allowed and to which outgoing traffic for this peer is directed. This IP address has to be in the same subnet as WireGuard interface set on ROS. If WireGuard interface is at 192.168.99.1/24, You have to input 192.168.99.2 to the client. By adding this IP under 'Allowed Address', you are saying that only this specific client (phone for example) is permitted to connect to this peer configuration.Allowed-address range cannot overlap on one interface, so you need to set own range for each peer.
comment(string; Default: ) | Short description of the peer.
disabled(yes | no; Default:no) | Enables/disables the peer.
endpoint-address(IP/Hostname; Default: ) | The IP address or hostname. It is used by WireGuard to establish a secure connection between two peers.
endpoint-port(integer:0..65535; Default:) | The Endpoint port is the UDP port on which a WireGuard peer listens for incoming traffic.
interface(string; Default:) | Name of the WireGuard interface the peer belongs to.
persistent-keepalive(integer:0..65535; Default: 0) | A seconds interval, between 1 and 65535 inclusive, of how often to send an authenticated empty packet to the peer for the purpose of keeping a stateful firewall or NAT mapping valid persistently. For example, if the interface very rarely sends traffic, but it might at anytime receive traffic from a peer, and it is behind NAT, the interface might benefit from having a persistent keepalive interval of 25 seconds.
preshared-key(string; Default:) | A base64 preshared key. Optional, and may be omitted. This option adds an additional layer of symmetric-key cryptography to be mixed into the already existing public-key cryptography, for post-quantum resistance.Also can be generated automatically or entered manually, when the key is provided by the system administrator.
private-key(auto/none; Default:none) | A base64 private key.
public-key(string; Default:) | A base64 public key is calculated from the private key.Each peer has a public key. Public keys are used by peers to authenticate each other. They can be passed around for use in configuration files.
show-client-config | Will show already created Peer configuration and generate a QR code for easier peer setup on a client device. Does not affect the WireGuard Server.
Used for the client-server setup scenario, when the configuration is imported using a qr code for a client, configuration details on tab with qrcode will appear once it has been set in the fields:
client-address(IP/IPv6 prefix; Default: ) | Whenimported using a qr code for a client (for example, a phone), then this address for the wg interface is set on that device.
client-dns(IP/IPv6 prefix; Default: ) | Specify when using WireGuard Server as a VPN gateway for peer traffic.
client-endpoint(IP/IPv6 prefix; Default: ) | The IP address and port number of the WireGuard Server.
client-keepalive(integer:0..65535; Default: 0) | Same aspersistent-keepalivebut from peer side.
client-listen-port(integer:0..65535; Default:) | The local port upon which this WireGuard tunnel will listen for incoming traffic from peers, and the port from which it will source outgoing packets.
name(string; Default:) | Allows adding name to a peer. Name will be used as a reference for a peer in WireGuard logs. (Available from RouterOS version 7.15)
responder(yes | no; Default:no) | Specifies if peer is intended to be connection initiator or only responder. Should be used on WireGuard devices that are used as "servers" for other devices as clients to connect to. Otherwise router will all repeatedly try to connect "endpoint-address" or "current-endpoint-address".
public-key(string; Default:)
A base64 public key is calculated from the private key.Each peer has a public key. Public keys are used by peers to authenticate each other. They can be passed around for use in configuration files.
show-client-config
Will show already created Peer configuration and generate a QR code for easier peer setup on a client device. Does not affect the WireGuard Server.
Used for the client-server setup scenario, when the configuration is imported using a qr code for a client, configuration details on tab with qrcode will appear once it has been set in the fields:
client-address(IP/IPv6 prefix; Default: )
Whenimported using a qr code for a client (for example, a phone), then this address for the wg interface is set on that device.
client-dns(IP/IPv6 prefix; Default: )
Specify when using WireGuard Server as a VPN gateway for peer traffic.
client-endpoint(IP/IPv6 prefix; Default: )
The IP address and port number of the WireGuard Server.
client-keepalive(integer:0..65535; Default: 0)
Same aspersistent-keepalivebut from peer side.
client-listen-port(integer:0..65535; Default:)
The local port upon which this WireGuard tunnel will listen for incoming traffic from peers, and the port from which it will source outgoing packets.
name(string; Default:)
Allows adding name to a peer. Name will be used as a reference for a peer in WireGuard logs. (Available from RouterOS version 7.15)
responder(yes | no; Default:no)
Specifies if peer is intended to be connection initiator or only responder. Should be used on WireGuard devices that are used as "servers" for other devices as clients to connect to. Otherwise router will all repeatedly try to connect "endpoint-address" or "current-endpoint-address".
*AllowedIPsconfiguration that is provided to the client through WireGuard peer export (configuration file or QR code) can not be changed and will be "0.0.0.0/0, ::/0" at the moment. If it is necessary to change these values on remote end, then that is up to the remote peer software used for WireGuard connection.
## Read-only properties
Property | Description
----------------------
current-endpoint-address(IP/IPv6) | The most recent source IP address of correctly authenticated packets from the peer.
current-endpoint-port(integer) | The most recent source IP port of correctly authenticated packets from the peer.
last-handshake(integer) | Time in seconds after the last successful handshake.
rx(integer) | The total amount of bytes received from the peer.
tx(integer) | The total amount of bytes transmitted to the peer.
# Application examples
## Site to Site WireGuard tunnel
Consider setup as illustrated below. Two remote office routers are connected to the internet and office workstations are behind NAT. Each office has its own local subnet, 10.1.202.0/24 for Office1 and 10.1.101.0/24 for Office2. Both remote offices need secure tunnels to local networks behind routers.
### WireGuard interface configuration
First of all, WireGuard interfaces must be configured on both sites to allow automatic private and public key generation. The command is the same for both routers:
```
/interface/wireguard
add listen-port=13231 name=wireguard1
```
Now when printing the interface details, both private and public keys should be visible to allow an exchange.
Office1
```
/interface/wireguard print 
Flags: X - disabled; R - running 
 0  R name="wireguard1" mtu=1420 listen-port=13231 private-key="yKt9NJ4e5qlaSgh48WnPCDCEkDmq+VsBTt/DDEBWfEo=" 
      public-key="u7gYAg5tkioJDcm3hyS7pm79eADKPs/ZUGON6/fF3iI="
```
Office2
```
/interface/wireguard/print 
Flags: X - disabled; R - running 
 0  R name="wireguard1" mtu=1420 listen-port=13231 private-key="KMwxqe/iXAU8Jn9dd1o5pPdHep2blGxNWm9I944/I24=" 
      public-key="v/oIzPyFm1FPHrqhytZgsKjU7mUToQHLrW+Tb5e601M="
```
### Peer configuration
Peer configuration defines who can use the WireGuard interface and what kind of traffic can be sent over it. To identify the remote peer, its public key must be specified together with the created WireGuard interface.
Office1
```
/interface/wireguard/peers
add allowed-address=10.1.101.0/24,10.255.255.1/32 endpoint-address=192.168.80.1 endpoint-port=13231 interface=wireguard1 \
public-key="v/oIzPyFm1FPHrqhytZgsKjU7mUToQHLrW+Tb5e601M="
```
Office2
```
/interface/wireguard/peers
add allowed-address=10.1.202.0/24,10.255.255.2/32 endpoint-address=192.168.90.1 endpoint-port=13231 interface=wireguard1 \
public-key="u7gYAg5tkioJDcm3hyS7pm79eADKPs/ZUGON6/fF3iI="
```
### IP and routing configuration
Lastly, IP and routing information must be configured to allow traffic to be sent over the tunnel.
Office1
```
/ip/address
add address=10.255.255.1/30 interface=wireguard1
/ip/route
add dst-address=10.1.101.0/24 gateway=wireguard1
```
Office2
```
/ip/address
add address=10.255.255.2/30 interface=wireguard1
/ip/route
add dst-address=10.1.202.0/24 gateway=wireguard1
```
### Firewall considerations
The default RouterOS firewall will block the tunnel from establishing properly. The traffic should be accepted in the "input" chain before any drop rules on both sites.
Office1
```
/ip/firewall/filter
add action=accept chain=input dst-port=13231 protocol=udp src-address=192.168.80.1
```
Office2
```
/ip/firewall/filter
add action=accept chain=input dst-port=13231 protocol=udp src-address=192.168.90.1
```
Additionally, it is possible that the "forward" chain restricts the communication between the subnets as well, so such traffic should be accepted before any drop rules as well.
Office1
```
/ip/firewall/filter
add action=accept chain=forward dst-address=10.1.202.0/24 src-address=10.1.101.0/24
add action=accept chain=forward dst-address=10.1.101.0/24 src-address=10.1.202.0/24
```
Office2
```
/ip/firewall/filter
add action=accept chain=forward dst-address=10.1.101.0/24 src-address=10.1.202.0/24
add action=accept chain=forward dst-address=10.1.202.0/24 src-address=10.1.101.0/24
```
# RoadWarrior WireGuard tunnel
## RouterOS configuration
Add a new WireGuard interface and assign an IP address to it.
```
/interface wireguard
add listen-port=13231 name=wireguard1
/ip address
add address=192.168.100.1/24 interface=wireguard1
```
Adding a new WireGuard interface will automatically generate a pair of private and public keys. You will need to configure the public key on your remote devices. To obtain the public key value, simply print out the interface details.
```
[admin@home] > /interface wireguard print 
Flags: X - disabled; R - running 
 0  R name="wireguard1" mtu=1420 listen-port=13231 private-key="cBPD6JNvbEQr73gJ7NmwepSrSPK3np381AWGvBk/QkU=" 
      public-key="VmGMh+cwPdb8//NOhuf1i1VIThypkMQrKAO9Y55ghG8="
```
For the next steps, you will need to figure out the public key of the remote device. Once you have it, add a new peer by specifying the public key of the remote device and allowed addresses that will be allowed over the WireGuard tunnel.
```
/interface wireguard peers
add allowed-address=192.168.100.2/32 interface=wireguard1 public-key="<paste public key from remote device here>"
```
Firewall considerations
If you have default or strict firewall configured, you need to allow remote device to establish the WireGuard connection to your device.
```
/ip firewall filter
add action=accept chain=input comment="allow WireGuard" dst-port=13231 protocol=udp place-before=1
```
To allow remote devices to connect to the RouterOS services (e.g. request DNS), allow the WireGuard subnet in input chain.
```
/ip firewall filter
add action=accept chain=input comment="allow WireGuard traffic" src-address=192.168.100.0/24 place-before=1
```
Or simply add the WireGuard interface to "LAN" interface list.
```
/interface list member
add interface=wireguard1 list=LAN
```
## iOS configuration
Download the WireGuard application from the App Store. Open it up and create a new configuration from scratch.
First of all give your connection a "Name" and choose to generate a keypair. The generated public key is necessary for peer's configuration on RouterOS side.
Specify an IP address in "Addresses" field that is in the same subnet as configured on the server side. This address will be used for communication. For this example, we used 192.168.100.1/24 on the RouterOS side, you can use 192.168.100.2 here.
If necessary, configure the DNS servers. If allow-remote-requests is set to yes under IP/DNS section on the RouterOS side, you can specify the remote WireGuard IP address here.
Click "Add peer" which reveals more parameters.
The "Public key" value is the public key value that is generated on the WireGuard interface on RouterOS side.
"Endpoint" is the IP or DNS with port number of the RouterOS device that the iOS device can communicate with over the Internet.
"Allowed IPs" are set to 0.0.0.0/0 to allow all traffic to be sent over the WireGuard tunnel.
```
Depending on your configuration, you may need to add a NAT rule
chain=dstnat action=dst-nat to-ports=port protocol=udp in-interface=interface dst-port=port
```
## Windows 10 configuration
Download WireGuard installer from WireguardRun as Administrator.
Press Ctrl+n to add new empty tunnel, add name for interface, Public key should be auto generated copy it to RouterOS peer configuration.Add to server configuration, so full configuration looks like this (keep your auto generated PrivateKey in [Interface] section:
```
[Interface]
PrivateKey = your_autogenerated_private_key=
Address = 192.168.100.2/24
DNS = 192.168.100.1
[Peer]
PublicKey = your_MikroTik_public_KEY=
AllowedIPs = 0.0.0.0/0
Endpoint = example.com:13231
```
Save and Activate