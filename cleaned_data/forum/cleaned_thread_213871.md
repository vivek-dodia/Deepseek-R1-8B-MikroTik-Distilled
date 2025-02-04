# Thread Information
Title: Thread-213871
Section: RouterOS
Thread ID: 213871

# Discussion

## Initial Question
I'm facing a recurring issue with my CCR2216-A router. The device reboots under high traffic load, and the log shows the message:Kernel failure in previous boot.Below are the specifics of my setup:Device: CCR2216-AConfiguration:Bonding1: 2 portsBonding2: 2 portsBonding3: 4 ports5 default routes (2 eBGP, 3 iBGP).Traffic Load: RX 10–11G, TX 40–42G (total >50G).Interconnection: Connected via 100G QSFP28 to another CCR2216-B (which operates without issues).RouterOS Version: v7.16.2 (clean netinstall performed).Problem:When total traffic (RX+TX) exceeds 50G, the CCR2216-A either hangs or reboots.i also did the Netinstall but the issue is same.Please help to resolve this issue . ---

## Response 1
Is L3HW offload enabled, or is everything hitting the CPU?What kind of firewall rules do you have?How many total external routes is it ingesting?Are you graphing memory use and CPU load? ---

## Response 2
Thanks for the reply sirbryan, yes L3HW is enable and CPU was on 0%i am using with my CDN Clusters and its doing BGP only with defaul routes.i am using snmp graph only ---