## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

**Objective:**
Configure IPv4 and IPv6 addressing on a MikroTik RouterOS device and verify connectivity.

**Requirements:**
- MikroTik RouterOS v7.12 or later
- Interfaces with appropriate physical connections

### Step-by-Step Implementation

**1. IPv4 Addressing**

- Go to **IP > Addresses**
- Click **Add New**
- Select **Interface:** (choose the interface to assign the IP address to)
- Enter **IP Address:** (e.g., 192.168.1.1/24)
- Click **Apply**

**2. IPv6 Addressing**

- Go to **IP > Addresses**
- Click **Add New**
- Select **Interface:** (choose the interface to assign the IPv6 address to)
- Enter **IPv6 Address:** (e.g., fe80::1/64)
- Select **Address Type:** (e.g., Manual, DHCPv6, SLAAC)
- Click **Apply**

### Complete Configuration Commands

**IPv4:**

```
/ip address add interface=<interface> address=<ip_address/subnet_mask>
```

**IPv6:**

```
/ip address add interface=<interface> address=<ipv6_address/subnet_mask> address-type=<address_type>
```

### Common Pitfalls and Solutions

- **Interface Not Listed:** Ensure that the interface is physically connected and appears in the **Interfaces** list.
- **Invalid IP Address:** Verify that the IP address and subnet mask are valid for the intended network.
- **IPv6 Address Conflict:** If using DHCPv6 or SLAAC, ensure no other devices on the network have the same IPv6 address.

### Verification and Testing Steps

- Go to **IP > Addresses** and verify that the IP addresses are listed.
- Use **Ping** to test connectivity to other devices on the network using both IPv4 and IPv6 addresses.

### Related Features and Considerations

- **IP Pools:** Allows for dynamic assignment of IP addresses.
- **IP Routing:** Configures routing rules to direct traffic between subnets.
- **MAC Server:** Maps MAC addresses to IP addresses for ARP resolution.
- **RoMON:** Provides remote management and IP address configuration.

### MikroTik REST API Examples

**Get IPv4 Addresses:**

**Endpoint:** `/ip/address/print`
**Request Method:** GET
**Example Response:**

```json
[
  {
    ".id": ".id",
    "address": "192.168.1.1/24",
    "comment": null,
    "disabled": false,
    "dynamic": false,
    "interface": "ether1",
    "network": "192.168.1.0/24"
  },
  {
    ".id": ".id",
    "address": "172.16.1.2/32",
    "comment": null,
    "disabled": false,
    "dynamic": false,
    "interface": "ether2",
    "network": "172.16.1.0/32"
  }
]
```

**Add IPv6 Address:**

**Endpoint:** `/ip/address/add`
**Request Method:** POST
**Example JSON Payload:**

```json
{
  "address": "fe80::1/64",
  "interface": "ether1",
  "address-type": "manual"
}
```

**Expected Response:**

```json
{
  ".id": ".id"
}
```