## MAC Server

### Configuration Scenario and Requirements

In this scenario, we need to configure a MikroTik router as a MAC server to authenticate and authorize network devices based on their MAC addresses.

### Step-by-Step Implementation

**1. Enable MAC Server**

- Go to `/ip mac-server` in WinBox or the command line.
- Click the "Enable" checkbox.

**2. Create MAC Pool**

- Click on the "Pools" tab.
- Click the "+" button to create a new MAC pool.
- Enter a name for the pool (e.g., "AllowedDevices").
- Click "Apply" to save the pool.

**3. Add MAC Addresses**

- Click on the "MACs" tab.
- Click the "+" button to add a new MAC address.
- Enter the MAC address (e.g., "00:11:22:33:44:55").
- Select the MAC pool created earlier (e.g., "AllowedDevices").
- Click "Apply" to save the MAC address.

**4. Apply MAC Filtering**

- Go to `/interface ethernet` in WinBox or the command line.
- Select the interface you want to apply MAC filtering to.
- Click on the "MAC Filters" tab.
- Click the "+" button to create a new MAC filter rule.
- Select the MAC server (e.g., "local") from the dropdown.
- Select the MAC pool created earlier (e.g., "AllowedDevices") from the dropdown.
- Click "Apply" to save the MAC filter rule.

### Complete Configuration Commands

```
/ip mac-server enable
/ip mac-server pool add name=AllowedDevices
/ip mac-server mac add mac=00:11:22:33:44:55 pool=AllowedDevices
/interface ethernet set [interface-name] mac-filter=yes mac-server=local mac-filter-policy=drop action=deny
```

### Common Pitfalls and Solutions

- Ensure that the MAC server is enabled.
- Verify that the MAC addresses are added to the correct MAC pool.
- Check that the MAC filter rule is applied to the desired interface.
- If devices are still failing to connect, check the security logs for errors related to MAC filtering.

### Verification and Testing Steps

- Try to connect a device with an authorized MAC address to the network.
- Verify that the device is able to connect and access the network resources.
- Try to connect a device with an unauthorized MAC address to the network.
- Confirm that the device is blocked from accessing the network resources.

### Related Features and Considerations

- **Policy-based MAC filtering:** MAC filtering rules can be configured to apply different actions based on the MAC pool or other criteria.
- **MAC authentication bypass:** Certain devices may need to bypass MAC filtering, such as IP phones or VoIP gateways. This can be configured by creating an exception rule in the MAC server.
- **Compliance:** MAC filtering can help organizations comply with security regulations that require network access control.

### MikroTik REST API Examples

**Get MAC Server Configuration**

```
GET /ip/mac-server/print
```

**Response:**

```json
{
  "enabled": true,
  "hash": 1756510608
}
```

**Add MAC Address to MAC Pool**

```
POST /ip/mac-server/mac/add
{
  "mac": "00:11:22:33:44:55",
  "pool": "AllowedDevices"
}
```

**Response:**

```json
{
  "hash": 652521686
}
```