## VLAN Configuration in MikroTik RouterOS 6.x

### 1. Configuration Scenario and Requirements

**Objective:** Configure multiple VLANs on a MikroTik router to segregate network traffic and improve security.

**Requirements:**
- MikroTik router running RouterOS 6.x
- Ethernet interfaces to connect VLAN members
- VLAN IDs to be created (e.g., 10, 20, 30)

### 2. Step-by-Step Implementation

**2.1. Create VLAN Interfaces**

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
/interface vlan add name=VLAN30 vlan-id=30
```

**2.2. Assign Interfaces to VLANs**

```
/interface ethernet set ether1 switch-vlan-ports=VLAN10
/interface ethernet set ether2 switch-vlan-ports=VLAN20
/interface ethernet set ether3 switch-vlan-ports=VLAN30
```

**2.3. Create VLAN Bridge**

```
/interface bridge add name=vlan-bridge
/interface bridge port add bridge=vlan-bridge interface=VLAN10
/interface bridge port add bridge=vlan-bridge interface=VLAN20
/interface bridge port add bridge=vlan-bridge interface=VLAN30
```

**2.4. Assign IP Addresses to VLAN Interfaces**

```
/ip address add address=10.0.10.1/24 interface=VLAN10
/ip address add address=10.0.20.1/24 interface=VLAN20
/ip address add address=10.0.30.1/24 interface=VLAN30
```

### 3. Complete Configuration Commands

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
/interface vlan add name=VLAN30 vlan-id=30
/interface ethernet set ether1 switch-vlan-ports=VLAN10
/interface ethernet set ether2 switch-vlan-ports=VLAN20
/interface ethernet set ether3 switch-vlan-ports=VLAN30
/interface bridge add name=vlan-bridge
/interface bridge port add bridge=vlan-bridge interface=VLAN10
/interface bridge port add bridge=vlan-bridge interface=VLAN20
/interface bridge port add bridge=vlan-bridge interface=VLAN30
/ip address add address=10.0.10.1/24 interface=VLAN10
/ip address add address=10.0.20.1/24 interface=VLAN20
/ip address add address=10.0.30.1/24 interface=VLAN30
```

### 4. Common Pitfalls and Solutions

- **VLAN ID conflict:** Ensure VLAN IDs are unique across the network to avoid conflicts.
- **VLAN interface not created:** Verify that the VLAN interfaces have been created before assigning them to the bridge.
- **Bridge port not configured:** Check that the VLAN interfaces have been added as bridge ports to the VLAN bridge.
- **IP address conflict:** Avoid assigning duplicate IP addresses within the same VLAN.

### 5. Verification and Testing Steps

- Check the VLAN interface configuration using `/interface vlan print`.
- Verify the bridge configuration using `/interface bridge print`.
- Test connectivity between devices within each VLAN.

### 6. Related Features and Considerations

- **VLAN tagging:** Enable dot1q VLAN tagging on Ethernet interfaces to ensure traffic is properly tagged with VLAN IDs.
- **Security:** Implement access control lists (ACLs) to restrict traffic between VLANs and enhance network security.
- **QoS:** Configure Quality of Service (QoS) policies to prioritize traffic on specific VLANs.

### 7. MikroTik REST API Examples

**API Endpoint:** `/interface/vlan`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "id": "VLAN10"
}
```

**Expected Response:**

```json
{
  "interface": "VLAN10",
  "vlan-id": 10
}
```