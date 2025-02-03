## MAC Server

### Configuration Scenario and Requirements

In a small office or home network (SOHO), you want to configure a MAC server on a MikroTik RouterOS device to authenticate and authorize devices connecting to the network.

### Step-by-Step Implementation

**1. Create a MAC Server Profile**

- Navigate to **IP > MAC Server** in WinBox or issue the following command in the CLI:

```
/ip mac-server profile
add name=mac-profile
```

**2. Configure MAC Address Authentication**

- In the "MAC Server Profile" window/command, click/type "Add" to create a new MAC address entry:

```
/ip mac-server mac
add mac-address=01:02:03:04:05:06 profile=mac-profile
```

**3. Enable MAC Server**

- Navigate to **IP > MAC Server > Settings** in WinBox or issue the following command in the CLI:

```
/ip mac-server settings
set enabled=yes
```

### Complete Configuration Commands

```
/ip mac-server profile add name=mac-profile
/ip mac-server mac add mac-address=01:02:03:04:05:06 profile=mac-profile
/ip mac-server settings set enabled=yes
```

### Common Pitfalls and Solutions

**Pitfall:** MAC server is not authenticating devices.

**Solution:** Ensure that the correct MAC profile is assigned to the interface accepting incoming connections.

**Pitfall:** Devices are bypassing MAC server authentication.

**Solution:** Check firewall rules to ensure there are no exceptions or bypass rules.

### Verification and Testing Steps

**1. Test Authentication**

- Connect a device to the network with an unauthenticated MAC address.
- Observe that the device is denied internet access.

**2. Test Authorization**

- Change the MAC address of the device to one that is authenticated in the MAC server profile.
- Observe that the device is now granted internet access.

### Related Features and Considerations

**DHCP Server:** MAC server can be integrated with the DHCP server to automatically authenticate and authorize devices that obtain IP addresses via DHCP.

**RADIUS Server:** MAC server can authenticate and authorize devices using a RADIUS server for centralized user management.

### MikroTik REST API Examples

**Get MAC Server Profile**

```
GET /rest/ip/mac-server/profile/
```

**Response:**

```json
[
  {
    "name": "mac-profile",
    "type": "static"
  }
]
```

**Create MAC Address Entry**

```
POST /rest/ip/mac-server/mac
{
  "mac-address": "01:02:03:04:05:06",
  "profile": "mac-profile"
}
```

**Response:**

```json
{
  "mac-address": "01:02:03:04:05:06",
  "profile": "mac-profile",
  "interface": "ether1"
}
```

**Enable MAC Server**

```
PUT /rest/ip/mac-server/settings
{
  "enabled": true
}
```