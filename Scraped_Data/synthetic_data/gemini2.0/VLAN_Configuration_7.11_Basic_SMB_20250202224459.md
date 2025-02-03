## VLAN Configuration on MikroTik RouterOS

### Configuration Scenario and Requirements

**Goal:** Create multiple VLANs and assign them to specific ports on a MikroTik router.

### Step-by-Step Implementation

**1. Create VLANs:**

```
/interface vlan add name=VLAN1
/interface vlan add name=VLAN2
```

**2. Assign VLANs to Ports:**

```
/interface ethernet set ether1 vlan-id=VLAN1
/interface ethernet set ether2 vlan-id=VLAN2
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN1
/interface vlan add name=VLAN2
/interface ethernet set ether1 vlan-id=VLAN1
/interface ethernet set ether2 vlan-id=VLAN2
```

### Common Pitfalls and Solutions

- **VLAN ID Conflict:** Ensure that VLAN IDs do not overlap.
- **Port Assignment:** Verify that ports are assigned to the correct VLANs.
- **Interface Configuration:** Make sure the Ethernet interfaces are properly configured with IP addresses and default gateways.

### Verification and Testing Steps

- Check the VLAN interfaces using: `/interface vlan print`
- Verify port assignments with: `/interface ethernet print`
- Test connectivity between devices on different VLANs using ping.

### Related Features and Considerations

- **VLAN Trunking:** Use 802.1Q trunking to carry multiple VLANs on a single physical connection.
- **Security:** Implement VLAN segregation for improved network security.
- **Management Interface:** Designate a dedicated management VLAN for remote access to the router.

### MikroTik REST API Examples

**API Endpoint:** `/interface/vlan`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "VLAN3",
  "interface": "ether3"
}
```

**Expected Response:**

```json
{
  "id": 3,
  "name": "VLAN3",
  "interface": "ether3"
}
```