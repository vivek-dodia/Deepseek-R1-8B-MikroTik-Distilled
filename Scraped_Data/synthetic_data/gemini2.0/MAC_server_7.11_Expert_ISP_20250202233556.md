## MAC Server Configuration in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

- Configure a MAC server on a MikroTik RouterOS 7.11 device.
- The MAC server will provide MAC address to IP address resolution for clients on the network.
- The MAC server will store MAC address and IP address mappings in a database.

### Step-by-Step Implementation

**1. Create a MAC Server**

- Navigate to IP > MAC Server in WinBox.
- Click the "Plus" button to create a new MAC server.
- Configure the following settings:
  - Name: Enter a name for the MAC server.
  - Comment: Optional description for the MAC server.
  - Timeout: Time in seconds after which MAC-IP binding will expire (default: 300).

**2. Define MAC-IP Mappings**

- Click on the "Bindings" tab.
- Click the "Plus" button to add a new MAC-IP binding.
- Configure the following settings:
  - MAC Address: MAC address of the client.
  - IP Address: IP address to be assigned to the client.
  - Comment: Optional description for the binding.

**3. Enable MAC Server**

- Click on the "General" tab.
- Ensure that the "Enable" checkbox is ticked.

**4. Apply Configuration**

- Click "Apply" to save the configuration changes.

### Complete Configuration Commands

```
/ip mac-server
add name=my-mac-server
/ip mac-server binding
add mac-address=aa:bb:cc:dd:ee:ff ip-address=192.168.1.10 comment="My Test Binding"
/ip mac-server set my-mac-server enabled=yes
```

### Common Pitfalls and Solutions

- **MAC-IP bindings not working:** Ensure that the MAC server is enabled and that the correct MAC-IP mappings are defined.
- **Clients not receiving IP addresses:** Check if the MAC address of the client is registered in the MAC server database.
- **MAC server database corruption:** If the MAC server database becomes corrupted, you can recreate it using the "/ip mac-server flush" command.

### Verification and Testing Steps

- Use the "/ip mac-server print" command to display the MAC server configuration.
- Use the "/ip mac-server binding print" command to display the MAC-IP bindings.
- Test the MAC server by connecting a client to the network and verifying that it receives an IP address.

### Related Features and Considerations

- **IP Pools:** MAC servers can be used in conjunction with IP pools to automatically assign IP addresses to clients.
- **RADIUS:** MAC servers can be used with RADIUS authentication to restrict access to the network based on MAC addresses.

### MikroTik REST API Examples

- **Get MAC server configuration:**
  - API Endpoint: `/ip/mac-server/{id}`
  - Request Method: GET
  - Example Request: `curl -X GET http://192.168.1.1/api/ip/mac-server/1`
  - Expected Response:
  ```json
  {
    "id": 1,
    "name": "my-mac-server",
    "comment": "",
    "enabled": true,
    "timeout": 300
  }
  ```

- **Add MAC-IP binding:**
  - API Endpoint: `/ip/mac-server/{id}/binding`
  - Request Method: POST
  - Example Request:
  ```
  curl -X POST -H "Content-Type: application/json" \
  -d '{"mac-address": "aa:bb:cc:dd:ee:ff", "ip-address": "192.168.1.10", "comment": "My Test Binding"}' \
  http://192.168.1.1/api/ip/mac-server/1/binding
  ```
  - Expected Response:
  ```json
  {
    "id": 1,
    "mac-address": "aa:bb:cc:dd:ee:ff",
    "ip-address": "192.168.1.10",
    "comment": "My Test Binding"
  }
  ```