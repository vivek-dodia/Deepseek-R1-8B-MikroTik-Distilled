## MikroTik RouterOS VLAN Configuration Documentation

**Configuration Level:** Basic

**Network Scale:** Enterprise

### 1. Configuration Scenario and Requirements

Configure Virtual LANs (VLANs) on a MikroTik RouterOS-based network to segment traffic and improve security.

**Requirements:**
- RouterOS version 6.48 or later
- Physical network devices that support VLAN tagging

### 2. Step-by-Step Implementation

**Step 1: Create the VLAN Interface**

- Go to Interfaces > VLAN
- Click on "+" button
- Enter a name for the VLAN interface (e.g., "VLAN10")
- Select the physical interface to which the VLAN will be tagged (e.g., "ether1")
- Enter a VLAN ID (e.g., "10")
- Click "Apply"

**Step 2: Configure the VLAN Interface**

- Go to Interfaces > VLAN10 (the newly created VLAN interface)
- Configure IPv4 address, Subnet mask, and Gateway as needed
- Enable "DHCP Client" or configure static IP settings
- Click "Apply"

**Step 3: Add VLAN Member Interfaces**

- Go to Interfaces > ether1 (physical interface)
- Select the "VLAN" tab
- Check the box for "VLAN10" (the VLAN interface created in step 1)
- Click "Apply"

### 3. Complete Configuration Commands

```
/interface vlan add name=VLAN10 interface=ether1 vlan-id=10
/interface vlan set VLAN10 address=192.168.10.1/24
/interface vlan set VLAN10 dhcp-client enable=yes
/interface ethernet set ether1 vlan-mode=tagged
/interface ethernet set ether1 vlan-tagged-interface=VLAN10
```

### 4. Common Pitfalls and Solutions

- **VLAN ID Conflict:** Ensure that the VLAN ID used is unique across the network to avoid conflicts.
- **Incorrect Interface Assignment:** Double-check that the physical interface selected for VLAN tagging is capable of supporting it.
- **Misconfigured IP Settings:** Verify that the IP address, subnet mask, and gateway are correctly configured for the VLAN interface.

### 5. Verification and Testing Steps

- Go to Interfaces > VLAN10
- Check the status of the interface, it should be "active"
- Ping from a device connected to the VLAN to verify connectivity
- Check DHCP lease or static IP assignment on the VLAN interface

### 6. Related Features and Considerations

- **Bridge Configuration:** For more advanced VLAN configurations, consider using MikroTik's bridging capabilities to connect VLAN interfaces.
- **Firewall Rules:** Implement appropriate firewall rules to restrict traffic between different VLANs as required.
- **Security Best Practices:** Consider isolating sensitive VLANs from untrusted networks using ACLs or other security measures.

### 7. MikroTik REST API Examples

**Endpoint:** `/interface/vlan`

**Request Method:** GET

**Example Payload:**

```
{
  ".proplist": "interface,name,vlan-id"
}
```

**Expected Response:**

```
[
  {
    "interface": "VLAN10",
    "name": "VLAN10",
    "vlan-id": "10"
  }
]
```

**Request Method:** POST

**Example Payload:**

```
{
  "interface": "VLAN20",
  "name": "VLAN20",
  "vlan-id": "20"
}
```

**Expected Response:**

```
{
  "interface": "VLAN20",
  "name": "VLAN20",
  "vlan-id": "20"
}
```