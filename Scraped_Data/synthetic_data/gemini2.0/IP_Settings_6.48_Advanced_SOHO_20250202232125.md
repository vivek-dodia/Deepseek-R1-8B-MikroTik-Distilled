## IP Settings

### Configuration Scenario and Requirements

This section covers advanced IP settings in MikroTik RouterOS, including:

- IP Addressing (IPv4 and IPv6)
- IP Pools
- IP Routing

### Step-by-Step Implementation

#### IP Addressing (IPv4 and IPv6)

1. Enable IP addresses on interfaces:

   ```
   /ip address add address=10.10.10.1/24 interface=ether1
   /ip address add address=2001:db8::1/64 interface=ether1
   ```

2. Configure default routes:

   ```
   /ip route add gateway=10.10.10.254
   /ipv6 route add gateway=2001:db8::254
   ```

#### IP Pools

1. Create an IP pool:

   ```
   /ip pool add name=office-static-pool addresses=10.10.10.10-10.10.10.20
   /ip pool add name=office-dhcp-pool ranges=10.10.10.100-10.10.10.200
   ```

2. Assign IP pools to DHCP servers:

   ```
   /ip dhcp-server add address-pool=office-static-pool interface=ether1
   /ip dhcp-server add address-pool=office-dhcp-pool interface=ether1
   ```

#### IP Routing

1. Enable static routes:

   ```
   /ip route add dst-address=10.10.20.0/24 gateway=10.10.10.254
   /ipv6 route add dst-address=2001:db8::1/64 gateway=2001:db8::254
   ```

2. Enable dynamic routing:

   ```
   /ip route add dst-address=0.0.0.0/0 protocol=rip
   /ipv6 route add dst-address=::/0 protocol=ospf6
   ```

### Complete Configuration Commands

The complete configuration commands used in this scenario are:

```
/ip address add address=10.10.10.1/24 interface=ether1
/ip address add address=2001:db8::1/64 interface=ether1
/ip route add gateway=10.10.10.254
/ipv6 route add gateway=2001:db8::254
/ip pool add name=office-static-pool addresses=10.10.10.10-10.10.10.20
/ip pool add name=office-dhcp-pool ranges=10.10.10.100-10.10.10.200
/ip dhcp-server add address-pool=office-static-pool interface=ether1
/ip dhcp-server add address-pool=office-dhcp-pool interface=ether1
/ip route add dst-address=10.10.20.0/24 gateway=10.10.10.254
/ipv6 route add dst-address=2001:db8::1/64 gateway=2001:db8::254
/ip route add dst-address=0.0.0.0/0 protocol=rip
/ipv6 route add dst-address=::/0 protocol=ospf6
```

### Common Pitfalls and Solutions

- **IP address conflicts:** Ensure that IP addresses assigned to interfaces and IP pools are unique within the network.
- **Incorrect subnet masks:** Verify that subnet masks are configured correctly to avoid routing issues.
- **Incomplete IPv6 addresses:** Ensure that both IPv6 addresses and gateways include leading zeroes.
- **Mismatched routes:** Check that routes match the destination networks and use appropriate gateways.

### Verification and Testing Steps

1. Verify IP addresses:

   ```
   /ip address print
   /ipv6 address print
   ```

2. Test IP connectivity:

   ```
   ping 10.10.10.2
   ping6 2001:db8::2
   ```

3. Test dynamic routing:

   ```
   /routing rip print
   /routing ospf6 print
   ```

### Related Features and Considerations

- **DHCP Reservations:** Reserve specific IP addresses for known devices within a DHCP pool.
- **Firewall Rules:** Configure firewall rules to control access based on IP addresses.
- **IPsec Tunnels:** Establish secure IP tunnels between remote networks using IPsec encryption.

### MikroTik REST API Examples

#### Get IP Addresses

```
GET /api/ip/address/print
```

Example Response:

```
[
  {
    "address": "10.10.10.1",
    "disabled": false,
    "interface": "ether1"
  },
  {
    "address": "2001:db8::1",
    "disabled": false,
    "interface": "ether1"
  }
]
```

#### Add Static Route

```
POST /api/ip/route/add
```

Example Request Body:

```
{
  "dst-address": "10.10.20.0/24",
  "gateway": "10.10.10.254"
}
```

Example Response:

```
{
  "id": 1
}
```