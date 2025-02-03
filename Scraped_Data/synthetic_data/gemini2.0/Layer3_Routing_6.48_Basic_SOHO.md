## Layer 3 Routing in MikroTik RouterOS 6.48

### Configuration Scenario and Requirements

**Objective:** Establish Layer 3 routing between two subnets connected to a MikroTik router.

**Requirements:**

- MikroTik router running RouterOS 6.48
- Two subnets:
  - Subnet A: 192.168.1.0/24
  - Subnet B: 10.0.0.0/24
- Ethernet interfaces connected to each subnet

### Step-by-Step Implementation

**1. Create the IP Addresses and Interfaces**

- Assign IP addresses to the Ethernet interfaces:
  ```
  /interface bridge add name=bridge1
  /interface ethernet add name=ether1 bridge=bridge1 mac-address=AA:BB:CC:DD:EE:FF
  /interface ip address add address=192.168.1.1/24 interface=ether1
  /interface ethernet add name=ether2 bridge=bridge1 mac-address=FF:EE:DD:CC:BB:AA
  /interface ip address add address=10.0.0.1/24 interface=ether2
  ```

**2. Configure the Default Gateway**

- Set the default gateway for both subnets:
  ```
  /ip route add gateway=192.168.1.1 distance=1
  /ip route add gateway=10.0.0.1 distance=1
  ```

**3. Enable IP Forwarding**

- Allow the router to forward IP traffic:
  ```
  /ip firewall filter add chain=forward action=accept
  ```

### Complete Configuration Commands

```
/interface bridge add name=bridge1
/interface ethernet add name=ether1 bridge=bridge1 mac-address=AA:BB:CC:DD:EE:FF
/interface ip address add address=192.168.1.1/24 interface=ether1
/interface ethernet add name=ether2 bridge=bridge1 mac-address=FF:EE:DD:CC:BB:AA
/interface ip address add address=10.0.0.1/24 interface=ether2
/ip route add gateway=192.168.1.1 distance=1
/ip route add gateway=10.0.0.1 distance=1
/ip firewall filter add chain=forward action=accept
```

### Common Pitfalls and Solutions

- **Incorrect MAC addresses:** Ensure the specified MAC addresses match the physical interfaces.
- **IP conflict:** Verify that the assigned IP addresses do not conflict with any existing devices on the network.
- **Disabled bridge:** Check that the bridge interface is enabled using `/bridge set <bridge-name> disabled=false`.
- **Firewall rules:** Make sure that no firewall rules are blocking the desired traffic.

### Verification and Testing Steps

- Ping from Subnet A to Subnet B: `ping 10.0.0.1`
- Verify routing table: `/ip route print`
- Monitor traffic using the `/tool sniffer` command

### Related Features and Considerations

- **Static Routing:** For more advanced routing scenarios, consider using static routes for specific destinations.
- **Dynamic Routing Protocols:** Routers can exchange routing information using protocols like RIP, OSPF, or BGP for more flexible and scalable network topologies.
- **Security:** Implement security measures such as firewall rules and access control lists (ACLs) to protect the network from unauthorized access.