## VLAN Configuration in RouterOS 7.11 (Expert)

**Configuration Scenario and Requirements**

- Configure multiple VLANs on a MikroTik router for network segmentation.
- Assign devices to specific VLANs based on their network location.
- Implement inter-VLAN routing to allow communication between different VLANs.

## Step-by-Step Implementation

### 1. Create VLANs

```
/interface vlan add name=VLAN1 vid=1
/interface vlan add name=VLAN2 vid=2
```

| Parameter | Description |
|---|---|
| name | Name of the VLAN |
| vid | VLAN ID (1-4094) |

### 2. Assign Interfaces to VLANs

```
/interface add bridge=bridge-name ports=eth1 vlan=VLAN1
/interface add bridge=bridge-name ports=eth2 vlan=VLAN2
```

| Parameter | Description |
|---|---|
| bridge-name | Name of the bridge interface that will aggregate the VLANs |
| ports | Physical interfaces to be added to the bridge and assigned to the VLAN |

### 3. Create VLAN Subinterfaces for Routing

```
/interface vlan subinterface add interface=vlan1 name=vlan1-sub1 vlan-id=1
/interface vlan subinterface add interface=vlan2 name=vlan2-sub1 vlan-id=2
```

| Parameter | Description |
|---|---|
| interface | Parent VLAN interface |
| name | Subinterface name |
| vlan-id | VLAN ID (must match the corresponding VLAN) |

### 4. Configure IP Addresses on VLAN Subinterfaces

```
/ip address add address=192.168.1.1/24 interface=vlan1-sub1
/ip address add address=192.168.2.1/24 interface=vlan2-sub1
```

| Parameter | Description |
|---|---|
| address | IP address and subnet mask for the VLAN subnet |
| interface | VLAN subinterface |

### 5. Enable Inter-VLAN Routing

```
/ip firewall add action=accept chain=forward dst-address=192.168.0.0/16 out-interface=vlan1-sub1
/ip firewall add action=accept chain=forward dst-address=192.168.0.0/16 out-interface=vlan2-sub1
```

| Parameter | Description |
|---|---|
| action | Firewall action (accept/drop) |
| chain | Firewall chain (input/output/forward) |
| dst-address | Destination IP address range for VLAN traffic |
| out-interface | VLAN subinterface for outgoing traffic |

## Common Pitfalls and Solutions

- **VLAN ID Conflict:** Ensure that VLAN IDs are unique across all interfaces.
- **Unassigned Interfaces:** Verify that all physical interfaces are assigned to a VLAN or bridge.
- **Firewall Rules:** Check that firewall rules allow communication between VLANs as intended.

## Verification and Testing Steps

- Ping between devices on different VLANs to confirm connectivity.
- Use traceroute to verify routing paths between VLANs.
- Check IP addresses and firewall rules for accuracy.

## Related Features and Considerations

- **VLAN Tagging:** Configure VLAN tagging for trunk ports that carry multiple VLANs.
- **Security:** Implement security measures on VLAN interfaces to isolate traffic.
- **QoS:** Prioritize traffic based on VLANs using bandwidth management features.

## MikroTik REST API Example

**Endpoint:** `/interface/vlan`

**Method:** `POST`

**Request Payload (JSON):**

```json
{
  "name": "VLAN3",
  "vid": 3
}
```

**Response (JSON):**

```json
{
  "id": 4,
  "name": "VLAN3",
  "vid": 3
}
```