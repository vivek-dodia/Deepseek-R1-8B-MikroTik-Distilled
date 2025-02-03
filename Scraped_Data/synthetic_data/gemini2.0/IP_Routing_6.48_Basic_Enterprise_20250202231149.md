## IP Routing in MikroTik RouterOS 6.48

### Configuration Scenario

This documentation provides a comprehensive guide to IP routing in MikroTik RouterOS 6.48. It covers:

- IP Addressing (IPv4 and IPv6)
- IP Pools
- IP Routing
- IP Settings
- Routing Protocols

### Step-by-Step Implementation

#### IP Addressing

- Assign an IPv4 address to an interface: `/ip address add address=192.168.1.1/24 interface=ether1`
- Assign an IPv6 address to an interface: `/ipv6 address add address=2001:db8::1/64 interface=ether1`

#### IP Pools

- Create an IP pool for DHCP: `/ip pool add name=dhcp-pool ranges=192.168.1.10-192.168.1.200`
- Assign the IP pool to a DHCP server: `/ip dhcp-server add interface=ether1 address-pool=dhcp-pool`

#### IP Routing

- Add a static route: `/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.2`
- Add a default route: `/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1`

#### IP Settings

- Configure DNS settings: `/ip settings set dns-servers=8.8.8.8,8.8.4.4`
- Configure the hostname: `/system identity set name=my-router`

#### Routing Protocols

- Enable OSPF routing: `/routing ospf enable`
- Add an OSPF process: `/routing ospf process add rid=my-router`
- Configure an OSPF interface: `/routing ospf interface add interface=ether1`

### Common Pitfalls and Solutions

- **Incorrect subnet mask:** Ensure the subnet mask matches the IPv4 address.
- **Duplicate IP addresses:** Check for duplicate IP addresses on the network and resolve conflicts.
- **Incorrect gateway:** Verify the gateway address is reachable and valid.
- **Disabled routing:** Ensure the routing table is enabled.
- **Firewall blocking:** Allow traffic through the firewall for necessary routing protocols.

### Verification and Testing Steps

- Use `ping` to verify IP address connectivity.
- Use `traceroute` to trace the route to a destination.
- Use `ip route print` to check the routing table.
- Test DHCP functionality by requesting an IP address from the DHCP server.
- Test routing protocols by sending and receiving routing updates.

### Related Features and Considerations

- **VLAN:** IP routing can be used in conjunction with VLANs to segment traffic.
- **MPLS:** MPLS can be used to create flexible and scalable VPNs.
- **Firewall:** Implement a firewall to protect the router and network from unauthorized access.
- **QoS:** Configure QoS to prioritize traffic and optimize network performance.

### MikroTik REST API Examples

#### Get IPv4 Address Information

```
GET /routing/ip/address
```

#### Add an IPv4 Address

```
POST /routing/ip/address
{
  "address": "192.168.1.1/24",
  "interface": "ether1"
}
```

#### Remove an IPv4 Address

```
DELETE /routing/ip/address/65e067930b47e209
```

### Technical Notes

- **Configuration Level:** Basic
- **Network Scale:** Enterprise
- **RouterOS Version:** 6.48
- **Supported Hardware:** RouterBOARD, CHR