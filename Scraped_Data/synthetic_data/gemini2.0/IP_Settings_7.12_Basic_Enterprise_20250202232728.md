## IP Settings

### Configuration Scenario and Requirements

Configure IP settings for an interface on a MikroTik RouterOS device.

### Step-by-Step Implementation

1. Open WinBox and establish a connection to the MikroTik RouterOS device.
2. Navigate to the **IP** > **IP Settings** menu.
3. Click on the **+** button to add a new IP address.
4. In the **Interface** field, select the interface to which the IP address should be assigned.
5. In the **Address** field, enter the desired IP address. This can be either an IPv4 or IPv6 address.
6. In the **Network** field, enter the subnet mask for the IP address.
7. In the **Gateway** field, enter the default gateway for the interface.
8. Click on the **Apply** button to save the changes.

### Complete Configuration Commands

```text
/ip address add address=192.168.1.10/24 interface=ether1
/ip address add address=2001:db8::1/64 interface=ether1
```

### Common Pitfalls and Solutions

- **If the IP address is not reachable**, check the following:
  - Make sure the IP address is in the same subnet as the default gateway.
  - Make sure the default gateway is reachable.
- **If the network is still not working**, check the following:
  - Ensure the physical connection between the MikroTik device and the network is secure.
  - Verify that the firewall is not blocking traffic.

### Verification and Testing Steps

1. Ping the IP address of the interface to verify it is reachable.
2. Browse the Internet to verify that the device has access to the network.

### Related Features and Considerations

- You can also configure static routes, DHCP settings, and DNS settings in the **IP** menu.
- You can use the **IP** > **ARP** menu to view and manage the ARP table.

### MikroTik REST API Examples

```text
**API Endpoint:** /ip/address
**Request Method:** POST
**Example JSON Payload:**

```json
{
  "address": "192.168.1.10/24",
  "interface": "ether1"
}
```

**Expected Response:**

```json
{
  "data": [
    {
      "address": "192.168.1.10/24",
      "interface": "ether1",
      "disabled": false,
      "comment": ""
    }
  ]
}
```