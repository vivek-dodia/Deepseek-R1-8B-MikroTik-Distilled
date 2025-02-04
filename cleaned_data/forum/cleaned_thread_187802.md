# Thread Information
Title: Thread-187802
Section: RouterOS
Thread ID: 187802

# Discussion

## Initial Question
Hi to All, I've updated the main router in my school this week from the 6.x to last 7.x version (7.4) and I've started noticing some problem that I haven't noticed in my lab environment:I'm using from many years the "reply-only" arp option on the interfaces of the laboratories of my school, to increase the security, assigning all the ips from the mikrotik's dhcp (static leases), and with the 6.x version, and previous versions, have ever worked perfectly.Now the "reply-only" option seam still working, but I've some problem on the arp table: many of the record of the table from those interfaces are marked as invalid, like this one:mikrotik_arp_problem_example.pngI've tried deleting one of those invalid records from the arp table and made the computer to do a new dhcp request. I can see the leases on the dhcp server that is bound, but nothing appear on the arp table for that device.I've double checked in the dhcp server configuration and the "Add ARP for leases" option is flagged.Here's are part of the configuration of one of the interfaces and the relative dhcp server:
```
/interfacevlanaddarp=reply-onlyinterface="LAN (sfp-sfpplus2)"name="lab_6 (24)"vlan-id=24/ip dhcp-serveraddadd-arp=yes authoritative=after-2sec-delayinterface="lab_6 (24)"\
    lease-time=3dname=lab_6/ip dhcp-server networkaddaddress=10.1.24.0/23dns-server=10.1.100.101,10.1.100.102,10.1.24.254\
    gateway=10.1.24.254netmask=23wins-server=10.1.100.102/ip dhcp-server leaseaddaddress=10.1.25.8comment="igroove - L33-PC08"mac-address=\
    xx:xx:xx:xx:xx:xx server=lab_6Does something have changed on this arp/dhcp server part in the 7.x releases? Could be a bug?Thanks to allBest regardsDaniele

---
```

## Response 1
I have the same problem with version 7.7 ---

## Response 2
Same problem too. Searched a little after upgrading from 6.4 why hotspot was not working....Is there a solution except set enable arp on interface? ---

## Response 3
hellothe same for me but it happens from time to time. all arp are invalid. devices are getting dhcp but have no internet access.I was tryiung to make supout file but each time ccr is been rebooting after 32%.I use hotspot on the bridge where bonding and vlans are setupped. and I had no such issue before upgrading from 6 ROS to 7 ---

## Response 4
I also had the same problem on version 7.9 when I turned on Reply-only ARP, then the Hotspot login page didn't work, I checked the ARP table and it said Invalid ---

## Response 5
Hi to All, I've updated the main router in my school this week from the 6.x to last 7.x version (7.4) and I've started noticing some problem that I haven't noticed in my lab environment:I'm using from many years the "reply-only" arp option on the interfaces of the laboratories of my school, to increase the security, assigning all the ips from the mikrotik's dhcp (static leases), and with the 6.x version, and previous versions, have ever worked perfectly.Now the "reply-only" option seam still working, but I've some problem on the arp table: many of the record of the table from those interfaces are marked as invalid, like this one:mikrotik_arp_problem_example.pngI've tried deleting one of those invalid records from the arp table and made the computer to do a new dhcp request. I can see the leases on the dhcp server that is bound, but nothing appear on the arp table for that device.I've double checked in the dhcp server configuration and the "Add ARP for leases" option is flagged.Here's are part of the configuration of one of the interfaces and the relative dhcp server:
```
/interfacevlanaddarp=reply-onlyinterface="LAN (sfp-sfpplus2)"name="lab_6 (24)"vlan-id=24/ip dhcp-serveraddadd-arp=yes authoritative=after-2sec-delayinterface="lab_6 (24)"\
    lease-time=3dname=lab_6/ip dhcp-server networkaddaddress=10.1.24.0/23dns-server=10.1.100.101,10.1.100.102,10.1.24.254\
    gateway=10.1.24.254netmask=23wins-server=10.1.100.102/ip dhcp-server leaseaddaddress=10.1.25.8comment="igroove - L33-PC08"mac-address=\
    xx:xx:xx:xx:xx:xx server=lab_6Does something have changed on this arp/dhcp server part in the 7.x releases? Could be a bug?Thanks to allBest regardsDanieledo you have to try reboot your router? maybe will work for you

---
```

## Response 6
Seem still the same in 7.11 ---

## Response 7
Issue still there in 7.11Anyone have it running in 7.x ? Can't mikrotik fix this ? ---

## Response 8
Didn't see anything related in 7.12RC changelog...so should still be there in 7.12 ---

## Response 9
Had the similar problem with 7.12.1 on RB952Ui (MIPSBE) but not C53UiG (arm64). The reboot fixed invalid static entries, as they became valid.SUP-137777 (cool number) ---

## Response 10
Still the same with 7.13 ---

## Response 11
Same on 7.13.1Except this time the ARP record remains invalid even after a reboot. To get this fixed I had to remove and re-add the entry. Rebooted after each action, for good measure. ---

## Response 12
Smooth upgrade from 7.13.1 to 7.13.2: the static ARP record was not marked as invalid. Fixed? ---

## Response 13
For me, the problem seems to occur immediately after the hotspot user appears in the active list. As a workaround, disabling the ARP entry and then enabling it using the following hotspot user-profiles On-Login script has solved the problem for now.
```
:localarplist[/ip arp findwheredisabled=no]:foreachiin=$arplistdo={if([/ip arpget$i address]=$address)do={/ip arp disable $i/ip arp enable $i}}To add the script to all Hotspot users (removes current On-Login scripts):
```

```
updated below

---
```

## Response 14
The above script works only for static ARP entries. A workaround for dynamic entries is to disable and enable add-arp-for-leases on the DHCP server.Here is a script that works for both (removes current On-Login scripts):
```
/ip hotspot user profileset[find]on-login="Fix_arp_schedule"/system scriptadddont-require-permissions=noname=Fix_arpowner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":lo\
    cal darplist [/ip arp find where invalid=yes and dynamic=yes]\r\
    \nif ( [:len \$darplist] > 0 ) do={ \r\
    \n:log info [:len \$darplist]\r\
    \n:local dlist [/ip dhcp-server find where add-arp=yes and disabled=no]; \r\
    \n/ip dhcp-server set \$dlist add-arp=no; \r\
    \n/ip dhcp-server set \$dlist add-arp=yes; }\r\
    \n\r\
    \n\r\
    \n:local sarplist [/ip arp find where invalid=yes and dynamic=no and disable\
    d=no]\r\
    \nif ( [:len \$sarplist] > 0 ) do={ \r\
    \n/ip arp disable \$sarplist;\r\
    \n/ip arp enable \$sarplist;\r\
    \n}"/system scriptadddont-require-permissions=noname=Fix_arp_scheduleowner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/\
    system scheduler add name=Fix_arp interval=00:00:01 on-event=\"/system sch\
    eduler remove Fix_arp;/system script run Fix_arp;\""/system scheduleradddisabled=nointerval=5sname=FixArpon-event=Fix_arppolicy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon

---
```

## Response 15
The 7.13.2 -> 7.13.3 upgrade broke the ARP record, it's "invalid" upon the first boot. Had to delete the record, reboot, and add then re-add it. ---

## Response 16
The 7.13.3 -> 7.13.4 upgrade broke the ARP record, it's "invalid" upon the first boot. Toggling the enabled status fixed the issue. ---

## Response 17
What's new in 7.16beta7 (2024-Jul-25 12:55):*) arp - fixed possible issue with invalid entries; ---

## Response 18
What's new in 7.16beta7 (2024-Jul-25 12:55):*) arp - fixed possible issue with invalid entries;Still not working for me on 7.16rc4 when using Hotspot with interfaces that have reply-only ARP, I still get invalid entries. ---

## Response 19
Still not working on final 7.16.....frustating ---

## Response 20
also on my hotspot system.Still not working on final 7.16 ---

## Response 21
Everyone reporting it doesn't work:already created a ticket to support with all relevant info ?Otherwise chances are high they will never see these messages. ---

## Response 22
yes my ticket is "Waiting for support" again. ---

## Response 23
It's crazy how this is still not fixed! ---

## Response 24
The issue is still present in v7.17 ---

## Response 25
same here, showing blank hotspot login pages on ros v7.17 ---