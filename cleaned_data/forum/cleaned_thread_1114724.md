# Thread Information
Title: Thread-1114724
Section: RouterOS
Thread ID: 1114724

# Discussion

## Initial Question
Hi guys, oh my god, sorry that i have to say, that mikrotik is driving me crazy. v7 and BFD has a long story and it looks like, the story will not end.First of all:It fails randomly without reproduction steps available. But mostly it will fail when BGP/BFD neighbor was lost and is trying to reconnect.What is the issue:after rebooting a neighbor, bfd does some strange things. It tells that the remote actual tx or rx is 2.0000s (2s), but it is configured as 0.50000s (500ms). Sometimes it tells 0.00001s (1µs) what is not possible on an ethernet interface.Nothing helps to resolve that issue as ´disable / re-enable bfd for that interface. disable / re-enable BGP neighbor. Only rebooting the router helps in 95% the time.After rebooting, IPv4 BFD and BGP-Peers went into running end established state. But IPv6 will not. Disable BFD on the BGP-Neighbor brings the routing table instead installed.Peer is a JUNIPER MX204.In the console it shows µs instead of ms.Screenshot 2024-12-13 085940.jpgScreenshot 2024-12-13 085922.jpg26a4ad33-f4f2-440f-a9d5-f4a9994ac50d.jpg ---

## Response 1
sometimes when issuing/routing/bfd/sessions/printthe CLI hangs. I have to reboot the router. ---