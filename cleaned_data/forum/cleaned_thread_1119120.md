# Thread Information
Title: Thread-1119120
Section: RouterOS
Thread ID: 1119120

# Discussion

## Initial Question
I am trying to setup a traffic generator and have a Router as a default gateway for the mikrotik device.The mikrotik device can ping the router ip address without any issues.However, when I am trying to initiate the traffic generator I am not seeing any traffic hitting the router as seen in the packet capture session for the udp traffic. the session pcaps show icmp for the pings.Is there anything that needs to be done to fix this?Any advise will be much appreciated ---

## Response 1
Is there any help I can get on this please?Let me know if you need any further information from me? ---

## Response 2
If you're running 7.17rc, you need to enable the traffic generator in /system/device-mode (see 7.17 thread here, or docs).Otherwise, it's possible you're not generating a valid packet that be dropped before your router sees it. Do you see it on the Mikrotik touch or sniffer locally? ---

## Response 3
This is a HexS device and the version I am running on is 6.49.10.the HexS is connected to a Juniper SSR Router which can see the pings but when we start the traffic generator we cannot see it reaching the Juniper . when we do a ping we can see it on the sessions.This is really strange and I cannot understand why I am not seeing the traffic. ---

## Response 4
If you create a pcap with your ping from the router using sniffer, and they use that same pcap in traffic generator does it work?IDK why the Juniper might not see it. But again if something generated is malformed, perhaps it drops it. Or, if IP/arp was wrong, then generated traffic might not be going to the Juniper based on RouterOS routing decisions, too. The only way to know is using sniffer on the RouterOS outbound side to confirm it going out and/or using wireshark on PC instead of Juniper to see if what's coming out. ---

## Response 5
Thanks a lot for your response. I do seem to be getting the sessions getting through now but it does not show the jitter stats etc.. ---