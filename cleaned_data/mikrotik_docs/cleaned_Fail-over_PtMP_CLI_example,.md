# Document Information
Title: Fail-over PtMP CLI example
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/189497349/Fail-over+PtMP+CLI+example,

# Content
# Summary
This example shows how to configure automatic fail-over (bonding) 5Ghz link in combination with 60Ghz devices in CLI.When a connection between 60Ghz wireless is lost, it will automatically use the bonded interface.Example is done from empty configuration state with [WinBox] utility
# Connect to the device step by step
After configuration reset - only mac-telnet is possible.Connect to device by connecting to it's MAC address or use WinBox New terminal to find device MAC address of the W60G device by issuing command:
/ip neighbor print
------------------
```
/ip neighbor print
```
To connect to the W60G device issue a command:
/tool mac-telnet mac-address
----------------------------
```
/tool mac-telnet mac-address
```
Enter username and password. By default username isadminand password is either blank or printed on the device sticker.
[admin@KD_GW] > /tool mac-telnet C4:AD:34:84:EE:5DLogin: adminPassword:Trying C4:AD:34:84:EE:5D...Connected to C4:AD:34:84:EE:5D
--------------------------------------------------------------------------------------------------------------------------------
```
[admin@KD_GW] > /tool mac-telnet C4:AD:34:84:EE:5DLogin: adminPassword:Trying C4:AD:34:84:EE:5D...Connected to C4:AD:34:84:EE:5D
```
# Configure bridge
Add new bridge and assign bridge members to it by issuing the following command:
/interface bridge add name=bridge
---------------------------------
```
/interface bridge add name=bridge
```
To check if the bridge has been created issue a command:
[admin@MikroTik] > /interface bridge printFlags: X - disabled, R - running0 R name="bridge" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=1A:7F:BB:41:B0:94 protocol-mode=rstpfast-forward=yes igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6vlan-filtering=no dhcp-snooping=no
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
[admin@MikroTik] > /interface bridge printFlags: X - disabled, R - running0 R name="bridge" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=1A:7F:BB:41:B0:94 protocol-mode=rstpfast-forward=yes igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6vlan-filtering=no dhcp-snooping=no
```
# Set up 60Ghz wireless connection
All previously explained steps are identical to Bridge and Station devices. When configuring wireless interface different modes needs to be used.For ap-bridge device -
Enable W60G interface after required parameters have been set.
[admin@MikroTik] > /interface w60g set wlan60-1 mode=ap-bridge frequency=auto ssid=MySSID password=choosepassword isolate-stations=no[admin@MikroTik] > /interface w60g printFlags: X - disabled, R - running0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=ap-bridge ssid="MySSID"frequency=auto default-scan-list=58320,60480,62640,64800 password="choosepassword" tx-sector=auto put-stations-in-bridge=none isolate-stations=no[admin@MikroTik] > /interface w60g enable wlan60-1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
[admin@MikroTik] > /interface w60g set wlan60-1 mode=ap-bridge frequency=auto ssid=MySSID password=choosepassword isolate-stations=no[admin@MikroTik] > /interface w60g printFlags: X - disabled, R - running0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=ap-bridge ssid="MySSID"frequency=auto default-scan-list=58320,60480,62640,64800 password="choosepassword" tx-sector=auto put-stations-in-bridge=none isolate-stations=no[admin@MikroTik] > /interface w60g enable wlan60-1
```
For Station devices -
Enable W60G interface after required parameters have been set.
[admin@MikroTik] > /interface w60g set wlan60-1 mode=station-bridge frequency=auto ssid=MySSID password=choosepassword isolate-stations=no[admin@MikroTik] > /interface w60g printFlags: X - disabled, R - running0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=station-bridge ssid="MySSID"frequency=auto default-scan-list=58320,60480,62640,64800password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=no[admin@MikroTik] > /interface w60g enable wlan60-1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
[admin@MikroTik] > /interface w60g set wlan60-1 mode=station-bridge frequency=auto ssid=MySSID password=choosepassword isolate-stations=no[admin@MikroTik] > /interface w60g printFlags: X - disabled, R - running0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=station-bridge ssid="MySSID"frequency=auto default-scan-list=58320,60480,62640,64800password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=no[admin@MikroTik] > /interface w60g enable wlan60-1
```
# Set up 5Ghz wireless connection
For ap-bridge device -
Enable 5Ghz interface after required parameters have been set.
[admin@MikroTik] > /interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword[admin@MikroTik] > /interface wireless set wlan1 frequency=auto scan-list=default installation=outdoor mode=ap-bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac[admin@MikroTik] > /interface wireless enable wlan1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
[admin@MikroTik] > /interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword[admin@MikroTik] > /interface wireless set wlan1 frequency=auto scan-list=default installation=outdoor mode=ap-bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac[admin@MikroTik] > /interface wireless enable wlan1
```
For Station devices -
Enable W60G interface after required parameters have been set.
[admin@MikroTik] > /interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword[admin@MikroTik] > /interface wireless set wlan1 frequency=auto scan-list=default installation=outdoor mode=station-bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac[admin@MikroTik] > /interface wireless enable wlan1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
[admin@MikroTik] > /interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword[admin@MikroTik] > /interface wireless set wlan1 frequency=auto scan-list=default installation=outdoor mode=station-bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac[admin@MikroTik] > /interface wireless enable wlan1
```
# Configure bridge for Access Point
Configure bridge for AP to ensure that 5ghz is working as fail-over. It is required to bridgewlan1,ether1, and all 60ghzstation interfaces.In the example it shows only 2 station devices but it is possible to add up to 8 devices.For ap-bridge device please setconfigurationas follows:
[admin@MikroTik] >/interface bridge portadd bridge=bridge hw=no interface=ether1add bridge=bridge interface=wlan1add bridge=bridge interface=wlan60-station-1add bridge=bridge interface=wlan60-station-2[admin@MikroTik] > interface/bridge/port/pr# INTERFACE         BRIDGE  HW  PVID  PRIORITY  PATH-COST  INTERNAL-PATH-COST  HORIZON0 ether1            bridge      no     1  0x80             10                  10  none1 wlan1             bridge             1  0x80             10                  10  none2 wlan60-station-1  bridge             1  0x80             10                  10  none3 wlan60-station-2  bridge             1  0x80             10                  10  none
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
[admin@MikroTik] >/interface bridge portadd bridge=bridge hw=no interface=ether1add bridge=bridge interface=wlan1add bridge=bridge interface=wlan60-station-1add bridge=bridge interface=wlan60-station-2[admin@MikroTik] > interface/bridge/port/pr# INTERFACE         BRIDGE  HW  PVID  PRIORITY  PATH-COST  INTERNAL-PATH-COST  HORIZON0 ether1            bridge      no     1  0x80             10                  10  none1 wlan1             bridge             1  0x80             10                  10  none2 wlan60-station-1  bridge             1  0x80             10                  10  none3 wlan60-station-2  bridge             1  0x80             10                  10  none
```
# Configure bridge and bonding for station devices
Configure bonding and assign slave interfaces in this setup it is selected as built in wlan1 interface, but it can be also ether interface in other kind of setups.
For station-bridge devices please setbondingas:
[admin@MikroTik] > /interface bonding add mode=active-backup name=bond1 primary=wlan60-1 slaves=wlan60-1,wlan1
--------------------------------------------------------------------------------------------------------------
```
[admin@MikroTik] > /interface bonding add mode=active-backup name=bond1 primary=wlan60-1 slaves=wlan60-1,wlan1
```
Add interface members (ether1 and bond1) to newly created bridge.
[admin@MikroTik] > /interface bridge port add interface=ether1 bridge=bridge[admin@MikroTik] > /interface bridge port add interface=bond1  bridge=bridge[admin@MikroTik] > /interface bridge port printFlags: X - disabled, I - inactive, D - dynamic, H - hw-offload# INTERFACE                              BRIDGE                              HW   PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON0     ether1                                 bridge                             yes     1     0x80         10                 10       none1     bond1                                  bridge                             yes     1     0x80         10                 10       none
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
[admin@MikroTik] > /interface bridge port add interface=ether1 bridge=bridge[admin@MikroTik] > /interface bridge port add interface=bond1  bridge=bridge[admin@MikroTik] > /interface bridge port printFlags: X - disabled, I - inactive, D - dynamic, H - hw-offload# INTERFACE                              BRIDGE                              HW   PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON0     ether1                                 bridge                             yes     1     0x80         10                 10       none1     bond1                                  bridge                             yes     1     0x80         10                 10       none
```
# Additional configuration
Link should be established after all previously explained steps are done. It's recommended to set up administrator password on both devices.
# Troubleshooting
Ensure connection is established to the correct device by checking the device settings like serial number and model name by issuing a command:
[admin@MikroTik] > /system routerboard print
--------------------------------------------
```
[admin@MikroTik] > /system routerboard print
```
If bridge wlan60-1 interface in bridge settings is inactive and configuration is done properly  to enable the interface on a device - issue a command:
[admin@MikroTik] > /interface w60g enable wlan60-1
--------------------------------------------------
```
[admin@MikroTik] > /interface w60g enable wlan60-1
```