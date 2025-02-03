**Topic: MAC Server**

**1. Configuration Scenario and Requirements**

- Create a MAC server on a MikroTik router to manage MAC addresses and associate them with specific IP addresses.
- The MAC server will be used to allow or deny access to the network based on MAC addresses.
- Network size: Enterprise

**2. Step-by-Step Implementation**

**2.1. Enable MAC Server**

- Go to **IP** > **MAC Server** in the WinBox GUI.
- Click the **+** button to create a new MAC server.
- Set **Name** to "MyMACServer."
- Leave other settings to default and click **OK**.

**2.2. Add MAC-IP Mappings**

- Click the **+** button under **MAC** to add a new MAC-IP mapping.
- Enter the MAC address of the desired device in the **MAC Address** field.
- Enter the corresponding IP address in the **IP Address** field.
- Click **OK**.

**3. Complete Configuration Commands**

```
/ip mac-server server add name="MyMACServer"
/ip mac-server mac add mac-address=<MAC_ADDRESS> ip-address=<IP_ADDRESS>
```

**4. Common Pitfalls and Solutions**

- **MAC address not found:** Verify that the MAC address is correct and entered without spaces or colons.
- **IP address already in use:** Check if the IP address assigned to the MAC is not already being used by another device.
- **MAC server not active:** Ensure that the MAC server is enabled and the **Status** field shows "enabled."

**5. Verification and Testing Steps**

- Ping the IP address associated with a MAC address in the MAC server.
- If the ping is successful, the MAC-IP mapping is working correctly.
- Try to access a network resource (e.g., website) from a device with a MAC address not in the MAC server. Access should be denied.

**6. Related Features and Considerations**

- **Security:** Use the MAC server to restrict access to specific devices and prevent unauthorized connections.
- **Management:** Centralize MAC address management and easily add or remove MAC-IP mappings.
- **Automation:** Use scripts or the REST API to automate MAC server configuration and mapping updates.

**7. MikroTik REST API Examples**

**7.1. Get MAC Server List**

**API Endpoint:** `/ip/mac-server`

**Request Method:** GET

**Response:**

```json
[
  {
    ".id": "1",
    "enabled": true,
    "name": "MyMACServer"
  }
]
```

**7.2. Add MAC-IP Mapping**

**API Endpoint:** `/ip/mac-server/mac`

**Request Method:** POST

**Request Payload:**

```json
{
  "mac-address": "00:11:22:33:44:55",
  "ip-address": "192.168.1.10"
}
```

**Response:**

```json
{
  ".id": "1",
  "mac-address": "00:11:22:33:44:55",
  "ip-address": "192.168.1.10"
}
```