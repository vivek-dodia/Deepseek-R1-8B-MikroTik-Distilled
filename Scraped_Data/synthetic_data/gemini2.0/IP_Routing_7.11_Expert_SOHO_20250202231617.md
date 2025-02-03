## IP Routing

### Configuration Scenario and Requirements

- Implement IP routing between multiple subnets on a MikroTik RouterOS 7.11 device.
- Use multiple interfaces for connectivity to different subnets.
- Establish default gateways for each subnet.
- Configure static routes for specific destinations.

### Step-by-Step Implementation

**1. Configure IP Addresses and Interfaces**

- Assign IP addresses and configure interfaces for each subnet.
```
/ip address add address=10.0.0.1/24 interface=ether1
/ip address add address=192.168.1.1/24 interface=ether2
```

**2. Configure Default Gateways**

- Specify the default gateway for each subnet.
```
/ip route add gateway=10.0.0.254
/ip route add gateway=192.168.1.254
```

**3. Add Static Routes**

- Create static routes for specific destinations.
```
/ip route add destination=0.0.0.0/0 gateway=10.0.0.254
/ip route add destination=10.0.1.0/24 gateway=192.168.1.1
```

### Complete Configuration Commands

```
/ip address add address=10.0.0.1/24 interface=ether1
/ip address add address=192.168.1.1/24 interface=ether2
/ip route add gateway=10.0.0.254
/ip route add gateway=192.168.1.254
/ip route add destination=0.0.0.0/0 gateway=10.0.0.254
/ip route add destination=10.0.1.0/24 gateway=192.168.1.1
```

### Common Pitfalls and Solutions

- **Incorrect IP Addresses or Gateways:** Verify that the IP addresses, subnet masks, and gateways are correct.
- **Interface Misconfiguration:** Ensure that the interfaces are properly configured and have valid IP addresses.
- **Overlapping Subnets:** Avoid using overlapping subnets on different interfaces, as this can cause routing conflicts.

### Verification and Testing Steps

- Use the `/ip route print` command to verify the routing table.
- Ping destinations on different subnets to test connectivity.

### Related Features and Considerations

- **Routing Policies:** Use routing policies to control routing behavior based on specific criteria.
- **DHCP Server:** Configure a DHCP server to dynamically assign IP addresses to devices on the network.
- **Firewall:** Implement firewall rules to control access and protect the network.

### MikroTik REST API Examples

**Get Routing Table:**

```
GET /routing/route/print
```

**Create Static Route:**

```
POST /routing/route
{
  "destination": "0.0.0.0/0",
  "gateway": "10.0.0.254"
}
```

**Delete Static Route:**

```
DELETE /routing/route/0.0.0.0/0/10.0.0.254
```