# Thread Information
Title: Thread-1114105
Section: RouterOS
Thread ID: 1114105

# Discussion

## Initial Question
Hello.We use IF-MIB::ifSpeed in zabbix to monitor traffic of interfaces and alert when total bandwidth is above 80% for example. Well, we have one CCR 1036 with ROS 6.37.3 and running a bonding interface with 2 gigabit ports, with means one 2Gbps virtual port right? This is exactly what I get via SNMP.
```
IF-MIB::ifDescr.17=STRING:lagg-uplink
IF-MIB::ifSpeed.17=Gauge32:2000000000But the same is not true when upgrade to ROS 6.39.1, look.
```

```
IF-MIB::ifDescr.16=STRING:lagg-uplink
IF-MIB::ifSpeed.16=Gauge32:1000000000Is this information right? Or this is a BUG of version 6.39.1?

---
```

## Response 1
Hello, updating this post, 6.39.2 have the same problem reported before on 6.39.1.Mikrotik staff, this is clearly a bug, comments? ---

## Response 2
Hello, anyone knows if this issue is OK on new versions? ---

## Response 3
No, this is not fixed yet. Just tested on 6.40.3.
```
interfacebondingprintFlags:X-disabled,R-running0R name="bonding1"mtu=1500mac-address=E4:8D:8C:1B:72:D6 arp=enabled arp-timeout=autoslaves=ether3,ether4 mode=balance-rr primary=none link-monitoring=mii 
      arp-interval=100msarp-ip-targets=""mii-interval=100msdown-delay=0msup-delay=0mslacp-rate=30secstransmit-hash-policy=layer-2min-links=0...
```

```
tool snmp-walk version=2ccommunity=public127.0.0.1oid=.1.3.6.1.2.1.2.2.1.2OID                                                                          TYPE             VALUE1.3.6.1.2.1.2.2.1.2.23octet-stringbonding1...
```

```
tool snmp-walk version=2ccommunity=public127.0.0.1oid=.1.3.6.1.2.1.2.2.1.5OID                                                                          TYPE             VALUE1.3.6.1.2.1.2.2.1.5.23gauge1000000000As we can see, has two interfaces of 1G on this bonding, but the current speed of the bonding interface related by SNMP is 1G not 2G. This bug was initially found on versions 6.39, any plans to solve this?This issue is generating a huge number of false positive alarms on our monitoring system.

---
```

## Response 4
What's new in 6.41rc38 (2017-Oct-03 11:51):...*) snmp - fixed "ifHighSpeed" value of VLAN, VRRP and Bonding interfaces;\o/ ---

## Response 5
Hello, I just make a test with 6.41.3 (and 6.41 also) and the problem persists.ifSpeed and ifHighSpeed are not informing the current speed of the Bonding interface, just of one interface on the bonding.Please, when we can get this solved? ---

## Response 6
Up.Mikrotik staff? ---

## Response 7
The fix "snmp - fixed "ifHighSpeed" value of VLAN, VRRP and Bonding interfaces;" should be backported to bugfix branch considering that many (W)ISP use this release.One more suggestion: set ifSpeed and ifHighSpeed for pppoe client interface to tx rate limit (from profile). In this way I can check if some client is saturating the line for more than T time.Thanks ---

## Response 8
But even on the current version, this not "fix" anything, we are getting the same wrong value.Since 6.39 we can not use this counter properly.It so hard to solve this bug? ---

## Response 9
We have a similar issue, .We have two SXT units online, 1 is responding correctly to the SNMP query, the second has the Ether1 & WLAN Interfaces switched:Both have been ungraded to 6.42.7*** WORKING ***IF-MIB::ifIndex.1 = INTEGER: 1IF-MIB::ifIndex.2 = INTEGER: 2IF-MIB::ifIndex.3 = INTEGER: 3IF-MIB::ifDescr.1 = STRING: ether1IF-MIB::ifDescr.2 = STRING: wlan1IF-MIB::ifDescr.3 = STRING: SXT_Wlan*** NOT WORKING ***IF-MIB::ifIndex.1 = INTEGER: 1IF-MIB::ifIndex.2 = INTEGER: 2IF-MIB::ifIndex.3 = INTEGER: 3IF-MIB::ifDescr.1 = STRING: wlan1IF-MIB::ifDescr.2 = STRING: SXT_WlanIF-MIB::ifDescr.3 = STRING: ether1No idea why but my reporting is all wrong. ---

## Response 10
@marcioeliasWe are also using Zabbix - would you share how you do the followingIF-MIB::ifSpeed in zabbix to monitor traffic of interfaces and alert when total bandwidth is above 80% for example.thank you ---

## Response 11
Hello @tbitech1.For sure.I will do better, just created a git repo to put templates, and this one is there.https://github.com/marcioelias/Zabbix-TemplatesAll you will need to do is translate hardcoded titles in Portuguese.To bypass the problem that was exposed at this thread, I have modified the trigger prototype on the Network discovery to the code below.
```
({TemplateMikrotik-CCR:ifType[{#SNMPVALUE}].last(0)}=6)and(({TemplateMikrotik-CCR:ifHighSpeed[{#SNMPVALUE}].last(0)}>0and{TemplateMikrotik-CCR:ifHCInOctets[{#SNMPVALUE}].avg(300)}>{TemplateMikrotik-CCR:ifHighSpeed[{#SNMPVALUE}].last(0)}*0.8)or({TemplateMikrotik-CCR:ifHighSpeed[{#SNMPVALUE}].last(0)}>0and({TemplateMikrotik-CCR:ifHCOutOctets[{#SNMPVALUE}].avg(300)})>({TemplateMikrotik-CCR:ifHighSpeed[{#SNMPVALUE}].last(0)})*0.8))Basically, I'm ignoring the interface type 161 (LACP) and monitoring just ethernet-like interface types (6).I hope that helps, plus this template will discovery all optical modules and monitoring some data.

---
```

## Response 12
Hi Marcio, Wonderfulwill give it a try and let you know how it works.thank you ---

## Response 13
hi, same problem in 6.44.2Interface bonding1(): Speed 2020-04-15 14:33:25 1 Gbpsany reply from mt when this will be resolved ? ---

## Response 14
This bug still exists on 6.45.7 ---

## Response 15
If you have not yet done, you should send an email tosupport@mikrotik.com. ---

## Response 16
I have the same problem with CCR2116-12G-4S+ on ROS 7.15.2. Bonding with two SFP+, but speed in OID 1.3.6.1.2.1.31.1.1.1.15 is 10 gigabit. ---

## Response 17
I know this in an old post, but i have this issue as well, i know the value can be modified changing the custom multiplier but there must be something that can be done on the mikrotik side as well, i hope there's a solution to this ---