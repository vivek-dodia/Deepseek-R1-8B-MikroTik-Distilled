## IP Pools

### Configuration Scenario and Requirements

In a SOHO network, DHCP is required to assign IP addresses to various client devices. However, there is a need to assign IP addresses from a specific range of IP addresses. IP pools allow us to achieve this.

### Step-by-Step Implementation

1. **Create an IP Pool:**
   - Navigate to `/ip pool` in WinBox GUI.
   - Click on the "+" icon to create a new pool.
   - Enter a pool name (e.g., "SOHO-Pool").
   - Specify the network address and subnet mask for the pool (e.g., 192.168.1.0/24).

2. **Set the Range of IP Addresses:**
   - Under the "Ranges" tab, click on the "+" icon.
   - Enter the start and end IP addresses of the range (e.g., 192.168.1.100-192.168.1.200).

3. **Apply the Pool to an Interface:**
   - Navigate to `/ip address` in WinBox GUI.
   - Select the interface that DHCP clients will connect to (e.g., ether1).
   - Click on the "DHCP Server" tab and enable "DHCP Server".
   - Under "Pool", select the created pool (e.g., SOHO-Pool).

### Complete Configuration Commands

```
/ip pool add name=SOHO-Pool ranges=192.168.1.100-192.168.1.200
/ip address set [interface-name] dhcp-server=yes pool=SOHO-Pool
```

### Common Pitfalls and Solutions

- **Pool Range Overlap:** Ensure that the range of IP addresses specified in the pool does not overlap with any existing IP assignments or static IP addresses.
- **Incorrect Subnet Mask:** Ensure that the subnet mask specified for the pool is correct and matches the network address.
- **DHCP Server Disabled:** Verify that the DHCP server is enabled on the interface to which the pool is applied.

### Verification and Testing Steps

1. **DHCP Client Configuration:**
   - Obtain a DHCP lease on a client device connected to the network.
   - Verify that the IP address assigned to the client is within the range specified in the IP pool.
2. **Network Ping:**
   - Ping devices on the network to ensure they are able to communicate and have valid IP addresses.
3. **Subnet Compatibility:**
   - Check that the subnet mask of the pool is consistent with the subnet mask of the client devices.

### Related Features and Considerations

- **DHCP Server:** IP pools are used in conjunction with DHCP servers to assign IP addresses to clients.
- **IP Address Ranges:** Pools provide the ability to segment IP address ranges and assign them to different devices or subnetworks.
- **Dynamic IP Assignment:** DHCP servers use pools to dynamically assign IP addresses from a specified range, ensuring efficient IP address allocation.

### MikroTik REST API Examples

**Endpoint:** `/api/ip/pool`

**Request Method:** GET

**Example JSON Payload:**

```
{
  "name": "SOHO-Pool"
}
```

**Expected Response:**

```
{
  "name": "SOHO-Pool",
  "ranges": [
    "192.168.1.100-192.168.1.200"
  ]
}
```