# Thread Information
Title: Thread-1119402
Section: RouterOS
Thread ID: 1119402

# Discussion

## Initial Question
Hi all, driving some large WiFi communities by Captive Portals on Mikrotik CCR show me a quite big amountof CPU power dedicated to the DNS process. Updating from v.6.41.x to v.6.42.3 increases this issue asone cpu core is stuck at 100% usage - and the user does not get an answer to each of his DNS requests(It seems that the DNS server on Mikrotik is still single threaded).Digging into the problem rises the question, why an authenticated user on the Hotspot Portal is stillredirected to the DNS server on the Mikrotik router (via port 64872/udp and 64872/tcp). Ok, I haveto ensure, that the DNS name for the captive portal is available by the recursing DNS server suppliedvia DHCP - but this might be the case in several settings.So is the following rule
```
/ip firewall nataddaction=jump chain=dstnat hotspot=from-client,auth jump-target=hs-autha solution to bypass all redirects for an authenticated user and use a powerful, external DNS resolver?Or is there a better solution for this? And what can be done, to optimize environments with 3000-4000concurrent users on a Mikrotik Hotspot Portal.CheersDieter

---
```

## Response 1
7 years later, nobody responded...I would like to revive this question.I too, am looking for such a solution. ---