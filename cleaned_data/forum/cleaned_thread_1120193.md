# Thread Information
Title: Thread-1120193
Section: RouterOS
Thread ID: 1120193

# Discussion

## Initial Question
According to the changelog for 7.15 stable a new feature was finally added to the /ip/dns service in RouterOS:https://download.mikrotik.com/routeros/7.15/CHANGELOG
```
*)dns-added VRF support;However I cant make this to work in 7.15.1 stable nor 7.15.2 stable (or 7.16beta2).I can verify that the VRF is properly setup along with the routing tables because I can reach the ether1 interface both locally (on the same external switch as ether1 is connected to) as well as being routed through what this VRF is using as its default gateway.Also outgoing ping and traceroute from the Mikrotik device (CRS326) towards 1.1.1.1 works.But when I do a DNS-lookup locally I get an error:
```

```
/put[:resolve ntp.se]failure:dns server failureSame with going to System->Packages in webfig I get:
```

```
ERROR:couldnotresolve dns name(timeout)The /ip/dns config is pretty straight forward:
```

```
/ip dnssetservers=1.1.1.1vrf=VRF-MGMTSo what am I missing here, have someone in here managed to get the VRF-support for /ip/dns to be working?

---
```

## Response 1
Im guessing noone in here are using /ip/dns along with VRF? ---

## Response 2
The broken VRF-support för /ip/dns have been confirmed for both CRS326-24S+2Q+ and CRS112-8G-4S using both RouterOS 7.15.2 stable and 7.16beta4 testing.Anyone in here who managed to get it working on these or some other Mikrotik model? ---

## Response 3
Interesting - I have a VRF in which I have an interface getting a DHCP address and the DNS, however the DNS is still placed in the main VRF. Probably another bug.
```
[admin@router4]>/ip/vrf/printFlags:X-disabled;*-builtin0;;;FrontVRF
      name="wan"interfaces=ether7,ether81*name="main"interfaces=all[admin@router4]>/ip/dhcp-client/printColumns:INTERFACE,USE-PEER-DNS,ADD-DEFAULT-ROUTE,STATUS,ADDRESS# INTERFACE  USE-PEER-DNS  ADD-DEFAULT-ROUTE  STATUS  ADDRESS0ether8     yes           yes                bound192.168.2.238/24[admin@router4]>/ip/dns/printservers:dynamic-servers:192.168.2.1use-doh-server:verify-doh-cert:nodoh-max-server-connections:5doh-max-concurrent-queries:50doh-timeout:5sallow-remote-requests:yes
          max-udp-packet-size:4096query-server-timeout:2squery-total-timeout:10smax-concurrent-queries:100max-concurrent-tcp-sessions:20cache-size:2048KiBcache-max-ttl:1waddress-list-extra-time:0svrf:main
                   cache-used:41KiBSetting manually the DNS seems to work.
```

```
[admin@router4]>/ip/dns/setvrf=wan servers=192.168.2.1[admin@router4]>/ip/dns/printservers:192.168.2.1dynamic-servers:use-doh-server:verify-doh-cert:nodoh-max-server-connections:5doh-max-concurrent-queries:50doh-timeout:5sallow-remote-requests:yes
          max-udp-packet-size:4096query-server-timeout:2squery-total-timeout:10smax-concurrent-queries:100max-concurrent-tcp-sessions:20cache-size:2048KiBcache-max-ttl:1waddress-list-extra-time:0svrf:wan
                   cache-used:42KiB[admin@router4]>:resolve www.yahoo.fr[admin@router4]>put[:resolve www.yahoo.fr]13.248.158.7[admin@router4]>put[:resolve mikrotik.com]159.148.172.205[admin@router4]>/put[:resolve ntp.se]194.58.200.20Now what doesn't work anymore is using the Mikrotik as a DNS server in the main VRF. Opening a ticket with the support.

---
```

## Response 4
exact same problem here on 2 CCR2004-16G-2S+ on latest stable ROSv7.15.3as soon as DNS is put in a VRF other than "main" resolving gets broken and stops to work, despite VRF routing table is set properly and a "ping vrf=vrfXYZ IP.of.DNS.Srv" is working and shows reachabilitycreated a support ticket SUP-160816 ---

## Response 5
Thanks!So then we can hopefully rule out that this would be some kind of misconfiguration on my side.Question is how the quality assurance works over at Mikrotik or how their config to validate this feature looks like?I have also filed a support ticket SUP-156966 on 24th of june which gives that it have now passed 1 month and 1 week without any reply from Mikrotik on this issue ---

## Response 6
SUbscribing to this topic because I think I am suffering from the same bug. ---

## Response 7
logicly you wouldn't be able toresolvefrom the main table if theDNSis in thevrf. ---

## Response 8
Im suffering the same issue on CRS310-8G+2S+ router os 7.15.3I have my ip address in a vrf on a specific management vlan. default route points in that vrf also but when i set dns that i can ping in the vrf from the device and set them in the vrf, i cant resolve anything ---

## Response 9
I have opened a ticket with the support and they acknowledged the problem...Currently VRF is supported for incoming DNS requests (if your router is the DNS server and it gets requests on VRF interfaces).VRF for outgoing requests is not supported yet (your router connects to DNS server from VRF interface), it is in "To do" list.Unfortunately we cannot give a clear ETA when this feature will be implemented. You will however receive an automated message when this will be fixed. ---

## Response 10
Yep, there was a photo posted some time ago, about picture on the box and actual contents, cannot find it right now, but this one will do: ---

## Response 11
Logged with support #[SUP-173653]VRF is supported only for incoming DNS requests (if your router is the DNS server, and it gets requests on VRF interfaces).VRF for outgoing requests is not supported yetUnfortunately, giving any ETA for when the feature will be implemented is impossible. ---

## Response 12
Hello, Soo... just barging in..Can someone please explain below (how it works if possible):*) dns - added VRF support (CLI only);(taken from some change-logs of a recent ROS version)Thanks and regards, Paul ---

## Response 13
Responding to my own post, it seems that this is no longer CLI only, I think newer Winbox versions matches this option in DNS, ability to select VRF.Someone please correct me, maybe there is more to it. I would very much like DNS to work on any VRF, not only main or whatever I (single only) select in DNS section.Regards, Paul ---

## Response 14
Responding to my own post, it seems that this is no longer CLI only, I think newer Winbox versions matches this option in DNS, ability to select VRF.Someone please correct me, maybe there is more to it. I would very much like DNS to work on any VRF, not only main or whatever I (single only) select in DNS section.Regards, PaulhiDNS is not yet fully VRF aware as i was told by MT support last year (unfortunately i cannot look back into the SUP ticket as of no tickets are shown to me in my account weirdly)VRF setting here is more to be understand like to tell the DNS service on which VRF it will LISTEN for DNS REQs rather than making upstream requests in that VRF (which is not working up until this day) ---

## Response 15
As for the ticket system: there is a default filter to show only open issues in the list. you need to change the filter to "any status". ---

## Response 16
As for the ticket system: there is a default filter to show only open issues in the list. you need to change the filter to "any status".bummer ... thanks for the hint. ---

## Response 17
Responding to my own post, it seems that this is no longer CLI only, I think newer Winbox versions matches this option in DNS, ability to select VRF.Someone please correct me, maybe there is more to it. I would very much like DNS to work on any VRF, not only main or whatever I (single only) select in DNS section.Regards, PaulhiDNS is not yet fully VRF aware as i was told by MT support last year (unfortunately i cannot look back into the SUP ticket as of no tickets are shown to me in my account weirdly)VRF setting here is more to be understand like to tell the DNS service on which VRF it will LISTEN for DNS REQs rather than making upstream requests in that VRF (which is not working up until this day)so here is the last answer i got in SUP-160816SUP-160816_03-01-2025.png ---

## Response 18
Eagerly awaiting to see this feature implemented in 7.18 ---