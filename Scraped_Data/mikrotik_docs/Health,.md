---
title: Health
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/25690117/Health,
crawled_date: 2025-02-02T21:14:53.701576
section: mikrotik_docs
type: documentation
---

## 1Summary2Voltage3Temperature4Fan control and behavior4.1PoE-out consumption4.2Limited manual fan-control option4.3Brief description of the fan-controlSummary
* 1Summary
* 2Voltage
* 3Temperature
* 4Fan control and behavior4.1PoE-out consumption4.2Limited manual fan-control option4.3Brief description of the fan-control
* 4.1PoE-out consumption
* 4.2Limited manual fan-control option
* 4.3Brief description of the fan-control
Hardware that supports monitoring will display different information about hardware status, like temperature, voltage, current, fan-speed, etc.
Example on CCR1072-1G-8S+ device:
```
[admin@MikroTik] > system/health/print 
Columns: NAME, VALUE, TYPE
 #  NAME                VALUE  TYPE
 0  power-consumption   50.8   W   
 1  cpu-temperature     43     C   
 2  fan1-speed          5654   RPM 
 3  fan2-speed          5825   RPM 
 4  fan3-speed          5800   RPM 
 5  fan4-speed          5750   RPM 
 6  board-temperature1  29     C   
 7  board-temperature2  28     C   
 8  psu1-voltage        0      V   
 9  psu2-voltage        12.1   V   
10  psu1-current        0      A   
11  psu2-current        4.2    A
```
Warning:For feature availability on RouterBOARD products checkmikrotik.com
Intensive health monitoring on theCCR2004-16G-2S+PCdevice (from the console, winbox or SNMP) causes significant CPU load.
## Voltage
Routers that support voltage monitoring will display supplied voltage value. In CLI/Winbox it will display volts. In scripts/API/SNMP this will be dV or value showed in CLI/Winbox
Note:Routers that have PEXT and PoE power input are calibrated using PEXT, as a result, value showed over PoE can be lower than input voltage due to additional ethernet protection chains.
```
[admin@MikroTik] > system/health/print 
Columns: NAME, VALUE, TYPE
#  NAME         VALUE  TYPE
0  voltage      23.8   V   
1  temperature  39     C
```
## Temperature
Routers that support temperature monitoring will display temperature reading. In CLI/Winbox it will display degrees Celsius. Using scripts/API/SNMP this value will be shown in CLI/Winbox multiplied by 10. There are various temperature sensors depending on the device. These sensors may refer to: cpu-temperature, pcb-temperature, sfp-temperature. Device tested ambient temperature range you can find in specification description atmikrotik.com. Tested ambient temperature range is temperature in which device can be physically located. It isnotthe same as temperature which reports system health monitor!
## Fan control and behavior
```
/system health set
```
Using this menu users will be able to control fan behaviour on TILE architecturedevices.
Note:Improved FAN stability starting from version 6.45.5.
There are three parameters that may affect fan behaviour: PoE-out consumption, SFP temperature and CPU temperature. As soon as one of the parameters exceeds the optimal value the, fans are started.
### PoE-out consumption
If a device has PoE-out, then the fan RPM will change as described below:
PoE-out load | RPM % of max FAN speed
-------------------------------------
0%..24% | FAN speed 0%
25%..46% | FAN speed 25%
47%..70% | FAN speed 50%
71%..92% | FAN speed 75%
93%.. | FAN speed 100%
RPM % of max FAN speed
For devices withPWMfans, the speed will linearly increase or decrease from 9..88% (note: below 100W the fan RPM=0)
### Limited manual fan-control option
Note:Starting from RouterOS version 7.9 limited manual fan-control options have been added for CRS3xx, CRS5xx and CCR2xxx devices.
Note:Starting from RouterOS version 7.14 limited manual fan-control is available for the CCR1036-8G-2S+-r2, CCR1036-12G-4S-r2 and CCR1016-12S-1S+-r2 devices.
Fan behavior can be manipulated using the settings section of system health:
```
/system health settings set
```
Available properties are described below:
Property | Description
----------------------
fan-full-speed-temp(integer[-273..65];Default:65) | Sets the temperature value upon which the fan speed will be increased to the maximum possible rpm.Reads temperature from CPU, PHY, SWITCH and SFP and adjusts fan speed based on the component with the highest temperature.
fan-target-temp(integer[-273..65];Default:58) | Sets the target temperature for the hottest component. Based on this setting adjusts fan behavior to hold temperatures in target range.
fan-min-speed-percent(integer[0..100];Default:depends on FAN controller) | Sets the minimum percentage of fan speed thus not allowing fans to have a lower rpm than this value.*NOTE:the default value may vary based on FAN controller chip and/or specific model requirements. From RouterOS verson 7.14 default value is set to12,all previous versions have0.
fan-control-interval(integer[5..30];Default:30) | Sets the actual temperature data read interval to get temperature values from CPU, PHY, SWITCH and SFP.*NOTE:THIS SETTING DIRECTLY AFFECTS CPU USAGE
cpu-overtemp-check(yes | no; Default: no) | Enables/disables CPU overtemperature monitoring.(Available for ARM/ARM64 devices)
cpu-overtemp-threshold(integer [0..105]; Default: 105) | Maximum temperature before triggering an overtemperature protection.
cpu-overtemp-startup-delay(time; Default: 1m) | Delay after startup before enabling overtemperature monitoring.
Sets the temperature value upon which the fan speed will be increased to the maximum possible rpm.
Reads temperature from CPU, PHY, SWITCH and SFP and adjusts fan speed based on the component with the highest temperature.
Sets the target temperature for the hottest component. Based on this setting adjusts fan behavior to hold temperatures in target range.
Sets the minimum percentage of fan speed thus not allowing fans to have a lower rpm than this value.*NOTE:the default value may vary based on FAN controller chip and/or specific model requirements. From RouterOS verson 7.14 default value is set to12,all previous versions have0.
Sets the actual temperature data read interval to get temperature values from CPU, PHY, SWITCH and SFP.
*NOTE:THIS SETTING DIRECTLY AFFECTS CPU USAGE
Enables/disables CPU overtemperature monitoring.
(Available for ARM/ARM64 devices)
Maximum temperature before triggering an overtemperature protection.
Delay after startup before enabling overtemperature monitoring.
### Brief description of the fan-control
If at least one of the internal measured (CPU, SFP, Switch, Board etc.) temperatures exceedfan-target-temp, the fans will start to spin. The higher the temperature, the faster the fans will spin. For devices with PWM fans, as the internal measured temperatures exceedfan-target-temp, the fans will linearly increase their RPM to try to keep the temperature atfan-target-tempif possible and will get to their Max RPM when the temperature is equal or exceedsfan-full-speed-temp.  For devices with DC fans, as the internal measured temperatures exceedfan-target-temp, the fans will start spinning but at a higher minimum RPM by default. This may result in cooling the device to the point where the fans turn-off completely iffan-min-speed-percentis set to0%, while with the default value of12%fans will never go to a full stop therefore reducing the noise and On/Off peaks that may occur. The temperature then may slowly increase tofan-target-tempand the fans will turn on again. Currently, there is one exception. The S+RJ10 modules have a temperature threshold of 65C before they trigger the fans. Since it's a higher temperature threshold, the fans will start spinning at a higher initial speed to cool the device. All the above mentioned functionality is directly related to thefan-control-intervalparameter value as it will determine how often FAN controller monitors all sensor data and triggers changes in fan-control.
Note:All readings are approximate and may not be 100% precise. Their purpose is to ~inform users about possible/upcoming failures.