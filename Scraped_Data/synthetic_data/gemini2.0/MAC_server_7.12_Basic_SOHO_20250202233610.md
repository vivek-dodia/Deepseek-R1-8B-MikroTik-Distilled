## MAC Server in MikroTik RouterOS 7.12

### Configuration Scenario and Requirements

This document guides you through the configuration of a MAC server in MikroTik RouterOS 7.12. A MAC server enables you to manage and control devices connected to your network based on their MAC addresses.

### Step-by-Step Implementation

**1. Create an IP Pool for DHCP**

```text
/ip pool
add name=mac_pool range=10.0.0.0/24
```

**2. Create a DHCP Server**

```text
/ip dhcp-server
add interface=ether1 pool=mac_pool lease-time=1h
```

**3. Create the MAC Server**

```text
/ip mac-server
add name=mac_server lease-time=1h
```

**4. Add MAC Address Entries to the MAC Server**

```text
/ip mac-server settings
set mac-server=mac_server comment="Static MAC mapping" mac-address=00:0C:29:18:00:10 lease-time=1h
```

**5. Bind the MAC Server to the DHCP Server**

```text
/ip dhcp-server
set mac-server=mac_server interface=ether1
```

### Complete Configuration Commands

```text
/ip pool add name=mac_pool range=10.0.0.0/24
/ip dhcp-server add interface=ether1 pool=mac_pool lease-time=1h
/ip mac-server add name=mac_server lease-time=1h
/ip mac-server settings set mac-server=mac_server comment="Static MAC mapping" mac-address=00:0C:29:18:00:10 lease-time=1h
/ip dhcp-server set mac-server=mac_server interface=ether1
```

### Common Pitfalls and Solutions

- **MAC address conflict:** Ensure that the MAC addresses used in the MAC server are unique.
- **DHCP server not assigning IP addresses:** Verify that the DHCP server is enabled and the correct IP pool is assigned.
- **Devices unable to obtain a DHCP lease:** Check if firewall rules are blocking DHCP traffic or if the MAC address is not included in the MAC server.

### Verification and Testing Steps

- Verify that devices with allowed MAC addresses obtain IP addresses from the DHCP server.
- Use the `/ip mac-server print` command to list registered MAC addresses.
- Simulate an unauthorized device by connecting a device with a MAC address not listed in the MAC server. It should not receive an IP address.

### Related Features and Considerations

- **IP Binding:** Consider using IP bindings to further restrict access based on IP addresses.
- **Logging:** Enable logging (/system logging) to track MAC server activities and troubleshoot issues.
- **RADIUS Integration:** Integrate the MAC server with RADIUS for more robust authentication and authorization.

### MikroTik REST API Examples

**Get list of MAC server entries:**

```text
API Endpoint: /api/ip/mac-server/print
Request Method: GET
Example JSON Payload: {}
Expected Response: [{"comment": "Static MAC mapping", "interface": "ether1", "ip_address": "10.0.0.10", "lease_time": "1h", "mac_address": "00:0C:29:18:00:10", "name": "mac_server"}]
```

**Add a new MAC server entry:**

```text
API Endpoint: /api/ip/mac-server/add
Request Method: POST
Example JSON Payload: {"comment": "New MAC mapping", "interface": "ether1", "lease_time": "1h", "mac_address": "00:0C:29:18:00:11"}
Expected Response: {"comment": "New MAC mapping", "interface": "ether1", "ip_address": "10.0.0.11", "lease_time": "1h", "mac_address": "00:0C:29:18:00:11", "name": "mac_server-1"}
```