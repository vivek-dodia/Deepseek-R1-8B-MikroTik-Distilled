## VLAN Configuration in MikroTik RouterOS 7.12

### 1. Configuration Scenario and Requirements

In this scenario, we need to configure VLANs to logically segment a network into multiple broadcast domains. Here are the requirements:

- Create two VLANs: VLAN 10 for data traffic and VLAN 20 for management traffic.
- Assign Ethernet ports to each VLAN.
- Allow inter-VLAN communication for specific services (e.g., DHCP, DNS).

### 2. Step-by-Step Implementation

**2.1. Create VLANs**

```
/interface vlan add name=vlan10
/interface vlan add name=vlan20
```

**2.2. Assign Ports to VLANs**

```
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=10
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=10
/interface bridge port add bridge=bridge2 interface=ether3 vlan-id=20
/interface bridge port add bridge=bridge2 interface=ether4 vlan-id=20
```

**2.3. Allow Inter-VLAN Communication**

```
/ip firewall rule add chain=input action=accept protocol=udp dst-port=67 dst-address-list=dhcp-clients in-interface=vlan10
/ip firewall rule add chain=input action=accept protocol=udp dst-port=53 dst-address-list=dns-clients in-interface=vlan20
```

### 3. Complete Configuration Commands

```
/interface vlan add name=vlan10
/interface vlan add name=vlan20
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=10
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=10
/interface bridge port add bridge=bridge2 interface=ether3 vlan-id=20
/interface bridge port add bridge=bridge2 interface=ether4 vlan-id=20
/ip firewall rule add chain=input action=accept protocol=udp dst-port=67 dst-address-list=dhcp-clients in-interface=vlan10
/ip firewall rule add chain=input action=accept protocol=udp dst-port=53 dst-address-list=dns-clients in-interface=vlan20
```

### 4. Common Pitfalls and Solutions

**Pitfall:** Forgetting to create a bridge for the VLANs.
**Solution:** Create a bridge before assigning ports to VLANs: `/interface bridge add name=bridge1`

**Pitfall:** Misconfiguring the firewall rules to allow inter-VLAN communication.
**Solution:** Ensure that the `dst-interface` parameter of the firewall rule matches the destination VLAN interface.

### 5. Verification and Testing Steps

- Check the VLAN configuration using `/interface vlan print`.
- Test connectivity between devices on different VLANs using ping.
- Use Wireshark to verify that traffic is being tagged with the correct VLAN ID.

### 6. Related Features and Considerations

- **VLAN Truncation:** Enable VLAN truncation on ports that connect to devices that do not support VLAN tagging.
- **VLAN Filtering:** Use VLAN filters to restrict traffic based on VLAN ID.
- **Security:** Implement security measures such as ACLs and firewall rules to protect the VLANs from unauthorized access.

### 7. MikroTik REST API Example

**API Endpoint:** `/interface/vlan`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "filter": {
    "name": "vlan10"
  }
}
```

**Expected Response:**

```json
[
  {
    "default-name": "vlan10",
    "name": "vlan10",
    "interfaces": [
      "ether1",
      "ether2"
    ]
  }
]
```