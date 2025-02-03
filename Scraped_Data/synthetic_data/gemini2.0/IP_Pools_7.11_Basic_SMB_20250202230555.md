**Topic: IP Pools**

## Configuration Scenario and Requirements

- Assign IP addresses dynamically to clients on a local network.
- Create multiple IP pools with different ranges and settings.

## Step-by-Step Implementation

1. **Create an IP Pool:**
   - Navigate to IP > Pools in RouterOS.
   - Click on the "+" button to create a new pool.
   - Configure the following parameters:
     - **Name:** A descriptive name for the pool.
     - **Range:** The range of IP addresses to assign from.
     - **Next Available:** The first IP address to be assigned from the range.
     - **Comment:** (Optional) Any additional notes or descriptions.

2. **Assign the Pool to an Interface:**
   - Navigate to IP > Interfaces.
   - Select the interface you want to assign the pool to.
   - Go to the "Address" tab.
   - Click on the "+" button to add a new IP address.
   - In the "Pool" field, select the IP pool you created.

3. **Configure Lease Settings:**
   - Navigate back to IP > Pools.
   - Select the pool you want to configure.
   - In the "Lease" tab, configure the following parameters:
     - **Lease Time:** The amount of time each IP address lease will be valid for.
     - **Max Lease Time:** The maximum amount of time a lease can be extended.
     - **ARP Limit:** The maximum number of ARP entries that can be associated with a single IP address.

4. **Enable DHCP Server:**
   - Navigate to IP > DHCP Server.
   - Enable the DHCP server by setting the "Enabled" parameter to "yes".
   - Select the IP pool you created in the "Default Lease Time" field.

## Complete Configuration Commands

```
/ip pool
add name=my-pool range=192.168.1.10-192.168.1.254 next=192.168.1.10
/ip address
add interface=ether1 address=192.168.1.1/24 pool=my-pool
/ip pool my-pool
set lease-time=1h
set max-lease-time=2h
set arp-limit=100
/ip dhcp-server
set enabled=yes
set default-lease-time=my-pool
```

## Common Pitfalls and Solutions

- **IP Address Conflicts:** Ensure that the IP pool range does not overlap with any existing static IP addresses on the network.
- **Lease Expiry:** Monitor the lease expiry times and renew or rebind IP addresses as necessary.
- **Exhausted IP Pool:** Adjust the pool range or create additional pools to accommodate growing network needs.

## Verification and Testing Steps

1. Connect a client to the network.
2. Check the client's IP address to verify that it has been assigned from the pool.
3. Run an IP scan to ensure that there are no IP address conflicts.
4. Test internet connectivity from the client.

## Related Features and Considerations

- **Static IPs:** For devices that require fixed IP addresses, use static IP addresses instead of IP pool assignments.
- **DHCP Snooping:** Enable DHCP snooping to prevent malicious devices from assigning rogue IP addresses.
- **IPv6 Pools:** Follow similar steps to create and configure IPv6 IP pools for IPv6 networks.

## MikroTik REST API Examples

**API Endpoint:** /api/ip/pool

**Request Method:** PUT

**Example JSON Payload:**

```json
{
  "name": "my-pool",
  "range": "192.168.1.10-192.168.1.254",
  "next": "192.168.1.10",
  "lease-time": "1h",
  "max-lease-time": "2h",
  "arp-limit": 100
}
```

**Expected Response:**

```json
{
  "name": "my-pool",
  "range": "192.168.1.10-192.168.1.254",
  "next": "192.168.1.10",
  "lease-time": "1h",
  "max-lease-time": "2h",
  "arp-limit": 100
}
```