# Thread Information
Title: Thread-1119654
Section: RouterOS
Thread ID: 1119654

# Discussion

## Initial Question
Mikrotik goes online via lte1. lte1 ip looks like 10.92.201.134 but actually the real ip is 176.89.208.201.I need to add the real ip to the address list to do ipsec with the center.It also checks the constantly changing public ip address with a script and corrects it automatically.It works as long as the public ip address is not changed by the ISP. But as soon as the ISP changes the public ip, mikrotik cannot go to the internet. I have to manually disable and re-enable pubaddr in the address list otherwise I can't go online.Do you have a suggestion for a solution?
```
/interfacebridgeaddname=bridgeaddname="bridge guest"/interfacelteset[finddefault-name=lte1]allow-roaming=noband=""sms-protocol=auto\
    sms-read=no/interfacevlanaddinterface=ether5 name=vlan13 vlan-id=13/interfacelistaddname=WANaddname=LAN/interfacelte apnset[finddefault=yes]add-default-route=nouse-network-apn=no\use-peer-dns=noaddadd-default-route=noapn=superboxuse-peer-dns=no/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTikaddauthentication-types=wpa2-psk mode=dynamic-keys name="Sec Profile"\
    supplicant-identity=""addauthentication-types=wpa2-psk mode=dynamic-keys name=otu \
    supplicant-identity=""/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5adddh-group=modp2048 dpd-interval=2mdpd-maximum-failures=5enc-algorithm=\
    aes-256hash-algorithm=sha256 lifetime=8hname=ike_crypto nat-traversal=\no/ip ipsec peeraddaddress=111.111.111.111/32disabled=yes exchange-mode=ike2local-address=\176.238.169.228name=peer profile=ike_crypto/ip ipsec proposaladdenc-algorithms=aes-256-cbc lifetime=1hname=ipsec_crypto pfs-group=\
    modp2048/ip pooladdcomment=10.5name=pool_lan ranges=10.10.5.20-10.10.5.200addcomment=10.5name=pool_misafir ranges=10.11.5.20-10.11.5.200/ip dhcp-serveraddaddress-pool=pool_laninterface=bridge name=dhcpaddaddress-pool=pool_misafirinterface="bridge guest"name=dhcp_misafir/interfacebridge portaddbridge=bridgeinterface=ether2addbridge=bridgeinterface=ether3addbridge=bridgeinterface=ether4addbridge=bridgeinterface=ether5addbridge=bridgeinterface=wlan1addbridge=bridgeinterface=wlan2addbridge="bridge guest"interface=vlan13addbridge="bridge guest"interface=wlan1-vlan13addbridge="bridge guest"interface=wlan2-vlan13/ip firewall connection trackingsetudp-timeout=10s/interfacedetect-internetsetdetect-interface-list=all/interfacelist memberaddinterface=ether1 list=WANaddinterface=bridge list=LANaddinterface=lte1 list=WAN/interfacewireless access-listaddmac-address=00:19:3B:21:F9:F3/ip addressaddaddress=10.10.5.1/24interface=bridge network=10.10.5.0addaddress=10.11.5.1/24interface="bridge guest"network=10.11.5.0/ip cloudsetddns-enabled=yes/ip dhcp-clientadddisabled=yesinterface=ether1/ip dhcp-server networkaddaddress=10.10.5.0/24comment=LAN dns-server=10.10.5.1gateway=10.10.5.1addaddress=10.11.5.0/24comment=Misafirdns-server=10.11.5.1gateway=\10.11.5.1/ip dnssetallow-remote-requests=yes servers=8.8.8.8,1.1.1.1/ip firewall address-listaddaddress=10.10.5.0/24list=LANaddaddress=10.10.5.0/24list=AdminAccessaddaddress=10.11.5.0/24list=AdminAccess/ip firewall filteraddaction=accept chain=input comment=Inputconnection-state=\
    established,related,untrackedaddaction=drop chain=input comment="Input Drop Invalid"connection-state=\
    invalidaddaction=accept chain=input comment=ICMP protocol=icmpaddaction=accept chain=input comment="Router Access"src-address-list=\AdminAccessaddaction=accept chain=input comment="LAN DNS queries-TCP"connection-state=\""dst-port=53in-interface-list=LAN protocol=tcpaddaction=accept chain=input comment="LAN DNS queries-UDP"connection-state=\""dst-port=53in-interface-list=LAN protocol=udpaddaction=drop chain=input comment="Input Drop All Else"addaction=fasttrack-connection chain=forward connection-state=\
    established,related hw-offload=yes/ip firewall mangleaddaction=mark-connection chain=forward comment="Mark IPsec In"\
    ipsec-policy=in,ipsecnew-connection-mark=ipsec passthrough=yesaddaction=mark-connection chain=forward comment="Mark IPsec Out"\
    ipsec-policy=out,ipsecnew-connection-mark=ipsec passthrough=yesaddaction=change-ttl chain=preroutingin-interface-list=WANnew-ttl=\
    increment:5passthrough=yes ttl=equal:1addaction=change-ttl chain=postroutingnew-ttl=set:64out-interface-list=WAN \
    passthrough=yes/ip firewall nataddaction=accept chain=srcnat dst-address=0.0.0.0/0\
    src-address=10.10.5.0/24addaction=masquerade chain=srcnatout-interface-list=WAN/ip ipsec identityaddpeer=peer/ip ipsec policyaddaction=none disabled=yes dst-address=10.10.5.0/24src-address=\10.10.5.0/24addcomment=ipsec disabled=yes dst-address=0.0.0.0/0peer=peer proposal=\
    ipsec_crypto src-address=10.10.5.0/24tunnel=yes/ip routeadddisabled=nodst-address=0.0.0.0/0gateway=lte1 routing-table=main \
    suppress-hw-offload=noaddcomment=pubaddr disabled=nodistance=2dst-address=31.142.247.255\
    gateway=lte1 routing-table=main scope=30suppress-hw-offload=no\
    target-scope=10/system scheduleradddisabled=yes interval=5mname=PubIPon-event=ReNewPubIPpolicy=\
    read,write,policy,test start-date=1970-01-01start-time=23:59:59/system scriptadddont-require-permissions=noname=ReNewPubIPowner=admin policy=\
    read,write,policy,test source=":local NewIP [/ip cloud get public-address]\
    \r\
    \n/ip address set [find where comment=\"pubaddr\"] address=\$NewIP network\
    =\$NewIP\r\
    \n/ip ipsec peer set peer local-address=\$NewIP"
```

```
/ip addressaddaddress=10.10.5.1/24interface=bridge network=10.10.5.0addaddress=10.11.5.1/24interface="bridge guest"network=10.11.5.0addaddress=176.89.208.201comment=pubaddrinterface=lte1 network=176.89.208.201.png

---
```

## Response 1
A few years back, i had a Telekom-SIM assigned to a Mikrotik-DeviceEncountered some Issues, but was able to find an alternativ APN / LTE configuration that directly assigned the PublicIP. ---

## Response 2
I don't have such a chance. There is no gsm operator in the region that provides static ip. ---

## Response 3
From your description and configuration it seems to me that the actual issue you need to address may be different.Since you use IKEv2, the remote peer (the "center" as you call it) should not need that thelocal-addressin your configuration was the public one. So I assume that what actually happens when you change thelocal-addressis that the IPsec stack stops attempting to keep the old session alive and initiates a new one from the new address, which causes a creation of a new UDP "connection" both in the firewall of your Mikrotik itself and the one of the mobile ISP. Since both the previous and new connection use the same address and port on the remote side and the same port on the local side, the Mikrotik firewall cannot reuse the same local port on the lte interface for the new connection and randomly choses another one, which makes the ISP treat the UDP connection as a new one as well and let it through, while it most likely drops the packets belonging to the "old" one. This whole assumption only makes sense if the address the ISP assigns to your lte1 interface "internally" remains unchanged when the public one changes, is that the case?If it is, disabling the peer for about 10 minutes and then re-enabling it should be sufficient for the connection to re-establish even without changing the address, so this should be your first test. If it proves true, the bad news is that it is an issue with how the ISP handles UDP connections in the process that, from the outside, manifests as a change of the public address, and there is no way to prevent the connection from getting interrupted for a while each time this process takes place. It can be done in much less than 10 minutes but there will still be some time required to detect the outage, albeit faster than waiting for the/ip cloudto notice the change of the public address. ---

## Response 4
I don't think the issue is the ISP it sounds quite normal.I take it the lte device switches public ip because it's keep alive time was up and it renegotiates new ip with ISP.The tik is sitting on some NAT behind the public IP and is blissfully unaware the public IP has changed.That about sum it up?In that case you would need to look at command set for lte device which gives it's IP and script a poll on the lte device to pick when it changes IP. ---

## Response 5
Actually, I don't have a problem with VPN. The problem occurs when I add the real public IP to the address list in order to make VPN.From your description and configuration it seems to me that the actual issue you need to address may be different.The tik is sitting on some NAT behind the public IP and is blissfully unaware the public IP has changed.I tried this;
```
# i removed local adress from Peers config and also pubaddr in the address list is disabled;/ip ipsec peeraddaddress=111.111.111.111/32disabled=yes exchange-mode=ike2 name=peer \
    profile=ike_cryptWhile the Mikrotik settings are like this at the Center (PaloAlto);
```

```
description contains'IKEv2 IKE SA negotiation is failed as responder, non-rekey. Failed SA: 111.111.111.111[4500]-176.238.239.255[51435] SPI:0239b91635ed0e98:426762ab448185a9.'received ID_I(type ipaddr[10.222.191.127])doesnotmatch peers id176.238.239.255 -> Mikrotik pulic ip for now10.222.191.127   -> ISP is giving me for nowI know that if I make the Peer IP Adress Type dynamic in paloalto ike gateway settings, the problem will be solved, but I don't want to do it.2.pngWhen I delete pubaddr in the address list and add public ip to the routing table with distance=2, when ISP changes my public ip, there is no internet disconnection problem, but the vpn problem persists. microtik tries to set up vpn with the ip given by ISP and paloalto does not accept it.PlaoAlto Log;description contains 'received ID_I (type ipaddr [10.222.191.127]) does not match peers idMikrotik Log;got fatal error: AUTHENTICATION_FAILED

---
```

## Response 6
It depends on how Palo Alto has actually implemented it, but it might be possible to set the "peer identification" field to type "DNS" or "FQDN" and value towhateverisyourserial.sn.mynetname.netand do an appropriate change at the Mikrotik side -/ip/ipsec/identity/set [find where peer=peer] my-id=fqdn:whateverisyourserial.sn.mynetname.net. This way, Mikrotik would stop using an auto-generated ID which isip:lo.cal.add.ress. Maybe it is even enough to do this change on the Mikrotik side and keep the Palo Alto config as-is. ---