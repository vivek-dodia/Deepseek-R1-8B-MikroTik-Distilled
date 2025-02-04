# Thread Information
Title: Thread-1115787
Section: RouterOS
Thread ID: 1115787

# Discussion

## Initial Question
add action=dst-nat chain=dstnat dst-port=3306 in-interface=Wan-ether1 protocol=tcp to-addresses=192.168.88.244 to-ports=80add action=dst-nat chain=dstnat dst-address-list=a.com dst-port=80 in-interface=bridge protocol=tcp to-addresses=192.168.88.244 to-ports=80add action=masquerade chain=srcnat dst-port=80 out-interface=bridge protocol=tcp src-address=192.168.88.0/24I added the following rule on the NAT page and found that the IP recorded in nginx's logs is the IP of router 192.168.88.1Is there any way to record the real IP addresses of the internal and external networks while ensuring performance ---

## Response 1
It's the last rule (masquerade) which messes src-address. In principle it's not needed unless you require "hairpin NAT" ... in which case thrte's no way around it.Unless you create separate IP subnet fot the server. ---

## Response 2
It's the last rule (masquerade) which messes src-address. In principle it's not needed unless you require "hairpin NAT" ... in which case thrte's no way around it.Unless you create separate IP subnet fot the server.Do I only need to execute these two commandsthen maintain null value for in-interfaceadd action=dst-nat chain=dstnat dst-port=80in-interface=Wan-ether1 protocol=tcp to-addresses=192.168.88.244 to-ports=80add action=dst-nat chain=dstnat dst-address-list=a.com dst-port=80 in-interface=bridge protocol=tcp to-addresses=192.168.88.244 to-ports=80 ---

## Response 3
The second rule hints at use of hairpin NAT because in-interface=bridge to-addresses=192.168.88.244 ... default config has 192.168.88.0/24 on LAN and bridge is the interface used by roouter to talk to LAN. And if that's how you need it, then you need the masquerade rule which obfuscates actual src-addresses. ---

## Response 4
If for some reason you absolutely cannot set up separate subnets for the server and for the local clients, and thus you have to use hairpin NAT, @Sob has suggested a workaround the other day that allows you to learn the address of the local client based on what gets logged: to useaction=netmapinstead ofaction=masqueradeto replace the prefix of the client's address with another one and keep the suffix unchanged. So e.g. if the client connects from 192.168.88.5, anetmaprule withto-addressesset to10.168.88.0/24will change that to 10.168.88.5 (or you can use any other private prefix that suits you better). In any case, the new source address (the "official" name isreply-dst-address) will be outside the own subnet of the server, so the server will have to use the Tik as a gateway to send its response, and you'll see an individual alias of the original address of the client in the logs.This approach only doesn't work if the server doesn't have any routes. ---

## Response 5
If for some reason you absolutely cannot set up separate subnets for the server and for the local clients, and thus you have to use hairpin NAT, @Sob has suggested a workaround the other day that allows you to learn the address of the local client based on what gets logged: to useaction=netmapinstead ofaction=masqueradeto replace the prefix of the client's address with another one and keep the suffix unchanged. So e.g. if the client connects from 192.168.88.5, anetmaprule withto-addressesset to10.168.88.0/24will change that to 10.168.88.5 (or you can use any other private prefix that suits you better). In any case, the new source address (the "official" name isreply-dst-address) will be outside the own subnet of the server, so the server will have to use the Tik as a gateway to send its response, and you'll see an individual alias of the original address of the client in the logs.This approach only doesn't work if the server doesn't have any routes.Thanks, but what I need is the ability to record every real internal or external IP address ---

## Response 6
The second rule hints at use of hairpin NAT because in-interface=bridge to-addresses=192.168.88.244 ... default config has 192.168.88.0/24 on LAN and bridge is the interface used by roouter to talk to LAN. And if that's how you need it, then you need the masquerade rule which obfuscates actual src-addresses.If I only keep first rule , it will cause the intranet to be inaccessible ---

## Response 7
Thanks, but what I need is the ability to record every real internal or external IP addressYou can make the srcnat rule only act if the source address is from server's own subnet, as the server will send responses to requests coming from any other subnet via the router anyway. You only need the srcnat rule to prevent the server from taking a shortcut when responding to an incoming request from its own subnet.But there is no way to have the srcnat rule for same-subnet clients and let the server see their real addresses. ---

## Response 8
Thanks, but what I need is the ability to record every real internal or external IP addressYou can make the srcnat rule only act if the source address is from server's own subnet, as the server will send responses to requests coming from any other subnet via the router anyway. You only need the srcnat rule to prevent the server from taking a shortcut when responding to an incoming request from its own subnet.But there is no way to have the srcnat rule for same-subnet clients and let the server see their real addresses.Thanks. UnderstoodI need to add a non 192.168.88 network segment to the server in order to obtain an accurate IP address for the internal networkHow to add rules for the external networkCan you give me an example ---