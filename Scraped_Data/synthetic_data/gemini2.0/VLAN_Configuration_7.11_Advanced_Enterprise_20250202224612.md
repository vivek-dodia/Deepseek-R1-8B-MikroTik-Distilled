## VLAN Configuration in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

- Create multiple VLANs on a single physical interface (ethernet or switch port)
- Assign VLAN tags to traffic and communicate between VLANs

### Step-by-Step Implementation

**1. Create VLAN Interfaces**

```
/interface vlan add name=VLAN1 vlan-id=1
/interface vlan add name=VLAN2 vlan-id=2
```

**2. Assign VLAN Tags to Physical Interfaces**

```
/interface ethernet set ether1 tagged-vlan=add vlan1
/interface ethernet set ether2 tagged-vlan=add vlan2
```

**3. Add VLANs to Bridge**

```
/interface bridge add name=my-bridge
/interface bridge port add bridge=my-bridge interface=vlan1
/interface bridge port add bridge=my-bridge interface=vlan2
```

**4. Create DHCP Server for VLANs**

```
/ip dhcp-server add interface=vlan1 address-pool=vlan1
/ip dhcp-server add interface=vlan2 address-pool=vlan2
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN1 vlan-id=1
/interface vlan add name=VLAN2 vlan-id=2
/interface ethernet set ether1 tagged-vlan=add vlan1
/interface ethernet set ether2 tagged-vlan=add vlan2
/interface bridge add name=my-bridge
/interface bridge port add bridge=my-bridge interface=vlan1
/interface bridge port add bridge=my-bridge interface=vlan2
/ip dhcp-server add interface=vlan1 address-pool=vlan1
/ip dhcp-server add interface=vlan2 address-pool=vlan2
```

### Common Pitfalls and Solutions

- Ensure that the physical interface supports VLAN tagging.
- Verify that the VLAN IDs are unique within the network.
- Double-check that the VLAN interfaces are added to the correct bridge.

### Verification and Testing Steps

- Check the VLAN interfaces using `/interface vlan print`.
- Verify that devices on the VLANs can communicate with each other.
- Use the `/ip arp print` command to confirm the MAC address table entries.

### Related Features and Considerations

- **QinQ VLANs:** Nested VLANs can be configured within a single trunk interface.
- **VLAN Trunks:** Use trunk ports to aggregate multiple VLANs over a single physical link.
- **Security:** Configure MAC ACLs or firewall rules to control traffic between VLANs.

### MikroTik REST API Examples

**Create a VLAN:**

**Endpoint:** `/interface/vlan`
**Method:** POST
**Payload:**
```json
{
  "name": "VLAN1",
  "vlan-id": 1
}
```
**Response:**
```json
{
  "id": 1
}
```

**Assign a VLAN Tag to an Interface:**

**Endpoint:** `/interface/ethernet/{interface-id}`
**Method:** PUT
**Payload:**
```json
{
  "tagged-vlan": "add",
  "vlan-id": 1
}
```
**Response:**
```json
{
  "id": 2
}
```