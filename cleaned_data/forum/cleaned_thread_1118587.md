# Thread Information
Title: Thread-1118587
Section: RouterOS
Thread ID: 1118587

# Discussion

## Initial Question
So far I love Chateau AX Pro big time, but it has a downside that makes maintenance very difficult. I always use static IP addresses + ARP for LAN/Ethernet devices with very strict firewall rules. I disable DHCP in Windows services and block broadcast packets in both directions.The problem is that this router doesn't see devices unless DHCP or FF:FF:FF:FF:FF:FF/255.255.255.255 packet is sent to it, even when static IP and MAC/ARP is already assigned in router settings. Windows Network Connection diagnostics shows that devices send packets to router, but do not receive any back, unless DHCP service is enabled and used. How do I go around that?This is the first router that has such a requirement and makes it very painful to connect new devices, especially if router is reset to stock. I have to wipe all firewall rules in Windows to enable DHCP packets and then re-import my static IP rules.Is there something I can do about it? Devices obviously send ARP packets/frames, but router doesn't respond to them unless DHCP is used. This is regardless of whether I use a browser or WinBox connection (via IP or MAC). ---

## Response 1
Bad, bad router?Or maybe - just maybe - there is the possibility that there could be something that needs to be changed in its configuration?If this latter could be the case, a good idea would be to post the current configuration for review (anonymizing the sensible data), instructions here:viewtopic.php?t=203686#p1051720 ---

## Response 2
The issue may be due to ARP cache handling on the Chateau AX Pro. To resolve it, try the following:1. **Enable ARP on Interfaces**: Ensure the router's LAN interfaces have `ARP` set to `enabled` (not `reply-only`) in `/interface ethernet`.2. **Static ARP Entries**: Manually add static ARP entries for devices in the router (`/ip arp add address=x.x.x.x mac-address=XX:XX:XX:XX:XX:XX interface=bridge`).3. **Bridge Settings**: Ensure the bridge has `use-ip-firewall` disabled unless explicitly needed, as this can interfere with ARP responses.4. **Firmware Update**: Check for any RouterOS updates as this might be a firmware-related issue.This should allow the router to recognize and respond to ARP requests without relying on DHCP. ---

## Response 3
Thanks! I've already had all that configured as you described (withoiut success), except for IP firewall. I assume bridge IP firewall is EBTables, correct? ---

## Response 4
Still a no-go. I set permanent ARP in both - router and Windows, but the same thing happens. Windows shows packets are sent, but none received. Router shows packets are received, but none sent back.Maybe this is a bug. I've never had this issue with other routers. I think developers should look into this. I use the latest test version of RouterOS. ---

## Response 5
Or maybe - just maybe - there is the possibility that there could be something that needs to be changed in its configuration?If this latter could be the case, a good idea would be to post the current configuration for review (anonymizing the sensible data), instructions here:viewtopic.php?t=203686#p1051720Actually, this is what you should do. ---

## Response 6
While waiting to see configuration export, just a comment: "static ARP" is calling for problems ... while it doesn't really provide any security (setting MAC address on interface is only too easy). ---