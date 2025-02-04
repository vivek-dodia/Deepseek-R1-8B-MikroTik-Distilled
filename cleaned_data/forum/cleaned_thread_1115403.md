# Thread Information
Title: Thread-1115403
Section: RouterOS
Thread ID: 1115403

# Discussion

## Initial Question
I am monitoring a MikroTik router using SNMP and Zabbix. My goal is to set up alerts for when the router switches from the main ISP to the backup ISP using recursive routing.I am able to retrieve a list of all routes successfully with the following command:
```
snmpwalk-v2c-cpublic10.16.254.31IP-FORWARD-MIB::ipCidrRouteMaskIP-FORWARD-MIB::ipCidrRouteMask.0.0.0.0.0.0.0.0.0.8.8.8.8 = IpAddress: 0.0.0.0But this command generates an error:
```

```
snmpwalk-v2c-cpublic10.16.254.31IP-FORWARD-MIB::ipCidrRouteMask.0.0.0.0.0.0.0.0.0.8.8.8.8IP-FORWARD-MIB::ipCidrRouteMask.0.0.0.0.0.0.0.0.0.8.8.8.8 = No Such Object available on this agent at this OIDAny ideas or suggestions?P.S. RoS 7.15.2 - checked several stable releases - 7.10.2, 7.12.1, 7.14.2

---
```

## Response 1
Have you tried to snmptranslate the hole Mikrotiks own mib.To see if there is the field that you looking for.
```
curl-O https://download.mikrotik.com/routeros/7.15.2/mikrotik.mibsnmptranslate-Tz-m./mikrotik.mib

---
```

## Response 2
Have you tried to snmptranslate the hole Mikrotiks own mib.To see if there is the field that you looking for.
```
curl-O https://download.mikrotik.com/routeros/7.15.2/mikrotik.mibsnmptranslate-Tz-m./mikrotik.mibAs you can see in my first query i get whole routing table (i just posted first line for example, but in fact there are 27 lines - all routes on this device) - objects and it's value. But in second query when i try to get value of any route - it gives me an error. A collegue from telegram channel tried same on 3 different vendors and it works. Only on routeros it fails. I am trying to add item for mikrotik hosts in zabbix and i can't do it using snmp query.Can you check it on one of your devices? Thank you.

---
```

## Response 3
Anyone who who have good skills in SNMP or anyone from Mikrotik - hlp me pls. ---

## Response 4
Hello Mikrotik - i need support:https://help.mikrotik.com/servicedesk/s ... SUP-160152 ---

## Response 5
Have similar problem
```
snmpwalk-Cc-v2c-cpublic10.0.0.1.1.3.6.1.2.1.4.24.4give me 252 routes (out of total 517 listed in winbox), from line number 253 SNMP repeat endlessly route from line 252 with (fake) nexthop 0.0.0.0, until I press CTRL+C (more than 10 000 lines catched before break).7.12.1 (two routers with same ros ver have same behaviour).

---
```

## Response 6
It happening even if I perform SNMWALK without OID specified, reading whole SNMP tree.1.3.6.1.2.1.4.24.4.1.1.10.12.33.192.255.255.255.224.0.0.0.0.0 10.12.33.192.1.3.6.1.2.1.4.24.4.1.1.10.12.34.12.255.255.255.252.0.0.0.0.0 10.12.34.12.1.3.6.1.2.1.4.24.4.1.1.10.12.34.16.255.255.255.252.0.10.12.102.140 10.12.34.16.1.3.6.1.2.1.4.24.4.1.1.10.12.34.20.255.255.255.252.0.10.12.102.140 10.12.34.20.1.3.6.1.2.1.4.24.4.1.1.10.12.34.20.255.255.255.252.0.0.0.0.0 10.12.34.20.1.3.6.1.2.1.4.24.4.1.1.10.12.34.20.255.255.255.252.0.0.0.0.0 10.12.34.20.1.3.6.1.2.1.4.24.4.1.1.10.12.34.20.255.255.255.252.0.0.0.0.0 10.12.34.20 ---

## Response 7
I'm actually working on the very same issue. I have over 20 stores where I need to know when we fall back to secondary ISP (SXT LTE) using zabbix. BTW, I'm using Paessler NSMP Tester and it's been a god-sendSo here's what I have so far based on thedocumentation:Used MIBs in RouterOS:MIKROTIK-MIBMIB-2HOST-RESOURCES-MIBIF-MIBIP-MIBIP-FORWARD-MIBIPV6-MIBBRIDGE-MIBDHCP-SERVER-MIBCISCO-AAA-SESSION-MIBENTITY-MIBUPS-MIBSQUID-MIBUsing Paessler MIB Importer, I downloaded the collection provided on the software downloads section from Mikrotik's website, but that mostly seems to monitor some of their proprietary stuff like neighbors ID-ing, System info (firmware upgrade version, serial, etc) along with other things like partitions, poe, modem.For routing, I believe we need to useIP-FORWARD-MIBbut that link seems to be the latest revision. I foundthiswhich also contains the obsolete and deprecated OIDs and some of those give me info as needed. Specifically, I was looking at the following:To count routes:
```
1.3.6.1.2.1.4.24.3To see Destination
```

```
1.3.6.1.2.1.4.24.4.1.4For any routes heading out, I think this MIB can help filter in zabbix by only keeping all values set to 0
```

```
1.3.6.1.2.1.4.24.4.1.5I'm still in the search for something that tells me when a route is disabled. Once I find it I'll come back and post to see if this can help you generate a trigger for that.

---
```

## Response 8
My earlier post just got approved but, I think I found a way to monitor this usingIP-FORWARD-MIBSpecificallyipCidrRouteStatus
```
1.3.6.1.2.1.4.24.4.1.16Example: I have a site that has been in failover due to an issue, so I can compare the output of one versus another. I've configured my routers like this example:
```

```
/ip routeaddcomment="Carrier 3 - Out"disabled=nodistance=1dst-address=8.8.4.4/32\
    gateway=192.168.88.1pref-src=""routing-table=main scope=10\
    suppress-hw-offload=notarget-scope=10addcomment="Carrier 1 - Out"disabled=nodistance=1dst-address=9.9.9.9/32\
    gateway=123.456.789.123pref-src=""routing-table=main scope=10\
    suppress-hw-offload=notarget-scope=10addcheck-gateway=ping comment="Carrier 1 - Check"disabled=nodistance=1\
    dst-address=0.0.0.0/0gateway=9.9.9.9pref-src=""routing-table=main scope=\10suppress-hw-offload=notarget-scope=11addcheck-gateway=ping comment="Carrier 3 - Check"disabled=nodistance=2\
    dst-address=0.0.0.0/0gateway=8.8.4.4pref-src=""routing-table=main scope=\10suppress-hw-offload=notarget-scope=12Using Paessler I get something like this in response from a routerNOT in failover:
```

```
PaesslerSNMPTester-23.3.87.552Computername:LTM112/18/20242:59:42PM(13ms):Device:1.2.3.412/18/20242:59:42PM(20ms):SNMP v112/18/20242:59:42PM(24ms):Walk1.3.6.1.2.1.4.24.4.1.1612/18/20242:59:42PM(94ms):1.3.6.1.2.1.4.24.4.1.16.0.0.0.0.0.0.0.0.0.8.8.4.4="1"[ASN_INTEGER]<<<Noticebothofmyroutes12/18/20242:59:42PM(165ms):1.3.6.1.2.1.4.24.4.1.16.0.0.0.0.0.0.0.0.0.9.9.9.9="1"[ASN_INTEGER]<<Existhere12/18/20242:59:42PM(226ms):1.3.6.1.2.1.4.24.4.1.16.8.8.4.4.255.255.255.255.0.192.168.1.1="1"[ASN_INTEGER]12/18/20242:59:42PM(287ms):1.3.6.1.2.1.4.24.4.1.16.9.9.9.9.255.255.255.255.0.192.168.200.254="1"[ASN_INTEGER]And this from a deviceIN failover:
```

```
PaesslerSNMPTester-23.3.87.552Computername:LTM112/18/20243:00:17PM(18ms):Device:1.2.3.512/18/20243:00:17PM(23ms):SNMP v112/18/20243:00:17PM(29ms):Walk1.3.6.1.2.1.4.24.4.1.1612/18/20243:00:17PM(120ms):1.3.6.1.2.1.4.24.4.1.16.0.0.0.0.0.0.0.0.0.8.8.4.4="1"[ASN_INTEGER]<<<Noticeonly active shows up12/18/20243:00:17PM(210ms):1.3.6.1.2.1.4.24.4.1.16.8.8.4.4.255.255.255.255.0.192.168.200.1="1"[ASN_INTEGER]12/18/20243:00:17PM(300ms):1.3.6.1.2.1.4.24.4.1.16.9.9.9.9.255.255.255.255.0.123.456.789.123="1"[ASN_INTEGER]12/18/20243:00:17PM(397ms):1.3.6.1.2.1.4.24.4.1.16.10.0.0.0.255.255.255.0.0.172.31.253.254="1"[ASN_INTEGER]So based on this, walk the following OID to get your:0.0.0.0 routes
```

```
1.3.6.1.2.1.4.24.4.1.16.0.0.0.0In my case, I'm using zabbix to check that 9.9.9.9 exists in the walk of the OID. Trigger an alert if it doesn't because that mean's it's not active. I have tested consistently across devices that have 9.9.9.9 and those that do not.On the Zabbix side:I'm creating an Item of type SNMP Agent, SNMP OID is walk[1.3.6.1.2.1.4.24.4.1.16.0.0.0.0.0.0.0.0.0]Under Preprocessing, add > Regular expression > Parameter: (1\.3\.6\.1\.2\.1\.4\.24\.4\.1\.16\.0\.0\.0\.0\.0\.0\.0\.0\.0\.9\.9\.9\.9).* > Output set to OK > Custom on Fail checked > Select "Set value to" and type in FAILEDThis will check that 9.9.9.9 exists (like on Device: 1.2.3.4's response) and create a trigger for when the value is FAILED.Hope this helps, just got to work on it today and I realized there's a few devices that don't have my route

---
```