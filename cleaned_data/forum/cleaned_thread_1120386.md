# Thread Information
Title: Thread-1120386
Section: RouterOS
Thread ID: 1120386

# Discussion

## Initial Question
HI, From my ISP I have:IPv6 Prefix: 2a00:1940:1234:56::/64IPv6 Delegated Prefix: 2a00:1940:123:a00::/56https://ibb.co/ByFxknLI have configured it and then split into /64 prefixes and addressed on VLANs where I obtain them statically on each device I need. Now I'd like to setup a DHCP server with a separate pool for 2a00:1940:123:a03::/64 in VLAN30, but I am getting error because it overlaps with existing /56:https://ibb.co/ZJkNSrtI thought setting it via the ND will resolve my issue but this shit is just deploying it across all VLANs adding them dynamically. Even if I knew how to limit it to just one VLAN it will not work because Chromecasts configured statically to IPv4 address only are getting IPv6 regardless.https://ibb.co/7y0MbyWhttps://ibb.co/3SGD73GIs there any way to do it? ---

## Response 1
Historically the Mikrotik DHCPv6 server has only supported prefix delegation, not handing out individual addresses. The latest testing branch release (7.17) adds address delegation, details in the help pageshttps://help.mikrotik.com/docs/spaces/R ... delegation ---

## Response 2
Historically the Mikrotik DHCPv6 server has only supported prefix delegation, not handing out individual addresses. The latest testing branch release (7.17) adds address delegation, details in the help pageshttps://help.mikrotik.com/docs/spaces/R ... delegationAnd how this is supposed to work? I've updated to 7.17 and I am now able to create a DHCPv6 server:https://ibb.co/yXcty60but no device in vlan30 network is being offered an address from that prefix. There is also no "lease" tab what so ever so I am not quite sure what this server is for. ---

## Response 3
The error says:https://ibb.co/pPYvPMLbut it won't let me creating another /64 pool from pool existing /56:https://ibb.co/ByFxknL ---