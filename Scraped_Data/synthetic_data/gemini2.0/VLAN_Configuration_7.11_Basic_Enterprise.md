## VLAN Configuration in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

- Create two VLANs on a switch port for network segmentation.
- Assign IP addresses and default gateways to the VLANs.

### Step-by-Step Implementation

**1. Create VLANs on the Switch Port**

```
/interface vlan add name=VLAN10 vlan-id=10 interface=ether1
/interface vlan add name=VLAN20 vlan-id=20 interface=ether1
```

**2. Assign IP Addresses and Default Gateways**

```
/ip address add address=10.10.10.1/24 interface=VLAN10
/ip address add address=10.10.20.1/24 interface=VLAN20
/ip route add gateway=10.10.10.1/24 interface=VLAN10
/ip route add gateway=10.10.20.1/24 interface=VLAN20
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN10 vlan-id=10 interface=ether1
/interface vlan add name=VLAN20 vlan-id=20 interface=ether1
/ip address add address=10.10.10.1/24 interface=VLAN10
/ip address add address=10.10.20.1/24 interface=VLAN20
/ip route add gateway=10.10.10.1/24 interface=VLAN10
/ip route add gateway=10.10.20.1/24 interface=VLAN20
```

### Common Pitfalls and Solutions

- **VLAN IDs must be unique:** Each VLAN on the same interface must have a different VLAN ID.
- **Secure VLANs:** Use VLAN tagging to prevent unauthorized access between VLANs.
- **Test connectivity:** Ping between devices on different VLANs to verify connectivity.

### Verification and Testing Steps

1. Check if VLANs are created and active: `/interface vlan print`
2. Ping from a device on VLAN10 to a device on VLAN20.
3. Verify IP route entries are correct: `/ip route print`

### Related Features and Considerations

- **QinQ (802.1ad):** Allows multiple VLANs over a single physical interface.
- **VLAN stacking:** Connects multiple VLANs across different switches.
- **Security:** Use access control lists (ACLs) to restrict access between VLANs.