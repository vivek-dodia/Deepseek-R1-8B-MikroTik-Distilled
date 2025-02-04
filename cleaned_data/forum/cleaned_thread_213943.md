# Thread Information
Title: Thread-213943
Section: RouterOS
Thread ID: 213943

# Discussion

## Initial Question
Hi guys, please bare with me for a while ...I have a RB960PGS and I thought it could be used for powering 4 Raspberry Pi 5's that are equipped with M.2/PoE hats used for 37+ Volt ... and yes, I did replace the PSU with one providing 48V and 2A.All I really need from the PoE hEX is the power and the ability to run Vlan's, no routing, no firewalling, nothing ...Started of by configuring the L2 on the Ether1 - 5 using a Bridge, all was fine but it degraded the bandwidth from around 930 Mbps as I was used to and I got around 860...ish... instead, good but not ok due to my OCD ...... so I inserted a 1 Gbps SFP into the SFP bay, purely for management and configured an IP address and nothing else, as I said it was just for management, even disabled IP forwarding in IP settings ...Port Ether1 is the trunk to my uplink switch, running an unused Vlan as default and then Vlan 100 and 68 tagged, same from the uplink switch. On port Ether 2 - 5, the PoE ports, the Raspberry Pi's are connected, all with Vlan 100 as default ( =untagged) and Ether2 and 5 also have Vlan 68 tagged. All this is done solely in the Switch configuraton of the PoE hEX, nothing is done under Bridge or Interfaces, nothing and it works great giving me the bandwidth I want ... except ...... once every 20-30 hours I lose connectivity to one, as it seem, random Raspberry Pi, they are stil active on their ethernet interface, I can see both rx and tx traffic but I lose IP connectivity to them, on all ports they should respond to. Now, this did not seem to happen when I used the Bridge configuration which I did for more than a week ...Any ideas or similar experiences?Have a nice evening!//Anders ---

## Response 1
There are many examples of such in the forums, and also a ref with examples.viewtopic.php?t=143620 ---

## Response 2
I don't think that covers using the Qualcom/Atheros switch chip in the hEX PoE, only VLAN-aware bridges which would be handled by the CPU in this case and not achieve anything near wire-speed throughput.I've not had any slowdowns when configuring VLAN support directly on the switch chip, the existing configuration may provide a clue. ---

## Response 3
There are many examples of such in the forums, and also a ref with examples.viewtopic.php?t=143620Thanks for replying, I read through the referenced topic but could not really see the connection to my issue with lost connectivity, sorry ...Have a good one.//Anders ---

## Response 4
I've not had any slowdowns when configuring VLAN support directly on the switch chip, the existing configuration may provide a clue..Hi, thanks for replying.Do you mean the configuration when configure the interfaces using bridge mode or the configuration as I have now only using the switch setup?Have a nice day,//Anders ---

## Response 5
Here is all relevant documentation on how to configure:https://help.mikrotik.com/docs/spaces/R ... upExamplesMake sure you read all comments on the QCA8337, because it has some exceptions.Can you share the current config?
```
/export file=anynameyoulikeRemove serial and any other private info, post between code tags by using the </> button.

---
```

## Response 6
Here is all relevant documentation on how to configure:https://help.mikrotik.com/docs/spaces/R ... upExamplesMake sure you read all comments on the QCA8337, because it has some exceptions.Can you share the current config?
```
/export file=anynameyoulikeRemove serial and any other private info, post between code tags by using the </> button.-Hi again, here are the config rows related to the switched ports.# 2025-01-17 07:50:09 by RouterOS 7.17## model = RB960PGS# serial number = xxxxxxxxxxxxx/interface bridgeadd name=bridge1 pvid=100 vlan-filtering=yes/interface wireless security-profilesset [ find default=yes ] supplicant-identity=PoE-RTR-1/interface bridge portadd bridge=bridge1 interface=ether2 pvid=100add bridge=bridge1 interface=ether3 pvid=100add bridge=bridge1 interface=ether4 pvid=100add bridge=bridge1 interface=ether5 pvid=100add bridge=bridge1 interface=ether1 pvid=100/interface bridge vlanadd bridge=bridge1 tagged=bridge1,ether1 untagged=ether2,ether3,ether4,ether5 \vlan-ids=100add bridge=bridge1 tagged=ether1,ether2,ether5 vlan-ids=68/interface ethernet switch vlanadd independent-learning=yes ports=ether1,ether2,ether3,ether4,ether5 switch=\switch1 vlan-id=100add independent-learning=yes ports=ether1,ether2,ether5 switch=switch1 \vlan-id=68... when using bridge mode, immediately losing apps. 50-60 Mbps upload, not as much down ...Have a nice day,//Anders

---
```

## Response 7
All is currently handled by the CPU, while you should have VLAN filtering handled by the switch chip.Something like this should work:
```
/interface bridge
add name=bridge1 protocol-mode=none

/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=PoE-RTR-1

/interface bridge port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5

/interface ethernet switch port
set 0 vlan-mode=secure
set 1 vlan-mode=secure
set 2 default-vlan-id=100 vlan-mode=secure
set 3 default-vlan-id=100 vlan-mode=secure
set 4 vlan-mode=secure
set 5 vlan-mode=secure

/interface ethernet switch vlan
add independent-learning=no ports=ether1,ether2,ether3,ether4,ether5 switch=switch1 vlan-id=100
add independent-learning=no ports=ether1,ether2,ether5 switch=switch1 vlan-id=68Please check the attached link for full explanation.Btw, above config is based on a v6 config. Might be some small differences.

---
```

## Response 8
All is currently handled by the CPU, while you should have VLAN filtering handled by the switch chip.Something like this should work:
```
/interface bridge
add name=bridge1 protocol-mode=none

/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=PoE-RTR-1

/interface bridge port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5

/interface ethernet switch port
set 0 vlan-mode=secure
set 1 vlan-mode=secure
set 2 default-vlan-id=100 vlan-mode=secure
set 3 default-vlan-id=100 vlan-mode=secure
set 4 vlan-mode=secure
set 5 vlan-mode=secure

/interface ethernet switch vlan
add independent-learning=no ports=ether1,ether2,ether3,ether4,ether5 switch=switch1 vlan-id=100
add independent-learning=no ports=ether1,ether2,ether5 switch=switch1 vlan-id=68Please check the attached link for full explanation.Btw, above config is based on a v6 config. Might be some small differences..Thank you so much for this, I will look into this later today.Have a nice day!//Anders

---
```

## Response 9
All is currently handled by the CPU, while you should have VLAN filtering handled by the switch chip..Hi agin, based on your suggested config I actually just added .../interface ethernet switch portset 1 vlan-mode=secureset 2 default-vlan-id=100 vlan-mode=secureset 3 default-vlan-id=100 vlan-mode=secureset 4 default-vlan-id=100 vlan-mode=secureset 5 default-vlan-id=100 vlan-mode=secure/interface ethernet switch vlanadd independent-learning=no ports=ether1, ether2, ether3, ether4, ether5 switch=switch1 vlan-id=100add independent-learning=no ports=ether1, ether2, ether5 switch=switch1 vlan-id=68... and this is pretty much all I need as it seem. This also give me full interface speed ... but I will continue to go through the referenced link as well.Have a nice weekend.//Anders ---