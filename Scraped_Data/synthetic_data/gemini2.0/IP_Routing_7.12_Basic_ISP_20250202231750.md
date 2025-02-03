## IP Routing

### Configuration Scenario and Requirements

- Configure IP routing to allow traffic to flow between different subnets in an ISP network.
- Assign IP addresses to subnets and interfaces.
- Enable routing between the subnets.

### Step-by-Step Implementation

#### Assign IP Addresses to Subnets and Interfaces

```
/ip address
add address=192.168.1.1/24 interface=ether1
add address=192.168.2.1/24 interface=ether2
```

#### Enable Routing Between Subnets

```
/ip route
add gateway=192.168.1.1 dst-address=192.168.2.0/24
add gateway=192.168.2.1 dst-address=192.168.1.0/24
```

### Complete Configuration Commands

```
/ip address
add address=192.168.1.1/24 interface=ether1
add address=192.168.2.1/24 interface=ether2

/ip route
add gateway=192.168.1.1 dst-address=192.168.2.0/24
add gateway=192.168.2.1 dst-address=192.168.1.0/24
```

### Common Pitfalls and Solutions

- **Incorrect IP addresses or subnet masks:** Ensure that the IP addresses and subnet masks are valid and match the network topology.
- **Missing gateway:** Add a gateway to the route to specify the next hop for traffic towards the destination subnet.
- **Firewall rules:** Check that there are no firewall rules blocking traffic between the subnets.

### Verification and Testing Steps

- **Ping:** Test connectivity between hosts in different subnets using the ping command (e.g., `ping 192.168.2.10`).
- **Traceroute:** Use traceroute to verify the path of packets between hosts (e.g., `traceroute 192.168.2.10`).

### Related Features and Considerations

- **Static Routing:** Configured manually as described in this scenario.
- **Dynamic Routing Protocols:** Automatically discover and maintain routing information (e.g., OSPF, RIP).
- **Policy Routing:** Direct traffic based on specific criteria (e.g., source IP, destination IP).

### MikroTik REST API Examples

**API Endpoint:** `/ip/route`

**Request Method:** POST

**Example JSON Payload:**

```
{
  "dst-address": "192.168.2.0/24",
  "gateway": "192.168.1.1"
}
```

**Expected Response:**

```
{
  "ret": 0
}
```