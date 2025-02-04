# Thread Information
Title: Thread-1123077
Section: RouterOS
Thread ID: 1123077

# Discussion

## Initial Question
Im getting weird MTU errors on my BT PPPoE connection seems to have started when upgraded to 7.17the full message is:
```
invalid mtu1500on BTfromfe80::7270:8bff:fe2c:a500whats interesting thats not the set MTU nor is it the MRU.. so I have tried to drop to the MTU 1480 from 1492 and even the expected MRU from auto to both with no change is this just a bug?I don't seem to have any issues with connectivity or thoughput just the log being spammed with these messages.

---
```

## Response 1
From what I was able to understand of the situation, I guess it could be that the ICMPv6 Router Advertisement from your ISP has the option 5 (MTU) set to 1500 while your PPPoE Client has an MTU (L3) of 1492 bytes (either by default or configured by you). Thus, your MikroTik router is unable to use the MTU value advertised by your ISP over IPv6 because the MTU of the PPPoE tunnel is smaller than that.IF (big IF) something like that is happening, you can check if your modem/ONT/GPON/whatever bridge supports an MTU (L3) greater than 1500 and allows you to make use of "Baby Jumbo Frames" on your PPPoE connection. For that, configure your PPPoE Client with MTU and MRU equal to 1500 bytes and the parent ethernet interface of the PPPoE Client to have an MTU (L3) greater or equal to 1508 bytes and an L2 MTU greater than or equal to 1512 bytes (just to be safe - if you don't perform VLAN tagging on your WAN interface, an L2 MTU greater than or equal to 1508 bytes should work fine). ---

## Response 2
After disabling IPv6 completely (I dont need it for my internal or wan network) the problem went away.What I find interesting is that there are no of disabling IPv6 on PPPoE interfaces from the seems of it even though there is no address given it was still recieving this error.thank you for your help yuripg1 ---

## Response 3
What I find interesting is that there are no of disabling IPv6 on PPPoE interfaces from the seems of it even though there is no address given it was still recieving this error.I think you need a PPP profile with "use-ipv6=no" to not have any IPv6 on your PPPoE interface. The default PPP profiles have it set to "yes". But I have never disabled IPv6 to be 100% sure of this, though.If you look at the Linux kernel, it has a "disable_ipv6" setting applied to each specific interface and then values for "all" and "default" that determine the setting for all currently existing interfaces and newly created ones, respectively.On RouterOS side, I see that MikroTik has 2 main settings regarding this:The first one is the "disable-ipv6" under "/ipv6 settings". To me, it seems like this ends up configuring the kernel setting "disable_ipv6" for the "all", "default" or all interfaces one by one.Then we have the "use-ipv6" under "/ppp profile". That I guess ends up configuring the same kernel setting "disable_iv6" only for the specific interfaces that have this PPP profile applied to them one by one. ---

## Response 4
... and the parent ethernet interface of the PPPoE Client to have an MTU (L3) greater or equal to 1508 bytes...This is not needed. The MTU of the parent ethernet interface is not relevant (can stay at the default value of 1500), only L2MTU must be big enough. However, there is another part that wrongly uses the parent's interface MTU value, and that's theChange TCP MSSsetting. With this setting enabled, the IPv4 TCP MSS will be wrongly capped at 1452 instead of the correct value of 1460 (for MTU 1500), unless you increase the parent ethernet interface's MTU to 1508. Just make a separate PPP profile with the setting turned off and use the profile for the pppoe-out connection and the ethernet MTU will be irrelevant. ---