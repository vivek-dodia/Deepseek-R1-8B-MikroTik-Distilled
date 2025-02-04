# Thread Information
Title: Thread-206621
Section: RouterOS
Thread ID: 206621

# Discussion

## Initial Question
Hello, I'm facing issue that few Wireless devices which i have on floor 1 - Master DHCP Router Wifi (AP-A) are time to time connect to the Slave AP on Floor 0 - router Wifi (AP-B) and it leads to weak / poor signal or complete disconnect from Wireless network. Even i need to restart those clients to connect again.So instead of putting all clients MACs on AP-B as White List - "Wireless Tables - Access list"Can i set "Black List" for few clients?So i can be sure that those few clients stay only on AP-A.Thanks ---

## Response 1
Depends on which wireless package respectively menu you are using. If it's the Wireless menu, it can be done through the connect list:
```
/interfacewireless connect-listaddinterface="wifi_interface"connect=nomac-address="mac_address"If the WiFi interfaces are in the Wifiwave2 or WiFi menu, then the blocking rule would be set up in the access list:
```

```
/interfacewifi access-listaddmac-address="mac_address"action=reject

---
```

## Response 2
Thanks for suggestion.Main Router 1st AP - hAP AX3The 2nd AP is - CRS125-24G-1S-2HnD (so i assume no Wifiwave2 support)To be honest i haven't really looked yet into the new changes Wireless / Wifiwave2 changes (i believe since 7.10+)
```
/interfacewireless connect-listaddinterface="wifi_interface"connect=nomac-address="mac_address"Here i'm adding new / 2nd Wifi interface let's say wlan2 and i will list MACs which won't be able to connect?Or i will use it on "wlan1" with an extra rule?
```

```
/interfacewireless connect-listaddinterface="wlan1"connect=nomac-address="mac_address"

---
```

## Response 3
Seems like this did the trick
```
/interfacewireless connect-listaddinterface="wlan1"connect=nomac-address="mac_address"What I've realized now i could also add some "Signal Strength Range" limit (i believe i read about it somewhere)So if it's weaker then XX devices wouldn't connect, so perhaps this way i don't need to set it for each MAC...right?

---
```

## Response 4
Yes, it could be done also like that but you'll have to setup the limit most probably based on trial and error ---

## Response 5
Coming back to this topic, even I thought for some time that is working...is not and the Devices are still connecting / disconnectingThis lead to a state that the Device will not connect anymore anywhere and I need to restart it.w1.pngAny clue what else could completely ignore the 2nd AP with weaker signal?w2.pngThanks ---