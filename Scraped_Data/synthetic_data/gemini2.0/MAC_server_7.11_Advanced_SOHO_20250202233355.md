**Scenario:**

Configure a MAC server on a MikroTik RouterOS 7.11 device to manage and control MAC addresses on the network.

**Implementation:**

**1. Preparation:**

- Ensure that the MikroTik device has a valid IP address and is accessible on the network.
- Update the device to the latest version of RouterOS 7.11.

**2. Enabling the MAC Server:**

**WinBox:**
- Navigate to IP --> MAC Server.
- Click on the "+" button to add a new MAC Server instance.
- Enter a name for the MAC Server.
- Enable the MAC Server by checking the "Enable" checkbox.

**Command Line:**

```
/ip mac-server set enabled=yes
```

**3. Configuring IP Address Pool:**

**WinBox:**
- Navigate to IP --> IP Pools.
- Click on the "+" button to add a new IP Pool.
- Enter a name for the IP Pool.
- Configure the IP address range and subnet mask.
- Specify the MAC Server instance created in Step 2.

**Command Line:**

```
/ip pool add name=pool1 ranges=10.10.10.0/24 mac-server=mac_server1
```

**4. Configuring DHCP Server:**

**WinBox:**
- Navigate to IP --> DHCP Server.
- Click on the "+" button to add a new DHCP Server instance.
- Select the IP Pool created in Step 3.
- Enable the DHCP Server by checking the "Enable" checkbox.

**Command Line:**

```
/ip dhcp-server add interface=ether1 address-pool=pool1 enabled=yes
```

**5. Adding MAC Addresses:**

**WinBox:**
- Navigate to IP --> MAC Server --> MAC Addresses.
- Click on the "+" button to add a new MAC Address.
- Enter the MAC address and specify whether to allow or block it.

**Command Line:**

```
/ip mac-server mac-address add mac-address=00:11:22:33:44:55 allowed=yes
```

**Common Pitfalls and Solutions:**

- **DHCP Server not assigning IP addresses:** Ensure that the IP Pool is configured correctly and that the DHCP Server is enabled.
- **MAC addresses not being managed:** Verify that the MAC Server is enabled and that the IP Pool is assigned to the correct MAC Server instance.
- **Unauthorized devices accessing the network:** Add all authorized MAC addresses to the MAC Server and block all others.

**Verification and Testing:**

- Use the command `/ip dhcp-server print` to check if the DHCP Server is running and assigning IP addresses.
- Use the command `/ip mac-server mac-address print` to verify the added MAC addresses and their status.
- Connect a device with a known MAC address to the network and check if it receives an IP address and if it can access the network.

**Related Features and Considerations:**

- **RoMON:** Use RoMON to monitor the performance and statistics of the MAC Server.
- **Certificates:** Use certificates to secure the MAC Server communication.
- **RADIUS:** Integrate the MAC Server with a RADIUS server for centralized authentication and authorization.
- **User / User groups:** Assign MAC addresses to specific users or user groups to enhance security and control.

**REST API Examples:**

**Add a new MAC Server instance:**

**API Endpoint:** `/ip/mac-server/add`
**Request Method:** POST
**Example JSON Payload:**
```json
{
  "name": "mac-server1",
  "enabled": true
}
```

**Add a new MAC Address:**

**API Endpoint:** `/ip/mac-server/mac-address/add`
**Request Method:** POST
**Example JSON Payload:**
```json
{
  "mac-address": "00:11:22:33:44:55",
  "allowed": false
}
```

**Expected Response:**

A successful response will include the created objects' ID and details.