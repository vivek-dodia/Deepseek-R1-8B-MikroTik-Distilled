## IP Routing

### Configuration Scenario and Requirements

This section covers the configuration of IP routing on a MikroTik RouterOS device in version 7.11. The goal is to establish static and dynamic routing on a SOHO network with a single router.

### Step-by-Step Implementation

**1. Configure IP Addresses**

- Assign IP addresses to the router's interfaces. For example, for the `ether1` interface:
```
/ip address add address=192.168.1.1/24 interface=ether1
```

**2. Create Static Routes**

- Add static routes for networks that are directly connected to the router. For instance, to route to the 10.0.0.0/24 network via the `ether2` interface:
```
/ip route add dst-address=10.0.0.0/24 gateway=192.168.2.2
```

**3. Configure Dynamic Routing**

- Enable dynamic routing using a routing protocol such as RIP. For RIP version 2 on the `ether3` interface:
```
/routing rip enable interface=ether3 version=2
```

**4. Configure Default Route**

- Add a default route to specify the gateway for traffic destined for networks not explicitly defined in the routing table.
```
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.254
```

**5. Verify Configuration**

- Use the `/ip route print` command to verify the routing table.
- Test connectivity to reachable destinations using the `ping` command.

### Complete Configuration Commands

```
# Configure IP addresses
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
/ip address add address=192.168.3.1/24 interface=ether3

# Create static routes
/ip route add dst-address=10.0.0.0/24 gateway=192.168.2.2 interface=ether2
/ip route add dst-address=172.16.0.0/24 gateway=192.168.3.2 interface=ether3

# Configure dynamic routing (RIPv2)
/routing rip enable interface=ether3 version=2

# Configure default route
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.254
```

### Common Pitfalls and Solutions

- **Incorrect gateway:** Ensure that the specified gateway for static routes is reachable from the interface used.
- **Overlapping IP addresses:** Avoid assigning the same IP address to multiple interfaces or networks.
- **Invalid routing protocol configuration:** Verify the correct syntax and parameters for the chosen routing protocol.

### Verification and Testing Steps

- Ping known IP addresses on different networks to test connectivity.
- Use tools like `traceroute` to verify the path taken by packets.
- Monitor the router's routing table for any unexpected changes or updates.

### Related Features and Considerations

- **IP Pool:** Assign IP addresses dynamically to clients using IP pools.
- **MAC server:** Learn MAC addresses of devices connected to the network.
- **Firewall:** Implement rules to control traffic flow based on IP addresses.
- **BFD:** Monitor the health of routing links for faster failover.

### MikroTik REST API Examples

**Get IP Routing Table**

**Endpoint:** `/routing/route/print`
**Request Method:** POST
**Example JSON Payload:**
```
{
  "active": true,
  "name": "DEFAULT",
  ".proplist": "active,age,distance"
}
```
**Expected Response:**
```
[
  {
    ".id": "1",
    "active": true,
    "age": 6433,
    "distance": 1
  },
  {
    ".id": "2",
    "active": true,
    "age": 0,
    "distance": 2
  }
]
```

**Add Static IP Routing**

**Endpoint:** `/routing/route/add`
**Request Method:** POST
**Example JSON Payload:**
```
{
  "dst-address": "192.168.0.0/24",
  "gateway": "192.168.1.254"
}
```
**Expected Response:**
```
{
  ".id": "3",
  "dst-address": "192.168.0.0/24",
  "gateway": "192.168.1.254"
}
```