# Document Information
Title: GPIO
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/68944101/GPIO,

# Content
note: In order to access GPIO settings, make sure thatiotpackageis installed beforehand.
You can find more information about GPIO following thelink.
GPIO stands for General-Purpose Input/Output. It is a digital signal pin/pins on the routerboard that allows you to send/receive the signal. It can be useful in different scenarios, like:
# RouterOS configuration
note:GPIO settings are available only using CLI.
Sub-menu:/iot gpio
```
/iot gpio
```
GPIO settings are divided into:
note:in our examples, we are usingKNOTas a reference device. Other devices may have a different pinout but the same principles apply.
# /iot gpio analog
```
[admin@device] /iot gpio analog> print
# NAME                                                                                     VALUE       OFFSET
0 pin2                                                                                       0mV          0mV
1 pin3                                                                                      32mV          0mV
```
"OFFSET" can be used to manually compensate voltage drop on the wires. "VALUE" is measured with:
value = adc_input + offset
```
value = adc_input + offset
```
, where adc_input is the voltage on the pin.
"OFFSET" configuration example is shown below:
```
[admin@device] /iot gpio analog> set pin2 offset
Offset ::= [-]Num[mV]
Num ::= -2147483648..2147483647    (integer number)
[admin@device] /iot gpio analog> set pin2 offset 2
[admin@device] /iot gpio analog> print
# NAME                                                                                           VALUE       OFFSET
0 pin2                                                                                             2mV          2mV
1 pin3                                                                                             0mV          0mV
```
# /iot gpio digital
In the "digital" section you can send/receive a logical 0 or 1 signal using the digital output/input pins (output pins are "open drain"):
```
[admin@device] /iot gpio digital> print
Flags: X - disabled
# NAME                                        DIRECTION OUTPUT INPUT SCRIPT
0   pin5                                        input     0      0
1   pin4                                        output    0
2   pin6                                        output    0
```
"DIRECTION" for the pin can be either "input" (a pin that can receive the signal) or "output" (a pin that can send the signal).
When the pin's direction is set to "output", you can configure the "OUTPUT" value. Changing the "OUTPUT" value sends the signal to the pin.
```
[admin@device] /iot gpio digital> set pin4 output=
Output ::= 0 | 1
[admin@device] /iot gpio digital> set pin4 output=1
[admin@device] /iot gpio digital> print
Flags: X - disabled
# NAME                                        DIRECTION OUTPUT INPUT SCRIPT
0   pin5                                        input     0      0
1   pin4                                        output    1
2   pin6                                        output    0
```
The "SCRIPT" field allows you to configure a script, that will be initiated whenever the "INPUT" or "OUTPUT" value changes (from 0 to 1 or from 1 to 0).
```
[admin@device] /iot gpio digital> set pin4 script=script1
[admin@device] /iot gpio digital> set pin5 script="/system .."
[admin@device] /iot gpio digital> print
Flags: X - disabled
# NAME                                        DIRECTION OUTPUT INPUT SCRIPT
0   pin5                                        input     0      0     /system ..
1   pin4                                        output    1            script1
2   pin6                                        output    0
```
# Different scenarios
# Controlling relays
One of the scenarios for the GPIO implementation is "controlling other relays" using digital output pins. Basically, sending "0" or "1" signal to the unit that is connected to the pin. To automate the process, you can use ascheduler, which will run the script at specific times.
For example, you can add the firstscript(a single line shown below) and name it "output=0":
/iot gpio digital set pin4 output=0
Then add a second script (a single line shown below) and name it "output=1":
/iot gpio digital set pin4 output=1
Having both scripts, you can configure a schedule:
```
[admin@device] /system scheduler> add name=run-30s interval=30s on-event="output=0"
```
The schedule configuration shown above will run the script with the name "output=0", every 30 seconds.
```
[admin@device] /system scheduler> add name=run-45s interval=45s on-event="output=1"
```
The schedule configuration shown above will run the script with the name "output=1", every 45 seconds.
As a result, the device will automatically send a signal to the 4th pin (digital output pin) with output value=0 every 30 seconds and a signal with output value=1 every 45 seconds.
You can change the scheduled time as you see fit (depending on the requirements).
# Monitoring input signal
Another scenario is to "monitor input signal" using the digital input pins. You need a script that will initiate e-mail notification or MQTT/HTTPS (fetch) publish whenever the "INPUT" value changes for the pin with the direction="input" (whenever the RouterOS device receives a signal "0 or 1" from another device connected to the pin).
E-mail notification script:
After creating a script, apply/set it to the "input" pin:
```
[admin@device] /iot gpio digital> set pin5 script=script1
[admin@device] /iot gpio digital> print
Flags: X - disabled
# NAME                     DIRECTION OUTPUT INPUT SCRIPT
0   pin5                     input     0      0     script1
1   pin4                     output    0            script1
2   pin6                     output    0
```
In the example above, the e-mail notification script is named "script1".
As a result, whenever the input value changes (from 0 to 1 or from 1 to 0), the script automatically initiates an e-mail notification that will display the input value in the e-mail body.
Do not forget to change the script line and configure the e-mail settings (/tool e-mail) accordingly:
/tool e-mail send to="config@mydomain.com" subject="[/system identity get name]"  body="$[/iot gpio digital get pin5 input]"
Configure the actual e-mail address that you use. You can also change the subject and the body for the mail as you see fit.
MQTT publish script:
:local broker "name"
:local topic "topic"
:local message "{\"inputVALUE\":$[/iot gpio digital get pin5 input]}"/iot mqtt publish broker=$broker topic=$topic message=$message
This script works the same way as the "e-mail notification" script, only when the input value changes the script initiates MQTT publish (instead of e-mail notification) and sends the input value received on the pin in the JSON format.
Do not forget to set up MQTT broker (/iot mqtt brokers add ..) and alter a few script lines beforehand:
:local broker "name"
The broker's "name" should be changed accordingly (you can check all created brokers and their names using CLI command /iot mqtt brokers print).
:local topic "topic"
The topic should be changed as well. The topic itself is configured on the server-side, so make sure that the correct topic is used.
Do not forget to apply/set the script to pin5 (/iot gpio digital set pin5 script=script_name), as shown in the "email notification" example above.
If the mechanical switch is used to send the signal to the GPIO pin, it is suggested to use the following script instead (in case the script is initiated more than once when the signal is received on the pin):
If the GPIO pin state changes more than once within mili/microseconds - the script above is going to make sure that e-mail notification is not sent more than once.
# Monitoring voltage
Last but not least - is to "monitor voltage" using the analog pins.  You need a script that will read/monitor voltage on schedule and then send the data via e-mail, MQTT or HTTPS (fetch).
Create a script, as shown below. In this example, we will be using MQTT publish (but you can create a similar script with "/tool e-mail .." to use e-mail notifications):
:local broker "name"
:local topic "topic"
:local message "{\"voltage(mV)\":$[/iot gpio analog get pin3 value]}"/iot mqtt publish broker=$broker topic=$topic message=$message
The script will read/measure the voltage on pin3 and publish the data to the MQTT broker.
Do not forget to set up MQTT broker (/iot mqtt brokers add ..) and alter a few script lines beforehand:
:local broker "name"
The broker's "name" should be changed accordingly (you can check all created brokers and their names using CLI command /iot mqtt brokers print).
:local topic "topic"
The topic should be changed as well. The topic itself is configured on the server-side, so make sure that the correct topic is used.
Save the script and name it, for example, "voltagepublish". To automate the process, you can use thescheduler.
```
[admin@device] /system scheduler> add name=run-45s interval=45s on-event="voltagepublish"
```
The schedule configuration shown above will run the script every 45 seconds.