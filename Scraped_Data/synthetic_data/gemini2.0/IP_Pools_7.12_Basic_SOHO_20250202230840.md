## IP Pools

### Configuration Scenario and Requirements

- Set up an IPv4 network with a fixed range of IP addresses for host devices.
- Manage IP address allocation and renewal.

### Step-by-Step Implementation

**1. Create an IP Pool**

```
/ip pool add name=my-pool ranges=192.168.1.10-192.168.1.50
```

| Parameter | Description |
|---|---|
| name | Name of the IP pool |
| ranges | Range of IP addresses in the pool |

**2. Link the IP Pool to an Interface**

```
/interface ip address add address=192.168.1.1/24 interface=ether1 pool=my-pool
```

| Parameter | Description |
|---|---|
| address | IP address of the interface |
| interface | Name of the interface |
| pool | Name of the IP pool |

### Complete Configuration Commands

```
/ip pool add name=my-pool ranges=192.168.1.10-192.168.1.50
/interface ip address add address=192.168.1.1/24 interface=ether1 pool=my-pool
```

### Common Pitfalls and Solutions

- **Duplicate IP Addresses:** Ensure that the IP address range specified in the pool does not overlap with any existing IP addresses in the network.
- **Invalid Interface:** Verify that the specified interface is enabled and configured correctly.
- **DHCP Disabled:** Make sure that DHCP is enabled on the interface if you want to dynamically assign IP addresses from the pool.

### Verification and Testing Steps

- Ping a host device to verify that it has received an IP address from the pool.
- Check the interface configuration (`/interface ip address print`) to confirm the assigned IP address.

### Related Features and Considerations

- DHCP Server: To automatically assign IP addresses from the pool, you can configure a DHCP server on the router.
- Address Reservations: You can reserve specific IP addresses within the pool for specific devices.
- IP Address Leases: By default, IP addresses are assigned with a lease time. You can configure the lease time to control how long devices can hold the addresses.

### MikroTik REST API Examples

#### Endpoint: `/ip/pool`

**Request Method:** GET

**Example Request:**

```json
{
  "id": "my-pool"
}
```

**Example Response Body:**

```json
{
  "id": "my-pool",
  "name": "my-pool",
  "ranges": [
    "192.168.1.10-192.168.1.50"
  ]
}
```

#### Endpoint: `/ip/pool/add`

**Request Method:** POST

**Example Request Body:**

```json
{
  "name": "my-pool",
  "ranges": [
    "192.168.1.10-192.168.1.50"
  ]
}
```