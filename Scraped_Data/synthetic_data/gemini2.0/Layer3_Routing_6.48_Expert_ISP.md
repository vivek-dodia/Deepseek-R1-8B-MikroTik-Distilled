## Layer3 Routing with RouterOS 6.x

### Configuration Scenario and Requirements

This documentation provides a comprehensive guide to configuring Layer3 routing in RouterOS 6.48 or higher. The scenario involves setting up a simple network with multiple subnets and routing traffic between them.

### Step-by-Step Implementation

**1. Define Interfaces and IP Addresses**

- Assign IP addresses and subnet masks to the physical interfaces on the RouterOS device.
```
/interface address add address=192.168.10.1/24 interface=ether1
/interface address add address=192.168.20.1/24 interface=ether2
```

**2. Create and Activate Routing Tables**

- Create a separate routing table for each subnet.
```
/ip routing table add name=RT_10
/ip routing table add name=RT_20
```

- Activate the routing tables on their respective interfaces.
```
/interface route-table set interface=ether1 table=RT_10
/interface route-table set interface=ether2 table=RT_20
```

**3. Add Static Routes**

- Configure static routes to define the paths between different subnets.
```
/ip route add dst-address=192.168.20.0/24 gateway=192.168.10.2 table=RT_10
/ip route add dst-address=192.168.10.0/24 gateway=192.168.20.2 table=RT_20
```

**4. Enable IP Forwarding**

- Allow the RouterOS device to forward traffic between interfaces.
```
/ip forwarding enable
```

### Complete Configuration Commands

```
/interface address add address=192.168.10.1/24 interface=ether1
/interface address add address=192.168.20.1/24 interface=ether2
/ip routing table add name=RT_10
/ip routing table add name=RT_20
/interface route-table set interface=ether1 table=RT_10
/interface route-table set interface=ether2 table=RT_20
/ip route add dst-address=192.168.20.0/24 gateway=192.168.10.2 table=RT_10
/ip route add dst-address=192.168.10.0/24 gateway=192.168.20.2 table=RT_20
/ip forwarding enable
```

### Common Pitfalls and Solutions

- **Incorrect IP Addresses or Subnet Masks:** Ensure that IP addresses and subnet masks are correctly configured for the interfaces and subnets.
- **Missing Routing Tables:** Create and activate routing tables for each subnet.
- **Invalid Static Routes:** Verify the destination addresses, gateways, and routing tables specified in the static routes.
- **Disabled IP Forwarding:** Check if IP forwarding is enabled on the RouterOS device.

### Verification and Testing Steps

- Ping devices from different subnets to test connectivity.
- Use traceroute to verify the routing paths between hosts.
- Inspect the routing table to ensure that static routes are correctly installed.

### Related Features and Considerations

- **Dynamic Routing Protocols:** Explore dynamic routing protocols like OSPF or BGP for more flexible and scalable routing.
- **Traffic Shaping and QoS:** Implement traffic shaping and QoS to prioritize and limit bandwidth consumption.
- **Security:** Configure firewall rules and other security measures to protect the network from unauthorized access and threats.