## VLAN Configuration in RouterOS 7.11 (Basic)

### Configuration Scenario and Requirements

- Create and manage multiple Virtual LANs (VLANs) on a MikroTik router
- Assign VLANs to specific physical interfaces
- Allow communication between devices within the same VLAN

### Step-by-Step Implementation

**1. Configure VLAN Interfaces**

Navigate to **Interfaces** > **VLAN** tab. Click the **+** button and configure the following parameters:

| Parameter | Description |
|---|---|
| Name | Name of the VLAN interface |
| VLAN ID | ID of the VLAN (1-4094) |
| Bridge Port | Physical interface to bridge the VLAN to |

Repeat this step for each VLAN required.

**2. Assign VLANs to Interfaces**

Navigate to the physical interface (e.g., **ether1**) you want to assign a VLAN to. Click the **Bridge** tab. In the **VLAN** field, select the desired VLAN interface.

**3. Configure Inter-VLAN Routing**

Enable IP routing on the router by navigating to **IP** > **Routing** and selecting **Enable IP Forwarding**.

Add a static route for each VLAN subnet. For example, for a VLAN with ID 10 and subnet 10.0.10.0/24:

```
/ip route add dst-address=10.0.10.0/24 gateway=LAN-interface
```

**4. Enable VLAN Tagging (Optional)**

If using VLAN tagging on the physical interfaces, enable it by navigating to **Interfaces** > **VLAN** and selecting the **Enable Tagging** checkbox for the VLAN interfaces.

### Complete Configuration Commands

```
/interface vlan add name=VLAN10 vlan-id=10
/interface bridge port add bridge=VLAN10 interface=ether1
/ip route add dst-address=10.0.10.0/24 gateway=LAN-interface
```

### Common Pitfalls and Solutions

- **VLAN ID Conflict:** Ensure that each VLAN ID is unique and does not conflict with existing VLANs.
- **Incorrect Bridge Port Assignment:** Ensure that the physical interface is capable of bridging VLANs and is assigned to the correct VLAN interface.
- **Missing IP Routing:** Remember to enable IP forwarding and add static routes for each VLAN subnet.
- **VLAN Tagging Mismatch:** If using VLAN tagging, ensure that it is enabled on both the router and the connected devices.

### Verification and Testing Steps

- Check the VLAN interface status by navigating to **Interfaces** > **VLAN**.
- Assign devices to different VLANs and verify connectivity within each VLAN.
- Use a tool like "ping" or "traceroute" to test communication between devices in different VLANs.

### Related Features and Considerations

- **VLAN Trunking:** Allows multiple VLANs to be carried over a single physical link.
- **Security:** Use access control lists (ACLs) to restrict traffic between VLANs.
- **VLAN Groups:** Group multiple VLANs together for easier management.

### MikroTik REST API Examples

**Retrieve VLAN List:**

**Endpoint:** `/interface/vlan`

**Method:** GET

**Example Response:**

```json
[
  {
    "interface": "VLAN10",
    "vlan-id": 10,
    "bridge-port": "ether1"
  }
]
```

**Create VLAN:**

**Endpoint:** `/interface/vlan`

**Method:** POST

**Example JSON Payload:**

```json
{
  "name": "VLAN10",
  "vlan-id": 10,
  "bridge-port": "ether1"
}
```