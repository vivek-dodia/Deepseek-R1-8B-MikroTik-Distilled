# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213813

# Discussion

## Initial Question
Author: Fri Jan 10, 2025 1:30 am
Hello, I'm attempting to repurpose a 2011UiAS-2HnD (previously used for a VoIP service) as a router, VPN client, and Wi-Fi access point. After performing a factory reset to regain admin access, I struggled to connect it to our OpenVPN server and decided to upgrade it to the latest firmware.Before the upgrade, the router worked normally (including Wi-Fi). However, after the factory reset and upgrade, the Wi-Fi interface appears in the interface list but does not show the “R” status or any operational information, as seen in this screenshot:Screenshot 2025-01-09 171655.jpgThe upgrade required three steps to reach the latest version, and I unfortunately did not record the working version beforehand. I also tried reverting to the oldest available version on mikrotik.com, but the Wi-Fi interface still behaves the same way:Screenshot 2025-01-09 171800.jpgUnder Resources → PCI, nothing appears in the device list, but `wlan1` does show up under IRQ:Screenshot 2025-01-09 172142.jpgHere is the current `wlan1` configuration:Screenshot 2025-01-09 172307.jpgFrom what I can see, the Wi-Fi hardware is recognized by RouterOS and the Wireless package, but there seems to be a configuration issue. If you have any suggestions on resolving this, I’d appreciate your input.Thanks! ---

## Response 1
Author: [SOLVED]Fri Jan 10, 2025 9:08 am
wireless interface shows "R" status only if there's at least one wireless client (station) connected to it.Are you saying that SSID is actually not broadcasted? This is best verified by using some kind of wireless debugging application on wireless client (there are plenty of usable apps for smart phones).You can get some stats by double-clicking wireless interface (wifi1) and selecting "Status" tab ... it should show actually used channel and Tx power and some more information. Having empty values for "Registered Clients" and "Authenticated Clients" can be fine ... it indicates that no wireless clients are connected. ---

## Response 2
Author: Mon Jan 13, 2025 6:50 pm
wireless interface shows "R" status only if there's at least one wireless client (station) connected to it.Are you saying that SSID is actually not broadcasted? This is best verified by using some kind of wireless debugging application on wireless client (there are plenty of usable apps for smart phones).You can get some stats by double-clicking wireless interface (wifi1) and selecting "Status" tab ... it should show actually used channel and Tx power and some more information. Having empty values for "Registered Clients" and "Authenticated Clients" can be fine ... it indicates that no wireless clients are connected.You were correct!The router is located in remote location and I don't have access to client with WIFI there until I asked someone to try. I was expecting the camera and security device will connect back to it since I used the same SSID and Key but eventually I was wrong.Thank you!