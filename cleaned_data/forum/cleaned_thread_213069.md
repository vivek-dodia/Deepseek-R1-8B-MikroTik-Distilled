# Thread Information
Title: Thread-213069
Section: RouterOS
Thread ID: 213069

# Discussion

## Initial Question
I have the following config working as expected, except that after power outage CAPSMAN is really slow to establish the connection to the CAPs after the power comes back up.At the moment CAPSMAN connects and disconnects to the CAPs many times before it successfully establishes connection and provision the configuration.Does it matter that hap AX3 is version 7.16 and the 2 wap ax are 7.15?Any suggestions on how to speed up the process? ---

## Response 1
Are you referring to caps radios becoming visible in capsman or the radios themselves becoming visible to clients ?The former should be rather quick. On my installations it is a matter of seconds after reboot.The latter can take up to 15 minutes if you use DFS frequencies (radar checks needs to be completed first before the AP is allowed to transmit).Only on 5GHz radios or also 2GHz radios ?Which device is acting as controller ?Is the problem with all APs or only some ? ---

## Response 2
Are you referring to caps radios becoming visible in capsman or the radios themselves becoming visible to clients ?The radios pop up in CAPSMAN for few seconds and then disappear, the can't become visible to the clients at all.Only on 5GHz radios or also 2GHz radios ?Both 5 and 2GHz radios.Which device is acting as controller ?Is the problem with all APs or only some ?hap AX3 is the main controller, the problem is only with the 2 wap ax APs, the hap ax2 is being managed by CAPsMAN but also gets the management super slow.From the time I posed this topic till now only ax2 has managed to get settings from AX3, the other two are still tryingI tried Skip DFS Channels all and disabled, no change ---

## Response 3
Then it may be time to put your config on the table.Controller and 1 wap AX please.Make sure to remove all private/public info.And please post both configs between code quotes. ---

## Response 4
Here is my config, please let me know if you see anything wrong with it, but as I previously stated it was working few days ago when I installed the wap ax access points. Nothing has changed except the fact that I had power outage and then it was not workinghap ax3 - CAPsMAN - manager
```
# 2024-12-06 09:42:03 by RouterOS 7.16.1
# software id = TF67-7ZFG
#
# model = C53UiG+5HPaxD2HPaxD
# serial number = ****
/interface bridge
add name=bridge1
/interface ethernet
set [ find default-name=ether1 ] mac-address=***** name=ether1-WAN
/interface wifi
set [ find default-name=wifi1 ] channel.band=5ghz-ax .skip-dfs-channels=disabled .width=20/40/80mhz configuration.country=***** .distance=3 .mode=ap .multicast-enhance=enabled .ssid=****** disabled=no \
    security.authentication-types=wpa2-psk .encryption=ccmp .ft=yes .ft-over-ds=yes .wps=push-button
set [ find default-name=wifi2 ] channel.band=2ghz-ax .skip-dfs-channels=disabled .width=20/40mhz-Ce configuration.country=***** .distance=3 .mode=ap .multicast-enhance=enabled .ssid=****** disabled=no \
    security.authentication-types=wpa2-psk .encryption=ccmp .ft=yes .ft-over-ds=yes .wps=push-button
/interface list
add name=WAN
add name=LAN
/interface wifi security
add authentication-types=wpa2-psk disabled=no encryption=ccmp name=CAP_sec1 wps=push-button
/interface wifi configuration
add country=****** disabled=no multicast-enhance=enabled name=5ghz security=CAP_sec1 security.authentication-types=wpa2-psk .encryption=ccmp .ft=yes .ft-over-ds=yes ssid=******
add country=****** disabled=no multicast-enhance=enabled name=2Ghz security=CAP_sec1 security.authentication-types=wpa2-psk .encryption=ccmp .ft=yes .ft-over-ds=yes ssid=******
/ip pool
add name=dhcp_pool1 ranges=10.10.10.2-10.10.10.254
/ip dhcp-server
add address-pool=dhcp_pool1 interface=bridge1 name=dhcp2
/interface bridge port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
add bridge=bridge1 interface=wifi1
add bridge=bridge1 interface=wifi2
/ip neighbor discovery-settings
set discover-interface-list=!LAN
/ipv6 settings
set disable-ipv6=yes
/interface list member
add interface=ether1-WAN list=WAN
add interface=bridge1 list=LAN
/interface wifi capsman
set ca-certificate=auto enabled=yes package-path="" require-peer-certificate=no upgrade-policy=none
/interface wifi provisioning
add action=create-dynamic-enabled disabled=no master-configuration=2Ghz supported-bands=2ghz-ax
add action=create-dynamic-enabled disabled=no master-configuration=5ghz supported-bands=5ghz-ax
/ip address
add address=10.10.10.1/24 interface=bridge1 network=10.10.10.0
/ip dhcp-client
add interface=ether1-WAN
/ip dhcp-server network
add address=0.0.0.0/24 gateway=0.0.0.0 netmask=24
add address=10.10.10.0/24 dns-server=46.40.72.9,8.8.8.8,8.8.4.4,46.40.72.9 gateway=10.10.10.1
/ip dns
set servers=8.8.8.8,8.8.4.4
/ip firewall filter
add action=accept chain=input protocol=icmp
add action=accept chain=input connection-state=established
add action=accept chain=input connection-state=related
add action=drop chain=input in-interface-list=!LAN
add action=accept chain=input connection-state=established,related,untracked
add action=drop chain=input connection-state=invalid
add action=accept chain=input protocol=icmp
add action=accept chain=input dst-address=127.0.0.1
add action=accept chain=input dst-port=53 in-interface-list=LAN protocol=udp
add action=accept chain=input dst-port=53 in-interface-list=LAN protocol=tcp
add action=drop chain=input
add action=fasttrack-connection chain=forward connection-mark=no-mark connection-state=established,related hw-offload=yes
add action=accept chain=forward connection-state=established,related,untracked
add action=drop chain=forward connection-state=invalid
add action=accept chain=forward in-interface-list=LAN out-interface-list=WAN
add action=drop chain=forward
add action=accept chain=forward connection-nat-state=dstnat
/ip firewall nat
add action=masquerade chain=srcnat out-interface-list=WAN
/system clock
set time-zone-name=Europe/Sofia
/system identity
set name=vRS
/system note
set show-at-login=nowAP ax
```

```
# 2024-12-06 09:44:59 by RouterOS 7.15.1
# software id = 2881-0S7F
#
# model = wAPG-5HaxD2HaxD
# serial number = ******
/interface bridge
add name=bridge1
/interface wifi
# no connection to CAPsMAN, managed locally
# SSID not set
set [ find default-name=wifi1 ] configuration.manager=capsman-or-local .mode=ap disabled=no
# no connection to CAPsMAN, managed locally
# SSID not set
set [ find default-name=wifi2 ] configuration.manager=capsman-or-local .mode=ap disabled=no
/interface bridge port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=wifi1
add bridge=bridge1 interface=wifi2
/interface wifi cap
set discovery-interfaces=bridge1 enabled=yes
/ip dhcp-client
add interface=bridge1
/system clock
set time-zone-name=Europe/Sofia
/system identity
set name=vRS_backyard
/system note
set show-at-login=no

---
```

## Response 5
I've noticed that after 3 days of trying everything was working again as expected, but again today we had power outage for 5 minutes and now again it is struggling to get the radios back up.I think this might be a clue why its not working, the cap-wifi1 and cap-wifi2 are getting provisioning fast and are identical to the management CAP. These 2 are on hap ax 2.The cap-wifi3 and cap-wifi4 in red are on wap ax and from what i see in Radios tab for 5GHz band it is trying to get few more bands assigned. Do I need to set some additional parameters in Configuration or similar to get the same result as on hap ax2? ---

## Response 6
```
/interface bridge port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=wifi1
add bridge=bridge1 interface=wifi2Your wifi interfaces should not be manually added to the bridge.Only have ether1 and ether2 as part of the bridge:
```

```
/interface bridge port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2

---
```

## Response 7
```
/interface bridge port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=wifi1
add bridge=bridge1 interface=wifi2Your wifi interfaces should not be manually added to the bridge.Only have ether1 and ether2 as part of the bridge:
```

```
/interface bridge port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2This solved the issue with CAPsMAN provisioning, but now DHCP server don't give IP addresses to devices connected to WiFi trough the CAP devices.

---
```

## Response 8
This solved the issue with CAPsMAN provisioning, but now DHCP server don't give IP addresses to devices connected to WiFi trough the CAP devices.External radios or local radios ?What's this ?
```
/ip dhcp-server network
add address=0.0.0.0/24 gateway=0.0.0.0 netmask=24I think that shouldn't be there.Your firewall rules seem odd, certainly not default but I don't see a direct reason there why it shouldn't work.Is anything visible in log file about DHCP messages ?

---
```

## Response 9
External radios or local radios ?if by external you mean the radios of the wap ax devices that are managed by the hap ax3 CAPsMAN, yes I can't get IP when I am trying to connect trough an external radioI can connect to wifi and get IP when I connect to the radio on my main router hap ax3. But not trough the radios of the CAP devices.add address=0.0.0.0/24 gateway=0.0.0.0 netmask=24Its an artefact left from config, removed it - not solved the issue ---

## Response 10
I was able to resolve the issue by setting the Bridge - Admin MAC address and after that adding the cap WiFi interfaces to their bridges.It seems the problem was that after reboot some times the CAP bridges get different MAC addresses assigned. ---