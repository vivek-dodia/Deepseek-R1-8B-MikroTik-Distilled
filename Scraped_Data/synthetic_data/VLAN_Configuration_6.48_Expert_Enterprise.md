## VLAN Configuration in RouterOS 6.48

### Configuration Scenario and Requirements

This guide provides comprehensive instructions on configuring VLANs in RouterOS 6.48 for enterprise-scale networks. The objectives include:

- Creating VLAN interfaces and assigning them to physical ports
- Configuring VLAN trunking between multiple switches
- Filtering traffic based on VLAN membership
- Verifying and troubleshooting VLAN connectivity

### Step-by-Step Implementation

#### 1. Create VLAN Interfaces

Create VLAN interfaces for each required VLAN:

```
/interface vlan add name=VLAN10 id=10 vlan-id=10
/interface vlan add name=VLAN20 id=20 vlan-id=20
```

#### 2. Assign VLAN Interfaces to Physical Ports

Assign the VLAN interfaces to the desired physical ports:

```
/interface ethernet set ether1 vlan=VLAN10
/interface ethernet set ether2 vlan=VLAN20
```

#### 3. Configure VLAN Trunking

Enable VLAN trunking on the ports connecting the switches:

```
/interface bridge port add bridge=bridge1 interface=ether1 pvid=1 untagged-vlan=VLAN10
/interface bridge port add bridge=bridge1 interface=ether2 pvid=1 untagged-vlan=VLAN20
```

#### 4. Filter Traffic Based on VLAN Membership

Create firewall rules to control traffic between VLANs:

```
/ip firewall filter add action=drop chain=input in-interface=ether1 vlan-id=VLAN10 dst-address=VLAN20
/ip firewall filter add action=drop chain=input in-interface=ether2 vlan-id=VLAN20 dst-address=VLAN10
```

### Complete Configuration Commands

The complete configuration commands for all steps:

```
/interface vlan add name=VLAN10 id=10 vlan-id=10
/interface vlan add name=VLAN20 id=20 vlan-id=20
/interface ethernet set ether1 vlan=VLAN10
/interface ethernet set ether2 vlan=VLAN20
/interface bridge port add bridge=bridge1 interface=ether1 pvid=1 untagged-vlan=VLAN10
/interface bridge port add bridge=bridge1 interface=ether2 pvid=1 untagged-vlan=VLAN20
/ip firewall filter add action=drop chain=input in-interface=ether1 vlan-id=VLAN10 dst-address=VLAN20
/ip firewall filter add action=drop chain=input in-interface=ether2 vlan-id=VLAN20 dst-address=VLAN10
```

### Common Pitfalls and Solutions

**Error:** VLAN traffic not passing through switch

**Solution:** Ensure that VLAN trunking is enabled on all switch ports involved.

**Error:** Incorrect VLAN ID configuration

**Solution:** Verify that the VLAN ID assigned to the VLAN interface matches the VLAN ID used in switch configuration.

**Error:** Firewall rules not applied properly

**Solution:** Double-check the firewall rule syntax and ensure that the rules are inserted in the correct chain.

### Verification and Testing Steps

- Verify VLAN interface creation: `/interface vlan print`
- Test inter-VLAN connectivity with ping: `ping x.x.x.x vlan-id=VLAN10`
- Monitor firewall logs to ensure successful traffic blocking: `/log print match="VLAN"`

### Related Features and Considerations

- **VLAN Trunking Protocols:** Use protocols like 802.1Q or ISL for inter-switch trunk configuration.
- **VLAN Security:** Implement access control lists (ACLs) to restrict access to specific VLANs.
- **VLAN Group Management:** Use bridge groups to manage multiple VLANs as a single entity.
- **VLAN Management Software:** Consider using external software tools for centralized VLAN configuration and monitoring.