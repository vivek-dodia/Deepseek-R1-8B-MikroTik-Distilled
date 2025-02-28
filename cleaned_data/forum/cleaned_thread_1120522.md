# Thread Information
Title: Thread-1120522
Section: RouterOS
Thread ID: 1120522

# Discussion

## Initial Question
Hi all, first time posting here but here goes nothing.I recently checked in with some of the machines I have been administering in my homelab. I have a casewhereby my one Mikrotik has two bridges configured - nothing special with that - I added them as follows:
```
/interface/bridge
add name=bridge1
add name=bridge2

ports/

add bridge=bridge1 interface=ether6
add bridge=bridge1 interface=ether7
add bridge=bridge2 interface=ether8
add bridge=bridge2 interface=ether9Now I have a scenario whereby I have a device (call it dev_a) connected via Ethernet to one of the enslaved ports of `bridge1`and then I have another device (call it dev_b) connected via Ethernet to one of the enslaved ports of `bridge2`.Here's the kicker (although I never assumed it should have been one because there is nothing wrong with this frommy networking understanding at both L2 and L3), dev_a and dev_b both have the same MAC address, but that shouldbe no problem - they are after all on **different** bridges:Screenshot from 2025-01-18 14-45-45.pngOkay, still fine.Now, we know that with how IPv6 link-local works that means the Linux kernel running on dev_a and dev_bis going to derive the link-local interface address from the MAC address (which is the same on both devices),meaning both dev_a and dev_b will have the same IPv6 link-local address (this should _still_ be fine as theyare on seperate L2 networks).When I ping the address like so:
```

```
ping fe80::6222:32ff:fe39:c56d%bridge1And like so:
```

```
ping fe80::6222:32ff:fe39:c56d%bridge2I noticed that only the second one (over bridge2) responds. The one over bridge1 sometimesdoes but is flaky - more timeouts than replies received. If, however, I unplug the ethernet cablethat connects dev_b to bridge2 (meaning that the entry for the MAC address disappears frombridge2), then the ping for dev_a (over bridge1) starts working again.---Can someone either tell me I am crazy, because this setup should work.

---
```

## Response 1
It's similar problem to having two devices with same IPv4 address (albeit with different MAC addresses) ... it's possible to have it but involves NAT and multiple routing tables. Since NAT in IPv6 is a different beast, I'm not sure if (and how) your problem can be solved. ---

## Response 2
@mkx, let me disagree - it is actually not the same since here, we are talking about link-local addresses and explicit indication of interface while pinging the link-local address directly from the router. So it should work the way the OP expects.On the other hand, if both those devices use SLAAC to generate a global address, the prefixes of these two global addresses will be different so everything should work normally. ---

## Response 3
@mkx, let me disagree - it is actually not the same ...I agree it's not the same, I used word "similar" ... ---

## Response 4
What I had in mind was that the issue is essentially different. We are not dealing with same subnets attached to two distinct interfaces, where a destination address alone is not enough to choose the correct route and multiple routing tables have to be used. If it was just that, possibly the "wrong" device would respond to the pings, but there would always be a response. Here, the specification of the interface is taken into account as the behavior does differ depending on which interface has been specified, but the behavior is incorrect as either the ping requests are not sent anywhere or the responses are ignored. ---

## Response 5
I believe your guess-work is far more educated than mine. I've no idea about how ROS works around such cases. ---

## Response 6
```
/ipv6/neighbor/print detail without-paging where mac-address=<MAC>https://help.mikrotik.com/docs/spaces/R ... ghborsList

---
```

## Response 7
What I had in mind was that the issue is essentially different. We are not dealing with same subnets attached to two distinct interfaces, where a destination address alone is not enough to choose the correct route and multiple routing tables have to be used. If it was just that, possibly the "wrong" device would respond to the pings, but there would always be a response. Here, the specification of the interface is taken into account as the behavior does differ depending on which interface has been specified, but the behavior is incorrect as either the ping requests are not sent anywhere or the responses are ignored.Indeed, the <interfaceid> is what makes the destination address (addr, interfaceid) unique, so it shouldn't be a problem. I find it very odd that RoS struggles with this.I don't have any weird configuration or anything, it should be easily reproducible. Get a mikrotik, create those bridges and then place a device (or two) that has two ethernet interfaces behind one enslaved port of bridgeA and another of an enslaved port of bridgeB. ---

## Response 8
```
/ipv6/neighbor/print detail without-paging where mac-address=<MAC>https://help.mikrotik.com/docs/spaces/R ... ghborsListI have looked at the IPv6 neighborhood list and it shows information I expect. The link-local address behind bridge1 and the samelink-local address behind bridge2. That makes sense; none of this should be a problem yet on RoS it seems to not work.

---
```

## Response 9
Get a mikrotik, create those bridges and then place a device (or two) that has two ethernet interfaces behind one enslaved port of bridgeA and another of an enslaved port of bridgeB.Sure, and introduce by mistake 2 to 34 of the possible 4587 differences between your configuration and the recreated one.Come on, follow these instructions and post (anonymized) the EXACT configuration you are testing:viewtopic.php?t=203686#p1051720maybethis way someone will take the time to reproduce/test it. ---

## Response 10
it should be easily reproducible. Get a mikrotik, create those bridges and then place a device (or two) that has two ethernet interfaces behind one enslaved port of bridgeA and another of an enslaved port of bridgeB.Now wait a bit, sir. So far I took for granted that you've got two distinct devices with same MAC addresses. If that's not the case, as the wording "a device (or two)" suggests, the explanation may be different. ---

## Response 11
Are there really two devices with the same MAC address, or is it a case of multiple paths to the same device. The OUI highlighted by the OP is Ubiquiti, so could be a switch or meshed wireless AP with the problem actually being somewhere other than the Mikrotik. ---

## Response 12
Are there really two devices with the same MAC address, or is it a case of multiple paths to the same device. The OUI highlighted by the OP is Ubiquiti, so could be a switch or meshed wireless AP with the problem actually being somewhere other than the Mikrotik.So it's actually one device. The reason I mentioned the example of dev_a and dev_b was because of the following. The device in question has 3 VLAN interfaces, meaning it generates Ethernet frames that egress it with a tag. These all go over a single underlying physical Ethernet interface (and into a seperate switch that splits them out to untagged access ports). This ALSO means the link-local IPv6 address of each of these VLAN interfaces (software interfaces) will be the same as they each have the same MAC address as the underlying interface. -- So far this should not be a problem.Okay so we have a trunk port that receives, let's say VLANs 70, 71 and 72. Then the switch pushes out anything tagged with 70 on its port 5, anything with 71 on its port 6 and anything with tag 72 on port 7. So frames coming out of port 5, 6 and 7 are just plain old ethernet frames.Now I currently have frames coming out of port 5 and going into one of my Miktorik routers. That works just fine as expected. -- All good**Now**, where things seem to go wrong is here. Remember I have cables coming out of port 6 and 7 from my switch? Yes, those connect to bridge1 and bridge2 on _another (different)_ Mikrotik router. port 6 ----> an enslaved port of bridge1 (on the Router), port 7 -----> an enslaved port of bridge2 (on the router). --- I have only been experiencing flapping issues on **this** Mikrotik (the different being that it has two bridges and has traffic coming into both with the same link-local address). -- That is the setup**When does it get flaky?** When you have traffic outgoing via bridge1 via the link-local shown above and _also_ have it outgoing via bridge2 (to the _same_ link-local). They both work for some time then stop.I hope that helps, there's very little configuration I have done, just added the two bridges and tested this. ---

## Response 13
it should be easily reproducible. Get a mikrotik, create those bridges and then place a device (or two) that has two ethernet interfaces behind one enslaved port of bridgeA and another of an enslaved port of bridgeB.Now wait a bit, sir. So far I took for granted that you've got two distinct devices with same MAC addresses. If that's not the case, as the wording "a device (or two)" suggests, the explanation may be different.Sure, I have explained below now to aid in that. The reason I mentioned that was because the setup (as you will see explained below) works fine with the originating device (the one with the VLAN interfaces and duplicate link-local IPv6's (per each software VLAN interface)). The problem seems to be when I yank that out via two access ports and plug one into an enslaved port of bridge1 and another into an enslaved port of bridge2 (on the SAME Mikrotik) -- then I seem to have problems - and just with that Mikrotik - it doesn't break anything else. ---

## Response 14
OK, so I did as you suggested, except that I have used EoIP tunnels to avoid reconfiguring the VLANs etc.CHR #1 has two bridges, each bridge has a single member port which is an EoIP tunnel; the other ends of those EoIP tunnels are two other Mikrotik devices, CHR #2 and a physical router. Both remote ends of the EoIP tunnels have the same MAC address, 02:AA:AA:BB:BB:BB.Everything works as one would expect - when I runping fe80::aa:aaff:febb:bbbb%bridge-interface-name, the pings reach the device corresponding tobridge-interface-name, as confirmed by running a sniffer on both, and the responses do come back and are shown. Of course I have tried pinging via both bridges:
```
[me@myTik] > ping fe80::aa:aaff:febb:bbbb%br-hapac2
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 fe80::aa:aaff:febb:bbbb                    56  64 1ms197us   echo reply
    1 fe80::aa:aaff:febb:bbbb                    56  64 743us      echo reply
    2 fe80::aa:aaff:febb:bbbb                    56  64 669us      echo reply
    sent=3 received=3 packet-loss=0% min-rtt=669us avg-rtt=869us max-rtt=1ms197us

[me@myTik] > ping fe80::aa:aaff:febb:bbbb%br-chr-2
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 fe80::aa:aaff:febb:bbbb                    56  64 1ms119us   echo reply
    1 fe80::aa:aaff:febb:bbbb                    56  64 653us      echo reply
    2 fe80::aa:aaff:febb:bbbb                    56  64 988us      echo reply
    sent=3 received=3 packet-loss=0% min-rtt=653us avg-rtt=920us max-rtt=1ms119usI'd suggest you to run/tool snifferat the Mikrotik (at both interfaces in question) andtcpdumpat the other device (again at both interfaces in question) and see what is actually happening. I assume you'll see the Mikrotik to send the requests via the corrrect interface but the responses to either take the wrong path or not be sent at all.

---
```

## Response 15
OK, so I did as you suggested, except that I have used EoIP tunnels to avoid reconfiguring the VLANs etc.CHR #1 has two bridges, each bridge has a single member port which is an EoIP tunnel; the other ends of those EoIP tunnels are two other Mikrotik devices, CHR #2 and a physical router. Both remote ends of the EoIP tunnels have the same MAC address, 02:AA:AA:BB:BB:BB.Everything works as one would expect - when I runping fe80::aa:aaff:febb:bbbb%bridge-interface-name, the pings reach the device corresponding tobridge-interface-name, as confirmed by running a sniffer on both, and the responses do come back and are shown. Of course I have tried pinging via both bridges:
```
[me@myTik] > ping fe80::aa:aaff:febb:bbbb%br-hapac2
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 fe80::aa:aaff:febb:bbbb                    56  64 1ms197us   echo reply
    1 fe80::aa:aaff:febb:bbbb                    56  64 743us      echo reply
    2 fe80::aa:aaff:febb:bbbb                    56  64 669us      echo reply
    sent=3 received=3 packet-loss=0% min-rtt=669us avg-rtt=869us max-rtt=1ms197us

[me@myTik] > ping fe80::aa:aaff:febb:bbbb%br-chr-2
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 fe80::aa:aaff:febb:bbbb                    56  64 1ms119us   echo reply
    1 fe80::aa:aaff:febb:bbbb                    56  64 653us      echo reply
    2 fe80::aa:aaff:febb:bbbb                    56  64 988us      echo reply
    sent=3 received=3 packet-loss=0% min-rtt=653us avg-rtt=920us max-rtt=1ms119usI'd suggest you to run/tool snifferat the Mikrotik (at both interfaces in question) andtcpdumpat the other device (again at both interfaces in question) and see what is actually happening. I assume you'll see the Mikrotik to send the requests via the corrrect interface but the responses to either take the wrong path or not be sent at all.Leaving the pings (both) running on my Mikrotik and see this on the receiving device:
```

```
eth4.51@eth4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 60:22:32:39:c5:6d brd ff:ff:ff:ff:ff:ff
    inet6 fe80::6222:32ff:fe39:c56d/64 scope link
       valid_lft forever preferred_lft forever

    RX:  bytes    packets     errors    dropped    overrun      mcast
      35835487     471849          0      23111          0      22958
    TX:  bytes    packets     errors    dropped    carrier collisions
     177487486     588091          0          0          0          0VLAN 51 refers to the port6 on my switch which connects to an enslaved port on bridge1 of my Miktorik (EdgeRouter <---trunk---> switch <--- access port ---> miktorik (on a port to either bridge1 or bridge2).So this, at the very least, explains something. The drops at least. It is odd but doesn't yet explain everything - so I need to investigate. I am thinking I'll connect some other device to the switch port and see how the EdgeRouter reacts to that once traffic tries reaching that vif interface.

---
```

## Response 16
Another update. I have plugged my PC into the switch port on my switch that reaches the VLAN interface on the EdgeRouter. I can leave that pinging the`fe80::6222fe39:c56d%someUglyFedoraRenamedINterfaceName` address just fine. I am monitoring my Miktorik and it hasn't failed pingingthe `fe80::6222fe39:c56d%bridge1` IP.That whole "dropped packet" counter I posted earlier also stopped incrementing.Therefore, I am *only* seeing this problem when I have the same IPv6 link-local address coming into more than one enslaved bridge port (onSEPERATE bridges). I can't see anything wrong with my EdgeRouters VLAN config - it's very simple. The switch handling trunking and accessports (a Miktorik Switch) also has the correct configuration. The only time it seems to be a problem if when I have declared two bridges onone miktorik router, enslaved ether6, ether7 to bridge1 and ether8, ether9 to bridge2. Then have the same link-local Ipv6 host appear on bridge1and bridge2 as a discovered host. Only then am I seeing problems.---I only seem to be getting this problem on the bridge2 device, that's where those drops seem to come into play. In fact in general it seems tobe occuring on the enslaved port on that bridge2.The bridge definitions are:
```
0 R ;;; Personal services
     name="bridge1" mtu=auto actual-mtu=1500 l2mtu=1598 arp=enabled arp-timeout=auto mac-address=48:A9:8A:B6:29:C4 
     protocol-mode=rstp fast-forward=yes igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s 
     forward-delay=15s transmit-hold-count=6 vlan-filtering=no dhcp-snooping=no port-cost-mode=short mvrp=no 
     max-learned-entries=auto 

 1 R ;;; Personal devices
     name="bridge2" mtu=auto actual-mtu=1500 l2mtu=1598 arp=enabled arp-timeout=auto mac-address=48:A9:8A:B6:29:C6 
     protocol-mode=rstp fast-forward=yes igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s 
     forward-delay=15s transmit-hold-count=6 vlan-filtering=no dhcp-snooping=no port-cost-mode=long mvrp=no 
     max-learned-entries=auto

---
```

## Response 17
What if you do it the other way round - shut down one of the two VLAN interfaces on eth4, set the MAC address of your Fedora laptop to 60:22:32:39:c5:6d, and connect it to a port of the Mikrotik bridge that is connected to the VLAN that has been shut down? ---

## Response 18
What if you do it the other way round - shut down one of the two VLAN interfaces on eth4, set the MAC address of your Fedora laptop to 60:22:32:39:c5:6d, and connect it to a port of the Mikrotik bridge that is connected to the VLAN that has been shut down?Hi again! This is a great idea. I will give this a try sometime this week and then report back. Easiest thing is to keep all VLAN interfaces running but simply unplug the one and have that cable to into my laptop (of which I shall set to use the same MAC address in order to replicate the concept).Thanks! Will report back soon! ---

## Response 19
It would be helpful if you provided a diagram, and what the devices involved are.What is the Ubiquiti device that has vlans? An edgerouter? ER-X or ER-6P?What is the vlan-aware switch? Is it a switch that supports and is configured to use IVL (independent vlan learning, where the vid is used in addition to the mac address when storing the [mac/vid] to switch-port table), or is it SVL (which uses only the mac address) in the mac to switch-port (assumes that same mac won't be a member of more than one vlan).If it is SVL, it is possible the switch is relearning the port that the mac address is coming from (when received from the mikrotik bridges, regardless of which vlan is involved.And that will cause problems. google SVL vs IVLThen consider what happens if you have two switchs, one configured for IVL and one for SVL with "access ports" connected between the switches, and trunk ports connected to two vlan-aware devices.IVL vs SVL.pngIf only a single vlan is used, there isn't a problem. But if you use multiple vlans simultaneously, the SVL switch will have mac table trashing, as it will see the port that the mac address of a specific device as changing between the three access ports, and packets will be dropped. ---