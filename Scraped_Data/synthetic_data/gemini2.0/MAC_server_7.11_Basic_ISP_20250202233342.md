## MAC Server

### Configuration Scenario and Requirements

* Configure a MAC server on a MikroTik RouterOS device to manage MAC addresses of connected devices on the network.
* The MAC server will be used to assign IP addresses to devices based on their MAC addresses.

### Step-by-Step Implementation

1. **Create a MAC Server:**
   - Navigate to **IP > MAC Server** and click on the **+** button.
   - Enter a **Name** for the MAC server and click **OK**.

2. **Configure MAC Server Settings:**
   - In the **General** tab, select the **Enabled** checkbox.
   - Set the **Mode** to **Standard**.
   - Under **DHCP Lease Time**, set the lease time for DHCP-assigned IP addresses.
   - In the **Ranges** tab, add IP address ranges to be assigned to devices based on their MAC addresses. To add a range, click on the **+** button and specify the **Address** and **Comment**.

3. **Add MAC Addresses:**
   - Navigate to **IP > MAC Server** and click on the **MAC** tab of the previously created MAC server.
   - Click on the **+** button to add a MAC address.
   - Enter the **MAC Address** and specify the **Action** (e.g., Add, Drop).

### Complete Configuration Commands

```
/ip mac-server set mac-server0 enabled=yes mode=standard
/ip mac-server set mac-server0 dhcp-lease-time=86400s
/ip mac-server add mac-server=mac-server0 address=192.168.1.1-192.168.1.100 comment="VLAN1 devices"
/ip mac-server add mac-server=mac-server0 mac-address=00:00:00:00:00:01 action=add
```

### Common Pitfalls and Solutions

* **IP address range conflict:** Ensure that the IP address ranges assigned by the MAC server do not overlap with other existing ranges on the network.
* **Duplicate MAC addresses:** MAC addresses should be unique. If a duplicate MAC address is detected, the device may not receive an IP address.

### Verification and Testing Steps

1. Connect devices with registered MAC addresses to the network.
2. Use a tool like Wireshark or tcpdump to verify that devices are receiving IP addresses from the MAC server.
3. Check the **Clients** tab in **IP > MAC Server** to see the list of connected devices and their MAC addresses.

### Related Features and Considerations

* **IP Pool:** MAC server can be used in conjunction with IP pools to dynamically assign IP addresses from a pool of available addresses.
* **DHCP Server:** MAC server can be integrated with a DHCP server to provide IP addressing and MAC address management.
* **Security:** MAC addresses can be used for basic network access control, but it's not a foolproof security measure. Consider using additional security measures such as firewalls and intrusion detection systems.

### MikroTik REST API Examples

**API Endpoint:** `/api/ip/mac-server/add`

**Request Method:** POST

**Request JSON Payload:**

```json
{
  "mac-address": "00:00:00:00:00:01",
  "mac-server": "mac-server0",
  "action": "add"
}
```

**Expected Response:**

```json
{
  "error": null,
  "message": null
}
```