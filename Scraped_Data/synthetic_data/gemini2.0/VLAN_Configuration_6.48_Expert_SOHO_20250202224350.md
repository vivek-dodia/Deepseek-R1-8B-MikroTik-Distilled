## VLAN Configuration in RouterOS 6.48 (Expert)

### Configuration Scenario and Requirements

* Create VLANs to segment the network for security and traffic isolation.
* Assign VLANs to switch ports to restrict access to specific networks.
* Configure inter-VLAN routing to allow communication between VLANs.

### Step-by-Step Implementation

**1. Create VLAN Interface:**

```
/interface vlan add name=vlan10 id=10
/interface vlan add name=vlan20 id=20
```

**2. Assign VLANs to Switch Ports:**

```
/interface switch port set ether1 mode=access vlan-id=10
/interface switch port set ether2 mode=access vlan-id=20
```

**3. Configure Inter-VLAN Routing:**

```
/ip route add dst-address=10.10.10.0/24 gateway=10.10.10.254 table=vlan10
/ip route add dst-address=10.10.20.0/24 gateway=10.10.20.254 table=vlan20
/ip firewall filter add action=accept chain=input-vlan10 in-interface=vlan10 dst-address=10.10.20.0/24
/ip firewall filter add action=accept chain=input-vlan20 in-interface=vlan20 dst-address=10.10.10.0/24
```

**4. Add Default Route (Optional):**

```
/ip route add default-route-distance=1 gateway=10.10.10.1
```

### Complete Configuration Commands

```
/interface vlan add name=vlan10 id=10
/interface vlan add name=vlan20 id=20
/interface switch port set ether1 mode=access vlan-id=10
/interface switch port set ether2 mode=access vlan-id=20
/ip route add dst-address=10.10.10.0/24 gateway=10.10.10.254 table=vlan10
/ip route add dst-address=10.10.20.0/24 gateway=10.10.20.254 table=vlan20
/ip firewall filter add action=accept chain=input-vlan10 in-interface=vlan10 dst-address=10.10.20.0/24
/ip firewall filter add action=accept chain=input-vlan20 in-interface=vlan20 dst-address=10.10.10.0/24
/ip route add default-route-distance=1 gateway=10.10.10.1
```

### Common Pitfalls and Solutions

* **VLAN ID collision:** Make sure VLAN IDs are unique across all switches.
* **Incorrect tagging:** Ensure that devices connected to VLAN ports are configured for the appropriate VLAN tag.
* **Firewall rules:** Remember to add firewall rules to allow traffic between VLANs.
* **Default route:** Add a default route on the VLAN interface that should have access to the internet or other networks.

### Verification and Testing Steps

* Check the switch port configuration with `/interface switch port print`.
* Confirm VLAN interface status with `/interface vlan print`.
* Ping between devices on different VLANs.
* Test internet connectivity from VLAN devices.

### Related Features and Considerations

* **Bridge VLAN:** Allows VLANs to span multiple physical interfaces.
* **DHCP filtering:** Restrict DHCP requests to specific VLANs.
* **Smart VLAN:** Automatically configure VLANs based on device MAC addresses.
* **Security:** Implement VLAN segmentation for enhanced security and network isolation.

### MikroTik REST API Examples

**API Endpoint:** `/interface/vlan`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "vlan30",
  "id": 30
}
```

**Expected Response:**

```json
{
  "id": "5f85f01846e477b0"
}
```

**Note:** This example creates a VLAN interface with the name "vlan30" and ID "30".