# Thread Information
Title: Thread-1117001
Section: RouterOS
Thread ID: 1117001

# Discussion

## Initial Question
Hi all.I'm having trouble setting up IPv6 on my MikroTik L009UiGS-2HaxD router, which replaced a Ubiquiti AmpliFi that worked out of the box.Despite multiple configuration attempts, I'm seeing UnSpecFail status errors and can't seem to acquire a stable IPv6 address and prefix.I'd prefer not to hardcode addresses but am running out of options.Network SetupNow:ISP -> fiber box -> MikroTik L009UiGS-2HaxD (sfp1)Previously:ISP -> fiber box -> fiber switch -> Ubiquiti AmpliFi (RJ45)Routerbord information
```
routerboard:yes
model:L009UiGS-2HaxDserial-number:redacted
firmware-type:ipq5000
factory-firmware:7.12current-firmware:7.16.1upgrade-firmware:7.16.1IPv6 configuration
```

```
/ipv6 firewall filteraddaction=accept chain=input comment="defconf: accept ICMPv6 after RAW"protocol=icmpv6addaction=accept chain=input comment="defconf: accept established,related"connection-state=established,relatedaddaction=accept chain=input comment="defconf: accept UDP traceroute"dst-port=33434-33534protocol=udpaddaction=accept chain=input comment="defconf: accept DHCPv6-Client prefix delegation."dst-port=546protocol=udp src-address=fe80::/10addaction=drop chain=input comment="defconf: drop all not coming from LAN"in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept established,related,untracked"connection-state=established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"connection-state=invalidaddaction=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1"hop-limit=equal:1protocol=icmpv6addaction=accept chain=forward comment="defconf: accept ICMPv6 after RAW"protocol=icmpv6addaction=accept chain=forward comment="defconf: accept HIP"protocol=139addaction=drop chain=forward comment="defconf: drop everything else not coming from LAN"in-interface-list=!LAN/ipv6 ndset[finddefault=yes]advertise-dns=nodisabled=yes managed-address-configuration=yes mtu=1500other-configuration=yes ra-delay=5sra-interval=5s-30sra-lifetime=none reachable-time=5maddadvertise-dns=nointerface=sfp1 ra-lifetime=none reachable-time=5m/ipv6 nd prefixdefaultsetpreferred-lifetime=20mvalid-lifetime=12h/ipv6 settingssetaccept-redirects=noaccept-router-advertisements=yes max-neighbor-entries=4096FindingsI have confirmed with my ISP that they hand out a ::/56 prefix.Sometimes I receive a link-local address that is added as a gateway in (IPv6 Route List) as DAg with a distance of 1.dhcp log from when dhcp client runs
```

```
1:34:32dhcp,debug,packet send sfp1->ff02::1:2%1311:34:32dhcp,debug,packet type:solicit11:34:32dhcp,debug,packet transaction-id:be031811:34:32dhcp,debug,packet->clientid:00030001789a18fc6dd011:34:32dhcp,debug,packet->ia_na:11:34:32dhcp,debug,packet    t1:011:34:32dhcp,debug,packet    t2:011:34:32dhcp,debug,packet    id:0xa11:34:32dhcp,debug,packet->oro:2311:34:32dhcp,debug,packet->elapsed_time:011:34:32dhcp,debug,packet->ia_pd:11:34:32dhcp,debug,packet    t1:011:34:32dhcp,debug,packet    t2:011:34:32dhcp,debug,packet    id:0xa11:34:32dhcp,debug,packet recv client:sfp1 fe80::redacted->fe80::redacted11:34:32dhcp,debug,packet type:advertise11:34:32dhcp,debug,packet transaction-id:be031811:34:32dhcp,debug,packet->clientid:00030001789a18fc6dd011:34:32dhcp,debug,packet->serverid:000100012763937700505687fc2c11:34:32dhcp,debug,packet->ia_na:11:34:32dhcp,debug,packet    t1:360011:34:32dhcp,debug,packet    t2:720011:34:32dhcp,debug,packet    id:0xa11:34:32dhcp,debug,packet->ia_addr:11:34:32dhcp,debug,packet     address:2001:redacted11:34:32dhcp,debug,packet     valid time:8640011:34:32dhcp,debug,packet     pref.time:5400011:34:32dhcp,debug,packet->status:1-failed11:34:32dhcp,debug,packet->dns_servers:11:34:32dhcp,debug,packet2001:redacted11:34:32dhcp,debug,packet2001:redacted11:34:32dhcp,debug,packet->ia_pd:11:34:32dhcp,debug,packet    t1:360011:34:32dhcp,debug,packet    t2:720011:34:32dhcp,debug,packet    id:0xa11:34:32dhcp,debug,packet->ia_prefix:11:34:32dhcp,debug,packet     prefix:2001:redacted::/5611:34:32dhcp,debug,packet     valid time:8640011:34:32dhcp,debug,packet     pref.time:54000Screenshots from dumpRequestResponseUnSpecFail reference (RFC3315)If a server receives a message that contains options it should notcontain (such as an Information-request message with an IA option),is missing options that it should contain, or is otherwise not valid,it MAY send a Reply (or Advertise as appropriate) with a ServerIdentifier option, a Client Identifier option if one was included inthe message and a Status Code option with status UnSpecFail.Reference threadsviewtopic.php?t=177172viewtopic.php?t=144099https://forum.opnsense.org/index.php?topic=20369.0https://michael.stapelberg.ch/posts/202 ... -ipv6-duidhttps://community.tp-link.com/en/smart- ... Id=1048964https://community.ui.com/questions/UDMp ... 3fafa19008https://www.reddit.com/r/mikrotik/comme ... ipv6_help/

---
```

## Response 1
Having a link local address for the default gateway is normal. Provide all of your IPv6 configuration, not just part of it - commonly the DHCP client settings should not add a default route and only request a prefix, not an address, also there should be no/ipv6 ndentry for the interface providing the WAN connection. ---

## Response 2
Having a link local address for the default gateway is normal. Provide all of your IPv6 configuration, not just part of it - commonly the DHCP client settings should not add a default route and only request a prefix, not an address, also there should be no/ipv6 ndentry for the interface providing the WAN connection.Hey. I did a /ipv6 export. If I do a /export I don't see anything else than what I have already added here.I feel like I have tried with every option. ---

## Response 3
There is no sign of any/ipv6 addressor/ipv6 dhcp-clientin the export yet you have DHCPv6 logging data ---

## Response 4
There is no sign of any/ipv6 addressor/ipv6 dhcp-clientin the export yet you have DHCPv6 logging dataipv6 dhcp-client settings
```
/ipv6 dhcp-clientaddadd-default-route=yes comment="isp prefix"interface=sfp1 pool-name=isp prefix-hint=::/56rapid-commit=norequest=address,prefixuse-interface-duid=yesuse-peer-dns=noipv6 neighbor
```

```
[admin@MikroTik]>/ipv6/neighbor/printFlags:R-router0R address=fe80::redactedinterface=sfp1 mac-address=22:22:00:01:00:01status="stale"ipv6 addresses
```

```
[admin@MikroTik]>/ipv6/address/printFlags:D-DYNAMIC;L-LINK-LOCALColumns:ADDRESS,INTERFACE,ADVERTISE#    ADDRESS                       INTERFACE  ADVERTISE0D::1/128lono1DL fe80::7a9a:18ff:fefc:6dd8/64sfp1no2DL fe80::7a9a:18ff:fefc:6dd9/64brnoI always receive a status: 1 - failed error from the gateway router in the dhcp logs. It does not matter if I only try to request an address or address+prefix or prefix.
```

```
13:24:19dhcp,debug,packet recv client:sfp1 fe80::redacted->fe80::7a9a:18ff:fefc:6dd813:24:19dhcp,debug,packet type:reply13:24:19dhcp,debug,packet transaction-id:0a446f13:24:19dhcp,debug,packet->clientid:00030001789a18fc6dd813:24:19dhcp,debug,packet->serverid:000100012763937700505687fc2c13:24:19dhcp,debug,packet->ia_na:13:24:19dhcp,debug,packet    t1:360013:24:19dhcp,debug,packet    t2:720013:24:19dhcp,debug,packet    id:0xa13:24:19dhcp,debug,packet->ia_addr:13:24:19dhcp,debug,packet     address:2001:redacted13:24:19dhcp,debug,packet     valid time:7835113:24:19dhcp,debug,packet     pref.time:4595113:24:19dhcp,debug,packet->status:1-failed13:24:19dhcp,debug,packet send sfp1->ff02::1:2%1313:24:19dhcp,debug,packet type:solicit13:24:19dhcp,debug,packet transaction-id:23e56e13:24:19dhcp,debug,packet->clientid:00030001789a18fc6dd813:24:19dhcp,debug,packet->ia_na:13:24:19dhcp,debug,packet    t1:013:24:19dhcp,debug,packet    t2:013:24:19dhcp,debug,packet    id:0xa13:24:19dhcp,debug,packet->elapsed_time:0

---
```

## Response 5
Not sure if it helps or not, but this is what I'm using for DHCP client settings (albeit on PPPoE interface):
```
/ipv6 dhcp-clientaddinterface=internet-pppoe pool-name=public-ipv6 pool-prefix-length=60prefix-hint=::/56request=prefixuse-peer-dns=no

---
```

## Response 6
Not sure if it helps or not, but this is what I'm using for DHCP client settings (albeit on PPPoE interface):
```
/ipv6 dhcp-clientaddinterface=internet-pppoe pool-name=public-ipv6 pool-prefix-length=60prefix-hint=::/56request=prefixuse-peer-dns=noUnfortunately not, but thanks for trying.Either MikroTik or my ISP is doing something wrong and they can't seem to get this to work. I assume that the IPv6 was assigned in another way using my old Ubiquiti AmpliFI device. I will try and capture the DHCP traffic using the old Ubiquiti device someday but at the moment I just disabled IPv6 and continued with life.. Too much time spent on this matter...Props to the support team though for investigating this and for trying to fix this issue!

---
```