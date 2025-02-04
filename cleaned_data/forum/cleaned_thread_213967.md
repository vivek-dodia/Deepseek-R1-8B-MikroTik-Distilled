# Thread Information
Title: Thread-213967
Section: RouterOS
Thread ID: 213967

# Discussion

## Initial Question
To get a working IKEv2/IPSec RSA connection, I have to manually add every single remote certificate and ID in /ip ipsec identity.Is it possible to automate this for every valid certificate in /certificate? ---

## Response 1
It should be possible with the appropriate script but I'm no expert in scripting ---

## Response 2
Actually, you don't have to add a dedicated/ip ipsec identityrow per client device unless you want each of them to get an individual treatment.I haven't tested that practically because I don't have a use case for that, but while acting as a responder, the IPsec stack of RouterOS should accept any certificate the initiator presents if it is signed by a root CA the RouterOS trusts. So if you setremote-idtoignoreandmatch-bytoremote-id, a single/ip ipsec identityrowshouldbe sufficient for all the clients. The drawback is that with this setting, you would need to maintain a CRL to be able to deny access to individual client devices (lost or stolen).Other than that, there is no tickbox that would make RouterOS dynamically create the identities from the list of certificates in a similar way like routes to connected subnets are created dynamically. But you can use a (relatively) simple script to create a list of certificates matching a certain set of conditions, and for each item on that list, check whether a matching row already exists in/ip ipsec identityand if it doesn't, create it:
```
:foreachcrtin=[/certificate findwhereissued ca=my-root-ca]do={:if([:len[/ip ipsec identity findwhereremote-certificate=$crt]]=0)do={/ip ipsec identityaddremote-certificate=$crt peer=xyz...}}(not tested!)

---
```