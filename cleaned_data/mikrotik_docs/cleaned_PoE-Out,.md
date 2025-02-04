# Document Information
Title: PoE-Out
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/19136769/PoE-Out,

# Content
# Summary
This page explains using the PoE-Out (Power over Ethernet) feature available on MikroTik devices equipped with at least one PoE-Out interface. MikroTik devices utilize an RJ45 mode B pinout for power delivery, with PoE supplied through pins 4 and 5 (+) and pins 7 and 8 (-).
# MikroTik supported PoE-Out standards
MikroTik devices can support some or all of the following PoE standards:
IEEE Standards 802.3af/at- Also known as PoE+ Type 1 (af) and PoE+ Type 2 (at), these IEEE standards aim to ensure compatibility between vendors. MikroTik PSEs that support these standards can power both Type 1 and Type 2 PDs. MikroTik devices that support af/at standard can also power devices that accept Passive PoE-In. (e.g.CRS112-8P-4S-IN,CRS328-24P-4S+RM,CRS354-48P-4S+2Q+RM.)
Each PoE-Out implementation supports overload and short-circuit detection.
# How to choose your PoE PSE
This table can help you choose which PSE device is best suitable for your needs.
Device name | PoE-Out port count | Passive PoE | 802.3af/at | 802.3bt | Power input | Maximum output per port | Maximum power output, W | Input 18-30V, mA | Input 30-57V, mA
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CSS610-8P-2S+IN | 8 | + | + | - | AC &DC 48-57 V | 1000 | 625 | 140
CRS328-24P-4S+RM | 24 | + | + | - | AC | 1000 | 450 | 450
CRS354-48P-4S+2Q+RM | 48 | + | + | - | AC | 1000 | 570 | 700
CRS112-8P-4S-IN | 8 | + | + | - | DC 18-30V & DC 30-57V | 1000 | 450 | 150
netPower 16P | 16 | + | + | - | DC 18-30V & DC 30-57V | 1100 | 600 | 160
RB5009UPr+S+ | 8 | + | + | - | DC 18-30V or DC 30-57V | 900 | 440 | 130
hEX PoE | 4 | + | + | - | DC 18-30V or DC 30-57V | 1000 | 450 | 102
PowerBox Pro | 4 | + | + | - | DC 18-30V or DC 30-57V | 1000 | 450 | 102
OmniTIK 5 PoE ac | 4 | + | + | - | DC 18-30V or DC 30-57V | 1000 | 450 | 102
hEX PoE lite | 4 | + | - | - | DC 18-30V | 1000 | - | 60
PowerBox | 4 | + | - | - | DC 18-30V | 1000 | 60
RB260GSP | 4 | + | - | - | DC 18-30V | 1000 | 60
OmniTIK 5 PoE | 4 | + | - | - | DC 18-30V | 1000 | 60
CRS320-8P-8B-4S+RM | 16 | + | + | + | AC | - | 560 (af/at) / 1667 (bt) | 963
Device name
PoE-Out port count
Passive PoE
802.3af/at
802.3bt
Power input
Maximum power output, W
Input 18-30V, mA
CSS610-8P-2S+IN
AC &DC 48-57 V
CRS328-24P-4S+RM
CRS354-48P-4S+2Q+RM
CRS112-8P-4S-IN
netPower 16P
RB5009UPr+S+
hEX PoE
PowerBox Pro
OmniTIK 5 PoE ac
hEX PoE lite
-
PowerBox
RB260GSP
OmniTIK 5 PoE
60
560 (af/at) / 1667 (bt)
963
# PoE-Out Configuration
PoE Configuration is supported on all MikroTik devices with PoE-Out interfaces, the configurations can be edited from the RouterOS and SwOS interfaces.
# RouterOS
Sub-menu:interface ethernet poe
# Usage
RouterOS provides an option to configure PoE-Out over Winbox, Webfig, and CLI, basic commands using the CLI are
Property | Description
----------------------
print() | Prints PoE-Out related settings.
export() | export is displayed under/interface ethernetmenu.
monitor(string| interface) | Shows poe-out-status of a specified port, or all ports with/interface ethernet poe monitor [find]command.
power-cycle(duration:0..1m |; Default:5s) | Disables PoE-Out power for a specified period of time.
```
/interface ethernet
```
```
/interface ethernet poe monitor [find]
```
# Global Settings
Sub-menu:/interface ethernet poe settings
```
/interface ethernet poe settings
```
Some MikroTik PoE-Out devices support the global PoE settings
Property | Description
----------------------
ether1-poe-in-long-cable(yes | no) | Setting it to "yes" will disable short detection on all poe-out ports. This is potentially dangerous settings and should be used with caution.  This feature disables strict input/output current monitoring (short detection) to allow the use of PoE-Out with long ethernet cables and/or avoiding improper short-circuit detection. Itcan also affect PoE-Out behavior on PSE which is powered using a DC connector
psuX-max-power | Specifies the maximum power in watts that the PSU can draw.default - 96Wpsu1 - RB5009UPr+S+IN  = DC-jack  | RB5009UPr+S+OUT - 2-PINpsu2 - RB5009UPr+S+IN  = 2-PIN terminal | RB5009UPr+S+OUT - not availableThis command is designed specifically for RB5009UPr+S+ to ensure the safety and optimal performance of the Power Supply Unit (PSU). It allows users to set the maximum power limit for the PSU, preventing potential overload that could compromise the stability and longevity of the system.
Specifies the maximum power in watts that the PSU can draw.default - 96W
psu1 - RB5009UPr+S+IN  = DC-jack  | RB5009UPr+S+OUT - 2-PIN
psu2 - RB5009UPr+S+IN  = 2-PIN terminal | RB5009UPr+S+OUT - not available
This command is designed specifically for RB5009UPr+S+ to ensure the safety and optimal performance of the Power Supply Unit (PSU). It allows users to set the maximum power limit for the PSU, preventing potential overload that could compromise the stability and longevity of the system.
# Port Settings
PoE-Out can be configured under the menu. Each port can be controlled independently.
Property | Description
----------------------
name() | Name of an interface
poe-out(auto-on | forced-on | off; Default:auto-on) | Specifies PoE-Out stateauto-on- the board will attempt to detect if power can be applied to the port. For powering there should be resistance in the range from 3kΩ to 26.5kΩforced-on- detection range is removed. As a result power over Ethernet will be always onoff- all detection and power is turned off for this port
poe-priority(integer:0..99 | any; Default:10) | poe-priority specifies the importance of PoE-Out ports, in cases when a total PoE-Out limit is reached, interface with the lowest port priority will be powered off first.Highest priority is 0, the lowest priority is 99. If there are 2 or more ports with the same priority then port with the smallest port number will have a higher priority.Every 6 seconds ports will be checked for a possibility to provide PoE-Out if it was turned off due to port priority.
poe-voltage(auto | low | high; Default:auto) | A feature that allows us to manually switch between two voltage outputs on PoE-Out ports. It will take effect only on PSE with switchable voltage modes (CRS112-8P-4S-IN,CRS328-24P-4S+RM,netPower 16P,CRS354-48P-4S+2Q+RM).
poe-lldp-enabled( yes / no;Default:no) | Link Layer Discovery Protocol(LLDP) is a layer-2 Ethernet protocol for managing devices. LLDP allows an exchange of information between a PSE and a PD.Starting from RouterOS version 7.15, the setting has been replaced with theNeighbor Discoverylldp-poe-powerproperty.
Highest priority is 0, the lowest priority is 99. If there are 2 or more ports with the same priority then port with the smallest port number will have a higher priority.
A feature that allows us to manually switch between two voltage outputs on PoE-Out ports. It will take effect only on PSE with switchable voltage modes (CRS112-8P-4S-IN,CRS328-24P-4S+RM,netPower 16P,CRS354-48P-4S+2Q+RM).
Link Layer Discovery Protocol(LLDP) is a layer-2 Ethernet protocol for managing devices. LLDP allows an exchange of information between a PSE and a PD.
Starting from RouterOS version 7.15, the setting has been replaced with theNeighbor Discoverylldp-poe-powerproperty.
```
lldp-poe-power
```
# Power-cycle settings
RouterOS provides a possibility to monitor PD using a ping, and power-cycle a PoE-Out port when the host does not respond. power-cycle-ping feature can be enabled under/interface ethernet poemenu.
```
/interface ethernet poe
```
Property | Description
----------------------
power-cycle-ping-enabled(yes | no; Default:no) | Enables ping watchdog, power-cycles port if a host does not respond to ICMP or MAC-Telnet packets.
power-cycle-ping-address(IPv4 | IPv6 | MAC; Default: ) | An address which will be monitored. Since RouterOS 6.46beta16, an active route towards PD is required in case an IP address is configured, so make sure PSE can reach the PD. In case the MAC address is specified, PSE will send MAC-Telnet ping requests only from a specified ethernet interface. When configuring abridge vlan-filteringor some way ofVLAN switching, it is recommended to use the IP address for monitoring your PD.
power-cycle-ping-timeout(time:0..1h |; Default:5s) | If the host does not respond for more than <timeout> period of time, then PoE-Out port is switched off for 5s.
power-cycle-interval(time| any; Default: ) | Disables PoE-Out power for 5s between the specified intervals. Not related with the power-cycle-ping feature.
If power-cycle is enabled,/interface ethernet poe monitorwill show the actual status of the host and time when power cycle will be performed[1]
```
/interface ethernet poe monitor
```
# SwOS
SwOS interface provides basic PoE-Out configuration and monitoring options, see more details in theSwOS PoEuser manual.
# PoE-Out Monitoring
# RouterOS
Sub-menu:interface ethernet poe monitor
```
interface ethernet poe monitor
```
Property | Description
----------------------
name() | Name of an interface
poe-out() | Shows PoE-Out settings
poe-out-status() | Shows current PoE-Out status on portpowered-on- Power is applied to the port, and PoE-Out is operating normally,waiting-for-load- PSE attempts to detect if power can be applied to the port. For powering there should be resistance in the range from 3kΩ to 26.5kΩ;short-circuit- Short-circuit is detected on PoE-Out port, power is switched off, the only detection with low voltage takes place. This can also mean that PoE is not supported on the connected device.overload- The PoE-Out current limit is exceeded, power is switched off on PoE-Out port. For port limits see each model specifications.voltage-too-low- PD can not be powered with the voltage provided from PSE.voltage_too_high- PSE controller cannot power PD with high voltage;current-too-low- current-too-low means that PD draws too low current  (<10mA) than normal PoE-Out device should, the reason for this can be:The delivered voltage at PD is too low for normal powering (for example Vmin =>30V, but provided 24V);PD uses a second power source which has a higher voltage than PSE, so all current is taken from the second DC source, not PSE PoE-Out port;off- all detection and power is turned off for this port;power_reset- PSE controller resetting the power, for example, when executing the power cycle command or when pings fail (power-cycle-ping);controller_init- PSE controller initialization;controller_upgrade- PSE controller is being upgraded;controller_error- PSE controller does not respond.
poe-out-voltage() | Displays PoE Voltage which is applied to the PD.
poe-out-current() | Displays port current (mA) which is drawn by the PD.
poe-out-power() | Displays PD power consumption
The delivered voltage at PD is too low for normal powering (for example Vmin =>30V, but provided 24V);
PD uses a second power source which has a higher voltage than PSE, so all current is taken from the second DC source, not PSE PoE-Out port;
Ifpower-cycle-pingfeature is used,/interface ethernet poe monitor [find]will show additional fields:
```
power-cycle-ping
```
```
/interface ethernet poe monitor [find]
```
# SNMP
It is possible to monitor PoE-Out values using SNMP protocol, this requires enabled SNMP on PSE.SNMP Wiki
SNMP OID tables:
SNMP values can be requested also from the RouterOS, for example,snmp-walkwill print current mA from all available PoE-Out ports:
```
snmp-walk
```
To get very specific OID value, usesnmp-gettool (displays current mA on ether3 interface):
```
snmp-get
```
# PoE-Out notifications
# PoE-Out LEDs
# Models with dependant voltage output
PoE-Out LED behavior can differ between models, but most of them will indicate PoE-Out state on one additional LED. Devices with one voltage output will light:
# Models with selectable voltage output
Models with multiple voltage options can indicate additional information:
# Model-specific LED behavior
# PoE-Out Logs
By default PoE-Out, eventloggingis enabled and uses "warning" and "info" topics to notify the user about PoE-Out state changes. Log entries will be added to each PoE-Out state change. Important logs will be added with a "warning" topic, informative logs will be added with the "info" topic.  When PoE LLDP is enabled, LLDP status updates are available in the device logs, for example:
Possible denial reasons:
To avoid unnecessary logging in cases when PD is not powered because of current-too-low, RouterOS will filter such events, and add one log per every 512 current-too-low events.
Logs can be disabled if necessary:
# PoE-Out Warnings in GUI/CLI
To notify a user about important PoE-Out related problems, messages will be shown in Winbox / WebFig and CLI interface fields:
WebFig and Winbox will notify user under interfaces:
# How it works
# PoE-Out Modes
# auto-on mode
If auto-on is selected on PoE-Out interface, then port operates in this strict order:
# forced-on mode
If forced-on is selected then port operates in this strict order:
# off mode
If off mode is used, PoE-Out on the port will be turned off, no detection will take place, and the interface will behave like a simple Ethernet port.
# PoE-Out limitations
It is important to check PoE-Out specification to find out hardware limitations because it can differ between models
# PoE-Out port limitation
PoE-Out ports are limited with max amp values which are supported in particular voltage, usually max current will differ for low voltage devices (up to 30 V), and for high voltage devices (31 to 57 V).
# PoE-Out total limitation
PSE has also a total PoE-Out current limitation which can't be exceeded, even if the individual port limit allows it.
# PoE Out polarity
All MikroTik PSE uses the same PoE-Out pin polarityMode B4,5 (+) and 7,8 (-), however other vendors can use opposite or Mode A pinout on PD. Reverse polarity would require using a crossover cable but Mode A PD would require Mode B to Mode A converter.
# Safety
PSE has the following safety features:
# PoE-Out compatibility detection
The auto-on mode is considered safe, it will check if the resistance on the port is within allowed range and only then enable PoE out on the interface. The range is 3kΩ to 26.5kΩ
# Overload protection
When a PoE-Out port is powered-on, it is constantly checked for overload. If the overload is detected, PoE-Out is turned off on the port to avoid damage to the PD or PSE.
In seconds the PoE Out feature will be turned on again to see if the environment has changed and PD can be supplied with power again. That is important for configurations that are not connected to mains (solar installations, equipment running on batteries due to mains failure) so that when voltage drops - overload will be detected and connected devices turned off. After a while when the voltage level returns to usual operating value - connected equipment can be powered up again.
# Short circuit detection
When power is enabled on PoE-Out port, PSE continuously checks for a short circuit. If it is detected to ensure that there is no additional damage to PD and PSE, the power is turned off on all ports. PSE will continue to check PoE-Out port until the environment returns to normal.
# Model-specific features
PSE with independent 8-port sections (CRS112-8P-4S-IN,CRS328-24P-4S+RM,netPower 16P,CRS354-48P-4S+2Q+RM) allows PoE-Out to work independently from the RouterOS, this means that you can reboot/upgrade your RouterOS and the PD will not be rebooted.
# PoE Out examples
RouterOS allows us to define priorities on PoE-Out ports, so if your installation is going overpower budget, the PSE will disable less important PD with the lowest priority.
The priority of0is the highest priority,99- lowest
# Setting up priority
Example of how to set priorities from CLI:
What will happen when power budget will go over total PoE-Out limit - first if the overload is detected, ether5 will be turned off (lowest priority), then recheck is done and if the still total limit overload is detected next port in priority will be turned off, in this example, ether3 will be turned off. Both of these ports will be reached every few seconds to check if it is possible to turn PoE-Out on for these ports. Power up will happen in reverse order as the power was cut.
# Same priority
if all, or some ports will have the same poe-priority, then port with the lowest port number will have higher priority
In this example, if the total PoE-Out limit is reached ether5 will be turned off first, then ether4 then ether3 as all of these ports have same poe priority.
# Monitoring PoE-Out
PoE-Out ports can be monitored using a command/interface ethernet poe monitor <interface>
```
/interface ethernet poe monitor <interface>
```
# Power-cycle ping
Monitor connected PD with power-cycle-ping feature:
In this example, PD attached to ether1 will be continuously monitored using a power-cycle-ping feature, which will send ICMP ping requests and wait for a reply. If PD with IP address 192.168.88.10 will not respond for more than 30s, the PoE-Out port will be switched off for 5s.
# Troubleshooting
In cases where a PD does not power-up or reboots unexpectedly when powered from your PSE, it's suggested to the first check:
```
(MAX power consumption of PSE) + (MAX power consumption of all PD) + 10%)
```
# Legacy
# PoE-Out Controller upgrade
PoE-Out devices which are running RouterOS 5.x can also hold old PoE-Out controller firmware, upgrade to RouterOS 6.x will automatically update the PoE-Out firmware. Changes between 1.x and 2.x PoE-Out controller firmware will result in higher Max-port limits (0.5A to 1A) in case if it's supported by the hardware, also will provide some additional data which can be monitored, and allow to use PoE-Out priorities.
All MikroTik devices which come with RouterOS 6.x already support the latest PoE-Out firmware.