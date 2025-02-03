## IP Pools

### Configuration Scenario and Requirements

Configure IP pools to dynamically assign IP addresses to clients on a MikroTik RouterOS device.

### Step-by-Step Implementation

1. **Create IP Pool:**
   ```
   /ip pool add name=pool1 ranges=10.1.1.0/24
   ```

2. **Configure DHCP Server:**
   ```
   /ip dhcp-server add interface=ether1 pool=pool1
   ```
   - Replace `ether1` with the actual interface name.

3. **Set Router Default Gateway:**
   ```
   /ip route add gateway=10.1.1.1
   ```
   - Replace `10.1.1.1` with the actual gateway address.

### Complete Configuration Commands

```
/ip pool add name=pool1 ranges=10.1.1.0/24
/ip dhcp-server add interface=ether1 pool=pool1
/ip route add gateway=10.1.1.1
```

### Common Pitfalls and Solutions

- **Incorrect IP Range:** Ensure the specified IP range does not overlap with any existing networks or reserved IP addresses.
- **No Default Gateway:** Configuring the router's default gateway is crucial for clients to access the internet.
- **DNS Not Configured:** Provide DNS server addresses in `/ip dhcp-server` to enable clients to resolve domain names.

### Verification and Testing Steps

1. Connect a client device to the configured interface.
2. Verify if the client obtains an IP address from the pool using `ip address` or `ifconfig` (on Linux).
3. Test internet connectivity by pinging an external IP address.

### Related Features and Considerations

- **DHCP Lease:** Customize DHCP lease time using `/ip dhcp-server lease add`.
- **Static Address:** Add specific clients with fixed IP addresses to the pool using `/ip dhcp-server lease add address=10.1.1.100 mac-address=00:00:00:00:00:01`.
- **Multiple DHCP Servers:** Use multiple DHCP servers with different pools for different subnets.

### MikroTik REST API Examples

**Endpoint:** `/ip/pool`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "pool1",
  "ranges": ["10.1.1.0/24"]
}
```

**Expected Response:**

```json
{
  "resource": "ip/pool/pool1"
}
```