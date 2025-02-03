## Layer 3 Routing in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

In this scenario, we will configure a MikroTik router as a Layer 3 gateway between two separate networks. The router will have two Ethernet interfaces:

- eth1 (192.168.1.1/24) connects to the first network
- eth2 (192.168.2.1/24) connects to the second network

**Requirements:**

- MikroTik router with RouterOS 7.11 or later
- Two Ethernet connections on the router

### Step-by-Step Implementation

**Step 1: Assign IP Addresses and Interfaces**

```
/ip address add address=192.168.1.1/24 interface=eth1
/ip address add address=192.168.2.1/24 interface=eth2
```

**Step 2: Create a Bridge for Inter-VLAN Traffic**

```
/interface bridge add name=bridge-vlan
/interface bridge port add bridge=bridge-vlan interface=eth1
/interface bridge port add bridge=bridge-vlan interface=eth2
```

**Step 3: Create Static Routes**

```
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.2
/ip route add dst-address=192.168.1.0/24 gateway=192.168.2.2
```

### Complete Configuration Commands

```
/ip address add address=192.168.1.1/24 interface=eth1
/ip address add address=192.168.2.1/24 interface=eth2
/interface bridge add name=bridge-vlan
/interface bridge port add bridge=bridge-vlan interface=eth1
/interface bridge port add bridge=bridge-vlan interface=eth2
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.2
/ip route add dst-address=192.168.1.0/24 gateway=192.168.2.2
```

### Common Pitfalls and Solutions

- **Incorrect IP Addresses or Gateway**: Ensure that the IP addresses and gateway addresses are correct for your network.
- **Non-routable IP Subnets**: Make sure that the subnets on the connected networks are routable.
- **VLAN Misconfiguration**: Verify that the bridge and VLANs are configured correctly if using separate VLANs.

### Verification and Testing Steps

- Ping devices on both networks to ensure connectivity.
- Use traceroute to verify that traffic is routed through the gateway.
- Check the routing table (`/ip route print`) to confirm the configured routes.

### Related Features and Considerations

- **Dynamic Routing Protocols**: For more complex routing scenarios, consider using dynamic routing protocols like OSPF or BGP.
- **Firewall Rules**: Implement firewall rules to control traffic between the networks and protect against security threats.
- **DHCP Server**: Set up a DHCP server to automatically assign IP addresses to devices on the connected networks.