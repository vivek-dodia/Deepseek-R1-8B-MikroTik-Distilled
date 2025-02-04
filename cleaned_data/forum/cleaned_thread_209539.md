# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 209539

# Discussion

## Initial Question
Author: Wed Jul 24, 2024 10:56 pm
``` 
```
/interface wifi channel add band=5ghz-ac disabled=no frequency=5220 name=channel5Gac-ch100 skip-dfs-channels=all width=20/40mhz
/interface wifi channel add band=5ghz-ax disabled=no frequency=5785 name=channel5Gax-ch100 skip-dfs-channels=all width=20/40mhz
/interface wifi channel add band=5ghz-n disabled=no frequency=5220 name=channel5Gan-ch100 skip-dfs-channels=all width=20/40mhz
/interface wifi datapath add bridge=ho-bridge client-isolation=no disabled=no name=datapath-ho
/interface wifi datapath add bridge=ho-bridge client-isolation=no disabled=no interface-list=all name=datapath-guest
/interface wifi datapath add bridge=ho-bridge client-isolation=no disabled=no interface-list=all name=datapath-wnt
/interface wifi security add authentication-types=wpa-psk,wpa2-psk,wpa-eap disable-pmkid=yes disabled=no encryption=ccmp,gcmp,ccmp-256,gcmp-256 group-key-update=1h name=ho-sec
/interface wifi security add authentication-types=wpa2-psk,wpa3-psk disable-pmkid=yes encryption=ccmp,gcmp,ccmp-256,gcmp-256 name=ho-sec-ax
/interface wifi security add authentication-types=wpa-psk,wpa2-psk,wpa-eap disable-pmkid=yes disabled=no encryption=ccmp,gcmp,ccmp-256,gcmp-256 name=guest-sec
/interface wifi security add authentication-types=wpa2-psk,wpa3-psk disable-pmkid=yes disabled=no encryption=ccmp,gcmp,ccmp-256,gcmp-256 name=guest-sec-ax
/interface wifi security add authentication-types=wpa-psk,wpa2-psk,wpa-eap disable-pmkid=yes disabled=no encryption=ccmp,gcmp,ccmp-256,gcmp-256 name=wnt-sec
/interface wifi security add authentication-types=wpa2-psk,wpa3-psk disable-pmkid=yes encryption=ccmp,gcmp,ccmp-256,gcmp-256 name=wnt-sec-ax
/interface wifi configuration add channel=channel5Gac-ch100 country=Austria datapath=datapath-ho disabled=no name=Config_HOME_5Gac-ch100 security=ho-sec ssid=Hades
/interface wifi configuration add channel=channel5Gax-ch100 country=Austria datapath=datapath-ho disabled=no name=Config_HOME_5Gax-ch100 security=ho-sec-ax ssid=Hades
/interface wifi configuration add channel=channel5Gax-ch100 country=Austria datapath=datapath-guest disabled=no name=Config_GUEST_5Gax-ch100 security=guest-sec-ax ssid=Firedrag
/interface wifi configuration add channel=channel5Gac-ch100 country=Austria datapath=datapath-guest disabled=no name=Config_GUEST_5Gac-ch100 security=guest-sec ssid=Firedrag
/interface wifi configuration add channel=channel5Gax-ch100 country=Austria datapath=datapath-wnt disabled=no hide-ssid=yes name=Config_WNT_5Gax-ch100 security=wnt-sec-ax ssid=WNT-NOC-CHO
/interface wifi configuration add channel=channel5Gac-ch100 country=Austria datapath=datapath-wnt disabled=no hide-ssid=yes name=Config_WNT_5Gac-ch100 security=wnt-sec ssid=WNT-NOC-CHO
/interface wifi configuration add channel=channel2Gn2-ch11 country=Austria datapath=datapath-wnt disabled=no hide-ssid=yes name=Config_WNT_2Gn-ch11 security=wnt-sec ssid=WNT-NOC-CHO
/interface wifi access-list add action=reject allow-signal-out-of-range=10s disabled=no interface=any signal-range=-120..-80 ssid-regexp=""
/interface wifi access-list add action=accept allow-signal-out-of-range=10s disabled=no interface=any signal-range=-79..10 ssid-regexp=""
/interface wifi cap set caps-man-addresses=127.0.0.1 certificate=request discovery-interfaces=ho-bridge enabled=yes lock-to-caps-man=yes slaves-static=yes
/interface wifi capsman set ca-certificate=auto certificate=auto enabled=yes interfaces=ho-bridge package-path="" require-peer-certificate=no upgrade-policy=require-same-version
/interface wifi provisioning add action=create-dynamic-enabled disabled=no master-configuration=Config_GUEST_5Gan-ch100 name-format="" radio-mac=48:A9:8A:E2:90:E9 slave-configurations=Config_HOME_5Gan-ch100,Config_WNT_5Gan-
ch100,Config_GUEST_5Gac-ch100,Config_HOME_5Gac-ch100,Config_WNT_5Gac-ch100,Config_GUEST_5Gax-ch100,Config_HOME_5Gax-ch100,Config_WNT_5Gax-ch100 supported-bands=5ghz-n,5ghz-ac,5ghz-ax
```

Hi,I try to archive a provisioning different hap ax3 through capsman with different bands per radio (5Gax 5Gac 5Gan and 2Gax, 2Gn). The caps take over the configuration except the correct band. I provision the cap via radio mac and a master slave configuration. But depending on which master configuration I use, it uses the band of the master configuration (seen in current channel and via wifi scanner) not the bands of the slave configurations.Thats my config, I reduced it to the 5G Bands:When I provision the 5G radio, I see unter Wifi the correct bands but unter current channel only the band of the master interface (see attachement):Is there a limitation, what I didn´t find in documentation or in the forum?2nd question, is it still not possible to provision the vlan-id from capsman to the caps (new capsman restriction). Do I still need to configure the vlans manual on the caps. If not could you post me a code with an excample?thx in advance for any support or any new thoughts.Chris


---
```

## Response 1
Author: Mon Aug 05, 2024 11:51 pm
Any suggestions?Didn't anybody hit these problems? ---

## Response 2
Author: Tue Aug 06, 2024 12:32 am
Why do you need that? AX devices are backward compatible with older standards..And yes, it's possible and working fine with AX devices.. ---

## Response 3
Author: [SOLVED]Tue Aug 06, 2024 8:21 am
Slave config will always follow the physical part of master.That's normal.You can play on slave part with ssid, security, fast transition, ... but not channel nor band, those will be taken from master.As for your second question:https://help.mikrotik.com/docs/display/ ... ionexample: ---

## Response 4
Author: Thu Aug 08, 2024 3:34 pm
Why do you need that? AX devices are backward compatible with older standards..And yes, it's possible and working fine with AX devices..Thx for the information. Had problems with some devices with ax band. I will configure it then accordingly. ---

## Response 5
Author: Thu Aug 08, 2024 3:40 pm
Slave config will always follow the physical part of master.That's normal.You can play on slave part with ssid, security, fast transition, ... but not channel nor band, those will be taken from master.As for your second question:https://help.mikrotik.com/docs/display/ ... ionexample:Okay, so I will create an ax band with lower security to provide "older" devices with the correct security mechanism on an and ac bands.The link you provided is the vlan configuration, I have configured on my capsman and my caps. Legacy capsman was able to provide vlan-ids from the capsman, and there was no need to configure it per interface. But when I don't need to configure each band (ac, an and ax), there is no need for so many interfaces.Thx for your help!!!!Chris