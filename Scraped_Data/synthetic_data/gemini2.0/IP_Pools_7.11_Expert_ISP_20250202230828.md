## IP Pools

### Configuration Scenario and Requirements

In this scenario, we will create and manage IP pools for dynamic IP address assignment to clients on an ISP network. The requirements are:

- Configure IP pools with specific subnet ranges and lease times.
- Assign IP pools to interfaces or DHCP servers for address allocation.
- Monitor and manage IP pool usage.

### Step-by-Step Implementation

#### Create an IP Pool

```
/ip pool add name=pool1 ranges=10.10.10.0/24
```

**Parameters:**

| Parameter | Description |
|---|---|
| name | Name of the IP pool |
| ranges | Subnet range(s) to allocate from the pool |

#### Assign an IP Pool to an Interface

```
/interface ethernet set ether1 dhcp-pool=pool1
```

**Parameters:**

| Parameter | Description |
|---|---|
| ether1 | Ethernet interface to assign the pool to |
| dhcp-pool | Name of the IP pool to assign |

#### Assign an IP Pool to a DHCP Server

```
/ip dhcp-server add interface=dhcp1 address-pool=pool1 lease-time=24h
```

**Parameters:**

| Parameter | Description |
|---|---|
| interface | DHCP server interface |
| address-pool | Name of the IP pool to assign |
| lease-time | Lease time for IP addresses (default: 1h) |

#### Monitor IP Pool Usage

```
/ip pool print
```

| Field | Description |
|---|---|
| name | Name of the IP pool |
| ranges | Allocated subnet range(s) |
| used-ranges | Currently used subnet range(s) |
| total | Total number of addresses in the pool |
| available | Number of available addresses |
| leases | Number of active leases |

### Common Pitfalls and Solutions

- **Pool Exhaustion:** If all addresses in a pool are allocated, clients will not be able to obtain IP addresses. To resolve this, increase the subnet range or add more IP pools.
- **Overlapping Subnet Ranges:** Ensure that subnets assigned to different pools do not overlap, as this can lead to IP address conflicts.
- **Incorrect Lease Time:** Choose an appropriate lease time to prevent excessive network churn or IP address starvation.

### Verification and Testing Steps

- Verify that clients are obtaining IP addresses from the pool by checking their IP address configuration.
- Use the `/ip pool print` command to monitor pool usage and verify that it is functioning as expected.
- Test connectivity between clients and ensure that they can access the network resources.

### Related Features and Considerations

- **DHCP Relay:** Use DHCP relay to extend IP pool management to multiple subnets.
- **IP Address Management (IPAM):** Utilize MikroTik's IPAM features to automate IP address assignment and monitor pool usage.
- **IPv6 Support:** Configure IP pools for IPv6 address allocation using similar commands.

### MikroTik REST API Examples

#### Create an IP Pool

**API Endpoint:** `/ip/pool/add`

**Request Method:** POST

**JSON Payload:**

```
{
  "name": "pool1",
  "ranges": ["10.10.10.0/24"]
}
```

**Response:**

```
{
  "id": ":id"
}
```

#### Get IP Pool Information

**API Endpoint:** `/ip/pool/print`

**Request Method:** GET

**JSON Response:**

```
[
  {
    ".id": ":id",
    "name": "pool1",
    "ranges": ["10.10.10.0/24"],
    "total": 254,
    "available": 254,
    "leases": 0
  }
]
```