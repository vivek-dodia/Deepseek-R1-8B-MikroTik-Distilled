## IP Pools

**Configuration Scenario and Requirements**

- Create an IP pool to assign IP addresses to DHCP clients.
- Configure the pool with a specific IP address range, subnet mask, and gateway.

**Step-by-Step Implementation**

1. **Create IP Pool:** Navigate to **IP** > **Pools** and click on **+** to create a new pool.

2. **Configure Pool Properties:**
   - **Name:** Specify a descriptive name for the pool.
   - **Ranges:** Enter the IP address range to assign to clients, e.g., `192.168.1.10-192.168.1.50`.
   - **Next Pool:** Leave this blank for the first pool. For subsequent pools, specify the name of the previous pool to create a sequential range.
   - **Comment:** Add an optional description.

3. **Set Gateway and DNS:**
   - **Gateway:** Specify the default gateway for the pool, e.g., `192.168.1.1`.
   - **DNS Servers:** Enter a comma-separated list of DNS server addresses, e.g., `8.8.8.8, 1.1.1.1`.

4. **Set Lease Parameters:**
   - **Lease Time:** Specify the duration of IP lease, e.g., `86400s` for 24 hours.
   - **Default Lease Time:** Set the initial lease time, e.g., `300s` for 5 minutes.
   - **Max Lease Time:** Set the maximum allowable lease time, e.g., `86400s`.

5. **Save Configuration:** Click **Apply** to save the changes.

**Complete Configuration Commands**

```
/ip pool add name=Pool1 ranges=192.168.1.10-192.168.1.50 gateway=192.168.1.1 dns-servers=8.8.8.8,1.1.1.1 lease-time=86400s default-lease-time=300s max-lease-time=86400s
```

**Common Pitfalls and Solutions**

- **IP Address Conflict:** Ensure the IP address range does not overlap with other existing networks or subnets.
- **Gateway Misconfiguration:** Verify that the specified gateway is reachable and responds to ping requests.
- **DNS Failure:** Check if the configured DNS servers are accessible and resolving correctly.
- **Lease Time Mismatch:** Avoid setting a default lease time longer than the maximum lease time, as it may lead to expired leases.

**Verification and Testing Steps**

- Check the **IP** > **Leases** list to confirm clients are assigned IP addresses from the pool.
- Test Internet connectivity by pinging external websites.
- Use a DNS lookup tool to verify DNS resolution.

**Related Features and Considerations**

- **IP Binding:** Use **/ip dhcp-server lease** to bind specific MAC addresses to IP addresses from the pool.
- **Pool Suppression:** Enable **Suppress MAC on Lease:** to prevent a client from renewing lease if its MAC address has changed.
- **Lease Expiration Notifications:** Configure **/ip dhcp-server lease expire-list** to receive notifications when leases are about to expire.

## MikroTik REST API Examples

**Get IP Pool List:**

**API Endpoint:** `/ip/pool/print`
**Request Method:** GET
**Expected Response:**

```json
[
  {
    "gateway": "192.168.1.1",
    "name": "Pool1",
    "ranges": [
      "192.168.1.10-192.168.1.50"
    ]
  }
]
```

**Create IP Pool:**

**API Endpoint:** `/ip/pool/add`
**Request Method:** POST
**JSON Payload:**

```json
{
  "gateway": "192.168.1.1",
  "name": "Pool2",
  "ranges": [
    "192.168.1.51-192.168.1.100"
  ]
}
```

**Expected Response:**

```json
{
  "id": 12
}
```