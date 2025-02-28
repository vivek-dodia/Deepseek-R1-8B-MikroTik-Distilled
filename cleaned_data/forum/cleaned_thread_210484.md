# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210484

# Discussion

## Initial Question
Author: Wed Aug 28, 2024 11:34 am
Hi, I have a mikrotik CRS112 switch and there are multiple redundant paths leading to a single destination and for that we have configured RSTP but I see the below error message in my logs very frequently. I tried searching on the forum and tried several things like checking MAC duplication and RSTP config in my network but everything seems to be fine. I would be immensely grateful If anyone from the experts could kindly help me resolve this issue.Note: I have all of my ports under one bridge and I have attached a picture of the config as well. Kindly see the attachment.ether1: bridge port received packet with own address as source address (cc:2d:e0:xx:1c:xx), probably loop ---

## Response 1
Author: Wed Aug 28, 2024 11:37 am
``` 
```
/exportfile=anynameyoulike
```

Can you add both the logging and the config?Remove serial and any other private info, post in between code tags by using the </> button.


---
```

## Response 2
Author: Wed Aug 28, 2024 11:55 am
``` 
```
# aug/28/2024 11:47:57 by RouterOS 6.48.1# software id = LQ7H-557D## model = CRS112-8P-4S# serial number = xxxxx/interfacebridgeaddname=bridge1/interfaceethernetset[finddefault-name=ether1]comment=abcset[finddefault-name=ether2]comment=abc poe-out=forced-onset[finddefault-name=ether3]comment=abc poe-out=forced-onset[finddefault-name=ether4]comment=abc poe-out=forced-onset[finddefault-name=ether5]comment=abc poe-out=forced-onset[finddefault-name=ether6]comment=abc poe-out=forced-onset[finddefault-name=ether7]comment=abc/interfacevlanaddinterface=bridge1 name=br_vlan2251 vlan-id=2251/interfacelistaddname=bridge/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTik/snmp communityset[finddefault=yes]name=ghprivateccr/interfacebridge portaddbridge=bridge1interface=ether1internal-path-cost=30path-cost=30addbridge=bridge1interface=ether2addbridge=bridge1interface=ether3addbridge=bridge1interface=ether4addbridge=bridge1interface=ether5addbridge=bridge1interface=ether6 path-cost=50addbridge=bridge1interface=ether7internal-path-cost=12path-cost=12addbridge=bridge1interface=ether8addbridge=bridge1interface=sfp9addbridge=bridge1interface=sfp10addbridge=bridge1interface=sfp11addbridge=bridge1interface=sfp12/ip neighbor discovery-settingssetdiscover-interface-list=!dynamic/interfaceethernetswitchegress-vlan-tagaddtagged-ports="switch1-cpu,ether1,ether2,ether3,ether4,ether5,ether6,ether7\
    ,ether8,sfp10,sfp9,sfp12,sfp11"vlan-id=2251addtagged-ports="switch1-cpu,ether1,ether2,ether3,ether4,ether5,ether6,ether7\
    ,ether8,sfp10,sfp9,sfp12,sfp11"vlan-id=1013/interfaceethernetswitchvlanaddports="switch1-cpu,ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8\
    ,sfp10,sfp9,sfp12,sfp11"vlan-id=2251addports="ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8,sfp10,sfp9,\
    sfp12,sfp11"vlan-id=1013addports="switch1-cpu,ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8\
    ,sfp10,sfp9,sfp12,sfp11"vlan-id=2260/interfacelist memberaddinterface=bridge1 list=bridge/ip dhcp-clientadddisabled=nointerface=br_vlan2251/snmpsetenabled=yes/system clocksettime-zone-name=abc/abc/system identitysetname="abc(MKT)"/system loggingaddtopics=stpaddtopics=bridge/system routerboard settingssetauto-upgrade=yes
```

Thank you for a quick response.


---
```

## Response 3
Author: Sat Aug 31, 2024 1:07 pm
I would be grateful if anyone out there could help me resolve this issue. ---

## Response 4
Author: Sat Aug 31, 2024 2:09 pm
``` 
```
/logprint
```

I guess that what erlinden asked for as "logging" was meant as:and copy and paste a few related lines of the log around the "probably loop"  error you posted.


---
```

## Response 5
Author: Sun Sep 01, 2024 8:36 am
``` 
```
aug/2516:59:23bridge,stp ether1 learning 
aug/2516:59:23bridge,stp ether1 forwarding 
aug/2516:59:57bridge,stp ether1 discarding 
aug/2517:06:47bridge,stp ether1 learning 
aug/2517:06:47bridge,stp ether1 forwarding 
aug/2517:07:23bridge,stp ether1 discarding 
aug/2517:15:25bridge,stp ether1 learning 
aug/2517:15:25bridge,stp ether1 forwarding 
aug/2517:16:04bridge,stp ether1 discarding 
aug/2517:19:43bridge,stp ether1 learning 
aug/2517:19:43bridge,stp ether1 forwarding 
aug/2517:20:14bridge,stp ether1 discarding 
aug/2517:24:27bridge,stp ether1 learning 
aug/2517:24:27bridge,stp ether1 forwarding 
aug/2517:25:00bridge,stp ether1 discarding 
aug/2517:25:25bridge,stp ether1 learning 
aug/2517:25:25bridge,stp ether1 forwarding 
aug/2517:25:58bridge,stp ether1 discarding 
aug/2517:30:53bridge,stp ether1 learning 
aug/2517:30:53bridge,stp ether1 forwarding 
aug/2517:31:32bridge,stp ether1 discarding 
aug/2517:34:55bridge,stp ether1 learning 
aug/2517:34:55bridge,stp ether1 forwarding 
aug/2517:35:26bridge,stp ether1 discarding 
aug/2517:42:53bridge,stp ether1 learning 
aug/2517:42:53bridge,stp ether1 forwarding 
aug/2517:43:24bridge,stp ether1 discarding 
aug/2517:46:05bridge,stp ether1 learning 
aug/2517:46:05bridge,stp ether1 forwarding 
aug/2517:46:44bridge,stp ether1 discarding 
aug/2517:48:13bridge,stp ether1 learning 
aug/2517:48:13bridge,stp ether1 forwarding 
aug/2517:48:50bridge,stp ether1 discarding 
aug/2517:48:51interface,warning ether1:bridge port received packetwithownaddressassource address(cc:2d:e0:xx:xx:8d),probably loop 
aug/2517:50:40bridge,stp ether1 learning 
aug/2517:50:40bridge,stp ether1 forwarding 
aug/2517:51:14bridge,stp ether1 discarding 
aug/2517:55:37bridge,stp ether1 learning 
aug/2517:55:37bridge,stp ether1 forwarding 
aug/2517:56:08bridge,stp ether1 discarding 
aug/2517:59:45bridge,stp ether1 learning 
aug/2517:59:45bridge,stp ether1 forwarding 
aug/2518:00:10bridge,stp ether1 discarding 
aug/2518:04:37bridge,stp ether1 learning 
aug/2518:04:37bridge,stp ether1 forwarding 
aug/2518:05:08bridge,stp ether1 discarding 
aug/2518:20:33bridge,stp ether1 learning 
aug/2518:20:33bridge,stp ether1 forwarding 
aug/2518:21:14bridge,stp ether1 discarding 
aug/2518:25:01bridge,stp ether1 learning 
aug/2518:25:01bridge,stp ether1 forwarding 
aug/2518:25:34bridge,stp ether1 discarding 
aug/2518:28:27bridge,stp ether1 learning 
aug/2518:28:27bridge,stp ether1 forwarding 
aug/2518:28:58bridge,stp ether1 discarding 
aug/2518:45:19bridge,stp ether1 learning 
aug/2518:45:19bridge,stp ether1 forwarding 
aug/2518:45:58bridge,stp ether1 discarding 
aug/2518:52:05bridge,stp ether1 learning 
aug/2518:52:05bridge,stp ether1 forwarding 
aug/2518:52:38bridge,stp ether1 discarding 
aug/2518:53:15bridge,stp ether1 learning 
aug/2518:53:15bridge,stp ether1 forwarding 
aug/2518:53:48bridge,stp ether1 discarding 
aug/2518:56:58bridge,stp ether1 learning 
aug/2518:56:58bridge,stp ether1 forwarding 
aug/2518:57:30bridge,stp ether1 discarding 
aug/2519:00:29bridge,stp ether1 learning 
aug/2519:00:29bridge,stp ether1 forwarding 
aug/2519:01:08bridge,stp ether1 discarding 
aug/2519:06:25bridge,stp ether1 learning 
aug/2519:06:25bridge,stp ether1 forwarding 
aug/2519:06:58bridge,stp ether1 discarding 
aug/2519:12:29bridge,stp ether1 learning 
aug/2519:12:29bridge,stp ether1 forwarding 
aug/2519:13:02bridge,stp ether1 discarding 
aug/2519:34:03bridge,stp ether1 learning 
aug/2519:34:03bridge,stp ether1 forwarding 
aug/2519:34:42bridge,stp ether1 discarding 
aug/2519:43:49bridge,stp ether1 learning 
aug/2519:43:49bridge,stp ether1 forwarding 
aug/2519:44:20bridge,stp ether1 discarding 
aug/2520:01:51bridge,stp ether1 learning 
aug/2520:01:51bridge,stp ether1 forwarding 
aug/2520:02:30bridge,stp ether1 discarding 
aug/2520:04:23bridge,stp ether1 learning 
aug/2520:04:23bridge,stp ether1 forwarding 
aug/2520:04:44bridge,stp ether1 discarding 
aug/2521:44:59bridge,stp ether1 learning 
aug/2521:44:59bridge,stp ether1 forwarding 
aug/2521:44:59bridge,stp ether1 discarding 
aug/2521:45:08bridge,stp ether1 learning 
aug/2521:45:08bridge,stp ether1 forwarding 
aug/2521:45:39bridge,stp ether1 discarding 
aug/2522:17:41bridge,stp ether1 learning 
aug/2522:17:41bridge,stp ether1 forwarding 
aug/2522:18:29bridge,stp ether1 discarding 
aug/2522:22:42bridge,stp ether1 learning 
aug/2522:22:42bridge,stp ether1 forwarding 
aug/2522:23:13bridge,stp ether1 discarding 
aug/2522:24:00bridge,stp ether1 learning 
aug/2522:24:00bridge,stp ether1 forwarding 
aug/2522:24:37bridge,stp ether1 discarding 
aug/2522:26:12bridge,stp ether1 learning 
aug/2522:26:12bridge,stp ether1 forwarding 
aug/2522:26:45bridge,stp ether1 discarding 
aug/2522:30:03bridge,stp ether1 learning 
aug/2522:30:03bridge,stp ether1 forwarding 
aug/2522:30:35bridge,stp ether1 discarding 
aug/2522:36:24bridge,stp ether1 learning 
aug/2522:36:24bridge,stp ether1 forwarding 
aug/2522:37:01bridge,stp ether1 discarding 
aug/2522:59:03bridge,stp ether1 learning 
aug/2522:59:03bridge,stp ether1 forwarding 
aug/2522:59:49bridge,stp ether1 discarding 
aug/2523:34:31bridge,stp ether1 learning 
aug/2523:34:31bridge,stp ether1 forwarding 
aug/2523:35:23bridge,stp ether1 discarding 
aug/2523:36:10bridge,stp ether1 learning 
aug/2523:36:10bridge,stp ether1 forwarding 
aug/2523:36:43bridge,stp ether1 discarding 
aug/2523:56:05bridge,stp ether1 learning 
aug/2523:56:05bridge,stp ether1 forwarding 
aug/2523:56:45bridge,stp ether1 discarding 
aug/2600:06:38bridge,stp ether1 learning 
aug/2600:06:38bridge,stp ether1 forwarding 
aug/2600:07:09bridge,stp ether1 discarding 
aug/2600:12:01bridge,stp ether1 learning 
aug/2600:12:01bridge,stp ether1 forwarding 
aug/2600:12:23bridge,stp ether1 discarding 
aug/2600:12:37bridge,stp ether1 learning 
aug/2600:12:37bridge,stp ether1 forwarding 
aug/2600:12:38bridge,stp ether1 discarding 
aug/2600:53:00bridge,stp ether1 learning 
aug/2600:53:00bridge,stp ether1 forwarding 
aug/2600:53:01bridge,stp ether1 discarding 
aug/2600:53:09bridge,stp ether1 learning 
aug/2600:53:09bridge,stp ether1 forwarding 
aug/2600:53:39bridge,stp ether1 discarding 
aug/2602:18:35bridge,stp ether1 learning 
aug/2602:18:35bridge,stp ether1 forwarding 
aug/2602:18:41bridge,stp ether1 discarding 
aug/2603:29:16bridge,stp ether1 learning 
aug/2603:29:16bridge,stp ether1 forwarding 
aug/2603:29:53bridge,stp ether1 discarding 
aug/2603:30:27bridge,stp ether1 learning 
aug/2603:30:27bridge,stp ether1 forwarding 
aug/2603:31:01bridge,stp ether1 discarding 
aug/2603:31:09bridge,stp ether1 learning 
aug/2603:31:09bridge,stp ether1 forwarding 
aug/2603:31:11bridge,stp ether1 discarding 
aug/2603:55:24bridge,stp ether1 learning 
aug/2603:55:24bridge,stp ether1 forwarding 
aug/2603:55:57bridge,stp ether1 discarding 
aug/2605:19:37bridge,stp ether1 learning 
aug/2605:19:37bridge,stp ether1 forwarding 
aug/2605:20:25bridge,stp ether1 discarding 
aug/2605:30:40bridge,stp ether1 learning 
aug/2611:02:11bridge,stp ether1 learning 
aug/2611:02:11bridge,stp ether1 forwarding 
aug/2611:02:27bridge,stp ether1 discarding 
aug/2611:42:47bridge,stp ether1 learning 
aug/2611:42:47bridge,stp ether1 forwarding 
aug/2611:43:27bridge,stp ether1 discarding 
aug/2613:51:35bridge,stp ether1 learning 
aug/2613:51:35bridge,stp ether1 forwarding 
aug/2613:51:36bridge,stp ether1 discarding 
aug/2613:51:44bridge,stp ether1 learning 
aug/2613:51:44bridge,stp ether1 forwarding 
aug/2613:51:53interface,warning ether1:bridge port received packetwithownaddressassource address(cc:2d:e0:xx:xx:8d),probably loop 
aug/2613:52:16bridge,stp ether1 discarding 
aug/2614:01:06bridge,stp ether1 learning 
aug/2614:01:06bridge,stp ether1 forwarding 
aug/2614:01:38bridge,stp ether1 discarding 
aug/2614:22:54bridge,stp ether1 learning 
aug/2614:22:54bridge,stp ether1 forwarding 
aug/2614:23:34bridge,stp ether1 discarding 
aug/2615:09:58bridge,stp ether1 learning 
aug/2615:09:58bridge,stp ether1 forwarding 
aug/2615:10:38bridge,stp ether1 discarding 
aug/2615:29:22bridge,stp ether1 learning 
aug/2615:29:22bridge,stp ether1 forwarding 
aug/2615:30:00bridge,stp ether1 discarding 
aug/2618:00:58bridge,stp ether1 learning 
aug/2618:00:58bridge,stp ether1 forwarding 
aug/2618:01:51bridge,stp ether1 discarding 
aug/2618:01:52interface,warning ether1:bridge port received packetwithownaddressassource address(cc:2d:e0:xx:xx:8d),probably loop 
aug/2618:02:00bridge,stp ether1 learning 
aug/2618:02:00bridge,stp ether1 forwarding 
aug/2618:02:21bridge,stp ether1 discarding 
aug/2618:50:56bridge,stp ether1 learning 
aug/2618:50:56bridge,stp ether1 forwarding 
aug/2618:51:29bridge,stp ether1 discarding 
aug/2620:33:38bridge,stp ether1 learning 
aug/2620:33:38bridge,stp ether1 forwarding 
aug/2620:34:17bridge,stp ether1 discarding 
aug/2621:00:34bridge,stp ether1 learning
```

Thank you for the guidance.


---
```

## Response 6
Author: Tue Sep 03, 2024 1:03 pm
Anyone from the experts ? ---

## Response 7
Author: Sat Sep 07, 2024 11:00 am
I have also updated the firmware from version 6.48 to 6.49. My bridge is in the RSTP mode and ether1 is an alternate port but I keep noticing in the logs that this port goes into the learning, forwarding and discarding state although it's an alternate port and according to my understanding it should remain in the discarding state.Bridge has MAC of this ether1 about which I am talking about.I have posted the config and logs in my previous posts. I think I'm quite near to resolving this error but need an opinion from the experts since it's my production environment. ---

## Response 8
Author: Sat Sep 07, 2024 10:39 pm
Try to set MAC of bridge manually ... to MAC different than any of bridge ports. For ideas about proper MAC address "invention", have a look atUniversal vs. local (U/L bit)section ofMAC addresswikipedia article (use MAC address of one of bridge ports as a basis and apply the L bit to it). ---

## Response 9
Author: Sun Sep 08, 2024 9:07 am
how about if you play with:port-cost-mode=short ---

## Response 10
Author: Sun Sep 08, 2024 11:16 am
how about if you play with:port-cost-mode=shortI have port cost enabled on different ports since there's redundancy and RSTP enabled but currently I have disabled this ether1. ---

## Response 11
Author: Sun Sep 08, 2024 11:24 am
``` 
```
Error:vlan2251:bridge RX looped packet-MAC e4:8d:8c:3a:x:x->ff:ff:ff:ff:ff:ff ETHERTYPE0x0806
```

Try to set MAC of bridge manually ... to MAC different than any of bridge ports. For ideas about proper MAC address "invention", have a look atUniversal vs. local (U/L bit)section ofMAC addresswikipedia article (use MAC address of one of bridge ports as a basis and apply the L bit to it).My bridge has MAC from ether1 which I disabled and the management vlan on bridge also has same MAC but upon disabling the ether1 port, bridge didn't change its MAC and neither I loose the access to my device. So, is there any chance that the bridge changes its MAC in the future and better to take precautions to avoid any access issues ?The reason why i disabled the ether1 port is because I occasionally loose access to my all devices on management vlan 2251 for about few second and sometimes about 10-15 seconds and I suspect this occurs whenever the ether1 port changes its STP states frequently on the mikrotik switch under discussionSince firmware upgradation I haven't received any loop packets message in this device but my DHCP router for all network management vlans is also a mikrotik and I see loop broadcast message for this management vlan repeatedly at different intervals.


---
```

## Response 12
Author: Sun Sep 08, 2024 11:47 am
I think the advise was to make your MAC static and different from any other one you have on that machine, see this:viewtopic.php?t=190747There are reports that the mechanism the RoS uses to auto-assign MAC can, in certain situations, change the MAC, creating havoc in certain setups and having it fixed is usually recommended, the discussion/debate is more whether the static, manually assigned MAC should (or should not) be the same as that of one of the interfaces belonging to the bridge.This is what RoS normally does (the bridge "inherits" the MAC of the first interface of the bridge, but irn some cases the order of interfaces or *whatever* makes the MAC change.If you want to invent your own, there are a couple rules on how the MAC should be generated, a "random" one will probably create issues, see:viewtopic.php?t=177585#p873414 ---

## Response 13
Author: Sun Sep 08, 2024 12:09 pm
As mentioned earlier we're WISP company and in the attached file I have tried to brief little about our structure.In the Ubuiqiti SW I have MSTP enabled whereas on Mikrotik Main SW and Mikrotik SW (Switch under discussion on this ticket) have RSTP enabled.Currently I don't see any loop messages on the Mikrotik SW but still face these broadcast messages on the Mikrotik Main switch on ether3 port which is connected to the Ubiquiti SW and on the DHCP RTR which I shared in my previous response.The Mikrotik SW has redundant paths leading to Mikrotik Main SW and ether1(alternate port) which I disabled on this Mikrotik SW is the link connected to the Ubiquiti SW.The problem is that I loose access to all my devices in the network which are managed under vlan 2251 for a few seconds(like consecutive 10-20 packet losses ).I have checked logs of all the devices(some 25-30 devices) managed under vlan 2251 and the topology picture I shared of the devices I suspect the issue is anywhere among them because of the reasons I cited above.I hope this helps in knowing more about the issue and offering any help that could help me resolve the issue. ---

## Response 14
Author: Sun Sep 08, 2024 12:18 pm
Mixing MSTP and RSTP is at least part (if not the whole) if your problem. RSTP is not VLAN aware and blocks physical link if it detects a loop (the error message, mentioned in this thread's title, does indicate this condition), while with MSTP it's possible to distribute VLANs over multiple physical links (for better throughput) and they will all move to single link if other redundant links fail.So either configure your MT to use MSTP (not possibke with all devices) or reconfigure the rest of infrastructure to use RSTP ... or consider using MLAG for links that require redundancy if that's feasible in your use case. ---

## Response 15
Author: Sun Sep 08, 2024 12:36 pm
Mixing MSTP and RSTP is at least part (if not the whole) if your problem. RSTP is not VLAN aware and blocks physical link if it detects a loop (the error message, mentioned in this thread's title, does indicate this condition), while with MSTP it's possible to distribute VLANs over multiple physical links (for better throughput) and they will all move to single link if other redundant links fail.So either configure your MT to use MSTP (not possibke with all devices) or reconfigure the rest of infrastructure to use RSTP ... or consider using MLAG for links that require redundancy if that's feasible in your use case.We're using a lot of mikrotik devices and in those we have RSTP enabled and two-three ubiquiti devices are configured with MSTP. I am reffering to devices managed under vlan 2251 for the management access.I will configure the Ubiquiti SWs to use RSTP but the little I know about these spanning trees protocols is that both RSTP and MSTP are compatible with each other so should it be the problem or part of it ?On the error message, My RSTP config is correct on this Mikrotik SW as you can see in the first post where I have pasted a picture of the bridge section as well, but to be precise why I am receiving this loop error ? is it only because of MSTP and RSTP ? ---

## Response 16
Author: Sun Sep 08, 2024 12:55 pm
... spanning trees protocols is that both RSTP and MSTP are compatible with each other so should it be the problem or part of it ?Various STP protocols may be compatible in a sense that message, created by one of those, can be processed by the others. However the way these protocols work out the hierarchy of links is incompatible between them, so it's almost required to operate whole infrstructure using one of them ... obviously the one supported by all infrastructure devices.You seem not to take my words for granted. Which is absolutely fine. But in this case the one thing you should get from my posts is that you'll have to learn about differencies between the various xSTP protocols yourself and then decide the way you want to go. ---

## Response 17
Author: Sun Sep 08, 2024 1:20 pm
... spanning trees protocols is that both RSTP and MSTP are compatible with each other so should it be the problem or part of it ?Various STP protocols may be compatible in a sense that message, created by one of those, can be processed by the others. However the way these protocols work out the hierarchy of links is incompatible between them, so it's almost required to operate whole infrstructure using one of them ... obviously the one supported by all infrastructure devices.You seem not to take my words for granted. Which is absolutely fine. But in this case the one thing you should get from my posts is that you'll have to learn about differencies between the various xSTP protocols yourself and then decide the way you want to go.Alright, thank you. Let me configure RSTP in my ubiquiti SWs as well and come back to you. Also I am going through the MAC invention link which you shared eariler to create a MAC and use it for the bridge in the Mikrotik SW. ---

## Response 18
Author: [SOLVED]Wed Sep 18, 2024 8:57 am
In my earlier posts I had shared logs of ether1 where it was seen that the port was changing it's state continuously although it was an alternative port. As soon as I disabled this port (as I had redundancies so everything still worked fine) I stopped encountering these loop packet messages and the packet losses issue in the whole network. ---

## Response 19
Author: Wed Sep 18, 2024 8:58 am
... spanning trees protocols is that both RSTP and MSTP are compatible with each other so should it be the problem or part of it ?Various STP protocols may be compatible in a sense that message, created by one of those, can be processed by the others. However the way these protocols work out the hierarchy of links is incompatible between them, so it's almost required to operate whole infrstructure using one of them ... obviously the one supported by all infrastructure devices.You seem not to take my words for granted. Which is absolutely fine. But in this case the one thing you should get from my posts is that you'll have to learn about differencies between the various xSTP protocols yourself and then decide the way you want to go.I have reconfigured my UBNT switches as well with RSTP protocol as my mikrotik devices are running RSTP. Thank you for your assistance.