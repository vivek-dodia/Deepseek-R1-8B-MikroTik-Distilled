## IP Routing

### Configuration Scenario and Requirements

- Configure IP routing on a MikroTik router to allow traffic between different subnets.
- Multiple subnets and interfaces are involved.
- Use static routes for specific destinations.

### Step-by-Step Implementation

#### IP Addressing

- Assign IP addresses to all interfaces involved.
- For example:
    ```
    /ip address add address=192.168.1.1/24 interface=ether1
    /ip address add address=192.168.2.1/24 interface=ether2
    ```

#### IP Routing

- Add static routes for specific destinations that are not directly connected.
- For example:
    ```
    /ip route add dst-address=10.0.0.0/24 gateway=192.168.1.2
    /ip route add dst-address=192.168.3.0/24 gateway=192.168.2.2
    ```

### Complete Configuration Commands

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.2
/ip route add dst-address=192.168.3.0/24 gateway=192.168.2.2
```

### Common Pitfalls and Solutions

- **Incorrect IP addresses:** Ensure that the IP addresses assigned to the interfaces are correct and match the network configuration.
- **Missing gateway:** Specify the gateway for static routes to ensure connectivity to remote networks.
- **Loopback routes:** Avoid creating routes that point to the local router's own IP address.

### Verification and Testing Steps

- Ping from one subnet to another to test connectivity.
- For example:
    ```
    /ping 10.0.0.1
    ```
- Check the routing table using `/ip route print`.

### Related Features and Considerations

- **Policy routing:** Use policy routing to route traffic based on specific criteria, such as source or destination IP address or port.
- **Dynamic routing protocols:** Consider using dynamic routing protocols, such as OSPF or RIP, for automatic route calculation and updates.

### MikroTik REST API Examples

- Get IPv4 routing table:
    - Endpoint: `/routing/ip/route`
    - Request Method: GET
    - Response Example:
        ```json
        [
          {
            "dst-address": "10.0.0.0/24",
            "gateway": "192.168.1.2",
            "id": "00000000000000000000000000000001",
            "interface": "ether1",
            "src-address": null
          },
          {
            "dst-address": "192.168.3.0/24",
            "gateway": "192.168.2.2",
            "id": "00000000000000000000000000000002",
            "interface": "ether2",
            "src-address": null
          }
        ]
        ```
- Add an IPv4 static route:
    - Endpoint: `/routing/ip/route`
    - Request Method: POST
    - Request Payload Example:
        ```json
        {
          "dst-address": "10.0.0.0/24",
          "gateway": "192.168.1.2"
        }
        ```
    - Response Example:
        ```json
        {
          "dst-address": "10.0.0.0/24",
          "gateway": "192.168.1.2",
          "id": "00000000000000000000000000000003",
          "interface": null,
          "src-address": null
        }
        ```