# Document Information
Title: Back To Home
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/197984280/Back+To+Home,

# Content
# 2Overview2.1Enabling BTH using the app2.2Sharing the BTH connection with another phone user2.3Sharing the BTH tunnel with a computer via the WireGuard(TM) app2.4Configuring BTH manually in RouterOS (optional, if no smartphone is available to you)2.5Removing and disabling connections3Property reference3.1IP Cloud3.2Back to Home users
# Overview
Sub-menu:/ip cloudPackages required:routerosRouterOS version required:v7.12 and newerHardware requirements:ARM/ARM64/TILE architecture devices
```
/ip cloud
```
```
routeros
```
Back To Home is a convenience feature, that configures your device for secure VPN access from anywhere in the world to your router and your network, even if your router does not have a public IP address, is behind NAT or Firewall.
Configuration is done with MikroTik Back to Home app (Android,iPhone).
If the VPN server (your home router) has a public IP address, the VPN app will create a direct VPN connection between the phone and the router. However, if the router is not directly reachable from the internet, the connection will be made through the MikroTik relay servers.The connection is always end-to-end encrypted, the relay server or any other device does not have access to the encryption keys, in essence, the relay only helps your device to reach the router. The connection will appear as going out from your router, not from the relay.In case of going through relay, speed could be limited.
This feature is a convenient option to access your home network or view content available in your home country, from locations, where some content is not available.It is not meant for anonymity, it is for simple one click access to your home network. For more granular security controls, we recommend to manually configure and secure a VPN connection using the advanced RouterOS options.
# Enabling BTH using the app
To set up Back to Home, you should have a smartphone with the BTH app and should be inside your home, connected to your routers WiFi network.
|  |  |  |  | Tap "Create new" | Provide your router credentials | Connection established | Allow VPN to be added | If device is not supported, error is shown
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Tap "Create new"
Provide your router credentials
Connection established
Allow VPN to be added
If device is not supported, error is shown
# Sharing the BTH connection with another phone user
It is possible to create Guest tunnels for your friends and family. You can even specify if you want these people to access your local network as well, or if they should be restricted to only use the internet via your router. Once you create shared tunnels, you can send Invitation links via any chat application in your phone, or show a QR code to your friend in person (in both these cases, the friend will have to also install the BTH app). If you want to connect to your router via the WireGuard(TM) app from another phone or from a computer, it is possible as well. Just select the share WireGuard(TM) config file, and open this file in the WireGuard(TM) app.
|  |  |  |  |
---------------
Manage shares | Connect to your tunnel first | Once connected, Create shares | Provide a name and access level | Share sheet opens | Send the invite link via WhatsApp, Signal etc.
To share your tunnel with somebody:
# Sharing the BTH tunnel with a computer via the WireGuard(TM) app
Since there is no BTH app for PCs, you can useWireGuard(TM) appto connect to the shared tunnel. You can even share your connection with yourself, by "inviting" your computer to connect.
Let's make a new share, this time for yourself, for using from the PC.
|  |  |  |  |
---------------
Create | Specify name and access level | You have two shares now | Click "..." to send invite | Pick "Share WireGuard config  file" | AirDrop to your macOS or e-mail the file
Install the WireGuard app in your computer and click "Import Tunnel from file"
# Configuring BTH manually in RouterOS (optional, if no smartphone is available to you)
```
/ip/cloud/set ddns-enabled=yes
```
```
/ip/cloud/set back-to-home-vpn=enabled
```
```
/ip/cloud/print
```
```
vpn-wireguard-client-config-qrcode
```
```
vpn-wireguard-client-config
```
# Removing and disabling connections
In the smartphone app, the VPN configuration is added to the System VPN settings. In this regard, the Back to Home app only acts as a wizard. It supplies needed config to the operating system (this is why iPhone will warn you about altering system configuration).
To remove the created connection, go into the smartphone settings app and remove the VPN connections from there.
In the MikroTik router side, you should manually delete the added Peers in the Wireguard menu. Note that "revoke-and-disable" button can't be used to "Pause" the use of the Back to Home feature. Once you revoke-and-disable in RouterOS, all Peers will be disassociated from the Cloud / Relay servers, and you will have to re-create the connection from the Smartphone app. Therefore, once you have used the option "revoke-and-disable" in RouterOS IP Cloud menu, you need to also delete the Peers from the Wireguard menu, as they can't be re-used.
# Property reference
# IP Cloud
Sub-menu:/ip/cloud/
```
/ip/cloud/
```
Back to Home shares the menu with IP Cloud. Back to Home parameters:
Property | Description
----------------------
back-to-home-vpn(enabled | revoked-and-disabled; Default:revoked-and-disabled) | Enables or revokes and disables the Back to Home service. ddns-enabled has to be set to yes, for BTH to function.
vpn-dns-name(read-only: string) | Shows the DNS name assigned to the device. Name consists of product serial number appended by.vpn.mynetname.net. This field is visible only after at least one ddns-request is successfully completed.
vpn-port(read-only: integer) | Port used by BTH VPN.
vpn-status(read-only: string) | Contains text string that describes the current BTH state.
vpn-relay-rtts(read-only;"region (ip4: time(ms), ip6: time (ms)") | Round trip time in milliseconds for each available relay, values are shown both for IPv4 and IPv6.
vpn-relay-ipv4-status(read-only: string) | Status on connection to relay and detailed information about relay
vpn-relay-ipv6-status(read-only: string) | Status on connection to relay and detailed information about relay
vpn-relay-codes(read-only: string) | Available VPN relay codes, which can be referenced in vpn-prefer-relay-code. All available relays will be shown here.
vpn-relay-addressess(read-only: string) | IPv4 address of the relay
vpn-relay-addressess-ipv6(read-only: string) | IPv6 address of the relay
vpn-private-key(read-only: string) | Private key for BTH
vpn-public-key(read-only: string) | Public key for BTH
vpn-peer-private-key(read-only: string) | Peer private key
vpn-peer-public-key(read-only: string) | Peer public key
vpn-prefer-relay-code(string;) | You can enter relay code that will be preferred for BTH connection, if not set, relay with smallest RTT will be chosen.
vpn-interface(read-only: string) | Name of the created interface for Back to Home WireGuard®tunnel.
vpn-wireguard-client-config(read-only: string) | Configuration that can beentered in your preferred WireGuard® client. Only one client at a time will be available to use this config.
vpn-wireguard-client-config-qrcode(read-only) | Scannable QR Code for yourpreferred WireGuard® client. Only one client at a time will be available to use this config.
Enables or revokes and disables the Back to Home service. ddns-enabled has to be set to yes, for BTH to function.
Configuration that can beentered in your preferred WireGuard® client. Only one client at a time will be available to use this config.
Scannable QR Code for yourpreferred WireGuard® client. Only one client at a time will be available to use this config.
# Back to Home users
Sub-menu:/ip/cloud/back-to-home-users/
```
/ip/cloud/back-to-home-users/
```
Since RouterOS 7.14 there is a new back to home specific user manager available in the menu/ip/cloud/back-to-home-users>where you can see all the users that are added by the Back to Home mobile app, change their firewall preference and also add new ones.
```
/ip/cloud/back-to-home-users>
```
```
[boss@mikrotik-ax] /ip/cloud/back-to-home-users> print detailFlags: X - disabled; A - active0  A name="user1" slot=3 expires=never client-address=192.168.216.3/32,fc00:0:0:216::3/128 allow-lan=noprivate-key="OHqR2BZXJp0N6//3JzzoJhBJVb0rrSxV0dxQL/2UdXY=" public-key="Na7oEq9XLdeK8ouCUX+tC4FIM51vEnZ7mLiFqG9xiUQ="[boss@mikrotik-ax] /ip/cloud/back-to-home-users>
```
When adding users in this menu, you can view their Wireguard config and QR code with this command/interface/wireguard/peers/show-client-config user1
```
/interface/wireguard/peers/show-client-config user1
```
Allow-lan=nowill add the users into a firewall address list, that only allows internet access, but blocks the user from accessing your internal network. Note that expiry date can't be changed, once a user has been added.
```
A
```
```
llow-lan=no
```
Property | Description
----------------------
name(string) | Informative name of BTH user
expires(string; never | date:"YYYY-MM-DD HH:MM:SS";Default:never) | Expiration time and date for user, cannot be changed once user is created
client-addresss(string: IPv4 | IPv6) | Client address, if not specified one will be made automatically
allow-lan(string: yes | no; Default:no) | Will add the user into a firewall address list, that only allows internet access, but blocks the user from accessing your internal network
private-key(string;) | Private key for user, if not set manually, it will be generated by the system
public-key(string;) | Public key for user, if not set manually, it will be generated by the system
Informative name of BTH user
expires(string; never | date:"YYYY-MM-DD HH:MM:SS";
Default:never)
Expiration time and date for user, cannot be changed once user is created
Client address, if not specified one will be made automatically
Will add the user into a firewall address list, that only allows internet access, but blocks the user from accessing your internal network
Private key for user, if not set manually, it will be generated by the system
Public key for user, if not set manually, it will be generated by the system