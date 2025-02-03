## Layer3 Routing in RouterOS 6.48

**Configuration Level:** Advanced

**Network Scale:** ISP

### Configuration Scenario

- Establish basic Layer3 routing between two networks.
- Use static routing to define specific routes.
- Configure firewall rules to control traffic flow.
- Verify connectivity and troubleshoot issues.

### Step-by-Step Implementation

**1. Create Interfaces**

- Define two Ethernet interfaces for connecting to Network A and Network B.

**2. Add IP Addresses and Subnets**

- Assign IP addresses to the interfaces and configure subnet masks.

**Command:**
```
/ip address add address=172.16.1.1/24 interface=ether1
/ip address add address=172.16.2.1/24 interface=ether2
```

**3. Configure Static Routes**

- Create static routes to direct traffic between the networks.

**Command:**
```
/ip route add dst-address=172.16.2.0/24 gateway=172.16.1.2
/ip route add dst-address=172.16.1.0/24 gateway=172.16.2.2
```

**4. Setup Firewall Rules**

- Allow traffic between the two networks.

**Command:**
```
/ip firewall filter add chain=forward in-interface=ether1 out-interface=ether2 action=accept
/ip firewall filter add chain=forward in-interface=ether2 out-interface=ether1 action=accept
```

### Complete Configuration Commands

```
/interface bridge add name=bridge1
/interface ethernet set ether1 master-port=bridge1
/interface ethernet set ether2 master-port=bridge1
/ip address add address=172.16.1.1/24 interface=ether1
/ip address add address=172.16.2.1/24 interface=ether2
/ip route add dst-address=172.16.2.0/24 gateway=172.16.1.2
/ip route add dst-address=172.16.1.0/24 gateway=172.16.2.2
/ip firewall filter add chain=forward in-interface=ether1 out-interface=ether2 action=accept
/ip firewall filter add chain=forward in-interface=ether2 out-interface=ether1 action=accept
```

### Common Pitfalls and Solutions

**- Incorrect IP Addresses or Subnet Masks:** Verify the IP address and subnet mask configurations.
**- Invalid Gateway Addresses:** Ensure that the gateway addresses are reachable and belong to the correct network.
**- Firewall Rule Misconfiguration:** Ensure that the firewall rules are allowing traffic in both directions.
**- Master-Port Bridge Configuration:** Check that the bridge master-port is set correctly for the Ethernet interfaces.

### Verification and Testing Steps

**1. Ping Test:**

- Ping from Network A to Network B using the IP address of a device on Network B.

**2. Traceroute Test:**

- Trace the route from Network A to Network B to check for any routing loops or issues.

**3. Firewall Test:**

- Attempt to connect from Network A to Network B using various services (e.g., HTTP, SSH) to verify firewall rule functionality.

### Related Features and Considerations

**- Advanced Routing Features:**
  - Dynamic Routing Protocols (e.g., OSPF, BGP)
  - Policy-Based Routing
  - Load Balancing
**- Security Best Practices:**
  - Use strong passwords for administrative access
  - Implement security filters (e.g., MAC filtering, IP filtering)
  - Monitor system logs for suspicious activity

**Note:** The specific commands and configuration values may vary depending on the specific network topology and requirements. It is recommended to consult with a qualified network engineer for optimal configuration and troubleshooting assistance.