## IP Pools

### Configuration Scenario and Requirements

For a small office or home network, you need to assign IP addresses automatically to devices connecting to the network. Use an IP pool to define a range of IP addresses for this purpose.

### Step-by-Step Implementation

**Create the IP Pool:**

- Navigate to **IP -> Pool** in RouterOS.
- Click **+** to create a new pool.
- Enter a **Name** for the pool (e.g., Office-Pool).
- Specify an **Address Range** for the pool (e.g., 192.168.1.100-192.168.1.200).
- Set the **Gateway** to the router's default gateway (e.g., 192.168.1.1).
- Optionally, set the **DNS Server** and **Netmask**.

**Assign the IP Pool to an Interface:**

- Navigate to **IP -> Addresses** in RouterOS.
- Click **+** to create a new address.
- Select the **Interface** to which the pool should be assigned.
- In the **Address** field, select the created pool (e.g., Office-Pool).
- Click **Apply** to save the configuration.

### Complete Configuration Commands

```
/ip pool add name=Office-Pool ranges=192.168.1.100-192.168.1.200 gateway=192.168.1.1
/ip address add interface=ether1-gateway address=Office-Pool
```

### Common Pitfalls and Solutions

- **IP address range conflict:** Ensure that the IP addresses in the pool do not overlap with any existing addresses on the network.
- **Gateway mismatch:** The gateway address specified in the pool must match the default gateway of the router.
- **DNS server not set:** If the DNS server is not set in the pool, devices may not be able to resolve domain names.

### Verification and Testing Steps

- Connect devices to the network and check if they receive IP addresses from the pool.
- Use ping to test connectivity between devices and external addresses.

### Related Features and Considerations

- **DHCP Server:** DHCP Server is a related feature that dynamically assigns IP addresses from the pool to devices.
- **NAT (Network Address Translation):** NAT can be used to translate the private IP addresses from the pool to a public IP address for internet access.
- **Security:** IP pools should be created securely and only as needed to minimize the risk of unauthorized device access.

### REST API Examples

**Create IP Pool:**

**Endpoint**: ```/api/ip/pool```
**Method**: ```POST```

**Request Body**:
```json
{
  "name": "Office-Pool",
  "ranges": ["192.168.1.100-192.168.1.200"],
  "gateway": "192.168.1.1"
}
```

**Response**:
```json
{
  "id": 1
}
```

**Assign IP Pool to Interface:**

**Endpoint**: ```/api/ip/address```
**Method**: ```POST```

**Request Body**:
```json
{
  "interface": "ether1-gateway",
  "address": "/ip/pool/Office-Pool"
}
```

**Response**:
```json
{
  "id": 1
}
```