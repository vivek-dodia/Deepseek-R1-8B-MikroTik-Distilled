# Thread Information
Title: Thread-213696
Section: RouterOS
Thread ID: 213696

# Discussion

## Initial Question
Hello, I have a strange behavior with my hotspot login.Some users (I think only windows) login with mac cookie before getting correct ip from dhcp server.Hotspot config have none in pools (users and server profiles).Arp hotpot interface is reply only. And arp is added from dhcp server.1 simultaneous mac is allowed.Here is the log07:24:56 hotspot, info, debug d5mqzxf6 (169.254.143.229): trying to log in by mac-cookie07:24:56 hotspot, info, debug d5mqzxf6 (169.254.143.229): login failed: simultaneous session limit reached07:25:04 dhcp, info dhcp1 assigned 192.168.18.56 to XX:XX:XX:XX:XX:XX07:25:16 hotspot, info, debug d5mqzxf6 (192.168.18.30): trying to log in by https07:25:18 hotspot, info, debug d5mqzxf6 (192.168.18.30): login failed: simultaneous session limit reached07:25:36 hotspot, info, debug d5mqzxf6 (192.168.18.30): trying to log in by https07:25:38 hotspot, info, debug d5mqzxf6 (192.168.18.30): login failed: simultaneous session limit reached07:25:55 hotspot, info, debug d5mqzxf6 (169.254.105.118): logged out: keepalive timeout07:26:04 hotspot, info, debug d5mqzxf6 (192.168.18.30): trying to log in by https07:26:05 hotspot, account, info, debug d5mqzxf6 (192.168.18.30): logged inAfter idle timeout session with wrong ip is deleted and user can login.Weird behavior..I tried block 169.254.0.0/16 in hotspot ip binding but no success.Not sure if it's a new thing with windows users. didn't remember to have already see that with my actual settings.run out of ideas now ---

## Response 1
https://en.wikipedia.org/wiki/Link-local_addressprobably the pool in dhcp has run out and windows connects with link-local addresses ---

## Response 2
No there is plenty of free ip in the pool.In the log I can see that it connect with wrong IP then it start dhcp dialog and just after it obtain the correct IP address.I try to block 169.254.0.0/16 in the raw firewall. i'll see next time. ---

## Response 3
sorry my capture log was not good.this one is more clear :08:31:51 hotspot, info, debug d5oy3ace (169.254.14.91): trying to log in by mac-cookie08:31:51 hotspot, account, info, debug d5oy3ace (169.254.14.91): logged in08:31:59 dhcp, info dhcp1 assigned 192.168.17.132 to XX:XX:XX:XX:XX:XX08:33:51 hotspot, info, debug d5oy3ace (192.168.17.132): trying to log in by https08:33:53 hotspot, info, debug d5oy3ace (192.168.17.132): login failed: simultaneous session limit reached08:33:55 hotspot, info, debug d5oy3ace (192.168.17.132): trying to log in by https08:33:57 hotspot, info, debug d5oy3ace (192.168.17.132): login failed: invalid password08:33:58 hotspot, info, debug d5oy3ace (169.254.14.91): logged out: keepalive timeout08:35:05 hotspot, info, debug d5oy3ace (192.168.17.132): trying to log in by https08:35:05 hotspot, account, info, debug d5oy3ace (192.168.17.132): logged inOnce user connected it didn't cause trouble for the day.Stange that it can use 169.254 ip address with pool set to none in hotspot conf. ---

## Response 4
You have a hotspot limit of one session per user.Blocking the 169.254.0.0/16 in raw will solve this problem......repair dhcp, it will be easier.---08:31:51 hotspot, account, info, debug d5oy3ace (169.254.14.91): logged in08:33:53 hotspot, info, debug d5oy3ace (192.168.17.132): login failed: simultaneoussession limitreached ---

## Response 5
Thanks. I'll wee how it goes with firewall raw.And Yes it's needed in my case one hotspot login per one equipement. Specific setup. ---

## Response 6
Firewall blocking didn't solve it06:03:52 hotspot, account, info, debug d5m957z8 (169.254.52.91): logged in06:03:52 firewall, info prerouting: in:ether …06:03:54 dhcp, info dhcp1 assigned 192.168.18.153 to XX:XX:XX:XX:XX:XX06:05:55 hotspot, info, debug d5m957z8 (169.254.52.91): logged out: keepalive timeoutuser login by mac cookie before anythingNot critical but annoying. ---

## Response 7
It seemingly shaved some little time off, however.Before it was08:31.51->08:33:58=2 minutes 7 secondsand now is:06:03:52->06:05:55=2 minutes 3 secondsCan the keepalive timeout be reduced? ---

## Response 8
Keep alive time out is 2m. Didn't changed it.May be if I lower it it'll cause some new problems. So not sure. ---

## Response 9
I'm thinking at what changed since last time in this setup.I have proxy arp enabled on my wifi APs but I have it since few years.This time I activated some acl rules on my Cambium APs to clean the air.To prevent un-authorized rogue DHCP server from the wireless clients.Unwanted DHCP client packets from wired network side.Drop L2 broadcast packets.Drop multicast packets.Drop ARP discovery packets from one SSID to another SSID interface.And drop mdns , and IPv6 trafic.Not sure why only some windows stations are affected the first time the log in the day. ---

## Response 10
I think I'll let run like that and debug when back in the lab. ---

## Response 11
Semi-random idea, would setting ip-binding to something like:/ ip hotspot ip-bindingadd address=169.254.1.0-169.254.254.255 type=blockedeffectively prevent the APIPA addresses from logging in (via mac-cookie)? ---

## Response 12
yes already tried that firstly but it still connect by mac cookie. very stange ---

## Response 13
maybe my mistake for the IP binding.For the range I used address and to-address and not address=169.254.1.0-169.254.254.255....So I try that ---

## Response 14
didn't RTFM...sorry ---

## Response 15
So, is it working with the correct range settings?I wasn't at all sure whether the mac-cookie login runs "before" the ip-binding block and thus by-passes it.. ---

## Response 16
I'll have to let it run some time to confirm it's ok.didn't see the message again for now. ---

## Response 17
I can confirm it works with blocking IP bindings.No more "simultaneous session limit" messages related to 169.254.x.x login with mac cookie.Thanks ---

## Response 18
Good.Though the "fault" is most probably in the client that attempts to login before having a "proper" DHCP address (or wait for a timeout), it is good to know that RouterOS can deal with that. ---