**Topic: MAC Server**

**Configuration Level: Advanced**

**Network Scale: SMB**

**RouterOS Version: 6.48 (6.x or 7.x)**

**1. Configuration Scenario and Requirements**

A MAC server is a device that provides dynamic IP address assignment based on the MAC address of a connected device. This is useful in scenarios where a large number of devices need to be assigned IP addresses, such as in a public hotspot or a corporate network.

For this configuration, we will set up a MAC server on a MikroTik router and assign IP addresses from a specific IP pool.

**2. Step-by-Step Implementation**

**2.1. Create an IP Pool**

- Navigate to **IP > Pool**
- Click on the **+** button
- Enter a name for the pool, e.g., "DHCP-Pool"
- Set the **Ranges** to the desired IP range, e.g., "192.168.1.0/24"
- Click **Apply**

**2.2. Enable MAC Server**

- Navigate to **IP > DHCP Server**
- Select the **DHCP Server** tab
- Click on the **+** button
- Enter a name for the server, e.g., "DHCP-Server"
- Select the **Interface** where the MAC server will be active, e.g., "ether1"
- Set **MAC Address** to **yes**
- Select the **IP Pool** created in step 2.1, e.g., "DHCP-Pool"
- Click **Apply**

**2.3. Configure MAC Address Binding**

- Navigate to **IP > DHCP Server > Leases**
- Click on the **+** button
- Enter the **MAC Address** of the device that will receive the IP address
- Enter the **IP Address** that should be assigned to the device
- Click **Apply**

**3. Complete Configuration Commands**

```
/ip pool add name=DHCP-Pool ranges=192.168.1.0/24
/ip dhcp-server add name=DHCP-Server interface=ether1 mac-address=yes address-pool=DHCP-Pool
/ip dhcp-server lease add mac-address=00:11:22:33:44:55 ip-address=192.168.1.10
```

**4. Common Pitfalls and Solutions**

- **Incorrect IP Pool Range:** Ensure that the IP pool range does not overlap with any existing networks.
- **Interface Misconfiguration:** Make sure the DHCP server is configured on the correct interface.
- **Duplicate MAC Address Bindings:** Avoid assigning the same IP address to multiple devices.

**5. Verification and Testing Steps**

- Use **tools > ping** to ping the IP addresses assigned by the MAC server.
- Check the **IP > DHCP Server > Leases** tab to verify that the desired devices have been assigned IP addresses.

**6. Related Features and Considerations**

- **Static vs. Dynamic MAC Binding:** Static bindings assign specific IP addresses to MAC addresses, while dynamic bindings assign addresses from the pool based on availability.
- **MAC Address Filtering:** The MAC server can be used to filter out or allow access to specific MAC addresses.
- **Security Considerations:** Ensure the DHCP server is protected from unauthorized access and that the IP pool is of sufficient size to support the expected number of devices.

**7. MikroTik REST API Examples**

**Endpoint:** `/ip/pool`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "action": "getall"
}
```

**Expected Response:**

```json
[
  {
    ".id": ".id",
    "name": "DHCP-Pool",
    "ranges": [
      "192.168.1.0/24"
    ]
  }
]
```

**Endpoint:** `/ip/dhcp-server`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "action": "add",
  "name": "DHCP-Server",
  "interface": "ether1",
  "mac-address": "yes",
  "address-pool": ".id"
}
```

**Expected Response:**

```json
{
  ".id": ".id",
  "name": "DHCP-Server",
  "interface": "ether1",
  "mac-address": "yes",
  "address-pool": ".id"
}
```