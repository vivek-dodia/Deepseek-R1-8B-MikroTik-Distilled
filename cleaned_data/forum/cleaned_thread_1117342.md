# Thread Information
Title: Thread-1117342
Section: RouterOS
Thread ID: 1117342

# Discussion

## Initial Question
I have a CCR 1016 that was on version 6.44.1 and I upgraded it to 6.44.3. After the upgrade IPSec is completely broken. I cannot add policies, peers, profiles, or anything IPSec related. all previous configurations are not working. The only thing in the logs is an l2tp error "could not add IPsec policy: std failure: timeout(13)". If I try to add anything to IPSec in the GUI or via CLI it fails.I tried to downgrade back to the original 6.44.1 but that still has the same errors. I am stuck as I cannot get anything to work at the moment. ---

## Response 1
I have a CCR 1016 that was on version 6.44.1 and I upgraded it to 6.44.3. After the upgrade IPSec is completely broken. I cannot add policies, peers, profiles, or anything IPSec related. all previous configurations are not working. The only thing in the logs is an l2tp error "could not add IPsec policy: std failure: timeout(13)". If I try to add anything to IPSec in the GUI or via CLI it fails.I tried to downgrade back to the original 6.44.1 but that still has the same errors. I am stuck as I cannot get anything to work at the moment.I had the same on a CHR installation. Had to go back to 6.43.14 and a backup made with a 6.43 version in the past. ---

## Response 2
IPSec works just fine here with 6.44.3 on several routers/models. Did not see that error on any of them.The only only thing that might make a difference is that I went from 6.44.2 to 6.44.3 and not from 6.44.1 to 6.44.3.The only change I see in 6.44.3 since 6.44.1 is:
```
*)ipsec-fixedfreshly created identitynottakeninaction(introducedinv6.44);*)ipsec-fixedpossible configuration corruption afterimport(introducedinv6.44);

---
```

## Response 3
I have 10 or so CCRs and I have upgraded most of them from 6.44.1 to 6.44.3 without any issues. This is the first time I have ever had an issue with upgrading a router in the 5 or so years I have been using Mikrotik. ---

## Response 4
I have 10 or so CCRs and I have upgraded most of them from 6.44.1 to 6.44.3 without any issues. This is the first time I have ever had an issue with upgrading a router in the 5 or so years I have been using Mikrotik.Did you use version 6.44 on the router too? The first time I lost the configuration was after a reboot with this version. I had to restore a backup. After that I had the problem again when upgrading from 6.44.2 to 6.44.3. ---

## Response 5
Hello everyone, we have many mikrotik devices in our company and few month ago we update to 6.42.x our gateway and no problem with IPCSEC, two tunnels works just fine. Today after some electricity problem was router rebooted and all IPSEC config are gone and I cant add new or import from backup any item with the same log as Marino "could not add IPsec policy: std failure: timeout(13)". I tried update to latest 6.45.3 with no success.Is this problem still with no solutions after this long period? Only way is to make downgrade to 6.43.14? So sad, I love Mikrotik in all way! Thanks in advance. ---

## Response 6
Hi, I am getting this error
```
l2tp,error:couldnotaddIPsecpolicy:std failure:timeout(13)on CCR-2116-12G-4S+. Enabled ipsec for L2TP vpn, tested connection (worked), then changed few settings (algorithms), and thendynamic IPSec Policyl2tp-in-servergot stuck. - can't be removed (even if I disable ipsec in l2tp)Running 7.16.1 :-/

---
```