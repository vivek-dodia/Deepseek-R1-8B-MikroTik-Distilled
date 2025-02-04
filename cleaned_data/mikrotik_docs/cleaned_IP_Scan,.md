# Document Information
Title: IP Scan
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/8323205/IP+Scan,

# Content
# Summary
IP Scan tool allows a user to scan networks based on some network prefix or by setting an interface to listen to. Either way, the tool collects certain data from the network:
When using IP scan tool user must choose what they want to scan for:
# Quick Example
In the following example, we will scan the devices on 10.155.126.0/24 network:
```
[admin@MikroTik] > /tool ip-scan address-range=10.155.126.1-10.155.126.255
Columns: ADDRESS, MAC-ADDRESS, TIMe, SNMP
ADDRESS         MAC-ADDRESS        TIM  SNMP
10.155.126.1    E4:8D:8C:1C:D3:18  2ms  CCR1036-8G-2S+
10.155.126.251                     2ms
10.155.126.151  E4:8D:8C:49:49:DB  1ms
10.155.126.153  6C:3B:6B:48:0E:8B  1ms  750Gr3
10.155.126.249  CC:2D:E0:8D:01:88  0ms  CRS328-24P-4S+
10.155.126.250  B8:69:F4:B3:1B:D2  0ms
10.155.126.252  6C:3B:6B:ED:83:69  0ms
10.155.126.253  6C:3B:6B:ED:81:83  0ms
```