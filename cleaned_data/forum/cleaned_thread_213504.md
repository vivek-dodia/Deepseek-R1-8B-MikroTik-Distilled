# Thread Information
Title: Thread-213504
Section: RouterOS
Thread ID: 213504

# Discussion

## Initial Question
Hi all, I'm trying to connect my Android to my LAN via Wireguard. My main router is 6.x.x and can't be upgraded to 7 easily so have opted to setup another Tik on the LAN (it's a WAP-ax). I've forwarded the UDP 13231 from the WAN router to the LAN Tik LAN IP 192.168.88.107/24 and added the fw filter rule to accept input on that udp port.On the WAP-ax i've setup then Wireguard interface and peer with IP 192.168.100.1/24, added fw filter on the input chain to accept the udp 13231 as well.When connecting the Android from the WAN side the connection succeeds and I see packets move through the WAN router and hit the WAP-ax but cannot ping anything at all.In know i'm missing something, so any help appreciated ---

## Response 1
My Guess is that the devices on your LAN are receiving a packet from 192.168.100.1/24 and sending their reply back to themain gateway. (Which also doesn't know where 192.168.100.1/24 is)One simple(ish) option might be to masquerade packets leaving your Wap-ax with source address of 192.168.100.0/24 to appear to come from the 192.168.88.107 address.Another option might be to add a static route on your main gateway to 192.168.100.1/24 via 192.168.88.107/24In this case You may also need to fiddle with the default drop invalid packets firewall rule. (The packets go direct from the wap ax to device, but come back from the device to wap ax via the main gateway, and main gateway sees only one half of the connection and may drop them as invalid) ---

## Response 2
Thanks for your reply. The static route on the main router was half the solution, the other half was to put the private and public keys in the correct fieldsOther than that the setup was pretty straight forward ---