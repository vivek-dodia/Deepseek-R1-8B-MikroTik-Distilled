# Thread Information
Title: Thread-213673
Section: RouterOS
Thread ID: 213673

# Discussion

## Initial Question
This is more of a BGP question I think. We are advertising RTBH to an upstream router, which broke after an upgrade to 7.16.2We have a script that was issuing this command to trigger the RTBH:/ip route add dst-address=$ip type=blackhole bgp-communities=7018:86, 7922:666, 65530:666The type and bgp-communities options are no longer available, so I changed the command to this:/ip route add blackhole dst-address=$ipPreviously I was advertising these communities to an upstream router for RTBH. The upstream router was looking for these communities. What is the recommended way to advertise these routes now?Here is my peer, template, and filter:/routing bgp connectionadd cisco-vpls-nlri-len-fmt=auto-bits connect=yes listen=yes local.role=ebgp \name=peer1 remote.address=<remote address> .as=<asn> .port=179 templates=\default/routing bgp templateset default disabled=no output.filter-chain=bgp-out .network=bgp-networks \.redistribute=static, vpn, dhcpadd as=<asn> disabled=yes name=bgp1 output.network=bgp-networks \.no-client-to-client-reflection=yes .redistribute=bgp router-id=\<routerid>/routing filter ruleadd chain=bgp-out disabled=no rule="if (protocol static && bgp-communities inc\ludes 65530:666, 7018:86, 7922:666) { accept; }"add chain=bgp-out disabled=no rule="if (protocol static) { reject; }"Thanks! ---

## Response 1
A route can still be marked as blackhole by just writingblackholebut for the BGP communities probably addtional filter rules would be needed, something likeappendor I don't know ---