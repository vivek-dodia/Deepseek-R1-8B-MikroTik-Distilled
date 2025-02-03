## VLAN Configuration in RouterOS 7.12 (ISP)

### Configuration Scenario and Requirements

Configure multiple VLANs on a MikroTik router to segment the network for different purposes, such as separating traffic for voice, data, and IoT devices.

### Step-by-Step Implementation

#### 1. Create VLAN Interfaces

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
/interface vlan add name=VLAN30 vlan-id=30
```

#### 2. Assign VLAN Interfaces to Physical Ports

```
/interface bridge port add interface=ether1 bridge=bridge1 vlan-id=10 tagged
/interface bridge port add interface=ether2 bridge=bridge1 vlan-id=20 tagged
/interface bridge port add interface=ether3 bridge=bridge1 vlan-id=30 tagged
```

#### 3. Create DHCP Server for Each VLAN

```
/ip dhcp-server add interface=VLAN10 address-pool=VLAN10-pool lease-time=86400
/ip dhcp-server add interface=VLAN20 address-pool=VLAN20-pool lease-time=86400
/ip dhcp-server add interface=VLAN30 address-pool=VLAN30-pool lease-time=86400
```

#### 4. Create Firewall Rules for Inter-VLAN Routing

```
/ip firewall filter add chain=forward in-interface=VLAN10 out-interface=VLAN20 action=accept
/ip firewall filter add chain=forward in-interface=VLAN20 out-interface=VLAN30 action=accept
/ip firewall filter add chain=forward in-interface=VLAN30 out-interface=VLAN10 action=accept
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
/interface vlan add name=VLAN30 vlan-id=30
/interface bridge port add interface=ether1 bridge=bridge1 vlan-id=10 tagged
/interface bridge port add interface=ether2 bridge=bridge1 vlan-id=20 tagged
/interface bridge port add interface=ether3 bridge=bridge1 vlan-id=30 tagged
/ip dhcp-server add interface=VLAN10 address-pool=VLAN10-pool lease-time=86400
/ip dhcp-server add interface=VLAN20 address-pool=VLAN20-pool lease-time=86400
/ip dhcp-server add interface=VLAN30 address-pool=VLAN30-pool lease-time=86400
/ip firewall filter add chain=forward in-interface=VLAN10 out-interface=VLAN20 action=accept
/ip firewall filter add chain=forward in-interface=VLAN20 out-interface=VLAN30 action=accept
/ip firewall filter add chain=forward in-interface=VLAN30 out-interface=VLAN10 action=accept
```

### Common Pitfalls and Solutions

- **Untagged Traffic Leakage:** Ensure that untagged traffic is not allowed on physical ports.
- **VLAN Membership:** Verify that all necessary devices are assigned to the correct VLANs.
- **Firewall Configuration:** Allow proper traffic flow between VLANs as per the required network topology.

### Verification and Testing Steps

- **VLAN Membership:** Run the `/interface vlan member print` command to verify the VLAN membership of physical ports.
- **DHCP Server:** Connect a device to a specific VLAN and check if it obtains an IP address from the corresponding DHCP server.
- **Inter-VLAN Routing:** Use `ping` or `traceroute` to test connectivity between devices in different VLANs.

### Related Features and Considerations

- **VLAN Trunking:** Configure 802.1q trunking to extend VLANs across multiple switches.
- **STP (Spanning Tree Protocol):** Enable STP to prevent network loops within VLANs.
- **Security:** Implement ACLs and firewall rules to control access and restrict traffic between VLANs.

### MikroTik REST API Examples

#### List VLANs

**Endpoint:** `/interface/vlan/getall`
**Request Method:** GET
**Example Request:**

```
GET /interface/vlan/getall
```

**Example Response:**

```json
[
  {
    "comment": null,
    "disabled": false,
    "interface": "bridge1.1",
    "ip": null,
    "mtu": null,
    "name": "VLAN10",
    "vlan-id": 10
  },
  {
    "comment": null,
    "disabled": false,
    "interface": "bridge1.2",
    "ip": null,
    "mtu": null,
    "name": "VLAN20",
    "vlan-id": 20
  }
]
```

#### Add a VLAN

**Endpoint:** `/interface/vlan/add`
**Request Method:** POST
**Example JSON Payload:**

```json
{
  "disabled": false,
  "interface": "bridge1",
  "name": "VLAN30",
  "vlan-id": 30
}
```

**Example Request:**

```
POST /interface/vlan/add
Content-Type: application/json

{
  "disabled": false,
  "interface": "bridge1",
  "name": "VLAN30",
  "vlan-id": 30
}
```