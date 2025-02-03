---
title: UPS
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/120324130/UPS,
crawled_date: 2025-02-02T21:15:36.671773
section: mikrotik_docs
type: documentation
---

## Summary
Sub-menu:/system upsStandards:APC Smart Protocol
```
/system ups
```
```
APC Smart Protocol
```
The UPS monitor feature works with APC UPS units that support “smart” signalling over serial RS232 or USB connection. The UPS monitor service is not included in the default set of packages so it needs to be downloaded and installed manually with ups.npk package. This feature enables the network administrator to monitor the UPS and set the router to ‘gracefully’ handle any power outage with no corruption or damage to the router. The basic purpose of this feature is to ensure that the router will come back online after an extended power failure. To do this, the router will monitor the UPS and set itself to hibernate mode when the utility power is down and the UPS battery has less than 10% of its battery power left. The router will then continue to monitor the UPS (while in hibernate mode) and then restart itself when the utility power returns. If the UPS battery is drained and the router loses all power, the router will power back to full operation when the ‘utility’ power returns.
The UPS monitor feature on the MikroTik RouterOS supports
* hibernate and safe reboot on power and battery failure
* UPS battery test and run time calibration test
* monitoring of all "smart" mode status information supported by UPS
* logging of power changes
## Connecting the UPS unit
The serial APC UPS (BackUPS Pro or SmartUPS) requires a special serial cable (unless connected with USB). If no cable came with the UPS, a cable may be ordered from APC or one can be made "in-house". Use the following diagram:
Router Side (DB9f) | Signal | Direction | UPS Side (DB9m)
---------------------------------------------------------
2 | Receive | IN | 2
3 | Send | OUT | 1
5 | Ground |  | 4
7 | CTS | IN | 6
If using a RouterBOARD device, make sure to set your "RouterBOOT setup key" toDeleteinstead of the defaultAny key. This is to avoid accidental opening of the setup menu if the UPS unit sends some data to the serial port during RouterBOARD startup. This can be done in the RouterBOOT options during boot time or via the RouterBoard Settings in Winbox :
```
Select key which will enter setup on boot:
 * 1 - any key
   2 - <Delete> key only
your choice:
```
## General Properties
Property | Description
----------------------
alarm-setting(delayed | immediate | low-battery | none; Default:immediate) | UPS sound alarm setting:delayed - alarm is delayed to the on-battery eventimmediate - alarm immediately after the on-battery eventlow-battery - alarm only when the battery is lownone - do not alarm
check-capabilities(yes | no; Default:yes) | Whether to check UPS capabilities before reading information. Disabling it can fix compatibility issues with some UPS models. (Applies to RouterOS version 6, implemented since v6.17)
min-runtime(time; Default:never) | Minimal run time remaining. After a 'utility' failure, the router will monitor the runtime-left value. When the value reaches the min-runtime value, the router will go to hibernate mode.never - the router will go to hibernate mode when the "battery low" signal is sent indicating that the battery power is below 10%0s - the router will continue to work as long as the battery is supplying sufficient voltage
offline-time(time; Default:0s) | How long to work on batteries. The router waits that amount of time and then goes into hibernate mode until the UPS reports that the 'utility' power is back0s - the router will go into hibernate mode according to the min-runtime setting. In this case, the router will wait until the UPS reports that the battery power is below 10%
port(string; Default: ) | Communication port of the router.
* delayed - alarm is delayed to the on-battery event
* immediate - alarm immediately after the on-battery event
* low-battery - alarm only when the battery is low
* none - do not alarm
* never - the router will go to hibernate mode when the "battery low" signal is sent indicating that the battery power is below 10%
* 0s - the router will continue to work as long as the battery is supplying sufficient voltage
* 0s - the router will go into hibernate mode according to the min-runtime setting. In this case, the router will wait until the UPS reports that the battery power is below 10%
Read-only properties:
Property | Description
----------------------
load(percent) | The UPS's output load as a percentage of full rated load in Watts. The typical accuracy of this measurement is ±3% of the maximum of 105%
manufacture-date(string) | UPS's date of manufacture in the format "mm/dd/yy" (month, day, year).
model(string) | Less than 32 ASCII character string consisting of the UPS model name (the words on the front of the UPS itself)
nominal-battery-voltage(integer) | UPS's nominal battery voltage rating (this is not the UPS's actual battery voltage)
offline-after(time) | When will the router go offline
serial(string) | A string of at least 8 characters directly representing the UPS's serial number as set at the factory. Newer SmartUPS models have 12-character serial numbers
version(string) | UPS version, consists of three fields: SKU number, firmware revision, country code. The country code may be one of the following:I - 220/230/240 VacD - 115/120 VacA - 100 VacM - 208 VacJ - 200 Vac
* I - 220/230/240 Vac
* D - 115/120 Vac
* A - 100 Vac
* M - 208 Vac
* J - 200 Vac
### Example
To enable the UPS monitor for port serial1:
```
[admin@MikroTik] system ups> add port=serial1 disabled=no
[admin@MikroTik] system ups> print
Flags: X - disabled, I - invalid
 0    name="ups" port=serial1 offline-time=5m min-runtime=5m
      alarm-setting=immediate model="SMART-UPS 1000" version="60.11.I"
      serial="QS0030311640" manufacture-date="07/18/00"
      nominal-battery-voltage=24V
[admin@MikroTik] system ups>
```
## Runtime Calibration
Command:/system ups rtc <id>
```
/system ups rtc <id>
```
The rtc command causes the UPS to start a run time calibration until less than 25% of full battery capacity is reached. This command calibrates the returned run time value.
## Monitoring
Command:/system ups monitor <id>
```
/system ups monitor <id>
```
Property | Description
----------------------
battery-charge() | the UPS's remaining battery capacity as a percent of the fully charged condition
battery-voltage() | the UPS's present battery voltage. The typical accuracy of this measurement is ±5% of the maximum value (depending on the UPS's nominal battery voltage)
frequency() | when operating on-line, the UPS's internal operating frequency is synchronized to the line within variations of 3 Hz of the nominal 50 or 60 Hz. The typical accuracy of this measurement is ±1% of the full scale value of 63 Hz
line-voltage() | the in-line utility power voltage
load() | the UPS's output load as a percentage of full rated load in Watts. The typical accuracy of this measurement is ±3% of the maximum of 105%
low-battery(yes | no) | only shown when the UPS reports this status
on-battery(yes | no) | Whether UPS battery is supplying power
on-line(yes | no) | whether power is being provided by the external utility (power company)
output-voltage() | the UPS's output voltage
overloaded-output(yes | no) | only shown when the UPS reports this status
replace-battery(yes | no) | only shown when the UPS reports this status
runtime-calibration-running(yes | no) | only shown when the UPS reports this status
runtime-left(time) | the UPS's estimated remaining run time in minutes. You can query the UPS when it is operating in the on-line, bypass, or on-battery modes of operation. The UPS's remaining run time reply is based on available battery capacity and output load
smart-boost-mode(yes | no) | only shown when the UPS reports this status
smart-ssdd-mode() | only shown when the UPS reports this status
transfer-cause(string) | the reason for the most recent transfer to on-battery operation (only shown when the unit is on-battery)
### Example
When running on utility power:
```
[admin@MikroTik] system ups> monitor 0
          on-line: yes
       on-battery: no
      RTC-running: no
     runtime-left: 20m
   battery-charge: 100%
  battery-voltage: 27V
     line-voltage: 226V
   output-voltage: 226V
             load: 45%
      temperature: 39C
        frequency: 50Hz
  replace-battery: no
      smart-boost: no
       smart-trim: no
         overload: no
      low-battery: no
[admin@MikroTik] system ups>
```
When running on battery:
```
[admin@MikroTik] system ups> monitor 0
          on-line: no
       on-battery: yes
   transfer-cause: "Line voltage notch or spike"
      RTC-running: no
     runtime-left: 19m
    offline-after: 4m46s
   battery-charge: 94%
  battery-voltage: 24V
     line-voltage: 0V
   output-voltage: 228V
             load: 42%
      temperature: 39C
        frequency: 50Hz
  replace-battery: no
      smart-boost: no
       smart-trim: no
         overload: no
      low-battery: no
      [admin@MikroTik] system ups>
```