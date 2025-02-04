# Thread Information
Title: Thread-213203
Section: RouterOS
Thread ID: 213203

# Discussion

## Initial Question
Is mynetname down again? My CNAME for that name has been down since about 9:55pm. ---

## Response 1
Seems to be. Mine isn’t working either. And the forum seems very slow. ---

## Response 2
Also i was looking for dns problem with mynetname.net.Does the mynetname is down? ---

## Response 3
I think I'm seeing a similar issue.
```
/ip cloud printshows the IP being updated, but actual DNS resolution against *.mynetname.net seems to getting a "Server failed" response.

---
```

## Response 4
Yep, looks like it died again. It's been a while since there was a crash ---

## Response 5
Yep, down for me too from around 20:57 UTC ---

## Response 6
Down for me and all clients at around 21 UTC too. ---

## Response 7
ETA? ---

## Response 8
Down for me too. ---

## Response 9
Yeap, it is down, waiting for the resolution... ---

## Response 10
Yes, waiting for a resolution. ---

## Response 11
Yup, seems down.And also means BackToHome (BTH) is down too....Just tried enabling on a router and it gets stuck at "allocating endpoint" ---

## Response 12
yup, mynetname is down here in Mexico too ---

## Response 13
It wasn't a good idea to use this MikroTik functionality.I have this in the production environment and everything is stopped.ETA? ---

## Response 14
Since DDNS going down is an ongoing issue, I wish Mikrotik would provide a website that informs people about what's happening. The website could possibly include an ETA. ---

## Response 15
have several across the US down. My first detection was 15:46 CST, ETA would be nice. Also noticed the forum lagging and mikrotik.com reported offline from a down detector and down for me, china cut another cable? ---

## Response 16
Since DDNS going down is an ongoing issue, I wish Mikrotik would provide a website that informs people about what's happening. The website could possibly include an ETA.Perhaps they need to start with a pager for someone... They don't seem to do well with issues in middle of the [Riga] night... ---

## Response 17
No they need to protect their services with cloudflare and then have the eureka moment of making cloudflare zerotrust an option package on at least ARM routers LOL. ---

## Response 18
Same for me, Toronto, Canada.Alarm was triggered, incident logged at Dec 10, 2024, 03:56PM GMT-5 ---

## Response 19
My HK-Gateway [1] is not working due to the xyz.sn.mynetname.net. I changed it to other DDNS to recover. I wish it can be fixed as soon as possible.Ref.[1]viewtopic.php?t=213013 ---

## Response 20
Still down!! GMT+2 zone timeAny official announcement? ---

## Response 21
We have over 100 mynetname sites on our monitoring servers that are flapping, they resolve some of the time, and then other times not. Static IP's work 100% for the same sites. ---

## Response 22
still down ---

## Response 23
Even mikrotik.com is down. I have a MTCNA exam schedule at this time. Really mikrotik? No high availability servers? Invest so much in R&D smh ---

## Response 24
Still down from Brazil, looking for imediate solution ---

## Response 25
Still down. Likely a DDOS attack on all services since even the forum feels sluggish. ---

## Response 26
Why is there no official comment from Mikrotik?Are they still asleep? ---

## Response 27
+1 Down ---

## Response 28
Still down from Poland. ---

## Response 29
STILL DOWN!!! ---

## Response 30
i think mikrotik resolvers are not responding159.148.172.251 and 159.148.147.201.I tried but no response ---

## Response 31
I have opened support ticket ---

## Response 32
Down for me too. ---

## Response 33
mynetname.net DNS server daemon responds sometimes (ns1/ns2.kissthenet.net).Maybe backend database for dynamic device serial <-> IP mappings is down?Good Morning, Riga. Time to wake up.
```
# dig @ns1.kissthenet.net <redacted serial>.sn.mynetname.net in cname
; <<>> DiG 9.18.28-0ubuntu0.24.04.1-Ubuntu <<>> <redacted serial>.sn.mynetname.net in cname
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 53986
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0

...

---
```

## Response 34
Down - South Africa ---

## Response 35
STILL DOWN - RomaniaPlease resolve it ASAP ---

## Response 36
+1 from Greece ---

## Response 37
We rely heavily on this service for stable connectivity, but it appears to be non-functional at the moment.Is there any alternative solution we can use to ensure a stable connection?We depend on this service for critical operations, so having a reliable alternative or knowing when it will be restored would be greatly appreciated. ---

## Response 38
Same problem. Ukraine. ---

## Response 39
Hi, Same here in Hungary.BrJanos Vincze ---

## Response 40
We rely heavily on this service for stable connectivity, but it appears to be non-functional at the moment.Is there any alternative solution we can use to ensure a stable connection?We depend on this service for critical operations, so having a reliable alternative or knowing when it will be restored would be greatly appreciated.Hi, DuckDNS works well with Mikrotik routers (update dns with script). But it is not the best alternative if you are using BTH Vpn.Br, Janos Vincze ---

## Response 41
We depend on this service for critical operations, so having a reliable alternative or knowing when it will be restored would be greatly appreciated.Universal solution would be for Mikrotik to implement DNS RFC2136 support allowing dynamic record updates to *any* standards compliant DNS server/service.Now they have their own custom dynamic DNS protocol and kissthenet.net servers.World is full of custom, free and commercial dynamic DNS services and protocols, but RFC2136 should be first to be implemented. ---

## Response 42
Same problem. México ---

## Response 43
Is there any alternative solution we can use to ensure a stable connection? We depend on this service for critical operations, so having a reliable alternative or knowing when it will be restored would be greatly appreciated.Pro tip: Don’t use these services for business-critical operations. We’ve switched to another provider since there have been plenty of issues in the past. ---

## Response 44
Same problem. Belarus.But the first thought was that it doesn't work because of some new sanctions... ---

## Response 45
Still down159.148.147.201 ns1.kissthenet.net:DNS daemon responds (very infrequently) but does not reach records database for serial # <-> IP mappings159.148.172.251 ns2.kissthenet.net:DNS daemon (udp/53, tcp/53) seems to be completely offline ---

## Response 46
I've found following script that updates your DDNS in no-ip service. You can add it as script and set to run in scheduler under system setting.
```
# No-IP DDNS Updater
# http://www.noip.com/integrate/

:global publicIP;
:global abortUpdate;

:if ([:typeof $abortUpdate] != "bool") do={
	:set $abortUpdate false;
}

:if ($abortUpdate) do={
	:error "DDNS: Update aborted. Intervention required.";
}

:local currentIP;
:local targetInterface "ether1";

:local ddnsUser "yourusername";
:local ddnsPass "yourpassword";
:local ddnsHost "youraddress";
:local ddnsURL "http://dynupdate.no-ip.com/nic/update?hostname=$ddnsHost&myip=$currentIP";

:if ($targetInterface = "ether1") do={
	:local response [/tool fetch url="http://ip1.dynupdate.no-ip.com/" as-value output=user];
	:if ($response->"status" = "finished") do={
		:set currentIP ($response->"data");
	} else={
		:set currentIP "";
	}
} else={
	:set currentIP [/ip address get [/ip address find interface=$targetInterface] address];
	:if ([:typeof $currentIP] = nil) do={
		:error "DDNS: No IP obtained.";
	} else={
		:set $currentIP [:pick [:tostr $currentIP] 0 [:find [:tostr $currentIP] "/"]];
	}
}

:if ($currentIP != $publicIP) do={
	:local response [/tool fetch url=$ddnsURL user=$ddnsUser password=$ddnsPass as-value output=user];
	:if ($response->"status" = "finished") do={
		:local data ($response->"data");
		:set $abortUpdate (!([:pick $data 0 4] = "good" || [:pick $data 0 5] = "nochg"));
		:set $publicIP $currentIP;

		:log info "DDNS: Update succeeded."
	} else={
		:log error "DDNS: Update failed.";
	}
} else {
	:log info "DDNS: No IP change.";
}Source:https://gist.github.com/frosty024/3a3fd ... 2f3cb14a1a

---
```

## Response 47
Service is back online! Finally! ---

## Response 48
We have identified the issue and a fix is coming shortly. ---

## Response 49
World is full of custom, free and commercial dynamic DNS services and protocols, but RFC2136 should be first to be implemented.Sure, build-in would be best, but plenty of mikrotik scripts out there for updating DNS servers. ---

## Response 50
Current issue aside I just wish that they would start using more respectable domains names for this dynamic DNS service.kissthenet.net and mynetname.net sound more like highly suspicious chinese spam operation than reliable DNS service.Maybe something with their main brand domain like:ns1.dyn.mikrotik.comns2.dyn.mikrotik.comand CNAMEs as:<serial>.sn.mikrotik.com IN CNAME <ip> ---

## Response 51
Finally, the service is back.The question is, can we trust this service in the future? ---

## Response 52
It seems to be working now, checking from Greece. BTW, free service means "Best effort" SLA... If critical systems depend on connectivity other means should be used for DDNS, usually with a fee. ---

## Response 53
No they need to protect their services with cloudflare and then have the eureka moment of making cloudflare zerotrust an option package on at least ARM routers LOL.It would be great to have zero trust inside mikrotik. +1Is mynetname down again? My CNAME for that name has been down since about 9:55pm.what software do you use to monitor status? uptime kuma? ---

## Response 54
It's ok!264 routers are updated in cloud! ---

## Response 55
The build in DDNS outage make everyone a lot of system outage.I am planing to switch to update the dns record public ip to cloudflare API by using scheduler script.
```
# get the public ip address
:global debugA [/tool/fetch url=https://api.ipify.org output=user as-value];
:global debugA1 ($debugA->"data");

# set the public ip address
:local $zone_id xxxxxxxxxxxxxxxxxxx
:local $redord_id xxxxxxxxxxxxxxxxxxx
:local $auth_api_token xxxxxxxxxxxxxxxxxxx
:global debugB [/tool fetch url="https://api.cloudflare.com/client/v4/zones/$zone_id/dns_records/$redord_id" http-method=patch http-header-field="Content-Type: application/json,Authorization: Bearer $auth_api_token" http-data="{\"content\":\"$debugA1\"}" output=user as-value];
:global debugB1 ($debugB->"status")
:global debugB2 ($debugB->"data")

---
```

## Response 56
It's still broken. ---

## Response 57
Finally, the service is back.The question is, can we trust this service in the future?This happens every 1-2 years, it's not the first timeUpd: some routers work, some still not ---

## Response 58
Nameservers are usually rock stable. But I have no idea of the architecture of this cloud service tbh. It is what it is:a convenient feature for home users or personal use. My opinion: don't rely on it for critical access or in commercial environment. It is out of your control. ---

## Response 59
None of you can complain about anything, since the service is not paid, it is not included in the RuterOS license, it is just a freecourtesythat MikroTik does.Relying on it for work is crazy. ---

## Response 60
HelloIt has been working for 10 minutes and it fails again, are you having a DDOS or is it an update that is giving you problems? ---

## Response 61
Yesterday my DNS IP Cloud stopped working.
```
C:\Users\xxx>nslookup
Default Server:  home.com
Address:  192.168.10.1

> server 8.8.8.8
Default Server:  dns.google
Address:  8.8.8.8

> 6f3--------60.sn.mynetname.net
Server:  dns.google
Address:  8.8.8.8

DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
*** Request to dns.google timed-outSettings has not changed.  Forced update does not help.This has worked fine for years.ddns_error.png

---
```

## Response 62
Greece still down is this a DDoS ? ---

## Response 63
viewtopic.php?t=213191 ---

## Response 64
Down from yesterday at 00:00+ ... all the services not usable, thanks god we have another host from other service... what happened? Maybe they want to charge the service? They try to change all the corporate type and be like cisco? Let's see... We will change all the hardware if Mikrotik change corporate stategies to be like ultra capitalistic cisco... In the first we choose this software-hardware for the diferrence of all the other companies... if it is the same this is bad for reputation and most of us will go to another software-hardware setup. ---

## Response 65
Did not see that thread, since I did search for the service name that is IP Cloud ---

## Response 66
Still down for me - South Africa. ---

## Response 67
Same problem. Bulgaria ---

## Response 68
viewtopic.php?t=213191Threads merged. ---

## Response 69
It seems to be working now, checking from Greece. BTW, free service means "Best effort" SLA... If critical systems depend on connectivity other means should be used for DDNS, usually with a fee.Correct attitude ! ---

## Response 70
same issue here ---

## Response 71
No need for +1 comments. You already have the attention by Mikrotik.We have identified the issue and a fix is coming shortly. ---

## Response 72
MikroTik Cloud, mynetname is down, Makedonija ---

## Response 73
No need for +1 comments. You already have the attention by Mikrotik.We have identified the issue and a fix is coming shortly.I'm sorry, but people are lazy & lazy, they don't read what is written before. ---

## Response 74
Hi every1, Working for me on most resolvers since about 10h20 CETI've setup a backup Cloudflare DDNS thoughRegards! ---

## Response 75
Down from yesterday at 00:00+ ... all the services not usable, thanks god we have another host from other service... what happened? Maybe they want to charge the service? They try to change all the corporate type and be like cisco? Let's see... We will change all the hardware if Mikrotik change corporate stategies to be like ultra capitalistic cisco... In the first we choose this software-hardware for the diferrence of all the other companies... if it is the same this is bad for reputation and most of us will go to another software-hardware setup.If you are a corporate client who relies on FREE dynamic DNS service for your critical functions, the problem is poor design. ---

## Response 76
Indeed, works here again as well. Didnotset up a Cloudflare DDNS though. ---

## Response 77
Google 8.8.8.8 still does not see my xxx60.sn.mynetname.net ---

## Response 78
Current issue aside I just wish that they would start using more respectable domains names for this dynamic DNS service.kissthenet.net and mynetname.net sound more like highly suspicious chinese spam operation than reliable DNS service.Maybe something with their main brand domain like:ns1.dyn.mikrotik.comns2.dyn.mikrotik.comand CNAMEs as:<serial>.sn.mikrotik.com IN CNAME <ip>just use your own dns, set up a cname to the ugly domain name and problem solved.remotepotato.mybeautifuldomainname.com cname to serial.ugly.mynetname.comProblem solved. ---

## Response 79
just use your own dns, set up a cname to the ugly domain name and problem solved.Is not.Even if your own DNS server can reply with CNAME record, clients still won't be able to resolve the serial.sn.mynetname.net ... the only way around it is to actually update A record on your DNS server whenever WAN IP address changes. Since you have full control over both entities (router with dynamic address and DNS server), it's possible to script some hack (which might work just fine). ---

## Response 80
It seems to be working now, but it would be nice if MT post a message telling that all are ok. ---

## Response 81
@JotneFrom @normis:We have identified the issue and a fix is coming shortly. ---

## Response 82
MikroTik Cloud, mynetname is down, Makedonijapozdrav majstore! ---

## Response 83
@JotneFrom @normis:We have identified the issue and a fix is coming shortly.I did off course read that. But it now seems to work and since no more post not working for me too, it would be nice with an update from MT, like:Error found and we have fixed the problem. ---

## Response 84
From: @rextended to @jontneFrom @normis:We have identified the issue and a fix is coming shortly.Yeah, since Normis is not saying the issue has actually been fixed, just that they've identified it. So we’ll have to wait for feedback, hopefully coming when it's done. ---

## Response 85
It is now fixed. Sorry for the wait. ---

## Response 86
I'd like to suggest a public status page for Mikrotik services. So people don't have to flood forum and support helpdesk with all the same "omg, it is down" reports. ---

## Response 87
We depend on this service for critical operations, so having a reliable alternative or knowing when it will be restored would be greatly appreciated.Universal solution would be for Mikrotik to implement DNS RFC2136 support allowing dynamic record updates to *any* standards compliant DNS server/service.FWIW, RouterOS does support RFC2136 updates – /tool/dns-update:https://help.mikrotik.com/docs/spaces/R ... ynamic+DNS.It is not what /ip/cloud uses, but they do support RFC-2136 via scripting. ---

## Response 88
FWIW I wrote a quickie script to update CloudFlare DNS directly last night.
```
:local wanInterface "ether1"
 	#DNS Zone ID 
       :local zoneID “12345" 
       #DNS record ID
       :local recordID "12345"
       #your API token
       :local apiToken "12345"

# determine if we use the dhcp script or the current address
 :if ([:typeof $"lease-address"] = "nothing") \
	do={:local myIP [:pick [/ip address get [find where interface=$wanInterface] address] 0 [:find [/ip address get [find where interface=$wanInterface] address] "/"]]; \
		/tool fetch check-certificate=yes url="https://api.cloudflare.com/client/v4/zones/$zoneID/dns_records/$recordID" http-method=patch http-header-field="Content-Type:application/json,Authorization:Bearer $apiToken" http-data="{\"content\":\"$myIP\"}"; \
	} \
	else={/tool fetch check-certificate=yes url="https://api.cloudflare.com/client/v4/zones/$zoneID/dns_records/$recordID" http-method=patch http-header-field="Content-Type:application/json,Authorization:Bearer $apiToken" http-data="{\"content\":\"$"lease-address"\"}"; \
	}The idea is you save this to /system/scripts and then add the script name to the dhcp clientscriptproperty. It’ll then run automatically when the router gets a new lease. Or you can run it manually.

---
```

## Response 89
I'd like to suggest a public status page for Mikrotik services. So people don't have to flood forum and support helpdesk with all the same "omg, it is down" reports.+1 ---

## Response 90
Perhaps a bit of clarity in MT Docs will help!OverviewSub-menu: /ip cloudPackages required: routerosRouterOS version required: v7.12 and newerHardware requirements: ARM/ARM64/TILE architecture devicesBack To Home is a convenientand freefeaturewhose 'uptime' is not 100% guaranteed*** and should not be used for business purposes.BTH allows one to configure their device for secure VPN access from anywhere in the world to your router and your network, even if your router does not have a public IP address, is behind NAT or Firewall.*** Mikrotik servers, supporting mynetname and wireguard relay are periodically unavailable due to circumstances beyond our control.and further suggestion to CLoud Doc page here --> { to keep my good friend, extended, happy } -->viewtopic.php?p=1114263#p1114263 ---

## Response 91
Hong Kong and China Mainland at HK time +8 11:42 cannot resolve mynetname and also changeip.Now both IPs are okay. ---

## Response 92
I do not agree about this:should not be used for business purposes.If you are aware of that nothing is guaranteed and you do not have problem with some outage, why not use it for business.Its a price/quality question.DynDNS was down for 10+ hour. I can just use my cellphone as an router and connect to it and work. ( I do now that its not possible for all to do that) ---

## Response 93
Around this outage i made a more user friendly cloudflare update script. Hope it helps to anyone.
```
########################################################################################

  # Cloudflare stuff
  :local ApiToken "_CLOUDFLARE_API_TOKEN_";
  :local ZoneId "_CLOUDFLARE_ZONE_ID_";
  :local DnsServer "1.1.1.1"; 

  # Records to update
  :local DnsRecords {"aaa.aaa.aaa"; "bbb.bbb.bbb"; "ccc.ccc.ccc"; \
                     "ddd.ddd.ddd"; "eee.eee.eee"; "fff.fff.fff"; \
                     "ggg.ggg.ggg"; "hhh.hhh.hhh"};

  # Interface to use
  :local WanInterface "_WAN_INTERFACE_";

########################################################################################
########################################################################################

  # Wait some for dhcp lease
  :delay 10;

  # Fetch WAN_IP from interface
  :local WanIp [/ip address get [find interface=$WanInterface] address];
  :set WanIp [:pick $WanIp 0 ([:len $WanIp] -3)];

  :foreach DnsRecord in=$DnsRecords do={
    :do {
      # Resolve DNS_IP from dns
      :local DnsIp [:resolve domain-name=$DnsRecord server=$DnsServer];

      # Compare and update if they differ
      :if ($WanIp != $DnsIp) do={
        # Prepare request payload
        :local ReqRead ("https://api.cloudflare.com/client/v4/zones/" . $ZoneId . "/dns_records?name=" . $DnsRecord);
        :local ReqAuth ("Authorization: Bearer " . $ApiToken . ", Content-Type: application/json");

        # Query dns record
        :local Resp [/tool fetch mode=https http-method=get url=$ReqRead http-header-field=$ReqAuth as-value output=user];
        :local Data [:deserialize from=json value=($Resp->"data")];

        # Check operation result
        :if ($Data->"success" != true) do={
          :error "Failed to retrieve record data.";
        }

        # Retrieve dns_record_id
        :local DnsRecordId ($Data->"result"->0->"id");

        # Prepare request payload
        :local ReqModi ("https://api.cloudflare.com/client/v4/zones/" . $ZoneId . "/dns_records/" . $DnsRecordId);
        :local ReqData ("{\"type\":\"A\",\"name\":\"" . $DnsRecord . "\",\"content\":\"" . $WanIp . "\",\"ttl\":1,\"proxied\":false}");

        # Perform the update
        :set Resp [/tool fetch mode=https http-method=put url=$ReqModi http-header-field=$ReqAuth http-data=$ReqData as-value output=user];
        :set Data [:deserialize from=json value=($Resp->"data")];

        # Check operation result
        :if ($Data->"result"->"content" != $WanIp) do={
          :error "Failed to update record.";
        }

        :log info ("CF_DDNS: Update of \"" . $DnsRecord . "\" successful.");
      }
    } on-error={
      :log info ("CF_DDNS: Error in \"" . $DnsRecord . "\" update.");
    }
  }

########################################################################################

---
```

## Response 94
Mikrotik Cloud down since yesterday Dominican Republic ---

## Response 95
I do not agree about this:should not be used for business purposes.If you are aware of that nothing is guaranteed and you do not have problem with some outage, why not use it for business.Its a price/quality question.DynDNS was down for 10+ hour. I can just use my cellphone as an router and connect to it and work. ( I do now that its not possible for all to do that)Clearly you are not paying attention, many folks are using this service for business and were complaining, aka way more than your voice of one.To be truthful, dont care about such idiots, I want the regular joe soho and home users to be aware of the limitations of the free service and especially if they rely on BTH. ---

## Response 96
It is now fixed. Sorry for the wait.It still doesn't seem to work on pure ipv6 networks. Please investigate it ---

## Response 97
```
cloud2.mikrotik.comis still not reachable over IPv6 from where I am (tested with two ISPs from my country, Vietnam). Trace route shows the last responding hop is
```

```
2a02:2330:f:41::2which is in Riga. It also shows that I am routed over Hong Kong, using nodes from AS1299 (Arelion). If I use their looking glass tool to do a traceroute from their HK location, I see theexact same hops, with the difference is that cloud2.mikrotik.com does respond 4 hops after
```

```
2a02:2330:f:41::2!https://lg.twelve99.net/?type=tracerout ... :4000::251
```

```
Router: hnk-b4 / Hong Kong (MEGA-i)
Command: traceroute ipv6 2a02:610:7501:4000::251

traceroute to 2a02:610:7501:4000::251 (2a02:610:7501:4000::251), 30 hops max, 80 byte packets
 1  mei-b6-v6.ip.twelve99.net (2001:2034:0:36::1)   156.203 ms  156.250 ms mei-b5-v6.ip.twelve99.net (2001:2034:0:15a::1)   155.363 ms
 2  ffm-bb1-v6.ip.twelve99.net (2001:2034:1:6b::1)   169.800 ms ffm-bb2-v6.ip.twelve99.net (2001:2034:1:6c::1)   169.741 ms  169.673 ms
 3  sto-bb1-v6.ip.twelve99.net (2001:2034:1:c4::1)   191.640 ms sto-bb2-v6.ip.twelve99.net (2001:2034:1:c5::1)   188.897 ms sto-bb1-v6.ip.twelve99.net (2001:2034:1:c4::1)   191.710 ms
 4  * * *
 5  siatet-ic-355842.ip.twelve99-cust.net (2001:2035:0:21c8::2)  210.563 ms  210.807 ms  210.802 ms
 6  2a02:2330:f:41::2 (2a02:2330:f:41::2)  205.067 ms  203.260 ms  205.321 ms
 7  * * *
 8  * * *
 9  * * *
10  cloud2.mikrotik.com (2a02:610:7501:4000::251)  199.486 ms  201.147 ms  199.449 msSo, it looks like MikroTik (or one of the 3 hops before them) is blocking IPv6 source addresses from my ISPs. I have no problems reaching other IPv6 services around the world. As a result /ip/cloud only produce an A-record for my router, and no AAAA-record.

---
```

## Response 98
```
cloud2.mikrotik.comis still not reachable over IPv6 from where I am (tested with two ISPs from my country, Vietnam). Trace route shows the last responding hop is
```

```
2a02:2330:f:41::2which is in Riga. It also shows that I am routed over Hong Kong, using nodes from AS1299 (Arelion). If I use their looking glass tool to do a traceroute from their HK location, I see theexact same hops, with the difference is that cloud2.mikrotik.com does respond 4 hops after
```

```
2a02:2330:f:41::2!https://lg.twelve99.net/?type=tracerout ... :4000::251
```

```
Router: hnk-b4 / Hong Kong (MEGA-i)
Command: traceroute ipv6 2a02:610:7501:4000::251

traceroute to 2a02:610:7501:4000::251 (2a02:610:7501:4000::251), 30 hops max, 80 byte packets
 1  mei-b6-v6.ip.twelve99.net (2001:2034:0:36::1)   156.203 ms  156.250 ms mei-b5-v6.ip.twelve99.net (2001:2034:0:15a::1)   155.363 ms
 2  ffm-bb1-v6.ip.twelve99.net (2001:2034:1:6b::1)   169.800 ms ffm-bb2-v6.ip.twelve99.net (2001:2034:1:6c::1)   169.741 ms  169.673 ms
 3  sto-bb1-v6.ip.twelve99.net (2001:2034:1:c4::1)   191.640 ms sto-bb2-v6.ip.twelve99.net (2001:2034:1:c5::1)   188.897 ms sto-bb1-v6.ip.twelve99.net (2001:2034:1:c4::1)   191.710 ms
 4  * * *
 5  siatet-ic-355842.ip.twelve99-cust.net (2001:2035:0:21c8::2)  210.563 ms  210.807 ms  210.802 ms
 6  2a02:2330:f:41::2 (2a02:2330:f:41::2)  205.067 ms  203.260 ms  205.321 ms
 7  * * *
 8  * * *
 9  * * *
10  cloud2.mikrotik.com (2a02:610:7501:4000::251)  199.486 ms  201.147 ms  199.449 msSo, it looks like MikroTik (or one of the 3 hops before them) is blocking IPv6 source addresses from my ISPs. I have no problems reaching other IPv6 services around the world. As a result /ip/cloud only produce an A-record for my router, and no AAAA-record.Same problem here.IPv4 address update works, but IPv6 still does not.The IPv6 address is empty.562-232-max.png

---
```

## Response 99
Update: If I do a traceroute using UDP instead of ICMP, I can reach cloud2.mikrotik.com over IPv6 from my place (but ping & traceroute with ICMPv6 don't work). Which means it's not a routing problem but a MikroTik server problem. ---

## Response 100
DDNS IPv6 service is now up and running!We are sorry for the inconvenience caused. ---

## Response 101
Thank you! I can confirm AAAA record is now working. Tested with two routers at two locations. ---