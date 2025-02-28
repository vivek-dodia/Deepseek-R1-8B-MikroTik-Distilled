# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210939

# Discussion

## Initial Question
Author: Sun Sep 15, 2024 6:05 am
``` 
```
[admin@MikroTik] /interface/wifi/access-list> print 
Columns: MAC-ADDRESS, ACTION
#  MAC-ADDRESS        ACTION
;;; Macbook
0  BC:D0:74:48:57:81  accept
;;; Deny All
9                     reject
```

Hello everyone!I just bought a Mikrotik Ax3 US version, unpacked it, set it up via Quick Set for LAN DHCP internet, and connected all devices via WiFi. When I tried to configure the access list through the web interface, I noticed that the "default authentication" option is no longer available in the interface. I added a "Deny all" rule at the end, and… these rules are simply being ignored. I tried to block a specific MAC address: it still connects. I reset the router and reconfigured everything—still not working. I also tried updating the firmware (was 7.14.3, updated to 7.15.3)—no effect. I noticed that the WiFi interface manager was set to Capsman, so I changed it to local—still not working. It seems like the access list is being ignored, no matter how I try to apply it. What am I doing wrong?Router: Ax3Firmware: 7.15.3 (Packages: routeros 7.15.3, wifi-qcom 7.15.3)Access list:I’m sure something is misconfigured somewhere. I’d appreciate any help in advance.PS: In the process, I accidentally bricked my AC2 (didn’t notice that the laptop reconnected to the old network) where everything was configured and working perfectly (firmware was around 6.49.2).


---
```

## Response 1
Author: Sun Sep 15, 2024 8:50 am
The interface or SSID to which connections should be denied is not specified. ---

## Response 2
Author: Mon Sep 16, 2024 1:08 am
The interface or SSID to which connections should be denied is not specified.It worked well this way on HAP ac2. But i tried to specify interfaces in each entry- still ignored. ---

## Response 3
Author: Mon Sep 16, 2024 1:22 am
The interface or SSID to which connections should be denied is not specified.It worked well this way on HAP ac2. But i tried to specify interfaces in each entry- still ignored.The key is you need one that to be matched, just accept without ANYTHING will get skipped - or at least that's what I've found. You can also use signal-range=-120..120 as the matcher (or a more restricted acceptable range).Also, it's possible the "interface" is bridge, not wifiX - but not sure. ---

## Response 4
Author: [SOLVED]Mon Sep 16, 2024 2:04 am
It worked well this way on HAP ac2. But i tried to specify interfaces in each entry- still ignored.The key is you need one that to be matched, just accept without ANYTHING will get skipped - or at least that's what I've found. You can also use signal-range=-120..120 as the matcher (or a more restricted acceptable range).Also, it's possible the "interface" is bridge, not wifiX - but not sure.Thank you man! I specified the signal range and the rules started considering. So the problem is when you create a rule: there is a stub range for time 00:00:00..00:00:00 and a signal 0..0. And when you press apply it makes a rule with absolutely strict ranges.So there are 3 ways to solve it:1. Make rules using the terminal2. Make ranges as -120..120 for signals and 00:00:00..23:59:59 for time (really wierd)3. OR just click to fold buttons in the interface and close the stub values. It will force the UI not to push ranges at all.So, this problem is with UI form only. ---

## Response 5
Author: Mon Sep 16, 2024 3:16 am
... really wierd...Yup. FWIW, the docs on how this works are lacking . My guess it operates a "matcher"/selector, not like the firewall "filter"/etc - or at least that how I rationalize the logic here. ---

## Response 6
Author: Mon Sep 16, 2024 2:46 pm
My guess it operates a "matcher"/selector, not like the firewall "filter"/etcBoth here and firewall filter rules have most properties "selectors" and only one property which does something (in both cases it'saction... to whatever it's set for a particular rule). In order for rule to trigger/execute, all "selectors" have to match - they are AND-ed together. So yes, it's UI playing games with @Magvaj ... it is not exactly buggy, it's important to know how UI operates - with webfig/winbox one has to "fold" properties which should not be set at all ... regardless what GUI does by default ... or set properties to sane values if folding is not possible.While we're talking about actions and selectors: for a change, NAT rules have (up to) two actions: dst-address and dst-port ... the rest of properties are, again, selectors. And these two actions are foldable ...