## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

- Configure IP addresses for multiple interfaces on a MikroTik router.
- Assign IPv4 and IPv6 addresses manually or through DHCP.
- Set up a default gateway and DNS servers for internet access.

### Step-by-Step Implementation

#### IPv4 Configuration

1. **Connect to the router:** Use WinBox or SSH to establish a connection to the router.
2. **Go to IP -> Addresses:** Navigate to the IP -> Addresses tab in the router's configuration tree.
3. **Add an IPv4 address:** Click the "+" button to create a new IPv4 address.
4. **Configure the address:** Enter the IP address, subnet mask, and interface.
5. **Set the default gateway:** Under the "Gateway" field, enter the IP address of the default gateway.
6. **Save the configuration:** Click the "OK" button to save the changes.

#### IPv6 Configuration

1. **Go to IP -> Addresses:** Navigate to the IP -> Addresses tab in the router's configuration tree.
2. **Add an IPv6 address:** Click the "+" button to create a new IPv6 address.
3. **Configure the address:** Enter the IPv6 address, prefix length, and interface.
4. **Set the default gateway:** Under the "Gateway" field, enter the IPv6 address of the default gateway.
5. **Save the configuration:** Click the "OK" button to save the changes.

### Complete Configuration Commands

#### IPv4

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=10.0.0.1/24 gateway=10.0.0.254 interface=ether2
```

#### IPv6

```
/ip address add address=2001:db8:85a3::8a2e:370:7334 interface=ether1
/ip address add address=fe80::1 interface=ether2
```

### Common Pitfalls and Solutions

- **No internet access:** Verify that the gateway settings are correct and that the router is connected to the internet.
- **IPv6 connectivity issues:** Ensure that the IPv6 addresses and prefix lengths are configured correctly on both the router and the connected devices.
- **Incorrect subnet masks:** The subnet mask must be compatible with the IP address. For example, a subnet mask of /24 requires the first three octets of the IP address to be the same.

### Verification and Testing Steps

1. **Ping the default gateway:** Use the ping command to test connectivity to the default gateway.
2. **Access the internet:** Try browsing a website or using other internet-based applications to confirm that internet access is working.
3. **Check IPv6 connectivity (if configured):** Use the ping6 command to test IPv6 connectivity to an IPv6-enabled host.

### Related Features and Considerations

- **DHCP:** MikroTik routers can act as DHCP servers to automatically assign IP addresses to connected devices.
- **IP pools:** IP pools can be used to create a range of IP addresses that can be assigned to devices.
- **IP routing:** IP routing allows the router to forward traffic between different subnets.
- **MAC server:** MAC servers can be used to maintain a table of MAC addresses and corresponding IP addresses, which can be useful for security and network management purposes.

### MikroTik REST API Examples

#### Retrieve IP Addresses

**Endpoint:** `/ip/address/print`
**Method:** GET
**Request:**
```
GET /ip/address/print HTTP/1.1
Authorization: Basic YWRtaW46cGFzc3dvcmQ=
```

**Example Response:**
```
[
  {
    ".id": ".1",
    "address": "192.168.1.1/24",
    "actual-mtu": 1500,
    "anycast": false,
    "comment": null,
    "disabled": false,
    "dynamic": false,
    "firewall": null,
    "interface": ".int1",
    "ipv4-address": "192.168.1.1",
    "ipv4-prefix-length": 24,
    "ipv6-address": null,
    "ipv6-prefix-length": null,
    "network": "192.168.1.0",
    "use-peer-dns": false,
    "use-peer-nb": false
  },
  {
    ".id": ".2",
    "address": "10.0.0.1/24",
    "actual-mtu": 1500,
    "anycast": false,
    "comment": null,
    "disabled": false,
    "dynamic": false,
    "firewall": null,
    "interface": ".int2",
    "ipv4-address": "10.0.0.1",
    "ipv4-prefix-length": 24,
    "ipv6-address": null,
    "ipv6-prefix-length": null,
    "network": "10.0.0.0",
    "use-peer-dns": false,
    "use-peer-nb": false
  }
]
```

#### Add an IP Address

**Endpoint:** `/ip/address/add`
**Method:** POST
**Request Body:**
```
{
  "address": "192.168.2.1/24",
  "interface": ".int3"
}
```

**Example Response:**
```
{
  ".id": ".3",
  "address": "192.168.2.1/24",
  "actual-mtu": 1500,
  "anycast": false,
  "comment": null,
  "disabled": false,
  "dynamic": false,
  "firewall": null,
  "interface": ".int3",
  "ipv4-address": "192.168.2.1",
  "ipv4-prefix-length": 24,
  "ipv6-address": null,
  "ipv6-prefix-length": null,
  "network": "192.168.2.0",
  "use-peer-dns": false,
  "use-peer-nb": false
}
```