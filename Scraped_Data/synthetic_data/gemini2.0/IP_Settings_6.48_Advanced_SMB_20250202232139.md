## IP Settings

### Configuration Scenario and Requirements

Configure IP settings for an SMB network using RouterOS 6.48, including:

- IPv4 and IPv6 addressing
- IP pool management
- Default gateway and DNS settings

### Step-by-Step Implementation

**1. Configure IPv4 Addressing**

```
/ip address
add address=192.168.1.1/24 interface=ether1
```

**2. Configure IPv6 Addressing**

```
/ipv6 address
add address=2001:db8::1/64 interface=ether1
```

**3. Configure IP Pool**

```
/ip pool
add name=office-pool ranges=192.168.1.10-192.168.1.200
```

**4. Configure Default Gateway**

```
/ip route
add dst-address=0.0.0.0/0 gateway=192.168.1.254
```

**5. Configure DNS Settings**

```
/ip dns
set servers=8.8.8.8,8.8.4.4
```

### Complete Configuration Commands

```
/ip address add address=192.168.1.1/24 interface=ether1
/ipv6 address add address=2001:db8::1/64 interface=ether1
/ip pool add name=office-pool ranges=192.168.1.10-192.168.1.200
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.254
/ip dns set servers=8.8.8.8,8.8.4.4
```

### Common Pitfalls and Solutions

- **IP Address Conflict:** Ensure that the IP addresses assigned are not already used by other devices on the network.
- **Invalid IP Pool Range:** Make sure the specified IP pool range falls within the configured subnet.
- **Gateway Unreachable:** Verify that the gateway IP address is correct and the gateway device is accessible.
- **DNS Server Unavailable:** Confirm that the DNS servers are responding and the network has access to them.

### Verification and Testing Steps

- Use the `/ip address print` and `/ipv6 address print` commands to verify IP address assignments.
- Run `/ip pool print` to check IP pool configuration.
- Ping an external IP address to test gateway connectivity.
- Resolve a domain name using nslookup to verify DNS settings.

### Related Features and Considerations

- **IP Routes:** Use IP routes to define specific paths for IP traffic.
- **IP Firewall:** Implement IP firewall rules to control access to and from the network.
- **DHCP Server:** Provide automatic IP address assignment using a DHCP server.
- **MAC Address Management:** Assign static MAC addresses for improved network visibility and security.

### MikroTik REST API Examples

**Get IP Address:**

```
API Endpoint: /ip/address/print
Request Method: GET
Example JSON Payload: {}
Expected Response:
```
```json
[
  {
    "address": "192.168.1.1/24",
    "interface": "ether1"
  }
]
```

**Create IP Pool:**

```
API Endpoint: /ip/pool/add
Request Method: POST
Example JSON Payload:
{
  "name": "office-pool",
  "ranges": ["192.168.1.10-192.168.1.200"]
}
Expected Response:
```
```json
{
  "name": "office-pool",
  "ranges": ["192.168.1.10-192.168.1.200"]
}
```