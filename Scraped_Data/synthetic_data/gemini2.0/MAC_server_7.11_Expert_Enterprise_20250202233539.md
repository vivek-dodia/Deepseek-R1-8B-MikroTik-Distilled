## MAC Server Configuration in RouterOS 7.11

### Configuration Scenario and Requirements

#### **Objective:**
To configure a MAC server that authenticates and authorizes network clients based on their MAC addresses.

#### **Requirements:**
- MikroTik router running RouterOS 7.11
- MAC addresses of clients that need to be authenticated

### Step-by-Step Implementation

#### 1. Create MAC Server
- Navigate to the MAC Server menu.
- Click on the "+" icon to create a new MAC server.
- Enter a name for the server.

#### 2. Define Auth Mode
- Select the authentication mode:
  - **Disabled:** No authentication.
  - **Accept:** Automatically authenticate any MAC address.
  - **Reject:** Automatically reject any MAC address.
  - **MAC list:** Authenticate only MAC addresses defined in the list.
  - **Radius:** Authenticate clients using RADIUS.

#### 3. MAC List Configuration (for MAC list auth mode)
- Add the MAC addresses that need to be authenticated to the list.
- Click on the "+" icon to add an address.
- Enter the MAC address and a comment (optional).

#### 4. Enable Radius Configuration (for Radius auth mode)
- Click on the "Radius" tab.
- Select the Radius server to use.
- Enter the shared secret for authentication.
- Configure other RADIUS parameters as needed.

#### 5. Apply Settings
- Click on the "Apply" button to save the configuration.

### Complete Configuration Commands

```
/mac-server set name=my-mac-server auth-mode=accept
/mac-server set name=my-mac-server auth-mode=mac-list
/mac-server set name=my-mac-server auth-mode=radius radius-server=radius-server.example.com secret=my-shared-secret
/mac-server set name=my-mac-server mac-list add mac-address=00:11:22:33:44:55
```

### Common Pitfalls and Solutions

#### 1. Wrong MAC Address
- Ensure that the MAC addresses added to the list are correct.
- Use a tool like Wireshark to capture and verify the client MAC address.

#### 2. Incorrect Radius Configuration
- Check that the Radius server is configured properly and the shared secret is correct.
- Use the "Test" button in the Radius configuration to verify connectivity.

### Verification and Testing Steps

#### 1. Connect Client
- Connect a client to the network.
- Verify that the client receives an IP address if authorized.

#### 2. Disconnect Unauthorized Client
- Disconnect a client that is not authorized.
- Verify that the client is unable to receive an IP address or is disconnected.

### Related Features and Considerations

#### **Firewall:**
- Create firewall rules to control traffic based on MAC addresses.

#### **DHCP:**
- Configure the DHCP server to assign IP addresses based on MAC server authentication.

#### **Monitor:**
- Use the "Monitor" tab in the MAC Server menu to view authentication events.

## REST API Examples

### Get MAC Server Configuration

```
GET /api/mac-server/
```

**Response:**

```
[
  {
    "name": "my-mac-server",
    "auth-mode": "accept"
  }
]
```

### Add MAC Address to MAC List

```
POST /api/mac-server/:id/mac-list
```

**Request Body:**

```
{
  "mac-address": "00:11:22:33:44:55"
}
```

**Response:**

```
{
  "id": 1,
  "mac-address": "00:11:22:33:44:55"
}
```