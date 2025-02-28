# Thread Information
Title: Thread-1117281
Section: RouterOS
Thread ID: 1117281

# Discussion

## Initial Question
Hi, I recently bought CCR2004-16g-2S+ model to replace my CRS326-24G-2S+. I was hoping to achieve 1Gbit network speed.But new device has issues in connecting dhcp clients to the gateway. I did fully the same setup as on the old device. But still unable to connect.The only difference I see is routeros version: 7.16.12 vs 6.49.13I see dhcp sends dicover request but it does not receives offer request.I am not able to find any differences in the setup.Here is log for dhcp client from CCR2004-16g-2S+:CCR2004-16g-2S-log.pngAnd on CRS326-24G-2S+:CRS326-24G-2S-log.pngWhat I am trying to achieve is to use sfp interface as source of the internet. Just like it was on older device.Here is my config:
```
# 1970-01-02 12:36:58 by RouterOS 7.16.2# software id = xxxxxxxxxx## model = CCR2004-16G-2S+# serial number = xxxxxxx/interfacebridgeaddname=bridge/interfaceethernetset[finddefault-name=sfp-sfpplus1]advertise=\1G-baseT-half,1G-baseT-full,1G-baseX/interfacelistaddname=WANaddname=LAN/ip pooladdname=dhcp ranges=192.168.88.2-192.168.88.254/ip dhcp-serveraddaddress-pool=dhcpinterface=bridge name=dhcp1/portset0name=serial0/interfacebridge portaddbridge=bridgeinterface=ether1addbridge=bridgeinterface=ether2addbridge=bridgeinterface=ether3addbridge=bridgeinterface=ether4addbridge=bridgeinterface=ether5addbridge=bridgeinterface=ether6addbridge=bridgeinterface=ether7addbridge=bridgeinterface=ether8addbridge=bridgeinterface=ether9addbridge=bridgeinterface=ether10addbridge=bridgeinterface=ether11addbridge=bridgeinterface=ether12addbridge=bridgeinterface=ether13addbridge=bridgeinterface=ether14addbridge=bridgeinterface=ether15addbridge=bridgeinterface=ether16addbridge=bridge disabled=yesinterface=sfp-sfpplus1addbridge=bridge disabled=yesinterface=sfp-sfpplus2/interfacelist memberaddinterface=sfp-sfpplus1 list=WANaddinterface=bridge list=LANaddinterface=sfp-sfpplus2 list=WAN/ip addressaddaddress=192.168.88.1/24interface=bridge network=192.168.88.0/ip dhcp-clientaddcomment=comfortnetinterface=sfp-sfpplus1/ip dhcp-server networkaddaddress=192.168.88.0/24dns-server=192.168.88.1gateway=192.168.88.1\
    netmask=24/ip dnssetservers=8.8.8.8,8.8.4.4/ip firewall address-listaddaddress=10.0.0.0/16list=admin-accessaddaddress=192.168.0.0/16list=admin-access/system loggingaddtopics=dhcp/system notesetshow-at-login=no/system routerboard settingssetenter-setup-on=delete-keyI would appreciate for any help.Thank you!

---
```

## Response 1
Remove SFP ports from bridge "bridge" and let them belong just to WAN list if they are really WAN ports.You can create bridgeWAN and move them to that bridge and assign bridgeWAN to WAN list and assign DHCP client for bridgeWAN ---

## Response 2
Remove SFP ports from bridge "bridge" and let them belong just to WAN list if they are really WAN ports.You can create bridgeWAN and move them to that bridge and assign bridgeWAN to WAN list and assign DHCP client for bridgeWANThanks for the reply.I did what you have suggested. But unfortunatelly, it did not make any change.Here are logs from terminal:Bridge configuration (fyi, I used name bridge1 because it did not allow me to edit it for some reason):
```
/interfacebridge portaddbridge=bridgeinterface=ether1addbridge=bridgeinterface=ether2addbridge=bridgeinterface=ether3addbridge=bridgeinterface=ether4addbridge=bridgeinterface=ether5addbridge=bridgeinterface=ether6addbridge=bridgeinterface=ether7addbridge=bridgeinterface=ether8addbridge=bridgeinterface=ether9addbridge=bridgeinterface=ether10addbridge=bridgeinterface=ether11addbridge=bridgeinterface=ether12addbridge=bridgeinterface=ether13addbridge=bridgeinterface=ether14addbridge=bridgeinterface=ether15addbridge=bridgeinterface=ether16addbridge=bridge1interface=sfp-sfpplus1/interfacelist memberaddinterface=bridge1 list=WANaddinterface=bridge list=LANDhcp client logs:
```

```
15:41:57dhcp,debug,packetClient-Id=01-78-9A-18-FC-7E-6E15:42:04dhcp,debug,packet dhcp-client on bridge1 sending discoverwithid3455712930to255.255.255.25515:42:04dhcp,debug,packet     secs=3515:42:04dhcp,debug,packet     flags=broadcast15:42:04dhcp,debug,packet     ciaddr=0.0.0.015:42:04dhcp,debug,packet     chaddr=78:XXXXXXXXX15:42:04dhcp,debug,packetHost-Name="MikroTik"15:42:04dhcp,debug,packetMsg-Type=discover15:42:04dhcp,debug,packetParameter-List=Subnet-Mask,Classless-Route,Router,Static-Route,Domain-Server,NTP-Server,CAPWAP-Server,Vendor-Specific15:42:04dhcp,debug,packetClient-Id=01-78-9A-18-FC-7E-6Edhcp client status:
```

```
>ip dhcp-clientprintColumns:INTERFACE,USE-PEER-DNS,ADD-DEFAULT-ROUTE,STATUS# INTERFACE  USE-PEER-DNS  ADD-DEFAULT-ROUTE  STATUS;;;comfortnet0bridge1    yes           yes                searching...

---
```

## Response 3
Are you sure that WAN side has any DHCP server active? ---

## Response 4
Are you sure that WAN side has any DHCP server active?yes, because I can prove it on my old device. dhcp client on old device successfully connects to the same gateway. ---

## Response 5
Why introduce bridge1? There are many reasons not to have multiple bridges.But if necessary to have an additional bridge, can you set interface for DHCP-client to bridge1? ---

## Response 6
Why introduce bridge1? There are many reasons not to have multiple bridges.But if necessary to have an additional bridge, can you set interface for DHCP-client to bridge1?I did both way. assigned to bridge1 and directly to sfp-sfpplus1 interface. but no success.feels like sfp interface is not comunicating to remote gateway.I have checked interface status, it says status: link_ok. means module is working. ---

## Response 7
Same SFP+ module? Is CRS still getting IP connected to the same line? Maybe ISP has rule that expects only your "registered" MAC to ask for an IP so clone the CRS' interface MAC to the bridge1 or to the used SFP interface if it is moved out of the bridge1. ---

## Response 8
Same SFP+ module? Is CRS still getting IP connected to the same line? Maybe ISP has rule that expects only your "registered" MAC to ask for an IP so clone the CRS' interface MAC to the bridge1 or to the used SFP interface if it is moved out of the bridge1.Just checked that assumption.Moved sfp module from CCR to CRS. It works there. I successfully connected there. And got ip address from ISP.On CRS it works with any SFP module. So ISP does noth have rule that will bind MAC address. They just require new authorization when mac changes. but IP address always successfully assigns.I see loopback interface on CCR, could that have any impact on my issue?ccr-interfaces.png ---

## Response 9
Nevermind, I was commenting on a temporary setup, later corrected. ---

## Response 10
I finally found the issue. it comes up that the SFP modules I have been using on CRS model are not compatible on CCR model. After switching tohttps://mikrotik.com/product/s_rj10it finally worked. And I got my 1Gbit speed on my desktop.Just for information, CRS model was giving me half speed only (500 Mbit). Due to low performance cpu.Thank you all who replied. ---