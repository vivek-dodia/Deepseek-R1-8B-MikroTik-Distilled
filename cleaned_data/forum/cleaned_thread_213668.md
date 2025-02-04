# Thread Information
Title: Thread-213668
Section: RouterOS
Thread ID: 213668

# Discussion

## Initial Question
When configuring DHCP Option 6 (DNS Servers) on 7.17rc3 (not sure if it occurs on prior releases), providing a comma-separated list of IP addresses enclosed in single quotes (the correct format) results in the DHCP server incorrectly interpreting the ASCII representation of the IP address string as IP addresses themselves. This leads to clients receiving nonsensical DNS server IP addresses.
```
/system/package/printColumns:NAME,VERSION,BUILD-TIME,SIZE# NAME      VERSION  BUILD-TIME           SIZE0routeros7.17rc32024-12-1007:40:3210.3MiB1wireless7.17rc32024-12-1007:40:321464.1KiBSteps to Reproduce(including somewhat obvious steps)Create aDHCP Option
```

```
/ip dhcp-server optionaddcode=6name=AlternateDNSvalue="'192.168.1.105,8.8.8.8'"Create aDHCP Option Set
```

```
/ip dhcp-server option-setaddname=HostSpecificDNSoptions=AlternateDNSIdentify aTarget Host: Determine the MAC address of a client device that will be used for testing.Create aStatic DHCP Lease
```

```
/ip dhcp-server leaseaddaddress=192.168.1.101mac-address=XX:XX:XX:XX:XX:XX option-set=HostSpecificDNSserver=dhcp1Renew DHCP Leaseon the ClientObserved BehaviorInstead of receiving the configured DNS servers (e.g., 192.168.1.105 and 8.8.8., the client receives incorrect IP addresses. These incorrect addresses are a direct result of the MikroTik DHCP server interpreting the ASCII representation of the IP address string as octets of an IP address.
```

```
>/ip/dhcp-server/option/printColumns:NAME,CODE,VALUE,RAW-VALUE#  NAME     CODE  VALUE                    RAW-VALUE0option16'192.168.1.105,8.8.8.8'3139322e3136382e312e3130352c382e382e382e38Above you see that if the value is '192.168.1.105,8.8.8.8', the "raw value" seen in MikroTik is 3139322e3136382e312e3130352c382e382e382e38. The client then receives the following incorrect DNS server addresses:nameserver[0] : 49.57.50.46nameserver[1] : 49.54.56.46nameserver[2] : 49.46.49.48nameserver[3] : 53.44.56.46nameserver[4] : 56.46.56.46which areseeminglyrandom IPs in South Korea, until I started looking closer:49.57.50.46 (49='1', 57='9', 50='2', 46='.')49.54.56.46 (49='1', 54='6', 56='8', 46='.')And so on...

---
```

## Response 1
It works as designed. The apostrophe syntax can handle a single IP address but not a list, however, you can concatenate elementary items. So the correct "spelling" looks like this:/ip dhcp-server option add code=6 name=AlternateDNS value="'192.168.1.105''8.8.8.8'" ---

## Response 2
It works as designed. The apostrophe syntax can handle a single IP address but not a list, however, you can concatenate elementary items. So the correct "spelling" looks like this:/ip dhcp-server option add code=6 name=AlternateDNS value="'192.168.1.105''8.8.8.8'"AhhhFantastic, that works. Thank you! ---

## Response 3
Just out of curiosity, what makes you manually define Option 6 rather than just setting the DNS server list on the/ip dhcp-server networkrow? ---