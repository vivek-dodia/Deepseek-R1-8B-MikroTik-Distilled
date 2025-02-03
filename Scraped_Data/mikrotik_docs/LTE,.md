---
title: LTE
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/30146563/LTE,
crawled_date: 2025-02-02T21:11:25.339159
section: mikrotik_docs
type: documentation
---

## 1Summary2LTE Client2.1Properties2.2APN profiles2.3LTE settings2.4LTE esim2.5Scanner2.6User Info command2.6.1Properties (Up to 6.40)2.7Modem firmware-upgrade command2.7.1Modems with firmware update support and connectivity required2.7.2Modem firmware-upgrade command examples:2.8User at-chat command3Quick setup example4Passthrough Example5Dual SIM5.1Boards with switchable SIM slots5.2Usage Example6Tips and Tricks6.1Find device location using Cell information6.2Using Cell lock6.3Cell Monitor7Troubleshooting7.1Locking band on Huawei and other modems7.2mPCIe modems with RB9xx series devices7.3Boards with USB-A port and mPCIe7.4Avoiding tethering speed throttling7.5Unlocking SIM card after multiple wrong PIN code attemptsSummary
* 1Summary
* 2LTE Client2.1Properties2.2APN profiles2.3LTE settings2.4LTE esim2.5Scanner2.6User Info command2.6.1Properties (Up to 6.40)2.7Modem firmware-upgrade command2.7.1Modems with firmware update support and connectivity required2.7.2Modem firmware-upgrade command examples:2.8User at-chat command
* 3Quick setup example
* 4Passthrough Example
* 5Dual SIM5.1Boards with switchable SIM slots5.2Usage Example
* 6Tips and Tricks6.1Find device location using Cell information6.2Using Cell lock6.3Cell Monitor
* 7Troubleshooting7.1Locking band on Huawei and other modems7.2mPCIe modems with RB9xx series devices7.3Boards with USB-A port and mPCIe7.4Avoiding tethering speed throttling7.5Unlocking SIM card after multiple wrong PIN code attempts
* 2.1Properties
* 2.2APN profiles
* 2.3LTE settings
* 2.4LTE esim
* 2.5Scanner
* 2.6User Info command2.6.1Properties (Up to 6.40)
* 2.7Modem firmware-upgrade command2.7.1Modems with firmware update support and connectivity required2.7.2Modem firmware-upgrade command examples:
* 2.8User at-chat command
* 2.6.1Properties (Up to 6.40)
* 2.7.1Modems with firmware update support and connectivity required
* 2.7.2Modem firmware-upgrade command examples:
* 5.1Boards with switchable SIM slots
* 5.2Usage Example
* 6.1Find device location using Cell information
* 6.2Using Cell lock
* 6.3Cell Monitor
* 7.1Locking band on Huawei and other modems
* 7.2mPCIe modems with RB9xx series devices
* 7.3Boards with USB-A port and mPCIe
* 7.4Avoiding tethering speed throttling
* 7.5Unlocking SIM card after multiple wrong PIN code attempts
```
Package: system
Optional lte-mipsbe.npk package is only required for SXT 3-7 built-in modem.
```
Support for Direct-IP mode type cards only. MBIM support is available in RouterOS v7 releases and the MBIM driver is loaded automatically. If the modem is not recognized in RouterOS v6 - Please test it in v7 releases before asking for support in RouterOS v6.
To enable access via a PPP interface instead of a LTE Interface, change the operational mode to "serial" with/interface lte settings set mode=serialCLI command and issue a reboot. Note that using PPP emulation mode you may not get the same throughput speeds as using the LTE interface emulation type.
```
/interface lte settings set mode=serial
```
## LTE Client
```
Sub-menu: /interface lte
```
### Properties
Property | Description
----------------------
allow-roaming(yes | no; Default:no) | Enable data roaming for connecting to other countries' data-providers. Not all LTE modems support this feature. Some modems, that do not fully support this feature, will connect to the network but will not establish an IP data connection with allow-roaming set to no.
apn-profiles(string; Default:default) | Which APN profile to use for this interface
band(integer list; Default:"") | LTE Frequency band used in communicationLTE Bands and bandwidths
nr-band(integer list; Default: "") | 5G NR Frequency band used in communication5G NR Bands and bandwidths
comment(string; Default:"") | Descriptive name of an item
disabled(yes | no; Default:no) | Whether the interface is disabled or not. By default it is enabled.
modem-init(string; Default:"") | Modem init string (AT command that will be executed at modem startup)
mtu(integer; Default:1500) | Maximum Transmission Unit. Max packet size that the LTE interface will be able to send without packet fragmentation.
name(string; Default:"") | Descriptive name of the interface.
network-mode(3g | gsm | lte | 5g) | Select/force mode for LTE interface to operate with
operator(integer; Default:"") | used to lock the device to a specific operator full PLMN number is used for the lock consisting of MCC+MNC.PLMN codes
pin(integer; Default:"") | SIM Card's PIN code.
sms-protocol(at | auto | mbim) | SMS functionality.mbim: uses MBIM driver.at: uses AT-Commands.auto: selects the appropriate option depending on the modem.
```
LTE Bands and bandwidths
```
```
5G NR Bands and bandwidths
```
### APN profiles
All network-related settings are under profiles
```
Sub-menu: /interface lte apn
```
Property | Description
----------------------
add-default-route(yes | no) | Whether to add a default route to forward all traffic over the LTE interface.
apn(string) | Service Provider's Access Point Name
authentication(pap | chap | none; Default:none) | Allowed protocol to use for authentication
default-route-distance(integer; Default:2) | Sets distance value applied to auto-created default route, if add-default-route is also selected. LTE route by default is with distance 2 to prefer wired routes over LTE
ip-type(ipv4 | ipv4-ipv6 | ipv6; Default: ) | Requested PDN type
ipv6-interface(; Default: ) | Interface on which to advertise IPv6 prefix
name(string; Default: ) | APN profile name
number(integer; Default: ) | APN profile number
passthrough-interface(; Default: ) | Interface to passthrough IP configuration (activates passthrough)
passthrough-mac(MAC; Default:auto) | If set to auto, then will learn MAC from the first packet
passthrough-subnet-selection(auto / p2p; Default:auto) | "auto" selects the smallest possible subnet to be used for the passthrough interface. "p2p" sets the passthrough interface subnet as /32 and picks gateway address from 10.177.0.0/16 range. The gateway address stays the same until the apn configuration is changed.
password(string; Default: ) | Password used if any of the authentication protocols are active
use-network-apn(yes | no; Default:yes) | Parameter is available starting from RouterOS v7 and used only for MBIM modems. If set to yes, uses network provided APN.
use-peer-dns(yes | no; Default:yes) | If set to yes, uses DNS received from LTE interface
user(integer) | Username used if any of the authentication protocols are active
### LTE settings
LTE and router-specific LTE settings. The menu is available starting from RouterOS v7.
```
Sub-menu: /interface lte settings
```
Property | Description
----------------------
mode(auto | mbim | serial/user;Default:auto) | Operation mode setting.auto - automatically select the operation mode.serial - provide only serial portsmbim - switch modem into MBIM mode if possibleuser - OS will not attempt to automatically switch the modem mode. (Available from RouterOS 7.16)
firmware-path(string) | Firmware path in host OS.Modem gobi firmware
external-antenna(auto | both | div | main | none; Default:auto) | This setting is only available for "Chateau" routers, except for Chateau 5G versions.auto - measures the signal levels on both internal and external antennas and selects the antennas with the best signal(RSRP).both - both antennas are set to externaldiv - diversity antenna set to externalmain - main antenna set to externalnone - no external antenna selected(using internal antennas)
external-antenna-selected() | This setting is only available for "Chateau" routers, except for Chateau 5G versions. Shows the currently selected antenna if "external-antenna" is set to "auto"
sim-slot() | This setting is available for routers that have switchable SIM slots (LtAP, SXT). Selection options differ between products.
Operation mode setting.
* auto - automatically select the operation mode.
* serial - provide only serial ports
* mbim - switch modem into MBIM mode if possible
* user - OS will not attempt to automatically switch the modem mode. (Available from RouterOS 7.16)
* auto - measures the signal levels on both internal and external antennas and selects the antennas with the best signal(RSRP).
* both - both antennas are set to external
* div - diversity antenna set to external
* main - main antenna set to external
* none - no external antenna selected(using internal antennas)
### LTE esim
All eSIM related commands. The menu is available starting from RouterOS 7.18beta2.
```
Sub-menu: /interface lte esim
```
printcommand is used to list the eSIM profiles for all lte interfaces using eSIM:
```
interface/lte/esim/print
Flags: E - ENABLED          
Columns: INTERFACE, NAME, SPN, UICCID, NICKNAME
#   INTERFACE  NAME           SPN                   UICCID  NICKNAME
0 E lte1       NAME1          SPN1    1111111111111111111   nickname1    
1   lte1       NAME2          SPN2    2222222222222222222   nickname2    
2   lte1       NAME3          SPN3    3333333333333333333   nickname3
```
Commands
Property | Description
----------------------
disable-profile | Disable eSIM profile./interface/lte/esim/disable-profile number=0
enable-profile | Enable eSIM profile./interface/lte/esim/enable-profile number=0
remove-profile | Permanently deletes eSIM profile from the eSIM card./interface/lte/esim/delete-profile number=0
provision | Provision new eSIM profile. The command takes three parameters:interface- the interface for which the eSIM profile will be enabled.matching-id- an activation code token. Example:  matching-id=ABCD10EFGHI5KL6Msm-dp-plus- SM-DP+ server hostnameExample eSIM LPA string decoded from QR:LPA:1$server.example.io$ABCD10EFGHI5KL6M/interface/lte/esim/provision interface=lte1 sm-dp-plus=server.example.iomatching-id=ABCD10EFGHI5KL6M
esim-id | Query the eSIM ID. The command takes one parameter:interface- select the interface for which to query the eSIM ID./interface/lte/esim/esim-id interface=lte1eid: 8903302342630000000004181FFFFFFF
set-nickname | Set a nickname for an eSIM profile./interface/lte/esim/set-nickname number=0 nickname=nickname1
refresh-profile-list | Re-query the eSIM profile list. The command takes one parameter:interface- Select an interface for which the eSIM profiles will be re-queried.
Disable eSIM profile.
```
/interface/lte/esim/disable-profile number=0
```
Enable eSIM profile.
```
/interface/lte/esim/enable-profile number=0
```
Permanently deletes eSIM profile from the eSIM card.
```
/interface/lte/esim/delete-profile number=0
```
Provision new eSIM profile. The command takes three parameters:
* interface- the interface for which the eSIM profile will be enabled.
* matching-id- an activation code token. Example:  matching-id=ABCD10EFGHI5KL6M
* sm-dp-plus- SM-DP+ server hostname
Example eSIM LPA string decoded from QR:LPA:1$server.example.io$ABCD10EFGHI5KL6M
```
/interface/lte/esim/provision interface=lte1 sm-dp-plus=server.example.iomatching-id=ABCD10EFGHI5KL6M
```
Query the eSIM ID. The command takes one parameter:
* interface- select the interface for which to query the eSIM ID.
```
/interface/lte/esim/esim-id interface=lte1eid: 8903302342630000000004181FFFFFFF
```
Set a nickname for an eSIM profile.
```
/interface/lte/esim/set-nickname number=0 nickname=nickname1
```
Re-query the eSIM profile list. The command takes one parameter:
* interface- Select an interface for which the eSIM profiles will be re-queried.
### Scanner
It is possible to scan LTE interfaces with/interface lte scancommand. Example:
```
/interface lte scan
```
```
[admin@MikroTik] > /interface lte scan duration=60 number=0 
Columns: OPERATOR, MCC-MNC, RSSI, RSRP, RSRQ
OPERATOR  MCC-MNC  RSSI    RSRP    RSRQ
LMT         24701  -36dBm  -63dBm  -7dB
```
Available properties:
Property | Description
----------------------
duration(integer) | Duration of scan in seconds
freeze-frame-interval(integer) | time between data printout
number(integer) | Interface number or name
### User Info command
It is possible to send a special "info" command to LTE interface with/interface lte infocommand. In RouterOS v7 this command is moved to/interface lte monitormenu.
```
/interface lte info
```
```
/interface lte monitor
```
#### Properties (Up to 6.40)
Property | Description
----------------------
user-command(string; Default:"") | send a command to the LTE card to extract useful information, e.g. with AT commands
user-command-only(yes | no; Default: ) |
### Modem firmware-upgrade command
Command allows to check and upgrade modem firmware if update is available for supported MikroTik modems.
For firmware update availability check and installation active internet connection is required, depending on modem internet connection can be provided using any  RouterOS  interface or modem interface (FOTA), please see table bellow regarding each modem supported connection methods.
Arguments / Properties | Description
------------------------------------
upgrade(yes | no; Default:no) | Set command execution mode:no- display current modem firmware version and show latest available firmware versionyes- performs firmware installation
update-channel(stable | testing; Default:stable) | Sets which firmware update channel is used:stable- firmware version for general usetesting- early access/testing channel where modem firmware is published before releasing it in stable channelFeature available from v7.17beta2.
firmware-file(string; Default:"" ) | Allows to override firmware update source and perform upgrade from custom location (file, url) in environments where upgrade using internet connection to MikroTik upgrade servers is not a viable option, eg private networks etc.
Set command execution mode:
* no- display current modem firmware version and show latest available firmware version
* yes- performs firmware installation
update-channel(stable | testing; Default:stable)
Sets which firmware update channel is used:
* stable- firmware version for general use
* testing- early access/testing channel where modem firmware is published before releasing it in stable channel
Feature available from v7.17beta2.
firmware-file(string; Default:"" )
Allows to override firmware update source and perform upgrade from custom location (file, url) in environments where upgrade using internet connection to MikroTik upgrade servers is not a viable option, eg private networks etc.
#### Modems with firmware update support and connectivity required
Use command/interface lte monitor [find] oncereturned property "model" for installed modem model identification.
Modem | Required connectivity to MikroTik upgrade servers
---------------------------------------------------------
EC200A-EUR11eL-EC200A-EU | Using modem LTE interfaceUsing any RouterOS interface(7.18beta1+)
EG06-A | Using any RouterOS interface
EP06-A | Using any RouterOS interface
EG12-EA | Using any RouterOS interface
EG18-EA | Using any RouterOS interface
FG621-EAR11eL-FG621-EA | Using any RouterOS interface
R11-LTE | Using modem LTE interface
R11e-4G | Using any RouterOS interface
R11e-LTE6 | Using any RouterOS interface
RG502Q-EA | Using any RouterOS interface
RG520F-EU | Using any RouterOS interface
EC200A-EU
R11eL-EC200A-EU
EG06-A
EP06-A
EG12-EA
Using any RouterOS interface
EG18-EA
Using any RouterOS interface
FG621-EA
R11eL-FG621-EA
R11e-LTE6
RG502Q-EA
Using any RouterOS interface
RG520F-EU
Using any RouterOS interface
#### Modem firmware-upgrade commandexamples:
Check for new firmware update availability
```
[admin@D53G] > /interface lte firmware-upgrade lte1                        
  installed: EG12EAPAR01A13M4G_02.001.02.001
     latest: EG12EAPAR01A15M4G_01.201.01.201
```
Check for new firmware update availability in early access/testing channel
```
[admin@D53G] > /interface lte firmware-upgrade lte1 update-channel=testing
  installed: EG12EAPAR01A15M4G_01.201.01.201
     latest: EG12EAPAR01A15M4G_01.203.01.203
```
Install latest firmware
```
[admin@D53G] > /interface lte firmware-upgrade lte1 upgrade=yes
```
Install latest firmware from early access/testing channel
```
[admin@D53G] > /interface lte firmware-upgrade lte1 upgrade=yes update-channel=testing
```
### User at-chat command
It is possible to send user defined "at-chat" command to the LTE interface with/interface lte at-chatcommand.
```
/interface lte at-chat
```
```
[admin@MikroTik] > /interface lte at-chat lte1 input="AT"
  output: OK
```
It is also possible to use the "wait" parameterwait=yeswith the command to make "at-chat" wait for 5 seconds and return all the output instead of returning only the first received data, this is useful for some commands that return multiline output or a large block of data.
```
[admin@MikroTik] > interface lte at-chat lte1 input="at+qcfg=?"
  output: 
[admin@MikroTik] > interface lte at-chat lte1 input="at+qcfg=?" wait=yes
  output: +QCFG: "rrc",(0-5)
          +QCFG: "hsdpacat",(6,8,10-24)
          +QCFG: "hsupacat",(5,6)
          +QCFG: "pdp/duplicatechk",(0,1)
          +QCFG: "risignaltype",("respective","physical")
          +QCFG: "lte/bandprior",(1-43),(1-43),(1-43)
          +QCFG: "volte_disable",(0,1)
          +QCFG: "diversity/config",(4,6),(1-4),(0)
          +QCFG: "div_test_mode",(0,1)
          +QCFG: "usbspeed",("20","30")
          +QCFG: "data_interface",(0,1),(0,1)
          +QCFG: "pcie/mode",(0,1)
          +QCFG: "pcie_mbim",(0,1)
          +QCFG: "sms_control",(0,1),(0,1)
          +QCFG: "call_control",(0,1),(0,1)
          +QCFG: "usb/maxpower",(0-900)
          +QCFG: "efratctl",(0,1)
          +QCFG: "netmaskset",(0,1)[,<netmask>]
          +QCFG: "mmwave",ant_chip,ant_type
          +QCFG: "gatewayset",(0,1)[,<gateway>]
          +QCFG: "clat",(0,1),(0,1),<prefix>,(0,32,40,48,56,64,96),<fqdn>,(0,1),(0,1,2,4,8),(0,1),(0,1),(0,1,2),(0,1,2)
          +QCFG: "usage/apmem"
          +QCFG: "enable_gea1"[,(0,1)]
          +QCFG: "dhcppktfltr",(0,1)
          OK
```
You can also use "at-chat" function in scripts and assign command output to variable.
```
[admin@MikroTik] > :global "lte_command" [/interface lte at-chat lte1 input="AT+CEREG?" as-value ] 
[admin@MikroTik] > :put $"lte_command" 
output=+CEREG: 0,1
OK
```
## Quick setup example
Start with network settings - Add new connection parameters under LTE apn profile (provided by network provider):
```
/interface lte apn add name=profile1 apn=phoneprovider.net authentication=chap password=web user=web
```
Select the newly created profile for an LTE connection:
```
/interface lte set [find] apn-profiles=profile1
```
LTE interface should appear with the running (R) flag:
```
[admin@MikroTik] > /interface lte print
Flags: X - disabled, R - running 
0 R name="lte1" mtu=1500 mac-address=AA:AA:AA:AA:AA:AA
```
If required, add NAT Masquerade for LTE Interface to get internet to the local network:
```
/ip firewall nat add action=masquerade chain=srcnat out-interface=lte1
```
After the interface is added, you can use the "info" command to see what parameters the client acquired (parameters returned depends on the LTE hardware device):
```
[admin@MikroTik] > interface/lte/monitor lte1                                                                                                            
            status: connected
             model: EG18-EA
          revision: EG18EAPAR01A12M4G
  current-operator: LMT
    current-cellid: 3103242
            enb-id: 12122
         sector-id: 10
        phy-cellid: 480
        data-class: LTE
    session-uptime: 15m54s
              imei: 86981604098XXXX
              imsi: 24701060267XXXX
              uicc: 8937101122102057XXXX
      primary-band: B3@20Mhz earfcn: 1300 phy-cellid: 480
     dl-modulation: qpsk
               cqi: 7
                ri: 2
               mcs: 1
              rssi: -68dBm
              rsrp: -97dBm
              rsrq: -9dB
              sinr: 6dB
```
## Passthrough Example
Some LTE interfaces support the LTE Passthrough feature where the IP configuration is applied directly to the client device. In this case, modem firmware is responsible for the IP configuration, and the router is used only to configure modem settings - APN, Network Technologies, and IP-Type. In this configuration, the router will not get IP configuration from the modem. The LTE Passthrough modem can pass both IPv4 and IPv6 addresses if that is supported by the modem. Some modems support multiple APNs where you can pass the traffic from each APN to a specific router interface.
Passthrough will only work for one host. The router will automatically detect the MAC address of the first received packet and use it for the Passthrough. If there are multiple hosts on the network it is possible to lock the Passthrough to a specific MAC. On the host on the network where the Passthrough is providing the IP a DHCP-Client should be enabled on that interface too. Note, that it will not be possible to connect to the LTE router via a public lte IP address or from the host which is used by the passthrough. It is suggested to create an additional connection from the LTE router to the host for configuration purposes. For example vlan interface between the LTE router and host.
To enable the Passthrough a new entry is required or the default entry should be changed in the '/interface lte apn' menu
```
/interface lte apn
```
Examples.
To configure the Passthrough on ether1:
```
[admin@MikroTik] > /interface lte apn add apn=apn1 passthrough-interface=ether1
[admin@MikroTik] > /interface lte set lte1 apn-profiles=apn1
```
To configure the Passthrough on ether1 host 00:0C:42:03:06:AB:
```
[admin@MikroTik] > /interface lte apn add apn=apn1 passthrough-interface=ether1 passthrough-mac=00:0C:42:03:06:AB
[admin@MikroTik] > /interface lte set lte1 apn-profiles=apn1
```
To configure multiple APNs on ether1 and ether2:
```
[admin@MikroTik] > /interface lte apn add apn=apn1 passthrough-interface=ether1
[admin@MikroTik] > /interface lte apn add apn=apn2 passthrough-interface=ether2
[admin@MikroTik] > /interface lte set lte1 apn-profiles=apn1,apn2
```
To configure multiple APNs with the same APN for different interfaces:
```
[admin@MikroTik] > /interface lte apn add name=interface1 apn=apn1
[admin@MikroTik] > /interface lte apn add name=interface2 apn=apn1 passthrough-interface=ether1
[admin@MikroTik] > /interface lte set lte1 apn-profiles=interface1
[admin@MikroTik] > /interface lte set lte2 apn-profiles=interface2
```
## Dual SIM
### Boards with switchable SIM slots
RouterBoard | Modem slot | SIM slots | Switchable
-------------------------------------------------
LtAP | lower | 2 | 3 | Y
upper | 1 | N
LtAP mini |  | up | down | Y
SXT R |  | a |  b | Y
SIM slots switching commands
* RouterOS v7
```
/interface lte settings set sim-slot=down
```
* RouterOS v6 after 6.45.1
```
/system routerboard modem set sim-slot=down
```
* RouterOS v6 pre 6.45.1:
```
/system routerboard sim set sim-slot=down
```
For more reference please see the board block diagram,  Quick Guide, and User manual.
### Usage Example
Follow this link -Dual SIM Application, to see examples of how to change SIM slot based on roaming status and in case the interface status is down, with the help of RouterOS scripts and scheduler.
## Tips and Tricks
This paragraph contains information for additional features and usage cases.
### Find device location using Cell information
On devices using the R11e-LTE International version card (wAP LTE kit) some extra information is provided under info command.
```
current-operator: 24701
                lac: 40
     current-cellid: 2514442
```
Property | Description
----------------------
current-operator(integer; Default: ) | Contains MCC and MNC. For example: current-operator: 24701 breaks to: MCC=247 MNC=01
lac(integer; Default: ) | location area code (LAC)
current-cellid(integer; Default: ) | Station identification number
Values can be used to find location in databases:Cell Id Finder
### Using Cell lock
It is possible to lock R11e-LTE, R11e-LTE6 and R11e-4G modems and equipped devices to the exact LTE tower. LTE info command provides currently used cellular tower information:
```
phy-cellid: 384
             earfcn: 1300 (band 3, bandwidth 20Mhz)
```
Property | Description
----------------------
phy-cellid(integer; Default: ) | Physical Cell Identification (PCI) of currently used cell tower.
earfcn(integer; Default: ) | Absolute Radio Frequency Channel Number
Exact tower location as well as available bands and other information can be acquired from mobile carrier or by using online services:
CellMapper
By using those acquired variables it's possible to send the AT command to modem for locking to tower in the current format:
for R11e-LTE and R11e-LTE6
```
AT*Cell=<mode>,<NetworkMode>,<band>,<EARFCN>,<PCI>
where
<mode> :
0 – Cell/Frequency disabled
1 – Frequency lock enabled
2 – Cell lock enabled
<NetworkMode>
0 – GSM
1 – UMTS_TD
2 – UMTS_WB
3 – LTE
<band>
Not in use, leave this blank
<EARFCN>
earfcn from lte info
<PCI>
phy-cellid from lte info
```
To lock modem at previously used tower at-chat can be used:
```
/interface lte at-chat lte1 input="AT*Cell=2,3,,1300,384"
```
For R11e-LTE all set on locks are lost after reboot or modem reset. Cell data can be also gathered from "cell-monitor".
For R11e-LTE6 cell lock works only for the primary band, this can be useful if you have multiple channels on the same band and you want to lock it to a specific earfcn. Note, that cell lock is not band-specific and for ca-band it can also use other frequency bands, unless you use band lock.
Use cell lock to set the primary band to the 1300 earfcn and use the second channel for the ca-band:
```
/interface lte at-chat lte1 input="AT*Cell=2,3,,1300,138"
```
Now it uses the earfcn: 1300 for the primary channel:
```
primary-band: B3@20Mhz earfcn: 1300 phy-cellid: 138
              ca-band: B3@5Mhz earfcn: 1417 phy-cellid: 138
```
You can also set it the other way around:
```
/interface lte at-chat lte1 input="AT*Cell=2,3,,1417,138"
```
Now it uses the earfcn: 1417 for the primary channel:
```
primary-band: B3@5Mhz earfcn: 1417 phy-cellid: 138
              ca-band: B3@20Mhz earfcn: 1300 phy-cellid: 138
```
For R11e-LTE6 modem cell lock information will not be lost after reboot or modem reset. To remove cell lock use at-chat command:
```
/interface lte at-chat lte1 input="AT*Cell=0"
```
for R11e-4G
```
AT%CLCMD=<mode>,<mode2>,<EARFCN>,<PCI>,<PLMN>
AT%CLCMD=1,1,3250,244,\"24705\"
where
<mode> :
0 – Cell/Frequency disabled
1 – Cell lock enabled
<mode2> :
0 - Save lock for first scan
1 - Always use lock 
(after each reset modem will clear out previous settings no matter what is used here)
<EARFCN>
earfcn from lte info
<PCI>
phy-cellid from lte info
<PLMN>
Mobile operator code
```
All PLMN codes availableherethis variable can be also left blank
To lock the modem to the cell - modem needs to be in non operating state, the easiest way forR11e-4Gmodem is to add CellLock line to "modem-init" string:
```
/interface lte set lte1 modem-init="AT%CLCMD=1,1,3250,244,\"24705\""
```
Multiple cells can also be added by providing a list instead of one tower information in the following format:
```
AT%CLCMD=<mode>,<mode2>,<EARFCN_1>,<PCI_1>,<PLMN_1>,<EARFCN_2>,<PCI_2>,<PLMN_2>
```
For example to lock to two different PCIs within the same band and operator:
```
/interface lte set lte1 modem-init="AT%CLCMD=1,1,6300,384,\"24701\",6300,385,\"24701\""
```
for Chateau LTE12, Chateau LTE18, Chateau 5G, LHG LTE18 and ATL LTE18
```
AT+QNWLOCK="common/4g",<num of cells>,[[<freq>,<pci>],...]
AT+QNWLOCK=\"common/4g\",1,6300,384
where
<num of cells>
number of cells to cell lock
<freq>
earfcn from lte info
<pci>
phy-cellid from lte info
```
Single-cell lock example:
```
/interface lte at-chat lte1 input="AT+QNWLOCK=\"common/4g\",1,3050,448"
```
Query current configuration:
```
/interface lte at-chat lte1 input="AT+QNWLOCK=\"common/4g\""
```
Multiple cells can also be added to the cell lock. For example to lock to two different cells:
```
/interface lte at-chat lte1 input="AT+QNWLOCK=\"common/4g\",2,3050,448,1574,474"
```
To remove the cell lock use this at-chat command:
```
/interface lte at-chat lte1 input="at+qnwlock=\"common/4g\",0"
```
for FG621-EA
```
AT+GTCELLLOCK=<mode>[,<rat>,<type>,<earfcn>[,<PCI>]]where< mode >: integer type; 0 Disable this function 1 Enable this function 2 Add new cell to be locked<rat>: integer type; 0 LTE 1 WCDMA<type>: integer type; 0 Lock PCI 1 Lock frequency<earfcn>: integer type; the range is 0-65535.<PCI>: integer type; If second parameter value is 0, the range is 0-503 for LTE If second parameter value is 1, the rang is 0-512 for WCDMA
```
Example:
```
/interface lte at-chat lte1 input="AT+GTCELLLOCK=1,0,0,6175,176"
```
### Cell Monitor
Cell monitor allows to scan available nearby mobile network cells:
```
[admin@MikroTik] > /interface lte cell-monitor lte1 
PHY-CELLID BAND         PSC EARFCN                 RSRP          RSRQ          RSSI         SINR
        49 B20              6300                -110dBm       -19.5dB
       272 B20              6300                -116dBm       -19.5dB
       374 B20              6300                -108dBm         -16dB
       384 B1               150                 -105dBm       -13.5dB
       384 B3               1300                -106dBm         -12dB
       384 B7               2850                -107dBm       -11.5dB
       432 B7               2850                -119dBm       -19.5dB
```
Gathered data can be used for more precise location detection or for Cell lock.
## Troubleshooting
Enable LTE logging:
```
[admin@MikroTik] > /system logging add topics=lte
```
Check for errors in log:
```
[admin@MikroTik] > /log print
11:08:59 lte,async lte1: sent AT+CPIN? 
11:08:59 lte,async lte1: rcvd +CME ERROR: 10
```
search for CME error description online,
in this case: CME error 10 - SIM not inserted
### Locking band on Huawei and other modems
To lock band for Huawei modems/interface lte set lte1 band=""option can't be used.
```
/interface lte set lte1 band=""
```
It is possible to use AT commands to lock to the desired band manually.
To check all supported bands run the at-chat command:
```
[admin@MikroTik] /interface lte at-chat lte1 input="AT^SYSCFGEX=\?"
output: ^SYSCFGEX: ("00","03","02","01","99"),((2000004e80380,"GSM850/GSM900/GSM1800/GSM1900/WCDMA BCI/WCDMA BCII/WCDMA BCV/WCDMA BCVIII"),
(3fffffff,"All Bands")),(0-2),(0-4),((800d7,"LTE BC1/LTE BC2/LTE 
BC3/LTE BC5/LTE BC7/LTE BC8/LTE BC20"),(7fffffffffffffff,"All Bands")) 
OK
```
Example to lock to LTE band 7:
```
[admin@MikroTik] /interface lte set lte1 modem-init="AT^SYSCFGEX=\"03\",3FFFFFFF,2,4,40,,"
```
Change last part40to desired band specified hexadecimal value where:
```
4 LTE BC3
40 LTE BC7
80000 LTE BC20
7FFFFFFFFFFFFFFF  All bands
etc
```
All band HEX values and AT commands can be found inHuawei AT Command Interface Specification guide
Check if the band is locked:
```
[admin@MikroTik] /interface lte at-chat lte1 input="AT^SYSCFGEX\?"
output: ^SYSCFGEX: "03",3FFFFFFF,0,2,40
OK
```
For more information check modem manufacturers AT command reference manuals.
### mPCIe modems with RB9xx series devices
In case your modem is not being recognized after a soft reboot, then you might need to add a delay before the USB port is initialized. This can be done using the following command:
```
/system routerboard settings set init-delay=5s
```
### Boards with USB-A port and mPCIe
Some devices such as specific RB9xx's and the RBLtAP-2HnD share the same USB lines between a single mPCIe slot and a USB-A port. If auto switch is not taking place and a modem is not getting detected, you might need to switch manually to either use the USB-A or mini-PCIe:
```
/system routerboard usb set type=mini-PCIe
```
### Avoiding tethering speed throttling
Some operators (TMobile, YOTA etc.) allow unlimited data only for the device the SIM card is used on, all other data coming from mobile hotspots or tethering is highly limited by volume or by throughput speed.Some sourceshave found out that this limitation is done by monitoring TTL (Time To Live) values from packets to determine if limitations need to be applied (TTL is decreased by 1 for each "hop" made). RouterOS allows changing the TTL parameter for packets going from the router to allow hiding sub networks. Keep in mind that this may conflict with fair use policy.
```
IPv4 mangle rule:
/ip firewall mangle
add action=change-ttl chain=postrouting new-ttl=set:65 out-interface=lte1 passthrough=yes
IPv6 mangle rule:
/ipv6 firewall mangle 
add action=change-hop-limit chain=postrouting new-hop-limit=set:65 passthrough=yes
```
More information:YOTA,TMobile
### Unlocking SIM card after multiple wrong PIN code attempts
After locking the SIM card, unlock can be done through "at-chat"
Check current PIN code status:
```
/interface lte at-chat lte1 input="at+cpin\?"
```
If card is locked - unlock it by providing:
```
/interface lte at-chat lte1 input="AT+CPIN=\"PUK_code\",\"NEW_PIN\""
```
Replace PUK_code and NEW_PIN with matching values.