## VLAN Configuration in RouterOS 7.12

### Configuration Scenario and Requirements

- Create multiple isolated virtual networks (VLANs) on a single physical network.
- Assign ports to specific VLANs to segregate traffic.
- Allow communication between VLANs as needed.

### Step-by-Step Implementation

#### 1. Create VLANs

- Go to **Interfaces** > **VLAN**
- Click on **+** to create a new VLAN
- Enter a **Name** (e.g., VLAN1, VLAN2)
- Select the **VLAN ID** (range: 1-4094)
- Click on **Apply**

#### 2. Assign Ports to VLANs

- Go to **Interfaces** > **Ports**
- Select the port(s) you want to assign to the VLAN
- In the **VLAN** field, enter the VLAN ID (e.g., 1 for VLAN1)
- Click on **Apply**

#### 3. Configure Inter-VLAN Communication (Optional)

To allow communication between VLANs, create a bridge between them:

- Go to **Interfaces** > **Bridge**
- Click on **+** to create a new bridge
- Enter a **Name** (e.g., InterVLAN)
- In the **Members** field, add the VLAN interfaces (e.g., VLAN1, VLAN2)
- Click on **Apply**

### Complete Configuration Commands

```
# Create VLAN
/interface vlan add name=VLAN1 vlan-id=1

# Assign Port to VLAN
/interface bridge port set bridge=VLAN1 vlan-id=1

# Create Bridge
/interface bridge add name=InterVLAN

# Add VLANs to Bridge
/interface bridge port add bridge=InterVLAN interface=VLAN1
/interface bridge port add bridge=InterVLAN interface=VLAN2
```

### Common Pitfalls and Solutions

- **Untagged VLAN Traffic:** If untagged traffic is present on a port, it will flood to all VLANs. Use a VLAN-aware switch or configure a default VLAN.
- **Duplicate VLAN IDs:** Ensure that VLAN IDs are unique across all switches and routers.
- **Security Concerns:** Inter-VLAN communication can introduce security risks. Use firewalls or ACLs to control access between VLANs.

### Verification and Testing Steps

- Check the VLAN configuration by going to **Interfaces** > **VLAN**
- Verify that ports are assigned to the correct VLANs by going to **Interfaces** > **Ports**
- Test inter-VLAN communication using ping or other connectivity tools.

### Related Features and Considerations

- **VLAN Trunks:** Use VLAN trunks to connect switches and routers that support multiple VLANs.
- **VLAN Subinterfaces:** Create subinterfaces on a physical interface to assign multiple VLANs to a single port.
- **Security:** Implement access control lists (ACLs) or firewall rules to restrict traffic flow between VLANs.