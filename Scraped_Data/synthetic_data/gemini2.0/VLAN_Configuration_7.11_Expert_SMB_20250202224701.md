## VLAN Configuration in RouterOS 7.11 (Expert)

### Configuration Scenario and Requirements

The task is to create multiple VLANs on a RouterOS device and configure them for network segmentation and traffic isolation. The network consists of different departments (e.g., Finance, IT, Marketing), and each department requires its own isolated network.

**Requirements:**

- RouterOS 7.11 (or higher) device
- VLAN-capable physical switches
- Subnets and IP addresses for each VLAN

### Step-by-Step Implementation

**1. Create VLANs**

```bash
/interface vlan add name=Finance-VLAN vlan-id=10
/interface vlan add name=IT-VLAN vlan-id=20
/interface vlan add name=Marketing-VLAN vlan-id=30
```

**2. Assign VLANs to Physical Interfaces**

```bash
/interface ethernet set ether1 tagged-vlan-id=Finance-VLAN
/interface ethernet set ether2 tagged-vlan-id=IT-VLAN
/interface ethernet set ether3 tagged-vlan-id=Marketing-VLAN
```

**3. Configure Subnets for VLANs**

```bash
/ip address add address=10.10.10.1/24 interface=Finance-VLAN
/ip address add address=10.10.20.1/24 interface=IT-VLAN
/ip address add address=10.10.30.1/24 interface=Marketing-VLAN
```

**4. Configure Routing between VLANs**

```bash
/ip route add dst-address=0.0.0.0/0 gateway=10.10.10.1 interface=Finance-VLAN
/ip route add dst-address=0.0.0.0/0 gateway=10.10.20.1 interface=IT-VLAN
/ip route add dst-address=0.0.0.0/0 gateway=10.10.30.1 interface=Marketing-VLAN
```

**5. Test Connectivity**

Use a device connected to each VLAN to ping devices in other VLANs.

### Complete Configuration Commands

```bash
/interface vlan add name=Finance-VLAN vlan-id=10
/interface vlan add name=IT-VLAN vlan-id=20
/interface vlan add name=Marketing-VLAN vlan-id=30

/interface ethernet set ether1 tagged-vlan-id=Finance-VLAN
/interface ethernet set ether2 tagged-vlan-id=IT-VLAN
/interface ethernet set ether3 tagged-vlan-id=Marketing-VLAN

/ip address add address=10.10.10.1/24 interface=Finance-VLAN
/ip address add address=10.10.20.1/24 interface=IT-VLAN
/ip address add address=10.10.30.1/24 interface=Marketing-VLAN

/ip route add dst-address=0.0.0.0/0 gateway=10.10.10.1 interface=Finance-VLAN
/ip route add dst-address=0.0.0.0/0 gateway=10.10.20.1 interface=IT-VLAN
/ip route add dst-address=0.0.0.0/0 gateway=10.10.30.1 interface=Marketing-VLAN
```

### Common Pitfalls and Solutions

- **VLANs not passing traffic:** Ensure that physical switches are correctly configured to support VLANs. Check for correct VLAN membership and trunking configuration.
- **Devices cannot reach gateway:** Verify that the gateway IP address is correct and that the device is assigned to the correct VLAN. Check for any firewall rules that may be blocking traffic.
- **Inter-VLAN routing not working:** Confirm that the routing table is configured correctly and that there are no conflicts with other routes. Verify that the default route is pointing to the appropriate gateway.

### Verification and Testing Steps

- **Ping test:** Use a device connected to each VLAN to ping devices in other VLANs.
- **Traceroute:** Use traceroute to verify the routing path between devices in different VLANs.
- **Network monitoring:** Use a network monitoring tool to monitor traffic flow and identify any issues with VLAN connectivity.

### Related Features and Considerations

- **VLAN trunks:** VLAN trunks allow multiple VLANs to be carried over a single physical link. Configure trunks between switches to extend VLANs across the network.
- **VLAN sub-interfaces:** VLAN sub-interfaces allow you to assign multiple VLANs to a single physical interface, providing greater flexibility and control over network segmentation.
- **Security considerations:** VLANs can improve network security by isolating traffic and preventing unauthorized access to specific segments. However, it's important to implement additional security measures such as firewalls and access control lists.

### MikroTik REST API Example

**Endpoint:** `/api/interface/vlan`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "v": "7.1",
  "id": ".id",
  "find": {
    "interface": ".id"
  }
}
```

**Expected Response:**

```json
[
  {
    ".id": "VLAN1",
    "interface": "ether1",
    "vlan-id": "10",
    "name": "Marketing-VLAN"
  }
]
```