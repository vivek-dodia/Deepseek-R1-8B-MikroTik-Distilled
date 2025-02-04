# Thread Information
Title: Thread-213906
Section: RouterOS
Thread ID: 213906

# Discussion

## Initial Question
Hi, My RouterOS box is between some Ethernet and wireguard tunnels. For the longest time everything was perfectly fine (clients with MTU=1500 and wiewguard on the RouterOS router MTU=1420). Just recently one single SSL server seemed to hang. Turns out I can fix this by decreasing MTU on my clients on Ethernet. But that's not a great solution ... I do not want to manually mess around with MTU, just because one link may have a lower MTU.Now I have read that RouterOS can change TCP MSS (which is deducted from MTU by the clients) automatically:
```
/ip firewall mangleaddaction=change-mss chain=forwardnew-mss=clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=synIs there any downside doing this?Is there any downside doing this globally, for all TCP SYN packets that are forwarded? In other words, is there any downside not adding a qualifier, like out-interface=tunnel-interface ?

---
```

## Response 1
"Most" clients will be automatically set the TCP MSS correctly (assuming ICMP/"ping" is not blocked in the path), but it's not 100%. And why "it worked for a while, then some device broke it..." So using an adjust-mss action makes sense for WG - keep in mind it only applies to TCP traffic which has a MSS, UDP things are unaffected by any MSS changes.Now, I don't think you'd want to set it "globally" (i.e. without a interface restriction)... Depending on the interface/situation, it is theoretically possible the far end may have alowerMTU that's causes aeven lowerMSS to be negotiated & so there is a possibility then of "over correcting" it byincreasingthe MSS with the rule. So I'd make sure it just applies to your wireguard path.Also WG's MTU is a constant, so you alternatively use just use the plain "adjust-mss" with a fixed MSS value of 1380, and apply it to TCP SYN packets with MSS value 1381-64000 - so that it applies only to traffic needing adjustment. ---

## Response 2
Hope this could be useful:viewtopic.php?p=1095429#p1095429As always, thanks to the precise and detailed contribution from @Amm0 ---

## Response 3
My recommendation is that the WG connections at both ends have the same MTU.Then the client peer device (if a router) aka NOT the server peer for handshake, should set the rule you stated.There are two variations to try.. .....add action=change-mss chain=forward comment="Clamp MSS to PMTU for Outgoing packets" new-mss=clamp-to-pmtu out-interface=wireguard1 passthrough=yes protocol=tcp tcp-flags=synANDadd action=change-mss chain=forward new-mss=1380 out-interface=wireguard1 protocol=tcp tcp-flags=syn tcp-mss=1381-65535+++++++++++++++++++++++++++++++++++++++++++If its pppoe connections at both ends there is another process to consider. ---