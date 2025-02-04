# Thread Information
Title: Thread-1117670
Section: RouterOS
Thread ID: 1117670

# Discussion

## Initial Question
Hello.I have an unsolvable problem. Unable to connect Smart Tuya devices to Mikrotik AP. I try to set only basic configuration on MikroTik AP - bridged port eth1 and wifi2 (2, 4GHz) with WPA auth. When trying connect in Tuya Smart app - not succes with timeout. Old noname (not sure of manufacturer) AP joined to same network working without problem - Tuya device was connected successfully. For this i am focusing on problem in MikroTik AP (hAP ax2) not in rest of the network.In different network, where i try connect my Mikrotik AP, the same problem.Does someone know the solution?V. ---

## Response 1
with WPA auth.Do these devices support this ancient standard?Reset the Mikrotik to factory settings, merge the ports into bridge and do not touch anything else. ---

## Response 2
Sorry for hte wrong information. Of course, I usingWPA2auth.But I also tried different autentication settings without success. (Other noname AP without probleam as I wrote).And I also wrote...only basic configuration on MikroTik AP - bridged port eth1 and wifi2...Other devices joined to the MikroTik AP (laptops, smartphones, TV) work fine.But only the Tuya not....The same problem on second hAP ax2 device. Other MikroTik devices not tested. ---

## Response 3
Does anyone have the same problem? ---

## Response 4
I have an unsolvable problem.If you yourself say it's unsolvable, why bother? ---

## Response 5
What do you see on the AP in logs? Can you provide supout file tosupport@mikrotik.com? Plenty of Tuya devices connected to MikroTik routers all over the globe. This definitely is not a global incompatibility issue. ---

## Response 6
The same problem on second hAP ax2 device. Other MikroTik devices not tested.I've got a similar problem with connecting 10-year old Kindle to AX2. Kindle doesn't even see the network. Tried disabling WPA3-PSK and enabling WPA-PSK and WPA2-PSK, no help. Switching 2GHz AX and switching to 2Ghz N worked so I'm guessing some devices don't work with AX at all. ---

## Response 7
What do you see on the AP in logs? Can you provide supout file tosupport@mikrotik.com? Plenty of Tuya devices connected to MikroTik routers all over the globe. This definitely is not a global incompatibility issue.Supout has been send... ---

## Response 8
Now tested hAP ac2 - works fine, Tuya connected. ---

## Response 9
Does anyone have the same problem?I have with tp link kasa smart plug2.4ax all possible combinations they can't find WiFi (kasa app shows all devices are off)Making 2.4n only make device connected and disconnecting loss signal2.4g makes work but not stable...Because of them im still using cap ac only 2.4 just for thenWhile cap ax I have only enabled 5g ax ---

## Response 10
2.4ax all possible combinations they can't find WiFi (kasa app shows all devices are off)Same with my ancient Kindle. I would be interesting if anyone has an AX device from another manufacturer and whether the same devices work with it in AX mode. I would hope/imagine not. ---

## Response 11
2.4ax all possible combinations they can't find WiFi (kasa app shows all devices are off)Same with my ancient Kindle. I would be interesting if anyone has an AX device from another manufacturer and whether the same devices work with it in AX mode. I would hope/imagine not.I Wish but unfortunately I don't want to buy any out of shelf router ax just to check they will work or notNow I was thinking maybe one of my android I can try to see if mobile hotspot with 2.4 can do ax ---

## Response 12
For me, the Kindle is a non-issue. Only needs to be on the internet when I need to download a new book so can use hotspot on phone. I'm guessing the solutions are a) switch to 2N on 2.4Ghz or b) install a cheap Wi-Fi 4 access point. Must be loads 2nd hand on eBay. Would suggest mAP lite but they're expensive IMO these days. TBH loosing 2AX wouldn't be disastrous as high speed devices will be connecting to 5GHz anyway. ---

## Response 13
TBH loosing 2AX wouldn't be disastrous as high speed devices will be connecting to 5GHz anyway.But even putting in 2gz-n it won't work or be very unstable....There is something with this legacy device that is messed up... ---

## Response 14
Further testing:* Smartphone connected to the hAP ac2, none device in Tuya app. I run new device adding procedure and device is added successfully. Device status is online and working well.* Now I switch off (disconnect from power) the hAP ac2. Previously added device status is going to offline (in Tuya app).* I switch on the TP-Link AP (connected to the same network), where is set the same wifi configuration as in hAP ac2 (the same SSID and WiFi password, security,…) Device in Tuya app is going to online automatically and working well.* I switch off the TP-Link AP. Tuya device status is going to offilne.* I switch on thehAP ax2(connected to the same network), where is set the same wifi configuration as in hAP ac2 (the same SSID and WiFi password, security,…) Device status in Tuya app stays offline. Device does not work] ---

## Response 15
Have you tried separating 2.5 and 5GHz networks with separate name (SSIDs)? Then both app device and Tuya IoT device need to be on the same 2.4Ghz network ---

## Response 16
For this tests 5GHz radio is disabled. Configured 2, 4GHz only. ---

## Response 17
I have the same exact issue. I think this is due to recent updates on Mikrotik routher. My devices used to work 4-5 years, not anymore.. ---

## Response 18
I am experiencing the same issue with the hAP ax lite, for example, when trying to adopt the Tuye WiFi switch. ---

## Response 19
My situation is similar but i solved it like that:I have gree AC (4 appliances) they do not want to connect only to the caps with only ax network. Using my provisovision section I have a hybrid structure of 2.4 IoT network: main 2.4g network with N and slave working in AX standard.My gree devices connect to my caps only when N standard is main and AX is slave. With AX first and only AX they do not connect. Strange is that they can connect to AX as you can see in my registration table. So probably when AX is only or AX is the first the devices can not see the network or something else. ---

## Response 20
Same problem with connecting "Wifi Tuya Smart Temperature and Humidity Sensor" to WiFi MikroTik RB951Ui-2HnD RouterOS v7.16.2.MikroTik RB951Ui-2HnD is an old device, only 2.4GHz, all home devices connect without problems, except "Tuya Smart WIFI Temperature Humidity Sensor".I tried to change the wireless interface modes and security profile settings can not solve the problem.What to do? ---

## Response 21
Now that is unusual. Most of the problems appear to be with older Wi-Fi 4 (N) devices connecting to newer Wi-Fi 6 (AX) access points which you can half understand. I would expect RB951Ui-2HnD to be very compatible with all Wi-Fi 4 devices like this temperature sensor. ---

## Response 22
...What to do?Do you have any device you can connect that sensor to? And then CC settings to Mikrotik? ---

## Response 23
Installed v.6.49.17 today and did the configuration manually.Didn't help, Tuya won't connectPSTuya connects to other WiFi hotspots without problems. ---

## Response 24
Didn't help, Tuya won't connectsame problem with Tuya WIFI-TH-2023 (temperature/humidity sensor)the devices started connecting to wifi when I set the following parameters:sec_profile.pngwlan.png ---

## Response 25
Thanks, I solved the problem.I made the settings as shown in the picturethe devices started connecting to wifi when I set the following parameters:It didn't work, the sensor didn't connect to WiFi.Then I made a virtual wlan2 AP with a different ssid test and the sensor connected!Then tried to connect to the previous WiFi AP and the sensor connected too!(Deleted the test virtual WiFi AP test.)The sensor works without problems thanks! ---