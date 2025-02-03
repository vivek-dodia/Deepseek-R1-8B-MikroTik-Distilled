## VLAN Configuration in MikroTik RouterOS 7.11 (SOHO)

### Configuration Scenario and Requirements

- Create multiple VLANs on a MikroTik router to segregate network traffic based on logical groups.
- Configure each VLAN with a unique subnet and appropriate firewall rules to ensure traffic isolation.

### Step-by-Step Implementation

**1. Create VLAN Interfaces:**

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
```

**2. Configure IP Addresses:**

```
/ip address add address=192.168.10.1/24 interface=VLAN10
/ip address add address=192.168.20.1/24 interface=VLAN20
```

**3. Add Ports to VLANs:**

```
/interface vlan-member add interface=ether1 vlan=VLAN10 tagged=yes
/interface vlan-member add interface=ether2 vlan=VLAN10 untagged=yes
/interface vlan-member add interface=ether3 vlan=VLAN20 tagged=yes
/interface vlan-member add interface=ether4 vlan=VLAN20 untagged=yes
```

**4. Configure Firewall Rules:**

```
/ip firewall filter add in-interface=VLAN10 action=accept
/ip firewall filter add in-interface=VLAN20 action=accept
/ip firewall filter add src-address=192.168.10.0/24 dst-address=192.168.20.0/24 action=allow
/ip firewall filter add src-address=192.168.20.0/24 dst-address=192.168.10.0/24 action=allow
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20

/ip address add address=192.168.10.1/24 interface=VLAN10
/ip address add address=192.168.20.1/24 interface=VLAN20

/interface vlan-member add interface=ether1 vlan=VLAN10 tagged=yes
/interface vlan-member add interface=ether2 vlan=VLAN10 untagged=yes
/interface vlan-member add interface=ether3 vlan=VLAN20 tagged=yes
/interface vlan-member add interface=ether4 vlan=VLAN20 untagged=yes

/ip firewall filter add in-interface=VLAN10 action=accept
/ip firewall filter add in-interface=VLAN20 action=accept
/ip firewall filter add src-address=192.168.10.0/24 dst-address=192.168.20.0/24 action=allow
/ip firewall filter add src-address=192.168.20.0/24 dst-address=192.168.10.0/24 action=allow
```

### Common Pitfalls and Solutions

- **VLAN ID Conflict:** Ensure that the VLAN IDs used do not conflict with any existing ones.
- **Incorrect Port Membership:** Verify that ports are assigned to the correct VLANs and with the appropriate tagging options.
- **Firewall Rule Overlap:** Pay attention to the order of firewall rules and ensure that traffic is not inadvertently blocked.

### Verification and Testing Steps

- Verify the creation of VLAN interfaces using `/interface vlan print`.
- Check IP addresses and subnet configurations using `/ip address print`.
- Use `/ip firewall filter print` to inspect the firewall rules.
- Connect devices to the appropriate VLAN ports and test connectivity using ping.

### Related Features and Considerations

- **VLAN Trunking:** Use a trunk port to carry traffic for multiple VLANs over a single physical link.
- **VLAN QoS:** Prioritize traffic on different VLANs using Quality of Service (QoS) policies.
- **VLAN Aliasing:** Create aliases for VLANs to make their names more descriptive.

### MikroTik REST API Examples

**Endpoint:** `/interface/vlan`

**Request Method:** GET

**Request Payload:**

```json
{
  "filter": {
    "name": "VLAN10"
  }
}
```

**Response:**

```json
[
  {
    "interface": "VLAN10",
    "vlan-id": 10,
    "frame-type": "native",
    "translation-ports": [],
    "interfaces": []
  }
]
```