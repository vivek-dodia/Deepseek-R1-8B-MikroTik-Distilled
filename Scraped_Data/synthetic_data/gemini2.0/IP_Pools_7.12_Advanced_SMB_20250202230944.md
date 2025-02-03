**Configuration Scenario and Requirements**

Configure an IP pool in RouterOS to assign IPv4 addresses automatically to DHCP clients.

**Step-by-Step Implementation**

1. Create an IP address pool:
   ```
   /ip pool
   add name=pool1 ranges=192.168.1.2-192.168.1.254
   ```

2. Link the pool to a DHCP server:
   ```
   /ip dhcp-server
   set pool=pool1 interfaces=ether1
   ```

**Complete Configuration Commands**

```
/ip pool add name=pool1 ranges=192.168.1.2-192.168.1.254
/ip dhcp-server set pool=pool1 interfaces=ether1
```

**Common Pitfalls and Solutions**

- Ensure that the DHCP server interface is the correct interface connecting to clients.
- Verify that the subnet mask and default gateway for the pool are correct.
- Check for IP address conflicts or duplicate pools.

**Verification and Testing Steps**

1. Connect a DHCP client to the network.
2. Check the client's IP address using `ipconfig` or `ifconfig`.
3. Verify that the IP address is assigned from the pool range.

**Related Features and Considerations**

- Binding addresses from a pool to specific MAC addresses can be managed using the MAC binding feature.
- The DHCP server can be configured to provide additional options, such as DNS servers and lease times.
- Managing multiple DHCP servers and IP pools requires careful planning and coordination.

**MikroTik REST API Examples**

**Endpoint:** `/router/ip/pool`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "name": "pool1"
}
```

**Expected Response:**

```json
[
  {
    "comment": null,
    "disabled": false,
    "has-arp": true,
    "name": "pool1",
    "ranges": "192.168.1.2-192.168.1.254"
  }
]
```