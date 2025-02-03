## IP Pools

### 1. Configuration Scenario and Requirements

- Create and configure IP pools to automatically assign IP addresses to clients on different subnets.
- Implement features like DHCP failover and address reservation for reliability and control.
- Ensure availability of IP addresses for connected devices within a specified range.

### 2. Step-by-Step Implementation

**2.1 Create a New IP Pool**

- Open WinBox and navigate to **IP > Pool**
- Click the "Add" button
- Specify the following parameters:
    - Name: CustomPool1
    - Ranges: 192.168.1.10-192.168.1.254
    - Next Pool: None
    - Router: (Current Router)

**2.2 Enable DHCP Server**

- Navigate to **IP > DHCP Server**
- Click the "Add" button
- Configure the following:
    - Interface: eth1
    - Address Pool: CustomPool1
    - Lease Time: 24 hours

### 3. Complete Configuration Commands

```
/ip pool
add name=CustomPool1 ranges=192.168.1.10-192.168.1.254 next-pool=none
/ip dhcp-server
add interface=eth1 address-pool=CustomPool1 lease-time=86400s
```

### 4. Common Pitfalls and Solutions

- **IP address conflict**: Ensure that the specified IP range is not already in use on the network.
- **DHCP lease expiration**: Monitor the DHCP server logs to ensure that clients are renewing their addresses regularly.
- **Address reservation**: Configure static IP addresses for critical devices outside the IP pool range.

### 5. Verification and Testing Steps

- Ping a client to verify IP address assignment
- Check the DHCP server logs to ensure lease distribution
- Connect additional clients to verify availability

### 6. Related Features and Considerations

- **DHCP Failover**: Use multiple DHCP servers with the "next-pool" parameter to provide redundancy.
- **DNS**: Configure DNS servers for the DHCP clients to resolve domain names.
- **Static Leases**: Create static leases for devices that require permanent IP addresses.

### 7. MikroTik REST API Examples

**Add IP Pool:**

**Endpoint**: `/ip/pool`

**Request Method**: POST

**JSON Payload**:

```json
{
  "name": "CustomPool1",
  "ranges": ["192.168.1.10-192.168.1.254"]
}
```

**Expected Response**:

```json
{
  "id": 1
}
```

**Add DHCP Server:**

**Endpoint**: `/ip/dhcp-server`

**Request Method**: POST

**JSON Payload**:

```json
{
  "interface": "eth1",
  "address-pool": "CustomPool1",
  "lease-time": 86400
}
```

**Expected Response**:

```json
{
  "id": 1
}
```