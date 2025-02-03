## IP Pools in RouterOS 6.48

### Configuration Scenario and Requirements

- Create and configure an IP pool for dynamic IP address assignment to clients on a specific network segment.
- Configure the pool to allocate addresses from a specific range and set lease time.
- Enable DHCP server on the relevant interface.

### Step-by-Step Implementation

#### 1. Create IP Pool

- Navigate to IP > Pool.
- Click the "+" button to create a new pool.
- Configure the following parameters:
    - Name: Enter a descriptive name for the pool.
    - Ranges: Specify the IP address range from which addresses will be allocated.
    - Comment: Add an optional comment for documentation purposes.

#### 2. Configure DHCP Server

- Navigate to IP > DHCP Server.
- Click the "+" button to create a new DHCP server instance.
- Configure the following parameters:
    - Interface: Select the interface that will use the IP pool.
    - Lease Time: Set the amount of time that an assigned IP address will remain valid (e.g., 24h).
    - Pool: Select the previously created IP pool.
    - Default Gateway: Specify the default gateway IP address that will be provided to clients.
    - DNS Servers: Provide a list of DNS server IP addresses.

### Complete Configuration Commands

```
/ip pool add name=my-pool ranges=192.168.1.100-192.168.1.200 comment="Pool for LAN clients"
/ip dhcp-server add interface=ether1 lease-time=24h pool=my-pool default-gateway=192.168.1.1 dns-server=8.8.8.8,8.8.4.4
```

### Common Pitfalls and Solutions

- **IP address range conflict:** Ensure that the specified IP pool range does not overlap with any existing static IP assignments or other IP pools.
- **Incorrect interface selection:** Select the correct interface that will use the IP pool. Assigning an IP pool to the wrong interface can lead to IP address conflicts or network issues.

### Verification and Testing Steps

- Verify the IP pool configuration by navigating to IP > Pool. The created pool should be listed.
- Connect a client to the network and check if it receives an IP address from the expected range.
- Check the DHCP server lease list to confirm that the IP address has been assigned to the client.

### Related Features and Considerations

- **DHCP Relay:** Use DHCP relay to forward DHCP requests from one network segment to another.
- **DNS:** Ensure that the DNS servers provided by DHCP are valid and can resolve domain names.
- **Lease Time:** Adjust the lease time based on the specific network environment and client requirements.

### MikroTik REST API Examples

#### Get IP Pool Information

**API Endpoint:** `/ip/pool`

**Request Method:** GET

**Example JSON Payload:**

```json
{}
```

**Expected Response:**

```json
[
  {
    "name": "my-pool",
    "ranges": "192.168.1.100-192.168.1.200",
    "comment": "Pool for LAN clients"
  }
]
```

#### Add IP Pool

**API Endpoint:** `/ip/pool`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "my-new-pool",
  "ranges": "192.168.2.100-192.168.2.200",
  "comment": "Pool for guest network"
}
```

**Expected Response:**

```json
{
  "id": 2
}
```