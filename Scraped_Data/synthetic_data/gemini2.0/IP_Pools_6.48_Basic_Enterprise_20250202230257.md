## IP Pools

### Configuration Scenario and Requirements

- Create an IP pool that will be used to assign IP addresses to DHCP clients within a specific subnet.
- Configure the pool with a range of available addresses, subnet mask, and default gateway.
- Test the pool functionality by assigning an IP address to a DHCP client.

### Step-by-Step Implementation

#### 1. Create IP Pool
Navigate to **IP > Pool** and click the "+" button to create a new pool.

- Name: Enter a descriptive name for the pool (e.g., "Employee-Pool").
- Ranges: Specify the range of IP addresses that will be available for allocation from the pool (e.g., 192.168.1.20-192.168.1.100).
- Interface: Select the interface that the pool will be associated with.
- Network: Enter the subnet mask for the pool (e.g., 255.255.255.0).
- Gateway: Specify the default gateway for the pool (e.g., 192.168.1.1).

#### 2. Link DHCP Server to Pool
Navigate to **IP > DHCP Server** and select the DHCP server associated with the interface where the IP pool will be used.

- Select the "Address Pools" tab.
- Click the "+" button to create a new address pool.
- Select the IP pool created in the previous step from the "Pool" dropdown.

#### 3. Verify Configuration
Restart the DHCP server by running the following command:

```
/ip dhcp-server enable
```

Test the pool by connecting a DHCP client to the network. The client should be assigned an IP address from the specified pool.

### Complete Configuration Commands

```
/ip pool add name=Employee-Pool ranges=192.168.1.20-192.168.1.100 interface=ether1 network=255.255.255.0 gateway=192.168.1.1
/ip dhcp-server enable
```

### Common Pitfalls and Solutions

- **Error: DHCP client not getting IP address from pool:**
   - Verify that the DHCP server is enabled and running on the correct interface.
   - Ensure that the client is within the subnet range of the IP pool.
   - Check for any firewall rules that may be blocking DHCP traffic.
- **Error: IP pool range conflicts with existing static IP addresses:**
   - Modify the IP pool range to avoid overlapping with any static IP assignments.
   - Consider using a different interface or subnet for the IP pool.

### Verification and Testing Steps

- Connect a DHCP client to the network and observe that it obtains an IP address from the specified pool.
- Check the DHCP lease list to verify that the IP address is being assigned from the correct pool.

### Related Features and Considerations

- **IP Address Allocation:** IP pools allow for flexible and efficient assignment of IP addresses to multiple devices.
- **DHCP Failover:** Configure multiple IP pools and DHCP servers to provide redundancy and improve uptime.
- **DNS Integration:** Configure DNS settings within the IP pool to provide DNS resolution for DHCP clients.

### MikroTik REST API Examples

#### Endpoint: **`/ip/pool`**
#### Request Method: **GET**

```json
{
  "name": "Employee-Pool",
  "ranges": [
    "192.168.1.20-192.168.1.30",
    "192.168.1.50-192.168.1.100"
  ]
}
```

#### Response:

```json
[
  {
    "name": "Employee-Pool",
    "ranges": [
      "192.168.1.20-192.168.1.30",
      "192.168.1.50-192.168.1.100"
    ]
  }
]
```