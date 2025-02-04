# Thread Information
Title: Thread-1123421
Section: RouterOS
Thread ID: 1123421

# Discussion

## Initial Question
Hi there!The dhcp-client isn't adding dynamic routes specified by DHCP. Any ideas why? Am I missing something obvious?I've included snippets of what I think is relevant below. Please let mw know if you need more information.
```
/system resourceprintuptime:15h32m20sversion:6.48.2(stable)build-time:Apr/09/202110:17:26factory-software:6.44.6free-memory:972.0MiBtotal-memory:1024.0MiBcpu:ARMv7cpu-count:4cpu-frequency:1400MHzcpu-load:0%free-hdd-space:422.7MiBtotal-hdd-space:512.3MiBarchitecture-name:arm
         board-name:RB4011iGS+platform:MikroTik/ip dhcp-clientadddisabled=nointerface=Starlink13:44:25dhcp,debug,packet dhcp-client onStarlinksending requestwithid2226451417to100.127.255.513:44:25dhcp,debug,packet     ciaddr=100.74.98.20713:44:25dhcp,debug,packet     chaddr=08:55:31:E8:DC:BF13:44:25dhcp,debug,packetMsg-Type=request13:44:25dhcp,debug,packetParameter-List=Subnet-Mask,Classless-Route,Router,Static-Route,Domain-Server,NTP-Server,CAPWAP-Server,Vendor-Specific13:44:25dhcp,debug,packetHost-Name="Gateway"13:44:25dhcp,debug,packetClient-Id=01-08-55-31-E8-DC-BF13:44:25dhcp,debug,packet dhcp-client onStarlinkreceived ackwithid2226451417from100.127.255.513:44:25dhcp,debug,packet     ciaddr=0.0.0.013:44:25dhcp,debug,packet     yiaddr=100.74.98.20713:44:25dhcp,debug,packet     chaddr=08:55:31:E8:DC:BF13:44:25dhcp,debug,packetMsg-Type=ack13:44:25dhcp,debug,packetServer-Id=100.127.255.513:44:25dhcp,debug,packetSubnet-Mask=255.192.0.013:44:25dhcp,debug,packetRouter=100.127.255.513:44:25dhcp,debug,packetDomain-Server=8.8.8.8,8.8.4.413:44:25dhcp,debug,packetAddress-Time=30013:44:25dhcp,debug,packetClassless-Route=192.168.100.1/32->0.0.0.0,34.120.255.244/32->0.0.0.0,0.0.0.0/0->100.127.255.513:44:25dhcp,debug,state dhcp-client onStarlinkentering<bound>state/ip dhcp-clientprintdetailFlags:X-disabled,I-invalid,D-dynamic0interface=Starlinkadd-default-route=yesdefault-route-distance=1use-peer-dns=yesuse-peer-ntp=yes dhcp-options=hostname,clientid status=bound address=100.74.98.207/10gateway=100.127.255.5dhcp-server=100.127.255.5primary-dns=8.8.8.8secondary-dns=8.8.4.4expires-after=2m44s/ip routeprintdetailFlags:X-disabled,A-active,D-dynamic,C-connect,S-static,r-rip,b-bgp,o-ospf,m-mme,B-blackhole,U-unreachable,P-prohibit0ADS  dst-address=0.0.0.0/0gateway=100.127.255.5gateway-status=100.127.255.5reachable viaStarlinkdistance=1scope=30target-scope=10vrf-interface=Starlink1ADC  dst-address=100.64.0.0/10pref-src=100.74.98.207gateway=Starlinkgateway-status=Starlinkreachable distance=0scope=102ADC  dst-address=192.168.1.0/24pref-src=192.168.1.1gateway=bridge gateway-status=bridge reachable distance=0scope=10Thanks!

---
```

## Response 1
Hi there! Same issue with 6.48.3. Any thoughts? ---

## Response 2
Replaced byviewtopic.php?f=2&t=175272#p871239 ---

## Response 3
Thank you for responding!I would generally agree with you however in the debug output that I showed, the Parameter-List does include Classless-Route (unless I'm misreading the output). Also the documentation seems to indicate an implicit request for classless routes. [https://wiki.mikrotik.com/wiki/Manual:IP/DHCP_Client]Just in case, I tested by removing the offending `dhcp-options=hostname, clientid` from the DHCP Client configuration and still didn't get routes set.Any other thoughts or hints? ---

## Response 4
Replaced byviewtopic.php?f=2&t=175272#p871239 ---

## Response 5
I removed the dhcp-options from the client configuration because you mentioned them and I hadn't tried that yet. :-) Initially I assumed you were telling me to explicitly add an option to request classless-routes but after re-reading the Mikrotik documentation saw that it's already there and seems unnecessary.I don't have access to the DHCP server to show its configuration but can do a packet capture if the debug information in the original post isn't enough. The server is a Starlink terminal [Dishy McFlatface].Are you thinking that the dhcp-client configuration that I have should be working? ---

## Response 6
Worth mentioning (it's obvious anyway) that this is regarding Starlink, maybe @rextended can take a look at the DHCP setting that they are using. Or just ignore the troll.Oh wait, he asked about the configuration of the DNS server, how is that related, beats me.Anyway, Just looking at those classless-routes received you'd see that there's no way those can be set currently on RouterOS. Probably that's why they are silently failing.Why? gateway=0.0.0.0 is an invalid value for .. gateway :) And unless RouterOS makes a translation from 0.0.0.0 -> dhcp_client_interface this will most likely never get fixed.But you can write a ticket anyway, maybe they find a way to handle this.Until then, you can set those two routes static, shouldwork, unless something more is needed:
```
/ip routeadddistance=1dst-address=34.120.255.244/32gateway=Starlinkadddistance=1dst-address=192.168.100.1/32gateway=Starlink

---
```

## Response 7
Replaced byviewtopic.php?f=2&t=175272#p871239 ---

## Response 8
Replaced byviewtopic.php?f=2&t=175272#p871239 ---

## Response 9
Ah, so NOW you took the time to read the details provided in the first post? Instead of asking for the "DNS Server config"...Hence, the troll.PS: good job at editing your replies.PS2: specifying the interface like I wrote above should be ok, as others tested on other routers:https://www.reddit.com/r/Starlink/comme ... &context=3&https://www.reddit.com/r/Starlink/comme ... p_to_work/As in, NOT specifying thedefault gatewayfor those two IPs :)Cheers.Let's see if you'll edit these replies now too.. ---

## Response 10
Replaced byviewtopic.php?f=2&t=175272#p871239 ---

## Response 11
Thank you, @Znevna, I was pretty sure the configuration was correct. I had assumed that RouterOS would have seen the 0.0.0.0 destination in the classless-route parameter, recognized the default route and set a dynamic route appropriately. Since it doesn't, I thought I had missed something.Incidentally, setting the routes manually with gateway set to the interface has always worked although setting gateway to the IP address does not. Again, I don't have the routing experience to recognize why (or perhaps it's RouterOS packet processing?). Thank you for doing the additional research on Starlink, @Znevna, I probably should have mentioned that in the original post and could have saved you the time. :-/In summary: The RouterOS dhcp-client is configured correctly but doesnotset the classless-routes sent by the Starlink terminal DHCP server. I'll contact Mikrotik support.On a [not really] related note, setting the routes manually works when using the interface as gateway but not the specified IP address [100.127.255.5 in this example]. That's probably a more simple well understood problem related to basic IP routing. :-) If you feel like explaining it I'd appreciate it but otherwise not to worry. I'll get to it eventually for my own education. This is partly related to @rextended stating that 192.168.100.1 and 34.120.255.244 should already be covered by 0.0.0.0. I would have agreed except it doesn't work. :-oThanks again for taking the time to respond. ---

## Response 12
Probably 192.168.100.1 are added for force the phone app to work everytime, ignoring all the mess you can do on the config.Starlink proprietary router can understand those two routes also for Starlink captive portal (34.120.255.244 my.starlink.com)The differences between:192.168.100.1->WAN interface = search 192.168.100.1 inside the device himself192.168.100.1->GatewayIP = search 192.168.100.1, passing by gateway, on the other side of the connection(please try to understood I try to explain it from Italian)obviously when I haved see 192.168.100.1/32->0.0.0.0 I do not have noticed the missing detail at the end: /0 !!!0.0.0.0/0 = any IPv40.0.0.0 = means that no intermediate routing hops are necessary because the system is directly connected to the destination (MikroTik do not understand this)@Znevna please consider the option to not consider me one troll, please. ---

## Response 13
Thank you, @Znevna, [...]In summary: The RouterOS dhcp-client is configured correctly but doesnotset the classless-routes sent by the Starlink terminal DHCP server. I'll contact Mikrotik support.[...]Welcome! Yeah, I wrote above why those two routes won't register, you can try manually and see the error msg. (and a typo):
```
/ip routeadddst-address=192.168.100.1gateway=0.0.0.0failure:Invalidroute configuration:Invalidgateway configrationAnd the only (easy) fix I can think of is also the one mentioned above, if they somehow translate "gateway=0.0.0.0" to "gateway=interface_of_current_dhcp_client" before adding the routes received.Or if Starlink finds another way to do this.Regarding why specifying the default gateway doesn't work .. well.. that's what you're trying to avoid, and by specifying it again is just redundant.

---
```

## Response 14
Replaced byviewtopic.php?f=2&t=175272#p871239 ---

## Response 15
[quote @Znevna] Regarding why specifying the default gateway doesn't work .. well.. that's what you're trying to avoid[/quote]LOL of course! :-o@rextended, don't worry about the script unless it's an exercise for yourself. I see what you're doing and it makes sense. This is residential and setting the routes manually is fine, I was just trying to figure out why the dhcp-client wasn't working. I may write the script myself for learning purposes (but probably not soon).If anyone is still reading and interested, the router that Starlink supplies is apparently a customized OpenWRT however it is not accessible by the user at this time. Simply removing it and connecting your own router to the terminal [dishy] works fine. I have connected an RB4011iGS+ and [controversially?] use a Mikrotik Audience for WiFi as well as a CRS326-24G-2S+.Thanks again! ---

## Response 16
@rextended, don't worry about the script unless it's an exercise for yourself. I see what you're doing and it makes sense.Thanks, but I think than be useful for anyone, not only for you, and practice for me :) ---

## Response 17
Replaced byviewtopic.php?f=2&t=175272#p871239 ---

## Response 18
There is any hope if I terminate the script you try it? ---

## Response 19
Yes, I'm happy to test the script. Feel free to contact me privately for further discussion if you prefer, then can post a working version here. ---

## Response 20
search tag # rextended starlink classless routeSummary of the progress made so far:By this setup on MikroTik DHCP Server I can simulate exactly what DHCP Server on Starlink device option 121 Classless-Route send to MikroTik DHCP Client:
```
/ip dhcp-server optionaddcode=121name=Classless-Routevalue=0x20C0A8640100000000202278FFF40000000000647FFF05/ip dhcp-server networkadd...dhcp-option=Classless-Route...Equivalent to:Classless-Route = 192.168.100.1/32->0.0.0.0,34.120.255.244/32->0.0.0.0,0.0.0.0/0->100.127.255.5With another device I can read Classless-Route passed and store it with DHCP Client interface name on two global variables:
```

```
/ip dhcp-client...script=":global dhcpClientIF \$interface ; :global dhcpClientCR (\$\"lease-options\"->\"121\")"...For better readability::global dhcpClientIF $interface:global dhcpClientCR ($"lease-options"->"121")and on global variables I obtain:
```

```
[rextended@MATRIX]/system script environment>pri# NAME               VALUE0dhcpClientIF      ether11dhcpClientCR        \C0\A8d\01\00\00\00\00"x\FF\F4\00\00\00\00\00d\7F\FF\05
spaces!!!------------^----------------------^Space, d (as d letter not as 0xD exadecimal value), " and x are presents because on print Mikrotik escape the characters than can not display.For example Space is present because hex value 0x20 (subnet /32) on ASCII correspond to Space charactersWhile >d< are for \64, the 100 of first IP address, >"< are for \22, the "34" of second IP adress, and >x< are for \78, the 120 of second IP address.Later I have create two function.The first called "chr2int" read one char passed to the function and return the corresponding decimal value.For example, passing one character, like "\C0" return 192The char can be any single char and return integer value from 0 to 255The second called "str2ip" convert one string of 4 chars or less, using previous function, to dotted IP.passing one 4 charecters string, like "\C0\A8\64\01" return "192.168.100.1"If the length of the imput string is more than 4, exceeding characters are ignoredIf the length of the imput string is less than 4, add carryng .0passing one 3 charecters string, like "\C0\A8\64" return "192.168.100.0"passing one 2 charecters string, like "\C0\A8" return "192.168.0.0"passing one 1 charecters string, like "\C0" return "192.0.0.0"passing one empty string, like "" value return "0.0.0.0"Passing one other type of variable is converted first (internally by RouterOS) to string and processed as before.How classless route work.All routes are subsequently one by one without any form of divisionNow I have understand how to split classless route raw value on single routesRules:1) first Byte is always the subnet and is always between hex \00 and \20 (dec 0 to 32)2) only relevant IP part of the ip / ip-prefix are provided, 5 cases are possible:if subnetis are /0 no other char/hex value for IP are present and it mean "all IPv4 space" (\00 = 0.0.0.0/0)and next four char/hex value for IP are used (\20\0A\0A\0A\0A = 0.0.0.0/0 default gateway 10.10.10.10)is a full IPv4 CLASSLESS IP (is whiy are called classles route...)if subnet is from /1 to /8 only one char/hex value for IP are present (\08\0A = 10/8 = 10.0.0.0/8)if subnet is from /9 to /16 only two char/hex value for IP are present (\10\0A\0A = 10.10/16 = 10.10.0.0/16)if subnet is from /17 to /24 only three char/hex value for IP are present (\18\0A\0A\0A = 10.10.10/24 = 10.10.10.0/24)if subnet is from /25 to /32 all four char/hex value for IP are present (\20\0A\0A\0A\0A = 10.10.10.10/32)0x20C0A8640100000000202278FFF40000000000647FFF05assuming dhcp-client.interface.name = Starlinkstart reading:first char \20 = subnet mask /32 (hex 20 = 32 dec)the following 4 chars, because the subnet mask are /32 "\C0\A8\64\01" = 192.168.100.1the following 4 chars, because now are set the classless route "\00\00\00\00" = 0.0.0.0Only on this case, as RFC specify, when the dst ip is 0.0.0.0, really this it means "this interface" intending on what interface the DHCP Client is setMikroTik do not understand this (as RFC say, if you do not understand this, ignore only this)All of this means that the routes is not really 192.168.100.1/32->0.0.0.0 but must be intended as192.168.100.1/32->Starlinkfollowing the read of data:"\20" subnet /32"\22\78\FF\F4" 34.120.255.244"\00\00\00\00" 0.0.0.034.120.255.244/32->Starlinkreading follow value "\00" is intended /0 and is for default gateway for all IP /0 (0.0.0.0/0)"\64\7F\FF\05" 100.127.255.50.0.0.0/0->100.127.255.5At this point, after all considerations, what I need to do to finish:x) Create the option for 3-only / 2-only / 1-only character and empty / nil / nothing / invalid values for str2dotIPDone on 2021/06/17x) Create one procedure that follows the raw classless-route value than understand and splits the routes as wrote before.Done on 2021/08/03Added 2021/06/17:saving the result as couple of array of values like"192.168.100.1/32;0.0.0.0 , 34.120.255.244/32;0.0.0.0 , 0.0.0.0/0;100.127.255.5"for be processed from following scriptDone on 2021/08/03Added 2021/08/03:Now finally I obtain after split:192.168.100.1/32->0.0.0.034.120.255.244/32->0.0.0.00.0.0.0/0->100.127.255.52021/08/03 What is missing now is:1) Create the DHCP-Client script for add classless-route to routung table and remove them when DHCP-Client are disabled / not renowed / released

---
```

## Response 21
Purpose? Lets say I have starlink service, what would I use this for................... ---

## Response 22
Purpose? [...]It's been a while, if I'm not mistaken it was to correctly reach the router and the captive portal with the classless routers that the DHCP server sent to the client... ---

## Response 23
... just had the ... thing ... to reverse my own option-121 too ....as lazy as I am ....I remitted some coffee-aglet ... to the guy where I usally generate the option ... ... lazy-ways ....https://www.medo64.com/2018/01/configur ... te-option/.... since he has the generation code ... ¯\_(ツ)_/¯ ... he can - while having a coffee - reverse the function ... and link it on his page.... so lazy me : ) ... can ... be ... a happy option-121-user ---

## Response 24
... in theory ... : ) ---

## Response 25
https://www.medo64.com/2025/02/decoding ... te-option/.... a fresh brew ... is magic ! ---

## Response 26
:D ... a fresh brew ... is magic !Using 0x20C0A8640100000000202278FFF40000000000647FFF05provide not correct, but not wrong, results:192.168.100.1/32 via 0.0.0.0 -> must be like 192.168.100.1/32 via <DHCP client interface>34.120.255.244/32 via 0.0.0.0 -> must be like 34.120.255.244/32 via <DHCP client interface>default via 100.127.255.5 -> OK***************************************************************I just realized now that I never posted the code, thank goodness I found it again...Example based of reading 0x20C0A8640100000000202278FFF40000000000647FFF05 inside DHCP-client on ether1renamed Starlink192.168.100.1/32->0.0.0.0 [Starlink]120.255.244/32->0.0.0.0 [Starlink]0.0.0.0/0->100.127.255.5 (default route)It's old, is for a preliminar version, not optimized, do not consider new v7 functions.old for debug code:global dhcpClientIF "Starlink" :global dhcpClientCR "\20\C0\A8\64\01\00\00\00\00\20\22\78\FF\F4\00\00\00\00\00\64\7F\FF\05" :global tmpChar "\00" :global hexChars "0123456789ABCDEF" :global charsString "" :for x from=0 to=15 step=1 do={ :for y from=0 to=15 step=1 do={ :local tmpHex ([:pick $hexChars $x ($x+1)].[:pick $hexChars $y ($y+1)]) [:parse (":global tmpChar \"\\$tmpHex\"")] :set $charsString ($charsString.$tmpChar) } } :global chr2int do={ :for z from=0 to=255 step=1 do={ :if ($1 = [:pick $charsString $z ($z+1)]) do={ :return $z } } } :global lenght [:len $dhcpClientCR] :global start 0 :global actualnum -1 :global numberofchar -1 :global ippart "" :global gatpart "" :global str2ip do={ :local ipstring $1 :local chrIP1 [:pick $ipstring 0 1] :local chrIP2 [:pick $ipstring 1 2] :local chrIP3 [:pick $ipstring 2 3] :local chrIP4 [:pick $ipstring 3 4] :local dotIP1 0 :local dotIP2 0 :local dotIP3 0 :local dotIP4 0 :for z from=0 to=255 step=1 do={ :local compare [:pick $charsString $z ($z + 1)] :if ($chrIP1 = $compare) do={ :set $dotIP1 $z } :if ($chrIP2 = $compare) do={ :set $dotIP2 $z } :if ($chrIP3 = $compare) do={ :set $dotIP3 $z } :if ($chrIP4 = $compare) do={ :set $dotIP4 $z } } :return [:toip "$dotIP1.$dotIP2.$dotIP3.$dotIP4"] } :if ($lenght < 5) do={ :put "invalid lenght $lenght"; :return -1 } :while ($start < $lenght) do={ :set actualnum [$chr2int [:pick $dhcpClientCR $start ($start + 1)] ] :set start ($start + 1) :if ($actualnum > 32) do={ :put "invalid subnet $actualnum"; :return -1 } :set numberofchar (($actualnum + 7) / 8) :set ippart [:pick $dhcpClientCR $start ($start + $numberofchar)] :set start ($start + $numberofchar) :set gatpart [$str2ip [:pick $dhcpClientCR $start ($start + 4)]] :set start ($start + 4) :if ($gatpart = 0.0.0.0) do={ :set gatpart $dhcpClientIF } :put "$[$str2ip $ippart]/$actualnum->$gatpart" }results code192.168.100.1/32->Starlink 34.120.255.244/32->Starlink 0.0.0.0/0->100.127.255.5The code should have continued that instead of ":put":The corresponding route was created, with a unique comment to be able to delete it when the DHCP client released or expired the lease.If the destination was 0.0.0.0 a route was created to the interface used by the DHCP client intead of one IP. ---