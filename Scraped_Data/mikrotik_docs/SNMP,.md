---
title: SNMP
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/8978519/SNMP,
crawled_date: 2025-02-02T21:15:08.178259
section: mikrotik_docs
type: documentation
---

* 1Overview
* 2Quick Configuration
* 3General Properties
* 4Community Properties4.1Properties
* 5Management information base (MIB)
* 6Object identifiers (OID)
* 7Traps
* 8SNMP write8.1System Identity8.2Reboot8.3Run Script8.4Running scripts with GET
* 4.1Properties
* 8.1System Identity
* 8.2Reboot
* 8.3Run Script
* 8.4Running scripts with GET
# Overview
Simple Network Management Protocol (SNMP) is an Internet-standard protocol for managing devices on IP networks. SNMP can be used to graph various data with tools such as CACTI, MRTG, or The Dude.
SNMP write support is only available for some OIDs. For supported OIDs SNMP v1, v2 or v3 write is supported.
# Quick Configuration
To enable SNMP in RouterOS:
```
[admin@MikroTik] /snmp> print 
enabled: no
contact: 
location: 
engine-id: 
trap-community: (unknown)
trap-version: 1
[admin@MikroTik] /snmp> set enabled yes
```
You can also specify administrative contact information in the above settings. All SNMP data will be available to communities configured in thecommunitymenu.
# General Properties
Sub-menu:/snmp
--------------
Sub-menu:/snmp
```
/snmp
```
This sub menu allows to enable SNMP and to configure general settings.
Property | Description
----------------------
contact(string; Default:"") | Contact information
enabled(yes | no; Default:no) | Used to disable/enable SNMP service
engine-id(string; Default:"") | For SNMP v3, used as part of the identifier. You can configure the suffix part of the engine id using this argument. If the SNMP client is not capable to detect set engine-id value then this prefix hex has to be used 0x80003a8c04
location(string; Default:"") | Location information
trap-community(string; Default:public) | Which communities configured in thecommunitymenu to use when sending out the trap.
trap-generators(interfaces | start-trap; Default: ) | What action will generate traps:interfaces - interface changes;start-trap - SNMP server starting on the routertemp-exception - send trap when temperature reached 100c (or value configured for cpu-overtemp-temperature at /system health )
trap-interfaces(string | all; Default: ) | List of interfaces that traps are going to be sent out.
trap-target(list of IP/IPv6; Default:0.0.0.0) | IP (IPv4 or IPv6) addresses of SNMP data collectors that have to receive the trap
trap-version(1|2|3; Default:1) | A version of SNMP protocol to use for trap
src-address(IPv4 or IPv6 address; Default:::) | Force the router to always use the same IP source address for all of the SNMP messages
vrf(VRF name; default value:main) | Set VRF on which service is listening for incoming connections
* interfaces - interface changes;
* start-trap - SNMP server starting on the router
* temp-exception - send trap when temperature reached 100c (or value configured for cpu-overtemp-temperature at /system health )
src-address(IPv4 or IPv6 address; Default:::)
vrf(VRF name; default value:main)
# Community Properties
Sub-menu:/snmp community
------------------------
Sub-menu:/snmp community
```
/snmp community
```
This sub-menu allows to set up access rights for the SNMP data.
There is little security in v1 and v2c, just Clear text community string („username“) and the ability for Limiting access by IP address.
In the production environment, SNMP v3 should be used as that provides security - Authorization (User + Pass) with MD5/SHA1, Encryption with DES and AES).
```
[admin@MikroTik] /snmp community> print value-list 
name: public
address: 0.0.0.0/0
security: none
read-access: yes
write-access: no
authentication-protocol: MD5
encryption-protocol: DES
authentication-password: *****
encryption-password: *****
```
## Properties
Property | Description
----------------------
address(IP/IPv6 address; Default:0.0.0.0/0) | Addresses from which connections to SNMP server is allowed
authentication-password(string; Default:"") | Password used to authenticate the connection to the server (SNMPv3)
authentication-protocol(MD5 | SHA1; Default:MD5) | The protocol used for authentication (SNMPv3)
encryption-password(string; Default:"") | the password used for encryption (SNMPv3)
encryption-protocol(DES | AES; Default:DES) | encryption protocol to be used to encrypt the communication (SNMPv3). AES (see rfc3826) available since v6.16.
name(string; Default: ) | 
read-access(yes | no; Default:yes) | Whether read access is enabled for this community
security(authorized | none | private; Default:none) | 
write-access(yes | no; Default:no) | Whether write access is enabled for this community
# Management information base (MIB)
The Management Information Base (MIB) is the database of information maintained by the agent that the manager can query. You can download the latest MikroTik RouterOS MIB file from here:www.mikrotik.com/downloads
Used MIBs in RouterOS:
* MIKROTIK-MIB
* MIB-2
* HOST-RESOURCES-MIB
* IF-MIB
* IP-MIB
* IP-FORWARD-MIB
* IPV6-MIB
* BRIDGE-MIB
* DHCP-SERVER-MIB
* CISCO-AAA-SESSION-MIB
* ENTITY-MIB
* UPS-MIB
* SQUID-MIB
# Object identifiers (OID)
Each OID identifies a variable that can be read via SNMP. Although the MIB file contains all the needed OID values, you can also print individual OID information in the console with theprint oidcommand at any menu level:
```
[admin@MikroTik] /interface> print oid
Flags: D - dynamic, X - disabled, R - running, S - slave 
0 R name=.1.3.6.1.2.1.2.2.1.2.1 mtu=.1.3.6.1.2.1.2.2.1.4.1 
mac-address=.1.3.6.1.2.1.2.2.1.6.1 admin-status=.1.3.6.1.2.1.2.2.1.7.1 
oper-status=.1.3.6.1.2.1.2.2.1.8.1 bytes-in=.1.3.6.1.2.1.2.2.1.10.1 
packets-in=.1.3.6.1.2.1.2.2.1.11.1 discards-in=.1.3.6.1.2.1.2.2.1.13.1 
errors-in=.1.3.6.1.2.1.2.2.1.14.1 bytes-out=.1.3.6.1.2.1.2.2.1.16.1 
packets-out=.1.3.6.1.2.1.2.2.1.17.1 discards-out=.1.3.6.1.2.1.2.2.1.19.1 
errors-out=.1.3.6.1.2.1.2.2.1.20.1
```
# Traps
SNMP traps enable the router to notify the data collector of interface changes and SNMP service status changes by sending traps. It is possible to send out traps with security features to support SNMPv1 (no security). SNMPv2 and variants and SNMPv3 with encryption and authorization.
For SNMPv2 and v3 you have to set up an appropriately configured community as atrap-communityto enable required features (password or encryption/authorization).
# SNMP write
SNMP write allows changing router configuration with SNMP requests. Consider securing access to the router or to router's SNMP, when SNMP and write-access are enabled.
To change settings by SNMP requests, use the command below to allow SNMP to write for the selected community.
```
/snmp community set <number> write-access=yes
```
## System Identity
It's possible to change router system identity by SNMP set command.
```
$ snmpset -c public -v 1 192.168.0.0 1.3.6.1.2.1.1.5.0 s New_Identity
```
* snmpset- SNMP application used for SNMP SET requests to set information on a network entity;
* public- router's community name;
* 192.168.0.0- IP address of the router;
* 1.3.6.1.2.1.1.5.0- SNMP value for router's identity;
SNMPset command above is equal to the RouterOS command:
```
/system identity set identity=New_Identity
```
## Reboot
It's possible to reboot the router with SNMP set command, you need to set the value for reboot SNMP settings, which is not equal to 0.
```
$ snmpset -c public -v 1 192.168.0.0 1.3.6.1.4.1.14988.1.1.7.1.0 s 1
```
* 1.3.6.1.4.1.14988.1.1.7.1.0, SNMP value for the router reboot;
* s 1, snmpset command to set value, value should not be equal to 0;
Reboot SNMPset command is equal to the RouterOS command:
```
/system reboot
```
## Run Script
SNMP write allows running scripts on the router from thesystem scriptmenu when you need to set value for the SNMP setting of the script.
```
$ snmpset -c public -v 1 192.168.0.0 1.3.6.1.4.1.14988.1.1.8.1.1.3.X s 1
```
* X, script number, numeration starts from 1;
* s 1, snmpset command to set value, the value should not be equal to 0;
The same command on RouterOS:
```
/system script> print 
Flags: I - invalid 
0 name="test" owner="admin" policy=ftp,reboot,read,write,policy,
test,winbox,password,sniff last-started=jan/01/1970
01:31:57 run-count=23 source=:beep 
/system script run 0
```
## Running scripts with GET
It is possible to run/system scriptsvia SNMP GET request of the script OID (since 6.37). For this to work SNMP community with write permission is required. OIDs for scripts can be retrieved via the SNMPWALK command as the table is dynamic.
Add script:
```
/system script
add name=script1 owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/sy reboot "
add name=script2 owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="[:put output]"
```
Get the script OID table
```
$ snmpwalk -v2c -cpublic 192.168.88.1 1.3.6.1.4.1.14988.1.1.8
iso.3.6.1.4.1.14988.1.1.8.1.1.2.1 = STRING: "script1"
iso.3.6.1.4.1.14988.1.1.8.1.1.2.2 = STRING: "script2"
iso.3.6.1.4.1.14988.1.1.8.1.1.3.1 = INTEGER: 0
iso.3.6.1.4.1.14988.1.1.8.1.1.3.2 = INTEGER: 0
```
To run the script use table 18
```
$ snmpget -v2c -cpublic 192.168.88.1 1.3.6.1.4.1.14988.1.1.18.1.1.2.2
iso.3.6.1.4.1.14988.1.1.18.1.1.2.2 = STRING: "output"
```