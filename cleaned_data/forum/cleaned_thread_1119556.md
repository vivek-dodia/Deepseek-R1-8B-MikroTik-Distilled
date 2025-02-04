# Thread Information
Title: Thread-1119556
Section: RouterOS
Thread ID: 1119556

# Discussion

## Initial Question
nuff said. ---

## Response 1
Already launched a support ticket ?You do know MT staff doesn't frequent this place that much ?PS the problem is with forum, not website. Just to get the requirements correct ...Edit: SUP-171456 created ---

## Response 2
I guess I'm the only one... ---

## Response 3
I can breathe again -- the forum is back online! ---

## Response 4
still laggy and times out, bandaids maybe, no fix! ---

## Response 5
Its been like this now for a couple of days Off and On .... ---

## Response 6
I think Mikrotik is trying to prove the point about device-mode that DoS attacks are real. ---

## Response 7
Maybe victim of traffic-gen attack ---

## Response 8
Might be time to try out a frontend like Cloudflare or similar to get rid of the DDoS attacks. ---

## Response 9
Might be time to try out a frontend like Cloudflare or similar to get rid of the DDoS attacks.One would think MT would use its own advice --->>>https://help.mikrotik.com/docs/spaces/R ... ProtectionORrealize its crap and remove it from MT Docs. ---

## Response 10
Yeah, that “help” doesn’t do much to stop real DDoS attacks. Pretty sure MT staff mentioned this in the forum too.A must-read for the MT team: ”Distributed denial-of-service (DDoS) protection” ---

## Response 11
I'm sure that it's FreeBSD related. ---

## Response 12
Yeah, me too! ---

## Response 13
To be clear — IDK why the forum was getting 500 errors / hanging — I more was trying to make a joke. Now, I did see the active users being 1500 or so - but that does not mean there was an "attack" per se.But it be nice if Mikrotik posted the post-mortem on the failure, since it might a learning experience for everyone. ---

## Response 14
Yeah, that “help” doesn’t do much to stop real DDoS attacks. Pretty sure MT staff mentioned this in the forum too.A must-read for the MT team: ”Distributed denial-of-service (DDoS) protection”https://www.cloudflare.com/en-ca/networ ... c-transit/Only pennies every nanosecond! ---

## Response 15
And it's still not working well...There are not normally 1000+ real viewers on Saturday.Screenshot 2024-11-16 at 7.07.53 AM.png ---

## Response 16
A spike in session counts is usually a good indicator of a DDoS attack. ---

## Response 17
They are probably several cloudflare versions behind in their own account! ---

## Response 18
A spike in session counts is usually a good indicator of a DDoS attack.Yup.I'd like to think it's still possible to self-host a 25 year old "web app" (phpBB here). i.e. without needing cloud services (AWS, cloudflare, Azure, etc.) or expensive enterprise security products. Perhaps not — that why I'd be curious about at "root cause" here from Mikrotik, perhaps be a good YouTube video. ---

## Response 19
You need a WAF at least to dodge all these massive nonsense requests that just generate load on the webserver. ---

## Response 20
Someone is doing something fishy here. The forum goes tits up, some time passes, it get back up. The number of users online goes steadily increasing, until the forum goes tits up. And... well, You got the picture.The only question is: did Mikrotik pissed off someone, or is it just a bad programmed harvester? ---

## Response 21
Still flaky.The only question is: did Mikrotik pissed off someone, or is it just a bad programmed harvester?LOL. That's my question here... I was kinda curious if newer/bad harvester, and not some attack. I guess it could be some attack targeting phpBB too. ---

## Response 22
Are DoS attacks a holiday tradition in Latvia?Still flaky.Even worse. ---

## Response 23
Barely useable I would say. Server error galore ---

## Response 24
Yup, seems like there’s still some kind of DDoS attack going on. The session count keeps bouncing between a few hundred and 1200-1300. ---

## Response 25
So it was DDoS then, it seems. ---

## Response 26
These “legal” index bots don’t cause spikes in guest session counts, so it’s most likely a DDoS attack going on.EDIT: I still occasionally get “500 Internal Server Error.” ---

## Response 27
This was a new one:IMG_2561.jpeg ---

## Response 28
But I always block all search bot and never had an issue with max session limit hit. And yes even Google misbehaves at times.It’s extremely rare nowadays for big companies using index bots to misbehave. If there’s a problem, it’s usually a misconfiguration on your end. Also, legal index bots don’t use anonymous access.If you allow anonymous access, spikes in guest session counts are almost always a pretty reliable indicator of a DDoS attack.EDIT:The guest session counts are currently at 1651, so I’m guessing the botnet driver has ramped up the pace. This is a battle Mikrotik won’t win unless they take some serious action. ---

## Response 29
Yeah it's still flaky today. I see 1300+ users online. ---

## Response 30
MT should just build a new forum web site and use Apache or nginx.They are already using nginx (it doesn't make any difference anyway). And no, they should not build a new forum. phpBB is perfectly fine. ---

## Response 31
MT should just build a new forum web site and use Apache or nginx.That's precisely what ubiquiti tried, and they ended up with an unusable mess of a forumMikrotik should steer away from fixing what's not broken... ---

## Response 32
Bots still there but forum is back to being zippy. Normis must have come back from holiday! ---

## Response 33
Not really.Just got error page referring to overload. ---

## Response 34
I wonder if related to two submerged sea comm cables getting cut, I read about in the news. ---

## Response 35
Yes 2 cables were cust in the Baltic Sea ….this had a major impact …https://www.bbc.com/news/articles/c9dl4vxw501o ---

## Response 36
I wonder if related to two submerged sea comm cables getting cut, I read about in the news.I doubt it. Got having those "bad gateway" errors, between their nginx HTTP server facing the web and the backend. I'd say it's a good and old ddos - either intentional or a byproduct of bad coded crawler. ---

## Response 37
While cable cuts add some international intrigue and drama here... It does seem more related to application load, not network bandwidth. ---

## Response 38
This is nothing but a disguised attempt to decrease the use of this forum........ and its eventual closure, as the discord channel is so much better ( holds nose ). ---

## Response 39
This is nothing but a disguised attempt to decrease the use of this forum........Or, Mikrotik is just hungover from their holiday. ---

## Response 40
Haha!Either way, it really doesn’t matter how it’s done, the pikes in guest session count clearly points to a classic DDoS attack (IMO)It’ll be interesting to see who holds out the longest in this battle, MT or the DDoS drivers. This kind of volume is pretty cheap to buy on the dark web. ￼ ---

## Response 41
It’ll be interesting to see who holds out the longest in this battle, MT or the DDoS drivers. This kind of volume is pretty cheap to buy on the dark web. ￼I'm betting on Mikrotik. The forum is a commercial asset. Fat chance of seeing them letting it go... ---

## Response 42
Sorry, my bad!I meant before MT gives in and adds a third-party DDoS protection service. ---

## Response 43
I meant before MT gives in and adds a third-party DDoS protection service.Ah. This we agree upon: it's past time they shove it behind some Cloudfare or whatnot. ---

## Response 44
I meant before MT gives in and adds a third-party DDoS protection service.Ah. This we agree upon: it's past time they shove it behind some Cloudfare or whatnot.+1 ---

## Response 45
Ah. This we agree upon: it's past time they shove it behind some Cloudfare or whatnot.+1Not be the contritaian. Why should some cloud solution be needed?I'm pretty sure Mikrotik can fix this without 3rd parties. Maybe not. But Mikrotik's basic product pitch is nothing depends on the cloud.And I've seen a recent trends to promotingself-hosting to avoid cloud costs, so the forum kinda curious test of that theory.i.e.to host a server for a few thousand users on BGP connected AS, without needing cloudflare. ---

## Response 46
Not be the contritaian. Why should some cloud solution be needed?Because this is not their core business. Their routers aren't the best bet to fend off heavy DDOSs - and they shouldn't: it isn't their market target. It's akin to asking Amazon why they are hiring heavy haulers to do the inventory transport. It isn't their core business. ---

## Response 47
Not be the contritaian. Why should some cloud solution be needed?Because this is not their core business. Their routers aren't the best bet to fend off heavy DDOSs - and they shouldn't: it isn't their market target.IDK, maybe it should be. I just don't buy that every publicly visible site needs to use hosted cloud services. If a company that makes high performance routers cannot secure a simple ~LAMP app... that would be telling.Personally, I'd like to see the forum run as containers on Mikrotik hardware (or, maybe Ampere). Microsoft always used to drag out MS's IT department when pitching new services to their customers, with their lessons learned. So if Mikrotik had to run production containers using their own features, maybe /container get more fixes. ---

## Response 48
If you need serious DDoS protection as a front-end service, it takes massive computing resources, expert skills, and experience.Normally, IMO that’s not something a company like MT could manage on-premise by themselves. ---

## Response 49
Maybe it's time to start using Cloudflare?By the way a website hosted in Latvia shouldn't have 320ms+ latency from Poland... ---

## Response 50
I guess I'm saying Mikrotik runs VPN proxy (BTH) and /ip/cloud DDNS already. So some PHP should actually be easier than BTH to secure.....and why I present the question.As a data point, I ran a ping over the weekend, it was ~250ms from the west coast to Mikrotik/Lativia, with 1.5% packet loss – which is similar to what I've seen in past.
```
--- forum.mikrotik.com ping statistics ---
141177 packets transmitted, 139046 packets received, 1.5% packet loss
round-trip min/avg/max/stddev = 53.201/237.958/1503.411/128.193 ms

---
```

## Response 51
Why do you all think that this is/was some sort of attack? ---

## Response 52
IDK, maybe it should be. I just don't buy that every publicly visible site needs to use hosted cloud services. If a company that makes high performance routers cannot secure a simple ~LAMP app... that would be telling.It COULD be. But the need of something able to fend off heavy ddos attacks and what Mikrotik sells today... it's several degrees of separation. I mean, I love Mikrotik hardware - but they have their limits, and it's OK: no one can be a jack of all trades.By Mikrotik to route.By something else to mitigate huge ddos.Buy a third vendor to cattle for your HTTP needs.Why should someone be the "do all and be all"? It's elephants all the way down! ---

## Response 53
Why do you all think that this is/was some sort of attack?Because the number of connected - and anonymous - users just keeps getting up until the forum crashes. Yes, we could be dealing of one (several?) bad written crawlers. But I don't know... more and more it looks to me as some kind of attack. ---

## Response 54
IDK, maybe it should be.It COULD be.I wasn't trying to argue – not wrong from a pure business perspective hosting might make more sense, especially if uptime and low-latency were a concern....But for Mikrotik it would be a sign of capitulation. And implication that any small/medium sized business should not self-host things like a public web site. IDK the right answer, given all threats. That being said... being dependent on a cloud provider has different risks too.Anyway, I'd be curious on the hearing the root cause from Mikrotik... ---

## Response 55
Anyway, I'd be curious on the hearing the root cause from Mikrotik...Won´t be all?I still think it's a matter of focus. No one complains to the Tyre maker when the ring has problems.No one think it's weird when a ring is damaged by bad roads.I think it's the same thing: Mikrotik does routers, not DDOSs mitigation equipment.Try the reverse: how many DDOSs equipment makers are geared through a simple routing algorithm? ---

## Response 56
Anyway, I'd be curious on the hearing the root cause from Mikrotik...Won´t be all?We don't know it wasn't some software update pushed by @normis late on Friday, that had some leak/etc that caused these issues.... ---

## Response 57
They banned my ip, I was only pinging their domain to see if I could see any packet loss.... LOL ---

## Response 58
Since guest session counts are back to normal, I’m guessing MT introduced some kind of measure, but I doubt we’ll ever find out what it was. ---

## Response 59
Since guest session counts are back to normal, I’m guessing MT introduced some kind of measure, but I doubt we’ll ever find out what it was.Looks like my residential IP was blocked - using Tor to post this. They must be dropping address blocks that originated attacks, and I got caught on the crossfire.1) No, my router wasn't compromised.2) Yes, I verified.3) My network and router CPU graphs are as they always were. ---

## Response 60
Looks like my residential IP was blocked - using Tor to post this. They must be dropping address blocks that originated attacks, and I got caught on the crossfire.Fire ticket to support to have it unblocked, or at least get explanation. ---

## Response 61
Well, here we go again! Now at about 1200 sessions and still climbing. Someone must be really pissed at MT... ---

## Response 62
I was thinking about it, but now I can access again. ---

## Response 63
Well, here we go again! Now at about 1200 sessions and still climbing. Someone must be really pissed at MT...This is really weird. Maybe Ukraine bought a huge batch of Mikrotik gear? Maybe Latvia sent some relief, aid or whatever? ---

## Response 64
We have disabled the search robots, except biggest ones, but the attacks are regular DDoS attacks going to different IP every time. We are trying to optimize the forum servers to handle bigger loads, but the attacks keep getting bigger too. Since PHPBB is old software, another option would be to migrate to other forum software that supports load balancing, high availibility etc. But I also know many forum users would not like it. ---

## Response 65
or put a web application firewall in front which handle rate limiting. done. ---

## Response 66
Or use cloudflare in between WWW and server. Now if only cloudflare zerotrust was available as an options package on at least ARM routers and newer.......!!! ---

## Response 67
inside joke there wfburton, but yes anything at this point. ---

## Response 68
We have disabled the search robots, except biggest ones, but the attacks are regular DDoS attacks going to different IP every time. We are trying to optimize the forum servers to handle bigger loads, but the attacks keep getting bigger too. Since PHPBB is old software, another option would be to migrate to other forum software that supports load balancing, high availibility etc. But I also know many forum users would not like it.You don’t need to do anything with PHPBB!Just point "forum.mikrotik.com" to the DDoS Protection Service provider of your choice, and then point the provider to the forum server's IP address. That’s it. If everything’s ready, it’ll only take you 5-10 minutes tops.Ps.. Pro tip: forget about reboots and focus on addressing the root cause instead.Or use cloudflare in between WWW and server.Yup, that is the way!No, just a better firewall.Cloudflare is a DDoS firewall! Cloud-based DDoS protection services are way better than anything you could ever build on-premise. ---

## Response 69
I think he might get the picture if you stick those fangs into him.............. ---

## Response 70
or put a web application firewall in front which handle rate limiting. done.PS: cloudflare is the most widely known WAF. But there are others as well.Even varnish could help to its extent - if you want to avoid 3rd party cloud services. But one is for sure: you cant beat or optimize anything out of phpbb legacy (other than throwing tons of hardware on it) ---

## Response 71
Now would be a good time to check the logs for user agents. May come up empty thou since you can use any valid user agents.I’m only gonna say this once: with a proper DDoS firewall that also catches other bad stuff, you don’t have to bother about invalid user agents since they’ll get blocked anyway!Even varnish could help to its extent - if you want to avoid 3rd party cloud services. But one is for sure: you cant beat or optimize anything out of phpbb legacy (other than throwing tons of hardware on it)Yup, that's how it is!Even if MT throw a bunch of new powerfull hardware at it, I’m pretty sure the DDoS operator will just spin up a few more threads. Like I said, DDoS bots are dirt cheap to rent, especially for small-scale attacks like the ones hitting this forum. ---

## Response 72
We would need to set all *.mikrotik.com DNS to be handled by CloudFlare (or any other 3rd party service). We don't want to do that. ---

## Response 73
No, just "forum.mikrotik.com". But don’t take my word for it, call or email some of them and they’ll explain how it works.Btw, here's a list of popular DDoS protection service providers. Most providers have their services spread out across all continents, and in many cases, you can pick which data center to use.codeProvider Name Website ============= =========== Cloudflarehttps://www.cloudflare.com/ddos/Akamaihttps://www.akamai.com/solutions/securi ... protectionAmazon AWS Shieldhttps://aws.amazon.com/shield/Impervahttps://www.imperva.com/products/ddos-p ... -services/Radwarehttps://www.radware.com/Gcorehttps://gcore.com/ddos-protection/Akamai Prolexichttps://www.akamai.com/products/prolexic-solutionsMicrosoft Azure DDoS Protectionhttps://azure.microsoft.com/en-us/servi ... rotection/Google Cloud Armorhttps://cloud.google.com/armorSucurihttps://sucuri.net/website-firewall/EDIT:Just an example ofCloudflare's pricing model:- Pro - for professional websites that aren’t business-critical, $25/month.- Business - for small businesses operating online, $250/month. ---

## Response 74
Side note: one added benefit from this whole situation ... spammers have little interest the past days for this place.It's remarkably quiet on that front ---

## Response 75
We would need to set forum.mikrotik.com DNS to be handled by CloudFlare (or any other 3rd party service). We don't wantto pay for that..Fixed for accuracy.For the really unspoken.......We would need to set forum.mikrotik.com DNS to be handled by CloudFlare (or any other 3rd party service). We don't want to pay for that. and overly admit that ourRoS, is not up to job.And in that case, remove the misleading section in MT documentation!! ---

## Response 76
Just an example ofCloudflare's pricing model:Pro- for professional websites that aren’t business-critical,$25/month.Business- for small businesses operating online,$250/month.All plans come with unmetered DDoS protection, they just differ in uptime SLA and number of rules for advanced setups. But there are plenty of other service providers that offer the same. ---

## Response 77
Side note: one added benefit from this whole situation ... spammers have little interest the past days for this place.What I noticed during the weekend was most of the "extra guests" (perhaps faking being a bot) were visiting the "User Control Panel" page, under the "Who's Online" section.Perhaps a tighter rate limit on /ucp.php inNGINX configwould help? ---

## Response 78
There's no need to fake anything since there are no restrictions on anonymous access (tho creating a post is). Your suggestion might very well work, but it could end up being like robbing Peter to pay Paul. ---

## Response 79
Anybody know if the ip range problems have been solved, it would be nice not to have to pass an ip that has a block on it while I can ---

## Response 80
You can't just set up one subdomain in cloudflare and keep the rest in another DNS server, the NS servers have to be set to cloudflare, all mikrotik.com DNS will be managed through there. ---

## Response 81
You can, in Enterprise planhttps://developers.cloudflare.com/dns/z ... ain-setup/ ---

## Response 82
There's no need to fake anything since there are no restrictions on anonymous access (tho creating a post is). Your suggestion might very well work, but it could end up being like robbing Peter to pay Paul.Perhaps. But if you're a guest... "user control panel" (aka /ucp.php) is an odd choice to see as the "Now viewing" page in the list of users. And I'm guessing /ucp.php has a higher load on the backend SQL, than viewing forum pages.Mainly pointing out that NGNIX has logging, so presumably there was some pattern to the attack.... ---

## Response 83
You can't just set up one subdomain in cloudflare and keep the rest in another DNS server, the NS servers have to be set to cloudflare, all mikrotik.com DNS will be managed through there.Yes, you can! There are several ways to do this, like DNS subdomain delegation, partial CNAME setups, and more. But as i said don’t take my word for it, please call or email them and they’ll explain how. ---

## Response 84
This is turning into the IT version of Netflix doc "Don't F**k with Cats"...I'm not the expert but setting up DNS is just first step to setup Cloudflare proxy services, I think the purposal here is that HTTPS traffic go through a Cloudflare IP before getting to "real" phpBB.[...] But once again don’t take my word for it, please call or email them and they’ll explain how.I think MT should speak to Cloudflare bizdev folks about some partnership... they'd might trade figuring out DoH for shipping a native Cloudflare package a la ZeroTier. Noting that despite a range of dozens potential solutions (AWS, Azure, Cisco, PaloAlto, etc etc etc) to the DoS problem... the community seems align on Cloudflare as solution. That says something. ---

## Response 85
I think MT should speak to Cloudflare bizdev folks about some partnership... they'd might trade figuring out DoH for shipping a native Cloudflare package a la ZeroTier. Noting that despite a range of dozens potential solutions (AWS, Azure, Cisco, PaloAlto, etc etc etc) to the DoS problem... the community seems align on Cloudflare as solution. That says something.I've used Cloudflare for the last four years for most of my sites (for free, BTW) and it's been great. I don't have any properties that get the volume of traffic that MikroTik gets, but I do have a video streaming app I built that peaks at around 1000-2000 users every six months. On the free tier, there are limits on the amount of bandwidth one can use, but I don't think cost is MT's concern as much as control over DNS is. (As for me, I like not having to run/manage DNS servers anymore. Did that and email for 15-20 years...)When COVID policies limited who could go to church, I put together a broadcasting solution for a couple dozen of our local congregations. Written in node.js, it uses web sockets to handle playback control and telemetry. Without Cloudflare, the app control server struggled with the WSS load at around 100 users. With Cloudflare, the WSS hits are smoothed out and the system can handle 1000+ users simultaneously. ---

## Response 86
Utah and North Pole have spoken. Cloudflare or bust! ---

## Response 87
Utah and North Pole have spoken. Cloudflare or bust!@anav, I thought you'd like that pivotAnd California be happy to take the tax revenue from Cloudflare.And, @wfburton isn't wrong RouterOS is pretty far from a "enterprise firewall". Installing Cloudflare's single exe tunnel in a NPK, with some UI/CLI for some of the common services seems like a simpler path to filling in the gap between RouterOS vs getting into being a security product themselves (which is hard, since new threats evolve daily...). ---

## Response 88
MikroTik and CloudFlare business relationship would be a good idea. Even on a limited level with ClouldFlare Free plain. It would be a start.Would require open minds and forward thinking business planning! Will see if both exist. ---

## Response 89
Shht ! Don't jinx it !! ---

## Response 90
And now all notifications from the past weeks are coming through ---

## Response 91
I'm getting dozens of emails.I can only imagine how many emails the more active participants here are getting. ---

## Response 92
And now all notifications from the past weeks are coming throughAnd here I was thinking there was something wrong with my email... That explains it. ---

## Response 93
Hmm seeing replays and quotes for posts that are no longer exist in this topic. Some profiles writing these posts removed/banned or is forum issue? ---

## Response 94
There must have been an obstruction in the notification drainpipe, now removedhttps://www.bbc.co.uk/news/articles/cvg7x8l5pv2o ---

## Response 95
OH NO........ its back LOL, and now Mynetname is hosed and of course with that BTH.................Its high time mikrotik used the services of cloudflare this is ridonkulous. ---

## Response 96
And seems unstable today, with a lot of HTTP 500 errors & 1200+ active users shown now.... ---

## Response 97
Hi, Yes, there lot of problems with the forum access... ---

## Response 98
It's the "New Year DDOS" - just to mark the year passage!I'm still wondering WHERE this comes from... Commercial rivals? Politically motivated? Someone tried to charge protection from Mikrotik, and it refused to pay (good on them, if was this)? ---

## Response 99
For me it has been down some days. But now back online ---

## Response 100
It’s a lucky dip if it’s online when I come on here. Brings a bit of excitement and variation to my day. ---

## Response 101
At least they had the decency of NOT calling it "Mikrotik 365". ---

## Response 102
It’s a lucky dip if it’s online when I come on here. Brings a bit of excitement and variation to my day.Did you buy a boat yet............ I hear all the excitement one needs is the free water Brits are getting. ---

## Response 103
At least they had the decency of NOT calling it "Mikrotik 365".Luv it!If I was a betting man, I would say its been orchestrated by Cloudflare, for what purpose I do not know, but I swear I did not bribe them to do so, in order to get MT to capitulate and put zerotrust cloudflare as an options package on all MT devices or something like that......... ---

## Response 104
Boats you find on the shores of the UK.You can't get back with that.Atleast the Mikrotik forum floats again. ---

## Response 105
DDoS again? I'm getting a lot of 500 Internal Server Errors.. ---

## Response 106
It has been a problem all over the weekend. ---

## Response 107
The various web-scanners from AI companies are getting even more aggressive than before, to the point articles start to be written about it causing four-five digits of extra fees from hosting companies to to the scanned website owners for all the bandwidth used.The stuff seems to be slapped together in the most lazy/basic ways, without any "I've been here already" tracking. (Not to mention ignoring the robots.txt rules asking them to stay away.)One old forum server I host was also hit hard, the webserver handled the load but I've started to get alerts because the (ancient) statistics software was taking so long to parse the hourly accesslog (which was growing to hundreds of MBs) it overlapped into the next hour, triggering a cronjob error.In the log it was basically obvious the crawler in question was digging through /all/ of the forum posts over and over from the beginning, from many IPs in parallel.So yeah, literal definition of a DDoS but not necessarily as a targetted attack. I wouldn't be surprised if something like this is happening here as well. ---

## Response 108
It's definitely not a crawler, and it seems like the DDoS attacks are getting worse.DDoS 01142025.png ---

## Response 109
I believe MikroTik could benefit from professional support or consulting regarding the operation and hosting of a web application. There have already been some suggestions in this regard. The forum is experiencing HTTP 500 errors almost daily.2025-01-14_11-22.pngThere is a typo: it should be "later" instead of "latter". ---

## Response 110
migrate to other forum software that supports load balancing, high availibility etcIm 100% sure one can do this with PHPBB and HAProxyhttps://www.haproxy.org/EDIT:something like this should work like a charm:
```
frontend WEB
listen :::80 v4v6
listen :::443 v4v6 crt /tmp/crt/ alpn h2,http/1.1
http-request redirect scheme https unless { ssl_fc }

stick-table type ip size 1m expire 10s store http_req_rate(10s)
tcp-request inspect-delay 10s
tcp-request content track-sc0 src
http-request deny if { sc_http_req_rate(0) gt 1 }

default_backend PHPBB

backend PHPBB
mode http
stick-table type string len 50 size 200k expire 30m
stick on phpbb3_cb7h1_sid prefix
default-server check rise 10
server phpbb_1 192.168.0.50:80
server phpbb_2 192.168.0.51:80
server phpbb_3 192.168.0.52:80

---
```

## Response 111
migrate to other forum software that supports load balancing, high availibility etcIm 100% sure one can do this with PHPBB and HAProxyhttps://www.haproxy.org/+1 to haproxyIt has been flaky today too... ---

## Response 112
A load balancer like haproxy as a single measure wont improve the situation significantly. Worst case it would introduce all kind of other issues other than HTTP 500 we currently see - if done badly.I have no experience with phpbb itself, but from a quick google research it seems to have a redis cache driver. To have a shared cache instance is basically first requirement to balance at all.It is unknown to us to which degree this phpbb instance is optimized at all.Most probably some kind of fine grained rate limiting could already do a good job - without the need for fancy pants SaaS solutions like cloudflare.we dont know what, which kind or how many of requests are taking down the forum after all. We are only speculating. So it is hard to tell where the bottleneck is located. ---

## Response 113
A load balancer like haproxy as a single measure wont improve the situation significantly. Worst case it would introduce all kind of other issues other than HTTP 500 we currently see - if done badly.I have no experience with phpbb itself, but from a quick google research it seems to have a redis cache driver. To have a shared cache instance is basically first requirement to balance at all.It is unknown to us to which degree this phpbb instance is optimized at all.Most probably some kind of fine grained rate limiting could already do a good job - without the need for fancy pants SaaS solutions like cloudflare.we dont know what, which kind or how many of requests are taking down the forum after all. We are only speculating. So it is hard to tell where the bottleneck is located.Was more about normis stating that you can't load balance phpbb.As for files there could also be 2 really dirty solutions:1. Just don't care about it for users not logged in (as they can't see attachments anyway) and only load balance those2. Use a shared volumeAnd yes we don't know what the problem load is other than it seems somewhere between 500 - 5000 phpbb sessionsAs most people on here were saying "use cloudflare" and mikrotik seems to be against it, it could be another solution.(I did include a rate limit in my quick haproxy mockup)As others have stated as well. It leaves a bad feeling about mikrotik cloud services. ---

## Response 114
How aboutRate Limiting with Nginx? Works well for a customer's Java web application to restrain the crawler bots. ---

## Response 115
When we do rate limiting, you users will also be limited. All connections come from random IP addresses. When there are thousands of connections coming in at once, either the servers get overloaded, or there is some cloudflare "read only because this is a cached site" page, either way, forum will not be fully operational when this happens. ---

## Response 116
How aboutRate Limiting with Nginx? Works well for a customer's Java web application to restrain the crawler bots.Well crawlers aren't ddos attacks.My customers run haproxy with a connection limit.Which means once that is reached new connections will join a queue. (Until the users browser times out)Webserver doesn't get overloaded but users do get affected.So it can happen that it's not fully usable for everyone.When we do rate limiting, you users will also be limited. All connections come from random IP addresses. When there are thousands of connections coming in at once, either the servers get overloaded, or there is some cloudflare "read only because this is a cached site" page, either way, forum will not be fully operational when this happens.If you rate limit the affected urls (I think someone was talking about ucp.php before) then it should slow down the attack and barely affect real users.But in the end we all know they will just look for a new url.Maybe shadowban the IP/url combo? So the user will just access a static version of the page (cloudflares cached message)There's many more possibilities but since none of us know the real vector of attack we can just assumeEDIT:Btw another idea would be to just slow down connections that hit the rate limit.And the problem should be getting less common ---

## Response 117
I guess they went the "will affect users" wayScreenshot 2025-01-15 175209.png ---

## Response 118
Every connection is from a unique IP, there is nothing to ban ---

## Response 119
Assuming that more than one request comes from each unique IP, implementing rate limits can at least help mitigate the issue. It would require someone with a strong dislike for MikroTik and control over an entire ASN to send, for example, 5000 requests using 5000 unique IPs. ---

## Response 120
It would require someone with a strong dislike for MikroTik and control over an entire ASN to send, for example, 5000 requests using 5000 unique IPs.The first D in DDoS stands for Distributed. And the typical TCP client in that scenario is a zombie in a botnet that has no traceable relationship to the person who orchestrates the attack, so an AS is totally irrelevant here. I can e.g. imagine a bad guy enjoying using/tool fetchon an zombie army of never upgraded Mikrotik routers to DDoS a Mikrotik forum. ---

## Response 121
Assuming that more than one request comes from each unique IP, implementing rate limits can at least help mitigate the issue. It would require someone with a strong dislike for MikroTik and control over an entire ASN to send, for example, 5000 requests using 5000 unique IPs.You can easily grab cheap DDoS attack tools on the darknet and they usually use hijacked consumer PCs with unique IPs from all around the world. ---

## Response 122
Alright, that makes sense. I guess I was too naive. ---

## Response 123
Nginx showing 403 Forbidden for any user:memberlist.php?mode=viewprofile&u=5 ---

## Response 124
The "Who's Online?" from the main forum page has been removed too. I suspect they blocked the "public profiles", to reduce the URLs that could be scraped/DDoS/whatever... ---

## Response 125
No complaints; just want to help. ---

## Response 126
most likely these who is online stats have quite an impact because they often mean database queries. ---