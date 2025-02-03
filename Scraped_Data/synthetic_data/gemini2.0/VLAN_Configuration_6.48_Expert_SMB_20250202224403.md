## VLAN Configuration in RouterOS 6.48

### Configuration Scenario and Requirements

- Configure multiple VLANs on a MikroTik router
- Assign ports to different VLANs
- Establish inter-VLAN routing

### Step-by-Step Implementation

1. **Enable VLAN Feature:**
```
/interface vlan enable
```

2. **Create VLAN Interfaces:**
```
/interface vlan add name=VLAN1 vlan-id=1
/interface vlan add name=VLAN2 vlan-id=2
```

3. **Assign Ports to VLANs:**
```
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=1
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=2
```

4. **Configure Inter-VLAN Routing:**
```
/ip route add dst-address=192.168.1.0/24 gateway=192.168.2.1 vlan=VLAN1
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.1 vlan=VLAN2
```

### Complete Configuration Commands

```
/interface vlan enable
/interface vlan add name=VLAN1 vlan-id=1
/interface vlan add name=VLAN2 vlan-id=2
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=1
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=2
/ip route add dst-address=192.168.1.0/24 gateway=192.168.2.1 vlan=VLAN1
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.1 vlan=VLAN2
```

### Common Pitfalls and Solutions

- **VLAN ID Conflict:** Ensure that each VLAN has a unique ID. Conflicts can cause connectivity issues.
- **Bridge Misconfiguration:** Verify that the bridge interfaces are correctly configured with the corresponding VLAN IDs.
- **Default Gateway Assignment:** Ensure that each VLAN has a unique default gateway for inter-VLAN routing.
- **IP Address Overlap:** Avoid using overlapping IP subnets on different VLANs to prevent routing conflicts.

### Verification and Testing Steps

- Check VLAN interfaces and port assignments: `/interface vlan print`
- Test connectivity within and between VLANs: Ping devices on different VLANs
- Verify inter-VLAN routing: Traceroute to devices on different VLANs

### Related Features and Considerations

- **QoS:** Prioritize traffic based on VLANs using queues and markings.
- **Security:** Isolate different VLANs with firewall rules or access control lists.
- **VLAN Trunking:** Extend VLANs across multiple switches using tagged ports.

### MikroTik REST API Examples

**Endpoint:** `/interface/vlan`

**Request Method:** GET

**Request Payload:**

```json
{
  "?.id": ":id"
}
```

**Response:**

```json
[
  {
    "allow-fast-path": false,
    "bridge": "bridge1",
    "id": "VLAN1",
    "interfaces": [
      "ether1"
    ],
    "name": "VLAN1",
    "vlan-id": 1
  },
  {
    "allow-fast-path": false,
    "bridge": "bridge1",
    "id": "VLAN2",
    "interfaces": [
      "ether2"
    ],
    "name": "VLAN2",
    "vlan-id": 2
  }
]
```