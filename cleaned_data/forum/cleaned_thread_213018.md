# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213018

# Discussion

## Initial Question
Author: Tue Dec 03, 2024 10:38 am
Hello, I have a question about Wifi6 Security profile configuration and especially about part Encryption, if I check in Authentication WPA2 PSK, but do not check anything in Encryption, does it mean that my wifi will be unencrypted and it will only ask for password? ---

## Response 1
Author: Tue Dec 03, 2024 11:02 am
If nothing is set in encryption property (but check in CLI if that's actually the case), then default will apply ... which is "CCMP" (good old AES in WPA2). When checking with CLI: note that setting property to empty string (i.e. "") is not the same as not setting it at all.You can try to set encryption to CCMP (it should be fine for vast majority of wireless clients). You can try to enable additional encryption types (e.g. CCMP-256, any of GCMP). I suggest you to set one at a time and verify that all clients are still happy. My experience is that GCMP doesn't fare nicely with quite a few clients (not so ancient Android Samsung smart phones for example). ---

## Response 2
Author: Tue Dec 03, 2024 11:03 am
It's encryption of the password. Password is always encrypted. If not set, default encryption is used: ccmp ---

## Response 3
Author: Tue Dec 03, 2024 11:12 am
When checking with CLI: note that setting property to empty string (i.e. "") is not the same as not setting it at all.Ok, and then what happens if it is set to empty string (i.e. "") and what happens if it is not set at all?It's encryption of the password. Password is always encrypted. If not set, default encryption is used: ccmphttps://help.mikrotik.com/docs/spaces/R ... Propertiesin here it is said, that it is - A list of ciphers to support for encrypting unicast traffic. ---

## Response 4
Author: [SOLVED]Tue Dec 03, 2024 11:23 am
When checking with CLI: note that setting property to empty string (i.e. "") is not the same as not setting it at all.Ok, and then what happens if it is set to empty string (i.e. "") and what happens if it is not set at all?When this property is not set at all, default (ccmp) applies. When it's set to empty string, then none of ciphers are available (not even default). I don't know what would in this case happen (likely SSID would be broadcast, but no clients would be able to connect due to inability to select any common encryption algorithm for WPA2 which requires encryption). ---

## Response 5
Author: Tue Dec 03, 2024 11:26 am
It's encryption of the password. Password is always encrypted. If not set, default encryption is used: ccmphttps://help.mikrotik.com/docs/spaces/R ... Propertiesin here it is said, that it is - A list of ciphers to support for encrypting unicast traffic.Correct: encryption algorithm is one of the listed ... and password is key, used by algorithm. That's why using WPA2-EAP (and RADIUS) is considered safer: every user uses different encryption key (with WPA2-PSK, every user uses same encryption key). ---

## Response 6
Author: Tue Dec 03, 2024 11:43 am
Ok, thank you.It's a bit confusing, that by default CCMP is not selected if it is used as default and left that you can check it even if you don't need to. ---

## Response 7
Author: Tue Dec 03, 2024 5:21 pm
Its a phuckng PILE of CWAP........ The new config for wifi reminds me of 10 years ago getting tools for kids from china, where the written instructions in english are so bad its comedy material.The MT wifi config is NOT intuitive and borders on stewpid, and is no laughing matter.