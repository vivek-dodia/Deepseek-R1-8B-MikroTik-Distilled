# Thread Information
Title: Thread-211141
Section: RouterOS
Thread ID: 211141

# Discussion

## Initial Question
Hello everyone, I wanted to share a guide on setting up a WireGuard VPN connection toNordVPNon a Mikrotik router runningRouterOS v7.x. While NordVPN provides instructions for setting up an IKEv2/IPSec VPN connection—which works fine—you need to usemangleto route specific destinations, and you cannot implement a kill switch. Other protocols like L2TP/IPSec have been retired by NordVPN, and OpenVPN does not work with Mikrotik routers. Using WireGuard offers better flexibility, including the ability to implement a kill switch and route specific traffic without complex configurations.PrerequisitesA Mikrotik router runningRouterOS v7.xA Linux system (e.g., Debian) to retrieve necessary keysAn active NordVPN subscriptionStep 1: Install NordVPN and WireGuard on LinuxFirst, install the NordVPN client on your Linux system. You can find detailed instructions on the NordVPN support site:Installing NordVPN on Linux distributionsNext, install WireGuard:
```
sudo apt install wireguardStep 2: Retrieve Your Private Key and Server InformationEstablish a VPN connection using the NordVPN client:
```

```
nordvpn connectThen, retrieve your private key:
```

```
sudo wg show nordlynxprivate-keyNote:Keep your private key secure and do not share it.Next, obtain the public key, IP address, and port of the connected NordVPN WireGuard server:
```

```
sudo wg show nordlynxExample output:peer: aaaaaaabbbbbbbbxxxxxxyyyyyyyyy=endpoint: x.x.x.x:51820Alternatively, to find other servers and their information, use the NordVPN API:
```

```
curl'https://nordvpn.com/wp-admin/admin-ajax.php?action=servers_recommendations&filters\[servers_technologies\]\[identifier\]=wireguard_udp&limit=1'|python3-m json.toolNote:Each server has its own public key, but your private key remains the same.Step 3: Configure WireGuard on the Mikrotik RouterCreate the WireGuard Interface
```

```
/interfacewireguardaddlisten-port=51820mtu=1420name=wg-nordvpnprivate-key="your_private_key"- Replace"your_private_key"with the private key you obtained earlier.Add the Peer (NordVPN Server)
```

```
/interface wireguard peers add allowed-address=0.0.0.0/0endpoint-address=your_server_address endpoint-port=51820interface=wg-nordvpn persistent-keepalive=5spublic-key="server_public_key"- Replaceyour_server_addresswith the endpoint address (e.g.,us100.nordvpn.com).- Replace"server_public_key"with the public key of the NordVPN server.Assign an IP Address to the Interface
```

```
/ip addressaddaddress=10.5.0.2interface=wg-nordvpn network=10.5.0.0Step 4: Configure Firewall RulesAllow Incoming WireGuard Connections
```

```
/ip firewall filteraddaction=accept chain=input comment="Allow WireGuard"dst-port=51820protocol=udpAllow Specific IPs to Use the VPNFirst, define the list of IP addresses that are allowed to use the VPN:
```

```
/ip firewall address-list add address=192.168.1.0/24list=access_vpnCreate a Firewall Rule to Allow Forwarding:
```

```
/ip firewall filteraddaction=accept chain=forward comment="Allow VPN Traffic"out-interface=wg-nordvpn src-address-list=access_vpnConfigure NAT for Outgoing Traffic
```

```
/ip firewall nataddaction=masquerade chain=srcnatout-interface=wg-nordvpnStep 5: Configure Routing and Implement a Kill SwitchCreate a New Routing Table
```

```
/routing tableaddfib name="private_route"Add Routing RulesRoute traffic from specific hosts through the VPN:
```

```
/routing rule add action=lookup-only-in-table src-address=192.168.1.100/32table=private_routeOr route traffic to specific destinations (e.g., NordVPN DNS server):
```

```
/routing rule add action=lookup-only-in-table dst-address=103.86.96.100/32table=private_routeNote:103.86.96.100is one of the DNS servers provided by NordVPN.Configure Routes for the New TableAdd a blackhole route as a kill switch:
```

```
/ip routeaddblackhole distance=5routing-table=private_routeAdd a route through the WireGuard interface:
```

```
/ip routeadddistance=2gateway=wg-nordvpn@main routing-table=private_routeStep 6: Test the ConfigurationEnsure that devices specified in the address list are routing traffic through the VPN.Verify that the kill switch works by disabling the WireGuard interface and checking if traffic from the specified devices is blocked.ConclusionThat's it! You should now have a working WireGuard VPN connection to NordVPN on your Mikrotik router, complete with policy routing and a kill switch. This setup allows you to route specific traffic through the VPN and ensures that if the VPN connection drops, traffic will not leak through your regular internet connection.Let me know how it works for you or if you have any questions!

---
```

## Response 1
Just to add that in some cases, you might need the router to adjust the TCP MSS, if TCP connections get stuck./ip firewall mangleadd action=change-mss chain=forward comment="Clamp MSS to PMTU" new-mss=clamp-to-pmtu out-interface=wg-nordvpn \protocol=tcp tcp-flags=syn ---

## Response 2
There are two options, the one that was stated as well as:add action=change-mss chain=forward new-mss=1380 out-interface=wg-nordvpn protocol=tcp tcp-flags=syn tcp-mss=1381-65535 ---

## Response 3
So, for my use case, I only want one device 10.10.15.x/32 to use nordlynx, but I want to be able to access that device from anywhere in the network. As I have it now, I was able to whitelist 10.10.15.0/24, 10.10.10.0/24, etc. Is this possible doing it through routeros? ---

## Response 4
The easiest way to provide access to a third party wireguard service is via WIFI.Simply make a virtual WLAN just for internet access to nord.........If you have the option one can dedicate a vlan and ensure those needing access at their desks, have a managed switch next to the PC ( old hexes are great for this ) and then they can plug their PC into the correct port when wanting to go out nord for internet.As for your requirement one user/device to go out nord, is fairly easy using routing rules vice anything more complex.What I dont understand is that you want to be able to access that device from anywhere.Can you elaborate the use cases in more detail.why does device need to go out nordwhy do users need to access device.something missing in the equation to understand ---