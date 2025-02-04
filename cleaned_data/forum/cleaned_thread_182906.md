# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 182906

# Discussion

## Initial Question
Author: Thu Feb 03, 2022 1:02 pm
Hi, I have a question for you, is it possible to send a variable, eg [Device.CustomField2] in ros_command.I want to write a universal function that will retrieve the appropriate parameterros_command(":local clientIP [Device.CustomField2]; :local peer; :local ph2; :foreach line in=[/ip ipsec policy print as-value where disabled=no and template!=yes and sa-dst-address=$clientIP] do={:foreach name, item in=$line do={if ($name=\"peer\") do= {:set peer $item}; if ($name=\"ph2-count\") do= {:set ph2 \"\"; if ($item=0) do={:set ph2 \"DOWN\"}; if ($item>0) do={:set ph2 \"UP\"};}; }; :put ($peer.\" \".$ph2)}") ---

## Response 1
Author: [SOLVED]Wed May 04, 2022 1:18 pm
``` ros_command(concatenate(":global test \"",device_property("Name"),"\"")) ``` The Dude code ---

## Response 2
Author: Fri Aug 04, 2023 12:50 pm
``` ros_command(concatenate(":global test \"",device_property("Name"),"\"")) ``` ``` ros_command(concatenate(":put [ip address get [find interface=",[Interface.Name]," ] address]")) ``` The Dude codeIs it possible to pass other information into ros_command other than from the device_property() function - I'm trying to pass [Interface.Name] into a ros_command to return the IP Address assigned to that interface.