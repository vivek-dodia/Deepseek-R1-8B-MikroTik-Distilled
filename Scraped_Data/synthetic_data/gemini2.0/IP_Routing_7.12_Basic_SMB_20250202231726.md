**1. IP Routing**

**Configuration Scenario and Requirements**

Configure IP routing on a MikroTik router to enable communication between different network segments.

**2. Step-by-Step Implementation**

1. Access the router's web interface or CLI.
2. Navigate to IP > Routes.
3. Click on the "Add" button.
4. Configure the following parameters:
   - Destination: IP address or network range to be routed
   - Gateway: IP address of the next hop router
   - Distance: Metric used for route selection
5. Click on "Apply" to save the changes.

**3. Complete Configuration Commands**

```
/ip route add dst-address=192.168.10.0/24 gateway=192.168.1.1 distance=1
```

**4. Common Pitfalls and Solutions**

- **Error:** Route not added.
   - **Solution:** Ensure the specified gateway IP is reachable and the destination network is not already routed.
- **Error:** Packets not being routed to the correct destination.
   - **Solution:** Verify the destination and gateway IP addresses in the route configuration.

**5. Verification and Testing Steps**

- Ping the destination IP address to test if the route is working.
- Use Traceroute to verify the path taken by packets to the destination.

**6. Related Features and Considerations**

- **Policy Routing:** Allows for fine-grained control over routing decisions based on criteria such as source IP, destination IP, or application traffic.
- **Virtual Routing and Forwarding (VRF):** Isolates traffic between different virtual networks on the same physical router.
- **Static vs. Dynamic Routing:** Static routing requires manual configuration of routes, while dynamic routing protocols automatically discover and maintain routes.

**7. MikroTik REST API Examples**

**Endpoint:** `/routing/route`
**Request Method:** POST
**Example JSON Payload:**

```
{
  "dst-address": "192.168.10.0/24",
  "gateway": "192.168.1.1",
  "distance": "1"
}
```

**Expected Response:**

```
{
  "success": true
}
```