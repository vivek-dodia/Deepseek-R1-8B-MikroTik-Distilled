# Thread Information
Title: Thread-213903
Section: RouterOS
Thread ID: 213903

# Discussion

## Initial Question
I have a setup of a Hex RB750Gr3 (7.16.2) and a couple of Unifi UAP AC Pro. The one UAP is connected to a switch that is in ether4 of the hEX, and the other to a switch that is in ether5. Both switches are just dumb ones.If I have two devices on e.g. the upstairs AP and I move on downstairs for one of the devices to roam to the AP downstairs, I will lose connectivity to the other device - I can see how pinging stops to work. After a little while, seemingly random, connectivity suddenly comes back. I've tried with multiple devices and the time it takes varies.If I connect both APs to the same switch, there are no trouble which is why I suspect the router.The config of the hEX is pretty default, I see nothing in the bridge or port config that should be causing issues. ARP config etc. is default:
```
/interfacebridgeaddcomment=defconf name=bridge port-cost-mode=short/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacebridge portaddbridge=bridge comment=defconf ingress-filtering=nointerface=ether2internal-path-cost=10path-cost=10addbridge=bridge comment=defconf ingress-filtering=nointerface=ether3internal-path-cost=10path-cost=10addbridge=bridge comment=defconf ingress-filtering=nointerface=ether4internal-path-cost=10path-cost=10addbridge=bridge comment=defconf ingress-filtering=nointerface=ether5internal-path-cost=10path-cost=10/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacedetect-internetsetdetect-interface-list=all/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WANDoes anyone have any pointer for what I can try to troubleshoot this?

---
```

## Response 1
You described using PING in your diagnosis, as you are roaming from one AP to another....Did you PING a local Device or something on the Internet like 8.8.8.8?Secondly, do you see something in the Logfiles of the Router as you are roaming from one AP to another ? ---

## Response 2
You described using PING in your diagnosis, as you are roaming from one AP to another....Did you PING a local Device or something on the Internet like 8.8.8.8?Secondly, do you see something in the Logfiles of the Router as you are roaming from one AP to another ?I'm pinging the other device, connected to the AP. The entire problem is losing connectivity to this device or any other under same circumstance ---