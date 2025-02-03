**RouterOS 6.48 MAC Server Guide**

## Configuration Scenario and Requirements

The MAC server in RouterOS allows you to manage and control network access based on MAC addresses. This is useful for implementing MAC-based authentication, whitelisting/blacklisting devices, and tracking client connections.

## Step-by-Step Implementation

**Step 1: Configure IP Pool**

Create an IP pool to assign IP addresses to authenticated MAC addresses:

```
/ip pool add name=my-pool ranges=192.168.1.10-192.168.1.20
```

**Step 2: Create MAC Server**

Create a MAC server instance and bind it to the IP pool:

```
/mac-server add name=my-mac-server ip-pool=my-pool secure-mac=yes
```

- `secure-mac=yes` enables MAC address learning, preventing unauthorized devices from accessing the network.

**Step 3: Set Firewall Rules**

Allow access to the authenticated network segment:

```
/ip firewall layer7-protocol add name=mac-allow protocol=all src-mac-list=my-mac-server action=accept chain=input
```

- `src-mac-list=my-mac-server` only allows traffic from devices authenticated by the MAC server.

## Complete Configuration Commands

```
/ip pool add name=my-pool ranges=192.168.1.10-192.168.1.20
/mac-server add name=my-mac-server ip-pool=my-pool secure-mac=yes
/ip firewall layer7-protocol add name=mac-allow protocol=all src-mac-list=my-mac-server action=accept chain=input
```

## Common Pitfalls and Solutions

- **Unauthorized MAC addresses can access the network:** Ensure `secure-mac=yes` is enabled in the MAC server configuration.
- **IP pool is full:** Increase the range of IP addresses in the IP pool to accommodate more devices.
- **Firewall rules are not configured:** Create firewall rules to allow traffic from authenticated MAC addresses.

## Verification and Testing Steps

1. Connect a device with a known MAC address to the network.
2. Check if the device receives an IP address from the specified IP pool.
3. Disconnect the device and verify that an IP address is no longer assigned to it.

## Related Features and Considerations

- **MAC address learning:** The MAC server can dynamically learn MAC addresses for authorized devices.
- **MAC filtering:** You can manually add or remove specific MAC addresses from the MAC server.
- **Authentication bypass:** Allow certain MAC addresses to bypass MAC authentication for troubleshooting or trusted devices.

## MikroTik REST API Examples

**Endpoint:** `/api/v6/ip/mac-server`

**Method:** GET

**Request:**

```json
{
  "id": 1
}
```

**Response:**

```json
{
  "id": 1,
  "name": "my-mac-server",
  "ip-pool": "my-pool",
  "secure-mac": true
}
```