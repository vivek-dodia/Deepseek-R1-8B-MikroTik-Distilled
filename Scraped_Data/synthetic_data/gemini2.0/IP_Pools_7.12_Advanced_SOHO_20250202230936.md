**Topic: IP Pools**

**1. Configuration Scenario and Requirements**

In this scenario, we will configure an IP pool for dynamic IP address assignment to clients on a local area network (LAN).

**2. Step-by-Step Implementation**

**2.1. Create IP Pool**

```
/ip pool add comment="LAN IP Pool"
name=lan-pool
ranges=192.168.1.10-192.168.1.254
```

**2.2. Assign IP Pool to Interface**

```
/interface bridge add address=192.168.1.1/24 bridge=bridge1
/ip dhcp-server add interface=bridge1 address-pool=lan-pool
```

**2.3. Configure DHCP Server**

```
/ip dhcp-server enable="yes"
```

**3. Complete Configuration Commands**

```
/ip pool add comment="LAN IP Pool" name=lan-pool ranges=192.168.1.10-192.168.1.254
/interface bridge add address=192.168.1.1/24 bridge=bridge1
/ip dhcp-server add interface=bridge1 address-pool=lan-pool
/ip dhcp-server enable="yes"
```

**4. Common Pitfalls and Solutions**

- **IP address conflict:** Ensure that the IP pool ranges do not overlap with any existing static IP addresses.
- **DHCP server not started:** Verify that the DHCP server is enabled with `/ip dhcp-server enable="yes"`.
- **Firewall rules:** Allow DHCP traffic on the interface where the IP pool is assigned.

**5. Verification and Testing Steps**

- **Ping from DHCP client:** Verify that a DHCP client can obtain an IP address from the pool by pinging a known IP address.
- **Check DHCP lease:** Run `/ip dhcp-server lease print address=192.168.1.100` to confirm the lease assignment.
- **Check IP address of client interface:** Use `/ip address print interface=gre0` to verify that the client interface has an IP address from the pool.

**6. Related Features and Considerations**

- **Network Address Translation (NAT):** Enable NAT to allow clients to access the internet.
- **Lease Time:** Configure the lease time for the IP addresses assigned by the DHCP server.
- **DNS Server:** Specify a DNS server for clients to resolve domain names.
- **Static IP Address Allocation:** Reserve specific IP addresses for devices that require static IP assignments.

**7. MikroTik REST API Examples**

**7.1. Create IP Pool**

**Endpoint:** `/ip/pool`
**Request Method:** POST
**Example JSON Payload:**
```
{
  "comment": "LAN IP Pool",
  "name": "lan-pool",
  "ranges": [
    "192.168.1.10-192.168.1.254"
  ]
}
```
**Expected Response:**
```
{
  "id": 8
}
```

**7.2. Assign IP Pool to Interface**

**Endpoint:** `/interface/bridge`
**Request Method:** POST
**Example JSON Payload:**
```
{
  "address": "192.168.1.1/24",
  "bridge": "bridge1"
}
```
**Expected Response:**
```
{
  "id": 10
}
```

**7.3. Configure DHCP Server**

**Endpoint:** `/ip/dhcp-server`
**Request Method:** POST
**Example JSON Payload:**
```
{
  "interface": "bridge1",
  "address-pool": "lan-pool"
}
```
**Expected Response:**
```
{
  "id": 11
}
```

**7.4. Enable DHCP Server**

**Endpoint:** `/ip/dhcp-server/settings`
**Request Method:** PUT
**Example JSON Payload:**
```
{
  "enabled": true
}
```
**Expected Response:**
```
{
  "enabled": true
}
```