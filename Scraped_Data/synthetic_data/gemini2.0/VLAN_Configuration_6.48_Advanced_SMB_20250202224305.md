## VLAN Configuration in RouterOS 6.48

### Configuration Scenario and Requirements

**Goal:** Create and configure VLANs on a MikroTik RouterOS device to segment the network and provide isolation between different segments.

**Requirements:**

- MikroTik RouterOS device running version 6.48 or higher
- Switch ports configured with trunking (e.g., 802.1q)
- VLAN-capable devices (e.g., IP phones, printers)

### Step-by-Step Implementation

**1. Create VLANs:**

```
/interface vlan add name=VLAN1 id=1
/interface vlan add name=VLAN2 id=2
```

**2. Assign VLANs to Switch Ports:**

```
/interface switch port set interface=ether1-1 vlan-id=1
/interface switch port set interface=ether2-1 vlan-id=2
```

**3. Configure IP Addresses for VLANs:**

```
/ip address add address=192.168.1.1/24 interface=VLAN1
/ip address add address=192.168.2.1/24 interface=VLAN2
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN1 id=1
/interface vlan add name=VLAN2 id=2
/interface switch port set interface=ether1-1 vlan-id=1
/interface switch port set interface=ether2-1 vlan-id=2
/ip address add address=192.168.1.1/24 interface=VLAN1
/ip address add address=192.168.2.1/24 interface=VLAN2
```

### Common Pitfalls and Solutions

- **VLAN ID Collision:** Ensure that VLAN IDs are unique across the network to avoid conflicts.
- **Incorrect Switch Port Configuration:** Verify that switch ports are configured correctly with the appropriate VLAN ID.
- **IP Address Assignment:** Assign unique IP addresses within each VLAN to avoid IP conflicts.

### Verification and Testing Steps

- **VLAN Connectivity:** Test connectivity between devices connected to different VLANs to ensure proper segmentation.
- **IP Address Assignment:** Check that devices on each VLAN have the correct IP addresses assigned.
- **VLAN Configuration Integrity:** Use the `/interface vlan print` command to verify that VLAN configurations are applied correctly.

### Related Features and Considerations

- **VLAN Tagging:** Use VLAN tagging (e.g., 802.1q) to identify VLAN traffic on trunked switch ports.
- **Security:** Implement VLANs as a security measure to isolate sensitive traffic and prevent unauthorized access.
- **QoS:** Configure VLANs with different QoS settings to prioritize important traffic.

### MikroTik REST API Examples

**Endpoint:** `/interface/vlan`

**Request Method:** GET

**Example JSON Payload:**

```
{
  ".proplist": ".id, .name"
}
```

**Expected Response:**

```
[
  {
    ".id": "1",
    "name": "VLAN1"
  },
  {
    ".id": "2",
    "name": "VLAN2"
  }
]
```