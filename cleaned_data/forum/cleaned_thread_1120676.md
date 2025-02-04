# Thread Information
Title: Thread-1120676
Section: RouterOS
Thread ID: 1120676

# Discussion

## Initial Question
===Background===1. Use PPPoE-Client to connect to my ISP2. ISP provided 8 ipv4 address, so I can dial up to 8 pppoe connect.3. I add pppoe-out1 ~ pppoe-out8 on my RB962 to use all my ip address.4. each pppoe link also provided ipv6 /64 ip address, too.and now I am trying to add ipv6 dhcp client to all my pppoe-out interfaces......the first one is ok, I can get my ipv6 prefix on pppoe-out1, and when I am add the second one, it fails (never got an ipv6 prefix), due to the same DUID, the only way to change DUID is to switch "use interface DUID", I tried, and seems like I can only got 2 prefix (and I would like to have 8 ).How can I have more then 2 DUIDs ? ---

## Response 1
You can try to add 7 additional MACVLAN interfaces (over the ethernet interface), each will have their own MAC address. Then dial pppoe-out2~8 on those MACVLAN interfaces instead of on the main ethernet interface, and turn onuse-interface-duidon those instances. ---

## Response 2
You can try to add 7 additional MACVLAN interfaces (over the ethernet interface), each will have their own MAC address. Then dial pppoe-out2~8 on those MACVLAN interfaces instead of on the main ethernet interface, and turn onuse-interface-duidon those instances.Thanks for advise.I tried, but.............(1) I add MACVLANs and dial pppoe-out 2~8 on them.(2) when I am trying to use DHCPv6 client.......if I add DHCPv6 client on pppoe-out interface, they got the same DUID, and if I add DHCPv6 client on macvlan interface, it shows different, but I cannot get my ipv6 prefix. ---

## Response 3
Edit: sorry, I misread.Does it mean that the DHCPv6 Clients on the different pppoe-out interfaces all have the same DUIDs, but different from when use-interface-duid is unchecked, right?Edit 2: Well, while trying to create additional PPPoE out instances and adding DHCPv6 clients to them, I have now been hit by this bug:viewtopic.php?t=211425viewtopic.php?t=211778Looks like I have to reset everything now. ---

## Response 4
I am afraid you'll have to open a support ticket and wait for months. A PPPoE client interface does not inherit the MAC address from the underlying L2 interface as it is itself an L3 one, so use of macvlan interface changes nothing. If you setuse-interface-duidtoyes, the DUID of any PPPoE interface is always set to 0x0003 (link-layer address) 0x0001 (Ethernet) 0x0000 0x0000 0x0000, which is not nice to say the least (as the hardware type is definitely not Ethernet). Ifuse-interface-duidstays at the defaultno, it uses the MAC address of ether1 to build the DUID. If you manually define a Client-IDoptionwith some arbitrary DUID value and make the DHCPv6 client use it, it indeed replaces the automatically generated one in the DHCPv6 Solicit message by the user-defined one, but it does not replace the DUID value in its internal data, so it ignores the Reply from the server, which contains a copy of the client ID, with abad client DUIDlog message. ---

## Response 5
I was hit by the same bug, reported, and got a reply that fixed on 7.17rc.Edit: sorry, I misread.Does it mean that the DHCPv6 Clients on the different pppoe-out interfaces all have the same DUIDs, but different from when use-interface-duid is unchecked, right?Edit 2: Well, while trying to create additional PPPoE out instances and adding DHCPv6 clients to them, I have now been hit by this bug:viewtopic.php?t=211425viewtopic.php?t=211778Looks like I have to reset everything now. ---

## Response 6
Yes, I upgraded to the latest 7.17rc3 and it's has been fixed as you said. And can confirm that sindy is correct about the DUID being all 0x00030001000000000000. So what I wrote above won't be able to solve your problem. ---

## Response 7
I followed Sindy's advice to open a ticket for that. ---

## Response 8
From 7.18beta "what's new" list:*) dhcpv6-client - allow specifying custom DUID;Some months are shorter than others ---