## MAC Server

### Configuration Scenario and Requirements

The MAC server allows you to manage MAC addresses on your network. You can use it to:

- Control access to your network
- Track device usage
- Identify and troubleshoot network issues

### Step-by-Step Implementation

**1. Enable MAC Server**

```
/interface mac-server server set enabled=yes
```

**2. Add MAC Address**

```
/interface mac-server mac-address add address=00:00:00:00:00:01 comment="My Device"
```

**3. Define Allowed MAC Addresses**

Use the `mac-filter` parameter to restrict access to only the specified MAC addresses.

```
/interface mac-server mac-filter add mac-address=00:00:00:00:00:02,00:00:00:00:00:03
```

**4. Define Blocked MAC Addresses**

Use the `mac-filter` parameter with the `action=deny` option to block specific MAC addresses.

```
/interface mac-server mac-filter add mac-address=00:00:00:00:00:04,00:00:00:00:00:05 action=deny
```

### Complete Configuration Commands

```
/interface mac-server server set enabled=yes
/interface mac-server mac-address add address=00:00:00:00:00:01 comment="My Device"
/interface mac-server mac-filter add mac-address=00:00:00:00:00:02,00:00:00:00:00:03
/interface mac-server mac-filter add mac-address=00:00:00:00:00:04,00:00:00:00:00:05 action=deny
```

### Common Pitfalls and Solutions

- **MAC address conflict:** If two devices have the same MAC address, they may not be able to connect to the network. To resolve this, change the MAC address of one of the devices.
- **Incorrect MAC address filtering:** Make sure the MAC addresses you are allowing or blocking are correct. Incorrect filtering can prevent legitimate devices from accessing the network or allow unauthorized devices to connect.
- **MAC server not enabled:** Ensure that the MAC server is enabled on the router. If it is not, MAC address management will not work.

### Verification and Testing Steps

- **Check MAC server status:** Use the `/interface mac-server server print` command to verify that the MAC server is enabled.
- **Test MAC address filtering:** Connect devices with different MAC addresses to the network. Devices with allowed MAC addresses should be able to connect, while devices with blocked MAC addresses should not.

### Related Features and Considerations

- **MACVLAN:** MACVLAN allows you to create virtual network interfaces that share the same MAC address as the parent interface. This can be useful for creating isolated networks or for connecting multiple devices to a single network interface.
- **L3 Hardware Offloading:** L3 Hardware Offloading can improve the performance of the MAC server by offloading certain tasks to the hardware. This can be enabled using the `/system offload set l3-hw-offload=enable` command.
- **MACsec:** MACsec provides encryption and authentication for MAC addresses. This can be used to secure sensitive communications or to prevent spoofing attacks.
- **Quality of Service:** Quality of Service (QoS) can be used to prioritize traffic based on MAC addresses. This can be useful for ensuring that critical traffic, such as VoIP or video conferencing, has priority over less important traffic.

### MikroTik REST API Examples

**Add MAC Address**

**Endpoint:** `/interface/mac-server/mac-address`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "address": "00:00:00:00:00:01",
  "comment": "My Device"
}
```

**Expected Response:**

```json
{
  "id": "1",
  "address": "00:00:00:00:00:01",
  "comment": "My Device"
}
```

**Block MAC Address**

**Endpoint:** `/interface/mac-server/mac-filter`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "mac-address": "00:00:00:00:00:04",
  "action": "deny"
}
```

**Expected Response:**

```json
{
  "id": "1",
  "mac-address": "00:00:00:00:00:04",
  "action": "deny"
}
```