## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

- Configure IPv4 and IPv6 addressing on a MikroTik RouterOS 7.11 device
- Enable DHCP server and client on specific network interfaces
- Configure static IP addresses and routes for specific hosts and subnets

### Step-by-Step Implementation

#### IPv4 Addressing
1. Assign an IPv4 address to an interface:
```
/interface address add address=192.168.1.1/24 interface=ether1
```

2. Enable DHCP server on an interface:
```
/ip dhcp-server set interface=ether1 address-pool=dhcp_pool disabled=no
```

3. Add an address pool for the DHCP server:
```
/ip pool add name=dhcp_pool ranges=192.168.1.10-192.168.1.20
```

4. Configure a DHCP client on an interface:
```
/ip client add interface=ether2 address=dhcp
```

5. Add a static IP route:
```
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.254
```

#### IPv6 Addressing
1. Assign an IPv6 address to an interface:
```
/ipv6 address add address=2001:db8:1::1/64 interface=ether1
```

2. Enable DHCPv6 server on an interface:
```
/ipv6 dhcp-server set interface=ether1 address-pool=dhcpv6_pool disabled=no
```

3. Add an address pool for the DHCPv6 server:
```
/ipv6 pool add name=dhcpv6_pool ranges=2001:db8:1::10-2001:db8:1::20
```

4. Configure a DHCPv6 client on an interface:
```
/ipv6 client add interface=ether2 address=dhcp
```

5. Add a static IPv6 route:
```
/ipv6 route add dst-address=::/0 gateway=2001:db8:1::254
```

### Complete Configuration Commands

```
# IPv4 Addressing
/interface address add address=192.168.1.1/24 interface=ether1
/ip dhcp-server set interface=ether1 address-pool=dhcp_pool disabled=no
/ip pool add name=dhcp_pool ranges=192.168.1.10-192.168.1.20
/ip client add interface=ether2 address=dhcp
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.254

# IPv6 Addressing
/ipv6 address add address=2001:db8:1::1/64 interface=ether1
/ipv6 dhcp-server set interface=ether1 address-pool=dhcpv6_pool disabled=no
/ipv6 pool add name=dhcpv6_pool ranges=2001:db8:1::10-2001:db8:1::20
/ipv6 client add interface=ether2 address=dhcp
/ipv6 route add dst-address=::/0 gateway=2001:db8:1::254
```

### Common Pitfalls and Solutions

- **IP address conflicts:** Ensure that each IP address is unique within the network subnet.
- **Gateway configuration:** Verify that the gateway address is reachable from the corresponding interface.
- **DNS settings:** Configure DNS servers on the DHCP server or client to ensure name resolution.
- **Subnet mask mismatch:** Double-check that the subnet mask matches the IPv4 or IPv6 address range.

### Verification and Testing Steps

1. Check the interface IP addresses using:
```
/interface print
```

2. Test DHCP functionality by connecting a client to the network and verifying IP assignment.
3. Verify routes using:
```
/ip route print
```

4. Test connectivity to external hosts using:
```
/ping <destination IP address>
```

### Related Features and Considerations

- **IP Aliases:** Assign multiple IP addresses to a single interface.
- **IP Filtering:** Implement firewalls and access rules to control IP traffic.
- **IP Address Management (IPAM):** Utilize tools such as the MikroTik Address Manager for bulk IP address management.

### MikroTik REST API Examples

**Get IPv4 Addresses:**

**API Endpoint:** `/interface/ip/address`
**Request Method:** GET
**Example JSON Payload:**
```json
{}
```

**Expected Response:**
```json
[
  {
    "address": "192.168.1.1/24",
    "interface": "ether1",
    "status": "active"
  },
  ...
]
```

**Configure IPv6 Address:**

**API Endpoint:** `/ipv6/address`
**Request Method:** POST
**Example JSON Payload:**
```json
{
  "address": "2001:db8:1::1/64",
  "interface": "ether1"
}
```

**Expected Response:**
```json
{
  "ret": "ok",
  "message": "address added"
}
```