## IP Pools

### Configuration Scenario and Requirements

**Scenario:**
Configure an IP pool on a MikroTik router to assign IP addresses dynamically to clients.

**Requirements:**
- RouterOS 6.48 (6.x or 7.x)
- Basic understanding of IP addressing and DHCP
- Router with an available network interface

### Step-by-Step Implementation

1. **Create a New IP Pool**

   - Go to **IP > Pool**.
   - Click on the **+** button.
   - Enter a name for the pool (e.g., "OfficePool").
   - Select the network interface to which the pool will be assigned.
   - Configure the IP address range for the pool (e.g., 192.168.1.0/24).

2. **Set DHCP Server Settings**

   - Go to **IP > DHCP Server**.
   - Click on the **+** button.
   - Select the interface assigned to the IP pool created in Step 1.
   - Enable DHCP server.
   - Configure the DHCP lease time (e.g., 24h).

3. **Apply Changes and Save**

   - Click on the **Apply** button to save the changes.
   - Click on the **OK** button to close the window.

### Complete Configuration Commands

```
/ip pool
add name=OfficePool ranges=192.168.1.0-192.168.1.254 interface=ether1
/ip dhcp-server
add interface=ether1 enable=yes lease-time=24h
```

### Common Pitfalls and Solutions

- **IP Address Conflict:** Ensure the IP address range specified for the pool does not overlap with any other configured network segments.
- **DHCP Server Not Enabled:** Verify that DHCP server is enabled on the interface assigned to the IP pool.
- **Mismatched Subnet:** The IP address range specified for the pool should match the subnet of the network interface.

### Verification and Testing Steps

- Check the **IP > ARP** table to see if clients are receiving IP addresses from the pool.
- Connect a client to the network and verify its IP address is assigned from the pool's range.

### Related Features and Considerations

- **Address Leases:** Use the `/ip dhcp-server lease` command to manage individual IP address leases.
- **DNS Server:** Configure a DNS server on the router to provide DNS resolution for clients.
- **Default Gateway:** Set the default gateway for the DHCP server to the router's IP address.
- **Security:** Consider using DHCP server options to enforce security measures (e.g., DHCP Option 66 for client hostname).

### MikroTik REST API Examples

**Endpoint:** `/ip/pool/add`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "OfficePool",
  "ranges": "192.168.1.0-192.168.1.254",
  "interface": "ether1"
}
```

**Expected Response:**

```json
{
  "id": 1
}
```

**Endpoint:** `/ip/dhcp-server/add`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "interface": "ether1",
  "enable": true,
  "lease-time": "24h"
}
```

**Expected Response:**

```json
{
  "id": 1
}
```