# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 197700

# Discussion

## Initial Question
Author: [SOLVED]Fri Jul 28, 2023 9:15 am
``` # argLoopbackInt: name of the loopback interface# argWanPool: name of the WAN pool# argUlaPool: name of the ULA pool# argManagedID: regex-escaped unique ID of the managed objects:globalargLoopbackInt:globalargWanPool:globalargUlaPool:globalargManagedID/ipv6/pool:localvarWanPrefix[getvalue-name=prefix $argWanPool]:localvarUlaPrefix[getvalue-name=prefix $argUlaPool]:globalWaitAddressdo={/ipv6/address:localvarAddress:retrycommand={:setvarAddress[getvalue-name=address[findinterface=$1(addressin$2)comment~"$3\$"]]}delay=1max=5:return$varAddress}:do{/ipv6/address:localvarOldGuaPrefix[getvalue-name=address[find comment~"$argManagedID\$"]]:localvarNewGuaPrefix[$WaitAddress $argLoopbackInt $varWanPrefix $argManagedID]:if($varOldGuaPrefix!=$varNewGuaPrefix)do={:log info"Set $varNewGuaPrefix <-> $varUlaPrefix"/ipv6/firewall/manglesetdst-prefix=$varNewGuaPrefix[find action=snpt comment~"$argManagedID\$"]setdst-address=$varNewGuaPrefix src-prefix=$varNewGuaPrefix[find action=dnpt comment~"$argManagedID\$"]}}on-error={/ipv6/addressremove[find comment~"$argManagedID\$"]addinterface=$argLoopbackInt advertise=nofrom-pool=$argWanPool comment="Managed: NPTv6 / $argManagedID":localvarGuaPrefix:do{:setvarGuaPrefix[$WaitAddress $argLoopbackInt $varWanPrefix $argManagedID]}on-error={remove[find comment~"$argManagedID\$"]:log error"Unable to allocate prefix from $varWanPrefix on $argLoopbackInt":error""}:log info"Add $varGuaPrefix <-> $varUlaPrefix"/ipv6/firewall/mangleremove[find comment~"$argManagedID\$"]addchain=postrouting action=snpt src-address=$varUlaPrefix src-prefix=$varUlaPrefix dst-prefix=$varGuaPrefix comment="Managed: NPTv6 / $argManagedID"addchain=prerouting action=dnpt dst-address=$varGuaPrefix src-prefix=$varGuaPrefix dst-prefix=$varUlaPrefix comment="Managed: NPTv6 / $argManagedID"} ``` ``` :if($"pd-valid"=1)do={:globalargLoopbackInt"loopback":globalargWanPool<PooladdedbyDHCPv6Client>:globalargUlaPool<PoolreservedforULA addresses>:globalargManagedID"some-random-string"/system/script/run nptv6} ``` Ended up using the loopback interface to force RouterOS to reserve a subnet from the delegated prefix. DHCPv6 Client's script is used to update the firewall rules as necessary. It's a somewhat smart because it makes sure that allocated subnet has the same prefix as the newly delegated one. Should help if script gets called before changes are propagated throughout RouterOS./system/script/add name=nptv6
```
/ipv6/dhpc-client/edit value-name=script
```

```
Where loopback is just "/interface/bridge/add name=loopback"


---
```

## Response 1
Author: Thu Dec 26, 2024 3:03 pm
... DHCPv6 Client's script is used to update the firewall rules as necessary. ... it makes sure that allocated subnet has the same prefix as the newly delegated one. Should help if script gets called before changes are propagated throughout RouterOS./system/script/add name=nptv6[...]/ipv6/dhpc-client/edit value-name=script...Thank you for answering my ask (probably without reading it) atpost #89 atChanging ipv6 prefixtopic! You created quite useful scripts for home/SOHO environment.