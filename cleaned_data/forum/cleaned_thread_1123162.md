# Thread Information
Title: Thread-1123162
Section: RouterOS
Thread ID: 1123162

# Discussion

## Initial Question
Hi All, I would like to have my server's ipv6 address in the DDNS configuration, as (if I understand ipv6 correctly) there is no NAT/PAT with ipv6 any more. Or is there a best practice to advertise ipv6 services through Mikrotik's public ipv6 address?Any advice is appreciated. ---

## Response 1
You don't need NAT with ipv6 , you normally get a /64 or /52 prefix that is enough for all your connected devices. ---

## Response 2
... you normally get a /64 or /52 prefix that is enough for all your connected devices./64 is most often not enough ... each LAN subnet needs separate /64 prefix while those brain-dead ISP who provide only /64 prefix often require that router uses one address from the same prefix on WAN interface ... which disables you to use any of that prefix on LAN sider of router.So minimum is to get /60 prefix (which means 15-16 /64 subnets), many ISPs hand out /56 (plenty of subnets). Some even hand out as short as /48, but that's IMO too large for typical SOHO usage. ---

## Response 3
I get /64, so router assigns itself sub:net::8, and puts it in ddns. I can access sub:net::9, but only directly, would need to add ::9 to ddns or do some NAT from ::8 to ::9, but not sure if I can do it having only the one /64 subnet from the isp. ---