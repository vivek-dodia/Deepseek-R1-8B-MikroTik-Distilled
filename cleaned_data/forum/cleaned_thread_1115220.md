# Thread Information
Title: Thread-1115220
Section: RouterOS
Thread ID: 1115220

# Discussion

## Initial Question
EDIT: I'm an idiot and typo'd an IP address. I've updated the code to be a copy of a working Wireguard config if anyone finds it useful.I have wireguard set up on a CHR, I'm able to establish a connection, logs show a successful handshake and keepalive packets, but I can't get any traffic through the tunnel in either direction. What am I doing wrong?Mikrotik Config
```
# 2024-12-17 14:06:30 by RouterOS 7.16.2# software id =#/interfaceethernetset[finddefault-name=ether1]disable-running-check=no/interfacewireguardaddlisten-port=25618mtu=1420name=WGprivate-key="<PRIVKEY>"/portset0name=serial0set1name=serial1/interfacewireguard peersaddallowed-address=10.200.0.2/32client-address=10.200.0.2/32client-endpoint=<FQDN>client-keepalive=20sclient-listen-port=25618interface=WGis-responder=yes name=\"TEST"persistent-keepalive=20spublic-key="<PUBKEY>"/ip addressaddaddress=10.10.11.29/24comment=LANinterface=ether1 network=10.10.11.0addaddress=10.200.0.1/24comment=WGinterface=WG network=10.200.0.0/ip dhcp-clientaddinterface=ether1/ip dnssetservers=8.8.8.8/ip firewall filteraddaction=drop chain=input comment="drop invalid"connection-state=invalidaddaction=drop chain=forward comment="drop invalid"connection-state=invalidaddaction=accept chain=input comment="accept established,related,untracked"connection-state=established,related,untrackedaddaction=accept chain=input comment="allow WireGuard traffic"dst-address=10.10.11.29dst-port=25618protocol=udpaddaction=accept chain=input comment="allow WireGuard traffic"in-interface=WGaddaction=accept chain=forward comment="allow WireGuard traffic"in-interface=WGaddaction=accept chain=input comment="accept ICMP"protocol=icmpaddaction=accept chain=input comment="accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=accept chain=input comment=mgmt dst-port=22,80,443protocol=tcpaddaction=drop chain=forward comment="drop everything not explicitly allowed"disabled=yesaddaction=drop chain=input comment="drop everything not explicitly allowed"disabled=yes/ip routeadddisabled=nodistance=10dst-address=0.0.0.0/0gateway=10.10.11.1pref-src=10.10.11.29routing-table=main suppress-hw-offload=no/system clocksettime-zone-name=America/Denver/system loggingaddtopics=wireguard/system notesetshow-at-login=no/system ntp clientsetenabled=yes/system ntp client serversaddaddress=utcnist.colorado.eduClient config (Windows):
```

```
[Interface]PrivateKey=<PRIVKEY>ListenPort=25618Address=10.200.0.2/32DNS=8.8.8.8[Peer]PublicKey=<PUBKEY>AllowedIPs=10.10.11.0/24Endpoint=FQDN:25618PersistentKeepalive=20

---
```

## Response 1
NEVERMIND. I'm an idiot. I typo'd an IP address and wasted 3 hours debugging. ---

## Response 2
We've all been there ---