## IP Pools

### Configuration Scenario and Requirements

- Configure an IP pool to provide IP addresses to DHCP clients.
- The IP pool should use the 192.168.1.0/24 network.
- The DHCP server should provide IP addresses in the range of 192.168.1.100 to 192.168.1.200.
- The DHCP server should provide a default gateway of 192.168.1.1.
- The DHCP server should provide a DNS server of 8.8.8.8.

### Step-by-Step Implementation

1. Create a new pool in the "/ip pool" menu.
2. Set the "name" of the pool to "my-pool".
3. Set the "ranges" of the pool to "192.168.1.100-192.168.1.200".
4. Click the "OK" button to save the pool.
5. Create a new DHCP server in the "/ip dhcp-server" menu.
6. Set the "interface" of the DHCP server to the interface that will be used to provide IP addresses to clients.
7. Set the "address-pool" of the DHCP server to the pool that was created in step 4.
8. Set the "default-lease-time" of the DHCP server to the desired lease time for IP addresses.
9. Set the "max-lease-time" of the DHCP server to the maximum lease time for IP addresses.
10. Set the "dns-server" of the DHCP server to the desired DNS server.
11. Set the "gateway" of the DHCP server to the desired gateway.
12. Click the "OK" button to save the DHCP server.

### Complete Configuration Commands

```
/ip pool
add name=my-pool ranges=192.168.1.100-192.168.1.200
/ip dhcp-server
add interface=ether1 address-pool=my-pool default-lease-time=86400 max-lease-time=604800 dns-server=8.8.8.8 gateway=192.168.1.1
```

### Common Pitfalls and Solutions

- Ensure that the pool is assigned to the DHCP server.
- Ensure that the DHCP server is listening on the correct interface.
- Ensure that the firewall is not blocking the DHCP traffic.

### Verification and Testing Steps

1. Connect a client to the network.
2. Obtain an IP address from the DHCP server.
3. Verify that the IP address is in the range of 192.168.1.100 to 192.168.1.200.
4. Verify that the default gateway is 192.168.1.1.
5. Verify that the DNS server is 8.8.8.8.

### Related Features and Considerations

- IP pools can be used to provide IP addresses to a variety of devices, including computers, printers, and phones.
- IP pools can be used to create a variety of network configurations, includingVLANs and subnets.
- IP pools can be used to implement security measures, such as IP address filtering.

### MikroTik REST API Examples

**Endpoint:** `/api/ip/pool`

**Request Method:** POST

**Example JSON Payload:**

```
{
  "name": "my-pool",
  "ranges": [
    "192.168.1.100-192.168.1.200"
  ]
}
```

**Expected Response:**

```
{
  "id": 1,
  "name": "my-pool",
  "ranges": [
    "192.168.1.100-192.168.1.200"
  ]
}
```