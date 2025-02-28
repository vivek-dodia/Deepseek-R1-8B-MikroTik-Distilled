# Thread Information
Title: Thread-1116835
Section: RouterOS
Thread ID: 1116835

# Discussion

## Initial Question
I am trying to set up a site-to-site WireGuard VPN between two RouterOS devices and have been having trouble getting the tunnel to stand up. I am using this tutorial:https://thesebytes.net/mikrotik-site-to ... vpn-setup/which does appear to be pretty similar to the documentation example here:https://help.mikrotik.com/docs/spaces/R ... /WireGuard1.1.1.1 and 2.2.2.2 (real IPs replaced) are the WAN addresses of both routers, and 10.254.254.1/30 and 10.254.254.2/30 are the addresses of both sides of the tunnel. I have created exceptions in the firewall to allow UDP 13231 to the router from WAN on the firewall of both ends. I have confirmed that both WAN endpoints are pingable from each other.R1 relevant config:
```
/interfacewireguardaddlisten-port=13231mtu=1420name=wireguard-poc734/interfacewireguard peersaddallowed-address=10.254.254.0/30endpoint-address=2.2.2.2endpoint-port=13231interface=wireguard-poc734 name=\
    wireguardpeer-poc734 persistent-keepalive=10spublic-key="redacted"/ip addressaddaddress=10.254.254.1/30interface=wireguard-poc734 network=10.254.254.0/ip firewall address-listaddaddress=2.2.2.2list=trusted-outside/ip firewall filteraddaction=accept chain=zone-outside-to-router comment="allow wireguard from outside"dst-port=13231protocol=udp \
    src-address-list=trusted-outsideR2 relevant config:
```

```
/interfacewireguardaddlisten-port=13231mtu=1420name=wireguard-poc994/interfacewireguard peersaddallowed-address=10.254.254.0/30endpoint-address=1.1.1.1endpoint-port=13231interface=wireguard-poc994 name=\
    wireguardpeer-poc994 persistent-keepalive=10spublic-key="redacted"/ip addressaddaddress=10.254.254.2/30interface=wireguard-poc994 network=10.254.254.0/ip firewall address-listaddaddress=1.1.1.1list=trusted-outside/ip firewall filteraddaction=accept chain=zone-outside-to-router comment="allow wireguard from outside"dst-port=13231protocol=udp \
    src-address-list=trusted-outsideThe tunnel does not stand up at this point and I get the following log message repeatedly: wireguard-poc734: [wireguardpeer-poc734] [key redacted]: Handshake for peer did not complete after 5 seconds, retrying (try 2)I am left scratching my head at what could be missing, as far as I can see the instructions have been followed correctly and all the necessary parts of the config are there.

---
```

## Response 1
Purpose of your wireguard network??Only one end needs to act as client SERVER for handshake.......... which one? ---

## Response 2
Purpose is to share network resources behind each router with each other - a machine on one router's internal network should be able to ping a device in the other router's network etc. R1 would be the server or hub, with R2 being the client - perhaps I need to set one side to responder? I am not sure of the requirement there. Routing is not set up for getting between networks at the moment, I was planning on getting that up after the tunnel was finished. ---

## Response 3
One thing I have noticed while doing some packet captures for troubleshooting, is I can see the wireguard packet leave the WAN interface on each router, but the other router never sees a wireguard packet received. This is really mysterious to me as I can ping each router and get a response, and had previously set up a GRE tunnel (which I abandoned in hopes of setting up wireguard) which came up and was able to communicate just fine. I even changed the ports on both ends just in case something was getting filtered out on my ISP's network, however the situation hasn't changed - both routers can transmit their initial handshake packet, but the other router never sees it. I even put a very basic firewall rule at the very top of the list to allow this traffic but I am not seeing it in the captures. ---

## Response 4
Well, I managed to get it working after taking the remote router and plugging it into a different internet connection - I think it's safe to say that either my DOCSIS modem or ISP doesn't like it when WireGuard or IPsec (tried that for tunneling too!) packets attempt to reach another WAN host on the same modem (both have a public IP address), but ICMP and GRE across the WAN is apparently ok with that topology. Super mysterious.Edit: My config is finalized and the tunnel is up and passing traffic, this seems to work well with the spoke endpoint having an unknown/dynamic IP address. Here it is for self-documentation's sake:R1 "Hub":
```
/interfacewireguardaddlisten-port=13231mtu=1420name=wireguard-poc734/interfacewireguard peersaddallowed-address=0.0.0.0/0interface=wireguard-poc734is-responder=yes name=wireguardpeer-poc734 \
    persistent-keepalive=10spublic-key="redacted"R2 "Spoke":
```

```
/interfacewireguardaddlisten-port=13231mtu=1420name=wireguard-poc994/interfacewireguard peersaddallowed-address=0.0.0.0/0endpoint-address=example.com endpoint-port=13231interface=wireguard-poc994 name=\
    wireguardpeer-poc994 persistent-keepalive=10spublic-key="redacted"

---
```

## Response 5
When you post full config on both/export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc.)I will gladly address some of the errors shown. ---