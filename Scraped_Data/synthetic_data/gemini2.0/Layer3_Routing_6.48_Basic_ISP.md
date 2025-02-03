**# Layer 3 Routing in RouterOS 6.48 (ISP)**

## 1. Configuration Scenario and Requirements

In this scenario, we will set up Layer 3 routing for an ISP using RouterOS 6.48. We will create static routes, RIPv2, and OSPFv3 routing protocols to ensure traffic flow across the network.

## 2. Step-by-Step Implementation

**2.1. Add Interfaces**

- Connect all necessary physical interfaces to the router.
- Assign IP addresses to each interface as per your network plan.

**2.2. Create Static Routes**

- Navigate to `/ip route`.
- Click the "Add" button.
- Configure the following parameters:
    - **Destination**: Network/subnet you want to route
    - **Gateway**: Gateway IP address
- Click "OK" to save the route.

**2.3. Configure RIPv2**

- Navigate to `/ip routing rip`.
- Click the "Add" button.
- Configure the following parameters:
    - **Interface**: Interface to enable RIPv2 on
    - **Address**: Address range to advertise
- Click "OK" to enable RIPv2 on the specified interface.

**2.4. Configure OSPFv3**

- Navigate to `/routing ospf`.
- Click the "Add" button.
- Configure the following parameters:
    - **Process ID**: Unique identifier for the OSPF process
    - **Router ID**: Router's ID used in OSPF
    - **Area**: Area the router will participate in
- Click "OK" to enable OSPFv3.

**2.5. Add Network Statements**

- Under the OSPFv3 configuration, click on the "Networks" tab.
- Click the "Add" button.
- Configure the following parameters:
    - **Network**: Network range to advertise
- Click "OK" to add the network statement.

## 3. Complete Configuration Commands

```
/ip route add dst-address=10.10.0.0/24 gateway=192.168.1.1
/ip routing rip add interface=ether1 address=192.168.1.0/24
/routing ospf add process=1 router-id=192.168.1.1 area=0
/routing ospf network add network=10.10.0.0/24
```

## 4. Common Pitfalls and Solutions

- **Incorrect IP Addresses or Subnets:** Ensure that the IP addresses and subnets configured are correct.
- **Interface Errors:** Verify that the physical interfaces are connected and configured correctly.
- **Routing Loops:** Avoid creating routing loops by carefully configuring static routes and routing protocols.
- **OSPF Neighboring Issues:** Ensure that OSPF neighbors are correctly established and exchanging routing information.

## 5. Verification and Testing Steps

- Ping from one subnet to another to test connectivity.
- Use traceroute to trace the network path between devices.
- Verify the routing table `/ip route print` to confirm that routes are installed and working correctly.
- Monitor the status of routing protocols, such as RIP and OSPF, using `/ip routing rip status` and `/routing ospf status`, respectively.

## 6. Related Features and Considerations

- **Security:** Implement appropriate firewall rules and ACLs to protect the network from unauthorized access.
- **Route Policy:** Use route policy to influence the routing decisions based on specific criteria.
- **DHCP Server:** Configure the router as a DHCP server to assign IP addresses to clients automatically.
- **Quality of Service (QoS):** Implement QoS mechanisms to prioritize traffic and improve network performance.