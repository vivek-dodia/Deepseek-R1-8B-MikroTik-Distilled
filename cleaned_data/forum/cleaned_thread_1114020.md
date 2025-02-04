# Thread Information
Title: Thread-1114020
Section: RouterOS
Thread ID: 1114020

# Discussion

## Initial Question
I use the CRS-317 switch as a transparent bridge with Spanning Tree set to 'none'. One of my clients uses their own RSTP configuration for redundancy, and their traffic, including STP packets, must be transmitted through this switch in a dedicated VLAN without any STP packet blocking/modifing etc.This setup worked flawlessly for many years. Two days ago, I upgraded from version 6.49 to 7.16.2 and immediately noticed a loop on the client’s network because their RSTP stopped being forwarded.I studied the changelogs and found a new disabled option called forward-reserved-addresses. I enabled it, but it had no positive effect—STP packets still don’t pass through.Has anyone encountered a similar issue? How can STP packets now be forwarded transitively in a VLAN? ---

## Response 1
hello, I'm sorry I don't quite understand this partuse the CRS-317 switch as a transparent bridge. Spanning tree is set to "none," and one of my clients, through this switch, uses their own RSTP in a dedicated VLAN for redundancy.did you mean your client set their own vlan - and you let their vlan traversing your transparent switch? or something else? ie. qinq or something?i think spanning tree set to none - literally mean you are allowing loops to happen on your switch or on your network. will the switch work?? yes - but you should see how much tx/rx errors in your switch.now - their rstp didn't work. that is a saviour on your switch and your network.or maybe I'm missing something? ---

## Response 2
I'm sorry I don't quite understand this partLet’s make it simpler: I need RSTP packets to pass through without any processing/modifing/blocking. I need a fully transparent bridge. Previously, simply disabling STP by setting it to "none" allowed this to happen. But now, I can't manage to get RSTP packets to pass through the transit VLAN on this switch.And the most confusing thing for me: the new option forward-reserved-addresses, which is supposed to restore the old behavior (pass through STP forwarding), doesn’t work!What should I do? Roll back to ROS 7.15.3? ---

## Response 3
What should I do? Roll back to ROS 7.15.3?it's definitely your callnext time - if i were you, i will definitely test drive first before live in production.if it is really important for you - try to reach the mt support. good luck ---

## Response 4
Hi, I wasn’t able to reproduce the same results in our lab. The forward-reserved-addresses=yes setting does forward all the reserved MACs 01:80:C2:00:00:0x, whether they are tagged or untagged.Maybe there is something else to blame here. Could you share your full export and clarify which switch ports and VLANs the BPDUs should be forwarded between? ---

## Response 5
Could you share your full export and clarify which switch ports and VLANs the BPDUs should be forwarded between?Thanks for your help.I have attached part of the exported config.RSTP blocked at 510, 511 vlan between sfp-sfpplus4 and sfp-sfpplus8. ---

## Response 6
Thanks.I was able to pass through tagged BPDUs with VLAN IDs 510, 511 using your configuration on CRS317 running 7.16.2.So I suspect one of these issues:1. sfp-sfpplus4, sfp-sfpplus8 do not even receive BPDUs.2. received BPDUs are untagged and does not get forwarded through CRS317 due to sfp-sfpplus4 and sfp-sfpplus8 being configured with isolated untagged VLANs (515 and 104).3. tagged BPDUs 510, 511 are forwarded, but dropped somewhere else along the path.You can conclude further by making an ACL rule to "copy-to-cpu" and running sniffer on these ports. It will display the VLAN ID and only the Rx traffic, the Tx will not be shown because the switch is already doing the forwarding (if the configuration allows it). Your configuration did not include switch rules, so I assume you do not have them configured.Try adding this rule and share the output of sniffer command:
```
/interfaceethernetswitchruleaddcopy-to-cpu=yes dst-mac-address=01:80:C2:00:00:00/FF:FF:FF:FF:FF:FF ports=sfp-sfpplus4,sfp-sfpplus8switch=switch1/tool sniffer quickinterface=sfp-sfpplus4,sfp-sfpplus8 mac-address=01:80:C2:00:00:00

---
```

## Response 7
Try adding this rule and share the output of sniffer command:[/code]Everything looks correct on the incoming traffic to sfp-sfpplus4, but there is no outgoing RSTP on sfp-sfpplus8 (sfp-sfpplus4 0.386 1 <- 02:95:88:05:73:54 01:80:C2:00:00:00 10 802.2 64 1sfp-sfpplus4 0.386 2 <- 02:95:88:05:73:54 01:80:C2:00:00:00 7 802.2 64 1sfp-sfpplus4 0.386 3 <- 02:95:88:05:73:54 01:80:C2:00:00:00 9 802.2 64 1sfp-sfpplus4 0.386 4 <- 02:95:88:05:73:54 01:80:C2:00:00:00 510 802.2 64 1sfp-sfpplus4 0.565 5 <- C4:AD:34:0F:62:19 01:80:C2:00:00:00 511 802.2 64 1sfp-sfpplus4 2.384 6 <- 02:95:88:05:73:54 01:80:C2:00:00:00 510 802.2 64 1sfp-sfpplus4 2.384 7 <- 02:95:88:05:73:54 01:80:C2:00:00:00 10 802.2 64 1sfp-sfpplus4 2.384 8 <- 02:95:88:05:73:54 01:80:C2:00:00:00 7 802.2 64 1sfp-sfpplus4 2.384 9 <- 02:95:88:05:73:54 01:80:C2:00:00:00 9 802.2 64 1sfp-sfpplus4 2.567 10 <- C4:AD:34:0F:62:19 01:80:C2:00:00:00 511 802.2 64 1To monitor outgoing packets, I had to add a second mirroring rule to the CPU for sfp-sfpplus8and set 01:80:C2:00:00:00 as the source. ---

## Response 8
Sniffer will not show outgoing traffic when using HW offloaded bridge, it is expected behavior.If you really want to check whether tagged BPDU packets are being sent from the sfp-sfpplus8 interface, you need to perform packet capture on the device at the other end of the link. Based on my tests, the packets should be outgoing.If capturing traffic on the other device isn’t an option, you can use the mirror-egress=yes option in the /interface ethernet switch port menu for the sfp-sfpplus8 interface. Then, configure any unused port as the target for mirrored traffic using the mirror-target setting in the /interface ethernet switch menu. Connect a packet-capturing device (capable of capturing tagged packets) to this target port, and check if tagged BPDU packets (VLANs 510 and 511) are visible.https://help.mikrotik.com/docs/spaces/R ... dMirroringDid not quite understand this point, how the configuration looks like?To monitor outgoing packets, I had to add a second mirroring rule to the CPU for sfp-sfpplus8 and set 01:80:C2:00:00:00 as the source. ---

## Response 9
The issue has been resolved; it turned out to be a coincidence. There's no problem. Thank you, everyone. ---