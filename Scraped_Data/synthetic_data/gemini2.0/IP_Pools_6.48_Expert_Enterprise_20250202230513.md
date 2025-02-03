## IP Pools

### 1. Configuration Scenario and Requirements

- Create and configure IP pools for dynamic IP assignment in an enterprise network.
- Set up multiple IP pools with different IP ranges, gateways, and DNS servers.
- Integrate IP pools with DHCP servers for IP address allocation.

### 2. Step-by-Step Implementation

#### 2.1 Create an IP Pool

- Navigate to IP > Pool
- Click the "+" button to create a new pool
- Configure the following parameters:
    - Name: Enter a descriptive name for the pool
    - Ranges: Specify the IP range to be assigned from the pool
    - Gateway: Enter the default gateway for the pool
    - DNS Servers: Enter the IP addresses of the DNS servers to be used by devices in the pool

#### 2.2 Create Multiple IP Pools

- Repeat step 2.1 to create multiple IP pools with different configurations.
- Ensure that the IP ranges do not overlap to avoid IP address conflicts.

#### 2.3 Integrate with DHCP Server

- Navigate to IP > DHCP Server
- Click the "+" button to create a new DHCP server
- Configure the following parameters:
    - Interface: Select the network interface that will use the IP pool
    - Address pool: Select the IP pool created in step 2.1 or 2.2
    - Lease time: Specify the duration for which IP addresses are leased to devices

### 3. Complete Configuration Commands

**IP Pool Creation:**

```
/ip pool add name=Pool1 ranges=192.168.1.0/24 gateway=192.168.1.1 dns-server=8.8.8.8,8.8.4.4
```

**DHCP Server Configuration:**

```
/ip dhcp-server add interface=ether1 address-pool=Pool1 lease-time=86400
```

### 4. Common Pitfalls and Solutions

- **IP Range Overlaps:** Ensure that IP ranges assigned to different pools do not overlap, as this can lead to IP address conflicts.
- **Gateway Configuration:** Make sure the gateway specified in the IP pool is reachable by devices using it.
- **DNS Server Availability:** Verify that the DNS servers configured in the IP pool are accessible and functional.

### 5. Verification and Testing Steps

- **IP Pool Status:** Navigate to IP > Pool to check the status of the created pools.
- **DHCP Lease Status:** Navigate to IP > DHCP Server > Leases to verify that devices are obtaining IP addresses from the pool.
- **Assigned IP Addresses:** Check the IP addresses assigned to devices using commands like `/ip address print` or `/ip address arp`.

### 6. Related Features and Considerations

- **IP Addressing:** Configure IP addresses for specific devices or subnets.
- **IP Routing:** Set up routing rules to direct traffic between networks.
- **IP Settings:** Adjust advanced IP-related settings, such as fragmentation and TCP/IP parameters.
- **MAC Server:** Manage MAC addresses and assign static IP addresses based on MAC addresses.

### 7. MikroTik REST API Examples

#### 7.1 Create an IP Pool

**API Endpoint:** `/api/ip/pool`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "Pool1",
  "ranges": ["192.168.1.0/24"],
  "gateway": "192.168.1.1",
  "dns-server": ["8.8.8.8", "8.8.4.4"]
}
```

**Expected Response:**

```json
{
  "id": "1",
  "name": "Pool1",
  "ranges": ["192.168.1.0/24"],
  "gateway": "192.168.1.1",
  "dns-server": ["8.8.8.8", "8.8.4.4"]
}
```

#### 7.2 Create a DHCP Server

**API Endpoint:** `/api/ip/dhcp-server`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "interface": "ether1",
  "address-pools": ["Pool1"],
  "lease-time": 86400
}
```

**Expected Response:**

```json
{
  "id": "1",
  "interface": "ether1",
  "address-pools": ["Pool1"],
  "lease-time": 86400
}
```