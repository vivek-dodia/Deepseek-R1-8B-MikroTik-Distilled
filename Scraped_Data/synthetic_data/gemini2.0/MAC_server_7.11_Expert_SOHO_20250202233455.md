---

## MAC Server in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

* Configure a MikroTik RouterOS device as a MAC server to associate MAC addresses with IP addresses.
* Use IP Pool to assign IP addresses to MAC addresses.
* Allow only specific MAC addresses to access the network.

### Step-by-Step Implementation

**1. Create an IP Pool**

```
/ip pool
add name=mac-pool ranges=192.168.1.10-192.168.1.99
```

**2. Create a MAC Server**

```
/ip mac-server
add name=mac-server
```

**3. Assign the IP Pool to the MAC Server**

```
/ip mac-server
set mac-server=mac-server ip-pool=mac-pool
```

**4. Add MAC Addresses to the MAC Server**

```
/ip mac-server
add mac-address=00:11:22:33:44:55 static=yes
```

**5. Allow Only Authorized MAC Addresses**

```
/ip firewall
add chain=input action=reject src-mac=!allow-mac
```

### Complete Configuration Commands

```
/ip pool
add name=mac-pool ranges=192.168.1.10-192.168.1.99
/ip mac-server
add name=mac-server
/ip mac-server
set mac-server=mac-server ip-pool=mac-pool
/ip mac-server
add mac-address=00:11:22:33:44:55 static=yes
/ip firewall
add chain=input action=reject src-mac=!allow-mac
```

### Common Pitfalls and Solutions

* **MAC addresses mismatch:** Ensure that the MAC address specified in the configuration matches the actual device's MAC address.
* **IP Pool exhaustion:** Monitor the IP pool usage to avoid running out of available IP addresses.
* **Firewall rules:** Make sure to create firewall rules to allow only authorized MAC addresses to access the network.

### Verification and Testing Steps

1. Connect a device with an authorized MAC address to the network.
2. Assign a static IP address from the MAC server pool to the device.
3. Test internet connectivity or access to internal resources.
4. Verify that devices with unauthorized MAC addresses are blocked by the firewall.

### Related Features and Considerations

* **PPPoE and MAC Server:** If using PPPoE, associate MAC addresses with PPPoE users to grant network access.
* **Bridging and MAC Server:** Configure MAC server on a bridge to associate MAC addresses with specific ports or devices.
* **VLAN and MAC Server:** Create separate MAC servers for different VLANs to segment and control MAC access.

### MikroTik REST API Examples

**API Endpoint:** `/api/ip/mac-server`

**Request Method:** `GET`

**Example JSON Payload:**

```json
{
  "ids": {
    "id": 1
  }
}
```

**Expected Response:**

```json
{
  "id": 1,
  "name": "mac-server",
  "enabled": true,
  "lease-duration": 0,
  "shared-secret": null,
  "comment": null,
  "ip-pool": "pool-name",
  "mac-address": [
    {
      "mac-address": "00:11:22:33:44:55",
      "address": "192.168.1.10",
      "status": "active",
      "last-seen": "2023-03-07T16:30:55Z",
      "comment": "allowed-device",
      "connected-device": {
        "id": 2,
        "name": "my-device"
      }
    }
  ]
}
```