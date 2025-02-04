# Thread Information
Title: Thread-1116409
Section: RouterOS
Thread ID: 1116409

# Discussion

## Initial Question
I have already created a support ticket about this (SUP-134914) but since that's on "waiting for support" since November and the issue is still troubling me, I'll copy it here with the hope that someone might know a workaround. My issue is this:Normally, outgoing packets use the global address, like these ping packets for example:2023-12-29-03-03-15-winbox64.pngBut this isn't the case for the ("outer") packets of an IPIPv6 tunnel. They use the link-local address of the outgoing interface:2023-12-29-03-04-35-chrome.pngThe tunnel won't work like this because the packets are not routed through the internet (and if they were the destination would not accept them).This can be reproduced (with a caveat) by setting up a tunnel, sending data through it (ping 192.168.99.2) and watching the packets in the sniffer:
```
/interfaceipipv6addname=test!keepalive remote-address=2001:4860:4860::8888/ip addressaddaddress=192.168.99.1/24interface=test network=192.168.99.0/tool sniffersetfilter-ipv6-address=2001:4860:4860::8888/128There seems to be a random component to this! Sometimes it will use the global address and sometimes the link-local address. When it is using the global address it will usually switch to the link-local address after a couple of days.

---
```

## Response 1
Setting local address seems as obvious choice for workaround. As simple as possible if it's static, a bit more annoying if not, but should be doable. ---

## Response 2
Oh, sorry, I forgot to mention, setting "local address" of the IPIPv6 tunnel to the global IPv6 address of the interface has no effect. ---

## Response 3
If it's ROSv7, you can also try NAT. ---

## Response 4
I have seen this issue (long) ago and reported it.In my case the IPv6 address is obtained from a PPPoE connection via IPv6 DHCP client, put in a pool, and then assigned to an interface.This of course takes time after a router boot, and the IPv6 tunnel comes up before that, the globally routed IPv6 address is not yet present at that time, and the local address is used instead. That does not change after the global address becomes available.However, it seems that this has been fixed at some point in time. What RouterOS version are you running? ---

## Response 5
If it's ROSv7, you can also try NAT.I did try to use NAT to change the outgoing address but either because I did it wrong or because those tunnel clients are not affected by NAT it didn't work. If you're positive that it should work I'll try again.In my case the IPv6 address is obtained from a PPPoE connection via IPv6 DHCP client, put in a pool, and then assigned to an interface.In my case as well. There's no PPPoE involved but the IP/prefix also comes from an DHCPv6 client.It would explain why newly created tunnels usually start out with the correct IP but it doesn't explain why they revert to link-local after a couple of days.Edit: Just deleted the broken tunnel and created a new tunnel again and it still uses the link-local address, even though the DHCPv6 client is bound and the global IPv6 address is working.However, it seems that this has been fixed at some point in time. What RouterOS version are you running?7.13rc2 ---

## Response 6
If it's ROSv7, you can also try NAT.So I tried it again. I added this rule:
```
/ipv6 firewall nataddaction=src-nat chain=srcnat dst-address=2001:4860:4860::8888/128out-interface=ether5-WAN src-address=fe80::de2c:6eff:fe17:93b3/128to-address=2a02:908:1400:1::1597/128And even though the rule seems to be hit (the packet counter goes up) the outgoing source address I see in the sniffer does not change and the tunnel doesn't work.

---
```

## Response 7
Did your router originally run version 6 and was it upgraded in-place to v7?In that case it may be worth a try to export the configuration, download the file, then use netinstall to re-install the v7 version you want, no defaults, and then re-import the configuration. Do not use backup/restore but export/import (or paste).(or when it is not too complicated, just reset to defaults and only cut/paste the locally added parts like that tunnel)In some cases after upgrade inexplicable things can happen that can be fixed this way. ---

## Response 8
Well, NAT does work (= is able to change source of tunnel's packets), but not exactly as expected.I can force tunnel to use link-local address as source, if I keep default route (with link-local gateway) and disable all global addresses. I assume something like that might be happening on your router, if you have dynamic config. Perhaps for a brief moment when it's renewed, there's route but not global address and tunnel has no choice and has to switch to link-local source. When global address becomes available again, sometimes tunnel switches to it right away and sometimes it takes a while (half a minute or so).And then there's NAT. The rule sees packets. In fact, it sees every single one (so it understands them as new "connections"), but doesn't do anything as long as there's original connection tracking entry with public addresses. Only when it times out (after 10 minutes) or I remove it manually, it kicks in and works as it should, i.e. changes link-local source to configured public address (and it creates new connection tracking entry with link-local source, as expected). Trouble is, when this new connection tracking entry exists, then even if public address became available and tunnel uses it as source (I'm logging packets in output), it somehow blocks the tunnel, no packets are sent from router. But then again, 10 minutes, the entry expires and everything is fine again.It's not exactly same as your problem, but something weird is definitely happening there. ---

## Response 9
FWIW, on my routers where I have 7.12.1 running I do not see a problem with GRE6 tunnels.I expect the situation will be the same with IPIP6 tunnels, but of course one can never be sure. ---

## Response 10
same issue on 6.49.17 with eoipv6 ---