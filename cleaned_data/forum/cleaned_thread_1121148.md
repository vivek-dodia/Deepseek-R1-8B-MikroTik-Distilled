# Thread Information
Title: Thread-1121148
Section: RouterOS
Thread ID: 1121148

# Discussion

## Initial Question
Hi.Can someone please confirm this is a right way to let tagged vlan50 incoming on WAN port ether1 to be routed to ether5 as untagged? (hap lite ac on default config)The set-up works, I'm just not sure if it's a correct way
```
/interfacevlanaddinterface=bridge name=br-vlan50 vlan-id=50/interfacevlanaddinterface=ether1 name=eth1-vlan50 vlan-id=50/interfacebridge portsetbridge=bridge pvid=50[findinterface="ether5"]/interfacebridge portaddbridge=bridgeinterface=eth1-vlan50 pvid=50/interfacebridge vlanaddbridge=bridge untagged=ether5,eth1-vlan50 vlan-ids=11,50/interfacebridgesetbridge vlan-filtering=yesIf not how can I set it? (since ether1 is not a part of bridge)

---
```

## Response 1
There a many different ways to solve this....The easiest Solution starting from the default config, 1. Remove ether5 from the default bridge2. Create VLAN50 on ether13. Create a new Bridge4. Assign both ether5 and eth1-vlan50 to the bridge ---

## Response 2
hAP lite ac has the Atheros8227 switch chip attached to the 5 ethernet port. To have hardware offload (wire speed switching) with VLAN support you should not use Bridge VLAN Filtering. And you should not create two bridges like @ConnyMercier suggested neither. Instead configure the VLAN using the /interface/ethernet/switch menu. You'll still create only one bridge, but do not turn on bridge vlan-filtering=yes. See the example here:https://help.mikrotik.com/docs/spaces/R ... upExamples ---

## Response 3
There a many different ways to solve this....The easiest Solution starting from the default config, 1. Remove ether5 from the default bridge2. Create VLAN50 on ether13. Create a new Bridge4. Assign both ether5 and eth1-vlan50 to the bridgemultiple bridge solution is something I am trying to get rid off since it's not suggested.hAP lite ac has the Atheros8227 switch chip attached to the 5 ethernet port. To have hardware offload (wire speed switching) with VLAN support you should not use Bridge VLAN Filtering. And you should not create two bridges like @ConnyMercier suggested neither. Instead configure the VLAN using the /interface/ethernet/switch menu. You'll still create only one bridge, but do not turn on bridge vlan-filtering=yes. See the example here:https://help.mikrotik.com/docs/spaces/R ... upExamplesThat will also not work since I can not switch port ether1 since it's not in a bridge... ---

## Response 4
That will also not work since I can not switch port ether1 since it's not in a bridge...There is nothing that prevents you from adding ether1 to the bridge, even if it's the WAN port. The Atheros8227 switch chip manages all 5 ethernet ports (unlike for instance the hEX refresh where ether1 is not part of the switch chip but connected to the CPU), with hardware VLAN support. You simply need to create a dummy VLAN, let's say VLAN 1000 and make ether1 a hybrid port, untagged for VLAN ID 1000 and tagged for VLAN ID 50. Your WAN interface is then the VLAN1000 interface, instead of ether1.In fact, I am running such configuration on my RB5009. That is also a router with a switch chip connecting all ethernet and SFP+ ports. My internet comes untagged on the SPF+ port. Instead of dialing PPPoE on the standalone sfp-sfpplus1 interface, I added that port to the main bridge (together with all the other ports), configure VLAN 1000, untagged on sfp-sfpplus1, then dial my PPPoE connection on the vlan1000 interface. It works perfectly because VLAN is handled in hardware by the switch chip. ---