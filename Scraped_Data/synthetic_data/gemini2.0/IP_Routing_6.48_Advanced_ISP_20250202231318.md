## IP Routing

### Configuration Scenario and Requirements

- A MikroTik router is required with RouterOS 6.48 or higher.
- The router should have multiple network interfaces connected to different subnets.
- The goal is to configure IP routing on the router to allow communication between different subnets.

### Step-by-Step Implementation

1. **Enable IP forwarding on the router.**

   ```
   /ip firewall set forwarding=on
   ```

2. **Add static routes to the routing table.**

   To add a static route to a subnet, use the following command:

   ```
   /ip route add dst-address=10.10.10.0/24 gateway=192.168.1.1
   ```

   Where:
   - `dst-address` is the destination subnet you want to reach.
   - `gateway` is the IP address of the next-hop router or gateway.

3. **Configure firewall rules to allow traffic through the router.**

   To allow traffic from one subnet to another, create a firewall rule using the following command:

   ```
   /ip firewall add chain=forward action=accept in-interface=ether1 out-interface=ether2 src-address=10.10.10.0/24 dst-address=192.168.1.0/24
   ```

   Where:
   - `chain` is the firewall chain you want to add the rule to.
   - `action` is the action you want the rule to perform (accept, drop, etc.).
   - `in-interface` is the interface that traffic is coming in on.
   - `out-interface` is the interface that traffic is going out on.
   - `src-address` is the source IP address or subnet.
   - `dst-address` is the destination IP address or subnet.

### Complete Configuration Commands

```
/ip firewall set forwarding=on
/ip route add dst-address=10.10.10.0/24 gateway=192.168.1.1
/ip firewall add chain=forward action=accept in-interface=ether1 out-interface=ether2 src-address=10.10.10.0/24 dst-address=192.168.1.0/24
```

### Common Pitfalls and Solutions

- **Make sure that IP forwarding is enabled on the router.**
- **Check that the static routes are configured correctly.** Verify that the destination subnet and gateway IP address are correct.
- **Ensure that firewall rules are in place to allow traffic through the router.** Make sure that the firewall rules are configured to allow traffic from the correct source and destination subnets.

### Verification and Testing Steps

- **Test connectivity between different subnets.** Ping from one subnet to another to verify that traffic is flowing correctly.
- **Check the routing table.** Use the `/ip route print` command to view the routing table and ensure that the static routes are present.
- **Examine the firewall rules.** Use the `/ip firewall print` command to view the firewall rules and ensure that they are configured correctly.

### Related Features and Considerations

- **Policy routing** can be used to control how traffic is routed through the router.
- **Virtual routing and forwarding (VRF)** can be used to create multiple virtual routers on a single physical router.
- **Quality of service (QoS)** can be used to prioritize traffic and ensure that critical traffic is handled correctly.

### MikroTik REST API Examples

**Get the current routing table:**

**API Endpoint:** `/routing/route`

**Request Method:** GET

**Example JSON Payload:**

```JSON
{}
```

**Expected Response:**

```JSON
[
  {
    "dst-address": "0.0.0.0/0",
    "gateway": "192.168.1.1",
    "distance": "1"
  },
  {
    "dst-address": "192.168.1.0/24",
    "gateway": null,
    "distance": "0"
  }
]
```

**Add a static route:**

**API Endpoint:** `/routing/route`

**Request Method:** POST

**Example JSON Payload:**

```JSON
{
  "dst-address": "10.10.10.0/24",
  "gateway": "192.168.1.1"
}
```

**Expected Response:**

```JSON
{
  "dst-address": "10.10.10.0/24",
  "gateway": "192.168.1.1",
  "distance": "1"
}
```

**Delete a static route:**

**API Endpoint:** `/routing/route/{route-id}`

**Request Method:** DELETE

**Example JSON Payload:**

```JSON
{}
```

**Expected Response:**

```JSON
{
  "dst-address": "10.10.10.0/24",
  "gateway": "192.168.1.1",
  "distance": "1"
}
```