# Thread Information
Title: Thread-213538
Section: RouterOS
Thread ID: 213538

# Discussion

## Initial Question
Hello, What is the best way to restrict access to IPv6 clients to Mikrotik router and, obviously, Internet ?Setup:All LAN interfaces have ARP set to reply-only, IPv4 DHCP-Server has AddressPool set to static-only and IPV4 ARP list is populated with allowed mac addresses.But a new, "rogue" device connected to the network get a valid IPv6 address (invalid/non-routable 169.x.y.z IPv4 address) and can access most of the Internet.How can I prevent that, other that using IPv6 firewall MAC rules ? Not so many rules, but seems to be the slowest method.Thank you! ---

## Response 1
/ipv6 firewall raw add action=drop chain=prerouting ---

## Response 2
I'm afraid I don't understand, that rule will block all IPv6 trafic, including for legitimate devices.Are you suggesting rules like:
```
/ipv6 firewall rawaddaction=accept chain=prerouting src-mac-address=x0:y0:x0:y0:x0:y0addaction=accept chain=prerouting src-mac-address=x0:y0:x0:y0:x0:y1...addaction=drop chain=preroutingWas thinking about rules like that:
```

```
/ipv6 firewall filteraddaction=accept chain=input comment="..."src-mac-address=x0:y0:x0:y0:x0:y0addaction=accept chain=forward comment="..."src-mac-address=x0:y0:x0:y0:x0:y0which double the rules and maintenance involved, so your solution is more elegant.What I don't understand: why reply-only work for IPv4, but not for IPv6 ?Is there a better approach other than IPv6 firewall rules ?Thank you!

---
```

## Response 3
What I don't understand: why reply-only work for IPv4, but not for IPv6 ?Because address acquisition for IPv6 works very differently than for IPv4. For starters there's SLAAC (which is based on RAs and those are elementary for getting routing working) and networked devices assign addresses them selves. Further more, they use multiple IPv6 addresses, one permanent and others intermittently (during certain period of time). Then there's DHCPv6, ROS implementation of server until recently didn't support handing out addresses, it handled only prefixes. And not every client supports DHCPv6, e.g. Android devices only use SLAAC. And while mentioning Android devices, you're probably aware of MAC address anonymity stuff going on with most modern smart phones (they are picking up random MAC addresses unless configured not to).So while blocking devices by MAC address might be the only way of keeping rogue devices out of your network, it's a tedious job ... due to randomizing MAC addresses it's best to white list allowed devices and block all others. But be aware that you can't secure your network if you can't control physical access to it ... ---

## Response 4
Yes, mobile phones are configured to use real MAC addressees, randomization is disabled.Don't know much about SLAAC only that is not DHCP in a regular way and is stateless, does not keep evidence of who's who or who received previously a specific address (leases). Regardless, RA-SLAAC are layer 2 and should be based on MAC which is also layer 2, that's why I didn't understand.It is all about my home devices, all under my management, under 20 devices.Security is needed because I don't want that occasionally used devices like Raspberry Pico, ESP32, generally IoT ones, to get IPv6 and be directly exposed on Internet or to not be able to access Internet at all.Also, on ND I disabled MAC based UID for IPv6:
```
/ipv6 ndsetadvertise-mac-address=noThank you for your support!

---
```

## Response 5
Simplifying SLAAC to the bare bone: the router advertises the upper 64 bits of the address, the device uses its own, slightly mangled, MAC address as the lower 64 bits, and the combination of those two makes the 128 bits of the device's own IPv6 address. So the router does not even know the address of the device in advance.If single rules have to match on individual addresses of devices, MAC or IP, the CPU consumption is about the same regardless whether they are/bridge filteror/ipv6 firewall filterrules; what does make difference, though, is the fact that the ip(v6) firewall can be stateful so you only have to deal with individual addresses when handling the initial packet of each connection. So somewhere between the "accept established or related" rule and "drop the rest" one (which contains an exception for LAN->WAN packets in the default configuration so you have to modify it), place a bunch ofaction=accept src-mac-address=xx:xx:xx:xx:xx:xxrules that will let the initial packets from the "privileged devices" to initiate new connections. The "drop the rest" rule will prevent non-privileged devices from doing the same. ---

## Response 6
I just reading about SLAACfirst local auto-generated address (fe80::/64), check for duplication (DAD), get the prefix from the router and construct the address via mechanism you describe.Already wrote the rules and it is working fine.Thank you! ---

## Response 7
It is all about my home devices, all under my management, under 20 devices.Security is needed because I don't want that occasionally used devices like Raspberry Pico, ESP32, generally IoT ones, to get IPv6 and be directly exposed on Internet or to not be able to access Internet at all.Put those devices in different VLANs + give them ULA addresses + don't implement NAT = No internet access for them. ---