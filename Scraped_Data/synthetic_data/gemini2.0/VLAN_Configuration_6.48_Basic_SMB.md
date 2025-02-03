## VLAN Configuration in RouterOS v6.48

### Configuration Scenario and Requirements

- Implement VLANs to segment a network into isolated broadcast domains.
- Use 802.1q VLAN tagging.
- Assign untagged (default) traffic to a specific VLAN.

### Step-by-Step Implementation

**1. Create VLAN Interface:**

```
/interface vlan add name=VLAN1 vlan-id=10
```

**2. Assign Untagged VLAN:**

```
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=10 untagged
```

**3. Configure Tagged VLAN Interface:**

```
/interface vlan add name=VLAN2 vlan-id=20
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=20 tagged
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN1 vlan-id=10
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=10 untagged
/interface vlan add name=VLAN2 vlan-id=20
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=20 tagged
```

### Common Pitfalls and Solutions

- **VLAN ID Conflict:** Ensure that each VLAN ID is unique within the network.
- **Untagged Traffic Misconfiguration:** Verify that untagged traffic is assigned to the correct VLAN.
- **Interface Binding Errors:** Double-check that interfaces are correctly assigned to the proper VLAN and bridge.

### Verification and Testing Steps

- Check the bridge configuration using `/interface bridge print`.
- Use `/interface vlan print` to verify VLAN details.
- Test connectivity between devices assigned to different VLANs.

### Related Features and Considerations

- **Security:** VLANs provide network isolation, reducing the risk of unauthorized access and data breaches.
- **Network Segmentation:** VLANs allow for flexible management and separation of network traffic.
- **Broadcast Control:** VLANs limit broadcast traffic to specific network segments, enhancing performance and reducing broadcast storms.