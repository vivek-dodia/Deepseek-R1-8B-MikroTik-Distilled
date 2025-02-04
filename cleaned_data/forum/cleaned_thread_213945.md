# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213945

# Discussion

## Initial Question
Author: Thu Jan 16, 2025 8:51 pm
``` /interfacevlanaddinterface=bridge name=vlan40 vlan-id=40 ``` Assumption: When running Bridge VLAN setups, the bridge must be a tagged port on the VLAN for Layer 3 services to function through the network.Assumption is false; make all bridge VLAN untagged. Make exceptions with:
```
---
```

## Response 1
Author: Fri Jan 17, 2025 4:47 am
``` /interfacevlanaddinterface=bridge name=vlan40 vlan-id=40 ``` ``` # BRIDGE VLAN-IDS CURRENT-TAGGED CURRENT-UNTAGGEDColumns:BRIDGE, VLAN-IDS, CURRENT-TAGGED, CURRENT-UNTAGGED# BRIDGE VLAN-IDS CURRENT-TAGGED CURRENT-UNTAGGED;;;vlan100bridge10bridge ether3 ether2;;;vlan301bridge30bridge ether3 ether2;;;vlan202bridge20bridge ether3 ether2 ``` Assumption: When running Bridge VLAN setups, the bridge must be a tagged port on the VLAN for Layer 3 services to function through the network.Assumption is false; make all bridge VLAN untagged. Make exceptions with:
```
Thank you, but I'm not quite following your suggestion. Are you suggesting to add the bridge as an untagged port for each VLAN entry in the table? Currently bridge is tagged for each VLAN:
```