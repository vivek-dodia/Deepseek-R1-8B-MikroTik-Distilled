## Layer 3 Routing in MikroTik RouterOS 6.48

### Configuration Scenario and Requirements

* **Goal:** Establish layer 3 routing between multiple subnets.
* **Network topology:** A MikroTik router with multiple physical interfaces.
* **Subnets:**
    * LAN: 192.168.1.0/24
    * WAN: 10.0.0.0/24

### Step-by-Step Implementation

**1. Configure Physical Interfaces**

```
/interface bridge add name=bridge1
/interface bridge port add bridge=bridge1 interface=ether1
/interface bridge port add bridge=bridge1 interface=ether2
/interface add name=WAN interface=ether3
```

**2. Assign IP Addresses to Interfaces**

```
/ip address add address=192.168.1.1/24 interface=bridge1
/ip address add address=10.0.0.1/24 interface=WAN
```

**3. Configure Routing**

```
/ip route add gateway=10.0.0.1 dst-address=0.0.0.0/0
/ip route add gateway=192.168.1.1 dst-address=10.0.0.0/24
```

**4. Enable IP Forwarding**

```
/ip firewall filter add action=accept chain=forward
```

### Complete Configuration Commands

| Command | Description |
|---|---|
| `/interface bridge add name=bridge1` | Creates a bridge interface named `bridge1`. |
| `/interface bridge port add bridge=bridge1 interface=ether1` | Adds `ether1` to the `bridge1` bridge. |
| `/interface bridge port add bridge=bridge1 interface=ether2` | Adds `ether2` to the `bridge1` bridge. |
| `/interface add name=WAN interface=ether3` | Creates a WAN interface named `WAN`. |
| `/ip address add address=192.168.1.1/24 interface=bridge1` | Assigns an IP address to the bridge interface. |
| `/ip address add address=10.0.0.1/24 interface=WAN` | Assigns an IP address to the WAN interface. |
| `/ip route add gateway=10.0.0.1 dst-address=0.0.0.0/0` | Adds a default route via the WAN interface. |
| `/ip route add gateway=192.168.1.1 dst-address=10.0.0.0/24` | Adds a static route to the LAN subnet via the bridge interface. |
| `/ip firewall filter add action=accept chain=forward` | Enables IP forwarding. |

### Common Pitfalls and Solutions

* **Incorrect IP addresses:** Verify that the IP addresses assigned to the interfaces are correct.
* **Missing routes:** Ensure that static routes are added to reach specific subnets.
* **Firewall blocking:** Check the firewall rules to ensure they are not blocking traffic.

### Verification and Testing Steps

* Ping hosts on different subnets to verify connectivity.
* Use `traceroute` to trace the route taken by packets.
* Monitor the router's CPU and memory usage to ensure proper operation.

### Related Features and Considerations

* **VLANs:** Use VLANs to segment traffic and improve security.
* **IPv6:** Configure IPv6 addressing and routing as needed.
* **NAT:** Configure NAT rules to enable external access to internal hosts.
* **Security:** Use firewall rules and security features to protect the network from unauthorized access.