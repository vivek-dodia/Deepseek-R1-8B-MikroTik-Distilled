# Thread Information
Title: Thread-1113529
Section: RouterOS
Thread ID: 1113529

# Discussion

## Initial Question
Hello, I’ve configured WireGuard on my MikroTik router (version 7.16), and it’s working correctly for one peer (Hamed-PC). This peer is able to connect, access the internet, and use the tunnel without any issues. However, for a second peer (Omid), the handshake is successfully established, but no traffic passes through the tunnel.Here’s my configuration:Interface Configuration:
```
/interfacewireguardaddlisten-port=40443mtu=1420name=WGprivate-key="QFBD8AfDtRK0UKxBcYw9lBYvDvlgGO29hnBNXC44jXM="Peers Configuration:
```

```
/interfacewireguard peersaddallowed-address=0.0.0.0/0client-address=192.168.10.100/32client-dns=8.8.8.8,4.2.2.4client-endpoint=31.41.35.121endpoint-address=31.41.35.121endpoint-port=40443interface=WG name=Hamed-PCprivate-key="SFbnsf4LR3yiLsMZNLNyo1BdLq6OaQpakLh6pAsWpWw="public-key="4WQ8hizcFvtwYat2m48DAk1hfCXYztR+42D8p7xK7S4="addallowed-address=0.0.0.0/0client-address=192.168.10.101/32client-dns=8.8.8.8,4.2.2.4client-endpoint=31.41.35.121endpoint-address=31.41.35.121endpoint-port=40443interface=WG name=Omidprivate-key="uOzYZiTG0lU3nHZ9TrSrQbmNRLuQMkUsT4psZkwDl2s="public-key="p7AwXg1+Yv5yXxVYPmeQ1ee6982z4QW7uBkNX2cg3Gs="The WireGuard interface on the router has an IP address of 192.168.10.1/24.NAT is configured and works perfectly for the first peer (Hamed-PC).Firewall rules are set to allow WireGuard traffic on port 40443.The handshake for both peers is established, but Omid cannot pass traffic.Troubleshooting Steps Taken:Verified NAT configuration and confirmed it works for the first peer (Hamed-PC).Verified DNS and routing settings on the Omid client.Checked WireGuard logs for both the router and the Omid client.Pinged the Omid IP address (192.168.10.101) from the router but received no response.Request for Help:What could cause one peer to work perfectly while another peer fails to pass traffic despite successful handshake? Any insights or suggestions for additional troubleshooting steps would be greatly appreciated.Thank you in advance!

---
```

## Response 1
Hi, I think that it's a common misunderstanding (I had to learn it myself) that the definition of "allowed-address" on the responder side allows any packets from the peer to the responder. This has to be done on the config on the client!I usually set* on the responder: allowed-address= to the client wg-address/32* on client: allowed-address= to the responder wg-address/32 plus responder network/24 or 0.0.0.0/0 for responder acting as default gateway)then try to ping the responders wg-inteface-ip from the client first.Start with minimal complexity and then get more complex.Maybe this helps.Ralf. ---

## Response 2
Think about the logic. One should understand the function of allowed addresses:.On inbound, it checks if the remote source address coming in is on the list!On outbound, it checks in order of the rules as they appear, a. does the destination exist. and b. assign it to the right peer.The first peer has an allowed IP address of 0.0.0.0/ therefore any traffic outbound will never hit the second peer.Put it another way, the return traffic from the second peer will always go back out the first peer and is thus effectively dropped.The server for handshake rarely has 0.0.0.0/0 to any peer for this reason.If you need one, for example to go out the internet of a peer client router, then the suggestion is a second wireguard interface just for this purpose.Allowed IPs is to identifya. remote subnets, IP one wishes to connect toORb. remote subnets, IP coming to the local router.o.o.o.o/o is logical at the client devices on the their peer settings identifying the router!WhY all the noise, get rid of it. This is all you neeed/interface wireguard peersadd allowed-address=192.168.10.100/32 interface=WG name=Hamed-P public-key="+++++add allowed-address=192.168.10.101/32 interface=WG name=Omid public-key="=======" ---

## Response 3
@hamed, Checked WireGuard logs for both the router and the Omid client.Pinged the Omid IP address (192.168.10.101) from the router but received no response.and what did those log and ping results say? ---