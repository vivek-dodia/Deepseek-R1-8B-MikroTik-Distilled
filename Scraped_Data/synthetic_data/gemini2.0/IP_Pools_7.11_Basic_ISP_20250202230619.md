## IP Pools

### Configuration Scenario and Requirements

We want to configure an IP pool on our MikroTik RouterOS 7.11 device to dynamically assign IP addresses to clients in a specific subnet. The pool should have a range of addresses and a default gateway.

### Step-by-Step Implementation

**1. Create a new IP pool.**

```
/ip pool add name=my-ip-pool ranges=192.168.1.100-192.168.1.200
```

**2. Set the default gateway for the pool.**

```
/ip pool set my-ip-pool gateway=192.168.1.1
```

**3. Add the pool to the desired interface.**

```
/interface ip address add address=192.168.1.1/24 interface=ether1 ip-pool=my-ip-pool
```

### Complete Configuration Commands

```
/ip pool add name=my-ip-pool ranges=192.168.1.100-192.168.1.200
/ip pool set my-ip-pool gateway=192.168.1.1
/interface ip address add address=192.168.1.1/24 interface=ether1 ip-pool=my-ip-pool
```

### Common Pitfalls and Solutions

- **Incorrect IP address range:** Ensure the specified IP address range does not overlap with any existing IP addresses on the network.
- **Missing default gateway:** If a default gateway is not set, clients assigned addresses from the pool will not be able to access the internet or other network resources.
- **Interface mismatch:** Verify that the pool is added to the correct interface. If added to an incorrect interface, clients will not receive IP addresses from the pool.

### Verification and Testing Steps

1. Check the pool configuration: ```/ip pool print name=my-ip-pool```
2. Assign an IP address from the pool to a client: ```/ip dhcp-client print interface=ether1 detail```
3. Test internet connectivity from the client.

### Related Features and Considerations

- **DHCP server:** IP pools are typically used in conjunction with a DHCP server to automatically assign IP addresses to clients.
- **Firewall rules:** Ensure appropriate firewall rules are in place to allow traffic from and to the assigned IP addresses.

### MikroTik REST API Examples

**Endpoint:** `/ip/pool`

**Request Method:** POST

**JSON Payload:**

```json
{
  "name": "my-ip-pool",
  "ranges": [
    "192.168.1.100-192.168.1.200"
  ],
  "gateway": "192.168.1.1"
}
```

**Expected Response:**

```json
{
  "id": "1",
  "name": "my-ip-pool",
  "ranges": [
    "192.168.1.100-192.168.1.200"
  ],
  "gateway": "192.168.1.1"
}
```