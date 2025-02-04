# Document Information
Title: LEDs
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/40992859/LEDs,

# Content
# Summary
Sub-menu:/system leds
```
/system leds
```
RouterOS allows configuring each LED's activity the way that the user wishes. It is possible to configure the LEDs to display wireless strength, blink the LEDs on interface traffic activity, and many other options.
For example, default led configuration on Groove
```
[admin@MikroTik] /system leds> print
Flags: X - disabled
# TYPE INTERFACE LEDS
0 wireless-signal-strength led1
led2
led3
led4
led5
1 interface-activity ether1 user-led
```
# Property Description
Property | Description
----------------------
disabled(yes | no; Default:no) | Whether an item is disabled
interface(string; Default: ) | Name of the interface which will be used for led status. Applicable only iftypeis interface specific.
modem-signal-treshold(integer [-113..-51]; Default: ) | Applicable if a type ismodem-signal
leds(list of leds; Default: ) | List of led names used for a status report. For example, wireless signal strength will require more than one led.
type(align-down | align-left | align-right | align-up | ap-cap | fan-fault | flash-access | interface-activity | interface-receive | interface-speed | interface-speed-1G | interface-speed-25G | interface-status | interface-transmit | modem-signal | modem-technology | off | on | poe-fault | poe-out | wireless-signal-strength | wireless-status; Default: ) | Type of the status:align-down- light the led if the w60g device needs to be aligned downwards for the best signal qualityalign-left- light the led if the w60g device needs to be aligned to the leftalign-right- light the led if the w60g device needs to be aligned to the rightalign-up- light the led if the w60g device needs to be aligned upwardsap-cap- blink on CAP initializing with CAPsMAN, steady on once connectedfan-fault- light the led when any of the devices controlled fans stop workingflash-access- blink the led on flash accessinterface-activity- blink the led on interface (traffic) activityinterface-receive- blink the led on interface received a trafficinterface-speed- light the led when interface works in 10Gbit rateinterface-speed-1G- light the led when interface works in 1Gbit rateinterface-speed-25G- light the led when interface works in 25Gbit rateinterface-speed-100G - light the led when interface works in 100Gbit rateinterface-status- light the led on interface status changeinterface-transmit- blink the led on interface transmitted trafficmodem-signal- blink the led on 3G modem signal (either USB or miniPCIe)modem-technology- turns on LEDs in order of modem technology generation: GSM; 3G; LTE; single led turns on only when LTE is active.off- turn off the ledon- turn on the ledpoe-fault- light the led when PoE out budget is close to the maximum supported limitpoe-out- light the led when interface PoE out turns onwireless-signal-strength- light the leds displaying wireless signal (requires more than one led)wireless-status- light the led on wireless status change.
# LED Settings
Global settings are stored in LEDs Setting menu.
Sub-menu:/system leds setting
```
/system leds setting
```
Property | Description
----------------------
all-leds-off(after-1h | after-1min | immediate | never; Default:never) | Whether and when all LEDs of a router can be turned off
The listed devices support turning off their LEDs (LED dark mode), however, some LEDs still cannot be turned off due to the device design factors.
# Indoor devices
RouterBoard | LED description
-----------------------------
CRS305-1G-4S+; CRS309-1G-8S+ | Turns off all LEDs except Ethernet LED and Power LED
RB5009UG+S+IN; RB5009UPr+S+ | Turns off all LEDs
L009UiGS-RM; L009UiGS-2HaxD-IN | Turns off PWR, USR and Ether1 LEDs
L41G-2axD; L41G-2axD&FG621-EA (hAP ax lite series) | Turns off all LEDs except Ethernet LEDs
RB760iGS (hEX S) | Turns off Power LED and SFP LED
E50UG | Turns off all LEDs except Ethernet1 LED
RB924i-2nD-BT5&BG77; RB924iR-2nD-BT5&BG77 (KNOT series) | Turns off all LEDs
RB951Ui-2HnD | Turns off all LEDs except Power LED
RB951Ui-2nD (hAP); RB952Ui-5ac2nD (hAP ac lite); RB952Ui-5ac2nD-TC (hAP ac lite TC) | Turns off all LEDs except Power LED
RB962UiGS-5HacT2HnT (hAP ac) | Turns off all LEDs except Port5 PoE LED
RBcAP2n; RBcAP2nD (cAP) | Turns off all LEDs
RBcAPGi-5acD2nD (cAP ac); RBcAPGi-5acD2nD-XL (cAP XL ac) | Turns off all LEDs
cAPGi-5HaxD2HaxD (cAP ax) | Turns off all LEDs
RBD25G/RB25GR-5HPacQD2HPnD (Audience) | Turns off all LEDs except Ethernet LEDs
RBD52G-5HacD2HnD-TC (hAP ac^2) | Turns off all LEDs
RBD53iG-5HacD2HnD (hAP ac^3) | Turns off all LEDs
RBD53G-5HacD2HnD-TC (Chateau series) | Turns off all LEDs
RBwsAP5Hac2nD (wsAP ac lite) | Turns off all LEDs
C52iG-5HaxD2HaxD-TC (hAP ax^2) | Turns off all LEDs except Ethernet LEDs
C53UiG+5HPaxD2HPaxD (hAP ax^3) | Turns off all LEDs except Ethernet LEDs
S53UG+5HaxD2HaxD-TC (Chateau ax series) | Turns off all LEDs except Ethernet LEDs
# Wireless Systems
RouterBoard | LED description
-----------------------------
CME22-2n-BG77 (CME Gateway) | Turns off all LEDs
CubeG-5ac60ay (Cube 60Pro ac); CubeG-5ac60ay-SA (CubeSA 60Pro ac) | Turns off all LEDs
CubeG-5ac60ad (Cube 60G ac) | Turns off all LEDs
RB912R-2nD-LTm (ltAP mini / ltAP mini LTE kit) | Turns off all LEDs
RB912UAG-6HPnD (BaseBox 6) | Turns off all LEDs
RBD23UGS-5HPacD2HnD (NetMetal ac^2) | Turns off all LEDs
L11UG-5HaxD; L11UG-5HaxD-NB (NetBox 5 ax) | Turns off all LEDs
L22UGS-5HaxD2HaxD-15S (mANTBox ax 15s) | Turns off all LEDs
L23UGSR-5HaxD2HaxD; L23UGSR-5HaxD2HaxD-NM (NetMetal ax) | Turns off all LEDs
RBLDF-2nD (LDF 2); RBLDF-5nD (LDF 5); RBLHGR | Turns off all LEDs
RBLDFG-5acD (LDF 5 ac) | Turns off all LEDs except Ethernet LED
RBLHG2nD (LHG 2); RBLHG2nD-XL (LHG XL 2) | Turns off all LEDs
RBLHG5nD (LHG 5); RBLHG5HPnD (LHG HP5); RBLHG5HPnD-XL (LHG XL HP5) | Turns off all LEDs
RBLHGG-5acD (LHG 5 ac); RBLHGG-5acD-XL (LHG XL 5 ac); RBLHGG-5HPacD2HPnD (LHG XL 52 ac); RBSXTsqG-5acD (SXTsq 5 ac) | Turns off all LEDs except Ethernet LED
RBLHGG-60ad (Wireless Wire Dish) | Turns off all LEDs
LHGGM&EG18-EA (LHG LTE18 kit); ATLGM&EG18-EA (ATL LTE18 kit) | Turns off all LEDs
RBLtAP-2HnD (LtAP) | Turns off all LEDs except Ethernet LEDs
RBSXTsq-60ad (SXTsq Lite60); RBCube-60ad (Cube Lite60) | Turns off all LEDs
RBwAPG-60ad (Wireless Wire) | Turns off all LEDs
RBwAPGR-5HacD2HnD (wAP ac) | Turns off all LEDs except Ethernet LED
# Examples
# Basic example
LED control via CLI commands for scripting purposes:
```
# add led entry with specific type "on" or "off" to leds menu
/system leds add leds=led1 type=off
# to control led
/system leds set [find where leds="led1"] type=on
or
/system leds set [find where leds="led1"] type=off
```
Enable the User ACT LED to show current CAP status on an RB951
```
/system leds
add leds=user-led type=ap-cap
```
# Modem Signal Strength example
The whole modem-signal strength range is [-113..-51] and the modem-signal-threshold increases the weakest signal limit to -91 so the signal range for LED indication is [-91..-51]. That range is divided into equal parts depending on number of LEDs configured for modem-signal LED trigger. The first LED turns on when signal is above -91 and the last LED turns on when signal reaches -51.
```
/system leds
add interface=lte1 leds=led1,led2,led3,led4,led5 modem-signal-treshold=-91 type=modem-signal
```
# Modem Access Technology example
These LED trigger examples turn on LEDs in order of modem technology generation: GSM; 3G; LTE.
```
/system leds add interface=lte1 leds=led1 modem-type=modem-technology
```
```
/system leds
add interface=lte1 leds=led1,led2 modem-type=modem-technology
```
```
/system leds add interface=lte1 leds=led1,led2,led3 modem-type=modem-technology
```