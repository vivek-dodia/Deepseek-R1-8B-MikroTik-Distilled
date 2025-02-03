## IP Addressing (IPv4 and IPv6) in MikroTik RouterOS 7.12

### Configuration Scenario and Requirements

- Configure IPv4 and IPv6 addressing on a MikroTik router
- Assign IP addresses from a pool
- Set up default gateway and DNS servers

### Step-by-Step Implementation

**IPv4 Configuration**

1. Create an IP pool:
```
/ip pool add name=my-ip-pool ranges=192.168.1.1-192.168.1.100
```

2. Assign the IP pool to an interface:
```
/interface ip address add interface=ether1 address-pool=my-ip-pool
```

3. Set default gateway:
```
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1
```

4. Set DNS servers:
```
/ip dns set servers=8.8.8.8,8.8.4.4
```

**IPv6 Configuration**

1. Create an IPv6 pool:
```
/ipv6 pool add name=my-ipv6-pool ranges=::1/64
```

2. Assign the IPv6 pool to an interface:
```
/ipv6 address add interface=ether1 address-pool=my-ipv6-pool
```

3. Set default gateway:
```
/ipv6 route add dst-address=::/0 gateway=::1
```

### Complete Configuration Commands

```
/ip pool add name=my-ip-pool ranges=192.168.1.1-192.168.1.100
/interface ip address add interface=ether1 address-pool=my-ip-pool
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1
/ip dns set servers=8.8.8.8,8.8.4.4
/ipv6 pool add name=my-ipv6-pool ranges=::1/64
/ipv6 address add interface=ether1 address-pool=my-ipv6-pool
/ipv6 route add dst-address=::/0 gateway=::1
```

### Common Pitfalls and Solutions

- **Incorrect subnet mask:** Ensure the subnet mask specified in the IP pool and address commands is compatible with the network configuration.
- **Invalid IP address pool:** Verify that the ranges specified in the IP pool are correct and non-overlapping.
- **Disabled interface:** Check if the interface you're configuring is enabled and has an IP address assigned to it.

### Verification and Testing Steps

- Check the IP address and IPv6 address of the interface using `/ip address print` and `/ipv6 address print`.
- Ping a known IP address or IPv6 address to verify connectivity.
- Check the default gateway and DNS servers using `/ip route print` and `/ip dns print`.

### Related Features and Considerations

- **Static IP addressing:** Manually assign specific IP addresses to interfaces using `/ip address add address=...` and `/ipv6 address add address=...`.
- **DHCP server:** Assign IP addresses dynamically using the DHCP server feature `/ip dhcp-server`.
- **DNS forwarder:** Configure the router to forward DNS queries to an upstream DNS server using `/ip dns forward`.
- **IPv6 prefix delegation:** Automatically assign IPv6 prefixes to devices connected via DHCP using `/ipv6 prefix delegation`.

### MikroTik REST API Examples

**Get IP address of an interface:**

**Endpoint:** `/interface/ip/address/print`
**Request Method:** GET
**Example JSON Request:**
```json
{
  "interface": "ether1"
}
```
**Expected Response:**
```json
[
  {
    "address": "192.168.1.10",
    "interface": "ether1",
    "mac-address": "00:00:00:00:00:01",
    "network": "192.168.1.0/24"
  }
]
```

**Add an IPv6 address to an interface:**

**Endpoint:** `/ipv6/address/add`
**Request Method:** POST
**Example JSON Request:**
```json
{
  "interface": "ether1",
  "address": "::1/64"
}
```
**Expected Response:**
```json
{
  "id": "1"
}
```