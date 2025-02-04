# Thread Information
Title: Thread-1123447
Section: RouterOS
Thread ID: 1123447

# Discussion

## Initial Question
I have noticed a strange issue with my RB5009 and CRS354. My RB5009 is connected via ether1 (1G) -> SFP1 (MikroTik S-RJ01) on CRS354. Normally the connection is stable and just works fine. Note: I cannot use SFP+ from RB5009, as I need this for my fiber ISP link, but since I only have 1G anyway, its ok.But when I do reboot the RB5009 (Either via ROS, push reset or pull the plug), the connection fails. This means, I can observe during bootup several times getting a link and after max. 1 second, the link is gone. When the RB5009 is fully powered on, the link stays down. If I pull the network cable before reset and put it after full bootup into RB5009, all works just fine. I can only reproduce this issue together with the CRS354. If I connect a different old test swich (e.g. Netgear GS750e), I don't see that issue.Any ideas, what could go wrong here? The logs are not very helpful. The only say "link up" or "link down". ---

## Response 1
When you say the issue does not show up if you connect some other switch than the CRS354, does it mean you move the S-RJ01 to that other switch or you use copper port (or another model of copper SFP) there?Does the issue show up if you use a copper port on the CRS354 instead of the S-RJ01?As it sounds like an issue with speed and duplex negotiation, how does it behave if you disable auto-negotiation at both ends of the link and set it to 1 Gbps and full duplex? ---

## Response 2
When you say the issue does not show up if you connect some other switch than the CRS354, does it mean you move the S-RJ01 to that other switch or you use copper port (or another model of copper SFP) there?It does not matter. It works either jusing copper (RJ45) directly on the other switch or by using MikroTik S-RJ01 (the same used on CRS354)Does the issue show up if you use a copper port on the CRS354 instead of the S-RJ01?I will try and report back.As it sounds like an issue with speed and duplex negotiation, how does it behave if you disable auto-negotiation at both ends of the link and set it to 1 Gbps and full duplex?I will give a try and set fixed mode for test. ---

## Response 3
Does the issue show up if you use a copper port on the CRS354 instead of the S-RJ01?Yes, it does.As it sounds like an issue with speed and duplex negotiation, how does it behave if you disable auto-negotiation at both ends of the link and set it to 1 Gbps and full duplex?Setting 1g fixed full doesn't change anything ---