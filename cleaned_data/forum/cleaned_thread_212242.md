# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212242

# Discussion

## Initial Question
Author: Sun Nov 03, 2024 12:14 am
``` 
```
# 2024-11-02 23:09:49 by RouterOS 7.16.1# model = cAPGi-5HaxD2HaxD/interfacebridgeaddadmin-mac=78:9A:18:96:CF:B1auto-mac=nocomment=defconf name=bridgeLocal/interfacewifi datapathaddbridge=bridgeLocal comment=defconf disabled=noname=capdp/interfacewifi# managed by CAPsMAN# mode: AP, SSID: myssid, channel: 5500/ax/Ceeeset[finddefault-name=wifi1]configuration.manager=capsman datapath=capdp disabled=no# managed by CAPsMAN# mode: AP, SSID: myssid, channel: 2462/ax/eCset[finddefault-name=wifi2]configuration.manager=capsman datapath=capdp disabled=no/interfacebridge portaddbridge=bridgeLocal comment=defconfinterface=ether1addbridge=bridgeLocal comment=defconfinterface=ether2/interfacewifi capsetdiscovery-interfaces=bridgeLocal enabled=yes slaves-datapath=capdp/ip dhcp-clientaddcomment=defconfinterface=bridgeLocal/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/system clocksettime-zone-name=Europe/Berlin/system identitysetname=ap-dg1/system loggingaddtopics=route,!debugaddtopics=capsaddtopics=radiusaddtopics=dhcpaddtopics=wireless/system notesetshow-at-login=no
```

```
```

```
22:58:09caps,info disconnecting ap-a4@D4:01:C3:89:71:30%*15,configuration changed22:58:09caps,info disconnecting ap-dg1@78:9A:18:96:CF:B1%*15,configuration changed22:58:09caps,info disconnecting ap-og1@78:9A:18:96:CF:C9%*15,configuration changed22:58:10system,info wifiCAPsMANsettings changedbytcp-msg(winbox):admin@192.168.10.199(/interface wifi capsman set ca-certificate=auto certificate=auto enabled=no interfaces=all package-path=/packagesrequire-peer-certificate=noupgrade-policy=suggest-same-version)23:00:39system,info wifiCAPsMANsettings changedbytcp-msg(winbox):admin@192.168.1.190(/interface wifi capsman set ca-certificate=auto certificate=auto enabled=yes interfaces=all package-path=/packagesrequire-peer-certificate=noupgrade-policy=suggest-same-version)23:00:42caps,info ap-og1@78:9A:18:96:CF:C9%*15joined23:00:43caps,info ap-a4@D4:01:C3:89:71:30%*15joined23:00:43wireless,info provision ap-a4@D4:01:C3:89:71:30%*15radio D4:01:C3:89:71:3523:00:43wireless,debug provisioning createdinterfacecap-wifi1forD4:01:C3:89:71:35@ap-a4@D4:01:C3:89:71:30%*1523:00:43wireless,info provision ap-a4@D4:01:C3:89:71:30%*15radio D4:01:C3:89:71:3623:00:43wireless,debug provisioning createdinterfacecap-wifi2forD4:01:C3:89:71:36@ap-a4@D4:01:C3:89:71:30%*1523:00:44caps,info ap-dg1@78:9A:18:96:CF:B1%*15joined23:00:44wireless,info provision ap-dg1@78:9A:18:96:CF:B1%*15radio78:9A:18:96:CF:B323:00:44wireless,debug provisioning createdinterfacecap-wifi3for78:9A:18:96:CF:B3@ap-dg1@78:9A:18:96:CF:B1%*1523:00:44wireless,info provision ap-dg1@78:9A:18:96:CF:B1%*15radio78:9A:18:96:CF:B423:00:44wireless,debug provisioning createdinterfacecap-wifi4for78:9A:18:96:CF:B4@ap-dg1@78:9A:18:96:CF:B1%*1523:00:46caps,info disconnecting ap-og1@78:9A:18:96:CF:C9%*15,configuration changed23:00:46caps,info disconnecting ap-a4@D4:01:C3:89:71:30%*15,configuration changed23:00:46caps,info disconnecting ap-dg1@78:9A:18:96:CF:B1%*15,configuration changed23:00:46system,info wifiCAPsMANsettings changedbytcp-msg(winbox):admin@192.168.1.190(/interface wifi capsman set ca-certificate=auto certificate=auto enabled=yes interfaces=all package-path=/packagesrequire-peer-certificate=noupgrade-policy=suggest-same-version)23:00:50caps,info ap-a4@D4:01:C3:89:71:30%*15joined23:00:50caps,info ap-og1@78:9A:18:96:CF:C9%*15joined23:00:50caps,info ap-dg1@78:9A:18:96:CF:B1%*15joined
```

Hey there.This one has me stumped. Maybe someone has a bright idea:I have two cAP ax, and a hAP ax3). One cAP and the hAP have been set up using capsman from the central router. Both are running as expected since months.I've now tried to add the second cAP. Capsman sees it and lists it in the "Remote CAP" tab, but does not provision it. Firmware upgrade to 7.16.1 worked via capsman. Configuration of the new hAP is identical to the old one, except for the radio config. This is the config, the new cAP is missing the two capsman managed wifi interfaces:Adding the lines manually doesn't help.Disabling capsman on the router and re-enabling it yielded the following log:Any clue what's wrong here? Why isn't it properly provisioning?


---
```

## Response 1
Author: Sun Nov 03, 2024 11:46 am
Tried resetting the config to caps mode again. Same result. New cAP finds capsman and joins, but the radios are never provisioned.Somehow I cannot see the radios on the AP. Is there any way to verify that the hardware is there? Can I list the radio devices somewhere else than /interface/wifi/radio? ---

## Response 2
Author: Sun Nov 03, 2024 12:00 pm
Are their provisioning rules which match the new radios?Can you share the wifi config of the CAPsMAN?/interface wifi export file=anynameyoulikeRemove any private info, post between code tags by using the </> button. ---

## Response 3
Author: [SOLVED]Sun Nov 03, 2024 12:13 pm
Found the reason for the missing radios: during a previous netinstall, I failed to add the wifi-qcom package. D'oh. No wifi package = no wifi support.Installed the package and the radios are there. However, they are not reported to capsman and still not provisioned. ---

## Response 4
Author: Sun Nov 03, 2024 12:24 pm
Thanks for your reply @erlindenManaged to solve it. After installing the missing wifi-package, I had to reset the config again, then enable caps mode as before. Everything worked as expected at that point.How can I mark this as solved? ---

## Response 5
Author: Sun Nov 03, 2024 12:33 pm
How can I mark this as solved?I took care of that for youOn the post which contains the answer, you can hit the button right next of the Quote icon. That sets it as solved.