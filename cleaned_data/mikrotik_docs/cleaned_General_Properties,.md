# Document Information
Title: General Properties
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/16351619/General+Properties,

# Content
Every RouterBOARD with a miniPCI-e slot which supports LTE modems can also be used as a LoRaWAN gateway by installingR11e-LoRa8orR11e-LoRa9card. Both UDP and LNS (starting withv7.12rc1testing version) protocols are supported.
In order to work with Lora, IoT package should be installed. You can find the package for your device architecture in extra packages archive on thedownloadpage.
# Properties
This menu is used to apply settings to the LoRa interface.
Sub-menu:/iot lora
```
/iot lora
```
Property | Description
----------------------
antenna-gain(integer [-128..127]; Default:0) | Antenna gain in dBi. This value should be equal tosetup-antenna-gainminuscable-loss. Using 6.5 dBi antenna, 6.5 is the value to be configured (not taking into account cable loss).Output power of the gateway is dictated by the server.The gateway will calculate its actual output power by subtractingantenna-gainsetting fromserver_value(value received in the downlink message).
channel-plan(as-923 | au-915 | custom | eu-868 | in-865 | kr-920 | ru-864 | ru-864-mid | us-915-1 | us-915-2; Default:eu-868) | Frequency plans for various regions.
disabled(yes | no; Default:yes) | Whether LoRaWAN gateway is disabled.
forward(ccrc-validtaion | dev-addr-validtaion | proprietary-traffic; Default:crc-validtaion) | Defines what kind of packets should be forwarded to Network server:crc-validtaion - Forward valid packets with correct CRC.dev-addr-validtaion - Checks if DevAddr of the packet corresponds to the NetID and if not, drops the packet. The following sequence happens: 1) Dev. Addr value gets "obtained" from the received LoRa packet; 2) Dev. Addr is "compared" against"valid" Net IDslist; 3) If there is no Net ID for the Dev. Addr, the packet is not forwarded; 4) If Net ID is valid, Dev. Addr range is valid, the packet is forwarded.proprietary-traffic - Checks the content of the LoRa packet and if the "type" of the frame is "proprietary", the packet is not forwarded.
gateway-id(string) | Gateway ID or Gateway EUI, is used when registering the gateway with the server.
lbt-enabled(yes | no; Default:no) | Whether gateway should use LBT (Listen Before Talk) protocol.
listen-time(integer [0us..4294967295us]; Default:5000us) | Time in microseconds to track RSSI before TX (used whenlbt-enabled=yes).
name(string; Default: ) | Name of LoRaWAN gateway.
network(private | public; Default:public) | Whether sync word should (network=private) or should not (network=public) be used.
rssi-threshold(integer [-32,768 .. 32,767]; Default:-65dB) | RSSI value to determine whether forwarder may use specific channel to talk. If RSSI value is belowrssi-threshold, channel could be used (used whenlbt-enabled=yes).
servers(list of string; Default: ) | Name of the server from the/iot lora serverssection.
src-address(IP; Default: ) | Specifies uplink packet source address if necessary (address should match an address configured on the RB).
spoof-gps(string; Default: ) | Set custom GPS location:Latitude [-90..90]Longitude [-180..180]Altitude(m) [-2147483648..2147483647]
Antenna gain in dBi. This value should be equal tosetup-antenna-gainminuscable-loss. Using 6.5 dBi antenna, 6.5 is the value to be configured (not taking into account cable loss).
```
setup-antenna-gain
```
```
cable-loss
```
Output power of the gateway is dictated by the server.The gateway will calculate its actual output power by subtractingantenna-gainsetting fromserver_value(value received in the downlink message).
```
antenna-gain
```
```
server_value
```
```
/iot lora servers
```
Set custom GPS location:
# Channels
This section is used to alter channel/frequency related settings.
Sub-menu:/iot lora channels
```
/iot lora channels
```
Property | Description
----------------------
bandwidth(7.8_kHz | 15.6_kHz | 31.2_kHz | 62.5_kHz | 125_kHz | 250_kHz | 500_kHz; Default:125_kHz) | Bandwidth of specific channel, predefined when any of channel-plan preset is used, but could be manually changed when channel-plan is set to custom.
disabled(yes | no; Default:no) | Disable or enable the channel.
freq-off(integer[-400000..400000]; Default:) | Channel frequency offset against radio central frequency, it makes possible to adjust channel frequencies so that channels does not overlap.
radio(radio0 | radio1; Default: ) | Defines which radio uses selected channel.
spread-factor(SF7 | SF8 | SF9 | SF10 | SF11 | SF12; Default: ) | Defines the Spread Factor for a channel with type=LoRa. Lower Spread Factor means higher data rate.
To view current channels, issue the command/iot lora cannels print:
```
/iot lora cannels print
```
```
/iot lora channels print
Columns: NAME, TYPE, RADIO, FREQ-OFF, BANDWIDTH, FREQ, SPREAD-FACTOR, DATARATE
# NAME       TYPE  RADIO   FREQ-OFF  BANDWIDTH  FREQ   SPREAD-FACTOR  DATARATE
0 gateway-0  MSF   radio1  -400000   125_kHz    868.1
1 gateway-0  MSF   radio1  -200000   125_kHz    868.3
2 gateway-0  MSF   radio1  0         125_kHz    868.5
3 gateway-0  MSF   radio0  -400000   125_kHz    867.1
4 gateway-0  MSF   radio0  -200000   125_kHz    867.3
5 gateway-0  MSF   radio0  0         125_kHz    867.5
6 gateway-0  MSF   radio0  200000    125_kHz    867.7
7 gateway-0  MSF   radio0  400000    125_kHz    867.9
8 gateway-0  LoRa  radio1  -200000   250_kHz    868.3  SF7
9 gateway-0  FSK   radio1  300000    125_kHz    868.8                    50000
```
Channels are created usingfreq-offand radio'scenter-freqfrequencies. To viewradioscenter frequencies use the command/iot lora radios print.
```
freq-off
```
```
center-freq
```
```
/iot lora radios print
```
To understand how each channel's frequency is calculated, check the example below:
```
# NAME       TYPE  RADIO   FREQ-OFF  BANDWIDTH  FREQ   SPREAD-FACTOR  DATARATE
0 gateway-0  MSF   radio1  -400000   125_kHz    868.1
```
radio1is selected to be used for channel # 0 and it is configured withcenter-freq=868500000(868500000 Hz or 868.5 MHz).
```
radio1
```
```
center-freq=868500000
```
By using frequency offset,freq-off=-400000(-400000 Hz or -0.4 MHz), we define channel # 0 to be868500000-400000=868100000Hz or 868.1 MHz.
```
freq-off=-400000
```
```
868500000-400000=868100000
```
# Join EUI
The gateway will forward to the server every single LoRaWAN payload it receives. That includes neighboring LoRaWAN node's payloads as well. It might not be ideal to forward everything, as, for example, it can increase the data amount used (and directly impact ISP plan cost).
The Join EUI menu allows you to specify a range of Join EUI's that the gateway will forward. After adding the range, make sure to apply it to theserversettings.
If the Join EUI of the packet does not match the configuration, the packet is not forwarded to the server.
You can find the Join EUI used by your node with the help of RouterOS GUI. Go to the "LoRa" section and to the "Traffic" sub-menu (which is only available using the graphical interface). After you power your LoRaWAN node, the node should send a "Join-request" packet. Double-click on it to inspect it:
Sub-menu:/iot lora joineui
```
/iot lora joineui
```
Property | Description
----------------------
joineui(string; Default: ) | Define a range of Join EUI's.
logging(yes | no; Default: no) | Enables additional logging for the filter feature.
name(string; Default: ) | Define the name for the range.
Define a range of Join EUI's.
Enables additional logging for the filter feature.
An example of Join EUI would look like thisE0 E1 E2 01 02 03 04 05. It consists of 8 octets in HEX format.
To add a range that allowsevery possibleJoin EUI, add a filter like this:
```
/iot lora joineui add name=ALL joineuis=0000000000000000-ffffffffffffffff
```
To add a range that allows "nothing" (basically "restrict" all Join EUI's), add a filter like this:
```
/iot lora joineui add name=NONE joineuis=0000000000000000-0000000000000000
```
For a specific single Join EUI, add a filter like this:
```
/iot lora joineui add name=SINGLE joineuis=E0E1E20102030405-E0E1E20102030405
```
# Network ID
The gateway will forward to the server every single LoRaWAN payload it receives. That includes neighboring LoRaWAN node's payloads as well. It might not be ideal to forward everything, as, for example, it can increase the data amount used (and directly impact ISP plan cost).
The NetID menu allows you to specify a list of NetIDs that the gateway will forward. After adding the list, make sure to apply it to theserversettings.
If the NetID (DevAddr range) of the packet does not match the configuration, the packet is not forwarded to the server.
NetIDs define the ranges of Device Addresses (DevAddr) that were assigned to different operators/servers by the LoRaWAN Alliance. A list with most ranges can be found in theTTN guide.
DevAddr is assigned to the LoRaWAN node by the LoRaWAN server after the communication with the server takes place. For example,TTNwill assign your node an address from within the range 26000000 - 27FFFFFF. You can find it under the LoRaWAN server dashboard or using RouterOS GUI, under the "Traffic" sub-menu (after "join-request" and "join-accept" communication takes place) in the Dev Addr column/field.
Let's say TTN assigned26 1B D8 D1Dev Addr to your node. Based on theTTN guide, it falls under the 26000000 - 27FFFFFF DevAddr range and it belongs to the000013 NetID.
Sub-menu:/iot lora netid
```
/iot lora netid
```
Property | Description
----------------------
netids(string; Default: ) | Define the NetIDs
logging(yes | no; Default: no) | Enables additional logging for the filter feature.
name(string; Default: ) | Define the name for the ID.
Define the NetIDs
Enables additional logging for the filter feature.
To add a filter for a specific NetId, use the command (you can add more than one using a "comma" separator):
```
/iot lora netids add name=TTN netids=000013
```
# Servers
This section is used to add new or alter current server settings.
Sub-menu:/iot lora servers
```
/iot lora servers
```
There are a few predefined servers that can be used (it requires to make anThe Things Networkaccount to use them):
```
[admin@MikroTik] /iot/lora/servers/print
Columns: NAME, UP-PORT, DOWN-PORT, ADDRESS
# NAME              UP-PORT  DOWN-PORT  ADDRESS
0  TTS Cloud (eu1)      1700       1700  eu1.cloud.thethings.industries
1  TTS Cloud (nam1)     1700       1700  nam1.cloud.thethings.industries
2  TTS Cloud (au1)      1700       1700  au1.cloud.thethings.industries
3  TTN V3 (eu1)         1700       1700  eu1.cloud.thethings.network
4  TTN V3 (nam1)        1700       1700  nam1.cloud.thethings.network
5  TTN V3 (au1)         1700       1700  au1.cloud.thethings.network
```
Custom servers can be added as well. Data forwarding to multiple servers can work simultaneously if the first server does not change "DevAdress" part of the packet and under the condition that all servers are able to decode the packet.
Property | Description
----------------------
address(domain name or IP address; Default: ) | Defines LoRaWAN Network server address.
name(string; Default: ) | Defines server name.
protocol(UDP | LNS | CUPS; Default:UDP) | Specify whether to use UDP, LNS or CUPS protocol for the communication with the LoRaWAN server.
down-port(integer [0..65535]; Default:1700) | Parameter that is used when UDP protocol is selected. Defines port for down-link communication (from server to node) with LoRaWAN Network server. Most of known open source servers uses port 1700 as default, but it can change if multiple servers are configured on the same machine.
up-port(integer [0..65535]; Default:1700) | Parameter that is used when UDP protocol is selected. Defines port for up-link communication (from node to server) with LoRaWAN Network server. Most of known open source servers uses port 1700 as default, but it can change if multiple servers are configured on the same machine.
netid(list of string; Default: ) | Parameter that is used when UDP protocol is selected. Applies a filter to only send LoRaWAN payloads that match the Network ID (Net ID) filter configured.
joineui(list of string; Default: ) | Parameter that is used when UDP protocol is selected. Applies a filter to only send LoRaWAN payloads that match the Join EUI filter configured.
port(integer [0..65535]; Default:8887) | Parameter that is used when LNS or CUPS protocol is selected. For LNS, defines the WSS (WebSocket) port and, for CUPS, defines HTTPS port.
key(string; Default: ) | Parameter that is used when LNS or CUPS protocol is selected. Specify the LoRa Basics Station LNS Authentication Key or CUPS API KEY (both generated on the server).
ssl(yes or no; Default: no) | Parameter that is used when LNS or CUPS protocol is selected. Specify whether to use or not to use SSL (if the server supports TLS server authentication). When this option is choosen, root SSL certificate(s) must be uploaded under thecertificatesmenu.
certificate(list of string; Default:none) | Parameter that is used when LNS or CUPS protocol is selected. Select an uploaded client certificate (if the server awaits TLS client authentication). If TLS client authentication is not required by the server, use the default "none" setting.
interval(integer [0..65535]; Default: ) | Parameter that is used when CUPS protocol is selected. Specify the interval with which the LoRa Basics Station will query CUPS server for configuration updates/changes.
down-port(integer [0..65535]; Default:1700)
There are a few pre-configued The Things default servers. If you deleted one and want to recover default servers, you can use the command:
```
/iot lora server reset-servers
```
# Traffic
This section displays LoRa payloads that were broadcasted by the surrounding nodes.
Sub-menu:/iot lora traffic
```
/iot lora traffic
```
To view the list, use theprintcommand:
```
print
```
```
[admin@MikroTik] /iot/lora/traffic/print
Columns: TIME, GWID, MSGTYPE, DEVADDR, MVER, FCNT, CRC, TYPE, JOINEUI, DEVEUI
# TIME                             GWID  MSGTYPE                DEVADDR      MVER         FCNT  CRC    TY  JOINEUI                  DEVEUI
0  2024-11-08 13:33:28  xxxxxxxxxxxxxxxx  Unconfirmed Data Up    6C B9 XX XX  LoRaWAN R1  59434  Error  Rx
1  2024-11-08 13:33:50  xxxxxxxxxxxxxxxx  Rejoin-request                      LoRaWAN R1         Error  Rx                           50 62 9F FE XX XX XX XX
2  2024-11-08 13:34:09  xxxxxxxxxxxxxxxx  Unconfirmed Data Down  5E 00 XX XX  RFU         41736  Error  Rx
3  2024-11-08 13:34:15  xxxxxxxxxxxxxxxx  Rejoin-request                      RFU                Error  Rx                           D9 C2 BD 4B XX XX XX XX
4  2024-11-08 13:34:55  xxxxxxxxxxxxxxxx  Join-request                        LoRaWAN R1         Error  Rx  A1 AE B1 8A XX XX XX XX  F4 62 81 BE XX XX XX XX
```
To clear the list (to remove all entries), issue theclearcommand:
```
clear
```
```
[admin@MikroTik] /iot/lora/traffic/clear
```
Traffic tab displays "LoRa" payloads. As soon as the LoRa interface is enabled with the/iot lora enable [find]command, all the payloads from the list will be converted into TCP/UDP packets (depending on whether you use UDP 1700 or LNS/CUPS protocol) and forwarded to the configured server.
```
/iot lora enable [find]
```
If you do not wish to use LoRaWAN topology, and if you wish to forward "raw" LoRa payloads to your own server, you have an option to do so, usingMQTTorFetchpost (HTTP post). To do that, remove the LoRa server configuration (so that no server is selected by the LoRa interface, thus the payloads are not forwarded anywhere) and then you will have to create ascript. The script will have to store the traffic as variables, structure MQTT/HTTP messages out of them (in a format that your server expects to receive the data) and then send it. After that, you can apply ascheduler, to run the script with an interval of your choice to constantly send the data.
A basic example (first step in the script) on how to convert traffic payloads into a varible called "traffic":
```
[admin@MikroTik] > :global traffic;:set traffic [/iot lora traffic print as-value ];put $traffic
.id=*4f;band=125 kHz;coderate=?/?;counter=890652548;crc=Error;datarate=SF 7;freqhz=868300;gwid=50313xxxxxx;ifcha
in=1;mod=LoRa;msgtype=Proprietary;mver=RFU;rfchain=1;rssi=-116.00;rxcrc=3809;size=213;snr=-12.00;snrmax=-8.25;snrmin=
-14.25;time=2024-11-08 14:39:45;type=Rx
```
# Debugging
If you have issues with the connection, make sure to enable logs:
```
/system/logging/add topics=debug,lora
```
This will enable debug logging and help you pin point where the potential issue could be. Logs can be viewed using:
```
/log/print
```
A successful connection would look like this:
```
13:50:33 lora,info gateway-0 forwarder started
13:50:38 lora,info [LNS] connecting to wss://eu1.cloud.thethings.network:8887/router-info
13:50:39 lora,info [LNS] eu1.cloud.thethings.network discovered
13:50:39 lora,info [LNS] eu1.cloud.thethings.network disconnected
13:50:39 lora,info [LNS] connecting to wss://eu1.cloud.thethings.network:8887/traffic/eui-xxxx
13:50:39 lora,info [LNS] eu1.cloud.thethings.network configured
13:50:52 lora,info gateway-0 forwarder is ready
```
More logging information can be found in ourLogguide.