## MAC Server

The MAC server feature in MikroTik RouterOS allows you to manage and control MAC addresses on your network. It provides capabilities for address learning, assignment, and filtering, enabling you to enforce network access policies and enhance security.

### Configuration Scenario and Requirements

* Establish a MikroTik router with RouterOS 6.48 or higher.
* Configure IP addressing and routing on the router.
* Identify the interfaces or VLANs on which MAC address management is required.

### Step-by-Step Implementation

**1. Enable MAC Server:**

```
/interface mac-server enable
```

**2. Create a MAC Server:**

```
/interface mac-server server add interface=<interface-name>
```

**3. Define MAC Address Learning:**

```
/interface mac-server server=<server-name> learning=yes
```

**4. Add MAC Address Mappings (Optional):**

```
/interface mac-server server=<server-name> mac-address=<mac-address> interface=<interface-name>
```

**5. Configure MAC Address Filtering (Optional):**

```
/interface mac-server server=<server-name>        filter=yes
/interface mac-server server=<server-name>        filter-action=accept
/interface mac-server server=<server-name>        filter-mode=allow
/interface mac-server server=<server-name>        filter-mac-list=<mac-list-name>
```

**6. Save Configuration:**

```
/system backup save
```

### Complete Configuration Commands

```
/interface mac-server enable
/interface mac-server server add interface=ether1
/interface mac-server server=ether1 learning=yes
/interface mac-server server=ether1 mac-address=00:11:22:33:44:55 interface=ether2
/interface mac-server server=ether1 filter=yes
/interface mac-server server=ether1 filter-action=accept
/interface mac-server server=ether1 filter-mode=allow
/interface mac-server server=ether1 filter-mac-list=allowed-macs
/system backup save
```

### Common Pitfalls and Solutions

* **Empty MAC Address Mapping:** If a MAC address is not added to the MAC server, it will not be learned or filtered.
* **Duplicate MAC Addresses:** Avoid assigning the same MAC address to multiple devices, as it can lead to conflicts and unpredictable behavior.
* **Incorrect Interface Selection:** Ensure that the MAC server is configured on the correct interface or VLAN where MAC management is required.

### Verification and Testing Steps

* **Check MAC Address Table:** Use the command `/interface mac-server server print` to view the MAC address table and confirm if the desired MAC addresses are learned and mapped correctly.
* **Test MAC Address Filtering:** Connect a device with a specific MAC address to the network and observe if the device can access the network based on the configured filter settings.

### Related Features and Considerations

* **DHCP Server:** The MAC server can be integrated with the DHCP server to automatically assign IP addresses to devices based on their MAC addresses.
* **Firewall:** MAC address filtering can be used in conjunction with the firewall to create access control lists and deny access to unauthorized devices.
* **Wireless Management:** MAC address filtering can be applied to wireless interfaces to control device access to the wireless network.

### MikroTik REST API Examples

**Get MAC Address Table:**

**Endpoint:** `/interface/mac-server/print`
**Request Method:** GET
**Example JSON Payload:**
```json
{}
```
**Expected Response:**
```json
[
  {
    ".id": "0",
    "interface": "ether1",
    "learning": "yes",
    "mac-address": "00:11:22:33:44:55",
    "seen": "16:20:48"
  }
]
```

**Add MAC Address Mapping:**

**Endpoint:** `/interface/mac-server/add`
**Request Method:** POST
**Example JSON Payload:**
```json
{
  "interface": "ether1",
  "mac-address": "00:11:22:33:44:55"
}
```
**Expected Response:**
```json
{
  ".id": "1",
  "interface": "ether1",
  "mac-address": "00:11:22:33:44:55",
  "added": true
}
```