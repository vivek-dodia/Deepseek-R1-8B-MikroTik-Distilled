# Thread Information
Title: Thread-208274
Section: RouterOS
Thread ID: 208274

# Discussion

## Initial Question
Hi everyone, I have a routerboard that works as a dhcp client on a Vodafone FWA connection.I have a Vodafone ZTE CPE configured in bridge mode on which it is only possible to configure the APN and the VLAN on which dhcp client is exposed. Everything works, the rb is issued a dynamic public IP with a 30 minute lease.The strange thing is that every 15 minutes, I get a NAK from the DHCP server losing connection for 1-2 seconds. Then it works again with the same IP. the IP changes only if the CPE is restarted. From the logs I read this message:
```
dhcp-client on vlan1038 lost IP address 1.2.3.209 - received NAK from dhcp server 1.2.3.210What could this depend on? I don't think there are any useful options in the DHCP client to solve the problem

---
```

## Response 1
Same issue here, same connection (Vodafone FWA)I am currently obtaining IP Address and Route through DHCP Client, then disabling it for 1038 VLAN and establishing a static address and a static route until IP changes, then disabling both static address and route and re-enabling DHCP client when it happens.I am wondering if there is a better solution through DHCP options as you are asking for. ---

## Response 2
is analyzing the situation thoroughly. it seems that provisioning on the CPE's tr069 occurs exactly every 15 minutes (900 seconds). Could that be causing this problem? ---

## Response 3
same issue on 5G network "3 AT" with a ZTE MC801A in bridge modeevery once in a while i receive a NAK from the WAN side (the ether1 which is connected to the ZTE 5G modem in bridge mode)172.16.88.1 is the local IP of the ZTE device (my MT has 172.16.88.2/26 on ether1-WAN additionally for management and webGUI access)lease time is 4h given out by DHCP but never reaches zero.i also saw NAK messages when i manually clicked on "renew" in dhcp-client. no idea what is causing thatbut what happens is, that short interrupts occur when this happensannoyingScreenshot From 2025-01-29 11-19-58.png ---

## Response 4
It's perfectly normal for DHCP client to try to renew DHCP lease after half of lifetime expires. When doing it, DHCP client offers to renew lease with its current IP address. Normally DHCP server ACKs that and thing is done for another half of lease lifetime.DHCP server may decide to NAK client's "offer" ... in which case DHCP client has to assume that it's lease is canceled and has to perform whole "new lease" procedure from scratch. And during that time (a few seconds) it doesn't have a valid DHCP lease and hence no IP address.What is not normal is that DHCP server NAKs client's "offer" ... and then, after following full "new lease" procedure, sends DHCP lease with same IP address.The only excuse might be if client's DHCP-ID (which most of times more or less resembles client's MAC address) changes since obtaining old DHCP lease ... which might make DHCP server believe it's a completely new DHCP client trying to obtain somebody else's lease.If you can, try to check state of leases on ZTE modem ... OTOH I wouldn't be too surprised if ZTE's DHCP server has some kinks on its own. ---

## Response 5
thx @mkxi know how dhcp works and a renew may occur half of max-lease-time.here it is not the case. given lease is valid for 4h but still there are NAKs way before lease-time ever reaches, for say, 2h left.if there is a release or just a renew, normally it works totally fine.the problem additionally is, it is not consistently reproduceable.unfortunately i do not have any control of the dhcp service of the bridged ZTE 5G modem-router.i wonder if there is a way to filter out those packets unless a renew is triggered from the mikrotik ---

## Response 6
Re blocking: since DHCP is typically done inside L2 broadcast domain, DHCP handshake doesn't go past routers. Which generally means that any DHCP handshake with ZTE thingy will generally originate from router itself (and not from some devices, connected to router's LAN segment). Unless you have all ports in bridge in which case ZTE may hear DHCP requests.But anyway, your logs screenshot already proves that it's about router doing DHCP handshake with ZTE. So you can't do much about it. You can try to sniff DHCP traffic on WAN port to get actual contents, exchanged between MT and ZTE, to see if there's anything that MT does incorrectly. But my gut feeling is that ZTE is the misbehaving device. ---

## Response 7
it is surely the ZTE which does not behave correctlyWAN port is not in a bridge. of course not (;i'll see what i could do about it.currently i changed the bridge-mode of the ZTE MC801A back to NAT, deactivated dhcp completely there and assigned a static IP. on the wan port of the MT it is 172.16.88.2/26 with a def. route " 0.0.0.0/0 via 172.16.88.1".works for now until i have mote time to look into (unless FTTH will be available in the next few days, which i higly doubt xD )additionally i defined 172.16.88.2 (MT) as DMZ host in the ZTE config.as said, works for now, but with the caveat of a double NAT (which does not affect me much, not having anything voip/sip related in this setup)i see no NAKs any longer this waybut as always, thanks for all the input ---