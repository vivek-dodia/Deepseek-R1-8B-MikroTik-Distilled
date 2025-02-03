## VLAN Configuration on MikroTik RouterOS 6.48

### Configuration Scenario and Requirements

* Create VLANs on a MikroTik router.
* Assign ports to the VLANs.
* Allow communication between VLANs.

### Step-by-Step Implementation

1. Create VLANs:
   ```
   /interface vlan add name=VLAN1 vlan-id=10
   /interface vlan add name=VLAN2 vlan-id=20
   ```

2. Assign ports to VLANs:
   ```
   /interface bridge port add bridge=bridge1 interface=ether1 vlan-id=10
   /interface bridge port add bridge=bridge1 interface=ether2 vlan-id=20
   ```

3. Allow communication between VLANs:
   ```
   /ip firewall mangle add chain=forward action=accept comment=allow-vlan-traffic
   /ip firewall mangle add chain=forward src-address=10.0.0.0/24 dst-address=10.0.1.0/24 action=accept comment=allow-vlan-traffic
   /ip firewall mangle add chain=forward src-address=10.0.1.0/24 dst-address=10.0.0.0/24 action=accept comment=allow-vlan-traffic
   ```

### Complete Configuration Commands

```
/interface vlan add name=VLAN1 vlan-id=10
/interface vlan add name=VLAN2 vlan-id=20
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=10
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=20
/ip firewall mangle add chain=forward action=accept comment=allow-vlan-traffic
/ip firewall mangle add chain=forward src-address=10.0.0.0/24 dst-address=10.0.1.0/24 action=accept comment=allow-vlan-traffic
/ip firewall mangle add chain=forward src-address=10.0.1.0/24 dst-address=10.0.0.0/24 action=accept comment=allow-vlan-traffic
```

### Common Pitfalls and Solutions

* Ensure that the VLAN IDs are unique and do not overlap.
* Make sure that the ports are assigned to the correct VLANs.
* Check that the firewall rules are configured to allow traffic between the VLANs.

### Verification and Testing Steps

* Ping from one VLAN to another to verify connectivity.
* Use the "/ip firewall mangle print" command to check the firewall rules.

### Related Features and Considerations

* VLAN trunks can be used to extend VLANs across multiple switches.
* Security groups can be used to restrict access between VLANs.

### MikroTik REST API Examples

#### List VLANs

**Endpoint**: `/api/interface/vlan`
**Method**: GET
**Example Response**:
```json
[
  {
    "interface": "VLAN1",
    "vlan-id": 10
  },
  {
    "interface": "VLAN2",
    "vlan-id": 20
  }
]
```

#### Create VLAN

**Endpoint**: `/api/interface/vlan`
**Method**: POST
**Request Payload**:
```json
{
  "name": "VLAN3",
  "vlan-id": 30
}
```

#### Assign Port to VLAN

**Endpoint**: `/api/interface/bridge/port`
**Method**: POST
**Request Payload**:
```json
{
  "bridge": "bridge1",
  "interface": "ether3",
  "vlan-id": 30
}
```