# Thread Information
Title: Thread-1122991
Section: RouterOS
Thread ID: 1122991

# Discussion

## Initial Question
Hello, The scenario:I have a Home Assistant server in my local network and additionally i have set up SSL with Lets Encrypt using duckdns to access it from the internet.It works fine and certificate is renewed when needed.When client PC is in local network HA can be accessed using its local IP, but i am unable to access it using the external url.When client PC is not on the local network external URL works correctly.So i am 100% sure that mikrotik router blocks the requests made by local clients to remote url.How can i configure it so that external and internal urls would work on the local network? My router is hAP ax².thank you ---

## Response 1
In MikroTik world this is called Hairpin NAT:https://help.mikrotik.com/docs/spaces/R ... HairpinNATAlternatively you could have the URL (at least the domain part) resolevd to its internal IP address. But that would require running DNS on your local network. ---

## Response 2
I checked my static DNS and i had the hostname of my-subdomain.duckdns.org added which had the Home assistant IP assigned. Sohttp://my-sub.duckdns.org:8123worked from inside and outside of LAN. But https never did.I removed the static DNS and added the hairpin NAT as the documentation described.chain: srcnatsrc address: 192.168.88.0/24dst address: 192.168.88.123protocol: tcpout interface list: LANaction: masqueradeThe result is the same.http://my-sub.duckdns.org:8123works form inside LAN.https://my-sub.duckdns.org:8124does not work from LAN but works from outside LAN.could this be due to previously cached static dns record? ---

## Response 3
/export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc. ) ---

## Response 4
I was about to make the file export today, but decided to check if it works. And yes, it does work now. I can access the external https url from local network.so hairpin rule did help and i needed for static dns to expire.thank you all ---