# Thread Information
Title: Thread-1116244
Section: RouterOS
Thread ID: 1116244

# Discussion

## Initial Question
Hiwe are using mikrotik as dns server for all serversthe problem is some linux systems requests for AAAA entry and mikrotik doesnt have it only has A record in static entry list so it goes to upstream dns serverit creates latency and under heavy load make mikrotik dns server unusablecan we have feature to block all ipv6 resolve requests?the bind has one line config like thisfilter-aaaa-on-v4 yes; ---

## Response 1
If requests are from IPv6 create input chain rule in IPv6 firewall filter to drop packets for port 53. If comes from v4, not sure you can filter it without additional DNS in the middle, for eg. in container, and such feature has sense, dnsmasqalso has such feature. ---