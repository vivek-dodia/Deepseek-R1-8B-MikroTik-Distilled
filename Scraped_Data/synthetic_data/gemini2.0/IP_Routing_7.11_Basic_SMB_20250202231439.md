## IP Routing

### Configuration Scenario and Requirements

**Objective:** Configure IP routing on a MikroTik RouterOS device to enable communication between different subnets.

### Step-by-Step Implementation

#### 1. Configure IP Addresses on Interfaces

Assign IP addresses to the network interfaces connected to different subnets.

**CLI Command:**

```
/interface ip address
add address=192.168.1.1/24 interface=ether1
add address=192.168.2.1/24 interface=ether2
```

#### 2. Configure Static Routes

Create static routes to direct traffic to specific subnets not directly connected to the router.

**CLI Command:**

```
/ip route
add dst-address=192.168.3.0/24 gateway=192.168.2.2
```

**Parameter:**

- `dst-address`: Destination IP address or subnet
- `gateway`: IP address of the next hop to reach the destination

#### 3. Configure Default Route

If the destination subnet is not directly connected or covered by a static route, configure a default route.

**CLI Command:**

```
/ip route
add gateway=192.168.2.2
```

#### 4. Enable IP Forwarding

Ensure that IP forwarding is enabled to allow traffic to be forwarded through the router.

**CLI Command:**

```
/ip firewall
set forward=accept
```

### Complete Configuration Commands

```
/interface ip address
add address=192.168.1.1/24 interface=ether1
add address=192.168.2.1/24 interface=ether2

/ip route
add dst-address=192.168.3.0/24 gateway=192.168.2.2
add gateway=192.168.2.2

/ip firewall
set forward=accept
```

### Common Pitfalls and Solutions

- **No Internet access:** Verify IP addresses and gateways are correct. Ensure that the default route is pointing to the correct gateway.
- **Traffic not being routed:** Check if the destination subnet is covered by a static route. If not, add the appropriate static route.
- **Packet loss:** Monitor traffic using tools like `/interface monitor-traffic` to identify any potential packet drops.

### Verification and Testing Steps

- **Ping:** Test connectivity to different subnets using the `/ping` command.
- **Traceroute:** Trace the path taken by packets to reach a destination using `/traceroute`.

### Related Features and Considerations

- **Policy routing:** Advanced routing rules can be configured to control the path taken by specific traffic based on criteria such as source/destination IP, port, etc.
- **Virtual routing and forwarding (VRF):** Multiple routing tables can be created to isolate different sets of subnets and control routing between them.
- **Security:** IP routing should be configured with security in mind, including firewall rules to prevent unauthorized access.

### MikroTik REST API Examples

**Example 1: Add a static route**

**Endpoint:** `/routing/ip/route`

**Request Method:** POST

**JSON Payload:**

```json
{
  "dst-address": "192.168.3.0/24",
  "gateway": "192.168.2.2"
}
```

**Example 2: Get all IP routes**

**Endpoint:** `/routing/ip/route`

**Request Method:** GET

**Expected Response:**

```json
[
  {
    "id": 1,
    "dst-address": "192.168.3.0/24",
    "gateway": "192.168.2.2",
    "disabled": false
  }
]
```