# Thread Information
Title: Thread-1117953
Section: RouterOS
Thread ID: 1117953

# Discussion

## Initial Question
Hi everyone, I'm trying to block internet access except for two domains, I managed to block the traffic but I can't unblock it for the two domains. I applied this configuration:IP > Firewall > Filter Rules(rule position 1)Chain: forwardProtocol: tcpDst. Ports: 80, 443Action: drop(adjust position 0)Chain: forwardDst. Address: AuthorizedListAction: acceptIP > Firewall > AddressListList: AuthorizedListAddress: diretta.itThe problem that doesn't unlock the domain is I don't see packet exchange on rule 0.If I delete Dst. Address and enter the entry direct.it in "content". Instead I browse all the sites except direct.itWhere am I wrong?Thank you ---

## Response 1
Can you give this a try:
```
/ip firewall rawaddaction=drop chain=prerouting disabled=yes dst-port=80protocol=tcp tls-host=!*diretta*addaction=drop chain=prerouting disabled=yes dst-port=443protocol=tcp tls-host=!*diretta*

---
```

## Response 2
Your AuthorizedList needs to at least include static.flashscore.com because most of the resources come from there. And probably content.livesportmedia.eu too. And your two rules should be below the
```
action=accept chain=forward connection-state=established,related,untrackedrule, if possible.Can you give this a try:
```

```
/ip firewall rawaddaction=drop chain=prerouting disabled=yes dst-port=80protocol=tcp tls-host=!*diretta*addaction=drop chain=prerouting disabled=yes dst-port=443protocol=tcp tls-host=!*diretta*I don't think this will work. Because the tls-host is only present in the first few packets of the connection, and there is no connection tracking in RAW.

---
```