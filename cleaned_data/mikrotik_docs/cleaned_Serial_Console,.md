# Document Information
Title: Serial Console
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328139/Serial+Console,

# Content
# Overview
The Serial Console and Serial Terminal are tools, used to communicate with devices and other systems that are interconnected via the serial port. The serial terminal may be used to monitor and configure many devices - including modems, network devices (including MikroTik routers), and any device that can be connected to a serial (asynchronous) port.
The Serial Console feature is for configuring direct-access configuration facilities (monitor/keyboard and serial port) that are mostly used for initial or recovery configuration. A special null-modem cable is needed to connect two hosts (like two PCs, or two routers; not modems). Note that a terminal emulation program (e.g., HyperTerminal on Windows or minicom on Linux) is required to access the serial console from another computer. Default settings of the router's serial port are 115200 bits/s (for x86 default is 9600 bits/s), 8 data bits, 1 stop bit, no parity, hardware (RTS/CTS) flow control.
Several customers have described situations where the Serial Terminal (managing side) feature would be useful:
With the serial-terminal feature of the MikroTik, up to 132 (and, maybe, even more) devices can be monitored and controlled.
# Serial Console Connections
Serial communications between devices are done with RS232, it is one of the oldest and most widely spread communication methods in the computer world. It was used for communication with the modems or other peripheral devices DTE/DCE. In the modern world, the main use of serial communication is DTE/DTE communication (Data Terminal Equipment) e.g. using a null-modem cable. There are several types of null modem cables and some of them may not work with RouterBoards at all.
# Null Modem Without Handshake
This cable does not utilize handshake pins at all:
Side1 (DB9f) | Side2 (DB9f) | Function
--------------------------------------
2 | 3 | Rx ← Tx
3 | 2 | Tx → Rx
5 | 5 | GND
Rx ← Tx
It allows data-only traffic on the cross-connected Rx/Tx lines. Hardware flow control is not possible with this type of cable. The only way to perform flow control is with software flow control using the XOFF and XON characters.
# Null Modem With Loopback Handshake
The problem with the first cable is when connected to a device on which hardware flow control is enabled software may hang when checking modem signal lines.
Null modem cable with loop back handshake fixes the problem, its main purpose is to fool well-defined software into thinking there is handshaking available:
Side1 (DB9f) | Side2 (DB9f) | Function
--------------------------------------
2 | 3 | Rx ← Tx
3 | 2 | Tx → Rx
5 | 5 | GND
1+4+6 | - | DTR → CD + DSR
- | 1+4+6 | DTR → CD + DSR
7+8 | - | RTS → CTS
- | 7+8 | RTS → CTS
Rx ← Tx
GND
Hardware flow control is not possible with this cable. Also if remote software does not send its own ready signal to DTR output communication will hang.
# Null Modem With Partial Handshake
This cable can be used when flow control enabled without being incompatible with the original way flow control was used with DTE/DCE communication.
This type of cable is not recommended for use with RouterOS.
Side1 (DB9f) | Side2 (DB9f) | Function
--------------------------------------
1 | 7+8 | RTS2 → CTS2 + CD1
2 | 3 | Rx ← Tx
3 | 2 | Tx → Rx
4 | 6 | DTR → DSR
5 | 5 | GND
6 | 4 | DSR ← DTR
7+8 | 1 | RTS1 → CTS1 + CD2
RTS2 → CTS2 + CD1
Tx → Rx
# Null Modem With Full Handshake
Used with special software and should not be used with RouterOS.
Side1 (DB9f) | Side2 (DB9f) | Function
--------------------------------------
2 | 3 | Rx ← Tx
3 | 2 | Tx → Rx
4 | 6 | DTR → DSR
5 | 5 | GND
6 | 4 | DSR ← DTR
7 | 8 | RTS → CTS
8 | 7 | CTS ← RTS
Tx → Rx
# Null Modem Compatibility
Summary tables below will allow you to choose the proper cable for your application.
| No handshake | Loopbackhandshake | Partialhandshake | Fullhandshake
----------------------------------------------------------------------
RouterBoardswith limited port functionality | Y | Y | N* | N
RouterBoardswith full functionality | Y | Y | Y | N
Loopbackhandshake
Partialhandshake
| No handshake | Loopbackhandshake | Partialhandshake | Fullhandshake
----------------------------------------------------------------------
Software flowcontrol only | Y | Y* | Y** | Y**
Low-speed DTE/DCE compatiblehardware flow control | N | Y | Y* | N
High-speed DTE/DCE compatiblehardware flow control | N | Y | Y** | N
High speedcommunicationusing special software | N | N | Y* | Y
Loopbackhandshake
Partialhandshake
# RJ45 Type Serial Port
This type of port is used on RouterBOARD 2011, 3011, 4011, CCR1072, CCR1036 r2, CCR2xxx and CRS series devices, sometimes called "Cisco style" serial port.
RJ45 to DB9 Cable Pinout:
Signal | Console Port (DTE)RJ-45 | RJ-45 Rolled CableRJ-45 Pin | Adapter DB-9 Pin | Adapter DB-25 Pin | Signal
--------------------------------------------------------------------------------------------------------------
RTS | 1 | 8 | 8 | 5 | CTS
DTR | 2 | 7 | 6 | 6 | DSR
TxD | 3 | 6 | 2 | 3 | RxD
Ground | 4 | 5 | 5 | 7 | Ground
Ground | 5 | 4 | 5 | 7 | Ground
RxD | 6 | 3 | 3 | 2 | TxD
DSR | 7 | 2 | 4 | 20 | DTR
CTS | 8 | 1 | 7 | 4 | RTS
# RB M33G Additional Serial Header
For RBM33G additional serial header can be attached on GPIO pins U3_RXD, GND, U3_TXD, and 3V3
# CCR Serial Header
The Cloud Core Router series devices have a serial header on the PCB board, called J402 or 100
Here is the pin-out of that connector:
# Serial Terminal Usage
RouterOS allows to communicate with devices and other systems that are connected to the router via the serial port using a/system serial-terminalcommand. All keyboard input will be forwarded to the serial port and all data from the port is output to the connected device.
```
/system serial-terminal
```
First, you have to have a free serial port, if the device has only one serial port (like all RouterBoards, WRAP/ALIX boards, etc.) you will have to disable the system console on this serial port to be able to use it asSerial Terminalfor connection to other equipment (switches, modems, etc):
```
/system console disable 0
```
Be sure to just disable the console rather than removing it, as RouterOS will recreate the console after the next reboot when you really remove it.
Next, you will have to configure your serial port according to the serial port settings of the connected device. Using the following command you will set your serial port to 19200 Baud 8N1. What settings you need to use depends on the device you connect:
```
/port set serial0 baud-rate=19200 data-bits=8 parity=none stop-bits=1
```
You can also try to let RouterOS guess the needed baud rate by setting
```
/port set serial0 baud-rate=auto
```
Now's the time to connect your device if not already done. Usually, you will have to use anull modem cable(the same thing as a cross-over-cable for Ethernet). Now we're ready to go:
```
/system serial-terminal serial0
```
This will give you access to the device you connected to port Serial0.Ctrl-Ais the prefix key, which means that you will enter a small "menu". If you need to send theCtrl-Acharacter to a remote device, pressCtrl-Atwice.
If you want to exit the connection to the serial device typeCtrl-A, thenQ. This will return you to your RouterOS console.
# Special Login
Special login can be used to access another device (like a switch, for example) that is connected through a serial cable by opening a telnet/ssh session that will get you directly on this device (without having to login to RouterOS first).
For demonstration we will use two RouterBoards and one PC.
Routers R1 and R2 are connected with serial cable and PC is connected to R1 via ethernet. Lets say we want to access router R2 via serial cable from our PC. To do this you have to set up serial interface proxy on R1. It can be done by feature calledspecial-login.
First task is to unbind console from serial simply by disabling entry in /system console menu:
```
[admin@MikroTik] /system console> print
Flags: X - disabled, U - used, F - free
# PORT                                                                    TERM
0 X serial0                                                                 vt102
```
Next step is to add new user, in this caseserial, and bind it to the serial port
```
[admin@MikroTik] > /user add name=serial group=full
[admin@MikroTik] > /special-login add user=serial port=serial0 disabled=no
[admin@MikroTik] > /special-login print
Flags: X - disabled
# USER                                                                    PORT
0   serial                                                                  serial0
```
Now we are ready to access R2 from our PC.
```
maris@bumba:/$ ssh serial@10.1.101.146
[Ctrl-A is the prefix key]
R2 4.0beta4
R2 Login:
[admin@R2] >
```
To exit special login mode press Ctrl+A and Q
```
[admin@MikroTik] >
[Q - quit connection]      [B - send break]
[A - send Ctrl-A prefix]   [R - autoconfigure rate]
Connection to 10.1.101.146 closed.
```
To fix this problem you need to allow access bootloader main menu from <any> key to <delete>:
```
What do you want to configure?
d - boot delay
k - boot key
s - serial console
n - silent boot
o - boot device
u - cpu mode
f - cpu frequency
r - reset booter configuration
e - format nand
g - upgrade firmware
i - board info
p - boot protocol
b - booter options
t - call debug code
l - erase license
x - exit setup
your choice: k - boot key
Select key which will enter setup on boot:
2 - <Delete> key only
your choice: 2
```