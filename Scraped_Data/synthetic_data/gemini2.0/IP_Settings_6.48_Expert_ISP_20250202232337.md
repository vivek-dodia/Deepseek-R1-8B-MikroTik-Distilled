**IP Settings**

**1. Configuration Scenario and Requirements**

Configure IP settings for a MikroTik RouterOS 6.48-based ISP gateway router. The router will have multiple WAN and LAN interfaces and require flexible IP addressing, routing, and security configurations.

**2. Step-by-Step Implementation**

**2.1. Interface Configuration**

- Create WAN and LAN interfaces with appropriate IP addresses, netmasks, and gateways:

```
> interface add name=wan address=192.168.1.1/24
> interface add name=lan address=10.0.0.1/24
```

**2.2. IP Routing**

- Enable IP forwarding and define static routes to external networks:

```
> ip firewall set forward=accept
> ip route add gateway=192.168.1.254 distance=1
```

**2.3. DHCP Server**

- Configure a DHCP server on the LAN interface to automatically assign IP addresses to clients:

```
> ip dhcp-server add interface=lan address-pool=LAN-pool
> ip dhcp-server set LAN-pool range=10.0.0.10-10.0.0.254 lease-time=12h
```

**2.4. DNS Settings**

- Configure DNS servers for the router and clients:

```
> ip dns set allow-remote-requests=yes
> ip dns add preferred-dns=8.8.8.8
> ip dns add alternate-dns=8.8.4.4
```

**2.5. Firewall Rules**

- Implement basic firewall rules to restrict access and protect the network:

```
> ip firewall add action=drop chain=input dst-address=10.0.0.0/24 in-interface=wan
> ip firewall add action=accept chain=input dst-address=10.0.0.0/24 in-interface=lan
```

**3. Complete Configuration Commands**

```
> interface add name=wan address=192.168.1.1/24
> interface add name=lan address=10.0.0.1/24
> ip firewall set forward=accept
> ip route add gateway=192.168.1.254 distance=1
> ip dhcp-server add interface=lan address-pool=LAN-pool
> ip dhcp-server set LAN-pool range=10.0.0.10-10.0.0.254 lease-time=12h
> ip dns set allow-remote-requests=yes
> ip dns add preferred-dns=8.8.8.8
> ip dns add alternate-dns=8.8.4.4
> ip firewall add action=drop chain=input dst-address=10.0.0.0/24 in-interface=wan
> ip firewall add action=accept chain=input dst-address=10.0.0.0/24 in-interface=lan
```

**4. Common Pitfalls and Solutions**

- **IP address conflicts:** Ensure unique IP addresses are assigned to all interfaces.
- **Routing loops:** Verify static routes and firewall rules do not create routing loops.
- **DNS resolution failures:** Ensure DNS servers are accessible and configured correctly.
- **Firewall misconfigurations:** Carefully review firewall rules to prevent unintended access or blockages.

**5. Verification and Testing Steps**

- Use "ip address print" to verify interface IP settings.
- Run "ping" commands to test connectivity to internal and external destinations.
- Check DNS resolution using "nslookup" or "dig."
- Verify firewall rules using "ip firewall print."

**6. Related Features and Considerations**

- **NAT:** Configure network address translation to allow private IP addresses to access the Internet.
- **PPPoE:** Establish PPPoE connections for WAN interfaces that require it.
- **VLANs:** Create virtual LANs to segregate network traffic.
- **Security groups:** Define security groups to apply firewall rules based on IP addresses or other criteria.

**7. MikroTik REST API Examples**

**Get Router IP Settings:**

**API Endpoint:** `/router/settings/ip`
**Request Method:** GET

**Example Response:**

```json
{
  "ethernet":[
    {
      "address":"10.0.0.1",
      "dns":"8.8.8.8",
      "gateway":"192.168.1.254",
      "interface":"ether1"
    }
  ],
  "ip":"192.168.1.1",
  "netmask":"255.255.255.0",
  "route":[
    {
      "distance":"1",
      "gateway":"192.168.1.254"
    }
  ]
}
```

**Set Static Route:**

**API Endpoint:** `/ip/route`
**Request Method:** POST

**Example JSON Payload:**

```json
{
  "distance": "1",
  "gateway": "192.168.1.254",
  "dst-address": "0.0.0.0/0"
}
```

**Expected Response:**

```
OK
```