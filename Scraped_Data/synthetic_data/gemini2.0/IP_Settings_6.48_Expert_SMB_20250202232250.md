## IP Settings

### Configuration Scenario and Requirements

This documentation covers advanced IP settings configuration in MikroTik RouterOS 6.48 for a small to medium-sized business (SMB) network. It includes configuration for IP addressing, IP pools, IP routing, and other advanced features.

### Step-by-Step Implementation

**1. IP Addressing**

Configure IPv4 and IPv6 addresses on interfaces:

```
/ip address add address=10.0.0.1/24 interface=ether1
/ipv6 address add address=2001:db8::1/64 interface=ether1
```

**2. IP Pools**

Create an IP pool for dynamic IP assignment:

```
/ip pool add name=dhcp-pool ranges=10.0.0.100-10.0.0.200
```

**3. IP Routing**

Configure static routes:

```
/ip route add dst-address=192.168.0.0/24 gateway=10.0.0.2
```

**4. IP Settings**

Enable IP forwarding:

```
/ip settings set forward=enable
```

Configure packet filtering rules:

```
/ip firewall filter add chain=input action=drop dst-address=192.168.0.0/24
```

**5. MAC Server**

Configure MAC address to IP address bindings:

```
/ip dhcp-server lease add address=10.0.0.100 mac-address=AA:BB:CC:DD:EE:FF
```

**6. RoMON**

Enable remote monitoring:

```
/system romon enable
```

**7. WinBox**

Change the WinBox default port:

```
/system identity set winbox-port=8291
```

**8. Certificates**

Create a self-signed certificate:

```
/certificate generate key-name=test-certificate ca=no
```

**9. PPP AAA**

Configure AAA for PPPoE authentication:

```
/radius add secret=radius-secret service=pppoe
/ppp aaa set authentication=radius realm=radius-realm
```

**10. RADIUS**

Configure a RADIUS server:

```
/radius add server=192.168.0.1 port=1812 secret=radius-secret
```

**11. User / User Groups**

Create a user and user group:

```
/user add name=test-user password=test-password
/user-group add name=test-group members=test-user
```

### Common Pitfalls and Solutions

- **Incorrect IP addressing:** Verify that IP addresses and subnet masks are configured correctly.
- **Duplicate IP addresses:** Ensure that no two devices have the same IP address.
- **Firewall blocking:** Check firewall rules to ensure that necessary traffic is allowed.
- **Authentication issues:** Verify that AAA and RADIUS settings are configured correctly.
- **RoMON not accessible:** Make sure that the RoMON port is open and accessible from the remote location.

### Verification and Testing Steps

- **Ping:** Test IP connectivity between devices.
- **Traceroute:** Verify the path taken by packets.
- **WinBox access:** Check if you can access the router using WinBox.
- **AAA authentication:** Test user authentication for PPPoE.
- **RADIUS server:** Verify if the RADIUS server is responding to authentication requests.

### Related Features and Considerations

- **DHCP Server:** Configure and manage dynamic IP address assignment.
- **DNS Server:** Provide name resolution services.
- **NAT:** Configure Network Address Translation for internet access.
- **Proxy Server:** Enable web browsing and filtering.
- **QoS:** Implement Quality of Service for network traffic management.
- **VPN:** Establish secure connections between remote locations.

### MikroTik REST API Examples

**Get IP Address**

```
GET /api/ip/address/print
```

**Example Response:**

```
[
  {
    "address": "10.0.0.1",
    "interface": "ether1",
    "netmask": "255.255.255.0"
  }
]
```

**Add IP Pool**

```
POST /api/ip/pool/add
{
  "name": "dhcp-pool",
  "ranges": ["10.0.0.100-10.0.0.200"]
}
```