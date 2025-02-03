## IP Pools in MikroTik RouterOS 7.12

### Configuration Scenario and Requirements

Configure an IP pool in RouterOS to assign dynamic IP addresses to clients on a LAN interface. The pool will be configured with a specific range of IP addresses, subnet mask, and default gateway.

### Step-by-Step Implementation

1. **Create the IP Pool:**
   - Navigate to **IP > Pool** in the RouterOS GUI.
   - Click the **+** button to create a new pool.
   - Enter the following parameters:
     - Name: Assign a descriptive name to the pool.
     - Ranges: Specify the IP address range to be assigned to clients from the pool.
     - Network: Select the LAN interface for which the pool is being created.

2. **Configure the Default Gateway and DNS:**
   - Click on the **DNS** tab and enter the IP address of the DNS server.
   - Click on the **Gateway** tab and enter the IP address of the default gateway.

3. **Apply the Changes:**
   - Click the **Apply** button to save the configuration.

### Complete Configuration Commands

```
/ip pool
add name=my-pool ranges=192.168.1.10-192.168.1.254 network=LAN1
/ip pool dns
set pool=my-pool servers=8.8.8.8
/ip pool gateway
set pool=my-pool gateway=192.168.1.1
```

### Common Pitfalls and Solutions

- **IP Address Range Conflict:** Ensure that the specified IP address range does not conflict with any other network segments or IP pools.
- **Incorrect Gateway Address:** Verify that the gateway address entered is correct and erreichbar.
- **DNS Server Unreachable:** Make sure that the specified DNS server is online and accessible.

### Verification and Testing Steps

- **Check DHCP Server:** Navigate to **IP > DHCP Server** and ensure that the created IP pool is listed under **Available Pools**.
- **Assign IP Addresses:** Connect a client device to the LAN interface and check if it receives an IP address from the pool.

### Related Features and Considerations

- **DHCP Server:** Configuring an IP pool in RouterOS automatically activates the DHCP server. Ensure that the DHCP server is enabled and listening on the correct interface.
- **Address Leases:** Specify the lease time for IP addresses assigned from the pool in the **DHCP Server** settings.
- **Reservations:** Create static DHCP reservations for specific client devices if necessary.

### MikroTik REST API Examples

#### Create IP Pool

**API Endpoint:** `/ip/pool`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "my-pool",
  "ranges": [
    "192.168.1.10-192.168.1.254"
  ],
  "network": "LAN1"
}
```

**Expected Response:**

```json
{
  "id": "1",
  "name": "my-pool"
}
```

#### Get IP Pool Details

**API Endpoint:** `/ip/pool/{id}`

**Request Method:** GET

**Example Request:**

```
/ip/pool/1
```

**Expected Response:**

```json
{
  "id": "1",
  "name": "my-pool",
  "ranges": [
    "192.168.1.10-192.168.1.254"
  ],
  "network": "LAN1",
  "dns": [
    "8.8.8.8"
  ],
  "gateway": "192.168.1.1"
}
```