**IP Routing**

**1. Configuration Scenario and Requirements**

* Configure IP routing between multiple subnets on a MikroTik router.
* Use static routes for specific destinations.
* Enable dynamic routing protocols for auto-discovery of routes.

**2. Step-by-Step Implementation**

**Configure IP Addresses and Interfaces**

- Assign IP addresses to router interfaces connected to each subnet.
```
# Configure interface eth1
/interface ethernet set [find interface=ether1] address=10.10.10.1/24
# Configure interface eth2
/interface ethernet set [find interface=ether2] address=192.168.1.1/24
```

**Add Static Routes**

- Create static routes to specific destinations not directly connected.
```
# Add static route to 10.10.20.0/24 via eth2
/ip route add dst-address=10.10.20.0/24 gateway=192.168.1.254
```

**Enable Dynamic Routing Protocols**

- Select and configure a dynamic routing protocol, such as OSPF or BGP, to automatically discover and update routes.
```
# Enable OSPF
/routing ospf set enabled=yes
```

**3. Complete Configuration Commands**

```
# Assign IP addresses
/interface ethernet set [find interface=ether1] address=10.10.10.1/24
/interface ethernet set [find interface=ether2] address=192.168.1.1/24

# Add static routes
/ip route add dst-address=10.10.20.0/24 gateway=192.168.1.254
/ip route add dst-address=192.168.20.0/24 gateway=10.10.10.254

# Enable OSPF
/routing ospf set enabled=yes
```

**4. Common Pitfalls and Solutions**

- **Check interface statuses:** Ensure that all interfaces are up and running.
- **Verify IP addresses:** Confirm that the assigned IP addresses are correct and not conflicting.
- **Check route destinations:** Ensure that the static routes added have valid destination network ranges.

**5. Verification and Testing Steps**

- **Ping between subnets:** Test connectivity between hosts on different subnets to verify routing.
- **Check routing table:** Use `/ip route print` command toを確認する routing table entries.
- **Monitor routing protocol status:** If dynamic routing is enabled, check its status using `/routing [protocol-name] print` command.

**6. Related Features and Considerations**

- **Use IP pools:** Consider using IP pools for easier management of IP address assignments.
- **Limit routing table size:** Use `/ip route table` command to set maximum route table size to prevent performance issues.
- **Enable MAC server:** The MAC server feature helps resolve MAC addresses for static routes.
- **Utilize RoMON:** RoMON provides diagnostic tools for troubleshooting routing issues.

**7. MikroTik REST API Examples**

**Add Static Route**

| Endpoint | Method | Payload | Response |
|---|---|---|---|
| `/routing/route` | `POST` | `{ "dst-address": "10.10.20.0/24", "gateway": "192.168.1.254" }` | `{ "id": "1", "disabled": false }` |

**Enable OSPF**

| Endpoint | Method | Payload | Response |
|---|---|---|---|
| `/routing/ospf/settings` | `PUT` | `{ "enabled": true }` | `{ "enabled": true }` |

**8. IP Addressing (IPv4 and IPv6)**

- **Configure IPv4 Interfaces**
```
/interface ip address add address=10.0.0.1/24 interface=eth1
```
- **Configure IPv6 Addresses**
```
/interface ipv6 address add address=2001:db8::1/64 interface=eth1
```

**9. IP Pools**

- **Create an IP Pool**
```
/ip pool add name=pool1 ranges=192.168.1.0-192.168.1.254
```

**10. IP Settings**

- **Configure DNS Settings**
```
/ip dns set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes
```

**11. MAC Server**

- **Add a MAC Server Entry**
```
/ip dhcp-server lease add mac-address=01:02:03:04:05:06 address=192.168.1.100
```

**12. RoMON**

- **Enable RoMON**
```
/tool romon set enabled=yes
```

**13. WinBox**

- **Login to WinBox**

```
winbox.exe [router-ip] [username] [password]
```

**14. Certificates**

- **Create a Certificate**
```
/certificate add name=my-certificate subject=/C=XX/ST=State/L=City/O=Organization/CN=hostname type=rsa key-size=2048
```

**15. PPP AAA**

- **Configure PPP Authentication**
```
/ppp profile add name=pppoe-profile authentication=mschap2 chap-secrets=user:password
```

**16. RADIUS**

- **Configure RADIUS Server**
```
/radius add address=192.168.1.2 secret=shared-secret
```

**17. User / User Groups**

- **Create a User**
```
/user add name=username password=password group=group1
```

**18. Bridging and Switching**

- **Create a Bridge**
```
/bridge add name=my-bridge ports=eth1,eth2
```

**19. MACVLAN**

- **Configure MACVLAN Interface**
```
/interface macvlan add name=eth1.10 parent=eth1 mac-address=01:02:03:04:05:10
```

**20. L3 Hardware Offloading**

- **Enable L3 Hardware Offloading**
```
/routing l3-hardware-offload set enabled=yes
```

**21. MACsec**

- **Configure MACsec Interface**
```
/interface macsec add name=eth1.1 key-id=1 key-size=256 tx-scb=scb-1 rx-scb=scb-2 mode=encrypt-authenticate
```

**22. Quality of Service**

- **Create a Queue**
```
/queue simple add name=my-queue target=eth1 packet-mark=10
```

**23. Switch Chip Features**

- **Enable Switch Chip Flow Control**
```
/switch chip set flow-control=on
```

**24. VLAN**

- **Create a VLAN**
```
/vlan add name=vlan10 tagged=eth1,eth2 untagged=eth3
```

**25. VXLAN**

- **Enable VXLAN Interface**
```
/interface vxlan add tunnel-id=42 name=vxlan1 local-address=10.0.0.1 remote-address=10.0.0.2
```

**26. Firewall and Quality of Service (Including: Connection tracking, Firewall, Packet Flow in RouterOS, Queues, Firewall and QoS Case Studies, Kid Control, UPnP, NAT-PMP)**

- **Configure Firewall**
```
/ip firewall add action=drop chain=input src-address=192.168.1.100 dst-address=192.168.1.200
```

**27. IP Services (DHCP, DNS, SOCKS, Proxy)**

- **Configure DHCP Server**
```
/ip dhcp-server add interface=eth1 address-pool=pool1
```

**28. High Availability Solutions (Including: Load Balancing, Bonding, Bonding Examples, HA Case Studies, Multi-chassis Link Aggregation Group, VRRP, VRRP Configuration Examples)**

- **Configure VRRP**
```
/vrrp add instance=vrrp1 interface=eth1 vrid=1 virtual-address=192.168.1.254 priority=200
```

**29. Mobile Networking (Including: GPS, LTE, PPP, SMS, Dual SIM Application)**

- **Configure LTE Interface**
```
/interface lte add name=lte1 number=1
```

**30. Multi Protocol Label Switching - MPLS (Including: MPLS Overview, MPLS MTU, Forwarding and Label Bindings, EXP bit and MPLS Queuing, LDP, VPLS, Traffic Eng, MPLS Reference)**

- **Configure MPLS Interface**
```
/interface