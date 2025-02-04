# Thread Information
Title: Thread-1116309
Section: RouterOS
Thread ID: 1116309

# Discussion

## Initial Question
I have this topology :flat-Page-5.jpgI would like to enable RSTP on all switches but this causes the network to hang.STP priorities :bridge on CRS510 - 0x1000bridge on CRS305 - 0x8000priority on TP-Link - 0xA000port path costether1 on CRS510 - 20000ether1 on CRS305 - 200002 ports on TPLink - 2000000(all other settings are default)I think it supposed to work but it doesn't as network hangs pretty much immediately.Any tips or tricks ? ---

## Response 1
Do I need to click Auto Isolate on ether1 ports on both Mikrotiks ? By default it is false. ---

## Response 2
You don't need to enable auto-isolate. You are not specific enough regarding what means "network hangs", so I can only speculate that there is some incompatibility between RSTP versions so the L2 loop does not get cut and broadcast traffic exhausts all the bandwidth. Hence I would make the physical topology a star or a line as a diagnostic step, enable RSTP on all devices and check the bridge status on all devices where it is possible (I suspect SwOS doesn't provide bridge state monitoring). Adjusting priorities should show you whether the root bridge moves accordingly and thus find out which devices do not understand each other's dialect of RSTP. ---