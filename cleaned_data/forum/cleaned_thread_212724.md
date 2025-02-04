# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212724

# Discussion

## Initial Question
Author: Thu Nov 21, 2024 3:34 pm
``` [admin@InfernisGigaSwitch] > /interface/wireless/access-list/remove numbers=0 [admin@InfernisGigaSwitch] > /interface/wireless/access-list/remove numbers=0 no such item (4) [admin@InfernisGigaSwitch] > /interface/wireless/access-list/print Flags: X - disabled 0 ;;; Router InfernisMT - Infernis (2.4GHz) mac-address=xxxx interface=all signal-range=-90..120 allow-signal-out-of-range=10s authentication=yes forwarding=yes ap-tx-limit=0 client-tx-limit=0 private-algo=none private-key="" private-pre-shared-key="" management-protection-key="" vlan-mode=default vlan-id=1 1 ;;; Router InfernisMT - Infernis (5GHz) mac-address=xxxx interface=all signal-range=-90..120 allow-signal-out-of-range=10s authentication=yes forwarding=yes ap-tx-limit=0 client-tx-limit=0 private-algo=none private-key="" private-pre-shared-key="" management-protection-key="" vlan-mode=default vlan-id=1 2 ;;; Router AragothMT - Infernis (2.4GHz) mac-address=xxxx interface=all signal-range=-90..120 allow-signal-out-of-range=10s authentication=yes forwarding=yes ap-tx-limit=0 client-tx-limit=0 private-algo=none private-key="" private-pre-shared-key="" management-protection-key="" vlan-mode=default vlan-id=1 3 ;;; Laptop Avalon - WiFi mac-address=xxxx interface=all signal-range=-90..120 allow-signal-out-of-range=10s authentication=yes forwarding=yes ap-tx-limit=0 client-tx-limit=0 private-algo=none private-key="" private-pre-shared-key="" management-protection-key="" vlan-mode=default vlan-id=1 [admin@InfernisGigaSwitch] > /interface/wireless/access-list/remove numbers=0 [admin@InfernisGigaSwitch] > /interface/wireless/access-list/remove numbers=0 no such item (4) [admin@InfernisGigaSwitch] > ``` Problem in 7.16.1. If you do not list items, the script does not recognize the next ones. This is also visible when executing in the console.
```
---
```

## Response 1
Author: Fri Nov 22, 2024 11:46 am
``` /interface wireless access-list remove ([find]->0) ``` /interface/wireless/access-list/remove numbers=0translate:remove the first (index 0) in the list of those already found... but there is no list of those already found, or nothing was found.The second time in a row that the command is given, the first has already been deleted, and the list is NOT updated when the first element is deleted.
```
Translate: Remove first element you find. Do error if empty.
```