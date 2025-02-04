# Document Information
Title: First Time Configuration
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328151/First+Time+Configuration,

# Content
# Connecting to the Router
There are two types of routers:
For additional details regarding the current default configuration, please refer to the Quick Guide document provided with your device. This document outlines which ports to initially utilize for connection and instructions on device setup.
This document describesthe step-by-step process for configuring the device from scratch. Therefore, we recommend clearing all defaults when initiating the setup.
When connecting the first time to the router with the default usernameadminandno password(or, for some models, check user and wireless passwords on the sticker).Upon the initial boot, a notification will appear, offering you the choiceto either remove the default configuration(even if the default config has only an IP address), leading to a reboot with no configuration applied, or to "Show Script" and retain the current default configuration, applying it accordingly.Since this article assumes that there is no configuration on the router, you should remove it by pressing "r" on the keyboard when prompted or click on the"Remove Configuration"button in WinBox.
# Router without Default Configuration
If the router doesn't have a default configuration, there are multiple options to consider. However, in this case, we'll opt for a method that best fits our requirements.
Connect the ISP cable tothe router's ether1 port and connect your PCto any port except ether1.Then, launch WinBox and search for your router using the neighbor discovery feature.See detailed example inWinbox article.
If the router appears in the list, select its MAC address and clickConnect.
The easiest method to ensure a completely clean router is to run the CLI command
```
/system reset-configuration no-defaults=yes skip-backup=yes
```
Or from WinBox:
# Configuring IP Access
As MAC connection can sometimes be unreliable, our first step is to configure the router to enable IP connectivity:
Setting up the bridge and assigning an IP address are straightforward processes:
```
/interface bridge add name=bridge1
/interface bridge port add interface=ether2 bridge=bridge1
/ip address add address=192.168.88.1/24 interface=bridge1
```
If you prefer WinBox/WebFig as configuration tools:
Next, proceed with setting up a DHCP server.To simplify and expedite this process, we'll execute thesetupcommand.
```
[admin@MikroTik] > ip dhcp-server/ setup [enter]
Select interface to run DHCP server on
dhcp server interface: bridge1 [enter]
Select network for DHCP addresses
dhcp address space: 192.168.88.0/24 [enter]
Select gateway for given network
gateway for dhcp network: 192.168.88.1 [enter]
Select pool of ip addresses given out by DHCP server
addresses to give out: 192.168.88.2-192.168.88.254 [enter]
Select DNS servers
dns servers: 192.168.88.1 [enter]
Select lease time
lease time: 1800 [enter]
```
Notice that most of the configuration options are automatically determined and you just simply need to hit the enter key.
The setup tool is also accessible in WinBox/WebFig:
Following these steps, the connected PC should now obtain a dynamic IP address. You can then close Winbox and reconnect to the router using the IP address (192.168.88.1).
# Configuring Internet Connection
To enable internet access for the router, you'll need to configure one of the following common types of internet connections:
# Dynamic Public IP
Dynamic address configuration is the easiest option. Simply set up a DHCP client on the public interface. The DHCP client will obtain information from your Internet Service Provider (ISP), such as an IP address, DNS servers, NTP servers, and default route, making the setup process straightforward for you.
```
/ip dhcp-client add disabled=no interface=ether1
```
After adding the client you should see the assigned address and status should be bound
```
[admin@MikroTik] > ip dhcp-client print
Columns: INTERFACE, USE-PEER-DNS, ADD-DEFAULT-ROUTE, STATUS, ADDRESS
# INTERFACE  USE-PEER-DNS  ADD-DEFAULT-ROUTE  STATUS  ADDRESS
0 ether1     yes           yes                bound   1.2.3.100/24
```
# Static Public IP
When configuring a static address, your ISP provides specific parameters, such as:
These are three basic parameters that you need to get the internet connection working.
To configure this in RouterOS, we'll manuallyadd an IP address, add a default route with a provided gateway, and set up a DNS server
```
/ip address add address=1.2.3.100/24 interface=ether1
/ip route add gateway=1.2.3.1
/ip dns set servers=8.8.8.8
```
# PPPoE Connection
PPPoE connection also gives you a dynamic IP address and can configure dynamically DNS and default gateway. Typically service provider (ISP) gives you a username and password for the connection
```
/interface pppoe-client
add disabled=no interface=ether1 user=me password=123 \
add-default-route=yes use-peer-dns=yes
```
Winbox/WebFig actions:
# Verify Connectivity
Once the configuration is complete, you should be able to access the internet from the router.To verify IP connectivity, try pinging a known IP address, such as a Google DNS server.
```
[admin@MikroTik] > /ping 8.8.8.8
SEQ HOST                                     SIZE TTL TIME       STATUS
0 8.8.8.8                                    56  55 14ms399us
1 8.8.8.8                                    56  55 18ms534us
2 8.8.8.8                                    56  55 14ms384us
```
Verify DNS request
```
[admin@MikroTik] > /ping google.com
SEQ HOST                                     SIZE TTL TIME       STATUS
0 142.250.74.14                              56  55 14ms475us
1 142.250.74.14                              56  55 14ms308us
2 142.250.74.14                              56  55 14ms238us
```
If all settings are configured correctly, both pings should succeed.If there's a failure, please refer to theTroubleshootingsectionfor assistance.
# Protecting the Router
As the router is now accessible worldwide, it's important to protect it from potential intruders and basic attacks.
# User Password Access
For MikroTik routers, it's essential to set up passwords. We recommend using a password generator tool to create robust passwords that meet the following criteria:
```
/user set 0 password="!={Ba3N!40TуX+GvKBzjTLIUcx/,"
```
Another method to set a password for the current user:
```
/password
```
We highly recommend using a secondary method or the Winbox interface to update your router's password, as an added measure to safeguard against unauthorized access.
```
[admin@MikroTik] > /password
old-password: ********
new-password: ****************************
confirm-new-password: ****************************
```
Ensure you remember the password!If it's forgotten, there's no way to recover it. You'll have to reset the configuration or reinstall the router system!
You can also add additional users with full or limited router access in the/usermenu
```
/user add name=myname password=mypassword group=full
/user remove admin
```
# MAC Connectivity Access
By default, the MAC server runs onallinterfaces. To restrict MAC connectivity from the WAN port, we'll disable the default all entry and add a LAN interface.
First, create an interface list:
```
[admin@MikroTik] > /interface list add name=LAN
```
Then, add your previously created bridge named "bridge1" to the interface list:
```
[admin@MikroTik] > /interface list member add list=LAN interface=bridge1
```
Apply newly created interface list to the MAC server:
```
[admin@MikroTik] > /tool mac-server set allowed-interface-list=LAN
```
Do the same for Winbox MAC access
```
[admin@MikroTik] > /tool mac-server mac-winbox set allowed-interface-list=LAN
```
Winbox/Webfig actions:
Do the same in theMACWinbox Servertab to block Mac Winbox connections from the internet.
# Neighbor Discovery
MikroTik Neighbor discovery protocol is used to show and recognize other MikroTik routers in the network. Disable neighbor discovery on public interfaces:
```
/ip neighbor discovery-settings set discover-interface-list=LAN
```
# IP Connectivity Access
While the firewall protects your router from unauthorized access by external networks, it's also possible to restrict username access based on specific IP addresses
```
/user set 0 address=x.x.x.x/yy
```
x.x.x.x/yy - your IP or network subnet that is allowed to access your router.
IP connectivity on the public interface must be limited in the firewall. We will accept only ICMP(ping/traceroute), IP Winbox, and ssh access.
```
/ip firewall filter
add chain=input action=accept connection-state=established,related,untracked comment="accept established,related,untracked"
add chain=input action=drop connection-state=invalid comment="drop invalid"
add chain=input in-interface=ether1 action=accept protocol=icmp comment="accept ICMP"
add chain=input in-interface=ether1 action=accept protocol=tcp port=8291 comment="allow Winbox";
add chain=input in-interface=ether1 action=accept protocol=tcp port=22 comment="allow SSH";
add chain=input in-interface=ether1 action=drop comment="block everything else";
```
The first rule accepts packets from already established connections, assuming they are safe to not overload the CPU. The second rule drops any packet that connection tracking identifies as invalid.After that, we set up typical accept rules for specific protocols.
If you are using Winbox/WebFig for configuration, here is an example of how to add an established/related/untracked rule:
To add additional rules, click on the "+" button for each new rule and fill in the same parameters as provided in the console example.
# Administrative Services
Although the firewall protects the router from the public interface, you may still want to disable RouterOS services.
Most of RouterOS administrative tools are configured at  the/ip servicemenu
Keep only secure ones,
```
/ip service disable telnet,ftp,www,api
```
Change default service ports, this will immediately stop most of the random SSH brute force login attempts:
```
/ip service set ssh port=2200
```
Additionally, each service can be secured by allowed IP address or address range(the address service will reply to), although more preferred method is to block unwanted access in firewall because the firewall will not even allow to open socket
```
/ip service set winbox address=192.168.88.0/24
```
# Other Services
A bandwidth server is used to test throughput between two MikroTik routers. Disable it in the production environment.
```
/tool bandwidth-server set enabled=no
```
A router might have DNS cache enabled, which decreases resolving time for DNS requests from clients to remote servers. In case DNS cache is not required on your router or another router is used for such purposes, disable it.
```
/ip dns set allow-remote-requests=no
```
Some RouterBOARDs have an LCD module for informational purposes, set pin or disable it.
```
/lcd set enabled=no
```
It is good practice to disable all unused interfaces on your router, in order to decrease unauthorized access to your router.
```
/interface print
/interface set x disabled=yes
```
Where "X" is a number of theunused interfaces.
RouterOS utilizes stronger crypto for SSH, most newer programs use it, to turn on SSH strong crypto:
```
/ip ssh set strong-crypto=yes
```
Following services are disabled by default,  nevertheless, it is better to make sure that none of then were enabled accidentally:
```
/ip proxy set enabled=no
```
```
/ip socks set enabled=no
```
```
/ip upnp set enabled=no
```
```
/ip cloud set ddns-enabled=no update-time=no
```
# NAT Configuration
At this point, PC is not yet able to access the Internet, because locally used addresses are not routable over the Internet. Remote hosts simply do not know how to correctly reply to your local address.
The solution for this problem is to change the source address for outgoing packets to routers public IP. This can be done with the NAT rule:
```
/ip firewall nat
add chain=srcnat out-interface=ether1 action=masquerade
```
Another benefit of such a setup is that NATed clients behind the router are not directly connected to the Internet, that way additional protection against attacks from outside mostly is not required.
# Port Forwarding
Some client devices may need direct access to the internet over specific ports. For example, a client with an IP address 192.168.88.254 must be accessible by Remote desktop protocol (RDP).
After a quick search on Google, we find out that RDP runs on TCP port 3389. Now we can add a destination NAT rule to redirect RDP to the client's PC.
```
/ip firewall nat
add chain=dstnat protocol=tcp port=3389 in-interface=ether1 \
action=dst-nat to-address=192.168.88.254
```
# Setting up Wireless
For ease of use bridged wireless setup will be made so that your wired hosts are in the same Ethernet broadcast domain as wireless clients.
The important part is to make sure that our wireless is protected, so the first step is the security profile.
Security profiles are configured from/interface wireless security-profilesmenu in a terminal.
```
/interface wireless security-profiles
```
```
/interface wireless security-profiles
add name=myProfile authentication-types=wpa2-psk mode=dynamic-keys \
wpa2-pre-shared-key=1234567890
```
in Winbox/Webfig click onWirelessto open wireless windows and choose theSecurity Profiletab.
If there are legacy devices that do not support WPA2 (like Windows XP), you may also want to allow WPA protocol.
Now when the security profile is ready we can enable the wireless interface and set the desired parameters
```
/interface wireless
enable wlan1;
set wlan1 band=2ghz-b/g/n channel-width=20/40mhz-Ce distance=indoors \
mode=ap-bridge ssid=MikroTik-006360 wireless-protocol=802.11 \
security-profile=myProfile frequency-mode=regulatory-domain \
set country=latvia antenna-gain=3
```
To do the same from Winbox/Webfig:
The last step is to add a wireless interface to a local bridge, otherwise connected clients will not get an IP address:
```
/interface bridge port
add interface=wlan1 bridge=bridge1
```
Now wireless should be able to connect to your access point, get an IP address, and access the internet.
# Protecting the Clients
Now it is time to add some protection for clients on our LAN. We will start with a basic set of rules.
```
/ip firewall filter
add chain=forward action=fasttrack-connection connection-state=established,related \
comment="fast-track for established,related";
add chain=forward action=accept connection-state=established,related \
comment="accept established,related";
add chain=forward action=drop connection-state=invalid
add chain=forward action=drop connection-state=new connection-nat-state=!dstnat \
in-interface=ether1 comment="drop access to clients behind NAT from WAN"
```
A ruleset is similar to input chain rules (accept established/related and drop invalid), except the first rule withaction=fasttrack-connection. This rule allows established and related connections to bypass the firewall and significantly reduce CPU usage.
```
action=fasttrack-connection
```
Another difference is the last rule which drops all new connection attempts from the WAN port to our LAN network (unless DstNat is used). Without this rule, if an attacker knows or guesses your local subnet, he/she can establish connections directly to local hosts and cause a security threat.
For more detailed examples on how to build firewalls will be discussed in the firewall section.
# Blocking Unwanted Websites
Sometimes you may want to block certain websites, for example, deny access to entertainment sites for employees, deny access to porn, and so on. This can be achieved by redirecting HTTP traffic to a proxy server and use an access-list to allow or deny certain websites.
First, we need to add a NAT rule to redirect HTTP to our proxy. We will use RouterOS built-in proxy server running on port 8080.
```
/ip firewall nat
add chain=dst-nat protocol=tcp dst-port=80 src-address=192.168.88.0/24 \
action=redirect to-ports=8080
```
Enable web proxy and drop some websites:
```
/ip proxy set enabled=yes
/ip proxy access add dst-host=www.facebook.com action=deny
/ip proxy access add dst-host=*.youtube.* action=deny
/ip proxy access add dst-host=:vimeo action=deny
```
Using Winbox:
# Troubleshooting
RouterOS has built-in various troubleshooting tools, like ping, traceroute, torch, packet sniffer, bandwidth test, etc.
We already used the ping tool in this article toverify internet connectivity.
# Troubleshoot if ping fails
The problem with the ping tool is that it says only that destination isunreachable, but no more detailed information is available. Let's overview the basic mistakes.
You cannot reachwww.google.comfrom your computer which is connected to a MikroTik device: