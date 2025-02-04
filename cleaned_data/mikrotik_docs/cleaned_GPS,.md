# Document Information
Title: GPS
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/84901890/GPS,

# Content
# Summary
Package requirement:gpsSub-menu:/system gpsStandards:GPS, NMEA 0183,Simple Text Output Protocol
```
gps
```
```
/system gps
```
```
GPS, NMEA 0183,Simple Text Output Protocol
```
Global Positioning System (GPS) is used for determining the precise location of a GPS receiver.
# Configuration Properties
Property | Description
----------------------
channel(integer [0..4294967295]; Default:0) | Port channel used by the device
coordinate-format(dd | dms | ddmm; Default:no) | Which coordinate format to use, "Decimal Degrees", "Degrees Minutes Seconds" or "NMEA format DDDMM.MM[MM]"
enabled(yes | no; Default:no) | Whether GPS is enabled
gps-antenna-select(external | internal; Default:internal) | Depending on the model. Internal antenna can be selected, if the device has one installed.
init-channel(integer [0..4294967295]; Default: ) | Channel for init-string execution
init-string(string; Default: ) | AT init string for GPS initialization
port(string; Default: ) | Name of the USB/Serial port where the GPS receiver is connected
set-system-time(yes | no; Default:no) | Whether to set the router's date and time to one received from GPS.
# Monitoring Status
Command:/system gps monitor
```
/system gps monitor
```
This command is used for monitoring the data received from a GPS receiver.
Parameters:
Property | Description
----------------------
date-and-time(date) | Date and time received from GPS
latitude(none | string) | Latitude in DM (Degrees Minute decimal) format
longitude(none | string) | Longitude in DM (Degrees Minute decimal) format
altitude(none | string) | Altitude based on GPS data
speed(none | string) | The current moving speed of the GPS unit
destination-bearing(none | string) | The direction toward which a GPS is moving
true-bearing(none | string) | The direction toward which a GPS is moving
magnetic-bearing(none | string) | The direction toward which a GPS is moving
valid(yes | no) |
satellites(integer) | Number of satellites seen by the device.
fix-quality(integer) | Quality of the signal
horizontal-dilution(integer) | Horizontal dilution of precision (HDOP);
data-age(integer) | The time that has passed since the device received the last NMEA message
# Basic examples
Check port usage, as only one instance can use the serial port simultaneously:
```
[admin@MikroTik] /port print
Flags: I - inactive
# DEVICE NAME                     CHANNELS USED-BY                   BAUD-RATE
0          serial0                         1 Serial Console            auto
```
In case there is one port and it is used by the console, release it from the console menu:
```
[admin@MikroTik] > /system console print
Flags: X - disabled, U - used, F - free
# PORT                                                                       TERM
0 U serial0                                                                    vt102
[admin@MikroTik] > /system console disable 0
```
Adjust port settings specifically for your device (leave "auto" for LtAP mini):
```
[admin@MikroTik] /port> set 0 baud-rate=4800 parity=odd
[admin@MikroTik] /port> print detail
Flags: I - inactive
0   name="usb1" used-by="" channels=1 baud-rate=4800 data-bits=8 parity=odd stop-bits=1 flow-control=none
```
Enable GPS:
```
[admin@MikroTik] /system gps> set enable=yes port=usb1
[admin@MikroTik] /system gps> print
enabled: yes
port: usb1
channel: 0
init-channel: 0
init-string:
set-system-time: no
```
Monitor status:
```
[admin@MikroTik] /system gps> monitor
date-and-time: sep/07/2021 08:26:26
latitude: 56.969689
longitude: 24.162471
altitude: 25.799999m
speed: 0.759320 km/h
destination-bearing: none
true-bearing: 185.500000 deg. True
magnetic-bearing: 0.000000 deg. Mag
valid: yes
satellites: 6
fix-quality: 1
horizontal-dilution: 1.3
```
Port and GPS settings forLtAP
```
/port set serial1 baud-rate=115200
```
```
/system gps set port=serial1 channel=0 enabled=yes
```
We have also created an in-depth article about live GPS tracking, using scripting and a web server:GPS-tracking.
# Troubleshooting
Note that sometimes to make the GPS module recognized in RouterOS you need to change the baud-rate setting in the '/port' menu.
```
/port
```
LtAP minihas a low-gain GPS antenna built-in and for a better experience, we suggest using an additionalexternal antenna.
Switch between internal and external antennas under the GPS menu:
```
[admin@MikroTik] > /system gps set gps-antenna-select=external
```
On some modems with GPS support, you need to send multiple init commands for continuous GPS monitoring, for example, for Huawei cards you need to send "AT^WPDST=1,AT^WPDGP" init string to get continuous monitoring.