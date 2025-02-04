# Thread Information
Title: Thread-1122566
Section: RouterOS
Thread ID: 1122566

# Discussion

## Initial Question
Hi thereThere is a need to monitor the number of connectionsThrough the console I can see
```
/ip firewall connection trackingprinttotal-entries:Is it possible to know this information via SNMP? Tell me OID.How do you watch the value of the number of NAT translations on your network?Regards,Pavel

---
```

## Response 1
You can do/ip firewall connection print count-onlyTo get only a count. With the new "run script via snmp" feature it should be possible to read that over snmp.When you succeed in doing that, please show us how. (there is little documentation about this) ---

## Response 2
Hi @pe1chiYou can do/ip firewall connection print count-onlyTo get only a count. With the new "run script via snmp" feature it should be possible to read that over snmp.When you succeed in doing that, please show us how. (there is little documentation about this)Thanks, it's good idea but the principle of the functionRun Scriptare still not clear.I try snmpwalk
```
admin@vspotappliance:~$ snmpwalk-cpublic-v1192.168.2.341.3.6.1.4.1.14988.1.1.8.1.1SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.6=STRING:"script1_password_guest"SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.7=STRING:"script2_first"SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.8=STRING:"radius-ping"SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.9=STRING:"script3"SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.6=INTEGER:0SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.7=INTEGER:0SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.8=INTEGER:0SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.9=INTEGER:0And than try to snmpset
```

```
admin@vspotappliance:~$ snmpset-cpublic-v1192.168.2.341.3.6.1.4.1.14988.1.1.8.1.1.3.9s1SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.9=INTEGER:49What is the value returned by the snmp (49).Is it possible to return another value, such as the value of the variable from the script?

---
```

## Response 3
It is not clear to me either. Hopefully we will get documentation. ---

## Response 4
If you want to read variable from the script, make it global and read it's value from /system script environment. I haven't tried it in your scenario, but it might work since that way variable is always accessible and there is a chance it will have functional OID. ---

## Response 5
There is OID with next parameters:mtxrScriptRunOutput.1.3.6.1.4.1.14988.1.1.18.1.1.2this oid on get request will run script and return it's outputOf course it does not work. Script Run Counter does not increase, and snmp returns the name of the script.
```
admin@vspotappliance:~$ snmpget-cpublic-v1192.168.2.341.3.6.1.4.1.14988.1.1.8.1.1.2.9SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.9=STRING:"script3"We would like to hear comments Mikrotik engineers

---
```

## Response 6
We would like to hear comments Mikrotik engineersIndeed! I also found those OID in the MIB and tried similar things as you did but never was able torun a script from SNMP to receive the output value. It would be a useful feature but I would havepreferred a separate table for OID->script mapping and enabling execution of the script instead ofthe vague "write permission" that is apparently used now. ---

## Response 7
We would like to hear comments Mikrotik engineersIndeed! I also found those OID in the MIB and tried similar things as you did but never was able torun a script from SNMP to receive the output value. It would be a useful feature but I would havepreferred a separate table for OID->script mapping and enabling execution of the script instead ofthe vague "write permission" that is apparently used now.Run the script with the read-only community is not entirely correct from a security standpoint. Who knows what scripts do you have on the equipment, run some risk to the network.Therefore, I agree with the use of the Write rights. ---

## Response 8
Run the script with the read-only community is not entirely correct from a security standpoint. Who knows what scripts do you have on the equipment, run some risk to the network.Therefore, I agree with the use of the Write rights.That is why I would have preferred to have an explicit OID->script table so you explicitly open the execution of scripts on reading certain OIDs (that you define yourself)and you can control which scripts are accessible this way.When a rights bit is used it should have been an explicit one (SNMP). That still leaves the nasty problem that you cannot predict the OID and keep it the same on a number of routers. ---

## Response 9
Hello There, I did it.1. Create a new script to request the number of connections
```
/system scriptaddname=script3_connections owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/ip firewall connection print count-only"2. Through snmpwalk get the script OID table
```

```
admin@vspotappliance:~$ snmpwalk-cpublic-v2c192.168.2.341.3.6.1.4.1.14988.1.1.8.1.1SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.6=STRING:"script1_password_guest"SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.7=STRING:"script2_first"SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.8=STRING:"radius-ping"SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.9=STRING:"script3_connections"SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.6=INTEGER:0SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.7=INTEGER:0SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.8=INTEGER:0SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.9=INTEGER:03. You must change the oid, replace 8 to 181.3.6.1.4.1.14988.1.1.8.1.1.2.9 to 1.3.6.1.4.1.14988.1.1.18.1.1.2.94. Do snmpget. SNMP performs the script and return its output - the number of connections
```

```
admin@vspotappliance:~$ snmpget-cpublic-v2c192.168.2.341.3.6.1.4.1.14988.1.1.18.1.1.2.9SNMPv2-SMI::enterprises.14988.1.1.18.1.1.2.9=STRING:"22"Profit

---
```

## Response 10
Ok that is reasonably simple.I still would have preferred when the OID (at least the last number) is settable in some screen andthe scripts would only be runnable when in that table.Now you have given the script all access and probably people often do that, and it means that nowtheir scripts can be run by anyone knowing the read-only SNMP community. (usually public) ---

## Response 11
it means that nowtheir scripts can be run by anyone knowing the read-only SNMP community. (usually public)In fact noI have noticed that the script is executed and returns its output only if the community has a right to writeIt may seem strange because we produce snmpget read operation, but it's true. You do not run the script with read-only community. ---

## Response 12
Ah that is why it failed to work here... I experimented but never got the above result.Well, that is not good either! It should be possible to read from the read-only community andstill execute a (trusted) script to provide the value. E.g. to graph some values using standardmonitoring software that reads all variables using the same community. ---

## Response 13
Ah that is why it failed to work here... I experimented but never got the above result.Well, that is not good either! It should be possible to read from the read-only community andstill execute a (trusted) script to provide the value. E.g. to graph some values using standardmonitoring software that reads all variables using the same community.Ok. It is another question. It is suitable for solving my problem ---

## Response 14
Hello There, I did it.1. Create a new script to request the number of connections
```
/system scriptaddname=script3_connections owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/ip firewall connection print count-only"2. Through snmpwalk get the script OID table
```

```
admin@vspotappliance:~$ snmpwalk-cpublic-v2c192.168.2.341.3.6.1.4.1.14988.1.1.8.1.1SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.6=STRING:"script1_password_guest"SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.7=STRING:"script2_first"SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.8=STRING:"radius-ping"SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.9=STRING:"script3_connections"SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.6=INTEGER:0SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.7=INTEGER:0SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.8=INTEGER:0SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.9=INTEGER:03. You must change the oid, replace 8 to 181.3.6.1.4.1.14988.1.1.8.1.1.2.9 to 1.3.6.1.4.1.14988.1.1.18.1.1.2.94. Do snmpget. SNMP performs the script and return its output - the number of connections
```

```
admin@vspotappliance:~$ snmpget-cpublic-v2c192.168.2.341.3.6.1.4.1.14988.1.1.18.1.1.2.9SNMPv2-SMI::enterprises.14988.1.1.18.1.1.2.9=STRING:"22"ProfitThanks this works for me.Best regards.

---
```