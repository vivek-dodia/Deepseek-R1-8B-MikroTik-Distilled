## VLAN Configuration in RouterOS 6.48 for ISP

### Configuration Scenario and Requirements

Configure VLANs on a MikroTik router to segment a network for an ISP. Multiple customers will connect to the router using tagged VLANs, and the router will route traffic between the VLANs and the external Internet.

### Step-by-Step Implementation

1. **Create the VLANs:**

   - Navigate to **Interfaces** > **VLAN**
   - Click **+** to create a new VLAN
   - Enter a **VLAN ID** and select the **Parent Interface** that the VLAN will be tagged on

2. **Configure the Parent Interface:**

   - Navigate to **Interfaces** > **<parent_interface_name>**
   - Enable **VLAN**
   - Select the **Name** of the VLAN created in step 1

3. **Add VLAN Interfaces:**

   - Navigate back to **Interfaces** > **VLAN**
   - For each VLAN, click **+** to create a new VLAN interface
   - Assign an **Interface Name** (e.g., vlan1, vlan2)
   - Select the **VLAN ID** and **Parent Interface**

4. **Create Firewall Rules:**

   - Navigate to **Firewall** > **Filter Rules**
   - Create a rule for each VLAN interface
   - Allow traffic from the VLAN interface to the external Internet (e.g., masquerade)

### Complete Configuration Commands

```
/interface vlan
add name=vlan1 vlan-id=1 parent=eth1
/interface vlan
add name=vlan2 vlan-id=2 parent=eth2
/interface vlan
add name=vlan1 interface=vlan1
/interface vlan
add name=vlan2 interface=vlan2
/ip firewall filter
add action=accept chain=forward in-interface=vlan1
/ip firewall filter
add action=accept chain=forward in-interface=vlan2
```

### Common Pitfalls and Solutions

- Ensure that the parent interface has VLAN enabled before adding VLAN interfaces.
- Double-check that the VLAN ID and parent interface are correct for each VLAN.
- If traffic is not flowing between VLANs, verify that firewall rules are correctly configured.

### Verification and Testing Steps

1. Use a VLAN-aware device to connect to each VLAN interface.
2. Verify that the device receives an IP address from the correct DHCP server.
3. Ping between devices on different VLANs to test connectivity.

### Related Features and Considerations

- Use **VLAN Trunking** to create a single trunk port that carries multiple VLANs.
- Configure **DHCP Server** on each VLAN to provide IP addresses to clients.
- Implement **Quality of Service (QoS)** to prioritize traffic on specific VLANs.

### MikroTik REST API Examples

**Endpoint:** `/interface/vlan`

**Request Method:** GET

**Example JSON Payload:**

```
{
  "filter": {
    "name": "vlan1"
  }
}
```

**Expected Response:**

```
[
  {
    "interface": "vlan1",
    "name": "vlan1",
    "vlan-id": 1,
    "parent": "eth1",
    "status": "running"
  }
]
```