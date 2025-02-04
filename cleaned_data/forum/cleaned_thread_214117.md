# Thread Information
Title: Thread-214117
Section: RouterOS
Thread ID: 214117

# Discussion

## Initial Question
Hi just wondering as i see it works, but need to be clear on this:I have P2P Ipsec connection and added with 3 x policy from one subnet to different subsets (in pic) and PH2 is all establish with the same p2p ipsec tunnel and it works.I did not found any information if i can use like that. Tried to find in official manual (maybe did not see), but there are no explanation if i can use like that. Every example is one subnet to one subnet and thats it. Can someone explain little about ?A/ip ipsec policyadd src-address=10.1.202.0/24src-port=any dst-address=10.1.101.0/24dst-port=any tunnel=yes action=encrypt proposal=ike1-site2 peer=ike1-site2B/ip ipsec policyadd src-address=10.1.101.0/24src-port=any dst-address=10.1.202.0/24dst-port=any tunnel=yes action=encrypt proposal=ike1-site1 peer=ike1-site1 ---

## Response 1
You would find more details in the IPsec RFCs, but this is by design. IPsec is different from all other VPN protocols in terms that it was originally intended to work on top of regular routing and take any traffic it likes. The tool to choose said traffic is a "traffic selector" whose match fields are similar to those of other types of packets match lists - IP protocol (ICMP, TCP, UDP, ...), source and destination addresses and, where applicable, ports; what is unique is that these match lists are negotiated between the peers and they must match in order that the Security Associations used to deliver the traffic that the match lists have chosen would even establish. The traffic selectors are used also as filters of incoming traffic - packets that match a traffic selector but did not come in via the SA associated to that traffic selector are silently dropped.So you can view it as routing and traffic filtering integrated in a single configuration. For simple topologies, it is an elegant solution; already for moderately complicated ones, it is an unmanageable nightmare and it is better to use IPsec to encrypt the transport packets of a more traditional tunnel and use normal routing to send the desired traffic to that tunnel. ---

## Response 2
Hi Sindy, From my tests that what i was thinking about these policies - they are like "traffic selectors or markers"Also if i use /32 mask on both ends it will be pretty tight p2p between hosts as i guess (no outside access to other IP address).As for the last part of question as far i understand we can use like this, but when complexity come into play we need to do SVI like with ipsec and route traffic to/out those interfaces ? ---

## Response 3
when complexity come into play we need to do SVI like with ipsec and route traffic to/out those interfaces ?No idea what you mean by SVI, but for years, Mikrotik refuses to implement a virtual tunnel interface for IPsec and sticks with this standard traffic selector approach. When connecting two Mikrotiks, an IPsec-encrypted IPIP tunnel is a tiny bit more complicated to configure than a VTI but the size of the transport packets is the same; however, the encapsulation format is not compatible between the two so you cannot connect a Mikrotik device e.g. to Azure cloud this way and you have to use complicated constructs where the traffic selector for the Azure is 0.0.0.0/0 <-> 0.0.0.0/0 and there is a ton of exception traffic selectors before it. Which disqualifies Mikrotik for some applications. ---

## Response 4
@mdd: Do you mean SVI (Switched Virtual Interface) as a VLAN interface?Regarding IPsec’s built-in "traffic selectors", I agree with Sindy; it can easily become an overcomplicated mess and is better handled using routing or other filtering mechanisms. ---

## Response 5
@larsa Yes sorry VTI, as i mixed with switch. Like wise Cisco has and it can be routed through it.Also i just wondering what better solution would be if we still need to have IPSEC () and have option to routed any network we need ? As L2TP + IPSEC is old. IPIP ? ---

## Response 6
Dear MikroTik, We love your products, but other vendors aren't as fond of the lack of VTI support. I'm sure this post won't be the last to mention it.Could you kindly let us know—should we wait for RouterOS v8.* to finally see VTI support? If so, I'll be telling stories to my grandchildren about the lack of VTI in RouterOS (for context, my daughters are 8 and 4—I hope everyone catches the sarcasm!).Thank you! ---

## Response 7
@dakobg – Since this is just a user forum, you might get more attention by contacting Mikrotik support or sales directly, particularly if you have a business case that requires VTI. ---

## Response 8
Well my question still open - what would be best solution to avoid "can easily become an over complicated mess and is better handled using routing or other filtering mechanisms" this kind of situation? ---

## Response 9
I’m not exactly sure what you’re looking for. Are you trying to add more sites or just filter certain types of traffic? It might be helpful if you could clarify your needs with a brief description of what you’re trying to achieve without IPsec-specific terms. ---

## Response 10
@mdd you are right IPIP will be a good solution for you.Typically this is configured with IPSEC on a /30 link with a BGP neighborhood... ---

## Response 11
@LarsaI am looking what is the best solution for this kind scenario:Requirements:Secure connection to site to site - IPSEC prefered.Site A: has subnet A1 which has to have access to Site B subnet B1 and B2Site B: has two subnets B1 and B2 to access from/to Site A subnet A1.Tested with with IPSEC tunnel with multiple policy (aka selectors traffic picture up) it works.But Sindy mention this is not the best solution to do this. So my question is what is then best solution to fulfill this requirements on MK.@panisk0 why BGP explain please. Could be enough just simple OSPF ? ---

## Response 12
@LarsaI am looking what is the best solution for this kind scenario: Secure connection to site to site - IPSEC prefered. Site A: has subnet A1 which has to have access to Site B subnet B1 and B2. Site B: has two subnets B1 and B2 to access from/to Site A subnet A1.Since your setup is a single site-to-site tunnel with just subnet selectors, it should work just fine as is. You can even skip the source/destination port selectors, since 'any' is the default.I know this wasn’t a part of the question, but you might want to check that your MikroTik devices on both sides support AES hardware acceleration as shown in this table: 'MikroTik IPsec Hardware Acceleration'. If either side doesn’t, consider using WireGuard for better throughput and less CPU load.About the "not the best solution" comment (just guessing here), I think Sindy was probably referring to significantly more complex setups with multiple tunnels and a mix of different IPSec selectors like ports, protocols, and subnets. ---

## Response 13
@Larsa yes i am linking to complex setups. As i have N tunnels (not IPSEC basic) i would like to be more clear off as i will have more IPSEC tunnels with different clients subnets (not in concern like ports, protocols) in future. Ideally it would be nice to have permanent good solution from the start, instead redoing later on. So is it will be good to stuck one "selector" like or better more to GRE+IPSEC like setups. ---

## Response 14
Bare IPsec with traffic selectors is a voucher for migraines for any setup that is not predictable, and potentially overlapping remote subnets are another one. So I'd definitely prefer GRE encrypted using IPsec in transport mode for such a scenario. ---

## Response 15
Thanks Sindy.Thanks Larsa. ---