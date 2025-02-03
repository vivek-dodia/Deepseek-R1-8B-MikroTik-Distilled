---

## VLAN Configuration in RouterOS 6.48 (Expert)

### Prerequisites

- RouterOS 6.48 or later
- VLAN-capable switch

### Configuration Scenario

Configure VLANs to segment a network into multiple logical subnets.

### Requirements

- Create a VLAN on the switch
- Add VLANs to RouterOS
- Assign VLANs to interfaces
- Configure firewall rules to allow traffic between VLANs

### Step-by-Step Implementation

**1. Create VLAN on Switch**

Configure the VLAN on the switch according to the vendor's documentation.

**2. Add VLANs to RouterOS**

```
/vlan add name=VLAN10 vlan-id=10
/vlan add name=VLAN20 vlan-id=20
```

**3. Assign VLANs to Interfaces**

Assign the VLANs to the appropriate interfaces:

```
/interface bridge add name=bridge1
/interface bridge port add bridge=bridge1 interface=ether1
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=10
/interface bridge port add bridge=bridge1 interface=ether3 vlan-id=20
```

**4. Configure Firewall Rules**

Allow traffic between VLANs with firewall rules:

```
/ip firewall rule add chain=forward action=accept src-address-list=VLAN10-src dst-address-list=VLAN20-dst
/ip firewall rule add chain=forward action=accept src-address-list=VLAN20-src dst-address-list=VLAN10-dst
```

### Verification and Testing

- Ping from one VLAN to another to verify connectivity:
  ```
  /ping 192.168.10.254 interface=ether2
  /ping 192.168.20.254 interface=ether3
  ```
- Check the firewall logs to ensure no traffic is being dropped.

### Common Pitfalls and Solutions

- **VLAN ID not configured on the switch:** Ensure the VLAN ID matches on both the switch and RouterOS.
- **Interface not assigned to the correct bridge:** Verify that the interface is assigned to the correct bridge and has the correct VLAN ID.
- **Firewall rules not properly configured:** Ensure the firewall rules are correctly configured to allow traffic between VLANs.
- **MAC address learning disabled:** Enable MAC address learning on the bridge interface if experiencing connectivity issues.

### Related Features and Considerations

- **VLAN trunking:** Configure VLAN trunking if multiple VLANs are required on a single interface.
- **VLAN filtering:** Implement VLAN filtering to restrict access to specific VLANs.
- **Security:** Use security features such as access lists and firewall rules to protect VLANs from unauthorized access.