## VLAN Configuration in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

* Create multiple Virtual LANs (VLANs) on a MikroTik router to segment the network traffic.
* Assign VLANs to physical interfaces to restrict traffic between different VLANs.
* Enable inter-VLAN routing to allow communication between different VLANs.

### Step-by-Step Implementation

**1. Create VLANs**

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
/interface vlan add name=VLAN30 vlan-id=30
```

**2. Assign VLANs to Interfaces**

```
/interface ethernet add name=Ether1 vlan=VLAN10
/interface ethernet add name=Ether2 vlan=VLAN20
/interface ethernet add name=Ether3 vlan=VLAN30
```

**3. Enable Inter-VLAN Routing**

```
/ip routing add dst-address-list=VLAN10 routing-mark=VLAN10
/ip routing add dst-address-list=VLAN20 routing-mark=VLAN20
/ip routing add dst-address-list=VLAN30 routing-mark=VLAN30
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
/interface vlan add name=VLAN30 vlan-id=30
/interface ethernet add name=Ether1 vlan=VLAN10
/interface ethernet add name=Ether2 vlan=VLAN20
/interface ethernet add name=Ether3 vlan=VLAN30
/ip routing add dst-address-list=VLAN10 routing-mark=VLAN10
/ip routing add dst-address-list=VLAN20 routing-mark=VLAN20
/ip routing add dst-address-list=VLAN30 routing-mark=VLAN30
```

### Common Pitfalls and Solutions

* Ensure that the VLAN IDs used do not conflict with any native VLAN configurations on the switch.
* Double-check that the physical interfaces are correctly assigned to the corresponding VLANs.
* Verify that the inter-VLAN routing rules are properly configured and match the network requirements.

### Verification and Testing Steps

* Ping between devices on the same VLAN to ensure connectivity.
* Ping between devices on different VLANs to verify inter-VLAN routing.
* Use a network scanner to verify that devices within a VLAN are not visible to devices in other VLANs.

### Related Features and Considerations

* **Security:** VLANs provide an additional layer of security by isolating traffic between different VLANs. This prevents unauthorized access to sensitive data.
* **Performance:** VLANs can improve network performance by reducing broadcast traffic and improving bandwidth utilization.
* **Management:** VLANs simplify network management by allowing administrators to logically segment the network and apply different policies to each VLAN.

### MikroTik REST API Examples

**API Endpoint:** `/interface/vlan`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "interface": "VLAN10"
}
```

**Expected Response:**

```json
{
  "interface": "VLAN10",
  "name": "VLAN10",
  "vlan-id": 10
}
```