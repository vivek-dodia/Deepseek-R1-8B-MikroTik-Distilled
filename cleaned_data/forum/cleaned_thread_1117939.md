# Thread Information
Title: Thread-1117939
Section: RouterOS
Thread ID: 1117939

# Discussion

## Initial Question
Can someone please take a look over these and see if they spot something wonky?I seem to be unable to connect to the RouterOS API from 10.0.105.0/24 network and I seem to be unable to get my IPv6 port-forward/NAT thing to work properly? It instead says it's filtered atm.This is what the a curl says to the Router's webui:
```
Connected to 10.0.105.1 (10.0.105.1) port 4443
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to 10.0.105.1:4443
* Closing connection
curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to 10.0.105.1:4443Here's the config:
```

```
/ip firewall address-list
add address=10.0.0.0/24 list=backdoor-addr-v4
add address=172.17.50.0/24 list=backdoor-addr-v4
add address=10.0.1.0/24 list=backdoor-addr-v4
add address=172.17.51.0/24 list=backdoor-addr-v4
/ip firewall filter
add action=accept chain=input comment="defconf: accept established,related,untracked" connection-state=established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment="defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=drop chain=input comment="defconf: drop all not coming from LAN" disabled=yes in-interface-list=!LAN
add action=drop chain=input dst-port=8291 in-interface-list=WAN protocol=tcp
add action=drop chain=input comment="Drop port 53 access from WAN" dst-port=53 in-interface-list=WAN protocol=tcp
add action=drop chain=input comment="Block NTP from WAN" dst-port=123 in-interface-list=WAN protocol=udp
add action=accept chain=input dst-port=4443 in-interface-list=VLANs log=yes protocol=tcp src-address=10.0.105.0/24
add action=accept chain=forward comment="defconf: accept in ipsec policy" ipsec-policy=in,ipsec
add action=accept chain=forward comment="defconf: accept out ipsec policy" ipsec-policy=out,ipsec
add action=fasttrack-connection chain=forward comment="defconf: fasttrack" connection-state=established,related hw-offload=yes
add action=accept chain=forward comment="defconf: accept established,related, untracked" connection-state=established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" connection-state=invalid disabled=yes
add action=drop chain=forward comment="defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat connection-state=new in-interface-list=WAN
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat comment="NAT Containers Traffic" out-interface=bridge src-address=172.19.0.0/24
add action=masquerade chain=srcnat dst-address-list=backdoor-addr-v4 out-interface=backdoor
add action=dst-nat chain=dstnat comment="Port-Forward to Kubernetes cluster external ingress" dst-port=80 in-interface-list=WAN log=yes protocol=tcp to-addresses=10.96.69.80 to-ports=80
add action=dst-nat chain=dstnat comment="Port-Forward to Kubernetes cluster external ingress" dst-port=443 in-interface-list=WAN log=yes protocol=tcp to-addresses=10.96.69.80 to-ports=443
/ip route
add distance=1 dst-address=172.17.51.0/24 gateway=backdoor routing-table=main scope=30 target-scope=10
add distance=1 dst-address=10.0.0.0/24 gateway=backdoor routing-table=main scope=30 target-scope=10
add distance=1 dst-address=10.0.1.0/24 gateway=backdoor routing-table=main scope=30 target-scope=10
add distance=1 dst-address=172.17.50.0/24 gateway=backdoor routing-table=main scope=30 target-scope=10
/ipv6 route
add disabled=no distance=1 dst-address=::/0 gateway=fe80::213:2%ether1 routing-table=main suppress-hw-offload=no
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set ssh address=192.168.99.0/24,192.168.2.0/24 port=10222
set www-ssl address=192.168.99.0/24,192.168.2.0/24 certificate=webfig disabled=no port=4443 tls-version=only-1.2
set api disabled=yes
set api-ssl certificate=webfig tls-version=only-1.2
/ipv6 firewall filter
add action=accept chain=input dst-port=179 in-interface-list=VLANs protocol=tcp
add action=accept chain=input comment="defconf: accept established,related,untracked" connection-state=established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=invalid
add action=accept chain=input comment="defconf: accept ICMPv6" protocol=icmpv6
add action=accept chain=input comment="defconf: accept UDP traceroute" dst-port=33434-33534 protocol=udp
add action=accept chain=input comment="defconf: accept DHCPv6-Client prefix delegation." dst-port=546 protocol=udp
add action=accept chain=input comment="defconf: accept IKE" dst-port=500,4500 protocol=udp
add action=accept chain=input comment="defconf: accept ipsec AH" protocol=ipsec-ah
add action=accept chain=input comment="defconf: accept ipsec ESP" protocol=ipsec-esp
add action=accept chain=input comment="defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=input comment="defconf: drop everything else not coming from LAN" disabled=yes in-interface-list=!LAN
add action=passthrough chain=input disabled=yes dst-port=443 in-interface-list=WAN protocol=tcp
add action=drop chain=input dst-port=8291 in-interface-list=WAN protocol=tcp
add action=accept chain=forward comment="defconf: accept established,related,untracked" connection-state=established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" connection-state=invalid
add action=drop chain=forward comment="defconf: drop packets with bad src ipv6" src-address-list=bad_ipv6
add action=drop chain=forward comment="defconf: drop packets with bad dst ipv6" dst-address-list=bad_ipv6
add action=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1" disabled=yes hop-limit=equal:1 protocol=icmpv6
add action=accept chain=forward comment="defconf: accept ICMPv6" protocol=icmpv6
add action=accept chain=forward comment="defconf: accept HIP" protocol=139
add action=accept chain=forward comment="defconf: accept IKE" dst-port=500,4500 protocol=udp
add action=accept chain=forward comment="defconf: accept ipsec AH" protocol=ipsec-ah
add action=accept chain=forward comment="defconf: accept ipsec ESP" protocol=ipsec-esp
add action=accept chain=forward comment="defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=forward comment="defconf: drop everything else not coming from LAN" in-interface-list=!LAN
add action=accept chain=output comment="Allow outgoing BGP traffic" dst-port=179 protocol=tcp
/ipv6 firewall nat
add action=dst-nat chain=dstnat dst-port=443 in-interface-list=WAN protocol=tcp to-address=fded:687e:c3bf::4443/128 to-ports=443
add action=dst-nat chain=dstnat dst-port=80 in-interface-list=WAN protocol=tcp to-address=fded:687e:c3bf::4443/128 to-ports=80
/ipv6 nd
set [ find default=yes ] disabled=yes dns=:: hop-limit=64
add dns=fd9d:7a72:44eb:a::1 hop-limit=64 interface=MainLAN
add dns=fd9d:7a72:44eb:c::1 hop-limit=64 interface=KubeProd managed-address-configuration=yes

---
```

## Response 1
IPv6:in filter/forward, there is no rule allowing dst-nated connections to get through before the final "drop whatever did not come in via LAN" one.IPv4:since you have disabled the "drop whatever did not come in via LAN" rule in filter/input rather than keeping it at the end of that chain and placing accept exceptions before it, the api-ssl service is now accessible to the worldtheaction=accept chain=input dst-port=4443 in-interface-list=VLANs log=yes protocol=tcp src-address=10.0.105.0/24rule does not override the restrictions in the/ip servicesection, as firewall comes first and the two parts of the configuration do not affect each other.set sshaddress=192.168.99.0/24, 192.168.2.0/24port=10222set www-ssladdress=192.168.99.0/24, 192.168.2.0/24certificate=webfig disabled=no port=4443 tls-version=only-1.2(and the rule itself is useless because whatever it does not accept is accepted by default) ---

## Response 2
IPv6:in filter/forward, there is no rule allowing dst-nated connections to get through before the final "drop whatever did not come in via LAN" one.IPv4:since you have disabled the "drop whatever did not come in via LAN" rule in filter/input rather than keeping it at the end of that chain and placing accept exceptions before it, the api-ssl service is now accessible to the worldtheaction=accept chain=input dst-port=4443 in-interface-list=VLANs log=yes protocol=tcp src-address=10.0.105.0/24rule does not override the restrictions in the/ip servicesection, as firewall comes first and the two parts of the configuration do not affect each other.set sshaddress=192.168.99.0/24, 192.168.2.0/24port=10222set www-ssladdress=192.168.99.0/24, 192.168.2.0/24certificate=webfig disabled=no port=4443 tls-version=only-1.2(and the rule itself is useless because whatever it does not accept is accepted by default)What would be the right way to restrict those services to the specific prefixes? Only do so in the firewall section and keep the drop whatever rule? ---

## Response 3
What would be the right way to ...Well...theright way... I'm probably too old to issue statements this strong. WhatI personally preferis to drop everything (using the last rule in each filter chain) and only explicitly accept the necessary exceptions. Because if you do it that way, your legal users will tell you quickly that you forgot to permit something. With the other way round, i.e. when you accept everything by default and only explicitly drop some exceptions, your illegal users will never tell you that you forgot to forbid something.As for where to define permitted addresses of clients who are allowed to access the management services like ssh or www - the settings under/ip servicework at application level, so the TCP SYN makes it to the socket and if it came from an address that is not allowed, the application sends back a TCP RST, so port scanners do notice that something is listening there, and theoretically there may be some vulnerability in the TCP stack that allows some kind of a magic SYN packet do something nasty even before the list of allowed addresses is consulted. So this is one reason why I prefer to restrict access to router's own services using the firewall filter chain input; the other one is that I prefer to do the same kind of thing at the same place even if multiple possibilities exist, as doing so spares my future self some time. ---

## Response 4
Another thing I found is that if my Kubernetes nodes announce svc addresses (via BGP) and I can connect to them from an IoT network, it loses the connection?Example from Mosquitto:
```
1736229933: New client connected from 10.0.50.121:49191 as DVES_5DF70D (p2, c1, k30, u'tasmota').
1736229933: Client DVES_5DF70D closed its connection.From inside the tasmota plug's console:
```

```
07:07:43.482 MQT: Attempting connection...
07:07:47.799 MQT: Connect failed to 10.96.69.10:1883, rc -4. Retry in 120 secCurrent firewall for IPv4:
```

```
/ip firewall address-list
add address=10.0.0.0/24 list=backdoor-addr-v4
add address=172.17.50.0/24 list=backdoor-addr-v4
add address=10.0.1.0/24 list=backdoor-addr-v4
add address=172.17.51.0/24 list=backdoor-addr-v4
add address=<snip>.sn.mynetname.net list=WANs
/ip firewall filter
add action=accept chain=input comment="defconf: accept established,related,untracked" connection-state=established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment="defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=accept chain=input dst-address-list=WANs dst-port=51821 protocol=udp
add action=drop chain=input comment="defconf: drop all not coming from LAN" in-interface-list=!LAN
add action=drop chain=input disabled=yes dst-port=8291 in-interface-list=WAN protocol=tcp
add action=drop chain=input comment="Drop port 53 access from WAN" disabled=yes dst-port=53 in-interface-list=WAN protocol=tcp
add action=drop chain=input comment="Block NTP from WAN" disabled=yes dst-port=123 in-interface-list=WAN protocol=udp
add action=accept chain=input dst-port=4443 in-interface-list=VLANs log=yes protocol=tcp src-address=10.0.105.0/24
add action=accept chain=input dst-port=161 protocol=udp src-address=192.168.99.0/24
add action=accept chain=forward comment="defconf: accept in ipsec policy" ipsec-policy=in,ipsec
add action=accept chain=forward comment="defconf: accept out ipsec policy" ipsec-policy=out,ipsec
add action=fasttrack-connection chain=forward comment="defconf: fasttrack" connection-state=established,related hw-offload=yes
add action=accept chain=forward comment="defconf: accept established,related, untracked" connection-state=established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" connection-state=invalid
add action=drop chain=forward comment="defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat connection-state=new in-interface-list=WAN
/ip firewall mangle
add action=mark-connection chain=prerouting comment="Mark connections for hairpin NAT" disabled=yes dst-address-list=WANs new-connection-mark="Hairpin NAT" passthrough=yes src-address-list=LANs

---
```

## Response 5
if my Kubernetes nodes announce svc addresses (via BGP) and I can connect to them from an IoT network, it loses the connection?Please review and maybe reword this sentence, I am not sure what actually happens under what circumstances. ---