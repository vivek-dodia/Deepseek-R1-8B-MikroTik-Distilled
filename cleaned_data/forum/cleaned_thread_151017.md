# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 151017

# Discussion

## Initial Question
Author: Sat Aug 10, 2019 4:20 pm
``` /ip sshsetstrong-crypto=yes ``` ``` user@server:~/.ssh$ ssh-keygen-t rsa-f server ``` ``` user@server:~/.ssh$ cat server.pub>>authorized_keys ``` ``` user@server:~/.ssh$ scp server* admin@router:/flash/ ``` ``` user@server:~/.ssh$ ssh admin@router[admin@router]>/user ssh-keys private import user="admin" public-key-file=flash/server.pubprivate-key-file=flash/server passphrase=""unable to load key file(incorrect passphrase?)! ``` ``` /flash/ ``` ``` flash/ ``` ``` input doesnotmatch anyvalueofprivate-key-file ``` ``` -----BEGINOPENSSH PRIVATE KEY-----key....-----ENDOPENSSH PRIVATE KEY----- ``` ``` ssh-rsa AAA......hd6 user@server ``` ``` user@server:~/.ssh$ ssh-i server admin@router ``` Hi, I want to connect to a linux (debian) server to run a command there. The connection has to be initiated in a script on the Mikrotik (RouterOS v6.45.1) router. Thus, I need ssh-exec and have to use keys to ssh into the server. As far as I understood, I need to generate private and public keys on my destination host and import them (or only the private one?) to the client (Mikrotik) where I want to initiate the connection from. However, I can't import the keys in the first place. I have enabled strong-crypto using
```
And for the keys:
```

```
For the passphrase I just hit enter. Then, I appended the key to the locally authorized:
```

```
and copied the files to the router:
```

```
Then, I sshed into the router and tried to import the keys:
```

```
Using
```

```
instead of
```

```
results in
```

```
.The server-file has the format
```

```
and the server.pub looks like
```

```
.What am I doing wrong? I also tried to leave out the passphrase and just hit enter when asked on import. Also generating keys with a passphrase and entering it does not work. I also tried to generate the keys with puttygen, this gives me a (wrong format) error. I also modified the keys according toviewtopic.php?t=48693. But with the same results.Can someone tell me the steps to properly import the keys? Am I on the right path, anyway? Because according tohttp://www.linuxproblem.org/art_9.html, it seems like I'm interchanging the roles of router (A) and server (B). However, followinghttps://wiki.mikrotik.com/wiki/Use_SSH_ ... o_RouterOSis my approach above, isn't? basically, it's like inviewtopic.php?t=128887#p633303but from RouterOS to host, not RouterOS to RouterOS.Thanks a lotJohannesPS: When I add the server.pub in System -> Users-> SSH keys, I can login from the server to the router without a password by
```

```
. But I need it the other way round.


---
```

## Response 1
Author: [SOLVED]Mon Aug 12, 2019 12:55 am
``` ssh-keygen-t rsa-m PEM.. ``` Try to generate your key in PEM format:
```
---
```

## Response 2
Author: Tue Aug 13, 2019 9:58 pm
We do it like this::global SUPPORTPUB "ssh-rsa RSAkeygoesheresupport@mycompany.net";:global SECCFG do={:global SUPPORTPUB;/file {print file=supportpub.txt; :delay 2; set supportpub.txt contents=$SUPPORTPUB};/user {remove [find name=YOURNAME];add name=YOURNAME password='YOURPASSWORD" group=full;ssh-keys import public-key-file=supportpub.txt user=YOURNAME};/file remove [find name=supportpub.txt];/ip {ssh set strong-crypto=yes;service {set ssh port=YOURPORT;set [find name!="ssh"] disabled=yes}}};$SECCFG;/system script environment remove [find name~""] ---

## Response 3
Author: Fri Aug 16, 2019 3:10 pm
``` ssh-keygen-t rsa-b2048-f mikrotik_rsa-v-C"Mikrotik Key"Generatingpublic/privatersa key pair.mikrotik_rsa already exists.Overwrite(y/n)?yEnterpassphrase(emptyfornopassphrase):Entersame passphrase again:Youridentification has been savedinmikrotik_rsa.Yourpublickey has been savedinmikrotik_rsa.pub.Thekey fingerprintis:SHA256:4WXp/Zljv2unvg9AvZRGywNkKgB4Pq0X1dkkrMlbZEoMikrotikKeyThekey's randomart image is: +---[RSA 2048]----+ | .... o.== . | | . . .E *=.= o | | o . +o*= . O | | o o.=*.o o o | | o .So. o . | | . . . o o | | . B | | . =.| | .=**| +----[SHA256]-----+ ``` ``` importuser=aremoteuser passphrase=""public-key-file=mikrotik _rsa.pubprivate-key-file=mikrotik_rsa ``` I'm having exactly the same problem importing private keys for SSH
```
Move the public & private key to the router....
```

```
unable to load key file (incorrect passphrase?) !Trying without the passphrase="" or without the quotes (i.e. passphrase=) gives the same responseAlso the same if I add a passphrase to the cert.Basically, there is no way to upload private keysUsing routerOS 6.34.3Please help!


---
```

## Response 4
Author: Fri Aug 16, 2019 4:32 pm
``` [sob@CHR2]>/user ssh-keysprivateimportuser=sobprivate-key-file=mikrotik_rsapublic-key-file=mikrotik_rsa.pub passphrase:[sob@CHR2]>/user ssh-keysprivateprintFlags:R-RSA, D-DSA# USER BITS KEY-OWNER0R sob2048MikrotikKey ``` Maybe try something a little less outdated? This is with 6.45.3:
```
---
```

## Response 5
Author: Fri Aug 16, 2019 11:25 pm
``` user@server:~/.ssh$ ssh-keygen-t rsa-m PEM-f server ``` Thanks a lot eworm, generating the keys by
```
did the trick!


---
```

## Response 6
Author: Mon Aug 19, 2019 7:03 pm
``` /user ssh-keysprintFlags:R-RSA, D-DSA# USER BITS KEY-OWNER0R routercomms4096MikrotikKey-4096RSA/user ssh-keysprivateprintFlags:R-RSA, D-DSA# USER BITS KEY-OWNER0R routercomms4096MikrotikKey-4096RSA/ip sshprintforwarding-enabled:noalways-allow-password-login:nostrong-crypto:noallow-none-crypto:nohost-key-size:4096/system ssh172.18.0.1user=routercomms can't agree on KEX algorithms Welcome back! ``` ``` /user ssh-keysprintFlags:R-RSA, D-DSA# USER BITS KEY-OWNER0R routercomms4096MikrotikKey-4096RS/user ssh-keysprivateprintFlags:R-RSA, D-DSA# USER BITS KEY-OWNER0R routercomms4096MikrotikKey-4096RSA/ip sshprintforwarding-enabled:noalways-allow-password-login:nostrong-crypto:noallow-none-crypto:nohost-key-size:4096/system ssh172.17.0.1user=routercomms password: ``` Thanks jojoHa / eworm, that got the keys uploaded OKI'm still having an issue though, and cannot get router to router communication...Router A:ROS v6.45.2
```
Router B:ROS v6.45.3
```

```
I have tried using the the same and different pub/priv pair on both routers, I have tried 2048 & 4096 key lengths, I can SSH in with no issue using these keys from a unix SSH command, I have tried dropping back to DSA rather than RSA.It would appear that when trying to connect the router isn't using the private key to communicate (one way), then has the KEX issue the other way.Any thoughts?


---
```

## Response 7
Author: Tue Aug 20, 2019 2:49 pm
``` [routercomms@router]/system script>printfrom=routercommstestFlags:I-invalid0name="routercommstest"owner="auser"policy=ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon dont-require-permissions=nolast-started=aug/20/201913:38:45run-count=62source=:localStatus([/system ssh-execuser=routercomms address=172.18.0.1command=":put ([/interface ethernet monitor [find where name=ether2] once as-value]->\"status\")"as-value]->"output"):log info $Status ``` ``` [auser@router]>/system script run routercommstest failure:authentication failure ``` ``` [routercomms@router]>/system script run routercommstest(Worksasexpected) ``` Hmmm, So I think I've found the issue.... basically, the script ignores the user param when executing...For the script.....
```
Get's these results.....
```

```
vs
```

```
So to make scripts work on target machines, I need to be logged in as the 'routercomms' user to execute the script successfully, or set it up as a scheduled script, on the source router.This is a PITA, especially when you want to protect the 'routercomms' account with a difficult password, and not share the private key.


---
```

## Response 8
Author: Wed Oct 06, 2021 4:58 pm
``` ssh-keygen-t rsa-m PEM.. ``` Try to generate your key in PEM format:
```
Thanks, it did work for me too!Only question is why is that in the Mikrotik official wikihttps://wiki.mikrotik.com/wiki/Use_SSH_ ... key_login)does it say only "ssh-keygen -t rsa" and does not talk about "-m PEM". Maybe Mikrotik can add that information to the wiki?Thanks!
```