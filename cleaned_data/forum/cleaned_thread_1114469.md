# Thread Information
Title: Thread-1114469
Section: RouterOS
Thread ID: 1114469

# Discussion

## Initial Question
Hi, I have a strange issue when using IPSEC - once connection is established at least once, and then terminated (regardless of reason), attempt to look at "Installed SAs" just hangs all IPSEC related functions, UI becomes unusable, CLI is responsive but hangs on anything below
```
/ip/ipsecOnce this happens, one CPU core is consuming 100% - the only fix is to reboot the router (at least this helps and works - but only from the CLI).Funny thing is that this happens only if there are no connections active - as long as it is active (= there are established SAs), everything is fine. Even if it was disconnected and then connected again - the problem is triggered only when you try to look at SAs when there are none after successful connection.The problem is reproducible on firmware 7.6, 7.14.3 and 7.16.1, on three different routers (2x RB5009 and one RB750Gr3) - so it is unlikely hardware dependent.My IPSEC config is quite simple - just a few changes from the default:
```

```
/ip ipsec peeraddaddress=192.168.7.10/32name=Office/ip ipsec profileset[finddefault=yes]dh-group=modp2048 dpd-interval=5senc-algorithm=aes-256lifetime=1hproposal-check=claim/ip ipsec proposalset[finddefault=yes]enc-algorithms=aes-256-cbc,aes-256-ctr,aes-256-gcm lifetime=1hpfs-group=modp2048/ip ipsec identityaddpeer=Office/ip ipsec policyset0disabled=yesadddst-address=192.168.10.0/24peer=Officesrc-address=192.168.8.0/24tunnel=yesOther parts of configuration seems to have no effect - I tried to change few things, like not using bridge, disabling HW offloading etc. IPSEC parameters also seems not to change anything.Before I report it, I just want to ask - did somebody experienced something like this?Thank you!

---
```

## Response 1
Hi, I have observed similar behaviour on CCR2116. Trying to display "Installed SA" tab causes IPSec crash. RouterOS drops all phase1 and phase2 connections, new connections either cannot be established or they are dropped after a few seconds. The difference is that on CCR2116 IPSec does not become totally unresponsive, 15 min to 2 hours after closing "Installed SA" view tunnels will be re-established.This problem has been present on CCR2116 since version 7.11.3 (factory firmware of this particular unit). ---