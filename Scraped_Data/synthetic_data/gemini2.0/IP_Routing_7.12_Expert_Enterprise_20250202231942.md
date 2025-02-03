**IP Routing**

## Configuration Scenario and Requirements

This section provides detailed technical documentation for IP routing in MikroTik RouterOS 7.12, tailored for enterprise-scale networks. The configuration addresses the following requirements:

- Establish static IP routes for optimal traffic forwarding
- Create IP pools for dynamic IP address allocation
- Configure default routes for internet connectivity
- Utilize routing protocols to establish dynamic routing

## Step-by-Step Implementation

### Static IP Routing

1. Navigate to `/ip route` in RouterOS
2. Click on the "+" button to create a new static route
3. Configure the following parameters:

| Parameter | Description |
|---|---|
| **Dst. Address** | Destination IP address or network |
| **Gateway** | Next-hop gateway IP address |
| **Distance** | Administrative distance (default: 1) |

**Example:**

```
/ip route add dst-address=192.168.1.0/24 gateway=192.168.1.1
```

### IP Pools

1. Navigate to `/ip pool` in RouterOS
2. Click on the "+" button to create a new IP pool
3. Configure the following parameters:

| Parameter | Description |
|---|---|
| **Name** | Name of the IP pool |
| **Ranges** | IP address ranges within the pool |
| **DNS Server** | DNS server IP address (optional) |

**Example:**

```
/ip pool add name=dhcp-pool ranges=192.168.1.100-192.168.1.200 dns-server=8.8.8.8
```

### Default Routes

1. Navigate to `/ip route` in RouterOS
2. Click on the "Add Default Route" button
3. Configure the following parameters:

| Parameter | Description |
|---|---|
| **Gateway** | Gateway IP address for internet connectivity |
| **Distance** | Administrative distance (default: 1) |

**Example:**

```
/ip route add gateway=192.168.1.254
```

### Routing Protocols

1. Navigate to `/routing` in RouterOS
2. Select the desired routing protocol (e.g., OSPFv2, RIPv2)
3. Configure the necessary routing parameters

**Example for OSPFv2:**

```
/routing ospf instance ospf1 interface=ether1 hello-interval=10
```

## Complete Configuration Commands

```
/ip route add dst-address=192.168.1.0/24 gateway=192.168.1.1
/ip pool add name=dhcp-pool ranges=192.168.1.100-192.168.1.200 dns-server=8.8.8.8
/ip route add gateway=192.168.1.254
/routing ospf instance ospf1 interface=ether1 hello-interval=10
```

## Common Pitfalls and Solutions

- **No default route configured:** Verify that a default route is configured to allow internet connectivity.
- **Invalid IP pool range:** Ensure that the IP pool range does not overlap with other assigned IP addresses or subnets.
- **Routing loop:** Check for potential routing loops caused by multiple active routing protocols.
- **High administrative distance:** Assigning a high administrative distance to a route can prevent it from being used.

## Verification and Testing Steps

- Use the `/ip route print` command to verify the static routes and default route.
- Test IP address allocation from the IP pool using a DHCP client.
- Ping external hosts to ensure internet connectivity.
- Monitor routing table updates using the `/routing watch` command.

## Related Features and Considerations

- Policy-based routing can be used to prioritize or control traffic based on specific criteria.
- Virtual routing and forwarding (VRF) allows the creation of multiple routing tables within a single router.
- Load balancing can be implemented across multiple next-hop gateways.

## MikroTik REST API Examples

**Get Static Routes:**

```json
GET /api/v7/routing/routes?dst-address=192.168.1.0%2F24
```

**Response:**

```json
[
  {
    "dst-address": "192.168.1.0",
    "dst-network": "192.168.1.0/24",
    "comment": "",
    "gateway": "192.168.1.1",
    "distance": 1,
    "scope": 32
  }
]
```

**Create IP Pool:**

```json
POST /api/v7/ip/pool
{
  "name": "dhcp-pool",
  "ranges": [
    {
      "range": "192.168.1.100-192.168.1.200"
    }
  ],
  "dns-server": ["8.8.8.8"]
}
```

**Response:**

```json
{
  "id": "1",
  "name": "dhcp-pool",
  "ranges": [
    {
      "id": "1",
      "range": "192.168.1.100-192.168.1.200"
    }
  ],
  "dns-server": ["8.8.8.8"]
}
```