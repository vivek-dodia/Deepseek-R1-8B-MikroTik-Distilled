## MikroTik RouterOS MAC Server Configuration

**Configuration Level:** Basic

**Network Scale:** ISP

### 1. Configuration Scenario and Requirements

This guide configures a MAC server on a MikroTik RouterOS ISP router. The goal is to restrict access to the network based on the MAC addresses of connected devices.

### 2. Step-by-Step Implementation

**Step 1:** Create a MAC server.

```
/tool mac-server set mode=static
```

**Step 2:** Add MAC address entries.

```
/tool mac-server add mac-address=01:23:45:67:89:AB
```

### 3. Complete Configuration Commands

**Step 1:**
```
/tool mac-server set mode=static
```

| Parameter | Description |
|---|---|
| mode | Sets the MAC server mode. Static mode requires manual entries, while dynamic mode automatically learns MAC addresses. |

**Step 2:**
```
/tool mac-server add mac-address=01:23:45:67:89:AB
```

| Parameter | Description |
|---|---|
| mac-address | MAC address to add to the server. |

**Step 3:** (Optional) Firewall rule to block access for unknown MAC addresses.
```
/ip firewall add chain=input action=drop mac-address-src=unknown
```

### 4. Common Pitfalls and Solutions

- **Incorrect MAC address format:** Ensure the MAC address is in the correct format (XX:XX:XX:XX:XX:XX).
- **Multiple Static MAC Server:** Don't create multiple MAC servers, as this can cause conflicts.
- **Firewall rule:** If access is not blocked for unknown MAC addresses, check the firewall rules and add an appropriate block rule.

### 5. Verification and Testing Steps

**Step 1:** Confirm MAC server is enabled.
```
/tool mac-server get mode
```
Expected output: **static**

**Step 2:** Check MAC address list.
```
/tool mac-server print
```
Expected output: List of MAC addresses added.

**Step 3:** Test access.
Connect a device with a known MAC address and verify successful access. Connect a device with an unknown MAC address and confirm access is blocked.

### 6. Related Features and Considerations

- DHCP leases can be assigned based on MAC addresses using MAC-binding.
- MAC server can be combined with radius authentication for stronger security.
- Wireless access can be controlled by MAC address filtering on the wireless interface.

### 7. MikroTik REST API Examples

**List MAC server entries:**

**API Endpoint:** `/tool/mac-server`
**Request Method:** GET

**Example Response:**

```json
[
  {
    "mac-address": "01:23:45:67:89:AB"
  }
]
```

**Add MAC server entry:**

**API Endpoint:** `/tool/mac-server`
**Request Method:** POST

**Example JSON Payload:**

```json
{
  "mac-address": "01:23:45:67:89:AB"
}
```

**Expected Response:**

```json
{
  "mac-address": "01:23:45:67:89:AB",
  "id": 1
}
```