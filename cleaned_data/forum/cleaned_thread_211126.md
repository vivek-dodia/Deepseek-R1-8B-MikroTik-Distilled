# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211126

# Discussion

## Initial Question
Author: Mon Sep 23, 2024 6:13 am
Hello, Let say i have radio 2.4GHz called 'RADIO-1' and this radio have mac address C4:AD:34:48:E1:05 and radio MAC C4:AD:34:48:E1:05 then i make a Virtual AP (VAP) and set radio 'RADIO-1' as master interface.After the VAP created i can see the VAP have same mac address with master interface (RADIO-1) but the Radio Mac is 00:00:00:00:00:00.My question is :What impact if i set the VAP radio mac to C4:AD:34:48:E1:05 (same with the master interface)What impact if i set the VAP mac address and radio mac to something else like 33:33:33:33:33:33 (same with the master interface) ---

## Response 1
Author: [SOLVED]Mon Sep 23, 2024 9:30 am
What impact if i set the VAP radio mac to C4:AD:34:48:E1:05 (same with the master interface)It most likely won't work ... station, connected to AP (either interface) will send wifi frame with "receiver address" field set to BSSID (MAC) of AP. And then AP will take this frame and do with it whatever it's supposed (e.g. wrap it with VLAN tag). The problem is if there are multiple wifi interfaces with same BSSID (MAC) ... AP will associate received wireless frame with one of interfaces (likely with physical one but that's not to be taken for granted).What impact if i set the VAP mac address and radio mac to something else like 33:33:33:33:33:33 (same with the master interface)In theory the only requirement is that MAC (BSSID) is unique in your (wireless) network. So if you don't have any other device with certain MAC, then it's fine.In reality, it's a good practice to "invent" MAC addresses that are LAA (readMAC address articleon wikipedia to learn about LAA). And to make things more robust (i.e. make probability of ending up with same MAC addresses) it's good to take MAC address of physical wireless interface and alter only the value of first octet of address .BTW, the example address you wrote above is a "multicast MAC address" and can confuse some wireless stations.