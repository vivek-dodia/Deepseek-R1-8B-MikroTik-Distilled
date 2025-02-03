## VLAN Configuration on MikroTik RouterOS 7.12

### Configuration Scenario and Requirements

- Create multiple Virtual LANs (VLANs) for network segmentation.
- Assign VLANs to specific interfaces on the router.
- Configure inter-VLAN routing to allow communication between VLANs.

### Step-by-Step Implementation

**1. Create VLANs**

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
```

**2. Assign VLANs to Interfaces**

```
/interface ethernet set ether1 vlan=VLAN10
/interface ethernet set ether2 vlan=VLAN20
```

**3. Configure Inter-VLAN Routing**

```
/ip route add dst-address=192.168.10.0/24 gateway=192.168.1.1 vlan=VLAN10
/ip route add dst-address=192.168.20.0/24 gateway=192.168.2.1 vlan=VLAN20
```

### Complete Configuration Commands

```
/interface vlan
  add name=VLAN10 vlan-id=10
  add name=VLAN20 vlan-id=20
/interface ethernet
  set ether1 vlan=VLAN10
  set ether2 vlan=VLAN20
/ip route
  add dst-address=192.168.10.0/24 gateway=192.168.1.1 vlan=VLAN10
  add dst-address=192.168.20.0/24 gateway=192.168.2.1 vlan=VLAN20
```

### Common Pitfalls and Solutions

**Pitfall:** Forgetting to assign VLANs to interfaces.
**Solution:** Use the `/interface vlan` menu to assign VLANs to specific interfaces.

**Pitfall:** Incorrect gateway configuration for inter-VLAN routing.
**Solution:** Ensure that the gateway IP address is the IP address of the router's interface in the destination VLAN.

### Verification and Testing Steps

- Ping from devices within each VLAN to verify connectivity.
- Check the routing table `/ip route print` to ensure that inter-VLAN routes are present.
- Use the `/tool netwatch` command to monitor network traffic and verify VLAN segmentation.

### Related Features and Considerations

- **VLAN Trunking:** Configure trunk ports to allow multiple VLANs to be transmitted on a single physical interface.
- **Security:** Use firewall rules and VLAN hopping protection to prevent unauthorized access between VLANs.
- **Performance Optimization:** Enable VLAN hardware offloading on supported devices to improve data forwarding performance.