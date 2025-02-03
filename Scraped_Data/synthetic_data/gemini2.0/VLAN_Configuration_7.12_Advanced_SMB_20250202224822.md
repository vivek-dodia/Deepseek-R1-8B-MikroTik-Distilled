## VLAN Configuration in MikroTik RouterOS 7.12

### Configuration Scenario and Requirements

* Create multiple VLANs to segment the network into logical subnets.
* Assign VLANs to physical interfaces or ports.
* Configure firewall rules to restrict traffic between VLANs.

### Step-by-Step Implementation

**1. Create VLANs:**

```
/interface vlan add name=VLAN1 vlan-id=10
/interface vlan add name=VLAN2 vlan-id=20
/interface vlan add name=VLAN3 vlan-id=30
```

**2. Assign VLANs to Interfaces:**

```
/interface ethernet set ether1 switch-vlan-tagged=VLAN1,VLAN2,VLAN3
/interface ethernet set ether2 switch-vlan-tagged=VLAN2,VLAN3
```

**3. Configure Firewall Rules:**

```
/ip firewall filter add chain=forward action=accept in-interface=VLAN1 out-interface=VLAN2
/ip firewall filter add chain=forward action=accept in-interface=VLAN2 out-interface=VLAN1
```

### Complete Configuration Commands

**VLAN Creation:**

```
/interface vlan add name=VLAN-NAME vlan-id=VLAN-ID
```

| Parameter | Description |
|---|---|
| name | Name of the VLAN |
| vlan-id | VLAN identifier (range: 1-4094) |

**VLAN Interface Assignment:**

```
/interface ethernet set INTERFACE-NAME switch-vlan-tagged=VLAN-LIST
```

| Parameter | Description |
|---|---|
| INTERFACE-NAME | Name of the physical interface |
| switch-vlan-tagged | List of VLANs to tag on the interface |

**Firewall Rule Configuration:**

```
/ip firewall filter add chain=FORWARD action=ACCEPT in-interface=VLAN-IN out-interface=VLAN-OUT
```

| Parameter | Description |
|---|---|
| chain | Firewall rule chain (e.g., forward) |
| action | Action to take on matching traffic |
| in-interface | Input VLAN interface |
| out-interface | Output VLAN interface |

### Common Pitfalls and Solutions

* Ensure that the VLAN ID is unique across all interfaces.
* If a device is not receiving traffic after VLAN configuration, check the physical port assignment and firewall rules.
* Use the `/interface vlan print` command to verify VLAN configurations.

### Verification and Testing Steps

* Use the `/interface vlan print` command to display VLAN information.
* Use a packet capture tool to verify traffic flow between VLANs.
* Test connectivity between devices in different VLANs.

### Related Features and Considerations

* **VLAN Trunking:** Configure a trunk port to carry multiple VLANs over a single physical link.
* **VLAN Filtering:** Enable VLAN filtering on interfaces to restrict traffic to specific VLANs.
* **VLAN Protocol:** Use the `/ip vlan protocol` command to specify the VLAN protocol (e.g., 802.1Q, 802.1ad).

### MikroTik REST API Examples

**Create a VLAN:**

**API Endpoint:** `/interface/vlan`

**Request Method:** POST

**JSON Payload:**

```json
{
  "interface": "VLAN-NAME",
  "vlan-id": VLAN-ID
}
```

**Expected Response:**

```json
{
  "id": "ID-OF-NEW-VLAN"
}
```

**Assign VLAN to Interface:**

**API Endpoint:** `/interface/ethernet/set`

**Request Method:** POST

**JSON Payload:**

```json
{
  "interface": "INTERFACE-NAME",
  "switch-vlan-tagged": "VLAN-LIST"
}
```

**Expected Response:**

```json
{
  "interface": "INTERFACE-NAME"
}
```