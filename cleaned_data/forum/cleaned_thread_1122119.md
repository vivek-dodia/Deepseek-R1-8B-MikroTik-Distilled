# Thread Information
Title: Thread-1122119
Section: RouterOS
Thread ID: 1122119

# Discussion

## Initial Question
My brand new Tenda N301 as AP doesnt work properlyI bought a brand new Tenda N301 Wireless Router which acts as an AP and in the configurations the operation mode is set to AP as well.I got a Mikrotik Router and I've made a Bridge and all ports eth2-4 are added.Previously I got another Access Point which worked well without problem. But my brand new Tenda N301 as AP doesnt work prorely.After connecting two devices (Mikrotik Router and Tenda AP) via a cable the connection repeatedly gets connected/disconnected.The Wires and Devices all are brand new and we got no hardware problems.Note: If Tenda N301 operation mode is set to 'Router' (not AP) it works good and It gets an IP from Mikrotik DHCP server and serves as a Router but I need all devises connected to Tenda (wire and wifi) get an IP directly from Mikrotik Router (Access Point) and be managable from Mikrotik Router.I noticed that even in AP Mode (tenda) it tries to assign devices its local ip addresses and doesnt use mikrotik dhcp server. theres no option for dhcp in AP mode. Do you think its a bug for Tenda device or what? ---

## Response 1
provide a link to the correct tenda manual (user guide) and I will look. ---

## Response 2
Previously I got another Access Point which worked well without problem. But my brand new Tenda N301 as AP doesnt work prorely.After connecting two devices (Mikrotik Router and Tenda AP) via a cable the connection repeatedly gets connected/disconnected.Note: If Tenda N301 operation mode is set to 'Router' (not AP) it works good and It gets an IP from Mikrotik DHCP server and serves as a Router but I need all devises connected to Tenda (wire and wifi) get an IP directly from Mikrotik Router (Access Point) and be managable from Mikrotik Router.I noticed that even in AP Mode (tenda) it tries to assign devices its local ip addresses and doesnt use mikrotik dhcp server. theres no option for dhcp in AP mode. Do you think its a bug for Tenda device or what?Hello, I Have the Exact Same Problem, i Run a hotspot on my router and My 2 tenda (AP mode) disconnected from the DHCP server. for this problem, I added them into the ip binding but the most important problem is when my router got reset ( for any reason ) those ap try to become the bad guy and start DHCP server and all of my clients get ip from 0.0/24 range. this is so annoying and I do not know what is this. did you find any solution? ---

## Response 3
I have same problem. Can anyone have solution? ---

## Response 4
Post a link to the manual for your device, we use MT not tenda devices!!! ---

## Response 5
I have same problem. Can anyone have solution?Hello! You also have 2 devices, one of which is a Mikrotik and the other is an access point from another manufacturer? Is the Mikrotik connected to the ISP as the main one? Is the access point not set to ''router mode''? Usually, we configure the access point only in AP mode, not router. All IP addresses are assigned to it from the primary Mikrotik, where an IP pool has been created for this AP. We can separate Work Lan and Guest Lan with a firewall policy.To say something more precisely, we need to understand where which device is connected, etc. ---