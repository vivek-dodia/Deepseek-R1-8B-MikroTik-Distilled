## IP Pools

### Configuration Scenario and Requirements

Create an IP pool on a MikroTik router to automatically assign IP addresses to clients on a specific network segment.

### Step-by-Step Implementation

1. **Create a New Pool:**
   - Navigate to **IP** > **Pools** > **Add New**.
   - Enter a **Name** for the pool.
   - Select the **Ranges** tab.

2. **Define IP Range:**
   - Enter the **Start** and **End** IP addresses of the range.
   - Specify the **Subnet** mask.

3. **Configure Address Lease Time (Optional):**
   - Navigate to the **Leases** tab.
   - Set the **Lease Time** (e.g., 24h).

4. **Enable DHCP Server:**
   - Navigate to **IP** > **DHCP Server** > **Add New**.
   - Select the created pool in the **Pool** field.
   - Specify the **Interface** to which the DHCP server will bind.

### Complete Configuration Commands

```
/ip pool add name=MyPool ranges=10.0.0.1-10.0.0.254
/ip dhcp-server add interface=ether1 pool=MyPool
```

### Common Pitfalls and Solutions

- **IP Conflict:** Ensure that the IP range used for the pool does not overlap with any existing IP addresses on the network.
- **Subnet Mismatch:** The subnet mask of the pool must match the subnet mask of the clients requesting addresses.
- **Gateway Discrepancy:** If the pool is not assigned as the default gateway on the clients, they may experience connectivity issues.

### Verification and Testing Steps

- Check the status of the IP pool: `/ip pool print`.
- Verify that the DHCP server is running: `/ip dhcp-server print`.
- Assign an IP address to a client: Connect a device to the network segment and check its assigned IP address.

### Related Features and Considerations

- **IP Binding:** Use DHCP bindings to assign specific IP addresses to specific clients.
- **DNS Server:** Configure a DNS server to provide name resolution for clients.
- **Firewall Rules:** Create firewall rules to restrict access to the IP pool.

### MikroTik REST API Examples

#### Get IP Pools

**API Endpoint:** `/ip/pool`

**Request Method:** GET

**Response:**

```json
[
  {
    "name": "MyPool",
    "ranges": [
      {
        "start": "10.0.0.1",
        "end": "10.0.0.254",
        "subnet-mask": "255.255.255.0"
      }
    ],
    "leases": {
      "lease-time": "24h"
    }
  }
]
```

#### Create IP Pool

**API Endpoint:** `/ip/pool`

**Request Method:** POST

**JSON Payload:**

```json
{
  "name": "MyPool",
  "ranges": [
    {
      "start": "10.0.0.1",
      "end": "10.0.0.254",
      "subnet-mask": "255.255.255.0"
    }
  ],
  "leases": {
    "lease-time": "24h"
  }
}
```