# Document Information
Title: WiFi
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/224559120/WiFi,

# Content
# Overview
The 'WiFi' configuration menu, introduced inRouterOS 7.13, is a RouterOS menu for managing Wi-Fi 5 wave2 and newer WiFi interfaces.
Devices with compatible radios also require either the 'wifi-qcom-ac' driver package (for 802.11ac chipsets) or the 'wifi-qcom'  driver package for 802.11ax and newer chipsets.
The configuration menu used to be called 'wifiwave2' in RouterOS versions before 7.13, where it was a part of the 'wifiwave2' software package.
# WiFi Terminology
Before we move on let's familiarize ourselves with terms important for understanding the operation of the menu. These terms will be used throughout the article.
# Basic Configuration
Basic password-protected AP
```
/interface/wifi
set wifi1 disabled=no configuration.country=Latvia configuration.ssid=MikroTik security.authentication-types=wpa2-psk,wpa3-psk security.passphrase=8-63_characters
```
Open AP with OWE transition mode
Opportunistic wireless encryption (OWE) allows the creation of wireless networks that do not require the knowledge of a password to connect, but still offer the benefits of traffic encryption and management frame protection. It is an improvement on regular open access points.
However, since a network cannot be simultaneously encrypted and unencrypted, 2 separate interface configurations are required to offer connectivity to older devices that do not support OWE and offer the benefits of OWE to devices that do.
This configuration is referred to as OWE transition mode.
```
/interface/wifi
add master-interface=wifi1 name=wifi1_owe configuration.ssid=MikroTik_OWE security.authentication-types=owe security.owe-transition-interface=wifi1 configuration.hide-ssid=yes
set wifi1 configuration.country=Latvia configuration.ssid=MikroTik security.authentication-types="" security.owe-transition-interface=wifi1_owe
enable wifi1,wifi1_owe
```
Client devices that support OWE will prefer the OWE interface. If you don't see any devices in your registration table that are associated with the regular open AP, you may want to move on from running a transition mode setup to a single OWE-encrypted interface.
Resetting configuration
WiFi interface configurations can be reset by using the 'reset' command.
```
/interface/wifi reset wifi1
```
Physical interface MAC address to default can be reset by the command 'reset-mac-address'.
```
/interface/wifi reset-mac-address wifi1
```
# Configuration profiles
One of the new WiFi additions is configuration profiles, you can create various presets, that can be assigned to interfaces as needed. Configuration settings for WiFi are grouped inprofilesaccording to the parameter sections found at the end of this page -aaa,channel,configuration,datapath,interworking, andsecurity, and can then be assigned to interfaces.Configurationprofilescan include other profiles as well as separate parameters from other categories.
This optional flexibility is meant to allow each user to arrange their configuration in a way that makes the most sense for them, but it also means that each parameter may have different values assigned to it in different sections of the configuration.
The following priority determines, which value is used:
If you are at any point unsure of which parameter value will be used for an interface, you can issue "/interface/wifi/print detail". The print command will show all values that the interface will have, including inherited values.
To see only values that were configured directly on the interface, without displaying inherited ones, use "/interface/wifi/print config".
For an example of configuration profile usage, see the following:
```
# Creating a security profile, which will be common for both interfaces
/interface wifi security
add name=common-auth authentication-types=wpa2-psk,wpa3-psk passphrase="diceware makes good passwords" wps=disable
# Creating a common configuration profile and linking the security profile to it
/interface wifi configuration
add name=common-conf ssid=MikroTik country=Latvia security=common-auth
# Creating separate channel configurations for each band
/interface wifi channel
add name=ch-2ghz frequency=2412,2432,2472 width=20mhz
add name=ch-5ghz frequency=5180,5260,5500 width=20/40/80mhz
# Assigning to each interface the common profile as well as band-specific channel profile, in case of "no supported channels" message on interfaces, make sure that correct (channel) configuration is applied to each.
/interface wifi
set wifi1 channel=ch-5ghz configuration=common-conf disabled=no
set wifi2 channel=ch-2ghz configuration=common-conf disabled=no
# "print detail" will show all values that interface will use, including inherited ones
[admin@c52i] > interface/wifi/print detail
Flags: M - master; D - dynamic; B - bound; X - disabled, I - inactive, R - running
0 M B  default-name="wifi1" name="wifi1" l2mtu=1560 mac-address=18:FD:74:AF:F4:28 arp-timeout=auto radio-mac=18:FD:74:AF:F4:28 configuration=common-conf
configuration.mode=ap .ssid="MikroTik" .country=Latvia
security.authentication-types=wpa2-psk,wpa3-psk .passphrase="diceware makes good passwords" .wps=disable
channel=ch-5ghz
channel.frequency=5180,5260,5500 .width=20/40/80mhz
1 M B  default-name="wifi2" name="wifi2" l2mtu=1560 mac-address=18:FD:74:AF:F4:29 arp-timeout=auto radio-mac=18:FD:74:AF:F4:29 configuration=common-conf
configuration.mode=ap .ssid="MikroTik" .country=Latvia
security.authentication-types=wpa2-psk,wpa3-psk .passphrase="diceware makes good passwords" .wps=disable
channel=ch-2ghz
channel.frequency=2412,2432,2472 .width=20mhz
# using "print detail config" will show only the values that were directly configured on the interface
[admin@c52i] > interface/wifi/print detail config
Flags: M - master; D - dynamic; B - bound; X - disabled, I - inactive, R - running
0 M B  default-name="wifi1" name="wifi1" l2mtu=1560 mac-address=18:FD:74:AF:F4:28 arp-timeout=auto radio-mac=18:FD:74:AF:F4:28 configuration=common-conf
configuration.mode=ap
channel=ch-5ghz
1 M B  default-name="wifi2" name="wifi2" l2mtu=1560 mac-address=18:FD:74:AF:F4:29 arp-timeout=auto radio-mac=18:FD:74:AF:F4:29 configuration=common-conf
configuration.mode=ap
channel=ch-2ghz
```
# Access List
The access list provides multiple ways of filtering and managing wireless connections.
RouterOS will check each new connection to see if its parameters match the parameters specified in any access list rule.
The rules are checked in the order they appear in the list. Only management actions specified in the first matching rule are applied to each connection.
Connections, which have been accepted by an access list rule, will be periodically checked, to see if they remain within the permittedtimeandsignal-range. If they do not, they will be terminated.
The access list has two kinds of parameters -filtering, andaction. Filtering properties are only used for matching clients, to whom the access list rule should be applied to. Action parameters can change connection parameters for that specific client andpotentially overriding its default connection parameters with ones specified in the access list rule.
# MAC address authentication
Implemented through thequery-radiusaction, MAC address authentication is a way to implement a centralized whitelist of client MAC addresses using a RADIUS server.
When a client device tries to associate with an AP, which is configured to perform MAC address authentication, the AP will send an access-request message to a RADIUS server with the device's MAC address as the user name and an empty password. If the RADIUS server answers with access-accept to such a request, the AP proceeds with whatever regular authentication procedure (passphrase or EAP authentication) is configured for the interface.
# Access rule examples
Only accept connections to guest network from nearby devices during business hours
```
/interface/wifi/access-list/print detail
Flags: X - disabled
0   signal-range=-60..0 allow-signal-out-of-range=5m ssid-regexp="MikroTik Guest" time=7h-19h,mon,tue,wed,thu,fri action=accept
1   ssid-regexp="MikroTik Guest" action=reject
```
Reject connections from locally-administered ('anonymous'/'randomized') MAC addresses
```
/interface/wifi/access-list/print detail
Flags: X - disabled
0   mac-address=02:00:00:00:00:00 mac-address-mask=02:00:00:00:00:00 action=reject
```
Assigning a different passphrase for a specific client can be useful, if you need to provide wireless access to a client, but don't want to share your wireless password, or don't want to create a separate SSID. When the matching client connects to this network, instead of using the password defined in the interface configuration, the access list will make that client use a different password. Just make sure that the specific client doesn't get matched by a more generic access list rule first.
Or reject all unknown MAC addresses, can be added as an ultimate rule, at the end of access list. - If you want to allow only specific clients on the network, make sure to also add a reject rule at the end of access-list, as there is no implicit reject rule by default.
```
/interface wifi access-list
add action=accept disabled=no mac-address=22:F9:70:E5:D2:8E interface=wifi1 passphrase=StrongPassword
```
# Frequency scan
The '/interface/wifi/frequency-scan wifi1' command provides information about RF conditions on available channels that can be obtained by running the frequency-scan command. Used to approximate the spectrum usage, it can be useful to find less crowded frequencies.
# Scan command
The '/interface wifi scan' command will scan for access points and print out information about any APs it detects. It doesn't show the frequency usage, per channel, but it will reveal all access points that are transmitting. You can use the "connect" button, to initiate a connection to a specific AP.
The scan command takes all the same parameters as the frequency-scan command.
# Sniffer
The sniffer command enables monitor mode on a wireless interface. This turns the interface into a passive receiver for all WiFi transmissions.The command continuously prints out information on received packets and can save them locally to a pcap file or stream them using the TZSP protocol.
The sniffer will operate on whichever channel is configured for the chosen interface.
# Spectral scan
The spectral scan can scan frequencies supported by your wifi interface, and plot them directly in the console. The spectral scan has been available since the 7.16beta1 version.
```
/interface/wifi/spectral-scan <wifiinterface name> range=
```
Continuously monitors spectral data. This command uses the same data source as 'spectral-history', and shares many parameters.
To use spectral scan, you must use the "range=" attribute.
Each line displays one spectrogram bucket -- frequency, magnitude (dBm), peak, and a character graphic bar. A bar shows power value with ':' characters and average peak hold with '.' characters.
data- min/max/avg, by default average is used for data. The average should be used in most scenarios, but in some cases "min" can be useful to check if there are any frequencies that have a constant signal output on them. Max represents the strongest signal that was detected during the interval of the scan, similar to the peak.duration- terminate command after a specified time. default is indefinite;freeze-frame-interval- Time interval at which to update command outputinterval- interval of how often to update the primary data values, not peakpeak-mode- avg/max/disabled - peak reflects the strongest signal over peak-hold-duration. By default "avg" is used, it is the average of max values over "peak-hold-duration", if "max" is used, then the highest value will be shown until the next "peak-hold-duration" update.peak-hold-duration- changes the peak hold duration used by peak-mode, by default 5 seconds.range- scan specific range, required;resolution- frequency step for spectral scanshow-interference- yes/no
```
data
```
```
duration
```
```
freeze-frame-interval
```
```
interval
```
```
peak-mode
```
```
peak-hold-duration
```
```
range
```
```
resolution
```
```
show-interference
```
Possible types of classified interference:
```
MWO
```
```
CW
```
```
WIFI
```
```
CORDLESS24
```
```
CORDLESS5
```
```
BLUETOOTH
```
```
FHSS
```
# Spectral history
```
/interface/wifi/spectral-history <wifi interface name> range=
```
Plots spectrogram. Power values that fall in different ranges are printed as different colored characters with the same foreground and background color, so it is possible to copy and paste the terminal output of this command.
data- min/max/avg, by default average is used for data. The average should be used in most scenarios, but in some cases "min" can be useful to check if there are any frequencies that have a constant signal output on them. Max will show the strongest signal that was detected, instead of the average signal.interv- interval of how often to update the data values;interval- interval at which spectrogram lines are printed;duration- terminate command after a specified time. default is indefinite;range- scan specific range, required;resolution- frequency step;show-interference- yes/no
```
data
```
```
interv
```
```
interval
```
```
duration
```
```
range
```
```
resolution
```
```
show-interference
```
Possible types of classified interference:
```
O
```
```
C
```
```
W
```
```
T
```
```
T
```
```
B
```
```
B
```
```
F
```
# WPS
# WPS client
The wps-client command enables obtaining authentication information from a WPS-enabled AP.
```
/interface/wifi/wps-client wifi1
```
# WPS server
An AP can be made to accept WPS authentication by a client device for 2 minutes by running the following command.
```
/interface/wifi wps-push-button wifi1
```
# Radios
Information about the capabilities of each radio can be gained by running the `/interface/wifi/radio print detail` command.  It can be useful to see what bands are supported by the interface and what channels can be selected. The country profile that is applied to the interface will influence the results.
```
interface/wifi/radio/print detail
Flags: L - local
0 L radio-mac=48:A9:8A:0B:F7:4A phy-id=0 tx-chains=0,1 rx-chains=0,1
bands=5ghz-a:20mhz,5ghz-n:20mhz,20/40mhz,5ghz-ac:20mhz,20/40mhz,20/40/80mhz,5ghz-ax:20mhz,
20/40mhz,20/40/80mhz
ciphers=tkip,ccmp,gcmp,ccmp-256,gcmp-256,cmac,gmac,cmac-256,gmac-256 countries=all
5g-channels=5180,5200,5220,5240,5260,5280,5300,5320,5500,5520,5540,5560,5580,5600,5620,5640,5660,
5680,5700,5720,5745,5765,5785,5805,5825
max-vlans=128 max-interfaces=16 max-station-interfaces=3 max-peers=120 hw-type="QCA6018"
hw-caps=sniffer interface=wifi1 current-country=Latvia
current-channels=5180/a,5180/n,5180/n/Ce,5180/ac,5180/ac/Ce,5180/ac/Ceee,5180/ax,5180/ax/Ce,
5180/ax/Ceee,5200/a,5200/n,5200/n/eC,5200/ac,5200/ac/eC,5200/ac/eCee,5200/ax...
...5680/n/eC,5680/ac,5680/ac/eC,5680/ax,5680/ax/eC,5700/a,5700/n,5700/ac,5700/ax
current-gopclasses=115,116,128,117,118,119,120,121,122,123 current-max-reg-power=30
```
While Radio information gives us information about supported channel width, it is also possible to deduce this information from the product page, to do so you need to check the following parameters:number of chains,max data rate. Once you know these parameters, you need to check the modulation and coding scheme (MCS) table, for example, here:https://mcsindex.com/.
If we take hAP ax2, as an example, we can see that number of chains is 2, and the max data rate is 1200 - 1201 in the MCS table. In the MCS table we need to find entry for 2 spatial streams - chains, and the respective data rate, which in this case shows us that 80MHz is the maximum supported channel width.
# Registration table
'/interface/wifi/registration-table/' displays a list of connected wireless clients and detailed information about them.
# De-authentication
Wireless peers can be manually de-authenticated (forcing re-association) by removing them from the registration table.
```
/interface/wifi/registration-table remove [find where mac-address=02:01:02:03:04:05]
```
# WiFi CAPsMAN
WiFi CAPsMAN allows applying wireless settings to multiple MikroTik WiFi AP devices from a central configuration interface.
More specifically, the Controlled Access Point system Manager (CAPsMAN) allows the centralization of wireless network management. When using the CAPsMAN feature, the network will consist of a number of 'Controlled Access Points' (CAP) that provide wireless connectivity and a 'system Manager' (CAPsMAN) that manages the configuration of the APs, it also takes care of client authentication.
WiFi CAPsMAN only passes wireless configuration to the CAP, all forwarding decisions are left to the CAP itself - there is no CAPsMAN forwarding mode.
Requirements:
# Radio Provisioning
CAPsMAN distinguishes between actual wireless interfaces (radios) based on their built-in MAC address (radio-mac). This implies that it is impossible to manage two radios with the same MAC address on one CAPsMAN. Radios currently managed by CAPsMAN (provided by connected CAPs) are listed in/interface/wifi/radiomenu, this list will also include the built-in wifi interfaces that are present on CAPsMAN itself if there are any:
```
/interface/wifi/radio
```
```
[admin@c52i] > interface/wifi/radio/print
Flags: L - LOCAL
Columns: CAP, RADIO-MAC, INTERFACE
# CAP                  RADIO-MAC          INTERFACE
0 L                      18:FD:74:AF:F4:28  wifi1
1 L                      18:FD:74:AF:F4:29  wifi2
2   hapAX3@192.168.88.30  48:A9:8A:0B:F7:4B  cap1
```
When CAP connects, CAPsMAN at first tries to bind each CAP radio to CAPsMAN master interface based on radio-mac. If an appropriate interface is found, the radio gets set up using master interface configuration and configuration of slave interfaces that refer to a particular master interface. At this moment interfaces (both master and slaves) are considered bound to radio and radio is considered provisioned. This happens only if there were matching static entries already present under/interface/wifi, typically if the entry was made previously either manually, or with provisioning rules that contain action "create-enabled" or "create-disabled".
```
/interface/wifi
```
If no matching master interface for radio is found, CAPsMAN executes 'provisioning rules', which are defined under/interface/wifi/provisioning/. Provisioning rules is an ordered list of rules that contain settings that specify which radio to match and settings that determine what action to take if a radio matches.
```
/interface/wifi/provisioning/
```
When CAP joins CAPsMAN, and there is no matching interface for it present under/interface/wifi, provisioning rules will automatically be checked, once a match is found, the CAP's wireless interface will appear under/interface/wifi. Such an interface is "provisioned", provisioned in this context means that there is a wifi interface present for the radio, and it has a configuration profile assigned to it.
```
/interface/wifi
```
```
/interface/wifi
```
There is also an option to manually provision interfaces, which will make CAPsMAN start evaluating provisioning rules against the specific interface, and a new interface will be created upon match. If there was already an entry present for the radio under/interface/wifi/, that entry will be deleted and re-created. Manual provisioning re-creates the interface and isgenerally not needed, since provisioning rules are evaluated automatically, and if you change the configuration profile associated with the provisioning rule, the changes will be applied to all wifi interfaces that use that configuration. If you manually provision interfaces, the interface ID or name can change, resulting in broken references to other objects, for example, bridge ports.
```
/interface/wifi/
```
Manual provision can be done under/interface/wifi/capsman/remote-cap/provisionto provision all radios associated with specific CAPs, it can also be done under/interface/wifi/radio/provision, to provision specific radios.
```
/interface/wifi/capsman/remote-cap/provision
```
```
/interface/wifi/radio/provision
```
CAPsMAN cannot manage it's own wifi interfaces usingconfiguration.manager=capsman, it is enough to just set the same configuration profile on local interfaces manually as you would with provisioning rules, and the end result will be the same as if they were CAPs. That being said, it is also possible to provision local interfaces via/interface/wifi/radiomenu, it should be noted that to regain control of local interfaces after provisioning, you will need to disable the matching provisioning rules and press "provision" again, which will return local interfaces to an unconfigured state.
```
configuration.manager=capsman
```
```
/interface/wifi/radio
```
# CAPsMAN - CAP simple configuration example:
CAPsMAN in WiFi uses the same menu as a regular WiFi interface, meaning when you pass configuration to CAPs, you have to use the same configuration, security, channel configuration, etc. as you would for regular WiFi interfaces.
CAPsMAN:
```
# create a security profile
/interface wifi security
add authentication-types=wpa3-psk name=sec1 passphrase=HaveAg00dDay
# create configuraiton profiles to use for provisioning
/interface wifi configuration
add country=Latvia name=5ghz security=sec1 ssid=CAPsMAN_5
add name=2ghz security=sec1 ssid=CAPsMAN2
add country=Latvia name=5ghz_v security=sec1 ssid=CAPsMAN5_v
# configure provisioning rules, configure band matching as needed
/interface wifi provisioning
add action=create-dynamic-enabled master-configuration=5ghz slave-configurations=5ghz_v supported-bands=\
5ghz-n
add action=create-dynamic-enabled master-configuration=2ghz supported-bands=2ghz-n
# enable CAPsMAN service
/interface wifi capsman
set ca-certificate=auto enabled=yes
```
CAP:
```
# enable CAP service, in this case CAPsMAN is on same LAN, but you can also specify "caps-man-addresses=x.x.x.x" here
/interface/wifi/cap set enabled=yes
# set configuration.manager= on the WiFi interface that should act as CAP
/interface/wifi/set wifi1,wifi2 configuration.manager=capsman-or-local
```
# CAPsMAN - CAP VLAN configuration example:
In this example, we will assign VLAN10 to our main SSID, and will add VLAN20 for the guest network, ether5 from CAPsMAN is connected to CAP.
# CAPsMAN:
```
/interface bridge
add name=br vlan-filtering=yes
/interface vlan
add interface=br name=MAIN vlan-id=10
add interface=br name=GUEST vlan-id=20
/interface wifi datapath
add bridge=br name=MAIN vlan-id=10
add bridge=br name=GUEST vlan-id=20
/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk ft=yes ft-over-ds=yes name=Security_MAIN passphrase=HaveAg00dDay
add authentication-types=wpa2-psk,wpa3-psk ft=yes ft-over-ds=yes name=Security_GUEST passphrase=HaveAg00dDay
/interface wifi configuration
add datapath=MAIN name=MAIN security=Security_MAIN ssid=MAIN_Network
add datapath=GUEST name=GUEST security=Security_GUEST ssid=GUEST_Network
/ip pool
add name=dhcp_pool0 ranges=192.168.1.2-192.168.1.254
add name=dhcp_pool1 ranges=192.168.10.2-192.168.10.254
add name=dhcp_pool2 ranges=192.168.20.2-192.168.20.254
/ip dhcp-server
add address-pool=dhcp_pool0 disabled=yes interface=br name=dhcp1
add address-pool=dhcp_pool1 interface=MAIN name=dhcp2
add address-pool=dhcp_pool2 interface=GUEST name=dhcp3
/interface bridge port
add bridge=br interface=ether5
add bridge=br interface=ether4
add bridge=br interface=ether3
add bridge=br interface=ether2
/interface bridge vlan
add bridge=br tagged=br,ether5,ether4,ether3,ether2 vlan-ids=20
add bridge=br tagged=br,ether5,ether4,ether3,ether2 vlan-ids=10
/interface wifi capsman
set enabled=yes interfaces=br
/interface wifi provisioning
add action=create-dynamic-enabled master-configuration=MAIN slave-configurations=GUEST supported-bands=5ghz-ax
add action=create-dynamic-enabled master-configuration=MAIN slave-configurations=GUEST supported-bands=2ghz-ax
/ip address
add address=192.168.1.1/24 interface=br network=192.168.1.0
add address=192.168.10.1/24 interface=MAIN network=192.168.10.0
add address=192.168.20.1/24 interface=GUEST network=192.168.20.0
/ip dhcp-server network
add address=192.168.1.0/24 gateway=192.168.1.1
add address=192.168.10.0/24 gateway=192.168.10.1
add address=192.168.20.0/24 gateway=192.168.20.1
/system identity
set name=cAP_Controller
```
# CAP using "wifi-qcom" package:
```
/interface bridge
add name=bridgeLocal
/interface wifi datapath
add bridge=bridgeLocal comment=defconf disabled=no name=capdp
/interface wifi
set [ find default-name=wifi1 ] configuration.manager=capsman datapath=capdp disabled=no
set [ find default-name=wifi2 ] configuration.manager=capsman datapath=capdp disabled=no
/interface bridge port
add bridge=bridgeLocal comment=defconf interface=ether1
add bridge=bridgeLocal comment=defconf interface=ether2
add bridge=bridgeLocal comment=defconf interface=ether3
add bridge=bridgeLocal comment=defconf interface=ether4
add bridge=bridgeLocal comment=defconf interface=ether5
/interface wifi cap
set discovery-interfaces=bridgeLocal enabled=yes slaves-datapath=capdp
/ip dhcp-client
add interface=bridgeLocal disabled=no
```
# CAP using "wifi-qcom-ac" package:
```
/interface bridge
add name=bridgeLocal vlan-filtering=yes
/interface wifi
set [ find default-name=wifi1 ] configuration.manager=capsman disabled=no
set [ find default-name=wifi2 ] configuration.manager=capsman disabled=no
add disabled=no  master-interface=wifi1 name=wifi21
add disabled=no  master-interface=wifi2 name=wifi22
/interface bridge port
add bridge=bridgeLocal comment=defconf interface=ether1
add bridge=bridgeLocal comment=defconf interface=ether2
add bridge=bridgeLocal comment=defconf interface=ether3
add bridge=bridgeLocal comment=defconf interface=ether4
add bridge=bridgeLocal comment=defconf interface=ether5
add bridge=bridgeLocal interface=wifi1 pvid=10
add bridge=bridgeLocal interface=wifi21 pvid=20
add bridge=bridgeLocal interface=wifi2 pvid=10
add bridge=bridgeLocal interface=wifi22 pvid=20
/interface bridge vlan
add bridge=bridgeLocal tagged=ether1 untagged=wifi1,wifi2 vlan-ids=10
add bridge=bridgeLocal tagged=ether1 untagged=wifi21,wifi22 vlan-ids=20
/interface wifi cap
set discovery-interfaces=bridgeLocal enabled=yes slaves-static=yes
```
Additionally, the configuration below has to be added to theCAPsMAN configuration:
```
/interface wifi datapath
add bridge=br name=DP_AC
/interface wifi configuration
add datapath=DP_AC name=MAIN_AC security=Security_MAIN ssid=MAIN_Network
add datapath=DP_AC name=GUEST_AC security=Security_GUEST ssid=GUEST_Network
/interface wifi provisioning
add action=create-dynamic-enabled master-configuration=MAIN_AC slave-configurations=GUEST_AC supported-bands=5ghz-ac
add action=create-dynamic-enabled master-configuration=MAIN_AC slave-configurations=GUEST_AC supported-bands=2ghz-n
```
# CAPsMAN - OWE configuration example:
# CAPsMAN:
```
/interface wifi configuration
add country=Latvia disabled=no hide-ssid=yes name=OWE security.authentication-types=owe .management-encryption=cmac .owe-transition-interface=auto ssid=MikroTik_OWE
add country=Latvia disabled=no name=open security.owe-transition-interface=auto ssid=Mikrotik_open
/interface wifi provisioning
add action=create-dynamic-enabled disabled=no master-configuration=open slave-configurations=OWE
/interface wifi capsman
set ca-certificate=auto enabled=yes
```
# CAP:
```
/interface/wifi/cap set enabled=yes
/interface/wifi/set wifi1,wifi2 configuration.manager=capsman-or-local
```
# Advanced examples
Enterprise wireless security with User Manager v5
# Replacing 'wireless' package
Some MikroTik Wi-Fi 5 APs, which ship with their interfaces managed by the 'wireless' menu, can install the additional 'wifi-qcom-ac' package to make their interfaces compatible with the 'wifi' menu instead.
To do this, it is necessary to uninstall the 'wireless' package, then install 'wifi-qcom-ac'.
# Compatibility
The wifi-qcom-acpackage includes alternative drivers for IPQ4018/4019 and QCA9984 radios that make them compatible with the WiFi configuration menu. For possible, wifi-qcom-ac/wifi-qcom/wireless, package combinations, please see the package types sectionhere.
As a rule of thumb, the package is compatible with 802.11ac products, which have an ARM CPU. It is NOT compatible with any of our 802.11ac products which have a MIPS CPU.
Compatibility | Devices
-----------------------
Compatible | Audience, Audience LTE kit, Chateau (all variants of D53), hAP ac^2, hAP ac^3, cAP ac, cAP XL ac,LDF 5 ac,LHG XL 5 ac,LHG XL 52 ac,NetMetal ac^2, mANTBox 52 15s,wAP ac (RBwAPG-5HacD2HnD),SXTsq 5 ac
Incompatible | RB4011iGS+5HacQ2HnD-IN (no support for the 2.4GHz interface),Cube 60Pro ac (no support for 60GHz interface), wAP ac (RBwAPG-5HacT2HnD) andall other devices with a MIPSBE CPU
# Benefits
# Lost features
The following notable features are lost when running 802.11ac products with drivers that are compatible with the 'wifi' management interface
# Property Reference
# AAA properties
Properties in this category configure an access point's interaction with AAA (RADIUS) servers.
Certain parameters in the table below takeformat-stringas their value. In aformat-string, certain characters are interpreted in the following way:
Character | Interpretation
--------------------------
a | Hexadecimal character making up the MAC address of the client device in lowercase
A | Hexadecimal character making up the MAC address of the client device in upper case
i | Hexadecimal character making up the MAC address of the AP's interface in lowercase
I (capital 'i') | Hexadecimal character making up the MAC address of the AP's interface in upper case
N | The entire name of the AP's interface (e.g. 'wifi1')
S | The entire SSID
All other characters are used without interpreting them in any way. For examples, see default values.
Property | Description
----------------------
called-format(format-string;Default:II-II-II-II-II-II:S) | Format for the value of the Called-Station-Id RADIUS attribute, in AP's messages to RADIUS servers.
calling-format(format-string;Default:AA:AA:AA:AA:AA:AA) | Format for the value of the Calling-Station-Id RADIUS attribute, in AP's messages to RADIUS servers.
interim-update(time interval; Default:5m) | Interval at which to send interim updates about traffic accounting to the RADIUS server.
mac-caching(time interval;Default:disabled) | Length of time to cache RADIUS server replies, when MAC address authentication is enabled.This resolves issues with client device authentication timing out due to (comparatively high latency of RADIUS server replies.
name(string;Default:no) | A unique name for the AAA profile.
nas-identifier(string) | Value of the NAS-Identifier attribute, in AP's messages to RADIUS servers. Defaults to the host name of the device (/system/identity).
password-format(format-string) | Format for value to use in calculating the value of the User-Password attribute in AP's messages to RADIUS servers when performing MAC address authentication.Default value: "" (an empty string).
username-format(format-string;Default:AA:AA:AA:AA:AA:AA) | Format for the value of the User-Name attribute in APs messages to RADIUS servers when performing MAC address authentication.
Description
Format for the value of the Called-Station-Id RADIUS attribute, in AP's messages to RADIUS servers.
```
AA:AA:AA:AA:AA:AA
```
```
)
```
Length of time to cache RADIUS server replies, when MAC address authentication is enabled.This resolves issues with client device authentication timing out due to (comparatively high latency of RADIUS server replies.
Format for value to use in calculating the value of the User-Password attribute in AP's messages to RADIUS servers when performing MAC address authentication.
Default value: "" (an empty string).
```
AA:AA:AA:AA:AA:AA
```
```
)
```
Format for the value of the User-Name attribute in APs messages to RADIUS servers when performing MAC address authentication.
# Channel properties
Properties in this category specify the desired radio channel.
Property | Description
----------------------
band(2ghz-g|2ghz-n|2ghz-ax|5ghz-a|5ghz-ac|5ghz-an|5ghz-ax) | Frequency band and wireless standard that will be used by the AP. Defaults to newest supported standard.Note that band support is limited by radio capabilities.
frequency(list of integers or integer ranges) | For an interface in AP mode, specifies frequencies (in MHz) to consider when picking control channel center frequency.For an interface in station mode, specifies frequencies on which to scan for APs.Leave unset (default) to consider all frequencies supported by the radio and permitted by the applicable regulatory profille.The parameter can contain 1 or more comma-separated values of integers or, optionally, ranges of integers denoted using the syntax RangeBeginning-RangeEnd:RangeStepExamples of valid channel.frequency values:24122412,2432,24725180-5240:20,5500-5580:20
secondary-frequency(list of integers| 'disabled') | Frequency (in MHz) to use for the center of the secondary part of a split 80+80MHz channel.Onlyofficial 80MHz channels(5210, 5290, 5530, 5610, 5690, 5775) are supported.Leave unset (default) for automatic selection of secondary channel frequency.
skip-dfs-channels(10min-cac|all|disabled; default:disabled) | Whether to avoid using channels, on which channel availability check (listening for presence of radar signals) is required.10min-cac- interface will avoid using channels, on which 10 minute long CAC is requiredall- interface will avoid using all channels, on which CAC is requireddisabled- interface may select any supported channel, regardless of CAC requirements
width(20mhz|20/40mhz|20/40mhz-Ce|20/40mhz-eC|20/40/80mhz|20/40/80+80mhz|20/40/80/160mhz) | Width of radio channel. Defaults to widest channel supported by the radio hardware.
reselect-interval(time interval;Default:disabled) | Specifies when the interface should rescan channel availability and select the most appropriate one to use. Specifying interval will allow the system to select this interval dynamically and randomly. This helps to avoid a situation when many APs at the same time scan the network, select the same channel, and prefer to use it at the same time. reselect-interval uses a background scan.The reselect process will choose the most suitable channel considering the number of networks in the channel, channel usage, and overlap with networks in adjacent channels. It can be used with a list of frequencies defined, or withfrequencynot set - using all supported frequencies.
Frequency band and wireless standard that will be used by the AP. Defaults to newest supported standard.Note that band support is limited by radio capabilities.
For an interface in AP mode, specifies frequencies (in MHz) to consider when picking control channel center frequency.
For an interface in station mode, specifies frequencies on which to scan for APs.
Leave unset (default) to consider all frequencies supported by the radio and permitted by the applicable regulatory profille.
The parameter can contain 1 or more comma-separated values of integers or, optionally, ranges of integers denoted using the syntax RangeBeginning-RangeEnd:RangeStep
Examples of valid channel.frequency values:
Frequency (in MHz) to use for the center of the secondary part of a split 80+80MHz channel.
Onlyofficial 80MHz channels(5210, 5290, 5530, 5610, 5690, 5775) are supported.
Leave unset (default) for automatic selection of secondary channel frequency.
Whether to avoid using channels, on which channel availability check (listening for presence of radar signals) is required.
Width of radio channel. Defaults to widest channel supported by the radio hardware.
Specifies when the interface should rescan channel availability and select the most appropriate one to use. Specifying interval will allow the system to select this interval dynamically and randomly. This helps to avoid a situation when many APs at the same time scan the network, select the same channel, and prefer to use it at the same time. reselect-interval uses a background scan.
The reselect process will choose the most suitable channel considering the number of networks in the channel, channel usage, and overlap with networks in adjacent channels. It can be used with a list of frequencies defined, or withfrequencynot set - using all supported frequencies.
```
frequency
```
# Configuration properties
This section includes properties relating to the operation of the interface and the associated radio.
Property | Description
----------------------
antenna-gain(integer 0..30) | Overrides the default antenna gain. Themasterinterface of each radio sets the antenna gain for every interface which uses the same radio.This setting cannot override the antenna gain to be lower than the minimum antenna gain of a radio.No default value.
beacon-interval(time interval 100ms..1s; default:100ms) | Interval between beacon frames of an AP.
chains(list of integer 0..7) | Radio chainsto use for receiving signals. Defaults to all chains available to the corresponding radio hardware.
country(name of a country; default:Latvia) | Determines, which regulatory domain restrictions are applied to an interface.
distance() | Maximum link distance in kilometers, needs to be set for long-range outdoor links. The value should reflect the distance to the AP or station that is furthest from the device. Unconfigured value allows usage of 2 km links.
dtim-period(integer 1..255; default:1) | Period at which to transmit multicast traffic, when there are client devices in power save mode connected to the AP. Expressed as a multiple of the beacon interval.Higher values enable client devices to save more energy, but increase network latency.
hide-ssid(no | yes; default:no) | yes- AP does not include its SSID in beacon frames, and does not reply to probe requests that have broadcast SSID.no- AP includes its SSID in the beacon frames, and replies to probe requests that have broadcast SSID.
manager (capsman|capsman-or-local|local; default:local) | capsman - the interface will act as CAP only, this option shouldnotbe passed via provisioning rules to the CAPcapsman-or-local - the interface will get configuration via CAPsMAN or use its own, if /interface/wifi/cap is not enabled.local - interface won't contact CAPsMAN in order to get configuration.
max-clients(integer 1..1000; default:1000) | Maximum number of associated clients.
mode(ap|station) | Interface operation modeap(default) - interface operates as an access pointstation- interface acts as a client device, scanning for access points advertising the configured SSIDstation-bridge - interface acts as a client device and enables support for a 4-address frame format, so that the interface can be used as a bridge portstation-pseudobridge - the interface keeps track of outgoing IP connections and performs MAC address translation similarly to how IP masquerading works
multicast-enhance(enabled|disabled; default:disabled) | With the multicast-enhance feature enabled, an AP will convert every multicast-addressed IP or IPv6 packet into multiple unicast-addressed frames for each connected station.This may improve link throughput and reliability since, unlike multicast frames, unicasts are acknowledged by stations and transmitted using a higher data rate.
qos-classifier(dscp-high-3-bits|priority; default:priority) | dscp-high-3-bits - interface will transmit data packets using a WMM priority equal to the value of the 3 most significant bits of the IP DSCP fieldpriority - interface will transmit data packets using a WMM priority equal to that set by IP firewall or bridge filter
ssid(string; default:no) | The name of the wireless network, aka the (E)SSID.
station-roaming(no | yes; Default:no) | Wifi interface running in station or station-bridge mode will periodically scan for AP candidates to roam to, the weaker the signal to AP is, the more often the scan will be performed. If an AP with a better signal is found, the station will roam to it. FT is supported, and station will respond to BSS Transion Request ifsteering.wnmis enabled.
tx-chains(list of integer 0..7) | Radio chainsto use for transmitting signals. Defaults to all chains available to the corresponding radio hardware.
tx-power(integer 0..40) | A limit on the transmit power (in dBm) of the interface. Can not be used to set power above limits imposed by the regulatory profile. Unset by default.
antenna-gain(integer 0..30)
Overrides the default antenna gain. Themasterinterface of each radio sets the antenna gain for every interface which uses the same radio.
This setting cannot override the antenna gain to be lower than the minimum antenna gain of a radio.No default value.
beacon-interval(time interval 100ms..1s; default:100ms)
Interval between beacon frames of an AP.
chains(list of integer 0..7)
Radio chainsto use for receiving signals. Defaults to all chains available to the corresponding radio hardware.
country(name of a country; default:Latvia)
Determines, which regulatory domain restrictions are applied to an interface.
distance()
Maximum link distance in kilometers, needs to be set for long-range outdoor links. The value should reflect the distance to the AP or station that is furthest from the device. Unconfigured value allows usage of 2 km links.
dtim-period(integer 1..255; default:1)
Period at which to transmit multicast traffic, when there are client devices in power save mode connected to the AP. Expressed as a multiple of the beacon interval.
Higher values enable client devices to save more energy, but increase network latency.
hide-ssid(no | yes; default:no)
yes- AP does not include its SSID in beacon frames, and does not reply to probe requests that have broadcast SSID.
no- AP includes its SSID in the beacon frames, and replies to probe requests that have broadcast SSID.
manager (capsman|capsman-or-local|local; default:local)
capsman - the interface will act as CAP only, this option shouldnotbe passed via provisioning rules to the CAP
capsman-or-local - the interface will get configuration via CAPsMAN or use its own, if /interface/wifi/cap is not enabled.
local - interface won't contact CAPsMAN in order to get configuration.
max-clients(integer 1..1000; default:1000)
Maximum number of associated clients.
Interface operation mode
With the multicast-enhance feature enabled, an AP will convert every multicast-addressed IP or IPv6 packet into multiple unicast-addressed frames for each connected station.This may improve link throughput and reliability since, unlike multicast frames, unicasts are acknowledged by stations and transmitted using a higher data rate.
```
steering.wnm
```
# Datapath properties
Parameters relating to forwarding packets to and from wireless client devices.
Property | Description
----------------------
bridge(bridge interface) | Bridge interface to add interface to, as a bridge port.Virtual ('slave') interfaces are by default added to the same bridge, if any, as the corresponding master interface. Master interfaces are not by default added to any bridge.
bridge-cost(integer; default:10) | Bridge port cost to use when adding as bridge port.
bridge-horizon(none|integer; default:none) | Bridge horizon to use when adding as bridge port.
client-isolation(no|yes; default:no) | Determines whether client devices connecting to this interface are (by default) isolated from others or not.This policy can be overridden on a per-client basis using access list rules, so a an AP can have a mixture of isolated and non-isolated clients.Traffic from an isolated client will not be forwarded to other clients and unicast traffic from a non-isolated client will not be forwarded to an isolated one.
interface-list(interface list; default:no) | List to which add the interface as a member.
vlan-id(none | integer 1..4095; default:none) | Default VLAN ID to assign to client devices connecting to this interface (only relevant to interfaces in AP mode).When a client is assigned a VLAN ID, traffic coming from the client is automatically tagged with the ID and only packets tagged with with this ID are forwarded to the client.
Default VLAN ID to assign to client devices connecting to this interface (only relevant to interfaces in AP mode).When a client is assigned a VLAN ID, traffic coming from the client is automatically tagged with the ID and only packets tagged with with this ID are forwarded to the client.
# Security Properties
Parameters relating to authentication.
Property | Description
----------------------
authentication-types(list of wpa-psk, wpa2-psk, wpa-eap, wpa2-eap, wpa3-psk, owe, wpa3-eap, wpa3-eap-192) | Authentication types to enable on the interface.The default value is an empty list (no authentication, an open network).Configuring a passphrase adds to the default list thewpa2-pskauthentication method (if the interface is an AP) or bothwpa-pskandwpa2-psk(if the interface is a station).Configuring aneap-usernameand aneap-passwordadds to the default listwpa-eap and wpa2-eapauthentication methods.
connect-group(string) | APs within the same connect group do not allow more than 1 client device with the same MAC address. This is to prevent malicious authorized users from intercepting traffic intended to other users ('MacStealer' attack) or performing a denial of service attack by spoofing the MAC address of a victim.Handling of new connections with duplicate MAC addresses depends on the connect-priority of AP interfaces involved.By default, all APs are assigned the same connect-group.
connect-priority(accept-priority/hold-priority (integers)) | These parameters determine, how a connection is handled if the MAC address of the client device is the same as that of another active connection to another AP.If (accept-priority of AP2) < (hold-priority of AP1), a connection to AP2 wil cause the client to be dropped from AP1.If (accept-priority of AP2) = (hold-priority of AP1), a connection to AP2 will be allowed only if the MAC address can no longer be reached via AP1.If (accept-priority of AP2) > (hold-priority of AP1), a connection to AP2 will not be accepted.If omitted, hold-priority is the same as accept-priority.By default, APs, which perform user authentication, have higher priority (lower integer value), than open APs.
dh-groups(list of 19, 20, 21) | Identifiers ofelliptic curve cryptography groupsto use in SAE (WPA3) authentication.
disable-pmkid(no|yes; default:no) | For interfaces in AP mode, disables inclusion of a PMKID in EAPOL frames. Disabling PMKID can cause compatibility issues with client devices that make use of it.yes- Do not include PMKID in EAPOL frames.no- include PMKID in EAPOL frames.
eap-accounting(no|yes; default:no) | Send accounting information to RADIUS server for EAP-authenticated peers.
eap-anonymous-identity(string; default:none) | Optional anonymous identity for EAP outer authentication.
eap-certificate-mode(dont-verify-certificate|no-certificates|verify-certificate|verify-certificate-with-crl; default:dont-verify-certificate) | Policy for handling the TLS certificate of the RADIUS server.verify-certificate - require server to have a valid certificate. Check that it is signed by a trusted certificate authority.dont-verify-certificate - Do not perform any checks on the certificate.no-certificates - Attempt to establish the TLS tunnel by performing anonymous Diffie-Hellman key exchange. To be used if the RADIUS server has no certificate at all.verify-certificate-with-crl - Same asverify-certificate,but also checks if the certificate is valid by checking the Certificate Revocation List.
eap-methods(list ofpeap, tls, ttls) | EAP methods to consider for authentication. Defaults to all supported methods.
eap-password(string; default:none) | Password to use, when the chosen EAP method requires one.
eap-tls-certificate(certificate;default:none) | Name or id of a certificate in the device's certificate store to use, when the chosen EAP authentication method requires one.
eap-username(string;default:none) | Username to use when the chosen EAP method requires one.
encryption(list of  ccmp, ccmp-256, gcmp, gcmp-256, tkip; default:ccmp) | A list of ciphers to support for encrypting unicast traffic.Defaults toccmp.
ft(no | yes: default:no) | Whether to enable 802.11r fast BSS transitions ( roaming).
ft-mobility-domain(integer 0..65535; default:44484 (0xADC4)) | The fast BSS transition mobility domain ID.
ft-nas-identifier(string of2..96 hex characters) | Fast BSS transition PMK-R0 key holder identifier. Default: MAC address of the interface.
ft-over-ds(no|yes;default:no) | Whether to enable fast BSS transitions over DS (distributed system).
ft-preserve-vlanid(no|yes) | no - when a client connects to this AP via 802.11r fast BSS transition, it is assigned a VLAN ID according to the access and/or interface settingsyes (default) - when a client connects to this AP via 802.11r fast BSS transition, it retains the VLAN ID, which it was assigned during initial authenticationThe default behavior is essential when relying on a RADIUS server to assign VLAN IDs to users, since a RADIUS server is only used for initial authentication.
ft-r0-key-lifetime(time interval 1s..6w3d12h15m;Default: 600000s (~7 days)) | Lifetime of the fast BSS transition PMK-R0 encryption key.
ft-reassociation-deadline(time interval 0..70s; default:20s) | Fast BSS transition reassociation deadline.
group-encryption(ccmp|ccmp-256|gcmp|gcmp-256|tkip; default:ccmp) | Cipher to use for encrypting multicast traffic.
group-key-update(time interval; default:24 hours) | The interval at which the group temporal key (key for encrypting broadcast traffic) is renewed.
management-encryption(cmac|cmac-256|gmac|gmac-256; default:cmac) | Cipher to use for encrypting protected management frames.
management-protection(allowed|disabled|required) | Whether to use 802.11w management frame protection.Incompatible with management frame protection in standard wireless package.The default value depends on the value of the selected authentication type. WPA2 allows the use of management protection, WPA3 requires it.
multi-passphrase-group(string) | Name of/interface/wifi/security/multi-passphrase/group that will be used. Only a single group can be defined under the security profile.
owe-transition-interface(interface) | Name or internal id of an interface whose MAC address and SSID to advertise as the matching AP when running in OWE transition mode.Required for setting up open APs that offer OWE, but also work with older devices that don't support the standard. Seeconfiguration example below.
passphrase(string of up to 63 characters) | The passphrase to use for PSK authentication types. Defaults to an empty string - "".WPA-PSK and WPA2-PSK authentication requires a minimum of 8 chars, while WPA3-PSK does not have a minimum passphrase length.
sae-anti-clogging-threshold('disabled'|integer; default:5) | Due to SAE (WPA3) associations being CPU resource intensive, overwhelming an AP with bogus authentication requests makes for a feasible denial-of-service attack.This parameter provides a way to mitigate such attacks by specifying a threshold of in-progress SAE authentications, at which the AP will start requesting that client devices include a cookie bound to their MAC address in their authentication requests. It will then only process authentication requests that contain valid cookies.
sae-max-failure-rate('disabled'|integer; default:40) | Rate of failed SAE (WPA3) associations per minute, at which the AP will stop processing new association requests.
sae-pwe(both|hash-to-element|hunting-and-pecking; default:both) | Methods to support for deriving SAE password element.
wps(disabled|push-button; default:push-button) | push-button- AP will accept WPS authentication for 2 minutes after 'wps-push-button' command is called. Physical WPS button functionality not yet implemented.disabled- AP will not accept WPS authentication
authentication-types(list of wpa-psk, wpa2-psk, wpa-eap, wpa2-eap, wpa3-psk, owe, wpa3-eap, wpa3-eap-192)
Authentication types to enable on the interface.
The default value is an empty list (no authentication, an open network).
Configuring a passphrase adds to the default list thewpa2-pskauthentication method (if the interface is an AP) or bothwpa-pskandwpa2-psk(if the interface is a station).
Configuring aneap-usernameand aneap-passwordadds to the default listwpa-eap and wpa2-eapauthentication methods.
APs within the same connect group do not allow more than 1 client device with the same MAC address. This is to prevent malicious authorized users from intercepting traffic intended to other users ('MacStealer' attack) or performing a denial of service attack by spoofing the MAC address of a victim.
Handling of new connections with duplicate MAC addresses depends on the connect-priority of AP interfaces involved.
By default, all APs are assigned the same connect-group.
These parameters determine, how a connection is handled if the MAC address of the client device is the same as that of another active connection to another AP.If (accept-priority of AP2) < (hold-priority of AP1), a connection to AP2 wil cause the client to be dropped from AP1.If (accept-priority of AP2) = (hold-priority of AP1), a connection to AP2 will be allowed only if the MAC address can no longer be reached via AP1.If (accept-priority of AP2) > (hold-priority of AP1), a connection to AP2 will not be accepted.
If omitted, hold-priority is the same as accept-priority.By default, APs, which perform user authentication, have higher priority (lower integer value), than open APs.
Identifiers ofelliptic curve cryptography groupsto use in SAE (WPA3) authentication.
Policy for handling the TLS certificate of the RADIUS server.
A list of ciphers to support for encrypting unicast traffic.
Defaults toccmp.
Whether to enable 802.11r fast BSS transitions ( roaming).
The fast BSS transition mobility domain ID.
Fast BSS transition PMK-R0 key holder identifier. Default: MAC address of the interface.
Whether to enable fast BSS transitions over DS (distributed system).
The default behavior is essential when relying on a RADIUS server to assign VLAN IDs to users, since a RADIUS server is only used for initial authentication.
Lifetime of the fast BSS transition PMK-R0 encryption key.
Fast BSS transition reassociation deadline.
Cipher to use for encrypting multicast traffic.
The interval at which the group temporal key (key for encrypting broadcast traffic) is renewed.
Cipher to use for encrypting protected management frames.
management-protection(allowed|disabled|required)
Whether to use 802.11w management frame protection.Incompatible with management frame protection in standard wireless package.
The default value depends on the value of the selected authentication type. WPA2 allows the use of management protection, WPA3 requires it.
multi-passphrase-group(string)
Name of/interface/wifi/security/multi-passphrase/group that will be used. Only a single group can be defined under the security profile.
```
/interface/wifi/security/multi-passphrase/
```
owe-transition-interface(interface)
Name or internal id of an interface whose MAC address and SSID to advertise as the matching AP when running in OWE transition mode.
Required for setting up open APs that offer OWE, but also work with older devices that don't support the standard. Seeconfiguration example below.
The passphrase to use for PSK authentication types. Defaults to an empty string - "".
WPA-PSK and WPA2-PSK authentication requires a minimum of 8 chars, while WPA3-PSK does not have a minimum passphrase length.
Due to SAE (WPA3) associations being CPU resource intensive, overwhelming an AP with bogus authentication requests makes for a feasible denial-of-service attack.
This parameter provides a way to mitigate such attacks by specifying a threshold of in-progress SAE authentications, at which the AP will start requesting that client devices include a cookie bound to their MAC address in their authentication requests. It will then only process authentication requests that contain valid cookies.
# Security multi-passphrase properties
/interface/wifi/security/multi-passphrase/
```
/interface/wifi/security/multi-passphrase/
```
multi-passphraseallows the use of PPSK - private pre-shared keys. Added in 7.17beta1.
```
multi-passphrase
```
It can be used by creating an access list entry and settingmulti-passphrase-groupname, or by assigning the group to a security profile that the interface uses.
```
multi-passphrase-group
```
The total limit of supported passphrases is 10000, the limit is shared between all interfaces. When the interface has an associated multi-passphrase group, upon being enabled it will start caching all passphrases from the specified group, while caching is taking place, the authentication will be slower. Once caching is completed there will be no perceptible added delay due to the use of multi-passphrase group.
If an access-list is used to applymulti-passphrase-group, the caching will start upon the first match for the group, and will continue until a match for the passphrase is found.
```
multi-passphrase-group
```
If there are thousands of entries for possible passphrases under a single group - it might take a few minutes for caching to complete, depending on device configuration and model.
group(string) | assigning the group to a security profile or an access list, will enable use of all passphrases defined under it
passphrase(string of up to 63 characters) | The passphrase to use for PSK authentication types. Multiple users can use the same passphrase.Not compatible with WPA3-PSK.
vlan-id(integer 0..4095; Default:) | vlan-id that will be assigned to clients using this passphrase
expires(date and time; "YYYY-MM-DD HH:SS" | The expiration date and time for passphrase specified in this entry, doesn't affect the whole group. Once the date is reached, existing clients using this passphrase will be disconnected, and new clients will not be able to connect using it. If not set, passphrase can be used indefinetly.
isolation(yes|no; Default:no) | Determines whether the client device using this passphrase is isolated from other clients on AP.Traffic from an isolated client will not be forwarded to other clients and unicast traffic from a non-isolated client will not be forwarded to an isolated one.
disabled(yes|no; Default:no) |
assigning the group to a security profile or an access list, will enable use of all passphrases defined under it
The passphrase to use for PSK authentication types. Multiple users can use the same passphrase.
Not compatible with WPA3-PSK.
vlan-id that will be assigned to clients using this passphrase
# Steering properties
Properties in this category govern mechanisms for advertising potential roaming candidates to client devices.
Property | Description
----------------------
neighbor-group(string) | When sending neighbor reports and BSS transition management requests, an AP will list all other APs within its neighbor group as potential roaming candidates.By default, a dynamic neighbor group is created for each set of APs with the same SSID and authentication settings.APs operating in the 5GHz band are indicated to be preferable to ones operating in the 2.4GHz band.
rrm(no|yes; Default:yes) | Enables sending of 802.11k neighbor reports.
wnm(no|yes; Default:yes) | Enables sending of solicited 802.11v BSS transition management requests.
When sending neighbor reports and BSS transition management requests, an AP will list all other APs within its neighbor group as potential roaming candidates.
By default, a dynamic neighbor group is created for each set of APs with the same SSID and authentication settings.APs operating in the 5GHz band are indicated to be preferable to ones operating in the 2.4GHz band.
# Miscellaneous properties
Property | Description
----------------------
arp(disabled|enabled|local-proxy-arp|proxy-arp|reply-only; default:enabled) | Address Resolution Protocol mode:disabled- the interface will not use ARPenabled- the interface will use ARPlocal-proxy-arp- the router performs proxy ARP on the interface and sends replies to the same interfaceproxy-arp- the router performs proxy ARP on the interface and sends replies to other interfacesreply-only- the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in theARPtable. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.
arp-timeout(time interval|'auto'; default:30s) | Determines how long a dynamically added ARP table entry is considered valid since the last packet was received from the respective IP address.Valueautoequals to the value ofarp-timeoutin/ip settings, which defaults to 30s.
disable-running-check(no|yes; default:no) | yes- interface'srunningproperty will be true whenever the interface is not disabledno- interface'srunningproperty will only be true when it has established a link to another device
disabled(no | yes; default:yes) |
mac-address(MAC) | MAC address (BSSID) to use for an interface.Hardware interfaces default to the MAC address of the associated radio interface.Default MAC addresses for virtual interfaces are generated byTaking the MAC address of the associated master interfaceSetting the second-least-significant bit of the first octet to 1, resulting in alocally administered MAC addressIf needed, increment the last octet of the address to ensure it doesn't overlap with the address of another interface on the device
mtu(integer [32..2290]; Default:1500) | Layer 3 Maximum transmission unit.
l2mtu(integer [32..2290]; Default:2290) | Layer 2 Maximum transmission unit.
master-interface(interface; default:none) | Multiple interface configurations can be run simultaneously on every wireless radio.Only one of them determines the radio's state (whether it is enabled, what frequency it's using, etc). This  'master' interface, isboundto a radio with the correspondingradio-mac.To create additional ('virtual') interface configurations on a radio, they need to beboundto the corresponding master interface.
name(string) | A name for the interface. Defaults towifiN, whereNis the lowest integer that has not yet been used for naming an interface.
yes- interface'srunningproperty will be true whenever the interface is not disabled
no- interface'srunningproperty will only be true when it has established a link to another device
disabled(no | yes; default:yes)
mac-address(MAC)
MAC address (BSSID) to use for an interface.
Hardware interfaces default to the MAC address of the associated radio interface.
Default MAC addresses for virtual interfaces are generated by
Taking the MAC address of the associated master interface
Setting the second-least-significant bit of the first octet to 1, resulting in alocally administered MAC address
If needed, increment the last octet of the address to ensure it doesn't overlap with the address of another interface on the device
mtu(integer [32..2290]; Default:1500)
Layer 3 Maximum transmission unit.
l2mtu(integer [32..2290]; Default:2290)
Layer 2 Maximum transmission unit.
master-interface(interface; default:none)
Multiple interface configurations can be run simultaneously on every wireless radio.
Only one of them determines the radio's state (whether it is enabled, what frequency it's using, etc). This  'master' interface, isboundto a radio with the correspondingradio-mac.
To create additional ('virtual') interface configurations on a radio, they need to beboundto the corresponding master interface.
name(string)
A name for the interface. Defaults towifiN, whereNis the lowest integer that has not yet been used for naming an interface.
# Read-only properties
Property | Description
----------------------
bound(boolean) (B) | True formasterinterfaces that are currently available for WiFi manager.True for a virtual interface (configurations linked to a master interface) when both the interface itself and its master interface are not disabled and themasterinterface has a bound flag.
default-name(string) | The default name for an interface.
inactive(boolean) (I) | False for interfaces in AP mode when they've selected a channel for operation (i.e. configuration has been successfully applied).False for interfaces in station mode when they've connected to an AP (i.e. configuration has been successfully applied, and an AP with matching settings has been found).True otherwise.
master(boolean) (M) | True for physical interfaces on the router itself or detected CAP if running as CAPsMAN.False for virtual interfaces.
radio-mac(MAC) | The MAC address of the associated radio.
running(boolean) (R) | True, when an interface has established a link to another device.Ifdisable-running-checkis set to 'yes', true whenever the interface is not disabled.
True formasterinterfaces that are currently available for WiFi manager.
True for a virtual interface (configurations linked to a master interface) when both the interface itself and its master interface are not disabled and themasterinterface has a bound flag.
False for interfaces in AP mode when they've selected a channel for operation (i.e. configuration has been successfully applied).
False for interfaces in station mode when they've connected to an AP (i.e. configuration has been successfully applied, and an AP with matching settings has been found).
True otherwise.
True for physical interfaces on the router itself or detected CAP if running as CAPsMAN.
False for virtual interfaces.
True, when an interface has established a link to another device.
Ifdisable-running-checkis set to 'yes', true whenever the interface is not disabled.
# Access List
Filtering parameters | Parameter | Description
----------------------------------------------
interface(interface|interface-list|any; default:any) | Match if connection takes place on the specified interface or interface belonging to a specified list.
mac-address(MAC address; default:none) | Match if the client device has the specified MAC address.
mac-address-mask(MAC address) | Modifies themac-addressparameter to match if it is equal to the result of performing bit-wise AND operation on the client MAC address and the given address mask.Default: FF:FF:FF:FF:FF:FF (i.e. client's MAC address must match value ofmac-addressexactly)
signal-range(min..max) | Match if the strength of the received signal from the client device is within the given range. Allowed values: '-120..120'
ssid-regexp(regex) | Match if the given regular expression matches the SSID.
time(start-end,days) | Match during the specified time of day and (optionally) days of week. Allow values: 0s-1d
multi-passphrase-group(string) | Name of/interface/wifi/security/multi-passphrase/group that will be used. Only single group can be set under one access list entry.
Filtering parameters
Modifies themac-addressparameter to match if it is equal to the result of performing bit-wise AND operation on the client MAC address and the given address mask.
Default: FF:FF:FF:FF:FF:FF (i.e. client's MAC address must match value ofmac-addressexactly)
```
/interface/wifi/security/multi-passphrase/
```
Action parameters | Parameter | Description
-------------------------------------------
allow-signal-out-of-range(time period | always; default:0s) | The length of time which a connected peer's signal strength is allowed to be outside the range required by thesignal-rangeparameter, before it is disconnected.If the value is set to 'always', peer signal strength is only checked during association.
action(accept|reject|query-radius; default:accept) | Whether to authorize a connectionaccept- connection is allowedreject- connection is not allowedquery-radius-  connection is allowed if MAC address authentication of the client's MAC address succeeds
client-isolation(no|yes; default:none) | Whether toisolatethe client from others connected to the same AP.
passphrase(string;default:none) | Override the default passphrase with given value.
radius-accounting(no|yes;default:none) | Override the default RADIUS accounting policy with given value.
vlan-id(none|integer 1..4095;default:none) | Assign the givenVLAN IDto matched clients.
Action parameters
The length of time which a connected peer's signal strength is allowed to be outside the range required by thesignal-rangeparameter, before it is disconnected.
If the value is set to 'always', peer signal strength is only checked during association.
Whether to authorize a connection
Whether toisolatethe client from others connected to the same AP.
# Frequency scan
Information about RF conditions on available channels can be obtained by running the frequency-scan command.
Command parameters | Parameter | Description
--------------------------------------------
duration(time interval;default:none) | Length of time to perform the scan for before exiting. Useful for non-interactive use.
freeze-frame-interval(time interval; default:1s) | Time interval at which to update command output.
frequency(list of frequencies/ranges) | Frequencies to perform the scan on. Seechannel.frequency parameter syntaxabove for more detail. Defaults to all supported frequencies.
number(string;default:none) | Either the name or internal id of the interface to perform the scan with. Required.
rounds(integer;default:none) | Number of times to go through list of scannable frequencies before exiting. Useful for non-interactive use.
save-file(string;default:none) | Name of file to save output to.
Output parameters | Parameter | Description
-------------------------------------------
channel(integer) | Frequency (in MHz) of the channel scanned.
networks(integer) | Number of access points detected on the channel.
load(integer) | Percentage of time the channel was busy during the scan.
nf(integer) | Noise floor (in dBm) of the channel.
max-signal(integer) | Maximum signal strength (in dBm) of APs detected in the channel.
min-signal(integer) | Minimum signal strength (in dBm) of APs detected in the channel.
primary(boolean) (P) | Channel is in use as the primary (control) channel by an AP.
secondary(boolean) (S) | Channel is in use as a secondary (extension) channel by an AP.
Number of access points detected on the channel.
# Flat-snoop
The '/interface wifi flat-snoop' is a tool for surveying APs and stations. Monitors frequency usage, and displays which devices occupy each frequency. Provides more detailed infromation regarding nearby APs than scan, and offers easy overview of frequency usage by station/AP count.
Output parameters | Parameter | Description
-------------------------------------------
duration(time interval;default:none) | Length of time to perform the scan before exiting. Useful for non-interactive use.
filter-type(bsss|frequency|stas) | bsss - list of active APs and their parameters.frequency - list of station and AP count per scanned frequencystas - a detailed list of stations on each scanned frequencyIf filter-type is unspecified all types will be returned.
freeze-frame-interval(time interval; default:1s) | Time interval at which to update command output.
bsss - list of active APs and their parameters.
frequency - list of station and AP count per scanned frequency
stas - a detailed list of stations on each scanned frequency
If filter-type is unspecified all types will be returned.
# Scan command
The '/interface wifi scan' command will scan for access points and print out information about any APs it detects.
The scan command takes all the same parameters as the frequency-scan command.
Output parameters | Parameter | Description
-------------------------------------------
active(boolean) (A) | This signifies that beacons from the AP have been received in the last 30 seconds.
address(MAC) | The MAC address (BSSID) of the AP.
channel(string) | The control channel frequency used by the AP, its supported wireless standards and control/extension channel layout.
security(string) | Authentication methods supported by the AP.
signal(integer) | The signal strength of the AP's beacons (in dBm).
ssid(string) | The extended service set identifier of the AP.
sta-count(integer) | The number of client devices associated with the AP. Only available if the AP includes this information in its beacons.
security(string)
Authentication methods supported by the AP.
# Sniffer
Command parameters | Parameter | Description
--------------------------------------------
duration(time interval;default:none) | Automatically interrupt the sniffer after the specified time has passed.
filter(string) | A string that specifies a filter to apply to captured frames. Only frames matched by the filter expression will be displayed, saved or streamed.This works similarly to filter strings in libpcap, for example.The filter can matchAddress fields (addr1, addr2, addr3)Wireless frame type and subtype, including shortcuts such as 'beacon' (type == 0 && subtype == 8)Flags (to-ds, from-ds, retry, power, protected)A string can include the following operators:== (exact match)!= (does not equal)&& (logical AND)|| (logical OR)() (for grouping filter expressions)
number(interface) | Interface to use for sniffing.
pcap-file(string) | Save captured frames to a file with the given name. No default value (captured frames are not saved to a file by default).
pcap-size-limit(integer;default:none) | File size limit (in bytes) when storing captured frames locally.When this limit has been reached, no new frames are added to the capture file.
stream-address(IP address;default:none) | Stream captured packets via the TZSP protocol to the given address. No default value (captured packets are not streamed anywhere by default).
stream-rate(integer) | Limit the rate (in packets per second) at which captured frames are streamed via TZSP.
A string that specifies a filter to apply to captured frames. Only frames matched by the filter expression will be displayed, saved or streamed.
This works similarly to filter strings in libpcap, for example.
The filter can match
A string can include the following operators:
number(interface)
# WPS
interface/wifi/wps-client wifi
Command parameters | Parameter | Description
--------------------------------------------
duration(time interval) | Length of time after which the command will time out if no AP is found. Unlimited by default.
interval(time interval; default:1s) | Time interval at which to update command output. Default: 1s.
mac-address(MAC;default:none) | Only attempt connecting to AP with the specified MAC (BSSID).
number(string;default:none) | Name or internal id of the interface with which to attempt a connection.
ssid(string;default:none) | Only attempt to connect to APs with the specified SSID.
# Radios
Information about the capabilities of each radio can be gained by running the `/interface/wifi/radio print detail` command.
Property | Description
----------------------
2g-channels(list ofintegers) | Frequencies supported in the 2.4GHz band.
5g-channels(list of integers) | Frequencies supported in the 5GHz band.
bands(list of strings) | Supported frequency bands, wireless standards, and channel widths.
ciphers(list of strings) | Supported encryption ciphers.
countries(list of strings) | Regulatory domains supported by the interface.
hw-caps(list of strings) | Additional supported features (e.g. sniffer, qos-classifier-dscp).
hw-type(string) | Radio hardware model number.
max-interfaces(integer) | Maximum number of logical interfaces.
max-peers(integer) | Maximum number of associated peers (connected stations).
max-station-interfaces(integer) | Maximum number of logical interfaces in station mode.
max-vlans(integer) | Maximum number of different per-user VLANs.
min-antenna-gain(integer) | Minimum antenna gain permitted for the interface.
phy-id(string) | A unique identifier.
radio-mac(MAC) | MAC address of the radio interface. Can be used to match radios to interface configurations.
rx-chains(list of integers) | IDs for radio chains available for receiving radio signals.
tx-chains(list of integers) | IDs for radio chains available for transmitting radio signals.
A unique identifier.
# Registration table
The registration table contains read-only information about associated wireless devices.
Parameter | Description
-----------------------
authorized(boolean) (A) | True when the peer has successfully authenticated.
auth-type (string) | Authentication type used for the particular client.
band(string) | Band on which particular router is communication with the AP.
bytes(list of integers) | Number of bytes in packets transmitted to a peer and received from it.
interface(string) | Name of the interface, which was used to associate with the peer.
last-activity(time) | last interface data tx/rx activity
mac-address(MAC) | The MAC address of the peer.
packets(list of integers) | Number of packets transmitted to a peer and received from it.
tx-bits-per-second (integer) | Rate of transmitted data to peer per second.
rx-bits-per-second (integer) | Rate of received data from peer per second.
rx-rate(string) | Bitrate of received transmissions from peer.
signal(integer) | Strength of signal received from the peer (in dBm).
ssid(string) | The SSID on which client is connected.
tx-rate(string) | Bitrate used for transmitting to the peer.
uptime(time interval) | Time since association.
vlan-id (integer) | VLAN which is assigned by AP or RADIUS for particular peer traffic.
Strength of signal received from the peer (in dBm).
The SSID on which client is connected.
Time since association.
VLAN which is assigned by AP or RADIUS for particular peer traffic.
# CAPsMAN Global Configuration
Menu: /interface/wifi/capsman
Property | Description
----------------------
ca-certificate(auto|certificate name) | Device CA certificate, CAPsMAN server requires a certificate, certificate on CAP is optional.
certificate(auto | certificate name | none; Default:none) | Device certificate
enabled(no|yes) | Disable or enable CAPsMAN functionality
package-path(string) | Folder location for the RouterOS packages. For example, use "/upgrade" to specify the upgrade folder from the files section. If an empty string is set, CAPsMAN can use built-in RouterOS packages, note that in this case only CAPs with the same architecture as CAPsMAN will be upgraded.
require-peer-certificate(yes | no; Default:no) | Require all connecting CAPs to have a valid certificate
upgrade-policy(none | require-same-version | suggest-same-upgrade; Default:none) | Upgrade policy optionsnone - do not perform upgraderequire-same-version - CAPsMAN suggests to upgrade the CAP RouterOS version and, if it fails it will not provision the CAP. (Manual provision is still possible)suggest-same-version - CAPsMAN suggests to upgrade the CAP RouterOS version and if it fails it will still be provisioned
interfaces(all | interface name | none;Default:all) | Interfaces on which CAPsMAN will listen for layer 2 CAP connections
Disable or enable CAPsMAN functionality
package-path(string)
require-peer-certificate(yes | no; Default:no)
Require all connecting CAPs to have a valid certificate
upgrade-policy(none | require-same-version | suggest-same-upgrade; Default:none)
Upgrade policy options
# CAPsMAN Provisioning
Provisioning rules for matching radios are configured in/interface/wifi/provisioning/menu:
Property | Description
----------------------
action(create-disabled | create-enabled | create-dynamic-enabled | none; Default:none) | Action to take if rule matches are specified by the following settings:create-disabled- create disabled static interfaces for radio. I.e., the interfaces will be bound to the radio, but the radio will not be operational until the interface is manually enabled;create-enabled- create enabled static interfaces. I.e., the interfaces will be bound to the radio and the radio will be operational;create-dynamic-enabled- create enabled dynamic interfaces. I.e., the interfaces will be bound to the radio, and the radio will be operational;none- do nothing, leaves radio in the non-provisioned state;
comment(string) | Short description of the Provisioning rule
common-name-regexp(string) | Regular expression to match radios by common name. Each CAP's common name identifier can be found under "/interface/wifi/radio" as value "REMOTE-CAP-NAME"
supported-bands(2ghz-ax | 2ghz-g | 2ghz-n | 5ghz-a | 5ghz-ac | 5ghz-ax | 5ghz-n;) | Match radios by supported wireless modes.
identity-regexp(string;) | Regular expression to match radios by router identity
address-ranges(IpAddressRange[,IpAddressRanges] max 100x;) | Match CAPs with IPs within the configured address range. Will only work for CAPs that joined CAPsMAN using IP, not MAC address.
master-configuration(string) | Ifactionspecifies to create interfaces, then a new master interface with its configuration set to this configuration profile will be created
name-format(string) | Base string to use when constructing names of provisioned interfaces. Each new interface will be created by taking the base string and appending a number to the end of it, a number will only be appended if the string is not unique.If included in the string, the character sequence%Iwill be replaced by the system identity of the cAP,%Cwill be replaced with the cAP's TLS certificate's Common Name,%R, or%rfor lowercase, will be replaced with the CAP's radio MACDefault: "cap-wifi"
slave-name-format(string) | Base string to use when constructing names of virtual interfaces. Each new interface will be created by taking the base string and appending a number to the end of it, a number will only be appended if the string is not unique.If included in the string, the chraracter sequence%vwill be replaced with "virtual", the chraracter sequence%mwill be replaced with the name of master interface,if included in the string, the character sequence%Iwill be replaced by the system identity of the cAP,%Cwill be replaced with the cAP's TLS certificate's Common Name,%R, or%rfor lowercase, will be replaced with the CAP's radio MACDefault: "master-interface-name-virtual"
radio-mac(MAC address) | MAC address of radio to be matched. No default value.
slave-configurations(string;) | Iftheactionspecifies to create interfaces, then a new slave interface for each configuration profile in this list is created.
disabled(yes| no;) | Specifies if the provision rule is disabled.
Base string to use when constructing names of provisioned interfaces. Each new interface will be created by taking the base string and appending a number to the end of it, a number will only be appended if the string is not unique.
If included in the string, the character sequence%Iwill be replaced by the system identity of the cAP,%Cwill be replaced with the cAP's TLS certificate's Common Name,%R, or%rfor lowercase, will be replaced with the CAP's radio MAC
Default: "cap-wifi"
Base string to use when constructing names of virtual interfaces. Each new interface will be created by taking the base string and appending a number to the end of it, a number will only be appended if the string is not unique.
If included in the string, the chraracter sequence%vwill be replaced with "virtual", the chraracter sequence%mwill be replaced with the name of master interface,if included in the string, the character sequence%Iwill be replaced by the system identity of the cAP,%Cwill be replaced with the cAP's TLS certificate's Common Name,%R, or%rfor lowercase, will be replaced with the CAP's radio MAC
Default: "master-interface-name-virtual"
Iftheactionspecifies to create interfaces, then a new slave interface for each configuration profile in this list is created.
Specifies if the provision rule is disabled.
# CAP configuration
Menu: /interface/wifi/cap
Property | Description
----------------------
caps-man-addresses(list of IP addresses; Default:empty) | List of Manager IP addresses that CAP will attempt to contact during discovery
caps-man-names() | An ordered list of CAPs Manager names that the CAP will connect to, if empty - CAP does not check Manager name
discovery-interfaces(list of interfaces;) | List of interfaces over which CAP should attempt to discover Manager
lock-to-caps-man(no | yes; Default:no) | Sets, if CAP should lock to the first CAPsMAN it connects to
slaves-static() | Creates Static Virtual Interfaces, allows the possibility to assign IP configuration to those interfaces. MAC address is used to remember each static-interface when applying the configuration from the CAPsMAN.
caps-man-certificate-common-names() | List of Manager certificate CommonNames that CAP will connect to, if empty - CAP does not check Manager certificate CommonName
certificate() | Certificate to use for authenticating
enabled(yes | no;Default:no) | Disable or enable the CAP feature
current-caps-man-address () | Shows currently used CAPsMAN address (available since 7.15)
current-caps-man-identity () | Shows currently used CAPsMAN identity (available since 7.15)
slaves-datapath() |
lock-to-caps-man(no | yes; Default:no)
slaves-static()
caps-man-certificate-common-names()