# Thread Information
Title: Thread-213960
Section: RouterOS
Thread ID: 213960

# Discussion

## Initial Question
MikroTik Chateau Pro AX has options for bridge filtering, which I assume, are either similar to Netfilter EBTables or is based on Netfilter EBTables. In GUI I can restrict protocols to TCP/UDP (via NAT Firewall), enable/disable ARP (via bridge and port settings/options), enable/disable LLDP (and similar) frames, filter VLAN tagged frames, but that is not enough. I want to disable any possibility of magic frames, Wake-on-LAN frames, etc. There are many of them (https://en.wikipedia.org/wiki/EtherType). I want my router to filter all frames, except the required ones:1. IPv4 (0x0800)2. ARP (0x0806), preferably restrict to only ARP Request and ARP Reply3. WiFi Authentication (0x888E)I can do that with EBTables, but does MikroTik allow for some other way to do it? I also want this kind of filtering to apply itself automatically on boot or shortly after OS is booted. ---

## Response 1
What is wrong with using "bridge filter", which probably indeed will map to ebtables, for that? ---

## Response 2
Bridge Filter doesn't specify what is filters. For example, your NAT firewall filter can be set to allow exclusively TCP and UDP traffic, but LLDP (data link layer) frames are not going to be filtered, even when bridge filtering is enabled. LLDP and similar frames are controlled by "Discovery" settings, but RouterOS doesn't have settings for every single EtherType. I don't think any router does, which is why I think it requires a custom script.It's unknown how MikroTik filters bridges anyway. For example, it is possible to BROUTE with EBTables. That forces data to skip Netfilter bridge tables entirely and send information to upper layer (IPTables), but IPTables can't filter any link layer frames (aside from ARP). This is why I ask.It would also be great if there was some layer 2 filtering (aside from ARP) for WAN port, but EBTables is LAN-only and doesn't filter WAN. ---

## Response 3
The command line parser accepts this:
```
/interfacebridge filteraddaction=drop mac-protocol=!arp,ip,0x888EEnter that line fragment followed by TAB key to see what else you can add.

---
```

## Response 4
It would also be great if there was some layer 2 filtering (aside from ARP) for WAN port, but EBTables is LAN-only and doesn't filter WAN.You can just add another bridge, put your WAN port in it, and move the WAN port config (IP address etc) from the WAN port to that bridge. Then you can apply bridge filters to your WAN.Alternatively, you can add a VLAN (e.g. VLAN 2) to your bridge, add a VLAN interface with Tag 2 on your existing bridge, move the WAN interface into the bridge as "untagged VLAN 2" and use the VLAN 2 interface as your WAN interface.This may seem more complicated and you will probably not trust it, but it is the preferred method in today's devices and RouterOS.(to have only a single bridge that does everything and use VLAN to separate the traffic) ---

## Response 5
Is anything required for these commands to function after reboot or am I supposed to enter them each time after reboot? ---

## Response 6
The command line parser accepts this:
```
/interfacebridge filteraddaction=drop mac-protocol=!arp,ip,0x888EEnter that line fragment followed by TAB key to see what else you can add.That command does not work and produces "input does not match any value of protocol-name, value of protocol-number contains invalid trailing characters".Once I figure out correct commands, do I need to re-enter them after every reboot or do they auto-apply after each reboot on their own?Also, how do I remove added rules? Replacing "Add" with "Remove" doesn't work and results in syntax error.

---
```

## Response 7
Unless operating in SAFE mode, configuration commands are persisted and viewable with export command.Command I supplied is incomplete; and may require "chain=forward" amongst other parameters; I'm just drawing attention to the capability that is there despite the absent documentation.My suggestion presumes command line and console proficiency which are documented here:https://help.mikrotik.com/docs/spaces/R ... t-SafeModehttps://help.mikrotik.com/docs/spaces/R ... +Interfacehttps://help.mikrotik.com/docs/spaces/R ... 98/ConsoleConsider web interface instead; I don't know WinBox; one or both may be easier to explore.Web interface:Bridge(left menu) >Filters(tab menu) >Add New(button).Web interfaceSafe Mode(button) is at the top, right of centerCommand line may support option combinations the visual interfaces don't; start visual then use command line export to see what they wrote.The last link above (Console) explains command hierarchy affecting everything, Item Names and Number, and theGeneral Commands(print, remove, ...). ---

## Response 8
The documentation:https://help.mikrotik.com/docs/spaces/R ... geFirewall ---

## Response 9
Is anything required for these commands to function after reboot or am I supposed to enter them each time after reboot?I suggest you first use the default settings, make your self familiar with RouterOS a bit more, maybe read some of the docs, and once you know the answer to such generic questions you come back and try the more advanced things like this.By then you have also learned what to do to prevent locking yourself out because of a mistake in filtering configuration. ---