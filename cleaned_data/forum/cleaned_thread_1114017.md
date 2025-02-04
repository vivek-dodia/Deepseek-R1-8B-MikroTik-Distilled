# Thread Information
Title: Thread-1114017
Section: RouterOS
Thread ID: 1114017

# Discussion

## Initial Question
I'm trying to setup BTH, but it's quite unstable for some reason.It's behind NAT and there are ECMP routes - should it work this way ? ---

## Response 1
/export file=anynameyouwish (minus router serial number, any public WANIP information, keys etc. ) ---

## Response 2
Yeah config going to be needed here.One additional consideration, is if you have IPv6 enabled, BTH will use IPv6 if available. This may or may not be expected, so might want confirm in /ip/firewall/connections and/or /ipv6/firewall/connections to see... RouterOS comes with IPv6 enabled, but sometimes it's left unconfigured...@anav, this be the other "trick" in BTH I have not mention in other thread — it supports both IPv4 and IPv6 peers by default. With "normal" WG, you have to explicitly add IPv6 addresses, while BTH will do that automatically ---

## Response 3
yeah the first thing I do in every config is blow up capsman and obliterate IPV6. They are like parasites that drain my energy ---

## Response 4
yeah the first thing I do in every config is blow up capsman and obliterate IPV6. They are like parasites that drain my energyLOL, I know your thoughts there & BTH does use IPv6 - why I highlight that detail. Although I suspect OP running into the WG+multipath "issue"... ---

## Response 5
ipv6 is disabledI have two WAN connections from different ISPAnd if I add two default routes through them ( ECMP per se ) - BTH/wg doesn't work or very unstableBut if I leave only one route - all works fineSo I wonder if it's "expected" problem ? ---

## Response 6
For last time......viewtopic.php?t=213165#p1113997@AMMO see this thread for your thoughts..viewtopic.php?t=213177#p1113986 ---