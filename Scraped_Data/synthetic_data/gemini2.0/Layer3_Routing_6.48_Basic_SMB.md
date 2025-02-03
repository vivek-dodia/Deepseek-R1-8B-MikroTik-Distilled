## **Layer3 Routing in MikroTik RouterOS 6.48**

### Configuration Scenario and Requirements

- Establish static routes between subnets on a network with multiple MikroTik routers.

### Step-by-Step Implementation

#### 1. Create IP Address for All Interfaces

Configure IP addresses on all interfaces where routing will occur.

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
```

#### 2. Establish Static Routes

Create static routes to direct traffic between subnets.

```
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.2
/ip route add dst-address=192.168.1.0/24 gateway=192.168.2.2
```

### Complete Configuration Commands

```
# Create IP Addresses
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2

# Establish Static Routes
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.2
/ip route add dst-address=192.168.1.0/24 gateway=192.168.2.2
```

### Common Pitfalls and Solutions

- **Incorrect interface:** Ensure the correct interfaces are specified in IP address and route configurations.
- **Gateway not reachable:** Verify that the gateway IP address is reachable and online.
- **Duplicate routes:** Remove duplicate static routes for the same destination network.

### Verification and Testing Steps

- Use the `/ip route print` command to verify that the static routes are active.
- Ping devices on the remote subnet to test connectivity.

### Related Features and Considerations

- **Dynamic Routing Protocols:** For more complex networks, consider using dynamic routing protocols like OSPF or BGP.
- **Security:** Protect routing configurations from unauthorized changes by implementing firewall rules and access control lists.