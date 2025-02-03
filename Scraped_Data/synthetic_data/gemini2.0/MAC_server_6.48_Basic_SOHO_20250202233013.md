**Topic: MAC Server**

**Configuration Level:** Basic

**Network Scale:** SOHO

**Configuration Scenario and Requirements:**

Configure a MAC server on a MikroTik RouterOS to provide dynamic IP address assignment based on MAC addresses.

**Step-by-Step Implementation:**

1. Create a DHCP pool:
```
/ip pool
add name=pool-name addresses=192.168.1.1-192.168.1.100 next-pool=""
```

2. Create a MAC address pool:
```
/ip mac-pool
add name=mac-pool-name
```

3. Enable MAC server on the interface:
```
/interface ethernet set ether1 mac-server=enabled
```

4. Bind the DHCP pool and MAC pool to the MAC server:
```
/interface ethernet mac-server set ether1 pool=pool-name mac-pool=mac-pool-name
```

**Complete Configuration Commands:**

```
/ip pool add name=pool-name addresses=192.168.1.1-192.168.1.100 next-pool=""
/ip mac-pool add name=mac-pool-name
/interface ethernet set ether1 mac-server=enabled
/interface ethernet mac-server set ether1 pool=pool-name mac-pool=mac-pool-name
```

**Common Pitfalls and Solutions:**

- Ensure that the interface where the MAC server is enabled is configured for DHCP and has an IP address assigned.
- Verify that the MAC pool has valid MAC addresses added.
- Check the firewall rules to ensure that DHCP and MAC server traffic is allowed.

**Verification and Testing Steps:**

- Connect a device with a known MAC address to the interface where the MAC server is enabled.
- Check the DHCP lease status on the device to verify that it has obtained an IP address from the pool.
- Ping the device to confirm that it has network connectivity.

**Related Features and Considerations:**

- IP Pools: Configuring DHCP pools allows for dynamic IP address assignment.
- MAC Address Pools: MAC address pools ensure that only authorized devices can obtain IP addresses from the DHCP server.
- DHCP Snooping: DHCP snooping prevents unauthorized DHCP servers from operating on the network.

**MikroTik REST API Example:**

**API Endpoint:**

```
/api/ip/mac-server
```

**Request Method:**

```
GET
```

**Example JSON Payload:**

```json
{
  "interface": "ether1",
  "pool": "pool-name",
  "mac-pool": "mac-pool-name"
}
```

**Expected Response:**

```json
{
  "enabled": true,
  "interface": "ether1",
  "pool": "pool-name",
  "mac-pool": "mac-pool-name"
}
```