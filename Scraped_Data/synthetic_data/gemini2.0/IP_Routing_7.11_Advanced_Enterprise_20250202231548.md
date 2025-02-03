**IP Routing**

**1. Configuration scenario and requirements**

- Configure IP routing on a MikroTik RouterOS 7.11 router to allow traffic between different subnets.

**2. Step-by-step implementation**

1. **Enable IP forwarding**
   - Navigate to IP > Settings and tick the "Enable IP Forwarding" checkbox.

2. **Add static routes**
   - Go to IP > Routes and click the "+" button to create a new route.
   - Enter the Destination Address, Gateway, and Distance.
   - Repeat for each subnet that you want to add a static route to.

3. **Configure firewall rules (optional)**
   - If necessary, add firewall rules to allow traffic to pass through the router.
   - Navigate to IP > Firewall > Filter Rules and click the "+" button to create a new rule.
   - Set the Chain to "input" or "forward," the Protocol to "ip," and the Action to "accept."

**3. Complete configuration commands**

- Enable IP forwarding:
    ```
    /ip settings set forward disable=no
    ```

- Add a static route:
    ```
    /ip route add dst-address=192.168.10.0/24 gateway=192.168.1.1
    ```

- Allow traffic through the firewall:
    ```
    /ip firewall filter add action=accept chain=input protocol=ip
    ```

**4. Common pitfalls and solutions**

- Ensure that IP forwarding is enabled.
- Check that the gateway IP address is correct.
- Verify that the firewall rules are not blocking traffic.

**5. Verification and testing steps**

- Ping hosts on different subnets to verify connectivity.
- Use the "traceroute" command to trace the path of packets.

**6. Related features and considerations**

- Consider using dynamic routing protocols (e.g., OSPF, RIP) for automatic route discovery.
- Use IP subnetting to divide the network into smaller, manageable chunks.
- Implement network monitoring to ensure that routes are working properly.

**7. MikroTik REST API examples**

**Endpoint:** `/routing/ip/route`
**Method:** GET
**Request:**
```
{
  "dst-address": "192.168.10.0/24"
}
```
**Response:**
```
[
  {
    "distance": 0,
    "dst-address": "192.168.10.0/24",
    "gateway": "192.168.1.1"
  }
]
```