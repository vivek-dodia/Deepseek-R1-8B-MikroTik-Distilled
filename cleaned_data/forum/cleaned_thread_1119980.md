# Thread Information
Title: Thread-1119980
Section: RouterOS
Thread ID: 1119980

# Discussion

## Initial Question
So I've got this scenario:my LAN is fully VLAN tagged, all MT gear is running 7.16.2 except wAP ax which is running 7.17I have hAP ac2 configured as main router and lately CAPsMAN. It doesn't have wifi-qcom-ac drivers installed, so it's wired-onlyI have wAP ax which runs wifi-qcom and can, thus, do VLANs in wifi driver. Hence it's possible to configure its wifiX interfaces as bridge ports and CAPsMAN provisions VLANs according to datapath config. Which means that adding slave SSIDs is done entirely via CAPsMAN.I have Audience. Since it's ac device, it runs wifi-qcom-ac driver which doesn't do VLANs in wifi driver. It's possible to configure VLANs by adding each of wifiX interfaces to bridge with pvid set as needed. And use datapath without vlan-id set on CAPsMAN to avoid warning about inability to handle VLAN ID.This kind of provisioning is error-prone and defeats most CAPsMAN benefits (enhanced mobility luckily remains).I don't have any idea about how to add slave SSID (which should be joined to different VID) to wifi-qcom-ac device (Audience) using CAPsMAN provisioning.Anybody having such combo working? ---

## Response 1
I don't have any idea about how to add slave SSID (which should be joined to different VID) to wifi-qcom-ac device (Audience) using CAPsMAN provisioning.I didn't even try, knowing that the limitation exists. Mikrotik says they keep working on wifi-qcom-ac, but I wouldn't hold my breath as you like to say. For me, such a hybrid setup is manageable in large homes where there are just units of ac devices and you don't want to throw all of them away at once, but for an enterprise installation, it is a voucher for a headache unless you manage to handle that using scripting.It would indeed make little sense to use CAPsMAN for the ac devices - if it wasn't for the steering.Anybody having such combo working?I currently do have multiple such combos:2×hAP ac², one of which is the main router and the other one is just an AP+bridge, 1×RB5009 as main router and CAPsMAN + 3×hAP ac² as APs and bridges, 1×hAP ax³ as the main router and 1×hAP ac² as an AP+bridge. ---

## Response 2
1×RB5009 as main router and CAPsMAN + 3×hAP ac² as APs and bridges, So how do you handle slave wifi interfaces in this scenario? ---

## Response 3
The way you have described in your point 4 - I've setslaves-staticunder/interface/wifi/captoyesand once capsman has created them, I've made those static interfaces access ports to the respective VLANs. I rarely use more than 3 SSIDs so it is not a big deal. ---

## Response 4
Ah, when looking at/interface/wifi/capI wasn't looking good enough ... and didn't see theslaves-staticsetting. Thank you for pointing it out. ---