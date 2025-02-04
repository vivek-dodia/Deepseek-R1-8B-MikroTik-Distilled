# Document Information
Title: PWR Line
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/47579194/PWR+Line,

# Content
# Summary
The PWR-Line series devices allow Ethernet-like connectivity between supported devices over regular power lines. When plugged into the same electrical circuit, the PWR-Line devices will establish connectivity by using the HomePlug AV standard.
# Properties
arp(disabled | enabled | proxy-arp | reply-only; Default:enabled) | Address Resolution Protocol mode:disabled - the interface will not use ARPenabled - the interface will use ARPproxy-arp - the interface will use the ARP proxy featurereply-only - the interface will only reply to requests originating from matching IP address/MAC address combinations which are entered as static entries in the "/ip arp" table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.
bandwidth(integer/integer; Default:unlimited/unlimited) | Sets max rx/tx bandwidth in kbps that will be handled by an interface. TX limit is supported on all Atherosswitch-chipports. RX limit is supported only on Atheros8327/QCA8337 switch-chip ports.
comment(string; Default: ) | Descriptive name of an item
l2mtu(integer [0..65536]; Default: ) | Layer2 Maximum transmission unit.MTU in RouterOS
mac-address(MAC; Default: ) | Media Access Control number of an interface.
mtu(integer [0..65536]; Default:1500) | Layer3 Maximum transmission unit
name(string; Default: ) | Name of an interface
orig-mac-address(MAC; Default: ) |
rx-flow-control(on | off | auto; Default:off) | When set to on, the port will process received pause frames and suspend transmission if required.autois the same asonexcept when auto-negotiation=yes flow control status is resolved by taking into account what the other end advertises. The feature is supported on AR724x, AR9xxx, and QCA9xxx CPU ports, all CCR ports, and all Atheros switch chip ports.
tx-flow-control(on | off | auto; Default:off) | When set to on, the port will send pause frames when specific buffer usage thresholds are met.autois the same asonexcept when auto-negotiation=yes flow control status is resolved by taking into account what the other end advertises. The feature is supported on AR724x, AR9xxx, and QCA9xxx CPU ports, all CCR ports, and all Atheros switch chip ports.
# Menu specific commands
Property | Description
----------------------
configure() | The command configures the attached PWR-Line device's network-key, network-password, plc-cco-selection-mode.
join() | Initiates the pairing sequence which will look for other PWR-Line devices in the same electrical circuit that is also in the pairing mode. This mode lasts for 60 seconds.
leave() | Initiates the leaving sequence which essentially randomizes the device's network-key.
monitor() | Outputs PWR-Line-related statuses in real-time.
upgrade-firmware() | Upgrades the PWR-Line device with specified firmware-file and pib-file files.
# Configuration example
For two or more devices to be able to connect with each other, they must share the same network-key value. The currently configured network-key can be seen using the monitor command as plc-actual-network-key.
```
[admin@MikroTik] > /interface pwr-line monitor pwr-line1
name: pwr-line1
connection-to-plc: ok
tx-flow-control: no
rx-flow-control: no
plc-actual-network-key: c973947c200e1540b0f84b571d92bebe
plc-hw-platform: QCA7420
plc-sw-platform: MAC
plc-fw-version: 1.4.0(24-20180515-CS)
plc-line-freq: 50Hz
plc-zero-crossing: detected
plc-mac: B8:69:F4:C4:34:68
```
# Method 1
There are two ways to set the same network-key on different devices. You can either use the network-key parameter which is a hashed version of network-password parameter. Or use the network-password parameter and let the router apply the hash on a human-readable string.
For example:
```
/interface pwr-line configure pwr-line1 network-password=mynetwork
```
is the same as:
```
/interface pwr-line configure pwr-line1 network-key=cb01fcc6167bf3d1edb1433c2ebde4b3
```
You must set the same key or password on all devices you wish to communicate with each other.
# Method 2
It is possible to use the join and leave commands and make the PWR-Line devices automatically synchronize the network-key value. It is advised to use the leave command before using the join command to make sure a new network-key is randomly generated and the device is not part of any old network.
```
/interface pwr-line leave pwr-line1
```
Then we can issue the join command. When doing so, the pairing sequence is enabled for 60 seconds, meaning you have to enable pairing mode on another device within 60 seconds for them to successfully pair.
```
/interface pwr-line join pwr-line1
```
# Method 3
It is also possible to set a specified role for the PWR-Line device (master or slave) with the plc-cco-selection-mode parameter.
Property | Description
----------------------
plc-cco-selection-mode(auto | always | never; Default:auto) | Sets PWR-Line device mode:auto - PWR-Line will automatically decide what role to take depending on the situation upon joining a PWR-Line network.always - PWR-Line will always be forced to act as "central-coordinator" or master device.never - PWR-Line will always be forced to act as a slave device.
Example:
```
/interface pwr-line configure pwr-line1 plc-cco-selection-mode=auto
```
```
/interface pwr-line configure pwr-line1 plc-cco-selection-mode=always
```
```
/interface pwr-line configure pwr-line1 plc-cco-selection-mode=never
```
# Sync Button usage
# Supported Hardware
The device is fully compatible with our PWR-LINE AP and the newest revisions of products that have a MicroUSB port, such as hAP lite, hAP lite tower, hAP mini, mAP, and mAP lite have a pwr-line interface. A simple software upgrade to v6.44+ enables this feature (supported by the mentioned devices with serial numbers that end with /9xx). PWR-LINE functionality is also supported by some previously manufactured units - if you have a unit with a serial number that ends with /8xx, upgrade to 6.44+ and see if the pwr-line interface shows up).