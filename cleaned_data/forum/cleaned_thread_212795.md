# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212795

# Discussion

## Initial Question
Author: Sun Nov 24, 2024 5:23 pm
I have purchased the Chateau 5G ax and I am satisfied with the performance of the 5G modem and Wi-Fi 6. However, I was unable to find a way to support both 802.11ac and ax on the same physical radio (5GHz). Even if I create another Wi-Fi interface as a subinterface of the main one (configured with ax) and apply a different Wi-Fi configuration (with ac) it broadcasts the SSID as Wi-Fi 6. I need to support Wi-Fi 5 for older clients, but if is not supported, I will need to fall them back to 802.11n on 2.4GHz which is undesirable. Is there a way to achieve this? ---

## Response 1
Author: [SOLVED]Sun Nov 24, 2024 5:55 pm
AC or AX band selection are physical settings always driven by master radio.If you set radio to AX, AC clients should connect just fine.Same with 2GHz AX radio and N clients.I have plenty of IoT clients only using N connecting to 2GHz AX radio.Just make sure your security settings are OK. Usually the problem is there. ---

## Response 2
Author: Wed Nov 27, 2024 10:25 am
You are correct - indeed, in the security options I was setting CCMP 256 and GCMP 256 which probably prevented the clients from connecting. When I cleared all the checkboxes and left only WPA2 and WPA3, AX and AC clients connected successfully. I guess that if I set AX on the 2.4 band, N will also work.Thank you very much for this hint. Just one more question - how can I disable TKIP as encryption method and the legacy standards - a/b/g and leave only n/ac/ax? Currently I haven't checked any of the cyphers and I guess that all of them are acceptable.Cyphers.png ---

## Response 3
Author: Wed Nov 27, 2024 11:00 am
You may want to look at output of command/interface/wifi/printand/interface/wifi/security/print(run them in terminal window ... you can start one from WinBox or connect to device using ssh) ... and look for "encryption" property in both outputs. Only then you'll see what is actually configured on device. Default (if property is unset) is "ccmp" only ... which is basically good ole AES in WPA2. So if you don't enable it explicitly, TKIP won't be available.According to my experience it's mostly safe to enable "ccmp, ccmp-256" while any of gcmp tends to freak out many not-so-modern devices. ---

## Response 4
Author: Wed Nov 27, 2024 11:09 am
Just one more question - how can I disable TKIP as encryption method and the legacy standards - a/b/g and leave only n/ac/ax? Currently I haven't checked any of the cyphers and I guess that all of them are acceptable.As for legacy standards, in legacy wireless drivers this was possible to specify.With wave2 drivers you can not limit this anymore. It's all or nothing but AX is backwards compatible with all of them. ---

## Response 5
Author: Wed Nov 27, 2024 11:52 am
Great, thank you both for your time and suggestions.