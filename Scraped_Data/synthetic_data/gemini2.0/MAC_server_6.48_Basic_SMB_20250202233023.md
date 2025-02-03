**Configuration Scenario and Requirements**

- Configure a MAC server on a MikroTik RouterOS 6.48 device to manage MAC addresses and provide access control for devices on the network.

**Step-by-Step Implementation**

**1. Enable MAC Server**

- Go to **IP > MAC Server**
- Click the **Enable** checkbox
- Click **Apply**

**2. Add a MAC Address**

- Click **Add New**
- Enter the **MAC Address**
- Enter a **Description** (optional)
- Select the **Access Mode** (allow, restrict, or remove)
- Click **Apply**

**3. Configure Default Action**

- Go to **IP > MAC Server** tab
- In the **Default Action** field, select the desired action for devices with MAC addresses not found in the MAC server database.
- Click **Apply**

**Complete Configuration Commands**

```
/ip mac-server enable
/ip mac-server add address=<mac-address> description=<description> added-by=api access-mode=<mode>
/ip mac-server set default-action=<action>
```

**Common Pitfalls and Solutions**

- **Incorrectly formatted MAC address:** Ensure the MAC address is in the correct format, e.g., "AA:BB:CC:DD:EE:FF".
- **Duplicate MAC addresses:** Do not add the same MAC address multiple times with different access modes.
- **Mismatched access modes:** Ensure the access mode matches the intended behavior for the device.

**Verification and Testing Steps**

- Check the **IP > MAC Server** tab to view the configured MAC addresses and their access modes.
- Connect a device with a MAC address that is not in the MAC server database and observe the applied action.

**Related Features and Considerations**

- **ARP Tables:** The MAC server interacts with ARP tables to associate MAC addresses with IP addresses.
- **IP Binding:** The MAC server can be used in conjunction with IP binding to further restrict access based on both MAC and IP addresses.
- **DHCP Server:** The MAC server can be used to integrate with DHCP to automatically discover and manage MAC addresses on the network.

**MikroTik REST API Examples**

**Endpoint:** `/api/ip/mac-server`

**Request Method:** GET

**Example JSON Payload:**

```
{
  "default-action": "accept"
}
```

**Expected Response:**

```
[
  {
    "address": "00:00:00:00:00:00",
    "description": "",
    "added-by": "none",
    "access-mode": "accept"
  }
]
```