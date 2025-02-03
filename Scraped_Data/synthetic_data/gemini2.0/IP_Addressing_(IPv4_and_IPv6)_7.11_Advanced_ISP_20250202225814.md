## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

- Configure IPv4 and IPv6 addressing on a MikroTik router.
- Use DHCP to dynamically assign IPv4 addresses to clients.
- Configure static IPv4 and IPv6 addresses for specific interfaces.

### Step-by-Step Implementation

**1. Configure DHCP Server**

```
/ip dhcp-server address-pool
add name=pool1 ranges=192.168.1.100-192.168.1.200 lease-time=3600s
```

**2. Enable DHCP Server on Interface**

```
/interface ethernet set ether1 dhcp-server=pool1
```

**3. Set Static IPv4 Address**

```
/ip address
add address=192.168.1.25/24 interface=ether1
```

**4. Set Static IPv6 Address**

```
/ipv6 address
add address=2001:db8::1/64 interface=ether1
```

### Verification and Testing Steps

- Use an IP scanner to verify thatDHCP is assigning addresses.
- Ping clients to test connectivity with the IPv4 and IPv6 addresses.

### Common Pitfalls and Solutions

- Ensure that the DHCP server pool range is not overlapping with the statically assigned addresses.
- If DHCP is not working, check that the router's firewall is not blocking DHCP traffic.

### Related Features and Considerations

- MikroTik RouterOS supports various DHCP options, such as setting DNS servers and lease time.
- DHCP Snooping can be used to prevent rogue DHCP servers on the network.
- IPv6 privacy extensions can be enabled to enhance privacy.

### MikroTik REST API Example

**Endpoint:** `/ip/address`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "address": "192.168.1.25/24",
  "interface": "ether1"
}
```

**Expected Response:**

```json
[
  {
    "address": "192.168.1.25/24",
    "interface": "ether1"
  }
]
```