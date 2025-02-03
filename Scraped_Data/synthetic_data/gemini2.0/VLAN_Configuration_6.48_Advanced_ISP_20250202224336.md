## VLAN Configuration on MikroTik RouterOS 6.x

### Configuration Scenario and Requirements

- Create and configure VLANs for isolating traffic on a network.
- Assign ports to specific VLANs for segmentation and security.
- Utilize default VLANs and untagged ports for administrative access.

### Step-by-Step Implementation

1. **Create VLANs:** Navigate to `Interfaces` > `VLAN` and click on the `+` button. Specify a `VLAN ID` and a descriptive `Name`. Repeat this process to create multiple VLANs.

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
```

2. **Assign Ports to VLANs:** Go to `Interfaces` > `Bridge` and select the bridge interface you want to configure. Click on the `Ports` tab. Select the desired port and choose the VLAN from the `VLAN ID` dropdown.

```
/interface bridge port add interface=ether1 bridge=bridge1 vlan-id=10
/interface bridge port add interface=ether2 bridge=bridge1 vlan-id=20
```

3. **Configure Default VLAN:** By default, RouterOS uses VLAN1 as the default VLAN. To modify this, go to `/system vlan` and set the `Default VLAN` parameter.

```
/system vlan set default-vlan=10
```

4. **Configure Untagged Ports:** Ports that should receive untagged traffic (default VLAN) can be configured by selecting `untagged` under the `VLAN ID` dropdown in the `Bridge` interface.

```
/interface bridge port add interface=ether3 bridge=bridge1 vlan-id=untagged
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
/interface bridge port add interface=ether1 bridge=bridge1 vlan-id=10
/interface bridge port add interface=ether2 bridge=bridge1 vlan-id=20
/system vlan set default-vlan=10
/interface bridge port add interface=ether3 bridge=bridge1 vlan-id=untagged
```

### Common Pitfalls and Solutions

**Duplicate VLAN IDs:** Ensure that each VLAN has a unique ID to avoid traffic collision.

**Unassigned Ports:** Make sure that all necessary ports are assigned to the correct VLANs.

**Default VLAN Conflicts:** Verify that the default VLAN is set appropriately for management access.

**STP Issues:** Spanning Tree Protocol (STP) can cause connectivity issues if configured incorrectly. Check STP settings and ensure they are appropriate for the network topology.

### Verification and Testing Steps

1. Use the command `/interface vlan print` to verify the created VLANs and their IDs.
2. Ping devices connected to different VLANs to test connectivity.
3. Verify that management traffic is accessible on the default VLAN.

### Related Features and Considerations

- **VLAN Trunks:** Use `VLAN trunks` to allow multiple VLANs to pass through a single physical link.
- **VLAN Security:** Implement access control lists (ACLs) on VLAN interfaces to restrict traffic flow and enhance security.
- **VLAN Routing:** Configure VLANs to participate in routing between different subnets.

### MikroTik REST API Examples

**Endpoint:** `/interface/vlan`

**Request Method:** GET

**Request JSON:**

```
{
  ":id": "1",
  ":limit": "10",
  ":order": [
    "name"
  ],
  ":where": {"name": "VLAN10"}
}
```

**Expected Response:**

```
[
  {
    "disabled": false,
    "interface": "ether1",
    "name": "VLAN10",
    "vlan-id": 10
  }
]
```

**Endpoint:** `/interface/vlan/add`

**Request Method:** POST

**Request JSON:**

```
{
  "name": "VLAN20",
  "vlan-id": 20
}
```

**Expected Response:**

```
{
  "error": null,
  "message": "added",
  ":id": "2"
}
```