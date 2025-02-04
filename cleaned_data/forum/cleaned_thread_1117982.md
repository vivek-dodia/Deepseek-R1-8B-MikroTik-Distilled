# Thread Information
Title: Thread-1117982
Section: RouterOS
Thread ID: 1117982

# Discussion

## Initial Question
According to VRF’s supported features list Wireguard is not yet supported.https://help.mikrotik.com/docs/pages/vi ... edfeaturesI would like to request to add support for Wireguard to be able to use a VRF on the peer endpoint address, much like L2TP Tunnels using the ip@vrf_name format.A use-case for such functionality would be for example when having two uplinks (eg DSL modem/routers) with conflicting IPs, that you cannot control/change their subnets (ie: both are in the 192.168.1.0/24 range with both gateways being .1 ). With VRFs you could do Wireguard tunnels on both uplinks without any conflicts.Request ticket id: SUP-134306 ---

## Response 1
Sweet, without VRF, there appears to be anarchy in the wireguard world, I supportgetting rid of anarchy, with chaos ---

## Response 2
VRF support for Wireguard would be very appreciated. ---

## Response 3
Yes, please add VRF support for Wireguard!I am not sure is this is 100% the same issue but I am seeing something odd:I place one internet connection (interface + default route) into a VRF, say "wwan"I add mangle+snat rules to force a specific wireguard endpoint (for tunnel "wg-wwan") into this VRFNow while the traffic doe this tunnel endpoint is in VRF wwan, I'd expect that the interface itself (wg-wwan) is in the main VRFHowever, it seems wg-wwan is now also in VRF wwan which is completely undesired. I can ping the other address of the tunnel by adding "vrf=wwan" but when doing a normal ping or "vrf=main" I am getting a timeout ---

## Response 4
VRF support for Wireguard Interfaces! Please! ---

## Response 5
Why, network better -- dont create overlapping subnets............Wireguard works just fine, if done properly.(caveat home user, dont support real work) ---

## Response 6
Why, network better -- dont create overlapping subnets............Wireguard works just fine, if done properly.(caveat home user, dont support real work)and also here ... it does not have to do something with overlapping networks.don't always assume stuff without properly knowing any background. ---

## Response 7
Why, network better -- dont create overlapping subnets............Wireguard works just fine, if done properly.(caveat home user, dont support real work)Why post better -- don't post useless stuff just for the sake of posting.................If you don't need VRF support in wireguard, good for you. Nobody cares for your non-needs.Instead of being a wise-ass, either post a real working solution to my use case or GTFO.It really gets on my nerves when people shit on others feature requests, when those requests won't affect ANYTHING on their workflow.I remember the same kind of behavior of other idiots when I was one of the first to ask for IPv6 NAT support.In the end MikroTik did add it. Where are all those opposing it? Did it cause any problems to them? No. They were just being arrogant for "knowing better" for "IPv6 is all about end to end connectivity" and other bs like that.If you don't care about Wireguard VRF support, and if you don't have valid criticism why it shouldn't be implemented, please, stay away from my thread. ---

## Response 8
Tongue in cheek Chaos, of course you guys (real IT and not homeowners) are stuck with dealing with such stupid setups such as below:A use-case for such functionality would be for example when having two uplinks (eg DSL modem/routers) with conflicting IPs, that you cannot control/change their subnets (ie: both are in the 192.168.1.0/24 range with both gateways being .1 ). With VRFs you could do Wireguard tunnels on both uplinks without any conflicts.It would seem like a no brainer to be able to combine VRF and wireguard, but is the limiting factor that wireguard is NOT like other VPNs and doesnt have the flexibility to be used for VRF??I dont know...... but if your experience and knowledge says it should be fairly easy then one would expect MT to do so SOONEST, as it provides a unique capability that makes the competitive advantage of MT RoS, that much greater.Time will tell....... have you got an answer on your SUP yet??? ---

## Response 9
14/Nov/23 11:01 AMHello, Thank you for contacting MikroTik Support.Its not supported, we will see if that could be implemented in the future.Best regards, ---

## Response 10
so we wait.cummulus (and therefore linux) is able to do that ---

## Response 11
Tongue in cheek Chaos, of course you guys (real IT and not homeowners) are stuck with dealing with such stupid setups such as below:A use-case for such functionality would be for example when having two uplinks (eg DSL modem/routers) with conflicting IPs, that you cannot control/change their subnets (ie: both are in the 192.168.1.0/24 range with both gateways being .1 ). With VRFs you could do Wireguard tunnels on both uplinks without any conflicts.This isn’t about "stupid setups" but rather about real-world problems that one inevitably encounters. Even though I only use VPNs personally - some for for work-related purposes - I’ve also faced the issue of overlapping subnets. However, that was neither stupid on my part nor on the part of the remote admin in any way.I'd like to express my +1 for this feature request. ---

## Response 12
...or if one has "n" customers on a CCR cluster and customers are in their own VRF respectivelyso in no case whatsoever it is remotely stupid ---