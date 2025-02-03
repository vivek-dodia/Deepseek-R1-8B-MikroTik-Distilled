## Routing in RouterOS

### IP Routing

**Scenario and Requirements:**

Configure IP routing on a MikroTik router to allow communication between different subnets.

### Step-by-Step Implementation:

1. **Add IP Addresses to Interfaces:** Assign IP addresses to the relevant interfaces using the `/ip address` command.

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
```

2. **Add Default Gateway:** Specify the default gateway for each subnet using the `/ip route` command.

```
/ip route add gateway=192.168.1.254 dst-address=0.0.0.0/0
/ip route add gateway=192.168.2.254 dst-address=0.0.0.0/0
```

### Complete Configuration Commands:

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
/ip route add gateway=192.168.1.254 dst-address=0.0.0.0/0
/ip route add gateway=192.168.2.254 dst-address=0.0.0.0/0
```

### Troubleshooting:

- **Check if IP addresses are correct:** Ensure the IP addresses and subnet masks are configured accurately.
- **Verify default gateways:** Confirm that the default gateways are reachable and responding.
- **Examine routing table:** Use the `/ip route print` command to check if the routing table contains the correct routes.

### Related Features and Considerations:

- **Policy Routing:** Allows you to define specific routing rules based on various criteria.
- **Virtual Routing and Forwarding (VRF):** Enables you to create multiple virtual routing tables, each with its own set of routing rules.
- **Static Routes:** Provides an explicit route to a destination without relying on routing protocols.

### REST API Example:

**API Endpoint:** `/ip/route`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "dst-address": "192.168.3.0/24",
  "gateway": "192.168.2.254"
}
```

**Expected Response:**

```json
{
  "ret": "success"
}
```