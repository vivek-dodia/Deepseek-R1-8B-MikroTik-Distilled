# Thread Information
Title: Thread-1121412
Section: RouterOS
Thread ID: 1121412

# Discussion

## Initial Question
For a single one of >30 machines on a local Ethernet Gigabit network, the machine won't get the IPv4 address assigned to it's MAC address (EC:A8:6B:F9:EF:74) in the router. Instead it gets an address in the DHCP guest pool. This makes the machine unreachable by it's host name.The problem happens, or vanishes, according to the value of the clientid field that I set using Winbox in the router's static lease.If I leave clientid to ff:6b:f9:ef:74:0:1:0:1:2f:26:20:d2:ec:a8:6b:f9:ef:74 as present when I convert the guest pool lease to a static lease, things work.If set clientid to 1:ec:a8:6b:f9:ef:74 (parroting other leases assigned by a configuration file, which work fine) or anything else I tried, the problem happens.So what's the Influence of clientid in the defintion of DHCP leases?Router runs MikroTik RouterOS 7.15.3.The problem machine runs Debian GNU/Linux 12 (bookworm) with kernel 6.1.0-30-amd64This machine formerly was assigned to a different IPv4 in the router configuration, with clientid=1:ec:a8:6b:f9:ef:74 but that's removed.TIA ---

## Response 1
So what's the Influence of clientid in the defintion of DHCP leases?In principle modern DHCP servers (I can't say anything about tens of years old DHCP servers) assign leases according to client ID value ... which is provided by clients. Vast majority of clients indicate that CLient ID is MAC address, some might do it differently (e.g. if client has multiple network interfaces but only one of them can be active at the same time ... it might use something unrelated as client ID to make sure that address provided by DHCP server is the same regardless which physical interface is active).So basically ... you have to set client id to correct value when creating static lease. Most of devices (all of them actually), leasing addresses from my DHCP server, are assigned Cliend ID as "1:<MAC>", i.e. MAC address, prepended with "1:". ---