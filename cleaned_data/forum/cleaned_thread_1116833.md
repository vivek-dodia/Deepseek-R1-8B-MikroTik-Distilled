# Thread Information
Title: Thread-1116833
Section: RouterOS
Thread ID: 1116833

# Discussion

## Initial Question
Hi colleagues, I'm on RouterOS 7.16.2 and there is issue with DoH certificate verification.Spoiler:/ip/dns/set verify-doh-cert=no|yes|yes-without-crlDetails:The DNS configuration is the following:
```
servers: 1.1.1.1
              dynamic-servers: 
               use-doh-server: https://cloudflare-dns.com/dns-query
              verify-doh-cert: no
   doh-max-server-connections: 5
   doh-max-concurrent-queries: 50
                  doh-timeout: 5sWhen there are no certificates installed, then using "/ip/dns/set verify-doh-cert=no" makes it working. This makes me thinking that "verify-doh-cert=no" completely disables all checks; such behaviour do not fit my case (equipment located in totally untrusted environment), so I want to avoid MITM and need to enable verification.If I install certificates chain (intermediate and root for the cloudflare-dns.com) and enable verify-doh-cert, it still do not work, because it cannot verify certificate against learned from the certificate CRL with the following message in the log
```

```
17:32:08 dns,error DoH server connection error: SSL: ssl: crl not found for: "C=US, S=California, L=San Francisco, O=Cloudflare, Inc., CN=cloudflare-dns.com" (6)The CRLs in the obtained certificate are the following and both are available online, while not present in /certificate/crl/print after importing intermediate/root certs on the previous step:
```

```
X509v3 CRL Distribution Points: 
                Full Name:
                  URI:http://crl3.digicert.com/DigiCertGlobalG2TLSRSASHA2562020CA1-1.crl
                Full Name:
                  URI:http://crl4.digicert.com/DigiCertGlobalG2TLSRSASHA2562020CA1-1.crlWhen I manually add these two URLs using /certificate/crl/add url=... , enabling verify-doh-cert starts to work.And there I see the issue.Manually adding CRL URLs from the end certificates is the way to the failure - remote site can change certificate without any notifications and if there will be another CRL URLs, then DNS resolution will stop work again. So, if I'm not missing something, this needs to be fixed and there are two ways to do this:1. like this done for /tool/fetch check-certificate=(no|yes|yes-without-crl), add 'yes-without-crl' to the verify-doh-cert parameter;2. dynamically learn from the learned CRL with the reasonable timeout, so first request will be delayed but subsequent requests will use cached data.Personally me thinks the first option is easier to be implemented (the code is already available for /tool/fetch) and keeps things safe enough.Will appreciate any comments on this. If I'm missing something - please, correct me. If this is really issue - are there chances to see it fixed?Thank you.

---
```

## Response 1
As you suggested, this approach would be similar to how /tool/fetch handles certificate verification (`check-certificate=(no|yes|yes-without-crl)`). This would avoid CRL checks but still perform basic verification of the certificate chain, geometry dash worldmitigating the MITM risk while bypassing the CRL requirement. Adding the "yes-without-crl" option to /ip/dns/set verify-doh-cert could solve the problem by allowing secure certificate verification while not requiring CRL management. ---

## Response 2
As you suggested, this approach would be similar to how /tool/fetch handles certificate verification (`check-certificate=(no|yes|yes-without-crl)`). This would avoid CRL checks but still perform basic verification of the certificate chain, mitigating the MITM risk while bypassing the CRL requirement. Adding the "yes-without-crl" option to /ip/dns/set verify-doh-cert could solve the problem by allowing secure certificate verification while not requiring CRL management.Exactly, thank you. Any ideas when it can be implemented? Thanks again. ---

## Response 3
Hi, bumping the question -Adding the "yes-without-crl" option to /ip/dns/set verify-doh-cert could solve the problem by allowing secure certificate verification while not requiring CRL management.any estimations on implementing 'yes-without-crl' to the '/ip/dns/set verify-doh-cert' ?Thank you. ---

## Response 4
Are you sure you use the right cert and your time/clock is right?For me no problem on MT_7.16.2I useDigiCert Global Root G2. If using firefox, load the url (https://cloudflare-dns.com/dns-query). Press [Ctrl]+I then Security then Cert and then just get the pem file.(Hadn't seen it was about CRL, I haven't activated that, sorry.) ---

## Response 5
Yes, this is a valid concern. I have opened on issue on it myself (SUP-164116), to date with little to no success.For most people that is not an issue, when functionality for CRL is disabled completely. See the certificate settings:
```
/certificate/settings/set crl-use=no;

---
```

## Response 6
I useDigiCert Global Root G2. If using firefox, load the url (https://cloudflare-dns.com/dns-query). Press [Ctrl]+I then Security then Cert and then just get the pem file.Importing the end certificate works, but this is what I said at the beginning - relying on the site's certificate is dangerous, because it can be changed without prior notifications, in this case DNS resolution will stop work and I consider this as the critical issue. It's much more safe to have loaded well-known root / signing chains.And here is another issue - RAM usage:
```
[doka@node] > /certificate/crl/print
#   CERT                                  LAST-UPDATE           NUM  REVOKED  URL                                                               
[ ... ]
3 D cloudflare-dns-com.pem_0              2024-12-29 14:27:02  1368   405777  http://crl3.digicert.com/DigiCertGlobalG2TLSRSASHA2562020CA1-1.crl
4 D cloudflare-dns-com.pem_0              2024-12-29 14:27:04  1368   405777  http://crl4.digicert.com/DigiCertGlobalG2TLSRSASHA2562020CA1-1.crl
5 D cloudflare-dns-com-chain.pem_0        2024-12-29 14:27:05   686       14  http://crl3.digicert.com/DigiCertGlobalRootG2.crl                 
6 D cloudflare-dns-com-chain.pem_0        2024-12-29 14:27:06   686       14  http://crl4.digicert.com/DigiCertGlobalRootG2.crlwhich is, to be frank, unnecessary to know about half of millions revoked certificatesFor most people that is not an issue, when functionality for CRL is disabled completely. See the certificate settings:
```

```
/certificate/settings/set crl-use=no;This worked for me, thanks for the suggestion. I have few cloud "servers" which check certificates but for them RAM is not an issue and plenty of "clients" which are limited to RAM, but don't need to check certificates.

---
```

## Response 7
which is, to be frank, unnecessary to know about half of millions revoked certificatesThey were revoked for a reason and it's only the right thing to be able to verify if certificate of server our device is talking to is one of those. If you don't care, then that's your problem (or wisdom). ---