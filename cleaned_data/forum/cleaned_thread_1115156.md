# Thread Information
Title: Thread-1115156
Section: RouterOS
Thread ID: 1115156

# Discussion

## Initial Question
1.When I bind 5 IPs to the WAN network card through IP/Addresses, such as 172.16.1.10 to 13 and30add address=172.16.1.10/24 interface=combo1-wan network=172.16.1.0add address=172.16.1.11/24 interface=combo1-wan network=172.16.1.0add address=172.16.1.12/24 interface=combo1-wan network=172.16.1.0add address=172.16.1.13/24 interface=combo1-wan network=172.16.1.0add address=172.16.1.30/24 interface=combo1-wan network=172.16.1.02.Then I configured a remote syslog server and set the remote option in the logging action in RouterOS. I want the source IP of the logs being sent to be 172.16.1.30./system logging actionset 3 remote=172.17.1.80 src-address=172.16.1.30However, I found that RouterOS sends the logs using the first IP (172.16.1.10), even though I specified the source IP.I tried disabling the first IP (172.16.1.10), and RouterOS then sent the logs using the next IP (172.16.1.11). How can this issue be resolved?It seems that RouterOS uses the smallest IP address as the source IP by default. ---

## Response 1
The fact that logging has the option of a source IP address, and ignores it seems like a bug.Though it might be your config. (Given Wan interfaces usually have some sort of src-nat/masquerade)Do you have a src-nat rule for the wan interface that might apply in this case.You could put in a specific src-nat rule, for this traffic to use the .30 IP address.Or perhaps a src-nat accept rule when the source address is already any one of your wan interface IP addresses.Above any existing existing src-nat rules ---

## Response 2
I also think this is a bug. Do you have an example of the method you mentioned that I can refer to? ---

## Response 3
Only as a side-side note, I believe this is how RoS works more generally.An interface with multiple IP addresses is seen by its "lowest" IP address.I have a Mikrotik (hap Ax Lite) used as an "intermediate" router used for failover between two ISP modem/routers, for some reasons both these routers have address 192.168.1.1 (unchangeable) and I set a vrf so that also the LAN port (ether4) is 192.168.1.1.When I did from a lan device (which is a "normal" 192.168.1.0/24) a traceroute to an IP on the internet, the first two hops were:1 192.168.1.12 192.168.1.13 ....So, I tried adding another static IP to ether4, 10.0.0.1, and the traceroute became:1 10.0.0.12 192.168.1.13 ...Also in Winbox, the Mikrotik device is now listed with IP 10.0.0.1, besides its MAC.So, it seems to me that the src-address you specify is correct (and identifies the right interface) but then the default "use lowest address" kicks in and the log uses this latter.No idea if this behaviour can be changed. ---

## Response 4
That is "source address selection", it applies to outgoing packets (originating from the router) that do not have an explicitly set source address.What the topic is about is "the logging to network ignores the specified source address, that must be a bug".But I agree with @rplant that probably it is not a bug in the logging function but a mistake in the configuration.When there is a "masquerade" rule active for the logging packets, it behaves exactly as observed.It is likely because of a too-wide scope of the masquerade rule, i.e. it erroneously applies to this traffic as well.When you have multiple addresses on a WAN interface, you likely do not want to use masquerade at all. ---

## Response 5
I think I’ve resolved the issue. After disabling the first rule, I can see that the syslog is being sent from 172.16.1.30.Thank you, everyone!/ip firewall natadd action=masquerade chain=srcnat disabled=yes log=yes out-interface-list=WANadd action=same chain=srcnat log=yes log-prefix=samerule out-interface=combo1-wan src-address=192.168.0.0/16 to-addresses=172.16.1.10-172.16.1.13 ---

## Response 6
It's possible to setpref-srcproperty on static routes, e.g.
```
/ip/routeadddst-address=0.0.0.0/0gateway=172.16.1.1pref-src=172.16.1.30Then router uses this address when making new connection using that particular route. But I don't know if the same selection applies if destination is in same IP subnet as those multiple IP addresses.

---
```