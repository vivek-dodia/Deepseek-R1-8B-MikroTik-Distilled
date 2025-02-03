## IP Routing

### Configuration Scenario and Requirements
Configure IP routing on a MikroTik RouterOS 6.48 device to enable communication between different subnets.

### Step-by-Step Implementation

**1. Configure IP Addresses:**
- Configure IP addresses on the interfaces connected to the subnets.
```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
```

**2. Enable IP Forwarding:**
- Enable IP forwarding to allow packets to be routed between subnets.
```
/ip firewall filter add chain=forward action=accept
```

**3. Configure Default Gateway:**
- Configure the default gateway on each subnet to point to the MikroTik device.
```
/ip route add gateway=192.168.1.1
/ip route add gateway=192.168.2.1
```

**4. Configure Static Routes (Optional):**
- Configure static routes to specific destinations if necessary.
```
/ip route add dst-address=10.10.10.0/24 gateway=192.168.1.5
```

### Complete Configuration Commands

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
/ip firewall filter add chain=forward action=accept
/ip route add gateway=192.168.1.1
/ip route add gateway=192.168.2.1
/ip route add dst-address=10.10.10.0/24 gateway=192.168.1.5
```

### Common Pitfalls and Solutions

- **Incorrect IP Addresses:** Ensure the IP addresses are correct and match the subnet masks.
- **Disabled Forwarding:** Verify that IP forwarding is enabled in the firewall settings.
- **Missing Default Gateway:** Check that the default gateway is configured on each subnet.
- **Static Route Conflicts:** Avoid overlapping static routes with the dynamic routes.

### Verification and Testing Steps

- Ping hosts on different subnets to test connectivity.
- Use the `traceroute` command to trace the packets' path through the network.
- Monitor firewall logs for dropped packets or routing issues.

### Related Features and Considerations

- **Dynamic Routing Protocols:** Consider using dynamic routing protocols (e.g., OSPF, RIP) to automatically build and maintain routing tables.
- **Route Policies:** Implement route policies to control the path taken by packets and prioritize traffic.
- **Advanced Routing Features:** Explore advanced routing features such as BGP, VRRP, and load balancing for complex network topologies.

### MikroTik REST API Examples

**Get IP Routing Table**    
```
**API Endpoint:** /routing/ip/route  
**Request Method:** GET  
**Example JSON Payload:**  
```
{}  
```
**Expected Response:**  
```json
[
  {
    "address": "10.0.0.0/24",
    "active": true,
    "distance": 0,
    "gateway": null,
    "interface": "ether1",
    "scope": "10",
    "type": "direct"
  },
  {
    "address": "192.168.1.0/24",
    "active": true,
    "distance": 20,
    "gateway": "192.168.1.1",
    "interface": null,
    "scope": "20",
    "type": "static"
  }
]
```

**Add Static IP Route**  
```
**API Endpoint:** /routing/ip/route  
**Request Method:** POST  
**Example JSON Payload:**  
```
{
  "dst-address": "10.10.10.0/24",
  "gateway": "192.168.1.1"
}  
```
**Expected Response:**  
```json
{
  "address": "10.10.10.0/24",
  "active": true,
  "distance": 20,
  "gateway": "192.168.1.1",
  "interface": null,
  "scope": "20",
  "type": "static"
}
```