## IP Routing

### Configuration Scenario and Requirements

In this scenario, we configure IP routing on a MikroTik RouterOS 6.48 device to enable the routing of traffic between different subnets. The device will have two interfaces: one connected to the WAN with an IP address of 192.168.1.1/24 and the other connected to the LAN with an IP address of 192.168.2.1/24.

### Step-by-Step Implementation

**1. Enable IP Forwarding**

```
/ip firewall set forward=accept
```

**2. Add Default Gateway to LAN Interface**

```
/ip route add gateway=192.168.1.1
```

**3. Create a Static Route to the WAN**

```
/ip route add dst-address=192.168.1.0/24 gateway=192.168.2.1
```

### Complete Configuration Commands

```
/ip firewall set forward=accept
/ip route add gateway=192.168.1.1
/ip route add dst-address=192.168.1.0/24 gateway=192.168.2.1
```

### Common Pitfalls and Solutions

- **Forgetting to enable IP forwarding:** Ensure that the `forward` parameter in `/ip firewall set` is set to `accept`.
- **Incorrect gateway address:** Verify that the gateway address specified in `/ip route add` is correct.
- **Overlapping subnets:** Ensure that the subnets on the WAN and LAN interfaces do not overlap.

### Verification and Testing Steps

- **Ping between LAN and WAN interfaces:** Ping the WAN IP from the LAN interface and vice versa to verify connectivity.
- **Traceroute to an external destination:** Perform a traceroute from the LAN interface to an external website to observe the routing path.

### Related Features and Considerations

- **Policy routing:** Allows for customized routing based on specific criteria, such as source or destination IP addresses.
- **Virtual routing and forwarding (VRF):** Isolates routing tables into distinct instances, allowing for multiple routing domains on a single device.

### MikroTik REST API Examples

**Add a Static Route**

**API Endpoint:** `/api/routing/ip/route`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "dst-address": "192.168.1.0/24",
  "gateway": "192.168.2.1"
}
```

**Expected Response:**

```json
{
  "id": 1,
  "dst-address": "192.168.1.0/24",
  "gateway": "192.168.2.1",
  "installed": true
}
```