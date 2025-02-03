## VLAN Configuration in MikroTik RouterOS 7.11

### 1. Configuration Scenario and Requirements

- **Goal:** Create and configure VLANs on a MikroTik router.
- **Requirements:**
    - MikroTik router running RouterOS 7.11 or higher
    - Multiple physical interfaces to create VLANs on

### 2. Step-by-Step Implementation

**2.1 Create VLAN Interfaces**
```
/interface vlan add vlan-id=<vlan-id> name=<vlan-name> interface=<physical-interface>
```
- **Example:** Create VLAN 10 on interface ether1
```
/interface vlan add vlan-id=10 name="VLAN10" interface=ether1
```

**2.2 Add IP Addresses to VLAN Interfaces**
```
/ip address add address=<ip-address>/<prefix> interface=<vlan-interface>
```
- **Example:** Assign IP address 192.168.10.1/24 to VLAN 10
```
/ip address add address=192.168.10.1/24 interface=VLAN10
```

**2.3 Create VLAN Bridge**
```
/bridge add name=<bridge-name> vlan=<vlan-list>
```
- **Example:** Create a bridge named "VLAN-Bridge" with VLAN 10 and 20
```
/bridge add name="VLAN-Bridge" vlan="VLAN10,VLAN20"
```

**2.4 Add Interfaces to Bridge**
```
/interface bridge add interface=<interface> bridge=<bridge-name>
```
- **Example:** Add ether2 interface to the VLAN-Bridge
```
/interface bridge add interface=ether2 bridge=VLAN-Bridge
```

### 3. Complete Configuration Commands

```
/interface vlan add vlan-id=10 name="VLAN10" interface=ether1
/interface vlan add vlan-id=20 name="VLAN20" interface=ether2
/ip address add address=192.168.10.1/24 interface=VLAN10
/ip address add address=192.168.20.1/24 interface=VLAN20
/bridge add name="VLAN-Bridge" vlan="VLAN10,VLAN20"
/interface bridge add interface=ether3 bridge=VLAN-Bridge
```

### 4. Common Pitfalls and Solutions

- **Duplicate VLAN IDs:** Ensure that each VLAN has a unique ID.
- **Overlapping IP Addresses:** Verify that each VLAN has a unique IP address range.
- **Incorrect Interface Assignments:** Make sure that VLAN interfaces are assigned to the correct physical interfaces.
- **VLAN Leaking:** Use trunking with VLAN tagging to prevent VLANs from leaking onto untagged interfaces.

### 5. Verification and Testing Steps

- Check VLAN interface configurations using:
```
/interface vlan print
```

- Verify IP addresses assigned to VLAN interfaces using:
```
/ip address print
```

- Test connectivity between devices in different VLANs.

### 6. Related Features and Considerations

- **VLAN Tagging:** Use VLAN tagging to differentiate traffic between VLANs.
- **Trunking:** Configure trunking on interfaces that connect to multiple VLANs.
- **Security:** Implement firewall rules and access control lists to control traffic between VLANs.

### 7. MikroTik REST API Examples

**Endpoint:** `/interface/vlan`

**Method:** POST

**Payload:**
```json
{
  "vlan-id": 10,
  "name": "VLAN10",
  "interface": "ether1"
}
```

**Response:**
```json
{
  "id": "2194439970"
}
```