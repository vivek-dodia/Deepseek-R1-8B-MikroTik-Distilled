# Thread Information
Title: Thread-1123244
Section: RouterOS
Thread ID: 1123244

# Discussion

## Initial Question
We actually don't know what kind of "abuse by vendor" can come out of this device-mode can of worms. They can even force the override of user-defined settings of device-mode on every subsequent upgrade - if they want to get rid of more customers...The whole auto-enabled device mode is a misguided attempt to fight things like several past issues with poorly configured ROS devices turned into bot-nets and used for DOS attacks.While main reason for this to happen is a good part of MTs target market lacks skills, resources and sometimes attitude to properly configure internet exposed devices.Now some folks will avoid updating to >=7.17 because they understandably want to avoid risking to lock up remote devices in a way requiring someone to travel to the site. And maybe even climb up a pole. Leading to ROS devices running intentionally on outdated versions.And if someone figures out a pattern to trigger the obscure "flagged" mode, there will be an easy way to DOS Mikrotik devices.Device mode might have it's applications, but force-enabling it on remote SW updates for existing productions devices is a more than questionable idea.It's a classic example of "we need to do something so we do something allowing us to claim we did something". ---

## Response 1
Why is device-mode even being discussed in this 7.18beta topic? As far as I can see, there hasn’t been a single changelog item related to device-mode in 7.18. It would make more sense to discuss this in the 7.17 thread or in a dedicated topic.A separate, well-focused discussion with significant attention and engagement is likely to catch MikroTik’s attention more effectively than scattered comments within release threads. The discussions during the 7.17 beta were productive and positive, and the community feedback helped refine the most problematic aspects of the initial device-mode implementation. ---

## Response 2
anyone has successfully experience implement MPLS-VPN6 (6vpe) on v7?is it works?thx ---

## Response 3
Why is device-mode even being discussed in this 7.18beta topic? As far as I can see, there hasn’t been a single changelog item related to device-mode in 7.18. It would make more sense to discuss this in the 7.17 thread or in a dedicated topic.A separate, well-focused discussion with significant attention and engagement is likely to catch MikroTik’s attention more effectively than scattered comments within release threads. The discussions during the 7.17 beta were productive and positive, and the community feedback helped refine the most problematic aspects of the initial device-mode implementation.Pretty obviousA) Devicemode shows up if updating lab devices from <=7.16 to 7.18beta for testing, so its natural such observations end up hereB) We still hope MT reconsiders this for 7.18 so we can update our devices to 7.18 once released without risking to get locked out and drive a few hours ---

## Response 4
I am still hoping for a solution where defconf for the firewall can be applied to an existing router... some command that removes the firewall config and reloads it from defconf, if only as a commandline script.So far none of changes in firewall defconf was ever applied when upgrading ROS. So I don't see this one coming either.To be clear: I am NOT suggesting that defconf be applied when upgrading RouterOS.What I am suggesting is that there should be a command that the admin can issue and that resets the firewall settings to the defconf for the currently running version of RouterOS.Entirely by their own request. Not automatic, and maybe after a confirmation similar to what you get when doing reset-configuration.Except it will reset only the firewall. ---

## Response 5
I think it’s a pretty good idea for a lot of reasons. ---

## Response 6
To be clear: I am NOT suggesting that defconf be applied when upgrading RouterOS. [...] Entirely by their own request. [...]Except it will reset only the firewall.I think it’s a pretty good idea for a lot of reasons.+1 - I love the idea. I feel like the default firewall keeps improving, so it be good to re-refresh just that. Perhaps even on device without a default configuration to add a "standard" one - MANUALLY.Also help with branding/netinstall custom defconfs... sinceafirewall should be included, it actually be better to be able to do some "/ip/firewall/reset-to-default", instead of adding the default by copy-and-paste to custom defconf. ---

## Response 7
since 7.16 I cannot use skin designer, profile is created on disk but not present in other parts...Is it a way to use it ?do I miss something ? ---

## Response 8
What I am suggesting is that there should be a command that the admin can issue and that resets the firewall settings to the defconf for the currently running version of RouterOS.+1 I'm also supporting this great idea. ---

## Response 9
anyone has successfully experience implement MPLS-VPN6 (6vpe) on v7?is it works?thxAfter testing on almost every version since "I don't even remember".After spending a lot and a lot of time.After having results like "It seems to work... Ooow, wait...hummm dammit"Frequently the issues ar in the iBGP keeping NLRI and recursive next-hop.I didn't have the strength to do this test 7.18beta2 so far.I have a virtual Lab running on 7.17, during this week I'm intended to upgrade to test it. ---

## Response 10
anyone has successfully experience implement MPLS-VPN6 (6vpe) on v7?is it works?thxWe are interested in using it, but the current state of implementation is useless to us because it does not support operation on an IPv4 backbone. ---

## Response 11
..[cut]..The suggestion I am making may seem very disruptive, but it is actually a development trend and not an innovation.Basically, the idea is that all RouteOS features expose the possibility of sending the events of these features to a hook manager.And from this hook manager, scripts can be invoked so that the user can do what he needs to do...[cut]..I love it! I hope MT guys do the same ;) ---

## Response 12
anyone has successfully experience implement MPLS-VPN6 (6vpe) on v7?is it works?thxIt worked for me over IPv6 till 7.16.x.In 7.17 and 7.18 there is a bug, which destroys almost all of the IPv4 RIB, DHCP default route is disappearing, so I disabled VPNv6 everywhere because it made almost all of our remote CPEs unreachable. I built a test setup for MT support and waiting them to investigate. ---

## Response 13
anyone has successfully experience implement MPLS-VPN6 (6vpe) on v7?is it works?thxWe are interested in using it, but the current state of implementation is useless to us because it does not support operation on an IPv4 backbone.You mean 6PE and 6VPE, right?Same here!In my opinion, it is related to the long absence of VRF as it is now. With its own loopback allowing leaks across VRFs, and etc...This exposure of real loopbacks is pretty recent, right? 7.14? ---

## Response 14
You mean 6PE and 6VPE, right?IIRC 6PE is not supported yet, only 6VPE over IPv6. VPNv6 routes exchanging over IPv4 BGP session too, but the nexthop encoding is incorrect and/or IPv6 route over IPv4 nexthop is not supported. ---

## Response 15
Hi, What is the position of Fasttrack rules in the IPv6 firewall?
```
/ipv6 firewall filter
add action=fasttrack-connection chain=forward comment="Enable FastTracked v6 traffic" connection-state=established,related
add action=accept chain=forward comment="accept established,related,untracked" connection-state=established,related,untracked

---
```

## Response 16
You can display the defconf using: /system/default-configuration/print ---

## Response 17
You can display the defconf using: /system/default-configuration/printThe fasttrack rule does not exist in the default configuration (you have to create it), it is not clear to me in which position it should go.
```
/ipv6 firewall {                                                                                                                          >
                       address-list add list=bad_ipv6 address=::/128 comment="defconf: unspecified address"                                                    >
                       address-list add list=bad_ipv6 address=::1 comment="defconf: lo"                                                                        >
                       address-list add list=bad_ipv6 address=fec0::/10 comment="defconf: site-local"                                                          >
                       address-list add list=bad_ipv6 address=::ffff:0:0/96 comment="defconf: ipv4-mapped"                                                     >
                       address-list add list=bad_ipv6 address=::/96 comment="defconf: ipv4 compat"                                                             >
                       address-list add list=bad_ipv6 address=100::/64 comment="defconf: discard only "                                                        >
                       address-list add list=bad_ipv6 address=2001:db8::/32 comment="defconf: documentation"                                                   >
                       address-list add list=bad_ipv6 address=2001:10::/28 comment="defconf: ORCHID"                                                           >
                       address-list add list=bad_ipv6 address=3ffe::/16 comment="defconf: 6bone"                                                               >
                       filter add chain=input action=accept connection-state=established,related,untracked comment="defconf: accept established,related,untrack>
                       filter add chain=input action=drop connection-state=invalid comment="defconf: drop invalid"                                             >
                       filter add chain=input action=accept protocol=icmpv6 comment="defconf: accept ICMPv6"                                                   >
                       filter add chain=input action=accept protocol=udp dst-port=33434-33534 comment="defconf: accept UDP traceroute"                         >
                       filter add chain=input action=accept protocol=udp dst-port=546 src-address=fe80::/10 comment="defconf: accept DHCPv6-Client prefix deleg>
                       filter add chain=input action=accept protocol=udp dst-port=500,4500 comment="defconf: accept IKE"                                       >
                       filter add chain=input action=accept protocol=ipsec-ah comment="defconf: accept ipsec AH"                                               >
                       filter add chain=input action=accept protocol=ipsec-esp comment="defconf: accept ipsec ESP"                                             >
                       filter add chain=input action=accept ipsec-policy=in,ipsec comment="defconf: accept all that matches ipsec policy"                      >
                       filter add chain=input action=drop in-interface-list=!LAN comment="defconf: drop everything else not coming from LAN"                   >
                       filter add chain=forward action=accept connection-state=established,related,untracked comment="defconf: accept established,related,untra>
                       filter add chain=forward action=drop connection-state=invalid comment="defconf: drop invalid"                                           >
                       filter add chain=forward action=drop src-address-list=bad_ipv6 comment="defconf: drop packets with bad src ipv6"                        >
                       filter add chain=forward action=drop dst-address-list=bad_ipv6 comment="defconf: drop packets with bad dst ipv6"                        >
                       filter add chain=forward action=drop protocol=icmpv6 hop-limit=equal:1 comment="defconf: rfc4890 drop hop-limit=1"                      >
                       filter add chain=forward action=accept protocol=icmpv6 comment="defconf: accept ICMPv6"                                                 >
                       filter add chain=forward action=accept protocol=139 comment="defconf: accept HIP"                                                       >
                       filter add chain=forward action=accept protocol=udp dst-port=500,4500 comment="defconf: accept IKE"                                     >
                       filter add chain=forward action=accept protocol=ipsec-ah comment="defconf: accept ipsec AH"                                             >
                       filter add chain=forward action=accept protocol=ipsec-esp comment="defconf: accept ipsec ESP"                                           >
                       filter add chain=forward action=accept ipsec-policy=in,ipsec comment="defconf: accept all that matches ipsec policy"                    >
                       filter add chain=forward action=drop in-interface-list=!LAN comment="defconf: drop everything else not coming from LAN"                 >
                     }

---
```

## Response 18
You can compare the ipv4 firewall.... ---

## Response 19
You mean 6PE and 6VPE, right?IIRC 6PE is not supported yet, only 6VPE over IPv6. VPNv6 routes exchanging over IPv4 BGP session too, but the nexthop encoding is incorrect and/or IPv6 route over IPv4 nexthop is not supported.But the next hop for real is (or should be) the RT and the associated Label.If you sniff the BGP messages on the route exchange, it is correct.I believe the problem is actually on VRF and RT+Label, and on VRF(RT) Lookups.Are you using the per-vrf label allocation?/routing bgp vpn addlabel-allocation-policy=per-vrf ---

## Response 20
IIRC 6PE is not supported yet, only 6VPE over IPv6. VPNv6 routes exchanging over IPv4 BGP session too, but the nexthop encoding is incorrect and/or IPv6 route over IPv4 nexthop is not supported.But the next hop for real is (or should be) the RT and the associated Label.If you sniff the BGP messages on the route exchange, it is correct.I believe the problem is actually on VRF and RT+Label, and on VRF(RT) Lookups.Are you using the per-vrf label allocation?/routing bgp vpn addlabel-allocation-policy=per-vrfI have an LxVPN lab with RoS7 too, and it has two VRFs, one of is using per-vrf, another is per-prefix to testing both. When I digged into it deeper some months ago, IIRC mrz from MT said on this forum that, its because of lack of support of "IPv6 route over IPv4 nexthop". Only "IPv4 route over IPv6 nextop" is supported in kernel, which they selected for RoS7. Similar issue is exists in FFRouting but there the nexthop encoding is incorrect:https://github.com/FRRouting/frr/issues/4661That should be seen, IPv6 route over IPv4, what is cisco and others do, is a hack, a necessary evil.Fortunately we have IOS-XR boxes which is the only cisco OS that supports VPNv6 over IPv6 and it can forward VPNv6 traffic between IPv6 MT CPEs and VPNv6 over IPv4 backbone. Now the ball is on MT's side to fix the issues around VPNv6. ---

## Response 21
First of all, amazing release! L3HW and IPv6 FastTrack were much needed and worked well on my RB5009, achieving 4Gb WAN speed.However, I have a strange issue. Has anyone else experienced new ND issues? Apple devices randomly lose IPv6 connectivity, and LAN devices receive adversed IPv6 addresses from all VLANs. Everything was fine until the latest 7.17 update and broke in 7.18-beta ---

## Response 22
The "LAN devices receive adversed IPv6 addresses from all VLANs" is that referring to Windows devices that are on ports with tagged VLANs present?As that is a Windows bug, has nothing to do with RouterOS. ---

## Response 23
You can display the defconf using: /system/default-configuration/printThe fasttrack rule does not exist in the default configuration (you have to create it), it is not clear to me in which position it should go.If you follow advice by @pe1chl, you'll place it as the very first rule in chain=forward, above this rule:
```
filter add chain=forward action=accept connection-state=established,related,untracked comment="defconf: accept established,related,untracked"BTW, when you listed default config, your terminal windows wasn't wide enough, some rules were clipped on the right side (the above written one as well).

---
```

## Response 24
The fasttrack rule does not exist in the default configuration (you have to create it), it is not clear to me in which position it should go.If you follow advice by @pe1chl, you'll place it as the very first rule in chain=forward, above this rule:
```
filter add chain=forward action=accept connection-state=established,related,untracked comment="defconf: accept established,related,untracked"BTW, when you listed default config, your terminal windows wasn't wide enough, some rules were clipped on the right side (the above written one as well).Ok, thanks!

---
```

## Response 25
BTW, when you listed default config, your terminal windows wasn't wide enough, some rules were clipped on the right side (the above written one as well).Well, an irritating problem in printing default-configuration is that it does not wrap the lines and the lines are very long.So you need to print with arg file=outputfile and then download the outputfile.txt to have a complete default-configuration.Even then I first thought that the fasttrack rule for ipv6 was already there, but it seems it is not, that still has to happen.But it is there for ip (v4) so that can be used as a guide. ---

## Response 26
What's new in 7.18beta4 (2025-Jan-31 15:46):*) bridge - fixed endless MAC update loop (introduced in v7.17);*) chr/x86 - fixed error message on bootup;*) cloud - added file-share feature (additional fixes);*) console - added dsv.remap to :serialize command to unpack array of maps from print as-value (additional fixes);*) defconf - added IPv6 FastTrack configuration;*) dhcpv4-server - fixed framed-route removal;*) dhcpv4-server - fixed lease assigning when server address is not bind to server interface (introduced in v7.17);*) fetch - fixed IPv6 handling in URL (introduced in v7.18beta2);*) file - improved handling of filesystems with many files (additional fixes);*) hotspot - fixed an issue where extra "flash/" is added to html-directory for devices with flash folders (introduced in v7.17);*) igmp-proxy - fixed multicast routing after upstream interface flaps (introduced in v7.17);*) ipsec - fixed chacha20 poly1305 proposal;*) ipv6 - added routing FastPath support (enabled by default) (additional fixes);*) ipv6 - fixed configuration loss due to conflicting settings after upgrade (introduced in v7.17);*) l3hw - added initial HW offloading for VXLAN on compatible switches (additional fixes);*) log - added CEF format support for remote logging (additional fixes);*) lte - added basic support for Quectel RG255C-GL modem in "at+qcfg="usbnet",0" USB composition;*) lte - added initial eSIM management support (CLI only) (additional fixes);*) lte - reduced SIM slot switchover time for modems with AT control channel;*) net - added initial support for automatic multicast tunneling (AMT) interface (additional fixes);*) ovpn - added requirement for server name when exporting configuration;*) poe-out - fixed invalid poe-in status detection for RB5009 (introduced in v7.18beta2);*) port - improved handling of USB device plug/unplug events;*) ppc - fixed HW encryption (introduced in v7.17);*) queue - improved system stability when many simple queues are added (introduced in v7.17);*) resolver - fixed static FQDN resolving (introduced in v7.17);*) routerboot - improved stability for IPQ8072 ("/system routerboard upgrade" required);*) smb - fixed connection issues with clients using older SMB versions (introduced in v7.17);*) supout - added IPv6 settings section;*) switch - improvements to certain switch operations (port disable, shaper and switch initialization) (additional fixes);*) vxlan - added IPv6 FastPath support;*) vxlan - fixed unset for "group" and "interface" properties;*) vxlan - replaced the "inherit" with "auto" option for dont-fragment property (new default);*) wifi-qcom - fixed potentially lowered throughput for station interfaces if channel.width property is set (introduced in v7.18beta2);*) winbox - fixed locked input fields when creating new certificate template;*) winbox - show warning messages for static DNS entries;*) x86 - fixed "unsupported speed" warning (additional fixes); ---

## Response 27
Settings for neighbor discover LLDP are lost on upgrade to 7.18beta2.E.g.:
```
/ip neighbor discovery-settings
set discover-interface-list=discover lldp-mac-phy-config=yes \
    lldp-med-net-policy-vlan=16After upgrade they can be re-applied and still work.

---
```

## Response 28
There are some minor change in the CEF logs:7.18beta42025-01-31T17:53:06.615+0100 hAP-test CEF:0|MikroTik|hAP ac^2|7.18beta4 (testing)|10|system, info|Low|dvchost=hAP-test dvc=10.10.10.14 msg=7.18beta22025-01-31T17:50:00.133+0100 RB951 CEF:0|MikroTik|RB951Ui-2HnD|7.18beta2 (testing)|65|dns|Unknown|msg=beta4 do have two new fields. dvchost and dvc. As I can see the dvc-host is are already present after the clock, so no need stuff two times.For Splunk using key=value helps for auto extraction.What does the number 10 and 65 mean? ---

## Response 29
The number after the version string is the "deviceEventClassId" which is supposed to be a unique ID of each message.However, the numbers 10 and 65 are probably not that, it looks like this is still to be implemented... ---

## Response 30
Maybe there just re-using topic id/hash for now, IDK. There are 104 topics FWIW.@normis was hopeful earlier:More CEF features are in development for the next betasBut some unique "log id" has long been missing... so hope that is part is included. ---

## Response 31
You mean 6PE and 6VPE, right?IIRC 6PE is not supported yet, only 6VPE over IPv6. VPNv6 routes exchanging over IPv4 BGP session too, but the nexthop encoding is incorrect and/or IPv6 route over IPv4 nexthop is not supported.i dont see any vpnv6 and send-label parameters available in bgp.so i think 6VPE and 6PE cannot run on MT v6 & v7so MT when will you implement 6VPE and 6PE ?thx ---

## Response 32
Calm down! Let them debug and finish BASIC FUNCTIONALITY in BGP before starting such things... ---

## Response 33
The number after the version string is the "deviceEventClassId" which is supposed to be a unique ID of each message.However, the numbers 10 and 65 are probably not that, it looks like this is still to be implemented...Ok that would be nice for long message that may be splitt to multiple messages. ---

## Response 34
I encountered an issue while testing VPNv6 in a CE-PE scenario.Issue Details:I configured fc00:101::1/126 on ether1 (PE router), which belongs to vrf-CE1.After adding this IPv6 prefix, /ipv6/route/ hangs, and the connected route for fc00:101::/126 does not appear in /ipv6/route/ under vrf-CE1 table.The CE router is unable to ping fc00:101::1.Running the export command results in the error:
```
#error exporting '/ipv6/route' (timeout)CPU usage spikes significantly.All router IDs under /routing/id become invalid.Workaround:Changing the prefix length from /126 to /64 resolves the issue.It appears that MikroTik RouterOS struggles with certain IPv6 subnet sizes in a VRF environment. Could you confirm if this is a known issue, and if there's any fix or workaround available?Thank you.

---
```

## Response 35
/file/printis still very buggy in beta4 when there are lots of files and/or multiple disks:
```
[cesar@RB5009] > /file/print 
 # NAME     TYPE       SIZE LAST-MODIFIED
 0 hotspot  directory       2025-01-31 14:08:36
invalid request
[cesar@RB5009] >Also, I wish RouterOS would return to <= v7.17 behavior when files in container store were hidden.

---
```

## Response 36
The number after the version string is the "deviceEventClassId" which is supposed to be a unique ID of each message.However, the numbers 10 and 65 are probably not that, it looks like this is still to be implemented...Ok that would be nice for long message that may be splitt to multiple messages.It is not to identify the individual message instances, like a sequence number, but to identify each different message that is issued under the same topic. E.g under "dhcp info" there may be a "dhcp de-assigned IP for MAC" and a "dhcp assigned IP for MAC" and these two would have a different ID. But all the "dhcp de-assigned IP for MAC" (for different IP and MAC, at different times) would have the same ID.About multiple messages: there are cases where messages are needlessly split into many multiples. It mainly happens with debug messages. E.g. enabling "ipsec" messages results in a seamlessly endless output of messages each with a single variable or parameter. That makes it difficult to use, especially because the relation to something like a peer IP address is completely lost.More of the small parts should be put in a single message that starts with a meaningful heading that includes session identifying information like a peer IP. ---

## Response 37
mikrotik does not Support BGP VPNv6 over IPv4 MPLS LDP transport?
```
[admin@PE2] >  /routing/route/print where afi=vpn6
Flags: U - UNREACHABLE; b - BGP
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
   DST-ADDRESS              GATEWAY          AFI   DISTANCE  SCOPE  TARGET-SCOPE
Ub 2001:db8::/48&65000:105  ::ffff:10.0.0.1  vpn6       200     40            30
Ub fc00:101::/64&65000:100  ::ffff:10.0.0.1  vpn6       200     40            30
Ub fc00:101::/64&65000:101  ::ffff:10.0.0.1  vpn6       200     40            30

---
```

## Response 38
Changing the prefix length from /126 to /64 resolves the issue.It appears that MikroTik RouterOS struggles with certain IPv6 subnet sizes in a VRF environment. Could you confirm if this is a known issue, and if there's any fix or workaround available?Did you reproduce this issue on a hardware-based scenario (device with switchchip) or on a virtual machine?The reason for the question is because that characteristic looks like some very old issues on some experienced hardware-based vendors related to binary threes, longest prefix match, and TCAM limited resources.On docs of HW offload of MikroTik I remember something like "more specific are preferred to go to off-load".A possibility issue could be that:- IPv6 smaller than /64 route + Route Target marker fits on tuple limit of TCAM on switch chip.- but IPv6 longer than /64 when added the Route Target marker exceeds the tuple limit.If this is in a software-based scenario... This probably doesn't apply.P.S.: When I was writing this, I felt in 2008 and dealing IPv6 firmware upgrades of some Cisco routers. ---

## Response 39
Also, I wish RouterOS would return to <= v7.17 behavior when files in container store were hidden.Would a type of permission per user-group like:"allow-to-read-files-inside-containers=[yes|no]"not be enough to solve your need?Note: This is just a suggested alternative in case hiding the internal files again is impossible. ---

## Response 40
Would a type of permission per user-group like:"allow-to-read-files-inside-containers=[yes|no]"not be enough to solve your need?Note: This is just a suggested alternative in case hiding the internal files again is impossible.I don't think there needs to be a permission for that.It could be a flag in/file/print(like/file/print show-container-store=yes) or a permanent setting in/file/settings(which does not exist right now). ---

## Response 41
Changing the prefix length from /126 to /64 resolves the issue.It appears that MikroTik RouterOS struggles with certain IPv6 subnet sizes in a VRF environment. Could you confirm if this is a known issue, and if there's any fix or workaround available?Did you reproduce this issue on a hardware-based scenario (device with switchchip) or on a virtual machine?The reason for the question is because that characteristic looks like some very old issues on some experienced hardware-based vendors related to binary threes, longest prefix match, and TCAM limited resources.On docs of HW offload of MikroTik I remember something like "more specific are preferred to go to off-load".A possibility issue could be that:- IPv6 smaller than /64 route + Route Target marker fits on tuple limit of TCAM on switch chip.- but IPv6 longer than /64 when added the Route Target marker exceeds the tuple limit.If this is in a software-based scenario... This probably doesn't apply.P.S.: When I was writing this, I felt in 2008 and dealing IPv6 firmware upgrades of some Cisco routers.I tested this in a virtualized environment using EVE-NG, so hardware offload and TCAM limitations should not apply in this case. Since the issue occurs in a purely software-based scenario, it seems more likely to be a RouterOS bug rather than a hardware limitation. ---

## Response 42
/file/printis still very buggy in beta4 when there are lots of files and/or multiple disks:This will never change, if they won't revise their file management mechanism.What if you have 100K files on SMB share for example? After adding a disk, it will start to scan aWHOLEstructure and create a huge load on your network for a very long time. And if you reboot, this process will begin again.There should be completely new mechanism. In WinBox there should be a file manager with abiliy to browse between folders without scanning a whole file structure. Same in CLI, if you issue/file printcommand, it should only show a content in a root directory (or another directory if you specify it in "where").Without this, working with large amount of files is impossible. ---

## Response 43
mikrotik does not Support BGP VPNv6 over IPv4 MPLS LDP transport?Unfortunately not yet. ---

## Response 44
mikrotik does not Support BGP VPNv6 over IPv4 MPLS LDP transport?
```
[admin@PE2] >  /routing/route/print where afi=vpn6
Flags: U - UNREACHABLE; b - BGP
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
   DST-ADDRESS              GATEWAY          AFI   DISTANCE  SCOPE  TARGET-SCOPE
Ub 2001:db8::/48&65000:105  ::ffff:10.0.0.1  vpn6       200     40            30
Ub fc00:101::/64&65000:100  ::ffff:10.0.0.1  vpn6       200     40            30
Ub fc00:101::/64&65000:101  ::ffff:10.0.0.1  vpn6       200     40            30Pls read the forum, not just posting.viewtopic.php?p=1122915#p1122915

---
```

## Response 45
well, i double check again, MT hide vpn6 option from winbox, it can be set using cli.thx ---

## Response 46
Would it be possible to add serial to the CEF logs? I do it by adding prefix to all logs. This works but has to be added manually to each rule.So instead of this:2025-02-01T09:49:13.642+0100 hAP-test CEF:0|MikroTik|hAP ac^2|7.18beta4 (testing)|65|dns|Unknown|dvchost=hAP-test dvc=192.168.10.14 msg=serial\=BEED0B3AAAAA MikroTik: done query: #21 upgrade.mikrotik.com 159.148.147.251To some like this (dvchost also removed since its already in start of the logs2025-02-01T09:49:13.642+0100 hAP-test CEF:0|MikroTik|hAP ac^2|7.18beta4 (testing)|BEED0B3AAAAA|65|dns|Unknown|dvc=192.168.10.14 msg=done query: #21 upgrade.mikrotik.com 159.148.147.251This way I do not need the prefix at all. We need serial number in the Splunk logs to make sure its a unique unit. You may at some time change your main router to another model keeping the name. This will mess stuff up since its not the same router any more.Since not all MikroTik do has serial, I did just made the script so it sets a random number. This may be handled better by MikroTik to give it an unique ID.
```
:do {
	:set serial ([/system routerboard get serial-number])
} on-error={
	:set serial ([:rndstr from=ABCDEF0123456 length=12])
}

---
```

## Response 47
When you have a special need to have a serial number in messages, why don't you add it to the device identity of your devices?So instead of hAP-test you call it hAP-test-E1548DC8753B ---

## Response 48
@Jotneif board-name ~ "x86" use [/system license get software-id]if board-name ~ "CHR" use [/system license get system-id]on other cases use [/system routerboard get serial-number]or simply: [/int eth get ([find]->0) orig-mac-address] since at least all RouterBOARD have one ethernet interface... ---

## Response 49
When you have a special need to have a serial number in messages, why don't you add it to the device identity of your devices?So instead of hAP-test you call it hAP-test-E1548DC8753BExactly, is wrong call all the devices "hAP ac^2".Every single device on my network have different names.When I replace the device, the new still have the same name, so, not worry about serials.... ---

## Response 50
The "LAN devices receive advertised IPv6 addresses from all VLANs" is that referring to Windows devices that are on ports with tagged VLANs present.As that is a Windows bug, has nothing to do with RouterOS.Thanks for the reply. The issue is not with Windows I have it with both Linux containers and Raspberypi directly connected to the router + other devices showing strange beahvior.My setup looks something like this:Router (RB5009) <==(tagged)==> CRS309 <==(untagged)==> Lan ports, Wifi AP, IoT AP, VMs (KVM connected to intel SFP+)Router (RB5009) <==(untagged with PVID)==> raspberry pi* VLAN filtering is enabled on both router and switch with vlan-tagged only admission + ingress filter and IGMP snooping on both bridges and both devices on the latest 7.18-beta4It seems RA is somehow STILL leaking between VLANs. I can see leaked in Linux dev (that is connected via untagged access port, it is only supposed to get :3: one):inet6 2a02:***:3:**/128 scope global dynamic noprefixrouteinet6 2a02:***:3:**/64 scope global dynamic noprefixrouteinet6 2a02:***:1:**/64 scope global deprecated dynamic noprefixrouteinet6 2a02:***:0:**/64 scope global deprecated dynamic noprefixrouteinet6 2a02:***:2:**/64 scope global deprecated dynamic noprefixroute(the prefixes are assigned from a /48 pool each for a VLAN. routeros assigned 0, 1, 2, 3)Apple devices seem to behave strangely. They randomly activate ipv6 or not and sometimes lose it shortly (I guess because wrong packets are still being leaked.(it might not be exactly related to this beta release but only reporting here as just having this issue. if it is more appropriate to make a new discussion I can do) ---

## Response 51
... IGMP snooping on both bridges and both devices on the latest 7.18-beta4RAs are multicast ... so IGMP snooping might be playing foul game here. Try to disable it to see if that's the case. ---

## Response 52
it certainly is related to the configuration as I have a similar network (IPv6 with different /64 on tagged VLANs) running without issue.so make a new topic including /export of bridge and ipv6. ---

## Response 53
Every single device on my network have different names.When I replace the device, the new still have the same name, so, not worry about serials....If you for example handles a big customer, he uses the city name as the router name.Then at a time later you add another customer with the same naming idea. Serial number will be unique all time.Not this happens often, but I have seen it in my life ;) ---

## Response 54
@Jotneif board-name ~ "x86" use [/system license get software-id]if board-name ~ "CHR" use [/system license get system-id]on other cases use [/system routerboard get serial-number]or simply: [/int eth get ([find]->0) orig-mac-address] since at least all RouterBOARD have one ethernet interface...Thanks for the tip, will look inn to it :) ---

## Response 55
mikrotik does not Support BGP VPNv6 over IPv4 MPLS LDP transport?
```
[admin@PE2] >  /routing/route/print where afi=vpn6
Flags: U - UNREACHABLE; b - BGP
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
   DST-ADDRESS              GATEWAY          AFI   DISTANCE  SCOPE  TARGET-SCOPE
Ub 2001:db8::/48&65000:105  ::ffff:10.0.0.1  vpn6       200     40            30
Ub fc00:101::/64&65000:100  ::ffff:10.0.0.1  vpn6       200     40            30
Ub fc00:101::/64&65000:101  ::ffff:10.0.0.1  vpn6       200     40            30Pls read the forum, not just posting.viewtopic.php?p=1122915#p1122915Hi oreggin,you're right that 6vpe silently/partially supported at least until v7.16.2, but i still have problems below.i got this error on P which also act as RR[admin@P-01] > /routing/route/print where bgp afi=vpn6Flags: U - UNREACHABLE; b - BGP; H - HW-OFFLOADEDColumns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPEDST-ADDRESS                      GATEWAY            AFI   DISTANCE  SCOPE  TARGET-SCOPEUbH 2001:f20:10c::1:1/128&1:1        ::ffff:172.17.1.1  vpn6       200     40            30UbH 2001:f20:10c::1:2/128&1:1        ::ffff:172.17.1.2  vpn6       200     40            30UbH 2001:f20:10c:0:10:0:1:0/112&1:1  ::ffff:172.17.1.1  vpn6       200     40            30UbH 2001:f20:10c:0:10:0:2:0/112&1:1  ::ffff:172.17.1.2  vpn6       200     40            30all next-hop gateway were unreachablehave u succeeded running 6vpe?could you give any clue what happen?should i add something on OSPF?anyway i've also try running the same configuration on v7.17.1 and v7.18.x it's going worst, router became hung, ospf were not stable.thx

---
```

## Response 56
The routes appear unreachable because you are running VPNv6 over IPv4 infrastructure, which is not yet supported on RouterOS. ---

## Response 57
Updated script to get serial from different systems:
```
:local boardName [/system resource get board-name]
:local serial na
:if ($boardName = "CHR") do={
	:set serial [/system license get system-id]
} else= {
	:local arch [/system resource get architecture-name]

	:if ($arch = "x86_64") do={
		:set serial [/system license get software-id]
	} else={
		:set serial ([/system routerboard get serial-number])
	}
}

---
```

## Response 58
Pls read the forum, not just posting.viewtopic.php?p=1122915#p1122915Hi oreggin, you're right that 6vpe silently/partially supported at least until v7.16.2, but i still have problems below.i got this error on P which also act as RR[admin@P-01] > /routing/route/print where bgp afi=vpn6Flags: U - UNREACHABLE; b - BGP; H - HW-OFFLOADEDColumns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPEDST-ADDRESS GATEWAY AFI DISTANCE SCOPE TARGET-SCOPEUbH 2001:f20:10c::1:1/128&1:1 ::ffff:172.17.1.1 vpn6 200 40 30UbH 2001:f20:10c::1:2/128&1:1 ::ffff:172.17.1.2 vpn6 200 40 30UbH 2001:f20:10c:0:10:0:1:0/112&1:1 ::ffff:172.17.1.1 vpn6 200 40 30UbH 2001:f20:10c:0:10:0:2:0/112&1:1 ::ffff:172.17.1.2 vpn6 200 40 30all next-hop gateway were unreachablehave u succeeded running 6vpe?could you give any clue what happen?should i add something on OSPF?anyway i've also try running the same configuration on v7.17.1 and v7.18.x it's going worst, router became hung, ospf were not stable.thxtry thisviewtopic.php?p=1123124#p1123050change prefix to /64 ---

## Response 59
Oh perfect! IPv6 is getting some love!Would be extra nice if BGP IPv6 sessions could be monitored via SNMP and not only IPv4 :) ---

## Response 60
try thisviewtopic.php?p=1123124#p1123050change prefix to /64buset1974 trying an unsupported feature but I think you catch a bug with this prefix length.In my labs (VM and physical), locally connected IPv6 prefixes was /112 on loopbacks (bridges) and this triggered a bug. If prefixes are /64 or for example /62, there is no crash but unfortunately the routing itself doesn't work anyway:
```
[oreggin@rtr1.CPE] > /routing/route/print where afi=vpn6 
Flags: A - ACTIVE; b - BGP, y - BGP-MPLS-VPN
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS                 GATEWAY               AFI   DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW                   
Ay b00b:10:11:10::/62&65530:1  Loopback_VRF_A@VRF_A  vpn6       200     40            10  Loopback_VRF_A                 
Ab b00b:10:12:11::/64&65530:1  b00b::10:0:10:12      vpn6       200     40            30  fe80::20c:42ff:fe53:1491%ether2
Ab b00b:10:13:11::/64&65530:1  b00b::10:0:10:13      vpn6       200     40            30  fe80::20c:42ff:fe53:1491%ether2
Ay b00b:10:11:12::/64&65530:2  Loopback_VRF_B@VRF_B  vpn6       200     40            10  Loopback_VRF_B                 
Ab b00b:10:12:12::/64&65530:2  b00b::10:0:10:12      vpn6       200     40            30  fe80::20c:42ff:fe53:1491%ether2
Ab b00b:10:13:12::/64&65530:2  b00b::10:0:10:13      vpn6       200     40            30  fe80::20c:42ff:fe53:1491%ether2Routes are only in BGP table and not in L3VPN RIB, except locally connected routes.

---
```

## Response 61
Routes are only in BGP table and not in L3VPN RIB, except locally connected routes.I must correct myself, in RIB routes are there:
```
[oreggin@rtr1.CPE] > /ip/route/print where bgp-mpls-vpn   
Flags: D - DYNAMIC; A - ACTIVE; y - BGP-MPLS-VPN
Columns: DST-ADDRESS, GATEWAY, DISTANCE
    DST-ADDRESS    GATEWAY     DISTANCE
DAy 10.0.12.8/29   10.0.10.12       200
DAy 10.0.12.16/29  10.0.10.13       200
DAy 10.0.11.8/29   10.0.10.12       200
DAy 10.0.11.16/29  10.0.10.13       200
[oreggin@rtr1.CPE] > /ipv6/route/print where bgp-mpls-vpn 
Flags: D - DYNAMIC; A - ACTIVE; y - BGP-MPLS-VPN
Columns: DST-ADDRESS, GATEWAY, DISTANCE
    DST-ADDRESS         GATEWAY           DISTANCE
DAy b00b:10:12:12::/64  b00b::10:0:10:12       200
DAy b00b:10:13:12::/64  b00b::10:0:10:13       200
DAy b00b:10:12:11::/64  b00b::10:0:10:12       200
DAy b00b:10:13:11::/64  b00b::10:0:10:13       200Difference is IPv4 nexhops has implicit-null and has active remote label, IPv6 nexthops are inactive and has no implicit-null in MPLS FWD table:
```

```
[oreggin@rtr1.CPE] > /mpls/forwarding-table/print 
Flags: L - LDP, P - VPN, V - VPLS
Columns: LABEL, VRF, PREFIX, NEXTHOPS, VPLS
 #   LABEL  VRF    PREFIX              NEXTHOPS                                                  VPLS  
 0 P    32  VRF_A                                                                                      
 1 P    33  VRF_B  b00b:10:11:12::/64                                                                  
 2 P    34  VRF_B  10.0.12.0/29                                                                        
 3 L    40  main   b00b::10:0:10:1     { nh=fe80::20c:42ff:fe53:1491%ether2; interface=ether2 }        
 4 L    41  main   b00b::10:0:10:12    { nh=fe80::20c:42ff:fe53:1491%ether2; interface=ether2 }        
 5 L    42  main   b00b::10:0:10:13    { nh=fe80::20c:42ff:fe53:1491%ether2; interface=ether2 }        
 6 L    37  main   10.0.10.1           { label=impl-null; nh=10.0.0.25; interface=ether2 }             
 7 L    38  main   10.0.10.12          { label=17; nh=10.0.0.25; interface=ether2 }                    
 8 L    39  main   10.0.10.13          { label=18; nh=10.0.0.25; interface=ether2 }                    
 9 L    35  main   10.0.0.0/30         { label=impl-null; nh=10.0.0.25; interface=ether2 }             
10 L    36  main   10.0.1.0/30         { label=impl-null; nh=10.0.0.25; interface=ether2 }             
11 V    29                                                                                       vpls13
12 V    28                                                                                       vpls14
[oreggin@rtr1.CPE] > /mpls/ldp/remote-mapping/print 
Flags: I - INACTIVE; D - DYNAMIC
Columns: VRF, DST-ADDRESS, NEXTHOP, LABEL, PEER
 #    VRF   DST-ADDRESS       NEXTHOP    LABEL      PEER       
 0 ID main  b00b::10:0:10:11             19         10.0.10.1:0
 1 ID main  ::1                          impl-null  10.0.10.1:0
 2 ID main  b00b::10:0:10:1              impl-null  10.0.10.1:0
 3 ID main  b00b::10:0:10:12             20         10.0.10.1:0
 4 ID main  b00b::10:0:10:13             21         10.0.10.1:0
 5 ID main  10.0.10.11                   16         10.0.10.1:0
 6  D main  10.0.10.1         10.0.0.25  impl-null  10.0.10.1:0
 7  D main  10.0.10.12        10.0.0.25  17         10.0.10.1:0
 8  D main  10.0.10.13        10.0.0.25  18         10.0.10.1:0
 9 ID main  10.0.0.24/30                 impl-null  10.0.10.1:0
10  D main  10.0.0.0/30       10.0.0.25  impl-null  10.0.10.1:0
11  D main  10.0.1.0/30       10.0.0.25  impl-null  10.0.10.1:0

---
```

## Response 62
unfortunately the routing itself doesn't work anyway:Routes are only in BGP table and not in L3VPN RIB, except locally connected routes.Exactly the conclusion I felt!And I'll say more... The beeps on my "guess-o-meter" indicate that this has to do with a route recursing to a destination that is not in the FIB.In this case a label, which is represented by a RD/RT. And what's more interesting... A label that works for IPv4 but not for IPv6.I haven't had the time and patience to test this new testing version yet. But I believe that if you do tests with "Next-Hop-Self" or use static routes and try to manipulate the NLRI in the route import filters, I imagine that this L3VPN v6 over LDPv4 scenario can work.I still believe that all of this may be related to this united-but-separate way of displaying IPv4, IPv6, MPLS, etc. routes.In the MikroTik world, "What is RIB?", "What is FIB?", "Are FIBv4 and FIBv6 united or separate?". ---

## Response 63
mikrotik does not Support BGP VPNv6 over IPv4 MPLS LDP transport?
```
[admin@PE2] >  /routing/route/print where afi=vpn6
Flags: U - UNREACHABLE; b - BGP
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
   DST-ADDRESS              GATEWAY          AFI   DISTANCE  SCOPE  TARGET-SCOPE
Ub 2001:db8::/48&65000:105  ::ffff:10.0.0.1  vpn6       200     40            30
Ub fc00:101::/64&65000:100  ::ffff:10.0.0.1  vpn6       200     40            30
Ub fc00:101::/64&65000:101  ::ffff:10.0.0.1  vpn6       200     40            30Pls read the forum, not just posting.viewtopic.php?p=1122915#p1122915hi oregginit's seem that you also got U = unreachable status for vpnv6 next-hopany trick to make it active?

---
```

## Response 64
In Cisco there is "vrf upgrade cli multi af mode common policies"Seems that the equivalent to that is missing in RouterOS.Today, in RouterOS v7, exists the objects:/ip/vrf//routing/table//routing/bgp/vpn/The meaning of all those has some intersection, but only /routing/bgp/vpn/ allows some definition of label bahavior in "label-allocation-policy".Shouldn't the Label-related attribute definition be in /ip/vrf/ or /routing/table/ ?The way it is defined today, it seems that there is no possibility of having a Label linked to a VRF if you are not using BGP.From where I can see it seems that this addition to "main-only" things is affecting the definition of where underlay and overlay begin and end. ---

## Response 65
I haven't had the time and patience to test this new testing version yet. But I believe that if you do tests with "Next-Hop-Self" or use static routes and try to manipulate the NLRI in the route import filters, I imagine that this L3VPN v6 over LDPv4 scenario can work.@fischerdouglas, How do you think VPNv6 could work over IPv4 infra? ---

## Response 66
it's seem that you also got U = unreachable status for vpnv6 next-hopWhere did you see them unreachable?any trick to make it active?Yes, as I mentioned, you MUST use IPv6 BGP neighborship and IPv6 IGP + LDPv6, but won't work with latest stable/testing releases. IIRC last worked with 7.17beta2 or 7.16.x ---

## Response 67
In Cisco there is "vrf upgrade cli multi af mode common policies"Seems that the equivalent to that is missing in RouterOS.Today, in RouterOS v7, exists the objects:/ip/vrf//routing/table//routing/bgp/vpn/The meaning of all those has some intersection, but only /routing/bgp/vpn/ allows some definition of label bahavior in "label-allocation-policy".Shouldn't the Label-related attribute definition be in /ip/vrf/ or /routing/table/ ?The way it is defined today, it seems that there is no possibility of having a Label linked to a VRF if you are not using BGP.From where I can see it seems that this addition to "main-only" things is affecting the definition of where underlay and overlay begin and end.Because only BGP allocates and distributes labels for VPN routes. ---

## Response 68
Pls read the forum, not just posting.viewtopic.php?p=1122915#p1122915hi oregginit's seem that you also got U = unreachable status for vpnv6 next-hopany trick to make it active?Currently IPv4 mapped gateways cannot be resolved. You have to change the gateway to valid ipv6 address with routing filters. ---

## Response 69
it's seem that you also got U = unreachable status for vpnv6 next-hopWhere did you see them unreachable?any trick to make it active?Yes, as I mentioned, you MUST use IPv6 BGP neighborship and IPv6 IGP + LDPv6, but won't work with latest stable/testing releases. IIRC last worked with 7.17beta2 or 7.16.xFlags: U - UNREACHABLE; b - BGPUb 2001:db8::/48&65000:105 ::ffff:10.0.0.1 vpn6 200 40 30 ---

## Response 70
Currently IPv4 mapped gateways cannot be resolved. You have to change the gateway to valid ipv6 address with routing filters.It means it could works without LDPv6? LDPv6 is problematic in interop environment. ---

## Response 71
Where did you see them unreachable?Yes, as I mentioned, you MUST use IPv6 BGP neighborship and IPv6 IGP + LDPv6, but won't work with latest stable/testing releases. IIRC last worked with 7.17beta2 or 7.16.xFlags: U - UNREACHABLE; b - BGPUb 2001:db8::/48&65000:105 ::ffff:10.0.0.1 vpn6 200 40 30viewtopic.php?p=1123531#p1123531Which row contains "U"nreachable flag? ---

## Response 72
Flags: U - UNREACHABLE; b - BGPUb 2001:db8::/48&65000:105 ::ffff:10.0.0.1 vpn6 200 40 30viewtopic.php?p=1123531#p1123531Which row contains "U"nreachable flag?Ub 2001:db8::/48&65000:105 ::ffff:10.0.0.1 vpn6 200 40 30 ---

## Response 73
viewtopic.php?p=1123531#p1123531Which row contains "U"nreachable flag?-U- b 2001:db8::/48&65000:105 ::ffff:10.0.0.1 vpn6 200 40 30 ---

## Response 74
-U- b 2001:db8::/48&65000:105 ::ffff:10.0.0.1 vpn6 200 40 30This is in your RIB, not in mine. You wrote: " it's seem that you also got U = unreachable status for vpnv6 next-hop", but I haven't got because I use native IPv6 datapath for VPNv6. That's why VPNv6 routes are active in my RIB. I hope all clear now :-) ---

## Response 75
How this works? Has someone tried already?
```
*)  cloud - added file-share feature;I enabled it, or at least I thought, but doesn't work.  It says running, and looked based on BTH's relay service to share files over internet.
```

```
/ip/cloud/file-share/settings/print
                enabled: yes                                                                         
               dns-name: <sn>.routingthecloud.net                                            
                 status: running                                                                     
             relay-rtts: EUR1 (ip4: 166.163ms, ip6: timeout)                                         
                         USA1 (ip4: 70.25ms, ip6: timeout)                                           
      relay-ipv4-status: connected (region: USA1 ip: <public ipv4> rtt: 70.25ms reachable: directly )
      relay-ipv6-status: testing rtt                                                                 
          relay-regions: EUR1                                                                        
                         USA1                                                                        
       relay-addressess: <public ipv4>                                                                
                         <public ipv4>.                                                               
  relay-addressess-ipv6: 2a02::<...>                                                          
                         2602::<...>                                                            
            certificate: <sn>.routingthecloud.netAdditionally it does a dynamic firewall rule to allow 443 from anywhere, and generates some HTTPS URLs in /ip/cloud/file-server – which I presume are how you use it — but those didn't work and returned a 404 from the router with a file-share enable:
```

```
/ip/cloud/file-share/print detail 
Flags: X - disabled; I - invalid 
 0    path=/ allow-uploads=yes expires=never key="UaN<keys>hs1" 
      url="https://9b<sn>.routingthecloud.net/s/UaN<keys>hs1" 
      direct-url="https://9b<sn>.routingthecloud.net/s/Ua<keys>hs1?dl" downloads=0With "9b<sn>.routingthecloud.net" address resolves to my router's WAN IP address.And, did find anotherbugwhen trying/ip/cloud/export- it fails to export config for the new /ip/cloud/file-share.  (Thus the "print" output above.)under ip cloud i had to click update force once again and then it has worked. u can also try to replace the domain name with your static ip (if u have one).

---
```