# Thread Information
Title: Thread-1122606
Section: RouterOS
Thread ID: 1122606

# Discussion

## Initial Question
I'm having trouble finding how to print the mac address table on devices that are not switches or do not have their ports under a bridge (interface ethernet switch host print, interface bridge host print). I'm specifically referring to an RB4011 and a CCR1072 running 7.16.2 (but I guess this goes for any other device not falling under what I described above). I don't want to do tool mac-scan because I want to do lookups by mac-address. Can you help me please? ---

## Response 1
/ip/arp/print/interface/bridge/host/print ---

## Response 2
Thanks for your input! Yeah ip arp is one option but I cannot search based on mac. Anyway my question was a bit off to begin with because routers don't generally build mac tables (ccr1072 doesn't even have a switch chip). ---

## Response 3
Both tables, mentioned by @panisk0 ... with addition of/interface/ethernet/switch/host... are serving different roles:/ip/arp (and /ipv6/neighbor for IPv6) lists hosts with which IP (or IPv6) stack of router communicated in near past. It contains both IP (or IPv6) address and MAC address of that device, as well as router's interface (which is not the same as bridge port)./interface/bridge/host (and /interface/ethernet/switch/host if bridge is not HW-offloaded but manual config is in place) lists hosts which communicate with each other via bridge (or switch chip). And it doesn't matter if bridge can be offloaded or not, each bridge needs it. This table will contain MAC addresses and bridge/switch ports, but won't show IP address ... ---

## Response 4
Thanks for your input! Yeah ip arp is one option but I cannot search based on mac. Anyway my question was a bit off to begin with because routers don't generally build mac tables (ccr1072 doesn't even have a switch chip).
```
/ip/arp/printwheremac-address=xx:xx:xx:xx:xx:xxSwitch chips have internal MAC table that is independent with respect to RourerOS Linux kernel ARP table which is built to allow router IPv4 address to MAC address translation.

---
```

## Response 5
I must have been fast asleep while trying it. I just couldn't for the life of me filter for mac addresses using ip arp and I thought it wasnt possible. Turns out I'm just on the less sharp side lol. Thanks again!!! ---

## Response 6
@OptiTech IMO while RouterOS CLI is powerful, it is not at all obvious even to experienced shell users; the where clause in particular.https://help.mikrotik.com/docs/spaces/R ... alCommands ---