Okay, let's dive into creating comprehensive documentation for a MAC server on a MikroTik router, targeting RouterOS 7.11, within an enterprise context, focusing on the provided subnet and interface name.

## Scenario Description:

We will configure a MAC server on a MikroTik router, specifically on interface "vlan-75" associated with the subnet `15.43.156.0/24`. This MAC server will be used for IP address assignment via the DHCP protocol, where clients are identified by their MAC addresses. This is useful in environments where specific devices need to always receive the same IP, for logging or administrative purposes. It can also be used to prevent rogue devices from obtaining an IP address on the network. This scenario is typical in small to medium-sized enterprises (SMB) where managed access is required.

## Implementation Steps:

Here's a step-by-step guide to setting up the MAC server.

### Step 1: Verify VLAN Interface (Optional, but recommended)

*   **Description:** Before configuring the MAC server, ensure that the VLAN interface `vlan-75` exists and is correctly configured. We will assume that the VLAN was created elsewhere.
*   **Before:** Let's assume that the VLAN interface `vlan-75` already exists, but has no address configured.
*   **Action:**
    *   **CLI:** We will verify that `vlan-75` is active with the command:
        ```mikrotik
        /interface print where name=vlan-75
        ```
        We will check if an IP address is configured on the interface:
        ```mikrotik
        /ip address print where interface=vlan-75
        ```
    *   **Winbox:** Navigate to `Interface` and confirm the existence of `vlan-75`. Open `IP` -> `Addresses` and verify no IP address is configured on the interface.
*   **After:** The output of the print commands should show the interface exists. We'll be configuring an IP in step 2.
*   **Purpose:** Validate the existence and status of the VLAN interface to prevent issues later.

### Step 2: Configure IP Address on the VLAN Interface

*   **Description:** Assign an IP address to the `vlan-75` interface. This IP will serve as the gateway for the subnet and DHCP server for clients on that network.
*   **Before:** No IP address on `vlan-75`.
*   **Action:**
    *   **CLI:**
        ```mikrotik
        /ip address add address=15.43.156.1/24 interface=vlan-75
        ```
    *   **Winbox:** Navigate to `IP` -> `Addresses` click on the `+` button. Enter `15.43.156.1/24` in the `Address` field and choose `vlan-75` in the `Interface` dropdown menu. Click `Apply` and then `OK`.
*   **After:** Interface `vlan-75` has the IP address `15.43.156.1/24`.
*   **Purpose:** Provide an IP address for the interface that clients can use as gateway to other networks and make the interface ready for acting as a DHCP server.

### Step 3: Create DHCP Server

*   **Description:** Create a DHCP server for the `15.43.156.0/24` subnet that will listen on `vlan-75`.
*   **Before:** No DHCP server configured.
*   **Action:**
    *   **CLI:**
        ```mikrotik
        /ip dhcp-server add name=dhcp-vlan-75 interface=vlan-75 address-pool=default
        ```
    *   **Winbox:** Go to `IP` -> `DHCP Server`, click the `+` button. Choose `vlan-75` under `Interface` and fill in `dhcp-vlan-75` for the `Name`. Leave `Address Pool` on `default` and click `Apply` and then `OK`.
*   **After:** DHCP server `dhcp-vlan-75` has been created on the interface `vlan-75`.
*   **Purpose:** Enables the assignment of IPs using DHCP.

### Step 4: Configure DHCP Network

*   **Description:** Configure the DHCP network settings, defining the network address, gateway, and DNS servers.
*   **Before:** DHCP server created but no network settings.
*   **Action:**
    *   **CLI:**
        ```mikrotik
        /ip dhcp-server network add address=15.43.156.0/24 gateway=15.43.156.1 dns-server=8.8.8.8,8.8.4.4
        ```
    *   **Winbox:** Go to `IP` -> `DHCP Server` and select the `Networks` tab. Click `+`. Fill in the `Address` field with `15.43.156.0/24`. The `Gateway` should be `15.43.156.1`. Set `DNS Server` to `8.8.8.8,8.8.4.4`. Click `Apply` and then `OK`.
*   **After:** DHCP network settings are configured for the server.
*   **Purpose:** Provides clients with necessary information to use the network, including their gateway and DNS servers.

### Step 5: Create MAC Address Bindings

*   **Description:** Configure static DHCP leases, binding MAC addresses to specific IPs. This is the core of the MAC server functionality.
*   **Before:** No static DHCP leases defined.
*   **Action:**
    *   **CLI:** To add a binding:
    ```mikrotik
    /ip dhcp-server lease add address=15.43.156.100 mac-address=00:11:22:33:44:55 server=dhcp-vlan-75
    ```
    Repeat for each device you want to bind. We will add one more.
    ```mikrotik
    /ip dhcp-server lease add address=15.43.156.101 mac-address=AA:BB:CC:DD:EE:FF server=dhcp-vlan-75
    ```
    *   **Winbox:** Go to `IP` -> `DHCP Server` and select the `Leases` tab. Click the `+` button. Under the `Address` field, enter the desired IP address (e.g., `15.43.156.100`), the `MAC Address` (e.g. `00:11:22:33:44:55`), then select the correct server under `Server` (e.g. `dhcp-vlan-75`). Click `Apply` and then `OK`. Add another binding.
*   **After:** DHCP server contains the binding entries.
*   **Purpose:** Clients with specific MAC addresses always receive the same IP address.

## Complete Configuration Commands:

```mikrotik
/interface print where name=vlan-75
/ip address print where interface=vlan-75

/ip address add address=15.43.156.1/24 interface=vlan-75

/ip dhcp-server add name=dhcp-vlan-75 interface=vlan-75 address-pool=default

/ip dhcp-server network add address=15.43.156.0/24 gateway=15.43.156.1 dns-server=8.8.8.8,8.8.4.4

/ip dhcp-server lease add address=15.43.156.100 mac-address=00:11:22:33:44:55 server=dhcp-vlan-75
/ip dhcp-server lease add address=15.43.156.101 mac-address=AA:BB:CC:DD:EE:FF server=dhcp-vlan-75
```

## Common Pitfalls and Solutions:

1.  **DHCP Server Not Enabled:**
    *   **Problem:** The DHCP server is created but not enabled.
    *   **Solution:** Ensure the DHCP server is enabled under `/ip dhcp-server print` and verify that `disabled=no`.
2.  **Incorrect Interface:**
    *   **Problem:** The DHCP server is bound to the wrong interface.
    *   **Solution:** Verify that `interface=vlan-75` is correctly set on the DHCP server.
3.  **No IP Address on Interface:**
    *   **Problem:** The VLAN interface does not have an IP.
    *   **Solution:** Add an IP address to the `vlan-75` interface.
4.  **Subnet Overlap:**
    *   **Problem:** Overlapping DHCP server subnet ranges can cause unexpected behavior.
    *   **Solution:** Ensure each DHCP network range is distinct.
5.  **Incorrect MAC Address:**
    *   **Problem:** The MAC address entered is incorrect.
    *   **Solution:** Double-check the MAC addresses for accuracy, note that MAC addresses are case insensitive.
6.  **Conflict Leases**
    * **Problem:** Manually assigned static leases conflict with existing dynamic leases.
    * **Solution:** Remove the existing dynamic lease to avoid IP conflict.

## Verification and Testing Steps:

1.  **DHCP Lease Acquisition:**
    *   **Action:** Connect a client device to the `vlan-75` network.
    *   **Verification:**
        *   **Client Side:** Verify that the client receives an IP address assigned by the DHCP server.
        *   **MikroTik CLI:** Use `/ip dhcp-server lease print` to check if the client received the correct static IP address and the `status` is `bound`.
2.  **Ping Test:**
    *   **Action:** From the client, ping the gateway (`15.43.156.1`).
    *   **Verification:** Verify successful ping responses.
3.  **Torch Tool:**
    *   **Action:** Use `/tool torch interface=vlan-75` to capture and analyze traffic for DHCP and network activity.
    *   **Verification:** Look for DHCP packets and ensure they are reaching the router.

## Related Features and Considerations:

1.  **DHCP Pool:** While we used the default pool, you could configure a specific IP address range for the DHCP pool if needed `/ip pool`. This is particularly useful if you want to segment DHCP-assigned vs. static IPs.
2.  **Lease Time:** `/ip dhcp-server print` - Change the lease-time setting according to your needs.
3.  **DHCP Options:** You can set other specific DHCP options like NTP server addresses or the default route.
4.  **Hotspot and User Manager:** Combine with the Hotspot feature, allowing a specific client to bypass the hotspot login.
5.  **RADIUS Integration:** Integrate with RADIUS servers for a more secure and scalable user authentication and authorization.
6.  **DHCP Snooping**: While not directly related to a mac server, it is a feature that when enabled will only allow trusted DHCP servers to work on the network.

## MikroTik REST API Examples (if applicable):

```json
// Get all DHCP Servers
// Endpoint: /ip/dhcp-server
// Method: GET
// Response (Example)
[
  {
    ".id": "*2",
    "name": "dhcp-vlan-75",
    "interface": "vlan-75",
    "address-pool": "default",
    "disabled": "no"
  }
]

// Create a DHCP server
// Endpoint: /ip/dhcp-server
// Method: POST
// Request:
{
  "name": "dhcp-vlan-api",
  "interface": "vlan-75",
  "address-pool": "default"
}
// Response (Example)
{
  ".id": "*3"
}
// Handling Errors: Check response code for non-200 and look for error messages in body.

// Get all DHCP leases
// Endpoint: /ip/dhcp-server/lease
// Method: GET
// Response (Example)
[
  {
    ".id": "*1",
    "address": "15.43.156.100",
    "mac-address": "00:11:22:33:44:55",
    "server": "dhcp-vlan-75",
    "active-address": "15.43.156.100",
    "active-mac-address": "00:11:22:33:44:55",
    "host-name": "test-device",
    "status": "bound"
  },
 {
    ".id": "*2",
    "address": "15.43.156.101",
    "mac-address": "AA:BB:CC:DD:EE:FF",
    "server": "dhcp-vlan-75",
    "active-address": "15.43.156.101",
    "active-mac-address": "AA:BB:CC:DD:EE:FF",
    "status": "bound"
  }
]

// Create a DHCP static lease (MAC binding)
// Endpoint: /ip/dhcp-server/lease
// Method: POST
// Request
{
    "address": "15.43.156.102",
    "mac-address": "12:34:56:78:90:AB",
    "server": "dhcp-vlan-75"
}
// Response (Example)
{
  ".id": "*3"
}
// Handling Errors: Check response code for non-200 and look for error messages in body.

// Delete a DHCP Lease
// Endpoint: /ip/dhcp-server/lease/{leaseId}
// Method: DELETE
// Example URL: /ip/dhcp-server/lease/*3
// Response (Example)
{}
// Handling Errors: Check response code for non-200 and look for error messages in body.
```
To handle errors, check the HTTP status codes returned by the API. A successful operation usually returns a `200 OK`, and a `201 Created` for post requests. Any code outside of the 200 range signifies an error, with details often provided in the JSON response body. Use a tool like `curl` or a web client to interact with the API.

## Security Best Practices

1.  **Disable Unnecessary Services:** Only enable necessary services. Avoid enabling `API` if not being used.
2.  **Strong Router Password:** Ensure a very strong password for the router.
3.  **Access Control:** Limit router access to authorized networks.
4.  **Firewall Rules:** Implement strict firewall rules, allowing only necessary ports and services on the router. If the DHCP server needs to provide IP addresses to different interfaces, create firewall rules that ensure each interface can only communicate to their specific DHCP server on the router.
5.  **Monitor Logs:** Regularly monitor router logs for any unusual or suspicious activity.
6.  **RouterOS Updates:** Keep the router operating system and packages up-to-date.
7.  **Secure the Web Interface:** Change the default web interface port to something non-standard.
8.  **Protect API Access**: Enable authentication and authorization for the API. Limit the IP ranges allowed to access the API.
9.  **Secure VLAN Tagging:** Prevent VLAN hopping using VLAN filters.

## Self Critique and Improvements

This configuration provides a basic but functional MAC server, but it could be improved in several ways:

*   **Dynamic Leases:** Implement a dynamic pool with exclusions for static assignments.
*   **More DHCP Options:** Set options for NTP, or custom options that some applications require.
*   **Advanced Logging:** Implement more detailed logs for DHCP activity.
*   **Scripted Management:** Scripted routines for easier binding management.
*   **Integration:** Incorporate with other features, such as RADIUS or Hotspot for advanced authentication or access control.

## Detailed Explanation of Topic

A MAC server, in the context of MikroTik DHCP, uses the MAC address of a device to assign a specific IP address. This provides an effective way to ensure that specific devices always obtain the same IP. It is often used in networks that require persistent addressing for printers, servers, or other network devices. This setup improves traceability and makes network administration easier.

## Detailed Explanation of Trade-offs

*   **Static Leases vs. Dynamic Leases:**
    *   **Static:** Ensures a specific device always gets the same IP. This can lead to IP address waste, if a device is disconnected often.
    *   **Dynamic:** More flexible. IPs are assigned from a pool. Can cause IP address changes in case of a device losing connectivity.
*   **Manual Configuration vs. Scripted:**
    *   **Manual:** Simple for a small number of devices, but not scalable.
    *   **Scripted:** Better for larger networks, but harder to set up initially.
*   **Basic vs. Advanced DHCP Options:**
    *   **Basic:** Requires only basic knowledge. Good for small deployments.
    *   **Advanced:** Allows finer control and more integration. Can be more complex to configure.

## Configuration for Specific RouterOS Versions:

The current setup is compatible with RouterOS 7.11, 7.x, and 6.48. There are no major differences in commands that would require version-specific instructions for this configuration. However, new features are often introduced to newer versions of RouterOS, always refer to the latest version documentation when implementing advanced configurations.

This complete document provides a comprehensive guide for implementing a MAC server on MikroTik, with real-world examples, detailed explanations, and security best practices. This should allow an experienced MikroTik user to implement the presented configuration with confidence.
