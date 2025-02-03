## Layer3 Routing in RouterOS 6.48 (Enterprise)

### Configuration Scenario and Requirements

- Configure static routes between two remote subnets connected via a Layer 3 interface.
- Implement dynamic routing protocols (OSPF or RIP) to establish optimal routing paths.
- Secure routing tables with route filters and firewall rules.

### Step-by-Step Implementation

**1. Static Routing (Example: Route to Remote Subnet)**

```
/ip route add dst-address=10.10.10.0/24 gateway=172.16.10.1
```

**2. Dynamic Routing (Example: Enable OSPF)**

**OSPF:**

```
/routing ospf enable
/routing ospf server add interface=ether1 area=0
```

**RIP:**

```
/routing rip enable
/routing rip interface add interface=ether1
```

**3. Route Filtering (Example: Drop Routes from Specific Source)**

```
/ip route filter add action=drop chain=input dst-address=10.10.11.0/24 src-address=172.16.11.0/24
```

**4. Firewall Rules (Example: Block Traffic from Specific Destination)**

```
/ip firewall filter add action=drop chain=forward dst-address=10.10.12.0/24
```

### Complete Configuration Commands

- **Static Routing:**
```
/ip route add dst-address=<Destination Subnet> gateway=<Gateway Address>
```

- **Dynamic Routing (OSPF):**
```
/routing ospf enable
/routing ospf server add interface=<Interface> area=<Area ID>
```

- **Dynamic Routing (RIP):**
```
/routing rip enable
/routing rip interface add interface=<Interface>
```

- **Route Filtering:**
```
/ip route filter add action=<Action> chain=<Chain> dst-address=<Destination Subnet> [src-address=<Source Subnet>]
```

- **Firewall Rules:**
```
/ip firewall filter add action=<Action> chain=<Chain> dst-address=<Destination Subnet> [src-address=<Source Subnet>]
```

### Common Pitfalls and Solutions

- **Incorrect Gateway Address:** Verify the gateway address for static routes.
- **OSPF Misconfiguration:** Ensure that the OSPF area ID is consistent on all connected routers.
- **RIP Conflicts:** Resolve IP address conflicts between routers participating in RIP.
- **Routing Loops:** Use route filters to prevent routing loops caused by misconfigured subnets or interfaces.

### Verification and Testing Steps

- **Static Routing:** Use `/ip route print` to verify the added routes. Ping the remote subnet to confirm connectivity.
- **Dynamic Routing:** Monitor `/routing ospf status` and `/routing rip status` for convergence information. Ping remote subnets to test reachability.
- **Route Filtering:** Check `/ip route filter print` to ensure that filters are applied correctly. Attempt to access filtered routes to verify blocking.

### Related Features and Considerations

- **Address Lists:** Use address lists to simplify filter criteria.
- **BGP Routing:** Implement BGP for more advanced routing scenarios.
- **QoS:** Prioritize traffic based on routing information using QoS policies.