# Thread Information
Title: Thread-1117860
Section: RouterOS
Thread ID: 1117860

# Discussion

## Initial Question
Found another thing that broke after upgrading to v.7.16I had a perfectly working IPv6 config before upgrading to 7.16 from the latest 7.15 version.After this the thing missing is the dhcp-client config info from /ipv6/dhcp-client/It is there but I'm unable to see it, I know that as a fact because I get the IPv6 prefix from my ISP, my clients get their IPv6 address etc.Something is not working properly here.I tried doing a netinstall and "keep config" option, wich did not fix the problem.The absolute last resort is resetting the router and setting it up all over again, vlans, fw rules, nat rules, interfaces, address-lists etc. and there is ALOT !When I do a "/ipv6/dhcp-client/print" in terminal, it just hangs, and does not output anything, on my secondary router (also a RB5009) it works perfectly.Another update:I also noticed that the IPv4 DHCP-Client does not renew its lease, it seems to just die randomly, the IP is released/dropped and no-internet is a fact, when opening /ip/dhcp-client in winbox it suddenly appears and pushing release makes the router release and renew after a few seconds.Nothing in the router logs whatsoever. ---

## Response 1
I'm not seeing the problem with hanging, and the lease looks to be correct.[igb@brsklink.batten.eu.org] /system/routerboard> /system/package/printColumns: NAME, VERSION, BUILD-TIME, SIZE# NAME VERSION BUILD-TIME SIZE0 routeros 7.16 2024-09-20 13:00:27 11.1MiB1 wireless 7.16 2024-09-20 13:00:27 1920.1KiB[igb@brsklink.batten.eu.org] /system/routerboard> /ipv6/dhcp-client/printColumns: INTERFACE, STATUS, REQUEST, PREFIX# INTERFACE STATUS REQUEST PREFIX;;; Gets a /64 from SLAAC, and a /48 from DHCPv6-PD. ALWAYS turn off Rapid Commit, which BRSK don't support.0 BRSK2001 bound prefix 2a10:XXXX:XXXX::/48, 23h53m37s[igb@brsklink.batten.eu.org] /system/routerboard> ---

## Response 2
I have same problem with 7.16 on CCR2004. /ipv6/dhcp-client/print stucked and I cant see any ipv6 client item in winbox ---

## Response 3
Same error.At some point, the configuration stopped exporting with the error #error exporting "/ipv6/dhcp-client" (timeout ... I reset the configuration and re-entered it from the old export. I might be wrong, but in version 7.16 there are a lot of changes, and it is advisable to export the config, update, and import it back. ---

## Response 4
memory:script error: action timed out - try again, if error continues contact MikroTik support and send a supout file (13)executing script from dhcpclient failed, please check it manually ---

## Response 5
Netinstall not fixed mi problem. Looks like memory leak ... ---

## Response 6
Same error here.I can´t see the dhcp client, but when I try to add a new dhcp client for that interface, it says I alread have a dhcp client for the interface.So, is there any way to remove the old dhcp client (even if I don´t see it).The command: /ipv6/dhcp-client/print hangs forever. The export command shows timeout.The remove 0 or remove 1 hangs forever.Same for disable 0 or disable 1All commands inside /ipv6/dhcp-client/ hangs.Any other solution to remove this? ---

## Response 7
I have the exact same problem on my RB4011iGS+ running 7.16.2. UI shows no DHCPv6 clients and terminal print command just hangs. DHCP client is working it seems, although I am having weird v6 issues right so not being able to see the v6 client status is very annoying!(Edit: Seems to be fixed in 7.17rc3 - my guess is it is fixed by this changelog entry " dhcpv6-client - improved system stability when DHCPv6 client is enabled on non-existing interface;", as I do have a DHCPv6 client attached to a disabled interface too. So hopefully this should be fixed in 7.17.0 stable.) ---