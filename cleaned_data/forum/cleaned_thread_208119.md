# Thread Information
Title: Thread-208119
Section: RouterOS
Thread ID: 208119

# Discussion

## Initial Question
Hello everyone. I'm new to these forums and will try not to make a fool of myself.I registered here after experiencing an issue following the upgrade to 7.15. I had recently managed to get a working dot1x setup using freeradius. I have several Mikrotik switches connecting to it using radsec. Today, I upgraded one of these switches, aCRS312-4C+8XG, to 7.15, which broke something in the communication. The TLS handshake works as normal, then the initial Access-Request is sent and received by freeradius. And no matter which response is sent in return, the switch is not apparently seeing it.I have temporarily fixed this by downgrading to an unsecured connection. Since I didn't see anyone reporting a similar issue, I figured I should write about it, in case it affects other people.Some relevant bits of my configuration:
```
# 2024-06-02 20:37:52 by RouterOS 7.15
# software id = H9BC-RUMQ
#
# model = CRS312-4C+8XG

/radius
add address=192.168.0.1 certificate=radius_client protocol=radsec require-message-auth=no service=wireless,dot1x timeout=10s
/interface dot1x server
add auth-types=dot1x,mac-auth interface=dot1x radius-mac-format=XX-XX-XX-XX-XX-XX
/interface list
add name=dot1x
/interface list member
add interface=ether4 list=dot1x
add interface=ether5 list=dot1x
add interface=ether6 list=dot1x
add interface=ether7 list=dot1x
add interface=ether3 list=dot1x
add interface=ether2 list=dot1x
add interface=combo1 list=dot1x
add interface=combo2 list=dot1x
add interface=combo3 list=dot1x
add interface=combo4 list=dot1x
add interface=ether8 list=dot1xSome relevant bit of log
```

```
17:12:10 dot1x,packet s ether3 rx EAPOL-Start
 17:12:10 dot1x,packet s ether3 tx EAPOL-Packet EAP-Request id:0 method:IDENTITY
 17:12:10 radius,debug new request 82:09 code=Access-Request service=dot1x called-id=12-34-56-78-90-AB
 17:12:10 radius,debug sending 82:09 to 192.168.0.1:2083
 17:12:10 radius,debug,packet sending Access-Request with id 2 to 192.168.0.1:2083
 17:12:10 radius,debug,packet     Signature = *************
 17:12:10 radius,debug,packet     Framed-MTU = 1400
 17:12:10 radius,debug,packet     NAS-Port-Type = 15
 17:12:10 radius,debug,packet     Called-Station-Id = "12-34-56-78-90-AB"
 17:12:10 radius,debug,packet     Calling-Station-Id = "FE-DC-BA-09-87-65"
 17:12:10 radius,debug,packet     Service-Type = 2
 17:12:10 radius,debug,packet     EAP-Message = 0x0200000a017661726469
 17:12:10 radius,debug,packet     User-Name = "host"
 17:12:10 radius,debug,packet     Acct-Session-Id = "86300003"
 17:12:10 radius,debug,packet     NAS-Port-Id = "ether3"
 17:12:10 radius,debug,packet     Unknown-Attribute(type=102) = 0x00
 17:12:10 radius,debug,packet     NAS-Identifier = "nas"
 17:12:10 radius,debug,packet     NAS-IP-Address = 192.168.0.2
 17:12:10 radius,debug,packet     Message-Authenticator = ************
 17:12:10 dot1x,packet s ether3 rx EAPOL-Packet EAP-Response id:0 method:IDENTITY
 17:12:20 radius,debug timeout for 82:09Configuration and logs have been redacted.

---
```

## Response 1
Hi, I can confirm that it is broken. Spent couple of hours troubleshooting the AP that was not getting the replies from RadSec server, claiming that the server timed out, when I saw the access-accept in the server logs every time; until I have stumbled accross your post.Not the first time something gets broken in the new version ...MikroTik, cmon, get your £$@% together !Downgrade to 7.14.3 solves the issue - RadSec works again.C. ---

## Response 2
I have the same issue with the Hotspot using Radius on 7.15.I've confirmed via Wireshark that 'Access-Accept' packets are being received by the Mikrotik, yet the 'Accepts' on the Mikrotik shows 0 (and the Hotspot doesn't auth users).example_of_hotspot_radius_fail.png ---

## Response 3
it is kind of disturbing that things break in areas not related to changelog. this somehow reduces my trust in ROS changelog. It is rather a fairy book ---

## Response 4
Thats not good.I'm writing a custom radius server program at the moment, and using MT as my test tool.Lets hope that gets sorted ---

## Response 5
In fairness I think this is the first ever issue I've had with Hotspot Radius in 10+ years of using Mikrotiks. ---

## Response 6
In my case this actually turned out to be a user error (on my part).I'd failed to see these lines in the release note:) radius - added "require-message-auth" option that requires "Message-Authenticator" in received Access-Accept/Challenge/Reject messages;) radius - include "Message-Authenticator" in any RADIUS communication messages besides accounting for all services;...setting 'require-message-auth = no' resolved the issue (for me).I can see this is not the same issue as the OP was having (as they've already set that attribute). ---

## Response 7
I can also confirm that radsec is completely unusable in 7.15. This occurs regardless of the "require-message-auth" setting.RouterOS reports a RADIUS timeout when radsec is enabled, leading me to believe that the code enforcing the presence of a message authenticator returns a DROP decision forallreceived radsec replies.Going back to udp with shared secrets solves the issue for now, but it's obviously far less secure.Please fix this! ---

## Response 8
Given this newBlast radiusvulnerability, it would be really nice to have radsec working... ---

## Response 9
I submitted a ticket to Mikrotik support on June 6th regarding this issue (SUP-155235). It is still in the WAITING FOR SUPPORT status and has had no comment. Rather surprising to have such a significant infrastructure and security feature go un-addressed this long, especially with two subsequent minor releases. ---

## Response 10
Hello everyone, I'm new on this forum, I expect you feel good.I experienced the same problem, message 'AUTH_FAILED'My configuration:CRS354-48G-4S+2Q+: 7.15.3with Server opvn Radius authenticationWindows Server 2022 with IAS serviceWindows 10 Client with OpenVPN GUI v11.49.0.0One day, after upgrade to 7.15.3 the VPN connections no longer work message on Windows client OpenVPN GUI : 'Incorrect credentials' in Log : '....AUTH_FAILED....'The Windows NPS Server log says client authorized.Mikrotik Radius Server Status says :Requests : 1Accept : 1Timeout : 4 !!Bad replies : 10 !!All other items : 0Downgrade step by step from 7.15.3 to 7.14.3 and OpenVPN connections work again.Mikrotik Radius Server Status says :Requests : 2Accept : 2Timeout : 0Bad replies : 0All other items : 0Where is the problem?Thanks in advance.In the meantime, I'm not doing any more upgrades !! ---

## Response 11
Just as an update, I can confirm this regression is still present in RouterOS 7.17-beta4.Iopened a support ticketas well, which has received no activity. ---

## Response 12
Me too stumbled on it.Radius server reporting that it sent Access-Challenge
```
Debug: (0) Sent Access-Challenge Id 36 from 0.0.0.0:2083 to 172.18.0.1:63258 length 80
Debug: (0)   EAP-Message = 0x010200160410e403eeccdc5ea411ed46ab4e4735f02b
Debug: (0)   Message-Authenticator = 0x00000000000000000000000000000000
Debug: (0)   State = 0x895b9ee189599ab998a29c329d297855Router OS in logs saying that connection aborted by timeoutrequire-message-auth = no' - not helpingAlso logs confusing they saying that radsec request going to 8968 portPlease fix it.

---
```

## Response 13
I too dropped in a case on this (still waiting to hear back 2 weeks later).On Freeradius side, I see the first access-callenge go unanswered:
```
radiusd:60366:1736548197.362852:Fri Jan 10 14:29:57 2025: Fri Jan 10 14:29:57 2025 : Debug: (6) Sent Access-Challenge Id 16 from 0.0.0.0:2083 to 172.18.96.1:49559 length 64
radiusd:60366:1736548197.362875:Fri Jan 10 14:29:57 2025: Fri Jan 10 14:29:57 2025 : Debug: (6)   EAP-Message = 0x010200061920
radiusd:60366:1736548197.362897:Fri Jan 10 14:29:57 2025: Fri Jan 10 14:29:57 2025 : Debug: (6)   Message-Authenticator = 0x00000000000000000000000000000000
radiusd:60366:1736548197.362920:Fri Jan 10 14:29:57 2025: Fri Jan 10 14:29:57 2025 : Debug: (6)   State = 0x05b269d605b070e56f176b1c6a5cb5cbAfter configured timeout is reached on Mikrotik side, the eapol session terminates due to timeout.If I test with Cisco/Meraki/Ubiquiti/Ruckus radsec works with existing freeradius config without issues as expected.  I also did confirm reverting to 7.14 radsec seems to work again.Toggling the require-message-auth configuration has no effect.

---
```

## Response 14
Trouble with RADIUS in Mikrotik using TekRADIUS.My configuration has been working well for over a decade, but upgrading beyond 7.14.3 breaks the implementation.A RADIUS reply that simply provides authorization works... However, RADIUS replies that have a FRAMED-IP-ADDRESS or a ROUTE attached to the username, fails against the server. I've selected "Require Message Auth: NO" - and it does not solve the matter. Unfortunately, I was unable to obtain any wireshark captures as this was on a production network and I had to revert to 7.14.3. I have tried 7.15 and 7.16.2 - I've avoided 7.17 as I had some trouble with winbox with this release.Has anyone had any luck in resolving? ---