## Layer3 Routing in RouterOS 6.48

### Configuration Scenario and Requirements

- Configure a Layer3 network with static routes.
- Enable Border Gateway Protocol (BGP) for dynamic routing.
- Apply firewall rules to control traffic flow.
- Implement Network Address Translation (NAT) for private IP address access.

### Step-by-Step Implementation

#### Static Routing

1. Create a new route:
   ```
   /ip route add dst-address=10.10.10.0/24 gateway=192.168.1.1
   ```

2. Add multiple destinations to a single route:
   ```
   /ip route add dst-address=10.10.10.0/24,10.10.11.0/24 gateway=192.168.1.1
   ```

3. Add a default route (0.0.0.0/0):
   ```
   /ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1
   ```

#### Border Gateway Protocol (BGP)

1. Enable BGP:
   ```
   /routing bgp enable
   ```

2. Configure a BGP neighbor:
   ```
   /routing bgp neighbor add address=10.10.10.1 remote-as=65534
   ```

3. Add a route advertisement rule:
   ```
   /routing bgp rule add action=accept dst-address=192.168.1.0/24
   ```

#### Firewall Rules

1. Create a firewall rule to allow traffic from specific IP addresses:
   ```
   /ip firewall filter add chain=input dst-address=10.10.10.1 action=accept
   ```

2. Create a firewall rule to block traffic from a specific port:
   ```
   /ip firewall filter add chain=input dst-port=80 action=drop
   ```

3. Create a firewall rule to masquerade traffic:
   ```
   /ip firewall nat add chain=srcnat src-address=192.168.1.0/24 action=masquerade
   ```

#### Network Address Translation (NAT)

1. Enable NAT:
   ```
   /ip nat enable
   ```

2. Configure a NAT rule:
   ```
   /ip nat rule add chain=dstnat dst-address=10.10.10.1 protocol=tcp dst-port=80 to-address=192.168.1.1 to-port=8080
   ```

### Complete Configuration Commands

```
# Static Routing
/ip route add dst-address=10.10.10.0/24 gateway=192.168.1.1
/ip route add dst-address=10.10.11.0/24 gateway=192.168.1.1
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1

# Border Gateway Protocol (BGP)
/routing bgp enable
/routing bgp neighbor add address=10.10.10.1 remote-as=65534
/routing bgp rule add action=accept dst-address=192.168.1.0/24

# Firewall Rules
/ip firewall filter add chain=input dst-address=10.10.10.1 action=accept
/ip firewall filter add chain=input dst-port=80 action=drop
/ip firewall nat add chain=srcnat src-address=192.168.1.0/24 action=masquerade

# Network Address Translation (NAT)
/ip nat enable
/ip nat rule add chain=dstnat dst-address=10.10.10.1 protocol=tcp dst-port=80 to-address=192.168.1.1 to-port=8080
```

### Common Pitfalls and Solutions

- **Incorrect gateway address:** Ensure the specified gateway address is reachable and has the necessary permissions.
- **Overlapping IP ranges:** Avoid creating routes with overlapping IP ranges, as this can lead to routing loops.
- **Incorrect firewall rules:** Ensure that firewall rules are properly configured to allow desired traffic while blocking malicious attempts.
- **NAT configuration errors:** Verify that the NAT rules are correctly defined and that the target IP addresses and ports are accessible.

### Verification and Testing Steps

- Use the `/ip route print` command to verify the static routes.
- Check BGP status using `/routing bgp print neighbor` and `/routing bgp info`.
- Test firewall rules with `ping` or other network testing tools.
- Verify NAT functionality by accessing the translated IP address from an external network.

### Related Features and Considerations

- **Route policies:** Control how specific routes are applied based on criteria such as IP address or protocol.
- **Quality of Service (QoS):** Prioritize traffic based on specific parameters to ensure optimal performance.
- **Virtual Routing and Forwarding (VRF):** Partition the routing table into multiple virtual tables to improve scalability and security.
- **Security best practices:** Implement strong firewall rules, use encryption, and configure access control lists (ACLs) to protect the network from unauthorized access.