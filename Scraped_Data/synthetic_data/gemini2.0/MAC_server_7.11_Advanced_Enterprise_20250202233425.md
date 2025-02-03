## MAC Server

### Configuration Scenario and Requirements

The MAC server feature allows a MikroTik RouterOS device to act as a central repository for MAC addresses and their corresponding IP addresses. This is useful for tracking the location of devices on a network, managing DHCP assignments, and enforcing security policies.

### Step-by-Step Implementation

1. **Create a MAC server.** Navigate to `/ip mac-server` in the RouterOS configuration menu. Click the "+" button to add a new MAC server. Specify a name and select the interface on which the MAC server should listen for MAC address updates.
2. **Configure MAC address entries.** Add MAC addresses and their corresponding IP addresses to the MAC server. Click the "+" button to add a new entry. Specify the MAC address, IP address, and optionally a description.
3. **Enable DHCP lease binding.** To automatically update the MAC server database when devices lease IP addresses via DHCP, enable the "DHCP Lease Binding" option on the MAC server configuration page.

### Complete Configuration Commands

```
/ip mac-server add name=main interface=ether1
/ip mac-server add server=main mac-address=00:11:22:33:44:55 ip-address=192.168.1.100 description="Server A"
/ip dhcp-server set lease-binding=yes
```

### Common Pitfalls and Solutions

- **Duplicate MAC addresses:** If multiple devices have the same MAC address, the MAC server may not be able to correctly track their locations.
- **Incorrect interface selection:** Ensure that the MAC server is listening on the correct interface, or devices on other interfaces will not be tracked.

### Verification and Testing Steps

1. **Check the MAC server database.** Navigate to `/ip mac-server print` to view the list of MAC addresses and their corresponding IP addresses.
2. **Test DHCP lease binding.** Assign an IP address to a device via DHCP. The MAC address and IP address of the device should be added to the MAC server database.

### Related Features and Considerations

- **DHCP server:** Integrate the MAC server with the DHCP server to automatically update MAC address entries when devices lease IP addresses.
- **Firewall:** Use the MAC server to filter traffic based on MAC addresses.
- **RoMON:** Monitor the MAC server status and statistics using RoMON.

### MikroTik REST API Examples

#### Get MAC Server List

- API Endpoint: `/rest/ip/mac-server`
- Request Method: GET
- Example JSON Payload:
```
{
  "filter": {"name": "main"}
}
```
- Expected Response:
```
[
  {
    "name": "main",
    "interface": "ether1",
    "dhcp-lease-binding": true
  }
]
```

#### Add MAC Server Entry

- API Endpoint: `/rest/ip/mac-server`
- Request Method: POST
- Example JSON Payload:
```
{
  "server": "main",
  "mac-address": "00:11:22:33:44:55",
  "ip-address": "192.168.1.100",
  "description": "Server A"
}
```
- Expected Response:
```
{
  "message": "ok"
}
```