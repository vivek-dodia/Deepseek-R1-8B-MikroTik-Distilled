## Layer3 Routing in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

**Objective:** Configure Layer3 routing on a MikroTik router to enable inter-VLAN communication.

**Requirements:**

- MikroTik Router with two or more physical Ethernet interfaces
- Two VLANs with different subnets
- IP addresses assigned to the interfaces and VLANs

### Step-by-Step Implementation

**1. VLAN Configuration**

- Create VLANs on the router's interfaces:
```
/interface vlan add name=vlan10 interface=ether1 vlan-id=10
/interface vlan add name=vlan20 interface=ether2 vlan-id=20
```

**2. Bridge Configuration**

- Create a bridge to connect the VLANs:
```
/interface bridge add name=br0
/interface bridge port add interface=vlan10 bridge=br0
/interface bridge port add interface=vlan20 bridge=br0
```

**3. IP Routing Configuration**

- Assign IP addresses to the VLAN interfaces:
```
/ip address add address=192.168.10.1/24 interface=vlan10
/ip address add address=192.168.20.1/24 interface=vlan20
```

- Enable IP forwarding:
```
/ip routing enable
```

**4. Static Routing Configuration**

- Add static routes to enable inter-VLAN communication:
```
/ip route add dst-address=192.168.20.0/24 gateway=192.168.10.1
/ip route add dst-address=192.168.10.0/24 gateway=192.168.20.1
```

### Common Pitfalls and Solutions

- **Incorrect VLAN ID**: Ensure that the VLAN ID assigned to the interface matches the VLAN ID of the actual VLAN.
- **Mismatched IP Subnets**: Check that the IP subnets assigned to the VLANs are different to avoid IP address conflicts.
- **Firewall Rules**: Verify that firewall rules do not block traffic between the VLANs if necessary.

### Verification and Testing Steps

1. Ping between devices on different VLANs to confirm connectivity:
```
[ether1] ping 192.168.20.10
```

2. Check the routing table to verify the static routes:
```
/ip route print
```

### Related Features and Considerations

- **Dynamic Routing Protocols**: RouterOS supports dynamic routing protocols such as OSPF and BGP for more complex routing scenarios.
- **Security Best Practices**: Consider using access lists or firewall rules to control traffic between VLANs and prevent unauthorized access.
- **Performance Optimization**: Utilize features like fastpath and hardware offloading to enhance routing performance in high-traffic environments.