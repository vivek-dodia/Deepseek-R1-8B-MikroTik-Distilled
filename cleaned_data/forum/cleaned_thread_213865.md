# Thread Information
Title: Thread-213865
Section: RouterOS
Thread ID: 213865

# Discussion

## Initial Question
Why do I receive and error like on title when I send a command : > system/hardware/health ? ---

## Response 1
```
[me@myTik]>system/health/printColumns:NAME,VALUE,TYPE#  NAME             VALUE  TYPE0cpu-temperature56CWhere have you found thehardwarepart of the path? The above is from ROS 7.16.2, but I cannot remember any other form of the command for past several years.

---
```

## Response 2
@sindymik 7.16.2.png ---

## Response 3
miksyshela.png ---

## Response 4
I could only find the/system/hardwarepath on a CHR, and there, it has nothing to do withhealth. Vice versa, there are no temperature, voltage, or fan speed sensors on a virtual router, so the/system/healthcannot show any useful values.So what is your routerboard model, and what you actually want to achieve? ---

## Response 5
I'm on CHR installation. I'd like to see if there are some values stored about CPU temp or other. ---

## Response 6
The physical machine on which the CHR is currently running may have tens of CPUs, the CHR gets slices of random ones of them, and at any time it can migrate to another machine. The CHR itself has no way to determine automatically whether it is running on your own hardware or somewhere in a cloud data center.So if you are running the CHR on your own server and want the CHR itself to do something based on this type of data, you'll have to obtain them from the IPMI/iLO/iDRAC/whatever the name of the monitoring and management adaptor your server is equipped with using SNMP or maybe from the hypervisor itself usingssh-exec. ---