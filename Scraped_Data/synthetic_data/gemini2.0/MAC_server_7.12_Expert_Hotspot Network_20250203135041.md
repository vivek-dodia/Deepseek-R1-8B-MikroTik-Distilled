Okay, let's craft some expert-level documentation for a MikroTik MAC server implementation within the context of a hotspot network. We'll aim for RouterOS 7.12 (and 6.48/7.x compatible) while using the specified parameters, and keep it practical and thorough.

## Scenario Description:

This document describes how to configure a MikroTik router to act as a MAC server within a Hotspot network. This allows clients on the network to obtain IP addresses via DHCP by authenticating their MAC addresses. We will be utilizing a bridge interface (`bridge-85`) on the router with the subnet `119.105.140.0/24`. MAC-based authentication adds a layer of control by requiring clients to be present in the allowed address list.

## Implementation Steps:

1. **Step 1: Create the Bridge Interface**
   - **Purpose:**  A bridge interface groups multiple network interfaces (Ethernet ports, wireless interfaces, VLANs) into a single logical interface. This allows us to treat multiple physical or logical interfaces as a single network segment.
   - **CLI Command:**
     ```mikrotik
     /interface bridge
     add name=bridge-85
     ```
   - **Winbox GUI:**
     - Go to "Bridge" in the left-hand menu.
     - Click the "+" button.
     - Enter `bridge-85` in the "Name" field.
     - Click "Apply" and then "OK."
   - **Before:** No bridge interface named `bridge-85` exists.
   - **After:** The bridge interface `bridge-85` is created but not yet operational.
   - **Effect:**  A logical bridge interface is created, which will act as a single network interface for DHCP server purposes.

2. **Step 2: Add Interfaces to the Bridge**
   - **Purpose:**  Include specific Ethernet or wireless interfaces in the bridge so that the MAC server will apply to clients connected to these interfaces. We'll assume for this example that `ether1` will be part of the bridge. You might need to add other physical interfaces or VLANS to the bridge in a real-world scenario.
   - **CLI Command:**
      ```mikrotik
      /interface bridge port
      add bridge=bridge-85 interface=ether1
      ```
  - **Winbox GUI:**
      - Go to "Bridge" in the left-hand menu.
      - Click the "Ports" tab.
      - Click the "+" button.
      - Select `ether1` from the "Interface" dropdown.
      - Select `bridge-85` from the "Bridge" dropdown.
      - Click "Apply" and then "OK."
    - **Before:** `ether1` is not part of the bridge interface.
    - **After:** `ether1` becomes a member of the bridge interface `bridge-85`.
    - **Effect:** Devices connected to the `ether1` port will now be part of the bridge `bridge-85`. Traffic will now flow through the bridge.

3. **Step 3: Configure the IP Address on the Bridge Interface**
   - **Purpose:**  Assign an IP address to the bridge interface, allowing the router to communicate on the 119.105.140.0/24 network. This IP address will be used as the default gateway for the clients who get their IP addresses from DHCP.
   - **CLI Command:**
     ```mikrotik
     /ip address
     add address=119.105.140.1/24 interface=bridge-85
     ```
   - **Winbox GUI:**
      - Go to "IP" -> "Addresses" in the left-hand menu.
      - Click the "+" button.
      - Enter `119.105.140.1/24` in the "Address" field.
      - Select `bridge-85` from the "Interface" dropdown.
      - Click "Apply" and then "OK."
   - **Before:** The bridge interface `bridge-85` has no IP address.
   - **After:** The bridge interface `bridge-85` has the IP address 119.105.140.1/24.
   - **Effect:** The router now has a way to communicate on the 119.105.140.0/24 network. This will be the gateway address of clients connecting to this network.

4. **Step 4: Configure the DHCP Server**
    - **Purpose:** Enable a DHCP server to automatically assign IP addresses to client devices. Configure the server to lease addresses from within the configured subnet range, specify the lease time and the gateway.
    - **CLI Command:**
      ```mikrotik
      /ip dhcp-server
      add address-pool=dhcp_pool disabled=no interface=bridge-85 name=dhcp-server-85
      /ip dhcp-server network
      add address=119.105.140.0/24 dns-server=8.8.8.8 gateway=119.105.140.1 netmask=24
      ```
     - **Winbox GUI:**
       - Go to "IP" -> "DHCP Server" in the left-hand menu.
       - Click the "+" button on the "DHCP Server" tab.
       - Set "Name" to `dhcp-server-85` and select `bridge-85` as the "Interface". Click "Apply"
       - Go to the "Networks" tab and click the "+" button.
       - Set the "Address" to `119.105.140.0/24` and set "Gateway" to `119.105.140.1`, click "Apply" then "OK".
       - Click the "DNS Servers" button and enter the DNS server, `8.8.8.8`, then click "OK".
    - **Before:** There is no DHCP server configured for bridge-85.
    - **After:** The DHCP server is now enabled on `bridge-85`. Clients can now request and be assigned IP addresses.
    - **Effect:** Clients connecting through the bridged interface `bridge-85` will now receive an IP address from the range 119.105.140.0/24.

5. **Step 5: Enable the MAC Server**
   - **Purpose:**  Enable the MAC server functionality which authenticates clients based on their MAC addresses. Without this step the router will allow all requests and ignore the MAC addresses.
   - **CLI Command:**
     ```mikrotik
     /ip dhcp-server lease
     set use-mac-address=yes
     ```
   - **Winbox GUI:**
     - Go to "IP" -> "DHCP Server" in the left-hand menu.
     - Go to the "Leases" tab.
     - Click the "Settings" button.
     - Check the box marked "Use MAC Address".
     - Click "Apply" and then "OK."
   - **Before:** The MAC server functionality is disabled. The DHCP server does not check for MAC addresses.
   - **After:** The MAC server is enabled. DHCP server will now only assign IPs based on registered MAC addresses.
   - **Effect:** DHCP server now relies on valid MAC addresses to assign IP addresses from the DHCP pool.

6. **Step 6: Add Allowed MAC Addresses**
   - **Purpose:** Manually add MAC addresses that should be allowed to receive IP addresses. This is needed in conjunction with the MAC server being enabled. You can populate the lease table with valid mac addresses with specific IP addresses.
   - **CLI Command:**
      ```mikrotik
      /ip dhcp-server lease
      add address=119.105.140.10 mac-address=00:11:22:33:44:55 server=dhcp-server-85
      add address=119.105.140.20 mac-address=AA:BB:CC:DD:EE:FF server=dhcp-server-85
      ```
   - **Winbox GUI:**
      - Go to "IP" -> "DHCP Server" in the left-hand menu.
      - Go to the "Leases" tab.
      - Click the "+" button.
      - Set "MAC Address" to `00:11:22:33:44:55`.
      - Set "Address" to `119.105.140.10`.
      - Set "Server" to `dhcp-server-85`.
      - Click "Apply" and then "OK".
      - Repeat for each additional MAC address and desired IP.
   - **Before:** No MAC addresses are in the DHCP server lease table.
   - **After:** The specified MAC addresses have been added and will be allowed to receive IP addresses, and be assigned the specific IP.
   - **Effect:** Clients with the MAC addresses `00:11:22:33:44:55` and `AA:BB:CC:DD:EE:FF` will be assigned the IPs `119.105.140.10` and `119.105.140.20` respectively. All other MACs will be ignored.

## Complete Configuration Commands:

```mikrotik
/interface bridge
add name=bridge-85

/interface bridge port
add bridge=bridge-85 interface=ether1

/ip address
add address=119.105.140.1/24 interface=bridge-85

/ip dhcp-server
add address-pool=dhcp_pool disabled=no interface=bridge-85 name=dhcp-server-85
/ip dhcp-server network
add address=119.105.140.0/24 dns-server=8.8.8.8 gateway=119.105.140.1 netmask=24

/ip dhcp-server lease
set use-mac-address=yes
add address=119.105.140.10 mac-address=00:11:22:33:44:55 server=dhcp-server-85
add address=119.105.140.20 mac-address=AA:BB:CC:DD:EE:FF server=dhcp-server-85
```

**Parameter Explanations:**

| Command | Parameter | Description |
|---|---|---|
| `/interface bridge add` | `name` | Name of the new bridge interface. |
| `/interface bridge port add` | `bridge` | Name of the bridge interface to which the port will be added. |
| `/interface bridge port add` | `interface` | Name of the interface (physical or logical) to add to the bridge. |
| `/ip address add` | `address` | IP address and subnet mask of the bridge interface. |
| `/ip address add` | `interface` | Name of the interface to which the IP address will be assigned. |
| `/ip dhcp-server add`| `address-pool`| Name of DHCP IP pool being assigned |
| `/ip dhcp-server add` | `disabled` | Enables/disables the DHCP server. |
| `/ip dhcp-server add` | `interface` | The interface on which the DHCP server is enabled. |
| `/ip dhcp-server add` | `name` | The name of the DHCP server. |
| `/ip dhcp-server network add` | `address` | The network address and subnet mask to use for the DHCP server. |
| `/ip dhcp-server network add`| `dns-server`| DNS server to provide to clients. |
| `/ip dhcp-server network add` | `gateway` | The default gateway for the clients. |
| `/ip dhcp-server network add` | `netmask` | Subnet mask for the network. |
| `/ip dhcp-server lease set` | `use-mac-address` | Enables or disables MAC address authentication of DHCP leases. |
| `/ip dhcp-server lease add` | `address`| The IP address being assigned. |
| `/ip dhcp-server lease add` | `mac-address` | The MAC address that should receive the associated IP. |
| `/ip dhcp-server lease add` | `server` | The name of the DHCP server. |

## Common Pitfalls and Solutions:

*   **Issue:** Clients are not getting IP addresses.
    *   **Solution:**
        *   Verify the bridge interface (`bridge-85`) is correctly configured and has the correct IP address assigned.
        *   Ensure the DHCP server (`dhcp-server-85`) is enabled and has the correct interface (`bridge-85`) selected.
        *   Double-check that the `use-mac-address` is enabled, if this is desired.
        *   Check the DHCP lease table for the correct MAC addresses.
        *   Examine the system logs (`/system logging`) for any error messages related to DHCP or interfaces.

*   **Issue:** Clients get IP addresses, but not the ones assigned in the DHCP table.
    *   **Solution:**
        *   Verify the mac address on the host is correct.
        *   Ensure `use-mac-address=yes` is enabled.
        *   Verify that a static lease is assigned to the specific host's MAC address in the lease table.
        *   Make sure the DHCP server assigned is correct for the given lease.

*   **Issue:** High CPU usage.
    *   **Solution:**
        *   If there are a large number of MAC address leases configured, the router might experience some performance overhead. If this becomes a problem consider a different method of authentication.
        *   Use the `/tool profile` command to identify resource-intensive processes.
        *   Make sure you are using the correct router for the network size.

*   **Issue:** Security Concerns
    *   **Solution:**
        *   MAC address spoofing is a potential risk. Ensure physical security to prevent devices being connected to unauthorized access points.
        *   Consider using additional authentication mechanisms such as a hotspot portal for added security.
        *   Enable firewall rules to filter traffic as needed.

## Verification and Testing Steps:

1.  **Connect a Test Device:** Connect a device (laptop, smartphone) to the `ether1` port.

2.  **IP Address Check:**
    *   Verify that the device receives an IP address within the 119.105.140.0/24 subnet (`119.105.140.10` or `119.105.140.20` if using those specific MAC addresses).
    *   Use `ipconfig` (Windows), `ifconfig` (Linux/macOS) or equivalent on the connected device.
3. **Ping the Gateway**: Ping the gateway address (`119.105.140.1`) from the connected device.

4.  **DHCP Lease Check:** Use the MikroTik CLI or Winbox to check the DHCP leases:
    ```mikrotik
    /ip dhcp-server lease print
    ```
    *   Verify if the device's MAC address is present and if an IP is assigned to it.
5. **Torch Tool:** Use the Torch tool to see the DHCP traffic on the specified interfaces:
    ```mikrotik
    /tool torch interface=bridge-85 protocol=udp port=67,68
    ```
    *   Verify DHCP requests and responses are present in the output, and that they are valid.

6. **System Log check:** View the system logs to ensure no errors are being produced:
    ```mikrotik
    /log print
    ```
    *   Check for errors related to the dhcp server, the bridge, and the interfaces.

## Related Features and Considerations:

*   **Hotspot:** Integrate with MikroTik's Hotspot feature for a more advanced captive portal, user management, and billing (not shown in the example).
*   **User Manager:** Use User Manager for more complex user management and authentication with a AAA server.
*   **VLANs:** You can combine MAC server with VLANs on the bridge for more logical network segmentation and security.
*   **DHCP Options:** Add custom DHCP options like DNS servers, NTP servers, etc to the DHCP server.
*   **Static Leases:** Create static leases in the DHCP server for specific hosts.

## MikroTik REST API Examples (if applicable):

**Note:** RouterOS REST API functionality is available in RouterOS 7.13 and newer and depends on the system being configured to allow API requests.

The API equivalent of what we have done above is much more complex. The following is an example to *create* a bridge interface.

```
API Endpoint: /interface/bridge
Method: POST
JSON Payload:
{
    "name": "bridge-85",
}

Expected Response (Success 200 OK):
{
   "id": "*12"
}

Example error handling:
{
 "error": "already exists",
 "code": 5
}
```

**Parameter Explanations:**

*   `name`: Name of the bridge interface.

A REST API call to enable MAC Address usage is complicated. The following code retrieves the relevant dhcp server configuration, modifies it, and then writes it back to the device.

```
API Endpoint: /ip/dhcp-server
Method: GET

Expected Response (Success 200 OK):
[
 {
  "id": "*1",
  "address-pool": "dhcp_pool",
  "disabled": "false",
  "interface": "bridge-85",
  "name": "dhcp-server-85",
 }
]
// We then modify the object received from the get call, by adding "use-mac-address": "yes".
// and then call the PUT method

API Endpoint: /ip/dhcp-server
Method: PUT
JSON Payload:
[
 {
  "id": "*1",
  "address-pool": "dhcp_pool",
  "disabled": "false",
  "interface": "bridge-85",
  "name": "dhcp-server-85",
  "use-mac-address": "yes",
 }
]
Expected Response (Success 200 OK):
[
 {
  "id": "*1",
  "address-pool": "dhcp_pool",
  "disabled": "false",
  "interface": "bridge-85",
  "name": "dhcp-server-85",
  "use-mac-address": "yes",
 }
]
```

**Parameter Explanations:**
*   `id`: The internal ID of the DHCP server configuration to modify
*   `address-pool`: The dhcp pool being used by this server.
*   `disabled`: Boolean for enabled or disabled.
*   `interface`: The interface the DHCP server is configured for.
*   `name`: The name of the DHCP server.
*   `use-mac-address`: Enables or disables MAC address authentication of DHCP leases.

## Security Best Practices

*   **MAC Address Spoofing:** Be aware that MAC addresses can be spoofed. MAC filtering is not a robust security mechanism on its own.
*   **Physical Security:** Ensure the physical security of your network hardware and cabling. Unauthorized physical access can easily bypass MAC filtering.
*   **Keep RouterOS Updated:** Always keep your RouterOS version up to date to patch security vulnerabilities.
*   **Firewall Rules:** Implement firewall rules to restrict access to resources and services, as needed.
*   **Regular Audits:** Perform regular security audits of your MikroTik configurations.

## Self Critique and Improvements

This configuration provides a functional MAC server implementation but has several areas for improvement:

*   **Scalability:** Managing a large number of static leases through the CLI is cumbersome. Consider using the User Manager and RADIUS for a more scalable solution with larger networks.
*   **Dynamic Updates:** The current setup requires manual updates to the lease table. This approach is not ideal for dynamically changing device lists.
*   **Redundancy:**  The current setup is a single point of failure. Consider VRRP or other redundancy mechanisms for more mission critical deployments.
*   **Granular Control:**  This configuration does not provide granular control or rate limiting of traffic per mac address. More complex methods can be used.
*   **More advanced APIs** The example API calls have been added for reference, but can be further extended to provide complete access to the router's configuration.

## Detailed Explanations of Topic

The MikroTik MAC server leverages the MAC address of network devices for authentication with a DHCP server. This works by matching the MAC address of a requesting device to a list of approved MAC addresses that are assigned specific IP addresses. If a requesting device's MAC address matches one of the approved addresses, the DHCP server responds with the specific IP and the network configuration. If not, then no IP address is returned, and no network communication can occur. This can provide a basic layer of network access control by only assigning IP addresses to known devices, but can be bypassed by cloning the mac address. This feature is used within the DHCP server, when `use-mac-address` is enabled.

## Detailed Explanation of Trade-offs

When choosing to use a MAC server, there are trade-offs to consider:

*   **Complexity vs. Security:**  MAC filtering provides a layer of access control but is not a replacement for robust authentication mechanisms. MAC addresses can be spoofed, and should be used as an additional layer, not as the only method.
*   **Management Overhead:** Manually managing a list of approved MAC addresses can be difficult in larger networks, and is more complex that allowing any address to access the DHCP server. Consider using more scalable methods, such as user-manager, radius or other advanced authentication methods.
*   **Scalability vs. Granular Control:** This system provides control per mac address, but does not provide granular access control or rate limiting options.
*   **Ease of use vs. Security** MAC filtering can cause issues if you need to bring new devices online frequently and quickly. Each new device must have it's mac address manually added to the configuration.

## Configuration for Specific RouterOS Versions:

The configurations provided in this document are compatible with RouterOS 6.48 and 7.x, including the targeted version 7.12. However, there are some minor differences:

*   **API Functionality:** REST API functionality is primarily available on version 7.13 and up.
*   **Command Syntax:** The commands provided are the same for both 6.48 and 7.x for the features we are using.

This documentation provides a very comprehensive guide to configuring a MAC server on a MikroTik RouterOS device. It includes detailed instructions, explanations, examples, and troubleshooting tips, keeping the needs of an expert in mind. Remember to test this configuration thoroughly in a staging environment before implementing it in a production network.
