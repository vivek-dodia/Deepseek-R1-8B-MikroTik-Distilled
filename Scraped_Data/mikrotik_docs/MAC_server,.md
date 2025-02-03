---
title: MAC server
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/98795539/MAC+server,
crawled_date: 2025-02-02T21:09:19.324018
section: mikrotik_docs
type: documentation
---

MAC server section allows you to configure MAC Telnet Server, MAC WinBox Server and MAC Ping Server on RouterOS device.
MAC Telnet is used to provide access to a router that has no IP address set. It works just like IP telnet. MAC telnet is possible between two MikroTik RouterOS routers only.
MAC WinBox is used to provide Winbox access to the router via MAC address.
MAC Ping is used to allow MAC pings to the router's MAC address.
## MAC Telnet Server
It is possible to set MAC Telnet access to specific interfaces that are a part of theinterface list:
```
[admin@device] /tool mac-server set allowed-interface-list=listBridge
[admin@device] /tool mac-server print
  allowed-interface-list: listBridge
```
In the example above, MAC Telnet is configured for the interface list "listBridge" and, as a result, MAC Telnet will only work via the interfaces that are members of the list (you can add multiple interfaces to the list).
To disable MAC Telnet access, issue the command (set "allowed-interface-list" to "none"):
```
[admin@device] /tool mac-server set allowed-interface-list=none
[admin@device] /tool mac-server print
  allowed-interface-list: none
```
You can check active MAC Telnet sessions (that the device accepted) with the command:
```
[admin@device] > tool mac-server sessions print
Columns: INTERFACE, SRC-ADDRESS, UPTIME
#  INTERFACE  SRC-ADDRESS        UPTIME
0  ether5     64:D1:54:FB:E3:E6  17s
```
### MAC Telnet Client
When MAC Telnet Server is enabled, you can use another RouterOS device to connect to the server using the mac-telnet client:
```
[admin@device2] > tool mac-telnet B8:69:F4:7F:F2:E7    
Login: admin
Password: 
Trying B8:69:F4:7F:F2:E7...
Connected to B8:69:F4:7F:F2:E7
  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK
  MikroTik RouterOS 7.1rc3 (c) 1999-2021       https://www.mikrotik.com/
Press F1 for help
[admin@device] >
```
Change the MAC address accordingly (to your setup) and you should get into the server's CLI (as shown in the example above).
### MAC Scan
Mac scan feature discovers all devices, which support MAC telnet protocol on the given network. The command requires you to select an interface that should be scanned:
```
[admin@Sw_Denissm] > tool mac-scan interface=all           
MAC-ADDRESS       ADDRESS                AGE
B8:69:F4:7F:F2:E7 192.168.69.1            26
2C:C8:1B:FD:F2:C3 192.168.69.3            56
```
In the example, above, all interfaces are chosen, and the scan will run infinitely unless stopped (by pressing "q").
You can also add a "duration" parameter that will dictate for how long the scan should go on:
```
[admin@Sw_Denissm] > tool mac-scan interface=all duration=1
MAC-ADDRESS       ADDRESS                AGE
B8:69:F4:7F:F2:E7 192.168.69.1            48
2C:C8:1B:FD:F2:C3 192.168.69.3            17
```
In the example above, we set the "duration" parameter to 1 second.
## MAC WinBox Server
Same as with MAC Telnet, it is possible to set MAC WinBox access to specific interfaces that are a part of theinterface list:
```
[admin@device] > tool mac-server mac-winbox set allowed-interface-list=listBridge 
[admin@device] > tool mac-server mac-winbox print                   
  allowed-interface-list: listBridge
```
In the example above, MAC WinBox access is configured for the interface list "listBridge" and, as a result, MAC WinBox will only work via the interfaces that are members of the list.
To disable MAC WinBox access, issue the command (set "allowed-interface-list" to "none"):
```
[admin@device] > tool mac-server mac-winbox set allowed-interface-list=none
[admin@device] > tool mac-server mac-winbox print                   
  allowed-interface-list: none
```
## MAC Ping Server
MAC Ping Server can be either set to be "disabled" or "enabled":
```
[admin@device] > tool mac-server ping print
  enabled: yes
```
You can enable or disable MAC ping with the help of the commands (enable=yes→ to enable the feature;enable=no→ to disable the feature):
```
[admin@device] > tool mac-server ping set enabled=yes
[admin@device] > tool mac-server ping set enabled=no
```
When MAC Ping is enabled, other hosts on the same broadcast domain can use ping tool to ping the mac address. For example, you can issue the following command to check MAC ping results:
```
[admin@device] > /ping 00:0C:42:72:A1:B0
HOST                                    SIZE  TTL TIME  STATUS                                         
00:0C:42:72:A1:B0                       56        0ms  
00:0C:42:72:A1:B0                       56        0ms  
    sent=2 received=2 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms
```