## IP Pools

### Configuration Scenario and Requirements

In an enterprise network, a dedicated IP pool is required to assign dynamic IP addresses to devices connecting to the network. The IP pool should be configured with a range of available IP addresses and subnet mask.

### Step-by-Step Implementation

1. **Create a new IP pool**
   - Navigate to IP > Pool
   - Click **+** to create a new pool
   - Enter a **Name** for the pool
   - Select the **Address Range** and **Subnet**

2. **Add hosts to the IP pool**
   - Navigate to IP > Addresses
   - Click **+** to create a new IP address
   - Enter the **IP Address**, **Subnet**, and **Interface**
   - Select the **IP Pool** created in step 1 from the dropdown

3. **Assign IP addresses from the pool**
   - Navigate to IP > DHCP Server
   - Enable the DHCP server
   - Select the **Interface** to listen on
   - Specify the **Pool** to assign addresses from

```
/ip pool add name=my-ip-pool ranges=192.168.10.10-192.168.10.50
/ip address add address=192.168.10.10/24 interface=ether1 pool=my-ip-pool
/ip dhcp-server add interface=ether1 enable=yes address-pool=my-ip-pool
/ip dhcp-server lease print
```

### Common Pitfalls and Solutions

- **DHCP server not responding:** Ensure that the DHCP server is enabled and listening on the correct interface.
- **IP address conflict:** Verify that the IP address range specified in the IP pool does not overlap with any other IP address ranges in use on the network.
- **Devices not getting IP addresses:** Check the DHCP configuration on the client devices and ensure that they are configured to obtain an IP address automatically.

### Verification and Testing Steps

1. Use an IP scanner to verify that the IP addresses are being assigned from the specified pool.
2. Test the network connectivity of devices assigned IP addresses from the pool.
3. Monitor the DHCP server logs to ensure there are no errors or issues.

### Related Features and Considerations

- **Static IP addresses:** For devices that require a fixed IP address, static IP addresses can be configured manually or through the DHCP reservation feature.
- **IP address conflict detection:** MikroTik includes a tool called "IP conflict detection" that can help identify and resolve IP address conflicts.

### MikroTik REST API Examples

**Create IP Pool**

```
curl -X POST -H "Content-Type: application/json" -u user:password http://192.168.1.1/rest/ip/pool -d '{"name": "my-ip-pool", "ranges": ["192.168.10.10-192.168.10.50"]}'
```

**Add Host to IP Pool**

```
curl -X POST -H "Content-Type: application/json" -u user:password http://192.168.1.1/rest/ip/address -d '{"address": "192.168.10.10/24", "interface": "ether1", "pool": "my-ip-pool"}'
```

**Get DHCP Leases**

```
curl -X GET -H "Content-Type: application/json" -u user:password http://192.168.1.1/rest/ip/dhcp-server/lease/print
```