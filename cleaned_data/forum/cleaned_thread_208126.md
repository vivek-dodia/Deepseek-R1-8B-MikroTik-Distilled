# Thread Information
Title: Thread-208126
Section: RouterOS
Thread ID: 208126

# Discussion

## Initial Question
Hello!I have L2TP Server on my Routerboard is up and running. RouterOS is 6.48.6. Clients can connect to the server using the ipv4 address. But clients can't connect to the server using its ipv6 address. For the testing purposes I've set up the OpnVPN server on the same Routerboard and clients can connect to it using Routerboards IPv6 address.What can be wrong with my setup? Can IPv6 be used as server address for L2TP connection anyway? ---

## Response 1
Tried the same yesterday and extended the IPv4 configuration with IPv6. The goal was, that clients can connect to the L2TP/IPSec server via IPv6. The LAN and Tunnel side remain unchanged. Clients (Windows 10) can connect via IPv4, but not via IPv6. The only change on the clientside is the IP address, to which it will connect.The connection is established until the point, where the LCP config request is sent. The connection stuck there, the config requests are repeated a couple of times and the the connection is terminated. That's what the log says. Very strange...edit: Router OS 7.16.1 ---

## Response 2
Without a config we can't tell anything:/export file=anynameyouwish (minus sensitive info) ---

## Response 3
Have to report back later. The export command of the IPSec section times out... Must have something to do with, that the whole IPSec section is broken on that device, since today... (viewtopic.php?p=1119492#p1119492).I don't know. The ROS stability is weak since last month. In December 2024 the routing on two devices partially stopped working, without any changes before. While searching for the cause, and (de)activating some routes in this process, everything get back to normal. A comparison of the configurations before and after shows not a single difference. MT support ticket is still open and untouched by MT. Then this strange behavior with IPv6 yesterday and since today the broken IPSec section, where any export or print of that section fails. ---