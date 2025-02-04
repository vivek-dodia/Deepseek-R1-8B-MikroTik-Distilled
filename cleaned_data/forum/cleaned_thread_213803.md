# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213803

# Discussion

## Initial Question
Author: [SOLVED]Thu Jan 09, 2025 9:18 pm
``` /ip firewall nataddchain=dstnat action=dst-nat to-addresses=10.0.0.69protocol=udp src-address=!10.0.0.69dst-address=!10.0.0.69dst-port=53addchain=dstnat action=dst-nat to-addresses=10.0.0.69protocol=tcp src-address=!10.0.0.69dst-address=!10.0.0.69dst-port=53 ``` Block both 53 and 853, both UDP and TCP. Be aware that DoH won't be blocked this way (but probably most IoT devices will only perform "normal" DNS requests).In addition, you could also redirect all outbound DNS requests to your router DNS server (where you have to replace the IP address by your routers IP address):