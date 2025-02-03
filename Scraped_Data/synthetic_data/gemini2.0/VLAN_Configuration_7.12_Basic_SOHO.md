## VLAN Configuration on MikroTik RouterOS 7.12 (Basic)

### Configuration Scenario and Requirements

- Configure two VLANs on a SOHO network:
  - VLAN 10 for Management (Default VLAN)
  - VLAN 20 for Devices

### Step-by-Step Implementation

**1. Create VLAN Interfaces**

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
```

**2. Assign Ports to VLANs**

```
/interface ethernet switch port set
    interface=ether1 vlan-id=10
/interface ethernet switch port set
    interface=ether2 vlan-id=20
```

**3. Enable VLAN Trunks**

To allow VLAN traffic to pass between the ports, enable trunking on the uplink port.

```
/interface bridge port set
    interface=ether1 bridge=bridge1 vlan-filtering=disabled
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
/interface ethernet switch port set interface=ether1 vlan-id=10
/interface ethernet switch port set interface=ether2 vlan-id=20
/interface bridge port set interface=ether1 bridge=bridge1 vlan-filtering=disabled
```

### Common Pitfalls and Solutions

- **VLAN ID Mismatch:** Ensure that the VLAN IDs assigned to the interfaces and ports match.
- **VLAN Filtering:** If VLAN filtering is enabled on the trunk port, it will block VLAN traffic.
- **IP Address Assignment:** Assign IP addresses from appropriate subnets for each VLAN.

### Verification and Testing Steps

- Verify VLAN creation: `/interface vlan print`
- Verify port assignments: `/interface ethernet switch port print`
- Ping between devices on different VLANs.

### Related Features and Considerations

- **VLAN Tagging:** VLAN tags (802.1Q) are added to packets to identify the VLAN they belong to.
- **Security:** Use VLANs to segment the network and improve security. Devices on different VLANs cannot communicate by default, reducing the risk of unauthorized access.
- **Performance:** VLANs can improve network performance by isolating traffic and reducing broadcast traffic.