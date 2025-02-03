---
title: Ports
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/8978525/Ports,
crawled_date: 2025-02-02T21:14:42.412205
section: mikrotik_docs
type: documentation
---

* 1Summary
* 2General
* 3Properties
* 4Remote Access
* 5Properties
# Summary
There are many ways how to use ports on the routers. Most obvious one is to use serial port for initial RouterOS configuration after installation (by default serial0 is used by serial-terminal).
Serial and USB ports can also be used to:
* connect 3G modems;
* connect to another device through a serial cable
* access device connected to serial cable remotely.
# General
Sub-menu:/port
```
/port
```
Menu lists all available serial and USB ports on the router and allows to configure port parameters, like baud-rate, flow-control, etc.
Below you can see default port configuration on LtAP.
```
[admin@LtAP] > /port/print                 
Columns: DEVICE, NAME, CHANNELS, USED-BY, BAUD-RATE
# DEVICE  NAME     CHANNELS  USED-BY                                     BAUD-RATE
0         serial0         1  Serial Console(#0)                          auto     
1         gps             1  GPS(#0)                                     115200
```
# Properties
Property | Description
----------------------
baud-rate(integer | auto; Default:auto) | Baud rate (speed) used by the port. If set toauto, then RouterOS tries to detect baud rate automatically.
data-bits(7 | 8; Default: ) | The number of data bits in each character.7- true ASCII8- any data (matches the size of a byte)
dtr(on | off; Default: ) | Whether to enable RS-232 DTR signal circuit used by flow control.
flow-control(hardware | none | xon-xoff; Default: ) | method of flow control to pause and resume the transmission of data.
name(string; Default: ) | Name of the port.
parity(even | none | odd; Default: ) | Error detection method. If enabled, extra bit is sent to detect the communication errors. In most cases parity is set tononeand errors are handled by the communication protocol.
rts(on | off; Default: ) | Whether to enable RS-232 RTS signal circuit used by flow control.
stop-bits(1 | 2; Default: ) | Stop bits sent after each character. Electronic devices usually uses 1 stop bit.
* 7- true ASCII
* 8- any data (matches the size of a byte)
Read-only properties
Property | Description
----------------------
channels(integer) | Number of channels supported by the port.
inactive(yes | no) | Shows current port state,inactive=yes- device with port previous was connected, but currently is not present
line-state() | 
used-by(string) | Shows who  is currently are using port and channel (#).  For example, by defaultSerial0is used by serial-console.
Shows current port state,inactive=yes- device with port previous was connected, but currently is not present
Shows who  is currently are using port and channel (#).  For example, by defaultSerial0is used by serial-console.
# Remote Access
Sub-menu:/port remote-access
```
/port remote-access
```
If you want to access serial device that can only talk to COM ports and is located somewhere else behind router, then you can use remote-access.
As defined in RFC 2217 RouterOS can transfer data from/to a serial device over TCP connection.
Enabling remote access on RouterOS is very easy:
```
/port remote-access add port=serial0 protocol=rfc2217 tcp-port=9999
```
# Properties
Property | Description
----------------------
allowed-addresses(IP address range; Default:0.0.0.0/0) | Range of IP addresses allowed to access port remotely.
channel(integer [0..4294967295]; Default:0) | Port channel that will be used. If port has only one channel then channel number should always be0.
disabled(yes | no; Default:no) | 
local-address(IP address; Default: ) | IP address used as source address.
log-file(string; Default:"") | Name of the file, where communication will be logged. By default logging is disabled.
port(string; Default: ) | Name of the port from Port list.
protocol(raw | rfc2217; Default:rfc2217) | RFC 2217 defines a protocol to transfer data from/to a serial device over TCP. If set toraw, then data is sent to serial as is.
tcp-port(integer [1..65535]; Default:0) | TCP port on which to listen for incoming connections.
Read-only properties
Property | Description
----------------------
active(yes | no) | Whether remote access is active and ready to accept connection.
busy(yes | no) | Whether port is currently busy.
inactive(yes | no) | 
logging-active(yes | no) | Whether logging to file is currently running
remote-address(IP address) | IP address of remote location that is currently connected.