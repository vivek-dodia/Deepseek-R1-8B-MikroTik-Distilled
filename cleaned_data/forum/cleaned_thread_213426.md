# Thread Information
Title: Thread-213426
Section: RouterOS
Thread ID: 213426

# Discussion

## Initial Question
I have a user that will use a residential StarLink on location, and that thing is behind a CGNAT.How to punch through to make a WireGuard work for remote access / admin? ---

## Response 1
BTH function is done exactly for such cases. ---

## Response 2
Thank you very much! ---

## Response 3
But don't do it in prod.It's only for HO. ---

## Response 4
But don't do it in prod.It's only for HO.Why? It is WireGuard, with specific client in. Should be quite safe. Or? What am I missing?(I have done some tests today, but nothing much. Didn't work out of the box, need some tweaking.) ---

## Response 5
It's working today, but maybe not tomorrow.Take a look at this answer from MikrotikOwnSupport Technician.viewtopic.php?p=1114268#p1114268 ---

## Response 6
A bit over the top, but it should not be used as a business entity as on occasion, not very frequently the Mikrotik servers have gone offline. A couple of times a year is probably a safe bet.Nothing for you to worry about unless your a hospital, a bank or any business requiring 24/7 VPN up time.If that is concern then rent a server in the cloud, for like $7 a month and put a CHR on it and use that as the wireguard server. ---

## Response 7
A bit over the top, but it should not be used as a business entity as on occasion, not very frequently the Mikrotik servers have gone offline. A couple of times a year is probably a safe bet.Exactly my point. If a client is not willing to shelve out for a business connection with an fixed IP, then I don't really see them willing to finance a CHR instance configuration and maintenance.Nothing for you to worry about unless your a hospital, a bank or any business requiring 24/7 VPN up time.If that is concern then rent a server in the cloud, for like $7 a month and put a CHR on it and use that as the wireguard server.As on the price of the cloud server - the issue is not a few bucks needed to make it work, but time to do so. All these costs need to be passed onto the client, and it adds up. It is simply more cost effective to have a business class internet access.Also, 24/7 is overrated for most use cases.(Also, I haven't forgot about that EAP I promised you, but I have so much work to do that I couldn't yet muster time to do a write up.) ---

## Response 8
Why is CHR necessary just for Wireguard peer? It can be setup on Linux running on cloud server and save some money for CHR licence. Once setup on Linux is created, image can be made of it for reuse.Initially some time will be spent to create setup, but later it should be more faster and charge moreknow-howthan spent time and profit from such clients. ---

## Response 9
So we must clarify what business use means. If the BTH is used for occasional management access for a support company, then support intervention is not possible if the BTH infrastructure is unavailable. That's definitely unpleasant but it is not the same like if BTH was hypothetically used to provide service for end customers, because support interventions are only required at random times and the BTH infrastructure becomes unavailable at other random times, so the probability that these two events coincide is not that high.But looking at it from the other side, if I provide support, it should not be a big deal for me to have a public (or global) IP address and let these customers actively connect to it so that I could reach their router for support interventions? ---

## Response 10
Concur with Sindy, if you are providing a paid service, then having your own cloud wireguard to support all your clients ( shared cost ), is the smart way to go. ---

## Response 11
Just to chip in a send a christmass thumbs up to anav and sindy.All the best guys. ---

## Response 12
All the best to you and your loved ones in 2025 there AtomD. ---

## Response 13
Why is CHR necessary just for Wireguard peer? It can be setup on Linux running on cloud server and save some money for CHR licence. Once setup on Linux is created, image can be made of it for reuse.Initially some time will be spent to create setup, but later it should be more faster and charge moreknow-howthan spent time and profit from such clients.This is a mikrotik forum, and I have no clue how to use linux LOL. ---

## Response 14
why don't you use IPv6? router should be reachable. ---

## Response 15
why don't you use IPv6? router should be reachable.Interesting proposition. But I think that local providers still use IPv4 here. Not sure about StarLink?Would check, as this actually could be useful in practice. ---

## Response 16
Starlink indeed gives you a/56 global subnet, but only in "bypass" mode (or how do they call the bridge mode of their router), or if you connect your own router directly to the dishy, bypassing their router that way. So along with a Hurricane Electric tunnel that allows you to get a global subnet using your IPv4-only uplink, this is the budget way to get there. ---

## Response 17
Starlink indeed gives you a/56 global subnet, but only in "bypass" mode (or how do they call the bridge mode of their router), or if you connect your own router directly to the dishy, bypassing their router that way. So along with a Hurricane Electric tunnel that allows you to get a global subnet using your IPv4-only uplink, this is the budget way to get there.We have end-user starlink terminal, the configuration options are more or less devoid of any options. Currently I have enabled BTH option and that one works flawlessly. However, I haven't yer configured firewall properly, so there is that... Configured BTH on site 2 days ago. I was surprised how easy it was... Probably the easiest setup for anything Mikrotik ever.As for StarLink, I presume bypass works only for business models, or?As for the antenna, it draws a lot of power. From what I understand the ethernet cable they provide is out of standard, as is power delivery, as it needs to supply up to 100W+ to the antenna itself? Meaning I can't really bypass the SL router itself. ---

## Response 18
As for StarLink, I presume bypass works only for business models, or?It works also for the consumer grade service.As for the antenna, it draws a lot of power. From what I understand the ethernet cable they provide is out of standard, as is power delivery, as it needs to supply up to 100W+ to the antenna itself? Meaning I can't really bypass the SL router itself.3rd party solutions are available that allow to exclude the indoor router from the scheme completely and provide the non-standard power supply via the non-standard connector to the dish and the data lines on a standard RJ-45 socket. But the "bypass mode" is actually a setting of the "router" which then becomes a bridge (for some models, you need a separate Ethernet adaptor, for others the router has the Ethernet port directly). ---

## Response 19
This was most informative. - Their "Bypass mode" is a bit a bit convoluted tho. Do I understand correctly that when I enable bypass mode, what happens is that the router itself is in bridge mode and "dead", but I will still get a DHCP ip from the antenna itself? It is like both antenna and router kind of redundant? The rotuer then just feeds the antenna and uses as an internal interface. ---

## Response 20
Indeed. Using DHCP, the antenna always hands out an IPv4 address from the 100.64.0.0/10 range and a /56 global prefix. If the router is active, it only requests an IPv4 address from the antenna, and only hands out IPv4 addresses from 192.168.1.0/24 on its LAN side; if it is set to bypass mode, it acts as a PoE switch only. To the extent that there is no way to configure it locally or over the air and to switch the bridge mode off, you have to use a "magic" sequence of power disconnects. ---

## Response 21
Thanks. Given I already have WAN port set and and enabled DHCP on it that connects to router, would it actually make any real world benefit for using bypass mode, apart from WiFi being turned off? I mean, I am pretty sure the router is quite powerful. Given that consumer router is behind cgnat and that I have BTH set and works not sure if it makes any sense (I am annoyed by 80mhz wifi tho, it eats up channels). How and do the firmware updates work for antenna router after bypass? ---

## Response 22
would it actually make any real world benefit for using bypass modeUnless you consider availability of IPv6 a real world benefit (it makes you independent on wthe BTH ifrastructure), and unless you suffer from the double-NAT-phobia, it wouldn't.How and do the firmware updates work for antenna router after bypass?They do - Starlink does have over-the-air access to the antenna even if the indoor router is not part of the setup. ---

## Response 23
Thanks.I currently work with IPv6 disabled, as it seems too much work to worry about that too. But I might enable bypass out of curiosity...Over the air access to antennas is the smart thing, but I have to admit that I was surprised to learn that the antenna itself was a standalone device. ---

## Response 24
Just a quick update - I enabled Bypass mode on Starlink and everything works as it should. The antenna is really standalone device - the router is just a power box and a filter. The only issue with this setup is the inability to set subnet. You get what you get (in common 192.168.x.x range), so the LAN behind it should adapt. There is little change yours will coincide, but still... On Router itself you can actually choose between several subnets (4-5 if I am not mistaken, in different ranges).My reason to do this was turning off the 80 MHz StarLink WiFi, not to interfere with my APs, and to prolong the life of the device itself.As for StarLink stability itself, I must say I am really impressed. I sometimes got over 400 mbps in dl, and routinely get 15-25 in upload.In any case, thank you for the tip! It really hepled!Here is an image of supercat: ---

## Response 25
You get what you get (in common 192.168.x.x range)That is a surprise for me - my experience so far was that in bypass mode, you get a single address from 100.64.0.0/10 with gateway 100.64.0.1, and it is up to you how you organize your LAN. And also when not in bypass mode, the bundled router was giving out addresses from 192.168.1.0/24 alone, no way to choose from multiple subnets. Something must have changed since I've checked the behavior last time. ---

## Response 26
You get what you get (in common 192.168.x.x range)That is a surprise for me - my experience so far was that in bypass mode, you get a single address from 100.64.0.0/10 with gateway 100.64.0.1, and it is up to you how you organize your LAN. And also when not in bypass mode, the bundled router was giving out addresses from 192.168.1.0/24 alone, no way to choose from multiple subnets. Something must have changed since I've checked the behavior last time.I have to correct myself. I just checked, and I remembered wrong - the IP I got from the antenna is 10.77.123.x. The gateway is on 10.64.0.1.As for the Router itself, I did indeed give me 192.168.something IP, but I changed that to 10.x.x.x range. I had several options to choose from in a dropdown menu, but no manual setting. The interface is really simple and in general I like it. The WiFi is also stable and strong. The setting is not obvious, but leaving the default subnet on 192 range is always a bad idea, because when the people VPN into the LAN there could be all sorts of problems if they have the same IP. I unfortunately found that out the hard way when I took over one old/ish LAN. ---