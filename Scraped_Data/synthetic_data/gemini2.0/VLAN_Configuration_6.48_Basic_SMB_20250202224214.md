## VLAN Configuration in RouterOS 6.48

### 1. Configuration Scenario and Requirements

- Create VLANs and assign them to physical interfaces
- Configure inter-VLAN routing and firewall rules

### 2. Step-by-Step Implementation

**VLAN Creation:**

1. Navigate to Interfaces -> VLANs -> +.
2. Enter a VLAN ID (e.g., 100).
3. Select the physical interface to associate with the VLAN (e.g., ether2).

**Inter-VLAN Routing:**

1. Navigate to IP -> Routes -> +.
2. Set the Destination to the VLAN IP range (e.g., 192.168.100.0/24).
3. Set the Gateway to the router's interface IP on the same VLAN (e.g., 192.168.100.1).

**Firewall Rules:**

1. Navigate to IP -> Firewall -> Filter Rules -> +.
2. Create a rule to allow traffic between VLANs (e.g., from VLAN 100 to VLAN 200).
    - Set the Src. Address to VLAN 100's IP range (192.168.100.0/24).
    - Set the Dst. Address to VLAN 200's IP range (192.168.200.0/24).

### 3. Complete Configuration Commands

```
/interface vlan add name=VLAN100 interface=ether2
/ip route add dst-address=192.168.100.0/24 gateway=192.168.100.1
/ip firewall filter add action=accept chain=forward in-interface=VLAN100 out-interface=VLAN200 src-address=192.168.100.0/24 dst-address=192.168.200.0/24
```

### 4. Common Pitfalls and Solutions

- **VLAN ID conflicts:** Check for any overlapping VLAN IDs across devices.
- **Incorrect interface assignment:** Ensure that the physical interface is correctly assigned to the VLAN.
- **Routing issues:** Verify that the routes between VLANs are configured correctly.
- **Firewall blocking:** Ensure that firewall rules are allowing traffic between the desired VLANs.

### 5. Verification and Testing Steps

- Ping between devices on different VLANs to ensure connectivity.
- Check the routing table (/ip route print) to validate inter-VLAN routing.
- Use the firewall filter command to verify that the rules are configured as expected.

### 6. Related Features and Considerations

- **Spanning Tree Protocol (STP):** STP should be configured to prevent loops when using VLANs.
- **VLAN Trunking:** Use trunking protocols (e.g., 802.1Q) to carry multiple VLANs over a single physical link.
- **Security:** Implement strong firewall rules and access control lists (ACLs) to protect VLANs from unauthorized access.

### 7. MikroTik REST API Examples

**Create VLAN:**

```json
POST /interface/vlan
{
  "name": "VLAN100",
  "interface": "ether2"
}
```

**Get VLANs:**

```json
GET /interface/vlan
```

**Create Firewall Rule:**

```json
POST /ip/firewall/filter
{
  "action": "accept",
  "chain": "forward",
  "in-interface": "VLAN100",
  "out-interface": "VLAN200",
  "src-address": "192.168.100.0/24",
  "dst-address": "192.168.200.0/24"
}
```