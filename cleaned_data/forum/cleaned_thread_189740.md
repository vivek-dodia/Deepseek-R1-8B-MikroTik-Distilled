# Thread Information
Title: Thread-189740
Section: RouterOS
Thread ID: 189740

# Discussion

## Initial Question
Hey Guys, i love the uncomplicated way how WireGuard works and the Users are much more confident with a stable working VPN.But in nearest time i need to secure these way with 2FA.I just read some threads where they hint to UserManager and OTP Secret. But i really need some more help with this.Where do i get der OTP Secret? Do i need to setup any Server for this? Mainly we use Microsoft Authenticator App.Can anybody maybe give me an example how to configure and Wireguard VPN with 2FA using the Usermanger? ---

## Response 1
You can't Wireguard doesn't have any accounting as far as I know.2FA with userman ---

## Response 2
You can't Wireguard doesn't have any accounting as far as I know.2FA with usermanYes i found this wiki but there is no description from where i get the OTP Secret ---

## Response 3
Not helpful but wondered if tailscale does this.......https://tailscale.com/kb/1075/multi-factor-auth/About WireGuard and 2FA/MFA loginWireGuard® is a modern and fast encrypted networking protocol that offers a number of performance benefits over traditional VPNs and TLS. Among other important features, WireGuard uses Curve25519 for key exchange, which keeps the negotiation phase extremely lightweight and fast. It also has a very low cost per live session, so it can keep direct connections open to a large number of nodes at once.Tailscale builds on top of WireGuard by adding automatic mesh configuration, single sign-on (SSO), 2-factor/multi-factor authentication (2FA/MFA), NAT traversal, TCP transport, and centralized Access Control Lists (ACLs). ---

## Response 4
viewtopic.php?p=911961&hilit=two+factor ... on#p818321 ---

## Response 5
Hey, as far as i unterstand its more a Problem of the Client as an Problem with the Server.I've found the tunsafe Client as a github Project, as far as i understand i just have to add this line to my ServerConfig[Peer]RequireToken = totp-sha1:SECRET, digits=6, period=30, precision=15and if i use my WG Conf Files with tunsafe Client i will get an TOTPIs there any Option to configure the whole Server Conf file at the Mikrotik or must it been added by the developers as an "checkbox"? ---

## Response 6
Main problem is that WG is just tunnels with static config using only keys, there's no support for anything else. So if you see WG with 2FA, it's either something extra aside handling it and controlling WG layer (Tailscale) or custom extension to standard WG (TunSafe):This implementation is a TunSafe specific and experimental extension to the protocol. We would love to find a variant of this proposal, or another solution that can provide the same functionality across other WireGuard implementations. We think a standardized way of doing two-factor authentication would be hugely beneficial to the WireGuard community.They're right, some standard way would be nice, but AFAIK, currently there isn't any. ---

## Response 7
Main problem is that WG is just tunnels with static config using only keys, there's no support for anything else. So if you see WG with 2FA, it's either something extra aside handling it and controlling WG layer (Tailscale) or custom extension to standard WG (TunSafe):This implementation is a TunSafe specific and experimental extension to the protocol. We would love to find a variant of this proposal, or another solution that can provide the same functionality across other WireGuard implementations. We think a standardized way of doing two-factor authentication would be hugely beneficial to the WireGuard community.They're right, some standard way would be nice, but AFAIK, currently there isn't any.experimental or not, if it works it is much more secure an "easy" to implement. At the moment i am thinking about a web based solution where the user has to login an has to enable his wireguard peer manual an if the connection closes or is restartet by any other IP than it disables. But thats much more work to do and so unflexy ---

## Response 8
It may work, but non-standard is bad. Even if MikroTik implemented this extension, it still wouldn't work with any standard WG client. And then someone else would come with own incompatible solution, because they wouldn't like this one for some reason. And someone else would implement that. And there could be more, so in the end we'd end up with several incompatible WGs, that's not good. WG with more features could be nice, but it needs to be joint effort resulting in standard supported by everyone. ---

## Response 9
But on Server side there is nothing more to implement as the posibility to set this Parameter or notOn „normal“ Wireguard Servers you only add the line and go for it.And that is per Peer so you can decide which peer becomes totp and which not ---

## Response 10
Did you test it with normal server (e.g. standard unmodified Linux WG) and did it work? I didn't study it in detail, but from the quick look, if it's extension to protocol, standard server wouldn't have any support for it. ---

## Response 11
No reason why MT couldnt hook checking the radius server as the first step after the initial handshake on the server side and making it an entry on the client side of MT.So if there is a value (entry) for the new parameter on the client side, (yes, no), the router knows that it needs to check the radius server for the credentials embedded after the MT tunnel is established prior to allowing any traffic. ---

## Response 12
No reason why MT couldnt hook checking the radius server as the first step after the initial handshake on the server side and making it an entry on the client side of MT.So if there is a value (entry) for the new parameter on the client side, (yes, no), the router knows that it needs to check the radius server for the credentials embedded after the MT tunnel is established prior to allowing any traffic.yes this would be a good way too, the company i work for wants to certificate with ISO27001 and i think if we dont can implement some version of 2fa with Mikrotik VPN they will cut out these Product out of our Portfolio... ---

## Response 13
You know that whatever like this would be added, it would have to be supported by both sides, right? So unless you'd be satisfied only by MikroTik<->MikroTik interoperability, or maybe including some other client using same non-standard implementation, it wouldn't help you, because no standard client would work with it. ---

## Response 14
That is correct SOB, it would at least allow anybody with an MT to MT scenario to make use of the radius server capability to simulate 2FA.This would encourage folks to get an MT for homeThis would encourage folks to get an MT small form factor wifi device to take on the road (for hotel wifi etc.).Note: This would also work with any android or IOS device connecting via wirequard and useing the IOS or android MT app to connect to the router.I think this is enough utility and coverage to justify the addition. But heck what do I know. ---

## Response 15
Bringing the thread back to lifeI'm actively searching for modernization of legacy VPN services that we are currently using (SSTP, L2TP/IPSec).I love the way wireguard works on all user operating systems, but the upcoming regulations have strict instructions regarding Multi Factor Authentication on remote access.In same matter I really need some authentication for the Wireguard, but except some custom-made server appliances running on VM or docker, I can't find anything that is able to manipulate RouterOS and interact with the user to confirm that this connection is initiated by him.I have idea how it could be managed but I'm not a developer and can not do it myself.If anyone is willing to help, we may be able to bring it to life and help all poor souls around the world that need to comply)It would be really great if Mikrotik itself can make it. I'm sure it will not be so hard to implement. ---

## Response 16
What is your idea? I really doubt that you would be able to implement anything directly on the MikroTik without using a container ... and if you go the route of using a container then you should consider using TailScale instead of reinventing an advanced security feature. ---

## Response 17
For sure there will be some API connecting the router and the RADIUS/AD server and the end user. Container on the router itself or on some hypervisor.My concept is working with the address lists. When new WG session is initiated, the IP of that interface will be in limited address list, the API will initiate a query against the radius to find out who is the user which have this IP as an attribute. If the user is not disabled and is member of specific group, then it will be considered as valid and will initiate the second factor request. For example an very simple app on the user's phone that should be enorlled at first place. So when the API initiate the request, notification will be pushed on the phone so the user will confirn if he is the initiator. If he decline the request, that should be logged and administrator notified for possible WG config stolen. If he approve, API will log to the router and execute command that will move the IP to the appropriate address list. ---