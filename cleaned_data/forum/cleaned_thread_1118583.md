# Thread Information
Title: Thread-1118583
Section: RouterOS
Thread ID: 1118583

# Discussion

## Initial Question
Hello all, how this is working? Is DHCP-Option 15?
```
/ip dhcp-server networkset[find]domain="internal"I would like to ping "device hostname".domain without adding as DNS Static.Not sure ifDomain=should be the router (eg.: router.lan) or the local domain (like .internal / .lan / home.arpa)Sorry for dumb post, lacking of knowledge.

---
```

## Response 1
Domain is domain name ... without leading dot. So if your host names are e.g. "host.my.domain.tld", then you should set domain property of DHCP server network entries todomain=my.domain.tld ---

## Response 2
Thanks sir.This is useful also in case of non-public domains likedomain=home.arpa? ---

## Response 3
This setting sets DHCP Option 15 (the domain name that client should use as suffix when resolving hostnames via the Domain Name System) ... and it's entirely up to clients on how they use them. Definitely nothing to do with DHCP server or DHCP client.So normally yes, <my.domain.tld> can be "home.arpa" or "local" (not sure about the later, some OSes have problems with domain names which don't contain at least one dot). ---