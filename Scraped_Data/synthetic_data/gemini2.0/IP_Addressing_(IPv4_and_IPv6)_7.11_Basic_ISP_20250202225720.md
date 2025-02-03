## IP Addressing (IPv4 and IPv6) in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

- Configure IPv4 and IPv6 addresses on a MikroTik router.
- Assign IP addresses to clients using DHCP.

### Step-by-Step Implementation

**IPv4 Addressing**

1. Go to IP > Addresses menu in WinBox.
2. Click on the "+" button to create a new IPv4 address.
3. Select the interface to which you want to assign the IP address.
4. Enter the IP address and subnet mask.
5. Click on Apply.

**IPv6 Addressing**

1. Go to IP > Addresses menu in WinBox.
2. Click on the "+" button to create a new IPv6 address.
3. Select the interface to which you want to assign the IPv6 address.
4. Enter the IPv6 address and prefix length.
5. Click on Apply.

**DHCP Server**

1. Go to IP > DHCP Server menu in WinBox.
2. Click on the DHCP Setup tab.
3. Select the interface on which you want to enable DHCP server.
4. Enter the IP address pool range.
5. Click on Apply.

### Complete Configuration Commands

**IPv4 Address Configuration**

```
/ip address add address=192.168.1.1/24 interface=ether1
```

**IPv6 Address Configuration**

```
/ipv6 address add address=2001:db8::1/64 interface=ether1
```

**DHCP Server Configuration**

```
/ip dhcp-server add address-pool=pool1 interface=ether1 range=192.168.1.100-192.168.1.200 lease-time=24h
```

### Common Pitfalls and Solutions

- Ensure that the subnet mask is correct for the IP address range.
- Avoid using overlapping IP address ranges.
- Make sure that the DHCP server is listening on the correct interface.
- Check if the firewall rules are allowing the DHCP traffic.

### Verification and Testing Steps

- Ping the IP address assigned by DHCP to verify connectivity.
- Use the "ip address print" and "ipv6 address print" commands to verify the IP address configurations.
- Use the "ip dhcp-server lease print" command to check the DHCP leases.

### Related Features and Considerations

- **Static IP Addressing:** Manually configure IP addresses for specific devices.
- **IP Routes:** Configure routes to reach other networks.
- **DNS Settings:** Configure DNS servers for name resolution.

### MikroTik REST API Examples

**Get IPv4 Address List**

**Endpoint:** `/ip/address`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  ".proplist": "list"
}
```

**Expected Response:**

```json
[
  {
    ".id": ".id",
    "address": "192.168.1.1",
    "comment": null,
    "disabled": false,
    "interface": "ether1",
    "network": "192.168.1.0",
    "use-peer-dns": false
  }
]
```

**Add IPv6 Address**

**Endpoint:** `/ipv6/address`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "address": "2001:db8::1",
  "interface": "ether1",
  "prefix-length": 64
}
```

**Expected Response:**

```json
{
  ".id": ".id"
}
```