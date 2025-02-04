# Thread Information
Title: Thread-213152
Section: RouterOS
Thread ID: 213152

# Discussion

## Initial Question
Hello, i have setup a Mikrotik Hotspot and it works fine.To Solve the issue that ssl (443) requests are not redirect to the login-page, i have created a let's encrypt dns certificate and add this to the hotspot profile.Now if a device is connected to the system, the login popup appaer.But, if a user click on "use network without login" the device is still connected, if the user is now using any browser to open "google.com", the login page will not appaer.Is there a solution to redirect the traffic for unauthorized devices to the login-page?PS: if i use (ios) chrome instead safari, i get the error by openinghttps://google.com"ERR_SSL_PROTOCOL_ERROR"if i use (android) duckduckgo/chrome browser i get ERR_CONNECTION_CLOSED, on Firefox it works every time (also in private mode)!*if i enter google.de it works too, and the mikrotik is redirect the client to thehttps://hotspot.mytestdomain.com... but google.com ebay.de are still not work.Hope someone can help.The hotspot config is default, i have only add the domain of the certificate to the DNS Name in the Hotspot profile and activate the certificate under Hotspot - Login SSL Certificate.
```
[admin@hotspot]>/ip/hotspot/profile/printFlags:*-default0*name="default"hotspot-address=0.0.0.0dns-name=""html-directory=hotspot 
     html-directory-override=""install-hotspot-queue=nohttp-proxy=0.0.0.0:0smtp-server=0.0.0.0login-by=cookie,http-chap http-cookie-lifetime=3dsplit-user-domain=nouse-radius=no1name="hsprof1"hotspot-address=10.5.50.1dns-name="hotspot.mytestdomain.com"html-directory=Responsive_Hotspothtml-directory-override=""install-hotspot-queue=nohttp-proxy=0.0.0.0:0smtp-server=0.0.0.0login-by=http-chap,https 
     ssl-certificate=fullchain.pem_0 split-user-domain=nouse-radius=no[admin@hotspot]>/ip/hotspot/printFlags:S-HTTPSColumns:NAME,INTERFACE,ADDRESS-POOL,PROFILE,IDLE-TIMEOUT#   NAME      INTERFACE      ADDRESS-POOL  PROFILE  IDLE-TIMEOUT0S hotspot1  ether4-hs-lan  hs-pool-5hsprof15m

---
```

## Response 1
If the user is now using any browser to open "google.com", the login page will not appaer. Is there a solution to redirect the traffic for unauthorized devices to the login-page? ---

## Response 2
try to make a rule in ip firewall nat on the unauth chain with dst Port 443 protocol tcp and as action I would try return you have to place it among the first unauth rules ---

## Response 3
isn't the rule existing with the default hotspot configuration (number 11)?
```
admin@hotspot]>/ip/firewall/nat/printFlags:X-disabled,I-invalid;D-dynamic0D chain=dstnat action=jump jump-target=hotspot hotspot=from-client1D chain=hotspot action=jump jump-target=pre-hotspot2D chain=hotspot action=redirect to-ports=64872protocol=udp dst-port=533D chain=hotspot action=redirect to-ports=64872protocol=tcp dst-port=534D chain=hotspot action=redirect to-ports=64873protocol=tcp hotspot=local-ds>dst-port=805D chain=hotspot action=redirect to-ports=64875protocol=tcp hotspot=local-ds>dst-port=4436D chain=hotspot action=jump jump-target=hs-unauth protocol=tcp hotspot=!auth7D chain=hotspot action=jump jump-target=hs-auth protocol=tcp hotspot=auth8D chain=hs-unauth action=redirect to-ports=64874protocol=tcp dst-port=809D chain=hs-unauth action=redirect to-ports=64874protocol=tcp dst-port=312810D chain=hs-unauth action=redirect to-ports=64874protocol=tcp dst-port=808011D chain=hs-unauth action=redirect to-ports=64875protocol=tcp dst-port=44312D chain=hs-unauth action=jump jump-target=hs-smtp protocol=tcp dst-port=2513D chain=hs-auth action=redirect to-ports=64874protocol=tcp hotspot=http14D chain=hs-auth action=jump jump-target=hs-smtp protocol=tcp dst-port=2515X;;;place hotspot rules here
      chain=unused-hs-chain action=passthrough

---
```