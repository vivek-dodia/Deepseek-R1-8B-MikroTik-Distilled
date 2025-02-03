**IP Addressing (IPv4 and IPv6)**

**1. Configuration Scenario and Requirements**

- Configure IP addresses and network settings for IPv4 and IPv6 networks.
- Assign IP addresses to interfaces and pools.
- Verify IP connectivity and troubleshoot common addressing issues.

**2. Step-by-Step Implementation**

**IPv4 Addressing**

**a. Configure IPv4 Interface Address**
- Go to **IP > Addresses**
- Click **+** to add a new address
- Select interface, IP address, and other parameters (netmask, gateway, etc.)

**b. Configure IPv4 Address Pool**
- Go to **IP > Pool**
- Click **+** to add a new pool
- Define name, prefixes, range, and other settings

**IPv6 Addressing**

**a. Configure IPv6 Interface Address**
- Go to **IP > Addresses**
- Click **+** to add a new address
- Select interface, IPv6 address, and other parameters (prefix length, etc.)

**b. Configure IPv6 Address Pool**
- Go to **IP > Pool**
- Click **+** to add a new pool
- Define name, prefixes, range, and other settings

**3. Complete Configuration Commands**

**IPv4 Address**
```
/ip address add address=192.168.1.10/24 interface=ether1
```

**IPv4 Pool**
```
/ip pool add name=my-pool
/ip pool add name=my-pool addresses=192.168.1.0/24
```

**IPv6 Address**
```
/ipv6 address add address=2001:db8::1/64 interface=ether1
```

**IPv6 Pool**
```
/ipv6 pool add name=my-ipv6-pool
/ipv6 pool add name=my-ipv6-pool addresses=2001:db8::/64
```

**4. Common Pitfalls and Solutions**

- Invalid IP address format: Ensure the IP address is in the correct format and syntax.
- IP address conflict: Check for duplicate IP addresses in the network.
- Incorrect subnet mask: Ensure the subnet mask is compatible with the IP address.
- Default gateway missing: Configure a default gateway on each interface to enable network access.

**5. Verification and Testing Steps**

- Ping IP addresses to verify connectivity.
- Use **ipconfig** or **ifconfig** commands to confirm IP settings.
- Monitor traffic and packet flow to detect any issues.

**6. Related Features and Considerations**

- **DHCP Server**: Assign IP addresses dynamically to clients.
- **DNS**: Configure DNS settings for name resolution.
- **NAT**: Translate IP addresses between different networks.

**7. MikroTik REST API Examples**

**IPv4 Address**

**Endpoint:** `/ip/address`
**Method:** POST
**JSON Payload:**
```
{
  "interface": "ether1",
  "address": "192.168.1.10/24"
}
```

**Expected Response:**
```
{
  "id": "1"
}
```

**IPv4 Pool**

**Endpoint:** `/ip/pool`
**Method:** POST
**JSON Payload:**
```
{
  "name": "my-pool",
  "ranges": [
    "192.168.1.0-192.168.1.255"
  ]
}
```

**Expected Response:**
```
{
  "id": "1"
}
```