# Document Information
Title: SMS
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/62390313/SMS,

# Content
# Summary
It is possible to connect the GSM modem to the RouterOS device and use it to send and receive SMS messages. RouterOS lists such modem as a serial port that appears in the '/port print' listing. GSM standard defines AT commands for sending SMS messages and defines how messages should be encoded in these commands.'/tool sms send'uses standard GSM AT commands to send SMS.
```
/port print
```
```
'/tool sms send'
```
# Sending
```
/tool sms send
```
# Example
Sending command for ppp interface:
```
/tool sms send usb3 "20000000" \ message="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@# \$%^&*(){}[]\"'~"
```
For LTE interface use LTE interface name in the port field:
```
/tool sms send lte1 "20000000" \ message="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@# \$%^&*(){}[]\"'~"
```
Parameter | Description
-----------------------
port(string) | Name of port from/portthat GSM modem is attached to.
phone-number(string) | Recipient phone number. Allowed characters are "0123456789*# abc". If the first character is "+" then the phone number type is set tointernational, otherwise, it is set tounknown.
channel(integer) | Which modem channel to use for sending.
message(string) | Message contents. It is encoded using GSM 7 encoding (UCS2 currently is not supported), so the message length is limited to 160 characters (characters ^{}\[]~
smsc(string) |
type(string) | If set toclass-0, then send class 0 SMS message. It is displayed immediately and not stored in the phone.
sms-storage(string) | Select storage where to save received SMS (modem/sim)
status-report-request(yes | no; Default: yes) | Set "no" to not requesta confirmation message indicating whether a text message was successfully sent to the recipient.
```
/port
```
# USSD messages
USSD (Unstructured Supplementary Service Data) messages can be used to communicate with mobile network provider to receive additional information, enabling additional services or adding funds to prepaid cards. USSD messages can be processed by using AT commands (commands can differ or even may be blocked on some modems).
3G or GSM network modes must be activated to use this functionality, as it's not supported under LTE only mode (R11e-LTEmodem auto switches to 3G mode to send out USSD message).
PDU (Protocol Data Unit) message and its decrypted version are printed under LTE debug logging.
# Example
Check if LTE debug logging is active:
```
/system logging print
Flags: X - disabled, I - invalid, * - default
# TOPICS ACTION PREFIX
0 * info memory
1 * error memory
2 * warning memory
3 * critical echo
```
If there is no logging entry add it by running this command:
```
/system logging add topics=lte,!raw
/system logging print
Flags: X - disabled, I - invalid, * - default
# TOPICS ACTION PREFIX
0 * info memory
1 * error memory
2 * warning memory
3 * critical echo
4 lte,!raw memory
```
To receive account status from*245# ```
/interface lte at-chat lte1 input="AT+CUSD=1,\"*245# \",15"
output: OK
/log print
11:51:20 lte,async lte1: sent AT+CUSD=1,"*245# ",15
11:51:20 lte,async lte1: rcvd OK
11:51:23 lte,async,event +CUSD: 0,"EBB79B1E0685E9ECF4BADE9E03", 0
11:51:23 gsm,info USSD: konta atlikums
```
# Receiving
RouterOS also supports receiving of SMS messages, can execute scripts, and even respond to the sender.
Before the router can receive SMS, the relevant configuration is required in the/tool smsmenu. The following parameters are configurable:
```
/tool sms
```
Parameter | Description
-----------------------
allowed-number(string; Default: "") | The sender number that will be allowed to run commands, must specify the country code ie. +371XXXXXXX
channel(integer; Default:0) | Which modem channel to use for receiving.
keep-max-sms(integer; Default:0) | Maximum number of messages that will be saved. If you set this bigger than SIM supports, new messages will not be received. Replaced withauto-eraseparameter starting from RouterOS v6.44.6
auto-erase(yes | no; Default:no) | SIM storage size is read automatically. Whenauto-erase=nonew SMS will not be received if storage is full. Setauto-erase=yesto delete the oldest received SMS to free space for new ones automatically. Available starting from v6.44.6
port(string; Default: (unknown)) | Modem port (modem can be used only by one process "/port> print" )
receive-enabled(yes | no; Default:no) | Must be turned on to receive messages
secret(string; Default: "") | the secret password, mandatory
polling(yes | no; Default:no) | checking the modem for new SMS every 10s, instead of updating the inbox only after receiving the command from the modem. Available starting from v7.16
```
auto-erase
```
```
auto-erase=no
```
```
auto-erase=yes
```
Basic Example configuration to be able to view received messages:
```
/tool sms set receive-enabled=yes port=lte1
/tool/sms/print
status: running
receive-enabled: yes
port: lte1
channel: 0
secret:
allowed-number:
auto-erase: no
sim-pin:
last-ussd:
```
# Inbox
```
/tool sms inbox
```
If you have enabled the reader, you will see incoming messages in this submenu:
Read-only properties:
Property | Description
----------------------
phone(string) | Senders phone number.
message(string) | Message body
timestamp(time) | The time when the message was received. It is the time sent by the operator, not the router's local time.
type(string) | Message type
# Syntax
```
:cmd SECRET script NAME [[ VAR[=VAL] ] ... ]
```
```
/system script
```
Other things to remember:
# Examples
Wrong:
```
:cmd script mans_skripts
:cmd slepens script mans skripts
:cmd slepens script mans_skripts var=
:cmd slepens script mans_skripts var= a
:cmd slepens script mans_skripts var=a a
```
Right:
```
:cmd slepens script mans_skripts
:cmd slepens script "mans skripts"
:cmd slepens script mans_skripts var
:cmd slepens script mans_skripts var=a
:cmd slepens script mans_skripts var="a a"
```
# Debugging
/tool sms sendcommand is logging data that is written and read. It is logged with tagsgsm,debug,writeandgsm,debug,readFor more information seesystem logging.
```
/tool sms send
```
# Implementation details
AT+CMGSandAT+CMGFcommands are used. Port is acquired for the duration of the command and cannot be used concurrently by another RouterOS component. Message sending process can take a long time, it times out after a minute and after two seconds during the initial AT command exchange.