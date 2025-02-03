## VLAN Configuration in MikroTik RouterOS 7.12

### Configuration Scenario and Requirements

**Objective:** Configure multiple VLANs on a MikroTik router to segment a network into different logical domains.

**Requirements:**

- MikroTik router running RouterOS 7.12 or later
- Switch or switches capable of VLAN tagging
- Client devices that support VLAN tagging (e.g., PCs, servers, printers)

### Step-by-Step Implementation

1. **Create VLAN Interfaces:**

```bash
/interface vlan add name=VLAN1 vlan-id=1
/interface vlan add name=VLAN2 vlan-id=2
```

2. **Assign VLAN Interfaces to Physical Ports:**

```bash
/interface bridge port add bridge=bridge1 interface=ether1 vlan-filtering=yes vlan-id=1
/interface bridge port add bridge=bridge1 interface=ether2 vlan-filtering=yes vlan-id=2
```

3. **Create DHCP Server for Each VLAN:**

```bash
/ip dhcp-server add address-pool=VLAN1 interface=VLAN1 range=10.1.1.1-10.1.1.254 lease-time=24h
/ip dhcp-server add address-pool=VLAN2 interface=VLAN2 range=10.1.2.1-10.1.2.254 lease-time=24h
```

4. **Configure Firewall Rules:**

```bash
/ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade
/ip firewall nat add chain=dstnat in-interface=ether1 action=dst-nat to-addresses=10.1.1.0/24
/ip firewall filter add chain=input action=accept in-interface=VLAN1 src-address=10.1.1.0/24
/ip firewall filter add chain=input action=accept in-interface=VLAN2 src-address=10.1.2.0/24
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN1 vlan-id=1
/interface vlan add name=VLAN2 vlan-id=2
/interface bridge port add bridge=bridge1 interface=ether1 vlan-filtering=yes vlan-id=1
/interface bridge port add bridge=bridge1 interface=ether2 vlan-filtering=yes vlan-id=2
/ip dhcp-server add address-pool=VLAN1 interface=VLAN1 range=10.1.1.1-10.1.1.254 lease-time=24h
/ip dhcp-server add address-pool=VLAN2 interface=VLAN2 range=10.1.2.1-10.1.2.254 lease-time=24h
/ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade
/ip firewall nat add chain=dstnat in-interface=ether1 action=dst-nat to-addresses=10.1.1.0/24
/ip firewall filter add chain=input action=accept in-interface=VLAN1 src-address=10.1.1.0/24
/ip firewall filter add chain=input action=accept in-interface=VLAN2 src-address=10.1.2.0/24
```

### Common Pitfalls and Solutions

- **VLAN Flooding:** Ensure that switches are configured correctly to prevent VLAN flooding by enabling "Port Security" or "802.1x Authentication" on access ports.
- **DHCP Server Conflict:** Avoid configuring DHCP servers on different VLANs with overlapping IP address ranges.
- **Firewall Misconfiguration:** Ensure that firewall rules are properly configured to allow necessary traffic between VLANs and the external network.

### Verification and Testing Steps

- Verify that VLAN interfaces are created and assigned to ports using `/interface vlan print`.
- Check DHCP server status and client connectivity using `/ip dhcp-server print` and ping tests.
- Test connectivity between devices on different VLANs and the external network using ping or traceroute.

### Related Features and Considerations

- **VLAN Trunking:** Configure VLAN trunking on the router and switch ports to allow multiple VLANs to pass through a single physical link.
- **Inter-VLAN Routing:** Enable inter-VLAN routing to allow communication between VLANs without the need for VLAN-aware switches.
- **Security:** Implement VLANs in conjunction with firewall rules and access control lists to enhance network segmentation and security.

### MikroTik REST API Examples

**Get list of VLAN interfaces:**

**Endpoint:** `/interface/vlan/getall`

**Request Method:** GET

**Response Body:**

```json
[
  {
    "interface": "VLAN1",
    "vlan-id": 1,
    "mtu": 1500,
    "comment": ""
  },
  {
    "interface": "VLAN2",
    "vlan-id": 2,
    "mtu": 1500,
    "comment": ""
  }
]
```

**Create a new VLAN interface:**

**Endpoint:** `/interface/vlan/add`

**Request Method:** POST

**Request Body:**

```json
{
  "name": "VLAN3",
  "vlan-id": 3,
  "mtu": 1500
}
```

**Response Body:**

```json
{
  "interface": "VLAN3",
  "vlan-id": 3,
  "mtu": 1500,
  "comment": ""
}
```