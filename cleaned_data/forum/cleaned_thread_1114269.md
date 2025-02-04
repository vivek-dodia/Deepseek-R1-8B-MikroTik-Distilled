# Thread Information
Title: Thread-1114269
Section: RouterOS
Thread ID: 1114269

# Discussion

## Initial Question
Hello, I'm facing a problem with certificate signing on RouterOS 7.16.I have CLIENT-tpl template certificate with defined days valid attribute (e.g. 365days)I have valid CA certificate, not expired.I created and signed certificate with commands:
```
/certificateaddname=vpnuser01 copy-from="CLIENT-tpl"common-name="vpnuser01"/certificate sign vpnuser01 ca="CA"name="vpnuser01"After signing process was done, certificate was expired with attribute values:Invalid Before: Jan/01/1970 02:00:00Invalid After: Jan/01/1970 02:00:00My clock is synchronized with NTP server and time is correct.Recently, I was generating my certificates exactly same way with no issues.Am I facing a bug?Thanks

---
```

## Response 1
You should describe what you're trying to do. From what I understand, you're trying to sign a client certificate from the Routers CA.From the little I played with the Mikrotik so far, this should be working fine.I followed the docs:https://help.mikrotik.com/docs/spaces/R ... rtificatesand more or less copy&pasted:
```
/certificateaddname=CA-Templatecommon-name=CAtempkey-usage=key-cert-sign,crl-signaddname=Servercommon-name=serveraddname=Clientcommon-name=client
signServername=ServerCA(yes that makesnosense hereinpractice,testing:))signClientca=ServerCAname=testtestprintFlags:K-PRIVATE-KEY;A-AUTHORITY;T-TRUSTEDColumns:NAME,COMMON-NAME,SKID#     NAME         COMMON-NAME  SKID0KAT test         test8edeb8371f2d99b45bc78499776159852bd1c81a1KA  test2        test223220e94100e7740f7f1283965030f58fa14be0b2CA-TemplateCAtemp3KATServerCAserver66505d111a6b5e96bdf928ca3b52884b438812de4KA  testtest     client       ce977beb05b8b2782a970e1a8004462b68ee6bfamy certificate came out to be
```

```
4K  A    name="testtest"digest-algorithm=sha256 key-type=rsa common-name="client"key-size=2048subject-alt-name=""days-valid=365trusted=nokey-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client ca=ServerCAserial-number="1A6A093FBDF8D2F9"fingerprint="d5c8cb725e03a281cef352f9a6c8275979b3f6a8463be2efc5079a24b494979e"akid=66505d111a6b5e96bdf928ca3b52884b438812deskid=ce977beb05b8b2782a970e1a8004462b68ee6bfa invalid-before=2024-11-1614:04:49invalid-after=2025-11-1614:04:49expires-after=52w23h53m29sMay help to run a
```

```
certificateprintdetailcarrotik

---
```

## Response 2
It indeed looks like a bug to me. I am also signing the client certificates using a CA on Mikrotik, but using the "correct" way where the private key is generated on the client itself along with a certificate signing request, the request alone is then transferred to the CA Mikrotik and signed there usingcertificate sign-certificate-request, and the signed certificate gets imported back on the client first and the locally generated key next, and I haven't experienced such a behaviour yesterday when signing a certificate request using 7.16.1. So if you can, try this way. If your client does not allow to generate certificate signing requests (many don't), you can still usecertificate create-certificate-requeston the CA Mikrotik itself instead. So the private key will be generated there, and much like when you directly sign the template, you'll be able to import the key and the signed certificate to the client (or maybe you'll have to import the key locally and then export certificate+key in pkcs12 format if that's the only format the client can import).In any case, it would be nice if you could create a supout.rif file right after the certificate with wrong dates gets generated, and open a support ticket with Mikrotik. Without that, the bug can never be fixed. ---

## Response 3
I can also confirm this bug. I am using version 7.16.1, and I have this behavior.The same procedure applies to another router that runs 7.15.3 and works properly, so the issue is imported in 7.16.1.This is why I am not running the same version in all infrastructure! ---

## Response 4
Same story here, upgraded my Mikrotik to 7.16.2 and a freshly generated certificate is invalid./certificate print detail shows:invalid-before=1970-01-01 02:00:00invalid-after=1970-01-01 02:00:00Currently, I can't create a VPN connection for our new colleague. I would appreciate any help or workaround. Thanks ---

## Response 5
I would appreciate any help or workaround.Have you tried the procedure I have suggested in my previous post? ---

## Response 6
Truth be told, I'm not skilled in certificates. I'm following a setup for an OpenVPN, which creates the certificate (key) directly on the Mikrotik. However, if this doesn't get fixed soon I might need to learn a new way (workaround).EDIT: Reported using Mikrotik service desk (SUP-173239) with a link to this thread. ---

## Response 7
Hello, The issue is fixed in RouterOS 7.17rc versions ---