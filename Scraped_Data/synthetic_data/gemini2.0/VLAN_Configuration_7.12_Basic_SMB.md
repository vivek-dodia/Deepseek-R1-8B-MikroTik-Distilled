## VLAN Configuration in MikroTik (RouterOS 7.12)

### Configuration Scenario and Requirements

- Create multiple VLANs on a MikroTik router.
- Assign specific ports to each VLAN.
- Allow VLANs to communicate with each other.

### Step-by-Step Implementation

#### 1. Create VLANs

```
/interface vlan add name=VLAN10
/interface vlan add name=VLAN20
/interface vlan add name=VLAN30
```

#### 2. Assign Ports to VLANs

| Port | VLAN |
|---|---|
| Ether1 | VLAN10 |
| Ether2 | VLAN20 |
| Ether3 | VLAN30 |

```
/interface ethernet set Ether1 vlan-id=10
/interface ethernet set Ether2 vlan-id=20
/interface ethernet set Ether3 vlan-id=30
```

#### 3. Enable Inter-VLAN Communication

```
/interface bridge add name=bridge1
/interface bridge vlan add bridge=bridge1 vlan=VLAN10
/interface bridge vlan add bridge=bridge1 vlan=VLAN20
/interface bridge vlan add bridge=bridge1 vlan=VLAN30
/interface bridge set bridge1 protocol-mode=rstp
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN10
/interface vlan add name=VLAN20
/interface vlan add name=VLAN30
/interface ethernet set Ether1 vlan-id=10
/interface ethernet set Ether2 vlan-id=20
/interface ethernet set Ether3 vlan-id=30
/interface bridge add name=bridge1
/interface bridge vlan add bridge=bridge1 vlan=VLAN10
/interface bridge vlan add bridge=bridge1 vlan=VLAN20
/interface bridge vlan add bridge=bridge1 vlan=VLAN30
/interface bridge set bridge1 protocol-mode=rstp
```

### Common Pitfalls and Solutions

- **VLAN IDs must be unique:** Ensure that each VLAN has a distinct ID.
- **Port tagging must match VLAN ID:** Verify that the VLAN ID assigned to a port matches the VLAN ID of the device connected to it.
- **Bridge protocol must be compatible:** Ensure that the bridge protocol used (e.g., RSTP) is supported by all devices in the network.

### Verification and Testing Steps

- Check the VLAN configuration using `/interface vlan print`.
- Verify port assignments with `/interface ethernet print`.
- Test inter-VLAN communication by sending traffic between different VLANs.

### Related Features and Considerations

- **Security:** Configure firewall rules and VLAN access restrictions to prevent unauthorized communication between VLANs.
- **Management:** Use the VLAN interface group feature to manage multiple VLANs under a single name.
- **Performance:** Optimize network performance by tuning VLAN MTU and QoS settings.