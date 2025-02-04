# Thread Information
Title: Thread-1120116
Section: RouterOS
Thread ID: 1120116

# Discussion

## Initial Question
Hello, I have 4 WANether1 : 192.168.1.11/24ether2: 192.168.2.11/24ether3: 192.168.3.11/24ether4: 192.168.4.11/24and i have L2tp public 93.93.93.1I want all ethernet could use the same vpn !Notic when i make ip route 93.93.93.1 to GT 192.168.1.1 the vpn will get ping and works fine but only works on ether1I need the l2tp works for all ethernetThe nat and pcc mangle are already done ---

## Response 1
Sorry, I don't understand what you want to achieve. Is it correct that you have got a single account from a VPN provider, that account is associated with a fixed public address, and you want the L2TP transport packets to be distributed among all the four WANs in order to aggregate the bandwidth of the WANs? ---

## Response 2
I wan getting the vpn ip connect for all wans without set ip route public/gt ---