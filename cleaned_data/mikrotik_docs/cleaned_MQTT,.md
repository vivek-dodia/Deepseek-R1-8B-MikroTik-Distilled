# Document Information
Title: MQTT
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/46759978/MQTT,

# Content
# Summary
MQTT is an open OASIS and ISO standard lightweight, publish-subscribe network protocol that transports messages between devices. A typical MQTT communication topology consists of:
RouterOS can act as an MQTT publisher and subscriber (starting with7.11beta2). You can also run an MQTT broker/server via thecontainerfeature. For Mosquitto MQTT broker configuration visit thelink here.
You can find application examples for MQTT publish scenarios below:
a)MQTT/HTTPS example with AWS cloud platform
b)MQTT example with Azure cloud platform
c)MQTT and ThingsBoard configuration
Please note that AWS and Azure examples (scripts) showcase publishing Bluetooth tag data. Currently, only theKNOThas a Bluetooth chip built-in.
# Configuration
Sub-menu:/iot mqtt
```
/iot mqtt
```
note:iotpackage is required.
IoT package is available with RouterOS version 6.48.3. You can get it from ourdownload page- under "Extra packages".
Property | Description
----------------------
brokers | A list of configured MQTT brokers.
connect | A command that specifies, which broker to connect to.
disconnect | A command that specifies, which broker to disconnect from.
publish | A command that defines the MQTT message that needs to be published.
subscribe | A command that defines MQTT topics to subscribe to.
subscriptions | A list of subscribed topics and received messages.
unsubscribe | A command that specifies, which topic to unsubscribe from.
subscribe
subscriptions
unsubscribe
# Brokers
To add a new MQTT broker (or an MQTT server), run the following command:
```
/iot mqtt brokers add
```
Configurable properties are shown below:
Property | Description
----------------------
address(IP|hostname; Default: ) | IP address or hostname of the broker.
auto-connect(yes | no; Default:no) | When enabled, after the connection with the MQTT broker goes down/gets interrupted, RouterOS will try to re-establish the connection over and over again.
certificate(string; Default: ) | The certificate that is going to be used for the SSL connection.
client-id(string; Default: ) | A unique ID used for the connection. The broker uses this ID to identify the client.
keep-alive(integer:30..64800; Default:60) | A parameter that defines the time (in seconds), after which the client should "ping" the MQTT broker that it is "alive", to ensure the connection stays ongoing. This value should be set according to MQTT broker settings.
name(string; Default: ) | Descriptive name of the broker.
parallel-scripts-limit(integer:3..1000;Default: off) | A parameter that defines how many scripts theon-messagefeature for this broker is allowed to run at the exact same time. Can be useful to reduce CPU, in cases when a large number of messages are constantly published.
password(string; Default: ) | Password for the broker (if required by the broker).
port(integer:0..4294967295; Default:1883) | Network port used by the broker.
ssl(yes | no; Default:no) | Secure Socket Layer configuration.
username(string; Default: ) | Username for the broker (if required by the broker).
client-id(string; Default: )
keep-alive(integer:30..64800; Default:60)
name(string; Default: )
parallel-scripts-limit(integer:3..1000;Default: off)
A parameter that defines how many scripts theon-messagefeature for this broker is allowed to run at the exact same time. Can be useful to reduce CPU, in cases when a large number of messages are constantly published.
password(string; Default: )
port(integer:0..4294967295; Default:1883)
ssl(yes | no; Default:no)
An example of adding a broker:
```
/iot mqtt brokers add name="broker" address="192.168.88.33" port=1883 ssl=no client-id="test-client" auto-connect=no keep-alive=60
```
The result:
```
/iot mqtt brokers print
0 name="broker" address="192.168.88.33" port=1883 ssl=no client-id="test-client" auto-connect=no keep-alive=60 connected=no
```
# Connect
To connect to the pre-configured MQTT broker, issue the command:
```
/iot mqtt connect broker="broker"
```
If the connection is successful, the "connected" parameter should change to "yes":
```
/iot mqtt brokers print
0 name="broker" address="192.168.88.33" port=1883 ssl=no client-id="test-client" auto-connect=no keep-alive=60 connected=yes
```
# Disconnect
To disconnect from the MQTT broker, issue the command:
```
/iot mqtt disconnect broker="broker"
```
To confirm that the broker was disconnected, issue the command below and it should indicate "connected=no":
```
/iot mqtt brokers print
0 name="broker" address="192.168.88.33" port=1883 ssl=no client-id="test-client" auto-connect=no keep-alive=60 connected=no
```
# Publish
Publish menu is used to send MQTT messages to the MQTT broker.
Property | Description
----------------------
broker(string; Default: ) | Select the broker, where to publish the message.
disconnect-after(yes | no; Default:no) | Parameter, that ensures that the connection with the broker will be automatically disconnected after the publish message is sent.
force(yes | no; Default:yes) | If set to "yes", when the connection with the broker is not yet established ("connected=no"), and the message is attempted to be published, RouterOS will try to establish an MQTT connection with the specified broker first and then publish the message. If set to "no", RouterOS will not be able to send the message, unless the connection is already established beforehand ("connected=yes").
message(string; Default: ) | The message that you wish to publish to the broker.
qos(integer:0..4294967295; Default:0) | Quality of service parameter, as defined by the broker.
retain(yes | no; Default:no) | Whether to retain the message or to discard it if no one is subscribed to the topic. This parameter is defined by the broker.
topic(string; Default: ) | Topic, as defined by the broker.
message(string; Default: )
qos(integer:0..4294967295; Default:0)
retain(yes | no; Default:no)
topic(string; Default: )
An example of publishing the message:
```
/iot mqtt publish message="test-message" broker="broker" topic="my/test/topic"
```
# Subscribe
This menu is used to subscribe to MQTT topics from the broker.
Property | Description
----------------------
broker(string; Default: ) | Select the broker, where to subscribe to.
force(yes | no; Default:yes) | If set to "yes", when the connection with the broker is not yet established ("connected=no"), and subscription is attempted, RouterOS will try to establish an MQTT connection with the specified broker first and then subscribe to the topic. If set to "no", RouterOS will not be able to subscribe to the topic, unless the connection is already established beforehand ("connected=yes").
qos(integer:0..4294967295; Default:0) | Quality of service parameter, as defined by the broker.
topic(string; Default: ) | Topic, as defined by the broker, where to subscribe to.
qos(integer:0..4294967295; Default:0)
topic(string; Default: )
An example of a subscription:
```
/iot mqtt subscribe broker="broker" topic="my/test/topic"
```
Wildcard (single level "+" and multi-level "# ") subscriptions are also supported (RouterOSdoes not allow publishingto wildcard topicsbut allows subscribingto them):
```
/iot mqtt subscribe broker="broker" topic="my/test/# "
/iot mqtt subscribe broker="broker" topic="my/test/+"
```
This means that if you subscribe totopic="my/test/# ", you will be able to receive messages published to any topic that begins with the pattern before the wildcard symbol "# " (e.g.,"my/test/topic","my/test/topic/something").
```
topic="my/test/# "
```
```
"my/test/topic"
```
```
"my/test/topic/something"
```
And, if you subscribe totopic="my/test/+", you will be able to receive messages published on the topic +1 level (e.g.,"my/test/topic","my/test/something").
```
topic="my/test/+"
```
```
"my/test/topic"
```
```
"my/test/something"
```
# Subscriptions
This section is used to manage already-added subscriptions (that were previously added via theSubscribesection).
It has the same properties as theSubscribesection.
Property | Description
----------------------
on-message(string; Default: ) | Configure ascriptthat will be automatically initiated/run whenever a new message is received in the subscribed topic.
To check already subscribed topics, issue the command:
```
/iot mqtt subscriptions print
0 broker=broker topic="my/test/topic" qos=0
```
After you publish a test message as shown in thePublishsection above:
```
/iot mqtt publish message="test-message" broker="broker" topic="my/test/topic"
```
You should be able to check the received message under:
```
/iot mqtt subscriptions recv print
0 broker=broker topic="my/test/topic" data="test-message" time=2023-05-22 16:57:00
```
To clear stored messages, issue the command:
```
/iot mqtt subscriptions recv clear
```
To run ascript(for example, a basic "log" script) whenever any new message appears in the subscribed topic, you can use theon-messagefeature:
```
on-message
```
```
/iot mqtt subscriptions set on-message={:log info "Got data {$msgData} from topic {$msgTopic}"} broker=broker 0
```
The script can use$msgDataand$msgTopicvariables.$msgDatadefines the MQTT message that was published and$msgTopicdefines the MQTT topic, where the message was published. Both variables are automatically generated when a new message appears.
After you publish a new MQTT message to the subscribed topic, a new log entry should appear:
```
/log print
10:19:15 script,info Got data {test-message} from topic {my/test/topic}
```
A second example shows how to run a script whenever a specific message (keywords from the message) appears. To achieve a scenario, where we want to run a script only when the MQTT message has specific content or a keyword, we can utilize theifcondition statement:
```
/iot mqtt subscriptions set 0 on-messag={:if ($msgData~"\\{\"test\":\"123\"\\}") do={:log info "Got data {$msgData} from topic {$msgTopic}"}}
```
Or:
```
/iot mqtt subscriptions set 0 on-messag={:if ($msgData~"test") do={:log info "Got data {$msgData} from topic {$msgTopic}"}}
```
As a result, on every received MQTT message, the script will check whether the if condition is true. If it is true (if$msgDatacontains the JSON string{"test":"123"}or if$msgDatacontains the string "test"), the log entry will be generated. Otherwise, nothing will happen.
Meaning, the script will be run only when you publish a message like this:
```
/iot mqtt publish broker=broker topic="my/test/topic" message="{\"test\":\"123\"}"
```
When you receive a message from a topic that falls under multiple subscriptions withon-messageconfiguration, onlyx1on-messagescript will be run. RouterOS will choose whichon-meesagescript to run using the following logic/priority:
```
on-message
```
```
on-message
```
```
on-meesage
```
An example:
```
/iot mqtt subscriptions print
0 broker=broker topic="some/sort/of/topic" qos=0 on-message="/system script run script1"
1 broker=broker topic="some/# " qos=0 on-message="/system script run script2"
2 broker=broker topic="some/sort/of/+" qos=0 on-message="/system script run script3"
3 broker=broker topic="some/thing/# " qos=0 on-message="/system script run script4"
```
When you publish the data tosome/sort/of/topic, script1 will be initiated → because the topic is an exact match.
```
some/sort/of/topic
```
When you publish the data tosome/sort/of/thing, scrtip3 will be initiated → because it falls under the single 1v1 wildcard topic name.
```
some/sort/of/thing
```
When you publish the data tosome/name, script2 will be initiated →  because it falls under the multi-level wildcard topic name.
```
some/name
```
When you publish the data tosome/thing/else, script 4 will be initiated → because it falls under the multi-level wildcard topic name (even though it is also matched bysome/# wildcard, it is a level closer tosome/thing/# entry).
```
some/thing/else
```
```
some/# ```
```
some/thing/# ```
# Unsubscribe
Property | Description
----------------------
broker(string; Default: ) | Select the broker to unsubscribe from.
topic(string; Default: ) | Select a topic, as defined by the broker, to unsubscribe from.
topic(string; Default: )
An example of unsubscribing from the broker and the topic is shown below:
```
/iot mqtt unsubscribe broker="broker" topic="my/test/topic"
```
# Publishing RouterOS statistics using scripts
You can also usescriptsto structure MQTT messages that contain RouterOS statistics. Then, you can apply theschedulerto run the script whenever you like.
For example, you can run a script likethis(copy the content of the RouterOS code shown below into a new terminal and press "enter"):
```
/system script add dont-require-permissions=no name=mqttpublish owner=admin policy=\
ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="# \
\_Required packages: iot\r\
\n\r\
\n# Configuration # \
# \r\
\n# Name of an existing MQTT broker that should be used for publishing\r\
\n:local broker \"broker\"\r\
\n\r\
\n# MQTT topic where the message should be published\r\
\n:local topic \"my/test/topic\"\r\
\n\r\
\n# System # \
# \r\
\n:put (\"[*] Gathering system info...\")\r\
\n:local cpuLoad [/system resource get cpu-load]\r\
\n:local freeMemory [/system resource get free-memory]\r\
\n:local usedMemory ([/system resource get total-memory] - \$freeMemory)\r\
\n:local rosVersion [/system package get value-name=version \\\r\
\n\A0 \A0 [/system package find where name ~ \"^routeros\"]]\r\
\n:local model [/system routerboard get value-name=model]\r\
\n:local serialNumber [/system routerboard get value-name=serial-number]\r\
\n:local upTime [/system resource get uptime]\r\
\n\r\
\n# MQTT # \
# \r\
\n:local message \\\r\
\n\A0 \A0 \"{\\\"model\\\":\\\"\$model\\\",\\\r\
\n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"sn\\\":\\\"\$serialNumber\\\",\\\r\
\n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"ros\\\":\\\"\$rosVersion\\\",\\\r\
\n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"cpu\\\":\$cpuLoad,\\\r\
\n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"umem\\\":\$usedMemory,\\\r\
\n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"fmem\\\":\$freeMemory,\\\r\
\n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"uptime\\\":\\\"\$upTime\\\"}\"\r\
\n\r\
\n:log info \"\$message\";\r\
\n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
\n:put (\"[*] Sending message to MQTT broker...\")\r\
\n/iot mqtt publish broker=\$broker topic=\$topic message=\$message\r\
\n:put (\"[*] Done\")"
```
The script collects the data from the RouterOS (model name, serial number, RouterOS version, current CPU, used memory, free memory, and uptime) and publishes the message (the data) to the broker in the JSON format:
```
/system script run mqttpublish
[*] Gathering system info...
[*] Total message size: 125 bytes
[*] Sending message to MQTT broker...
[*] Done
```
You can subscribe to the topic to check the results:
```
/iot mqtt subscriptions recv  print
0 broker=broker topic="my/test/topic" data="{"model":"RB924i-2nD-BT5&BG77","sn":"E9C80EAEXXXX","ros":"7.9","cpu":13,"umem":47476736,
"fmem":19632128,"uptime":"02:21:18"}"
time=2023-05-22 17:03:52
```
Do not forget to change the "Configuration" part of the script (topic and the broker) based on your settings.