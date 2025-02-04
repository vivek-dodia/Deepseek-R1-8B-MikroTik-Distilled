# Document Information
Title: Bluetooth tag-tracking using MQTT and ThingsBoard
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/176914435/Bluetooth+tag-tracking+using+MQTT+and+ThingsBoard,

# Content
# Introduction
Bluetooth interface implementation in RouterOS allows the device to capture Bluetooth advertising packets that are broadcasted over 37, 38, and 39 advertising channels. More information can be found in theguide here.
Bluetooth tags like, for example,TG-BT5-INandTG-BT5-OUT, do exactly that. They broadcast advertising payloads over the mentioned channels. To understand what kind of information is stored in the payload, make sure to check thelink. The tags can be configured (using theMikroTik Beacon Managerapp) to broadcast the payloads automatically, with an interval or/and when a movement, tilt, or free-fall trigger is detected. In simple terms, the tag will "tell" (broadcast to) all the surrounding Bluetooth scanners (like theKNOT) information about itself periodically.
When the payload is broadcasted by the tag, and the tag is within the KNOT's Bluetooth operating range, the KNOT will capture and display the payload under its "scanner" Bluetooth interface section. It would look like this:
```
/iot bluetooth scanners advertisements print
Columns: DEVICE, PDU-TYPE, TIME, ADDRESS-TYPE, ADDRESS, RSSI, LENGTH, DATA
# DEVICE  PDU-TYPE        TIME                  ADDRESS-TYPE  ADDRESS            RSSI    LENGTH  DATA
0  bt1     adv-noconn-ind  mar/07/2023 12:11:57  public        DC:2C:6E:0F:C0:3D  -51dBm      22  15ff4f09010079100000ffff0000cf188a6b2b000064
1  bt1     adv-noconn-ind  mar/07/2023 12:11:58  public        2C:C8:1B:4B:BB:0A  -49dBm      22  15ff4f090100168dfefffffffeffa51ae1362200005e
```
The example above shows us, that the KNOT sees two Bluetooth tags within its operating range with MAC addresses "DC:2C:6E:0F:C0:3D" and "2C:C8:1B:4B:BB:0A", their respective payloads ("DATA" field) and the signal strength ("RSSI" field).
With the help of RouterOSscriptingandscheduling, we can make the KNOT automatically-periodically scan the payload list and, in case, a specific payload or a specific tag's MAC address is found on the list, we can make the KNOT structure an MQTT message (out of the printed information shown in the example above) and send it to the configured server viaMQTT,e-mailorHTTPpost. Script examples will be shown later on in the guide.
As the title suggests, the goal is to implement aBluetooth tag-tracking solutionand the idea is quite simple.When you have 2 KNOTs(KNOT-A and KNOT-B), running the same script on a scheduler,and the tag moves between their Bluetooth operating ranges, the data onthe server will indicatewhetherit wasKNOT-A or KNOT-Bthathave sentthetag'spayload. That will help you figure out the proximity of the tag. Whether the tag is broadcasting payloads in the KNOT-A zone, or in the KNOT-B zone.
You will need a server where the data is going to be stored and visualized. In this guide, we will showcase a server calledThingsBoardand how to communicate with it using the MQTT protocol.
ThingsBoard has a cloud solution and different local installation options (on different OS). Since we've added acontainerfeature, it became possible to also run the platform within RouterOS. In order to do that, you will need a RouterOS device that has at least2 GB RAM to spare or 1 GB RAM to spare with minimal load, has the option to increase storage (for example, an additional USB port), and is either ARM64 or AMD64architecture. Consider usingCHRmachine, as it could be a good fit.
# Setup requirements:
# Scenario explanation
Let's take a look at a basic example first. We have two KNOTs (KNOT-A and KNOT-B). We've tested Bluetooth ranges in our environment and could verify that both KNOTs are able to capture the tag at a 70-meter distance. If we install KNOT-A and KNOT-B 140 meters apart, their Bluetooth ranges will not overlap or overlap just slightly. When the tag moves into the KNOT-A range → the payload from the monitored tag will appear under the Bluetooth scanner list →  the script will be initiated on a set schedule → an MQTT message with a report is going to be sent to the server →  and, finally, the server will display that the tag is in the KNOT-A zone. When the tag moves into the KNOT-B range, the same happens, and the server will display that the tag is inside the KNOT-B zone.
The actual Bluetooth operating distance can vary from site to site because a lot of different factors can impact it, like 2.4 GHz interference or the surrounding materials used. For example, in line of sight, with no interference, the distance at which the KNOT is able to capture the tag's broadcasted payload, can be up to 180 meters (KNOT — ~180 meters — TG-BT5-OUT). But you also have to keep in mind that with further distance, more packets will be lost on the way. In the office environment, the range can go down to 30-100 meters.
Logically, if the Bluetooth operating ranges overlap and the tag is within the overlapped area (at the same time within KNOT-A and KNOT-B Bluetooth ranges), both KNOTs will send the data and the server is going to show that the tag is reported by both devices at the same time.
Surely, there will be zones where two or more KNOT's Bluetooth ranges overlap and you can use it to your advantage. Basically, you will have information that the tag, right now, is on the edges of the Bluetooth ranges in-between specific KNOT zones. In other words, when the asset moves into the overlapped area, you will have information on the server that the asset is somewhere between the two KNOT operating ranges, which is useful information to haveas it gives more precision.
Additionally,the tag's output power can be reduced usingTx powerparameter. Meaning, that even if the tag's payloads are broadcasted way too far and they are caught by other KNOTs that are not supposed to see those payloads (at longer distances) → you can reduce the output power of the tag, which will reduce the distance at which the KNOT is able to capture it. That way, you can "tweak" the "range" of reception and also avoid "interfering" with the signal in other zones.
The scripts we've prepared also allows you to set up a filter (that will be shown later on), which will make the KNOT ignore the payloads that the scanner captures unless the signal strength (RSSI) is stronger than the specified value. In the Bluetooth scanner example print shown above under the "Introduction" section, we can see that the KNOT sees one of the tags with anRSSIsignal strength of-51 dBm(tag with a MAC address "DC:2C:6E:0F:C0:3D") and the other one with anRSSIsignal strength of-49 dBm(tag with a MAC address "2C:C8:1B:4B:BB:0A"). So,if weapply a filter to the scripttoignoreall payloads that are received with signal strength (RSSI)weaker than -50 dBm, ourKNOT would report that only tag "2C:C8:1B:4B:BB:0A" is within the Bluetooth range, because its RSSI is -49 dBm, and the second tag (with RSSI -51 dBm) will be ignored. What this means, essentially, it is a second way of "tweaking" the "range" of reception. The actual signal strength will vary between different locations (as mentioned before, because of interference and surrounding materials), so it needs to be tested on sight.
# Example # 1
One of the use cases is shown in the topology below:
We have a warehouse area andwe have 3 assets(pallets) that we are interested in tracking.Wealsohave 3 zones: zoneA, where newly arrived pallets are stored; zoneB, where our assets are relocated to be inspected; and zoneC, where assets are moved after inspection. To achieve Bluetooth asset-tracking, just install x1 KNOT per zone and x1 tag per asset.
If TAG 1 and TAG 2 (pallets) arrive in the "arrival" zone A, KNOT A will report to the server that both assets are within its Bluetooth range. If TAG 3 gets moved to zone C, the server will indicate it is within the KNOT C range. If TAG 1 and TAG 2 move toward the B zone, and stay on the edges between A and B zones, the server will show that it is in the overlapped area (at the same time within KNOT-A and KNOT-B ranges). If the tags move to the middle of the warehouse, the server will indicate that they are in all 3 zones at once, in the overlapping area.
# Configuration
In this example, we will showcase a basic topology, when two KNOTs are used and we just want to know whether the tag is located in one part of the building or the other one (whether it is inside zone A or zone B).
# ThingsBoard preparation
Check the guide overhereto understand how the ThingsBoard and the RouterOS can be set up to utilize MQTT communication.
Create 2 KNOTs under the ThingsBoard GUI and make them "gateways".
Go to the "Devices" section, click on "+" button and "Add new device":
Name the device and checkbox the "Is gateway" option:
Do that for each KNOT that you have:
Set up a unique access token (unique credentials) for each KNOT under the device you've just created, under the "Manage credentials" tab:
# RouterOS configuration
# Preparation
Before we proceed, we need to confirm that our Bluetooth tag actually appears in the KNOT's Bluetooth range and that the KNOT detects them. To do that, you can issue the command "/iot bluetooth scanners advertisements print":
```
/iot bluetooth scanners advertisements print
```
```
/iot bluetooth scanners advertisements print
# DEVICE     PDU-TYPE        TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA
0 bt1        adv-noconn-ind  mar/08/2023 12:35:15 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f090100b0110100ffff00000019d68d2300005d
1 bt1        adv-noconn-ind  mar/08/2023 12:35:16 public       DC:2C:6E:0F:C0:3D        -39dBm         22 15ff4f0901008f3cfcfffbfffaff301783c22c000064
2 bt1        adv-noconn-ind  mar/08/2023 12:35:35 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f09010084d500000400ffff0319ea8d2300005d
3 bt1        adv-noconn-ind  mar/08/2023 12:35:45 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f090100e607faffffff03000319f48d2300005d
```
Or you can check it usingWebfigorWinboxunder the IoT>Bluetooth>Advertising reports tab.
The list can be chaotic. Random payloads can appear on the list as the scanner captures everything around it. To help reduce the list, you can filter it using the tag's MAC address "/iot bluetooth scanners advertisements print where address=DC:2C:6E:0F:C0:3D":
```
/iot bluetooth scanners advertisements print where address=DC:2C:6E:0F:C0:3D
```
```
/iot bluetooth scanners advertisements print where address=DC:2C:6E:0F:C0:3D
# DEVICE    PDU-TYPE        TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA
0 bt1       adv-noconn-ind  mar/08/2023 12:41:06 public       DC:2C:6E:0F:C0:3D        -49dBm         22 15ff4f0901005ab20100fdfffdff4017e1c32c000064
1 bt1       adv-noconn-ind  mar/08/2023 12:41:26 public       DC:2C:6E:0F:C0:3D        -40dBm         22 15ff4f090100349704000000fcff4017f5c32c000064
2 bt1       adv-noconn-ind  mar/08/2023 12:41:36 public       DC:2C:6E:0F:C0:3D        -49dBm         22 15ff4f09010073fb0000000000003017ffc32c000064
3 bt1       adv-noconn-ind  mar/08/2023 12:41:46 public       DC:2C:6E:0F:C0:3D        -43dBm         22 15ff4f090100b88cffffffffffff401709c42c000064
```
To figure out how to decypher the payload, please check the guidehere.
# MQTT broker
On each KNOT setup MQTT broker.
For KNOT A:
```
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=1883 username=knot-A_access_token
```
Where:
```
name
```
```
address
```
```
port
```
```
username
```
For KNOT B → Do the same step. Just changeusernameto the respective access token that was generated for the KNOT B device (gateway).
```
username
```
# Script
Import the script shown below to each KNOT. To do that, just copy the below shown "code" and paste it into a new terminal window and press "ENTER":
```
/system script add dont-require-permissions=no name=tracking owner=admin policy=\
ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="# Requ\
ired packages: iot\r\
\n\r\
\n# Configuration # \
# \r\
\n# Name of an existing MQTT broker that should be used for publishing\r\
\n:local broker \"tb\"\r\
\n\r\
\n# MQTT topic where the message should be published\r\
\n:local topic \"v1/gateway/telemetry\"\r\
\n\r\
\n# POSIX regex for filtering advertisement Bluetooth addresses. E.g. \"^BC:33:\
AC\"\r\
\n# would only include addresses which start with those 3 octets.\r\
\n# To disable this filter, set it to \"\"\r\
\n:local addressRegex \"\"\r\
\n\r\
\n# POSIX regex for filtering Bluetooth advertisements based on their data. Sam\
e\r\
\n# usage as with 'addressRegex'.\r\
\n:local advertisingDataRegex \"\"\r\
\n\r\
\n# Signal strength filter. E.g. -40 would only include Bluetooth advertisement\
s\r\
\n# whose signal strength is stronger than -40dBm.\r\
\n# To disable this filter, set it to \"\"\r\
\n:local rssiThreshold \"\"\r\
\n\r\
\n# Name the KNOT. Identity of the unit that will be senting the message. This n\
ame will be reported to the MQTT broker.\r\
\n:local gwName \"KNOT_A\"\r\
\n\r\
\n# Bluetooth # \
# \r\
\n:put (\"[*] Gathering Bluetooth info...\")\r\
\n\r\
\n:global makeRecord do={\r\
\n    :local jsonStr \"{\\\"ts\\\":\$ts,\\\"values\\\":{\\\"reporter\\\":\\\"\$\
gwName\\\",\\\"rssi\\\":\$rssi}}\"\r\
\n    :return \$jsonStr\r\
\n}   \r\
\n\r\
\n# array of record strings collected for each advertising MAC address\r\
\n:global macRecords [:toarray \"\"]\r\
\n\r\
\n# process advertisements and update macRecords\r\
\n:local advertisements [/iot bluetooth scanners advertisements print detail as\
-value where \\\r\
\naddress ~ \$addressRegex and \\\r\
\ndata ~ \$advertisingDataRegex and \\\r\
\nrssi > \$rssiThreshold]\r\
\n\r\
\n/iot/bluetooth/scanners/advertisements clear\r\
\n\r\
\n:foreach adv in=\$advertisements do={\r\
\n:local address (\$adv->\"address\")\r\
\n:local rssi (\$adv->\"rssi\")\r\
\n:local epoch (\$adv->\"epoch\")\r\
\n                \r\
\n:local recordStr [\$makeRecord ts=\$epoch gwName=\$gwName rssi=\$rssi]\r\
\n\r\
\n:if ([:len (\$macRecords->\$address)] > 0) do={\r\
\n:local str (\$macRecords->\$address)\r\
\n:local newStr \"\$str,\$recordStr\"\r\
\n:set (\$macRecords->\$address) \$newStr} else={:set (\$macRecords->\$address)\
\_\$recordStr}}\r\
\n\r\
\n# TODO: add some logic to decide when we want to send data\r\
\n:local sendData true\r\
\n\r\
\n:if (\$sendData) do={\r\
\n:local jsonStr \"{\"\r\
\n\r\
\n:foreach addr,advRec in=\$macRecords do={\r\
\n:set jsonStr \"\$jsonStr\\\"\$addr\\\":[\$advRec],\"}\r\
\n\r\
\n:local payloadlength\r\
\n:set payloadlength [:len (\$jsonStr)]\r\
\n:local remcom\r\
\n:set remcom [:pick \$jsonStr 0 (\$payloadlength-1)]\r\
\n:set jsonStr \"\$remcom}\"\r\
\n:local message\r\
\n:set message \"\$jsonStr\"\r\
\n:log info \"\$message\";\r\
\n:put (\"[*] Message structured: \$message\")\r\
\n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
\n:put (\"[*] Sending message to MQTT broker...\")\r\
\n/iot mqtt publish broker=\"\$broker\" topic=\"\$topic\" message=\$message}"
```
The script should appear under the "System>Scripts>Script List" tab with the name "tracking" or with the help of the command "/system script print".
```
/system script print
```
There are certain script lines that you need to pay attention to.
Broker name configuration line, where you need to input the MQTT broker name that you have set:
:local broker "tb"
You need to input a correct topic, used by the MQTT broker. CheckThingsBoard documentationfor more details and, by default, the topic should be:
:local topic "v1/gateway/telemetry"
MAC address filtering option inside the script itself. You can type in all 6 octets of the MAC address (to apply the filter to 1 specific tag), or you can filter the list using a few/couple of octets, like "^BC:33:AC" (to apply the filter, so that only MAC addresses that begin with "BC:33:AC:..." would be processed):
:local addressRegex "DC:2C:6E:0F:C0:3D"
Payload content/data line. Allows you to filter the list, per specific payload content, like "manufacturer data". For example, "15ff4f09" would discard all payloads that are not MikroTik format payloads:
:local advertisingDataRegex "15ff4f09"
RSSI signal strength filtering option. This filtering option was mentioned in the "Scenario explanation" section. This filter allows you to ignore any payload that has RSSI weaker than the configured value. For example. "-40" would only include Bluetooth advertisements that have signal strength stronger than -40dBm:
:local rssiThreshold "-40"
KNOT identifier line. You will need to change it for each unique KNOT. For example, name your first KNOT →  KNOT_A and your second KNOT →  KNOT_B:
The rest of the script does not need to be changed/altered
How does the script work when you run it? The script "inspects" the "Advertising reports" tab (payload list tab) using the filters applied and structures a JSON message. An example of the JSON message would be:
```
{
"2C:C8:1B:4B:BB:0A": [
{
"ts": 1678967250600,
"values": {
"reporter": "KNOT_A",
"rssi": -47
}
}
],
"DC:2C:6E:0F:C0:3D": [
{
"ts": 1678967247850,
"values": {
"reporter": "KNOT_A",
"rssi": -59
}
},
{
"ts": 1678967257849,
"values": {
"reporter": "KNOT_A",
"rssi": -67
}
}
]
}
```
The data is structured per theThingsBoard guide, where "2C:C8:1B:4B:BB:0A" and "DC:2C:6E:0F:C0:3D" are MAC addresses of tags that appeared in the KNOT's range, "ts" is unix timestamp of each payload broadcasted by the tag in milliseconds, "reporter" indicates which specific KNOT has sent the message and "rssi" is the signal strength of each payload broadcasted by the tag in dBm.
```
2C:C8:1B:4B:BB:0A
```
```
DC:2C:6E:0F:C0:3D
```
```
ts
```
```
reporter
```
```
rssi
```
After the payload list is "searched" and the JSON message is structured, the Bluetooth interface payload list gets "cleaned" (or "flashed"), and the previously structured JSON message is sent to the ThingsBoard MQTT broker.
To run the script, use the command:
```
/system script run tracking
```
# Scheduler
Apply a scheduler to the script, so that RouterOS periodically initiates the script by itself:
```
/system/scheduler/add name=bluetoothscheduler interval=30s on-event="/system/script/run tracking"
```
You can set up shorter and longer intervals. If you want to send data more often, so that the data is "fresher" →  set up shorter time intervals (10-15 seconds). If you want to send fewer messages, less often → you can set up longer time intervals (30min+).
The JSON message structured using the script has a "ts" value (timestamp) assigned for each payload received. Meaning thatwhen the script is run, for example,every minute, 1 tag is used andthe tag broadcasts1 payload every 10 seconds (that is6 payloads per minute) → ThingsBoard data (GUI) will be updated every minute, and every minute, 6 new entries will appear (each entry will indicate that it was received 10 seconds after the previous one). And if you send the message every 15 minutes when using 1 tag that is broadcasting a payload every 10 seconds (that is 6*15=90 payloads per 15 minutes) → ThingsBoard data (GUI) will be updated every 15 minutes but 90 entries will appear.
```
ts
```
# ThingsBoard data visualization and result verification
After you run the script with/system script run trackingor via a scheduler and refresh the GUI portal → all MAC addresses (tags) that are found in the JSON message, will be made into new devices under the ThingsBoard GUI:
```
/system script run tracking
```
To help you visualize the data, you can use the built-inwidgetsor create your own one.
Select the tag's MAC address from the list of devices, go to the "Latest telemetry" section, checkbox the "reporter" parameter, and click on the "Show on widget" button:
Select a widget that you wish to use, for example under the "Cards" bundle, "Timeseries table" and click on "Add to dashboard":
Create a new dashboard and name it, however, you like. Click on "Add":
Do the same steps for your other tags that appeared under the "Devices" tab. Create a new widget for each unique tag under the same dashboard.
Change the widget's "Timewindow" from "Realtime-last minute" (which is used by default) to "Realtime-current day":
As a result, if both tags are inside theKNOT Arange, the dashboard would show:
If they move to theKNOT B range, it would show:
If the tags move to theoverlapped area, inside both ranges, both reporters (KNOT_A and KNOT_B) should show up within a few seconds after each other, depending on the interval used in the scheduler:
# Example # 2
In the second example, we will showcase another topology:
We have a few warehouses, a few company delivery vehicles, and 3 assets that we are interested in tracking. Our assets are pallets that hold cargo and our goals are to know:
To achieve Bluetooth asset-tracking, just install x1 KNOT per warehouse, x1 KNOT per vehicle, and x1 tag per asset.
We can see that TAG 1 is inside the vehicle, and this vehicle just parked near the warehouse. Both KNOT 1 and KNOT 4 will report to the server that the asset is inside their ranges. This will tell you that the asset is parked but not being transported yet.
We can see that TAG 2 is traveling between the warehouses and is only inside the KNOT 5 Bluetooth range. In this case, KNOT 5 will be the only reporter and the result that is displayed on the server would mean that the asset is getting transported.
We can see that TAG 3 is inside the warehouse. The server will indicate just that.
The data on the server will show the timestamps of each report sent by the KNOT, which will tell you for how long did the asset stay inside the specific device's Bluetooth range.
# Configuration
In this example, we will showcase a basic topology with 2 warehouses, 1 vehicle/truck traveling between them, and 1 asset/pallet/tag.
# ThingsBoard preparation
Check the guide overhereto understand how the ThingsBoard and the RouterOS can be set up to utilize MQTT communication.
Create 3 KNOTs under the ThingsBoard GUI and make them "gateways".
Go to the "Devices" section, click on "+" button and "Add new device":
Name the device and checkbox the "Is gateway" option:
Do that for each KNOT that you have:
Set up a unique access token (unique credentials) for each KNOT under the device you've just created, under the "Manage credentials" tab:
# RouterOS configuration
# Preparation
Before we proceed, we need to confirm that our Bluetooth tag actually appears in the KNOT's Bluetooth range and that the KNOT detects them. To do that, you can issue the command "/iot bluetooth scanners advertisements print":
```
/iot bluetooth scanners advertisements print
```
```
/iot bluetooth scanners advertisements print
# DEVICE     PDU-TYPE        TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA
0 bt1        adv-noconn-ind  mar/08/2023 12:35:15 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f090100b0110100ffff00000019d68d2300005d
1 bt1        adv-noconn-ind  mar/08/2023 12:35:16 public       DC:2C:6E:0F:C0:3D        -39dBm         22 15ff4f0901008f3cfcfffbfffaff301783c22c000064
2 bt1        adv-noconn-ind  mar/08/2023 12:35:35 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f09010084d500000400ffff0319ea8d2300005d
3 bt1        adv-noconn-ind  mar/08/2023 12:35:45 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f090100e607faffffff03000319f48d2300005d
```
Or you can check it usingWebfigorWinboxunder the IoT>Bluetooth>Advertising reports tab.
The list can be chaotic. Random payloads can appear on the list as the scanner captures everything around it. To help reduce the list, you can filter it using the tag's MAC address "/iot bluetooth scanners advertisements print where address=DC:2C:6E:0F:C0:3D":
```
/iot bluetooth scanners advertisements print where address=DC:2C:6E:0F:C0:3D
```
```
/iot bluetooth scanners advertisements print where address=DC:2C:6E:0F:C0:3D
# DEVICE    PDU-TYPE        TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA
0 bt1       adv-noconn-ind  mar/08/2023 12:41:06 public       DC:2C:6E:0F:C0:3D        -49dBm         22 15ff4f0901005ab20100fdfffdff4017e1c32c000064
1 bt1       adv-noconn-ind  mar/08/2023 12:41:26 public       DC:2C:6E:0F:C0:3D        -40dBm         22 15ff4f090100349704000000fcff4017f5c32c000064
2 bt1       adv-noconn-ind  mar/08/2023 12:41:36 public       DC:2C:6E:0F:C0:3D        -49dBm         22 15ff4f09010073fb0000000000003017ffc32c000064
3 bt1       adv-noconn-ind  mar/08/2023 12:41:46 public       DC:2C:6E:0F:C0:3D        -43dBm         22 15ff4f090100b88cffffffffffff401709c42c000064
```
To figure out how to decypher the payload, please check the guidehere.
# MQTT broker
On each KNOT setup MQTT broker.
For KNOT_1:
```
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=1883 username=knot-1_access_token
```
Where:
```
name
```
```
address
```
```
port
```
```
username
```
For KNOT_2 and KNOT_3 → Do the same steps. Just changeusernameto the respective access token that was generated.
```
username
```
# Script
Import the script shown below to each KNOT. To do that, just copy the below shown "code" and paste it into a new terminal window and press "ENTER":
```
/system script add dont-require-permissions=no name=tracking owner=admin policy=\
ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="# Required package\
s: iot\r\
\n\r\
\n# Configuration # \r\
\n# Name of an existing MQTT broker that should be used for publishing\r\
\n:local broker \"tb\"\r\
\n\r\
\n# MQTT topic where the message should be published\r\
\n:local topic \"v1/gateway/telemetry\"\r\
\n\r\
\n# POSIX regex for filtering advertisement Bluetooth addresses. E.g. \"^BC:33:AC\"\r\
\n# would only include addresses which start with those 3 octets.\r\
\n# To disable this filter, set it to \"\"\r\
\n:local addressRegex \"\"\r\
\n\r\
\n# POSIX regex for filtering Bluetooth advertisements based on their data. Same\r\
\n# usage as with 'addressRegex'.\r\
\n:local advertisingDataRegex \"\"\r\
\n\r\
\n# Signal strength filter. E.g. -40 would only include Bluetooth advertisements\r\
\n# whose signal strength is stronger than -40dBm.\r\
\n# To disable this filter, set it to \"\"\r\
\n:local rssiThreshold \"\"\r\
\n\r\
\n# Name the KNOT. Identity of the unit that will be senting the message. This name will be \
reported to the MQTT broker.\r\
\n:local gwName \"1\"\r\
\n\r\
\n# Bluetooth # \r\
\n:put (\"[*] Gathering Bluetooth info...\")\r\
\n\r\
\n:global makeRecord do={\r\
\n    :local jsonStr \"{\\\"ts\\\":\$ts,\\\"values\\\":{\\\"KNOT_\$gwName\\\":\\\"\$gwName\
\\\",\\\"rssi\\\":\$rssi}}\"\r\
\n    :return \$jsonStr\r\
\n}   \r\
\n\r\
\n# array of record strings collected for each advertising MAC address\r\
\n:global macRecords [:toarray \"\"]\r\
\n\r\
\n# process advertisements and update macRecords\r\
\n:local advertisements [/iot bluetooth scanners advertisements print detail as-value where\
\_\\\r\
\naddress ~ \$addressRegex and \\\r\
\ndata ~ \$advertisingDataRegex and \\\r\
\nrssi > \$rssiThreshold]\r\
\n\r\
\n/iot/bluetooth/scanners/advertisements clear\r\
\n\r\
\n:foreach adv in=\$advertisements do={\r\
\n:local address (\$adv->\"address\")\r\
\n:local rssi (\$adv->\"rssi\")\r\
\n:local epoch (\$adv->\"epoch\")\r\
\n                \r\
\n:local recordStr [\$makeRecord ts=\$epoch gwName=\$gwName rssi=\$rssi]\r\
\n\r\
\n:if ([:len (\$macRecords->\$address)] > 0) do={\r\
\n:local str (\$macRecords->\$address)\r\
\n:local newStr \"\$str,\$recordStr\"\r\
\n:set (\$macRecords->\$address) \$newStr} else={:set (\$macRecords->\$address) \$recordStr\
}}\r\
\n\r\
\n# TODO: add some logic to decide when we want to send data\r\
\n:local sendData true\r\
\n\r\
\n:if (\$sendData) do={\r\
\n:local jsonStr \"{\"\r\
\n\r\
\n:foreach addr,advRec in=\$macRecords do={\r\
\n:set jsonStr \"\$jsonStr\\\"\$addr\\\":[\$advRec],\"}\r\
\n\r\
\n:local payloadlength\r\
\n:set payloadlength [:len (\$jsonStr)]\r\
\n:local remcom\r\
\n:set remcom [:pick \$jsonStr 0 (\$payloadlength-1)]\r\
\n:set jsonStr \"\$remcom}\"\r\
\n:local message\r\
\n:set message \"\$jsonStr\"\r\
\n:log info \"\$message\";\r\
\n:put (\"[*] Message structured: \$message\")\r\
\n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
\n:put (\"[*] Sending message to MQTT broker...\")\r\
\n/iot mqtt publish broker=\"\$broker\" topic=\"\$topic\" message=\$message}"
```
The script should appear under the "System>Scripts>Script List" tab with the name "tracking" or with the help of the command "/system script print".
```
/system script print
```
There are certain script lines that you need to pay attention to.
Broker name configuration line, where you need to input the MQTT broker name that you have set:
:local broker "tb"
You need to input a correct topic, used by the MQTT broker. CheckThingsBoard documentationfor more details and, by default, the topic should be:
:local topic "v1/gateway/telemetry"
MAC address filtering option inside the script itself. You can type in all 6 octets of the MAC address (to apply the filter to 1 specific tag), or you can filter the list using a few/couple of octets, like "^BC:33:AC" (to apply the filter, so that only MAC addresses that begin with "BC:33:AC:..." would be processed):
:local addressRegex "DC:2C:6E:0F:C0:3D"
Payload content/data line. Allows you to filter the list, per specific payload content, like "manufacturer data". For example, "15ff4f09" would discard all payloads that are not MikroTik format payloads:
:local advertisingDataRegex "15ff4f09"
RSSI signal strength filtering option. This filtering option was mentioned in the "Scenario explanation" section. This filter allows you to ignore any payload that has RSSI weaker than the configured value. For example. "-40" would only include Bluetooth advertisements that have signal strength stronger than -40dBm:
:local rssiThreshold "-40"
KNOT identifier line. You will need to change it for each unique KNOT. For example, ID your first KNOT as "1", your second KNOT as "2" and your third KNOT as "3":
The rest of the script does not need to be changed/altered
How does the script work when you run it? The script "inspects" the "Advertising reports" tab (payload list tab) using the filters applied and structures a JSON message. An example of the JSON message would be:
```
{
"2C:C8:1B:4B:BB:0A": [
{
"ts": 1680526087729,
"values": {
"KNOT_1": "1",
"rssi": -47
}
}
],
"DC:2C:6E:0F:C0:3D": [
{
"ts": 1680526065000,
"values": {
"KNOT_1": "1",
"rssi": -49
}
},
{
"ts": 1680526075001,
"values": {
"KNOT_1": "1",
"rssi": -50
}
}
]
}
```
The data is structured per theThingsBoard guide, where "2C:C8:1B:4B:BB:0A" and "DC:2C:6E:0F:C0:3D" are MAC addresses of tags that appeared in the KNOT's range, "ts" is unix timestamp of each payload broadcasted by the tag in milliseconds, "KNOT_X" indicates which specific KNOT has sent the message and "rssi" is the signal strength of each payload broadcasted by the tag in dBm.
```
2C:C8:1B:4B:BB:0A
```
```
DC:2C:6E:0F:C0:3D
```
```
ts
```
```
KNOT_X
```
```
rssi
```
After the payload list is "searched" and the JSON message is structured, the Bluetooth interface payload list gets "cleaned" (or "flashed"), and the previously structured JSON message is sent to the ThingsBoard MQTT broker.
To run the script, use the command:
```
/system script run tracking
```
# Script that includes temperature data (optional)
In case you wish to add temperature reports to the structured message, use the script below:
```
/system script add dont-require-permissions=no name=tracking+temp owner=admin policy=\
ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="# Required package\
s: iot\r\
\n\r\
\n# Configuration # \r\
\n# Name of an existing MQTT broker that should be used for publishing\r\
\n:local broker \"tb\"\r\
\n\r\
\n# MQTT topic where the message should be published\r\
\n:local topic \"v1/gateway/telemetry\"\r\
\n\r\
\n# POSIX regex for filtering advertisement Bluetooth addresses. E.g. \"^BC:33:AC\"\r\
\n# would only include addresses which start with those 3 octets.\r\
\n# To disable this filter, set it to \"\"\r\
\n:local addressRegex \"\"\r\
\n\r\
\n# POSIX regex for filtering Bluetooth advertisements based on their data. Same\r\
\n# usage as with 'addressRegex'.\r\
\n:local advertisingDataRegex \"\"\r\
\n\r\
\n# Signal strength filter. E.g. -40 would only include Bluetooth advertisements\r\
\n# whose signal strength is stronger than -40dBm.\r\
\n# To disable this filter, set it to \"\"\r\
\n:local rssiThreshold \"\"\r\
\n\r\
\n# Name the KNOT. Identity of the unit that will be senting the message. This name will be \
reported to the MQTT broker.\r\
\n:local gwName \"1\"\r\
\n\r\
\n# Bluetooth # \r\
\n:global invertU16 do={\r\
\n    :local inverted 0\r\
\n    :for idx from=0 to=15 step=1 do={\r\
\n        :local mask (1 << \$idx)\r\
\n        :if (\$1 & \$mask = 0) do={\r\
\n            :set \$inverted (\$inverted | \$mask)\r\
\n        }\r\
\n    }\r\
\n    return \$inverted\r\
\n}\r\
\n\r\
\n:global le16ToHost do={\r\
\n    :local lsb [:pick \$1 0 2]\r\
\n    :local msb [:pick \$1 2 4]\r\
\n\r\
\n    :return [:tonum \"0x\$msb\$lsb\"]\r\
\n}\r\
\n:local from88 do={\r\
\n    :global invertU16\r\
\n    :global le16ToHost\r\
\n    :local num [\$le16ToHost \$1]\r\
\n\r\
\n    # Handle negative numbers\r\
\n    :if (\$num & 0x8000) do={\r\
\n        :set num (-1 * ([\$invertU16 \$num] + 1))\r\
\n    }\r\
\n\r\
\n    # Convert from 8.8. Scale by 1000 since floating point is not supported\r\
\n    :return ((\$num * 125) / 32)\r\
\n}\r\
\n:put (\"[*] Gathering Bluetooth info...\")\r\
\n\r\
\n:global makeRecord do={\r\
\n    :local jsonStr \"{\\\"ts\\\":\$ts,\\\"values\\\":{\\\"KNOT_\$gwName\\\":\\\"\$gwName\
\\\",\\\"temp\\\":\$temp}}\"\r\
\n    :return \$jsonStr\r\
\n}   \r\
\n\r\
\n# array of record strings collected for each advertising MAC address\r\
\n:global macRecords [:toarray \"\"]\r\
\n\r\
\n# process advertisements and update macRecords\r\
\n:local advertisements [/iot bluetooth scanners advertisements print detail as-value where\
\_\\\r\
\naddress ~ \$addressRegex and \\\r\
\ndata ~ \$advertisingDataRegex and \\\r\
\nrssi > \$rssiThreshold]\r\
\n\r\
\n/iot/bluetooth/scanners/advertisements clear\r\
\n\r\
\n:foreach adv in=\$advertisements do={\r\
\n:local address (\$adv->\"address\")\r\
\n:local ad (\$adv->\"data\")\r\
\n:local rssi (\$adv->\"rssi\")\r\
\n:local epoch (\$adv->\"epoch\")\r\
\n:local temp [\$from88 [:pick \$ad 28 32]]\r\
\n                \r\
\n:local recordStr [\$makeRecord ts=\$epoch gwName=\$gwName temp=\$temp]\r\
\n\r\
\n:if ([:len (\$macRecords->\$address)] > 0) do={\r\
\n:local str (\$macRecords->\$address)\r\
\n:local newStr \"\$str,\$recordStr\"\r\
\n:set (\$macRecords->\$address) \$newStr} else={:set (\$macRecords->\$address) \$recordStr\
}}\r\
\n\r\
\n# TODO: add some logic to decide when we want to send data\r\
\n:local sendData true\r\
\n\r\
\n:if (\$sendData) do={\r\
\n:local jsonStr \"{\"\r\
\n\r\
\n:foreach addr,advRec in=\$macRecords do={\r\
\n:set jsonStr \"\$jsonStr\\\"\$addr\\\":[\$advRec],\"}\r\
\n\r\
\n:local payloadlength\r\
\n:set payloadlength [:len (\$jsonStr)]\r\
\n:local remcom\r\
\n:set remcom [:pick \$jsonStr 0 (\$payloadlength-1)]\r\
\n:set jsonStr \"\$remcom}\"\r\
\n:local message\r\
\n:set message \"\$jsonStr\"\r\
\n:log info \"\$message\";\r\
\n:put (\"[*] Message structured: \$message\")\r\
\n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
\n:put (\"[*] Sending message to MQTT broker...\")\r\
\n/iot mqtt publish broker=\"\$broker\" topic=\"\$topic\" message=\$message}"
```
In this case, the JSON message would look like this:
```
{
"2C:C8:1B:4B:BB:0A": [
{
"ts": 1680527467840,
"values": {
"KNOT_1": "1",
"temp": 26460
}
}
],
"DC:2C:6E:0F:C0:3D": [
{
"ts": 1680527464996,
"values": {
"KNOT_1": "1",
"temp": 24750
}
},
{
"ts": 1680527474996,
"values": {
"KNOT_1": "1",
"temp": 24750
}
}
]
}
```
# Script that includes GPS data (optional)
In case you also wish to include GPS data (longitude and latitude values from the KNOTs), use the script shown below:
```
/system script add dont-require-permissions=no name=tracking+gps+temp owner=admin policy=\
ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="# Required package\
s: iot\r\
\n\r\
\n# Configuration # \r\
\n# Name of an existing MQTT broker that should be used for publishing\r\
\n:local broker \"tb\"\r\
\n\r\
\n# MQTT topic where the message should be published\r\
\n:local topic \"v1/gateway/telemetry\"\r\
\n:local gwtopic \"v1/devices/me/telemetry\"\r\
\n\r\
\n# POSIX regex for filtering advertisement Bluetooth addresses. E.g. \"^BC:33:AC\"\r\
\n# would only include addresses which start with those 3 octets.\r\
\n# To disable this filter, set it to \"\"\r\
\n:local addressRegex \"\"\r\
\n\r\
\n# POSIX regex for filtering Bluetooth advertisements based on their data. Same\r\
\n# usage as with 'addressRegex'.\r\
\n:local advertisingDataRegex \"15ff\"\r\
\n\r\
\n# Signal strength filter. E.g. -40 would only include Bluetooth advertisements\r\
\n# whose signal strength is stronger than -40dBm.\r\
\n# To disable this filter, set it to \"\"\r\
\n:local rssiThreshold \"\"\r\
\n\r\
\n# Name the KNOT. Identity of the unit that will be senting the message. This name will be \
reported to the MQTT broker.\r\
\n:local gwName \"2\"\r\
\n\r\
\n# GPS# \r\
\n:global lat\r\
\n:global lon\r\
\n\r\
\n/interface ppp-client set ppp-out1 disabled=yes\r\
\n:log info (\"disabling WWAN to get GPS coordinates\")\r\
\n\r\
\n/interface ppp-client at-chat ppp-out1 input=\"AT+QGPSCFG=\\\"priority\\\",0\"\r\
\n:log info (\"enabling priority for GPS\")\r\
\n\r\
\n# the time in the delay below is the time that the device will wait for to get the coord\
inate fix\r\
\n:delay 32000ms\r\
\n:log info (\"reading GPS coordinates\")\r\
\n/system gps monitor once do={\r\
\n:set \$lat \$(\"latitude\")\r\
\n:set \$lon \$(\"longitude\")\r\
\n}\r\
\n:if (\$lat != \"none\") do={\\\r\
\n:log info (\"enabling priority back to WWAN\")\r\
\n/interface ppp-client at-chat ppp-out1 input=\"AT+QGPSCFG=\\\"priority\\\",1\"\r\
\n:log info (\"enabling WWAN\")\r\
\n/interface ppp-client set ppp-out1 disabled=no\r\
\n:delay 1000ms\r\
\n# if dial on demand is enabled\r\
\n/ping 1.1.1.1 count=1\r\
\n\r\
\n# the delay below waits for 5 seconds for the ppp connection to get established - this tim\
e can differ based on the signal strength\r\
\n:delay 5000ms\r\
\n:log info (\"posting coordinates via mqtt\")\r\
\n:local gpsmessage \\\r\
\n    \"{\\\"latitude\\\":\$lat,\\\r\
\n    \\\"longitude\\\":\$lon}\"\r\
\n/iot mqtt publish broker=\$broker topic=\$gwtopic message=\$gpsmessage} else={\\\r\
\n:log info (\"could not read GPS coordinates...enabling back WWAN\")\r\
\n/interface ppp-client at-chat ppp-out1 input=\"AT+QGPSCFG=\\\"priority\\\",1\"\r\
\n/interface ppp-client set ppp-out1 disabled=no\r\
\n:delay 1000ms\r\
\n# if dial on demand is enabled\r\
\n/ping 1.1.1.1 count=1\r\
\n:delay 5000ms\r\
\n}\r\
\n\r\
\n# Bluetooth# \r\
\n:global invertU16 do={\r\
\n    :local inverted 0\r\
\n    :for idx from=0 to=15 step=1 do={\r\
\n        :local mask (1 << \$idx)\r\
\n        :if (\$1 & \$mask = 0) do={\r\
\n            :set \$inverted (\$inverted | \$mask)\r\
\n        }\r\
\n    }\r\
\n    return \$inverted\r\
\n}\r\
\n\r\
\n:global le16ToHost do={\r\
\n    :local lsb [:pick \$1 0 2]\r\
\n    :local msb [:pick \$1 2 4]\r\
\n\r\
\n    :return [:tonum \"0x\$msb\$lsb\"]\r\
\n}\r\
\n:local from88 do={\r\
\n    :global invertU16\r\
\n    :global le16ToHost\r\
\n    :local num [\$le16ToHost \$1]\r\
\n\r\
\n    # Handle negative numbers\r\
\n    :if (\$num & 0x8000) do={\r\
\n        :set num (-1 * ([\$invertU16 \$num] + 1))\r\
\n    }\r\
\n\r\
\n    # Convert from 8.8. Scale by 1000 since floating point is not supported\r\
\n    :return ((\$num * 125) / 32)\r\
\n}\r\
\n:put (\"[*] Gathering Bluetooth info...\")\r\
\n\r\
\n:global makeRecord do={\r\
\n    :local jsonStr \"{\\\"ts\\\":\$ts,\\\"values\\\":{\\\"KNOT_\$gwName\\\":\\\"\$gwName\
\\\",\\\"temp\\\":\$temp}}\"\r\
\n    :return \$jsonStr\r\
\n}   \r\
\n\r\
\n# array of record strings collected for each advertising MAC address\r\
\n:global macRecords [:toarray \"\"]\r\
\n\r\
\n# process advertisements and update macRecords\r\
\n:local advertisements [/iot bluetooth scanners advertisements print detail as-value where\
\_\\\r\
\naddress ~ \$addressRegex and \\\r\
\ndata ~ \$advertisingDataRegex and \\\r\
\nrssi > \$rssiThreshold]\r\
\n\r\
\n/iot/bluetooth/scanners/advertisements clear\r\
\n\r\
\n:foreach adv in=\$advertisements do={\r\
\n:local address (\$adv->\"address\")\r\
\n:local ad (\$adv->\"data\")\r\
\n:local rssi (\$adv->\"rssi\")\r\
\n:local epoch (\$adv->\"epoch\")\r\
\n:local temp [\$from88 [:pick \$ad 28 32]]\r\
\n                \r\
\n:local recordStr [\$makeRecord ts=\$epoch gwName=\$gwName temp=\$temp]\r\
\n\r\
\n:if ([:len (\$macRecords->\$address)] > 0) do={\r\
\n:local str (\$macRecords->\$address)\r\
\n:local newStr \"\$str,\$recordStr\"\r\
\n:set (\$macRecords->\$address) \$newStr} else={:set (\$macRecords->\$address) \$recordStr\
}}\r\
\n\r\
\n# TODO: add some logic to decide when we want to send data\r\
\n:local sendData true\r\
\n\r\
\n:if (\$sendData) do={\r\
\n:local jsonStr \"{\"\r\
\n\r\
\n:foreach addr,advRec in=\$macRecords do={\r\
\n:set jsonStr \"\$jsonStr\\\"\$addr\\\":[\$advRec],\"}\r\
\n\r\
\n:local payloadlength\r\
\n:set payloadlength [:len (\$jsonStr)]\r\
\n:local remcom\r\
\n:set remcom [:pick \$jsonStr 0 (\$payloadlength-1)]\r\
\n:set jsonStr \"\$remcom}\"\r\
\n:local message\r\
\n:set message \"\$jsonStr\"\r\
\n:log info \"\$message\";\r\
\n:put (\"[*] Message structured: \$message\")\r\
\n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
\n:put (\"[*] Sending message to MQTT broker...\")\r\
\n/iot mqtt publish broker=\"\$broker\" topic=\"\$topic\" message=\$message}"
```
This is where you need to keep in mind theBG77 modem behavior→ BG77 cellular modem (used in the KNOT) can not be used to have a cellular CAT-M/NB-IoT ongoing connection and to obtain GPS coordinates at the same time.
When the script is run:
# Scheduler
Apply a scheduler to the script, so that RouterOS periodically initiates the script by itself:
```
/system/scheduler/add name=bluetoothscheduler interval=50s on-event="/system/script/run tracking"
```
You can set up shorter and longer intervals. If you want to send data more often, so that the data is "fresher" →  set up shorter time intervals (10-15 seconds). If you want to send fewer messages, less often → you can set up longer time intervals (30min+).
The JSON message structured using the script has a "ts" value (timestamp) assigned for each payload received. Meaning thatwhen the script is run, for example,every minute, 1 tag is used andthe tag broadcasts1 payload every 10 seconds (that is6 payloads per minute) → ThingsBoard data (GUI) will be updated every minute, and every minute, 6 new entries will appear (each entry will indicate that it was received 10 seconds after the previous one). And if you send the message every 15 minutes when using 1 tag that is broadcasting a payload every 10 seconds (that is 6*15=90 payloads per 15 minutes) → ThingsBoard data (GUI) will be updated every 15 minutes but 90 entries will appear.
```
ts
```
# ThingsBoard data visualization and result verification
After you run the script with/system script run trackingor via a scheduler and refresh the GUI portal → all MAC addresses (tags) that are found in the JSON message, will be made into new devices under the ThingsBoard GUI:
```
/system script run tracking
```
To help you visualize the data, you can use the built-inwidgetsor create your own one.
Select the tag's MAC address from the list of devices, go to the "Latest telemetry" section, checkbox KNOT IDs that you wish to monitor, and click on the "Show on widget" button:
Select a widget that you wish to use, for example under the "Charts" bundle, "Timeseries Bar Chart" and click on "Add to dashboard":
Create a new dashboard and name it, however, you like. Click on "Add":
Change the widget's "Timewindow" from "Realtime-last minute" (which is used by default) to "Realtime-last 5 hours" and disable "data aggregation function" (select "none"):
To help you better visualize the result, edit the widget and then edit each "KNOT_X" parameter/key. Enable the "Show points" checkbox for each key:
Check the ThingsBoard widgetguidefor more options that you have.
The end result would look like this:
Per the dashboard, we can tell that:
# Temperature visualization (optional)
Select the tag's MAC address from the list of devices, go to the "Latest telemetry" section, checkbox "temp" parameter, and click on the "Show on widget" button:
```
temp
```
Select a widget that you wish to use, for example under the "Charts" bundle, "Timeseries Line Chart". Click on "Add to dashboard", and choose the dashboard where you want to add the widget.
The result would look like this:
Now you have an additional graph that indicates how the tag's temperature changes during different time intervals.
# GPS coordinate visualization (optional)
Per the script in theScript that includes GPS datasection, the script sends x2 MQTT messages. Each message is sent to a different MQTT topic. GPS coordinate message will be posted to a topic named "1/devices/me/telemetry", while Bluetooth data will be posted to a topic named "v1/gateway/telemetry". Coordinates will be available to you under the ThingsBoard device list, under the specific gateway:
Checkbox both "latitude" and "longitude" parameters, click on the "Show on widget button", select "Current bundle" to "Maps", and choose the "Route Map - OpenStreetMap" widget:
To finish things up, click on the "Add to dashboard" button and choose the dashboard where you want the widget to be shown.
After adding 3 widgets into 1 dashboard (temperature line chart, Bluetooth reporter bar chart, and GPS coordinates map), you would get something similar to this:
* You will have a map that shows the GPS position of the KNOT.