## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

In this scenario, we will configure IPv4 and IPv6 addressing on a MikroTik RouterOS device. We will create IP pools, assign IP addresses to interfaces, and enable IPv6 neighbor discovery.

### Step-by-Step Implementation

**1. Create IP Pools**

Create IP pools for both IPv4 and IPv6:

```
/ip pool
add address=10.0.0.0/24 name=ipv4-pool
add address=fe80::/64 name=ipv6-pool
```

**2. Enable IPv4 and IPv6 Neighbor Discovery**

Enable IPv4 and IPv6 neighbor discovery on all interfaces:

```
/ipv6 neighbor
set discover=yes
/ip neighbor
set discover=yes
```

**3. Assign IP Addresses to Interfaces**

Assign the IPv4 IP pool to the `ether1` interface:

```
/ip address
add address=10.0.0.1/24 interface=ether1
```

Assign the IPv6 IP pool to the `ether1` interface via DHCPv6:

```
/ip address
add address=fe80::1/64 interface=ether1 address-family=ipv6 dhcp6-pd=ipv6-pool
```

### Complete Configuration Commands

```
/ip pool
add address=10.0.0.0/24 name=ipv4-pool
add address=fe80::/64 name=ipv6-pool

/ipv6 neighbor
set discover=yes

/ip neighbor
set discover=yes

/ip address
add address=10.0.0.1/24 interface=ether1
add address=fe80::1/64 interface=ether1 address-family=ipv6 dhcp6-pd=ipv6-pool
```

### Common Pitfalls and Solutions

- Ensure that the IP pools are created and assigned to the correct interfaces.
- Verify that IPv4 and IPv6 neighbor discovery are enabled on all relevant interfaces.
- Check for any firewall rules or other configuration that might block IP traffic.

### Verification and Testing Steps

- Use the `/ip address print` command to verify the assigned IP addresses.
- Use the `/ipv6 neighbor print` and `/ip neighbor print` commands to verify IPv4 and IPv6 neighbor discovery.
- Ping other devices on the network to test connectivity.

### Related Features and Considerations

- Use the `/ip ipsec` command to configure IPsec tunnels.
- Use the `/ipv6 tunnel` command to configure IPv6 tunnels.
- Consider using DHCPv6 for automatic IP address assignment.

### MikroTik REST API Examples

**Get IPv4 addresses:**

```
API Endpoint: /ip/address
HTTP Request: GET
Example JSON Payload: {}
Expected Response:
[
  {
    "address": "10.0.0.1/24",
    "interface": "ether1"
  }
]
```

**Add an IPv6 address:**

```
API Endpoint: /ip/address
HTTP Request: POST
Example JSON Payload:
{
  "address": "fe80::1/64",
  "interface": "ether1",
  "address-family": "ipv6",
  "dhcp6-pd": "ipv6-pool"
}
Expected Response:
{
  "address": "fe80::1/64",
  "interface": "ether1",
  "id": 2
}
```