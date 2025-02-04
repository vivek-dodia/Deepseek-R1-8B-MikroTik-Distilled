# Thread Information
Title: Thread-1117829
Section: RouterOS
Thread ID: 1117829

# Discussion

## Initial Question
Hi, I have an RB4011 running ROS v7.5I've used the newly added Let's Encrypt / ACME support to create a let's encrypt certificate, which we are using for Hotspot and SSTP-VPN - all working, all good.Let's Encrypt certificates expire after 90 days, so for renewal of the certificate, I have created the following script:
```
/ip service enable[find name="www"];/certificate enable-ssl-certificate dns-name=[MyDNSName];/ip service disable[find name="www"];(obviously, the real script in the MikroTik has the actual DNS Name for the SSL Certificate in it, just hidden it here).Reason for the first and third line - I was advised to disable the www service to the firewall itself for security reasons, and as we use the Winbox software via the local network or VPN to administer the firewall, this didn't seem to present any issues... but for Let's Encrypt renewal, this must be enabled... so in my script I enable it, then disable it when everything is finished.Two Problems:When I try to run the renewal command manually via the Terminal, it comes back with "[success] ssl certificate updated", but the expiry date on the certificate itself doesn't change, when I check it in SYSTEM --> CertificatesThe script, when I execute it manually, seems to run and finish much faster (less than 1s) than when I execute the certificate renewal manually in the terminal (approx 10-15s), so I'm wondering if it's really doing anything, or if I need to put some more lines in to make it wait for one thing to finish before doing the next or something like this?Thanks...Colin

---
```

## Response 1
This might help you.viewtopic.php?t=189205#p957288 ---

## Response 2
Good Morning Mikrotik Community, This is an older thread that I started a while ago - since the original post, I found what looked like a really helpful video on the MikroTik YouTube channel (https://www.youtube.com/watch?v=T1Dyg4_caa4) about using Let's Encrypt certificates. Towards the end of the video, it explains what you have to do to allow the inbuilt automatic renewal to happen, without simply exposing port 80 to the internet permanently... or at least, that's what I understood.My RB4011 (ROS7.6) config (the relevant parts) looks like this:I have created the address lists as described in the video:
```
/ip firewall address-listaddaddress=acme-v02.api.letsencrypt.org list=LetsEncrypt/ip firewall address-listaddaddress=acme-staging-v02.api.letsencrypt.org list=LetsEncrypt/ip firewall address-listaddaddress=letsencrypt.org list=LetsEncryptI have enabled the www service:(oddly, I can't find a line in the exported config for this, but Winbox is showing that it's enabled when I look in IP-->ServicesI have created a firewall filter rule to accept traffic on the input chain from the Let's Encrypt list:
```

```
/ip firewall filteraddaction=accept chain=input comment=LetsEncryptdst-port=80protocol=tcp src-address-list=LetsEncryptTo test this, although we do have a fixed public IP, I enabled the IP-->Cloud-->DDNS option to give me a name there and then used the command shown in the video to create a let's encrypt certificate for automatically generated domain name:
```

```
/certificate enable-ssl-certificateWhen I do this however, I always get an error back that the let's encrypt servers cannot contact my router.I can see that the IP Addresses in the list I created are being dynamically updated.I'm guessing I'm missing something obvious here, but I can't see what it is.Any help would be appreciated.

---
```

## Response 3
I'm not sure it's supposed to work, see:https://letsencrypt.org/docs/faq/#what- ... web-server ---

## Response 4
Hi, That was why the video (the MikroTik YouTube video) said to add the domain names to the address list (and have the DNS resolve these dynamically).ThanksColin ---

## Response 5
That's not what I meant. First, out of the three hostnames, only one could possibly make sense, acme-v02.api.letsencrypt.org is the one LE client is connecting to, acme-staging-v02.api.letsencrypt.org is testing (non-prodution) version of that, and letsencrypt.org is just for public website. But as I understand it (anyone correct me if I'm wrong), addresses of servers doing validation are intentionally not public, i.e. you're not supposed to know them beforehand. When I look in logs on server that had its certificate renewed earlier today, there were connections from three different addresses and neither of them was what acme-v02.api.letsencrypt.org resolves to. ---

## Response 6
Oh - I see. Ok.That’s a little disappointing, but I guess just means that I need to go back to using a script to do the renewals if I want them to work automatically.Thanks for the responses. ---

## Response 7
Good Morning Mikrotik Community, I've taken the script from rextended (thanks very much, viewtopic.php?t=189205#p957288) and modified it as I thought I needed:1. Enable the Firewall Filter rule to allow port 80 in input chain2. Delete old certificate3. Request new certificate4. Set new certificate up in SSTP Server config5. Setup new certificate in Hotspot Server Profile6. Disable Firewall Filter rule for Port 80 in input chain.Here's the script:
```
:log info"Script - Certificate renewal start":localcommName"wifi.drumhill.co.uk":localdnsName"wifi.drumhill.co.uk"/ip firewall filter
enable[findwherecomment="LetsEncrypt"]#Delete old certificate, create new certificate/certificateremove[findwherecommon-name=$commName]enable-ssl-certificate dns=$dnsName#Delay to allow the certification request process to complete before the script proceeds:delay90s/certificate:localcertName[get[findwherecommon-name=$commName]name]#Set new certificate in SSTP Profile/interfacesstp-server serversetcertificate=$certName#Set new certificate in Hotspot profile/ip hotspot profileset[findwherename=Hotspot]ssl-certificate=$certName/ip firewall filter
disable[findwherecomment="LetsEncrypt"]Points 1-4 work perfectly. It seems to stop at point #5. I think because I'm not referencing the Hotspot Server profile I want to assign the certificate to properly, so clearly my FIND WHERE is not right.Anyone got any suggestions?ThanksColin

---
```

## Response 8
Fixed it. This part of the script:
```
set[findwherename=Hotspot]ssl-certificate=$certNameNeeded changing to:
```

```
setssl-certificate=$certName[findwherename="Hotspot"]Full Script now looks like:
```

```
:log info"Script - Certificate renewal start":localcommName"xxx":localdnsName"xxx"/ip firewall filter
enable[findwherecomment="LetsEncrypt"]#Delete old certificate, create new certificate/certificateremove[findwherecommon-name=$commName]enable-ssl-certificate dns=$dnsName# better insert here a loop that check when cert is ready, or timeout after x seconds:delay45s/certificate:localcertName[get[findwherecommon-name=$commName]name]#Set new certificate in SSTP Profile/interfacesstp-server serversetcertificate=$certName#Set new certificate in Hotspot profile/ip hotspot profilesetssl-certificate=$certName[findwherename="Hotspot"]/ip firewall filter
disable[findwherecomment="LetsEncrypt"]Thanks very much to Rextended for the script posted (Link is above in this thread).Colin

---
```

## Response 9
Thanks for the mention.Probably forHotspotwork because you add " ", not because you move the order.More tips:
```
/interfaceovpn-server serversetcertificate=$certName/ip servicesetwww-ssl certificate=$certNamesetapi-ssl certificate=$certName/ip hotspot profileset[findwhere!default]ssl-certificate=$certName

---
```

## Response 10
Hi Everyone, This is something that was working really well... but seems not to work anymore. My script (below) renews the let's encrypt certificate that is used for my SSTP VPN.To recap, it's an RB4011 running ROS 7.12.1What I don't understand is that I've run every line of the script (replacing the variable names with the variable values of course) in the Terminal window and it does everything that I would expect it to do and renews the certificate.Could this be permissions somewhere?
```
:log info"Script - Certificate renewal start":localcommName"[##CLOUD-DNS-NAME##]"/ip service enable[findwherename=“www”]/ip firewall filter enable[findwherecomment="LetsEncrypt"]#Delete old certificate, create new certificate/certificateremove[findwherecommon-name=$commName]/certificate enable-ssl-certificate dns=$commName:delay60s/certificate:localcertName[get[findwherecommon-name=$commName]name]#Set new certificate in SSTP Profile/interfacesstp-server serversetcertificate=$certName/ip service disable[findwherename=“www”]/ip firewall filter disable[findwherecomment="LetsEncrypt"]:log info"Script - Certificate renewal finished"The script is implemented in router as follows:
```

```
/system scriptadddont-require-permissions=noname=LetsEncryptRenewalowner=admin policy=ftp,reboot,read,write,policy,t
est,password,sniff,sensitive,romon(I've omitted the source= part of the above bit of the config, as I've given the script above).

---
```

## Response 11
@ColinSlatercould you please post full step by step solution? ---