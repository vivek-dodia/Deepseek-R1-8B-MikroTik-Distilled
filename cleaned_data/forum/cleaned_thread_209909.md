# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 209909

# Discussion

## Initial Question
Author: Tue Aug 06, 2024 12:14 pm
``` 
```
slaves-static=yes
```

```
```

```
/interface wifi
# managed by CAPsMAN
# mode: AP, SSID: lan.robtor.de, channel: 5240/n
set [ find default-name=wifi2 ] configuration.manager=capsman .mode=ap disabled=no name=wifi2LAN
# managed by CAPsMAN
# mode: AP, SSID: lan.robtor.de, channel: 2417/n
set [ find default-name=wifi1 ] configuration.manager=capsman .mode=ap disabled=no name=wifiLAN
# managed by CAPsMAN
# mode: AP, SSID: smarthome.robtor.de
add configuration.mode=ap disabled=no mac-address=4A:A9:8A:E8:E3:0E master-interface=wifiLAN name=wifiSMARTHOME
# managed by CAPsMAN
# mode: AP, SSID: Bar Wifi Gast
add configuration.mode=ap disabled=no mac-address=4A:A9:8A:E8:E3:11 master-interface=wifi2LAN name=wifi2GUEST
# managed by CAPsMAN
# mode: AP, SSID: fon.robtor.de
add configuration.mode=ap disabled=no mac-address=4A:A9:8A:E8:E3:0F master-interface=wifiLAN name=wifiFON
# managed by CAPsMAN
# mode: AP, SSID: Bar Wifi Gast
add configuration.mode=ap disabled=no mac-address=4A:A9:8A:E8:E3:10 master-interface=wifiLAN name=wifiGUEST
/interface wifi cap
set caps-man-addresses=172.20.0.1 certificate=CAP-48A98AE8E30C discovery-interfaces=vlanMGM enabled=yes lock-to-caps-man=yes slaves-static=yes
```

Hey guys, I actually have some weird behavior in my CAPsMAN setup with a plenty of CAP-AC's and a RB3011 as the controller.I recently switched to the wifi-qcom-ac driver to have 802.11r and WPA3. Unfortunately this driver does not support vlan taggingyet.So I figured out to do the vlan tagging on the bridge with bridge vlan filtering. For this I had to enable theoption on the CAP's.(See this post:viewtopic.php?t=202476)Sometimes this worked very well. I actually named the nowstaticslave interfaces by myself to identify them and then added them to the bridge and configured the vlan tag.But sometimes when I run upgrades or reprovision the CAP's, the interfaces are named again wifi1, wifi2, ... and all the vlan configuration is broken an my whole wifi network does not work anymore!Does anybody have an idea why this happens? The slaves-static is always enabled. Is the renaming of the interfaces an issue? Or do I have to add some additional configuration on the CAPsMAN's side?Here's my config of the CAP:But sometimes after reprovisioning the configuration ends up with a total mess, e.g. the "lan.robtor.de" is then named wifi1 and then is even not a memeber of the bridge and thus does not get any vlan tag.


---
```

## Response 1
Author: Wed Aug 07, 2024 8:28 pm
``` 
```
/interface wifi provisioning
add action=create-dynamic-enabled disabled=no master-configuration=GuestWiFi_2Ghz-Auto_AX name-format=2G-%I- slave-configurations=BearsTV_2Ghz-Auto_AX,BearsOffice_2Ghz-Auto_AX supported-bands=2ghz-ax
add action=create-enabled disabled=no master-configuration=GuestWifi-2Ghz-Auto-qcom-AC name-format=2G-%I slave-configurations=BearsTV-2Ghz-Auto-qcom-AC,BearsOffice-2Ghz-Auto-qcom-AC supported-bands=2ghz-n
add action=create-dynamic-enabled disabled=no master-configuration=GuestWiFi_5Ghz-Auto_AX name-format=5G-%I slave-configurations=BearsTV_5Ghz-Auto_AX,BearsOffice_5Ghz-Auto_AX supported-bands=5ghz-ax
add action=create-enabled disabled=no master-configuration=GuestWiFi-5Ghz-Auto-qcom-AC name-format=5G-%I slave-configurations=BearsTV-5Ghz-Auto-qcom-AC,BearsOffice-5Ghz-Auto-qcom-AC supported-bands=5ghz-ac

/interface wifi datapath
add bridge=all-vlan-bridge disabled=no name=vlan10_BearsNet vlan-id=10
add bridge=all-vlan-bridge client-isolation=yes disabled=no name=vlan129_BearsTV vlan-id=129
add bridge=all-vlan-bridge client-isolation=yes disabled=no name=vlan40_GuestWiFi vlan-id=40
add bridge=all-vlan-bridge client-isolation=yes disabled=no name=QCOM-AC-Guest
add bridge=all-vlan-bridge client-isolation=yes disabled=no name=QCOM-AC-BearsTV
add bridge=all-vlan-bridge disabled=no name=QCOM-AC-BearsOffice
```

```
```

```
/interface wifi
# managed by CAPsMAN
# mode: AP, SSID: Bears Guest, channel: 2412/n
set [ find default-name=wifi1 ] configuration.antenna-gain=3 .manager=capsman .mode=ap disabled=no
# managed by CAPsMAN
# mode: AP, SSID: Bears Guest, channel: 5805/ac/eC
set [ find default-name=wifi2 ] configuration.antenna-gain=6 .manager=capsman .mode=ap disabled=no
# managed by CAPsMAN
# mode: AP, SSID: Bears TV
add disabled=no mac-address=C6:AD:34:B9:35:EE master-interface=wifi1 name=wifi3
# managed by CAPsMAN
# mode: AP, SSID: Bears Office
add disabled=no mac-address=C6:AD:34:B9:35:EF master-interface=wifi1 name=wifi4
# managed by CAPsMAN
# mode: AP, SSID: Bears TV
add disabled=no mac-address=C6:AD:34:B9:35:F0 master-interface=wifi2 name=wifi5
# managed by CAPsMAN
# mode: AP, SSID: Bears Office
add disabled=no mac-address=C6:AD:34:B9:35:F1 master-interface=wifi2 name=wifi6
/interface wifi cap
set discovery-interfaces=bridgeLocal enabled=yes slaves-static=yes
/interface bridge
add admin-mac=C4:AD:34:B9:35:EC auto-mac=no comment=defconf ingress-filtering=no name=bridgeLocal port-cost-mode=short pvid=88 vlan-filtering=yes

/interface bridge port
add bridge=bridgeLocal comment=defconf ingress-filtering=no interface=ether1 internal-path-cost=10 path-cost=10 pvid=88
add bridge=bridgeLocal comment=defconf ingress-filtering=no interface=sfp1 internal-path-cost=10 path-cost=10
add bridge=bridgeLocal interface=wifi1 pvid=40
add bridge=bridgeLocal interface=wifi2 pvid=40
add bridge=bridgeLocal interface=wifi3 pvid=129
add bridge=bridgeLocal interface=wifi5 pvid=129
add bridge=bridgeLocal interface=wifi4 pvid=10
add bridge=bridgeLocal interface=wifi6 pvid=10
/interface bridge vlan
add bridge=bridgeLocal tagged=bridgeLocal vlan-ids=88
add bridge=bridgeLocal untagged=wifi4,wifi6 vlan-ids=10
add bridge=bridgeLocal untagged=wifi3,wifi5 vlan-ids=129
add bridge=bridgeLocal untagged=ether1 vlan-ids=10
```

I'm also experiencing this same issue.  Followed MikroTik documentation within their Wiki, and even adjusted the CAPsMAN provisioning to be "create enabled" instead of "create dynamic enabled".When "pushing" new config, or re-provisioning the CAP running qcom-ac driver, the WLAN interfaces change and increment; breaking the bridge and vlan assignment for the WLAN SSID's.But yet, when I was "testing" the Datapath setting in CAPsMan for sending VLAN-ID.. it works-- the cap running qcom-ac driver receives it on the bridge interface and a PVID is set... However, CAPsMAN complains. MikroTik Documentation states that is invalid configuration.We're also seeing antenna-gain is broken for sector antenna [mANTBoxes],  It is defaulting to zero.  We usually reduce the gain.Here is ours.Then here is a cap side -


---
```

## Response 2
Author: Wed Aug 07, 2024 9:32 pm
But yet, when I was "testing" the Datapath setting in CAPsMan for sending VLAN-ID.. it works-- the cap running qcom-ac driver receives it on the bridge interface and a PVID is set... However, CAPsMAN complains. MikroTik Documentation states that is invalid configuration.So do I correctly understand you that on the qcom-ac (non-ax) devices the vlan configuration is working without adding the slave-static interfaces to the bridge by just setting the datapath? Even though they say "unsupported" in the documentation? I never ever tried to do that because I thought it won't work or maybe cause bugs/misconfiguration.Hopefully MT will get this fixed, as the whole CAPsMAN is kind of useless when using qcom-ac devices. In my opinion the greatest advantage was the central configuration of vlan's on the CAPsMAN. I do not want to fix all my 8 AP's vlan configuration each time I do an upgrade, reprovision or configuration change. I also hope cAP-ac is not end of life yet, I think there might be a plenty of users who would appreciate if this gets fixed.Switching back to the old wireless driver (that acutally worked pretty well!!) is for me also not an option because it lacks the WPA3 encryption and 802.11r. ---

## Response 3
Author: Thu Aug 08, 2024 5:42 am
But yet, when I was "testing" the Datapath setting in CAPsMan for sending VLAN-ID.. it works-- the cap running qcom-ac driver receives it on the bridge interface and a PVID is set... However, CAPsMAN complains. MikroTik Documentation states that is invalid configuration.So do I correctly understand you that on the qcom-ac (non-ax) devices the vlan configuration is working without adding the slave-static interfaces to the bridge by just setting the datapath? Even though they say "unsupported" in the documentation? I never ever tried to do that because I thought it won't work or maybe cause bugs/misconfiguration.Hopefully MT will get this fixed, as the whole CAPsMAN is kind of useless when using qcom-ac devices. In my opinion the greatest advantage was the central configuration of vlan's on the CAPsMAN. I do not want to fix all my 8 AP's vlan configuration each time I do an upgrade, reprovision or configuration change. I also hope cAP-ac is not end of life yet, I think there might be a plenty of users who would appreciate if this gets fixed.Switching back to the old wireless driver (that acutally worked pretty well!!) is for me also not an option because it lacks the WPA3 encryption and 802.11r.Sorry for the confusion, I was just mentioning that I went against their documentation and tested by creating seperate dedicated datapaths for the new qcom-ac access points. I had already created the newer datapaths, but went and specified VLAN-ID's for each SSID/datapath.the vlan-id pushes to the qcom-ac [non-ax] caps - and has PVID, all looks nominal. However CAPsMAN complains and then drops connections to the CAP. Appears this is still a software bug or limitation.... very unfortunate and fustrating. It does make the existing "WiFi5" AP's seem legacy with the new CAPsMAN "WIFI" configuratiaon. Further, it seems the qcom-ac driver is only geared for SOHO -- fitting the MikroTik nichce market.Love hate relationship with MikroTik, where they are still confused as to what they are and can do [What market they want to fit into]. I fear we are limited by software at this time.For us, It is either we start replacing the existing MikroTik AC devices with their new outdoor AX units -- which will require ALL new switching infrastructure [no more 802af standard], or we swap out for other vendor. ---

## Response 4
Author: Thu Aug 08, 2024 8:10 am
For us, It is either we start replacing the existing MikroTik AC devices with their new outdoor AX units -- which will require ALL new switching infrastructure [no more 802af standard], or we swap out for other vendor.Or wait for true wAP AX which surely will use 802af (like cap AX does).But that new wAP however is being teased for quite a while already (I have to look back but at least since early this year). ---

## Response 5
Author: Fri Aug 09, 2024 6:34 pm
Maybe some MT staff can tell more about this. Can we ever expect that vlan with datapath will work withqcom-ac? I hope so. I don't know any implementation details, but is it really that hard to implement this? ---

## Response 6
Author: Fri Aug 09, 2024 11:04 pm
I've resorted to removing the wifi-qcom-ac drivers and going back to the original WiFi5. Too many issues, and the CAPS became unstable with wireless connections to end-users / devices.Also, when you "provision" the CAP via CAPsMAN -- it causes the CAP WLAN interface to increment and break VLAN assignments. Only a rebooting the CAP fixes it and brings back the original number of WLAN interfaces [sub-interfaces].I feel since 7.12+. wireless has not be as stable. ---

## Response 7
Author: Sat Aug 10, 2024 2:17 pm
viewtopic.php?p=1065672 ---

## Response 8
Author: Sun Aug 11, 2024 4:44 pm
I've look through your interesing examples. But I think they would also suffer from this problem, as you use the names of the CAPsMAN wifi interfaces (wifi1, wifi2, ...) in your bridge vlan configuration. This is actually the point that does not work in my setup. After reprovisioning their numbers would increase and do not match anymore. ---

## Response 9
Author: Mon Aug 12, 2024 11:36 pm
I echo what @Robtor says.I have open ticket(s) with MikroTik support regarding this issue. Can others also open tickets regarding the wifi-qcom-ac and the dynamic wlan issue? ---

## Response 10
Author: Tue Aug 13, 2024 11:19 pm
I lastly read through the changelog of 7.16rc and found the following, that sounds interesting in this context.*) wifi - added "slave-name-format";If this won't fix the problem after 7.16 is fully released as stable, I would probably generate a supout and send it to Mikrotik support.But I'm still hoping that they implement the vlan tagging on qcom-ac over Capsman data paths. It would be really sad if that does not work. Another solution for my personal situation would also be WPA3 support in normal wireless stack. ---

## Response 11
Author: Wed Aug 14, 2024 7:40 am
Will see, but I am doubtful of 7.16 fixing this issue at this time. I feel MikroTik is still figuring out the Qualcom drivers...I think this fix for *) Wifi - added "slave-name-format" is for applying proper name to dynamic interfaces. I am specifying 2G-%I or 5G-%I for the interfaces. However, since 7.1X release and with QCOM-AC --- it's not 100%. Unless its a display issue with Winbox. I feel CAPsMAN v2 did a better job of displaying the slave or sub-wifi interfaces. ---

## Response 12
Author: [SOLVED]Thu Aug 15, 2024 10:15 am
After asking about this functionality I received the following answer:robtor"wifi - added "slave-name-format";" just adds more control on how virtual interfaces can be named.Regarding the forum post you linked, a lot of issues can be caused by re-provision, there seems to be a misconception that configuration needs to be "pushed" via help of provisioning the interfaces. That is not the case, provision must be done only initially, and is done automatically upon CAP joining if there are matching provisioning rules that are enabled.If you adjust any configuration profile that is linked to provisioned interface, all changes will be "pushed" as soon as you apply changes to the profile. With no need to re-create already existing interface.Provisioning itself is not for sending configuration, it is for essentially creating a new interface. In most cases, there is no reason to perform manual provisioning once you already have CAP interfaces running.Now, if create-enabled together with slave-static is used and interface names change after reboot or upgrade, please let us know viasupport@mikrotik.comalong with details of what was upgraded/rebooted. In our tests, names should not change, and references to CAP interfaces should work, and not be lost, both on CAPsMAN and CAP side, even if virtual CAP interface is renamed on CAP.At least it is not the solution for my problem, but, and I say many thanks to @Guntis for that, I totally misunderstood the purpose of the provisioning function.As I now understand correctly, the use of theProvisionbutton in winbox or the corresponding command is not necessary when changing configurations. As it is only for creating the new (virtual) interfaces on the CAPs.It's a pity that this command is not documented, because from the naming I always thought it means "push all new configuration to the CAPs". I used it andneververified if the configuration was already on the CAPs beforeThe explanation by @Guntis is from this thread:viewtopic.php?t=209903 ---

## Response 13
Author: Fri Aug 16, 2024 8:45 pm
@Robtor - thanks for sharing this information.it is very unclear and yet to be documented "feature" regarding the Provisioning functionality. It does not do what we logically think it'll do, so why is the Provision function there? ---

## Response 14
Author: Fri Aug 16, 2024 9:06 pm
Documented here:https://help.mikrotik.com/docs/display/ ... ovisioning ---

## Response 15
Author: Sat Aug 17, 2024 12:40 am
@infaboThank you for the link. I lastly searched for "provisioning" in the wifi docs and did not find anything. Sobi looked through the change history and found that they recently added those necessary information.https://help.mikrotik.com/docs/pages/di ... Version=47But with this documentation this case is clear!And special thanks to @Guntis to clarify the case and add the documentation!