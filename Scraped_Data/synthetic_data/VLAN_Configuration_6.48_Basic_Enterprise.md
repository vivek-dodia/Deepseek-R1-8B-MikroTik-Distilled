## VLAN Configuration in MikroTik RouterOS 6.48

### Configuration Scenario and Requirements

This configuration guide covers the setup of VLANs on a MikroTik RouterOS 6.48 device. We will create multiple VLANs, assign them to physical interfaces, and configure inter-VLAN routing.

**Requirements:**

- RouterOS 6.48 or higher
- Ethernet switch with VLAN support
- Physical interfaces on the RouterOS device

### Step-by-Step Implementation

**1. Create VLANs**

```
/interface vlan add name=VLAN10
/interface vlan add name=VLAN20
```

**2. Assign VLANs to Physical Interfaces**

```
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=10
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=20
```

**3. Enable Inter-VLAN Routing**

```
/ip routing add src-address=192.168.10.0/24 dst-address=192.168.20.0/24 gateway=192.168.20.1
```

**4. Configure DHCP Server for Each VLAN**

```
/ip dhcp-server add address-pool=VLAN10 interface=VLAN10
/ip dhcp-server add address-pool=VLAN20 interface=VLAN20
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN10
/interface vlan add name=VLAN20
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=10
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=20
/ip routing add src-address=192.168.10.0/24 dst-address=192.168.20.0/24 gateway=192.168.20.1
/ip dhcp-server add address-pool=VLAN10 interface=VLAN10
/ip dhcp-server add address-pool=VLAN20 interface=VLAN20
```

### Common Pitfalls and Solutions

- Ensure the physical interfaces support VLAN tagging.
- Verify that the VLAN IDs match between the RouterOS device and the switch.
- Check for any firewall rules that may block inter-VLAN traffic.
- If devices are not able to communicate across VLANs, verify the routing and DHCP configuration.

### Verification and Testing Steps

1. Connect devices to the different VLANs.
2. Assign IP addresses from the DHCP pool to the devices.
3. Ping between devices on different VLANs to verify connectivity.

### Related Features and Considerations

- **VLAN Trunking:** Extend VLANs across multiple physical interfaces to create larger VLANs.
- **QinQ:** Encapsulate multiple VLANs within a single trunk.
- **Security:** Implement VLAN ACLs to restrict traffic between VLANs.