# Thread Information
Title: Thread-1121960
Section: RouterOS
Thread ID: 1121960

# Discussion

## Initial Question
Hello, Any RouterOS version above 7.15.3 (7.16.x and 7.17) sees critical performance issues. Affected are all TCP streams, most noticeable is performance drop while attempting SMB file operations. Wireskark sees multiple duplicated ACKs and retransmissions. Config (working on 7.15.3), GRE addressing not redacted.
```
/interface/gre/export/interfacegreaddallow-fast-path=nolocal-address=172.16.64.21name=gre-mdggdn remote-address=172.16.64.20addallow-fast-path=nolocal-address=172.16.64.23name=gre-mdgwaw remote-address=172.16.64.22/ip/ipsec/export/ip ipsec peeraddaddress=xxxx/32exchange-mode=ike2 name=node-a send-initial-contact=noaddaddress=xxxx/32exchange-mode=ike2 name=node-b/ip ipsec policygroupaddname=common/ip ipsec profileset[finddefault=yes]dh-group=ecp521 dpd-interval=30sdpd-maximum-failures=3enc-algorithm=aes-256hash-algorithm=sha512/ip ipsec proposalset[finddefault=yes]auth-algorithms=sha512 enc-algorithms=aes-256-cbc pfs-group=ecp521/ip ipsec identityaddauth-method=digital-signature certificate=*redacted*generate-policy=port-strict match-by=\
    certificate peer=node-b policy-template-group=common remote-certificate=*redacted*addauth-method=digital-signature certificate=*redacted*match-by=certificate peer=node-a \
    policy-template-group=common remote-certificate=*redacted*/ip ipsec policyadddst-address=172.16.64.20/32level=unique peer=node-a protocol=gre src-address=172.16.64.21/32tunnel=yesadddst-address=172.16.64.22/32level=unique peer=node-b protocol=gre src-address=172.16.64.23/32tunnel=yes/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"ipsec-policy=out,noneout-interface-list=WAN protocol=!gre

---
```

## Response 1
When using any tunnel protocol, consider making MTU changes to take tunnel overhead into account for preventing packet fragmentation. ---

## Response 2
Quick calculations here:1500B - (8B PPPoE) - (20B IPSec header) - (8B Nat-T) - (8B ESP header) - (16B ESP IV) - (24B GRE) - (34B ESP trailer) = 1382 bytes of actual MTUboth sides have this value, I even forced it manually to cross check - that didn't help. Also, lowering it down to 1300 haven't helped either. ---

## Response 3
TL;DR how does the CPU load (/tool/profile cpu=all) look under the traffic load?There have been some changelog notes in last few versions regarding hardware AES acceleration specifically on the Alpine SoC family being broken and fixed and fixed again, etc.RB4011 has an Alpine chip, so this might be somehow related - even though the changelogs were specifically highlighting AES-GCM which is not what you have in your config. ---

## Response 4
Quick calculations here:1500B - (8B PPPoE) - (20B IPSec header) - (8B Nat-T) - (8B ESP header) - (16B ESP IV) - (24B GRE) - (34B ESP trailer) = 1382 bytes of actual MTUboth sides have this value, I even forced it manually to cross check - that didn't help. Also, lowering it down to 1300 haven't helped either.I ended with 1376 as working common number for IPSec GRE/IPIP over different providers across Poland. ---

## Response 5
@BartoszP - I don't think this is really MTU issue. Autonegotiated MTU actually aligns with one I've calculated and lowering it does not help either. I may test it in direct connection with one of the peers to test against NAT-T or other potentially offending voodoo.@wrkq - on 7.15.3 I see a spike during transfer up to 90% of single core utilization, more typical:
```
# 2025-01-26 22:02:06 by RouterOS 7.15.3# software id = RNLB-4V15#Columns:NAME,CPU,USAGE
NAME          CPU  USAGE
console00%firewall00%networking03.5%winbox01%logging00.5%management02%encrypting00%routing00%profiling01%bridging00%unclassified01.5%cpu09.5%console10%firewall10.5%networking12%winbox10%management11.5%encrypting10%routing10%profiling10.5%bridging10%unclassified10%cpu14.5%ethernet20%console20.5%firewall20%networking20%winbox20%management21%routing20%profiling20%bridging20%unclassified20%cpu21.5%ethernet30.5%console30%firewall312%networking340.5%management30%encrypting30%routing38.5%profiling31%bridging31%unclassified32.5%cpu366%With 7.17 I get this:
```

```
# 2025-01-26 22:08:13 by RouterOS 7.17# software id = RNLB-4V15#Columns:NAME,CPU,USAGE
NAME        CPU  USAGE
ppp00%networking00%management00%telnet00%console00%routing00.5%wireless00%cpu00.5%networking10%management10.5%console10%wireless10.5%firewall10%kernel10%led10%cpu11%ppp20%networking20%management21.5%winbox20.5%console21%crypto20%routing20%wireless20.5%profiling20%kernel20.5%bridge221%cpu25%networking30%management32.5%winbox30%console30.5%wireless32%firewall30%bridging30%cpu35%but no transfer is actually seen.

---
```

## Response 6
@mwisniewski, how do iperf3 tests for UDP or TCP with different packet sizes impact throughput and CPU usage? Have you tried different algorithms forIPsec Hardware acceleration? Is there an RB4011 on both ends? ---