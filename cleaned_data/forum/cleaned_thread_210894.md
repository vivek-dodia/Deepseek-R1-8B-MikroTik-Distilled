# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210894

# Discussion

## Initial Question
Author: Fri Sep 13, 2024 4:18 am
Dear experts, sorry, I'm very very poor knowledge of scripting...I was able to add my IP in a global variable, like::global WAN1 "100.10.20.40":global WAN2 "100.10.20.50"it would be nice to achieve something like::log info "WAN1 IP is 100.10.20.40 and WAN2 IP is 100.10.20.50"goal is to "get" the WAN name to set $WAN1/2 , like$[$[/interface get [find name=WAN1] name]]Is this possible?Hope this is understandable ---

## Response 1
Author: Fri Sep 13, 2024 10:39 am
is a nonsense[/interface get [find name=WAN1] name]everytime, if WAN1 exist, the result is WAN1goal is to "get" the WAN name to set $WAN1/2If you must insert WAN1 or WAN2 on the script, are already WAN1 and WAN2...Be more clear. ---

## Response 2
Author: Fri Sep 13, 2024 12:47 pm
Right, it was not very accurate...1) In the DHCP up script I get the interface and address + create a global variable::local WANif [/interface get $"interface" name]:local WANip [:tostr $"lease-address"][:parse ":global $WANif $WANip"] <-THANKS to REXTENDED for this!:put $WAN1 -> 100.10.20.402) In the DHCP down, I know the interface name but not the previous IP::local WANif [/interface get $"interface" name]:log warning "Interface down, IP100.10.20.40is not available" <- to retrieve IP from interface name,$WANif -> WAN1 or WAN2, then with the WAN name i should "call" the global variable$WAN1 -> 100.10.20.40, something like [$[$WANif]] ---

## Response 3
Author: [SOLVED]Fri Sep 13, 2024 6:53 pm
``` # WRITE :global globalvarname :local WANif [/interface get $"interface" name] :local WANip [:tostr $"lease-address"] :set ($globalvarname->$WANif) $WANip # READ :global globalvarname :local WANif [/interface get $"interface" name] :local previousIP ($globalvarname->$WANif) ``` [:parse ":global $WANif $WANip"] <-THANKS to REXTENDED for this!Thanks***********************************Bad approach.Simply create one global array with inside interface / ip pair "WANx=o.l.d.ip;WANy=an.othe.r.ip",is more easy and intuitive.untested concept codeEXTRA: Consider that one interface can have more than on IP, and get do not support arrays as results...